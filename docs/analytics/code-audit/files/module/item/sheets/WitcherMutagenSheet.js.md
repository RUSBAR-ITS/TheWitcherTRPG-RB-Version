# module/item/sheets/WitcherMutagenSheet.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/item/sheets/WitcherMutagenSheet.js](../../../../../../../module/item/sheets/WitcherMutagenSheet.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `7edb814aa870da75c7ad7633536e899a8d07e205` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.015](../../../../../../tasks/task-0003.015.md), одна порция из пятнадцати файлов |
| Запись перекрёстной сверки | [TASK-0003.015](../../../../review-log.md#task-0003015) |

## Назначение файла

Специализированный лист Item mutagen: основной шаблон и варианты категории.

## Условия использования

registerSheets импортирует класс и назначает листом по умолчанию соответствующего типа. При создании экземпляра наследуется WitcherItemSheet; HBM использует PARTS.main. Собственных действий, drop-обработчиков и слушателей нет. configuration наследуется от базового листа.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| WitcherMutagenSheet | default class extends WitcherItemSheet | Лист mutagen | Регистрация registerSheets | Рендер и подготовка контекста |
| PARTS.main | static object | template systems/TheWitcherTRPG/templates/sheets/item/mutagen-sheet.hbs; scrollable=[''] | HandlebarsApplicationMixin | Рендер основной части |
| config.type | Результат getTypes | Словарь категорий | Контекст HBS | Изменяется общий CONFIG.WITCHER через ссылку context.config |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| async _prepareContext(options) | Опции рендера; контекст родителя | Дополненный context | await super._prepareContext; config.Availability.WITCHER='WITCHER.Item.AvailabilityWitcher'; config.type=this.getTypes() | Мутирует общий config, не сохраняет Item |
| getTypes() | Аргументов нет | Новый словарь категорий | red→WITCHER.Mutagen.Red, green→WITCHER.Mutagen.Green, blue→WITCHER.Mutagen.Blue | Синхронно; модель StringField не ограничена этим набором |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| WitcherItemSheet | [module/item/sheets/WitcherItemSheet.js](../../../../../../../module/item/sheets/WitcherItemSheet.js) | Прямой импорт / наследование | Контекст, configureItem, формы/эффекты/действия | Определение и место использования сверены |
| Основной HBS | [templates/sheets/item/mutagen-sheet.hbs](../../../../../../../templates/sheets/item/mutagen-sheet.hbs) | PARTS.main.template | Представление | Определение и место использования сверены |
| CONFIG.WITCHER | [module/setup/config.js](../../../../../../../module/setup/config.js) | Данные через родителя | Availability и изменяемый config.type | Определение и место использования сверены |
| Ключи категорий | [lang/ru.json](../../../../../../../lang/ru.json) | Локализация | getTypes/createSelects; AvailabilityWitcher | Определение и место использования сверены |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/setup/registerSheets.js](../../../../../../../module/setup/registerSheets.js) | WitcherMutagenSheet | Импорт и регистрация типа mutagen | registerSheet makeDefault |
| [templates/sheets/item/mutagen-sheet.hbs](../../../../../../../templates/sheets/item/mutagen-sheet.hbs) | config.type; item/system | Основная форма | PARTS |
| [templates/partials/item-header.hbs](../../../../../../../templates/partials/item-header.hbs) | config.type / configuration | Общая шапка; кнопка configureItem; выбор цвета | Включение основным шаблоном |

Область поиска: текущие module/ и templates/; регистрации сверены отдельно. Динамические обращения внешних модулей не исследовались.

## Данные и изменения состояния

Контекст родителя содержит item, data, systemFields, config, showConfig. config не клонируется: Availability.WITCHER и type попадают в общий CONFIG.WITCHER; _prepareContext не обновляет документ. В конфигурации две вкладки general/activeEffects; унаследованная general не показывает isConsumable/consumeProperties. При этом main→item-header действительно выводит selector system.type red/green/blue. Обычные именованные поля сохраняются унаследованным механизмом формы, не этим файлом.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Контекст и регистрация | Полный класс + registerSheets + реальный _prepareContext | Выбран ожидаемый класс; 3 цвета в config.type | Полный браузерный выбор листа не проверялся |
| HBS/вкладки | Настоящие HBS и core _prepareTabs/_getTabsConfig | 3 варианта по 10 именованных полей; selector type=1; 2 вкладки | DocumentSheet/DOM фасады, selectOptions ограниченный генератор |

## Непроверенные участки и открытые вопросы

Полное сохранение формы, одновременно открытые окна и пользовательские sheet-настройки не проверялись. У мутагена добавление Availability.WITCHER не создаёт поле avail в модели. В этой порции не делаются выводы о правилах мутаций или категориях контента.

## Связанные проблемы

[issue-00093](../../../../../../issues/potential/issue-00093.md). Нет configuration расходования; отсутствие выбора цвета не обнаружено.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.015 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.
