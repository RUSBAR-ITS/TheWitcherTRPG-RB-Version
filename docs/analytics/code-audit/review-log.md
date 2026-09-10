# Журнал перекрёстных сверок

## TASK-0003.004

Дата: 2026-09-10. Ветка rusbar-main, HEAD `17eeb6ae9efccf7474b9ca1845b9ab6370671a26`. На старте рабочее дерево чистое, отслеживались 776 файлов. Все 621 исходник совпали со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. Foundry 14.367.0 по /opt/foundryvtt/package.json, Node 24.16.0.

Полностью прочитаны восемь файлов [TASK-0003.004](../../tasks/task-0003.004.md), всего 116 строк: backgroundData.js (7), detailsData.js (16), homelandData.js (9), lifeEventData.js (10), lifeEventsData.js (29), generalData.js (21), damageModificationData.js (9), damageTypeModificationData.js (15). Соседние модели, обработчики и шаблоны проверены до определений используемых сущностей; отдельными завершёнными карточками они не считаются.

### Содержательная и перекрёстная сверка

| Направление | Источники и фактический результат |
| --- | --- |
| Схемы ↔ включение | background/details/homeland/lifeEvents → general → CharacterData; damageModification → damageTypeModification → CommonActorData → CharacterData/MonsterData. Восьми карточкам соответствуют восемь строк реестра. |
| Биография ↔ enrichedText ↔ форма | CharacterData:34–40 и createEnrichedText передают исходную строку, отдельный enriched и HTMLField в formGroup tab-background:52. TextEditor подменён сборщиком аргументов; редактор не запускался. |
| Подробности ↔ valueLabel | Семь пар value/label, динамические inputs tab-background:27–33; текстовая general.reputation отличается от числовой system.reputation. Карточка valueLabel дополнена. |
| Родина ↔ Item ↔ шаблоны | В отсутствие Item.homeland используются general.homeland.value/otherValue; при наличии Item оба шаблона выбирают его данные. WITCHER.homelands содержит 26 вариантов, schema choices не ограничены. |
| Социальное положение ↔ формула | Шесть вариантов CONFIG, строковый socialStanding. Исходный addSocialStanding: tolerated/emp/charisma → -1, hatedFeared → -2-1, feared/will/intimidation → +1, equal → пусто. Это код, не проверка рулбука. |
| События ↔ контекст ↔ схема | Двадцать ключей 10–200 и decade=1–20. Подготовка контекста заменяет объект живой модели массивом; toObject(false) читает ключ 10 как исходную запись 110, ключ 20=undefined. _source/toObject() сохранены; toggle формирует update для ключа 10. |
| Счётчик ↔ eachLimit | Реальная модель принимает 21; HTML-ввод ограничен 1–20. Исходный helper при 2 выдаёт записи key10/20, при 21 — один undefined. Достижимость обхода ограничений обычной формы не установлена. |
| Типы урона ↔ мастер эффектов | Семь типов × три поля =21 путь; исходный getDamageModifcators выдаёт их для Actor и принадлежащего ему Item, 0 для самостоятельного Item. Все 21 пути найдены в схеме. В CONFIG есть дополнительный silver; отсутствие его в схеме оставлено вопросом. |
| Параметры ↔ обработчики | applyAP=true без AP вызывает TypeError из-за damageProperties вместо properties; AP даёт ранний выход. multiplication=0.5 для damage10 даёт 10/2/2/0 без брони/с надетой/с естественной/с обеими. flat=-3/0/+3 даёт [10]/[10]/[10,3]. |
| Переводы ↔ реальные правила чтения | 51 ключ en/ru найден после foundry.utils.expandObject; составной background.other также найден. Источник нормализации: /opt/foundryvtt/client/helpers/localization.mjs:365–368. |
| JSON-компедиумы ↔ пути | Рекурсивно просмотрены строковые значения 226 packsJson/*.json: путей с префиксами system.general или system.damageTypeModification нет. Бинарные packs/БД не исследовались. |
| Уже описанные зависимости ↔ новые карточки | Дополнены valueLabelData, dataUtils, config, handlebars, registerDataModels; сохранены версии и предыдущие записи. Issue-00021 дополнена связью потерянного damage.type с fallback getters. |
| Наблюдения ↔ issues | Зарегистрированы issue-00024–issue-00027; 27 карточек остаются potential. Отдельные issues для серебра, произвольных строк, счётчика вне HTML-диапазона и отсутствия прямых потребителей name/race/reputation не создавались без достаточного основания. |

### Фактически выполненные проверки

Чтение: git status --short; git rev-parse HEAD; git branch --show-current; полный вывод восьми исходников с номерами строк. Поиск rg по именам фабрик, general.*, lifeEvents, lifeEventCounter, getDamageModifcators, getFlatDamageMod/getMultiDamageMod, calculateArmorResistances, applyAP и consumers в module/, templates/, packsJson/. Первичный поиск включал несуществующий корневой scripts/ и вернул exit 2; далее использовался реальный каталог module/, включающий module/scripts/. Вывод с обрезанными соседними фрагментами дополнен точечными чтениями нужных определений.

Изолированный запуск выполнен из корня репозитория, без создания стенда и файлов скрипта:

```sh
node --input-type=module - <<'JS'
import fs from 'node:fs';
import vm from 'node:vm';
import assert from 'node:assert/strict';
await import('/opt/foundryvtt/common/primitives/_module.mjs');
const fields=await import('/opt/foundryvtt/common/data/fields.mjs');
const {default:DataModel}=await import('/opt/foundryvtt/common/abstract/data.mjs');
const {default:TypeDataModel}=await import('/opt/foundryvtt/common/abstract/type-data.mjs');
const utils=await import('/opt/foundryvtt/common/utils/helpers.mjs');
globalThis.foundry={data:{fields},abstract:{DataModel,TypeDataModel},utils,applications:{api:{DialogV2:{}}}};
const {default:Character}=await import('./module/data/actor/characterData.js');
const {default:Monster}=await import('./module/data/actor/monsterData.js');
const {default:Common}=await import('./module/data/actor/commonActorData.js');
const {default:Loot}=await import('./module/data/actor/lootData.js');
const {WITCHER}=await import('./module/setup/config.js');
const {DamageInstance}=await import('./module/scripts/damageInstance.js');
const game={settings:{get:()=>false},i18n:{localize:k=>k}};
const baseGlobals={foundry,game,CONFIG:{WITCHER},DamageInstance};
function source(file,names,extra={}){
 const code=fs.readFileSync(file,'utf8').replace(/^import .*;\r?$/gm,'').replace(/^export (?=(?:async )?(?:function|let|const|class))/gm,'');
 const ctx={...baseGlobals,...extra};
 vm.runInNewContext("'use strict';\n"+code+'\nthis.result={'+names.join(',')+'};',ctx,{filename:file});
 return ctx.result;
}
const char=new Character({});
const obj=char.toObject();
assert.equal(char.general.background.value,'');
assert.equal(Character.schema.getField('general.background.value').constructor.name,'HTMLField');
assert.equal(Object.keys(char.general.details).length,7);
for(const detail of Object.values(char.general.details)){assert.equal(detail.value,'');assert(detail.label.startsWith('WITCHER.'))}
assert.deepEqual(char.general.homeland,{value:'',otherValue:''});
assert.deepEqual(char.general.reputation,{value:'',label:'WITCHER.Reputation'});
assert.equal(char.general.age,0);
for(const k of ['name','race','socialStanding'])assert.equal(char.general[k],'');
const lifeKeys=Array.from({length:20},(_,i)=>String((i+1)*10));
assert.deepEqual(Object.keys(char.general.lifeEvents),lifeKeys);
lifeKeys.forEach((key,i)=>assert.deepEqual(char.general.lifeEvents[key],{decade:i+1,value:'',details:'',isOpened:false}));
const damageKeys=['slashing','piercing','bludgeoning','elemental','electricity','fire','ice'];
for(const Model of [Common,Character,Monster]){
 const model=new Model({});
 assert.deepEqual(Object.keys(model.damageTypeModification),damageKeys);
 for(const v of Object.values(model.damageTypeModification))assert.deepEqual(v,{flat:0,multiplication:1,applyAP:false});
}
assert.equal(new Monster({}).general,undefined);
assert.equal(new Loot({}).damageTypeModification,undefined);
const odd=new Character({general:{age:-1.5,homeland:{value:'custom'},lifeEvents:{10:{decade:1.5}}},lifeEventCounter:21,damageTypeModification:{fire:{flat:-3.5,multiplication:-0.5,applyAP:true}}});
assert.equal(odd.general.age,-1.5);assert.equal(odd.general.homeland.value,'custom');
assert.equal(odd.general.lifeEvents[10].decade,1.5);assert.equal(odd.lifeEventCounter,21);
assert.equal(odd.damageTypeModification.fire.flat,-3.5);assert.equal(odd.damageTypeModification.fire.multiplication,-0.5);
const r={defaults:{generalKeys:Object.keys(char.general),detailsKeys:Object.keys(char.general.details),lifeKeys,decades:lifeKeys.map(k=>char.general.lifeEvents[k].decade),damageKeys},numberAndStringConstraints:'negative/fractional age, decade and damage values; arbitrary homeland; counter=21 accepted'};
const {baseMixin}=source('module/activeEffect/mixins/baseMixin.js',['baseMixin']);
const paths=baseMixin.getDamageModifcators.call({document:{parent:{system:char}}}).map(v=>v.value);
assert.equal(paths.length,21);
for(const p of paths)assert(Character.schema.getField(p.slice(7)),p);
const nested=baseMixin.getDamageModifcators.call({document:{parent:{system:{},parent:{system:char}}}});
assert.equal(nested.length,21);
assert.equal(baseMixin.getDamageModifcators.call({document:{parent:{system:{},parent:null}}}).length,0);
r.wizard={actor:21,ownedItem:21,unownedItem:0};
const get=(o,p)=>p.split('.').reduce((v,k)=>v?.[k],o);
const labelKeys=[...Object.values(char.general.details).map(d=>d.label),char.general.reputation.label,...Object.values(WITCHER.homelands),...Object.values(WITCHER.socialStanding),...damageKeys.map(k=>'WITCHER.DamageType.'+k),'WITCHER.Effect.wizard.flat','WITCHER.Effect.wizard.multi','WITCHER.Effect.wizard.applyAP','WITCHER.Effect.wizard.resistances'];
r.localizations={};
for(const lang of ['en','ru']){
 const content=utils.expandObject(JSON.parse(fs.readFileSync('lang/'+lang+'.json')));
 const missing=labelKeys.filter(k=>get(content,k)===undefined);assert.equal(missing.length,0);
 r.localizations[lang]={checked:labelKeys.length,missing};
}
let enrichArgs;
foundry.applications.ux={TextEditor:{implementation:{enrichHTML:async field=>{enrichArgs=field;return '<processed>'+field+'</processed>'}}}};
char.general.background.value='<p>History</p>';
const enriched=(await char.enrichedText()).general.background;
assert.equal(enrichArgs,'<p>History</p>');
assert.equal(enriched.value,enrichArgs);
assert.equal(enriched.systemField,Character.schema.getField('general.background.value'));
r.enrichment={value:enriched.value,enriched:enriched.enriched,field:enriched.systemField.fieldPath};
const lifeModel=new Character({general:{lifeEvents:{10:{value:'first'},110:{value:'eleventh'}}}});
const before=lifeModel.toObject();
const updates=[];
const actor={system:lifeModel,update:data=>{updates.push(data);return Promise.resolve(data)}};
class FakeBase {async _prepareContext(){return {actor,system:actor.system}}}
const sheetText=fs.readFileSync('module/actor/sheets/WitcherCharacterSheet.js','utf8');
const method=sheetText.slice(sheetText.indexOf('    async _prepareContext(options) {'),sheetText.indexOf('    async _prepareCharacterData(context) {'));
const context={...baseGlobals,FakeBase};
vm.runInNewContext('this.Sheet=class extends FakeBase {\n'+method+'\n};',context);
const sheet=new context.Sheet();
for(const name of ['_prepareCharacterData','_prepareDiagramFormulas','_prepareCrafting','_prepareSubstances','_prepareAlchemy','_prepareValuables'])sheet[name]=()=>{};
sheet._prepareAlchemyComponentsList=()=>[];sheet._prepareTabs=()=>({});
sheet.document={system:lifeModel};
const prepared=await sheet._prepareContext({});
assert.equal(prepared.system,lifeModel);
assert(Array.isArray(lifeModel.general.lifeEvents));
assert.equal(lifeModel.toObject(false).general.lifeEvents['10'].value,'eleventh');
assert.equal(lifeModel.toObject(false).general.lifeEvents['20'],undefined);
assert.deepEqual(lifeModel.toObject(),before);
const parentText=fs.readFileSync('module/actor/sheets/WitcherActorSheet.js','utf8');
const toggle=parentText.slice(parentText.indexOf('    _onLifeEventDisplay(event) {'),parentText.indexOf('\n}\n',parentText.indexOf('    _onLifeEventDisplay(event) {')));
vm.runInNewContext('this.Toggle=class {\n'+toggle+'\n};',context);
context.Toggle.prototype._onLifeEventDisplay.call({actor},{preventDefault(){},currentTarget:{closest:()=>({dataset:{event:'10'}})}});
assert.equal(updates[0]['system.general.lifeEvents.10.isOpened'],true);
r.lifeEvents={preparedIsArray:true,derivedKey10:lifeModel.toObject(false).general.lifeEvents['10'].value,derivedKey20:String(lifeModel.toObject(false).general.lifeEvents['20']),sourceUnchanged:true,toggleUpdate:updates[0]};
const {damageUtilMixin}=source('module/actor/mixins/damageUtilMixin.js',['damageUtilMixin']);
const {armorMixin}=source('module/actor/mixins/armorMixin.js',['armorMixin']);
const {damageMixin}=source('module/actor/mixins/damageMixin.js',['damageMixin']);
const damageActor={system:new Common({}),...damageUtilMixin,...armorMixin,...damageMixin};
const properties={armorPiercing:false,improvedArmorPiercing:false,bypassesWornArmor:false,bypassesNaturalArmor:false};
const damage={type:'fire',properties,location:{name:'torso',formula:1}};
const armor={system:{resistance:{fire:true}}};
damageActor.system.damageTypeModification.fire={flat:0,multiplication:0.5,applyAP:true};
let error;
try{damageActor.calculateArmorResistances(DamageInstance.create(10).setType('fire'),damage,{})}catch(e){error={name:e.name,message:e.message}}
assert.equal(error?.name,'TypeError');
assert.equal(damageActor.calculateArmorResistances(DamageInstance.create(10).setType('fire'),{...damage,properties:{...properties,armorPiercing:true}},{}).damage,10);
r.applyAP={nonPiercing:error,piercingDamage:10};
damageActor.system.damageTypeModification.fire.applyAP=false;
r.multiplication={};
for(const [name,armorSet] of Object.entries({none:{},worn:{lightArmor:armor},natural:{naturalArmor:armor},both:{lightArmor:armor,naturalArmor:armor}})){
 r.multiplication[name]=damageActor.calculateArmorResistances(DamageInstance.create(10).setType('fire'),damage,armorSet).damage;
}
assert.deepEqual(r.multiplication,{none:10,worn:2,natural:2,both:0});
damageActor.getLocationArmor=()=>({armorSet:{},totalSP:0,displaySP:0});
damageActor.applyAlwaysSpDamage=async()=>0;damageActor.applySpDamage=async()=>0;
r.flat=[];
damageActor.system.damageTypeModification.fire.multiplication=1;
for(const flat of [-3,0,3]){
 damageActor.system.damageTypeModification.fire.flat=flat;
 const result=await damageActor.calculateDamageWithLocation({},damage,[DamageInstance.create(10).setType('fire')]);
 r.flat.push({flat,result:result.damageInstances.map(i=>i.damage),types:result.damageInstances.map(i=>i.type)});
}
assert.deepEqual(r.flat.map(v=>v.result),[[10],[10],[10,3]]);
const {skillMixin}=source('module/actor/mixins/skillMixin.js',['skillMixin'],{});
r.social=[];
for(const [standing,attribute,skill,expected] of [['tolerated','emp','charisma','-1'],['hatedFeared','emp','charisma','-2-1'],['feared','will','intimidation','+1'],['equal','emp','charisma','']]){
 const value=skillMixin.addSocialStanding.call({type:'character',system:{general:{socialStanding:standing}}},{name:attribute},skill);
 assert.equal(value,expected);r.social.push({standing,attribute,skill,value});
}

const helpers={};
const Handlebars={registerHelper:(name,fn)=>{if(typeof name==='object')Object.assign(helpers,name);else helpers[name]=fn},createFrame:d=>({...d})};
const {registerHandelbarHelpers}=source('module/setup/handlebars.js',['registerHandelbarHelpers'],{Handlebars});
await registerHandelbarHelpers();
const emitted=[];
helpers.eachLimit(prepared.system.general.lifeEvents,2,{fn:v=>{emitted.push(v.lifeEvent.key);return ''}});
assert.deepEqual(emitted,['10','20']);
let overflow=0;
helpers.eachLimit(prepared.system.general.lifeEvents,21,{fn:v=>{if(v.lifeEvent===undefined)overflow++;return ''}});
assert.equal(overflow,1);
r.eachLimit={firstTwo:emitted,undefinedAt21:overflow};
const jsonFiles=[];
function walk(dir){for(const e of fs.readdirSync(dir,{withFileTypes:true})){const p=dir+'/'+e.name;if(e.isDirectory())walk(p);else if(p.endsWith('.json'))jsonFiles.push(p)}}
walk('packsJson');
const refs=[];
function scan(value,file,path=''){
 if(typeof value==='string'&&/^system\.(?:general(?:\.|$)|damageTypeModification(?:\.|$))/.test(value))refs.push({file,path,value});
 else if(value&&typeof value==='object')for(const [k,v] of Object.entries(value))scan(v,file,path+'.'+k);
}
for(const file of jsonFiles)scan(JSON.parse(fs.readFileSync(file)),file);
assert.equal(refs.length,0);r.packs={files:jsonFiles.length,refs};

console.log(JSON.stringify(r));

JS
```

Результат: exit 0. Вывод:

```text
{"defaults":{"generalKeys":["background","details","homeland","reputation","socialStanding","name","race","age","lifeEvents"],"detailsKeys":["clothing","personality","hairStyle","affectations","valuedPerson","value","feelingsOnPeople"],"lifeKeys":["10","20","30","40","50","60","70","80","90","100","110","120","130","140","150","160","170","180","190","200"],"decades":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],"damageKeys":["slashing","piercing","bludgeoning","elemental","electricity","fire","ice"]},"numberAndStringConstraints":"negative/fractional age, decade and damage values; arbitrary homeland; counter=21 accepted","wizard":{"actor":21,"ownedItem":21,"unownedItem":0},"localizations":{"en":{"checked":51,"missing":[]},"ru":{"checked":51,"missing":[]}},"enrichment":{"value":"<p>History</p>","enriched":"<processed><p>History</p></processed>","field":"system.general.background.value"},"lifeEvents":{"preparedIsArray":true,"derivedKey10":"eleventh","derivedKey20":"undefined","sourceUnchanged":true,"toggleUpdate":{"system.general.lifeEvents.10.isOpened":true}},"applyAP":{"nonPiercing":{"name":"TypeError","message":"Cannot read properties of undefined (reading 'armorPiercing')"},"piercingDamage":10},"multiplication":{"none":10,"worn":2,"natural":2,"both":0},"flat":[{"flat":-3,"result":[10],"types":["fire"]},{"flat":0,"result":[10],"types":["fire"]},{"flat":3,"result":[10,3],"types":["fire",null]}],"social":[{"standing":"tolerated","attribute":"emp","skill":"charisma","value":"-1"},{"standing":"hatedFeared","attribute":"emp","skill":"charisma","value":"-2-1"},{"standing":"feared","attribute":"will","skill":"intimidation","value":"+1"},{"standing":"equal","attribute":"emp","skill":"charisma","value":""}],"eachLimit":{"firstTwo":["10","20"],"undefinedAt21":1},"packs":{"files":226,"refs":[]}}
(node:654963) [MODULE_TYPELESS_PACKAGE_JSON] Warning: Module type of file:///var/lib/foundryvtt/Data/systems/TheWitcherTRPG-RB-Version/module/data/actor/characterData.js is not specified and it doesn't parse as CommonJS.
Reparsing as ES module because module syntax was detected. This incurs a performance overhead.
To eliminate this warning, add "type": "module" to /var/lib/foundryvtt/Data/systems/TheWitcherTRPG-RB-Version/package.json.
(Use `node --trace-warnings ...` to show where the warning was created)
```

При первом запуске проверки переводов использовался поиск по необработанному JSON: составной background.other оказался ложно отмечен как отсутствующий. Проверен загрузчик Foundry, сценарий исправлен на настоящий foundry.utils.expandObject и повторён успешно. Проблема локализации не регистрировалась. Предупреждение Node MODULE_TYPELESS_PACKAGE_JSON относится к загрузке ES modules в изолированном сценарии; package.json не менялся.

Подмены: game.settings/i18n; базовый контекст листа и соседние подготовки; Actor.update как запись аргументов в массив; TextEditor; регистрация Handlebars/createFrame; данные брони и операции SP. Импортированы настоящие DataModel/TypeDataModel/fields и фабрики системы, методы вычислений и DamageInstance. _prepareContext и _onLifeEventDisplay взяты из исходного текста без изменения тел. Сохранение, HTTP/DOM, полный лист, бой, правила игры, длительность эффектов и весь цикл подготовки Actor не проверены.

### Проверка документации и состава

После оформления выполнены сверка 621 пути с Git/фактическим деревом и байтов с базовым срезом/HEAD; контроль SHA256 исходников; сравнение mode/uid/gid/inode всех ранее отслеживаемых файлов; соответствие карточек строкам реестра; обязательные разделы и поля всех восьми карточек; уникальные issues/status potential; состояния задач; существование локальных Markdown-ссылок и якорей; структура таблиц и git diff --check. Существующие записи журнала сверены с HEAD без изменений.

Итог проверки: exit 0. Реестр — 621 исходник, 41 проверенная карточка, 580 файлов не разобраны; добавлены восемь карточек. Все 27 issues находятся в potential. Проверены 110 Markdown-документов и 2547 локальных ссылок; изменены или созданы 29 документов. Содержимое исходников и mode/uid/gid/inode всех 776 ранее отслеживаемых файлов сохранены; git diff --check прошёл. Историческая часть журнала совпала с HEAD. TASK-0003.004 завершена, родительская TASK-0003 остаётся in-progress; следующая TASK-0003.005 — planned.

## TASK-0003.003

Дата: 2026-09-10. Ветка `rusbar-main`, HEAD `c34b790379fd98cd7e33ccbeeca085e49297a40f`. Рабочее дерево на старте чистое; отслеживались 763 файла. Все 621 исходник совпали со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. Foundry 14.367.0 по /opt/foundryvtt/package.json, Node 24.16.0.

Прочитаны полностью восемь файлов из module/data/actor/templates/common, всего 129 строк: adrenalineData.js (8), currencyData.js (13), focusData.js (9), lifepathData.js (15), noteData.js (9), reputationData.js (20), temporaryEffectsData.js (14), combatEffectsData.js (41). Полное покрытие соседних моделей, листов и обработчиков из этих точечных чтений не выводится.

### Содержательная и перекрёстная сверка

| Направление | Источники и фактический результат |
| --- | --- |
| Файлы ↔ карточки | Сверены все поля восьми файлов, default exports, методы Reputation, наследование DataModel, прямые импорты и внешние вызовы фабрик. |
| Вложение ↔ владельцы | CommonActorData содержит семь непосредственно подключаемых структур порции; TemporaryEffects вложена через combatEffects. Currency дополнительно используется LootData; focus() вызывается четыре раза; notes — ArrayField. |
| Адреналин ↔ потребители | value/label, миграция current→value, настройка useOptionalAdrenaline, кнопки +/- и query из ветки crit. addAdrenaline при разрешении сформировал update value=1; при запрете записи нет. |
| Валюты ↔ модель, курсы и операции | Семь ключей совпали с WITCHER.currency; шесть курсов, falsecoin исключён. Сумма 28 монет даёт вес 0.028 в Common/Loot. Нормальный обмен crown100, amount10→oren дал 90/10; crown→crown дал 110. |
| Focus ↔ форма и castSpell | Четыре независимых слота name/value, чтение положительных значений в focusOptions, два выбора, вычитание из стоимости STA, минимум итоговой стоимости 1. Полный castSpell не запускался. |
| Notes ↔ формы и обработчики | Пустой ArrayField, push/splice и запись массива проверены исходными методами. Шаблоны показывают отдельно Item.note (oldNotes) и массивные записи. Кнопки создания текущих шаблонов — add-item, .add-note вне listener не найдена. |
| Lifepath ↔ schema/подсказки/формула | Четыре скалярных поля и attacks.<ключ>.value. Схемное strong={value:2} дало ` -3+[object Object]`; подсказки strong/joint не содержат .value. |
| Reputation ↔ stat/подготовка/бросок | Пять полей stat; миграция и подготовка на трёх входах дали max 0/7/4. Common.prepareBaseData сам копирует базу, Actor.calculateStats — max в value; два режима броска прочитаны. |
| Локализация ↔ label | WITCHER.Actor.DerStat.Rep отсутствует в восьми языках. WITCHER.Actor.Adrenaline есть в семи, отсутствует в it; en/ru содержат перевод. Fallback клиента не запускался. |
| Боевые записи ↔ config/JSON | 11 changes statusEffects под combatEffects: 5 записей начала хода, 6 модификаторов. 17 строковых путей из 226 JSON, в 17 файлах, все соответствуют схемам; 16 целых записей и один damage.modifier. |
| attack/defenseModifier ↔ формулы | Записи -2/-3 дают строки ` -2[a]` / ` -3[d]`, ноль пропускается. defenseMixin повторно определяет addDefenseModifiers после modifierMixin. |
| turnStartEffects ↔ обработчик | Урон 5+2=7, флаги повреждения переданы, но тип fire потерян до DamageInstance. nonLethal выбирает sta. При heal.amount3/modifier2, HP5/20 записывается 8. |
| TemporaryEffects ↔ лист/расход | Только словарь temporaryHp; temporaryHpSum добавляет лист, не схема. Два значения 3/4 дают сумму 7. При расходе составного эффекта (tempHP3 + attack5) урон6 меняет attack до2 и сохраняет HP10. |
| Ранее описанные зависимости ↔ новые карточки | Уточнены config, registerDataModels, settings, hooks и statData. Дополнены issue-00006/00011/00014 без дубликатов. |

Основные поиски выполнялись через rg по именам фабрик/классов и полям adrenaline, currency, focus1–4, lifepathModifiers, notes, reputation, combatEffects, turnStartEffects, temporaryHp в module/templates. Каждый найденный существенный потребитель прочитан до конкретного обращения; индексы JSON приведены в карточке combatEffectsData.js. Отсутствие прямого пути в JSON не исключает динамическое построение.

В ядре прочитаны DataModel/TypedObjectField/SchemaField и Actor.applyActiveEffects: активные документы собираются через allApplicableEffects, изменения применяются к подготовленным данным в фазах initial/final. Управление документом-источником в системе сверено с onManageActiveEffect delete/toggle. Автоматическое истечение и полный пересчёт после удаления в клиенте не воспроизводились.

### Изолированные проверки

Следующая команда выполнена из корня репозитория. Реальны классы данных/поля и utils Foundry, модели системы, config.js, DamageInstance и указанные исходные методы. Код методов загружается в vm со строгим режимом. Подменены GUI, i18n/settings, ChatMessage и запись Actor/ActiveEffect. В цепочке урона настоящий applyDamageFromStatus доходит до перехваченного Actor.applyDamage; итоговые сопротивления/HP не вычисляются. В проверке смешанного временного эффекта настоящим является updateDerivedStat, документы заменены минимальными объектами.

```bash
node --input-type=module <<'JS'
import fs from 'node:fs';
import vm from 'node:vm';
import assert from 'node:assert/strict';
await import('/opt/foundryvtt/common/primitives/_module.mjs');
const fields=await import('/opt/foundryvtt/common/data/fields.mjs');
const {default:DataModel}=await import('/opt/foundryvtt/common/abstract/data.mjs');
const {default:TypeDataModel}=await import('/opt/foundryvtt/common/abstract/type-data.mjs');
const utils=await import('/opt/foundryvtt/common/utils/helpers.mjs');
globalThis.foundry={data:{fields},abstract:{DataModel,TypeDataModel},utils,applications:{api:{DialogV2:{}}}};
const {default:Common}=await import('./module/data/actor/commonActorData.js');
const {default:Loot}=await import('./module/data/actor/lootData.js');
const {default:Reputation}=await import('./module/data/actor/templates/common/reputationData.js');
const {default:TemporaryEffects}=await import('./module/data/actor/templates/common/temporaryEffectsData.js');
const {WITCHER}=await import('./module/setup/config.js');
const CONFIG={WITCHER};
const get=(o,p)=>p.split('.').reduce((v,k)=>v?.[k],o);
const copy=o=>JSON.parse(JSON.stringify(o));
const fresh=new Common({});
const r={defaults:Object.fromEntries(['adrenaline','currency','focus1','focus2','focus3','focus4','lifepathModifiers','notes','reputation','combatEffects'].map(k=>[k,copy(fresh[k])]))};
assert.equal(fresh.notes.length,0);
assert.equal(fresh.currency.crown,0);
assert.equal(fresh.combatEffects.temporaryEffects.temporaryHpSum,undefined);
assert.equal(fresh.focus1.name,'');assert.equal(fresh.focus1.value,0);
fresh.focus1.value=3;assert.equal(fresh.focus2.value,0);
assert.deepEqual(Object.keys(fresh.currency),Object.keys(WITCHER.currency));
assert.deepEqual(Object.keys(WITCHER.currencyRates),Object.keys(fresh.currency).filter(k=>k!=='falsecoin'));
const wallet={bizant:1,ducat:2,lintar:3,floren:4,crown:5,oren:6,falsecoin:7};
assert.equal(new Common({currency:wallet}).calcCurrencyWeight(),0.028);
assert.equal(new Loot({currency:wallet}).calcCurrencyWeight(),0.028);
r.currencyWeight=0.028;
r.reputation=[];
for(const input of [{max:7},{max:7,unmodifiedMax:0},{max:7,unmodifiedMax:4}]){
 const model=new Reputation({...input});model.prepareBaseData();
 const common=new Common({reputation:{...input}});common.prepareBaseData();
 assert.equal(model.max,common.reputation.max);
 r.reputation.push({input,max:model.max,unmodifiedMax:model.unmodifiedMax});
}
assert.deepEqual(r.reputation.map(v=>v.max),[0,7,4]);
assert.equal(new Common({adrenaline:{current:3}}).adrenaline.value,3);
assert.equal(new Common({adrenaline:{value:2,current:3}}).adrenaline.value,2);
assert.equal(new Common({adrenaline:{value:0,current:3}}).adrenaline.value,3);
r.adrenalineMigration=[3,2,3];
let settings={useOptionalAdrenaline:true};
const game={settings:{get:(s,k)=>settings[k]??false},i18n:{localize:k=>k,format:k=>k},user:{isActiveGM:true,id:'test'}};
const baseGlobals={foundry,CONFIG,game,CONST:{CHAT_MESSAGE_STYLES:{OTHER:0}},ChatMessage:{create:()=>{},getSpeaker:()=>({}),applyMode:()=>{}}};
function source(file,names,extra={}){
 const code=fs.readFileSync(file,'utf8').replace(/^import .*;\r?$/gm,'').replace(/^export \{[^\n]*\};?\r?$/gm,'').replace(/^export (?=(?:async )?(?:function|let|const|class))/gm,'');
 const ctx={...baseGlobals,...extra};vm.runInNewContext("'use strict';\n"+code+'\nglobalThis.result={'+names.join(',')+'};',ctx);return ctx.result;
}
const {adrenalineMixin}=source('module/actor/mixins/adrenalineMixin.js',['adrenalineMixin']);
const adrenalineUpdates=[];
const adrenalineActor={system:fresh,update:u=>adrenalineUpdates.push(u)};
await adrenalineMixin.addAdrenaline.call(adrenalineActor);
settings.useOptionalAdrenaline=false;await adrenalineMixin.addAdrenaline.call(adrenalineActor);
assert.equal(adrenalineUpdates.length,1);assert.equal(adrenalineUpdates[0]['system.adrenaline.value'],1);
const {noteMixin}=source('module/actor/sheets/mixins/noteMixin.js',['noteMixin']);
const noteWrites=[],noteActor={system:fresh,update:u=>noteWrites.push(copy(u))};
await noteMixin._onNoteAdd.call({actor:noteActor});
assert.deepEqual(copy(fresh.notes),[{title:'',details:''}]);
await noteMixin._onNoteDelete.call({actor:noteActor},{currentTarget:{dataset:{noteIndex:'0'}}});
assert.equal(fresh.notes.length,0);r.noteWrites=noteWrites;
const {baseMixin}=source('module/activeEffect/mixins/baseMixin.js',['baseMixin']);
r.lifepathSuggestions=baseMixin.getLifepathSuggestions();
const attackData=new Common({lifepathModifiers:{attacks:{strong:{value:2}}}});
const {weaponAttackMixin}=source('module/actor/mixins/weaponAttackMixin.js',['weaponAttackMixin']);
r.strikeFormula=weaponAttackMixin.handleStrikeType.call({system:attackData},'strong',false);
assert(r.strikeFormula.includes('[object Object]'));
r.strikeFieldClasses={outer:attackData.schema.getField('lifepathModifiers.attacks').constructor.name,element:attackData.schema.getField('lifepathModifiers.attacks').element.constructor.name};
assert(attackData.schema.getField('lifepathModifiers.attacks').element instanceof fields.SchemaField);
assert(attackData.schema.getField('lifepathModifiers.attacks').element.fields.value instanceof fields.NumberField);
const {modifierMixin}=source('module/actor/mixins/modifierMixin.js',['modifierMixin']);
const mods=new Common({combatEffects:{attackModifier:{a:{name:'a',value:-2},zero:{name:'zero',value:0}},defenseModifier:{d:{name:'d',value:-3}}}});
r.modifierStrings={attack:modifierMixin.addAttackModifiers.call({system:mods}),defense:modifierMixin.addDefenseModifiers.call({system:mods})};
assert.equal(r.modifierStrings.attack,' -2[a]');assert.equal(r.modifierStrings.defense,' -3[d]');
let dialogResult;
foundry.applications={api:{DialogV2:{input:async()=>dialogResult}},handlebars:{renderTemplate:async()=>''}};
const {currencyConverterMixin}=source('module/actor/mixins/currencyConverterMixin.js',['currencyConverterMixin']);
r.conversions=[];
for(const to of ['oren','crown']){
 const updates=[],data=new Common({currency:{crown:100}});
 dialogResult={amount:10,from:'crown',to,fee:0};
 await currencyConverterMixin.openCurrencyConverter.call({system:data,name:'test',getCurrencyRates:currencyConverterMixin.getCurrencyRates,update:async u=>updates.push(copy(u))});
 r.conversions.push({to,updates});
 assert.equal(updates[0]['system.currency.crown'],to==='oren'?90:110);
}
const {DamageInstance}=await import('./module/scripts/damageInstance.js');
const {applyDamageFromStatus}=source('module/scripts/combat/applyDamage.js',['applyDamageFromStatus'],{DamageInstance});
const {applyCombatEffect,applyCombatEffects,applyGeneralCombatHooks}=source('module/scripts/combat/generalCombatHook.js',['applyCombatEffect','applyCombatEffects','applyGeneralCombatHooks'],{applyDamageFromStatus});
const {healMixin}=source('module/actor/mixins/healMixin.js',['healMixin']);
const statusData=new Common({derivedStats:{hp:{value:5,max:20}},combatEffects:{turnStartEffects:{
 fire:{name:'fire',damage:{amount:5,modifier:2,type:'fire',allLocations:true,ignoreArmor:true,bypassesShield:true,spDamage:1}},
 heal:{name:'heal',heal:{amount:3,modifier:2}}
}}});
const damageCalls=[],healUpdates=[];
const statusActor={system:statusData,type:'character',getLocationObject:()=>({name:'torso'}),applyDamage:(dialog,instances,props,stat)=>damageCalls.push({instances:instances.map(i=>({damage:i.damage,type:i.type??null})),props,stat}),update:async u=>healUpdates.push(copy(u)),calculateHealValue:healMixin.calculateHealValue,createHealMessage:async()=>{}};
await applyCombatEffect(statusActor,statusData.combatEffects.turnStartEffects.fire);
await applyCombatEffect(statusActor,statusData.combatEffects.turnStartEffects.heal);
assert.equal(damageCalls[0].instances[0].damage,7);assert.equal(damageCalls[0].instances[0].type,null);
assert.equal(healUpdates[0]['system.derivedStats.hp.value'],8);
const nonlethal=new Common({combatEffects:{turnStartEffects:{test:{damage:{amount:1,modifier:2,nonLethal:true}}}}});
await applyCombatEffect(statusActor,nonlethal.combatEffects.turnStartEffects.test);
assert.equal(damageCalls[1].stat,'sta');
r.statusDamage=damageCalls;r.statusHeal=healUpdates;
const tempData=new TemporaryEffects({temporaryHp:{one:{name:'one',value:3},two:{name:'two',value:4}}});
assert.equal(Object.values(tempData.temporaryHp).reduce((s,t)=>s+t.value,0),7);
const {damageMixin}=source('module/actor/mixins/damageMixin.js',['damageMixin']);
const effectWrites=[],hpWrites=[];
const effect={system:{changes:[
 {key:'system.combatEffects.temporaryEffects.temporaryHp.test',value:'{"name":"temp","value":3}'},
 {key:'system.combatEffects.attackModifier.test',value:'{"name":"attack","value":5}'}
]},update:async u=>effectWrites.push(copy(u))};
await damageMixin.updateDerivedStat.call({system:{derivedStats:{hp:{value:10}}},temporaryEffects:[effect],update:async u=>hpWrites.push(copy(u))},6,'hp');
assert.equal(JSON.parse(effect.system.changes[1].value).value,2);
assert.equal(hpWrites[0]['system.derivedStats.hp.value'],10);
r.mixedTemporaryEffect={changes:effect.system.changes,updates:effectWrites,hpWrites};
r.statusDefinitions=WITCHER.statusEffects.flatMap(s=>(s.changes??[]).filter(c=>c.key.startsWith('system.combatEffects.')).map(c=>({status:s.id,key:c.key,value:JSON.parse(c.value)})));
import path from 'node:path';
const files=[];function list(dir){for(const e of fs.readdirSync(dir,{withFileTypes:true})){const p=path.posix.join(dir,e.name);if(e.isDirectory())list(p);else if(p.endsWith('.json'))files.push(p);}}list('packsJson');
const prefixes=['system.adrenaline','system.currency','system.focus','system.lifepathModifiers','system.notes','system.reputation','system.combatEffects'];
const refs=[];function walk(o,file,p=''){if(!o||typeof o!=='object')return;for(const[k,v]of Object.entries(o)){if(typeof v==='string'&&prefixes.some(x=>v.startsWith(x)))refs.push({file,path:p+'.'+k,key:v,change:o});walk(v,file,p+'.'+k);}}
for(const f of files)walk(JSON.parse(fs.readFileSync(f,'utf8')),f);
assert.equal(files.length,226);assert.equal(refs.length,17);
const errors=[];
for(const ref of refs){
 const relative=ref.key.slice('system.'.length);
 const field=fresh.schema.getField(relative,{source:fresh.toObject()});
 if(!field)errors.push(ref.key);
 if(relative.endsWith('.modifier')){assert(field instanceof fields.NumberField);continue;}
 const id=relative.split('.').at(-1);
 const data=new Common({combatEffects:{turnStartEffects:{[id]:JSON.parse(ref.change.value)}}});
 assert.equal(typeof data.combatEffects.turnStartEffects[id].damage.amount,'number');
}
assert.deepEqual(errors,[]);
r.packRefs={files:files.length,references:refs.length,sourceFiles:new Set(refs.map(x=>x.file)).size,paths:[...new Set(refs.map(x=>x.key))],invalid:errors};
const samples=new Common({combatEffects:{attackModifier:{test:{}},turnStartEffects:{test:{}}}});
r.emptyEntries={modifier:copy(samples.combatEffects.attackModifier.test),turn:copy(samples.combatEffects.turnStartEffects.test)};
const langKeys=['WITCHER.Actor.Adrenaline','WITCHER.Actor.DerStat.Rep'];
const langs=fs.readdirSync('lang').filter(f=>f.endsWith('.json'));
r.localizations=Object.fromEntries(langKeys.map(key=>[key,langs.filter(file=>get(JSON.parse(fs.readFileSync('lang/'+file,'utf8')),key)===undefined)]));
assert.equal(r.localizations['WITCHER.Actor.DerStat.Rep'].length,8);

for(const d of r.statusDefinitions){
 const data=utils.expandObject({[d.key.slice(7)]:d.value});
 const model=new Common(data);
 const value=get(model,d.key.slice(7));
 assert(value && typeof value==='object');
}
assert.equal(r.statusDefinitions.length,11);
console.log(JSON.stringify(r,null,2));
JS
```

Результат: **exit 0**, все assert прошли. Основные результаты записаны в таблице выше и карточках issues. Для сериализации перехваченного типа урона undefined заменён null; это не утверждение, что исходный DamageInstance.type равен null.

На этапе настройки сценария непустой TypedObjectField потребовал foundry.utils.isDeletionKey: после чтения определения подключён настоящий common/utils/helpers.mjs. Проверка getField по динамическому ключу без source также потребовала уточнения API: схема записи проверяется через element либо getField с source. Эти промежуточные ограничения запуска не зарегистрированы как проблемы системы. Node сообщает MODULE_TYPELESS_PACKAGE_JSON и автоматически распознаёт ES module; package.json не менялся.

### Проверка документов и сохранности

Проверяются состав реестра по Git/дереву, совпадение всех исходников с HEAD и базовым срезом, начальные хеши содержимого/метаданных, карточки, связи, статусы и Markdown. Применяются прежние исключения; ни docs, ни assets/.github не включаются в покрытие исходников.

```bash
python3 - <<'PY'
import hashlib, json, os, re, subprocess
from pathlib import Path
from urllib.parse import unquote
base='15da5b225535e34af4e132c701b5353ef4eb667f'
expected_head='c34b790379fd98cd7e33ccbeeca085e49297a40f'
registry=Path('docs/analytics/code-audit/registry.md').read_text()
rows=[line for line in registry.splitlines() if re.match(r'^\| \[[^\]]+\]\(\.\./\.\./\.\./',line)]
paths=[re.match(r'^\| \[([^\]]+)\]',r).group(1) for r in rows]
assert len(paths)==len(set(paths))==621
assert sum(r.endswith('| Проверено |') for r in rows)==33
assert sum(r.endswith('| Не начат |') for r in rows)==588
excluded={'README.md','AGENTS.md','LICENSE','.gitignore','.prettierrc','.prettierignore','jsconfig.json.default','package-lock.json','styles/fonts/thewitcher2.ttf'}
def keep(p):
 return p.split('/')[0] not in {'.git','docs','assets','.github'} and p not in excluded and not (p.startswith('packs/') and p.endswith('/LOCK'))
tracked=[p for p in subprocess.check_output(['git','ls-files','-z'],text=True).split('\0') if p]
assert set(filter(keep,tracked))==set(paths)
actual=[]
for d,dirs,files in os.walk('.'):
 if d=='.':dirs[:]=[x for x in dirs if x not in {'.git','docs','assets','.github'}]
 for f in files:
  p=(Path(d)/f).as_posix()
  if keep(p):actual.append(p)
assert set(actual)==set(paths)
assert subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip()==expected_head
for p in paths:
 b=Path(p).read_bytes()
 assert b==subprocess.check_output(['git','show',base+':'+p]),p
 assert b==subprocess.check_output(['git','show',expected_head+':'+p]),p
digest=lambda b:hashlib.sha256(b).hexdigest()
assert digest(b''.join(p.encode()+b'\0'+Path(p).read_bytes()+b'\0' for p in paths))=='9de49bf9b75194490fcfd7bfc80e2b1c8bcd9d90dd26f3603faf21d92b3d0e1e'
meta={p:[Path(p).stat().st_mode,Path(p).stat().st_uid,Path(p).stat().st_gid,Path(p).stat().st_ino] for p in tracked if Path(p).is_file()}
assert digest(json.dumps(meta,sort_keys=True).encode())=='599982e66c22b2595e038ca2d56a439cb28eb6946a1f5cd9fd522e777d2abb2d'
cards=[p for p in Path('docs/analytics/code-audit/files').rglob('*.md') if p.name!='README.md']
assert len(cards)==33
for row in rows:
 p=re.match(r'^\| \[([^\]]+)\]',row).group(1)
 c=Path('docs/analytics/code-audit/files')/(p+'.md')
 assert c.is_file()==row.endswith('| Проверено |'),p
titles=['Назначение файла','Условия использования','Введённые сущности и действия с ними','Основные функции и методы','Используемые сущности и зависимости','Известные потребители','Данные и изменения состояния','Проверки и доказательства','Непроверенные участки и открытые вопросы','Связанные проблемы','История актуализации']
for p in ["module/data/actor/templates/common/adrenalineData.js","module/data/actor/templates/common/currencyData.js","module/data/actor/templates/common/focusData.js","module/data/actor/templates/common/lifepathData.js","module/data/actor/templates/common/noteData.js","module/data/actor/templates/common/reputationData.js","module/data/actor/templates/common/temporaryEffectsData.js","module/data/actor/templates/common/combatEffectsData.js"]:
 t=Path('docs/analytics/code-audit/files/'+p+'.md').read_text()
 for title in titles:assert '## '+title in t,(p,title)
 assert expected_head in t and '| Статус анализа | Проверено |' in t
issues=list(Path('docs/issues').glob('*'+'/issue-*.md'))
assert len(issues)==23
assert {p.stem for p in issues}=={f'issue-{n:05}' for n in range(1,24)}
assert all(p.parent.name=='potential' for p in issues)
task=Path('docs/tasks/task-0003.003.md').read_text()
assert '| Статус | `done` |' in task and '- [ ]' not in task
assert '| Статус | `in-progress` |' in Path('docs/tasks/task-0003-remaining-files.md').read_text()
for n in range(4,11):
 assert '| Статус | `planned` |' in Path(f'docs/tasks/task-0003.{n:03}.md').read_text()
# Сверка точного состава порции и методов.
task_paths=re.findall(r'\[module/[^]]+\]\(\.\./\.\./(module/[^)]+)\)',task)
portion=[p for p in task_paths if '/templates/common/' in p]
assert len(portion)==len(set(portion))==8
assert sum(len(Path(p).read_text().splitlines()) for p in portion)==129
for p in portion:
 raw=Path(p).read_text()
 card=Path('docs/analytics/code-audit/files/'+p+'.md').read_text()
 for field in re.findall(r'(\w+): new fields\.',raw):
  assert field in card,(p,field)
for n in [1,2]:
 assert '| Статус | '+chr(96)+'done'+chr(96)+' |' in Path(f'docs/tasks/task-0003.{n:03}.md').read_text()
checked_links=0
mdfiles=list(Path('docs').rglob('*.md'))
def text_only(text):
 return re.sub(r'^```[^\n]*\n.*?^```[ \t]*$', '',text,flags=re.M|re.S)
def headings(text):
 out=set()
 for h in re.findall(r'^#{1,6}\s+(.+)$',text,flags=re.M):
  h=re.sub(r'\[([^\]]+)\]\([^)]+\)',r'\1',h)
  out.add(re.sub(r'[^\w\-\s]','',h.replace('`','').lower()).replace(' ','-'))
 out.update(re.findall(r'\bid=["\']([^"\']+)',text))
 return out
for f in mdfiles:
 text=re.sub(r'`+[^`]*`+', 'code', text_only(f.read_text()))
 for label,url in re.findall(r'\[([^\]\n]+)\]\(([^)\n]+)\)',text):
  if re.match(r'\w+://',url):continue
  target,_,anchor=url.partition('#')
  dest=(f.parent/unquote(target)).resolve() if target else f.resolve()
  assert dest.exists(),(str(f),url)
  if anchor:assert unquote(anchor) in headings(text_only(dest.read_text())),(str(f),url)
  checked_links+=1
changed=subprocess.check_output(['git','status','--porcelain','--untracked-files=all'],text=True).splitlines()
for row in changed:
 p=row[3:]
 assert p.startswith('docs/'),p
 raw=Path(p).read_text()
 assert all(l==l.rstrip() for l in raw.splitlines()),p
 for block in re.findall(r'(?:^\|.*\n)+',text_only(raw),flags=re.M):
  assert len({len(l.split('|')) for l in block.strip().splitlines()})==1,p
subprocess.run(['git','diff','--check'],check=True)
print(json.dumps({'source_files':621,'cards':33,'not_started':588,'new_cards':8,'potential_issues':23,'tracked_metadata_preserved':len(meta),'markdown_files':len(mdfiles),'local_links':checked_links,'changed_docs':len(changed),'source_and_metadata_hashes':'unchanged','diff_check':'passed'},ensure_ascii=False))
PY
```

Итог проверки: exit 0. Реестр — 621 исходник, 33 проверенные карточки, 588 файлов не разобраны; добавлены восемь карточек. Все 23 issues находятся в potential. Проверены 98 Markdown-документов и 2372 локальные ссылки; изменены или созданы 32 документа. Содержимое исходников и mode/uid/gid/inode всех 763 ранее отслеживаемых файлов сохранены; git diff --check прошёл. TASK-0003.003 завершена, родительская TASK-0003 остаётся in-progress; следующая TASK-0003.004 — planned.

### Наблюдения и пределы

Новые [issue-00019](../../issues/potential/issue-00019.md), [issue-00020](../../issues/potential/issue-00020.md), [issue-00021](../../issues/potential/issue-00021.md), [issue-00022](../../issues/potential/issue-00022.md), [issue-00023](../../issues/potential/issue-00023.md) находятся в potential. Дополнены [issue-00006](../../issues/potential/issue-00006.md), [issue-00011](../../issues/potential/issue-00011.md) и [issue-00014](../../issues/potential/issue-00014.md). Подтверждения пользователем и исправления не выполнялись.

Проверки не включают запуск мира/браузера, запись документов, сетевые запросы, импорт компедиумов, полный боевой цикл, экономику и соответствие рулбуку. Исходники и игровые данные не изменялись. Карточки фиксируют реальные обращения и пределы их изучения; это основание для дальнейших порций, а не доказательство исправности всей системы.

## TASK-0003.002

Дата: 2026-09-10. Ветка `rusbar-main`, HEAD `52acddd5fb7d67e993eed1ad2c89b335aef6fd1d`. На старте рабочее дерево было чистым, отслеживались 750 файлов. Все 621 исходник исследования совпали со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. Foundry 14.367.0 по `/opt/foundryvtt/package.json`; Node 24.16.0.

Полностью прочитаны девять файлов и 262 строки из module/data/actor/templates/common/skills: skillData.js (19), skillsData.js (21), bodyData.js (23), craData.js (28), dexData.js (30), empData.js (35), intData.js (41), refData.js (31), willData.js (34). Карточки и статусы соседних файлов не менялись на «Проверено» из-за чтения отдельных обращений.

### Содержательная и перекрёстная сверка

| Направление | Доказательство и результат |
| --- | --- |
| Девять исходников ↔ карточки | Полные определения, импорт Skill в 7 группах, импорт всех групп в skills(); таблицы каждого поля, подписи, миграции и способы чтения/изменения сверены. |
| Группы ↔ CommonActorData | Единственный прямой вызов skills() — CommonActorData.defineSchema:39; CharacterData и MonsterData наследуют общую модель. Семь групп содержат 13/8/5/2/10/7/7 навыков: всего 52. |
| Схема ↔ skillMap | Все 52 пары attribute.name/name существуют; каждый схемный навык имеет запись. У commonsp ключ справочника commonspeech — единственное несовпадение имён. |
| Skill ↔ поля и вычисление | 7 сохраняемых полей, getter modifiedValue=value+activeEffectModifiers; пять независимых числовых примеров, отсутствие getter в toObject. Ограничение диапазона/целочисленности в Skill не задано. |
| Группы ↔ жизненный цикл Foundry | Реальный DataModelSchemaField вызывает Skill.defineSchema() без label. В свежей CommonActorData 52 label отсутствуют; после toObject/повторной загрузки 52 подписи заполнены миграциями. Метаданные isVisible.label остаются undefined. |
| Миграции ↔ сохранность данных | Все 52 существующие записи проверены с произвольной подписью, value=3 и true-флагами: label заменяется, числовое значение и флаги сохраняются. Пустой source не получает навыков от migrateData. |
| Подписи ↔ lang | Три внешних ключа CRA отсутствуют во всех 8 языках; в skillMap отсутствуют picklock.label и trapcraft.label/rollLabel. Все 52 label после повторного создания разрешаются в en. |
| Формы ↔ поле видимости | Реальный DataField.toFormGroup с подставленным input выбирает label=isVisible. _getSkills возвращает undefined для int.commonspeech и поля для остальных 51 записи. |
| Шаблоны ↔ текущий лист монстра | PARTS.skills выбирает character/tab-skills; он передаёт навык в character/skill-display без фильтра isVisible. Изолированный HTML одинаков при false/true. Отдельный monster-skill-display скрывает запись при false. |
| Бросок ↔ модификаторы | Реальный rollSkillCheck берёт value, затем отдельно вызывает addActiveEffects. Для commonsp с value=3 и модификатором 2 сформировано 1d10 +0 +3; для awareness — 1d10 +0 +3 +2. |
| Повышение ↔ update и журнал | У spellcast 2→3 при магических очках 10 журнал -4, но update сохраняет 10; при 1 — журнал -1 magic/-3 обычных, update сохраняет magic=1 и обычные=17. |
| JSON ↔ реальные поля | Рекурсивно разобраны 226 JSON: 267 строковых ссылок в 37 файлах, 54 различных пути. 264 разрешаются в модель; 3 неверных commonspeech находятся в Torn Stomach и двух состояниях. Индекс файлов — в карточке skillsData.js. |
| Прежние карточки ↔ новые | Уточнены config.js, registerDataModels.js и TheWitcherTRPG.js: полное покрытие skillMap, вложенный Skill отдельно от Item.skill, Polyglot и языковые поля. |

Основные поиски: `rg -n 'system\.skills|skills\(\)|skillData.js|skillsData.js' module`; поиск isVisible/modifiedValue/data-action и ссылок на skill-display в templates и sheets; чтение девяти файлов целиком с номерами строк. Внешние определения прочитаны по фактически установленному ядру: `common/data/fields.mjs` (DataModelSchemaField и DataField.toFormGroup), `common/abstract/data.mjs`, `client/applications/handlebars.mjs` (renderTemplate/formGroup), `client/helpers/localization.mjs` (localize). Эти файлы не входят в реестр системы.

### Изолированные проверки

Команда выполняется из корня системы; отдельный файл сценария не добавлялся. Реальны DataModel/TypeDataModel, поля Foundry, код моделей, config.js, методы формирования путей, навыка и модификаторов, а также два шаблона. Подменены GUI-базовые классы, DOM input/createFormGroup, i18n/settings, ChatMessageData/RollConfig, пользовательский модификатор, социальные/броневые добавки, бросок, журнал и update. Формула перехватывается строкой; очки проверяются по аргументам update. В проверке повышения используется минимальный объект данных, в проверке схем и формул — настоящая CommonActorData.

```bash
node --input-type=module <<'JS'
import fs from 'node:fs';
import vm from 'node:vm';
import assert from 'node:assert/strict';
import {createRequire} from 'node:module';
await import('/opt/foundryvtt/common/primitives/_module.mjs');
const fields=await import('/opt/foundryvtt/common/data/fields.mjs');
const {default:DataModel}=await import('/opt/foundryvtt/common/abstract/data.mjs');
const {default:TypeDataModel}=await import('/opt/foundryvtt/common/abstract/type-data.mjs');
globalThis.foundry={data:{fields},abstract:{DataModel,TypeDataModel}};
const {default:Skill}=await import('./module/data/actor/templates/common/skills/skillData.js');
const {default:Common}=await import('./module/data/actor/commonActorData.js');
const {default:skills}=await import('./module/data/actor/templates/common/skills/skillsData.js');
const {WITCHER}=await import('./module/setup/config.js');
const get=(o,p)=>p?.split('.').reduce((v,k)=>v?.[k],o);
const en=JSON.parse(fs.readFileSync('lang/en.json','utf8'));
const game={i18n:{localize:k=>get(en,k)??k},settings:{get:()=>false}};
const CONFIG={WITCHER};
const models=Object.fromEntries(Object.entries(skills()).map(([g,f])=>[g,f.model]));
const fresh=new Common({});
const reload=new Common(fresh.toObject());
const result={};
const rows=Object.entries(models).flatMap(([g,M])=>Object.keys(M.schema.fields).map(k=>({g,k,field:M.schema.fields[k],fresh:fresh.skills[g][k],reload:reload.skills[g][k]})));
assert.equal(rows.length,52);
assert.deepEqual(Object.keys(Skill.schema.fields),['value','label','isVisible','activeEffectModifiers','isProfession','isPickup','isLearned']);
assert.equal(rows.filter(r=>r.fresh.label===undefined).length,52);
assert.equal(rows.filter(r=>r.reload.label&&get(en,r.reload.label)).length,52);
assert.equal(rows.filter(r=>r.fresh.schema.fields.isVisible.label===undefined).length,52);
result.schema={groups:Object.fromEntries(Object.entries(models).map(([g,M])=>[g,Object.keys(M.schema.fields).length])),skills:52,freshLabelsMissing:52,reloadedLabelsPresent:52,visibilityFieldLabelsMissing:52};
result.modifiedValues=[];
for(const [value,mod,expected] of [[0,0,0],[4,3,7],[1,-4,-3],[12,3,15],[2.5,0.5,3]]) {
 const s=new Skill({value,activeEffectModifiers:mod});
 assert.equal(s.modifiedValue,expected);assert(!Object.hasOwn(s.toObject(),'modifiedValue'));
 result.modifiedValues.push({value,mod,result:s.modifiedValue});
}
for(const [g,M]of Object.entries(models)){
 const keys=Object.keys(M.schema.fields), source=Object.fromEntries(keys.map(k=>[k,{label:'custom',value:3,isVisible:true,isProfession:true,isPickup:true,isLearned:true}]));
 const migrated=M.migrateData(source);
 assert.equal(migrated,source);
 for(const k of keys){assert.equal(source[k].label,reload.skills[g][k].label);assert.equal(source[k].value,3);for(const flag of ['isVisible','isProfession','isPickup','isLearned'])assert.equal(source[k][flag],true);}
 const empty={};M.migrateData(empty);assert.deepEqual(empty,{});
}
const langs=Object.fromEntries(fs.readdirSync('lang').filter(p=>p.endsWith('.json')).map(p=>[p,JSON.parse(fs.readFileSync('lang/'+p,'utf8'))]));
const missingFor=key=>Object.entries(langs).filter(([,l])=>typeof get(l,key)!=='string').map(([n])=>n);
result.missingOuterLabels=rows.filter(r=>missingFor(r.field.label).length===8).map(r=>({path:r.g+'.'+r.k,label:r.field.label,missingIn:missingFor(r.field.label)}));
result.missingConfigLabels=Object.entries(WITCHER.skillMap).flatMap(([id,s])=>['label','rollLabel'].filter(f=>s[f]&&missingFor(s[f]).length===8).map(f=>({id,field:f,label:s[f]})));
assert.equal(result.missingOuterLabels.length,3);
assert.equal(result.missingConfigLabels.length,3);
result.skillMap=Object.entries(WITCHER.skillMap).map(([id,s])=>({id,name:s.name,group:s.attribute.name,pathExists:!!fresh.skills[s.attribute.name]?.[s.name],sameKey:id===s.name}));
assert.equal(result.skillMap.filter(s=>s.pathExists).length,52);
assert.deepEqual(result.skillMap.filter(s=>!s.sameKey).map(s=>s.id),['commonspeech']);
foundry.applications={fields:{createFormGroup:config=>config}};
const visible=Skill.schema.fields.isVisible;
const form=visible.toFormGroup({input:{outerHTML:'stub'}}, {});
result.formLabel=form.label;
assert.equal(form.label,'isVisible');
const {baseMixin}=await import('./module/activeEffect/mixins/baseMixin.js');
globalThis.CONFIG=CONFIG;globalThis.game=game;
const suggestions=Object.values(baseMixin.getSkillSuggestions());
result.invalidSuggestions=suggestions.filter(s=>!get({system:fresh},s.value.replace('.activeEffectModifiers',''))).map(s=>s.value);
assert.deepEqual(result.invalidSuggestions,['system.skills.int.commonspeech.activeEffectModifiers']);
foundry.applications.api={HandlebarsApplicationMixin:C=>C};foundry.applications.sheets={ActorSheetV2:class{}};
foundry.utils={getProperty:get};
const {default:MonsterConfig}=await import('./module/actor/sheets/configurations/WitcherMonsterConfigurationSheet.js');
const visConfig=MonsterConfig.prototype._getSkills.call({actor:{system:fresh}});
result.missingConfigFields=Object.entries(visConfig).flatMap(([g,ss])=>Object.entries(ss).filter(([,s])=>!s.isVisible).map(([k])=>g+'.'+k));
assert.deepEqual(result.missingConfigFields,['int.commonspeech']);
const {modifierMixin}=await import('./module/actor/mixins/modifierMixin.js');
const context={CONFIG,game,ChatMessageData:class{},RollConfig:class{},getCustomModifier:async()=>'',extendedRoll:async formula=>formula};
vm.runInNewContext(fs.readFileSync('module/actor/mixins/skillMixin.js','utf8').replace(/^import .*;\r?$/gm,'').replace('export let skillMixin','const skillMixin')+'\nglobalThis.result=skillMixin;',context);
const actor={system:reload,appliedEffects:[],...modifierMixin,...context.result,addSocialStanding:()=>'',getArmorEcumbrance:()=>0};
reload.skills.int.commonsp.value=3;reload.skills.int.commonsp.activeEffectModifiers=2;
reload.skills.int.awareness.value=3;reload.skills.int.awareness.activeEffectModifiers=2;
result.formulas={commonsp:await actor.rollSkill('commonspeech'),awareness:await actor.rollSkill('awareness')};
assert(!result.formulas.commonsp.endsWith(' +2'));assert(result.formulas.awareness.endsWith(' +2'));
await assert.rejects(()=>actor.rollSkillCheck(WITCHER.skillMap.commonsp),/Cannot read properties of undefined/);
await assert.rejects(()=>actor.levelUpSkill('commonsp'),/Cannot read properties of undefined/);
await assert.rejects(()=>actor.levelUpSkill('commonspeech'),/Cannot read properties of undefined/);
result.commonspFailures=['rollSkillCheck(skillMap.commonsp)','levelUpSkill(commonsp)','levelUpSkill(commonspeech)'];
result.levelUps=[];
for(const magic of [10,1]){
 const updates=[],logs=[];
 const system={skills:{will:{spellcast:{value:2}}},magic:{magicImprovementPoints:magic},improvementPoints:20,logs:{addIpReward:(...a)=>logs.push(a)}};
 await context.result.levelUpSkill.call({system,update:u=>updates.push(u)},'spellcast');
 assert.equal(updates.length,1);assert.equal(updates[0]['system.skills.will.spellcast.value'],3);
 assert.equal(updates[0]['system.magic.magicImprovementPoints'],magic);
 assert.equal(updates[0]['system.improvementPoints'],magic===10?20:17);
 result.levelUps.push({magicBefore:magic,update:updates[0],logs});
}
const require=createRequire(import.meta.url), H=require('/opt/foundryvtt/node_modules/handlebars').create();
H.registerHelper('localize',game.i18n.localize);H.registerHelper('gte',(a,b)=>a>=b);H.registerHelper('or',(...a)=>a.slice(0,-1).some(Boolean));
const current=H.compile(fs.readFileSync('templates/partials/character/skill-display.hbs','utf8'));
const legacy=H.compile(fs.readFileSync('templates/partials/monster/monster-skill-display.hbs','utf8'));
const opt={allowProtoMethodsByDefault:true,allowProtoPropertiesByDefault:true},data={skill:reload.skills.int.awareness,name:'awareness',stat:'int'};
data.skill.isVisible=false;const hidden=current(data,opt),oldHidden=legacy(data,opt);
data.skill.isVisible=true;const shown=current(data,opt),oldShown=legacy(data,opt);
assert.equal(hidden,shown);assert(hidden.includes('data-skill="awareness"'));assert.equal(oldHidden.trim(),'');assert(oldShown.includes('awareness'));
result.visibility={currentIdentical:true,legacyHidden:true,handlebars:H.VERSION};
import path from 'node:path';
const files=[];function list(dir){for(const e of fs.readdirSync(dir,{withFileTypes:true})){const p=path.posix.join(dir,e.name);if(e.isDirectory())list(p);else if(p.endsWith('.json'))files.push(p);}}list('packsJson');
const refs=[];function walk(o,file,p=''){if(!o||typeof o!=='object')return;for(const[k,v]of Object.entries(o)){if(typeof v==='string'&&v.startsWith('system.skills.'))refs.push({file,path:p+'.'+k,key:v});walk(v,file,p+'.'+k);}}
for(const f of files)walk(JSON.parse(fs.readFileSync(f,'utf8')),f);
const invalid=refs.filter(r=>get({system:fresh},r.key)===undefined);
assert.equal(files.length,226);assert.equal(refs.length,267);assert.equal(invalid.length,3);
assert(invalid.every(r=>r.key==='system.skills.int.commonspeech.activeEffectModifiers'));
result.packPaths={jsonFiles:files.length,refs:refs.length,sourceFiles:new Set(refs.map(r=>r.file)).size,uniquePaths:new Set(refs.map(r=>r.key)).size,valid:refs.length-invalid.length,invalid};
result.skillMap={entries:result.skillMap.length,validPaths:result.skillMap.filter(s=>s.pathExists).length,mismatchedKeys:result.skillMap.filter(s=>!s.sameKey).map(s=>s.id)};
console.log(JSON.stringify(result,null,2));
JS
```

**Результат:** exit 0, все assert прошли. Фактические числа и строки записаны в таблице выше и карточках issues. Node выдал MODULE_TYPELESS_PACKAGE_JSON и автоматически распознал ES module; конфигурация пакета не изменялась.

При подготовке проверки первый вызов toFormGroup дошёл до отсутствующего DOM createCheckboxInput. Сценарий уточнён: готовый input передаётся в groupConfig, поэтому проверяется выбор label без имитации рендеринга checkbox. Ошибки первого пробного запуска не объявляются ошибками системы.

### Проверка документов и сохранности исходников

Сценарий проверяет состав путей по реестру, Git и дереву, содержимое относительно HEAD/базового среза, метаданные ранее отслеживаемых файлов (mode/uid/gid/inode), девять новых карточек, их таблицы и статусы задач, issues и локальные Markdown-ссылки. Хеши зафиксированы на старте порции.

```bash
python3 - <<'PY'
import hashlib, json, os, re, subprocess
from pathlib import Path
from urllib.parse import unquote
base='15da5b225535e34af4e132c701b5353ef4eb667f'
expected_head='52acddd5fb7d67e993eed1ad2c89b335aef6fd1d'
registry=Path('docs/analytics/code-audit/registry.md').read_text()
rows=[line for line in registry.splitlines() if re.match(r'^\| \[[^\]]+\]\(\.\./\.\./\.\./',line)]
paths=[re.match(r'^\| \[([^\]]+)\]',r).group(1) for r in rows]
assert len(paths)==len(set(paths))==621
assert sum(r.endswith('| Проверено |') for r in rows)==25
assert sum(r.endswith('| Не начат |') for r in rows)==596
excluded={'README.md','AGENTS.md','LICENSE','.gitignore','.prettierrc','.prettierignore','jsconfig.json.default','package-lock.json','styles/fonts/thewitcher2.ttf'}
def keep(p):
 return p.split('/')[0] not in {'.git','docs','assets','.github'} and p not in excluded and not (p.startswith('packs/') and p.endswith('/LOCK'))
tracked=[p for p in subprocess.check_output(['git','ls-files','-z'],text=True).split('\0') if p]
assert set(filter(keep,tracked))==set(paths)
actual=[]
for d,dirs,files in os.walk('.'):
 if d=='.':dirs[:]=[x for x in dirs if x not in {'.git','docs','assets','.github'}]
 for f in files:
  p=(Path(d)/f).as_posix()
  if keep(p):actual.append(p)
assert set(actual)==set(paths)
assert subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip()==expected_head
for p in paths:
 b=Path(p).read_bytes()
 assert b==subprocess.check_output(['git','show',base+':'+p]),p
 assert b==subprocess.check_output(['git','show',expected_head+':'+p]),p
digest=lambda b:hashlib.sha256(b).hexdigest()
assert digest(b''.join(p.encode()+b'\0'+Path(p).read_bytes()+b'\0' for p in paths))=='9de49bf9b75194490fcfd7bfc80e2b1c8bcd9d90dd26f3603faf21d92b3d0e1e'
meta={p:[Path(p).stat().st_mode,Path(p).stat().st_uid,Path(p).stat().st_gid,Path(p).stat().st_ino] for p in tracked if Path(p).is_file()}
assert digest(json.dumps(meta,sort_keys=True).encode())=='3b4ce984634e9b72300e49903549c6834564986c0ed6a5662f8ff8a0b631e0a9'
cards=[p for p in Path('docs/analytics/code-audit/files').rglob('*.md') if p.name!='README.md']
assert len(cards)==25
for row in rows:
 p=re.match(r'^\| \[([^\]]+)\]',row).group(1)
 c=Path('docs/analytics/code-audit/files')/(p+'.md')
 assert c.is_file()==row.endswith('| Проверено |'),p
titles=['Назначение файла','Условия использования','Введённые сущности и действия с ними','Основные функции и методы','Используемые сущности и зависимости','Известные потребители','Данные и изменения состояния','Проверки и доказательства','Непроверенные участки и открытые вопросы','Связанные проблемы','История актуализации']
for p in ["module/data/actor/templates/common/skills/bodyData.js","module/data/actor/templates/common/skills/craData.js","module/data/actor/templates/common/skills/dexData.js","module/data/actor/templates/common/skills/empData.js","module/data/actor/templates/common/skills/intData.js","module/data/actor/templates/common/skills/refData.js","module/data/actor/templates/common/skills/skillData.js","module/data/actor/templates/common/skills/skillsData.js","module/data/actor/templates/common/skills/willData.js"]:
 t=Path('docs/analytics/code-audit/files/'+p+'.md').read_text()
 for title in titles:assert '## '+title in t,(p,title)
 assert expected_head in t and '| Статус анализа | Проверено |' in t
issues=list(Path('docs/issues').glob('*'+'/issue-*.md'))
assert len(issues)==18
assert {p.stem for p in issues}=={f'issue-{n:05}' for n in range(1,19)}
assert all(p.parent.name=='potential' for p in issues)
task=Path('docs/tasks/task-0003.002.md').read_text()
assert '| Статус | `done` |' in task and '- [ ]' not in task
assert '| Статус | `in-progress` |' in Path('docs/tasks/task-0003-remaining-files.md').read_text()
for n in range(3,11):
 assert '| Статус | `planned` |' in Path(f'docs/tasks/task-0003.{n:03}.md').read_text()
# Содержательная сверка таблиц групп с определениями файлов.
skill_dir=Path('module/data/actor/templates/common/skills')
assert sum(len(p.read_text().splitlines()) for p in skill_dir.glob('*.js'))==262
for p in skill_dir.glob('*Data.js'):
 if p.name in {'skillData.js','skillsData.js'}:continue
 fields=re.findall(r"(\w+): new fields\.EmbeddedDataField\(Skill, \{ label: '([^']+)'",p.read_text())
 card=Path('docs/analytics/code-audit/files')/(str(p)+'.md')
 table_rows=[l for l in card.read_text().splitlines() if l.startswith('| '+chr(96))]
 assert len(fields)==len(table_rows),(p,len(fields),len(table_rows))
 for key,label in fields:
  assert any('| '+chr(96)+key+chr(96)+' | '+chr(96)+label+chr(96)+' |' in row for row in table_rows),(p,key)
assert len(re.findall(r"import .* from './", (skill_dir/'skillsData.js').read_text()))==7
assert '| Статус | '+chr(96)+'done'+chr(96)+' |' in Path('docs/tasks/task-0003.001.md').read_text()
checked_links=0
mdfiles=list(Path('docs').rglob('*.md'))
def text_only(text):
 return re.sub(r'^```[^\n]*\n.*?^```[ \t]*$', '',text,flags=re.M|re.S)
def headings(text):
 out=set()
 for h in re.findall(r'^#{1,6}\s+(.+)$',text,flags=re.M):
  h=re.sub(r'\[([^\]]+)\]\([^)]+\)',r'\1',h)
  out.add(re.sub(r'[^\w\-\s]','',h.replace('`','').lower()).replace(' ','-'))
 out.update(re.findall(r'\bid=["\']([^"\']+)',text))
 return out
for f in mdfiles:
 text=re.sub(r'`+[^`]*`+', 'code', text_only(f.read_text()))
 for label,url in re.findall(r'\[([^\]\n]+)\]\(([^)\n]+)\)',text):
  if re.match(r'\w+://',url):continue
  target,_,anchor=url.partition('#')
  dest=(f.parent/unquote(target)).resolve() if target else f.resolve()
  assert dest.exists(),(str(f),url)
  if anchor:assert unquote(anchor) in headings(text_only(dest.read_text())),(str(f),url)
  checked_links+=1
changed=subprocess.check_output(['git','status','--porcelain','--untracked-files=all'],text=True).splitlines()
for row in changed:
 p=row[3:]
 assert p.startswith('docs/'),p
 raw=Path(p).read_text()
 assert all(l==l.rstrip() for l in raw.splitlines()),p
 for block in re.findall(r'(?:^\|.*\n)+',text_only(raw),flags=re.M):
  assert len({len(l.split('|')) for l in block.strip().splitlines()})==1,p
subprocess.run(['git','diff','--check'],check=True)
print(json.dumps({'source_files':621,'cards':25,'not_started':596,'new_cards':9,'potential_issues':18,'tracked_metadata_preserved':len(meta),'markdown_files':len(mdfiles),'local_links':checked_links,'changed_docs':len(changed),'source_and_metadata_hashes':'unchanged','diff_check':'passed'},ensure_ascii=False))
PY
```

**Фактический итог:** exit 0. Реестр содержит 621 исходник: 25 карточек проверены, 596 файлов не разобраны; добавлены девять карточек. Все 18 issues находятся в potential. Проверены 85 Markdown-документов и 2130 локальных ссылок; изменены или созданы 28 документов. Содержимое 621 исходника и mode/uid/gid/inode всех 750 ранее отслеживаемых файлов сохранены. `git diff --check` прошёл. TASK-0003.002 завершена, родительская TASK-0003 остаётся in-progress; следующая TASK-0003.003 сохраняет статус planned.

### Наблюдения и пределы

Зарегистрированы [issue-00015](../../issues/potential/issue-00015.md), [issue-00016](../../issues/potential/issue-00016.md), [issue-00017](../../issues/potential/issue-00017.md), [issue-00018](../../issues/potential/issue-00018.md); дополнена [issue-00004](../../issues/potential/issue-00004.md). Все остаются potential, подтверждение пользователем и исправления не выполнялись.

Мир, браузерные клики, сохранение документов/компедиумов и полный процесс применения ActiveEffect не проверялись. Наблюдение new CommonActorData({}) не доказывает окончательное состояние Actor после клиентского/серверного цикла создания. Совпадение строковых JSON-путей не доказывает исполнение эффектов или корректность механик по рулбуку. Полный анализ соседних файлов остаётся следующим порциям.

## TASK-0003.001

Дата: 2026-09-10. Ветка `rusbar-main`, HEAD `7b7788bc614e5b7a57f8c596fb64ca75ecabd8b7`. На старте рабочее дерево было чистым; 741 отслеживаемый файл. Все 621 исходник исследования совпали со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. Версия Foundry — 14.367.0 по `/opt/foundryvtt/package.json`.

Полностью прочитаны пять файлов, 143 строки: dataUtils.js (7), valueLabelData.js (8), statData.js (11), statsData.js (70), derivedStatsData.js (47). Соседние определения и потребители проверялись в пределах связей и не получили статуса завершённого пофайлового анализа.

### Содержательная и перекрёстная сверка

| Проверка | Результат | Пределы |
| --- | --- | --- |
| Определения и импорты | createEnrichedText: 5 импортирующих моделей и 20 вызовов; valueLabel: 2 импортирующие фабрики и 8 вызовов; stat: 3 модели и 23 вызова; Stats/DerivedStats импортируются CommonActorData | Поиск по module и чтение определений/обращений; не анализ внешних модулей и макросов миров |
| Поля | Stats содержит 10 записей, DerivedStats — 12; stat создаёт 5 полей каждой записи; valueLabel — 2 | Наличие поля не подтверждает правильность всех потребителей |
| Пределы чисел | Фабрика stat не задаёт min/max; настоящие NumberField сохраняют -3, 0 и 15; integer округляет 2.6 до 3, value=2.5 сохраняется | Это поведение модели, не вывод о правилах игры |
| Подготовка | Stats.prepareBaseData только копирует unmodifiedMax в max, не меняет value/totalModifiers и идемпотентен; основной путь Actor выполняет копирование в CommonActorData | Прямой вызов Stats в проверке не означает автоматический вызов вложенной модели ядром |
| Миграция | Все 10 статов и ровно 6 производных записей имеют перенос при ==0; отсутствующее поле его не вызывает | Установлено на реальных моделях; реальные старые документы мира не исследовались |
| statMap | 9 stats + 11 derivedStats с непустым origin имеют корректные пути totalModifiers; reputation имеет пустой origin; toxicity и shield отсутствуют в справочнике | Для toxicity проверен отдельный getToxSuggestions; различия не объявлены ошибкой |
| Чтение и запись | Разделены построение схем, вычисления подготовленных значений, source-миграция и update ресурсов у потребителей | Полный Actor/Item, бой, формы и эффекты остаются будущим порциям |
| Контракт текста | createEnrichedText ожидает enrichHTML, затем получает поле схемы; исходное value сохранено; исключение распространяется; неизвестный путь даёт undefined | TextEditor подменён, схема и getField настоящие |
| Шаблоны | Прослежены результаты моделей через листы в формы; исходный HBS знаний монстра передаёт value вместо enriched в 3 полях | Handlebars 4.7.9 настоящий; formGroup/localize/TextEditor подменены |
| Локализация | Из 31 проверенного ключа фабрик 30 есть в en/ru; отсутствующий WITCHER.Actor.DerStat.Rep не найден во всех 8 языках | Переводы остальных ключей в других языках и UI локализации не проверялись |
| Компедиумы | В 48 JSON найдены точные key-пути к исследуемым данным: 45 файлов с system.stats и 8 с system.derivedStats, с пересечением | Документы и effects целиком не разобраны; пути перечислены в карточках моделей |
| Взаимная согласованность | Карточка config дополнена соответствием statMap схемам; карточка registerDataModels — вложением Stats/DerivedStats и отсутствием отдельной регистрации этих классов/фабрик | Не расширяет завершённый разбор на CommonActorData или другие соседние файлы |

### Наблюдения

Зарегистрированы только в `potential`:

- [issue-00011](../../issues/potential/issue-00011.md): отсутствие unmodifiedMax не обрабатывается переносом max; в реальной CommonActorData входные int.max=7 и vigor.max=7 без базы после подготовки дали 0.
- [issue-00012](../../issues/potential/issue-00012.md): два прохода calculateStats дали luck.max=14 при базе 10/+2 и toxicity.max=110 при базе 100/+5. Проверены исходные prepareDerivedData/calculateStats, соседние методы подменены.
- [issue-00013](../../issues/potential/issue-00013.md): в аргумент enriched формы знаний монстра попал исходный текст, несмотря на подготовленный результат модели.
- [issue-00014](../../issues/potential/issue-00014.md): отсутствующий ключ подписи числовой репутации передаётся в метаданные поля, которые использует автодополнение ActiveEffect.

С существующими issue-00001–issue-00010 совпадений по установленной локализации не обнаружено. Подтверждение проблем, исправления, смена статусов и новые задачи на исправление не выполнялись.

### Результат и пределы

Подготовлены пять [карточек](files/README.md); в реестре теперь **16 проверенных файлов и 605 неразобранных**. TASK-0003.001 завершена; родительская TASK-0003 остаётся in-progress, следующие девять подзадач первой серии — planned.

Проверены состав и содержимое исходников, локальные ссылки, обязательные разделы карточек, таблицы, статусы и отсутствие изменений вне docs. Для всех 741 существовавших отслеживаемых файлов сохранены mode, uid, gid и inode. Соседние файлы не получили новых карточек. Успешные проверки не подтверждают загрузку мира, доступ службы по HTTP, работу полного жизненного цикла документов, редактора в браузере или обмен между клиентами.

Первый пробный импорт моделей в Node выявил недостающие расширения Array.filterJoin; после подключения штатного `common/primitives/_module.mjs` модели работали без подмен полей или миграции. Предупреждение Node MODULE_TYPELESS_PACKAGE_JSON относится к этому способу локального запуска; package.json не менялся. Результаты реальных моделей и проверки с подменами разделены ниже.

### Проверка схем, миграции и потребителей

Команда выполнялась из корня системы. Импортирует только классы/примитивы ядра и код моделей; не запускает сервер и не записывает документы. В блоке Actor исполняются исходные prepareDerivedData/calculateStats, но родительский метод и соседние расчёты подменены, как указано в коде.

```bash
node --input-type=module <<'JS'
import assert from 'node:assert/strict';
import fs from 'node:fs';
import vm from 'node:vm';
await import('/opt/foundryvtt/common/primitives/_module.mjs');
const fields=await import('/opt/foundryvtt/common/data/fields.mjs');
const {default:DataModel}=await import('/opt/foundryvtt/common/abstract/data.mjs');
const {default:TypeDataModel}=await import('/opt/foundryvtt/common/abstract/type-data.mjs');
globalThis.foundry={data:{fields},abstract:{DataModel,TypeDataModel}};
const {default:stat}=await import('./module/data/actor/templates/common/stats/statData.js');
const {default:valueLabel}=await import('./module/data/actor/templates/valueLabelData.js');
const {default:Stats}=await import('./module/data/actor/templates/common/stats/statsData.js');
const {default:DerivedStats}=await import('./module/data/actor/templates/common/stats/derivedStatsData.js');
const {default:CommonActorData}=await import('./module/data/actor/commonActorData.js');
const {createEnrichedText}=await import('./module/data/dataUtils.js');
const result={};
assert.deepEqual(Object.keys(stat('test')),['max','unmodifiedMax','value','label','totalModifiers']);
assert.deepEqual(Object.keys(valueLabel('test')),['value','label']);
const single=stat('test',100);
assert.equal(single.unmodifiedMax.initial,100);
assert.equal(single.unmodifiedMax.label,'test');
for(const key of ['max','unmodifiedMax','value','totalModifiers']){
 assert.equal(single[key].min,undefined);assert.equal(single[key].max,undefined);
}
assert.equal(single.value.integer,false);assert.equal(single.max.integer,true);
const defaults=new Stats({});
assert.equal(defaults.toxicity.unmodifiedMax,100);
defaults.prepareBaseData();
assert.equal(defaults.toxicity.max,100);
result.schema={stats:Object.keys(Stats.schema.fields),derived:Object.keys(DerivedStats.schema.fields),numberLimits:'not defined'};
const inputs=[-3,0,7,15,2.6];
result.preparation=inputs.map(n=>{
 const s=new Stats({int:{unmodifiedMax:n,value:2.5,totalModifiers:4}});
 s.prepareBaseData();
 const once=JSON.stringify(s.toObject(false));
 s.prepareBaseData();
 assert.equal(JSON.stringify(s.toObject(false)),once);
 assert.equal(s.int.max,Math.round(n));
 assert.equal(s.int.value,2.5);assert.equal(s.int.totalModifiers,4);
 return {input:n,max:s.int.max,value:s.int.value};
});
result.migration=[];
for(const old of [{max:7},{max:7,unmodifiedMax:0},{max:7,unmodifiedMax:4}]){
 const s=new Stats({int:structuredClone(old)});
 const before={...s.int};
 s.prepareBaseData();
 result.migration.push({input:old,afterConstruction:before,afterPreparation:{...s.int}});
}
assert.equal(result.migration[0].afterPreparation.max,0);
assert.equal(result.migration[1].afterPreparation.max,7);
assert.equal(result.migration[2].afterPreparation.max,4);
for(const key of result.schema.stats){
 const source={[key]:{max:7,unmodifiedMax:0}};
 assert.equal(Stats.migrateData(source),source); assert.equal(source[key].unmodifiedMax,7);
}
const migrated=['stun','run','leap','enc','woundTreshold','vigor'];
for(const key of result.schema.derived){
 const s=new DerivedStats({[key]:{max:7,unmodifiedMax:0}});
 assert.equal(s[key].unmodifiedMax,migrated.includes(key)?7:0);
}
const oldVigor=new DerivedStats({vigor:{max:7}});
assert.equal(oldVigor.vigor.unmodifiedMax,0);
assert.equal(typeof oldVigor.prepareBaseData,'undefined');
result.derivedMigration={migrated,missingVigorBase:oldVigor.vigor.unmodifiedMax};
const legacyActorData=new CommonActorData({stats:{int:{max:7}},derivedStats:{vigor:{max:7}}});
legacyActorData.prepareBaseData();
assert.equal(legacyActorData.stats.int.max,0);
assert.equal(legacyActorData.derivedStats.vigor.max,0);
result.legacyActorData={intMax:legacyActorData.stats.int.max,vigorMax:legacyActorData.derivedStats.vigor.max};
const common=new CommonActorData({stats:{body:{unmodifiedMax:6},will:{unmodifiedMax:4},spd:{unmodifiedMax:5},int:{unmodifiedMax:7,value:3}}});
common.prepareBaseData();
assert.equal(common.derivedStats.stun.unmodifiedMax,5);
assert.equal(common.derivedStats.run.unmodifiedMax,15);
assert.equal(common.derivedStats.leap.unmodifiedMax,3);
assert.equal(common.derivedStats.enc.unmodifiedMax,60);
assert.equal(common.derivedStats.rec.unmodifiedMax,5);
assert.equal(common.derivedStats.resolve.unmodifiedMax,55);
assert.equal(common.derivedStats.focus.unmodifiedMax,9);
result.commonPreparation=Object.fromEntries(Object.entries(common.derivedStats).map(([k,v])=>[k,v.unmodifiedMax]));
const configSource=fs.readFileSync('module/setup/config.js','utf8');
const block=configSource.slice(configSource.indexOf('WITCHER.statMap ='),configSource.indexOf('//Skills'));
const ctx={WITCHER:{}};vm.runInNewContext(block,ctx);
const missing=[];const seen={stats:[],derivedStats:[]};
for(const [key,entry] of Object.entries(ctx.WITCHER.statMap)){
 if(!entry.origin)continue;
 const model=entry.origin==='stats'?Stats:DerivedStats;
 if(!model.schema.getField(key+'.totalModifiers'))missing.push(key);
 seen[entry.origin].push(key);
}
assert.deepEqual(missing,[]);
result.statMap={entries:Object.keys(ctx.WITCHER.statMap).length,missing,
 uncoveredStats:result.schema.stats.filter(k=>!seen.stats.includes(k)),
 uncoveredDerived:result.schema.derived.filter(k=>!seen.derivedStats.includes(k)),
 reputation:ctx.WITCHER.statMap.reputation};
assert.deepEqual(result.statMap.uncoveredStats,['toxicity']);
assert.deepEqual(result.statMap.uncoveredDerived,['shield']);
let calls=[];let complete;
foundry.applications={ux:{TextEditor:{implementation:{enrichHTML:async raw=>{
 calls.push(['enrich',raw]); await new Promise(resolve=>complete=resolve);return '<b>enriched</b>';
}}}}};
const model={schema:{getField:path=>{calls.push(['getField',path]);return Stats.schema.getField('int.value');}}};
const original='@UUID[Actor.example]';
const promise=createEnrichedText(model,original,'int.value');
assert.deepEqual(calls,[['enrich',original]]);
complete();
const enriched=await promise;
assert.equal(enriched.value,original);
assert.equal(enriched.enriched,'<b>enriched</b>');
assert.equal(enriched.systemField,Stats.schema.getField('int.value'));
assert.deepEqual(calls,[['enrich',original],['getField','int.value']]);
foundry.applications.ux.TextEditor.implementation.enrichHTML=async ()=>{throw Error('enrich failed');};
await assert.rejects(createEnrichedText(model,'text','int.value'),/enrich failed/);
assert.equal(calls.length,2);
foundry.applications.ux.TextEditor.implementation.enrichHTML=async ()=>'<p>result</p>';
const unknown=await createEnrichedText(new Stats({}),'text','unknown');
assert.equal(unknown.systemField,undefined);
result.enrichedText={order:['enrich awaited','getField'],originalPreserved:true,fieldIdentity:true,rejectionPropagates:true,unknownPath:unknown.systemField??null};
const actorSource=fs.readFileSync('module/actor/witcherActor.js','utf8');
let actorClass=actorSource.slice(actorSource.indexOf('export default class'),actorSource.indexOf('Object.assign(')).replace('export default class','class');
const actorContext={Actor:class{prepareDerivedData(){}},Math,WITCHER:{armorEffects:[]}};
vm.createContext(actorContext);
vm.runInContext(actorClass+'\nglobalThis.Subject=WitcherActor;',actorContext);
const a=new actorContext.Subject();
a.type='character';a.system=common;a.getList=()=>[];a.applyStatus=()=>{};
a.calculateStat=()=>{};a.calculateFixedDerivedStats=()=>{};a.calculateDerivedStats=()=>{};a.calculateAttackStats=()=>{};
common.stats.luck.max=10;common.stats.luck.totalModifiers=2;
common.stats.toxicity.max=100;common.stats.toxicity.totalModifiers=5;
a.prepareDerivedData();
assert.equal(common.stats.luck.max,14);assert.equal(common.stats.toxicity.max,110);
result.actorDoublePass={luck:{base:10,modifier:2,actual:14},toxicity:{base:100,modifier:5,actual:110},scope:'actual prepareDerivedData and calculateStats; other methods stubbed'};
console.log(JSON.stringify(result));

JS
```

Результат: все assert прошли. В частности, при входах Stats `{max:7}`, `{max:7,unmodifiedMax:0}`, `{max:7,unmodifiedMax:4}` после подготовки max равен 0, 7, 4. CommonActorData с отсутствующей базой int/vigor также дала 0. Для BODY=6, WILL=4, SPD=5, INT=7 (исходные), INT.value=3 и WILL.value=0 базовая подготовка дала stun=5, run=15, leap=3, enc=60, rec=5, woundTreshold=5, resolve=55, focus=9 в unmodifiedMax.

### Проверка передачи данных в шаблон

```bash
node --input-type=module <<'JS'
import assert from 'node:assert/strict';
import fs from 'node:fs';
import {createRequire} from 'node:module';
await import('/opt/foundryvtt/common/primitives/_module.mjs');
const fields=await import('/opt/foundryvtt/common/data/fields.mjs');
const {default:DataModel}=await import('/opt/foundryvtt/common/abstract/data.mjs');
const {default:TypeDataModel}=await import('/opt/foundryvtt/common/abstract/type-data.mjs');
globalThis.foundry={data:{fields},abstract:{DataModel,TypeDataModel},applications:{ux:{TextEditor:{implementation:{enrichHTML:async raw=>'<b>PROCESSED</b>'+raw}}}}};
const {default:MonsterData}=await import('./module/data/actor/monsterData.js');
const raw='<p>@UUID[Actor.example]</p>';
const monster=new MonsterData({common:raw,academicKnowledge:raw,monsterLore:raw});
const enrichedText=await monster.enrichedText();
const require=createRequire(import.meta.url), H=require('/opt/foundryvtt/node_modules/handlebars').create();
H.registerHelper('localize',key=>key);
const captures=[];
H.registerHelper('formGroup',(_field,options)=>{captures.push(options.hash);return '';});
const tpl=fs.readFileSync('templates/sheets/actor/partials/monster/tabs/partials/monster-knowledge.hbs','utf8');
const system=monster.toObject(false);
H.compile(tpl)({system,document:{system},systemFields:monster.schema.fields,enrichedText});
assert.equal(captures.length,3);
for(const c of captures){assert.equal(c.value,raw);assert.equal(c.enriched,raw);}
assert.notEqual(enrichedText.lore.common.enriched,captures[0].enriched);
console.log(JSON.stringify({modelCreatesProcessedHtml:true,templatePassesOriginalInstead:true,fields:captures.length,handlebars:require('/opt/foundryvtt/node_modules/handlebars/package.json').version,stubs:['TextEditor.enrichHTML','formGroup','localize'],browser:false}));

JS
```

Результат: все assert прошли; 3 вызова formGroup получили исходный текст вместо обработанного. Подмены: TextEditor.enrichHTML, formGroup и localize. Настоящие: MonsterData и вложенные модели, Handlebars 4.7.9, исходный шаблон. Это не рендер настоящего редактора Foundry.

### Повторная проверка состава и документации

Этот контроль относится к зафиксированному HEAD и метаданным текущего checkout до последующих коммитов. При дальнейшем развитии исследования изменение ожидаемых количеств, HEAD или inode требует осознанного пересмотра проверки; исторические результаты TASK-0001/TASK-0002 ниже сохраняются.

```bash
python3 - <<'PY'
import hashlib, json, os, re, subprocess
from pathlib import Path
from urllib.parse import unquote
base='15da5b225535e34af4e132c701b5353ef4eb667f'
expected_head='7b7788bc614e5b7a57f8c596fb64ca75ecabd8b7'
registry=Path('docs/analytics/code-audit/registry.md').read_text()
rows=[line for line in registry.splitlines() if re.match(r'^\| \[[^\]]+\]\(\.\./\.\./\.\./',line)]
paths=[re.match(r'^\| \[([^\]]+)\]',r).group(1) for r in rows]
assert len(paths)==len(set(paths))==621
assert sum(r.endswith('| Проверено |') for r in rows)==16
assert sum(r.endswith('| Не начат |') for r in rows)==605
excluded={'README.md','AGENTS.md','LICENSE','.gitignore','.prettierrc','.prettierignore','jsconfig.json.default','package-lock.json','styles/fonts/thewitcher2.ttf'}
def keep(p):
 return p.split('/')[0] not in {'.git','docs','assets','.github'} and p not in excluded and not (p.startswith('packs/') and p.endswith('/LOCK'))
tracked=[p for p in subprocess.check_output(['git','ls-files','-z'],text=True).split('\0') if p]
assert set(filter(keep,tracked))==set(paths)
actual=[]
for d,dirs,files in os.walk('.'):
 if d=='.':dirs[:]=[x for x in dirs if x not in {'.git','docs','assets','.github'}]
 for f in files:
  p=(Path(d)/f).as_posix()
  if keep(p):actual.append(p)
assert set(actual)==set(paths)
assert subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip()==expected_head
for p in paths:
 b=Path(p).read_bytes()
 assert b==subprocess.check_output(['git','show',base+':'+p]),p
 assert b==subprocess.check_output(['git','show',expected_head+':'+p]),p
digest=lambda b:hashlib.sha256(b).hexdigest()
assert digest(b''.join(p.encode()+b'\0'+Path(p).read_bytes()+b'\0' for p in paths))=='9de49bf9b75194490fcfd7bfc80e2b1c8bcd9d90dd26f3603faf21d92b3d0e1e'
meta={p:[Path(p).stat().st_mode,Path(p).stat().st_uid,Path(p).stat().st_gid,Path(p).stat().st_ino] for p in tracked if Path(p).is_file()}
assert digest(json.dumps(meta,sort_keys=True).encode())=='4f60b7857ee562cacd2e8973e002e71c26ac63cd57a9a750903adf5c442d40f9'
cards=[p for p in Path('docs/analytics/code-audit/files').rglob('*.md') if p.name!='README.md']
assert len(cards)==16
for row in rows:
 p=re.match(r'^\| \[([^\]]+)\]',row).group(1)
 c=Path('docs/analytics/code-audit/files')/(p+'.md')
 assert c.is_file()==row.endswith('| Проверено |'),p
titles=['Назначение файла','Условия использования','Введённые сущности и действия с ними','Основные функции и методы','Используемые сущности и зависимости','Известные потребители','Данные и изменения состояния','Проверки и доказательства','Непроверенные участки и открытые вопросы','Связанные проблемы','История актуализации']
for p in ["module/data/dataUtils.js","module/data/actor/templates/valueLabelData.js","module/data/actor/templates/common/stats/statData.js","module/data/actor/templates/common/stats/statsData.js","module/data/actor/templates/common/stats/derivedStatsData.js"]:
 t=Path('docs/analytics/code-audit/files/'+p+'.md').read_text()
 for title in titles:assert '## '+title in t,(p,title)
 assert expected_head in t and '| Статус анализа | Проверено |' in t
issues=list(Path('docs/issues').glob('*'+'/issue-*.md'))
assert len(issues)==14
assert {p.stem for p in issues}=={f'issue-{n:05}' for n in range(1,15)}
assert all(p.parent.name=='potential' for p in issues)
task=Path('docs/tasks/task-0003.001.md').read_text()
assert '| Статус | `done` |' in task and '- [ ]' not in task
assert '| Статус | `in-progress` |' in Path('docs/tasks/task-0003-remaining-files.md').read_text()
for n in range(2,11):
 assert '| Статус | `planned` |' in Path(f'docs/tasks/task-0003.{n:03}.md').read_text()
checked_links=0
mdfiles=list(Path('docs').rglob('*.md'))
def text_only(text):
 return re.sub(r'^```[^\n]*\n.*?^```[ \t]*$', '',text,flags=re.M|re.S)
def headings(text):
 out=set()
 for h in re.findall(r'^#{1,6}\s+(.+)$',text,flags=re.M):
  h=re.sub(r'\[([^\]]+)\]\([^)]+\)',r'\1',h)
  out.add(re.sub(r'[^\w\-\s]','',h.replace('`','').lower()).replace(' ','-'))
 out.update(re.findall(r'\bid=["\']([^"\']+)',text))
 return out
for f in mdfiles:
 text=re.sub(r'`+[^`]*`+', 'code', text_only(f.read_text()))
 for label,url in re.findall(r'\[([^\]\n]+)\]\(([^)\n]+)\)',text):
  if re.match(r'\w+://',url):continue
  target,_,anchor=url.partition('#')
  dest=(f.parent/unquote(target)).resolve() if target else f.resolve()
  assert dest.exists(),(str(f),url)
  if anchor:assert unquote(anchor) in headings(text_only(dest.read_text())),(str(f),url)
  checked_links+=1
changed=subprocess.check_output(['git','status','--porcelain','--untracked-files=all'],text=True).splitlines()
for row in changed:
 p=row[3:]
 assert p.startswith('docs/'),p
 raw=Path(p).read_text()
 assert all(l==l.rstrip() for l in raw.splitlines()),p
 for block in re.findall(r'(?:^\|.*\n)+',text_only(raw),flags=re.M):
  assert len({len(l.split('|')) for l in block.strip().splitlines()})==1,p
subprocess.run(['git','diff','--check'],check=True)
print(json.dumps({'source_files':621,'cards':16,'not_started':605,'new_cards':5,'potential_issues':14,'tracked_metadata_preserved':len(meta),'markdown_files':len(mdfiles),'local_links':checked_links,'changed_docs':len(changed),'source_and_metadata_hashes':'unchanged','diff_check':'passed'},ensure_ascii=False))
PY
```

Результат контрольной команды: 621 исходник, 16 карточек, 605 файлов со статусом «Не начат», 14 potential issues. Проверены 72 Markdown-документа и 1799 локальных ссылок. Изменены/созданы 22 документа; исходники и метаданные 741 отслеживаемого файла не изменились. `git diff --check` прошёл. При проверке ссылок учитываются ссылки на существующие каталоги, а примеры JavaScript в строковом коде не трактуются как Markdown-навигация.

## TASK-0002 — итоговая перекрёстная сверка

Дата: 2026-09-10. Ветка rusbar-main; HEAD проверки `3252300787c348e11f95098c345a6af7704b690c`. Все исследуемые исходники совпали со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. Установленное ядро — 14.367.0; это отдельно прочитанная версия, не вывод из compatibility манифеста.

| Проверка | Результат и пределы |
| --- | --- |
| Git и независимый обход дерева с согласованными исключениями | 621 одинаковый путь; исключённые файлы не получили строк реестра |
| Реестр и карточки | Ровно 11 файлов TASK-0002 имеют существующие карточки и статус «Проверено»; остальные 610 — «Не начат» |
| Полнота карточек | Все 11 исходников прочитаны полностью; обязательные разделы, версии и условия проверки присутствуют |
| Связи | Проверены импорты/определения/вызовы и реестры, примеси Actor/Item, helper sum, отправители query/socket, потребители настроек |
| Согласованность порций | Итог проверки четырёх дополнительных типов перенесён в манифест; языковые поля и namespace-импорты уточнены в точке входа; номера строк сверены |
| Конфигурация и шаблоны | Описаны 36 разделов, 21 ключ statMap, 52 навыка, 24 записи Crit, 26 статусов; сверены 59 путей шаблонов и 17 helpers |
| Проблемы | Девять новых карточек issue-00002–issue-00010; вместе с существовавшей issue-00001 — десять уникальных ID, все potential |
| Markdown | Проверены локальные пути ссылок, число столбцов таблиц, обязательные разделы и концевые пробелы; код не трактуется как навигация |
| Неизменность системы | Все 621 исходник совпали с Git blob обеих указанных версий; изменены и созданы только файлы docs |
| Метаданные доступа | Для 726 существовавших на старте путей проверены mode, uid, gid и inode: различий и пропавших путей нет; после завершающих правок проверка повторена |
| Пределы | Статическое чтение и изолированное выполнение с подменами не подтверждают запуск мира, браузер, межклиентскую доставку и игровую корректность всех механик |

Контрольные суммы состава и содержимого равны TASK-0001: `f6291adae3b89183f60336e7cee8c74afe45ed8dddd3d5a19b68e2e458a4f3d8` и `ff62af9c097bf62087f4a67485e78fab808a46008067a323f7478c0d56e9e88f`. Их вычисление приведено ниже.

TASK-0002 завершена; README, реестр, задача и CHANGELOG согласованы с результатом. TASK-0003–TASK-0005 остаются заготовками. Регистрация potential issues не является подтверждением пользователя, исправлением или постановкой задачи.

### Повторная проверка результата TASK-0002

Запуск из корня системы. Команда проверяет именно указанный HEAD и результат этапа. После нового коммита сначала сопоставить исследуемые исходники, прежде чем менять ожидаемую версию. Метаданные доступа проверялись отдельно относительно снимка начала работы; этот снимок не добавлялся в репозиторий.

```bash
python3 - <<'PY'
from pathlib import Path
from urllib.parse import unquote
import collections, hashlib, json, os, re, subprocess

BASE = "15da5b225535e34af4e132c701b5353ef4eb667f"
HEAD = "3252300787c348e11f95098c345a6af7704b690c"
audit = Path("docs/analytics/code-audit")
expected_cards = {
    "system.json", "module/TheWitcherTRPG.js",
    *("module/setup/" + name + ".js" for name in (
        "config", "registerDataModels", "registerSheets", "settings", "hooks",
        "handlebars", "queries", "socketHook", "deprecations"
    ))
}
excluded_files = {
    "README.md", "AGENTS.md", "LICENSE", ".gitignore", ".prettierrc",
    ".prettierignore", "jsconfig.json.default", "package-lock.json",
    "styles/fonts/thewitcher2.ttf"
}
def excluded(p):
    return (p.split("/")[0] in {"docs", "assets", ".github", ".git"}
            or p in excluded_files
            or (p.startswith("packs/") and Path(p).name == "LOCK"))
def git(*args):
    return subprocess.check_output(["git", *args])
assert git("rev-parse", "HEAD").decode().strip() == HEAD
tracked = git("ls-files", "-z").decode().split("\0")[:-1]
included = sorted(p for p in tracked if not excluded(p))
assert len(included) == 621
actual = []
for directory, dirs, files in os.walk("."):
    dirs[:] = [d for d in dirs if not excluded(str((Path(directory)/d).as_posix()))]
    actual.extend(str((Path(directory)/f).as_posix()) for f in files
                  if not excluded(str((Path(directory)/f).as_posix())))
assert sorted(actual) == included
rows = {}
for line in (audit/"registry.md").read_text().splitlines():
    m = re.match(r"\| \[([^]]+)\]\([^)]*\) \| (.*?) \| (.*?) \| (.*?) \|$", line)
    if m:
        path, purpose, desc, status = m.groups()
        assert path not in rows
        rows[path] = (purpose, desc, status)
assert sorted(rows) == included
assert {p for p, r in rows.items() if r[2] == "Проверено"} == expected_cards
assert all(r[2] == "Не начат" for p, r in rows.items() if p not in expected_cards)
cards = {str(p.relative_to(audit/"files"))[:-3]: p
         for p in (audit/"files").rglob("*.md") if p.name != "README.md"}
assert set(cards) == expected_cards
headings = [
    "Назначение файла", "Условия использования", "Введённые сущности и действия с ними",
    "Основные функции и методы", "Используемые сущности и зависимости",
    "Известные потребители", "Данные и изменения состояния", "Проверки и доказательства",
    "Непроверенные участки и открытые вопросы", "Связанные проблемы", "История актуализации"
]
for source, path in cards.items():
    text = path.read_text()
    assert all("\n## " + h + "\n" in text for h in headings)
    assert HEAD in text and BASE in text and "| Статус анализа | Проверено |" in text
    assert rows[source][1] == "[Карточка](files/" + source + ".md)"
for commit in (BASE, HEAD):
    blobs = {}
    for entry in git("ls-tree", "-rz", commit).split(b"\0")[:-1]:
        info, path = entry.split(b"\t", 1)
        blobs[path.decode()] = info.decode().split()[2]
    for path in included:
        data = Path(path).read_bytes()
        assert hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest() == blobs[path]
path_hash = hashlib.sha256(("\n".join(included)+"\n").encode()).hexdigest()
data_hash = hashlib.sha256(b"".join(
    p.encode()+b"\0"+hashlib.sha256(Path(p).read_bytes()).digest()+b"\n"
    for p in included)).hexdigest()
assert path_hash == "f6291adae3b89183f60336e7cee8c74afe45ed8dddd3d5a19b68e2e458a4f3d8"
assert data_hash == "ff62af9c097bf62087f4a67485e78fab808a46008067a323f7478c0d56e9e88f"
issues = list(Path("docs/issues").glob("*/issue-*.md"))
assert len(issues) == 10
assert {p.stem for p in issues} == {"issue-" + str(n).zfill(5) for n in range(1, 11)}
assert all(p.parent.name == "potential" for p in issues)
issue_registry = Path("docs/issues/README.md").read_text()
assert all("[{0}](potential/{0}.md)".format(p.stem) in issue_registry for p in issues)
links = 0
for p in Path("docs").rglob("*.md"):
    text = p.read_text()
    assert all(line == line.rstrip() for line in text.splitlines()), str(p)
    clean = re.sub(r"^\x60\x60\x60[^\n]*\n.*?^\x60\x60\x60\s*$", "", text, flags=re.M|re.S)
    no_code = re.sub(r"\x60[^\x60\n]*\x60", "", clean)
    for url in re.findall(r"\[[^]\n]+\]\(([^\s)]+)\)", no_code):
        if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", url):
            continue
        target = unquote(url.split("#", 1)[0])
        assert (p.parent/target if target else p).exists(), (str(p), url)
        links += 1
    width = None
    for line in clean.splitlines():
        if line.startswith("|"):
            columns = len(re.split(r"(?<!\\)\|", line))-2
            if width is None: width = columns
            assert width == columns, (str(p), line)
        else: width = None
