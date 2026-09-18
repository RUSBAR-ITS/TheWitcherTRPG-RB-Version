# templates/sheets/actor/partials/monster/tabs/tab-profession.hbs

## Текущее состояние

**14.3.1.00066, TASK-0010.008.** Существующий definingSkill передаёт явный data-skill-path; девять слотов этим старым шаблоном по-прежнему не выводятся.

[Исходник](../../../../../../../../../../templates/sheets/actor/partials/monster/tabs/tab-profession.hbs); [проверка и пределы](../../../../../../../../task-0010-008-checks.md).

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/sheets/actor/partials/monster/tabs/tab-profession.hbs](../../../../../../../../../../templates/sheets/actor/partials/monster/tabs/tab-profession.hbs) |
| Тип файла | Handlebars |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `b47ba02cdaebc6a66ad14a5638213b6eb24460b4` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.038](../../../../../../../../../tasks/task-0003.038.md), 4 файла, 965 логических строк |
| Запись перекрёстной сверки | [TASK-0003.038](../../../../../../../review-log.md#task-0003038) |

## Назначение файла

Сокращённая вкладка профессии монстра: имя Item, определяющий навык и заметки. Ветви skillPath1–3 и раса не выводятся.

## Условия использования

WitcherMonsterSheet.PARTS.profession, context.profession=getList(profession)[0]. Общие Item/skill listeners наследуются от WitcherActorSheet. Файл не входит в найденный preload.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| section.tab/if profession | 1–46 | Вкладка primary/profession | tabs.profession.cssClass | При наличии Item контейнер .item с _id |
| definingSkill | 11–37 | Основной профессиональный навык | 3inline-edit, одна profession-roll | skillName/stat/level; display data-name |
| notes/description | 32–42 | Два editor с editable=false | target profession.system.* | Исходный текст |
| add-item | 48 | Кнопка добавления profession | data-itemType=profession | Показ если profession отсутствует |

## Основные функции и методы

JS-функций нет. if/unless, eq(stat,"none"), selectOptions(config.statTypes), editor и localize. Порогов/самостоятельного attack UI нет. Бросок не фильтруется по level0/пустому имени; игнорирование ветвей в представлении не удаляет их из Item и поиска Actor.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| WitcherMonsterSheet | [module/actor/sheets/WitcherMonsterSheet.js](../../../../../../../../../../module/actor/sheets/WitcherMonsterSheet.js) | PARTS/context | 41/133 | Подготавливает profession без enrichedText профессии |
| WitcherActorSheet | [module/actor/sheets/WitcherActorSheet.js](../../../../../../../../../../module/actor/sheets/WitcherActorSheet.js) | Наследуемое поведение | config/tabs/editable/listeners | Монстр использует общий слой |
| ProfessionData/professionSkill | [module/data/item/professionData.js](../../../../../../../../../../module/data/item/professionData.js); [module/data/item/templates/professionSkillData.js](../../../../../../../../../../module/data/item/templates/professionSkillData.js) | Модель Item | system.definingSkill.skillName/stat/level/definition; system.notes | Полная schema доступна, HBS читает лишь defining |
| itemMixin | [module/actor/sheets/mixins/itemMixin.js](../../../../../../../../../../module/actor/sheets/mixins/itemMixin.js) | Inline edit/Item lifecycle | system.definingSkill.{skillName,stat,level} | Строковые value→Item.update |
| skillListener/professionMixin | [module/actor/sheets/mixins/skillMixin.js](../../../../../../../../../../module/actor/sheets/mixins/skillMixin.js); [module/actor/mixins/professionMixin.js](../../../../../../../../../../module/actor/mixins/professionMixin.js) | Бросок | data-name→первое совпадение | Один найденный DOM consumer |
| config.statTypes | [module/setup/config.js](../../../../../../../../../../module/setup/config.js) | Варианты select | Определяющая характеристика | none и остальные stat ключи |
| preloadHandlebarsTemplates | [module/setup/handlebars.js](../../../../../../../../../../module/setup/handlebars.js) | Отрицательная сверка preload | HBS не включён | Загрузку задаёт PARTS |
| Helpers | Foundry14.367.0 / Handlebars4.7.9 | Рендер | editor/selectOptions/localize/if/unless/eq | Core helpers и DOM-фасад |
| Локализация | [lang/en.json](../../../../../../../../../../lang/en.json); [lang/ru.json](../../../../../../../../../../lang/ru.json) | Строки | WITCHER.Notes/Actor.Adda.Profession/statTypes | expandObject+fallback |
| CSS | [styles/profession-sheet.css](../../../../../../../../../../styles/profession-sheet.css); [styles/character/tab-profession.css](../../../../../../../../../../styles/character/tab-profession.css) | Стили | monster-profession-flex и общие карточки | Селекторы прочитаны по использованию |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/actor/sheets/WitcherMonsterSheet.js](../../../../../../../../../../module/actor/sheets/WitcherMonsterSheet.js) | tab-profession.hbs | PARTS.profession | 41 |

