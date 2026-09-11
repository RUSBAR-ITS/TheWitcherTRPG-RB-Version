# module/actor/mixins/skillMixin.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/actor/mixins/skillMixin.js](../../../../../../../module/actor/mixins/skillMixin.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `273a6d7db0b7c866399db3ecd4f7191817ae6f10` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.029](../../../../../../tasks/task-0003.029.md), 14 файлов, 763 логических строк |
| Запись перекрёстной сверки | [TASK-0003.029](../../../../review-log.md#task-0003029) |

## Назначение файла

Примесь Actor для повышения встроенных навыков, бросков встроенного и собственного Item-навыка и социального модификатора. Это слой построения формулы; вычисление и отправку результата выполняет extendedRoll.

## Условия использования

Объект skillMixin присоединяется к WitcherActor.prototype. Встроенный навык выбирается по CONFIG.WITCHER.skillMap, собственный — по embedded Item ID из события. Методы повышения фактически требуют CharacterData с журналом и IP; методы броска используются также монстром.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| skillMixin | export let, строки 6–174 | Пять методов Actor | Object.assign(WitcherActor.prototype, skillMixin) | Сборка формул, запуск броска, журнал и обновление развития |
| rollFormula / RollConfig | Локальные значения методов броска | Формула 1d10 и параметры общего обработчика | Не сохраняются | showCrit/showSuccess включены; threshold передаётся только встроенным маршрутом |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| levelUpSkill(skillName) | Ключ skillMap; system.skills, improvementPoints, magic и logs | Promise без результата | Стоимость max(уровень, 1) × costMultiplier; журнал отрицательного IP; уровень +1 и обновление балансов | Нет проверки достаточности IP и максимума уровня. Внутренний let magicalCost затеняет внешний 0; журнальное и финальное update конкурируют. Ни update, ни Log.addIpReward не ожидаются |
| rollSkill(skillName, threshold = -1) | Ключ CONFIG.WITCHER.skillMap | Promise результата rollSkillCheck | Передаёт найденное описание и threshold | Неизвестный ключ не проверяется; commonsp/commonspeech расходятся в карте и схеме |
| rollSkillCheck(skillMapEntry, threshold = -1) | Описание с attribute/name/label и Actor.system | Результат extendedRoll | 1d10 + характеристика, если !dontAddAttr + уровень; затем addActiveEffects, addSocialStanding, EC трёх магических навыков и getCustomModifier | Читает характеристику даже при dontAddAttr. Отмена запроса модификатора отклоняет Promise; сообщения до extendedRoll нет |
| addSocialStanding(attribute, skillName) | attribute.name, тип Actor и general.socialStanding | Строка добавки к формуле либо пустая строка | Для character: tolerated −1 / hated −2 к charisma, leadership, persuasion, seduction; feared ещё −1 к charisma и +1 к intimidation | toleratedFeared/hatedFeared сочетают обе части; у монстра и прочих навыков нет добавки. Читает единое поле Actor, не региональные данные Race Item |
| rollCustomSkillCheck(event) | closest('.item').dataset.itemId; Item.system.attribute/value | Promise результата extendedRoll | 1d10 + выбранная характеристика, если !dontAddAttr + Item.value; addActiveEffects(Item.name), необязательный modifiers, запрос модификатора | Нет проверки ID, типа и атрибута. Собственное activeEffectModifiers не читается. Неизвестное имя не получает даже allSkills из modifierMixin; threshold остаётся −1 |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| ChatMessageData | [module/chatMessage/chatMessageData.js](../../../../../../../module/chatMessage/chatMessageData.js) | Прямой default import | Оба броска: Actor и подпись характеристики/навыка | Строки 1, 57–58, 145–146 |
| getCustomModifier | [module/scripts/helper.js](../../../../../../../module/scripts/helper.js) | Прямой named import | Ожидаемый запрос перед extendedRoll | Строки 2, 78, 166 |
| RollConfig | [module/scripts/rollConfig.js](../../../../../../../module/scripts/rollConfig.js) | Прямой named import | showCrit=true; showSuccess=true; встроенный threshold | Строки 3, 80–83, 168–171 |
| extendedRoll | [module/scripts/rolls/extendedRoll.js](../../../../../../../module/scripts/rolls/extendedRoll.js) | Прямой named import | Вычисляет формулу и публикует результат | Строки 4, 83, 171 |
| WITCHER.skillMap / magicSkills / statMap | [module/setup/config.js](../../../../../../../module/setup/config.js) | Глобальный CONFIG.WITCHER | Описания 52 навыков, коэффициенты стоимости, три магических ключа и девять исходных характеристик | levelUpSkill, rollSkill, rollCustomSkillCheck |
| addActiveEffects | [module/actor/mixins/modifierMixin.js](../../../../../../../module/actor/mixins/modifierMixin.js) | Метод этой же составной Actor | Добавки по имени встроенного навыка и skillGroupModifiers | rollSkillCheck / rollCustomSkillCheck; helper сначала требует ключ карты |
| getArmorEcumbrance | [module/actor/mixins/armorMixin.js](../../../../../../../module/actor/mixins/armorMixin.js) | Метод Actor | max(0, сумма EC надетой брони − ignoredArmorEncumbrance) | rollSkillCheck вычитает положительный EC только из hexweave/ritcraft/spellcast |
| CharacterData, Log.addIpReward | [module/data/actor/characterData.js](../../../../../../../module/data/actor/characterData.js); [module/data/actor/templates/character/logData.js](../../../../../../../module/data/actor/templates/character/logData.js) | Поля system / метод вложенной модели | Обычные и магические IP; журнал сам обновляет баланс | levelUpSkill; Log.addIpReward обращается к parent.parent.update |
| Skill, CommonActorData, MonsterData | [module/data/actor/templates/common/skills/skillData.js](../../../../../../../module/data/actor/templates/common/skills/skillData.js); [module/data/actor/commonActorData.js](../../../../../../../module/data/actor/commonActorData.js); [module/data/actor/monsterData.js](../../../../../../../module/data/actor/monsterData.js) | Схемы Actor | Уровни встроенных навыков; dontAddAttr; у монстра нет Character IP/logs/magic | Чтение схем и исполнение с настоящими моделями |
| SkillItemData | [module/data/item/skillItemData.js](../../../../../../../module/data/item/skillItemData.js) | Схема embedded Item | attribute, value и activeEffectModifiers; modifiers не объявлен | rollCustomSkillCheck |
| GeneralData / RaceData.socialStanding | [module/data/actor/templates/character/generalData.js](../../../../../../../module/data/actor/templates/character/generalData.js); [module/data/item/raceData.js](../../../../../../../module/data/item/raceData.js); [module/data/item/templates/socialStandingData.js](../../../../../../../module/data/item/templates/socialStandingData.js) | Сопоставление разных полей | Одно состояние Actor против пяти региональных состояний расы | addSocialStanding и определения схем; автоматического переноса при поиске не найдено |
| Actor.update / items; game.settings / i18n | Foundry VTT 14.367; настройки системы — module/setup/settings.js | Внешний API и глобальный контекст | Изменение документов, выбор Item, displayRollsDetails и локализация | Прямые обращения в пяти методах |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/actor/witcherActor.js](../../../../../../../module/actor/witcherActor.js) | skillMixin | Импорт и Object.assign в Actor | Импорт и присоединение прототипа |
| [module/actor/sheets/mixins/skillMixin.js](../../../../../../../module/actor/sheets/mixins/skillMixin.js) | rollSkillCheck / levelUpSkill | Обработчики data-action=rollSkill/level-up | skillListener |
| [module/actor/sheets/mixins/customSkillMixin.js](../../../../../../../module/actor/sheets/mixins/customSkillMixin.js) | rollCustomSkillCheck | Обработчик #custom-rollable | customSkillListener |
| [module/scripts/investigation/rollClue.js](../../../../../../../module/scripts/investigation/rollClue.js) | rollSkill | Бросок навыка расследования; DC сейчас не передаётся | rollClue вызывает actor.rollSkill(skillName) |

