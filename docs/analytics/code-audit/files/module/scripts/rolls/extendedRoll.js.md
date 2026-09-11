# module/scripts/rolls/extendedRoll.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/scripts/rolls/extendedRoll.js](../../../../../../../module/scripts/rolls/extendedRoll.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `9f16a7ae4bc942df85a105fd37d9a3cb3ef99f4b` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.028](../../../../../../tasks/task-0003.028.md), 5 файлов, 372 логических строк |
| Запись перекрёстной сверки | [TASK-0003.028](../../../../review-log.md#task-0003028) |

## Назначение файла

Общий вычислитель броска: выполняет переданную формулу, распознаёт критический результат/провал, рассчитывает дополнительный бросок, сравнивает итог с порогом и подготавливает либо отправляет сообщение.

## Условия использования

Named export async extendedRoll. Формулу, параметры сообщения и конфигурацию готовят потребители; сам файл не выбирает Actor, навык или правило травмы. Roll берётся из глобального Foundry API, RollConfig импортирован явно. Для вычисления нужны game.i18n и messageData.system; сообщение и дополнительные флаги обрабатываются только при config.showResult.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| extendedRoll | async export, 9–99 | Полный маршрут вычисления и сообщения | 12 импортирующих файлов | Возвращает Promise<Roll>. |
| isCrit / isFumble | Локальные функции, 101–107 | Распознавание первого результата | Не экспортируются | Сравнивают roll.dice[0]?.results[0].result с 10/1. |
| roll / evaluatedRoll / rollTotal | 10–12, 59 | Первый Roll и итоговый результат | Локальные ссылки | При crit/fumble evaluatedRoll заменяется новым числовым Roll. |
| extraRollFormula / extraRollTotal / options | 29–59 | Дополнительный бросок и признаки результата | Локально; options попадают в возвращаемый Roll | crit либо fumble/fumbleAmount; затем success/rollOver. |
| message / flags callback | 86–94 | Запись чата и флагов | Локальные | toMessage ожидается; setFlag не ожидается. |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| extendedRoll(rollFormula,messageData,config=new RollConfig(),flags=[]) | Строка формулы; объект с system/flavor; RollConfig либо соответствующий объект | Promise<Roll> | evaluate первого Roll → при showCrit первый результат 10/1 → 1d10x10 → числовой итог → rollTotal → порог → сообщение/отложенные данные | Мутирует messageData; конфигурацию не меняет. Ошибка parse/evaluate/toMessage отклоняет Promise; setFlag не включён в его ожидание. |
| isCrit(roll) | Roll с dice и, при наличии первого кубика, хотя бы одним results | Boolean | Точное сравнение первого результата с 10 | Не проверяет faces, active/discarded, итог кубика или последующие кубики. |
| isFumble(roll) | Тот же контракт | Boolean | Первый результат равен 1 | Нет кубиков → false; первый кубик с пустыми results не защищён вторым optional access. |
| flags.forEach callback | Массив объектов key/value | Не собирает Promise | message.setFlag('TheWitcherTRPG',key,value) | Единичный объект обрабатывается аналогично; false/null пропускаются. При showResult=false весь аргумент flags игнорируется. |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| RollConfig | [module/scripts/rollConfig.js](../../../../../../../module/scripts/rollConfig.js) | Named import | 1, default config:9 | Описаны все поля; showSuccess здесь не читается. |
| Roll / evaluate / dice / options / total / toMessage | Foundry 14.367.0: client/dice/roll.mjs, client/dice/parser.mjs, client/dice/grammar.pegjs, client/dice/terms/{dice,die,numeric,operator,term}.mjs | Глобальный конструктор и методы | 10–12, 30, 58, 63–86 | Настоящие парсер, Roll и term-классы исполнены с управляемыми гранями; toMessage заменён. |
| ChatMessageData — формат входа | [module/chatMessage/chatMessageData.js](../../../../../../../module/chatMessage/chatMessageData.js) | Контракт аргумента; без импорта | messageData.system.rollTotal/flavor; showResult=false | Класс хранит ссылки; extendedRoll не требует instanceof, принимает аналогичный обычный объект. |
| WITCHER.Crit / Fumble / BeforeCrit / Chat.Success / Chat.Fail | [lang/en.json](../../../../../../../lang/en.json); [lang/ru.json](../../../../../../../lang/ru.json) | Локализация | 16–32, 35–83 | Точные ключи; thresholdDesc также локализуется динамически. |
| ChatMessage.setFlag | Foundry ChatMessage / Document API; namespace TheWitcherTRPG | Внешняя запись | 89–93 | Сохраняет дополнительные данные после создания сообщения; завершение не ожидается. |
| message.system.rollTotal | [module/data/chatMessage/baseMessageData.js](../../../../../../../module/data/chatMessage/baseMessageData.js); [module/data/chatMessage/attackMessageData.js](../../../../../../../module/data/chatMessage/attackMessageData.js); [module/data/chatMessage/defenseMessageData.js](../../../../../../../module/data/chatMessage/defenseMessageData.js) | Поля принимающих моделей | 63 | BaseMessageData NumberField, наследники используют rollTotal; сам extendedRoll схемы не создаёт. |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/item/witcherItem.js](../../../../../../../module/item/witcherItem.js) | extendedRoll | Получает готовые formula/messageData/config, ставит showResult=false; после изготовления сам выводит Roll. RollConfig импортирован только для JSDoc. | realCraft:181–186 |
| [module/item/systems/repair.js](../../../../../../../module/item/systems/repair.js) | extendedRoll | Готовит порог ремонта, тексты успеха/неудачи и showResult=false; вывод сообщения после ремонта. | commonRepair:190; prepareRollConfig:226–239 |
| [module/actor/mixins/skillMixin.js](../../../../../../../module/actor/mixins/skillMixin.js) | extendedRoll | Броски навыков: getCustomModifier, ChatMessageData base и RollConfig; пользовательский навык не задаёт threshold. | rollSkillCheck:57–82; rollCustomSkillCheck:146–172 |
| [module/actor/sheets/mixins/statMixin.js](../../../../../../../module/actor/sheets/mixins/statMixin.js) | extendedRoll | Спасбросок с reversal и модификатором; репутация — reversal либо обычный бросок. Перед вызовом присваивает flavor. | _onStatSaveRoll:13–35; _onReputation:51–81 |
| [module/actor/sheets/mixins/deathSaveMixin.js](../../../../../../../module/actor/sheets/mixins/deathSaveMixin.js) | extendedRoll | Испытание смерти: reversal=true, showCrit=false, threshold=stunBase; передаёт ChatMessageData base. | _onDeathSaveRoll:26–42 |
| [module/actor/mixins/defenseMixin.js](../../../../../../../module/actor/mixins/defenseMixin.js) | extendedRoll | Защита откладывает сообщение, дополняет ChatMessageData через append({crit})/append({stun}); stunSave отключает крит и включает reversal. | 194–241, createDefenseRollConfig:293–299, stunSave:437–451 |
| [module/actor/mixins/professionMixin.js](../../../../../../../module/actor/mixins/professionMixin.js) | extendedRoll | Атака профессии; бросок профессионального навыка с getCustomModifier, порогом и showResult из аргументов. У навыка в speaker передано this.actor. | 222–229, doProfessionSkillRoll:350–378 |
| [module/actor/mixins/verbalCombatMixin.js](../../../../../../../module/actor/mixins/verbalCombatMixin.js) | extendedRoll | addPart собирает формулу; сообщение damage с vcDamage и два дополнительных флага verbalCombat/damage. Вызов extendedRoll не ожидает. | 61–84, createVerbalCombatFlags:87–101 |
| [module/actor/mixins/castSpellMixin.js](../../../../../../../module/actor/mixins/castSpellMixin.js) | extendedRoll | Атака заклинанием: ChatMessageData attack, RollConfig({showResult:false}); затем await roll.toMessage(messageData). | 238–248 |
| [module/actor/mixins/weaponAttackMixin.js](../../../../../../../module/actor/mixins/weaponAttackMixin.js) | extendedRoll | Оружейная атака: ChatMessageData attack с UUID атакующего; extendedRoll с конфигурацией по умолчанию, без импорта RollConfig. | 303–310 |
| [module/actor/sheets/WitcherCharacterSheet.js](../../../../../../../module/actor/sheets/WitcherCharacterSheet.js) | extendedRoll | Изготовление: создаёт ChatMessageData base, задаёт RollConfig и тексты, вызывает Item.realCraft либо extendedRoll для симуляции. | ChatMessageData:265/361; конфигурация и вызов:326–346/414–434 |
| [module/scripts/verbalCombat/verbalCombatDefense.js](../../../../../../../module/scripts/verbalCombat/verbalCombatDefense.js) | extendedRoll | Словесная защита: ChatMessageData base, defense=true и порог totalAttack; передаёт флаги createVerbalCombatFlags. Выбор Actor отдельно в context callback:13. | 94–123 |

