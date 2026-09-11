# module/actor/sheets/mixins/statMixin.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/actor/sheets/mixins/statMixin.js](../../../../../../../../module/actor/sheets/mixins/statMixin.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `aa6af106e86a9c75fe050d599f961c8fadb74f1b` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.030](../../../../../../../tasks/task-0003.030.md), 9 файлов, 424 логических строк |
| Запись перекрёстной сверки | [TASK-0003.030](../../../../../review-log.md#task-0003030) |

## Назначение файла

Примесь листов Actor для спасброска характеристики, двух бросков репутации, суммы исходных максимумов и ручных действий с удачей/адреналином.

## Условия использования

Именованный export statMixin подключён к V2/V1 ActorSheet и WitcherModifiersConfiguration. Требует actor и глобальные Foundry/Roll/Dialog/jQuery. calc_total_stats используется CharacterSheet; у MonsterSheet аналогичного заполнения totalStats не найдено.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| statMixin | export let, 6–132 | Восемь методов листа | Object.assign трёх прототипов | Броски, ресурсы, сумма и слушатели |
| Dialog.buttons.t1/t2.callback | 38–86 | Спасбросок и давление репутацией | Локальные async callback | После выбора создают ChatMessageData/RollConfig и запускают extendedRoll |
| parts / statName | 8–35 | Формула 1d10 и динамическая подпись WITCHER.St<Stat> | Локальные переменные | Пользовательский модификатор добавляется к кубику, характеристика служит порогом |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| _onStatSaveRoll(event) | closest('.stat-display').dataset.stat; Actor.stats | Promise<void> после extendedRoll | Порог = value для восьми характеристик, max для luck; 1d10 + getCustomModifier; reversal/showCrit/showSuccess=true, thresholdDesc=statName | Не прибавляет характеристику к кубику; строгий roll<threshold. Возврат Roll не передаёт. Отмена/неизвестный stat отклоняют Promise |
| _onReputation(event) | Actor.reputation.value и stats.will.value | Promise<void> сразу после render Dialog | t1:1d10 с reversal и порогом reputation.value; t2:1d10 + Number(rep.value) + Number(will.value) без порога | Callback ожидают броски; внешний метод не ждёт выбора/закрытия. Криты обоих бросков включены стандартным RollConfig |
| calc_total_stats(context) | context.system.stats | Сумма max | for..in всех записей кроме ключа toxicity | value и totalModifiers непосредственно не читаются; нет floor/min/max и фильтра по конфигурации |
| _onLuckMinus(event) | luck.value | Ожидает Actor.update при value>0 | preventDefault; value−1 | Ноль/отрицательное не меняет; 0.5 даёт −0.5, поскольку нижнего clamp нет |
| _onLuckReset(event) | luck.max | Ожидает Actor.update | preventDefault; value=max | Копирует фактический максимум без собственного ограничения |
| _onAdrenalineMinus(event) | adrenaline.value | Ожидает Actor.update при value>0 | preventDefault; value−1 | Не проверяет optional setting; 0.5 даёт −0.5 |
| _onAdrenalinePlus(event) | Actor.addAdrenaline | Promise<void> до записи Actor | preventDefault; вызов addAdrenaline | Не ожидает/не возвращает Promise метода; сам addAdrenaline также не ждёт update |
| statListener(html) | DOM и $ | Шесть click-обработчиков | stat-roll, reputation-roll, luck-minus/reset, adrenaline-minus/plus привязаны к this | html заменяется локальной jQuery-обёрткой; глобальную jQuery этот метод не перезаписывает |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| extendedRoll | [module/scripts/rolls/extendedRoll.js](../../../../../../../../module/scripts/rolls/extendedRoll.js) | Прямой named import | Все три броска | Строки 1,35,63,80; отрицательный threshold отключает сравнение |
| RollConfig | [module/scripts/rollConfig.js](../../../../../../../../module/scripts/rollConfig.js) | Прямой named import | Опции порога, reversal, критов и вывода | Строки 2,29–34,58–62,80 |
| ChatMessageData | [module/chatMessage/chatMessageData.js](../../../../../../../../module/chatMessage/chatMessageData.js) | Прямой default import | Actor speaker и message type base | Строки 3,13,50,71 |
| getCustomModifier | [module/scripts/helper.js](../../../../../../../../module/scripts/helper.js) | Прямой named import | Диалог только спасброска характеристики | Строки 4,23–27 |
| Stats/stat / Reputation / adrenaline | [module/data/actor/templates/common/stats/statData.js](../../../../../../../../module/data/actor/templates/common/stats/statData.js); [module/data/actor/templates/common/stats/statsData.js](../../../../../../../../module/data/actor/templates/common/stats/statsData.js); [module/data/actor/templates/common/reputationData.js](../../../../../../../../module/data/actor/templates/common/reputationData.js); [module/data/actor/templates/common/adrenalineData.js](../../../../../../../../module/data/actor/templates/common/adrenalineData.js) | Поля моделей | max/value, пределы и типы чисел | Определения полей; дробные ресурсы допускаются схемой |
| addAdrenaline | [module/actor/mixins/adrenalineMixin.js](../../../../../../../../module/actor/mixins/adrenalineMixin.js) | Метод составного Actor | Проверка useOptionalAdrenaline и update | _onAdrenalinePlus |
| tab-stats и sidebar | [templates/partials/character/tab-stats.hbs](../../../../../../../../templates/partials/character/tab-stats.hbs); [templates/sheets/actor/partials/character/sidebar.hbs](../../../../../../../../templates/sheets/actor/partials/character/sidebar.hbs) | DOM-контракт | Броски текущей вкладки и четыре ресурсные кнопки | Селекторы и dataset |
| game.i18n / Dialog / Actor.update / $ | Foundry VTT 14.367, браузер/jQuery; словари lang/en.json и lang/ru.json | Внешний API | Локализация, legacy Dialog и изменения документа | JSON локализации предварительно раскрывается expandObject |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/actor/sheets/WitcherActorSheet.js](../../../../../../../../module/actor/sheets/WitcherActorSheet.js) | statMixin | Импорт/Object.assign, statListener | 5, activateListeners,310 |
| [module/actor/sheets/WitcherActorSheetV1.js](../../../../../../../../module/actor/sheets/WitcherActorSheetV1.js) | statMixin | Импорт/Object.assign, statListener | 5, activateListeners,290 |
| [module/actor/sheets/configurations/WitcherModifiersConfiguration.js](../../../../../../../../module/actor/sheets/configurations/WitcherModifiersConfiguration.js) | statMixin | Импорт/Object.assign; activateListeners | 4,50,70 |
| [module/actor/sheets/WitcherCharacterSheet.js](../../../../../../../../module/actor/sheets/WitcherCharacterSheet.js) | calc_total_stats | context.totalStats | _prepareCharacterData:168 |
| [templates/partials/character/tab-stats.hbs](../../../../../../../../templates/partials/character/tab-stats.hbs) | stat/reputation-roll | Текущие цели клика обоих Actor-листов | Классы и stat dataset |
| [templates/sheets/actor/partials/character/sidebar.hbs](../../../../../../../../templates/sheets/actor/partials/character/sidebar.hbs) | luck/adrenaline кнопки | Текущие ресурсные действия персонажа | 136–156 |
| [templates/sheets/actor/monster-sheet.hbs](../../../../../../../../templates/sheets/actor/monster-sheet.hbs) | stat-roll | Старый шаблон, активный V2 потребитель не найден | Строка 15; контекст .stat-display родителя |

