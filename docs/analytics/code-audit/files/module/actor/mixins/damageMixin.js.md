# module/actor/mixins/damageMixin.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/actor/mixins/damageMixin.js](../../../../../../../module/actor/mixins/damageMixin.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-12 |
| Ветка и коммит | rusbar-main, 965132d5d7972a0edd73aaa62484a1b6ba15991f |
| Изменения относительно коммита | Нет; совпадает со срезом TASK-0001 15da5b225535e34af4e132c701b5353ef4eb667f |
| Задача и порция | [TASK-0003.044](../../../../../../tasks/task-0003.044.md), 9 файлов / 603 логических строк; данный файл — 356 |
| Запись перекрёстной сверки | [TASK-0003.044](../../../../review-log.md#task-0003044) |

## Назначение файла

Применение урона к Actor: щит, броня, локации, сопротивления, HP/STA, сообщения и получение критической травмы.

## Условия использования

Именованный export damageMixin присоединяется к WitcherActor.prototype через Object.assign в [module/actor/witcherActor.js](../../../../../../../module/actor/witcherActor.js). Импорт определяет объект методов; сам по себе не наносит урон. [module/scripts/combat/applyDamage.js](../../../../../../../module/scripts/combat/applyDamage.js) передаёт урон из сообщения или статуса, [module/scripts/combat/combat.js](../../../../../../../module/scripts/combat/combat.js) вызывает отдельные действия критического результата.

Вход damageObject — структура атаки/повреждения с properties, location, внешним type и необязательными itemUuid/duration/strike. Это не Item.system.damageProperties. dialogData/enemyData содержит resistNonSilver/resistNonMeteorite/isVulnerable; штатный маршрут статуса и критического урона передаёт null. derivedStat — имя ресурса, обычно hp или sta. damageInstances — изменяемый массив настоящих DamageInstance.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| damageMixin | Экспорт объекта:6–356 | Методы Actor | Object.assign прототипа Actor | 12 методов, перечисленных ниже |
| locationArmor, armorSet, totalSP, displaySP | Локальные переменные:153–160 | Набор брони, числовой бюджет и текст SP | calculateDamageWithLocation | Число totalSP расходуется между экземплярами; displaySP не расходуется |
| damageResult / result | Возвращаемые объекты:190–197,238–244 | Результат одной локации | Обёртки и сообщения | Хранят ссылку на массив; обычный результат содержит properties, блокированный — нет |
| templateContext / chatData | Локальные структуры сообщений | Представление расчёта | Четыре HBS; ChatMessage.create | Создаются отдельно от списания ресурса |
| possibleWounds / woundRoll | Локальный отбор:315–335 | Выбор записи индекса | applyCritWound | Фильтруются prepared index-поля; UUID разрешается отдельно |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| async applyDamage:7–34 | dialogData, instances, damageObject, derivedStat; Actor | Promise<void> | Щит; ранний выход; масло; одна/все локации; статусы/applied; Item applyOnDamage | Ждёт обёртку урона; не ждёт вызовы статусных/активных эффектов; bypassesShield проверяется после расхода щита |
| async handleShield:36–68 | Массив, derivedStats.shield.value | Тот же массив | Общий щит расходуется по порядку; пишет shielded/damage; update щита; сообщение только при остатке>0 | update и ChatMessage.create без await; отрицательный damage увеличивает щит |
| async applyDamageToLocation:70–83 | Контекст и одна location | Promise<void> | Ждёт calculateDamageWithLocation; blocked→сообщение и return; иначе сообщение и updateDerivedStat суммы | Оба вызова методов сообщения без await; списание ресурса ожидается |
| async applyDamageToAllLocations:85–119 | getAllLocations/getLocationObject | Promise<void> | Меняет один damage.location в цикле; запускает расчёты с одним массивом; Promise.all; суммирует results; чат; ресурс | Массив и экземпляры не клонирует; ChatMessage.create здесь ожидается; speaker не задан |
| async updateDerivedStat:121–147 | damage, derivedStat; temporaryEffects для hp | Promise<void> | floor урона; расход временных HP; затем текущее значение минус остаток | Ждёт update каждого эффекта и Actor; JSON.parse без проверки типа; все changes выбранного эффекта считаются HP; границ ресурса нет |
| async calculateDamageWithLocation:149–245 | enemyData, damageProperties (весь damage), instances | Promise<result> | SP/IAP; серебро; расход SP; обязательный износ; flat; локация; сопротивления; обычный износ | Меняет instances/поля; ждёт SP-обёртки, но они не ждут реальных записей; подробности ниже |
| async createDamageBlockedBySp:247–261 | instances, displaySP | Promise<void> | initialDamageText.join(' + '), HBS spAbsorbs, speaker Actor, messageMode | Ждёт renderTemplate, не ChatMessage.create |
| async createDamageResultMessage:263–286 | damageResult | Promise<void> | Строки всех стадий, HBS damageToLocation, speaker/mode | Читает damageResult.damageProperties, хотя producer возвращает properties; не ждёт create |
| async applyCritDamage:288–298 | crit.critdamage | Promise<void> | Один DamageInstance без типа; источник Types.Item.criticalWound; torso, hp, обход обеих броней | Вызов applyDamage без await/return; щит не обходится |
| async applyBonusCritDamage:300–310 | crit.bonusdamage | Promise<void> | Тот же маршрут с бонусным значением | Те же границы завершения; это отдельное действие чата |
| async applyCritWound:312–344 | crit.location, criticalLevel; индекс выбранного pack | Promise<void> | Отбор none/location/level; выбор lesserEffect; await fromUuid; addItem; сообщение описания | Не ждёт addItem/create; нет проверки pack, пустого списка, отсутствующего варианта и resolve=null |
| calculateHealingTime:346–355 | criticalLevel, BODY.max | Число или undefined | simple=max(8−BODY,1); complex=max(12−BODY,1); difficult=max(15−BODY,1) | Без записи; deadly/unknown→undefined; вызовов этого метода в module/ не найдено |

### Порядок обработки

1. Щит обрабатывается до проверки bypassesShield и до добавления масла/серебра/flat. При полном поглощении обычного урона applyDamage прекращается; масло и эффекты не обрабатываются.
2. При совпадении truthy Actor.system.category и properties.oilEffect добавляется 5 типа oil. Этот новый экземпляр не проходил handleShield.
3. calculateDamageWithLocation получает locationArmor; improvedArmorPiercing делит числовой SP пополам с ceil. Та же операция над поясняющей строкой составной брони даёт NaN — issue-00283.
4. При настройке silverTrait=true свойство silverTrait присваивает строку методу instances[0].setType; type остаётся прежним — issue-00073. Иначе, при silverDamage и resistNonSilver, дополнительный Roll создаёт серебряный экземпляр. Для strong строка '*2' дописывается непосредственно к silverDamage, без скобок вокруг сложной формулы. Группа 39: 1d6+1 при minimize даёт 3 вместо 4 при умножении всего выражения — новая 298.
5. Один totalSP последовательно поглощает все экземпляры; каждому записывается afterSp. Затем вызывается applyAlwaysSpDamage. При отсутствии положительного остатка возвращается blockedBySp до flat/локации/сопротивлений/обычного износа.
6. Только flat>0 добавляет отдельный экземпляр без type и без afterSp. Отрицательный flat игнорируется. Все экземпляры умножаются на location.formula, округляются вниз и ограничиваются снизу 0; результат записывается в afterLocation.
7. Для каждого экземпляра ищется CONFIG.WITCHER.damageTypes по его type. calculateArmorResistances вызывается с общим damage и выбранной бронёй. Далее проверяется сопротивление несеребру/неметеориту; неподходящий тип делится пополам с floor. Наличие любого silverDamage подавляет первую проверку для всех экземпляров. Серебро по цели без resistNonSilver отдельно делится пополам. isVulnerable удваивает остаток. Записывается afterResistance.
8. Вызывается applySpDamage. Обычный result содержит properties, location, displaySP, spDamage и тот же массив. Сумму финальных damage передают updateDerivedStat.

В allLocations первые части async-расчётов выполняются до await, а затем продолжаются над общим массивом. Даже локально захваченная location не изолирует экземпляры. Без SP исходные 16 заканчиваются одним общим damage=3 и шестью ссылками на него: total=18. При Light SP 5 и исходных 10 все результаты blocked, total=0; отдельные независимые расчёты тех же зон дают 15,5,2,2,2,2. Это проверка фактической арифметики и взаимного влияния ветвей, не выбор нового правила суммирования.

### Временные HP и формат Foundry 14

system.changes — действующий путь, унаследованный WitcherActiveEffectData от ActiveEffectTypeDataModel Foundry 14. Ошибкой сам этот путь не является. Однако updateDerivedStat безусловно JSON.parse-ит change.value. Ядро при миграции прежнего корневого changes превращает корректную JSON-строку в объект. Такой объект уже не подходит повторному JSON.parse (группа 35, issue-00294).

Даже при строковом value внутри выбранного эффекта обрабатываются все changes: temporaryHp=3 вместе с attackModifier=5 при уроне 6 изменяет второй бонус до 2, оставляя HP 100. Настоящее сохранение не проверено; это мутация подготовленных записей и перехваченный payload update. Временные эффекты не удаляются при обнулении. STA обходится без этого цикла. Некорректная JSON-строка прекращает обработку до записи Actor; формат и чужие changes — разные причины отказа.

### Критические травмы

Это выбор Item из индекса Compendium, без RollTable.draw. ready заранее вызывает getIndex с полями treatment/location/criticalLevel/lesserEffect. При единственном кандидате случайность не нужна. При нескольких используется location.critEffect, если он не null/undefined; иначе getRandomInt(6)+critEffectModifier. Значение>4 выбирает lesserEffect===false, иначе true. Необъявленный модификатор после DefenseMessageData даёт NaN и меньшую травму — прежняя issue-00258.

Новый Item передаётся общему Actor.addItem. При совпадении имени/типа с существующим Item вне хранения addItem пытается увеличить quantity. У CriticalWoundData его нет: запрос получается NaN, новой травмы и новых effects нет; treatment/daysHealed не сбрасываются. Идентичность по UUID/семейству травмы здесь не реализована. При первом добавлении создаётся копия Item, а дальнейшие prepareDerivedData/heal/treat находятся в CriticalWoundData; этот файл сам не стабилизирует и не лечит.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| getRandomInt | [module/scripts/helper.js](../../../../../../../module/scripts/helper.js) | import/call | applyCritWound:326, d6 от 1 до 6 | Определение 73–75; фиксированный вход в проверках |
| DamageInstance | [module/scripts/damageInstance.js](../../../../../../../module/scripts/damageInstance.js) | import/new через create, чтение/мутация | Масло, серебро, flat, критический урон, методы текста | Все определения и вызовы прочитаны |
| applyActiveEffectToActorViaId | [module/scripts/temporaryEffects/applyActiveEffect.js](../../../../../../../module/scripts/temporaryEffects/applyActiveEffect.js) | import/call | applyDamage:32, Item.effects с system.applyOnDamage | Вложенный helper разрешает Item/Actor и применяет копии/запрос владельцу |
| applyStatusEffectToActor | [module/scripts/statusEffects/applyStatusEffect.js](../../../../../../../module/scripts/statusEffects/applyStatusEffect.js) | import/call | applyDamage:29, только statusEffect && applied | Получает Actor.uuid, ID и damage.duration |
| getLocationArmor; applyAlwaysSpDamage; applySpDamage; calculateArmorResistances | [module/actor/mixins/armorMixin.js](../../../../../../../module/actor/mixins/armorMixin.js) | Соседние методы через this | Расчёт SP, сопротивлений, износа | Полная предыдущая карточка и группы 18/24/34 |
| getFlatDamageMod / getMultiDamageMod | [module/actor/mixins/damageUtilMixin.js](../../../../../../../module/actor/mixins/damageUtilMixin.js) | Через this / через armorMixin | flat:200; multiplier читается внутри сопротивлений брони | Неправильный путь applyAP отдельно в issue-00025 |
| getAllLocations / getLocationObject | [module/actor/mixins/locationMixin.js](../../../../../../../module/actor/mixins/locationMixin.js); [module/actor/witcherActor.js](../../../../../../../module/actor/witcherActor.js) | Обёртки и static | Перебор и критический torso | Wrapper теряет monster this; tailWing отдельно доступен |
| addItem / items | [module/actor/witcherActor.js](../../../../../../../module/actor/witcherActor.js) | Вызов метода Actor | applyCritWound:336 | Общий merge name/type/quantity, строки 259–273 |
| CriticalWoundData | [module/data/item/criticalWoundData.js](../../../../../../../module/data/item/criticalWoundData.js) | Контракт index/Item и последующий lifecycle | treatment/location/lesserEffect/criticalLevel; собственное healingTime | В модели нет quantity; её calculateHealingTime не вызывает Actor helper |
| DamageProperties / DamageMessageData | [module/data/item/templates/combat/damagePropertiesData.js](../../../../../../../module/data/item/templates/combat/damagePropertiesData.js); [module/data/chatMessage/damageMessageData.js](../../../../../../../module/data/chatMessage/damageMessageData.js) | Входные поля | properties.effects у сообщения — Array; в Item — TypedObject | Нормальный маршрут applyDamage получает массив; прямой TypedObject вызывает filter-ошибку после HP |
| damageData / DefenseMessageData | [module/data/chatMessage/templates/damageData.js](../../../../../../../module/data/chatMessage/templates/damageData.js); [module/data/chatMessage/defenseMessageData.js](../../../../../../../module/data/chatMessage/defenseMessageData.js) | Очистка перед вызовом | Потеря duration / critEffectModifier | Схемы и прежние проверки 257/258 |
| criticalWoundsPack | [module/setup/settings.js](../../../../../../../module/setup/settings.js); [module/TheWitcherTRPG.js](../../../../../../../module/TheWitcherTRPG.js) | Настройка и подготовка индекса | applyCritWound:315–319 | ready getIndex четырёх полей |
| WITCHER.damageTypes / statusEffects | [module/setup/config.js](../../../../../../../module/setup/config.js) | Реестр типов/эффектов | type→likeSilver/likeMeteorite; source ключи | oil и null отсутствуют в damageTypes; неизвестный config ломает активные проверки сопротивления |
| derivedStats / temporaryHp | [module/data/actor/templates/common/stats/derivedStatsData.js](../../../../../../../module/data/actor/templates/common/stats/derivedStatsData.js); [module/data/actor/templates/common/temporaryEffectsData.js](../../../../../../../module/data/actor/templates/common/temporaryEffectsData.js) | Чтение/обновление | shield/hp/sta; временные JSON-записи | Происхождение полей отделено от расхода |
| damageTypeModification | [module/data/actor/templates/character/general/damage/damageTypeModificationData.js](../../../../../../../module/data/actor/templates/character/general/damage/damageTypeModificationData.js) | Чтение через helpers | flat/multiplication/applyAP | Реестр по типам |
| changes/applyAfterCalculations | [module/data/activeEffects/witcherActiveEffectData.js](../../../../../../../module/data/activeEffects/witcherActiveEffectData.js); [module/activeEffect/witcherActiveEffect.js](../../../../../../../module/activeEffect/witcherActiveEffect.js) | Модель и update hook | Расход временных HP | Ядро 14 common/data/active-effect.mjs; миграция common/documents/active-effect.mjs |
| Roll/evaluate; ChatMessage; fromUuid; update | Foundry14.367.0, client/dice/roll.mjs, common/abstract/document.mjs | Внешний API | Бросок серебра, запись/UUID/чат | Roll и core-модели настоящие; создание/UUID/update в проверках перехвачены |
| renderTemplate; messageMode; i18n | Foundry14.367.0 | Внешний API | Сообщения и переводы | Настоящие HBS/Handlebars; settings/localize фасады |
| Четыре шаблона damage | [templates/chat/damage/damageToLocation.hbs](../../../../../../../templates/chat/damage/damageToLocation.hbs); [templates/chat/damage/damageToAllLocations.hbs](../../../../../../../templates/chat/damage/damageToAllLocations.hbs); [templates/chat/damage/shieldAbsorbs.hbs](../../../../../../../templates/chat/damage/shieldAbsorbs.hbs); [templates/chat/damage/spAbsorbs.hbs](../../../../../../../templates/chat/damage/spAbsorbs.hbs) | renderTemplate | Представление этапов | Контексты сверены в собственных карточках |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/actor/witcherActor.js](../../../../../../../module/actor/witcherActor.js) | damageMixin | Импорт и Object.assign | Регистрация методов экземпляра |
| [module/scripts/combat/applyDamage.js](../../../../../../../module/scripts/combat/applyDamage.js) | applyDamage | Из сообщения после диалога или напрямую из статуса | DamageInstance.create(total).setType(damage.type); ресурс hp/sta |
| [module/scripts/combat/combat.js](../../../../../../../module/scripts/combat/combat.js) | applyCritDamage/applyBonusCritDamage/applyCritWound | Три пункта контекстного меню .crit-taken | message.system.crit |
| [module/scripts/combat/generalCombatHook.js](../../../../../../../module/scripts/combat/generalCombatHook.js) | applyDamage через applyDamageFromStatus | Эффекты начала хода | Свойства обхода щита/брони передаются обычным объектом |
| Четыре HBS этой порции | Результаты/контекст | Только чтение для чата | Прямых записей и обработчиков HBS нет |

