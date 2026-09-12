# package.json

| Поле | Значение |
| --- | --- |
| Исходный файл | [package.json](../../../../package.json) |
| Тип файла | JSON |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-12 |
| Ветка и коммит | rusbar-main, 3f78cbf0372e1da3d5a840e41b456d954c64e403 |
| Изменения относительно коммита | Нет; совпадает со срезом TASK-0001 15da5b225535e34af4e132c701b5353ef4eb667f |
| Задача и порция | [TASK-0003.050](../../../tasks/task-0003.050.md), 7 файлов / 582 логических строк; данный файл — 10 |
| Запись перекрёстной сверки | [TASK-0003.050](../review-log.md#task-0003050) |

## Назначение файла

Объявляет две зависимости разработки и две npm-команды для сборки и извлечения компедиумов.

## Условия использования

npm читает файл как конфигурацию локального проекта. npm run build:db запускает Node с utils/packs.mjs; npm run extract — utils/extract.mjs. Скрипты рассчитаны на cwd корня checkout. Foundry не подключает package.json как клиентский модуль; JS/CSS для клиента объявлены в system.json.

## Введённые сущности и действия с ними

| Ключ | Строки | Значение и действие |
| --- | --- | --- |
| devDependencies | 2–5 | @foundryvtt/foundryvtt-cli:^3.0.3; prettier:^3.3.3 |
| scripts.build:db | 7 | node ./utils/packs.mjs package pack |
| scripts.extract | 8 | node ./utils/extract.mjs с конечным пробелом |

name, version, type, engines, dependencies, scripts.test, scripts.build и scripts.release отсутствуют. Разрешение локального .js при изолированных Node-проверках выдаёт предупреждение MODULE_TYPELESS_PACKAGE_JSON; это не доказательство сбоя Foundry, который загружает свой ES-модуль через манифест.

## Основные функции и методы

Функций нет. Команды передают управление Node. Аргументы package pack сохраняются в process.argv, но utils/packs.mjs не читает argv: фактический режим всегда задаётся его телом. Конечный пробел extract не добавляет самостоятельный аргумент. Задачи форматирования через npm здесь нет, хотя prettier объявлен.

## Используемые сущности и зависимости

| Сущность | Источник | Вид связи, место и назначение | Основание |
| --- | --- | --- | --- |
| compilePack | [utils/packs.mjs](../../../../utils/packs.mjs); внешняя CLI | npm build:db → импорт CLI | Команда и весь скрипт сверены |
| extractPack | [utils/extract.mjs](../../../../utils/extract.mjs); внешняя CLI | npm extract → импорт CLI | Команда и весь скрипт сверены |
| @foundryvtt/foundryvtt-cli | Внешний npm-пакет | devDependencies ^3.0.3 означает разрешённую совместимую ветвь 3.x начиная с 3.0.3 | Объявление не равно фактической установке |
| prettier | Внешний npm-пакет | devDependencies ^3.3.3, без команды вызова | Использование форматтера не проверялось |
| node/npm, process.cwd/argv | Среда Node | Запускают .mjs; рабочий каталог определяет пути | Проверен Node 24.16.0 |
| package-lock.json | [Lock-файл, вне границ аудита](../../../../package-lock.json) | npm ci получает точные версии | lockfileVersion 3; CLI 3.0.3, prettier 3.3.3 |
| Release Creation | [Внешний для границ аудита workflow](../../../../.github/workflows/release.yml) | Читает package через npm ci/npm run build:db | Прочитан только как потребитель; не запускался |

Внешний источник API — [опубликованный пакет CLI 3.0.3](https://registry.npmjs.org/@foundryvtt/foundryvtt-cli/3.0.3), index.mjs и lib/package.mjs из tarball. Архив прочитан через HTTPS в память, SHA-512 совпал с integrity в package-lock.json; установка не выполнялась. Это проверенная версия внешнего источника, не установленная в checkout зависимость.

## Известные потребители

| Потребитель | Действия и условия |
| --- | --- |
| npm | Читает scripts и devDependencies по команде разработчика |
| [.github/workflows/release.yml](../../../../.github/workflows/release.yml) | При published release вызывает npm ci, затем npm run build:db |
| [utils/packs.mjs](../../../../utils/packs.mjs), [utils/extract.mjs](../../../../utils/extract.mjs) | При запуске требуют разрешимого импорта CLI; не разбирают package.json самостоятельно |

build.json не читается npm-командами напрямую: его отдельный потребитель — get-includes.js в release workflow.

## Данные и изменения состояния

Сам JSON декларативен. npm ci меняет установленные зависимости; обе npm-команды работают с компедиумами, а не являются проверкой без записи. build:db обновляет LevelDB через CLI, extract удаляет/записывает JSON. Здесь эти команды не запускались.

## Проверки и доказательства

Разобраны все 10 строк JSON. createRequire от package.json checkout не смог разрешить ни CLI, ни prettier: MODULE_NOT_FOUND; соответствующих установленных каталогов нет. В lock-файле стоят CLI 3.0.3 и prettier 3.3.3. У CLI engines node>17.0.0, у prettier >=14; у самой системы engines не задан. Вывод о пригодности конкретного npm окружения CI не делался.

C06 проверил точные строки команд; P01–P14 исполнили исходные тела utils с подменёнными FS/DB. Библиотека из опубликованного архива использовалась отдельно в памяти, без npm install и без реальных баз. [Протокол](../review-log.md#task-0003050).

## Непроверенные участки и открытые вопросы

Непрочитанных частей нет. npm ci, разрешение будущей версии по диапазону, реальная сборка, работа native classic-level, выпуск архива и CI не проверялись. Для воспроизводимости различать declared range, lock и installed version.

## Связанные проблемы

Проблемы скрипта извлечения описаны в [00313](../../../issues/potential/issue-00313.md), [00314](../../../issues/potential/issue-00314.md), [00315](../../../issues/potential/issue-00315.md). Для самого package.json новая issue не зарегистрирована.

## История актуализации

| Дата | Версия и область | Результат |
| --- | --- | --- |
| 2026-09-12 | 3f78cbf0372e1da3d5a840e41b456d954c64e403; полный файл | Первичная карточка; [перекрёстная сверка](../review-log.md#task-0003050) |
