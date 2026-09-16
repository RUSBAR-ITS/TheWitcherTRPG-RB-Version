# templates/partials/character/tab-profession.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/partials/character/tab-profession.hbs](../../../../../../../templates/partials/character/tab-profession.hbs) |
| Тип файла | Handlebars |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `b47ba02cdaebc6a66ad14a5638213b6eb24460b4` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.038](../../../../../../tasks/task-0003.038.md), 4 файла, 965 логических строк |
| Запись перекрёстной сверки | [TASK-0003.038](../../../../review-log.md#task-0003038) |

## Назначение файла

Вкладка персонажа с десятью навыками первой профессии, её заметками и блоком расы: четыре особенности и пять региональных социальных отношений.

## Условия использования

CharacterSheet.PARTS.profession и старый preloadHandlebarsTemplates. Контекст profession/race берётся из getList()[0]; вкладка primary/profession. Редактируемые data-field относятся к вложенному Item, а не Actor.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| section.tab | 1 | Контейнер primary/profession | tabs.profession.cssClass | Рендер active вкладки |
| profession / definingSkill / skillPath1–3 | 2–247 | Определяющий навык и 9 ячеек ветвей | 30 inline-edit полей | skillName/stat/level; путь поля устойчивый, бросок по имени |
| editors профессии | 29–237 | 11 описаний: definingSkill,notes,9 ветвей | target profession.system.*; editable=false | Исходный HTML, без enrichedText |
| race/perk1–4/socialStanding | 252–330 | Особенности расы и отношения | 4editor и 5select | Контекст отдельного Item.race |
| .add-item/.item-edit/.item-delete | Header/пустые блоки | Создание/правка/удаление профессии или расы | Item listeners | item контейнер задаёт data-item-id |

## Основные функции и методы

JavaScript-функций нет. if/unless разделяют наличие Item; десять unless(eq stat "none") скрывают бросок только для none, а не для пустого/неизвестного stat или level0. selectOptions использует config.statTypes/socialStanding. editor получает исходный HTML; localize — подписи. Нет UI выбора threshold, attack/self/target/стоимости: их настраивает отдельный Item-редактор.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| Контекст profession/race/tabs/config/enrichedText | [module/actor/sheets/WitcherCharacterSheet.js](../../../../../../../module/actor/sheets/WitcherCharacterSheet.js) | PARTS/context | _prepareCharacterData154–167 | В HBS enrichedText не читается |
| Базовый render/обработчики | [module/actor/sheets/WitcherActorSheet.js](../../../../../../../module/actor/sheets/WitcherActorSheet.js) | Наследование листа | activateListeners и context.editable | Этот HBS сам события не регистрирует |
| ProfessionData/professionSkill/professionPath | [module/data/item/professionData.js](../../../../../../../module/data/item/professionData.js); [module/data/item/templates/professionSkillData.js](../../../../../../../module/data/item/templates/professionSkillData.js); [module/data/item/templates/professionPathData.js](../../../../../../../module/data/item/templates/professionPathData.js) | Схема Item | Все 30data-field | definingSkill.{skillName,stat,level}; skillPath1–3.skill1–3.{skillName,stat,level} |
| RaceData | [module/data/item/raceData.js](../../../../../../../module/data/item/raceData.js) | Схема Item | perk1–4; socialStanding.{north,nilfgaard,skellige,dolBlathanna,mahakam} | 4editor+5select |
| itemMixin._onItemInlineEdit/itemListeners | [module/actor/sheets/mixins/itemMixin.js](../../../../../../../module/actor/sheets/mixins/itemMixin.js) | События/запись | closest .item, dataset.field, element.value | Пишет item.update; строки false/true особая ветка |
| skillListener | [module/actor/sheets/mixins/skillMixin.js](../../../../../../../module/actor/sheets/mixins/skillMixin.js) | Click | profession-roll→Actor._onProfessionRoll | Читает data-name через примесь Actor |
| professionMixin | [module/actor/mixins/professionMixin.js](../../../../../../../module/actor/mixins/professionMixin.js) | Поведение броска | Поиск по имени, не по inline path | Одноимённые навыки могут перенаправить бросок |
| statTypes/socialStanding | [module/setup/config.js](../../../../../../../module/setup/config.js) | Select options | Все stat и регионы | Переводы значений |
| preloadHandlebarsTemplates | [module/setup/handlebars.js](../../../../../../../module/setup/handlebars.js) | Загрузка HBS | Прямой список preload:11 | Также PARTS CharacterSheet |
| editor/selectOptions/localize/eq/if/unless | Foundry14.367.0 и Handlebars4.7.9 | Helpers | Рендер ветвей и HTML | Реальные helpers с фасадом editor DOM |
| Переводы | [lang/en.json](../../../../../../../lang/en.json); [lang/ru.json](../../../../../../../lang/ru.json) | Локализация | WITCHER.Notes/Actor.Perks/Adda/socialStanding | expandObject+fallback |
| CSS | [styles/profession-sheet.css](../../../../../../../styles/profession-sheet.css); [styles/character/tab-profession.css](../../../../../../../styles/character/tab-profession.css); [styles/witcher-styles.css](../../../../../../../styles/witcher-styles.css) | Стили | Карточки/цветные пути/числа/иконки | Подключены @import |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/actor/sheets/WitcherCharacterSheet.js](../../../../../../../module/actor/sheets/WitcherCharacterSheet.js) | tab-profession.hbs | PARTS.profession | 48 |
| [module/setup/handlebars.js](../../../../../../../module/setup/handlebars.js) | tab-profession.hbs | preload | 11 |

