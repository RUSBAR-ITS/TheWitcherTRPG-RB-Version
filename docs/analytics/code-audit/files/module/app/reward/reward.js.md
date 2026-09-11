# module/app/reward/reward.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/app/reward/reward.js](../../../../../../../module/app/reward/reward.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `639fde4bad4a7ba4c538d3b08ddc5cfd846ca75e` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.037](../../../../../../tasks/task-0003.037.md), 8 файлов, 313 логических строк |
| Запись перекрёстной сверки | [TASK-0003.037](../../../../review-log.md#task-0003037) |

## Назначение файла

Публичный сервис выдачи IP и валюты: формирует список получателей, запрашивает параметры, вызывает журнал Actor и создаёт общее сообщение.

## Условия использования

main.init публикует ссылки game.api.rewards.ip/currency. Оба handout проверяют game.user.isGM до окна; диалоги сами права не проверяют и только собирают данные. Без actors или при null диалог использует getPlayerActors(); явный [] остаётся пустым.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| Rewards | default class:5–178 | Пять static методов | game.api.rewards через main | Диалог → Log → chat |
| DialogV2 | local const:3 | Ссылка на Foundry API | Оба диалога | input возвращает form values или отмену |
| options/choosenActors | Локальные массивы | UUID/name выбора и результаты fromUuidSync | Не экспортируются | options selected:true; map получателей без filter/dedupe |
| forEach/map callbacks | getPlayerActors и оба диалога/handout | Отбор hasPlayerOwner, сбор вариантов, вызовы Log | Локальные обработчики | Не возвращают агрегированный Promise |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| getPlayerActors() | game.actors коллекция | Actor[] | filter(actor=>actor.hasPlayerOwner) | Без фильтра type/active/наличия logs; GM не считается player owner |
| ipRewardDialog(actors) | Actor[] или отсутствие; CONFIG/core DOM | Promise values | multi-checkbox actors; text label; number ip; checkbox isMagic; DialogV2.input | Все options preselected; нет required/min/max/step; прямой вызов не начисляет |
| handoutIpRewards(actors) | GM; ответ actors,ip,label,isMagic | Promise<void> | await dialog; guard выбора; fromUuidSync; if(ip) Log.addIpReward; await render; if(ip) ChatMessage.create | Не ждёт записи Log или ChatMessage; неправильный Actor прерывает batch |
| currencyRewardDialog(actors) | Actor[]; CONFIG.WITCHER.currency | Promise values | multi-checkbox actors; text label; number amount; select type с localize:true | Семь CONFIG ключей, включая falsecoin; нет conversion/rates |
| handoutCurrencyRewards(actors) | GM; ответ actors,amount,label,type | Promise<void> | Как IP; Log.addCurrencyReward и chat context amount/type | Не проверяет допустимость type; context не имеет currency — ветка HBS не показывается |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| createLabeledInput/createLabeledSelect | [module/app/htmlUtils.js](../../../../../../../module/app/htmlUtils.js) | Named import | import1 и сборка обоих диалогов | Полностью сверены helpers |
| DialogV2.input/FormDataExtended | Foundry 14.367.0: client/applications/api/dialog.mjs, ux/form-data-extended.mjs | Внешний API | Возврат данных формы | Исполнено тело input с facade prompt/form; ядро обрабатывает отмену отдельно |
| createMultiSelectInput/createSelectInput | Foundry 14.367.0: applications/forms/fields.mjs; elements/multi-select.mjs | Создание полей | actors и type | Реальные builders/_initialize/_getValue; Set убирает повторные выбранные UUID |
| game.actors / hasPlayerOwner / fromUuidSync | Foundry 14.367.0: client/documents/abstract/client-document.mjs:163–165 и UUID API | Коллекция/разрешение UUID | Выбор и повторное разрешение после ответа | Getter учитывает любого не-GM OWNER, даже inactive; fromUuidSync в сценарии — map |
| game.user.isGM / ChatMessage.create / CONST.CHAT_MESSAGE_STYLES.OTHER | Foundry 14.367.0, глобальные API | Права/сообщения | Guard57/145 и ChatMessage.create86/176 | Нет своего socket/проверки конкретного документа или speaker/timestamp |
| CONFIG.WITCHER.currency | [module/setup/config.js](../../../../../../../module/setup/config.js) | Конфигурация | Ключи и labels select type | Все семь валют; rates/excluded конвертера не используются |
| game.api.rewards | [module/TheWitcherTRPG.js](../../../../../../../module/TheWitcherTRPG.js) | Регистрация | Публичные handout | main39–41: ссылки на методы; тело обращается к Rewards, не к this API |
| Log.addIpReward/addCurrencyReward | [module/data/actor/templates/character/logData.js](../../../../../../../module/data/actor/templates/character/logData.js) | Динамические вызовы | actor.system.logs,69/157 | Методы push историю и update абсолютный баланс |
| logs/IP/magic/currency модели | [module/data/actor/characterData.js](../../../../../../../module/data/actor/characterData.js); [module/data/actor/commonActorData.js](../../../../../../../module/data/actor/commonActorData.js); [module/data/actor/monsterData.js](../../../../../../../module/data/actor/monsterData.js); [module/data/actor/lootData.js](../../../../../../../module/data/actor/lootData.js); [module/data/actor/templates/character/ipLogData.js](../../../../../../../module/data/actor/templates/character/ipLogData.js); [module/data/actor/templates/character/currencyLogData.js](../../../../../../../module/data/actor/templates/character/currencyLogData.js); [module/data/actor/templates/common/currencyData.js](../../../../../../../module/data/actor/templates/common/currencyData.js) | Пути данных/контракт | Получатели и payload | logs/IP/magic определяет CharacterData; Monster/Loot имеют currency без logs |
| Шаблон сообщения | [templates/chat/rewards.hbs](../../../../../../../templates/chat/rewards.hbs) | renderTemplate | 73/161 | IP context actors,label,ip; currency context actors,label,amount,type |
| Локализация WITCHER.rewards / WITCHER.Currency | [lang/en.json](../../../../../../../lang/en.json); [lang/ru.json](../../../../../../../lang/ru.json) | Строки формы/сообщения | localize заголовка/подписей/options | Отсутствуют dialog.amount и chat.amount после expandObject/fallback |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/TheWitcherTRPG.js](../../../../../../../module/TheWitcherTRPG.js) | Rewards | default import22; init game.api.rewards | 39–41 |
| [module/actor/mixins/rewardsMixin.js](../../../../../../../module/actor/mixins/rewardsMixin.js) | Публичные handout | Обёртки передают [this] | 3/7 |
| [templates/chat/rewards.hbs](../../../../../../../templates/chat/rewards.hbs) | Контекст сообщения | Отрисовывается обоими handout | Прямые renderTemplate |

