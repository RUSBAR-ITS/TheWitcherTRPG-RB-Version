# module/chatMessage/chatMessageData.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/chatMessage/chatMessageData.js](../../../../../../module/chatMessage/chatMessageData.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `9f16a7ae4bc942df85a105fd37d9a3cb3ef99f4b` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.028](../../../../../tasks/task-0003.028.md), 5 файлов, 372 логических строк |
| Запись перекрёстной сверки | [TASK-0003.028](../../../review-log.md#task-0003028) |

## Назначение файла

Собирает обычный объект параметров сообщения: speaker, flavor, type, system и flags. Используется перед Roll.toMessage/extendedRoll и для добавления блоков результата защиты. Отличается от схем BaseMessageData/AttackMessageData/DefenseMessageData, которые описывают message.system.

## Условия использования

Default-export class без наследования. constructor сразу вызывает ChatMessage.getSpeaker({actor}); остальной код работает с переданными ссылками. Для корректной адресации нужен объект Actor; строка UUID не разрешается здесь самостоятельно. Не регистрируется как документ или DataModel.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| ChatMessageData | default class, 1–21 | Контейнер параметров сообщения | Default import | Создание в обработчиках бросков и прямого урона. |
| speaker / flavor / type / system / flags | constructor:2–7 | Пять полей | Открытые свойства | speaker вычисляется ядром; остальные назначаются непосредственно. |
| append(messageData) | 10–20 | Дополнение сообщения | Метод экземпляра | Склеивает flavor и поверхностно объединяет два объекта. |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| constructor(actor,flavor,type='base',system={},flags={TheWitcherTRPG:{}}) | Actor и произвольные данные сообщения | Новый объект | getSpeaker; сохраняет system/flags по ссылке | flavor не имеет default; неизвестный actor обрабатывается fallback ядра, не верифицируется этим классом. |
| append(messageData) | Объект с flavor/system/flags | undefined | flavor +=; system={...old,...new}; flags={...old,...new} | Объекты system/flags заменяются; вложенные данные не копируются глубоко. Новая namespace TheWitcherTRPG заменяет старую целиком, в том числе пустым объектом. speaker/type не меняются. |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| ChatMessage.getSpeaker | Foundry 14.367.0: client/documents/chat-message.mjs:231–329 | Глобальный API | constructor:3 | Проверены настоящие getSpeaker и три private helper: Actor, Token, fallback на персонажа пользователя/пользователя. |
| BaseMessageData / AttackMessageData / DefenseMessageData | [module/data/chatMessage/baseMessageData.js](../../../../../../module/data/chatMessage/baseMessageData.js); [module/data/chatMessage/attackMessageData.js](../../../../../../module/data/chatMessage/attackMessageData.js); [module/data/chatMessage/defenseMessageData.js](../../../../../../module/data/chatMessage/defenseMessageData.js) | Связь по данным, без импорта | type/system передаются далее в ChatMessage | Конструктор этой карточки ничего не преобразует по схемам; схемы применяет Foundry при создании сообщения. |
| registerDataModels / ChatMessage types | [module/setup/registerDataModels.js](../../../../../../module/setup/registerDataModels.js); [system.json](../../../../../../system.json) | Регистрация внешнего потребителя | Модели base/attack/defense/damage | registerDataModels:76–80; manifest объявляет attack/defense/damage; известное наблюдение о base отделено от этого контейнера. |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/actor/mixins/skillMixin.js](../../../../../../module/actor/mixins/skillMixin.js) | ChatMessageData | Броски навыков: getCustomModifier, ChatMessageData base и RollConfig; пользовательский навык не задаёт threshold. | rollSkillCheck:57–82; rollCustomSkillCheck:146–172 |
| [module/actor/sheets/mixins/statMixin.js](../../../../../../module/actor/sheets/mixins/statMixin.js) | ChatMessageData | Спасбросок с reversal и модификатором; репутация — reversal либо обычный бросок. Перед вызовом присваивает flavor. | _onStatSaveRoll:13–35; _onReputation:51–81 |
| [module/actor/sheets/mixins/deathSaveMixin.js](../../../../../../module/actor/sheets/mixins/deathSaveMixin.js) | ChatMessageData | Испытание смерти: reversal=true, showCrit=false, threshold=stunBase; передаёт ChatMessageData base. | _onDeathSaveRoll:26–42 |
| [module/actor/mixins/defenseMixin.js](../../../../../../module/actor/mixins/defenseMixin.js) | ChatMessageData | Защита откладывает сообщение, дополняет ChatMessageData через append({crit})/append({stun}); stunSave отключает крит и включает reversal. | 194–241, createDefenseRollConfig:293–299, stunSave:437–451 |
| [module/actor/mixins/professionMixin.js](../../../../../../module/actor/mixins/professionMixin.js) | ChatMessageData | Атака профессии; бросок профессионального навыка с getCustomModifier, порогом и showResult из аргументов. У навыка в speaker передано this.actor. | 222–229, doProfessionSkillRoll:350–378 |
| [module/actor/mixins/verbalCombatMixin.js](../../../../../../module/actor/mixins/verbalCombatMixin.js) | ChatMessageData | addPart собирает формулу; сообщение damage с vcDamage и два дополнительных флага verbalCombat/damage. Вызов extendedRoll не ожидает. | 61–84, createVerbalCombatFlags:87–101 |
| [module/actor/mixins/castSpellMixin.js](../../../../../../module/actor/mixins/castSpellMixin.js) | ChatMessageData | Атака заклинанием: ChatMessageData attack, RollConfig({showResult:false}); затем await roll.toMessage(messageData). | 238–248 |
| [module/actor/mixins/weaponAttackMixin.js](../../../../../../module/actor/mixins/weaponAttackMixin.js) | ChatMessageData | Оружейная атака: ChatMessageData attack с UUID атакующего; extendedRoll с конфигурацией по умолчанию, без импорта RollConfig. | 303–310 |
| [module/actor/sheets/WitcherCharacterSheet.js](../../../../../../module/actor/sheets/WitcherCharacterSheet.js) | ChatMessageData | Изготовление: создаёт ChatMessageData base, задаёт RollConfig и тексты, вызывает Item.realCraft либо extendedRoll для симуляции. | ChatMessageData:265/361; конфигурация и вызов:326–346/414–434 |
| [module/scripts/verbalCombat/verbalCombatDefense.js](../../../../../../module/scripts/verbalCombat/verbalCombatDefense.js) | ChatMessageData | Словесная защита: ChatMessageData base, defense=true и порог totalAttack; передаёт флаги createVerbalCombatFlags. Выбор Actor отдельно в context callback:13. | 94–123 |
| [module/actor/sheets/WitcherActorSheet.js](../../../../../../module/actor/sheets/WitcherActorSheet.js) | ChatMessageData | Создаёт ChatMessageData(this.actor) без flavor; отдельный 1d10x10 через Roll.toMessage, без extendedRoll. | _onCritRoll:253–256 |
| [module/actor/sheets/WitcherActorSheetV1.js](../../../../../../module/actor/sheets/WitcherActorSheetV1.js) | ChatMessageData | Аналогичный отдельный 1d10x10 и ChatMessageData без flavor; без extendedRoll. | _onCritRoll:230–233 |
| [module/item/mixins/damageUtilMixin.js](../../../../../../module/item/mixins/damageUtilMixin.js) | ChatMessageData | getRandomInt(100) для вероятности эффекта; ChatMessageData(this.parent, flavor, 'damage', {damage}) для урона. | 61, 77 |

