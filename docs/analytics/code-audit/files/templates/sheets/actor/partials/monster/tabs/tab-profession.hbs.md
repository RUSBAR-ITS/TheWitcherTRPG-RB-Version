# templates/sheets/actor/partials/monster/tabs/tab-profession.hbs

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

Полностью прочитан файл; соседние определения проверены в пределах вызовов. 24 группы изолированных сценариев: реальные модели/методы, Roll/extendedRoll, Handlebars 4.7.9 и отдельные функции ядра Foundry 14.367.0 на Node24.16.0. Dialog, DOM/Application, ActiveEffect-конструктор, запись Actor/Item/ChatMessage и query — фасады. Core миграция ActiveEffect выполнена отдельно на payload. Браузерные события/валидация/сохранение, полный жизненный цикл эффекта, HTTP, БД и несколько клиентов не запускались. Игровые требования сверх кода не выбирались.

## Связанные проблемы

[issue-00110](../../../../../../../../../issues/potential/issue-00110.md), [issue-00112](../../../../../../../../../issues/potential/issue-00112.md), [issue-00118](../../../../../../../../../issues/potential/issue-00118.md). Только определяющий навык не является автоматически новой ошибкой: требование показывать ветви монстру не согласовано. Прежние ограничения имени/характеристики и редактора definingSkill сохраняются.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `b47ba02cdaebc6a66ad14a5638213b6eb24460b4`; полный файл | Первая карточка; [сверка порции](../../../../../../../review-log.md#task-0003038) |
