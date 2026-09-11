# module/item/sheets/WitcherItemSheet.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/item/sheets/WitcherItemSheet.js](../../../../../../../module/item/sheets/WitcherItemSheet.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `07237960627bf7debc2b4283aa55d1a8c5d1bb8b` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.011](../../../../../../tasks/task-0003.011.md), одна порция из семи файлов |
| Запись перекрёстной сверки | [TASK-0003.011](../../../../review-log.md#task-0003011) |

## Назначение файла

Задаёт общую основу предметных листов ApplicationV2: контекст system, окно конфигурации, сохранение формы, редактирование записей предметных воздействий и маршрутизацию drop. Сам класс не задаёт ни одной части содержимого.

## Условия использования

[module/setup/registerSheets.js](../../../../../../../module/setup/registerSheets.js) регистрирует класс по умолчанию без types, затем назначает специализированные классы. Прямых наследников в module/item/sheets — 17; WitcherSkillItemSheet и два листа расследований используют собственные основы. При создании экземпляра configuration получает новый WitcherConfigurationSheet для того же document; шесть наследников затем заменяют его специализированным окном. Поля PARTS/TABS пусты, defaultOptions относится к прежнему API: в проверенной цепочке ApplicationV2 его чтения не найдено. На note остаётся общий класс и пустое содержимое.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| WitcherItemSheet | Класс, 7–171 | Общая основа Item-листов | default export; регистрация без types | Создание → подготовка → рендер → действия формы |
| HandlebarsApplicationMixin, ItemSheetV2, ux | Локальные aliases, 3–5 | Наследование и доступ к TextEditor | Константы модуля | Считываются при импорте/обращении к API |
| DEFAULT_OPTIONS | Static, 9–28 | 520×480, witcher/sheet/item, submitOnChange=true, closeOnSubmit=false, три actions | Наследуемая конфигурация ApplicationV2 | addEffect/removeEffect/configureItem; dragDrop legacy-массив сам по себе не связывает контроллер |
| PARTS / TABS | Static, 30/32 | Пустые реестры частей/вкладок | Переопределяются наследниками | Самостоятельный рендер не получает шаблонов |
| configuration | Поле экземпляра, 42 | Окно настройки того же Item | new WitcherConfigurationSheet | Читается showConfig и configureItem; собственного закрытия/освобождения этого окна нет |
| Три actions и callbacks drop/permissions | 9–28, 64–73 | Связь UI с методами | Application actions / DragDrop callbacks | Сохраняют this через bind; editEffect обслуживается change формы |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| static get defaultOptions;35–39 | Обращение к старому свойству | Объект с legacy tabs | mergeObject(super.defaultOptions, tabs) | В текущем ApplicationV2 чтения не найдено; не является фактической TABS |
| _prepareContext;45–58 | options, document.system/schema | Контекст Promise | super; config=CONFIG.WITCHER, item, systemFields, system.enrichedText?.(), data=system, showConfig | Меняет options.classes при каждом вызове; config/data — общие ссылки; enrichedText ожидается, ошибок не перехватывает |
| _onRender;61–76 | context/options, element | Promise<void> | Ожидает super; создаёт DragDrop и bind(element); activateListeners(element) | Core ItemSheetV2 уже bind-ит свой контроллер; новая привязка заменяет ondrop, а не добавляет второй вызов |
| _onChangeForm;78–83 | formConfig,event.target.dataset | undefined | Сначала super._onChangeForm; при editEffect вызывает _onEditEffect | Ручное обновление не ожидается; обычное сохранение идёт через ядро |
| activateListeners;85 | html | undefined | Пустая точка расширения | Наследники сами добавляют listeners; общий файл их не перечисляет |
| _canDragStart;87–89 | Без используемых аргументов | false | Запрещает dragstart для .draggable | Core bind выставляет draggable=false, обнуляет ondragstart |
| _canDragDrop;91–93 | Состояние листа | this.isEditable | Проверяет редактируемость | Права/запертый pack определяются DocumentSheetV2, не этим методом |
| _onDrop;100–111 | event, isEditable | Promise<маршрут/исходные данные/undefined> | TextEditor.getDragEventData → getDocumentClass → fromDropData → _onDropDocument; при отсутствии класса возвращает data | Не вызывает dropItemSheetData; fromDropData ожидается; исключения не перехвачены |
| _onDropDocument;123–135 | document.documentName | Promise<результат/null> | ActiveEffect/Actor/Item/Folder передаёт в одноимённые обработчики, другие типы → null | ActiveEffect — метод ядра; Actor/Folder отсутствуют; Item есть лишь у шести наследников |
| static _onAddEffect;138–143 | element.dataset.target | Promise<void> | Создаёт randomID, update({[target.id]:{percentage:0}}) | Не создаёт ActiveEffect; update не возвращается и не ожидается |
| _onEditEffect;145–157 | Элемент внутри .list-item: id,target,field,value | Promise<void> | При value=='on' берёт checked, затем update target.id.field | Смешивает checkbox с текстом on; число остаётся строкой до очистки схемой; update не ожидается |
| static _oRemoveEffect;159–166 | Родительская строка с id,target | Promise<void> | update({[target+'.-='+id]:null}) | Старый синтаксис удаления ещё преобразуется ядром в ForcedDeletion; update не ожидается |
| static _renderConfigureDialog;168–170 | configuration | Promise<void> | configuration?.render(true) | Optional chaining защищает отсутствие окна; возвращаемый render не передаётся вызывающему |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| WitcherConfigurationSheet | [module/item/sheets/configurations/WitcherConfigurationSheet.js](../../../../../../../module/item/sheets/configurations/WitcherConfigurationSheet.js) | ES import/new | 1,42; отдельное окно для Item | Полный разбор той же порции |
| ItemSheetV2, item/actor, _onDropActiveEffect, _onRender | Foundry14.367 /opt/foundryvtt/client/applications/sheets/item-sheet.mjs | Наследование | 7,61,126; права drop, копирование эффекта, контроллер | Исходный класс исполнен с подменённым DocumentSheetV2 |
| HandlebarsApplicationMixin/PARTS | Foundry14.367 /opt/foundryvtt/client/applications/api/handlebars-application.mjs | Наследование/рендер | 7,30; сборка и рендер частей | Настоящий mixin: note parts=[], rendered={} |
| DocumentSheetV2 / ApplicationV2: form, editImage, actions | Foundry14.367 /opt/foundryvtt/client/applications/api/document-sheet.mjs; /opt/foundryvtt/client/applications/api/application.mjs | Унаследованная форма | submitOnChange → FormDataExtended → validate → update/create; editImage открывает FilePicker | Проверено чтением; полный submit в браузере не выполнялся |
| DragDrop.implementation, TextEditor.implementation, getDocumentClass | Foundry14.367 /opt/foundryvtt/client/applications/ux/drag-drop.mjs; /opt/foundryvtt/client/applications/ux/text-editor.mjs; foundry.utils | Вызовы API | 64–73,102–108; разрешение и перенос документа | DragDrop настоящий; TextEditor/fromDropData подменены |
| mergeObject/randomID | Foundry14.367 /opt/foundryvtt/common/utils/helpers.mjs; foundry.utils.randomID | Вызов | 36,141; старые опции и идентификатор строки | Реальные utils в изолированной проверке |
| CONFIG.WITCHER | [module/setup/config.js](../../../../../../../module/setup/config.js) | Глобальная конфигурация | 47; контекст по ссылке | Сверено с шаблонами и наследником Mutagen |
| document.system, update | [module/item/witcherItem.js](../../../../../../../module/item/witcherItem.js) | Документ/данные | 50–56,142,156,163 | Документный класс зарегистрирован в module/TheWitcherTRPG.js; запись — API ядра |
| system.enrichedText?.() / schema.fields | [module/data/item/commonItemData.js](../../../../../../../module/data/item/commonItemData.js); [module/setup/registerDataModels.js](../../../../../../../module/setup/registerDataModels.js) | Динамический метод/схема | 51–52; прямой вызов модели | В CommonItemData enrichedText не определён; реализации Race/Profession/CriticalWound найдены у зарегистрированных моделей |
| _onDropItem | [module/item/sheets/WitcherArmorSheet.js](../../../../../../../module/item/sheets/WitcherArmorSheet.js); [module/item/sheets/WitcherWeaponSheet.js](../../../../../../../module/item/sheets/WitcherWeaponSheet.js); [module/item/sheets/WitcherContainerSheet.js](../../../../../../../module/item/sheets/WitcherContainerSheet.js); [module/item/sheets/WitcherDiagramSheet.js](../../../../../../../module/item/sheets/WitcherDiagramSheet.js); [module/item/sheets/WitcherRitualSheet.js](../../../../../../../module/item/sheets/WitcherRitualSheet.js); [module/item/sheets/WitcherCriticalWoundSheet.js](../../../../../../../module/item/sheets/WitcherCriticalWoundSheet.js) | Динамическая диспетчеризация | 130; специализированные обработчики Item | Шесть определений найдены; файлы читались в пределах связи |
| data-target/id/field; add/edit/removeEffect | [templates/sheets/item/armor-sheet.hbs](../../../../../../../templates/sheets/item/armor-sheet.hbs); [templates/sheets/item/enhancement-sheet.hbs](../../../../../../../templates/sheets/item/enhancement-sheet.hbs) | HTML → action/change | 138–166; редактирование system.effects | Поля формы сверены с itemEffect и TypedObjectField |
| showConfig/configureItem | [templates/partials/item-header.hbs](../../../../../../../templates/partials/item-header.hbs); [templates/partials/spell-header.hbs](../../../../../../../templates/partials/spell-header.hbs) | Контекст → кнопка | 56,168; показ и открытие настроек | Общий item-header полностью разобран, прочие специализированные формы проверены точечно |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/setup/registerSheets.js](../../../../../../../module/setup/registerSheets.js) | WitcherItemSheet | Импорт и makeDefault без types:24/34 | Регистрации перехвачены в Node |
| [module/item/sheets/WitcherAlchemicalSheet.js](../../../../../../../module/item/sheets/WitcherAlchemicalSheet.js) | WitcherItemSheet | Прямое наследование; super контекст/рендер, собственный PARTS | Поиск imports/extends по module/item/sheets |
| [module/item/sheets/WitcherArmorSheet.js](../../../../../../../module/item/sheets/WitcherArmorSheet.js) | WitcherItemSheet | Прямое наследование; super контекст/рендер, собственный PARTS | Поиск imports/extends по module/item/sheets |
| [module/item/sheets/WitcherComponentSheet.js](../../../../../../../module/item/sheets/WitcherComponentSheet.js) | WitcherItemSheet | Прямое наследование; super контекст/рендер, собственный PARTS | Поиск imports/extends по module/item/sheets |
| [module/item/sheets/WitcherContainerSheet.js](../../../../../../../module/item/sheets/WitcherContainerSheet.js) | WitcherItemSheet | Прямое наследование; super контекст/рендер, собственный PARTS | Поиск imports/extends по module/item/sheets |
| [module/item/sheets/WitcherCriticalWoundSheet.js](../../../../../../../module/item/sheets/WitcherCriticalWoundSheet.js) | WitcherItemSheet | Прямое наследование; super контекст/рендер, собственный PARTS | Поиск imports/extends по module/item/sheets |
| [module/item/sheets/WitcherDiagramSheet.js](../../../../../../../module/item/sheets/WitcherDiagramSheet.js) | WitcherItemSheet | Прямое наследование; super контекст/рендер, собственный PARTS | Поиск imports/extends по module/item/sheets |
| [module/item/sheets/WitcherEnhancementSheet.js](../../../../../../../module/item/sheets/WitcherEnhancementSheet.js) | WitcherItemSheet | Прямое наследование; super контекст/рендер, собственный PARTS | Поиск imports/extends по module/item/sheets |
| [module/item/sheets/WitcherHexSheet.js](../../../../../../../module/item/sheets/WitcherHexSheet.js) | WitcherItemSheet | Прямое наследование; super контекст/рендер, собственный PARTS | Поиск imports/extends по module/item/sheets |
| [module/item/sheets/WitcherHomelandSheet.js](../../../../../../../module/item/sheets/WitcherHomelandSheet.js) | WitcherItemSheet | Прямое наследование; super контекст/рендер, собственный PARTS | Поиск imports/extends по module/item/sheets |
| [module/item/sheets/WitcherMountSheet.js](../../../../../../../module/item/sheets/WitcherMountSheet.js) | WitcherItemSheet | Прямое наследование; super контекст/рендер, собственный PARTS | Поиск imports/extends по module/item/sheets |
| [module/item/sheets/WitcherMutagenSheet.js](../../../../../../../module/item/sheets/WitcherMutagenSheet.js) | WitcherItemSheet | Прямое наследование; super контекст/рендер, собственный PARTS | Поиск imports/extends по module/item/sheets |
| [module/item/sheets/WitcherProfessionSheet.js](../../../../../../../module/item/sheets/WitcherProfessionSheet.js) | WitcherItemSheet | Прямое наследование; super контекст/рендер, собственный PARTS | Поиск imports/extends по module/item/sheets |
| [module/item/sheets/WitcherRaceSheet.js](../../../../../../../module/item/sheets/WitcherRaceSheet.js) | WitcherItemSheet | Прямое наследование; super контекст/рендер, собственный PARTS | Поиск imports/extends по module/item/sheets |
| [module/item/sheets/WitcherRitualSheet.js](../../../../../../../module/item/sheets/WitcherRitualSheet.js) | WitcherItemSheet | Прямое наследование; super контекст/рендер, собственный PARTS | Поиск imports/extends по module/item/sheets |
| [module/item/sheets/WitcherSpellSheet.js](../../../../../../../module/item/sheets/WitcherSpellSheet.js) | WitcherItemSheet | Прямое наследование; super контекст/рендер, собственный PARTS | Поиск imports/extends по module/item/sheets |
| [module/item/sheets/WitcherValuableSheet.js](../../../../../../../module/item/sheets/WitcherValuableSheet.js) | WitcherItemSheet | Прямое наследование; super контекст/рендер, собственный PARTS | Поиск imports/extends по module/item/sheets |
| [module/item/sheets/WitcherWeaponSheet.js](../../../../../../../module/item/sheets/WitcherWeaponSheet.js) | WitcherItemSheet | Прямое наследование; super контекст/рендер, собственный PARTS | Поиск imports/extends по module/item/sheets |
| [templates/partials/item-header.hbs](../../../../../../../templates/partials/item-header.hbs) | item/config/showConfig; configureItem | Общая шапка десяти предметных форм | Пять вариантов полей/действий сверены |
| [templates/sheets/item/armor-sheet.hbs](../../../../../../../templates/sheets/item/armor-sheet.hbs); [templates/sheets/item/enhancement-sheet.hbs](../../../../../../../templates/sheets/item/enhancement-sheet.hbs) | _onAddEffect/_onEditEffect/_oRemoveEffect | Действия над system.effects | Сверены data-атрибуты и payload |