Поиск потребителей выполнен в module/, templates/ и styles/. Одноимённый calculateHealingTime у CriticalWoundData — самостоятельный метод; вызов Actor helper по имени в этой области не найден. Внешние макросы и модули не исследовались.

## Данные и изменения состояния

Массивы, DamageInstance и damage.location меняются в памяти. shielded/afterSp/afterLocation/afterResistance — поля этого объекта, а не сохранённые параметры Actor. Запись shield/update эффектов/update HP/STA и создание ChatMessage — отдельные операции с различным ожиданием. В одном локационном сообщении методы текста вызываются правильно, но флаги не передаются по ожидаемому пути; в общем сообщении partial получает сырые results без текстовых полей.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Все 12 методов | Node stdin, полный исходный объект через vm | Группы 08–30,33–37; порядок, значения, ошибки и ожидание | Зависимости UI/документов перехвачены |
| Щит и ресурсы | 08–17 | Общий бюджет, bypass, отрицательные значения, pending updates, временные HP | Наличие отрицательных HP не названо нарушением правил |
| Одна/все локации | 18–25,34 | Общие ссылки, SP, серебро, flat/multi, контексты | 34 использует настоящую ArmorData; запись SP не выполнена |
| Получение травмы | 26–30,36–37 | Фильтры, выбор, отсутствие результатов, первое/повторное добавление | Каталог и fromUuid фасады; не живые packs |
| Формат v14 | 31,35 | system.changes допустим; миграция JSON→object ломает расход | Настоящий BaseActiveEffect.migrateData; не полный document lifecycle |