Область поиска: module/ и templates/ текущего checkout; прямые импорты и места вызова сверены отдельно от динамических обращений. Типы и листы сверены с system.json, module/setup/registerDataModels.js и module/setup/registerSheets.js. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Три inline поля не имеют name, адресуют Item через data-field и ближайший .item. Два readonly editor получают raw definition/notes; присланный enriched контекст не читается, MonsterSheet его и не создаёт для этой профессии. Основной skill имеет data-stat/level/name/effet; используется только name. Нет фильтра на уровень, вид атаки/эффекта или возможность применить на цель. Пустая профессия даёт кнопку add-item, а не пустое дерево.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Рендер | Группы 18–20 | Одна кнопка/3data-field; none скрыт, empty stat виден; paths совместимы со schema | Монстр не получает полную Character форму |
| Общий маршрут | Статическая сверка listener/Actor + группы 01–06 | Применение доступных defining настроек общее | Редактирование конфигурации definingSkill остаётся issue112 |

## Непроверенные участки и открытые вопросы

В TASK-0004.008 текущий файл и его связи сопоставлены с датированными протоколами TASK-0003.018/.019 (2026-09-10) и .038 (2026-09-11), в пределах относящихся к нему сценариев. Новых поведенческих запусков нет; прежние настоящие модели/методы и фасады различены в протоколе. Браузерный submit, мир, сеть и запись в БД не проверены. Установлены процессы R008-05, R008-09, R008-20; оставшиеся границы: [U008-01](../../../../../../../cross-check-0002.md#u008-01), [U008-06](../../../../../../../cross-check-0002.md#u008-06). Полный пофайловый разбор соседей в TASK-0003 не равен проверке клиентского lifecycle.

## Связанные проблемы

[issue-00110](../../../../../../../../../issues/potential/issue-00110.md), [issue-00112](../../../../../../../../../issues/potential/issue-00112.md), [issue-00118](../../../../../../../../../issues/potential/issue-00118.md). Только определяющий навык не является автоматически новой ошибкой: требование показывать ветви монстру не согласовано. Прежние ограничения имени/характеристики и редактора definingSkill сохраняются.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `b47ba02cdaebc6a66ad14a5638213b6eb24460b4`; полный файл | Первая карточка; [сверка порции](../../../../../../../review-log.md#task-0003038) |

## Дополнительная сверка TASK-0003.047

2026-09-12, rusbar-main, 2f94c6c29e298ccf73d67ccc2e5fb8fc358dae2c; исходники не изменены.

[CSS в каталоге character](../../../../../../styles/character/tab-profession.css.md) явно включает .application.sheet.witcher.monster. Реальный core _prepareTabs даёт profession active; группа 13 получила один definingSkill и notes в monster-profession-flex, без profession-path/race-header. Поэтому правила трёх ветвей и расы сейчас не адресуют данный HBS, хотя общий CSS их содержит. [Общее правило](../../../../../../styles/profession-sheet.css.md) monster-profession-flex .profession-card задаёт width100/max:none и сильнее простой поздней карточки max400. Вывод основан на selectors/источниках; браузерная ширина не измерялась.

[Сценарии, результаты и ограничения](../../../../../../../review-log.md#task-0003047). Связанные файлы повторно не засчитываются в покрытие.

## Сквозная сверка TASK-0004.008

2026-09-14; rusbar-main, f96434101e0e827838c2e6a3e09da8933a9801ef. Исходник совпадает со срезом TASK-0001; изменено только описание.

Monster-HBS показывает только definingSkill и notes. Три inline поля и единственная кнопка используют общий listener; stat=none скрывает кнопку. Его Sheet не производит enriched профессии, поэтому raw HTML отделён от неиспользованного enriched в Character.

Сопоставленные определения и потребители: [module/actor/sheets/WitcherMonsterSheet.js](../../../../../../module/actor/sheets/WitcherMonsterSheet.js.md), [module/actor/sheets/WitcherActorSheet.js](../../../../../../module/actor/sheets/WitcherActorSheet.js.md), [module/data/item/professionData.js](../../../../../../module/data/item/professionData.js.md), [module/data/item/templates/professionSkillData.js](../../../../../../module/data/item/templates/professionSkillData.js.md), [module/actor/sheets/mixins/itemMixin.js](../../../../../../module/actor/sheets/mixins/itemMixin.js.md), [module/actor/sheets/mixins/skillMixin.js](../../../../../../module/actor/sheets/mixins/skillMixin.js.md), [module/actor/mixins/professionMixin.js](../../../../../../module/actor/mixins/professionMixin.js.md), [module/setup/config.js](../../../../../../module/setup/config.js.md), [module/setup/handlebars.js](../../../../../../module/setup/handlebars.js.md), [lang/en.json](../../../../../../lang/en.json.md), [lang/ru.json](../../../../../../lang/ru.json.md), [styles/profession-sheet.css](../../../../../../styles/profession-sheet.css.md), [styles/character/tab-profession.css](../../../../../../styles/character/tab-profession.css.md).

[Протокол и границы](../../../../../../../review-log.md#task-0004008) — TASK-0004.008; процессы [R008-05](../../../../../../../cross-check-0002.md#r008-05), [R008-09](../../../../../../../cross-check-0002.md#r008-09), [R008-20](../../../../../../../cross-check-0002.md#r008-20). В этой порции выполнена статическая сверка; прежние опыты сохраняют свои даты и фасады. Новых поведенческих запусков нет; браузер, мир, сеть и запись в БД не запускались.
