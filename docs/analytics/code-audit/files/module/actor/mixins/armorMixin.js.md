# module/actor/mixins/armorMixin.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/actor/mixins/armorMixin.js](../../../../../../../module/actor/mixins/armorMixin.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-12 |
| Ветка и коммит | rusbar-main, 929ac4c6d90509ce06ef0795be380925e8b59e69 |
| Изменения относительно коммита | Нет; совпадает со срезом TASK-0001 15da5b225535e34af4e132c701b5353ef4eb667f |
| Задача и порция | [TASK-0003.043](../../../../../../tasks/task-0003.043.md), 3 файла / 320 логических строк; данный файл — 285 |
| Запись перекрёстной сверки | [TASK-0003.043](../../../../review-log.md#task-0003043) |

## Назначение файла

Выбор и сочетание брони по локации, EV, сопротивления и запросы износа предметов и естественной брони монстра.

## Условия использования

Экспортирует объект armorMixin; прямых import нет. [WitcherActor](../../../../../../../module/actor/witcherActor.js) импортирует его и присоединяет через Object.assign на строке 449. Одиннадцать методов становятся методами Actor. При импорте расчёты и записи не выполняются.

[calculateDamageWithLocation](../../../../../../../module/actor/mixins/damageMixin.js) получает armorSet/totalSP/displaySP, уменьшает входящий урон на SP, вызывает applyAlwaysSpDamage до проверки полного поглощения, затем сопротивления и обычный applySpDamage при оставшемся уроне. Примесь сама не снимает HP, не выбирает цель и не создаёт сообщений.

## Введённые сущности и действия с ними

| Сущность | Место / доступность | Назначение и действия |
| --- | --- | --- |
| armorMixin | Export let, 1–285 | Один объект, 11 методов; регистрация на прототипе Actor |
| armorSet | getArmors, 87–121 | Объект ссылок lightArmor/mediumArmor/heavyArmor/naturalArmor; не новые Item |
| Массивы локаций | getLocationArmor, 13–20 | Отбор покрывающих голову, торс, руки и ноги предметов |
| totalSP / displaySP | getLocationArmor/getStackedArmorSp | Числовой результат и отдельное пояснение; displaySP смешивает number и string |
| Callbacks filter/forEach | Отбор и подсчёт | Синхронный обход предметов; отдельных Hooks/обработчиков UI нет |

## Основные функции и методы

| Метод / строки | Входы | Результат и действия | Ограничения и изменения |
| --- | --- | --- | --- |
| getArmorEcumbrance, 2–10 | Actor.items, ignoredArmorEncumbrance | max(сумма encumb надетых armor − игнорирование, 0) | Все armor, включая isStored; не проверяет количество, локацию или состояние SP |
| getLocationArmor, 12–85 | location.name, properties | armorSet, totalSP, displaySP | getList('armor') исключает stored; equipped и modifiedMaxStoppingPower>0 определяют покрытие; неизвестная локация не обработана |
| getArmors, 87–121 | Список предметов данной локации | Ссылки на последний Item каждого класса | Более одного Light/Medium/Heavy: notification и undefined; Natural не подсчитывается |
| getArmorSp, 123–131 | armorSet, имя локации, properties | Делегирует четыре modifiedStoppingPower | armorSet должен существовать; пропущенный Item допустим |
| getStackedArmorSp, 133–179 | SP Light/Medium/Heavy/Natural, properties | Сочетание слоёв и отдельное сложение Natural | Носимая часть начинается с Heavy, затем Medium, затем Light; сортировки по текущему SP нет |
| getArmorDiffBonus, 181–204 | Два SP | Бонус по абсолютной разнице | Если любой SP≤0, результат 0; таблица ниже |
| calculateArmorResistances, 206–228 | DamageInstance, общий damage, armorSet | Изменяет instance.damage и возвращает тот же объект | AP/IAP: немедленный выход; до сопротивлений вызывает getMultiDamageMod |
| applySpDamage, 230–246 | location, properties, armorSet | Обычный износ: 1 либо floor(Roll('1d6/2+1')); crushingForce удваивает | bypassesWornArmor прекращает весь метод, включая естественную броню монстра; дочерние записи не ожидаются |
| applyAlwaysSpDamage, 248–255 | Те же; properties.spDamage | Возвращает spDamage ?? 0; запускает износ | Не проверяет bypassesWornArmor, ablating/crushingForce; даже ноль передаётся дальше |
| applySpDamageToItemArmor, 257–261 | armorSet, location, spDamage | Вызывает system.applySpDamage у Light/Medium/Heavy | Natural пропущен; async-метод не ожидает вызовы и возвращает undefined |
| applySpDamageToMonsterArmor, 263–284 | Actor.type, location, properties, spDamage | Запрос Actor.update одного поля с max(остаток,0) | Только monster и !bypassesNaturalArmor; update не ожидается |

### EV и отбор покрытия

EV и SP используют разные отборы: getArmorEcumbrance читает this.items напрямую, getLocationArmor — getList('armor') из Actor. Надетая броня isStored=true добавляет EV, но не SP (группа 02). Щит участвует в EV как armor. Его reliability не участвует в SP; однако вручную заполненные поля покрытия щита включаются обычным отбором (04).

Строка Item.system.location не определяет расчёт покрытия: его определяют шесть modifiedMaxStoppingPower. Поэтому location='Head' с torso.maxStoppingPower=10 защищает торс (03). Броня с current=0/max>0 всё ещё входит в armorSet и может предоставлять сопротивление (14).

### Источники SP по локациям

| Локация | Поле естественной брони Actor | Item-поле |
| --- | --- | --- |
| head | armorHead | head |
| torso, rightArm, leftArm | armorUpper | Соответствующее имя |
| rightLeg, leftLeg | armorLower | Соответствующее имя |
| tailWing | armorTailWing | Носимый набор всегда пуст |

Поля Actor читаются с ??0 без проверки type; штатно они объявлены у MonsterData. На чтении они складываются с предметным Natural. bypassesNaturalArmor убирает оба источника; bypassesWornArmor убирает Light/Medium/Heavy. Для монстра torso=4, Light=10, Natural=3 результаты: 17; только обход носимой — 7; только обход естественной — 10; оба — 0 (09).

getLocationArmor вызывает getArmorSp дважды — отдельно для текста и числа. Стандартный расчёт синхронный. При двух предметах одного носимого класса getArmors возвращает undefined, а getArmorSp затем выбрасывает TypeError; уведомление не завершает маршрут корректно (08).

### Сочетание слоёв

| Абсолютная разница положительных SP | Бонус |
| --- | --- |
| 0–5 | 5 |
| >5–9 | 4 |
| >9–15 | 3 |
| >15–20 | 2 |
| >20 | 0 |

Для целых значений границы испытаны в группе 06. При трёх слоях вторая разница берётся между Medium и Light, а не между уже накопленной суммой и Light. Light=10, Medium=15, Heavy=20 дают 30; Natural=3 добавляет до 33. Все восемь сочетаний носимых слоёв проверены отдельно (30).

Основа выбирается по классу и truthy SP, а не по наибольшему текущему числу. Heavy=1/max=20 и Light=10 дают 5; отключение Heavy возвращает 10 (07). Игровое правило сочетания повреждённых слоёв не переопределялось. Отрицательные SP и несколько Natural не нормализуются: последний Natural выигрывает по порядку отсортированного getList.

### Сопротивления и бронебойность

armorPiercing/improvedArmorPiercing не меняют getLocationArmor. В consumer только improvedArmorPiercing делит totalSP пополам с округлением вверх; оба флага обходят calculateArmorResistances.

При сопротивлении любого носимого слоя выполняется один floor(0.5 × instance.damage × damageMulti). Проверяется resistance[damageInstance.type]. Для Natural — отдельный такой же расчёт, но ключ взят из damage.type. Это разные типы для добавочной серебряной порции: при основной slashing естественная resistance.slashing уменьшила silver=20 до 10, носимая не изменила его (13).

damageMulti вычисляется по общему damage.type; без сопротивлений не применяется, при двух ветках применяется дважды. Группа 12 повторила issue-00026: 20 → 20/30/45 при коэффициенте 3. applyAP=true по штатному damage.properties повторяет issue-00025 ещё до проверки брони. initialDamage/afterResistance этот метод не меняет; afterResistance заполняет consumer.

### Износ и запись

Обычный износ вызывается consumer после пробития SP; постоянный — перед проверкой полного поглощения. properties.spDamage поступает, в частности, от [applyCombatEffect](../../../../../../../module/scripts/combat/generalCombatHook.js) из status.damage.spDamage; это дополнительное поле plain object, отсутствующее в DamageProperties. Само отсутствие поля в модели не доказывает потери на этом маршруте.

[ArmorData.applySpDamage](../../../../../../../module/data/item/armorData.js) сравнивает ущерб с modifiedStoppingPower, а записывает базовый stoppingPower. При SP=3 урон 2/3/4 даёт запросы 1/0/ничего (15, issue-00083). При базе 1 и улучшении +2 урон 2 запрашивает базу −1; _source в опыте остаётся 1 (16). Отрицательная база с улучшением отдельно не объявлена ошибкой.

Монстр запрашивает изменение armorHead/armorUpper/armorLower/armorTailWing и ограничивает остаток нулём. Один общий armorUpper используется для торса и обеих рук, armorLower — для обеих ног. Natural Item не передаётся в метод износа предметов. Правило его деградации требует отдельного подтверждения; это описанное различие, не выполненное исправление.

Четыре async-метода не ждут сохранение дочерних документов. При исходных Item SP=10/monster armorUpper=10 последовательные await износа 2 и 1 запросили 8/8, затем 9/9, пока записи оставались pending (21). Это доказательство чтения прежних значений и раннего завершения, а не результат реальной БД.

## Используемые сущности и зависимости

| Сущность | Источник | Вид, место и цель | Основание |
| --- | --- | --- | --- |
| getList | [module/actor/witcherActor.js](../../../../../../../module/actor/witcherActor.js) | Вызов в getLocationArmor:13; фильтр isStored и sort | Точное тело использовано в опытах |
| equipped, type, encumb, шесть SP, resistance, applySpDamage | [module/data/item/armorData.js](../../../../../../../module/data/item/armorData.js) | Чтение/динамический вызов | Настоящие ArmorData и родитель DataModel-фасад |
| modifiedStoppingPower / modifiedMaxStoppingPower | [module/data/item/templates/armor/spData.js](../../../../../../../module/data/item/templates/armor/spData.js) | Отбор и расчёт SP | Выполнены настоящие base/derived; улучшение задано в памяти |
| resistance | [module/data/item/templates/armor/resistanceData.js](../../../../../../../module/data/item/templates/armor/resistanceData.js) | slashing/piercing/bludgeoning | Реальная схема; проверки обеих веток |
| armorHead/Upper/Lower/TailWing | [module/data/actor/monsterData.js](../../../../../../../module/data/actor/monsterData.js) | Чтение и запрос обновления | Реальная MonsterData; без Actor lifecycle |
| ignoredArmorEncumbrance | [module/data/actor/templates/common/lifepathData.js](../../../../../../../module/data/actor/templates/common/lifepathData.js) | Начальное вычитание EV | Путь схемы и consumer |
| damage.properties | [module/data/item/templates/combat/damagePropertiesData.js](../../../../../../../module/data/item/templates/combat/damagePropertiesData.js) | AP/IAP, bypass, ablating/crushingForce | Реальная модель в большинстве опытов |
| DamageInstance.damage/type | [module/scripts/damageInstance.js](../../../../../../../module/scripts/damageInstance.js) | Изменение отдельной порции | Настоящий экземпляр; возвращается та же ссылка |
| getMultiDamageMod | [module/actor/mixins/damageUtilMixin.js](../../../../../../../module/actor/mixins/damageUtilMixin.js) | Сопротивления:212 | Настоящий helper; ошибка пути applyAP и кратность коэффициента |
| spDamage | [module/scripts/combat/generalCombatHook.js](../../../../../../../module/scripts/combat/generalCombatHook.js), [module/data/actor/templates/common/combatEffectsData.js](../../../../../../../module/data/actor/templates/common/combatEffectsData.js) | Источник прямого износа | Проверен producer и NumberField; полный ход боя не запускался |
| Roll.evaluate | Foundry 14.367.0, /opt/foundryvtt/client/dice/roll.mjs | Ablation, строка 236 | Настоящий Roll с minimize/maximize |
| update / notifications / localize | Foundry; [lang/en.json](../../../../../../../lang/en.json), [lang/ru.json](../../../../../../../lang/ru.json) | Запись и сообщения | Вызовы перехвачены; i18n возвращает ключ, перевод не тестировался |

## Известные потребители

| Файл | Использование |
| --- | --- |
| [module/actor/witcherActor.js](../../../../../../../module/actor/witcherActor.js) | Import/Object.assign; calculateStat вычитает EV у REF/DEX отдельно от штрафа массы |
| [module/actor/mixins/damageMixin.js](../../../../../../../module/actor/mixins/damageMixin.js) | calculateDamageWithLocation: SP → постоянный износ → локация → сопротивления → обычный износ |
| [module/actor/mixins/castSpellMixin.js](../../../../../../../module/actor/mixins/castSpellMixin.js) | castSpell: EV и ignoredEvWhenCasting, строки 35–47 |
| [module/actor/mixins/skillMixin.js](../../../../../../../module/actor/mixins/skillMixin.js) | rollSkillCheck: EV для hexweave/ritcraft/spellcast, строки 69–74 |
| Эта примесь | Внутренние вызовы остальных методов |

Оружейная атака и защита получают уже подготовленные значения REF/DEX; собственных прямых вызовов getArmorEcumbrance у них нет. Поиск всех одиннадцати имён выполнен по module/templates. Соседи вне состава порции не получили полного покрытия.

## Данные и изменения состояния

Расчёты читают подготовленные поля; armorSet хранит ссылки на исходные документы. Сопротивления меняют DamageInstance в памяти; износ только запрашивает Item/Actor.update. Базовый и модифицированный SP различаются, текст displaySP не является числовым totalSP.

На стороне calculateDamageWithLocation Math.ceil(displaySP/2) для составного текста даёт NaN, хотя число SP делится корректно: Heavy=20+Light=10 даёт SP=23, IAP оставляет 12, урон 30 → afterSp=18 (23). В этой порции зафиксирован результат producer для сообщения; реальный чат не рендерился.

## Проверки и доказательства

Все 285 строк и 11 методов прочитаны. [Журнал](../../../../review-log.md#task-0003043) содержит 31 группу: все сочетания слоёв, границы разницы/SP, bypass/AP, реальные ArmorData/MonsterData/DamageInstance/Roll, consumer урона и участки EV. Износ/HP/сохранение мира не заявляются проверенными по фасадам.

## Непроверенные участки и открытые вопросы

Непрочитанных участков файла нет. Не проверены реальный Actor/Item lifecycle, порядок сетевых подтверждений, HP, эффекты на persisted:false поля, полный бой по всем локациям, визуальный чат и соответствие правилу книги. Несколько Natural, отрицательные SP/износ и сопротивления при SP=0 описаны без выбора нового игрового правила.

## Связанные проблемы

Новые: [277](../../../../../../issues/potential/issue-00277.md) (stored EV), [278](../../../../../../issues/potential/issue-00278.md) (дубли класса), [279](../../../../../../issues/potential/issue-00279.md) (уменьшение SP добавленным слоем), [280](../../../../../../issues/potential/issue-00280.md) (тип Natural resistance), [281](../../../../../../issues/potential/issue-00281.md) (bypass и естественный износ), [282](../../../../../../issues/potential/issue-00282.md) (раннее завершение/старый SP), [283](../../../../../../issues/potential/issue-00283.md) (NaN пояснения).
Прежние [25](../../../../../../issues/potential/issue-00025.md), [26](../../../../../../issues/potential/issue-00026.md), [35](../../../../../../issues/potential/issue-00035.md), [83](../../../../../../issues/potential/issue-00083.md), [254](../../../../../../issues/potential/issue-00254.md) уточнены; все остаются potential.

## История актуализации

| Дата | Версия и область | Результат |
| --- | --- | --- |
| 2026-09-12 | 929ac4c6d90509ce06ef0795be380925e8b59e69; полный файл | Первичная карточка; [перекрёстная сверка](../../../../review-log.md#task-0003043) |
