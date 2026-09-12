# module/scripts/combat/combat.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/scripts/combat/combat.js](../../../../../../../module/scripts/combat/combat.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-12 |
| Ветка и коммит | rusbar-main, 20ce99a1218a82bf46c84570e55587253d0cfbc3 |
| Изменения относительно коммита | Нет; совпадает со срезом TASK-0001 15da5b225535e34af4e132c701b5353ef4eb667f |
| Задача и порция | [TASK-0003.045](../../../../../../tasks/task-0003.045.md), 5 файлов / 336 логических строк; данный файл — 96 |
| Запись перекрёстной сверки | [TASK-0003.045](../../../../review-log.md#task-0003045) |

## Назначение файла

Связывает боевые кнопки и контекстные команды чата с броском урона Item, защитой, оглушением и критическими последствиями Actor.

## Условия использования

Именованные экспорты импортируются namespace Combat в [module/TheWitcherTRPG.js](../../../../../../../module/TheWitcherTRPG.js). renderChatMessageHTML:52–58 вызывает attackChatMessageListeners и defenseChatMessageListeners с HTMLElement. getChatMessageContextOptions:139–140 подключает два расширения меню. Сам модуль не регистрирует Hook и при импорте не применяет урон. addAttackChatListeners — прежний массовый обход: прямого вызова в module/templates не найдено; его jQuery-контракт несовместим с нынешним одиночным listener.

## Введённые сущности и действия с ними

| Сущность | Вид и место | Доступность | Действия |
| --- | --- | --- | --- |
| addAttackChatListeners | function:3–13 | export | Обход .chat-message, чтение data-message-id и коллекции сообщений |
| attackChatMessageListeners | async arrow:15–17 | export | Назначение click первой button.damage |
| onDamage | function:19–24 | local | UUID Item → rollDamage с damage сообщения |
| defenseChatMessageListeners | async arrow:26–38 | export | Click каждой button.stun и button.crit-stun |
| addDefenseOptionsContextMenu | function:40–51 | export | Добавление пункта защиты с visible/onClick |
| executeDefense | async function:53–65 | local | Получение сообщения и вызов Actor.prepareAndExecuteDefense |
| addCritMessageContextOptions | function:67–96 | export | Три пункта: весь критический урон, бонусный урон, травма |
| each / canDefend / wasCritted / click / onClick | closures:4–11,16,28–36,41–48,68–94 | callbacks DOM/меню | Замыкают message либо читают ID целевого элемента; возвращают найденный объект как условие видимости |

## Основные функции и методы

| Функция | Входы | Результат и действия | Ошибки и ожидания |
| --- | --- | --- | --- |
| addAttackChatListeners(html) | jQuery-совместимый .find/.each; .data('messageId') | undefined; неизвестное сообщение пропускается; найденное передаётся одиночному listener | async callback each не ожидается внешней функцией; element после $ всё ещё jQuery, а следующий метод требует querySelector |
| attackChatMessageListeners(message,html) | HTMLElement-контейнер | Promise undefined после регистрации click; отсутствующая button допустима | querySelector выбирает только первую; повторная регистрация добавляет listener; метод не ожидает будущего click |
| onDamage(message) | system.attack.itemUuid и system.damage | undefined; fromUuidSync → item.rollDamage(damage) | Нет guard Item/attack; не возвращает и не ждёт rollDamage |
| defenseChatMessageListeners(message,html) | HTMLElement и attackWeaponProperties.stun для обычного stun | Promise undefined после регистрации всех кнопок; обычная stun передаёт stun, критическая — без аргумента | В click ожидается getInteractActor, но отсутствующий Actor не проверяется, stunSave не ожидается |
| addDefenseOptionsContextMenu(html,options) | Массив menu entries | Тот же массив с одним пунктом; visible читает message.system.defenseOptions | html не используется; отсутствующее message ломает visible; onClick ждёт выбор, но не executeDefense |
| executeDefense(actor,messageId) | Actor, message.system с пятью аргументами защиты | При !actor return; иначе вызов prepareAndExecuteDefense(attack,defenseOptions,damage,attackRoll,attacker) | Нет guard сообщения; Promise защиты не возвращает/не ожидает |
| addCritMessageContextOptions(html,options) | Массив меню | Тот же массив + applyCritDamage/applyBonusCritDamage/applyCritWound; visible ищет .crit-taken | Callback получает target вторым аргументом, выбирает Actor и передаёт message.system.crit; нет guard Actor/message; вызванные методы не ожидаются |

Нажатие на вложенный элемент кнопки не меняет сообщение: click замыкает message и не читает event.target. Контекстные onClick используют второй аргумент target, а не дочерний элемент PointerEvent. Поэтому замечание про event.target у ремонта не переносится сюда автоматически. Действия не отмечают сообщение использованным: повторное нажатие запускает действие повторно; намерение запрещать повторы не установлено.

## Используемые сущности и зависимости

| Сущность | Источник | Вид связи и место | Основание |
| --- | --- | --- | --- |
| getInteractActor | [module/scripts/helper.js](../../../../../../../module/scripts/helper.js) | import:1; stun/menu callbacks | Возвращает выбранный Actor либо undefined; отмена input может отклонить Promise |
| rollDamage | [module/item/mixins/damageUtilMixin.js](../../../../../../../module/item/mixins/damageUtilMixin.js); сборка [module/item/witcherItem.js](../../../../../../../module/item/witcherItem.js) | onDamage:23; динамический метод Item | Получает system.damage; ожидает методы DamageProperties в сообщении атаки |
| prepareAndExecuteDefense / stunSave | [module/actor/mixins/defenseMixin.js](../../../../../../../module/actor/mixins/defenseMixin.js); [module/actor/witcherActor.js](../../../../../../../module/actor/witcherActor.js) | executeDefense:58–64; click:29/35 | Методы на Actor через Object.assign; сборка/бросок защиты и спасбросок |
| applyCritDamage / applyBonusCritDamage / applyCritWound | [module/actor/mixins/damageMixin.js](../../../../../../../module/actor/mixins/damageMixin.js) | Три критических onClick | HP и получение Item критической травмы — downstream |
| AttackMessageData | [module/data/chatMessage/attackMessageData.js](../../../../../../../module/data/chatMessage/attackMessageData.js); [module/data/chatMessage/templates/attackData.js](../../../../../../../module/data/chatMessage/templates/attackData.js) | Чтение system.attack/damage/defenseOptions/attackRoll/attacker | Очищенная модель сохраняет itemUuid и восстанавливает DamageProperties |
| DefenseMessageData | [module/data/chatMessage/defenseMessageData.js](../../../../../../../module/data/chatMessage/defenseMessageData.js) | system.attackWeaponProperties.stun / crit | critEffectModifier теряется до этого consumer; он не восстанавливает ключ |
| Контекстные labels | [lang/en.json](../../../../../../../lang/en.json), [lang/ru.json](../../../../../../../lang/ru.json) | WITCHER.Context.Defense, applyCritDmg, applyBonusCritDmg, applyCritWound | Имена ключей сверяются с исходником; локализация через game.i18n |
| game.messages / fromUuidSync / HTMLElement / $ | Foundry 14.367.0, DOM, jQuery | Поиск документов и назначение listeners | Документы в опытах — map-фасады; синхронный UUID resolver не загружает документ асинхронно |
| ContextMenu.onClick / visible | /opt/foundryvtt/client/applications/ux/context-menu.mjs | onClick(event,target), visible(target) | Настоящий _onClickItem исполнен с DOM-фасадом; ApplicationV2 передаёт jQuery:false |

## Известные потребители

| Файл | Сущность | Условие / доказательство |
| --- | --- | --- |
| [module/TheWitcherTRPG.js](../../../../../../../module/TheWitcherTRPG.js) | Два render-listener и два menu extender | renderChatMessageHTML и getChatMessageContextOptions; прямые регистрации |
| [module/actor/mixins/weaponAttackMixin.js](../../../../../../../module/actor/mixins/weaponAttackMixin.js) | button.damage / данные атаки | Формирует flavor и сообщение атаки; обработку клика получает через Hook |
| [module/actor/mixins/professionMixin.js](../../../../../../../module/actor/mixins/professionMixin.js); [templates/chat/combat/spellItem.hbs](../../../../../../../templates/chat/combat/spellItem.hbs); [module/actor/mixins/castSpellMixin.js](../../../../../../../module/actor/mixins/castSpellMixin.js) | Кнопка урона и attack.itemUuid | Альтернативные producers; отсутствие Item у профессии описано в issue-00239 |
| [templates/chat/combat/defense/defenseCrit.hbs](../../../../../../../templates/chat/combat/defense/defenseCrit.hbs); [templates/chat/combat/defense/defenseStun.hbs](../../../../../../../templates/chat/combat/defense/defenseStun.hbs) | .crit-taken, button.crit-stun, button.stun | append из defenseMixin → сообщение → Hook |

Поиск выполнен по module/templates. Для addAttackChatListeners найдено только определение; сторонние модули и макросы не исследованы. Локальные onDamage/executeDefense не экспортированы.

## Данные и изменения состояния

В модуле добавляются listeners и элементы options. Сам не пишет Actor/Item/ChatMessage: запросы передаются методам документов. Передаёт вложенные объекты по ссылке, не пересоздаёт crit и не читает flags вместо system. Выбранный Actor не обязательно speaker исходного сообщения. Видимость меню не проверяет ownership документа/возможность записи.

## Проверки и доказательства

| Проверка | Результат | Пределы |
| --- | --- | --- |
| Группы 01–03 | Первая damage-кнопка, все stun-кнопки, вложенный target, отсутствие кнопок, повторная регистрация; неизвестный Item → исключение; несовместимый jQuery → querySelector TypeError | DOM/$/UUID — фасады; массовый обход проверен для отсутствующего сообщения и отдельно граница передачи jQuery |
| Группы 04–05 | Без Actor executeDefense выходит; stun/три critical callbacks отклоняются; точные пять аргументов защиты и identity crit сохранены; отсутствующее message ломает обработку | Методы Actor фиксируют вызов; полный бросок не повторён |
| Группа 06 | Реальный ContextMenu Foundry передал target обеим формам callback | Без браузерного render/позиционирования меню |
| Группа 23 | Настоящий DefenseMessageData удалил modifier; критический onClick передал тот же очищенный crit | Выбор компедиума/создание травмы в этой группе не запускались |

## Непроверенные участки и открытые вопросы

Все 96 строк прочитаны. Реальные нажатия в браузере, права, удаление документов, повторный рендер клиента, сохранение чата и полный многоклиентский бой не проверены. Получение Item по UUID и Actor через helper представлены явно заданными результатами. Отмена выбора helper описана прежней .028; в .045 проверено отсутствие Actor и отклонение окна нанесения урона, без повторного запуска всех вариантов выбора.

## Связанные проблемы

[149](../../../../../../issues/potential/issue-00149.md) — отсутствие Actor/отмена, уже включает боевых потребителей; [239](../../../../../../issues/potential/issue-00239.md) — отсутствующий Item у кнопки способности; [258](../../../../../../issues/potential/issue-00258.md) — потеря critEffectModifier. [299](../../../../../../issues/potential/issue-00299.md) — раннее завершение цепочек действий, особенно урона начала хода. Устаревший неиспользуемый массовый wrapper и первая damage-кнопка описаны как ограничения, без утверждения о неисправности штатной карточки с одной кнопкой.

## История актуализации

| Дата | Версия и область | Результат |
| --- | --- | --- |
| 2026-09-12 | 20ce99a1218a82bf46c84570e55587253d0cfbc3; полный файл | Первичная карточка; [перекрёстная сверка](../../../../review-log.md#task-0003045) |