git("diff", "--check")
changes = git("diff", "--name-only").decode().splitlines()
untracked = git("ls-files", "--others", "--exclude-standard").decode().splitlines()
assert all(p.startswith("docs/") for p in changes + untracked)
print(json.dumps({
    "included": len(included), "cards": len(cards), "notStarted": 610,
    "issuesPotential": len(issues), "localLinks": links,
    "pathHash": path_hash, "dataHash": data_hash,
    "sourceMatches": [BASE, HEAD], "onlyDocsChanged": True
}, ensure_ascii=False))
PY
```

## TASK-0002 — порция 1: манифест и точка входа

Дата: 2026-09-10. Коммит проверки: `3252300787c348e11f95098c345a6af7704b690c`; исходники совпадают со срезом `15da5b225535e34af4e132c701b5353ef4eb667f`. Между срезом и HEAD изменена только документация. Рабочее дерево на старте чистое. Установленное ядро — 14.367.0 по `/opt/foundryvtt/package.json`.

Полностью прочитаны system.json (195 строк) и module/TheWitcherTRPG.js (172 строки). Проверены 21 импорт и экспорты источников, соответствие ES-модуля манифесту, существование CSS и восьми локализаций, имена packFolders. Семь буквальных путей packs отсутствуют в checkout; сборка и обработка путей ядром не проверялись, поэтому это не объявлено ошибкой релиза.

Сверены вызовы регистрации и определения обработчиков чата, классов документов, API наград/эффектов, метод WitcherActor.useItem и потребители game.api в rewardsMixin. Проверка зависимого определения не считается полным разбором его файла. Типы данных и листов дополнительно сверяются в порции 3.

Изолированно выполнен исходный ready callback в Node vm с подменой импортов и Foundry API: без pack — TypeError и отсутствие дальнейших шагов; контрольный pack дал getIndex, hotbarDrop, socket, deprecations. Зарегистрирована [issue-00002](../../issues/potential/issue-00002.md). Браузерные сценарии и исполнение макроса не проверялись.

Результат: две карточки, две строки «Проверено». Исходники не изменялись. Итоговая проверка ссылок и покрытия выполняется также после всех порций.

## TASK-0002 — порция 2: конфигурация

Дата: 2026-09-10; HEAD `3252300787c348e11f95098c345a6af7704b690c`, исходник равен срезу TASK-0001. Полностью прочитаны 2431 строка config.js последовательными частями. Сверены все 36 свойств WITCHER, в том числе 52 навыка, 24 записи Crit, 26 статусов. Модуль без импортов выполнен из строки в Node: подсчитаны ключи и разобраны все JSON-строки в changes статусов.

Буквальные обращения CONFIG.WITCHER и шаблонного config сопоставлены с определениями; динамические группы проверены в modifierMixin/baseMixin. Сверены поля Stat, Skill, combatEffects и intData. Прямой буквальный потребитель Crit не найден; damageMixin.applyCritWound читает компедиум. Недостижимость Crit через динамический доступ не утверждается.

Изолированные вызовы настоящего кода с подменой Foundry API: handleStatusCounterIntegration при активном statuscounter и duration=2 даёт TypeError; chooseSkill для общего языка возвращает путь с commonspeech вместо существующего commonsp. Зарегистрированы [issue-00003](../../issues/potential/issue-00003.md) и [issue-00004](../../issues/potential/issue-00004.md). Реальный statuscounter, сохранение эффекта и бросок в мире не запускались.

В ядре 14.367.0 дополнительно проверен setter CONFIG.statusEffects (/opt/foundryvtt/client/client.mjs:30–38), копирующий переданный массив в реестр ядра: присваивание в init само по себе не объявлено ошибкой. Строковые типы changes сверены с миграцией формата в /opt/foundryvtt/common/documents/active-effect.mjs.

Результат: карточка и её связи сверены; пределы поиска и динамические связи явно отмечены. Проверка зависимых определений не выдана за полный разбор их файлов.

## TASK-0002 — порция 3: модели, листы и настройки

Дата: 2026-09-10; тот же HEAD и базовый срез. Полностью прочитаны registerDataModels.js (81 строка), registerSheets.js (145), settings.js (96). Проверены определения 33 импортов моделей/документа чата и 26 импортов листов. Оба регистратора сопоставлены между собой, с манифестом и вызовами из init.

В Node vm выполнены исходные функции с подменой классов и регистрационных API: 4 модели Actor, 22 Item с base, 2 ActiveEffect, 4 ChatMessage; отдельный класс WitcherChatMessage. Листы: 21 Item, 4 Actor, unregister/register ActiveEffect. Настройки: 9 ключей; callback choices на фиктивных Item/Actor pack вернул только Item.

Actor.mystery и Item.clue/obstacle/skill отсутствуют в documentTypes — [issue-00005](../../issues/potential/issue-00005.md). По ядру проверено: Document.TYPES читает game.model; DocumentTypeField проверяет этот список; DocumentSheetConfig допускает отдельную запись sheetClasses[type]. Падение регистрации листов не утверждается. Создание документов в действующем мире не проверено.

Буквальные чтения девяти настроек сверены с module/templates, включая helper getSetting. Наличие чтений в V1-файле не выдано за используемый интерфейс. Карточки разделяют регистрацию, создание модели и рендер. Результат: три карточки и их связи сверены; реальные Foundry-классы и UI не запускались.

## TASK-0002 — порция 4: события, шаблоны, запросы и сокет

Дата: 2026-09-10; тот же HEAD `3252300787c348e11f95098c345a6af7704b690c` и срез TASK-0001. Полностью прочитаны hooks.js (13 строк), handlebars.js (217), queries.js (51), socketHook.js (24), deprecations.js (7). Разделены импорт, регистрация и вызов обработчика. Проверены источники импортов, динамические методы Actor/Item, их подключение примесями, отправители запросов и сокета.

В handlebars сверены 59 существующих шаблонов и 17 helpers; буквальные потребители собраны по templates/**/*.hbs и сопоставлены с регистрацией. Неявная зависимость getOwnedComponentCount → findNeededComponent → Array.prototype.sum подтверждена определениями craftingMixin/ActorSheet и подключением к Actor. Это не утверждение полного разбора зависимых файлов.

Изолированные проверки исходных функций в Node vm с подменой API:

- hooks + два настоящих зависимых обработчика: update флагов без round/turn записал HP 5→7 и duration региона 3→2 — [issue-00006](../../issues/potential/issue-00006.md).
- Helpers: получены 59 путей и 17 регистраций; проверены сравнение, CSV, разность, and/or, capitalize, eachLimit за числом ключей и перепутанные подписи ног — [issue-00007](../../issues/potential/issue-00007.md). eachLimit описан без утверждения достижимости ошибочного входа из UI.
- Query: true до разрешения Promise цели и при отсутствии метода; unknown=false, constructor=true — [issue-00008](../../issues/potential/issue-00008.md). Цели подменены управляемыми заглушками; реальные операции не выполнялись.
- Query регионов: вложенный метод не вызван при true, deleteSpellVisualEffect=false. Настоящий deleteSpellVisualEffect при isGM=false даёт ReferenceError: item is not defined — [issue-00009](../../issues/potential/issue-00009.md).
- Сокет: addItem передал аргументы нужному UUID и удалил его из message.data; unknown на активном GM дал TypeError, другой пользователь проигнорирован — [issue-00010](../../issues/potential/issue-00010.md).

Пустой deprecationWarnings проверен чтением; запуск функции без тела не выдаётся за отдельный тест. Для внешнего поведения дополнительно прочитаны локальные User.query и loadTemplates ядра 14.367.0. Мир, сеть между клиентами, настоящий statuscounter, Handlebars-рендер и canvas не запускались.

Результат: пять карточек сверены с первичными исходниками, регистрациями/вызовами в точке входа и установленными потребителями. Найденные проблемы зарегистрированы только как potential; исходники и данные не исправлялись.

## 2026-09-10 — TASK-0001: состав исследуемого среза

| Поле | Значение |
| --- | --- |
| Задача | [TASK-0001](../../tasks/task-0001-code-inventory.md) |
| Ветка | `rusbar-main` |
| Коммит | `15da5b225535e34af4e132c701b5353ef4eb667f` |
| Начальная проверка состава | `2026-09-10 07:12:58 UTC` |
| Рабочее дерево до записи материалов | Чистое |
| Область проверки | Полный перечень файлов после согласованных исключений; существование и версия исходников |

### Выполненная сверка источников перечня

| Проверка | Способ | Полученный результат |
| --- | --- | --- |
| Исходная версия | `git rev-parse HEAD`, `git branch --show-current`, `git status --porcelain=v1` | Коммит и ветка выше; вывод статуса на старте пустой |
| HEAD и индекс Git | `git ls-tree -rz --name-only HEAD` и `git ls-files -z` | По 706 путей; разность множеств пуста |
| Применение исключений | Сопоставление путей с согласованными 14 правилами | 85 отслеживаемых файлов исключены, 621 включён |
| Фактическое дерево без правил Git ignore | `rg --files --hidden --no-ignore --null` с исключением служебных каталогов, затем согласованных файлов | 621 включённый путь |
| Независимый обход каталогов | `os.walk` с теми же явными исключениями | 621 путь; разности с Git и `rg` пусты |
| Игнорируемые файлы | `git ls-files --others --ignored --exclude-standard -z` | На старте не найдено |
| Неотслеживаемые файлы | `git ls-files --others --exclude-standard -z` | На старте не найдено |
| Чтение и тип включённых файлов | `lstat` и чтение байтов каждого файла | Ошибок чтения и обхода нет; все 621 файла обычные, без символических ссылок |
| Содержимое относительно коммита | Сопоставление Git blob SHA-1 прочитанных байтов с объектами `git ls-tree -rz HEAD` | Все 621 файла совпали с коммитом |

### Учёт исключений

Количество относится к отслеживаемым файлам зафиксированного коммита. Содержимое `.git/` не перечислялось и в Git-перечень не входит.

| Правило | Исключено отслеживаемых файлов |
| --- | --- |
| `docs/` | 28 |
| `assets/` | 39 |
| `.github/` | 4 |
| `.git/` | 0 |
| `README.md` | 1 |
| `AGENTS.md` | 1 |
| `LICENSE` | 1 |
| `.gitignore` | 1 |
| `.prettierrc` | 1 |
| `.prettierignore` | 1 |
| `jsconfig.json.default` | 1 |
| `package-lock.json` | 1 |
| `styles/fonts/thewitcher2.ttf` | 1 |
| `packs/**/LOCK` | 5 |
| **Всего** | **85** |

Рост относительно оценки 701 / 80 обусловлен пятью добавленными файлами задач в `docs/`. Анализируемый состав остался прежним: 621 файл.

### Контрольные суммы

| Проверяемый набор | SHA-256 |
| --- | --- |
| Отсортированный перечень 621 пути | `f6291adae3b89183f60336e7cee8c74afe45ed8dddd3d5a19b68e2e458a4f3d8` |
| Пути и содержимое 621 файла | `ff62af9c097bf62087f4a67485e78fab808a46008067a323f7478c0d56e9e88f` |

Для первой суммы пути сортируются лексикографически, соединяются переводами строки с завершающим переводом строки и кодируются UTF-8. Для второй в том же порядке объединяются UTF-8 путь, нулевой байт, 32 байта SHA-256 содержимого и перевод строки; затем считается SHA-256 объединения.

### Повторная проверка реестра

Команда запускается из корня системы. Она проверяет именно результат TASK-0001 с ещё не начатым пофайловым разбором. После появления карточек ожидаемые статусы и их количество должны проверяться по результатам соответствующей порции; исходная запись этой сверки сохраняется.

```bash
python3 - <<'PY'
from pathlib import Path, PurePosixPath
from urllib.parse import unquote
import collections, hashlib, json, os, re, subprocess

