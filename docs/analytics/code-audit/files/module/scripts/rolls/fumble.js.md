# module/scripts/rolls/fumble.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/scripts/rolls/fumble.js](../../../../../../../module/scripts/rolls/fumble.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `9f16a7ae4bc942df85a105fd37d9a3cb3ef99f4b` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.028](../../../../../../tasks/task-0003.028.md), 5 файлов, 372 логических строк |
| Запись перекрёстной сверки | [TASK-0003.028](../../../../review-log.md#task-0003028) |

## Назначение файла

Добавляет в контекстное меню сообщения пункт результата провала и выбирает текст для атак/защиты. Не бросает кубики повторно и не применяет урон, травму, потерю надёжности или статус: создаёт описательное сообщение.

## Условия использования

TheWitcherTRPG.js импортирует namespace Fumble и регистрирует addFumbleContextOptions на getChatMessageContextOptions. При построении меню добавляется entry с visible и legacy callback. В Foundry 14.367 ChatLog использует ApplicationV2._createContextMenu с jQuery:false: callback получает HTMLElement первым аргументом, что соответствует li.dataset. Пользовательское нажатие запускает локальный applyFumble.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| addFumbleContextOptions / isFumble / callback | export:4–15; локальные closures:5, 10–12 | Добавление и действие пункта меню | Hook через главный модуль | Проверка rolls[0].options.fumble; html аргумент не используется. |
| applyFumble | 17–26 | Выбор обработчика | Локальная функция | switch по точному message.system.constructor. |
| attackFumble / defenseFumble | 28–73 / 75–93 | Разбор типа атаки/защиты | Локальные функции | Читают fumbleAmount и поля моделей. |
| unarmedAttackDefense | 95–106 | Общая таблица безоружного провала | Локальная функция | Возвращает суффикс ключа локализации либо undefined. |
| createResultMessage | 108–119 | Вывод результата | Локальная async-функция | Формирует speaker/content/style, инициирует ChatMessage.create. |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| addFumbleContextOptions(html,options) | Массив пунктов меню | Тот же options | push({label,icon,visible,callback}) | Мутирует options; не фильтрует тип ChatMessage заранее. |
| isFumble(li) — локальная closure | HTMLElement с dataset.messageId, существующее message и rolls | Первый Roll.options.fumble либо undefined | game.messages.get → rolls[0]?.options.fumble | rolls=[] скрывает пункт; отсутствующее message/rolls/dataset вызывает TypeError. |
| callback(li) / applyFumble(message) | Пункт по существующему сообщению | Promise<undefined> / undefined | Для точного DefenseMessageData/AttackMessageData вызывает соответствующую функцию | base/damage/неизвестный constructor и subclass не обрабатываются. callback не возвращает завершение ChatMessage.create. |
| attackFumble(message) | attack.skill/attackOption, attacker, rolls[0].options.fumbleAmount | undefined | Две независимые проверки melee/ranged, затем spell переопределяет результат | Неизвестный skill без spell → undefined; UUID attacker передаётся как actor без разрешения. |
| defenseFumble(message) | defense, defender, fumbleAmount | undefined | <6 → nothing; melee кроме brawling → armedDefense, остальные → unarmed | Без отдельной магической/дальней таблицы защиты; 9 у вооружённой защиты попадает в >9. |
| unarmedAttackDefense(fumbleAmount) | Число | Суффикс nothing/unarmed.* либо undefined | <6 nothing; 6–8 точные ключи; >9 тяжёлый исход | 9 не попадает ни в одну ветвь. |
| createResultMessage(actor,result) | Ожидаемый Actor и суффикс локализации | Promise<undefined> | HTML с WITCHER.fumbleResults.name и WITCHER.fumbleResults.<result>; user, speaker, style OTHER | getSpeaker получает переданный аргумент; ChatMessage.create не ожидается, цепочка не возвращает Promise записи. |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| AttackMessageData | [module/data/chatMessage/attackMessageData.js](../../../../../../../module/data/chatMessage/attackMessageData.js) | Default import и точное сравнение constructor | 18–23, 30–31 | attacker — DocumentUUIDField; attack — SchemaField; attackRoll getter здесь не читается. |
| DefenseMessageData | [module/data/chatMessage/defenseMessageData.js](../../../../../../../module/data/chatMessage/defenseMessageData.js) | Default import и точное сравнение constructor | 18–20, 77–85 | defender — DocumentUUIDField, defense — StringField. |
| attackData.skill / attackOption | [module/data/chatMessage/templates/attackData.js](../../../../../../../module/data/chatMessage/templates/attackData.js) | Поля входной схемы | attackFumble | Оба StringField; attackOption==='spell' перекрывает выбранную таблицу. |
| WITCHER.meleeSkills / rangedSkills | [module/setup/config.js](../../../../../../../module/setup/config.js) | Глобальная конфигурация | 35, 49, 83 | Строки 136–137: melee=brawling/melee/smallblades/staffspear/swordsmanship; ranged=athletics/archery/crossbow. |
| fumble / fumbleAmount | [module/scripts/rolls/extendedRoll.js](../../../../../../../module/scripts/rolls/extendedRoll.js) | Данные Roll.options | 5, 29, 76 | fumbleAmount сохраняется до ограничения итогового результата нулём; таблица использует полную величину. |
| WITCHER.Context.fumble / fumbleResults.* | [lang/en.json](../../../../../../../lang/en.json); [lang/ru.json](../../../../../../../lang/ru.json) | Локализованные название и таблицы | Меню и createResultMessage | Сверены все подтаблицы, включая существующие armedDefense.9 и unarmed.9; rangedAttack ключи 6-7, 8-9, >9. |
| ChatMessage.getSpeaker / create, CONST.CHAT_MESSAGE_STYLES.OTHER | Foundry 14.367.0: client/documents/chat-message.mjs:231–329; ChatMessage/CONST API | Внешнее создание сообщения | 113–118 | getSpeaker исполнен настоящий; UUID строка не является Actor и ведёт к fallback. create представлен фасадом. |
| getChatMessageContextOptions / ContextMenu callback | Foundry 14.367.0: client/applications/sidebar/tabs/chat.mjs:398–403; api/application.mjs:2230–2235; ux/context-menu.mjs:621 | Hook и сигнатура legacy callback | Регистрация и вызов entry | jQuery:false → target HTMLElement; неподходящий PointerEvent вместо li не является контрактом этого callback. |
| registerDataModels | [module/setup/registerDataModels.js](../../../../../../../module/setup/registerDataModels.js) | Регистрация моделей входных документов | CONFIG.ChatMessage.dataModels | 76–80: классы base/attack/defense/damage; строгий constructor ограничивает обработчик двумя из них. |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/TheWitcherTRPG.js](../../../../../../../module/TheWitcherTRPG.js) | Fumble.addFumbleContextOptions | Namespace import и Hook регистрации | 8, 141; регистрация отделена от последующего вызова меню. |

