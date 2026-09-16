# module/data/item/templates/regions/templatePropertiesData.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/data/item/templates/regions/templatePropertiesData.js](../../../../../../../../../module/data/item/templates/regions/templatePropertiesData.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `ef8117ba6e5a184989e65761d47a068381056e4a` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.022](../../../../../../../../tasks/task-0003.022.md), 5 файлов, 289 логических строк |
| Запись перекрёстной сверки | [TASK-0003.022](../../../../../../review-log.md#task-0003022) |

## Назначение файла

Вложенная модель настроек геометрии и срока визуального региона для spell/ritual. Хранит четыре поля; не создаёт область и не рассчитывает её длительность в бою.

## Условия использования

SpellData и RitualData включают TemplateProperties через EmbeddedDataField. Формы читают настройки, spellRegionMixin использует их при создании/удалении. Это не самостоятельный Item или Region.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| fields | const; 1 | foundry.data.fields | Локально | Ссылка на API |
| TemplateProperties | default class; 3–13 | Наследник foundry.abstract.DataModel | Импорт в SpellData/RitualData | Вложенная схема |
| createTemplate | BooleanField initial=false; 6 | Разрешение создания области | system.templateProperties.createTemplate | Читается guard createSpellRegion |
| templateSize | NumberField initial=0; 7 | Размер в единицах сцены согласно подписи формы | system.templateProperties.templateSize | Пересчитывается примесью; min/max/integer не заданы |
| templateType | StringField initial=''; 8 | Ключ вида области | system.templateProperties.templateType | В схеме нет choices; варианты задают листы |
| visualEffectDuration | NumberField без initial; 9 | Задержка удаления через клиентский таймер | system.templateProperties.visualEffectDuration | Положительное значение ×1000 мс; отдельно от flags.duration |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| static defineSchema() | API fields | Объект четырёх полей | Создаёт Boolean/Number/String/Number | Без side effects или записи |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| foundry.abstract.DataModel; BooleanField/NumberField/StringField | Foundry 14.367.0; common/abstract/data.mjs; common/data/fields.mjs | Наследование/схема | defineSchema | Настоящие классы в Node |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/data/item/spellData.js](../../../../../../../../../module/data/item/spellData.js) | TemplateProperties | EmbeddedDataField и перенос прежних параметров | 35; 117–133 |
| [module/data/item/ritualData.js](../../../../../../../../../module/data/item/ritualData.js) | TemplateProperties | EmbeddedDataField и перенос прежних параметров | 32; 75–87 |
| [module/data/item/mixin/spellRegionMixin.js](../../../../../../../../../module/data/item/mixin/spellRegionMixin.js) | Все четыре поля | Guard, вычисление shapes/range, таймер | 2–172 |
| [module/item/sheets/WitcherSpellSheet.js](../../../../../../../../../module/item/sheets/WitcherSpellSheet.js) | Варианты templateType | createSelects для формы | 56–62 |
| [module/item/sheets/WitcherRitualSheet.js](../../../../../../../../../module/item/sheets/WitcherRitualSheet.js) | Варианты templateType | createSelects для формы | 27–33 |
| [templates/sheets/item/spell-sheet.hbs](../../../../../../../../../templates/sheets/item/spell-sheet.hbs) | templateProperties.* | Актуальные name-пути | 55, 91–101 |
| [templates/sheets/item/ritual-sheet.hbs](../../../../../../../../../templates/sheets/item/ritual-sheet.hbs) | Прежние поля | Форма ещё обращается без templateProperties | 85–110; issue129 |
| [module/item/sheets/configurations/WitcherPropertiesConfigurationSheet.js](../../../../../../../../../module/item/sheets/configurations/WitcherPropertiesConfigurationSheet.js) | createTemplate | Устаревший путь при выборе PART | _configureRenderParts; issue74 |