Область поиска: module/ и templates/ текущего checkout; прямые импорты и места вызова сверены отдельно от динамических обращений. Типы сообщений проверены по system.json и module/setup/registerDataModels.js. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Первый Roll сохраняет исходные кубики только для обычного результата. Критическое 10 запускает 1d10x10 и прибавляет весь итог; провальное 1 запускает такой же взрывающийся бросок, сохраняет исходную величину в options.fumbleAmount, затем ограничивает вычитаемое исходным total. При 1d10+8 и гранях 1;10,10,3 итог 0, fumbleAmount=23. При исходном отрицательном total провальная ветвь тоже даёт 0. Новый итоговый Roll содержит числа и подписи, в добавленном HTML остаются исходная формула и общий результат, но отдельные исходные грани в dice возвращаемого Roll не сохраняются.

Сравнение включено при threshold>=0: обычная атака total>threshold, защита total>=threshold; reversal — соответственно < и <=. rollOver равен total−threshold либо threshold−total. threshold=-1, другой отрицательный или undefined не дают options.success/rollOver и строки успеха. showSuccess не используется. reversal меняет CSS успеха/провала, но крит по-прежнему прибавляет, а провал вычитает.

showResult=false возвращает тот же messageData по ссылке в roll.messageData, без toMessage и применения аргумента flags. При true ожидается toMessage, затем инициируются независимые setFlag. В обоих режимах system.rollTotal и flavor изменяются у входного объекта. Изменения Actor, списание ресурсов, наложение травм/статусов остаются в потребителях, не в этом файле.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Обычный/числовой бросок и повторный крит | Группы 03–06 | 1d10+8 при 5 → 13; при 10;10,10,3 → 41; провал 1;10,10,3 → 0 с fumbleAmount=23; числовой 0 без кубиков работает | Roll/grammar/terms настоящие; грани заданы через fulfillment handler. |
| Первая грань и режимы | Группы 06–08 | showCrit=false не запускает второй бросок; d20=10 считается критом, d6=1 провалом; неактивный первый 1 у 2d10kh1 тоже провал. Матрица 4/5/6 с threshold=5 покрыла 12 сочетаний | Это контракт функции; обычные потребители начинают с 1d10. Не заявляется сбой стандартного однокубикового броска из-за проверки faces/active. |
| Ссылки и асинхронность | Группы 02, 09–10 | system/flags передаются по ссылке; toMessage удерживает общий Promise, setFlag — нет; отдельные flags при showResult=false не применяются | Фасады сообщений и управляемые Promise; сеть/БД не проверялись. |
| Формулы и ошибки | Группа 11 | Настоящий парсер принимает +-2, ++-2, ++2 и скобочный -2; отвергает 1d10+8+0 2[bonus] и незакрытую скобку. Отсутствие system вызывает TypeError | Подтверждён синтаксический контраст с issue-00033/00103; штатный ремонт останавливается раньше на настройке. |

