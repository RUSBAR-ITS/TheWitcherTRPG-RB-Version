# module/scripts/rollConfig.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/scripts/rollConfig.js](../../../../../../module/scripts/rollConfig.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `9f16a7ae4bc942df85a105fd37d9a3cb3ef99f4b` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.028](../../../../../tasks/task-0003.028.md), 5 файлов, 372 логических строк |
| Запись перекрёстной сверки | [TASK-0003.028](../../../review-log.md#task-0003028) |

## Назначение файла

Определяет конфигурацию extendedRoll: вывод сообщения, критический бросок, сравнение с порогом и оформление результата. Не меняет характеристики Actor и не содержит формул правил.

## Условия использования

При импорте IIFE создаёт локальный class RollConfig и возвращает его в named export var RollConfig. Экземпляр создаётся вызывающим кодом или параметром по умолчанию extendedRoll. Настройки задаются прямыми присваиваниями полям после new; конструкция не является DataModel Foundry.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| RollConfig | export var + IIFE, 2–19 | Ссылка на одноимённый class | Именованный импорт | При загрузке создаётся класс, при new — отдельная конфигурация. |
| RollConfig.constructor(options) | 4–16 | Начальные девять полей | Метод класса | Читает только options.showResult. |
| defense / reversal / threshold | 7–8, 12 | Режим равенства, направление сравнения, порог | Публичные свойства | false / false / -1; порог ниже нуля отключает сравнение в потребителе. |
| showCrit / showSuccess / showResult | 9–11 | Флаги вычисления и вывода | Публичные свойства | true / true / options.showResult; showSuccess потребителем не читается. |
| thresholdDesc / messageOnSuccess / messageOnFailure | 13–15 | Подпись порога и HTML-тексты исходов | Публичные свойства | По умолчанию пустые строки. |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| constructor(options={showResult:true}) | Без аргументов либо объект options | Экземпляр RollConfig | Фиксированные значения восьми полей; showResult берётся из options | {} даёт showResult=undefined; null вызывает TypeError; переданные options.threshold/showCrit и прочие дополнительные ключи игнорируются. В найденных вызовах используется new без аргументов либо {showResult:false}. |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| extendedRoll — потребитель контракта | [module/scripts/rolls/extendedRoll.js](../../../../../../module/scripts/rolls/extendedRoll.js) | Обратная связь; собственного импорта нет | Порог, crit/fumble, оформление и toMessage | 9–98: читает все перечисленные поля, кроме showSuccess. |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/item/witcherItem.js](../../../../../../module/item/witcherItem.js) | RollConfig | Получает готовые formula/messageData/config, ставит showResult=false; после изготовления сам выводит Roll. RollConfig импортирован только для JSDoc. | realCraft:181–186 |
| [module/item/systems/repair.js](../../../../../../module/item/systems/repair.js) | RollConfig | Готовит порог ремонта, тексты успеха/неудачи и showResult=false; вывод сообщения после ремонта. | commonRepair:190; prepareRollConfig:226–239 |
| [module/actor/mixins/skillMixin.js](../../../../../../module/actor/mixins/skillMixin.js) | RollConfig | Броски навыков: getCustomModifier, ChatMessageData base и RollConfig; пользовательский навык не задаёт threshold. | rollSkillCheck:57–82; rollCustomSkillCheck:146–172 |
| [module/actor/sheets/mixins/statMixin.js](../../../../../../module/actor/sheets/mixins/statMixin.js) | RollConfig | Спасбросок с reversal и модификатором; репутация — reversal либо обычный бросок. Перед вызовом присваивает flavor. | _onStatSaveRoll:13–35; _onReputation:51–81 |
| [module/actor/sheets/mixins/deathSaveMixin.js](../../../../../../module/actor/sheets/mixins/deathSaveMixin.js) | RollConfig | Испытание смерти: reversal=true, showCrit=false, threshold=stunBase; передаёт ChatMessageData base. | _onDeathSaveRoll:26–42 |
| [module/actor/mixins/defenseMixin.js](../../../../../../module/actor/mixins/defenseMixin.js) | RollConfig | Защита откладывает сообщение, дополняет ChatMessageData через append({crit})/append({stun}); stunSave отключает крит и включает reversal. | 194–241, createDefenseRollConfig:293–299, stunSave:437–451 |
| [module/actor/mixins/professionMixin.js](../../../../../../module/actor/mixins/professionMixin.js) | RollConfig | Атака профессии; бросок профессионального навыка с getCustomModifier, порогом и showResult из аргументов. У навыка в speaker передано this.actor. | 222–229, doProfessionSkillRoll:350–378 |
| [module/actor/mixins/verbalCombatMixin.js](../../../../../../module/actor/mixins/verbalCombatMixin.js) | RollConfig | addPart собирает формулу; сообщение damage с vcDamage и два дополнительных флага verbalCombat/damage. Вызов extendedRoll не ожидает. | 61–84, createVerbalCombatFlags:87–101 |
| [module/actor/mixins/castSpellMixin.js](../../../../../../module/actor/mixins/castSpellMixin.js) | RollConfig | Атака заклинанием: ChatMessageData attack, RollConfig({showResult:false}); затем await roll.toMessage(messageData). | 238–248 |
| [module/actor/sheets/WitcherCharacterSheet.js](../../../../../../module/actor/sheets/WitcherCharacterSheet.js) | RollConfig | Изготовление: создаёт ChatMessageData base, задаёт RollConfig и тексты, вызывает Item.realCraft либо extendedRoll для симуляции. | ChatMessageData:265/361; конфигурация и вызов:326–346/414–434 |
| [module/scripts/verbalCombat/verbalCombatDefense.js](../../../../../../module/scripts/verbalCombat/verbalCombatDefense.js) | RollConfig | Словесная защита: ChatMessageData base, defense=true и порог totalAttack; передаёт флаги createVerbalCombatFlags. Выбор Actor отдельно в context callback:13. | 94–123 |
| [module/scripts/rolls/extendedRoll.js](../../../../../../module/scripts/rolls/extendedRoll.js) | RollConfig | Конфигурация аргумента по умолчанию | import:1; extendedRoll:9 |

