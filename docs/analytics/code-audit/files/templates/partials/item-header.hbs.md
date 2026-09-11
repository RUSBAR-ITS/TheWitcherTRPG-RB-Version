# templates/partials/item-header.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/partials/item-header.hbs](../../../../../../templates/partials/item-header.hbs) |
| Тип файла | Handlebars, HTML-шаблон |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `07237960627bf7debc2b4283aa55d1a8c5d1bb8b` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.011](../../../../../tasks/task-0003.011.md), одна порция из семи файлов |
| Запись перекрёстной сверки | [TASK-0003.011](../../../review-log.md#task-0003011) |

## Назначение файла

Общая шапка десяти предметных форм: имя, настройка, редактируемая картинка, количество/масса, цена либо тип мутагена и книга-источник.

## Условия использования

Предзагружается в [module/setup/handlebars.js](../../../../../../module/setup/handlebars.js) и включается partial-вызовом без переименования контекста. [module/item/sheets/WitcherItemSheet.js](../../../../../../module/item/sheets/WitcherItemSheet.js) передаёт item/config/showConfig; MutagenSheet дополнительно записывает config.type. Флажок картинки показывается, если тип есть в CSV-настройке и пользователь GM либо выключено ограничение только для GM. Это условие видимости checkbox, не проверка прав на запись документа.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| header.item-header / input[name=name] | 1–7 | Заголовок и имя Item | Partial | Изменение имени через стандартную форму |
| configure-item[data-action=configureItem] | 4–6 | Открыть отдельную конфигурацию | Условие showConfig | Действие WitcherItemSheet._renderConfigureDialog |
| img.profile-img[data-action=editImage][data-edit=img] | 10–21 | Изменить путь img | В обеих ветвях картинки | Действие DocumentSheetV2, не _onItemShow |
| system.clickableImage / clickable-image-<item._id> | 10–17 | Переключатель увеличения картинки в списках | Условие типа/GM/настройки | Checkbox поля нет в проверенной модели; см. issue-00063 |
| system.quantity, system.weight | 24–39 | Количество и вес | input text с data-dtype=Number | quantity в CommonItemData — StringField, weight — NumberField |
| system.type / system.cost | 41–60 | Тип мутагена либо цена | Взаимоисключающие ветви item.type==mutagen | type через config.type/selectOptions; cost input с data-dtype=Number |
| system.sourcebook | 61–68 | Книга-источник | input text | StringField общей модели |

## Основные функции и методы

JavaScript-функций нет. Шаблон вычисляет условия Handlebars и создаёт разметку; обработчики и запись документов принадлежат указанным ниже файлам.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| item, showConfig, config | [module/item/sheets/WitcherItemSheet.js](../../../../../../module/item/sheets/WitcherItemSheet.js) | Контекст | 3–66; document и настройка | _prepareContext:45–58; шапка отрендерена в 12 комбинациях |
| getSetting/includes/window | [module/setup/handlebars.js](../../../../../../module/setup/handlebars.js) | Helpers | 10; CSV разбивается по запятым и trim, window.game.user.isGM | Исполнены исходные три helper |
| clickableImageItemTypes / clickableImageCheckboxForGMOnly | [module/setup/settings.js](../../../../../../module/setup/settings.js) | Чтение world-настроек | 10; defaults valuable / true | 69–84; различены тип String и Boolean |
| quantity/weight/cost/sourcebook; clickableImage | [module/data/item/commonItemData.js](../../../../../../module/data/item/commonItemData.js) | Пути полей | 30,38,57,66 и14 | Все поля, кроме clickableImage, определены; настоящая модель не сохраняет неизвестный флаг |
| config.type / type | [module/item/sheets/WitcherMutagenSheet.js](../../../../../../module/item/sheets/WitcherMutagenSheet.js); [module/data/item/mutagenData.js](../../../../../../module/data/item/mutagenData.js) | Контекст/поле | 42–49; red/green/blue | Конфигурация передаётся по ссылке; получение списка прочитано |
| configureItem | [module/item/sheets/WitcherItemSheet.js](../../../../../../module/item/sheets/WitcherItemSheet.js) | data-action | 5→DEFAULT_OPTIONS.actions→_renderConfigureDialog | Показ зависит только от showConfig |
| editImage / form submit / FormDataExtended | Foundry14.367 /opt/foundryvtt/client/applications/api/document-sheet.mjs; /opt/foundryvtt/client/applications/ux/form-data-extended.mjs | Внешний обработчик/форма | 11/19; FilePicker обновляет src и отправляет форму; data-edit=img | Код ядра прочитан; полный FilePicker/submit не исполнялся |
| checked/selectOptions/localize/and/or/eq | Foundry Handlebars + [module/setup/handlebars.js](../../../../../../module/setup/handlebars.js) | Helpers | Условия, checkbox, подписи и список | Рендер Handlebars; selectOptions представлен фасадом, точные подписи проверены по en/ru |
| WITCHER.Item.ClickableImage/Quantity/Weight/Cost/SourceBook, WITCHER.Type | [lang/en.json](../../../../../../lang/en.json); [lang/ru.json](../../../../../../lang/ru.json) | Локализация | 16,27,35,44,54,63 | Ключи/подписи сверены; placeholder Name задан литералом |
| .item-header/.item-header-tablerow | [styles/item-header.css](../../../../../../styles/item-header.css); [styles/witcher-styles.css](../../../../../../styles/witcher-styles.css) | CSS/импорт | 1,25,33,41,61 | Стиль подключён через главный CSS; визуальная проверка не выполнялась |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/setup/handlebars.js](../../../../../../module/setup/handlebars.js) | Путь partial | Предзагрузка:50 | Список содержит путь |
| [templates/sheets/item/alchemical-sheet.hbs](../../../../../../templates/sheets/item/alchemical-sheet.hbs) | item-header | Прямое включение на строке2 | 10 совпадений поиска по templates |
| [templates/sheets/item/armor-sheet.hbs](../../../../../../templates/sheets/item/armor-sheet.hbs) | item-header | Прямое включение на строке2 | 10 совпадений поиска по templates |
| [templates/sheets/item/component-sheet.hbs](../../../../../../templates/sheets/item/component-sheet.hbs) | item-header | Прямое включение на строке2 | 10 совпадений поиска по templates |
| [templates/sheets/item/container-sheet.hbs](../../../../../../templates/sheets/item/container-sheet.hbs) | item-header | Прямое включение на строке2 | 10 совпадений поиска по templates |
| [templates/sheets/item/diagrams-sheet.hbs](../../../../../../templates/sheets/item/diagrams-sheet.hbs) | item-header | Прямое включение на строке2 | 10 совпадений поиска по templates |
| [templates/sheets/item/enhancement-sheet.hbs](../../../../../../templates/sheets/item/enhancement-sheet.hbs) | item-header | Прямое включение на строке2 | 10 совпадений поиска по templates |
| [templates/sheets/item/mount-sheet.hbs](../../../../../../templates/sheets/item/mount-sheet.hbs) | item-header | Прямое включение на строке2 | 10 совпадений поиска по templates |
| [templates/sheets/item/mutagen-sheet.hbs](../../../../../../templates/sheets/item/mutagen-sheet.hbs) | item-header | Прямое включение на строке2 | 10 совпадений поиска по templates |
| [templates/sheets/item/valuable-sheet.hbs](../../../../../../templates/sheets/item/valuable-sheet.hbs) | item-header | Прямое включение на строке2 | 10 совпадений поиска по templates |
| [templates/sheets/item/weapon-sheet.hbs](../../../../../../templates/sheets/item/weapon-sheet.hbs) | item-header | Прямое включение на строке2 | 10 совпадений поиска по templates |

