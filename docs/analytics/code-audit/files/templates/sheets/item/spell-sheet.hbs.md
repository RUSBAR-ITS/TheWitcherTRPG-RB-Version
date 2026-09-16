# templates/sheets/item/spell-sheet.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/sheets/item/spell-sheet.hbs](../../../../../../../templates/sheets/item/spell-sheet.hbs) |
| Тип файла | Handlebars |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-16: актуализация технических обращений по issue-00001 |
| Ветка и коммит | `dev`, база `d8e0e1ad1159cb71a8769b0353f812de6f1ed4d8` + незакоммиченное исправление issue-00001 |
| Изменения относительно коммита | issue-00001; текущие технические обращения актуализированы. Прежние опыты ниже относятся к своим датам. |
| Задача и порция | [TASK-0003.021](../../../../../../tasks/task-0003.021.md), 13 файлов, 936 логических строк |
| Запись перекрёстной сверки | [TASK-0003.021](../../../../review-log.md#task-0003021) |

Актуализация [issue-00001](../../../../../../issues/closed/issue-00001.md), 2026-09-16: Обращения к ресурсам и/или техническим namespaces переведены на TheWitcherTRPG-RB-Version. Формулы и порядок действий сохранены. Датированные проверки ниже выполнены до смены ID.

## Назначение файла

Основная форма Item spell: стоимость, описание, вид знака, побочный эффект дара, параметры области и три независимых признака урона/щита/лечения.

## Условия использования

PARTS.main WitcherSpellSheet загружает HBS, который включает spell-header. Использует item.system и selects. Обычные name-поля передаются inherited форме, own JS событий файл не определяет.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| section.scrollable; item-table; spell-template-damage | Разметка 1–125 | Группы формы | PARTS.main | Рендер |
| spell-header partial | Включение 2 | Имя, картинка, класс/уровень/источник/книга | Указанный путь partial | Контекст передаётся без изменения |
| staminaIsVar/stamina/range/duration/defence/domain | Поля таблицы 5–39 | Переменная стоимость; STA скрыта при true; range/defence скрыты у MagicalGift; domain только Witcher | name=system.* | stamina введена text, схема Number; остальные строки |
| effect/sideEffect | textarea42–48 | Описание и побочный эффект дара | name=system.* | sideEffect только MagicalGift |
| templateProperties.createTemplate/causeDamages/createsShield/doesHeal | 4 checkbox54–68 | Независимые признаки | name=system.* | Включают соответствующие поля ниже |
| templateProperties.templateSize/templateType/visualEffectDuration | 91–101 | Геометрия и срок визуального эффекта | Вложенные name-пути | Показываются при createTemplate===true; размер text, срок number |
| damage/shield/heal | 106–119 | Текст формул | name=system.* | Показываются по своим checkbox; falsy значение в UI заменяется на 1d6+0 |

## Основные функции и методы

Функций JavaScript нет. if/eq/unless управляют набором полей; selectOptions использует selects.domain/templateType. Обновление модели выполняет форма базового листа.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| eq/and/or/includes/getSetting/window | [module/setup/handlebars.js](../../../../../../../module/setup/handlebars.js) | Системные helpers | Условия, CSV типов изображений и доступ к game.user | Определения 94–128 прочитаны |
| clickableImageItemTypes/clickableImageCheckboxForGMOnly | [module/setup/settings.js](../../../../../../../module/setup/settings.js) | Настройки через helpers | Условия checkbox картинки | default valuable / true |
| localize, checked, selectOptions; if/unless/each | Foundry14.367.0, client/applications/handlebars.mjs; Handlebars4.7.9 | Helpers/шаблонизация | Поля и условия | HBS исполнялся; UI helpers заменены по прочитанному контракту |
| Ключи WITCHER.* | [lang/en.json](../../../../../../../lang/en.json); [lang/ru.json](../../../../../../../lang/ru.json) | Локализация | Подписи и title | Literal-ключи проверены; динамические перечислены отдельно |
| WitcherItemSheet | [module/item/sheets/WitcherItemSheet.js](../../../../../../../module/item/sheets/WitcherItemSheet.js) | Базовый контекст/форма | item, config, showConfig; submitOnChange/configureItem | _prepareContext/DEFAULT_OPTIONS |
| WitcherSpellSheet | [module/item/sheets/WitcherSpellSheet.js](../../../../../../../module/item/sheets/WitcherSpellSheet.js) | Контекст/загрузчик | selects.domain/templateType | createSelects и PARTS.main |
| SpellData | [module/data/item/spellData.js](../../../../../../../module/data/item/spellData.js) | Контракт полей | Поля модели | Проверены schema и условия |
| spell-header.hbs | [templates/partials/spell-header.hbs](../../../../../../../templates/partials/spell-header.hbs) | Partial | 2 | Настоящее включение при рендере |
| TemplateProperties | [module/data/item/templates/regions/templatePropertiesData.js](../../../../../../../module/data/item/templates/regions/templatePropertiesData.js) | Вложенная схема | Четыре templateProperties поля | String/Number/Boolean сверены |
| castSpellMixin | [module/actor/mixins/castSpellMixin.js](../../../../../../../module/actor/mixins/castSpellMixin.js) | Потребитель настроек | damage/shield/heal/STA | Проверены входные обращения и ветка переменного лечения |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/item/sheets/WitcherSpellSheet.js](../../../../../../../module/item/sheets/WitcherSpellSheet.js) | Этот HBS | PARTS.main | 10 |