Область поиска: module/ и templates/ текущего checkout; прямые импорты и места вызова сверены отдельно от динамических обращений. Типы и листы сверены с system.json, module/setup/registerDataModels.js и module/setup/registerSheets.js. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Десять .profession-display содержат data-stat/data-level/data-name и description (в большинстве data-effet, только path1.skill1 data-definition). Текущий dispatcher читает лишь data-name; остальные attrs не передают формулу. 30data-field плюс 5 социальных при наличии race, без name у inline controls. numeric level передаётся Item.update строкой, затем NumberField приводит значение. Разбор всех 35 путей подтвердил существование схем; это не проверка native submit.

Имена навыков/level/stat редактируются, имена пути только заголовки; descriptions/notes профессии editable=false. Race editors target race.system.perkN.description с editable из листа, отдельное сохранение редактора в браузере не проверялось. Нет min/max/step/required у level. Уровень 0 не блокирует кнопку. Если Item отсутствует, выводится add-item с data-itemType profession/race. Полный HBS показал два состояния независимо друг от друга.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Все ветви/поля | Группы 18–20 | 10 кнопок/30 полей новой профессии;35 с расой;0 уровень показан; none скрывает | Браузерные изменения отсутствуют |
| Описание/запись | Группы 19–20 | inline0 строка→Number0; raw UUID разметка вместо переданного enriched | Core editor с DOM-фасадом; rich text save не выполнен |

## Непроверенные участки и открытые вопросы

