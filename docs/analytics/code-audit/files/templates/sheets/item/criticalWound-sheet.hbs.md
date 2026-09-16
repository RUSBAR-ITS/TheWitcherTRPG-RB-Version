# templates/sheets/item/criticalWound-sheet.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/sheets/item/criticalWound-sheet.hbs](../../../../../../../templates/sheets/item/criticalWound-sheet.hbs) |
| Тип файла | Handlebars |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `b09f992960a76d1c75946f402e42d93fa0785008` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.020](../../../../../../tasks/task-0003.020.md), 10 файлов, 428 логических строк |
| Запись перекрёстной сверки | [TASK-0003.020](../../../../review-log.md#task-0003020) |

## Актуализация N01–N08 — 14.3.1.00010

2026-09-16, dev, база aeb527c6e6402e8a5f940a2c3ad0020d7e5b35e4. Отображаемые placeholder/tooltip используют `WITCHER.Name`. Привязки name/data-field, классы действий, условия шаблона и введённые имена сохранены.

[Реализация и адресные проверки](../../../../../../issues/open/issue-00330.md#реализация-n01n08--143100010). Датированные разборы ниже сохраняют результаты прежних срезов.


## Назначение файла

Основная форма Item критической травмы: имя, степень, лечение, локация, счётчик/срок заживления, описание, lesserEffect и followUp.

## Условия использования

PARTS.main WitcherCriticalWoundSheet, с контекстом общего WitcherItemSheet._prepareContext. Получает document, config, systemFields, enrichedText и showConfig. Предзагрузка как partial не требуется: лист загружает свой PARTS.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| section; configure-item | 1–5 | Шестерёнка при showConfig | data-action=configureItem | Открывает общую конфигурацию, включая Item.effects |
| name и три select | 8–18 | Редактируемые name, system.criticalLevel/treatment/location | selectOptions из CONFIG | Степени simple/complex/difficult/deadly; состояния none/stabilized/treated; шесть обычных локаций |
| days-healed / healing-time | 20–28 | Дни и цель заживления | system.daysHealed числовой input; healingTime disabled | Счётчик редактируется, срок вычисляет модель; min/max/step здесь не заданы |
| description / lesserEffect / followUp | 32–34 | HTML, флаг, UUID | formInput и два formGroup | Используются поля схемы, правильный enriched и toggled=true |

## Основные функции и методы

JavaScript-функций и обработчиков файл не определяет. Handlebars только формирует разметку; выполнение действий и сохранение находятся в перечисленных потребителях.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| PARTS.main | [module/item/sheets/WitcherCriticalWoundSheet.js](../../../../../../../module/item/sheets/WitcherCriticalWoundSheet.js) | Назначение шаблона | 12 | Собственный лист 600×620 |
| Контекст/submit/configureItem | [module/item/sheets/WitcherItemSheet.js](../../../../../../../module/item/sheets/WitcherItemSheet.js) | Наследуемый producer и actions | _prepareContext; submitOnChange; _renderConfigureDialog | document/systemFields/enrichedText/showConfig присутствуют |
| CriticalWoundData | [module/data/item/criticalWoundData.js](../../../../../../../module/data/item/criticalWoundData.js) | Пути данных и schema | Все system.* | Полный разбор схемы; только daysHealed редактируется из двух чисел |
| critLevel/critTreatment/location | [module/setup/config.js](../../../../../../../module/setup/config.js) | Словари selectOptions | 9–17 | Выбор интерфейса, не choices схемы |
| localize/selectOptions/formInput/formGroup | Foundry 14.367.0 / Handlebars 4.7.9 | Helpers | Все поля | В проверке formInput/formGroup заменены регистраторами аргументов, не настоящими виджетами |
| Ключи label/hint | [lang/en.json](../../../../../../../lang/en.json); [lang/ru.json](../../../../../../../lang/ru.json) | Локализация | Старый WITCHER.CritWound.HealingTime.Label и метаданные модели | Все ключи найдены после раскрытия составных JSON-ключей |
| critwound*/healing-time* | [styles/crit-wounds-table.css](../../../../../../../styles/crit-wounds-table.css) | CSS | Обёртка и счётчик | Связь по селекторам; визуальный рендер не проверялся |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/item/sheets/WitcherCriticalWoundSheet.js](../../../../../../../module/item/sheets/WitcherCriticalWoundSheet.js) | Весь HBS | PARTS.main | Единственный найденный прямой владелец |

Область поиска: module/ и templates/ текущего checkout; регистрация сверена с system.json. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Сама разметка ничего не сохраняет. Именованные входы идут общему submitOnChange. Из 9 полей модели sterilized не представлен отдельной галочкой; это флаг использования бонуса при заживлении. Здесь нет редактора img или встроенного списка ActiveEffect: effects редактируются через шестерёнку общей конфигурации. Выбор treatment вручную не вызывает treat; отдельной кнопки перехода эта форма не содержит.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Рендер/аргументы | Настоящий HBS; модель/поля настоящие, helpers форм — фасады | description: system.description с value/enriched; lesserEffect: system.lesserEffect; UUID: system.followUp | Не браузерная форма и не сохранение редактора |
| Select и числовые поля | Полные 36 строк и модель | name/3 select/daysHealed доступны; healingTime disabled; варианты не ограничивают StringField | Внешний DocumentUUID виджет не запускался |
| Подписи | 44 ключа порции вместе со словарями | en/ru без пропусков, включая старый ключ HealingTime.Label | Это проверка наличия, не литературного качества перевода |

## Непроверенные участки и открытые вопросы

Текущая сверка охватила исходник, описанные поля и конкретных потребителей; прежние результаты выше сохраняют даты своих опытов. Схема, fromUuid и запросы create/delete сопоставлены. Остаются существование мирового UUID, права/ошибки сервера, порядок сохранения, повторная подготовка Actor/AE и отдельно скопированные эффекты. Следующий критерий: отличать загруженный шаблон, запрос записи и подтверждённое состояние. Запуск мира или изменение доступа здесь не согласованы. Границы: [U012-01](../../../../cross-check-0002.md#u012-01) и [U012-08](../../../../cross-check-0002.md#u012-08).

## Связанные проблемы

[issue-00121](../../../../../../issues/potential/issue-00121.md), [issue-00122](../../../../../../issues/potential/issue-00122.md). Форма позволяет задать счётчик и ссылку, которые читаются описанными ветвями модели; отдельной подтверждённой ошибки разметки в этой порции не выявлено.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `b09f992960a76d1c75946f402e42d93fa0785008`; полный файл | Первая карточка; [сверка порции и второй серии](../../../../review-log.md#task-0003020) |

## Уточнение TASK-0003.058

2026-09-12; rusbar-main, 5283da15a49422fc339c44add4e7d7d02c174ce4; исходник не изменён.

Полям формы сопоставлены реальные Simple Item и схема CriticalWoundData. Семь Item содержат HTML при пустом effects; редактор описания не превращает текст в changes. Эффекты остальных Item разобраны отдельно в карточках владельцев. Браузерный сценарий не выполнялся.

[Карточки Simple](../../../packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/_Folder.json.md), [протокол, методы и ограничения](../../../../review-log.md#task-0003058). Реальные записи в мир не выполнялись; состояния issues не менялись.

## Сквозная сверка TASK-0004.012

2026-09-14; rusbar-main, a853fc2ff721e5d33b2716081c657bd92d62d86b. Исходник совпадает со срезом TASK-0001; изменено только описание.

Форма редактирует поля модели и followUp; Drop сохраняет UUID любого Item, не строит новую травму из состояния текущей. Унаследованный Drop проверяет isEditable, но внутренний update не ожидается. Обычные ActiveEffect доступны через конфигурацию Item; canHaveTemporaryItemImprovement=false относится к временному улучшению. стерилизация отдельным полем этой формы не выведена.

Сопоставленные определения и потребители: [module/data/item/criticalWoundData.js](../../../module/data/item/criticalWoundData.js.md), [module/item/sheets/WitcherCriticalWoundSheet.js](../../../module/item/sheets/WitcherCriticalWoundSheet.js.md), [module/item/sheets/WitcherItemSheet.js](../../../module/item/sheets/WitcherItemSheet.js.md).

[Протокол и границы](../../../../review-log.md#task-0004012) — TASK-0004.012; процессы [R012-02](../../../../cross-check-0002.md#r012-02). В этой порции выполнена статическая сверка; прежние опыты сохраняют свои даты и фасады. Новых поведенческих запусков нет; браузер, мир, сеть и запись в БД не запускались.