## Данные и изменения состояния

Имена полей: name, system.clickableImage, system.quantity, system.weight, system.type, system.cost, system.sourcebook; img передаётся через data-edit. Handlebars экранирует строки стандартным выводом. Взаимоисключающие ветви оставляют один img и одно из type/cost. В шаблоне нет собственного submit/action-кода. Checked=true в изолированной матрице не доказывает сохранение флага: в настоящих проверенных Item-моделях clickableImage отсутствует.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Ветви | 12 рендеров: GM×ограничение GM×3 типа; ещё showConfig=false | Checkbox только для разрешённого типа/пользователя; у mutagen только type, у остальных cost; всегда один editImage | Исполнены исходные helpers; модель кнопки/браузер не запускались |
| Схема | CommonItemData и 4 настоящие специализированные модели с clickableImage=true | quantity StringField; прочие известные поля согласованы; флаг не попал в подготовленные данные/toObject | Не выполнялась запись Item в мир |
| Потребители | rg item-header.hbs в module/templates | 1 предзагрузка + 10 прямых partial-включений | Не проверены внешние модули/переопределения шаблонов |

## Непроверенные участки и открытые вопросы

Все 71 строка прочитана. Не исполнялись полноценный FormDataExtended, FilePicker и серверное сохранение. Неизвестно влияние внешних модулей на schema/clickableImage. Отдельная картинка item-image.hbs обслуживает инвентарь и не включена этой шапкой; два действия просмотра/редактирования изображения не смешиваются.