## Непроверенные участки и открытые вопросы

Полностью прочитаны 107 строк. Нет валидации первого die.faces/active, произвольного HTML flavor или типов отдельных полей config. Эти факты не превращены в новые issues без самостоятельного сценария текущего потребителя. Случайное распределение, сетевое сохранение флагов и браузерный рендер не проверялись; формулы и арифметика исполнены ядром с заданными гранями.

## Связанные проблемы

[issue-00033](../../../../../../issues/potential/issue-00033.md), [issue-00103](../../../../../../issues/potential/issue-00103.md), [issue-00184](../../../../../../issues/potential/issue-00184.md). Две прежние проблемы подготовки формулы сопоставлены с реальным парсером. issue-00184 описывает окно между созданием сообщения и сохранением дополнительных флагов.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `9f16a7ae4bc942df85a105fd37d9a3cb3ef99f4b`; полный файл | Первая карточка; [сверка порции](../../../../review-log.md#task-0003028) |

## Уточнение TASK-0003.029

2026-09-11, `273a6d7db0b7c866399db3ecd4f7191817ae6f10`. Потребитель actor/skillMixin теперь разобран полностью. Исполнены реальные формулы семи характеристик, dontAddAttr монстра, EC магии, социальная матрица, собственные бонусы, детали и отмена. Skill-слой передаёт конфигурацию showCrit/showSuccess=true и обычно showResult=true; встроенный threshold передаётся, собственный остаётся −1. Боевая цепочка этим расширением не считается проверенной целиком.

Сверенные связи: [module/actor/mixins/skillMixin.js](../../../../../../../module/actor/mixins/skillMixin.js). Полные карточки новых файлов — в [указателе порции](../../../README.md#навыки-броски-развитие-и-пользовательские-навыки--task-0003029). [Проверки, ограничения и версия](../../../../review-log.md#task-0003029). Исходники и статус проблем не менялись.

## Уточнение TASK-0003.030

2026-09-11, `aa6af106e86a9c75fe050d599f961c8fadb74f1b`. Полностью описаны stat/death consumers. Настоящий Roll показал: порог 0 сравнивается, отрицательные−1/−2 оставляют success/rollOver undefined. В death-save отключён showCrit, поэтому 1/10 остаются одним кубиком; stat-save и обе ветви репутации используют критический механизм. Нет нового общего минимума характеристики.

Сверенные источники: [module/actor/sheets/mixins/statMixin.js](../../../../../../../module/actor/sheets/mixins/statMixin.js); [module/actor/sheets/mixins/deathSaveMixin.js](../../../../../../../module/actor/sheets/mixins/deathSaveMixin.js). [Итоговая сверка третьей серии, сценарии и ограничения](../../../../review-log.md#task-0003030). Код и статусы проблем не менялись.

## Уточнение TASK-0003.031

2026-09-11, `928ce4e537c6a3fdc34f8b6fa3fcfdb5a669f68d`. Обычное изготовление Character прошло через настоящий extendedRoll/Foundry Roll с управляемым d10. Для CRA4/crafting3/modifier1/d10=5 получено13, с диаграммой15; total=10 при DC10 неуспешно. Состояние с пустой подписью модификатора разобрано отдельно как синтаксическая ошибка +1[]. Алхимические ветви условны из-за issue-00037.

Связи: [module/actor/sheets/WitcherCharacterSheet.js](../../actor/sheets/WitcherCharacterSheet.js.md). [Методика и ограничения сверки](../../../../review-log.md#task-0003031).