Область поиска: module/ и templates/ текущего checkout; прямые импорты и места вызова сверены отдельно от динамических обращений. Типы сообщений проверены по system.json и module/setup/registerDataModels.js. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Фактические диапазоны: melee кроме brawling — <6 nothing, 6/7/8/9 одноимённые, >=10 >9; ranged — <6 nothing, только 6 → 6-7, 7/8 → 8-9, >=9 → >9; spell — <7 → 1-6, 7/8/9 → 7-9, >=10 → >9. Вооружённая защита — <6 nothing, 6/7/8 одноимённые, >=9 >9. Безоружная атака/прочая защита — <6 nothing, 6/7/8 одноимённые, 9 undefined, >9 тяжёлый исход. Эти границы описывают код, а не утверждают соответствие книге правил.

Воздействие ограничено дополнительным сообщением. Инлайн-формулы из переводов могут обрабатываться стандартным отображением чата, но этот файл их не вычисляет и не списывает ресурсы. Нет удаления исходного сообщения и признака уже обработанного провала; повторное нажатие снова создаёт текст.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Все таблицы | Группа 12; ключи en/ru; CONFIG.WITCHER | 70 проверок: 7 маршрутов × 0/1/5/6/7/8/9/10/11/23; отдельно неизвестный навык и все melee/rangedSkills | Настоящие Attack/Defense DataModel и методы; локализация возвращала ключи для точной проверки ветви. |
| Меню и типы | Группа 13; исходник ContextMenu | base/обычный объект/subclass видимы при fumble=true, callback ничего не создаёт; rolls=[] скрывает пункт; неправильные event/message дают TypeError | Выполнены callbacks с DOM-фасадом; браузерное меню не запускалось. |
| Actor сообщения | Группа 14 | UUID Actor A при назначенном B дал speaker B и для attack, и для defense; без персонажа — пользователь; корректный объект Actor A в контрольном getSpeaker дал A | Настоящий код getSpeaker и реальные поля модели; Actor/canvas/create заменены. |

## Непроверенные участки и открытые вопросы

Все 119 строк прочитаны. Сопоставлены код, конфигурация и переводы; правила рулбука, стихийные последствия и отдельный полноценный боевой процесс не исследовались. Неизвестный skill без spell и неверный fumbleAmount не валидируются; это отмечено как входной контракт. Полный флоу схемы base в мире ограничен известным наблюдением issue-00005.

## Связанные проблемы

[issue-00005](../../../../../../issues/potential/issue-00005.md), [issue-00181](../../../../../../issues/potential/issue-00181.md), [issue-00182](../../../../../../issues/potential/issue-00182.md), [issue-00183](../../../../../../issues/potential/issue-00183.md). Три новых наблюдения: диапазоны таблиц, UUID вместо Actor у speaker и видимый пункт без обработчика для других типов сообщений. Все остаются potential.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `9f16a7ae4bc942df85a105fd37d9a3cb3ef99f4b`; полный файл | Первая карточка; [сверка порции](../../../../review-log.md#task-0003028) |