## Связанные проблемы

[issue-00063](../../../../../issues/potential/issue-00063.md) — разрывы цепочки clickableImage между checkbox, схемой и текущим инвентарём.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.011 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.

## Уточнение TASK-0003.015

2026-09-10, `7edb814aa870da75c7ad7633536e899a8d07e205`; исходник неизменен. [Перекрёстная сверка](../../../review-log.md#task-0003015).

Полностью разобраны формы [templates/sheets/item/alchemical-sheet.hbs](../../../../../../templates/sheets/item/alchemical-sheet.hbs), [templates/sheets/item/mutagen-sheet.hbs](../../../../../../templates/sheets/item/mutagen-sheet.hbs), [templates/sheets/item/valuable-sheet.hbs](../../../../../../templates/sheets/item/valuable-sheet.hbs). Для mutagen ветка header заменяет cost на system.type и получает red/green/blue из WitcherMutagenSheet.getTypes. Настоящий HBS во всех трёх вариантах даёт один selector типа. Проблема мутагена относится к неподключённой configuration расходования, а не к выбору цвета. Стандартная clickableImageItemTypes добавляет checkbox мутагену и valuable; отсутствие поля модели остаётся в issue-00063.

## Уточнение TASK-0003.016

2026-09-10, `53f74994011383cb544cabac96285430f00cb38a`; исходник неизменен. [Перекрёстная сверка](../../../review-log.md#task-0003016).

Полностью описаны [templates/sheets/item/component-sheet.hbs](../../../../../../templates/sheets/item/component-sheet.hbs) и [templates/sheets/item/diagrams-sheet.hbs](../../../../../../templates/sheets/item/diagrams-sheet.hbs), включающие общую шапку. Стандартная clickableImageItemTypes не добавляет checkbox этим двум типам. В диагностике компонент с временным helper select имел 10 собственных+общих именованных полей, либо 11 для substances. Рецепт со связанным результатом — 12/20 в двух режимах; editor.description проверен отдельно как фасад. Это числа шаблонов, не успешный штатный рендер component.

## Уточнение TASK-0003.024

2026-09-11, `66cd03705dbc398eba0026284a298b5fbe337035`; исходник не изменился. Форма контейнера включает шапку без отдельного hash-контекста. Настоящий HBS отрендерен вместе с общей шапкой и context item/data/config/showConfig; system-пути соответствуют 11 полям ContainerData при обычном контейнере. Общая configuration доступна, image использует editImage. Helpers настроек/права окна подменены; вариант clickableImage для контейнера не включался и не подтверждён этой проверкой.

Связанные карточки: [templates/sheets/item/container-sheet.hbs](../sheets/item/container-sheet.hbs.md), [module/data/item/containerData.js](../../module/data/item/containerData.js.md).

[Перекрёстная сверка порции](../../../review-log.md#task-0003024). Мир, БД, код и метаданные доступа не менялись.
