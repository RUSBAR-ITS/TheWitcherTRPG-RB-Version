# module/item/sheets/configurations/WitcherConfigurationSheet.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/item/sheets/configurations/WitcherConfigurationSheet.js](../../../../../../../../module/item/sheets/configurations/WitcherConfigurationSheet.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `07237960627bf7debc2b4283aa55d1a8c5d1bb8b` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.011](../../../../../../../tasks/task-0003.011.md), одна порция из семи файлов |
| Запись перекрёстной сверки | [TASK-0003.011](../../../../../review-log.md#task-0003011) |

## Назначение файла

Создаёт отдельную форму базовых настроек Item и встроенных ActiveEffect. Предоставляет части header/general/activeEffects и навигацию; группирует эффекты и обслуживает четыре действия над документами.

## Условия использования

Экземпляр создаёт [module/item/sheets/WitcherItemSheet.js](../../../../../../../../module/item/sheets/WitcherItemSheet.js) в поле configuration; действие configureItem открывает его. Класс напрямую наследует HandlebarsApplicationMixin(ItemSheetV2), а не WitcherItemSheet. Поэтому получает dropItemSheetData и перенос ActiveEffect из ядра, не системный Drop-router. Прямые наследники конфигурации: Properties, Consumable, Profession; Armor и Spell наследуются через Properties. Сам класс отдельно через registerSheets не регистрируется.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| WitcherConfigurationSheet | Класс,4–143 | Общая конфигурация Item | default export | Создание при создании основного листа; подготовка/рендер; actions |
| HandlebarsApplicationMixin / ItemSheetV2 | Aliases,1–2 | Базовый UI/API Item | Локальные const | Наследуемые drag/drop, форма и item getter |
| DEFAULT_OPTIONS | 6–25 | 520×480, классы, submitOnChange=true, closeOnSubmit=false | Static | Четыре действия с одним static handler |
| PARTS | 27–43 | header, tabs, general, activeEffects | Static | Три системных шаблона; tabs — templates/generic/tab-navigation.hbs ядра |
| TABS.primary | 45–51 | general/activeEffects, initial=general, labelPrefix WITCHER.Item.Settings | Static | Контекст вкладок формирует ApplicationV2 |
| Категории temporary/passive/inactive/temporaryItemImprovement | 76–97 | Контейнеры effects[] с type/label | Новые объекты при каждом prepareActiveEffectCategories | Ссылки на существующие эффекты; копии документов не создаются |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| _prepareContext;54–66 | options, document.system.schema/effects | Promise<context> | super → config, item, effects categories, systemFields | Добавляет item-type в options.classes; не вычисляет enrichedText и showConfig; DB не пишет |
| prepareActiveEffectCategories;74–108 | Итерируемые эффекты | Четыре категории | Порядок: disabled → не применённое temporaryItemImprovement → isTemporary → passive | Suppressed отдельно не исключается; isAppliedTemporaryItemImprovement читается только во второй ветви |
| static onManageActiveEffect;116–142 | event, element[data-action] внутри li | Promise<создание/рендер/удаление/обновление/undefined> | Берёт effectId из ближайшего li и effect из this.document.effects; create/edit/delete/toggle | Возвращает nested Promise, в отличие от ручных system.effects методов; нет catch и guard отсутствующего effect |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| ItemSheetV2, item, _dragDrop, _onDropActiveEffect | Foundry14.367 /opt/foundryvtt/client/applications/sheets/item-sheet.mjs | Наследование | 4; здесь методы не заменены | Прочитаны исходники, Drop-сценарий исполнен изолированно |
| HandlebarsApplicationMixin / DocumentSheetV2 / ApplicationV2 | Foundry14.367 /opt/foundryvtt/client/applications/api/handlebars-application.mjs; /opt/foundryvtt/client/applications/api/document-sheet.mjs; /opt/foundryvtt/client/applications/api/application.mjs | Форма/части/действия | PARTS/TABS, submitOnChange, права редактирования, click-dispatch | Унаследованные права и запись отличены от тела этого класса |
| CONFIG.WITCHER | [module/setup/config.js](../../../../../../../../module/setup/config.js) | Глобальное чтение | 56; selectOptions general и локализация | Сверено с заголовками и полями |
| document.system.schema.fields | [module/setup/registerDataModels.js](../../../../../../../../module/setup/registerDataModels.js); [module/data/item/commonItemData.js](../../../../../../../../module/data/item/commonItemData.js) | Типизированная модель | 64; формирование formGroup | Настоящие схемы всех 22 зарегистрированных Item исследованы для выбора полей |
| document.effects / createEmbeddedDocuments / update | [module/item/witcherItem.js](../../../../../../../../module/item/witcherItem.js); Foundry Item API | Чтение/запись | 62,119,122; владельцем действия служит document | Создание ActiveEffect перехвачено; обновления не исполнялись в БД |
| disabled, isTemporary, isTemporaryItemImprovement, isAppliedTemporaryItemImprovement | [module/activeEffect/witcherActiveEffect.js](../../../../../../../../module/activeEffect/witcherActiveEffect.js); [module/data/activeEffects/witcherActiveEffectData.js](../../../../../../../../module/data/activeEffects/witcherActiveEffectData.js); [module/data/activeEffects/witcherTemporaryItemImprovementData.js](../../../../../../../../module/data/activeEffects/witcherTemporaryItemImprovementData.js) | Поля/getters эффекта | 100–105; категоризация | Сверено с TASK-0003.009, порядок проверен на шести случаях |
| header / general / activeEffects | [templates/sheets/item/configuration/tabs/header.hbs](../../../../../../../../templates/sheets/item/configuration/tabs/header.hbs); [templates/sheets/item/configuration/tabs/general.hbs](../../../../../../../../templates/sheets/item/configuration/tabs/general.hbs); [templates/sheets/item/configuration/tabs/activeEffectConfiguration.hbs](../../../../../../../../templates/sheets/item/configuration/tabs/activeEffectConfiguration.hbs) | PARTS→шаблоны | 29,36,40 | Все три полностью разобраны |
| effectId/effectType/data-action | [templates/partials/effect-part.hbs](../../../../../../../../templates/partials/effect-part.hbs) | DOM→handler | 118–140; header li для create и effect row для остальных | partial возвращает эти атрибуты; parentUuid здесь не используется |
| effect.sheet.render | [module/activeEffect/WitcherActiveEffectSheet.js](../../../../../../../../module/activeEffect/WitcherActiveEffectSheet.js); [module/setup/registerSheets.js](../../../../../../../../module/setup/registerSheets.js) | Динамический зарегистрированный лист | 136; edit | Запись оборачивается ядром в соответствующий лист |
| WITCHER.activeEffect.* / WITCHER.Item.Settings.* | [lang/en.json](../../../../../../../../lang/en.json); [lang/ru.json](../../../../../../../../lang/ru.json) | Локализация | 79–94, TABS labelPrefix | Ключи en/ru прочитаны; локализации полностью не разбирались |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/item/sheets/WitcherItemSheet.js](../../../../../../../../module/item/sheets/WitcherItemSheet.js) | WitcherConfigurationSheet | Импорт, new configuration:1/42; render:168 | Создаётся для того же Item |
| [module/item/sheets/configurations/WitcherPropertiesConfigurationSheet.js](../../../../../../../../module/item/sheets/configurations/WitcherPropertiesConfigurationSheet.js) | WitcherConfigurationSheet | Прямое extends, super контекст, расширение PARTS/TABS/actions | Поиск imports/extends |
| [module/item/sheets/configurations/WitcherConsumableConfigurationSheet.js](../../../../../../../../module/item/sheets/configurations/WitcherConsumableConfigurationSheet.js) | WitcherConfigurationSheet | Прямое extends, super контекст, расширение PARTS/TABS/actions | Поиск imports/extends |
| [module/item/sheets/configurations/WitcherProfessionConfigurationSheet.js](../../../../../../../../module/item/sheets/configurations/WitcherProfessionConfigurationSheet.js) | WitcherConfigurationSheet | Прямое extends, super контекст, расширение PARTS/TABS/actions | Поиск imports/extends |
| [module/item/sheets/configurations/WitcherArmorConfigurationSheet.js](../../../../../../../../module/item/sheets/configurations/WitcherArmorConfigurationSheet.js) | Унаследованная основа через Properties | Замена general-части | Точечная сверка цепочки наследования |
| [module/item/sheets/configurations/WitcherSpellConfigurationSheet.js](../../../../../../../../module/item/sheets/configurations/WitcherSpellConfigurationSheet.js) | Унаследованная основа через Properties | Замена general-части | Точечная сверка цепочки наследования |
| [templates/sheets/item/configuration/tabs/general.hbs](../../../../../../../../templates/sheets/item/configuration/tabs/general.hbs); [templates/sheets/item/configuration/tabs/activeEffectConfiguration.hbs](../../../../../../../../templates/sheets/item/configuration/tabs/activeEffectConfiguration.hbs) | item/config/systemFields/effects/tabs | Контекст форм и списка | Поля и категории сверены |

