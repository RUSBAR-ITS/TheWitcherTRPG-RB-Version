# templates/chat/combat/defense/defenseStun.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/chat/combat/defense/defenseStun.hbs](../../../../../../../../templates/chat/combat/defense/defenseStun.hbs) |
| Тип файла | Handlebars / HTML |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-12 |
| Ветка и коммит | rusbar-main, 16695cbfc7fec3e0de56660c7cab21bc0304e94b |
| Изменения относительно коммита | Нет; совпадает со срезом TASK-0001 15da5b225535e34af4e132c701b5353ef4eb667f |
| Задача и порция | [TASK-0003.042](../../../../../../../tasks/task-0003.042.md), 5 файлов / 477 логических строк; данный файл — 3 |
| Запись перекрёстной сверки | [TASK-0003.042](../../../../../review-log.md#task-0003042) |

## Назначение файла

Условная кнопка спасброска от оглушающего свойства атаки с отображением модификатора.

## Условия использования

[module/actor/mixins/defenseMixin.js](../../../../../../../../module/actor/mixins/defenseMixin.js):229–239 получает checkForStun(attackDamageObject), при truthy результате рендерит {stun}, дописывает flavor и system.stun. Сам HBS повторно проверяет if stun; результат защиты ему не передаётся.

## Введённые сущности и действия с ними

| Сущность | Строки | Назначение |
| --- | --- | --- |
| if stun | 1–3 | Нет объекта — нет HTML |
| button.stun | 2 | localize WITCHER.Defense.stun.button и экранированный stun.modifier |

## Основные способы использования

JS-функций, форм, partial и собственных обработчиков нет. Выведенный modifier — справочная часть кнопки; его не помещают в dataset. Отрицательное значение отображается как отрицательное число, ноль в штатном producer не приводит к объекту stun, поскольку проверка свойства truthy.

## Используемые сущности и зависимости

| Сущность | Источник | Вид / основание |
| --- | --- | --- |
| stun.modifier | [module/actor/mixins/defenseMixin.js](../../../../../../../../module/actor/mixins/defenseMixin.js):301–308 | checkForStun возвращает properties.stun для torso/head |
| properties.stun | [module/data/item/templates/combat/damagePropertiesData.js](../../../../../../../../module/data/item/templates/combat/damagePropertiesData.js) | NumberField; допускает знак, нулевое значение false в условии производителя |
| if / localize | Handlebars/Foundry, [lang/en.json](../../../../../../../../lang/en.json), [lang/ru.json](../../../../../../../../lang/ru.json) | Условие и ключ подписи |
| button.stun | [module/scripts/combat/combat.js](../../../../../../../../module/scripts/combat/combat.js):26–31 | getInteractActor → stunSave(message.system.attackWeaponProperties.stun) |
| stun.modifier / attackWeaponProperties.stun | [module/data/chatMessage/defenseMessageData.js](../../../../../../../../module/data/chatMessage/defenseMessageData.js) | Две копии значения в модели; обработчик читает вторую, не system.stun.modifier |
| .chat-message .flavor-text .stun | [styles/chat.css](../../../../../../../../styles/chat.css):70 | Оформление через входной CSS |

## Известные потребители

Производитель — [module/actor/mixins/defenseMixin.js](../../../../../../../../module/actor/mixins/defenseMixin.js), обработчик — [module/scripts/combat/combat.js](../../../../../../../../module/scripts/combat/combat.js), оформление — [styles/chat.css](../../../../../../../../styles/chat.css). Поиск по module/templates/styles выполнен. Клик не извлекает данные из event.target/currentTarget: callback замыкает message и выбирает Actor через getInteractActor.

## Данные и изменения состояния

Только HTML. Оглушение не применяется появлением кнопки; после клика stunSave выполняет бросок и при провале запрашивает статус. Отсутствие defender UUID в кнопке не означает отсутствия поля в сообщении; выбор адресата выполняет соседний helper.

## Проверки и доказательства

Прочитаны 3 логические строки. Группа 24: properties.stun=−2, torso, равенство защиты/атаки 15 — кнопка выведена, действий попадания нет. Для leftArm/tailWing checkForStun ничего не вернул. Группа 27 проверила пустой if и непустую кнопку; группа 30 передала расходящиеся system.stun.modifier=99/attackWeaponProperties.stun=−2: callback вызвал stunSave(−2). [Сверка](../../../../../review-log.md#task-0003042).

## Непроверенные участки и открытые вопросы

Файл прочитан полностью. Реальный DOM, выбор Actor пользователем, сохранение статуса, переводы и браузер не запускались. Правила возникновения оглушения требуют подтверждения до изменения условия.

## Связанные проблемы

[docs/issues/potential/issue-00272.md](../../../../../../../issues/potential/issue-00272.md) — предложение оглушения после успешной защиты; условие находится в производителе, шаблон только выводит полученный объект.

## История актуализации

| Дата | Версия и область | Результат |
| --- | --- | --- |
| 2026-09-12 | 16695cbfc7fec3e0de56660c7cab21bc0304e94b; полный файл | Первичная карточка; [перекрёстная сверка](../../../../../review-log.md#task-0003042) |
