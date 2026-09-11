# templates/sheets/item/ritual-sheet.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/sheets/item/ritual-sheet.hbs](../../../../../../../templates/sheets/item/ritual-sheet.hbs) |
| Тип файла | Handlebars |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `a29234e7c42ef5f9d8095c2b5470e5e3c95824cc` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.021](../../../../../../tasks/task-0003.021.md), 13 файлов, 936 логических строк |
| Запись перекрёстной сверки | [TASK-0003.021](../../../../review-log.md#task-0003021) |

## Назначение файла

Основная форма ритуала: описательные параметры, устаревшие поля области и две редактируемые таблицы компонентов.

## Условия использования

PARTS.main WitcherRitualSheet. Контекст содержит item.system и selects; prepareDerivedData модели создаёт массивы представления. Плюс событийные обработчики базового/ритуального листа.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| name/configureItem/img/clickableImage/sourcebook/cost/level | 3–54 | Заголовок, конфигурация, картинка и общие поля | Обычные name; configureItem; settings | Кнопка конфигурации без if showConfig; costtext data-dtypeNumber; img без action |
| staminaIsVar/stamina/preparationTime/difficultyCheck/duration/effect | 60–80 | Стоимость, время подготовки, DC, длительность, описание | system.* | STA скрывается при переменном режиме; DC/text, не Roll |
| createTemplate/templateSize/templateType/visualEffectDuration | 85–110 | Прежние параметры области | name=system.<поле> без templateProperties | Условия тоже используют старый createTemplate |
| components | textarea119 | Свободное описание состава | system.components | Не синхронизируется автоматически со списками |
| .ritualComponents/.alternateComponents | 121–160 | Контейнеры списков и зона выбора Drop | each по ritualComponents/alternateRitualComponents | Модель создаёт записи {item, quantity, img} |
| tr.list-item dataset.uuid/target | 125, 145 | Адрес строки для edit/remove | UUID от component.item.uuid; target основной/альтернативный uuid-массив | Не отдельный ID записи |
| .remove-component/.edit-component | 127–135, 147–155 | Удаление ссылки и число quantity | click/blur в WitcherRitualSheet; data-field=quantity | Удаление имеет title с начальным пробелом; inputnumber data-dtypeNumber без name |

## Основные функции и методы

Функций JavaScript нет. if/unless/eq скрывают поля; each строит строки двух таблиц; selectOptions отображает уровень/тип области. Drop определяется DOM-контейнером, а не именами полей.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| eq/and/or/includes/getSetting/window | [module/setup/handlebars.js](../../../../../../../module/setup/handlebars.js) | Системные helpers | Условия, CSV типов изображений и доступ к game.user | Определения 94–128 прочитаны |
| clickableImageItemTypes/clickableImageCheckboxForGMOnly | [module/setup/settings.js](../../../../../../../module/setup/settings.js) | Настройки через helpers | Условия checkbox картинки | default valuable / true |
| localize, checked, selectOptions; if/unless/each | Foundry14.367.0, client/applications/handlebars.mjs; Handlebars4.7.9 | Helpers/шаблонизация | Поля и условия | HBS исполнялся; UI helpers заменены по прочитанному контракту |
| Ключи WITCHER.* | [lang/en.json](../../../../../../../lang/en.json); [lang/ru.json](../../../../../../../lang/ru.json) | Локализация | Подписи и title | Literal-ключи проверены; динамические перечислены отдельно |
| WitcherItemSheet | [module/item/sheets/WitcherItemSheet.js](../../../../../../../module/item/sheets/WitcherItemSheet.js) | Базовый контекст/форма | item, config, showConfig; submitOnChange/configureItem | _prepareContext/DEFAULT_OPTIONS |
| WitcherRitualSheet | [module/item/sheets/WitcherRitualSheet.js](../../../../../../../module/item/sheets/WitcherRitualSheet.js) | Загрузчик/обработчики | Контекст/Drop/edit/remove | Все dataset/селекторы сверены |
| RitualData | [module/data/item/ritualData.js](../../../../../../../module/data/item/ritualData.js) | Схема/подготовка | Оба массива и старые пути области | Модель содержит templateProperties; резервный item содержит только name |
| component() | [module/data/item/templates/componentData.js](../../../../../../../module/data/item/templates/componentData.js) | Схема записей | uuid/quantity | Нет ID строки/img/name |
| TemplateProperties | [module/data/item/templates/regions/templatePropertiesData.js](../../../../../../../module/data/item/templates/regions/templatePropertiesData.js) | Актуальная вложенная схема | 4 поля области | Несовпадение имён формы подтверждено |
| DocumentSheetV2/ApplicationV2 | Foundry14.367.0 client/applications/api/document-sheet.mjs / application.mjs | Внешние действия | editImage/формы | Проверено чтением маршрутизации |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/item/sheets/WitcherRitualSheet.js](../../../../../../../module/item/sheets/WitcherRitualSheet.js) | Этот HBS; CSS-селекторы и dataset | PARTS.main, blur/click, Drop | 6, 37–80 |

Область поиска: module/ и templates/ текущего checkout; регистрация сверена с system.json. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Обычные поля сохраняются общей формой; quantity не имеет name и записывается вручную на blur. Отображаемое имя/UUID строки берётся из разрешённого документа. При неизвестной ссылке имя показывает исходный UUID, но dataset.uuid пуст. Таблица не различает две записи одного документа. Скрытие старых полей области не означает отсутствия области в актуальной модели.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Область | Группа 12 | Актуальный createTemplate=true не показывает старые size/type/duration; legacy checkbox не связан с schema | Сохранение мира не проверялось |
| Компоненты | Группы 06–09 | Оба списка; отсутствующий UUID ломает edit/remove; duplicate меняет первую/удаляет все | DOM-события и update заменены |
| Контекст/локализация | Группы 10, 15 | Типы/уровни и quantity выведены; RemoveComponent с пробелом не локализован; картинки без action | Нет полного браузерного цикла |

## Непроверенные участки и открытые вопросы

Все 161 строка прочитана. Изменение массива в активном мире и взаимодействие нескольких окон не запускались.

## Связанные проблемы

[issue-00063](../../../../../../issues/potential/issue-00063.md), [issue-00098](../../../../../../issues/potential/issue-00098.md), [issue-00129](../../../../../../issues/potential/issue-00129.md), [issue-00130](../../../../../../issues/potential/issue-00130.md), [issue-00131](../../../../../../issues/potential/issue-00131.md), [issue-00132](../../../../../../issues/potential/issue-00132.md), [issue-00136](../../../../../../issues/potential/issue-00136.md), [issue-00137](../../../../../../issues/potential/issue-00137.md). 98 дополнена обеими кнопками; 129–132 фиксируют несовпадения формы/модели/обработчиков; 136/137 — изображения и подписи.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `a29234e7c42ef5f9d8095c2b5470e5e3c95824cc`; полный файл | Первая карточка; [сверка порции](../../../../review-log.md#task-0003021) |

## Уточнение TASK-0003.022

2026-09-11, `ef8117ba6e5a184989e65761d47a068381056e4a`; исходник не изменён.

Актуальная TemplateProperties содержит четыре прежних поля под вложенным объектом; формы здесь используют верхние пути и условия. Подтверждена граница issue129 без нового ID. Исправная схема вложенной области не исправляет привязки HBS автоматически.

Связанные карточки: [module/data/item/templates/regions/templatePropertiesData.js](../../../module/data/item/templates/regions/templatePropertiesData.js.md).

[Результаты и пределы сверки](../../../../review-log.md#task-0003022).
