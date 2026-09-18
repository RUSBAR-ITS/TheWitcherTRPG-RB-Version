# TASK-0010.008 — Подключение потребителей: локальная проверка

**Уточнение .00067:** отдельная issue-00111 исправлена после согласования: action и второй аргумент обработчика согласованы с ядром. [10 локальных проверок](issue-00111-checks.md) прошли. Указанная ниже блокировка относится к срезу .00066; полноценная браузерная приёмка Б16 по-прежнему впереди.

Дата:2026-09-18. Ветка dev, HEAD0537500936de736ce898b0173670c82714b72f23; рабочая версия14.3.1.00066. Foundry14.367.0/Node24.16.0 использованы как локальные библиотеки. Мир/браузер/служба не запускались. Стадия .008 выполнена в согласованной области; .009–.013 впереди.

## Поведение

Игровые проверки вызывают prepareCheck после определения фактического навыка. Он ждёт отдельный числовой ручной ввод при необходимости, затем окно условных строк. Новый вызов начинает с выключенных галочек; отсутствие кандидатов не создаёт окно; null означает отмену. При обычной проверке вклады входят в формулу один раз, при обратной — поправка к порогу, куб остаётся1d10. dontAddAttr сохраняется. Урон/таблицы не превращаются в проверки навыка.

Item-навык выбирается по Item ID; профессия — по Item ID и разрешённому slot. Пустые/одинаковые/переименованные навыки независимы, совпадение с builtin именем не перенаправляет бросок. Шесть методов редактора используют этот же адрес; definingSkill получил общий блок настройки. Собственные поправки и ручные строки модели сохраняются отдельно, allSkills не дублируется. Сильный/совместный удар используют числовое .value.

В оружейной серии каждый удар получает отдельный свежий выбор; все выборы завершаются до расходов серии. Отмена на любом из них не расходует STA/боеприпас/метательное оружие. Магия и защита также выбирают модификаторы до соответствующего расхода. Остальные правила расходов/попадания/доставки не переработаны.

Stat Save, Death Save и Stun используют строгое< и общий финальный порог. Отрицательное число остаётся реальным порогом, null — отсутствие сравнения. При Death Save база и счётчик прежние; дополнительные строки относятся к STUN, произвольный roll-only BODY/skill не наследуется. Словесная дуэль не получает физический attack/defense бонус автоматически.

## Изменённые файлы

