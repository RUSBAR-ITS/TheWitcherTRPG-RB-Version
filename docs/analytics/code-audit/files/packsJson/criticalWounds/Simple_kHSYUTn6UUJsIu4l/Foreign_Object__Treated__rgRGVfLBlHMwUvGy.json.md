# packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Foreign_Object__Treated__rgRGVfLBlHMwUvGy.json

## Актуальный контракт — 14.3.1.00049

Шаблон criticalWound; существующие UUID, имя, описание, effects/changes/statuses/priority/transfer и папка сохранены. `followUp` и сохраняемый `healingTime` удалены. Новые данные управляют общими операциями, специальных правил по ID в коде нет.

| Поле | Значение |
| --- | --- |
| `woundTypeId` | `"foreign-object"` |
| `location` | `"torso"` |
| `treatment` | `"treated"` |
| `cannotStabilize` | `true` |
| `cannotTreat` | `true` |
| `canHeal` | `true` |
| `healingDuration` | `"max(8-@body,1)"` |
| `stabilizedWound` | `null` |
| `treatedWound` | `null` |
| `daysHealed` | `0` |
| `sterilized` | `false` |

Используется через [module/item/criticalWoundOperations.js](../../../../../../../module/item/criticalWoundOperations.js) и [module/data/item/criticalWoundData.js](../../../../../../../module/data/item/criticalWoundData.js). Цели с тем же ID/местом проверены; полный список — [матрица](../../../../../critical-wounds-content-matrix.md). JSON/сборка/установка сверены; [протокол](../../../../../task-0009-lifecycle-checks.md). Численный пересчёт эффектов остаётся TASK-0010. Старые датированные сведения ниже не описывают новые переходы.

