# module/scripts/combat/applyDamage.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/scripts/combat/applyDamage.js](../../../../../../../module/scripts/combat/applyDamage.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-12 |
| Ветка и коммит | rusbar-main, 20ce99a1218a82bf46c84570e55587253d0cfbc3 |
| Изменения относительно коммита | Нет; совпадает со срезом TASK-0001 15da5b225535e34af4e132c701b5353ef4eb667f |
| Задача и порция | [TASK-0003.045](../../../../../../tasks/task-0003.045.md), 5 файлов / 336 логических строк; данный файл — 124 |
| Запись перекрёстной сверки | [TASK-0003.045](../../../../review-log.md#task-0003045) |

## Назначение файла

Добавляет команды нанесения урона из чата, получает параметры применения в диалоге и передаёт урон сообщения или статуса в Actor.applyDamage.

## Условия использования

Namespace ApplyDamage в [module/TheWitcherTRPG.js](../../../../../../../module/TheWitcherTRPG.js) регистрирует addDamageMessageContextOptions на getChatMessageContextOptions:136. [module/scripts/combat/generalCombatHook.js](../../../../../../../module/scripts/combat/generalCombatHook.js) импортирует applyDamageFromStatus. При загрузке сохраняется DialogV2, игровые действия ещё не выполняются. Экспортированы addDamageMessageContextOptions, ApplyNormalDamage, ApplyNonLethalDamage, applyDamageFromStatus.

## Введённые сущности и действия с ними

| Сущность | Вид / место | Доступность | Действия |
| --- | --- | --- | --- |
| DialogV2 | const:4 | local | Ссылка на Foundry prompt |
| addDamageMessageContextOptions | function:6–35 | export | Два пункта меню с общим canApplyDamage |
| canApplyDamage / callback | closures:7,13–19,25–31 | menu entries | Проверка .damage-message, выбор Actor, чтение первой .dice-total |
| ApplyNormalDamage | async:37–40 | export в конце файла | HP либо STA по isNonLethal |
| ApplyNonLethalDamage | async:42–44 | export в конце файла | Безусловный STA |
| createApplyDamageDialog | async:46–97 | local | Формирование HTML и чтение пяти параметров |
| locationOptions / ok.callback | строка:47–56; closure:77–85 | local / prompt | Восемь вариантов локации; optional чтение элементов формы |
| applyDamageFromStatus | async:99–101 | export в конце файла | Один DamageInstance с типом, без диалога |
| applyDamageFromMessage | async:103–122 | local | Диалог, изменение prepared damage и вызов Actor |

## Основные функции и методы

| Функция | Входы | Действия / результат | Ошибки, ожидания |
| --- | --- | --- | --- |
| addDamageMessageContextOptions(html,options) | Массив меню | Возвращает тот же массив + обычный/несмертельный урон; visible ищет .damage-message | html не используется; callback ждёт Actor, читает parseInt первого .dice-total.innerText и li.dataset.messageId; не ждёт Apply* |
| ApplyNormalDamage(actor,totalDamage,messageId) | Сообщение с system.damage.properties | Передаёт hp, либо sta при isNonLethal | Promise undefined без ожидания applyDamageFromMessage; неизвестное message отклоняет собственный Promise |
| ApplyNonLethalDamage(actor,totalDamage,messageId) | Те же параметры | Передаёт sta независимо от флага | Вложенный Promise не ожидается/не возвращается |
| createApplyDamageDialog(actor,damageObject) | actor.type/system; location.alias; type | HTML → modal prompt; возвращает {resistNonSilver,resistNonMeteorite,newLocation,isVulnerable,addOilDmg} | rejectClose:true, отказ распространяется; optional controls могут дать undefined; отсутствующий Actor/location ломает создание |
| ok.callback(event,button,dialog) | button.form.elements | Читает changeLocation.value и checked четырёх checkbox | event/dialog не используются; отсутствующее поле даёт undefined |
| applyDamageFromStatus(actor,totalDamage,damageObject,derivedStat) | Число, полный объект damage, hp/sta | actor.applyDamage(null,[DamageInstance.create(totalDamage).setType(damageObject.type)],damageObject,derivedStat) | Без guard/type/числовой валидации; Promise Actor не ожидается |
| applyDamageFromMessage(actor,totalDamage,messageId,derivedStat) | Сообщение, Actor, число | Берёт system.damage по ссылке; ждёт диалог; при newLocation!='Empty' заменяет location; при addOilDmg присваивает oilEffect=actor.system.category; передаёт один DamageInstance | Actor.applyDamage не ожидается; !addOilDmg не удаляет ранее записанное масло; flags и Roll не читает |

### Диалог

Empty сохраняет текущую локацию. Остальные значения: head, torso, leftArm, rightArm, leftLeg, rightLeg, tailWing. Список одинаков для типов Actor; monster дополнительно получает resistNonSilver/resistNonMeteorite с начальными значениями из resistantNonSilver/resistantNonMeteorite. В шаблонной строке false выводится как атрибут unchecked; он не является checked. isVulnerable/addOilDmg изначально не отмечены, прежний oilEffect не управляет галочкой. Отдельного HBS у этого окна нет. location.alias и локализованные строки вставлены прямо в HTML; sanitization/браузер не проверялись.

### Контекстное меню Foundry 14

Старый callback здесь поддерживается ядром: ContextMenu._onClickItem вызывает callback(target,event). ChatLog._onFirstRender создаёт меню через ApplicationV2._createContextMenu, который задаёт jQuery:false. Поэтому li в данном зарегистрированном маршруте — HTMLElement. Это отличается от других меню, которые забывают jQuery:false или используют неподходящую сигнатуру. Deprecation сама по себе не доказывает поломку.

## Используемые сущности и зависимости

| Сущность | Источник | Связь / место | Основание |
| --- | --- | --- | --- |
| DamageInstance.create / setType | [module/scripts/damageInstance.js](../../../../../../../module/scripts/damageInstance.js) | import:1; applyStatus:100 / applyMessage:118 | amount и type передаются без преобразования в Roll |
| getInteractActor | [module/scripts/helper.js](../../../../../../../module/scripts/helper.js) | import:2; menu callbacks | Выбор получателя урона; возможен undefined |
| applyDamage / location | [module/actor/mixins/damageMixin.js](../../../../../../../module/actor/mixins/damageMixin.js); [module/actor/mixins/locationMixin.js](../../../../../../../module/actor/mixins/locationMixin.js); [module/actor/witcherActor.js](../../../../../../../module/actor/witcherActor.js) | Динамические методы Actor | Расход щита, SP, HP/STA/temporaryHP и эффекты принадлежат следующему модулю |
| system.damage | [module/data/chatMessage/damageMessageData.js](../../../../../../../module/data/chatMessage/damageMessageData.js); [module/data/chatMessage/templates/damageData.js](../../../../../../../module/data/chatMessage/templates/damageData.js); [module/data/chatMessage/templates/locationData.js](../../../../../../../module/data/chatMessage/templates/locationData.js) | prepared-схемы сообщения | effects уже Array с applied; duration не объявлена; location — mutable object |
| isNonLethal / oilEffect | [module/data/item/templates/combat/damagePropertiesData.js](../../../../../../../module/data/item/templates/combat/damagePropertiesData.js) | Копия схемы внутри DamageMessageData | Ресурс и масляный бонус |
| resistantNonSilver / resistantNonMeteorite / category | [module/data/actor/monsterData.js](../../../../../../../module/data/actor/monsterData.js) | Начальные checkbox и oilEffect | Имена полей Actor отличаются от имён возвращаемых controls |
| DialogV2.prompt | /opt/foundryvtt/client/applications/api/dialog.mjs, Foundry 14.367.0 | Модальное окно с rejectClose:true | Callback настоящий, prompt в опытах — фасад |
| .dice-total / .damage-message | [module/item/mixins/damageUtilMixin.js](../../../../../../../module/item/mixins/damageUtilMixin.js) и Foundry Roll chat render | Чтение HTML результата | rollDamage формирует marker/flavor, числовую .dice-total формирует ядро; не суммирует message.rolls |
| ContextMenu / ApplicationV2 / ChatLog | /opt/foundryvtt/client/applications/ux/context-menu.mjs; applications/api/application.mjs:2230–2235; applications/sidebar/tabs/chat.mjs:398–403 | callback совместимости, jQuery:false | Код ядра прочитан; настоящий dispatch проверен локально |
| game.i18n / Context.*, Damage.*, DamageType.*, Dialog.attack* | [lang/en.json](../../../../../../../lang/en.json), [lang/ru.json](../../../../../../../lang/ru.json) | Подписи меню, типа, восьми options и checkbox | Проверка существования через expandObject/getProperty описана в журнале |

## Известные потребители

| Файл | Сущность | Действие |
| --- | --- | --- |
| [module/TheWitcherTRPG.js](../../../../../../../module/TheWitcherTRPG.js) | addDamageMessageContextOptions | Hook расширения меню |
| [module/scripts/combat/generalCombatHook.js](../../../../../../../module/scripts/combat/generalCombatHook.js) | applyDamageFromStatus | Эффекты начала хода, hp/sta |
| Этот файл | ApplyNormalDamage / ApplyNonLethalDamage / внутренние функции | callback → wrapper → dialog → Actor |

В module/templates внешних прямых вызовов ApplyNormalDamage/ApplyNonLethalDamage не найдено. Наличие export допускает вызовы макросов, которые в область поиска не входят.

## Данные и изменения состояния

Операция изменяет prepared system.damage существующего сообщения по ссылке. На настоящей DamageMessageData _source остался исходным; message.update не вызывается. Следующее применение того же живого объекта видит изменённые location/oilEffect даже при Empty и снятой галочке масла. Перезагрузка/повторная подготовка документа — отдельный lifecycle, его результат в клиенте не проверен. Сам файл не записывает HP/STA, он запускает Actor.applyDamage.

Число берётся из HTML: 7.9 превращается в 7, '?' в NaN, отсутствие .dice-total вызывает исключение. message.rolls и system.rollTotal не используются; два результата в DOM не суммируются. Это не поддержка составной формулы: составной Roll обычно уже имеет один итог; несколько отдельных Roll — другая граница.

## Проверки и доказательства

| Проверка | Фактический результат | Пределы |
| --- | --- | --- |
| Группы 06–08 | Ядро поддерживает callback; первый DOM total7.9 дал 7 вопреки rolls99/1; isNonLethal/принудительный режим → STA; отсутствующий total → TypeError, '?' → NaN | DOM и Actor фасады; не заявлена штатная генерация неверного HTML |
| Группы 09–11 | Wrapper завершается при pending prompt, внутренний метод — при pending applyDamage; 8 options, monster controls и callback проверены; cancel прерывает внутренний метод до Actor | Диалог не открывался в браузере; внешние wrappers не перехватывают отказ внутреннего Promise |
| Группа 12 | Настоящий DamageMessageData: duration удалена, head/oil меняются в prepared, _source прежний; следующий Actor получает head/старое масло | Записи сообщения нет; live-document reprepare не моделировался |
| Группы 29–31 | Настоящие downstream методы: потерянный fire даёт 5 вместо 9 при flat.fire4; две записи HP97/96 из 100; отрицательный damage повышает shield5→8 | Документный update управляется в памяти, сеть и БД не запускались |

## Непроверенные участки и открытые вопросы

Все 124 строки разобраны. Не проверены sanitization/реальный DOM, права на выбранного Actor, асинхронная загрузка сообщений, реальный отказ update и взаимодействие клиентов. Связанные ошибки расчёта щита, SP и временных HP не исправлены; успешный вызов этой обёртки не доказывает успешную запись.

## Связанные проблемы

[21](../../../../../../issues/potential/issue-00021.md) — потеря типа до applyDamageFromStatus; [149](../../../../../../issues/potential/issue-00149.md) — отсутствие выбранного Actor; [257](../../../../../../issues/potential/issue-00257.md) — потерянная duration; [299](../../../../../../issues/potential/issue-00299.md) — отсутствие ожидания; [300](../../../../../../issues/potential/issue-00300.md) — повторное использование изменённых данных сообщения; [301](../../../../../../issues/potential/issue-00301.md) — непроверенный DOM total. [291](../../../../../../issues/potential/issue-00291.md) — отрицательный итог статуса доходит до увеличения щита.

## История актуализации

| Дата | Версия и область | Результат |
| --- | --- | --- |
| 2026-09-12 | 20ce99a1218a82bf46c84570e55587253d0cfbc3; полный файл | Первичная карточка; [перекрёстная сверка](../../../../review-log.md#task-0003045) |