Область поиска: module/ и templates/ текущего checkout; прямые импорты и места вызова сверены отдельно от динамических обращений. Типы сообщений проверены по system.json и module/setup/registerDataModels.js. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

В памяти хранится конфигурация конкретного броска. extendedRoll её не изменяет; WitcherItem.realCraft ставит showResult=false. defense допускает равенство порогу; reversal меняет направление сравнения и классы оформления критического результата, но не знак прибавления/вычитания дополнительного броска. showSuccess не связан с условием отображения: его определяет threshold>=0.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Все поля и варианты конструктора | Группа 01; весь файл, 19 строк | Проверены значения по умолчанию, {}, {showResult:false,threshold:99}, null | Исполнен настоящий класс, без Foundry/UI. |
| Контракт вычисления | Группы 06–10 | showCrit=false исключает дополнительный бросок; showSuccess=false не скрывает результат при threshold>=0 | Настоящие extendedRoll/Roll; создание сообщения заменено. |
| Потребители | Поиск импортов и присваиваний по module/ | 12 импортирующих файлов; WitcherItem использует импорт для JSDoc, остальные — new | Соседние файлы просмотрены только по соответствующим связям. |

## Непроверенные участки и открытые вопросы

Полностью прочитаны 19 строк. Неиспользуемое showSuccess и неполное заполнение options описаны как фактический контракт; найденные вызывающие места не задают showSuccess=false и не передают конфигурацию целиком через constructor. Отдельного подтверждённого пользовательского сбоя этих полей не заявляется.

## Связанные проблемы

[issue-00033](../../../../../issues/potential/issue-00033.md), [issue-00103](../../../../../issues/potential/issue-00103.md). Проблемы относятся к подготовке формулы до общего броска, не к конструктору. Новые проблемы самого RollConfig отдельно не зарегистрированы.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `9f16a7ae4bc942df85a105fd37d9a3cb3ef99f4b`; полный файл | Первая карточка; [сверка порции](../../../review-log.md#task-0003028) |

## Уточнение TASK-0003.029

2026-09-11, `273a6d7db0b7c866399db3ecd4f7191817ae6f10`. Оба метода навыков создают RollConfig без аргумента, затем showCrit/showSuccess=true. Только встроенный rollSkillCheck присваивает threshold входа; Item-бросок оставляет −1. showResult не меняется, сообщения создаёт extendedRoll. Граница равенства threshold даёт false по уже описанному строгому сравнению.

Сверенные связи: [module/actor/mixins/skillMixin.js](../../../../../../module/actor/mixins/skillMixin.js). Полные карточки новых файлов — в [указателе порции](../../README.md#навыки-броски-развитие-и-пользовательские-навыки--task-0003029). [Проверки, ограничения и версия](../../../review-log.md#task-0003029). Исходники и статус проблем не менялись.

## Уточнение TASK-0003.030

2026-09-11, `aa6af106e86a9c75fe050d599f961c8fadb74f1b`. stat-save ставит reversal=true, thresholdDesc и оставляет криты включёнными; rep-save также reversal с критами, face-down без порога; death-save reversal с showCrit=false. Вычисленный отрицательный threshold ниже слоя конфигурации перестаёт сравниваться, а не автоматически считается неуспехом.

Сверенные источники: [module/actor/sheets/mixins/statMixin.js](../../../../../../module/actor/sheets/mixins/statMixin.js); [module/actor/sheets/mixins/deathSaveMixin.js](../../../../../../module/actor/sheets/mixins/deathSaveMixin.js). [Итоговая сверка третьей серии, сценарии и ограничения](../../../review-log.md#task-0003030). Код и статусы проблем не менялись.

## Уточнение TASK-0003.031

2026-09-11, `928ce4e537c6a3fdc34f8b6fa3fcfdb5a669f68d`. Оба Character callback создают RollConfig с showCrit=true/showSuccess=true и порогом выбранного кода: обычный craftingDC, алхимический alchemyDC. Алхимический fallback к crafting не переключает этот порог. Проверки DC10/total10 и добавочного +2 используют настоящий объект конфигурации.

Связи: [module/actor/sheets/WitcherCharacterSheet.js](../actor/sheets/WitcherCharacterSheet.js.md). [Методика и ограничения сверки](../../../review-log.md#task-0003031).

## Дополнительная сверка TASK-0003.038

2026-09-11, `rusbar-main`, `b47ba02cdaebc6a66ad14a5638213b6eb24460b4`; исходники не менялись.

Profession skill override присваивает threshold/thresholdDesc/showResult; default параметра метода{threshold:0,showResult:true} отличается от constructor.threshold−1. Threshold метода не определён при переданном объекте без threshold. Атака безоружия не создаёт собственный RollConfig, пользуется defaults extendedRoll.

[module/actor/mixins/professionMixin.js](../actor/mixins/professionMixin.js.md), [templates/partials/character/tab-profession.hbs](../../templates/partials/character/tab-profession.hbs.md), [templates/sheets/actor/partials/monster/tabs/tab-profession.hbs](../../templates/sheets/actor/partials/monster/tabs/tab-profession.hbs.md), [templates/dialog/combat/profession-attack.hbs](../../templates/dialog/combat/profession-attack.hbs.md).

[Сверка и ограничения](../../../review-log.md#task-0003038). Связанные файлы повторно в покрытии не учитывались; код и статусы issues не изменены.