Область поиска: module/ и templates/ текущего checkout; регистрация сверена с system.json. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Начальные значения false/0/''/undefined. Отрицательные и дробные числа проходят схему, неизвестная строка типа тоже; это факт отсутствия ограничений, без решения о допустимых игровых значениях. Секундный visualEffectDuration не синхронизируется с duration заклинания/флагом Region: второй механизм находится в regionHooks.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Схема/границы | Группа 01 | Подтверждены defaults и отсутствие выбора/числовых ограничений | Поля настоящие, UI не запускался |
| Потребители | Группы 06–07, 11, 14; формы .021 | Нулевой размер блокирует createSpellRegion; положительный visualEffectDuration задаёт таймер; геометрия зависит от типа | Нет сохранения/рисования |

## Непроверенные участки и открытые вопросы

Исходник и указанные связи сопоставлены в TASK-0004.009. Схема не определяет радиус/диаметр, бессрочность, целевые сцены и единицы текста duration; живое размещение/удаление не выполнялось. Остаток: [U009-04](../../../../../../cross-check-0002.md#u009-04), [U009-05](../../../../../../cross-check-0002.md#u009-05), [U009-07](../../../../../../cross-check-0002.md#u009-07). Новых поведенческих запусков нет; прежние протоколы сохраняют даты и фасады.

## Связанные проблемы

[issue-00074](../../../../../../../../issues/potential/issue-00074.md), [issue-00128](../../../../../../../../issues/potential/issue-00128.md), [issue-00129](../../../../../../../../issues/potential/issue-00129.md), [issue-00141](../../../../../../../../issues/potential/issue-00141.md), [issue-00144](../../../../../../../../issues/potential/issue-00144.md). 74/128/129 — установленные связи с прежними порциями; 141 — перевод размера эманации; 144 — выбор сцены при таймере.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `ef8117ba6e5a184989e65761d47a068381056e4a`; полный файл | Первая карточка; [сверка порции](../../../../../../review-log.md#task-0003022) |

## Сквозная сверка TASK-0004.009

2026-09-14; rusbar-main, 7adc2362937779de0c03957aacf73ff2cf13e211. Исходник совпадает со срезом TASK-0001; изменено только описание.

Четыре поля templateProperties сопоставлены с переносом Spell/Ritual, актуальной формой Spell и устаревшими путями Ritual/общего конфигуратора. create/type/size управляют guard; размер идёт в геометрию, visualEffectDuration — в отдельный секундный таймер. flags.duration вычисляется другим путём из текста магии.

Сопоставленные определения и потребители: [module/data/item/spellData.js](../../spellData.js.md), [module/data/item/ritualData.js](../../ritualData.js.md), [module/data/item/mixin/spellRegionMixin.js](../../mixin/spellRegionMixin.js.md), [module/item/sheets/WitcherSpellSheet.js](../../../../item/sheets/WitcherSpellSheet.js.md), [module/item/sheets/WitcherRitualSheet.js](../../../../item/sheets/WitcherRitualSheet.js.md), [templates/sheets/item/spell-sheet.hbs](../../../../../templates/sheets/item/spell-sheet.hbs.md), [templates/sheets/item/ritual-sheet.hbs](../../../../../templates/sheets/item/ritual-sheet.hbs.md), [module/item/sheets/configurations/WitcherPropertiesConfigurationSheet.js](../../../../item/sheets/configurations/WitcherPropertiesConfigurationSheet.js.md).

[Протокол и границы](../../../../../../review-log.md#task-0004009) — TASK-0004.009; процессы [R009-02](../../../../../../cross-check-0002.md#r009-02), [R009-15](../../../../../../cross-check-0002.md#r009-15), [R009-17](../../../../../../cross-check-0002.md#r009-17), [R009-21](../../../../../../cross-check-0002.md#r009-21). В этой порции выполнена статическая сверка; прежние опыты сохраняют свои даты и фасады. Новых поведенческих запусков нет; браузер, мир, сеть и запись в БД не запускались.
