# module/actor/sheets/configurations/WitcherMonsterConfigurationSheet.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/actor/sheets/configurations/WitcherMonsterConfigurationSheet.js](../../../../../../../../module/actor/sheets/configurations/WitcherMonsterConfigurationSheet.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `8b938d44a042749df027d8b58e28bb1d79638091` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.032](../../../../../../../tasks/task-0003.032.md), 13 файлов, 973 логические строки |
| Запись перекрёстной сверки | [TASK-0003.032](../../../../../review-log.md#task-0003032) |

## Назначение файла

Окно настройки монстра: общие параметры, пользовательские максимумы и флаги видимости встроенных навыков. Полностью прочитана 91 строка; собственные методы только _prepareContext и _getSkills.

## Условия использования

Не регистрируется отдельным default Actor-листом. Создаётся полем configuration в WitcherMonsterSheet; открывается базовым _renderConfigureDialog через .configure-actor. Наследует HandlebarsApplicationMixin(ActorSheetV2); поля сохраняет общая форма ядра при submitOnChange=true/closeOnSubmit=false.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| WitcherMonsterConfigurationSheet | default class: 4 | ActorSheetV2 | new в MonsterSheet: 109 | Работает с тем же Actor |
| DEFAULT_OPTIONS | 6 | 520×480, witcher/extended-sheet/actor | Foundry merge | Автосохранение, окно не закрывается |
| PARTS | 18 | header/tabs/general/skills | 4 части | Три HBS системы и core navigation |
| TABS.primary | 36 | general и skills, initial general | Единственная группа | Core Application._prepareContext автоматически готовит tabs |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| _prepareContext; 45 | options,this.document | Promise<context> | await super; context.config=CONFIG.WITCHER; создаёт statLabels из statMap.label??labelShort; system/systemFields/skillConfig | config — общая ссылка: запись statLabels меняет CONFIG.WITCHER в памяти; Actor не обновляется здесь |
| _getSkills; 65 | CONFIG.WITCHER.statMap/skillMap, actor.system.schema | объект групп навыков | Выбирает stat.origin==='stats'; для каждого ключа skillMap той же attribute.name получает поле skills/attribute/key/isVisible и текущее значение; удаляет пустые группы | 52 записи; ключ commonspeech не совпадает с commonsp, поэтому field/value undefined; комментарий про NumberField/value устарел — возвращаются BooleanField/isVisibleValue |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| ActorSheetV2/HandlebarsApplicationMixin; форма/вкладки | Foundry 14.367.0; application.mjs: 691–727, document-sheet.mjs: 172–183/464–469/525 | наследование | Контекст document/tabs и запись формы | Настоящие тела _prepareTabs/_getTabsConfig; каркас Document/Application заменён |
| statMap/skillMap, label/labelShort | [module/setup/config.js](../../../../../../../../module/setup/config.js) | глобальные данные | _prepareContext/_getSkills | Map ключи и поля моделей сверены |
| MonsterData, CommonActorData, Skill | [module/data/actor/monsterData.js](../../../../../../../../module/data/actor/monsterData.js); [module/data/actor/commonActorData.js](../../../../../../../../module/data/actor/commonActorData.js); [module/data/actor/templates/common/skills/skillData.js](../../../../../../../../module/data/actor/templates/common/skills/skillData.js) | модель/schema/getField | systemFields, 52 записи настройки | Fresh isVisible=false, label исходно undefined; Bool меняется при повторной подготовке |
| general/header/skillConfiguration | [templates/sheets/actor/configuration/monster/header.hbs](../../../../../../../../templates/sheets/actor/configuration/monster/header.hbs); [templates/sheets/actor/configuration/monster/general.hbs](../../../../../../../../templates/sheets/actor/configuration/monster/general.hbs); [templates/sheets/actor/configuration/partials/skillConfiguration.hbs](../../../../../../../../templates/sheets/actor/configuration/partials/skillConfiguration.hbs) | HBS пути | PARTS | 10 общих input либо 13 при customStat; 51 checkbox навыков |
| foundry.utils.getProperty | Foundry 14.367.0 common/utils | динамический доступ | isVisibleValue | Строковый путь по ключу skillMap |
| Локализация | [lang/en.json](../../../../../../../../lang/en.json); [lang/ru.json](../../../../../../../../lang/ru.json) | labelPrefix/поля | Actor.settings и model labels | expandObject + настоящий fallback |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/actor/sheets/WitcherMonsterSheet.js](../../../../../../../../module/actor/sheets/WitcherMonsterSheet.js) | default class и экземпляр | configuration: 109 | Базовый _renderConfigureDialog открывает |
| [templates/sheets/actor/configuration/monster/header.hbs](../../../../../../../../templates/sheets/actor/configuration/monster/header.hbs) | контекст окна | PARTS.header | Локализованный заголовок |
| [templates/sheets/actor/configuration/monster/general.hbs](../../../../../../../../templates/sheets/actor/configuration/monster/general.hbs) | system/systemFields/tabs | PARTS.general | Сохранение общих параметров |
| [templates/sheets/actor/configuration/partials/skillConfiguration.hbs](../../../../../../../../templates/sheets/actor/configuration/partials/skillConfiguration.hbs) | skillConfig/config.statLabels | PARTS.skills | BooleanField.toFormGroup |

Область поиска: module/ и templates/ текущего checkout; прямые импорты и места вызова сверены отдельно от динамических обращений. Типы и листы сверены с system.json, module/setup/registerDataModels.js и module/setup/registerSheets.js. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

В подготовке меняется только общий CONFIG.WITCHER.statLabels и контекст. Изменение значений формы передаётся унаследованному обработчику DocumentSheet; отдельного _updateObject или submit handler нет. Изменение isVisible в модели отражается повторным _getSkills, но текущая общая вкладка навыков не фильтрует по нему. Для category/threat/difficulty/bounty нет formGroup или других редакторов.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Поля/группы | 03 | 52 записи, 51 поле, commonspeech undefined; флаг awareness true→false отражён новым контекстом | Предупреждение formGroup о пропавшем поле ожидаемо |
| Общая форма | 04–05 | 10/13 input; payload customStat/maxima/flags принят MonsterData.updateSource; max HP90/STA70/resolve80 сохранены при customStat | DOM/createInput фасады, БД не запускается |
| Открытие | 14 | Базовый action открывает именно configuration | render перехвачен |

## Непроверенные участки и открытые вопросы

Файл прочитан целиком. Мир, браузер, HTTP-доступ, Document.update и работа нескольких клиентов не запускались. Настоящие модели, Handlebars, core helpers и вычисления использовались с фасадами Application/DOM и перехватом записи; подробные границы — в журнале .032. CSS и ресурсы проверены только как зависимости, соседние файлы вне порции не засчитываются в покрытие.

## Связанные проблемы

[issue-00004](../../../../../../../issues/potential/issue-00004.md), [issue-00015](../../../../../../../issues/potential/issue-00015.md), [issue-00018](../../../../../../../issues/potential/issue-00018.md), [issue-00032](../../../../../../../issues/potential/issue-00032.md), [issue-00192](../../../../../../../issues/potential/issue-00192.md), [issue-00209](../../../../../../../issues/potential/issue-00209.md). Это конфигурация видимости/общих полей, отличная от WitcherModifiersConfiguration. Новых исправлений нет.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `8b938d44a042749df027d8b58e28bb1d79638091`; полный файл | Первая карточка; [сверка порции](../../../../../review-log.md#task-0003032) |