Область поиска: module/ и templates/ текущего checkout; прямые импорты и места вызова сверены отдельно от динамических обращений. Типы сообщений проверены по system.json и module/setup/registerDataModels.js. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Конструктор не создаёт ChatMessage в БД. system/flags извне сначала сохраняют идентичность; extendedRoll затем записывает system.rollTotal и дописывает flavor. append переобъявляет только два верхних объекта и flavor. Если исходный flavor не задан, append со строкой даёт префикс undefined. В _onCritRoll обоих базовых листов flavor действительно не задан, но append/extendedRoll не вызываются — эта ветвь не доказывает префикс undefined в интерфейсе. В защите две операции append добавляют crit и stun к исходным defender/defense/rollTotal; текущие три объекта не несут содержательных flags.TheWitcherTRPG, поэтому потеря уже заполненной namespace там не воспроизведена.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Объект и append | Группа 02; 21 строка целиком | Проверены идентичность входов, новая ссылка после append, сохранение вложенных ссылок, прежних speaker/type, перезапись namespace и undefinedsuffix | Слияние настоящее; ChatMessage.create не вызывается. |
| Адресация speaker | Группа 14 | Настоящие методы ядра отличают Actor от UUID; корректный Actor A остаётся A, UUID приводит к fallback B/пользователю | Минимальные Actor/Token-классы и game/canvas заменены; документы мира не читались. |
| Обратные связи | 13 импортирующих файлов; defenseMixin:194–241 | Найдены два append только в защите; прямые _onCritRoll обходят extendedRoll | Полный цикл боевых моделей/чата оставлен внешней связью. |

## Непроверенные участки и открытые вопросы

Полностью прочитаны 21 строка. Поверхностное слияние flags и flavor без default — ограничения API, но текущая цепочка защиты не передаёт непустые конфликтующие namespace. Поэтому самостоятельная issue о потере флагов в append не заведена. Сохранение и рендер реального сообщения, включая схему type=base, в этой порции не проверялись.

## Связанные проблемы

[issue-00005](../../../../../issues/potential/issue-00005.md), [issue-00126](../../../../../issues/potential/issue-00126.md), [issue-00175](../../../../../issues/potential/issue-00175.md), [issue-00182](../../../../../issues/potential/issue-00182.md). issue-00126/00175 и новая issue-00182 относятся к вызывающим местам, передающим неподходящий actor; контейнер сам UUID/имя в Actor не преобразует. issue-00005 — отдельное наблюдение о регистрации типов.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `9f16a7ae4bc942df85a105fd37d9a3cb3ef99f4b`; полный файл | Первая карточка; [сверка порции](../../../review-log.md#task-0003028) |

## Уточнение TASK-0003.029

2026-09-11, `273a6d7db0b7c866399db3ecd4f7191817ae6f10`. Оба броска навыка создают ChatMessageData(this, '<характеристика>: <навык> Check') с корректным Actor, типом base и стандартным пустым system. Вычисляемый extendedRoll дополняет результат и публикует; свойств Item в messageData класс не извлекает. Английское Check — буквальный текст формулы подписи, не отдельный новый ключ локализации.

Сверенные связи: [module/actor/mixins/skillMixin.js](../../../../../../module/actor/mixins/skillMixin.js). Полные карточки новых файлов — в [указателе порции](../../README.md#навыки-броски-развитие-и-пользовательские-навыки--task-0003029). [Проверки, ограничения и версия](../../../review-log.md#task-0003029). Исходники и статус проблем не менялись.
