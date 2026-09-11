# templates/partials/character/tab-stats.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/partials/character/tab-stats.hbs](../../../../../../../templates/partials/character/tab-stats.hbs) |
| Тип файла | Handlebars |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `aa6af106e86a9c75fe050d599f961c8fadb74f1b` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.030](../../../../../../tasks/task-0003.030.md), 9 файлов, 424 логических строк |
| Запись перекрёстной сверки | [TASK-0003.030](../../../../review-log.md#task-0003030) |

## Назначение файла

Текущая общая вкладка характеристик персонажа и монстра: значения, максимумы, разницы, репутация и ссылки на редактор.

## Условия использования

PARTS.stats CharacterSheet и MonsterSheet указывает на этот HBS. Получает system, tabs.stats.cssClass, totalStats, isGM/displayRep. Листовая statMixin связывает stat-roll и reputation-roll.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| Основной список system.stats | 8–35 | Девять характеристик, исключение toxicity по локализованной подписи | stat-display/stat-roll/data-stat | value, max и formatModLabel(value,max); классы plus/zero/minus |
| totalStats / reputation | 37–67 | Сумма и условная репутация | or isGM displayRep | Репутация: value в основном числе и ошибочно в span.max, разница вычисляется с настоящим max |
| system.derivedStats | 75–112 | Шесть показателей после исключения шести ресурсов | char-derived-button | HP/STA/shield/resolve/focus/vigor исключены по подписи; STUN/RUN/LEAP/ENC/REC/WT без roll-класса |
| openModifiers | 5,71 | Две ссылки редактора | data-type=stats/derivedStats | Передают тип через actions листа |

## Основные функции и методы

JavaScript-функций, partial-вызовов и именованных input нет. each/unless/eq/or выбирают записи; gte/gt форматируют ноль и знак; formatModLabel вычитает max из value. Фильтры сравнивают локализованные labels, не ключи полей. Поэтому подмена label может изменить состав списка даже при прежнем ключе.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| Stats / DerivedStats / Reputation | [module/data/actor/templates/common/stats/statsData.js](../../../../../../../module/data/actor/templates/common/stats/statsData.js); [module/data/actor/templates/common/stats/derivedStatsData.js](../../../../../../../module/data/actor/templates/common/stats/derivedStatsData.js); [module/data/actor/templates/common/reputationData.js](../../../../../../../module/data/actor/templates/common/reputationData.js) | Модели контекста | label/value/max | Оба each и блок репутации |
| formatModLabel / сравнения | [module/setup/handlebars.js](../../../../../../../module/setup/handlebars.js) | Системные helpers | value−max и классы знаков | 110–118; текущий HBS в preload-списке не найден, подключён PARTS |
| statMixin | [module/actor/sheets/mixins/statMixin.js](../../../../../../../module/actor/sheets/mixins/statMixin.js) | DOM и producer totalStats через CharacterSheet | stat/reputation-roll; calc_total_stats | Селекторы, метод и CharacterSheet:168 |
| Контекст/actions двух листов | [module/actor/sheets/WitcherActorSheet.js](../../../../../../../module/actor/sheets/WitcherActorSheet.js); [module/actor/sheets/WitcherCharacterSheet.js](../../../../../../../module/actor/sheets/WitcherCharacterSheet.js); [module/actor/sheets/WitcherMonsterSheet.js](../../../../../../../module/actor/sheets/WitcherMonsterSheet.js) | PARTS/контекст/действия | displayRep, isGM базового core, tabs; openModifiers | База читает настройку; Character задаёт totalStats, Monster не задаёт |
| displayRep | [module/setup/settings.js](../../../../../../../module/setup/settings.js) | Мировая настройка через контекст | Показывать репутацию не-GM | 61–68; не является проверкой прав обработчика |
| localize | Foundry/Handlebars; lang/en.json/lang/ru.json | Внешний helper | Подписи и фильтры по локализованной строке | Dotted JSON ключи предварительно раскрываются expandObject |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/actor/sheets/WitcherCharacterSheet.js](../../../../../../../module/actor/sheets/WitcherCharacterSheet.js) | Весь HBS | PARTS.stats | 40 |
| [module/actor/sheets/WitcherMonsterSheet.js](../../../../../../../module/actor/sheets/WitcherMonsterSheet.js) | Весь HBS | PARTS.stats | 33 |
| [module/actor/sheets/mixins/statMixin.js](../../../../../../../module/actor/sheets/mixins/statMixin.js) | Два класса roll | Подключение click | statListener |

Область поиска: module/ и templates/ текущего checkout; прямые импорты и места вызова сверены отдельно от динамических обращений. Типы и листы сверены с system.json, module/setup/registerDataModels.js и module/setup/registerSheets.js. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Шаблон ничего не записывает. Ресурсы удачи/адреналина изменяются отдельным sidebar; здесь luck.value отображается, но её спасбросок использует luck.max. Репутация видна при isGM||displayRep. Итог totalStats приходит извне; HBS его не рассчитывает.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Полные 114 строк и producers | PARTS двух листов, модели, helpers и actions | Текущий путь один; derived-ячейки сами не инициируют бросок | Полные классы дочерних листов остаются вне покрытия |
| Настоящий Handlebars | Группы 12–13: 9 stat/6 derived, 3 комбинации видимости, 0/отрицательные, label mutation | Знаки и фильтры подтверждены; reputation.value3/max8 показывает span.max '+3' при разнице −5 | Без CSS/браузера |
| Сумма монстра | Группа 19: настоящий _prepareCharacterData Monster и HBS | Контекст не содержит totalStats, заголовок пуст; прямой calc_total_stats даёт 72 | Базовый контекст и его отсутствие другого producer проверены статически |

## Непроверенные участки и открытые вопросы

Сравнение по переводам само по себе не признано дефектом для штатных labels. Внешние модули могут добавлять контекст/переводы; не исследованы. Семь ошибочно объявленных отсутствующими подписей прошлого этапа исправлены с учётом expandObject.

## Связанные проблемы

[issue-00012](../../../../../../issues/potential/issue-00012.md), [issue-00035](../../../../../../issues/potential/issue-00035.md), [issue-00036](../../../../../../issues/potential/issue-00036.md), [issue-00198](../../../../../../issues/potential/issue-00198.md), [issue-00199](../../../../../../issues/potential/issue-00199.md). Расчётные проблемы отделены от двух подтверждённых несогласованностей вывода.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `aa6af106e86a9c75fe050d599f961c8fadb74f1b`; полный файл | Первая карточка; [сверка порции](../../../../review-log.md#task-0003030) |

## Уточнение TASK-0003.031

2026-09-11, `928ce4e537c6a3fdc34f8b6fa3fcfdb5a669f68d`. PARTS.stats Character напрямую указывает на этот шаблон; его контекст totalStats теперь проверен полным _prepareContext: 72 для девяти max8. Ключи действий и данные модификаторов сопоставлены с базовыми listeners и #openModifiers специализированного листа.

Связи: [module/actor/sheets/WitcherCharacterSheet.js](../../../module/actor/sheets/WitcherCharacterSheet.js.md). [Методика и ограничения сверки](../../../../review-log.md#task-0003031).