Область поиска: module/ и templates/ текущего checkout; прямые импорты и места вызова сверены отдельно от динамических обращений. Типы и листы сверены с system.json, module/setup/registerDataModels.js и module/setup/registerSheets.js. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Бросок использует уже подготовленные значения Actor и не записывает характеристику/уровень. Формула содержит независимые добавки, не вводит новый потолок характеристики. Социальный статус хранится в Actor.general.socialStanding; Race Item не является источником этого значения в данном обработчике. Повышение пишет system.skills.<attribute>.<переданный ключ>.value, system.improvementPoints и system.magic.magicImprovementPoints; Log отдельно пишет ipLog и один баланс. Для собственного навыка system.modifiers читается только при наличии, хотя текущая модель этот список не сохраняет.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Все методы, карта, схемы и потребители | Полное чтение 174 строк; rg по module/templates; определения прямых импортов | 4 импорта, 5 методов; системные и Item-навыки разделены | Соседние боевые методы проверены только в используемой части |
| Настоящие броски | Foundry 14.367 Roll/парсер, лица кубов заданы; 7 характеристик; Monster.dontAddAttr; EC; эффекты; запрос модификатора | 5+7+2=14; при threshold=14 успех false. Без характеристики 7; EC магии −3. Комплексная формула дала 18 | UI запроса, запись сообщения и инфраструктура Actor подменены; игровой мир не запускался |
| Социальная матрица | 6 состояний × charisma/leadership/persuasion/seduction/intimidation; Actor против Race | Для charisma: 0/−1/−2/−1/−2/−3; intimidation: 0/0/0/+1/+1/+1; Monster без добавки | Проверка реализации, не сверка текста правил |
| Развитие | Настоящие CharacterData и Log; уровни 0/2/10/−2, costMultiplier, магические IP 10/1/0; ожидаемые update удержаны | Обычный навык 2 при IP 0 даёт payload уровня 3 и IP −2; магический расход 4: Log пишет 6, завершающий update пишет прежние 10; метод завершён до update | Payload и порядок вызовов подтверждены; итог записи на сервере не моделировался |
| Собственные навыки и ошибки | Реальные SkillItemData; неизвестные ключи/атрибуты/ID; отмена; имя awareness | Item.activeEffectModifiers=4 проигнорирован; переименование в awareness подключает встроенные +7; неизвестное имя игнорирует allSkills; ошибки/отмена без успешного сообщения | modifiers в сценарии был явно внедрён в обход схемы для проверки старого кода |

