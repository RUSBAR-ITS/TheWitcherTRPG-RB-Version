# module/actor/mixins/currencyConverterMixin.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/actor/mixins/currencyConverterMixin.js](../../../../../../../module/actor/mixins/currencyConverterMixin.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `32d8fdd029ce4c6401db25f0d9645445ac0f8ca2` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.036](../../../../../../tasks/task-0003.036.md), 4 файла, 164 логические строки |
| Запись перекрёстной сверки | [TASK-0003.036](../../../../review-log.md#task-0003036) |

## Назначение файла

Методы Actor для обмена валюты: получение курсов CONFIG, подготовка окна, расчёт комиссии/округления, одна запись двух остатков и сообщение чата. Обмен не переносит предметы, не использует покупку Loot и не вызывает журнал наград.

## Условия использования

WitcherActor импортирует currencyConverterMixin:17 и Object.assign.prototype:452; все Actor этого класса получают три метода. Кнопка текущего Character инвентаря через одноимённую примесь листа вызывает handleCurrencyConverter с this=Actor. У Monster/Loot методы Actor есть, но кнопка в их текущих HBS не найдена. V1 sheet не подключает эту примесь. CONFIG.WITCHER устанавливается в init из setup/config. Импорт определяет объект/ссылку на DialogV2 без открытия окна.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| DialogV2 | const:1 | Внешний API input | локальная ссылка | Запрос формы с default отменой null |
| currencyConverterMixin | export const:3–107 | Три метода Actor | Object.assign WitcherActor | Разделение event adapter / config / процесса |
| excluded / currencyKeys / options / currencies | локальные:18–34 | Набор доступных валют и отображение баланса | контекст формы | Одинаковые options для from/to; currencyData ссылка захвачена до async render/input |
| amount / from / to / fee / feeRate / rates | локальные:57–64 | Вход формы и числовые коэффициенты | DialogV2.input→расчёт | amount/fee тип Number через FormDataExtended; пустое numeric поле null |
| currentFrom / baseValue / converted / afterFee / rounded / newFrom / newTo | локальные:66–86 | Последовательность расчёта | Одна запись Actor | Два вычисляемых ключа сливаются при from===to |
| chatContent | локальное:89–105 | HTML результата и speaker Actor | ChatMessage.create | Передаёт actor:this.name в HBS, но тот его не читает |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| handleCurrencyConverter(event):4–7 | Событие с preventDefault, this Actor | Promise результата openCurrencyConverter | preventDefault(); return this.openCurrencyConverter() | Promise сохраняется; addEventListener не является ожидающим caller |
| getCurrencyRates():9–15 | CONFIG.WITCHER.currencyRates | Та же ссылка на объект | Проверяет лишь truthy rates | Нет объекта→Error Missing CONFIG.WITCHER.currencyRates. Пустой объект truthy; элементы/положительность/finite не проверяет |
| openCurrencyConverter():17–106 — подготовка | CONFIG.currency, optional excluded, this.system.currency | Окно DialogV2.input | keys без excluded → options {value,label}; currencies {key,label,value}; await renderTemplate; await input | Нет CONFIG.currency→TypeError; нет currency→Error Invalid actor: missing system.currency; пустые options не останавливают окно; !values→return |
| openCurrencyConverter():57–87 — расчёт/запись | values amount/from/to/fee, актуальный CONFIG rates; захваченный currencyData | await this.update с двумя system.currency.* | Проверяет лишь amount>currentFrom; floor(amount×fromRate/toRate×(1−fee/100)); newFrom=max(0,currentFrom−amount); newTo=oldTo+rounded | Отрицательные/дробные/NaN/неизвестные ключи не отбрасывает. Запись ожидается; отказ прерывает до чата. Устаревшая ссылка/параллельные подтверждения могут перезаписать свежие остатки |
| openCurrencyConverter():89–105 — сообщение | Успешная запись Actor | ChatMessage OTHER, speaker=this | await renderTemplate currency-conversion; ChatMessage.create | create не await/return; ошибка подготовки HTML случится после записи кошелька |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| CONFIG.WITCHER.currency / currencyRates / currencyConverter | [module/setup/config.js](../../../../../../../module/setup/config.js) | глобальная конфигурация | 10,18–34,62–70,94–95 | currency624–632; rates634–641: bizant4,ducat1/3,lintar2,floren3,crown1,oren1; excluded=['falsecoin']643–645 |
| CONFIG.WITCHER=WITCHER | [module/TheWitcherTRPG.js](../../../../../../../module/TheWitcherTRPG.js) | init регистрация | Доступ к CONFIG в методах | 30, импорт config1; чтение настроек не game.settings |
| currency() / CommonActorData / LootData | [module/data/actor/templates/common/currencyData.js](../../../../../../../module/data/actor/templates/common/currencyData.js); [module/data/actor/commonActorData.js](../../../../../../../module/data/actor/commonActorData.js); [module/data/actor/lootData.js](../../../../../../../module/data/actor/lootData.js) | пути модели | system.currency, update84–87 | Семь NumberField; CommonActorData.currency20 и LootData.currency10. Character/Monster наследуют общую модель, Loot отдельно |
| currencyConverter.hbs | [templates/sheets/actor/currencyConverter/currencyConverter.hbs](../../../../../../../templates/sheets/actor/currencyConverter/currencyConverter.hbs) | literal renderTemplate | 36–42 | options/currencies; данные не передаются как Actor context |
| currency-conversion.hbs | [templates/chat/currency-conversion.hbs](../../../../../../../templates/chat/currency-conversion.hbs) | literal renderTemplate | 89–99 | actor,amount,from,to,fee,result; ключи локализации валют |
| WITCHER.currencyConverter.* / WITCHER.Currency.* | [lang/en.json](../../../../../../../lang/en.json); [lang/ru.json](../../../../../../../lang/ru.json) | локализация | title/convert/insufficient и labels | 16 ключей: девять converter включая кнопку соседа + семь валют; expandObject/Localization и fallback |
| DialogV2.input / FormDataExtended | Foundry /opt/foundryvtt/client/applications/{api/dialog.mjs,ux/form-data-extended.mjs} | ввод формы | 44–55 | input390–393 читает .object; wait405+ default rejectClose=false; numeric blank→null, Number dtype |
| renderTemplate / ChatMessage / CONST / Actor.update / ui.notifications | Foundry Handlebars API; documents/chat-message.mjs; common/constants.mjs; common/documents/actor.mjs | рендер, запись и сообщения | 36,68,84,89,101–105 | Speaker получает Actor, style OTHER; права update сохраняются в ядре, вызов не получает GM-привилегий |
| Set / Object.keys / Number / Math.floor / Math.max | ECMAScript | фильтрация/приведение/округление | 18–82 | Порядок формулы прямо из источника; Math.floor округляет вниз, включая отрицательные числа |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/actor/witcherActor.js](../../../../../../../module/actor/witcherActor.js) | currencyConverterMixin | import17; Object.assign452 | Добавляет три метода |
| [module/actor/sheets/mixins/currencyConverterMixin.js](../../../../../../../module/actor/sheets/mixins/currencyConverterMixin.js) | handleCurrencyConverter | bind(this.actor)→click | 3–4 |
| [templates/sheets/actor/tabs/tab-inventory.hbs](../../../../../../../templates/sheets/actor/tabs/tab-inventory.hbs) | handleCurrencyConverter через примесь листа | Единственная найденная .open-currency-converter | 14–16; CharacterSheet.PARTS.inventory |

