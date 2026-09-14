# templates/partials/character/tab-magic.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/partials/character/tab-magic.hbs](../../../../../../../templates/partials/character/tab-magic.hbs) |
| Тип файла | Handlebars |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `c598d74e34f4be51535de78b38f0601c286c5407` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.039](../../../../../../tasks/task-0003.039.md), 6 файлов, 870 логических строк |
| Запись перекрёстной сверки | [TASK-0003.039](../../../../review-log.md#task-0003039) |

## Назначение файла

Общая вкладка магии текущих листов персонажа и монстра: шесть вложенных вкладок, двенадцать включений списков и настройки vigor, магических IP и четырёх фокусов.

## Условия использования

WitcherCharacterSheet.PARTS.magic и WitcherMonsterSheet.PARTS.magic ссылаются на этот путь. module/setup/handlebars.js предзагружает HBS. Требует tabs.magic и magicTabs, подготовленные листом; списки даёт WitcherActorSheet._prepareSpells. Это живой маршрут монстра, несмотря на character в пути.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| section[data-tab=magic] | Строка 1 | Основная вкладка | group primary | cssClass от tabs.magic |
| magicTabs/all, magic, rituals, hexes, magicalGift, focus | nav и шесть секций | Вложенные вкладки | data-action=tab, data-group=magicTabs | all дублирует содержимое специализированных списков в отдельном DOM |
| Двенадцать включений spell-type-list | Строки 10–41 | Шесть групп на all и шесть в отдельных секциях | Partial с spells,itemType,spellType,header | Spells/Invocations/Witcher объединяются по уровню |
| Десять input | Строки 47–77 | vigor.unmodifiedMax, magicImprovementPoints, focus1–4.name/value | name=system.* | Автосохранение формы листа; без своих обработчиков |

## Основные функции и методы

Собственных функций JavaScript нет. each создаёт навигацию, partial-включения создают списки. concat/localize строят заголовки; переключение вкладок и сохранение выполняют внешние методы.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| Контекст вкладок/PARTS | [module/actor/sheets/WitcherCharacterSheet.js](../../../../../../../module/actor/sheets/WitcherCharacterSheet.js); [module/actor/sheets/WitcherMonsterSheet.js](../../../../../../../module/actor/sheets/WitcherMonsterSheet.js) | Прямые потребители HBS / источник контекста | TABS.magicTabs, _prepareContext | Оба текущих класса выбирают этот шаблон |
| _prepareSpells / getList | [module/actor/sheets/WitcherActorSheet.js](../../../../../../../module/actor/sheets/WitcherActorSheet.js); [module/actor/witcherActor.js](../../../../../../../module/actor/witcherActor.js) | Списки | noviceSpells,journeymanSpells,masterSpells,rituals,hexes,magicalgift | getList исключает isStored и сортирует sort; три класса + точный lowercase level |
| spell-type-list.hbs | [templates/sheets/actor/partials/character/spell-type-list.hbs](../../../../../../../templates/sheets/actor/partials/character/spell-type-list.hbs) | Двенадцать literal partial-включений | Данные строк и кнопки добавления | spells и itemType задаются явно; spellType наследуется следующим partial |
| CommonActorData / focus / CharacterData | [module/data/actor/commonActorData.js](../../../../../../../module/data/actor/commonActorData.js); [module/data/actor/templates/common/focusData.js](../../../../../../../module/data/actor/templates/common/focusData.js); [module/data/actor/characterData.js](../../../../../../../module/data/actor/characterData.js); [module/data/actor/monsterData.js](../../../../../../../module/data/actor/monsterData.js) | Схемы полей | derivedStats.vigor.unmodifiedMax/max; focus1–4; magic.magicImprovementPoints | magic определён CharacterData; у MonsterData этого поля нет, хотя общий шаблон его выводит |
| castSpell / calcStaminaMulti | [module/actor/mixins/castSpellMixin.js](../../../../../../../module/actor/mixins/castSpellMixin.js) | Косвенный потребитель фокусов | Использование положительных focus.value | Вкладка хранит фокусы; стоимость определяется при каждом cast |
| Предзагрузка/помощники | [module/setup/handlebars.js](../../../../../../../module/setup/handlebars.js) | preloadHandlebarsTemplates/registerHandelbarHelpers | Путь загружается заранее | localize/concat относятся к ядру |
| Локализация/ресурсы | [lang/en.json](../../../../../../../lang/en.json); [lang/ru.json](../../../../../../../lang/ru.json) | Подписи | localize, динамический concat, изображения Item | Настоящие expandObject/Localization; пользовательские img и Font Awesome, без исследования assets |
| Tab action / submitOnChange | Foundry 14.367 ApplicationV2/DocumentSheetV2 | Внешний UI API | data-action=tab, name-поля формы | Фасад формы; реальный submit и права не проверены |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/actor/sheets/WitcherCharacterSheet.js](../../../../../../../module/actor/sheets/WitcherCharacterSheet.js) | PARTS.magic | Текущий character | Литеральный template |
| [module/actor/sheets/WitcherMonsterSheet.js](../../../../../../../module/actor/sheets/WitcherMonsterSheet.js) | PARTS.magic | Текущий monster | Тот же путь |
| [module/setup/handlebars.js](../../../../../../../module/setup/handlebars.js) | HBS | preloadHandlebarsTemplates | Предзагрузка |