| Файл | Назначение изменения |
| --- | --- |
| [module/scripts/rolls/prepareCheck.js](../../module/scripts/rolls/prepareCheck.js) | Общий вход подготовки проверки. |
| [module/scripts/helper.js](../../module/scripts/helper.js) | Числовой ручной ввод. |
| [module/actor/rollContext.js](../../module/actor/rollContext.js) | Разрешение фактической цели броска. |
| [module/actor/mixins/skillMixin.js](../../module/actor/mixins/skillMixin.js) | Встроенные и Item-навыки. |
| [module/actor/sheets/mixins/customSkillMixin.js](../../module/actor/sheets/mixins/customSkillMixin.js) | Клик и ручные строки Item-навыка. |
| [module/data/item/skillItemData.js](../../module/data/item/skillItemData.js) | Модель собственного навыка. |
| [module/data/item/templates/professionSkillData.js](../../module/data/item/templates/professionSkillData.js) | Собственная числовая поправка слота. |
| [module/data/item/professionData.js](../../module/data/item/professionData.js) | Адрес выбранной профессиональной защиты. |
| [module/actor/mixins/professionMixin.js](../../module/actor/mixins/professionMixin.js) | Адресные проверки/атаки профессии. |
| [module/item/sheets/configurations/WitcherProfessionConfigurationSheet.js](../../module/item/sheets/configurations/WitcherProfessionConfigurationSheet.js) | Редактор конкретного слота профессии. |
| [module/actor/mixins/weaponAttackMixin.js](../../module/actor/mixins/weaponAttackMixin.js) | Контекст каждого оружейного удара. |
| [module/activeEffect/mixins/baseMixin.js](../../module/activeEffect/mixins/baseMixin.js) | Числовые цели сильного/совместного удара. |
| [module/actor/mixins/defenseMixin.js](../../module/actor/mixins/defenseMixin.js) | Общая проверка защиты и оглушения. |
| [module/actor/mixins/castSpellMixin.js](../../module/actor/mixins/castSpellMixin.js) | Магическая проверка. |
| [module/actor/mixins/verbalCombatMixin.js](../../module/actor/mixins/verbalCombatMixin.js) | Атака словесной дуэли. |
| [module/scripts/verbalCombat/verbalCombatDefense.js](../../module/scripts/verbalCombat/verbalCombatDefense.js) | Защита словесной дуэли. |
| [module/actor/sheets/mixins/statMixin.js](../../module/actor/sheets/mixins/statMixin.js) | Испытания характеристики и противостояние. |
| [module/actor/sheets/mixins/deathSaveMixin.js](../../module/actor/sheets/mixins/deathSaveMixin.js) | Испытание смерти. |
| [module/actor/sheets/WitcherCharacterSheet.js](../../module/actor/sheets/WitcherCharacterSheet.js) | Алхимия и изготовление. |
| [module/item/systems/repair.js](../../module/item/systems/repair.js) | Подготовка проверки ремонта. |
| [module/scripts/investigation/rollClue.js](../../module/scripts/investigation/rollClue.js) | Выбранный навык расследования. |
| [templates/partials/character/custom-skill-display.hbs](../../templates/partials/character/custom-skill-display.hbs) | Отображение и ID Item-навыка. |
| [templates/partials/character/tab-skills.hbs](../../templates/partials/character/tab-skills.hbs) | Передача Item в partial. |
| [templates/partials/character/tab-profession.hbs](../../templates/partials/character/tab-profession.hbs) | Адреса профессиональных кликов. |
| [templates/sheets/actor/partials/monster/tabs/tab-profession.hbs](../../templates/sheets/actor/partials/monster/tabs/tab-profession.hbs) | Альтернативный клик профессии монстра. |
| [templates/sheets/item/configuration/partials/profession/skillPathPart.hbs](../../templates/sheets/item/configuration/partials/profession/skillPathPart.hbs) | Адрес трёх слотов пути. |
| [templates/sheets/item/configuration/partials/profession/skillPathSkillPart.hbs](../../templates/sheets/item/configuration/partials/profession/skillPathSkillPart.hbs) | Путь в CRUD строках профессии. |
| [templates/sheets/item/configuration/tabs/general.hbs](../../templates/sheets/item/configuration/tabs/general.hbs) | Настройки definingSkill. |
| [system.json](../../system.json) | Версия системы. |

## Сверка остальных входов карты воздействия

| Вход/файлы | Результат .008 |
| --- | --- |
| module/actor/sheets/mixins/skillMixin.js; WitcherActorSheet.js, WitcherActorSheetV1.js; WitcherMonsterSheet.js | Проверены, изменение не требуется: передают существующий builtin key/Item коллекцию, текущий monster использует общий tab-skills. Новый custom listener принимает и legacy ID |
| Старый templates/partials/monster/monster-custom-skill-display.hbs и monster-skill-tab.hbs | Проверен, изменение не требуется: #custom-rollable внутри .item с ID поддержан. Это не новая регистрация старого листа |
| templates/dialog/combat/{weapon-attack,profession-attack,spell-attack}.hbs; templates/dialog/{verbal-combat,verbal-combat-defense,repair-dialog}.hbs | Проверены, изменение не требуется: выбор навыка/обстоятельства и ручное число остаются там; условное окно общее и открывается после выбора |
| RollConfig, extendedRoll, conditionalModifiers, rollModifiers, parameterPreparation, modifierMixin | Проверены, изменение не требуется в .008: инфраструктура .007 уже отделяет null/обратный порог/полный вклад. Поиск module не находит игровых вызовов старых addActiveEffects/addAttackModifiers/addDefenseModifiers/getCustomModifier; определения сохранены |
| Порог в profession Threshold.value, craftingDC/alchemyDC и chat totalAttack | Проверены: числовые модели сохраняются; строковый chat totalAttack преобразуется Number на входе защиты; профессиональный default=null |
| Actor/AE lifecycle, сохранение и прокачка .004–.006, редактор параметров, ru/en | Проверены на отсутствие необходимости изменений этой порции. Метаданные новых строк уже поддержаны. Нет новых локализационных строк |
| Доставка/несуммирование/таймеры AE и damage schema | Согласованная следующая .009, здесь не изменялись и не объявлены проверенными |
| criticalWounds JSON/установленные базы компедиумов | .010/.011 впереди; в .008 не менялись и не пересобирались |