Область поиска: module/ и templates/ текущего checkout; прямые импорты и места вызова сверены отдельно от динамических обращений. Типы и листы сверены с system.json, module/setup/registerDataModels.js и module/setup/registerSheets.js. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Курсы — относительные коэффициенты в общей базе, не запрос рынка и не настройка world. По умолчанию falsecoin исключён из обоих select и балансов, курса для него нет. amount/fee из обычного input Number/null, from/to String. Балансы показываются до подтверждения; currencyData сохраняет ссылку до await render/input, rates запрашиваются после подтверждения. Комиссия применяется к конвертированному результату, затем floor; списывается полный amount. Пример bizant2→floren при10%: floor(2×4/3×0.9)=2; ducat2→crown даёт0, но списывает2. Fee100 даёт0. При from=to объект содержит только последнее значение newTo: crown100,amount10,fee0→110 (старый issue20). В обычном обмене crown100/oren5→90/15. update ожидается; один payload не означает проверки конкурентной свежести баланса. ChatMessage создаётся только после успешного update, но его завершение не возвращается.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Весь файл/маршрут | nl/rg; группы01–17,19–21 | Все три метода, временные значения, внешние шаги и оба HBS прочитаны | Не запуск мира |
| Проверки чисел | 01–12 | Шесть курсов; корректные/некорректные вводы; комиссии/округление; same currency20; исключённые/неизвестные ключи | Часть значений программно передана через input фасад, не штатный select |
| Асинхронность | 13–17 | update держит Promise, отказ не даёт chat; chat pending при returned; два одновременных обмена имеют одинаковый payload; replacement модели при открытом окне использует старую ссылку | Контролируемые Promise/записи, не доказательство каждой серверной гонки |
| Форма/API | 02,12,19–21 | Настоящий core input/FormDataExtended; direct _onSubmit не вызывает checkValidity;16 ключей EN/RU | Санитизация и маршруты клика дополнительно прочитаны статически; браузер не запускался |

## Непроверенные участки и открытые вопросы

Проверены локальные исходники Foundry 14.367.0, Node 24.16.0, настоящие модели/методы/HBS и отдельные core-функции. Dialog, базовые приложения, коллекции и запись документов подменены; EventTarget настоящий Node, не браузерный DOM. Мир, сеть, права и транзакции реальной БД не запускались. HTML min/max/step не выдаются за серверную валидацию. Курсы и экономические правила не менялись. Прямые вызовы на Character/Monster/Loot проверены с реальными моделями. Наличие метода у Actor не означает кнопку у каждого листа. Имена source/target должны рассматриваться как технические ключи; экономическая политика округления и same currency не выбиралась.

## Связанные проблемы

[issue-00020](../../../../../../issues/potential/issue-00020.md), [issue-00227](../../../../../../issues/potential/issue-00227.md), [issue-00228](../../../../../../issues/potential/issue-00228.md), [issue-00229](../../../../../../issues/potential/issue-00229.md), [issue-00231](../../../../../../issues/potential/issue-00231.md). 20 уточнён без нового ID; новые наблюдения остаются potential. Повторная регистрация кнопки отдельно в карточке примеси листа/issue230. Отличие от покупки issue221: этот процесс ожидает update.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `32d8fdd029ce4c6401db25f0d9645445ac0f8ca2`; полный файл | Первая карточка; [сверка порции](../../../../review-log.md#task-0003036) |