Область поиска: module/ и templates/ текущего checkout; прямые импорты и места вызова сверены отдельно от динамических обращений. Типы и листы сверены с system.json, module/setup/registerDataModels.js и module/setup/registerSheets.js. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Оба DialogV2.input задают window.title через WITCHER.rewards.dialog.title, ok.label через WITCHER.rewards.dialog.confirm и ok.icon=fa-solid fa-floppy-disk. modal/rejectClose и обработчики записи в конфигурации не задаются. Дополнительный вызов localize(WITCHER.rewards.dialog.label) перед сборкой поля не используется. Для денежного select передаётся type=single; createSelectInput формирует обычный одиночный select.

Ввод actors — массив UUID, label — строка, ip/amount — Number (пустое поле → null), isMagic — Boolean, type — строка. Нативный select по умолчанию выбирает первый bizant. ip/amount=0 или null пропускают update и создание чата, но при непустом выборе шаблон всё равно рендерится. Отрицательные и дробные числовые payload принимаются; допустимость такой корректировки как игрового правила здесь не определяется. Нет проверки конечности/диапазона в handout.

Журнал — не источник вычисления остатка: Log прибавляет награду к текущему improvementPoints либо magic.magicImprovementPoints/currency[type] и записывает всю историю. Нет общего await/rollback/результатов на каждого получателя. fromUuidSync→undefined или отсутствие logs вызывает TypeError, возможно после вызовов для предыдущих Actor. Асинхронный отказ update не проходит через Promise handout и не мешает последующему сообщению. Частичный/повторный сценарий отличается от доказательства серверной гонки.

Оба handout создают OTHER chat без speaker, timestamp, isMagic и подтверждений записей. В IP HBS отображается ip, в currency не передан проверяемый флаг currency. Собственной даты в ipLog/currencyLog нет; метаданные даты ChatMessage не являются датой записи журнала. Неизвестный type из подменённого ответа доходит до NaN patch; обычный select его не предлагает. Повторные UUID в нормальном multi-checkbox дедуплицируются Set, а уже подменённый массив handout принимает повторно.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Полный маршрут | Группы01–15 | Обе формы, реальная модель/журнал, GM guard, zero, multiple, invalid receivers | Dialog/Actor persistence заменены |
| Асинхронность | Группы16–19 | Wrapper/Log/chat Promise не соединены; 10+2+3 при удержании записей даёт patches12/13 | Контролируемый порядок, не серверное воспроизведение |
| Форма/локализация/журналы | Группы20–24 | Просмотр, bool/тип, экранирование, отсутствующие переводы; inactive player owner входит | Настоящие модели/core функции, не клиентский UI |

## Непроверенные участки и открытые вопросы

Файл прочитан целиком. Изолированные вызовы исполняют настоящий код, модели и Handlebars 4.7.9 на Foundry 14.367.0 / Node 24.16.0; Application, DOM и Actor.update/ChatMessage.create — фасады. Браузерное отображение/валидация, доступ службы по HTTP, серверные права, БД и несколько клиентов не проверялись. Реальные макросы миров и сторонние модули не исследовались.

## Связанные проблемы

[issue-00028](../../../../../../issues/potential/issue-00028.md), [issue-00030](../../../../../../issues/potential/issue-00030.md), [issue-00017](../../../../../../issues/potential/issue-00017.md), [issue-00232](../../../../../../issues/potential/issue-00232.md), [issue-00233](../../../../../../issues/potential/issue-00233.md), [issue-00234](../../../../../../issues/potential/issue-00234.md), [issue-00235](../../../../../../issues/potential/issue-00235.md). issue17 относится к иной операции levelUpSkill: выдача isMagic=true здесь увеличивает правильный пул. Issue30 — соседняя неподдержанная IP-форма monster; новый233 фиксирует самостоятельный путь наград. Асинхронный риск уточняет28, а не создаёт её дубликат.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `639fde4bad4a7ba4c538d3b08ddc5cfd846ca75e`; полный файл | Первая карточка; [сверка порции](../../../../review-log.md#task-0003037) |
