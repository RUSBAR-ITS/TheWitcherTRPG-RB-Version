# packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Compound_Arm_Fracture__Left___Stabilized__tdcGSOZGCUhNArDc.json

| Поле | Значение |
| --- | --- |
| Исходный файл | [packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Compound_Arm_Fracture__Left___Stabilized__tdcGSOZGCUhNArDc.json](../../../../../../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Compound_Arm_Fracture__Left___Stabilized__tdcGSOZGCUhNArDc.json) |
| Тип файла | JSON: Item типа criticalWound |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-16: актуализация технических обращений по issue-00001 |
| Ветка и коммит | `dev`, база `d8e0e1ad1159cb71a8769b0353f812de6f1ed4d8` + незакоммиченное исправление issue-00001 |
| Изменения относительно коммита | issue-00001; текущие технические обращения актуализированы. Прежние опыты ниже относятся к своим датам. |
| Задача и порция | [TASK-0003.060](../../../../../../tasks/task-0003.060.md) |
| Запись перекрёстной сверки | [Протокол .060](../../../../review-log.md#task-0003060) |

Актуализация [issue-00001](../../../../../../issues/closed/issue-00001.md), 2026-09-16: Внутренние UUID направлены на TheWitcherTRPG-RB-Version. ID документов, диапазоны, эффекты и _stats сохранены. Датированные результаты и прежние значения UUID ниже являются историей.

## Назначение файла

Экспорт Compound Arm Fracture (Left - Stabilized): состояние stabilized, локация leftArm. Вложенных ActiveEffect: 0; изменений: 0. Данные задают шаблон травмы и её переход; действия выполняют потребители системы и Foundry.

## Условия использования

[system.json](../../../../../../../system.json) регистрирует пакет Item `TheWitcherTRPG.criticalWounds` по пути packs/criticalWounds.db. [compilePack](../../../../../../../utils/packs.mjs) рекурсивно собирает экспорт, [extractPack](../../../../../../../utils/extract.mjs) извлекает его с папками; команды из [package.json](../../../../../../../package.json) не запускались. JSON не читается непосредственно в игровом applyCritWound; содержимое установленной БД не проверялось.

[ready:62–67](../../../../../../../module/TheWitcherTRPG.js) запрашивает четыре поля индекса: system.criticalLevel/location/lesserEffect/treatment; выбор пакета задаёт [criticalWoundsPack](../../../../../../../module/setup/settings.js). Item исключается из исходного выбора по treatment и используется через followUp или ручное добавление. Проверен индекс-фасад из настоящих очищенных моделей, не действующий серверный индекс.

## Введённые сущности и действия с ними

| Сущность | Вид и место | Назначение и доступность | Действия |
| --- | --- | --- | --- |
| Compound Arm Fracture (Left - Stabilized) | Корневой Item; name:3, _id:30 | ID `tdcGSOZGCUhNArDc`; UUID `Compendium.TheWitcherTRPG-RB-Version.criticalWounds.Item.tdcGSOZGCUhNArDc` | Загрузка, копирование к Actor, подготовка, лечение/удаление |
| _key / folder / sort | Корневые поля | `"!items!tdcGSOZGCUhNArDc"` / `"ox3lLmV3zp0K67Ht"` / `0` | Ключ экспорта, родительская папка и сортировка; sort не приоритет эффекта |
| flags / _stats | Корневые метаданные | `{}` / `{"compendiumSource":null,"duplicateSource":null,"exportSource":null,"coreVersion":"13.351","systemId":"TheWitcherTRPG","systemVersion":"AUTOMATICALLY REPLACED BY GITHUB WORKFLOW ACTION"}` | История экспорта и пользовательские флаги; версия в _stats не подтверждает запуск этой версии сейчас |
| img / ownership | Корневые поля | `"icons/svg/item-bag.svg"` / `{"default":0,"ugXtPMJIktbl63QV":3}` | Ресурс ядра вне пофайлового анализа; наличие указанного пользователя в мире не подтверждено |
| system / effects | Объекты, строки 6 / 20 | criticalWound / 0 embedded ActiveEffect | Схема и воздействия перечислены далее |

| Поле system | Экспортное значение | Смысл и потребитель |
| --- | --- | --- |
| htmlFields | `["description"]` | Устаревшая декларация; defineSchema её не содержит, очистка модели удаляет поле. |
| description | `"<p>The arm is useless</p>"` | HTMLField; enrichedText/createEnrichedText, редактор и сообщение applyCritWound. Текст не преобразуется в changes. |
| criticalLevel | `"difficult"` | StringField; выбор кандидатов и ветвь difficult расчёта healingTime. |
| treatment | `"stabilized"` | StringField; выбор none и проверка treated в heal. |
| location | `"leftArm"` | StringField; фильтр applyCritWound и lookup подписи списка. |
| lesserEffect | `false` | BooleanField; при нескольких кандидатах first find: false для >4, true для ≤4. |
| daysHealed | `0` | NumberField; счётчик заживления, редактирование и update в heal. |
| healingTime | `0` | NumberField; у владельца Actor prepareDerivedData рассчитывает max(15−BODY.max,1). |
| sterilized | `false` | BooleanField; новая стерилизация даёт ещё +2 дня к очередному дню. |
| followUp | `"Compendium.TheWitcherTRPG-RB-Version.criticalWounds.Item.zaKPfDQFGTR8FKju"` | DocumentUUIDField типа Item; treat загружает адресата или удаляет конечный Item. |

Effects=[]: активных эффектов, changes и статусов из этого Item нет. Условия в описании не преобразуются движком в автоматические модификаторы.

## Основные функции и методы

JSON не вводит собственных функций или обработчиков. Действия принадлежат следующим потребителям:

| Метод | Вход / условие | Результат и граница ожидания |
| --- | --- | --- |
| applyCritWound → addItem | Уровень, локация, critEffect и индекс | Выбор Item, запрос добавления и чат; повтор name/type может попасть в quantity |
| prepareDerivedData → calculateHealingTime | Родитель Actor | healingTime=max(15−BODY.max,1), вычисление без самостоятельной записи |
| treat | followUp или null | await fromUuid; createEmbeddedDocuments без await; затем delete без await |
| heal | treated и sterilized | +1 день, впервые со стерилизацией ещё +2; по достижении healingTime → treat; иначе update без await |
| allApplicableEffects → applyActiveEffects | Активные transfer-эффекты Item | Фаза/приоритет, применение через DataField и подготовленные значения Actor; multiply=10 раньше add=20; исходный JSON не записывается |

## Используемые сущности и зависимости

| Сущность | Источник | Вид связи | Место/цель и доказательство |
| --- | --- | --- | --- |
| criticalWounds | [system.json](../../../../../../../system.json) | Регистрация | Строки 28,52–56; Item-пакет и packFolders |
| compilePack / extractPack | [utils/packs.mjs](../../../../../../../utils/packs.mjs), [utils/extract.mjs](../../../../../../../utils/extract.mjs) | Сборка/экспорт | Рекурсивные JSON и folders:true; статически, без записи |
| CriticalWoundData.defineSchema/treat/heal | [module/data/item/criticalWoundData.js](../../../../../../../module/data/item/criticalWoundData.js) | Модель и переходы | Поля system и followUp; реальные вызовы на всех документах |
| registerDataModels | [module/setup/registerDataModels.js](../../../../../../../module/setup/registerDataModels.js) | Реестр | criticalWound:52 и base:73 |
| WitcherItem.migrateData/migrateSpells | [module/item/witcherItem.js](../../../../../../../module/item/witcherItem.js) | Миграция документа | Статически: Hexes/Rituals здесь отсутствуют; исполнялся BaseItem с реальной системной моделью |
| WitcherActiveEffectData.defineSchema | [module/data/activeEffects/witcherActiveEffectData.js](../../../../../../../module/data/activeEffects/witcherActiveEffectData.js) | Наследование схемы | super сохраняет system.changes; флаги по умолчанию false |
| WitcherActiveEffect.isSuppressed | [module/activeEffect/witcherActiveEffect.js](../../../../../../../module/activeEffect/witcherActiveEffect.js) | Подавление и применение | Настоящий класс; disabled/transfer/applySelf-контроли |
| CharacterData/CommonActorData | [module/data/actor/characterData.js](../../../../../../../module/data/actor/characterData.js) | Схема Actor | Настоящие модели и базовая подготовка |
| calculateStats/calculateFixedDerivedStats/calculateDerivedStats | [module/actor/witcherActor.js](../../../../../../../module/actor/witcherActor.js) | Расчёт | Настоящие методы после initial effects; вес/броня=0 |
| ready/getIndex | [module/TheWitcherTRPG.js](../../../../../../../module/TheWitcherTRPG.js) | Подготовка индекса | 62–67: четыре запрошенных поля; серверный getIndex не исполнялся |
| criticalWoundsPack | [module/setup/settings.js](../../../../../../../module/setup/settings.js) | Настройка | Выбор пакета по ключу; проверен код и индекс-фасад |
| BaseItem/BaseActor/BaseActiveEffect, NumberField/SchemaField | Foundry 14.367.0; /opt/foundryvtt/common/documents/ и common/data/fields.mjs | Внешнее ядро | Настоящие классы, строгая валидация и штатная миграция |
| ActiveEffect.prepareBaseData/applyChange; Actor.applyActiveEffects | Foundry 14.367.0; /opt/foundryvtt/client/documents/active-effect.mjs и actor.mjs | Внешнее ядро | Реальные методы с фасадом окружения; 189 изменений адресуют NumberField, девять — SchemaField, три пути commonspeech отсутствуют в схеме |

## Известные потребители

| Потребитель | Используемые данные | Условия и доказательство |
| --- | --- | --- |
| [module/actor/mixins/damageMixin.js](../../../../../../../module/actor/mixins/damageMixin.js) | criticalLevel/treatment/location/lesserEffect и UUID | applyCritWound:312–345; восемь проверок выбора на очищенном индексе |
| [module/actor/witcherActor.js](../../../../../../../module/actor/witcherActor.js) | name/type и модификаторы Actor | addItem:259–273 и расчёты; реальные методы |
| [module/actor/sheets/mixins/criticalWoundMixin.js](../../../../../../../module/actor/sheets/mixins/criticalWoundMixin.js) | UUID и system.treat | _onTreat:12–17; статическая связь, treat исполнен отдельно |
| [module/item/sheets/WitcherCriticalWoundSheet.js](../../../../../../../module/item/sheets/WitcherCriticalWoundSheet.js) | Item и followUp | _onDropItem:17–21 сохраняет item.uuid; браузер не запускался |
| [templates/sheets/item/criticalWound-sheet.hbs](../../../../../../../templates/sheets/item/criticalWound-sheet.hbs) | Имя/изображение/system | Редактор полей и UUID; статическое чтение |
| [templates/partials/crit-wounds-table.hbs](../../../../../../../templates/partials/crit-wounds-table.hbs) | Локация, лечение, дни, UUID | lookup локации:18; кнопка вызывает treat |
| [module/actor/sheets/mixins/healMixin.js](../../../../../../../module/actor/sheets/mixins/healMixin.js) | system.heal | recoverActor:88 без ожидания; статическая связь, heal исполнен отдельно |

Текстовая [Difficult Critical](../../../../../../../packsJson/combat/Difficult_Critical_VIup1SZTMKCSGGbT.json) не читается applyCritWound как источник Item. Найденные маршруты не исключают внешние макросы или динамических потребителей.

## Данные и изменения состояния

Папка: [Difficult](_Folder.json.md). Предшественник: [Compound Arm Fracture (Left)](Compound_Arm_Fracture__Left__saPd4IMUCv5qZE60.json.md). Следующий Item: [Compound Arm Fracture (Left - Treated)](Compound_Arm_Fracture__Left___Treated__zaKPfDQFGTR8FKju.json.md), `zaKPfDQFGTR8FKju`, treatment=treated. Реальный treat инициировал создание этого документа, затем удаление текущего. Создание/удаление перехвачены и возвращали pending Promise. Переход загружает другой шаблон с его собственными эффектами; не переписывает изменения прежнего эффекта. На новой подготовке без Item его воздействия не применяются.

Контрольный Actor: восемь unmodifiedMax=5, HP.value=25, dodge.value=athletics.value=8 до эффектов, броня/вес=0. Результат: INT=5, WILL=5, REF=5, DEX=5, BODY=5, SPD=5; BODY.max=5, SPD.max=5; RUN=15, LEAP.value=3, LEAP.max=3, ENC=50, STUN=5, REC=5, HP.max=25, RESOLVE.max=25, FOCUS.max=15; healingTime=10. Навыки: dodge.value=8, dodge.activeEffectModifiers=0; athletics.value=8, athletics.activeEffectModifiers=0. Статусы=`[]`; turnStartEffects={}. Значения прочитаны непосредственно из подготовленных полей; сериализация DataModel/toObject возвращает источник и не заменяет такую проверку.

None и treated этого семейства содержат bleed, stabilized — пустой effects. Использование руки ограничено текстом HTML, изменения полей экипировки/атаки не заданы. Возврат bleed в treated отмечен как свойство контента; правильность по рулбуку не устанавливалась.

## Проверки и доказательства

[Протокол .060](../../../../review-log.md#task-0003060): все 25 JSON / 3351 строк прочитаны, корневые ID/_key сверены среди 98 criticalWounds, вложенные _key/ID — в своей области. Все 16 followUp проверены до конечного состояния, без циклов и переходов вне Difficult. Настоящие модели и методы в изолированном Node 24.16.0 прошли 1748 утверждений: 24 Item, Folder, 25 effects/201 changes, подготовленные поля/производные, 24 treat, семь heal, восемь выборов, повторный addItem, исключение эффекта и подпись правой treated ноги. Отдельный сценарий: 43 утверждения, девять исходных периодических записей и три диагностические копии с override вместо ADD. Всего 1791 утверждение. Числа относятся к порции, индивидуальные значения указаны выше.

## Непроверенные участки и открытые вопросы

Текущая сверка охватила исходник, описанные поля и конкретных потребителей; прежние результаты выше сохраняют даты своих опытов. ADD SchemaField, NumberField modifier, statuses и очередь начала хода различены. Исходные16 ADD объектов не достигают урона; override-копии только диагностические. Остаются одноимённые источники при удалении, start/expiry/updateDuration/registry, Combat/GM и конечные HP. .017/.018 сохраняют эти границы без исправления экспорта. Границы: [U012-05](../../../../cross-check-0002.md#u012-05) и [U012-08](../../../../cross-check-0002.md#u012-08).

## Связанные проблемы

[issue-00121](../../../../../../issues/potential/issue-00121.md) — ожидание замены, [issue-00127](../../../../../../issues/potential/issue-00127.md) — граница завершения лечения, [issue-00288](../../../../../../issues/potential/issue-00288.md) — повтор name/type. Статусы potential сохранены, подтверждения/исправления не выполнялись. Наличие этих общих проблем не объявляет дефектом каждое поле или папку.

## История актуализации

2026-09-13 — полная карточка в TASK-0003.060 на указанном коммите; исходник не изменён. [Протокол .060](../../../../review-log.md#task-0003060) содержит общие условия и индивидуальные проверки.

## Сквозная сверка TASK-0004.012

2026-09-14; rusbar-main, a853fc2ff721e5d33b2716081c657bd92d62d86b. Исходник совпадает со срезом TASK-0001; изменено только описание.

Item `tdcGSOZGCUhNArDc` («Compound Arm Fracture (Left - Stabilized)»): `difficult/stabilized/leftArm`; 0 ActiveEffect, 0 changes. Предшественник: `saPd4IMUCv5qZE60`; `followUp` ведёт к `zaKPfDQFGTR8FKju` («Compound Arm Fracture (Left - Treated)», `treated/leftArm`).

Этот Item отсекается начальным фильтром `treatment=none`, но доступен через ссылку предыдущего состояния. При контрольном `BODY.max=5` срок 10 дней независимо от штрафов к `BODY.value`. Изменений числовых полей не задано; текст/статусы рассматриваются отдельно.

В обеих none/treated bleed-object amount2, stabilized effects пуст. У правого stabilized location=rightLeg, остальные rightArm: переходы сохраняют поля нового шаблона. Это ошибка данных 00327, отдельная от ADD00328 и ожидания 00121. HTML использования руки не становится автоматическим запретом.

Сопоставленные определения и потребители: [module/data/item/criticalWoundData.js](../../../module/data/item/criticalWoundData.js.md), [module/actor/mixins/damageMixin.js](../../../module/actor/mixins/damageMixin.js.md), [module/actor/witcherActor.js](../../../module/actor/witcherActor.js.md), [module/activeEffect/witcherActiveEffect.js](../../../module/activeEffect/witcherActiveEffect.js.md), [templates/partials/crit-wounds-table.hbs](../../../templates/partials/crit-wounds-table.hbs.md), [packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Compound_Arm_Fracture__Left___Treated__zaKPfDQFGTR8FKju.json](Compound_Arm_Fracture__Left___Treated__zaKPfDQFGTR8FKju.json.md), [packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Compound_Arm_Fracture__Left__saPd4IMUCv5qZE60.json](Compound_Arm_Fracture__Left__saPd4IMUCv5qZE60.json.md).

[Протокол и границы](../../../../review-log.md#task-0004012) — TASK-0004.012; процессы [R012-16](../../../../cross-check-0002.md#r012-16). В этой порции выполнена статическая сверка; прежние опыты сохраняют свои даты и фасады. Новых поведенческих запусков нет; браузер, мир, сеть и запись в БД не запускались.