## Непроверенные участки и открытые вопросы

Полностью прочитан файл; браузер, игровой мир, серверная запись, конкурентные клиенты и соответствие рулбуку не проверены. Входы фасадов update показывают запрос и ожидаемое локальное состояние, а не сохранение в БД. Пустые/невалидные каталог и UUID проверены контролируемыми подстановками. Состав реальных травм и включение их в RollTable остаются вне этой порции.

## Связанные проблемы

Прежние: [00023](../../../../../../issues/potential/issue-00023.md), [00025](../../../../../../issues/potential/issue-00025.md), [00026](../../../../../../issues/potential/issue-00026.md), [00027](../../../../../../issues/potential/issue-00027.md), [00032](../../../../../../issues/potential/issue-00032.md), [00043](../../../../../../issues/potential/issue-00043.md), [00073](../../../../../../issues/potential/issue-00073.md), [00117](../../../../../../issues/potential/issue-00117.md), [00257](../../../../../../issues/potential/issue-00257.md), [00258](../../../../../../issues/potential/issue-00258.md), [00280](../../../../../../issues/potential/issue-00280.md), [00282](../../../../../../issues/potential/issue-00282.md), [00283](../../../../../../issues/potential/issue-00283.md).

Новые: [00284](../../../../../../issues/potential/issue-00284.md) обход щита; [00285](../../../../../../issues/potential/issue-00285.md) общие экземпляры локаций; [00286](../../../../../../issues/potential/issue-00286.md) отсутствующий тип flat/oil; [00287](../../../../../../issues/potential/issue-00287.md) контекст сообщений; [00288](../../../../../../issues/potential/issue-00288.md) повтор травмы; [00289](../../../../../../issues/potential/issue-00289.md) незавершённый выбор травмы; [00290](../../../../../../issues/potential/issue-00290.md) эффекты при полном SP; [00291](../../../../../../issues/potential/issue-00291.md) отрицательный урон и щит; [00292](../../../../../../issues/potential/issue-00292.md) повторный расход прежнего щита; [00294](../../../../../../issues/potential/issue-00294.md) объект value после миграции.