## Данные и изменения состояния

Контекст содержит подготовленную модель, не её снимок. configuration — отдельный Application для того же Item. Обычные именованные поля сохраняет ядро через validate/очистку формы и update; ручные списки system.effects пишутся отдельными update. Собственных проверок isEditable в ручных add/edit/remove нет: визуальная блокировка и права записи ядра — другие уровни; обход прав этим не доказан. Нет собственного dropItemSheetData. Копирование ActiveEffect сохраняет object через core create с parent=item; повтор того же родителя и isOwner=false ядро отвергает.

Количество options.classes растёт при повторной подготовке (два вызова добавили две одинаковые строки); последствие для видимого UI не устанавливалось. Повторный bind DragDrop не удваивает ondrop. Повторные слушатели наследников требуют проверки при полном разборе соответствующих листов.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Полнота | 171 строка, 13 собственных методов/getter, 3 static-реестра, configuration; поиск наследников | 17 прямых наследников; шесть замен configuration; шесть _onDropItem | Соседние файлы полностью не разбирались |
| Маршруты/контроллер | Настоящие SystemSheet + CoreItemSheet + HBM + DragDrop | Три отсутствующих метода дали TypeError; другие типы null; один drop после двух рендеров | DocumentSheet/DOM/разрешение документов подменены |
| Hooks | Core и system _onDrop при Hooks.call→false | Core остановился; system дошёл до создания эффекта | Hook и create перехвачены; сеть/БД отсутствуют |
| Ручные воздействия | Настоящий _onEditEffect и EnhancementData | Текст on→false→строка false; checkbox→true; число 25 остаётся строкой в payload | Ввод/запись подменены |
| Удаление/Promise | EnhancementData.updateSource и контролируемый pending update | -=fx удалил запись через ForcedDeletion; action завершился до update | updateSource в памяти; предупреждение совместимости перехвачено |
| Note | Регистрации + настоящие HBM _configureRenderOptions/_renderHTML | Единственный подходящий класс WitcherItemSheet; 0 частей | Не проверены пользовательские sheet-настройки и браузер |