Область поиска: module/ и templates/ текущего checkout; регистрация сверена с system.json. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Шаблон читает значения; сам не присваивает их и не стирает скрытые поля. Начальное отображение 1d6+0 — HTML value, а не initial модели (damage=null, shield/heal=''). Момент записи зависит от submitOnChange. Поля текстового эффекта не создают ActiveEffect автоматически.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Все условия | Группа 11: 4 класса×2 STA-режима; признаки true | Поле стоимости скрывается, дар меняет range/sideEffect, Witcher добавляет domain; формулы имеют UI-default | DOM браузера/сохранение не запускались |
| Контракты | Полное чтение 125 строк; поля модели/лист/partial | Пути области актуальны; damage/shield/heal строки | Непроверенное правило применения не выводится из интерфейса |

## Непроверенные участки и открытые вопросы

Исходник и указанные связи сопоставлены в TASK-0004.009. Настоящее сохранение checkbox/формул, живые Region/ресурсы и полный боевой цикл не проверены. Остаток: [U009-01](../../../../cross-check-0002.md#u009-01), [U009-02](../../../../cross-check-0002.md#u009-02), [U009-04](../../../../cross-check-0002.md#u009-04), [U009-07](../../../../cross-check-0002.md#u009-07). Новых поведенческих запусков нет; прежние протоколы сохраняют даты и фасады.

## Связанные проблемы

[issue-00063](../../../../../../issues/potential/issue-00063.md), [issue-00074](../../../../../../issues/potential/issue-00074.md), [issue-00075](../../../../../../issues/potential/issue-00075.md), [issue-00134](../../../../../../issues/potential/issue-00134.md), [issue-00137](../../../../../../issues/closed/issue-00137.md). 63/137 идут через заголовок/словари; 74/75 — конфигурация области; 134 — выполнение доступной комбинации doesHeal+staminaIsVar.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `a29234e7c42ef5f9d8095c2b5470e5e3c95824cc`; полный файл | Первая карточка; [сверка порции](../../../../review-log.md#task-0003021) |

## Уточнение TASK-0003.022

2026-09-11, `ef8117ba6e5a184989e65761d47a068381056e4a`; исходник не изменён.

Четыре вложенных поля templateProperties подтверждены схемой. Срок visualEffectDuration запускает клиентский таймер, а поле system.duration через castSpell попадает в отдельный flags.duration и счётчик боя. Их синхронизация этой формой не выполняется. Геометрия/жизненный цикл теперь полностью описаны в .022.

Связанные карточки: [module/data/item/templates/regions/templatePropertiesData.js](../../../module/data/item/templates/regions/templatePropertiesData.js.md).

[Результаты и пределы сверки](../../../../review-log.md#task-0003022).

## Сквозная сверка TASK-0004.009

2026-09-14; rusbar-main, 7adc2362937779de0c03957aacf73ff2cf13e211. Исходник совпадает со срезом TASK-0001; изменено только описание.

Spell HBS подключает header и записывает вложенный templateProperties, в отличие от Ritual. Четыре независимых флага области/урона/щита/лечения открывают разные поля; default формулы в input не является валидацией выражения. Дальнейшее лечение/щит разобраны до кнопок и числового consumer.

Сопоставленные определения и потребители: [module/setup/handlebars.js](../../../module/setup/handlebars.js.md), [module/setup/settings.js](../../../module/setup/settings.js.md), [lang/en.json](../../../lang/en.json.md), [lang/ru.json](../../../lang/ru.json.md), [module/item/sheets/WitcherItemSheet.js](../../../module/item/sheets/WitcherItemSheet.js.md), [module/item/sheets/WitcherSpellSheet.js](../../../module/item/sheets/WitcherSpellSheet.js.md), [module/data/item/spellData.js](../../../module/data/item/spellData.js.md), [templates/partials/spell-header.hbs](../../partials/spell-header.hbs.md), [module/data/item/templates/regions/templatePropertiesData.js](../../../module/data/item/templates/regions/templatePropertiesData.js.md), [module/actor/mixins/castSpellMixin.js](../../../module/actor/mixins/castSpellMixin.js.md).

[Протокол и границы](../../../../review-log.md#task-0004009) — TASK-0004.009; процессы [R009-03](../../../../cross-check-0002.md#r009-03), [R009-12](../../../../cross-check-0002.md#r009-12). В этой порции выполнена статическая сверка; прежние опыты сохраняют свои даты и фасады. Новых поведенческих запусков нет; браузер, мир, сеть и запись в БД не запускались.
