# templates/sheets/investigation/clue-sheet.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/sheets/investigation/clue-sheet.hbs](../../../../../../../templates/sheets/investigation/clue-sheet.hbs) |
| Тип файла | Handlebars |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `538dbac9bb9432c123fe4f3c00ab788b58517afb` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.023](../../../../../../tasks/task-0003.023.md), 14 файлов, 449 логических строк |
| Запись перекрёстной сверки | [TASK-0003.023](../../../../review-log.md#task-0003023) |

## Актуализация N01–N08 — 14.3.1.00010

2026-09-16, dev, база aeb527c6e6402e8a5f940a2c3ad0020d7e5b35e4. Отображаемые placeholder/tooltip используют `WITCHER.Name`. Привязки name/data-field, классы действий, условия шаблона и введённые имена сохранены.

[Реализация и адресные проверки](../../../../../../issues/open/issue-00330.md#реализация-n01n08--143100010). Датированные разборы ниже сохраняют результаты прежних срезов.


## Назначение файла

Форма отдельного предмета-улики для ItemSheet V1. Редактирует имя и поля system.

## Условия использования

Загружается getter template класса WitcherClueSheet. Контекст содержит item/cssClass от базового ItemSheet V1 и skills от системного getData. Это самостоятельная форма, а не partial строки тайны.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| form / cssClass / autocomplete | 1 | Форма V1 | class={{cssClass}}, autocomplete=off | Базовая отправка ItemSheet |
| name | 2 | Имя Item | input name='name', item.name | Текстовый ввод; placeholder Name |
| type | input text | Значение ClueData.type | name='system.type'; item.system.type | Редактирование через базовый лист |
| dc | input number | Значение ClueData.dc | name='system.dc'; item.system.dc | Редактирование через базовый лист |
| skillsUsed | multi-select | Значение ClueData.skillsUsed | name='system.skillsUsed'; item.system.skillsUsed | Редактирование через базовый лист |
| timeIncrement | input text | Значение ClueData.timeIncrement | name='system.timeIncrement'; item.system.timeIncrement | Редактирование через базовый лист |
| timeBonus | input number | Значение ClueData.timeBonus | name='system.timeBonus'; item.system.timeBonus | Редактирование через базовый лист |
| damage | input text | Значение ClueData.damage | name='system.damage'; item.system.damage | Редактирование через базовый лист |
| obfuscation | input number | Значение ClueData.obfuscation | name='system.obfuscation'; item.system.obfuscation | Редактирование через базовый лист |
| penalty | input text | Значение ClueData.penalty | name='system.penalty'; item.system.penalty | Редактирование через базовый лист |
| focusDamage | input text | Значение ClueData.focusDamage | name='system.focusDamage'; item.system.focusDamage | Редактирование через базовый лист |
| selectOptions skills | multi-select | Полный словарь навыков | selected=item.system.skillsUsed; nameAttr/name; valueAttr=name; labelAttr=label; localize=true | Показывает сохранённый массив |

## Основные функции и методы

Программных функций нет. name='system.*' связывает форму с Item. Inline-edit — только CSS-класс этого шаблона: WitcherClueSheet не устанавливает собственный _onInlineEdit; сохранение идёт через базовый лист V1. selectOptions создаёт варианты навыков, сам Item не обновляет.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| WitcherClueSheet | [module/item/sheets/investigation/WitcherClueSheet.js](../../../../../../../module/item/sheets/investigation/WitcherClueSheet.js) | Загрузка/контекст | template/getData | Прочитан полный класс |
| ClueData | [module/data/investigation/clueData.js](../../../../../../../module/data/investigation/clueData.js) | Схема | Все перечисленные system-пути | Группа 16 |
| localize / selectOptions | Foundry 14.367.0, client/applications/handlebars.mjs:460–500; forms/fields.mjs:290–360 | Handlebars helpers | Подписи и <option> | Исполнены настоящие selectOptions/prepareSelectOptionGroups; запись DOM заменена HTML-фасадом |
| WITCHER.skillMap | [module/setup/config.js](../../../../../../../module/setup/config.js) | Контекст skills | name/valueAttr/labelAttr | name — ключ передаваемого навыка; label — ключ перевода |
| WITCHER.Type; WITCHER.DC; WITCHER.Investigation.skillsUsed; WITCHER.Investigation.timeIncrement; WITCHER.Investigation.timeBonus; WITCHER.Investigation.damage; WITCHER.Investigation.obfuscation; WITCHER.Investigation.penalty; WITCHER.Investigation.focusDamage | [lang/en.json](../../../../../../../lang/en.json); [lang/ru.json](../../../../../../../lang/ru.json) | Локализация | Подписи полей | Статические ключи этого шаблона найдены в en/ru; динамические label picklock/trapcraft — issue-00016 |
| ItemSheet V1 / multi-select | Foundry 14.367.0 client/appv1/sheets/item-sheet.mjs; applications/elements/multi-select.mjs:122–124 | Форма/поле | Имя поля и выбранные значения | getData синхронен; _getValue возвращает массив строк |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/item/sheets/investigation/WitcherClueSheet.js](../../../../../../../module/item/sheets/investigation/WitcherClueSheet.js) | clue-sheet.hbs | getter template | 19 |

Область поиска: module/ и templates/ текущего checkout; регистрация сверена с system.json. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Шаблон показывает имя и 9 полей system. isHidden редактируется действием hideItem на листе тайны, здесь его ввода нет. Нет отдельного UI для img/описания и нет кнопок броска/удаления. Формулы damage/focusDamage выводятся как текст. Используемых опциями класса контейнеров .sheet-tabs/.sheet-body и .items-list .item здесь нет.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Рендер и выбор навыков | Группа 04 | Настоящий HBS с контекстом листа даёт одну форму; выбранные option соответствуют skillsUsed | База V1 и создание DOM-options — фасады |
| Поля/локализация | Группа 16 | Именованные system-пути существуют в модели, статические ключи есть в en/ru | Динамический fallback и сохранение не исполнялись |

## Непроверенные участки и открытые вопросы

Все 23 строки прочитаны. Реальные V1 submit/native multi-select — [U015-02](../../../../cross-check-0002.md#u015-02); пустой числовой ввод и сохранение — [U015-03](../../../../cross-check-0002.md#u015-03)/[U015-05](../../../../cross-check-0002.md#u015-05); внешнее применение последствий — [U015-08](../../../../cross-check-0002.md#u015-08). Сбой из отсутствующих tabs не выводится.

## Связанные проблемы

[issue-00016](../../../../../../issues/closed/issue-00016.md) — подписи picklock/trapcraft в общем словаре навыков; группа 17. [issue-00005](../../../../../../issues/potential/issue-00005.md), [issue-00150](../../../../../../issues/potential/issue-00150.md). Тип не объявлен в манифесте; схема позволяет неизвестные навыки, хотя этот селектор предлагает только skillMap.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `538dbac9bb9432c123fe4f3c00ab788b58517afb`; полный файл | Первая карточка; [сверка порции](../../../../review-log.md#task-0003023) |

## Сквозная сверка TASK-0004.015

2026-09-14; rusbar-main, 7e0d53944f3089cd61667670377aa6770fabc8cf. Исходник совпадает со срезом TASK-0001; изменено только описание.

Отдельная V1-форма передаёт named name/system.*; её multi-select читает item.system.skillsUsed, а не контекст partial. Поля dc/timeBonus/obfuscation числовые, остальные последствия текстовые; isHidden здесь не редактируется. Наличие полей DC/ущерба не подключает их к rollClue: из модели он читает только skillsUsed. inline-edit у этого select не означает вызов MysterySheet._onInlineEdit, который привязан к другому листу.

Сопоставленные определения и потребители: [module/item/sheets/investigation/WitcherClueSheet.js](../../../module/item/sheets/investigation/WitcherClueSheet.js.md), [module/data/investigation/clueData.js](../../../module/data/investigation/clueData.js.md), [module/scripts/investigation/rollClue.js](../../../module/scripts/investigation/rollClue.js.md), [templates/sheets/investigation/partials/clue-display.hbs](partials/clue-display.hbs.md).

[Протокол и границы](../../../../review-log.md#task-0004015) — TASK-0004.015; процессы [R015-04](../../../../cross-check-0002.md#r015-04), [R015-11](../../../../cross-check-0002.md#r015-11), [R015-14](../../../../cross-check-0002.md#r015-14), [R015-15](../../../../cross-check-0002.md#r015-15). В этой порции выполнена статическая сверка; прежние опыты сохраняют свои даты и фасады. Новых поведенческих запусков нет; браузер, мир, сеть и запись в БД не запускались.
