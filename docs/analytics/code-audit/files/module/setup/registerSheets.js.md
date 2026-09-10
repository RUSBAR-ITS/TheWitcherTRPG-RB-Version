# module/setup/registerSheets.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/setup/registerSheets.js](../../../../../../module/setup/registerSheets.js) |
| Тип файла | JavaScript — регистрация |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `3252300787c348e11f95098c345a6af7704b690c`; исходник совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f` |
| Изменения относительно коммита | Нет |
| Задача и порция | [TASK-0002](../../../../../tasks/task-0002-system-initialization.md); порция 3 |
| Запись перекрёстной сверки | [Журнал сверок](../../../review-log.md) — TASK-0002, порция 3 |

## Назначение файла

Регистрирует общие и специализированные листы Actor/Item и заменяет стандартный редактор ActiveEffect.

## Условия использования

[module/TheWitcherTRPG.js](../../../../../../module/TheWitcherTRPG.js) — обработчик init, вызывает функцию после назначения классов документов.

При импорте дополнительно сохраняет ссылки Actors и Items из foundry.documents.collections. Вызов передаёт регистрации ядру; на стадии init ядро накапливает их в очереди, а не немедленно открывает окна.

## Введённые сущности и действия с ними

| API | Первый аргумент | Второй аргумент | Остальные аргументы |
| --- | --- | --- | --- |
| Items | witcher | `WitcherItemSheet` | [{"makeDefault":true}] |
| Items | witcher | `WitcherAlchemicalSheet` | [{"makeDefault":true,"types":["alchemical"]}] |
| Items | witcher | `WitcherArmorSheet` | [{"makeDefault":true,"types":["armor"]}] |
| Items | witcher | `WitcherContainerSheet` | [{"makeDefault":true,"types":["container"]}] |
| Items | witcher | `WitcherComponentSheet` | [{"makeDefault":true,"types":["component"]}] |
| Items | witcher | `WitcherCriticalWoundSheet` | [{"makeDefault":true,"types":["criticalWound"]}] |
| Items | witcher | `WitcherDiagramSheet` | [{"makeDefault":true,"types":["diagrams"]}] |
| Items | witcher | `WitcherEnhancementSheet` | [{"makeDefault":true,"types":["enhancement"]}] |
| Items | witcher | `WitcherHomelandSheet` | [{"makeDefault":true,"types":["homeland"]}] |
| Items | witcher | `WitcherMutagenSheet` | [{"makeDefault":true,"types":["mutagen"]}] |
| Items | witcher | `WitcherProfessionSheet` | [{"makeDefault":true,"types":["profession"]}] |
| Items | witcher | `WitcherSpellSheet` | [{"makeDefault":true,"types":["spell"]}] |
| Items | witcher | `WitcherHexSheet` | [{"makeDefault":true,"types":["hex"]}] |
| Items | witcher | `WitcherRaceSheet` | [{"makeDefault":true,"types":["race"]}] |
| Items | witcher | `WitcherMountSheet` | [{"makeDefault":true,"types":["mount"]}] |
| Items | witcher | `WitcherRitualSheet` | [{"makeDefault":true,"types":["ritual"]}] |
| Items | witcher | `WitcherValuableSheet` | [{"makeDefault":true,"types":["valuable"]}] |
| Items | witcher | `WitcherWeaponSheet` | [{"makeDefault":true,"types":["weapon"]}] |
| Actors | witcher | `WitcherCharacterSheet` | [{"makeDefault":true,"types":["character"]}] |
| Actors | witcher | `WitcherMonsterSheet` | [{"makeDefault":true,"types":["monster"]}] |
| Actors | witcher | `WitcherLootSheet` | [{"makeDefault":true,"types":["loot"]}] |
| Actors | witcher | `WitcherMysterySheet` | [{"makeDefault":true,"types":["mystery"]}] |
| Items | witcher | `WitcherClueSheet` | [{"makeDefault":true,"types":["clue"]}] |
| Items | witcher | `WitcherObstacleSheet` | [{"makeDefault":true,"types":["obstacle"]}] |
| Items | witcher | `WitcherSkillItemSheet` | [{"makeDefault":true,"types":["skill"]}] |
| unregisterSheet | ActiveEffect | `core` | ["CoreActiveEffectConfig"] |
| registerSheet | ActiveEffect | `witcher` | ["WitcherActiveEffectConfig",{"makeDefault":true}] |

21 регистрация Item: общий WitcherItemSheet без types и 20 специализированных. Для note отдельного листа нет — применяется общий при наличии типа в реестре ядра. Четыре листа Actor. Один unregisterSheet и один registerSheet для ActiveEffect. Namespace листов — witcher, это отдельный идентификатор регистрации, не system.id. Импорт WitcherProfessionSheet ссылается на default-класс с фактическим именем WitcheProfessionSheet; допустимое имя импорта не обязано совпадать с именем default-класса.

## Основные функции и методы

| Функция | Вход / результат | Действия и условия |
| --- | --- | --- |
| registerSheets() | Без аргументов; undefined; синхронная | Передаёт makeDefault: true во все регистрации. Сначала общий Item-лист, затем специальные; core ActiveEffectConfig снимается, WitcherActiveEffectConfig регистрируется для всех доступных типов. |

В установленном ядре сохранённый выбор листа пользователя учитывается при вычислении default; makeDefault не означает безусловную отмену сохранённых настроек.

## Используемые сущности и зависимости

| Сущность | Файл / API | Вид связи | Место / назначение | Доказательство |
| --- | --- | --- | --- | --- |
| `WitcherCharacterSheet` | [module/actor/sheets/WitcherCharacterSheet.js](../../../../../../module/actor/sheets/WitcherCharacterSheet.js) | ES import → регистрация | registerSheets: класс в аргументе API | стр. 11: `export default class WitcherCharacterSheet extends WitcherActorSheet {` |
| `WitcherMonsterSheet` | [module/actor/sheets/WitcherMonsterSheet.js](../../../../../../module/actor/sheets/WitcherMonsterSheet.js) | ES import → регистрация | registerSheets: класс в аргументе API | стр. 7: `export default class WitcherMonsterSheet extends WitcherActorSheet {` |
| `WitcherLootSheet` | [module/actor/sheets/WitcherLootSheet.js](../../../../../../module/actor/sheets/WitcherLootSheet.js) | ES import → регистрация | registerSheets: класс в аргументе API | стр. 8: `export default class WitcherLootSheet extends HandlebarsApplicationMixin(ActorSheetV2) {` |
| `WitcherWeaponSheet` | [module/item/sheets/WitcherWeaponSheet.js](../../../../../../module/item/sheets/WitcherWeaponSheet.js) | ES import → регистрация | registerSheets: класс в аргументе API | стр. 5: `export default class WitcherWeaponSheet extends WitcherItemSheet {` |
| `WitcherDiagramSheet` | [module/item/sheets/WitcherDiagramSheet.js](../../../../../../module/item/sheets/WitcherDiagramSheet.js) | ES import → регистрация | registerSheets: класс в аргументе API | стр. 3: `export default class WitcherDiagramSheet extends WitcherItemSheet {` |
| `WitcherContainerSheet` | [module/item/sheets/WitcherContainerSheet.js](../../../../../../module/item/sheets/WitcherContainerSheet.js) | ES import → регистрация | registerSheets: класс в аргументе API | стр. 4: `export default class WitcherContainerSheet extends WitcherItemSheet {` |
| `WitcherMysterySheet` | [module/actor/sheets/investigation/WitcherMysterySheet.js](../../../../../../module/actor/sheets/investigation/WitcherMysterySheet.js) | ES import → регистрация | registerSheets: класс в аргументе API | стр. 6: `export default class WitcherMysterySheet extends HandlebarsApplicationMixin(ActorSheetV2) {` |
| `WitcherClueSheet` | [module/item/sheets/investigation/WitcherClueSheet.js](../../../../../../module/item/sheets/investigation/WitcherClueSheet.js) | ES import → регистрация | registerSheets: класс в аргументе API | стр. 1: `export default class WitcherClueSheet extends foundry.appv1.sheets.ItemSheet {` |
| `WitcherObstacleSheet` | [module/item/sheets/investigation/WitcherObstacleSheet.js](../../../../../../module/item/sheets/investigation/WitcherObstacleSheet.js) | ES import → регистрация | registerSheets: класс в аргументе API | стр. 1: `export default class WitcherObstacleSheet extends foundry.appv1.sheets.ItemSheet {` |
| `WitcherSpellSheet` | [module/item/sheets/WitcherSpellSheet.js](../../../../../../module/item/sheets/WitcherSpellSheet.js) | ES import → регистрация | registerSheets: класс в аргументе API | стр. 5: `export default class WitcherSpellSheet extends WitcherItemSheet {` |
| `WitcherAlchemicalSheet` | [module/item/sheets/WitcherAlchemicalSheet.js](../../../../../../module/item/sheets/WitcherAlchemicalSheet.js) | ES import → регистрация | registerSheets: класс в аргументе API | стр. 4: `export default class WitcherAlchemicalSheet extends WitcherItemSheet {` |
| `WitcherArmorSheet` | [module/item/sheets/WitcherArmorSheet.js](../../../../../../module/item/sheets/WitcherArmorSheet.js) | ES import → регистрация | registerSheets: класс в аргументе API | стр. 5: `export default class WitcherArmorSheet extends WitcherItemSheet {` |
| `WitcherValuableSheet` | [module/item/sheets/WitcherValuableSheet.js](../../../../../../module/item/sheets/WitcherValuableSheet.js) | ES import → регистрация | registerSheets: класс в аргументе API | стр. 4: `export default class WitcherValuableSheet extends WitcherItemSheet {` |
| `WitcherActiveEffectConfig` | [module/activeEffect/WitcherActiveEffectSheet.js](../../../../../../module/activeEffect/WitcherActiveEffectSheet.js) | ES import → регистрация | registerSheets: класс в аргументе API | стр. 6: `export class WitcherActiveEffectConfig extends foundry.applications.sheets.ActiveEffectConfig {` |
| `WitcherProfessionSheet` | [module/item/sheets/WitcherProfessionSheet.js](../../../../../../module/item/sheets/WitcherProfessionSheet.js) | ES import → регистрация | registerSheets: класс в аргументе API | стр. 4: `export default class WitcheProfessionSheet extends WitcherItemSheet {` |
| `WitcherSkillItemSheet` | [module/item/sheets/WitcherSkillItemSheet.js](../../../../../../module/item/sheets/WitcherSkillItemSheet.js) | ES import → регистрация | registerSheets: класс в аргументе API | стр. 4: `export default class WitcherSkillItemSheet extends HandlebarsApplicationMixin(ItemSheetV2) {` |
| `WitcherMutagenSheet` | [module/item/sheets/WitcherMutagenSheet.js](../../../../../../module/item/sheets/WitcherMutagenSheet.js) | ES import → регистрация | registerSheets: класс в аргументе API | стр. 3: `export default class WitcherMutagenSheet extends WitcherItemSheet {` |
| `WitcherEnhancementSheet` | [module/item/sheets/WitcherEnhancementSheet.js](../../../../../../module/item/sheets/WitcherEnhancementSheet.js) | ES import → регистрация | registerSheets: класс в аргументе API | стр. 3: `export default class WitcherEnhancementSheet extends WitcherItemSheet {` |
| `WitcherHexSheet` | [module/item/sheets/WitcherHexSheet.js](../../../../../../module/item/sheets/WitcherHexSheet.js) | ES import → регистрация | registerSheets: класс в аргументе API | стр. 3: `export default class WitcherHexSheet extends WitcherItemSheet {` |
| `WitcherRitualSheet` | [module/item/sheets/WitcherRitualSheet.js](../../../../../../module/item/sheets/WitcherRitualSheet.js) | ES import → регистрация | registerSheets: класс в аргументе API | стр. 3: `export default class WitcherRitualSheet extends WitcherItemSheet {` |
| `WitcherRaceSheet` | [module/item/sheets/WitcherRaceSheet.js](../../../../../../module/item/sheets/WitcherRaceSheet.js) | ES import → регистрация | registerSheets: класс в аргументе API | стр. 3: `export default class WitcherRaceSheet extends WitcherItemSheet {` |
| `WitcherItemSheet` | [module/item/sheets/WitcherItemSheet.js](../../../../../../module/item/sheets/WitcherItemSheet.js) | ES import → регистрация | registerSheets: класс в аргументе API | стр. 7: `export default class WitcherItemSheet extends HandlebarsApplicationMixin(ItemSheetV2) {` |
| `WitcherMountSheet` | [module/item/sheets/WitcherMountSheet.js](../../../../../../module/item/sheets/WitcherMountSheet.js) | ES import → регистрация | registerSheets: класс в аргументе API | стр. 3: `export default class WitcherMountSheet extends WitcherItemSheet {` |
| `WitcherComponentSheet` | [module/item/sheets/WitcherComponentSheet.js](../../../../../../module/item/sheets/WitcherComponentSheet.js) | ES import → регистрация | registerSheets: класс в аргументе API | стр. 3: `export default class WitcherComponentSheet extends WitcherItemSheet {` |
| `WitcherHomelandSheet` | [module/item/sheets/WitcherHomelandSheet.js](../../../../../../module/item/sheets/WitcherHomelandSheet.js) | ES import → регистрация | registerSheets: класс в аргументе API | стр. 3: `export default class WitcherHomelandSheet extends WitcherItemSheet {` |
| `WitcherCriticalWoundSheet` | [module/item/sheets/WitcherCriticalWoundSheet.js](../../../../../../module/item/sheets/WitcherCriticalWoundSheet.js) | ES import → регистрация | registerSheets: класс в аргументе API | стр. 3: `export default class WitcherCriticalWoundSheet extends WitcherItemSheet {` |

Внешние зависимости: foundry.documents.collections.Actors/Items, глобальный ActiveEffect, foundry.applications.apps.DocumentSheetConfig, foundry.applications.sheets.ActiveEffectConfig. Источник поведения очереди/выбора листа: установленный /opt/foundryvtt/client/applications/apps/document-sheet-config.mjs:370, 381–394, 410–467.

## Известные потребители

[module/TheWitcherTRPG.js](../../../../../../module/TheWitcherTRPG.js) — обработчик init, вызывает функцию после назначения классов документов.

[system.json](../../../../../../system.json) задаёт объявленные типы; [module/setup/registerDataModels.js](../../../../../../module/setup/registerDataModels.js) регистрирует модели тех же типов. Дальнейший потребитель CONFIG — механизм документов и листов Foundry; прямого создания Actor/Item здесь нет.

## Данные и изменения состояния

Изменяется набор доступных листов/ожидающих регистраций ядра. Прямого сохранения Actor/Item, рендера листов или записи настройки листа здесь нет.

## Проверки и доказательства

Полный файл прочитан. Все 26 импортов сопоставлены с существующими экспортами и точными регистрациями. Исходная функция выполнена в Node vm с заменами импортов и API; полученные регистрации сведены в таблицу выше. Ключи сопоставлены с JSON-манифестом и соседним регистратором. Это проверка вызовов регистрации, не загрузка реальных классов в Foundry.

## Непроверенные участки и открытые вопросы

Схемы и поведение самих моделей/листов за пределами проверки определений не анализировались полностью. Мир не запускался, окна не открывались, сохранённые настройки листов и создание незаявленных типов не проверялись.

## Связанные проблемы

[issue-00005](../../../../../issues/potential/issue-00005.md) — четыре типа зарегистрированы в коде, но отсутствуют в манифесте.

## История актуализации

2026-09-10 — первичный разбор полного файла на указанном коммите; сверка порции 3 отражена в журнале. Файлы зависимостей проверены в пределах определений и обращений, без объявления их полного разбора.

## Уточнение TASK-0003.005

2026-09-10, `c9eac1ffb28fdf69935d500fff26d4d0ad1d1609`. Проверены конкретные последствия текущей регистрации WitcherCharacterSheet/WitcherMonsterSheet: оба используют общий tab-skills, но IP-секция обращается к девяти полям, отсутствующим в MonsterData ([issue-00030](../../../../../issues/potential/issue-00030.md)). [Карточка pannels](../data/actor/templates/character/pannelsData.js.md) отделяет текущие общие skills/magic-шаблоны от старых monster-* шаблонов с флагами раскрытия. Предзагрузка старого шаблона не доказывает его текущий выбор листом.

[Сверка TASK-0003.005](../../../review-log.md#task-0003005).

## Уточнение TASK-0003.006

2026-09-10, `fe7ea7420cd4dfa6ee51baf7520f7b0ad8f8b13d`. Типы character/monster/loot связаны с соответствующими моделями и листами; текущие PARTS специализированных листов точечно сверены. Общая IP-вкладка монстра всё ещё не соответствует его полям (issue-00030). Отображение полей старыми шаблонами не приравнивается к использованию текущим зарегистрированным листом.

Карточки сборки: [characterData](../data/actor/characterData.js.md), [monsterData](../data/actor/monsterData.js.md), [lootData](../data/actor/lootData.js.md). [Сверка TASK-0003.006](../../../review-log.md#task-0003006).

## Уточнение TASK-0003.008

2026-09-10, `c5edcbadd05ff4038a174bd2e2a49785e40ea878`; исходник не изменился относительно исходного среза. Отдельно от регистрации моделей и CONFIG.Item.documentClass функция регистрирует WitcherItemSheet и специализированные листы. Проверенный WitcherItemSheet._prepareContext:45–58 читает document.system/schema и вызывает system.enrichedText?.() напрямую; обёртка WitcherItem.enrichedText не является фактическим промежуточным вызовом этого листа.

Связанные карточки: [CommonItemData](../data/item/commonItemData.js.md) и [WitcherItem](../item/witcherItem.js.md). [Перекрёстная сверка](../../../review-log.md#task-0003008). Новая запись уточняет связи; исторические результаты прежних порций сохранены.

## Уточнение TASK-0003.010

2026-09-10, `247d3d86e344238a1445377c686eb6455146693c`; исходник прежнего среза не изменён.

Полностью разобран зарегистрированный [module/activeEffect/WitcherActiveEffectSheet.js](../../../../../../module/activeEffect/WitcherActiveEffectSheet.js). Он наследует core ActiveEffectConfig, добавляет actions.wizard, PARTS.systemSpecific и TABS.sheet.systemSpecific; остальные части/submit остаются ядровыми. Присоединены baseMixin (8 методов) и temporaryItemImprovementMixin (2). Регистрация не ограничена отдельными types, поэтому шаблон системных полей должен учитывать разные схемы (issue-00053).

[Общая сверка первой серии](../../../review-log.md) — TASK-0003.010. Полный клиент и БД не запускались.

## Уточнение TASK-0003.011

2026-09-10, `07237960627bf7debc2b4283aa55d1a8c5d1bb8b`; содержимое исходника совпадает с предыдущим срезом.

Полностью разобраны [общий лист Item](../item/sheets/WitcherItemSheet.js.md) и [его базовая конфигурация](../item/sheets/configurations/WitcherConfigurationSheet.js.md). У общего листа 17 прямых наследников, у конфигурации — три прямых и два через Properties. Для note нет специализированной регистрации: после перехвата исходных регистраций подходящим остаётся WitcherItemSheet, а настоящий HandlebarsApplicationMixin рендерит ноль частей. Это [issue-00057](../../../../../issues/potential/issue-00057.md), отдельное наблюдение от отсутствующих типов issue-00005. Runtime-проверка не моделировала пользовательский выбор листа и БД.

[TASK-0003.011 — сценарии и сверка](../../../review-log.md#task-0003011).

## Уточнение TASK-0003.013

2026-09-10, `8cca18e14b75ec53028ee6bc49a837597de4d9af`; исходник неизменен. [Перекрёстная сверка](../../../review-log.md#task-0003013).

Полностью разобран зарегистрированный [module/item/sheets/WitcherWeaponSheet.js](../../../../../../module/item/sheets/WitcherWeaponSheet.js): MAIN-шаблон оружия, экземпляр общей конфигурации боевых свойств, контекст навыков, слушатели видов урона и примесь связанного рецепта. Регистрация не изменена. [module/item/sheets/configurations/WitcherPropertiesConfigurationSheet.js](../../../../../../module/item/sheets/configurations/WitcherPropertiesConfigurationSheet.js) является окном конфигурации, создаваемым листом, а не отдельным типом Item.

## Уточнение TASK-0003.014

2026-09-10, `0fa589bd300856ff309f362afcb66d6fa43401ab`; исходник неизменен. [Перекрёстная сверка](../../../review-log.md#task-0003014).

Полностью описаны [module/item/sheets/WitcherArmorSheet.js](../../../../../../module/item/sheets/WitcherArmorSheet.js), [module/item/sheets/WitcherEnhancementSheet.js](../../../../../../module/item/sheets/WitcherEnhancementSheet.js) и конфигурация брони. Регистрации Item.armor/Item.enhancement не менялись. Armor открывает специализированную конфигурацию общих свойств, Enhancement сохраняет базовую. Все три новых HBS разобраны; сторонние листы и V1 инвентарь не получили статуса полного анализа.

## Уточнение TASK-0003.015

2026-09-10, `7edb814aa870da75c7ad7633536e899a8d07e205`; исходник неизменен. [Перекрёстная сверка](../../../review-log.md#task-0003015).

Полностью разобраны регистрации трёх специализированных ItemSheet: [module/item/sheets/WitcherAlchemicalSheet.js](../../../../../../module/item/sheets/WitcherAlchemicalSheet.js), [module/item/sheets/WitcherMutagenSheet.js](../../../../../../module/item/sheets/WitcherMutagenSheet.js), [module/item/sheets/WitcherValuableSheet.js](../../../../../../module/item/sheets/WitcherValuableSheet.js). Выбор конкретной configuration задаёт экземпляр листа: у Alchemical/Valuable она расходуемая, у Mutagen базовая. В изолированных контекстах получены 3/2/3 вкладки. Пользовательские переопределения листов и сторонние модули не исследовались.