| Поле | Значение |
| --- | --- |
| Исходный файл | [packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Foreign_Object__Treated__rgRGVfLBlHMwUvGy.json](../../../../../../../packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Foreign_Object__Treated__rgRGVfLBlHMwUvGy.json) |
| Тип файла | JSON: Item типа criticalWound |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-12 |
| Ветка и коммит | rusbar-main, 5283da15a49422fc339c44add4e7d7d02c174ce4 |
| Изменения относительно коммита | Нет; 37 строк; SHA-256 ed7eac25376f7bb6d02c699fb4c9a9362817b598c5c282f0d3a3f828113d3acb |
| Задача и порция | [TASK-0003.058](../../../../../../tasks/task-0003.058.md) |
| Запись перекрёстной сверки | [Протокол TASK-0003.058](../../../../review-log.md#task-0003058) |

## Назначение файла

Экспорт Foreign Object (Treated): документ травмы с состоянием `treated` и локацией `torso`. Содержит 0 ActiveEffect и 0 изменений. Разбор описывает структуру и работу потребителей; соответствие игровым правилам не проверяется.

## Условия использования

[system.json](../../../../../../../system.json) регистрирует Item-пакет `TheWitcherTRPG.criticalWounds` по пути `packs/criticalWounds.db`. [compilePack в packs.mjs](../../../../../../../utils/packs.mjs) рекурсивно читает экспортный каталог; [extractPack в extract.mjs](../../../../../../../utils/extract.mjs) записывает JSON с папками и исключением изменяемых временных меток. Команды определены в [package.json](../../../../../../../package.json); они не запускались. Экспортный каталог не загружается движком напрямую и не доказывает содержимое действующего пакета.

[module/setup/registerDataModels.js](../../../../../../../module/setup/registerDataModels.js) связывает типы criticalWound и base с CriticalWoundData и WitcherActiveEffectData. [module/setup/settings.js](../../../../../../../module/setup/settings.js) задаёт criticalWoundsPack. В автоматическом получении applyCritWound сначала отбирает treatment=none, затем location и criticalLevel; при нескольких кандидатах использует lesserEffect. Этот Item исключён из исходного выбора по treatment и используется через followUp или ручное добавление. Проверен индекс-фасад из настоящих очищенных моделей Simple, а не серверный индекс пакета.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| Foreign Object (Treated) | Корневой Item, name: 2, _id: 34 | Шаблон травмы | `rgRGVfLBlHMwUvGy`; UUID `Compendium.TheWitcherTRPG.criticalWounds.Item.rgRGVfLBlHMwUvGy` | Загрузка, копирование к Actor, подготовка, лечение и удаление |
| _key / folder / sort | Корневые поля | Идентификация экспортного документа и порядок | `"!items!rgRGVfLBlHMwUvGy"` / `"kHSYUTn6UUJsIu4l"` / `1500000` | Потребление ядром и инструментами экспорта; sort не задаёт приоритет изменений |
| img / flags / ownership / _stats | Корневые поля | Значок, права и история экспорта | `"icons/svg/item-bag.svg"`; flags=`{}`; ownership=`{"default":0,"ugXtPMJIktbl63QV":3}` | Иконка — ресурс ядра вне пофайлового анализа; ID владельца не доказывает существование такого пользователя в текущем мире |
| system | Объект, строка 5 | Модель травмы | criticalWound | Поля состояния перечислены ниже |
| effects | EmbeddedCollection, строка 19 | Собственные воздействия Item | 0 документов | При переносе Item остаются вложенными; активные transfer-эффекты собираются для Actor |

| Поле system | Экспортное значение | Проверенный потребитель и смысл |
| --- | --- | --- |
| htmlFields | `["description"]` | Устаревшая декларация текстовых полей; отсутствует в defineSchema и удалена очисткой модели. |
| description | `"<table class=\"NormalTable\"><tbody><tr><td style=\"border-left-style:none;border-bottom-style:none;border-right-style:none;border-top-style:none;\"><p><span class=\"fontstyle0\">You take a -2 to Recovery and a -1 to your Critical Healing.</span></p></td></tr></tbody></table>"` | HTMLField; enrichedText → createEnrichedText, редактор и сообщение получения травмы. Числа внутри HTML не становятся changes. |
| criticalLevel | `"simple"` | StringField; фильтр applyCritWound и ветвь calculateHealingTime. |
| treatment | `"treated"` | StringField; выбор исходной травмы и проверка treated в heal. |
| location | `"torso"` | StringField; отбор по локации и lookup подписи на листе. |
| lesserEffect | `true` | BooleanField; при нескольких кандидатах false для результата >4, true для ≤4. |
| daysHealed | `0` | NumberField; счётчик в heal; записывается через update либо удаляется Item. |
| healingTime | `0` | NumberField; у Item с Actor вычисляется Math.max(8 - BODY.max, 1). |
| sterilized | `false` | BooleanField; при heal с новой стерилизацией дополнительно +2 дня. |
| followUp | `null` | DocumentUUIDField типа Item; treat загружает адресата и инициирует замену. |

_stats: `{"compendiumSource":null,"duplicateSource":null,"exportSource":null,"coreVersion":"13.351","systemId":"TheWitcherTRPG","systemVersion":"AUTOMATICALLY REPLACED BY GITHUB WORKFLOW ACTION"}`. Метки версии — история экспорта, не результат текущей миграции. Поле system.description содержит приведённый выше HTML без ссылок UUID или исполняемого скрипта.

Вложенных ActiveEffect и changes нет. Условия из HTML не разбираются моделью как модификаторы; автоматический расчёт соответствующих штрафов из текста не установлен. Это граница автоматизации данных, а не вывод о соответствии рулбуку.

## Основные функции и методы

Собственных функций, классов и обработчиков JSON не вводит. Ниже указаны методы внешних потребителей; они не определены в этом JSON.

| Метод потребителя | Входы и предусловия | Результат и действия | Асинхронность и состояние |
| --- | --- | --- | --- |
| applyCritWound / addItem | Уровень, локация, индекс, UUID | Выбор документа, запрос добавления и чат | Совпадение name/type может вести к quantity вместо нового Item; [issue-00288](../../../../../../issues/closed/issue-00288.md) |
| CriticalWoundData.prepareDerivedData / calculateHealingTime | Item с родителем Actor | healingTime=max(8−BODY.max,1) | Вычисляемое поле; само не сохраняется |
| CriticalWoundData.treat | followUp либо null | При ссылке fromUuid → createEmbeddedDocuments; затем delete | Ожидает загрузку, не ожидает создание/удаление; [issue-00121](../../../../../../issues/closed/issue-00121.md) |
| CriticalWoundData.heal | sterilized, treatment, дни | treated: +1 день, впервые со стерилизацией +2; достижение healingTime → treat | update/treat не ожидаются; [issue-00127](../../../../../../issues/closed/issue-00127.md) |
| Actor.allApplicableEffects / applyActiveEffects | Активные transfer-эффекты Item | Отбор фазы и приоритета, применение через NumberField | Меняется подготовленная модель Actor, не исходный JSON |

## Используемые сущности и зависимости

| Сущность | Файл-источник или API | Вид связи | Место и цель | Доказательство |
| --- | --- | --- | --- | --- |
| criticalWounds | [system.json](../../../../../../../system.json) | Регистрация пакета | name/type/path и packFolders | Манифест, строки 28 и 52–56 |
| compilePack / extractPack | [utils/packs.mjs](../../../../../../../utils/packs.mjs), [utils/extract.mjs](../../../../../../../utils/extract.mjs) | Экспорт/сборка | Рекурсивный каталог и Folder | Статический разбор; без записи |
| ready / getIndex | [module/TheWitcherTRPG.js](../../../../../../../module/TheWitcherTRPG.js) | Подготовка индекса | ready:62–67 запрашивает system.criticalLevel, location, lesserEffect, treatment для выбранного пакета | Статическое чтение; серверный индекс не запускался |
| CriticalWoundData.defineSchema / treat | [module/data/item/criticalWoundData.js](../../../../../../../module/data/item/criticalWoundData.js) | Модель, ссылки и жизненный цикл | system и followUp | Реальная модель и перехваченные вызовы |
| registerDataModels | [module/setup/registerDataModels.js](../../../../../../../module/setup/registerDataModels.js) | Реестр типов | criticalWound и base | Строки 33, 52, 73 |
| WitcherItem.migrateData / migrateSpells | [module/item/witcherItem.js](../../../../../../../module/item/witcherItem.js) | Наследуемая миграция | Ветка Hexes/Rituals не затрагивает этот тип | Строки 12–27; BaseItem исполнен в сценарии |
| WitcherActiveEffectData.defineSchema | [module/data/activeEffects/witcherActiveEffectData.js](../../../../../../../module/data/activeEffects/witcherActiveEffectData.js) | Наследование схемы | super сохраняет system.changes, пять bool-флагов | Реальная модель для всех эффектов |
| WitcherActiveEffect.isSuppressed | [module/activeEffect/witcherActiveEffect.js](../../../../../../../module/activeEffect/witcherActiveEffect.js) | Подавление | Поля Item и четыре apply-флага | Реальный класс, active/target и контроль applySelf |
| CommonActorData / CharacterData | [module/data/actor/commonActorData.js](../../../../../../../module/data/actor/commonActorData.js) | Схема и базовая подготовка | Пути числовых модификаторов | Реальный CharacterData в BaseActor |
| WitcherActor.calculateStats / calculateFixedDerivedStats | [module/actor/witcherActor.js](../../../../../../../module/actor/witcherActor.js) | Расчёт после изменений | Характеристики и производные | Исполнены точные методы; вес и броня заданы нулём |
| BaseItem / BaseActiveEffect / NumberField | Foundry 14.367.0; /opt/foundryvtt/common/documents/item.mjs, documents/active-effect.mjs, data/active-effect.mjs, data/fields.mjs | Внешнее ядро | Очистка, миграция, DocumentUUIDField и вычисление изменения | Настоящие классы; строгая валидация |
| ActiveEffect.prepareBaseData / applyChange; Actor.applyActiveEffects | Foundry 14.367.0; /opt/foundryvtt/client/documents/active-effect.mjs и actor.mjs | Внешнее ядро | Приоритеты, фазы, поля, сбор effects | Реальные методы; фасад клиентского окружения |

## Известные потребители

| Файл-потребитель | Что использует | Способ и условия | Основание |
| --- | --- | --- | --- |
| [module/actor/mixins/damageMixin.js](../../../../../../../module/actor/mixins/damageMixin.js) | criticalLevel/treatment/location/lesserEffect, имя/описание | applyCritWound:312–345 | Проверены восемь исходных кандидатов Simple |
| [module/actor/witcherActor.js](../../../../../../../module/actor/witcherActor.js) | name/type и числовые поля Actor | addItem:259–273; calculateStats и производные | Реальные методы |
| [module/actor/sheets/mixins/criticalWoundMixin.js](../../../../../../../module/actor/sheets/mixins/criticalWoundMixin.js) | Item.uuid / system.treat | _onTreat:12–17 по кнопке | Статическая связь с шаблоном |
| [module/item/sheets/WitcherCriticalWoundSheet.js](../../../../../../../module/item/sheets/WitcherCriticalWoundSheet.js) | Item и followUp | _onDropItem:17–21 сохраняет item.uuid | Редактор, без проверки браузера |
| [templates/sheets/item/criticalWound-sheet.hbs](../../../../../../../templates/sheets/item/criticalWound-sheet.hbs) | system, name, image | Редактирование травмы и UUID | Статическое чтение шаблона |
| [templates/partials/crit-wounds-table.hbs](../../../../../../../templates/partials/crit-wounds-table.hbs) | system.location/treatment, дни и UUID | lookup подписи:18; кнопка лечения:36 | Статическое чтение шаблона |
| [module/actor/sheets/mixins/healMixin.js](../../../../../../../module/actor/sheets/mixins/healMixin.js) | system.heal | recoverActor:88 для всех criticalWound | Вызов без ожидания вложенных операций |

Поиск и проверенные маршруты не исключают внешние макросы, модули и динамические обращения. Текстовая таблица [Simple Critical](../../../../../../../packsJson/combat/Simple_Critical_SkHR3GrB2e3Tz1v4.json) не является источником этих Item для applyCritWound.

## Данные и изменения состояния

Папка: [Simple](_Folder.json.md). Прямые предшественники: [Foreign Object (Stabilized)](Foreign_Object__Stabilized__fnYssldrMLVqbF22.json.md). followUp=null: treat инициировал только удаление текущего Item. Создание/удаление возвращали удерживаемые Promise и не писали в мир. Удаление Item убирает его вложенные effects; следующий расчёт Actor собирает эффекты оставшихся Item. При переходе эффекты не редактируются в прежнем Item, загружается другой шаблон.

Контрольный Actor: все восемь характеристик unmodifiedMax=5, HP.value=25, броня/вес=0. Для этого документа получены BODY.value=5, BODY.max=5, SPD.value=5, RUN=15, LEAP=3, ENC=50, HP.max=25; healingTime=3. Все перечисленные changes дали соответствующие числовые суммы в целевых полях. Это расчёт без других эффектов, перегруза и ранений; BODY.max остаётся базовым, а totalModifiers меняет BODY.value и зависимые расчёты.

## Проверки и доказательства

[Протокол TASK-0003.058](../../../../review-log.md#task-0003058): структурно проверены 25 JSON / 2068 строк, уникальность корневых ID и _key среди 98 criticalWounds, принадлежность Folder, все 16 переходов и все 17 эффектов / 55 изменений. Изолированный Node 24.16.0 исполнил 672 утверждения: настоящие модели Foundry 14.367.0 и системы, применение числовых изменений, 24 вызова treat, шесть вариантов heal, восемь выборов исходных травм, сложение двух ног, disabled/transfer/suppression и повторный addItem. Для данного файла проверены его собственные значения; общая цифра относится ко всей порции.

## Непроверенные участки и открытые вопросы

Текущая сверка охватила исходник, описанные поля и конкретных потребителей; прежние результаты выше сохраняют даты своих опытов. HTML ограничения рук, зрения, спасбросков и протезов не исполняется автоматически. Наблюдаемые штрафы, повтор травмы, Deadly и лечебные бонусы не сверены с рулбуками; новая автоматизация и изменения условий требуют самостоятельного согласования. .017/.018 сохраняют технический охват. Границы: [U012-07](../../../../cross-check-0002.md#u012-07) и [U012-08](../../../../cross-check-0002.md#u012-08).

## Связанные проблемы

[issue-00121](../../../../../../issues/closed/issue-00121.md) — последовательность замены, [issue-00127](../../../../../../issues/closed/issue-00127.md) — граница завершения лечения, [issue-00288](../../../../../../issues/closed/issue-00288.md) — повторный одноимённый Item. Статусы potential сохранены; пользователь не подтверждал проблемы, исправления не выполнялись. Старый формат changes, default lesserEffect и пустые эффекты сами по себе новыми issues не объявлены.

## История актуализации

2026-09-12 — полное описание в TASK-0003.058 на указанном коммите; исходник не изменён. [Протокол TASK-0003.058](../../../../review-log.md#task-0003058) фиксирует доказательства и пределы проверки.

## Сквозная сверка TASK-0004.012

2026-09-14; rusbar-main, a853fc2ff721e5d33b2716081c657bd92d62d86b. Исходник совпадает со срезом TASK-0001; изменено только описание.

Item `rgRGVfLBlHMwUvGy` («Foreign Object (Treated)»): `simple/treated/torso`; 0 ActiveEffect, 0 changes. Предшественник: `fnYssldrMLVqbF22`; `followUp=null`: ручной `treat()` запрашивает удаление этого Item.

Этот Item отсекается начальным фильтром `treatment=none`, но доступен через ссылку предыдущего состояния. При контрольном `BODY.max=5` срок 3 дней независимо от штрафов к `BODY.value`. Изменений числовых полей не задано; текст/статусы рассматриваются отдельно.

Foreign Object описывает REC/лечение текстом и не содержит effects; none/stabilized рук тоже описывают ограничения без changes. Treated рук дают physique.activeEffectModifiers−1. Описание само не создаёт модификатор или условие выбора действия.

Сопоставленные определения и потребители: [module/data/item/criticalWoundData.js](../../../module/data/item/criticalWoundData.js.md), [module/actor/mixins/damageMixin.js](../../../module/actor/mixins/damageMixin.js.md), [module/actor/witcherActor.js](../../../module/actor/witcherActor.js.md), [module/activeEffect/witcherActiveEffect.js](../../../module/activeEffect/witcherActiveEffect.js.md), [templates/partials/crit-wounds-table.hbs](../../../templates/partials/crit-wounds-table.hbs.md), [packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Foreign_Object__Stabilized__fnYssldrMLVqbF22.json](Foreign_Object__Stabilized__fnYssldrMLVqbF22.json.md).

[Протокол и границы](../../../../review-log.md#task-0004012) — TASK-0004.012; процессы [R012-11](../../../../cross-check-0002.md#r012-11). В этой порции выполнена статическая сверка; прежние опыты сохраняют свои даты и фасады. Новых поведенческих запусков нет; браузер, мир, сеть и запись в БД не запускались.
