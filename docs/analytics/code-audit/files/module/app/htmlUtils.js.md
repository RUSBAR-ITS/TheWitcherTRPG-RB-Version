# module/app/htmlUtils.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/app/htmlUtils.js](../../../../../../module/app/htmlUtils.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `639fde4bad4a7ba4c538d3b08ddc5cfd846ca75e` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.037](../../../../../tasks/task-0003.037.md), 8 файлов, 313 логических строк |
| Запись перекрёстной сверки | [TASK-0003.037](../../../review-log.md#task-0003037) |

## Назначение файла

Два DOM-конструктора подписанных полей: обычный input и select через Foundry fields.

## Условия использования

Единственный найденный импорт и потребитель обоих exports — Rewards. Функции возвращают label HTMLElement, который вызывающий код добавляет в div и сериализует через outerHTML для DialogV2.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| createLabeledInput | named export function:1–11 | label + input | Rewards import1 | Создание DOM в памяти |
| createLabeledSelect | named export function:13–25 | label + core select | Rewards import1 | Создание DOM в памяти |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| createLabeledInput(title,type,name) | Строки подписи, type и name | HTMLElement label | style flex/gap10px/align-items:center; innerHTML=title; input.type/name; appendChild | Не задаёт value/min/max/step/required/data-dtype/id; не пишет документы |
| createLabeledSelect(title,name,options) | Подпись, name, core options | HTMLElement label | Та же обёртка; createSelectInput({name,...options}); appendChild | options.name может заменить name; текущий вызывающий код этого не делает |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| document.createElement, HTMLElement | DOM API; проверен фасад DOM в Node | Создание/сериализация | Оба helper | В браузере выполняется нативный DOM; изолированно проверен контракт вызовов |
| foundry.applications.fields.createSelectInput | Foundry 14.367.0: client/applications/forms/fields.mjs:225–237 | Core builder | createLabeledSelect:18–21 | Исполнены настоящий builder, prepareSelectOptionGroups, setInputAttributes, _appendOption |
| Подписи и параметры | [module/app/reward/reward.js](../../../../../../module/app/reward/reward.js) | Входы от потребителя | Только локализованные title из Rewards | title не является текстом награды из поля label |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/app/reward/reward.js](../../../../../../module/app/reward/reward.js) | createLabeledInput/createLabeledSelect | import1; оба диалога; text/number/checkbox и currency select | 33–40/113–128 |

Область поиска: module/ и templates/ текущего checkout; прямые импорты и места вызова сверены отдельно от динамических обращений. Типы и листы сверены с system.json, module/setup/registerDataModels.js и module/setup/registerSheets.js. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Присваивание innerHTML допускает HTML в title. В найденных вызовах это доверенный результат game.i18n.localize; введённая пользователем подпись награды не передаётся сюда. Поэтому helper сам по себе не доказывает внедрение HTML через награду. Функции не добавляют listeners, валидаторы, update или сортировку. Number-тип формы позднее приводит FormDataExtended, а не этот helper.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| DOM/опции | Группа01 | label содержит flex style и input.name/type; select options.name перекрывает вход; label options экранирует core | Минимальный фасад HTMLElement |
| Типы ответов | Группы04–05 | Number/null и Boolean получены реальным FormDataExtended | Native validity/DOM не запускались |
| Потребители | rg createLabeledInput/createLabeledSelect в module/templates | Только reward.js | Внешние макросы не проверены |

## Непроверенные участки и открытые вопросы

Файл прочитан целиком. Изолированные вызовы исполняют настоящий код, модели и Handlebars 4.7.9 на Foundry 14.367.0 / Node 24.16.0; Application, DOM и Actor.update/ChatMessage.create — фасады. Браузерное отображение/валидация, доступ службы по HTTP, серверные права, БД и несколько клиентов не проверялись. Реальные макросы миров и сторонние модули не исследовались.

## Связанные проблемы

Ошибка отсутствующих переводов располагается в вызывающем Rewards и HBS (issue234); отдельная проблема этих двух конструкторов не зарегистрирована.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `639fde4bad4a7ba4c538d3b08ddc5cfd846ca75e`; полный файл | Первая карточка; [сверка порции](../../../review-log.md#task-0003037) |