Область поиска: module/ и templates/ текущего checkout; прямые импорты и места вызова сверены отдельно от динамических обращений. Типы и листы сверены с system.json, module/setup/registerDataModels.js и module/setup/registerSheets.js. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Ресурсы пишутся в system.stats.luck.value/system.adrenaline.value. Броски и сумма не изменяют их. Сумма max отличается от текущих value и от исходных unmodifiedMax после эффектов. Комментарий перед _onStatSaveRoll просит сохранить метод для внешних модулей; он фактически делает спасбросок характеристики, хотя комментарий упоминает skill rolls.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Полный разбор | 132 строки; 4 импорта; 8 методов и 2 callback | Все определения и семь файлов потребителей сверены | Внешние модули не исследованы |
| Броски | Группы 01–03: настоящий Roll/парсер, 9 характеристик, модификаторы, 0/отрицательный порог, крит/провал, отмена | При value=3/max=8 и кубике 5 luck успешен, прочие нет; репутация 5+WILL4+кубик 5=14 | Dialog и отправка сообщений подменены |
| Ресурсы и сумма | Группы 04–06,10: настоящие модели и удержанные update | 9×max8=72, toxicity999 исключена; минус ожидает запись; плюс адреналина не ожидает | Без БД и конкурентного клиента |

## Непроверенные участки и открытые вопросы

Полный браузерный Dialog и submit не запускались; частные числовые ограничения описаны как код, не как новое правило. _onStatSaveRoll допускает отрицательный порог, который общий обработчик не сравнивает. Вся подготовка Actor проверена здесь только в используемых расчётах.

## Связанные проблемы

[issue-00012](../../../../../../../issues/potential/issue-00012.md), [issue-00035](../../../../../../../issues/potential/issue-00035.md), [issue-00036](../../../../../../../issues/potential/issue-00036.md), [issue-00196](../../../../../../../issues/potential/issue-00196.md), [issue-00197](../../../../../../../issues/potential/issue-00197.md), [issue-00199](../../../../../../../issues/potential/issue-00199.md), [issue-00193](../../../../../../../issues/potential/issue-00193.md). Предыдущие проблемы расчёта связаны с их потребителями; русский savingThrow добавлен к уточнённой языковой карточке.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `aa6af106e86a9c75fe050d599f961c8fadb74f1b`; полный файл | Первая карточка; [сверка порции](../../../../../review-log.md#task-0003030) |
