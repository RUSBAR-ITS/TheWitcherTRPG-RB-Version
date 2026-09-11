# templates/partials/monster/monster-skill-tab.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/partials/monster/monster-skill-tab.hbs](../../../../../../../templates/partials/monster/monster-skill-tab.hbs) |
| Тип файла | Handlebars |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `273a6d7db0b7c866399db3ecd4f7191817ae6f10` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.029](../../../../../../tasks/task-0003.029.md), 14 файлов, 763 логических строк |
| Запись перекрёстной сверки | [TASK-0003.029](../../../../review-log.md#task-0003029) |

## Назначение файла

Старый табличный список навыков монстра: семь фиксированных групп, раскрытие по pannels, встроенные и собственные строки.

## Условия использования

Единственный найденный буквальный родитель — templates/sheets/actor/monster-sheet.hbs. Он предзагружается, но текущий WitcherMonsterSheet.PARTS.skills использует character/tab-skills.hbs. Поиск module/templates и регистрации листов не обнаружил активного подключения старого родителя как текущего листа; preload не доказывает его использование.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| Две колонки / семь .skill | Весь HBS, 141 строка | Группы int/ref/dex/body/emp/cra/will | data-skilltype для старого обработчика | Для каждой свой pannels.<stat>IsOpen |
| skill-display / таблица | Повторённый блок каждой группы | Переключение шеврона и класса invisible | Click связывается sheet/skillMixin | Каждая таблица перебирает system.skills.<stat> и customSkills.<stat> |

## Основные функции и методы

Собственных функций нет. Семь пар if/else выбирают шеврон и семь условий class скрывают таблицы. Встроенному partial передаются skill/name/stat с буквальным stat; собственному — текущий Item без hash. Всего 14 partial-вызовов к двум различным файлам.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| Встроенная строка | [templates/partials/monster/monster-skill-display.hbs](../../../../../../../templates/partials/monster/monster-skill-display.hbs) | Буквальный partial, семь вызовов | Поля модели встроенного навыка и isVisible | Каждая группа |
| Собственная строка | [templates/partials/monster/monster-custom-skill-display.hbs](../../../../../../../templates/partials/monster/monster-custom-skill-display.hbs) | Буквальный partial, семь вызовов | Embedded Item из customSkills | Каждая группа |
| Skills / Pannels | [module/data/actor/templates/common/skills/skillsData.js](../../../../../../../module/data/actor/templates/common/skills/skillsData.js); [module/data/actor/templates/character/pannelsData.js](../../../../../../../module/data/actor/templates/character/pannelsData.js) | Данные system | Семь групп и intIsOpen/refIsOpen/dexIsOpen/bodyIsOpen/empIsOpen/craIsOpen/willIsOpen | Имена полей в условиях и циклах |
| _prepareCustomSkills | [module/actor/sheets/WitcherActorSheetV1.js](../../../../../../../module/actor/sheets/WitcherActorSheetV1.js); [module/actor/sheets/WitcherActorSheet.js](../../../../../../../module/actor/sheets/WitcherActorSheet.js) | Проверенные производители контекста | Группировка Item type skill по attribute | Определения обоих базовых листов; не регистрация старого родителя |
| _onSkillDisplay | [module/actor/sheets/mixins/skillMixin.js](../../../../../../../module/actor/sheets/mixins/skillMixin.js) | Событие DOM | skill-display и ближайший skilltype → pannels | Селектор и динамический путь update |
| localize / preload | [module/setup/handlebars.js](../../../../../../../module/setup/handlebars.js) | Core helper и список предзагрузки | WITCHER.Actor.Skill.Intelligence/Reflex/Dexterity/Body/Empathy/Crafting/Willpower | Все семь ключей присутствуют в lang/en.json и lang/ru.json как dotted keys; исправлено в TASK-0003.030 |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [templates/sheets/actor/monster-sheet.hbs](../../../../../../../templates/sheets/actor/monster-sheet.hbs) | Весь HBS | Старый literal partial во вкладке skills | Строка 289; текущий V2 PARTS не использует этого родителя |
| [module/setup/handlebars.js](../../../../../../../module/setup/handlebars.js) | Весь HBS | Предзагрузка | Буквальная ссылка; не активная регистрация листа |

Область поиска: module/ и templates/ текущего checkout; прямые импорты и места вызова сверены отдельно от динамических обращений. Типы и листы сверены с system.json, module/setup/registerDataModels.js и module/setup/registerSheets.js. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

HBS только читает system.pannels и два набора навыков. Переключение делегирует update Actor. Сам не хранит флаги видимости и значения Item. Групп spd/luck нет; это свойство старого списка, актуальная проблема группировки подтверждена отдельно на действующем общем HBS.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Полный список и потребители | 141 строка; rg ссылки, PARTS и registerSheets | Семь групп, 14 вызовов, два partial; активный V2 путь иной | Внешние макросы и сторонние листы не исследованы |
| Настоящий Handlebars | Полный старый родительский partial со Skill и Item, pannels true/false | Семь таблиц; классы/шевроны следуют pannels; собственный Item получает нужный ID | Рендер изолирован; не заявление о текущем пользовательском окне |
| Локализация | Точный lookup семи ключей в en/ru | Прежний вывод об отсутствии отозван: после expandObject все семь найдены в en/ru | Прочие языки и runtime-переводы модулей не проверялись |

## Непроверенные участки и открытые вопросы

Данный файл не объявляется удалённым или полностью недостижимым: найден старый HBS-потребитель. Доказано отсутствие его выбора в исследованном текущем V2 маршруте. Не производилась очистка старых шаблонов.

## Связанные проблемы

[issue-00188](../../../../../../issues/potential/issue-00188.md), [issue-00193](../../../../../../issues/potential/issue-00193.md). Для отсутствующих групп есть сопоставление с текущим UI; прежнее утверждение о языковых пропусках старого маршрута отозвано после проверки expandObject.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `273a6d7db0b7c866399db3ecd4f7191817ae6f10`; полный файл | Первая карточка; [сверка порции](../../../../review-log.md#task-0003029) |

## Уточнение TASK-0003.030

2026-09-11, `aa6af106e86a9c75fe050d599f961c8fadb74f1b`. Исправлена языковая часть проверки .029: Foundry сначала выполняет expandObject словаря. Семь WITCHER.Actor.Skill.* присутствуют в en/ru в виде dotted ключей; утверждение об их отсутствии отозвано. Остальные выводы о старом родителе и невыбранном текущими V2 PARTS пути сохраняются. Повторены 22 сценария .029 с корректной локализацией, все прошли.

Сверенные источники: [templates/dialog/deprecations/statSkillModifiers.hbs](../../../../../../../templates/dialog/deprecations/statSkillModifiers.hbs); [module/setup/handlebars.js](../../../../../../../module/setup/handlebars.js). [Итоговая сверка третьей серии, сценарии и ограничения](../../../../review-log.md#task-0003030). Код и статусы проблем не менялись.

## Уточнение TASK-0003.032

2026-09-11, `8b938d44a042749df027d8b58e28bb1d79638091`. Полностью разобран внешний старый monster-sheet.hbs, который подключает эту вкладку: 289. Сам старый лист найден только в preload, не в текущем PARTS. Изолированный полный render подтверждает совместимость выбранного контекста/частей, не достижимость V1 в клиенте.

Связи: [templates/sheets/actor/monster-sheet.hbs](../../sheets/actor/monster-sheet.hbs.md). [Результаты и пределы проверки](../../../../review-log.md#task-0003032).
