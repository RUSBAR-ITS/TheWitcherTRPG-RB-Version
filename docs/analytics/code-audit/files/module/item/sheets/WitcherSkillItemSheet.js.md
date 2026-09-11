# module/item/sheets/WitcherSkillItemSheet.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/item/sheets/WitcherSkillItemSheet.js](../../../../../../../module/item/sheets/WitcherSkillItemSheet.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `273a6d7db0b7c866399db3ecd4f7191817ae6f10` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.029](../../../../../../tasks/task-0003.029.md), 14 файлов, 763 логических строк |
| Запись перекрёстной сверки | [TASK-0003.029](../../../../review-log.md#task-0003029) |

## Назначение файла

Отдельный лист Item-навыка на ItemSheetV2. Готовит список основных характеристик и передаёт документ в короткую форму имени и атрибута.

## Условия использования

Default export class extends HandlebarsApplicationMixin(ItemSheetV2). registerSheets делает его листом по умолчанию для типа skill. При подготовке контекста ожидает базовый _prepareContext, добавляет config/item/system/stats и CSS-класс.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| WitcherSkillItemSheet | Класс, 4–43 | Лист Item skill | Default export; регистрация в registerSheets | Рендер и штатная форма Foundry. |
| DEFAULT_OPTIONS | 6–16 | Размер 520×480, классы witcher/sheet/item, submitOnChange=true, closeOnSubmit=false | Статическая конфигурация | Объединяется с опциями базового листа. |
| PARTS.main.template | 18–22 | Единственный HBS | Статическая конфигурация | skill-item-sheet.hbs. |
| _prepareContext / filteredStats | 25–42 | Формирование контекста | Метод и локальный reduce | Оставляет statMap entries с origin==='stats'. |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| async _prepareContext(options) | document и базовый ItemSheetV2 | Promise<context> | await super; config=CONFIG.WITCHER; classes.push('item-skill'); item=document; reduce statMap; system=item.system | config/item/system и записи stats сохраняют ссылки. При каждом вызове добавляет ещё один item-skill; собственных submit handlers нет. |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| HandlebarsApplicationMixin / ItemSheetV2 | Foundry 14.367.0 applications.api / applications.sheets | Наследование | 1–4 и super._prepareContext | В проверке базовый лист/миксин заменены; метод настоящего класса исполнен. |
| WITCHER.statMap | [module/setup/config.js](../../../../../../../module/setup/config.js) | Чтение глобального справочника | 31–36 | Девять origin=stats: int/ref/dex/body/spd/emp/cra/will/luck; derivedStats исключены. |
| SkillItemData | [module/data/item/skillItemData.js](../../../../../../../module/data/item/skillItemData.js) | Поля document.system | attribute в форме | Модель принимает любую строку; choices ограничивает только этот UI. |
| skill-item-sheet.hbs | [templates/sheets/item/skill-item-sheet.hbs](../../../../../../../templates/sheets/item/skill-item-sheet.hbs) | PARTS.main | 20 | Контекст item/stats; selectOptions localize=true. |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/setup/registerSheets.js](../../../../../../../module/setup/registerSheets.js) | WitcherSkillItemSheet | Импорт и Items.registerSheet(makeDefault:true,types:['skill']) | 18, 131–134 |
| [templates/sheets/item/skill-item-sheet.hbs](../../../../../../../templates/sheets/item/skill-item-sheet.hbs) | item / stats | Контекст формы и обратные пути name/system.attribute | Весь шаблон |

Область поиска: module/ и templates/ текущего checkout; прямые импорты и места вызова сверены отдельно от динамических обращений. Типы и листы сверены с system.json, module/setup/registerDataModels.js и module/setup/registerSheets.js. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Изменяет контекст и this.options.classes, но сам не записывает Item. Штатному механизму формы передаются поля name и system.attribute; значение навыка и его флаги эта форма не показывает. Допускаемые SPD/LUCK сохраняются моделью, но текущие вкладки перебирают только семь групп system.skills и не выводят такие Item.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Контекст и selectOptions | Группа 02 | 9 options, выбран dex; ссылки item/system/config сохранены; только name/system.attribute доступны в форме | Настоящие метод/Handlebars/selectOptions/prepareSelectOptionGroups; создание HTML select и базовый лист заменены. |
| Повторная подготовка | Группа 02 | Два вызова добавили два item-skill в classes | Не исследован эффект дублирования класса в браузере; отдельная issue не заведена. |
| Доступность групп | Группа 17 | Item со spd/luck попадает в подготовленные customSkills, но отсутствует в цикле отображения | Точечная проверка базового ActorSheet и текущего HBS. |

## Непроверенные участки и открытые вопросы

Полностью прочитаны 43 строки. Работа штатного submitOnChange, сохранение документа сервером, SheetConfig и реальный рендер окна не исполнялись; поля подтверждены шаблоном и схемой.

## Связанные проблемы

[issue-00188](../../../../../../issues/potential/issue-00188.md). Несогласованность списка атрибутов с группировкой вкладок; отдельный технический вариант решения не выбран.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `273a6d7db0b7c866399db3ecd4f7191817ae6f10`; полный файл | Первая карточка; [сверка порции](../../../../review-log.md#task-0003029) |