SNAPSHOT = "15da5b225535e34af4e132c701b5353ef4eb667f"
audit = Path("docs/analytics/code-audit")
expected_rules = [
    "docs/", "assets/", ".github/", ".git/",
    "README.md", "AGENTS.md", "LICENSE", ".gitignore", ".prettierrc",
    ".prettierignore", "jsconfig.json.default", "package-lock.json",
    "styles/fonts/thewitcher2.ttf", "packs/**/LOCK",
]

def output(*args):
    return subprocess.check_output(args).decode()

def excluded(path):
    for rule in expected_rules:
        if rule.endswith("/") and path.startswith(rule):
            return True
        if rule == "packs/**/LOCK":
            if path.startswith("packs/") and PurePosixPath(path).name == "LOCK":
                return True
        elif path == rule:
            return True
    return False

def documented_rules(path):
    text = path.read_text()
    section = text.split("## Согласованные исключения\n", 1)[1].split("\n## ", 1)[0]
    return re.findall(r"^\| `([^`]+)` \|", section, re.M)

assert documented_rules(audit / "README.md") == expected_rules
assert documented_rules(Path("docs/tasks/task-0001-code-inventory.md")) == expected_rules
tree = [p for p in output("git", "ls-tree", "-rz", "--name-only", SNAPSHOT).split("\0") if p]
expected = sorted(p for p in tree if not excluded(p))
current_git = {p for p in output("git", "ls-files", "-z").split("\0") if p and not excluded(p)}
rg_paths = {
    p for p in output("rg", "--files", "--hidden", "--no-ignore", "--null",
                      "-g", "!.git/**", "-g", "!docs/**", "-g", "!assets/**", "-g", "!.github/**").split("\0")
    if p and not excluded(p)
}
walk_paths, walk_errors = set(), []
for directory, dirs, files in os.walk(".", followlinks=False, onerror=lambda e: walk_errors.append(str(e))):
    base = Path(directory)
    dirs[:] = [d for d in dirs if not excluded((base / d).as_posix() + "/")]
    for name in files:
        path = base / name
        if not excluded(path.as_posix()):
            assert path.is_file() and not path.is_symlink(), path
            walk_paths.add(path.as_posix())
