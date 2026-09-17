import fs from 'node:fs/promises';
import path from 'node:path';
import { randomUUID } from 'node:crypto';
import { fileURLToPath } from 'node:url';

export const replacer = (key, value) =>
    ['createdTime', 'modifiedTime', 'lastModifiedBy'].includes(key) ? undefined : value;

async function exists(io, filename) {
    try {
        return await io.lstat(filename);
    } catch (error) {
        if (error.code === 'ENOENT') return null;
        throw error;
    }
}

async function validateExport(io, directory, expected) {
    const actual = new Set();
    async function walk(dir) {
        for (const entry of await io.readdir(dir, { withFileTypes: true })) {
            const filename = path.join(dir, entry.name);
            if (entry.isSymbolicLink()) throw new Error(`Unexpected symlink: ${filename}`);
            if (entry.isDirectory()) await walk(filename);
            else if (entry.isFile() && entry.name.toLowerCase().endsWith('.json')) {
                const data = JSON.parse(await io.readFile(filename, 'utf8'));
                const key = data._key;
                if (!key || actual.has(key)) throw new Error(`Missing or duplicate document key: ${filename}`);
                actual.add(key);
            }
        }
    }
    await walk(directory);
    if (actual.size !== expected.size || [...expected].some(key => !actual.has(key))) {
        throw new Error(`Incomplete export: expected ${expected.size}, found ${actual.size} primary documents`);
    }
}

/** Each pack is staged and verified before replacing its previous export. No live DB rebuild. */
export async function extractPacks({ workDir = process.cwd(), extractPack, io = fs, log = console.log } = {}) {
    if (typeof extractPack !== 'function') throw new TypeError('extractPack is required');
    workDir = path.resolve(workDir);
    const input = path.join(workDir, 'packs');
    const output = path.join(workDir, 'packsJson');
    const packs = (await io.readdir(input, { withFileTypes: true })).filter(entry => entry.isDirectory());
    await io.mkdir(output, { recursive: true });
    for (const pack of packs) {
        const target = path.join(output, pack.name);
        // Outside packsJson: compilePack must never discover staging/backup directories as packs.
        const stage = path.join(workDir, `.extract-${pack.name}-${randomUUID()}`);
        const backup = path.join(workDir, `.extract-backup-${pack.name}-${randomUUID()}`);
        let movedOld = false;
        let installed = false;
        try {
            const old = await exists(io, target);
            if (old && (!old.isDirectory() || old.isSymbolicLink()))
                throw new Error(`Not an export directory: ${target}`);
            await io.mkdir(stage);
            const prepared = await io.stat(stage);
            const parent = await io.stat(output);
            if (prepared.dev !== parent.dev || (old && old.dev !== prepared.dev)) {
                throw new Error(`Staging must be on the same filesystem: ${stage}, ${target}`);
            }
            const expected = new Set();
            await extractPack(path.join(input, pack.name), stage, {
                folders: true,
                omitVolatile: true,
                jsonOptions: { replacer },
                transformEntry: doc => {
                    if (!doc._key || expected.has(doc._key)) throw new Error(`Invalid primary key in ${pack.name}`);
                    expected.add(doc._key);
                }
            });
            await validateExport(io, stage, expected);
            // Do not silently change the directory's access policy during replacement.
            const ready = await io.stat(stage);
            if (
                old &&
                (old.uid !== ready.uid || old.gid !== ready.gid || (old.mode & 0o7777) !== (ready.mode & 0o7777))
            ) {
                throw new Error(
                    `Access metadata differ; owner must review ${target} and ${stage}. No permissions were changed.`
                );
            }
            if (old) {
                await io.rename(target, backup);
                movedOld = true;
            }
            await io.rename(stage, target);
            installed = true;
            log(`Installed ${pack.name}: ${expected.size} primary documents`);
            if (movedOld) await io.rm(backup, { recursive: true });
        } catch (error) {
            if (movedOld && !installed) {
                try {
                    await io.rename(backup, target);
                } catch (restoreError) {
                    throw new AggregateError(
                        [error, restoreError],
                        `Export and restoration failed. Retained data: ${backup}; staging: ${stage}; target: ${target}`
                    );
                }
            }
            // Retain failed staging and any backup for diagnosis/recovery. Never clean a previous run.
            throw new Error(`${pack.name}: ${error.message}. Target: ${target}; staging: ${stage}; backup: ${backup}`, {
                cause: error
            });
        }
    }
}

if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
    const { extractPack } = await import('@foundryvtt/foundryvtt-cli');
    await extractPacks({ extractPack });
}