## Непроверенные участки и открытые вопросы

Весь файл прочитан. Не исполнялись полный ApplicationV2/DocumentSheetV2, FormDataExtended в браузере, запись документов и внешние модули. Не моделировались отказы DB и одновременные формы/обновления; ручные методы не имеют собственного catch. Результаты копирования данных на стороне сервера и жизненный цикл второго окна требуют полноценного клиента. Условия legacy defaultOptions не переносились на API V14 по одному названию.

## Связанные проблемы

[issue-00057](../../../../../../issues/potential/issue-00057.md), [issue-00058](../../../../../../issues/potential/issue-00058.md), [issue-00059](../../../../../../issues/potential/issue-00059.md), [issue-00060](../../../../../../issues/potential/issue-00060.md), [issue-00063](../../../../../../issues/potential/issue-00063.md). Статус potential; исправления не выполнялись.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.011 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.

## Уточнение TASK-0003.013

2026-09-10, `8cca18e14b75ec53028ee6bc49a837597de4d9af`; исходник неизменен. [Перекрёстная сверка](../../../../review-log.md#task-0003013).

Проверен полный дочерний [module/item/sheets/WitcherWeaponSheet.js](../../../../../../../module/item/sheets/WitcherWeaponSheet.js). Базовый _onRender вызывает this.activateListeners(this.element), поэтому override оружия действительно получает управление: изолированный вызов _onRender зарегистрировал change для .damage-type и click для .remove-associated-diagram. Затем исходный обработчик записал system.type с двумя включёнными флагами и text «Режущий, Колющий». Это закрывает вопрос о подключении legacy-слушателя в проверенной цепочке, но не заменяет браузерную проверку. Специализированный _onDropItem оружия делегирует [module/item/sheets/mixins/associatedDiagramMixin.js](../../../../../../../module/item/sheets/mixins/associatedDiagramMixin.js) и не использует общий обработчик сброса Item для этой операции.

## Уточнение TASK-0003.014

2026-09-10, `0fa589bd300856ff309f362afcb66d6fa43401ab`; исходник неизменен. [Перекрёстная сверка](../../../../review-log.md#task-0003014).

Полностью разобраны [module/item/sheets/WitcherArmorSheet.js](../../../../../../../module/item/sheets/WitcherArmorSheet.js) и [module/item/sheets/WitcherEnhancementSheet.js](../../../../../../../module/item/sheets/WitcherEnhancementSheet.js). Броня заменяет configuration, расширяет общий config и через activateListeners подключает recipe-remove; улучшение добавляет отдельный context.selects и наследует базовую configuration. Обе формы используют собственные словари system.effects и общие add/remove/edit методы. Исходный обработчик снова дал name=false для текста on; добавление percentage=0 и удаление -= адресуют тот же словарь. Полное браузерное сохранение не выполнялось.

## Уточнение TASK-0003.015

2026-09-10, `7edb814aa870da75c7ad7633536e899a8d07e205`; исходник неизменен. [Перекрёстная сверка](../../../../review-log.md#task-0003015).

Полностью проверены [module/item/sheets/WitcherAlchemicalSheet.js](../../../../../../../module/item/sheets/WitcherAlchemicalSheet.js), [module/item/sheets/WitcherMutagenSheet.js](../../../../../../../module/item/sheets/WitcherMutagenSheet.js), [module/item/sheets/WitcherValuableSheet.js](../../../../../../../module/item/sheets/WitcherValuableSheet.js). Первые и последние создают WitcherConsumableConfigurationSheet; Mutagen наследует обычную configuration. Наследуемый header показывает configureItem во всех трёх случаях, но состав окна различается: 3/2/3 вкладки. Собственных activateListeners у этих листов нет; ручные таблицы расходования слушает отдельный класс configuration. Цвет мутагена находится в header, поэтому отсутствие собственного selector в main не означает отсутствия настройки.

## Уточнение TASK-0003.016

2026-09-10, `53f74994011383cb544cabac96285430f00cb38a`; исходник неизменен. [Перекрёстная сверка](../../../../review-log.md#task-0003016).

Полностью разобраны наследники [module/item/sheets/WitcherComponentSheet.js](../../../../../../../module/item/sheets/WitcherComponentSheet.js) и [module/item/sheets/WitcherDiagramSheet.js](../../../../../../../module/item/sheets/WitcherDiagramSheet.js). ComponentSheet задаёт лишь DEFAULT_OPTIONS.width/PARTS; DiagramSheet добавляет контекст и activateListeners. Настоящий базовый _onRender действительно вызвал override: зарегистрированы click/blur/click/click для добавления, редактирования, удаления компонента и удаления результата. В DiagramSheet реализован собственный _onDropItem, который пишет UUID результата либо массив материалов. Его null offsetParent даёт отклонение Promise; это другой caller того же небезопасного DOM-доступа, что issue-00080.

## Уточнение TASK-0003.018

2026-09-10, `rusbar-main`, `29319a7a7e1dfc0663edbc15166f3b6a19682a2f`. [Лист расы](../../../../../../../module/item/sheets/WitcherRaceSheet.js) и [лист родины](../../../../../../../module/item/sheets/WitcherHomelandSheet.js) используют общие _prepareContext и configuration без переопределения. С настоящими моделями контекст race получил 4 записи enrichedText, homeland — undefined через необязательный вызов; оба получили CONFIG.WITCHER, systemFields, data и showConfig. Наследуемый configureItem открыл конфигурацию-фасад по одному разу. Сохранение UI и браузерное слияние параметров окна не выполнялись.

[Перекрёстная сверка](../../../../review-log.md#task-0003018). Исходники не изменены; это уточнение проверенных связей, а не повторный полный разбор файла.

## Уточнение TASK-0003.019

2026-09-10, `rusbar-main`, `c26eb64dd54cc434087f54c3c6b678b6092b15a2`. [Лист профессии](../../../../../../../module/item/sheets/WitcherProfessionSheet.js) наследует основной контекст и заменяет configuration на [специализированную](../../../../../../../module/item/sheets/configurations/WitcherProfessionConfigurationSheet.js). Его _prepareContext использует config как общую ссылку и добавляет statOptions; основной HBS получил 47 именованных элементов и 11 enriched HTML. Direct Item CRUD/настройка эффектов у базового листа остаются отдельными от 6 методов правки записей навыка.

[Перекрёстная сверка](../../../../review-log.md#task-0003019). Исходники не изменены; уточнение касается проверенных связей, не повторного полного разбора файла.

## Уточнение TASK-0003.020

2026-09-11, `rusbar-main`, `b09f992960a76d1c75946f402e42d93fa0785008`; проверены связи с критическими травмами, лечением и отдыхом. Полный первоначальный разбор и его ограничения сохранены.

| Связь | Файл | Результат проверки |
| --- | --- | --- |
| WitcherCriticalWoundSheet | [module/item/sheets/WitcherCriticalWoundSheet.js](../../../../../../../module/item/sheets/WitcherCriticalWoundSheet.js) | Реализован собственный _onDropItem: сохраняет UUID в followUp без ожидания update. Этот наследник имеет Item-обработчик, в отличие от незаданных маршрутов базового класса. |
| criticalWound-sheet.hbs | [templates/sheets/item/criticalWound-sheet.hbs](../../../../../../../templates/sheets/item/criticalWound-sheet.hbs) | Наследуемый контекст обеспечивает document/config/systemFields/enrichedText/showConfig. Шестерёнка открывает общую конфигурацию. |

[Сверка порции и итоговая сверка 96 файлов второй серии](../../../../review-log.md#task-0003020); браузер, мир и записи в БД не запускались.

## Уточнение TASK-0003.021

Проверено 2026-09-11 на `a29234e7c42ef5f9d8095c2b5470e5e3c95824cc`; исходник не менялся.

Все три листа наследуют контекст и форму; только WitcherSpellSheet заменяет configuration специализированным классом. WitcherRitualSheet добавляет blur/click в activateListeners, а базовый _onDropDocument вызывает его _onDropItem. Последний не ожидает update, поэтому await на стороне родителя не обеспечивает завершение записи. Карточки HBS различают обычные name-поля и quantity с отдельным blur.

Сверенные карточки: [module/item/sheets/WitcherSpellSheet.js](WitcherSpellSheet.js.md), [module/item/sheets/WitcherHexSheet.js](WitcherHexSheet.js.md), [module/item/sheets/WitcherRitualSheet.js](WitcherRitualSheet.js.md), [templates/sheets/item/spell-sheet.hbs](../../../templates/sheets/item/spell-sheet.hbs.md), [templates/sheets/item/hex-sheet.hbs](../../../templates/sheets/item/hex-sheet.hbs.md), [templates/sheets/item/ritual-sheet.hbs](../../../templates/sheets/item/ritual-sheet.hbs.md), [templates/partials/spell-header.hbs](../../../templates/partials/spell-header.hbs.md).

[Результаты и пределы сверки](../../../../review-log.md#task-0003021).