Область поиска: module/ и templates/ текущего checkout; прямые импорты и места вызова сверены отдельно от динамических обращений. Типы и листы сверены с system.json, module/setup/registerDataModels.js и module/setup/registerSheets.js. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Контекст: tabs.magic.cssClass; magicTabs[*].id/label/cssClass; шесть массивов магии. Вкладка all содержит novice/journeyman/master spell, ritual, hex и MagicalGift; специализированные вкладки повторяют строки. itemType: spell/ritual/hex; spellType: spellNovice/spellJourneyman/spellMaster/magicalgift, для ritual/hex не задаётся. Новые Item создаёт вложенный summary и itemMixin, не сам HBS.

Поля: system.derivedStats.vigor.unmodifiedMax (type=number,data-dtype=Number), рядом вычисленный system.derivedStats.vigor.max; system.magic.magicImprovementPoints (number); system.focus1.name/value, focus2.name/value, focus3.name/value, focus4.name/value (text). Подсказки имён First/Second/Third/Fourth Focus буквальные английские. У монстра поле magicImprovementPoints не соответствует его схеме; сохранение через браузер в этой порции не проверялось. Ни vigor, ни IP не расходуются кодом этой вкладки. Изучение заклинаний здесь не реализовано отдельным действием.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Группировка и дублирование | Группы 03–04 | 12 применений для 12 видимых Item дают 24 кнопки в all+специализированных секциях; пустые группы остаются | Скрытие CSS в браузере не проверено |
| Добавление | Группа 05 | spellType доходит через наследуемый контекст summary; payload class Spells/level novice | Item.create заменён |
| Фокусы/стоимость | Группы 06/08/28 | Числовые значения из селектов применяются при cast | Ни вкладка, ни фокус не доказывают право второго фокуса по книге |

## Непроверенные участки и открытые вопросы

Исходник и указанные связи сопоставлены в TASK-0004.009. Полный browser lifecycle, изменение focus/vigor/магического IP и layout не запускались. Отсутствующее у Monster поле IP остаётся смежным наблюдением. Остаток: [U009-01](../../../../cross-check-0002.md#u009-01), [U009-02](../../../../cross-check-0002.md#u009-02), [U009-07](../../../../cross-check-0002.md#u009-07). Новых поведенческих запусков нет; прежние протоколы сохраняют даты и фасады.

## Связанные проблемы

[issue-00192](../../../../../../issues/potential/issue-00192.md). Общая вкладка дополнительно показывает магические IP, которых нет в схеме монстра; связь уточнена в прежней issue-00192 о полях развития персонажа в UI монстра. Браузерная запись этого поля не проверялась.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `c598d74e34f4be51535de78b38f0601c286c5407`; полный файл | Первая карточка; [сверка порции](../../../../review-log.md#task-0003039) |

## Сквозная сверка TASK-0004.009

2026-09-14; rusbar-main, 7adc2362937779de0c03957aacf73ff2cf13e211. Исходник совпадает со срезом TASK-0001; изменено только описание.

Текущие Character/Monster выбирают общий magic PART. Он включает spell-type-list двенадцать раз (шесть групп all и специальные вкладки), показывает focus/vigor и magicImprovementPoints. Вложенный контекст сохраняет spellType для add Item; старый monster partial не подменяет этот маршрут.

Сопоставленные определения и потребители: [module/actor/sheets/WitcherCharacterSheet.js](../../../module/actor/sheets/WitcherCharacterSheet.js.md), [module/actor/sheets/WitcherMonsterSheet.js](../../../module/actor/sheets/WitcherMonsterSheet.js.md), [module/actor/sheets/WitcherActorSheet.js](../../../module/actor/sheets/WitcherActorSheet.js.md), [module/actor/witcherActor.js](../../../module/actor/witcherActor.js.md), [templates/sheets/actor/partials/character/spell-type-list.hbs](../../sheets/actor/partials/character/spell-type-list.hbs.md), [module/data/actor/commonActorData.js](../../../module/data/actor/commonActorData.js.md), [module/data/actor/templates/common/focusData.js](../../../module/data/actor/templates/common/focusData.js.md), [module/data/actor/characterData.js](../../../module/data/actor/characterData.js.md), [module/data/actor/monsterData.js](../../../module/data/actor/monsterData.js.md), [module/actor/mixins/castSpellMixin.js](../../../module/actor/mixins/castSpellMixin.js.md), [module/setup/handlebars.js](../../../module/setup/handlebars.js.md), [lang/en.json](../../../lang/en.json.md), [lang/ru.json](../../../lang/ru.json.md).

[Протокол и границы](../../../../review-log.md#task-0004009) — TASK-0004.009; процессы [R009-07](../../../../cross-check-0002.md#r009-07). В этой порции выполнена статическая сверка; прежние опыты сохраняют свои даты и фасады. Новых поведенческих запусков нет; браузер, мир, сеть и запись в БД не запускались.