assert not walk_errors, walk_errors
assert set(expected) == current_git == rg_paths == walk_paths
rows = re.findall(
    r"^\| \[([^\]]+)\]\(([^)]+)\) \| ([^|]+) \| ([^|]+) \| ([^|]+) \|$",
    (audit / "registry.md").read_text(), re.M
)
paths = [row[0] for row in rows]
assert len(paths) == len(set(paths)) and paths == expected
assert all(row[2:] == ("Не установлено", "Не подготовлено", "Не начат") for row in rows)
for path, target, *_ in rows:
    assert (audit / unquote(target)).resolve() == Path(path).resolve()
cards = [p for p in (audit / "files").rglob("*.md") if p != audit / "files/README.md"]
assert not cards, cards

digest = hashlib.sha256()
for path in expected:
    digest.update(path.encode() + b"\0" + hashlib.sha256(Path(path).read_bytes()).digest() + b"\n")
paths_hash = hashlib.sha256(("\n".join(expected) + "\n").encode()).hexdigest()
assert paths_hash == "f6291adae3b89183f60336e7cee8c74afe45ed8dddd3d5a19b68e2e458a4f3d8"
assert digest.hexdigest() == "ff62af9c097bf62087f4a67485e78fab808a46008067a323f7478c0d56e9e88f"