## Данные и изменения состояния

create отправляет type=base либо temporaryItemImprovement; name, icon и origin берутся из Item. duration.value равен 1 для temporary, null для других категорий; units, start, transfer и system.changes в payload не заданы и определяются ядром/моделью. disabled=true только для inactive. Сам create не создаёт строк изменений. edit открывает effect.sheet, delete удаляет документ, toggle инвертирует e.disabled. Обращения к parentUuid из HTML нет — ищется effectId только в текущем Item.

Нет собственного слушателя .effect-display, хотя partial скрывает description. Нет собственного isEditable guard у actions; базовая форма и права документа проверяются ядром. Непосредственный вызов handler в изоляции не доказывает обход прав в Foundry.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Состав | 143 строки; три собственных метода, три static-конфигурации, четыре категории | Все определения и три прямых наследника сверены | Остальные методы наследников вне полного разбора |
| Группировка | Исходный метод на 6 комбинациях свойств | disabled→inactive; не применённое улучшение→спецкатегория; применённое→passive; temporary→temporary; suppressed остаётся passive | Объекты эффекта контролируемые |
| Действия | Четыре create + edit/toggle/delete | Payload type/duration/disabled соответствует категории; возврат nested API сохранён | API документов и sheet.render перехвачены |
| Шаблоны | General со схемами 22 моделей, ActiveEffect partial в реальном Handlebars | Поля условны; описание FX остаётся invisible; стандартные actions присутствуют | toFormGroup представлен фасадом, не полной DOM-формой |

