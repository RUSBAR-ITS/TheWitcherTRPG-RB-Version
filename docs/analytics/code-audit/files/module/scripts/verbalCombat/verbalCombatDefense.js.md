# module/scripts/verbalCombat/verbalCombatDefense.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/scripts/verbalCombat/verbalCombatDefense.js](../../../../../../../module/scripts/verbalCombat/verbalCombatDefense.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-12 |
| Ветка и коммит | rusbar-main, a69f11d2e4c4318cfbf635dabad97b0062c63c20 |
| Изменения относительно коммита | Нет; совпадает со срезом TASK-0001 15da5b225535e34af4e132c701b5353ef4eb667f |
| Задача и порция | [TASK-0003.046](../../../../../../tasks/task-0003.046.md), 5 файлов / 301 логических строк; данный файл — 118 |
| Запись перекрёстной сверки | [TASK-0003.046](../../../../review-log.md#task-0003046) |

## Назначение файла

Добавляет команду словесной защиты, открывает выбор способа и формирует сравнительный бросок либо новую атаку Counterargue.

## Условия использования

[module/TheWitcherTRPG.js](../../../../../../../module/TheWitcherTRPG.js):138 регистрирует addVerbalCombatDefenseMessageContextOptions на getChatMessageContextOptions. В установленном Foundry14.367.0 ChatLog передаёт HTMLElement, а menu entry использует смешанный DOM/jQuery-код. Для полного описания нижние методы проверялись отдельно от этого барьера.

Окно создаётся через глобальный Dialog V1, который в 14 ещё существует: /opt/foundryvtt/client/client.mjs:170 экспортирует appv1.api.Dialog, deprecated до 16. Его options.jQuery по умолчанию true; callback получает jQuery. Поэтому html.find внутри callback окна допустим и отличается от li.find в callback меню.

## Введённые сущности и действия с ними

| Сущность | Вид / место | Доступность | Действие |
| --- | --- | --- | --- |
| addVerbalCombatDefenseMessageContextOptions | function:6–17 | export | Расширяет меню защиты |
| canDefend / callback | closures:7,12–14 | menu entry | Marker/Actor/число атаки из HTML |
| executeDefense | async function:19–42 | local | HBS, создание Dialog, bind callback |
| executeDefenseCallback | async function:44–109 | local | Выбор защиты, формула/flags, сравнительный extendedRoll |
| createRollConfig | function:111–118 | local | defense=true, threshold и thresholdDesc |
| t1 / t2 | Dialog buttons:32–40 | Roll / Cancel | t1 вызывает bound callback; t2 собственного callback не имеет |

## Основные функции и методы

| Функция | Входы | Действия / результат | Ошибки, завершение |
| --- | --- | --- | --- |
| addVerbalCombatDefenseMessageContextOptions(html,options) | options | Тот же массив + entry | visible=querySelector(marker)?.length, у DOM undefined; callback li.find(...)[0] несовместим с HTMLElement; executeDefense не ожидается |
| executeDefense(actor,messageId,totalAttack) | Actor, ID, итог атаки | !actor→return; ждёт renderTemplate({defenses}); new Dialog(...).render(true) | messageId не читает; не ждёт выбора/сравнения; закрытие Cancel не запускает действие |
| executeDefenseCallback(actor,totalAttack,html) | Actor, scalar threshold, jQuery диалога | Глобально ищет radio; нет→return; Counterargue→actor.verbalCombat() и return; иначе CONFIG.Defenses[value] и формула | Counterargue не ждёт; неверное имя/данные вызывают исключение; обычный путь ждёт extendedRoll, который не ждёт flags |
| createRollConfig(skill,totalAttack) | На фактическом вызове vcSkill — число, totalAttack — строка/число | new RollConfig; showResult=true, defense=true, threshold=totalAttack, thresholdDesc=skill.label | Число не имеет label: undefined; математический порог сохраняется |

### Четыре защиты и формула

Ignore: WILL+resistcoerc, урон 1d10+EMP. ChangeSubject: EMP+persuasion, урон 1d6+INT. Disengage: WILL+resistcoerc, урона нет. Counterargue открывает общий actor.verbalCombat без аргументов; исходный totalAttack и customModifiers в новую атаку не передаются. Этот callback не сравнивает результат контраргумента с прежней атакой. Ручной выбор/сопоставление остаётся за пределами автоматического кода.

Обычная формула:1d10 + значение характеристики + значение навыка + actor.addActiveEffects(skill.name). При displayRollsDetails добавляются подписи. customAtt из html.find('[name=customModifiers]')[0].value добавляется только при customAtt<0 или >0. Нулевой ввод скрывается; строка 2+3 даёт NaN при сравнении и игнорируется, в отличие от addPart общего action. Это граница числового ввода, не заявленная поддержка выражений защитным полем.

vcDmg при baseDmg всегда добавляет [localized dmgStat.label]; иначе None. Flavor использует тот же .verbal-combat-attack-message, что атака, и кнопку .vcDamage при наличии d в строке. Результат/кнопка урона формируются до определения success; кнопка не скрывается при провале. Тексты effect только выводятся.

extendedRoll с defense=true принимает равенство threshold за успех; showCrit=true включает доп. d10x10 при первом 1/10. createRollConfig передаёт число навыка вместо описания: thresholdDesc undefined, результат показывает числовой threshold через fallback extendedRoll. Ни Resolve, ни фактический урон этим файлом не изменяются.

## Используемые сущности и зависимости

| Сущность | Источник | Вид / место | Основание |
| --- | --- | --- | --- |
| extendedRoll | [module/scripts/rolls/extendedRoll.js](../../../../../../../module/scripts/rolls/extendedRoll.js) | import:1; await:108 | Применяет порог/криты, toMessage и два флага |
| getInteractActor | [module/scripts/helper.js](../../../../../../../module/scripts/helper.js) | import:2; menu callback | Выбор защищающегося, не speaker сообщения |
| RollConfig | [module/scripts/rollConfig.js](../../../../../../../module/scripts/rollConfig.js) | import:3; new:112 | Параметры сравнения |
| ChatMessageData | [module/chatMessage/chatMessageData.js](../../../../../../../module/chatMessage/chatMessageData.js) | import:4; new:94 | DTO default type base, system пуст; flavor затем назначается |
| verbalCombat / createVerbalCombatFlags | [module/actor/mixins/verbalCombatMixin.js](../../../../../../../module/actor/mixins/verbalCombatMixin.js); [module/actor/witcherActor.js](../../../../../../../module/actor/witcherActor.js) | Actor methods:52/108 | Новое действие Counterargue / flags для последующего урона |
| addActiveEffects | [module/actor/mixins/modifierMixin.js](../../../../../../../module/actor/mixins/modifierMixin.js) | Actor call:79 | Модификаторы навыка/групп |
| Defenses / skillMap / statMap | [module/setup/config.js](../../../../../../../module/setup/config.js) | Чтение:25,56–71 | Четыре конфигурации, характеристики и ключи |
| stats/skills | [module/data/actor/commonActorData.js](../../../../../../../module/data/actor/commonActorData.js); [module/data/actor/templates/common/skills/empData.js](../../../../../../../module/data/actor/templates/common/skills/empData.js); [module/data/actor/templates/common/skills/willData.js](../../../../../../../module/data/actor/templates/common/skills/willData.js) | Подготовленные данные Actor | Значения навыков, не их label |
| base model | [module/data/chatMessage/baseMessageData.js](../../../../../../../module/data/chatMessage/baseMessageData.js) | Сохранение system.rollTotal | Важные сведения словесного боя во flags |
| verbal-combat-defense.hbs | [templates/dialog/verbal-combat-defense.hbs](../../../../../../../templates/dialog/verbal-combat-defense.hbs) | renderTemplate:22–27 | Контекст только {defenses} |
| displayRollsDetails / i18n keys | [module/setup/settings.js](../../../../../../../module/setup/settings.js); [lang/en.json](../../../../../../../lang/en.json); [lang/ru.json](../../../../../../../lang/ru.json) | Формула и подписи | WITCHER.Context.Defense, Dialog.DefenseTitle/ButtonRoll, Button.Cancel, verbalCombat.*, Settings.Custom |
| Dialog / ContextMenu / document.querySelector | Foundry14.367.0 и DOM | Разные UI-контракты | Global Dialog alias есть; legacy submit передаёт jQuery; ChatLog menu — HTMLElement |

## Известные потребители

[module/TheWitcherTRPG.js](../../../../../../../module/TheWitcherTRPG.js) — единственный внешний импорт/вызов menu extender; далее Foundry вызывает menu callback, Dialog вызывает executeDefenseCallback. Внутренний createRollConfig имеет единственный вызов:106. [module/scripts/verbalCombat/verbalCombat.js](../../../../../../../module/scripts/verbalCombat/verbalCombat.js) читает два созданных флага и кнопку будущего сообщения. Макросы/модули вне module/templates не исследовались.

## Данные и изменения состояния

Создаёт окно/сообщение, дополнительных расходов нет. Данные атаки из сообщения по ID не проверяются: menu извлекает только DOM total и передаёт scalar. В обычном пути DTO имеет type base; в общем actor.verbalCombat — damage. Обоим extendedRoll дописывает system.rollTotal и flags после создания. Результат Counterargue не связан автоматически с исходным messageId.

## Проверки и доказательства

| Группы | Результат | Пределы |
| --- | --- | --- |
| 11–12 | Нормальный DOM marker даёт undefined visible, li.find ломает принудительный callback; ядро передаёт HTMLElement | Пункты скрыты до исполнения нижней ветви; полного menu render нет |
| 17–20 | Нет Actor/выбора → выход, Cancel без callback; все 4 защиты; числа модификатора±2/0 и пропуск 2+3; чужой radio Seduce даёт неизвестную Defenses запись | Dialog/DOM фасады, методы исходные |
| 21–23 | numeric skill теряет label; реальный extendedRoll:8≥8 успех,8<9 провал; fumble7<8, crit18=18 успех; callback ждёт extendedRoll, executeDefense только открывает окно | Real Roll с deterministic minimize/maximize; ChatMessage/запись фасады |
| 25–26 | Настоящий core Dialog.submit передаёт jQuery и закрывает окно без ожидания async callback;14 ключей en, один известный ru gap | Метод извлечён из ядра, root document/window не создавались |

## Непроверенные участки и открытые вопросы

Все 118 строк прочитаны. Скрытое меню 302 не исправлено; проверки методов напрямую не доказывают рабочий сценарий UI. Не проверены полный Dialog/браузерные radio, сохранение messages/flags, права, несколько клиентов и правила контраргумента по книге. Поддерживаемый legacy Dialog не объявлен сломанным по имени API.

## Связанные проблемы

[302](../../../../../../issues/potential/issue-00302.md) — menu DOM; [303](../../../../../../issues/potential/issue-00303.md) — чужое radio; [305](../../../../../../issues/potential/issue-00305.md) — числовой skill вместо label; [184](../../../../../../issues/potential/issue-00184.md) — flags. [149](../../../../../../issues/potential/issue-00149.md) — отсутствие Actor до guarded executeDefense; [304](../../../../../../issues/potential/issue-00304.md) — ожидание Actor.verbalCombat в Counterargue не гарантируется.

## История актуализации

| Дата | Версия и область | Результат |
| --- | --- | --- |
| 2026-09-12 | a69f11d2e4c4318cfbf635dabad97b0062c63c20; полный файл | Первичная карточка; [перекрёстная сверка](../../../../review-log.md#task-0003046) |
