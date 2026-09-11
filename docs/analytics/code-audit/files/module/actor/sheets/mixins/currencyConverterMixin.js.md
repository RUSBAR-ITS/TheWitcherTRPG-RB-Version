# module/actor/sheets/mixins/currencyConverterMixin.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/actor/sheets/mixins/currencyConverterMixin.js](../../../../../../../../module/actor/sheets/mixins/currencyConverterMixin.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `32d8fdd029ce4c6401db25f0d9645445ac0f8ca2` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.036](../../../../../../../tasks/task-0003.036.md), 4 файла, 164 логические строки |
| Запись перекрёстной сверки | [TASK-0003.036](../../../../../review-log.md#task-0003036) |

## Назначение файла

Связывает кнопки .open-currency-converter листа с методом Actor.handleCurrencyConverter. Сам обмен выполняется в другой одноимённой примеси по пути module/actor/mixins.

## Условия использования

Именованный импорт8 и Object.assign321 в WitcherActorSheet; activateListeners244 вызывается после _onRender213–217. В текущем Character инвентаре есть кнопка, Monster унаследовал listener без подходящего элемента. WitcherLootSheet наследует core и не присоединяет эту примесь; V1 не импортирует/не вызывает её.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| currencyConverterMixin | export let:1–7 | Объект с одним методом | WitcherActorSheet prototype | Не содержит курсов/формулы |
| currencyConverterListeners(html) | method:2–6 | Регистрация обработчиков | activateListeners(html) | html должен иметь querySelectorAll |
| forEach callback / bound handler | 3–4 | Каждой кнопке addEventListener('click',...) | DOM EventTarget | Каждый вызов bind создаёт новую функцию; ссылки для removeEventListener/защиты повтора нет |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| currencyConverterListeners(html):2–6 | HTMLElement-подобный корень и this.actor.handleCurrencyConverter | undefined | querySelectorAll('.open-currency-converter').forEach; bind Actor; addEventListener click | Пустой NodeList безопасен. Повтор на прежнем элементе добавляет ещё один handler. Promise от Actor не возвращается из этого регистратора и не ожидается EventTarget |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| Actor.handleCurrencyConverter | [module/actor/mixins/currencyConverterMixin.js](../../../../../../../../module/actor/mixins/currencyConverterMixin.js) | динамический вызов через bind | 4 | Определение event adapter:4–7; return openCurrencyConverter сохраняет Promise |
| querySelectorAll / addEventListener / Function.bind | DOM / ECMAScript | поиск/подписка/this | 3–4 | Настоящий Node EventTarget в группе18; полный browser DOM не исполнялся |
| _onRender / activateListeners | [module/actor/sheets/WitcherActorSheet.js](../../../../../../../../module/actor/sheets/WitcherActorSheet.js) | жизненный цикл вызова | 213–244 | Передаёт this.element, подписывает после каждого render |
| .open-currency-converter | [templates/sheets/actor/tabs/tab-inventory.hbs](../../../../../../../../templates/sheets/actor/tabs/tab-inventory.hbs) | селектор HBS | 14–16 | Кнопка без data-action, не DEFAULT_OPTIONS action |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/actor/sheets/WitcherActorSheet.js](../../../../../../../../module/actor/sheets/WitcherActorSheet.js) | currencyConverterMixin/currencyConverterListeners | import8; activateListeners244; Object.assign321 | Полный consumer source |
| [templates/sheets/actor/tabs/tab-inventory.hbs](../../../../../../../../templates/sheets/actor/tabs/tab-inventory.hbs) | currencyConverterListeners | click выбранной кнопки | Через WitcherCharacterSheet.PARTS и базовый activateListeners |

Область поиска: module/ и templates/ текущего checkout; прямые импорты и места вызова сверены отдельно от динамических обращений. Типы и листы сверены с system.json, module/setup/registerDataModels.js и module/setup/registerSheets.js. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Записывает только подписки EventTarget, не данные Actor. Группа18: первый click после одной регистрации вызвал метод1 раз; после второй на том же узле click вызвал2 раза; на новом узле с одной регистрацией снова1. Core HandlebarsApplicationMixin заменяет только отрендеренные части; при полном обновлении инвентаря кнопка новая, при сохранённой части возможна повторная подписка. Наблюдение не означает удвоение при каждом полном render.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Binding/повтор | 17–18 | this=Actor; Actor Promise ждёт open; zero nodes безопасно; повторный bind удваивает вызов на том же EventTarget | Изолированные Node события |
| Потребители/render | rg и core handlebars-application.mjs:191–224 | V2 вызывает на всём element; частичный render сохраняет другие части; V1/Loot без mixin | Конкретный браузерный partial-render не запускался |

## Непроверенные участки и открытые вопросы

Проверены локальные исходники Foundry 14.367.0, Node 24.16.0, настоящие модели/методы/HBS и отдельные core-функции. Dialog, базовые приложения, коллекции и запись документов подменены; EventTarget настоящий Node, не браузерный DOM. Мир, сеть, права и транзакции реальной БД не запускались. HTML min/max/step не выдаются за серверную валидацию. Курсы и экономические правила не менялись. При прямой передаче jQuery-объекта без querySelectorAll метод неприменим; текущий V2 передаёт HTMLElement. Ошибка V1 не заявляется: там нет регистрации и кнопки этого маршрута.

## Связанные проблемы

[issue-00230](../../../../../../../issues/potential/issue-00230.md). Потенциальный повторный listener отделён от same-currency и конкурирующих записей кошелька. Код не исправлялся.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `32d8fdd029ce4c6401db25f0d9645445ac0f8ca2`; полный файл | Первая карточка; [сверка порции](../../../../../review-log.md#task-0003036) |
