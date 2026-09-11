# templates/sheets/actor/partials/monster/header.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/sheets/actor/partials/monster/header.hbs](../../../../../../../../../templates/sheets/actor/partials/monster/header.hbs) |
| Тип файла | Handlebars |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `8b938d44a042749df027d8b58e28bb1d79638091` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.032](../../../../../../../../tasks/task-0003.032.md), 13 файлов, 973 логические строки |
| Запись перекрёстной сверки | [TASK-0003.032](../../../../../../review-log.md#task-0003032) |

## Назначение файла

Заголовок текущего монстра: редактируемое имя, текстовые категория/угроза/сложность, настройки, броски, экспорт добычи и счётчик спасбросков.42 строки прочитаны полностью.

## Условия использования

Выбран PARTS.header MonsterSheet; также предзагружается. Содержит одно именованное поле name, остальные сведения читаются из MonsterData.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| .monster-header/input.charname | 2–7 | Имя Actor и кнопка настройки | name/actor.name, .configure-actor | Имя экранируется; клику настройки соответствует базовый _renderConfigureDialog |
| .monster-general | 8–20 | Категория/угроза/сложность | system.category/threat/difficulty | Type.<category>, lookup monsterDifficulty/monsterComplexity; редакторов здесь нет |
| .monster-button-list | 23–31 | Броски и экспорт | init-roll/death-roll/crit-roll/verbal-button/export-loot | verbal условен, exportLoot — data-action |
| .death-section | 33–40 | deathSaves и reset/add | death-minus/death-plus | Подсказки Reset/Add буквальные; счётчик не ограничен 9 как в старой разметке |

## Основные функции и методы

Программных функций и экспортов нет. Ниже описаны поля/условия разметки и их контракт с моделями и обработчиками; собственной записи документа файл не выполняет.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| MonsterData и CommonActorData | [module/data/actor/monsterData.js](../../../../../../../../../module/data/actor/monsterData.js); [module/data/actor/commonActorData.js](../../../../../../../../../module/data/actor/commonActorData.js) | модель/поля | system и systemFields | Пути сверены с определениями, использованы настоящие модели |
| Контекст листа | [module/actor/sheets/WitcherMonsterSheet.js](../../../../../../../../../module/actor/sheets/WitcherMonsterSheet.js); [module/actor/sheets/WitcherActorSheet.js](../../../../../../../../../module/actor/sheets/WitcherActorSheet.js) | PARTS/подготовка | actor/document/system, опции, записи enrichedText | Полный _prepareContext выполнен с Application-фасадом |
| helpers и переводы | [module/setup/handlebars.js](../../../../../../../../../module/setup/handlebars.js); [lang/en.json](../../../../../../../../../lang/en.json); [lang/ru.json](../../../../../../../../../lang/ru.json) | Handlebars/локализация | localize, concat, eq/gte, checked, selectOptions, formGroup/editor по месту | Системные helpers и core helpers сверены; DOM-элементы формы заменены |
| DEFAULT_OPTIONS.actions.exportLoot | [module/actor/sheets/WitcherMonsterSheet.js](../../../../../../../../../module/actor/sheets/WitcherMonsterSheet.js) | action | export-loot: 30 | Скопированный Actor обрабатывается отдельным методом |
| Init/crit/verbal; configure | [module/actor/sheets/WitcherActorSheet.js](../../../../../../../../../module/actor/sheets/WitcherActorSheet.js) | click | Действия заголовка | activateListeners; методов собственного header нет |
| deathSaveListener/_onDeathSaveRoll/_removeDeathSaves/_addDeathSaves | [module/actor/sheets/mixins/deathSaveMixin.js](../../../../../../../../../module/actor/sheets/mixins/deathSaveMixin.js) | click | death-roll/minus/plus | minus сбрасывает весь счётчик |
| MonsterTypes/monsterDifficulty/monsterComplexity | [module/setup/config.js](../../../../../../../../../module/setup/config.js) | словари | Подписи | 12 категорий; 4 уровня угрозы; 3 сложности |
| CSS-селекторы | [styles/monster/header.css](../../../../../../../../../styles/monster/header.css) | оформление | .monster-header/.monster-general/.monster-actions | Прочитаны нужные селекторы; полный CSS вне порции |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/actor/sheets/WitcherMonsterSheet.js](../../../../../../../../../module/actor/sheets/WitcherMonsterSheet.js) | HBS header | PARTS.header | Путь/обращение сверены в исходнике |
| [module/setup/handlebars.js](../../../../../../../../../module/setup/handlebars.js) | путь HBS | preloadHandlebarsTemplates | Путь/обращение сверены в исходнике |
| [module/actor/sheets/WitcherActorSheet.js](../../../../../../../../../module/actor/sheets/WitcherActorSheet.js) | селекторы | activateListeners | Путь/обращение сверены в исходнике |
| [module/actor/sheets/mixins/deathSaveMixin.js](../../../../../../../../../module/actor/sheets/mixins/deathSaveMixin.js) | death-* | deathSaveListener | Путь/обращение сверены в исходнике |

Область поиска: module/ и templates/ текущего checkout; прямые импорты и места вызова сверены отдельно от динамических обращений. Типы и листы сверены с system.json, module/setup/registerDataModels.js и module/setup/registerSheets.js. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

name сохраняет общая форма; счётчики и действия обслуживаются JS. Пустые threat/difficulty дают пустые подписи через lookup/localize; category имеет начальное Humanoid. Наличие exportLoot не является обходом прав Actor.create ядра; реальные права не проверены.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Имя/сведения/опции | 06 | Экранировано <Name>, Vampire/hard/complex переведены; один input; verbal true/false | Рендер Handlebars без браузера |
| События | 14 | configure/death listeners присутствуют, export action определён в классе | Привязка DOM фасадом |

## Непроверенные участки и открытые вопросы

Файл прочитан целиком. Мир, браузер, HTTP-доступ, Document.update и работа нескольких клиентов не запускались. Настоящие модели, Handlebars, core helpers и вычисления использовались с фасадами Application/DOM и перехватом записи; подробные границы — в журнале .032. CSS и ресурсы проверены только как зависимости, соседние файлы вне порции не засчитываются в покрытие.

## Связанные проблемы

[issue-00209](../../../../../../../../issues/potential/issue-00209.md). Исправления не выполнялись; вывод ограничен указанными проверками.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `8b938d44a042749df027d8b58e28bb1d79638091`; полный файл | Первая карточка; [сверка порции](../../../../../../review-log.md#task-0003032) |