## Проверки

Артефакты: `/var/lib/foundryvtt/Data/work-cat/witcher-task0010-008-20260918`; before.json хранит хеши и метаданные доступа до порции, source-before.json — исходный текст. Сравнение с этим рабочим снимком, не со старым HEAD.

**52 отдельных runtime-проверки прошли:**24 интеграционных проверок потребителей (I01–I23, I19 в двух вариантах) и28 регрессионных .007. Основная команда: `node --experimental-vm-modules --test consumers.test.mjs`; регрессия — `node --experimental-vm-modules --test roll.test.mjs`. integration-tests.tap содержит19/22 успешных; затем только зависимые фикстуры/проверки повторены в consumer-recheck.tap, repair-recheck.tap, final-consumer-recheck.tap и manual-recheck.tap. roll-regression.tap —28/28. Неодинаковые прототипы массивов VM, неполная подмена ChatMessageData.append, frozen экземпляр Repair, недостающий HBS partial и неверная фикстура torso исправлены в стенде; место torso реально даёт−1. Неудачи стенда не скрыты и не названы дефектами игры.

Проверено: own/manual/allSkills ровно один раз; Item совпадает именем с builtin; профессия defining/duplicate/blank и шесть CRUD; stat5+level3+own2+attack1=11 до куба/локации в обоих атаках; dontAddAttr; собственный cap и отрицательный Item-навык; ручные строки с ID и числовой сериализацией; fresh выбор серии; отмена до расходов; reverse bonus/manual и autfail; магия; verbal обе стороны; crafting/alchemy; repair formula/cancel; investigation. Реальные модели/JS/установленные lifecycle/ActiveEffect/Roll, контролируемые кубы; UI, сообщения, коллекции и запись — in-memory подмены. Это не сохранение в БД и не браузерная приёмка.

Статические результаты: static-results.json (JS/HBS, ссылки, scope, inode/mode/uid/gid); graph-update.json/index-tests.txt/index-check.json — адресная актуализация графа и один freshness. Полный исторический набор не запускается.

## Границы и оставшиеся задачи

- issue-00111 сохраняется: HBS action удаления эффекта профессии не совпадает с зарегистрированным action, обработчик также использует event.currentTarget. Адреса шести методов локально проверены, **удаление этой кнопкой в UI не объявлено исправленным**. Это отдельный существующий дефект вне согласованного состава .008; до сквозного Б16 потребуется согласовать его исправление.
- TASK-0011: исполнение ремонта00102, компоненты алхимии00037, DOM словесного боя00302/00303 и компенсация EV остаются отдельно. Проверка callback/formula не подтверждает полный UI-путь.
- Подготовка duration/доставка эффектов, повторы и компедиум — следующие стадии. Успех прямой профессиональной атаки не означает исправление её последующей кнопки урона без Item UUID.
- Issues не закрыты; С19/С30/С33/С35–С38 подтверждены в обозначенной изолированной области. Б06–Б08/Б16–Б18 — после команды пользователя на игровую приёмку .013.

## Итог адресной сверки

Граф: 638 источников, 5802 сущностей, 15752 связей, 485 процессов, покрытие partial. Сохранены подробные неизменённые ветви процессов, заменены старые name lookup и сборка формул; явно поставлены узлы выбора до расходов оружия/магии/защиты. Проверки навигации:17 адресных сценариев (.008/.007/численное ядро); первая попытка16/17, затем отдельно исправлена отсутствовавшая явная ссылка issue-00111 в описании уже существующей границы и повторена зависимая проверка.

21 JS прошёл node --check;7 HBS компилируются; ru/en без новых/удалённых ключей; манифест отличается от снимка порции только version. Изменения вне docs ограничены29 согласованными исходниками. Снимок inode/mode/uid/gid существующих файлов совпадает.