[issue-00298](../../../../../../issues/potential/issue-00298.md) — область действия множителя дополнительного серебра. Группа 40 также воспроизвела likeSilver-ошибку на автоматически добавленном oil и очистку quantity 1 настоящей CriticalWoundData.

## История актуализации

| Дата | Версия и область | Результат |
| --- | --- | --- |
| 2026-09-12 | 965132d5d7972a0edd73aaa62484a1b6ba15991f; полный файл | Первичная карточка; [перекрёстная сверка](../../../../review-log.md#task-0003044) |

## Дополнительная сверка TASK-0003.045

2026-09-12, rusbar-main, 20ce99a1218a82bf46c84570e55587253d0cfbc3; исходники не изменены.

Полностью разобраны [обёртки урона](../../../../../../../module/scripts/combat/applyDamage.js) и [Combat consumer](../../../../../../../module/scripts/combat/generalCombatHook.js). Их await не включает данный applyDamage: группа 30 прошла реальные методы до двух удерживаемых HP-записей 97/96 из 100 (урон 3/4), итог 96 после разрешения Promise; shield-запросы исполнялись сразу. Issue299 дополняет отдельные проблемы щита 292 и SP282. Группа 29 потеряла fire до входа: фактический урон 5 против 9 при сохранённом type и fire.flat4. Группа 31 показала путь положительного amount2/modifier−5 к shield5→8 (291). Все сообщения/update — фасады, реальная очередь документов не проверена.

[Проверки, результаты и ограничения](../../../../review-log.md#task-0003045). Связанные файлы не засчитываются повторно в покрытии.
