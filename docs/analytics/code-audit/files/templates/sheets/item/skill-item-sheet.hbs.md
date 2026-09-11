# templates/sheets/item/skill-item-sheet.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/sheets/item/skill-item-sheet.hbs](../../../../../../../templates/sheets/item/skill-item-sheet.hbs) |
| Тип файла | Handlebars |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `273a6d7db0b7c866399db3ecd4f7191817ae6f10` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.029](../../../../../../tasks/task-0003.029.md), 14 файлов, 763 логических строк |
| Запись перекрёстной сверки | [TASK-0003.029](../../../../review-log.md#task-0003029) |

## Назначение файла

Минимальная форма собственного Item-навыка: имя документа и выбор исходной характеристики.

## Условия использования

Рендерится как PARTS.main WitcherSkillItemSheet, зарегистрированного по умолчанию для Item type skill. Контекст содержит item и отфильтрованные stats. Это форма Item; значение навыка Actor хранится в ином документе.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| section / sheet-header | Весь шаблон, 12 строк | Контейнер формы | PARTS.main | Отображает name и system.attribute |
| selectOptions stats | Строки 8–10 | Девять исходных характеристик | Core Handlebars helper | selected берётся из item.system.attribute; localize=true |

## Основные функции и методы

Собственных JavaScript-функций нет. Input name='name' редактирует Item.name; select name='system.attribute' выбирает характеристику. Сохранение передано стандартному form lifecycle ItemSheetV2 с submitOnChange=true, closeOnSubmit=false; собственного обработчика submit в HBS нет.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| WitcherSkillItemSheet._prepareContext / PARTS / DEFAULT_OPTIONS | [module/item/sheets/WitcherSkillItemSheet.js](../../../../../../../module/item/sheets/WitcherSkillItemSheet.js) | Контекст и владелец формы | item, stats и сохранение при изменении | Литерал PARTS.main и поля контекста |
| SkillItemData.attribute | [module/data/item/skillItemData.js](../../../../../../../module/data/item/skillItemData.js) | Схема Item | StringField; исходное значение пустое; choices схема не задаёт | name=system.attribute |
| WITCHER.statMap | [module/setup/config.js](../../../../../../../module/setup/config.js) | Данные через stats | Девять записей originstat; среди них spd/luck | Фильтрация в классе листа |
| selectOptions / prepareSelectOptionGroups / ItemSheetV2 | Foundry VTT 14.367 и Handlebars | Внешние helper и форма | Рендер опций, localize и стандартное сохранение | Настоящие core helper использованы в изолированной проверке |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/item/sheets/WitcherSkillItemSheet.js](../../../../../../../module/item/sheets/WitcherSkillItemSheet.js) | Весь HBS | PARTS.main template | Буквальная ссылка systems/TheWitcherTRPG/templates/sheets/item/skill-item-sheet.hbs |

Область поиска: module/ и templates/ текущего checkout; прямые импорты и места вызова сверены отдельно от динамических обращений. Типы и листы сверены с system.json, module/setup/registerDataModels.js и module/setup/registerSheets.js. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Форма предлагает только name и system.attribute. В ней нет полей value, label, isProfession/isPickup/isLearned, isOpened и activeEffectModifiers. Начальное attribute='' не совпадает ни с одной из девяти опций; фактическое поведение выбора браузера до изменения пользователем не проверялось.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Полный шаблон и владелец | 12 строк; PARTS и _prepareContext | Два редактируемых пути, один selectOptions | Нет самостоятельного JS |
| Настоящий рендер | Handlebars 4.7.9 + core selectOptions/prepareSelectOptionGroups + настоящий контекст листа | 9 опций, dex выбран; локализованные подписи | Создание select DOM и оболочка Application подменены |
| Соответствие вкладкам Actor | _prepareCustomSkills группирует 9 атрибутов; tab-skills перебирает 7 групп system.skills | spd/luck можно выбрать, но строка такого Item на общей вкладке не появляется | Вывод ограничен текущими листами системы |

## Непроверенные участки и открытые вопросы

Реальный submit ItemSheetV2 и запуск окна в браузере не выполнялись. Перечень допустимых для собственного навыка характеристик по правилам не устанавливался.

## Связанные проблемы

[issue-00188](../../../../../../issues/potential/issue-00188.md). Расхождение выбора характеристик и группировки вкладок оформлено как potential.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `273a6d7db0b7c866399db3ecd4f7191817ae6f10`; полный файл | Первая карточка; [сверка порции](../../../../review-log.md#task-0003029) |
