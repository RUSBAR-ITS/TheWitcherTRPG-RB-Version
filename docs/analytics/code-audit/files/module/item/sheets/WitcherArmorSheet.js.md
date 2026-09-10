# module/item/sheets/WitcherArmorSheet.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/item/sheets/WitcherArmorSheet.js](../../../../../../../module/item/sheets/WitcherArmorSheet.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `0fa589bd300856ff309f362afcb66d6fa43401ab` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.014](../../../../../../tasks/task-0003.014.md), одна порция из девяти файлов |
| Запись перекрёстной сверки | [TASK-0003.014](../../../../review-log.md#task-0003014) |

## Назначение файла

Лист брони и щитов: основная форма, специализированная конфигурация, варианты типа/локации и связь с рецептом.

## Условия использования

Default export WitcherArmorSheet extends WitcherItemSheet; зарегистрирован для Item.armor. Поле configuration создаёт WitcherArmorConfigurationSheet для того же документа. Object.assign добавляет три метода associatedDiagramMixin; отдельная схема Actor не создаётся.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| WitcherArmorSheet | Класс 5–53 | Лист Item.armor | Default export / Items.registerSheet | Наследует базовую форму, действия effects и drag/drop |
| configuration; PARTS.main | 6;8–13 | Конфигурация и основной HBS | Поле экземпляра; static PARTS | Шаблон armor-sheet, scrollable:[''] |
| config.Availability.WITCHER; config.type; config.armorLocations | 19–21 | Варианты выбора | Объект context.config общий с CONFIG.WITCHER | Присваивания затрагивают общий объект в памяти |
| Методы associatedDiagramMixin | Object.assign 55 | Связанный рецепт | Методы в prototype | Подключение, удаление, приём drop |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| _prepareContext(options) | Контекст super | Promise<context> | Добавляет Availability.WITCHER и результаты getTypes/getArmorLocations | Не копирует CONFIG; не пишет Item |
| getTypes() | Нет аргументов | Новый объект четырёх пар | Light/Medium/Heavy/Natural → ключи локализации | Совпадает с choices ArmorData.type |
| getArmorLocations() | Нет аргументов | Новый объект пяти пар | Head/Torso/Leg/FullCover/Shield → ключи | Это список UI, актуальная StringField.location его не ограничивает |
| activateListeners(html) | Корень формы | undefined | super; _addAssociatedDiagramListeners | Базовый _onRender вызывает этот override |
| _onDropItem(event,item) | Результат Item drop | Promise<void> | _onDropDiagram с armor и elderfolk-armor | Не возвращает/не ждёт внутренний Promise |
| _addAssociatedDiagramListeners; _onRemoveAssociatedDiagram; _onDropDiagram | Примесь | По внешним определениям | Удаление ссылки и проверка области/типа рецепта | Не собственные определения файла; методы прочитаны как зависимости |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| WitcherArmorConfigurationSheet | [module/item/sheets/configurations/WitcherArmorConfigurationSheet.js](../../../../../../../module/item/sheets/configurations/WitcherArmorConfigurationSheet.js) | Import/new | configuration:6 | Полный разбор специализации |
| WitcherItemSheet | [module/item/sheets/WitcherItemSheet.js](../../../../../../../module/item/sheets/WitcherItemSheet.js) | Import/наследование | Контекст, _onRender, CRUD effects, форма/Drop | Настоящий вызов _onRender зарегистрировал listener |
| associatedDiagramMixin | [module/item/sheets/mixins/associatedDiagramMixin.js](../../../../../../../module/item/sheets/mixins/associatedDiagramMixin.js) | Import/Object.assign/calls | 47,51,55 | Принимает только подходящий тип в associatedDiagram через offsetParent |
| armor-sheet.hbs | [templates/sheets/item/armor-sheet.hbs](../../../../../../../templates/sheets/item/armor-sheet.hbs) | PARTS | 10 | Пять локаций и пустая строка проверены |
| CONFIG.WITCHER.Availability | [module/setup/config.js](../../../../../../../module/setup/config.js) | Общий объект context.config | Добавление особой доступности WITCHER | Контекст действительно разделяет ссылку |
| WITCHER.Armor.*, WITCHER.Item.AvailabilityWitcher | [lang/ru.json](../../../../../../../lang/ru.json); [lang/en.json](../../../../../../../lang/en.json) | Локализация | Списки типа/локации | Ключи проверены по JSON |
| ItemSheetV2/HBM, jQuery, Item.update | Foundry 14.367.0 и jQuery клиента | Внешний API | Рендер, подписки и запись | Core ItemSheet/DragDrop настоящие, окружение документа/DOM/update подменены |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/setup/registerSheets.js](../../../../../../../module/setup/registerSheets.js) | WitcherArmorSheet | Items.registerSheet, types armor | Импорт 14, регистрация 40 |
| [templates/sheets/item/armor-sheet.hbs](../../../../../../../templates/sheets/item/armor-sheet.hbs) | config.type/armorLocations/Availability; методы примеси | Формы и область рецепта | Все поля и ветви разобраны |
| [templates/partials/associated-diagram.hbs](../../../../../../../templates/partials/associated-diagram.hbs) | _onRemoveAssociatedDiagram / drop | data-type associatedDiagram, кнопка удаления | Точечная сверка |

Область поиска: текущие module/ и templates/; регистрации сверены отдельно. Динамические обращения внешних модулей не исследовались.

## Данные и изменения состояния

Установка локации меняет отображаемые поля SP/надёжности в HBS. getTypes и getArmorLocations возвращают новые объекты, но _prepareContext помещает их в общую CONFIG.WITCHER. Внесённая Availability.WITCHER остаётся доступна другим читателям того же объекта; нежелательность этого сама по себе не установлена. Drop меняет только associatedDiagramUuid, не добавляет рецепт в инвентарь.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Контекст | Настоящий ArmorSheet._prepareContext | 4 типа, 5 локаций, shared config=true | Не полный клиент |
| Listeners | Настоящий базовый _onRender | .remove-associated-diagram/click подключён | jQuery/DOM — фасад |
| Drop | armor, elderfolk-armor, weapon | Первые два UUID переданы update; третий отклонён | update и событие подменены; null offsetParent ранее проверен на той же примеси |
| Форма | Шесть вариантов location | 15/17/21/19/27/17 именованных полей с header | clickableImageItemTypes — штатная строка; реальное окно не открывалось |

## Непроверенные участки и открытые вопросы

Не проверены реальная геометрия drop, сетевое обновление, последовательное открытие других листов после изменения CONFIG. Общий обработчик Actor/Folder не входит в специализированную обработку рецепта.

## Связанные проблемы

[issue-00058](../../../../../../issues/potential/issue-00058.md), [issue-00060](../../../../../../issues/potential/issue-00060.md), [issue-00080](../../../../../../issues/potential/issue-00080.md), [issue-00088](../../../../../../issues/potential/issue-00088.md). Общий Drop, редактирование текстового воздействия, общая примесь рецепта и показ вычисленного сопротивления.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.014 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.
