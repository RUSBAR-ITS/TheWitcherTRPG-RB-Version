# module/TheWitcherTRPG.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/TheWitcherTRPG.js](../../../../../module/TheWitcherTRPG.js) |
| Тип файла | JavaScript |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `3252300787c348e11f95098c345a6af7704b690c`; исходник совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f` |
| Изменения относительно коммита | Нет |
| Задача и порция | [TASK-0002](../../../../tasks/task-0002-system-initialization.md); порция 1 |
| Запись перекрёстной сверки | [Журнал сверок](../../review-log.md) — TASK-0002, порция 1 |

## Назначение файла

Точка входа системы: связывает конфигурацию и классы документов с Foundry, регистрирует обработчики жизненного цикла, чата и макросов, публикует API наград и эффектов, подключает интеграцию Polyglot.

## Условия использования

Подключается из system.json как ES-модуль. При его оценке выполняются импорты, registerHooks(), регистрация Hooks и registerHandelbarHelpers(). Тела init, ready, обработчиков чата и Polyglot выполняются позднее по соответствующим событиям. Ошибка одного этапа не означает, что последующие строки уже выполнены.

## Введённые сущности и действия с ними

| Сущность и строки | Вид / доступность | Действие |
| --- | --- | --- |
| Обработчик init — 27–50 | Одноразовый Hook | Устанавливает CONFIG.WITCHER/statusEffects, классы Item/Actor/ActiveEffect и expiryAction=delete; присваивает game.api; вызывает пять функций регистрации/подготовки |
| Обработчик renderChatMessageHTML — 52–58 | Повторяемый Hook | Передаёт message и html пяти обработчикам: две функции Combat и по одной VerbalCombat, ApplyStatusEffects, Chat; их обещания не ожидаются |
| renderActiveEffectConfig — 60 | Пустой async Hook | Зарегистрирован, но действий не выполняет |
| Обработчик ready — 62–92 | Одноразовый async Hook | Сначала ожидает индекс pack; затем регистрирует hotbarDrop, применяет шрифт при настройке, вызывает регистрацию сокета и deprecationWarnings |
| hotbarDrop — 70–75 | Hook, создаваемый внутри ready | Для data.type=Item вызывает createMacro и возвращает false; обещание createMacro не возвращается |
| FictionalGameSystemLanguageProvider — 95–132 | Локальный класс, extends LanguageProvider | Объявляет common/dwarven/elder и метод getUserLanguages; передаётся API Polyglot |
| getUserLanguages(actor) — 102–131 | Метод локального класса | Возвращает [known_languages, literate_languages]; common включён всегда, elder/dwarven добавляются по флагам навыка или modifiedValue>0; literate_languages остаётся пустым |
| Шесть getChatMessageContextOptions — 136–141 | Регистрации внешних функций | Добавляют действия урона, вербального боя, защиты, критов и осложнений |
| createMacro(data, slot) — 150–170 | Локальная async-функция, не экспортируется | Проверяет принадлежность UUID Actor/Token, получает Item, ищет или создаёт Macro, назначает его на панель |
| game.api — 37–43 | Объект, присваиваемый глобальному game | Публикует applyActiveEffectToActorViaId и rewards.ip/currency; присваивание заменяет предыдущее значение game.api |

## Основные функции и методы

| Функция / обработчик | Входы | Результат | Основные действия и ограничения |
| --- | --- | --- | --- |
| init | Нет используемых аргументов | undefined | Последовательная регистрация; preloadHandlebarsTemplates вызван без await. Фактическое завершение загрузки шаблонов не гарантируется возвратом init |
| ready | Нет используемых аргументов | Promise; при нормальном завершении undefined | getIndex требует существующий pack. При отказе getIndex или отсутствии pack остальные действия этого callback не выполняются |
| renderChatMessageHTML | message, html; data не используется | undefined | Передаёт управление зависимым функциям, собственного разбора HTML нет |
| polyglot.init | LanguageProvider от внешнего модуля | undefined | Создаёт класс и вызывает game.polyglot.api.registerSystem |
| getUserLanguages | actor с system.skills.int | Массив двух Set | Читает три навыка, не записывает Actor; отсутствие нужной структуры не проверяется |
| createMacro | data.uuid, slot | Promise; явного итогового return нет | fromUuidSync должен вернуть принадлежащий Actor/Token Item. Команда обращается к actor.useItem; поиск Macro по имени и строке команды. UUID и результат fromUuidSync после первоначальной строковой проверки не валидируются |
| Анонимные callback поиска Macro и применения CSS | m или el | Boolean / undefined | Сравнение name/command; добавление класса witcher-style |

createMacro формирует строку `actor = fromUuidSync(...); actor.useItem(...)`; объявление actor в этой строке отсутствует. Исполнение созданного макроса ядром не проверялось, поэтому отдельный вывод о его работоспособности здесь не делается.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| { WITCHER } | [module/setup/config.js](../../../../../module/setup/config.js) | Импорт и вызов / регистрация | Импорт в строке 1; использование в обработчиках выше | Файл существует; просмотрены экспорты: `export const WITCHER = {};` (стр. 1) |
| Chat.chatMessageListeners (namespace import Chat) | [module/scripts/chat.js](../../../../../module/scripts/chat.js) | Импорт и вызов / регистрация | Импорт в строке 2; использование в обработчиках выше | Файл существует; просмотрены экспорты: `export function chatMessageListeners(message, html) {` (стр. 4) |
| VerbalCombat.chatMessageListeners, VerbalCombat.addVerbalCombatMessageContextOptions | [module/scripts/verbalCombat/verbalCombat.js](../../../../../module/scripts/verbalCombat/verbalCombat.js) | Импорт и вызов / регистрация | Импорт в строке 3; использование в обработчиках выше | Файл существует; просмотрены экспорты: `export function addVerbalCombatChatListeners(html) {` (стр. 3); `export function addVerbalCombatMessageContextOptions(html, options) {` (стр. 15); `export const chatMessageListeners = async (message, html) => {` (стр. 32); `export async function rollDamage(verbalCombat, damage) {` (стр. 44); `export async function applyVerbalCombatDamage(targetActor, totalDamage, messageId) {` (стр. 52) |
| VerbalCombatDefense.addVerbalCombatDefenseMessageContextOptions | [module/scripts/verbalCombat/verbalCombatDefense.js](../../../../../module/scripts/verbalCombat/verbalCombatDefense.js) | Импорт и вызов / регистрация | Импорт в строке 4; использование в обработчиках выше | Файл существует; просмотрены экспорты: `export function addVerbalCombatDefenseMessageContextOptions(html, options) {` (стр. 6) |
| Combat.attackChatMessageListeners, Combat.defenseChatMessageListeners, Combat.addDefenseOptionsContextMenu, Combat.addCritMessageContextOptions | [module/scripts/combat/combat.js](../../../../../module/scripts/combat/combat.js) | Импорт и вызов / регистрация | Импорт в строке 5; использование в обработчиках выше | Файл существует; просмотрены экспорты: `export function addAttackChatListeners(html) {` (стр. 3); `export const attackChatMessageListeners = async (message, html) => {` (стр. 15); `export const defenseChatMessageListeners = async (message, html) => {` (стр. 26); `export function addDefenseOptionsContextMenu(html, options) {` (стр. 40); `export function addCritMessageContextOptions(html, options) {` (стр. 67) |
| ApplyDamage.addDamageMessageContextOptions | [module/scripts/combat/applyDamage.js](../../../../../module/scripts/combat/applyDamage.js) | Импорт и вызов / регистрация | Импорт в строке 6; использование в обработчиках выше | Файл существует; просмотрены экспорты: `export function addDamageMessageContextOptions(html, options) {` (стр. 6); `export { ApplyNormalDamage, ApplyNonLethalDamage, applyDamageFromStatus };` (стр. 124) |
| ApplyStatusEffects.chatMessageListeners | [module/scripts/statusEffects/applyStatusEffect.js](../../../../../module/scripts/statusEffects/applyStatusEffect.js) | Импорт и вызов / регистрация | Импорт в строке 7; использование в обработчиках выше | Файл существует; просмотрены экспорты: `export function addStatusEffectChatListeners(html) {` (стр. 3); `export const chatMessageListeners = async (message, html) => {` (стр. 15); `export async function onApplyStatus(event) {` (стр. 23); `export async function applyStatusEffectToTargets(statusEffects, duration) {` (стр. 30); `export async function applyStatusEffectToActor(actorUuid, statusEffectId, duration) {` (стр. 43) |
| Fumble.addFumbleContextOptions | [module/scripts/rolls/fumble.js](../../../../../module/scripts/rolls/fumble.js) | Импорт и вызов / регистрация | Импорт в строке 8; использование в обработчиках выше | Файл существует; просмотрены экспорты: `export function addFumbleContextOptions(html, options) {` (стр. 4) |
| { registerSettings } | [module/setup/settings.js](../../../../../module/setup/settings.js) | Импорт и вызов / регистрация | Импорт в строке 9; использование в обработчиках выше | Файл существует; просмотрены экспорты: `export const registerSettings = function () {` (стр. 1) |
| WitcherItem | [module/item/witcherItem.js](../../../../../module/item/witcherItem.js) | Импорт и вызов / регистрация | Импорт в строке 11; использование в обработчиках выше | Файл существует; просмотрены экспорты: `export default class WitcherItem extends Item {` (стр. 10) |
| WitcherActor | [module/actor/witcherActor.js](../../../../../module/actor/witcherActor.js) | Импорт и вызов / регистрация | Импорт в строке 12; использование в обработчиках выше | Файл существует; просмотрены экспорты: `export default class WitcherActor extends Actor {` (стр. 21) |
| { registerDataModels } | [module/setup/registerDataModels.js](../../../../../module/setup/registerDataModels.js) | Импорт и вызов / регистрация | Импорт в строке 14; использование в обработчиках выше | Файл существует; просмотрены экспорты: `export const registerDataModels = () => {` (стр. 35) |
| { registerSheets } | [module/setup/registerSheets.js](../../../../../module/setup/registerSheets.js) | Импорт и вызов / регистрация | Импорт в строке 15; использование в обработчиках выше | Файл существует; просмотрены экспорты: `export const registerSheets = () => {` (стр. 33) |
| { registerSocketListeners } | [module/setup/socketHook.js](../../../../../module/setup/socketHook.js) | Импорт и вызов / регистрация | Импорт в строке 16; использование в обработчиках выше | Файл существует; просмотрены экспорты: `export const registerSocketListeners = function () {` (стр. 1) |
| WitcherActiveEffect | [module/activeEffect/witcherActiveEffect.js](../../../../../module/activeEffect/witcherActiveEffect.js) | Импорт и вызов / регистрация | Импорт в строке 17; использование в обработчиках выше | Файл существует; просмотрены экспорты: `export default class WitcherActiveEffect extends ActiveEffect {` (стр. 3) |
| { registerHooks } | [module/setup/hooks.js](../../../../../module/setup/hooks.js) | Импорт и вызов / регистрация | Импорт в строке 18; использование в обработчиках выше | Файл существует; просмотрены экспорты: `export function registerHooks() {` (стр. 4) |
| { deprecationWarnings } | [module/setup/deprecations.js](../../../../../module/setup/deprecations.js) | Импорт и вызов / регистрация | Импорт в строке 19; использование в обработчиках выше | Файл существует; просмотрены экспорты: `export const deprecationWarnings = function () {` (стр. 3) |
| { applyActiveEffectToActorViaId } | [module/scripts/temporaryEffects/applyActiveEffect.js](../../../../../module/scripts/temporaryEffects/applyActiveEffect.js) | Импорт и вызов / регистрация | Импорт в строке 20; использование в обработчиках выше | Файл существует; просмотрены экспорты: `export async function applyActiveEffectToTargets(activeEffects, duration) {` (стр. 3); `export async function applyActiveEffectToActorViaId(actorUuid, itemUuid, applyWhen, duration) {` (стр. 14); `export async function applyActiveEffectToActor(actorUuid, activeEffects, duration) {` (стр. 32) |
| { preloadHandlebarsTemplates, registerHandelbarHelpers } | [module/setup/handlebars.js](../../../../../module/setup/handlebars.js) | Импорт и вызов / регистрация | Импорт в строке 21; использование в обработчиках выше | Файл существует; просмотрены экспорты: `export async function preloadHandlebarsTemplates() {` (стр. 1); `export async function registerHandelbarHelpers() {` (стр. 82) |
| Rewards.handoutIpRewards, Rewards.handoutCurrencyRewards | [module/app/reward/reward.js](../../../../../module/app/reward/reward.js) | Импорт и вызов / регистрация | Импорт в строке 22; использование в обработчиках выше | Файл существует; просмотрены экспорты: `export default class Rewards {` (стр. 5) |
| { registerQueries } | [module/setup/queries.js](../../../../../module/setup/queries.js) | Импорт и вызов / регистрация | Импорт в строке 23; использование в обработчиках выше | Файл существует; просмотрены экспорты: `export function registerQueries() {` (стр. 48) |
| Hooks, CONFIG, game, Macro, ui, fromUuidSync | Foundry 14.367.0 | Внешний API | Регистрация, доступ к настройкам/пакетам и создание Macro | Прочитана версия установленного ядра; полного запуска нет |
| LanguageProvider, game.polyglot.api | Внешний модуль Polyglot | Событие и наследование | polyglot.init, строки 94–134 | Условная интеграция; версия Polyglot и её выполнение не проверены |
| document, Set, Array | DOM и JavaScript | Внешняя среда | CSS-классы и наборы языков | Использование видно в строках 77–130 |
| WitcherActor.useItem | [module/actor/witcherActor.js](../../../../../module/actor/witcherActor.js) | Вызов из строки макроса | createMacro, строка 157 | Метод определён с 225-й строки |
| Навыки языка commonsp/eldersp/dwarven | [module/data/actor/templates/common/skills/intData.js](../../../../../module/data/actor/templates/common/skills/intData.js) | Чтение Actor.system.skills.int | getUserLanguages | Поля модели сверены: стр. 12–14; полный разбор Intelligence/Skill добавлен в TASK-0003.002 ниже |

## Известные потребители

| Потребитель | Сущность | Способ и условия | Основание |
| --- | --- | --- | --- |
| [system.json](../../../../../system.json) | Сам модуль | ES-модуль пакета | esmodules, строка 22 |
| [module/actor/mixins/rewardsMixin.js](../../../../../module/actor/mixins/rewardsMixin.js) | game.api.rewards.ip/currency | Методы addIpReward/addCurrencyReward передают [this] | Строки 3 и 7 |
| Foundry Hooks | Зарегистрированные callback | События init, ready, чат и hotbarDrop | Регистрации в данном файле |
| Polyglot | Класс LanguageProvider | Использование после события polyglot.init | Внешний модуль; фактический вызов не проверен |

Поиск потребителей выполнен в module, templates, styles, utils и манифесте. Прямых импортов точки входа другими исходниками не найдено; пользовательские макросы и сторонние модули не исследовались.

## Данные и изменения состояния

Изменяет реестры CONFIG, game.api и Hooks; может менять DOM-классы, создавать Macro и назначать панель пользователя. При ready загружает индекс компедиума. Сам не создаёт расу, травму или предмет Actor: соответствующие действия делегированы API и методам зависимостей.

## Проверки и доказательства

Прочитаны все 172 строки. Проверены 21 импорт и наличие экспортов в файлах-источниках; просмотрены определения непосредственных обработчиков чата, классов документов, API эффектов и наград. В изолированном Node vm выполнен исходный ready callback с подменёнными Foundry API: без pack получен TypeError до hotbarDrop/socket/deprecations; с pack.getIndex, возвращающим Promise, все три шага достигнуты. Эта проверка не запускает Foundry.

## Непроверенные участки и открытые вопросы

Исходник прочитан полностью. Не проверялись реальная загрузка мира, выполнение шаблонов, обработка DOM в браузере, запуск созданного макроса и Polyglot. Внутренние алгоритмы импортированных документов и обработчиков вне этой порции не объявляются изученными. Отказ предварительной загрузки шаблонов, замена game.api и неполный вход createMacro требуют отдельного сценария, если станет необходимо установить их пользовательское влияние.

## Связанные проблемы

[issue-00002](../../../../issues/potential/issue-00002.md) — отсутствие выбранного компедиума прерывает оставшуюся инициализацию ready.

## Дополнительная сверка навыков — TASK-0003.002

2026-09-10, HEAD `52acddd5fb7d67e993eed1ad2c89b335aef6fd1d`; исходник не изменён.

Группа [Intelligence](data/actor/templates/common/skills/intData.js.md) и вложенный [Skill](data/actor/templates/common/skills/skillData.js.md) разобраны полностью. getUserLanguages:102–130 читает существующие commonsp/eldersp/dwarven, три независимых признака обучения и getter modifiedValue=value+activeEffectModifiers. Common добавляется безусловно, затем при условии повторно в тот же Set; literate_languages этим методом не заполняется. Базовое API Polyglot и работа модуля в мире не проверялись.

Результаты и пределы проверок — в [журнале TASK-0003.002](../../review-log.md#task-0003002).

## История актуализации

2026-09-10 — первичный разбор полного файла на указанном коммите; сверка порции 1 отражена в журнале. Файлы зависимостей проверены в пределах определений и обращений, без объявления их полного разбора.

2026-09-10 — TASK-0003.002: уточнены связи моделей навыков и их потребителей, добавлены взаимные ссылки и фактические ограничения проверки.
