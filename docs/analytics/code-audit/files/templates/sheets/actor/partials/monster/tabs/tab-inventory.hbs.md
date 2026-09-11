# templates/sheets/actor/partials/monster/tabs/tab-inventory.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/sheets/actor/partials/monster/tabs/tab-inventory.hbs](../../../../../../../../../../templates/sheets/actor/partials/monster/tabs/tab-inventory.hbs) |
| Тип файла | Handlebars |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `ce0c7eb7069b215b641d725913b3aae21502e811` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.027](../../../../../../../../../tasks/task-0003.027.md), 12 файлов, 1375 логических строк |
| Запись перекрёстной сверки | [TASK-0003.027](../../../../../../../review-log.md#task-0003027) |

## Назначение файла

Действующая вкладка инвентаря монстра: общие таблицы оружия/брони, условная добыча и кнопка exportLoot.

## Условия использования

WitcherMonsterSheet.PARTS.inventory, TABS.primary.inventory. Корневые tabs.inventory/cssClass/data-group/data-tab совпадают с V2. Включения оружия/брони безусловны; loots — при непустом массиве.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| 1–8 | Блок HBS | Вкладка и экипировка | Рендер через потребителей | Общие weapons/armors с теми же флагами, что у Character |
| 10–16 | Блок HBS | Добыча и экспорт | Рендер через потребителей | valuables=loots/hasQuantity=true; button data-action=exportLoot, class export-loot |

## Основные функции и методы

Собственных JS-функций, экспортов и схем нет. В файле используются if, localize и включения partial. Ветви и поля описаны по блокам выше.

| Селектор / вход | Обработчик и источник | Действие и поле |
| --- | --- | --- |
| .export-loot | [WitcherMonsterSheet.#exportLoot](../../../../../../../../../../module/actor/sheets/WitcherMonsterSheet.js) | Современный data-action=exportLoot; у прежней ссылки есть только class без action |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| WitcherMonsterSheet | [module/actor/sheets/WitcherMonsterSheet.js](../../../../../../../../../../module/actor/sheets/WitcherMonsterSheet.js) | Регистрация/producer/action | PARTS.inventory, _prepareLoot, DEFAULT_OPTIONS.actions.exportLoot→#exportLoot | Экспорт: prompt множителя→создание loot Actor→генерация/количество Item→render; полное действие не исполнялось |
| Общий ActorSheet | [module/actor/sheets/WitcherActorSheet.js](../../../../../../../../../../module/actor/sheets/WitcherActorSheet.js) | Контекст и listeners | weapons/armors/items/_prepareItems | Сначала исключается stored; _prepareLoot сохраняет enhancement и не проверяет applied |
| if, localize | Handlebars 4.7.9 / Foundry VTT 14.367.0 | Внешний шаблонный API | Вызовы в этом HBS; core localize/concat: /opt/foundryvtt/client/applications/handlebars.mjs | Рендер настоящий; game.i18n/окружение представлены фасадом, core helper localize/concat дополнительно исполнены |
| Словари и подписи | [lang/en.json](../../../../../../../../../../lang/en.json); [lang/ru.json](../../../../../../../../../../lang/ru.json) | Контекст и локализация | Точные строковые ключи localize в HBS | 114 статических ключей порции сверены с en/ru; отсутствующие и динамические ключи отражены в issue-00178 |
| Обработчики DOM | [module/actor/sheets/WitcherMonsterSheet.js](../../../../../../../../../../module/actor/sheets/WitcherMonsterSheet.js) | DOM→JS | Сопоставление ниже в таблице действий | Селекторы и ближайшие контейнеры проверены по реальному шаблону и определениям |
| partial tab-inventory-armors.hbs | [templates/sheets/actor/partials/character/inventory/tab-inventory-armors.hbs](../../../../../../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-armors.hbs) | Литеральное включение | Шаблонный контекст и hash-аргументы из исследуемого файла | Путь существует, регистрация/вызов и встречное включение сверены |
| partial tab-inventory-valuables.hbs | [templates/sheets/actor/partials/character/inventory/tab-inventory-valuables.hbs](../../../../../../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-valuables.hbs) | Литеральное включение | Шаблонный контекст и hash-аргументы из исследуемого файла | Путь существует, регистрация/вызов и встречное включение сверены |
| partial tab-inventory-weapons.hbs | [templates/sheets/actor/partials/character/inventory/tab-inventory-weapons.hbs](../../../../../../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-weapons.hbs) | Литеральное включение | Шаблонный контекст и hash-аргументы из исследуемого файла | Путь существует, регистрация/вызов и встречное включение сверены |
| Классы списка, details, progress, изображения | [styles/tab-inventory.css](../../../../../../../../../../styles/tab-inventory.css) | CSS/HTML | grid заголовков/строк, stored-item и carry-bar до привязки селекторов | Полный CSS и вид браузера не проверялись; img без src не получает fallback в HBS, assets вне границ анализа |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/actor/sheets/WitcherMonsterSheet.js](../../../../../../../../../../module/actor/sheets/WitcherMonsterSheet.js) | PARTS.inventory | Зарегистрированный V2 вызывает рендер части inventory | Поиск module/templates; конкретный путь найден в исходном потребителе |

Область поиска: module/ и templates/ текущего checkout. Типы проверены по system.json, регистрация листов — по module/setup/registerSheets.js. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Сама кнопка экспорт не создаёт данные без внешнего action. Класс export-loot не является listener: актуальный вход — data-action. Свободное enhancement.type=weapon/armor может появиться и в экипировке, и в loots; это описанное пересечение producer-списков, не отдельное доказательство необходимости менять фильтр. Прямой таблицы валюты/веса здесь нет.

Системные поля Item/Actor непосредственно в этом фрагменте не читаются; входы header/has*/itemType/spellType описаны выше.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Полное чтение/структура | 16 логических строк; все блоки и вложенные each/if прочитаны | Назначение, входные поля, partial и actions сопоставлены | HBS не является реализацией методов Item/Actor |
| Изолированные проверки | Группы 01,12–13; реальный Handlebars/модели и обработчики | При двух ремонтируемых Item отрендерены две кнопки ремонта и одна exportLoot; один свободный weapon-enhancement присутствовал в двух списках. Поиск module не нашёл monster-listener для item-repair. Экспорт Actor/БД не запускался. | Actor/DOM/запись/диалоги представлены фасадами; без мира и браузера |
| Встречные связи | Определения producer/helper/handler и найденные потребители | Пути и имена сверены, частичный разбор соседей не добавляет охват | Мировые макросы, внешние модули и компедиумы не проверялись |

## Непроверенные участки и открытые вопросы

Весь файл прочитан. Проверены данные рендера и существенные границы, перечисленные выше. Не запускались браузер, серверная запись, DragDrop, реальные броски/производство/ремонт/экспорт или полноценные листы Actor. CSS проверен только до селекторов. Реальный Foundry Document и UI представлены ограниченными фасадами; фактическая регистрация проверена статически. Полные файлы Character/Monster/MountData, валюта/награды и производство остаются за дальнейшими порциями.

## Связанные проблемы

[issue-00063](../../../../../../../../../issues/potential/issue-00063.md), [issue-00177](../../../../../../../../../issues/potential/issue-00177.md). Наблюдения остаются potential. Прежние issues сопоставлены по конкретному маршруту; отсутствие новой карточки не означает проверки исправности всей подсистемы.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `ce0c7eb7069b215b641d725913b3aae21502e811`; полный файл | Первая карточка; [сверка порции](../../../../../../../review-log.md#task-0003027) |

## Уточнение TASK-0003.032

2026-09-11, `8b938d44a042749df027d8b58e28bb1d79638091`. Полный MonsterSheet._prepareLoot подтверждает 9 принимаемых типов, getList/items исключают stored; weapon/armor подготовлены отдельно. Кнопки .item-repair по-прежнему не имеют listener в полном классе. exportLoot копирует actor.toObject().items целиком, не context.loots, и обрабатывает все копии.

Связи: [module/actor/sheets/WitcherMonsterSheet.js](../../../../../../module/actor/sheets/WitcherMonsterSheet.js.md). [Результаты и пределы проверки](../../../../../../../review-log.md#task-0003032).

## Дополнительная сверка TASK-0003.036

2026-09-11, `rusbar-main`, `32d8fdd029ce4c6401db25f0d9645445ac0f8ca2`; исходники не менялись.

Сверен отрицательный consumer: в этом HBS нет .open-currency-converter или вызова HBS конвертера. Его exporter остаётся отдельным действием. Наследуемый MonsterSheet currencyConverterListeners получает пустой набор таких элементов; отсутствие стандартной кнопки не означает отсутствия метода на Actor.

Карточки процесса: [module/actor/mixins/currencyConverterMixin.js](../../../../../../module/actor/mixins/currencyConverterMixin.js.md), [module/actor/sheets/mixins/currencyConverterMixin.js](../../../../../../module/actor/sheets/mixins/currencyConverterMixin.js.md), [templates/sheets/actor/currencyConverter/currencyConverter.hbs](../../../currencyConverter/currencyConverter.hbs.md), [templates/chat/currency-conversion.hbs](../../../../../chat/currency-conversion.hbs.md).

[Проверки и перекрёстная сверка](../../../../../../../review-log.md#task-0003036). Связанный файл повторно в покрытии не учитывается; правок системы нет.