В TASK-0004.008 текущий файл и его связи сопоставлены с датированными протоколами TASK-0003.018/.019 (2026-09-10) и .038 (2026-09-11), в пределах относящихся к нему сценариев. Новых поведенческих запусков нет; прежние настоящие модели/методы и фасады различены в протоколе. Браузерный submit, мир, сеть и запись в БД не проверены. Установлены процессы R008-05, R008-09, R008-20; оставшиеся границы: [U008-01](../../../../cross-check-0002.md#u008-01), [U008-06](../../../../cross-check-0002.md#u008-06). Полный пофайловый разбор соседей в TASK-0003 не равен проверке клиентского lifecycle.

## Связанные проблемы

[issue-00109](../../../../../../issues/potential/issue-00109.md), [issue-00110](../../../../../../issues/potential/issue-00110.md), [issue-00118](../../../../../../issues/potential/issue-00118.md), [issue-00153](../../../../../../issues/potential/issue-00153.md). 109 — потеря enriched;110 — бросок по совпадающему имени;118 — пустая характеристика;153 — общий inline callback преобразует текстовые true/false, не локальная проблема этой формы.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `b47ba02cdaebc6a66ad14a5638213b6eb24460b4`; полный файл | Первая карточка; [сверка порции](../../../../review-log.md#task-0003038) |

## Дополнительная сверка TASK-0003.047

2026-09-12, rusbar-main, 2f94c6c29e298ccf73d67ccc2e5fb8fc358dae2c; исходники не изменены.

Полностью сопоставлены [общая профессия](../../../styles/profession-sheet.css.md), [Actor-scope](../../../styles/character/tab-profession.css.md) и [высота расового редактора](../../../styles/race-sheet.css.md). Группа 12 исполнила core _prepareTabs и получила cssClass='profession active'; группа 13 с этим контекстом отрисовала 10 карточек/кнопок и 3 цветных пути. Для активного Actor пути становятся row/gap0, карточки пути min190; definingSkill вне пути сохраняет min250. Группа 14 отдельно дала 4 perk/editor-content через тестовый editor. CSS не исправляет ранее найденный выбор raw вместо enriched (109); геометрия и rich text save не проверены.

[Сценарии, результаты и ограничения](../../../../review-log.md#task-0003047). Связанные файлы повторно не засчитываются в покрытие.

## Сквозная сверка TASK-0004.008

2026-09-14; rusbar-main, f96434101e0e827838c2e6a3e09da8933a9801ef. Исходник совпадает со срезом TASK-0001; изменено только описание.

Character-HBS показывает десять навыков и расу: inline data-field адресует Item-путь, кнопка броска передаёт имя. Пятнадцать editor читают raw HTML вместо подготовленного enriched; none скрывает бросок, пустой stat и level0 оставляют кнопку. Сохранение вложенного HTML через Actor-форму не установлено.

Сопоставленные определения и потребители: [module/actor/sheets/WitcherCharacterSheet.js](../../../module/actor/sheets/WitcherCharacterSheet.js.md), [module/actor/sheets/WitcherActorSheet.js](../../../module/actor/sheets/WitcherActorSheet.js.md), [module/data/item/professionData.js](../../../module/data/item/professionData.js.md), [module/data/item/templates/professionSkillData.js](../../../module/data/item/templates/professionSkillData.js.md), [module/data/item/templates/professionPathData.js](../../../module/data/item/templates/professionPathData.js.md), [module/data/item/raceData.js](../../../module/data/item/raceData.js.md), [module/actor/sheets/mixins/itemMixin.js](../../../module/actor/sheets/mixins/itemMixin.js.md), [module/actor/sheets/mixins/skillMixin.js](../../../module/actor/sheets/mixins/skillMixin.js.md), [module/actor/mixins/professionMixin.js](../../../module/actor/mixins/professionMixin.js.md), [module/setup/config.js](../../../module/setup/config.js.md), [module/setup/handlebars.js](../../../module/setup/handlebars.js.md), [lang/en.json](../../../lang/en.json.md), [lang/ru.json](../../../lang/ru.json.md), [styles/profession-sheet.css](../../../styles/profession-sheet.css.md), [styles/character/tab-profession.css](../../../styles/character/tab-profession.css.md), [styles/witcher-styles.css](../../../styles/witcher-styles.css.md).

[Протокол и границы](../../../../review-log.md#task-0004008) — TASK-0004.008; процессы [R008-05](../../../../cross-check-0002.md#r008-05), [R008-09](../../../../cross-check-0002.md#r008-09), [R008-20](../../../../cross-check-0002.md#r008-20). В этой порции выполнена статическая сверка; прежние опыты сохраняют свои даты и фасады. Новых поведенческих запусков нет; браузер, мир, сеть и запись в БД не запускались.
