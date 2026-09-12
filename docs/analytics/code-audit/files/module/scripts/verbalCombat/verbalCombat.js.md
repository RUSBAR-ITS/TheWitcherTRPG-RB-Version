# module/scripts/verbalCombat/verbalCombat.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/scripts/verbalCombat/verbalCombat.js](../../../../../../../module/scripts/verbalCombat/verbalCombat.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-12 |
| Ветка и коммит | rusbar-main, a69f11d2e4c4318cfbf635dabad97b0062c63c20 |
| Изменения относительно коммита | Нет; совпадает со срезом TASK-0001 15da5b225535e34af4e132c701b5353ef4eb667f |
| Задача и порция | [TASK-0003.046](../../../../../../tasks/task-0003.046.md), 5 файлов / 301 логических строк; данный файл — 55 |
| Запись перекрёстной сверки | [TASK-0003.046](../../../../review-log.md#task-0003046) |

## Назначение файла

Связывает кнопку урона словесного боя с Roll из флагов и добавляет команду изменения Resolve выбранного Actor.

## Условия использования

[module/TheWitcherTRPG.js](../../../../../../../module/TheWitcherTRPG.js) вызывает chatMessageListeners на renderChatMessageHTML:55 и регистрирует addVerbalCombatMessageContextOptions на getChatMessageContextOptions:137. Штатный html — HTMLElement. Массовый addVerbalCombatChatListeners не имеет найденных вызовов; его несовместимость не препятствует отдельной штатной регистрации. Сам файл не создаёт подписки при импорте.

## Введённые сущности и действия с ними

| Сущность | Вид / место | Доступность | Действие |
| --- | --- | --- | --- |
| addVerbalCombatChatListeners | function:3–13 | export | Прежний массовый обход .chat-message |
| addVerbalCombatMessageContextOptions | function:15–30 | export | Одна команда нанесения словесного урона |
| canApplyVcDamage / callback | closures:16,21–27 | menu entry | Поиск marker, Actor и .dice-total |
| chatMessageListeners | async arrow:32–36 | export | Назначение click первой button.vcDamage |
| onDamage | function:38–42 | local | Чтение двух флагов и запуск rollDamage |
| rollDamage | async function:44–50 | export | Roll/evaluate/toMessage и дополнительный damage flag |
| applyVerbalCombatDamage | async function:52–55 | export | update resolve.value |

## Основные функции и методы

| Функция | Входы | Результат / действия | Ошибки и ожидания |
| --- | --- | --- | --- |
| addVerbalCombatChatListeners(html) | Внешний контейнер | Пытается querySelector('.chat-message').each; затем $(element), data ID, get message | querySelector возвращает Element/null, у них нет each; внешних вызовов не найдено |
| addVerbalCombatMessageContextOptions(html,options) | Массив меню | Возвращает тот же массив + visible/callback | visible возвращает querySelector(marker)?.length: у найденного div undefined, пункт скрыт; callback читает querySelector('.dice-total')[0].innerText, что также не DOM-контракт |
| chatMessageListeners(message,html) | HTMLElement | Если нет кнопки и есть a.apply-status — ранний выход; иначе optional bind первой кнопки | Promise после регистрации; повторный bind добавляет listener; message захвачен closure, event.target не читается |
| onDamage(message) | getFlag API | Читает TheWitcherTRPG.verbalCombat/damage → rollDamage | Не проверяет flags и не ждёт/не возвращает Promise |
| rollDamage(verbalCombat,damage) | name и damage.formula | Ждёт Roll.evaluate и Roll.toMessage; после сообщения вызывает setFlag damage | Promise undefined до сохранения flag; нет guard/formula validation; flavor malformed перед h1 |
| applyVerbalCombatDamage(targetActor,totalDamage,messageId) | Actor.system.derivedStats.resolve.value | currentResolve−Math.floor(totalDamage), Actor.update с абсолютным значением | messageId не используется; update не ожидается; Actor/число/границы не проверяются |

## Используемые сущности и зависимости

| Сущность | Источник | Связь / цель | Основание |
| --- | --- | --- | --- |
| getInteractActor | [module/scripts/helper.js](../../../../../../../module/scripts/helper.js) | import:1; callback:23 | Выбор получателя Resolve-урона, может вернуть undefined |
| flags.verbalCombat / flags.damage | [module/actor/mixins/verbalCombatMixin.js](../../../../../../../module/actor/mixins/verbalCombatMixin.js); [module/scripts/verbalCombat/verbalCombatDefense.js](../../../../../../../module/scripts/verbalCombat/verbalCombatDefense.js); [module/scripts/rolls/extendedRoll.js](../../../../../../../module/scripts/rolls/extendedRoll.js) | Producers/config → post-message flags → onDamage | Имена флагов совпадают; запись после toMessage создаёт временную недоступность |
| resolve.value | [module/data/actor/templates/common/stats/derivedStatsData.js](../../../../../../../module/data/actor/templates/common/stats/derivedStatsData.js); [module/data/actor/templates/common/stats/statData.js](../../../../../../../module/data/actor/templates/common/stats/statData.js) | Чтение/запрос update | NumberField без min; здесь max не читается |
| calculateDerivedStat | [module/actor/witcherActor.js](../../../../../../../module/actor/witcherActor.js) | Соседний расчёт максимума Resolve | value не синхронизируется автоматически этим расчётом; метод урона не вызывает его |
| Roll/evaluate/toMessage/setFlag | Foundry14.367.0 | Бросок и чат | Используется обычный Roll, не extendedRoll; нет критического/сравнительного расчёта урона |
| ContextMenu/HTMLElement | /opt/foundryvtt/client/applications/ux/context-menu.mjs; applications/api/application.mjs | callback(target,event), jQuery:false в ChatLog | Старое имя callback поддерживается; проблема — .length и [0] |
| localize / WITCHER.Context.applyDmg / WITCHER.table.Damage | [lang/en.json](../../../../../../../lang/en.json), [lang/ru.json](../../../../../../../lang/ru.json) | Имя меню/урона и verbalCombat.name | Подписи; логики Resolve не содержат |
| game.messages / $ | Foundry/jQuery | Только массовый helper | Поиск по ID и старый элемент; текущий listener получает message напрямую |

## Известные потребители

| Файл | Сущность | Условие |
| --- | --- | --- |
| [module/TheWitcherTRPG.js](../../../../../../../module/TheWitcherTRPG.js) | chatMessageListeners, addVerbalCombatMessageContextOptions | Render/menu Hooks |
| [module/actor/mixins/verbalCombatMixin.js](../../../../../../../module/actor/mixins/verbalCombatMixin.js) | button.vcDamage / flags | Атака и общие действия с baseDmg |
| [module/scripts/verbalCombat/verbalCombatDefense.js](../../../../../../../module/scripts/verbalCombat/verbalCombatDefense.js) | button.vcDamage / flags | Ignore/ChangeSubject после защиты, независимо от success |

onDamage/rollDamage/applyVerbalCombatDamage вызываются внутри этого модуля; внешних прямых production-вызовов экспортированных rollDamage/applyVerbalCombatDamage в module не найдено. Сторонние макросы не проверялись.

## Данные и изменения состояния

rollDamage не задаёт speaker/type/system: создаёт объект только flavor и отдаёт штатному Roll.toMessage. Defaults speaker/type зависят от ядра и текущего пользователя; Actor автора атаки не передаётся. В flavor строка `<div class="verbalcombat-damage-message" <h1>` теряет закрывающий > до h1: parse5 сохраняет marker, но h1 становится атрибутом div.

Урон Resolve применяется к выбранному Actor независимо от flags/исходного сообщения, успеха защиты и конкретного действия; messageId лишний. Дробное 3.8 округляется вниз до 3, строковое число приводится Math.floor; отрицательное−2 повышает Resolve на 2,15 из 10 даёт−5, '?' → NaN в запросе. Это фактическая граница входа, а не согласованное правило нормализации. Никаких эффектов из verbalCombat.effect здесь не исполняется.

## Проверки и доказательства

| Группы | Результат | Пределы |
| --- | --- | --- |
| 09–12 | Первая кнопка, вложенный target и повторы; legacy each падает; оба menu selectors несовместимы с DOM; ядро передаёт именно target | Настоящий dispatch ContextMenu с заменёнными render/close; полного UI нет |
| 13–14 | Настоящие Roll2+3→5,1d6/2+7→7.5 при minimize,−2→−2; отсутствующие flags/невалидная формула отклоняются; flag pending после возврата; malformed HTML | toMessage/setFlag фасады, HTML parse5 |
| 15–16 | Resolve10 при уроне 3.8→7, отрицательные/NaN/перерасход; нет Actor → ошибка; две pending-записи 7/6 из 10, итог 6 | Прямой вызов consumer обходит скрытое меню 302; update в памяти, не БД |

## Непроверенные участки и открытые вопросы

Все 55 строк разобраны. Доступность меню в полном клиенте не исправлена; прямые проверки нижних функций не означают рабочий пользовательский сценарий. Реальное сохранение Resolve/флагов, права, сетевой порядок и повторная подготовка Actor не исполнялись. Встроенный math не устанавливает минимальный/максимальный Resolve; решение по допустимым значениям требует отдельного согласования.

## Связанные проблемы

[302](../../../../../../issues/potential/issue-00302.md) — меню DOM/jQuery; [304](../../../../../../issues/potential/issue-00304.md) — возврат до Resolve-update; [184](../../../../../../issues/potential/issue-00184.md) — flag после сообщения; [293](../../../../../../issues/potential/issue-00293.md) — malformed flavor, расширенная существующая issue. [149](../../../../../../issues/potential/issue-00149.md) — отсутствие выбранного Actor; ранний барьер 302 отдельно.

## История актуализации

| Дата | Версия и область | Результат |
| --- | --- | --- |
| 2026-09-12 | a69f11d2e4c4318cfbf635dabad97b0062c63c20; полный файл | Первичная карточка; [перекрёстная сверка](../../../../review-log.md#task-0003046) |
