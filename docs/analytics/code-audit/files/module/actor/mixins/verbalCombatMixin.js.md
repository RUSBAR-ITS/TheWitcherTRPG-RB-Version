# module/actor/mixins/verbalCombatMixin.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/actor/mixins/verbalCombatMixin.js](../../../../../../../module/actor/mixins/verbalCombatMixin.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-12 |
| Ветка и коммит | rusbar-main, a69f11d2e4c4318cfbf635dabad97b0062c63c20 |
| Изменения относительно коммита | Нет; совпадает со срезом TASK-0001 15da5b225535e34af4e132c701b5353ef4eb667f |
| Задача и порция | [TASK-0003.046](../../../../../../tasks/task-0003.046.md), 5 файлов / 301 логических строк; данный файл — 101 |
| Запись перекрёстной сверки | [TASK-0003.046](../../../../review-log.md#task-0003046) |

## Назначение файла

Добавляет Actor выбор действия словесного боя, формирование броска и двух флагов для последующего броска урона.

## Условия использования

Экспорт verbalCombatMixin подключён через Object.assign в [module/actor/witcherActor.js](../../../../../../../module/actor/witcherActor.js):446. Общие листы [module/actor/sheets/WitcherActorSheet.js](../../../../../../../module/actor/sheets/WitcherActorSheet.js) и [module/actor/sheets/WitcherActorSheetV1.js](../../../../../../../module/actor/sheets/WitcherActorSheetV1.js) вызывают actor.verbalCombat из _onVerbalCombat по .verbal-button. Настройка useOptionalVerbalCombat управляет показом кнопки через контекст листа, но здесь не проверяется. Другой caller — Counterargue в [module/scripts/verbalCombat/verbalCombatDefense.js](../../../../../../../module/scripts/verbalCombat/verbalCombatDefense.js).

При импорте сохраняется DialogV2. Метод открывает общий выбор всех групп CONFIG.WITCHER.verbalCombat, включая Defenses и Tools. Это не только семь атак. Собственного типа Item, схемы вербального сообщения или хранения состояния словесной дуэли здесь нет.

## Введённые сущности и действия с ними

| Сущность | Вид / место | Доступность | Действие |
| --- | --- | --- | --- |
| DialogV2 | const:6 | local | Ссылка на API prompt |
| verbalCombatMixin | object:8–101 | export | Два метода Actor |
| verbalCombat | async method:9–85 | На Actor после Object.assign | Диалог, действие CONFIG, формула, DTO и extendedRoll |
| ok.callback | closure:21–33 | DialogV2.prompt | Глобальный поиск отмеченного radio и чтение customModifiers из нажатой формы |
| createVerbalCombatFlags | method:87–100 | На Actor; вызывается также защитой | Массив двух инструкций записи flag |
| verbalCombat / vcName / vcStat / vcSkill / vcDmg / effect | Локальные значения:38–56 | В рамках действия | Конфигурация, данные Actor, текст/формула урона и пояснение |

## Основные функции и методы

| Функция | Входы | Результат / вычисление | Ожидания и ошибки |
| --- | --- | --- | --- |
| verbalCombat() | this Actor; CONFIG; UI | Promise undefined; ждёт HBS и prompt, затем строит бросок и вызывает extendedRoll | Не ждёт/не возвращает extendedRoll; отказ окна распространяется; guard выбранного radio/группы/действия отсутствует |
| ok.callback(event,button,dialog) | document и button.form.elements.customModifiers | {group:checkedBox.dataset.group, verbal:checkedBox.value, customModifier:value} | Radio ищется по всему document; текстовый модификатор берётся из текущей формы; пустой выбор → TypeError |
| createVerbalCombatFlags(verbalCombat,vcDamage) | Объект действия CONFIG и строка | [{key:'verbalCombat',value:verbalCombat},{key:'damage',value:{formula:vcDamage}}] | Новый массив и объект damage; запись verbalCombat по ссылке, deep clone отсутствует; сам flags не сохраняет |

### Формулы и все варианты

Если skill задан: 1d10 + this.system.stats[skill.attribute.name].value + this.system.skills[attribute][skill.name].value + this.addActiveEffects(skill.name). Если skill отсутствует — 1d10 без характеристики/навыка и без addActiveEffects. Затем addPart(customModifier,'WITCHER.Settings.Custom','hide'): строка hide truthy, нулевой модификатор скрывается. Отрицательные/положительные числа и составная строка сохраняются для парсера Roll. displayRollDetails прочитан в этом методе, но локальная переменная дальше не используется; форматирование выполняет addPart, повторно читающий настройку.

Данные CONFIG не определяются этим файлом; ниже точное сопоставление producer и consumer, проверенное для всех 16 записей. Характеристика броска навыка и добавка урона могут различаться.

| Группа | Действие | Навык / характеристика броска | vcDmg до подстановки значения |
| --- | --- | --- | --- |
| EmpatheticAttacks | Seduce | seduction / emp | 1d6 + EMP |
| EmpatheticAttacks | Persuade | persuasion / emp | 1d6/2 + EMP |
| EmpatheticAttacks | Appeal | leadership / emp | 1d10 + EMP |
| EmpatheticAttacks | Befriend | charisma / emp | 1d6 + EMP |
| AntagonisticAttacks | Deceive | deceit / emp | 1d6 + INT |
| AntagonisticAttacks | Ridicule | socialetq / int | 1d6 + WILL |
| AntagonisticAttacks | Intimidate | intimidation / will | 1d10 + WILL |
| Defenses | Ignore | resistcoerc / will | 1d10 + EMP |
| Defenses | Counterargue | Нет | Перевод CounterargueDmg, не числовая формула |
| Defenses | ChangeSubject | persuasion / emp | 1d6 + INT |
| Defenses | Disengage | resistcoerc / will | Перевод None |
| EmpatheticTools | Romance | charisma / emp | Перевод None |
| EmpatheticTools | Study | perception / emp | Перевод None |
| AntagonisticTools | ImplyPersuade | persuasion / emp | Перевод None |
| AntagonisticTools | ImplyDeceit | deceit / emp | Перевод None |
| AntagonisticTools | Bribe | gambling / emp | Перевод None |

При baseDmg строится baseDmg+значение[dmgStat.label]; подпись характеристики урона добавляется независимо от displayRollsDetails. Persuade не заключает всю сумму в скобки: делится d6, потом прибавляется EMP. Соответствие книги здесь не оценивалось.

Flavor: div.verbal-combat-attack-message с h2, уроном, локализованным effect и hr. Button.vcDamage добавляется при vcDmg.includes('d'), а не по отдельному числовому признаку. В проверенных en/ru кнопка есть только у девяти записей с baseDmg; None/CounterargueDmg не дают кнопку. Сравнения результата с противником здесь нет: новый RollConfig сохраняет threshold−1, showResult=true, showCrit=true.

## Используемые сущности и зависимости

| Сущность | Источник | Вид / место и цель | Основание |
| --- | --- | --- | --- |
| ChatMessageData | [module/chatMessage/chatMessageData.js](../../../../../../../module/chatMessage/chatMessageData.js) | import:1; new:80 | DTO(actor,flavor,'damage',{vcDamage}); flags первоначально пустые |
| addPart | [module/scripts/helper.js](../../../../../../../module/scripts/helper.js) | import:2;61–62,67 | Операторы, описание и скрытие нуля |
| RollConfig / extendedRoll | [module/scripts/rollConfig.js](../../../../../../../module/scripts/rollConfig.js); [module/scripts/rolls/extendedRoll.js](../../../../../../../module/scripts/rolls/extendedRoll.js) | import:3–4;82–84 | Криты/провалы, rollTotal, toMessage и post-create setFlag |
| addActiveEffects | [module/actor/mixins/modifierMixin.js](../../../../../../../module/actor/mixins/modifierMixin.js); [module/actor/witcherActor.js](../../../../../../../module/actor/witcherActor.js) | Динамический метод Actor:64 | Прямые activeEffectModifiers и skillGroupModifiers |
| verbalCombat / skillMap / statMap | [module/setup/config.js](../../../../../../../module/setup/config.js) | Чтение CONFIG:14,38–56 | 5 групп/16 записей, поля name/skill/baseDmg/dmgStat/effect |
| stats / skills | [module/data/actor/commonActorData.js](../../../../../../../module/data/actor/commonActorData.js); [module/data/actor/templates/common/skills/empData.js](../../../../../../../module/data/actor/templates/common/skills/empData.js); [module/data/actor/templates/common/skills/intData.js](../../../../../../../module/data/actor/templates/common/skills/intData.js); [module/data/actor/templates/common/skills/willData.js](../../../../../../../module/data/actor/templates/common/skills/willData.js) | Подготовленные значения Actor | Источники навыков/характеристик; не raw base/max |
| DamageMessageData | [module/data/chatMessage/damageMessageData.js](../../../../../../../module/data/chatMessage/damageMessageData.js) | Очистка system при type:damage | vcDamage не объявлен и удаляется; дальнейший consumer читает flags, не этот ключ |
| verbal-combat.hbs | [templates/dialog/verbal-combat.hbs](../../../../../../../templates/dialog/verbal-combat.hbs) | renderTemplate:11–16 | Контекст {verbalCombat:CONFIG.WITCHER.verbalCombat} |
| Настройки / строки | [module/setup/settings.js](../../../../../../../module/setup/settings.js); [lang/en.json](../../../../../../../lang/en.json); [lang/ru.json](../../../../../../../lang/ru.json) | displayRollsDetails; WITCHER.verbalCombat.*, Context.unavailable, Settings.Custom, Weapon.Damage, table.Damage | optional rule в листе; label/effect выводятся, не исполняются как эффект |
| DialogV2 / document.querySelector / renderTemplate | Foundry14.367.0, DOM | Модальный prompt с rejectClose:true и глобальный radio | UI/DOM фасады; HBS и core fields/Roll настоящие |

## Известные потребители

| Файл | Сущность | Способ / условие |
| --- | --- | --- |
| [module/actor/witcherActor.js](../../../../../../../module/actor/witcherActor.js) | verbalCombatMixin | import/Object.assign |
| [module/actor/sheets/WitcherActorSheet.js](../../../../../../../module/actor/sheets/WitcherActorSheet.js); [module/actor/sheets/WitcherActorSheetV1.js](../../../../../../../module/actor/sheets/WitcherActorSheetV1.js) | actor.verbalCombat() | _onVerbalCombat; не ожидают результат |
| [module/scripts/verbalCombat/verbalCombatDefense.js](../../../../../../../module/scripts/verbalCombat/verbalCombatDefense.js) | verbalCombat / createVerbalCombatFlags | Counterargue вызывает без аргументов; обычная защита получает два флага |
| [module/scripts/verbalCombat/verbalCombat.js](../../../../../../../module/scripts/verbalCombat/verbalCombat.js) | flags.verbalCombat / flags.damage; button.vcDamage | onDamage читает getFlag и запускает Roll |

Поиск module/templates; макросы и сторонние модули не исследованы. Локальные helpers/methods на Actor доступны извне прототипа.

## Данные и изменения состояния

Создаётся DTO с type damage и system.vcDamage; extendedRoll добавляет rollTotal. Настоящая DamageMessageData удаляет vcDamage, создаёт свои damage defaults. Формула/описание действия отдельно записываются во flags.TheWitcherTRPG.verbalCombat и damage. Это два канала данных: сохранность флагов не следует из system. Метод не расходует Resolve, валюту или ресурсы, не применяет status/ActiveEffect и не реализует накопительные условия текстов effect.

## Проверки и доказательства

| Группы | Результат | Пределы |
| --- | --- | --- |
| 01–03 | Все 16 действий, точные skill/stat/dmgStat; настоящие Roll/addPart/modifierMixin, 0/−2/+2/2+3 и детали; Counterargue без навыка | Actor и prompt фасады, значения EMP7/INT6/WILL5, навыки 2 |
| 04–06 | Пустой radio/неизвестный выбор/отмена; другое окно задаёт действие, текущая форма модификатор; возврат до pending extendedRoll; reference flags | Реальные функции, глобальный DOM-селектор заменён заданным результатом |
| 07–08 | Настоящая DMD удаляет vcDamage; extendedRoll создаёт сообщение до двух setFlag, pending flags ещё недоступны consumer | ChatMessage/toMessage/update фасады; серверная задержка не измерена |
| 24/26 | Все варианты en/ru, кнопка только при baseDmg;14 буквальных ключей, известный ru customModifier gap | Handlebars/core concat, expandObject/getProperty; не полный Localization service |

## Непроверенные участки и открытые вопросы

Все 101 строка прочитаны. Не запускались реальный Actor prepareData, браузерные окна/radio, владение документами, сохранение флагов в БД и полный бой нескольких пользователей. Соответствие игровых текстов правилам и желание их автоматизировать не определялись. Матрица описывает CONFIG текущего форка; например perception здесь Human Perception на EMP, а не произвольно выбранный навык INT.

## Связанные проблемы

[303](../../../../../../issues/potential/issue-00303.md) — глобальный radio; [304](../../../../../../issues/potential/issue-00304.md) — раннее завершение запуска броска/Resolve; [184](../../../../../../issues/potential/issue-00184.md) — отдельная запись flags после сообщения. [302](../../../../../../issues/potential/issue-00302.md) блокирует следующие меню, не создание самой атаки.

## История актуализации

| Дата | Версия и область | Результат |
| --- | --- | --- |
| 2026-09-12 | a69f11d2e4c4318cfbf635dabad97b0062c63c20; полный файл | Первичная карточка; [перекрёстная сверка](../../../../review-log.md#task-0003046) |