links, anchors, errors = 0, 0, []
markdown = [Path("README.md"), Path("AGENTS.md"), *sorted(Path("docs").rglob("*.md"))]
for file in markdown:
    text = file.read_text()
    lines = text.splitlines()
    for index, line in enumerate(lines):
        if line.rstrip() != line:
            errors.append(f"{file}:{index + 1}: trailing whitespace")
        if line.startswith("#") and index + 1 < len(lines) and lines[index + 1].strip():
            errors.append(f"{file}:{index + 1}: no blank line after heading")
    for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
        target = target.strip().strip("<>")
        if re.match(r"^[a-zA-Z][\w+.-]*:", target):
            continue
        name, sep, fragment = target.partition("#")
        destination = file.parent / unquote(name) if name else file
        if not destination.exists():
            errors.append(f"{file}: missing {target}")
        elif destination.is_file() and destination.suffix == ".md" and sep and fragment:
            headings = re.findall(r"^#+\s+(.+)$", destination.read_text(), re.M)
            slugs = {re.sub(r"[^\w\s-]", "", h.lower()).replace(" ", "-") for h in headings}
            if unquote(fragment) not in slugs:
                errors.append(f"{file}: missing heading {target}")
            anchors += 1
        links += 1
assert not errors, errors
subprocess.run(["git", "diff", "--check"], check=True)
print(json.dumps({
    "snapshot": SNAPSHOT,
    "tracked_in_snapshot": len(tree),
    "excluded_in_snapshot": len(tree) - len(expected),
    "registry_rows": len(paths),
    "git_rg_walk_equal": True,
    "file_cards": len(cards),
    "content_unchanged": True,
    "local_links": links,
    "heading_anchors": anchors,
    "markdown_files": len(markdown),
    "groups": dict(sorted(collections.Counter(p.split("/")[0] if "/" in p else "(root)" for p in paths).items())),
    "errors": []
}, ensure_ascii=False, indent=2))
PY
```

### Результат проверки готовых документов

Приведённая команда выполнена после создания материалов и повторно после оформления итогов; оба запуска завершились с кодом 0. Итоговая проверка охватила 35 Markdown-документов, 813 локальных ссылок и 5 ссылок на заголовки. Состав реестра и контрольные суммы повторно совпали с исходной проверкой.

| Проверка | Результат |
| --- | --- |
| Строки реестра против Git, `rg` и обхода каталогов | 621 уникальная строка; множества путей совпали в обе стороны; порядок соответствует сортировке |
| Исключения в задаче и README | Все 14 согласованных правил совпадают; исключённых файлов в реестре нет |
| Ссылки на исходники | Каждый путь ведёт к соответствующему существующему файлу |
| Назначения, карточки и статусы | Во всех 621 строках «Не установлено», «Не подготовлено», «Не начат»; карточек исходников нет; `files/README.md` учитывается как указатель |
| Шаблон карточки | Сверен с требованиями: назначение, определения, функции и методы, действия с данными, зависимости, потребители, доказательства, ограничения и проблемы предусмотрены |
| Контрольные суммы исходников | Перечень и содержимое совпали с начальной проверкой |
| Локальные ссылки и якоря заголовков | Ошибок не выявлено; ссылки на каталоги также проверены |
| Markdown и `git diff --check` | Пробелов в конце строк и ошибок проверяемого оформления нет |
| Метаданные доступа существующих файлов | Права, владельцы, группы и inode сохранены |

TASK-0001 завершена как инвентаризация и подготовка основы. Появление 621 строки не означает завершения пофайлового анализа. Реестр и документы результатов находятся в исключённой папке `docs/` и не увеличивают исследуемый состав.

### Пределы вывода

Совпадение путей и содержимого подтверждает состав и версию исследуемых файлов. В этом этапе не проверялись назначения отдельных файлов, функции, межфайловые связи, загрузка системы или игровые сценарии. Базы компедиумов не собирались и не извлекались.

Новых проблем системы при сверке состава не выявлено. Отсутствие новых карточек проблем на этапе инвентаризации не означает исправности кода.