## Непроверенные участки и открытые вопросы

Весь исходник прочитан. Не проверены полноценный submit, одновременное открытие основного листа и конфигурации, внешние listeners, стили и сетевые ошибки. Действие над исчезнувшим effect предполагает его наличие; штатный браузерный сценарий такой гонки не моделировался. Настоящее сохранение duration/defaults не выводится из перехваченного payload.

## Связанные проблемы

[issue-00056](../../../../../../../issues/potential/issue-00056.md), [issue-00059](../../../../../../../issues/potential/issue-00059.md), [issue-00061](../../../../../../../issues/potential/issue-00061.md), [issue-00062](../../../../../../../issues/potential/issue-00062.md). В issue-00059 конфигурация является контрольным маршрутом ядра, обход hook относится к основному WitcherItemSheet.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.011 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.

## Уточнение TASK-0003.013

2026-09-10, `8cca18e14b75ec53028ee6bc49a837597de4d9af`; исходник неизменен. [Перекрёстная сверка](../../../../../review-log.md#task-0003013).

Полностью разобран [module/item/sheets/configurations/WitcherPropertiesConfigurationSheet.js](../../../../../../../../module/item/sheets/configurations/WitcherPropertiesConfigurationSheet.js): добавлены три описателя PARTS, пять записей TABS.primary до фильтрации и настройка silverTrait в context. Его addEffect/removeEffect и change/editEffect изменяют TypedObjectField system.damageProperties.effects. Управление документами ActiveEffect остаётся у базовой конфигурации и относится к другой структуре данных. Сверка фильтрации выявила расхождение региональной навигации и PARTS ([issue-00074](../../../../../../../issues/potential/issue-00074.md)); отсутствие поля внутри шаблона описано отдельно.

## Уточнение TASK-0003.015

2026-09-10, `7edb814aa870da75c7ad7633536e899a8d07e205`; исходник неизменен. [Перекрёстная сверка](../../../../../review-log.md#task-0003015).

Полностью разобран прямой наследник [module/item/sheets/configurations/WitcherConsumableConfigurationSheet.js](../../../../../../../../module/item/sheets/configurations/WitcherConsumableConfigurationSheet.js). Он расширяет PARTS и TABS вкладкой consumableProperties и добавляет собственные actions/listeners. Базовая configuration продолжает обслуживать документы Item.effects, в то время как consumableProperties содержит обычные массивы записей статусов. [module/item/sheets/WitcherMutagenSheet.js](../../../../../../../../module/item/sheets/WitcherMutagenSheet.js) оставляет этот базовый класс без новой вкладки; общая general не выводит isConsumable/consumeProperties.

## Уточнение TASK-0003.018

2026-09-10, `rusbar-main`, `29319a7a7e1dfc0663edbc15166f3b6a19682a2f`. Для [race](../../../../../../../../module/data/item/raceData.js) и [homeland](../../../../../../../../module/data/item/homelandData.js) общий шаблон general не вывел именованных полей, поскольку в схемах нет attack/damage/defense. При этом конфигурация содержит четыре категории ActiveEffect. Прямой вызов настоящего onManageActiveEffect для passive обеих моделей передал запрос createEmbeddedDocuments с name/icon/origin/duration/disabled; явные transfer и changes в этом payload отсутствуют. Запросы перехвачены, документы в БД не создавались. Доступность редактора эффекта не означает наличия настроенного воздействия.

[Перекрёстная сверка](../../../../../review-log.md#task-0003018). Исходники не изменены; это уточнение проверенных связей, а не повторный полный разбор файла.

## Уточнение TASK-0003.019

2026-09-10, `rusbar-main`, `c26eb64dd54cc434087f54c3c6b678b6092b15a2`. [Конфигурация профессии](../../../../../../../../module/item/sheets/configurations/WitcherProfessionConfigurationSheet.js) сохраняет 4 общих PARTS, добавляет 3 пути и использует 5 вкладок. Общий general пуст для схемы профессии; activeEffects содержит 4 категории и общие actions. Основной навык не добавлен в части (issue-00112). Собственные actions записей effects/thresholds не являются ActiveEffect CRUD.

[Перекрёстная сверка](../../../../../review-log.md#task-0003019). Исходники не изменены; уточнение касается проверенных связей, не повторного полного разбора файла.

## Уточнение TASK-0003.020

2026-09-11, `rusbar-main`, `b09f992960a76d1c75946f402e42d93fa0785008`; проверены связи с критическими травмами, лечением и отдыхом. Полный первоначальный разбор и его ограничения сохранены.

| Связь | Файл | Результат проверки |
| --- | --- | --- |
| criticalWound | [module/data/item/criticalWoundData.js](../../../../../../../../module/data/item/criticalWoundData.js) | Девять полей без боевых attackOptions/defenseOptions/damageType, поэтому общая вкладка general условно пуста. Вкладка activeEffects продолжает предоставлять управление Item.effects. |
| WitcherCriticalWoundSheet | [module/item/sheets/WitcherCriticalWoundSheet.js](../../../../../../../../module/item/sheets/WitcherCriticalWoundSheet.js) | Не переопределяет configuration; использует экземпляр базы. Собственного редактора эффектов или ruleId не вводит. |

[Сверка порции и итоговая сверка 96 файлов второй серии](../../../../../review-log.md#task-0003020); браузер, мир и записи в БД не запускались.