## Непроверенные участки и открытые вопросы

Полный бой, подготовка всех характеристик, гонки документов в работающем мире, сторонние макросы и синхронизация клиентов не исследовались. Табличный предел навыка по правилам здесь не устанавливался: отсутствие ограничения в коде описано отдельно от утверждения о нарушении правил. Реальный браузер и сохранение embedded Item не запускались.

## Связанные проблемы

[issue-00004](../../../../../../issues/potential/issue-00004.md), [issue-00017](../../../../../../issues/potential/issue-00017.md), [issue-00028](../../../../../../issues/potential/issue-00028.md), [issue-00186](../../../../../../issues/potential/issue-00186.md), [issue-00190](../../../../../../issues/potential/issue-00190.md), [issue-00191](../../../../../../issues/potential/issue-00191.md), [issue-00192](../../../../../../issues/potential/issue-00192.md). Прежние наблюдения о ключах и IP уточнены; новые находятся в potential. Исправления и выбор решения не входят в порцию.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `273a6d7db0b7c866399db3ecd4f7191817ae6f10`; полный файл | Первая карточка; [сверка порции](../../../../review-log.md#task-0003029) |

## Дополнительная сверка TASK-0003.037

2026-09-11, `rusbar-main`, `639fde4bad4a7ba4c538d3b08ddc5cfd846ca75e`; исходники не менялись.

levelUpSkill расходует IP через Log, но не открывает Rewards и не зависит от его GM gate. В новом диалоге isMagic=true успешно увеличивает magic.magicImprovementPoints (группа09). Это не опровержение issue17: локальное затенение magicalCost относится к расходу при развитии навыка. Общая потеря await Log остаётся issue28.

[module/actor/mixins/rewardsMixin.js](rewardsMixin.js.md), [module/actor/rewardsSheet.js](../rewardsSheet.js.md), [module/app/reward/reward.js](../../app/reward/reward.js.md), [templates/chat/rewards.hbs](../../../templates/chat/rewards.hbs.md).

[Перекрёстная сверка и ограничения](../../../../review-log.md#task-0003037). Связанные файлы повторно в покрытие не добавлялись; исходники и статусы issues не менялись.
