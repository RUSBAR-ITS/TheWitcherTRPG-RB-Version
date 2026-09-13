# packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Sprained_Leg__Left___Treated__f7NaW1AMnrSLGkd3.json

| Поле | Значение |
| --- | --- |
| Исходный файл | [packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Sprained_Leg__Left___Treated__f7NaW1AMnrSLGkd3.json](../../../../../../../packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Sprained_Leg__Left___Treated__f7NaW1AMnrSLGkd3.json) |
| Тип файла | JSON: Item типа criticalWound |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-12 |
| Ветка и коммит | rusbar-main, 5283da15a49422fc339c44add4e7d7d02c174ce4 |
| Изменения относительно коммита | Нет; 92 строк; SHA-256 f07ba37aa2c2251d23948ef4608867e7620836351f537427e4b3ca8a0147025d |
| Задача и порция | [TASK-0003.058](../../../../../../tasks/task-0003.058.md) |
| Запись перекрёстной сверки | [Протокол TASK-0003.058](../../../../review-log.md#task-0003058) |

## Назначение файла

Экспорт Sprained Leg (Left - Treated): документ травмы с состоянием `treated` и локацией `leftArm`. Содержит 1 ActiveEffect и 1 изменений. Разбор описывает структуру и работу потребителей; соответствие игровым правилам не проверяется.

## Условия использования

[system.json](../../../../../../../system.json) регистрирует Item-пакет `TheWitcherTRPG.criticalWounds` по пути `packs/criticalWounds.db`. [compilePack в packs.mjs](../../../../../../../utils/packs.mjs) рекурсивно читает экспортный каталог; [extractPack в extract.mjs](../../../../../../../utils/extract.mjs) записывает JSON с папками и исключением изменяемых временных меток. Команды определены в [package.json](../../../../../../../package.json); они не запускались. Экспортный каталог не загружается движком напрямую и не доказывает содержимое действующего пакета.

[module/setup/registerDataModels.js](../../../../../../../module/setup/registerDataModels.js) связывает типы criticalWound и base с CriticalWoundData и WitcherActiveEffectData. [module/setup/settings.js](../../../../../../../module/setup/settings.js) задаёт criticalWoundsPack. В автоматическом получении applyCritWound сначала отбирает treatment=none, затем location и criticalLevel; при нескольких кандидатах использует lesserEffect. Этот Item исключён из исходного выбора по treatment и используется через followUp или ручное добавление. Проверен индекс-фасад из настоящих очищенных моделей Simple, а не серверный индекс пакета.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| Sprained Leg (Left - Treated) | Корневой Item, name: 3, _id: 89 | Шаблон травмы | `f7NaW1AMnrSLGkd3`; UUID `Compendium.TheWitcherTRPG.criticalWounds.Item.f7NaW1AMnrSLGkd3` | Загрузка, копирование к Actor, подготовка, лечение и удаление |
| _key / folder / sort | Корневые поля | Идентификация экспортного документа и порядок | `"!items!f7NaW1AMnrSLGkd3"` / `"kHSYUTn6UUJsIu4l"` / `2400000` | Потребление ядром и инструментами экспорта; sort не задаёт приоритет изменений |
| img / flags / ownership / _stats | Корневые поля | Значок, права и история экспорта | `"icons/svg/item-bag.svg"`; flags=`{}`; ownership=`{"default":0,"ugXtPMJIktbl63QV":3}` | Иконка — ресурс ядра вне пофайлового анализа; ID владельца не доказывает существование такого пользователя в текущем мире |
| system | Объект, строка 6 | Модель травмы | criticalWound | Поля состояния перечислены ниже |
| effects | EmbeddedCollection, строка 20 | Собственные воздействия Item | 1 документов | При переносе Item остаются вложенными; активные transfer-эффекты собираются для Actor |

| Поле system | Экспортное значение | Проверенный потребитель и смысл |
| --- | --- | --- |
| htmlFields | `["description"]` | Устаревшая декларация текстовых полей; отсутствует в defineSchema и удалена очисткой модели. |
| description | `""` | HTMLField; enrichedText → createEnrichedText, редактор и сообщение получения травмы. Числа внутри HTML не становятся changes. |
| criticalLevel | `"simple"` | StringField; фильтр applyCritWound и ветвь calculateHealingTime. |
| treatment | `"treated"` | StringField; выбор исходной травмы и проверка treated в heal. |
| location | `"leftArm"` | StringField; отбор по локации и lookup подписи на листе. |
| lesserEffect | `false` | BooleanField; при нескольких кандидатах false для результата >4, true для ≤4. |
| daysHealed | `0` | NumberField; счётчик в heal; записывается через update либо удаляется Item. |
| healingTime | `0` | NumberField; у Item с Actor вычисляется Math.max(8 - BODY.max, 1). |
| sterilized | `false` | BooleanField; при heal с новой стерилизацией дополнительно +2 дня. |
| followUp | `null` | DocumentUUIDField типа Item; treat загружает адресата и инициирует замену. |

_stats: `{"compendiumSource":null,"duplicateSource":null,"exportSource":null,"coreVersion":"13.351","systemId":"TheWitcherTRPG","systemVersion":"AUTOMATICALLY REPLACED BY GITHUB WORKFLOW ACTION"}`. Метки версии — история экспорта, не результат текущей миграции. Поле system.description пустое.

### ActiveEffect 1: Sprained Leg (Right)

_ID `6VnddvqR8bg7Tzup`; origin=`"Item.1AxybnKTfdd6Tb8B"`. Тип `base`, disabled=false, transfer=true; img=`"icons/svg/item-bag.svg"`, tint=`"#ffffff"`, sort=0, statuses=`[]`, description=`""`. Флаги: `{"statuscounter":{"value":1,"config":{"type":"default"},"visible":false}}`. _stats: `{"compendiumSource":null,"duplicateSource":null,"exportSource":null,"coreVersion":"13.351","systemId":"TheWitcherTRPG","systemVersion":"AUTOMATICALLY REPLACED BY GITHUB WORKFLOW ACTION"}`.

Системные поля до миграции: `{"applySelf":false,"applyOnTarget":false,"applyOnHit":false,"applyOnDamage":false}`. applyAfterCalculations отсутствует и получает false. Все изменения после миграции находятся в system.changes, type=add, value — число, phase=initial; при prepareBaseData null-приоритет становится 20, явно заданный 0 сохраняется. Старая duration=`{"startTime":null,"combat":null,"seconds":null,"rounds":null,"turns":null,"startRound":null,"startTurn":null}` преобразуется в start=null и duration={value:null, units:"seconds", expiry:null, expired:false}; после prepareBaseData value=Infinity. Истечение по таймеру не задано. Полный updateDuration/registry в сценарии не запускался.

| № / строка key | Ключ изменения | Исходные mode / value / priority | После миграции и подготовки | Схема назначения |
| --- | --- | --- | --- | --- |
| 1 / 45 | `system.stats.spd.totalModifiers` | 2 / `"-1"` / `0` | add; -1; priority=0; phase=initial | NumberField; [statData.js](../../../../../../../module/data/actor/templates/common/stats/statData.js) |

origin ссылается на мировой Item: его наличие не проверялось. Это не followUp и не указатель цели применения; целевой Actor определяется владельцем Item и transfer. Повторение ID эффекта в разных Item не является коллизией внутри одной EmbeddedCollection. Флаг statuscounter принадлежит внешнему модулю; его интерфейс и сохранение не проверялись. В изолированном окружении без регистрации этого модуля ядро очищает его flags; это не объявлено потерей флагов в действующем мире.

## Основные функции и методы

Собственных функций, классов и обработчиков JSON не вводит. Ниже указаны методы внешних потребителей; они не определены в этом JSON.

| Метод потребителя | Входы и предусловия | Результат и действия | Асинхронность и состояние |
| --- | --- | --- | --- |
| applyCritWound / addItem | Уровень, локация, индекс, UUID | Выбор документа, запрос добавления и чат | Совпадение name/type может вести к quantity вместо нового Item; [issue-00288](../../../../../../issues/potential/issue-00288.md) |
| CriticalWoundData.prepareDerivedData / calculateHealingTime | Item с родителем Actor | healingTime=max(8−BODY.max,1) | Вычисляемое поле; само не сохраняется |
| CriticalWoundData.treat | followUp либо null | При ссылке fromUuid → createEmbeddedDocuments; затем delete | Ожидает загрузку, не ожидает создание/удаление; [issue-00121](../../../../../../issues/potential/issue-00121.md) |
| CriticalWoundData.heal | sterilized, treatment, дни | treated: +1 день, впервые со стерилизацией +2; достижение healingTime → treat | update/treat не ожидаются; [issue-00127](../../../../../../issues/potential/issue-00127.md) |
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

Папка: [Simple](_Folder.json.md). Прямые предшественники: [Sprained Leg (Left - Stabilized)](Sprained_Leg__Left___Stabilized__eblucqnyOS7lb5E5.json.md). followUp=null: treat инициировал только удаление текущего Item. Создание/удаление возвращали удерживаемые Promise и не писали в мир. Удаление Item убирает его вложенные effects; следующий расчёт Actor собирает эффекты оставшихся Item. При переходе эффекты не редактируются в прежнем Item, загружается другой шаблон.

Контрольный Actor: все восемь характеристик unmodifiedMax=5, HP.value=25, броня/вес=0. Для этого документа получены BODY.value=5, BODY.max=5, SPD.value=4, RUN=12, LEAP=2, ENC=50, HP.max=25; healingTime=3. Все перечисленные changes дали соответствующие числовые суммы в целевых полях. Это расчёт без других эффектов, перегруза и ранений; BODY.max остаётся базовым, а totalModifiers меняет BODY.value и зависимые расчёты.

Несоответствие локации: оба предшественника имеют leftLeg, этот Item — leftArm. Шаблон списка выводит подпись по полю, а не по имени. Штраф SPD остаётся тем же, поскольку путь changes от location не зависит. См. [issue-00325](../../../../../../issues/potential/issue-00325.md).

## Проверки и доказательства

[Протокол TASK-0003.058](../../../../review-log.md#task-0003058): структурно проверены 25 JSON / 2068 строк, уникальность корневых ID и _key среди 98 criticalWounds, принадлежность Folder, все 16 переходов и все 17 эффектов / 55 изменений. Изолированный Node 24.16.0 исполнил 672 утверждения: настоящие модели Foundry 14.367.0 и системы, применение числовых изменений, 24 вызова treat, шесть вариантов heal, восемь выборов исходных травм, сложение двух ног, disabled/transfer/suppression и повторный addItem. Для данного файла проверены его собственные значения; общая цифра относится ко всей порции.

## Непроверенные участки и открытые вопросы

Полный клиент, браузер, серверный индекс, БД packs/, фактические записи/ошибки записи, все разновидности Actor и модули не проверены. В сценарии использован BaseItem с настоящей CriticalWoundData, не полный WitcherItem; его миграция сопоставлена статически. Реальный WitcherActiveEffect загружен с фасадом ClientDocumentMixin и registry; prepareBaseData и изменения выполнены, автоматический цикл подготовки/истечения клиента не запускался целиком. fromUuid, индекс, чат, create/update/delete и броня/вес представлены явно заданными фасадами. Игровые числа и формулировки не сверялись с книгами. Успешное локальное чтение не доказывает HTTP-доступ службы.

## Связанные проблемы

[issue-00121](../../../../../../issues/potential/issue-00121.md) — последовательность замены, [issue-00127](../../../../../../issues/potential/issue-00127.md) — граница завершения лечения, [issue-00288](../../../../../../issues/potential/issue-00288.md) — повторный одноимённый Item. [issue-00325](../../../../../../issues/potential/issue-00325.md) — собственное поле location. Статусы potential сохранены; пользователь не подтверждал проблемы, исправления не выполнялись. Старый формат changes, default lesserEffect и пустые эффекты сами по себе новыми issues не объявлены.

## История актуализации

2026-09-12 — полное описание в TASK-0003.058 на указанном коммите; исходник не изменён. [Протокол TASK-0003.058](../../../../review-log.md#task-0003058) фиксирует доказательства и пределы проверки.

## Уточнение TASK-0003.059

2026-09-13 — исправлен номер строки корневого _id в таблице сущностей: ранее указывал на вложенный ActiveEffect. Сам ID, связи и выводы о поведении не изменены; исходный JSON сохранён. [Перекрёстная сверка](../../../../review-log.md#task-0003059).
