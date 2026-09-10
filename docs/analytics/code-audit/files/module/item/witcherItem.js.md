# module/item/witcherItem.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/item/witcherItem.js](../../../../../../module/item/witcherItem.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `c5edcbadd05ff4038a174bd2e2a49785e40ea878` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.008](../../../../../tasks/task-0003.008.md), одна порция из двух файлов |
| Запись перекрёстной сверки | [TASK-0003.008](../../../review-log.md#task-0003008) |

## Назначение файла

Документ WitcherItem поверх Foundry Item: миграция двух старых классов магии, выбор варианта атаки, подготовка списка алхимических веществ, изготовление по рецепту, замена генератора добычи результатами RollTable и применение перенесённых улучшений к данным Item. Подключает пять примесей действий. Схему system выбирает реестр моделей по типу Item.

## Условия использования

[module/TheWitcherTRPG.js](../../../../../../module/TheWitcherTRPG.js) импортирует класс (11) и в init назначает `CONFIG.Item.documentClass = WitcherItem` (32). При выполнении модуля определяется класс, затем пять Object.assign дополняют прототип; изготовление, броски и обновления от одного импорта не запускаются. Прямых Hooks в файле нет.

Класс один для Item в мировой коллекции, компедиуме и у Actor. Ядро Foundry 14.367.0 `/opt/foundryvtt/client/documents/item.mjs:32–34` возвращает `item.actor = parent`, только если parent — экземпляр Actor, иначе null. `system.parent` у модели — Item, а `item.parent` у встроенного предмета — Actor. realCraft, успешная ветка генератора добычи и многие примеси требуют владельца Actor; самостоятельный Item не получает его автоматически. Без Actor можно выбирать атаку, мигрировать источник, читать модель и применять улучшение к самому предмету, если соблюдены остальные предусловия.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| WitcherItem | Класс 10–370 | Документ и собственные действия | default export; CONFIG.Item.documentClass | Создаётся ядром, использует system/effects/actor/uuid |
| migrateData, migrateSpells | Два static, 12–26 | Замена типа Hexes/Rituals | Через класс | Меняют переданный source до делегирования ядру |
| getItemAttack, isConsumable, isAlchemicalCraft, alchemyCraftComponentsList, enrichedText | Метод/геттеры, 28–174 | Выбор атаки и представление модели | Через экземпляр | Чтение; список веществ создаётся заново |
| AlchemyComponent | Локальный класс, 81–93 | Строка списка алхимии | Доступен только внутри getter | Поля name, alias, content, quantity и constructor; 9 новых экземпляров |
| realCraft, checkIfItemHasRollTable | Async методы, 181–315 | Изготовление и генерация добычи | Вызовы из листов Actor | Инициируют удаление/добавление/обновление Item и сообщения |
| prepareEmbeddedDocuments, allApplicableEffects, applyActiveEffects | Метод, generator, метод; 321–369 | Подготовка и применение улучшений | Жизненный цикл документа | Читают effects, меняют подготовленные значения и overrides |
| consumeMixin | Импорт и Object.assign, 372 | Присоединяет 2 методов | Прототип WitcherItem | Определения перечислены ниже; не означают вызов |
| repairMixin | Импорт и Object.assign, 373 | Присоединяет 2 методов | Прототип WitcherItem | Определения перечислены ниже; не означают вызов |
| dismantlingMixin | Импорт и Object.assign, 374 | Присоединяет 3 методов | Прототип WitcherItem | Определения перечислены ниже; не означают вызов |
| damageUtilMixin | Импорт и Object.assign, 375 | Присоединяет 3 методов | Прототип WitcherItem | Определения перечислены ниже; не означают вызов |
| defenseOptionMixin | Импорт и Object.assign, 376 | Присоединяет 1 методов | Прототип WitcherItem | Определения перечислены ниже; не означают вызов |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| WitcherItem.migrateData; 12–16 | source объекта документа | Результат super.migrateData(source) | Вызывает this.migrateSpells(source), затем ядро | Синхронно; миграция в памяти, не update БД |
| WitcherItem.migrateSpells; 18–26 | source.system?.class | undefined | Hexes → source.type='hex'; Rituals → 'ritual'; остальные без изменения | Не ограничивает исходный source.type; system.class не удаляет |
| WitcherItem.getItemAttack; 28–70 | options по умолчанию {alt:false,ctrl:false,shift:false}; attackOptions как Set | {attackOption, skill, alias, itemUuid}; без поля attackOptions — только none и uuid | Порядок Set и клавиши выбирают индекс; skill из system[attackOption+'AttackSkill']; alias из WITCHER.skillMap[skill]?.label | Синхронно; пустой Set возвращает undefined для option/skill/alias, не none; null options при существующем Set не поддержан |
| WitcherItem.isConsumable; 72–74 | system.isConsumable | Значение поля или false по ?? | Не определяет допустимые типы Item | Getter; отсутствующее поле не является ошибкой |
| WitcherItem.isAlchemicalCraft; 76–78 | system.alchemyDC | alchemyDC && alchemyDC > 0 | Выбирает алхимический путь realCraft | Не строго boolean: при 0 → 0, при отсутствии → undefined |
| WitcherItem.alchemyCraftComponentsList; 80–170 | system.alchemyComponents; i18n | 9 AlchemyComponent в фиксированном порядке | Локализует имя и собирает HTML картинки/исходного значения; quantity положительное либо 0 | Не фильтрует нули; отрицательное исходное число остаётся в HTML; отсутствие alchemyComponents вызывает ошибку |
| AlchemyComponent.constructor; 87–92 | name, alias, content, quantity | Новый объект четырёх полей | Присваивает аргументы полям с начальными '', '', '', 0 | Локальное создание, без документа |
| WitcherItem.enrichedText; 172–174 | Необязательный system.enrichedText | Promise результата модели или undefined | await this.system.enrichedText?.() | Не обогащает текст самостоятельно; исключение модели передаётся вызывающему |
| WitcherItem.realCraft; 181–250 | rollFormula, messageData с flavor/system, config; this.actor; модель рецепта | Promise<undefined> | extendedRoll с showResult=false; проверка/списание компонентов при успехе; fromUuid результата; addItem; toMessage | Ожидает Roll/fromUuid, не ожидает removeItem/addItem/toMessage; не возвращает boolean результата; config/messageData меняются |
| WitcherItem.checkIfItemHasRollTable; 257–315 | newQuantity; таблица по имени в game.packs; Actor для найденной таблицы | false при отсутствии; true после цикла/удаления генератора; в ошибочных ветках результат notifications.error | Для каждого шага roll берёт results[0], загружает Item из pack, создаёт/увеличивает количество; шепчет GM; удаляет генератор | getDocument/roll/getIndex/create/delete ожидаются; update существующей стопки и ChatMessage.create не ожидаются; ошибки не перехватывает |
| WitcherItem.prepareEmbeddedDocuments; 321–324 | Контекст Item | undefined | super.prepareEmbeddedDocuments(), затем this.applyActiveEffects() | Синхронная подготовка; не запись игровых документов |
| WitcherItem.allApplicableEffects; 331–335 | this.effects | Generator эффектов с truthy isAppliedTemporaryItemImprovement | Проверяет признак system.isTransferred через WitcherActiveEffect | Сам не проверяет disabled/active/type/transfer; active проверяется следующим методом |
| WitcherItem.applyActiveEffects; 342–369 | Применимые активные эффекты с system.changes | undefined; this.overrides | Клонирует changes, дописывает effect и недостающий priority, сортирует, пропускает пустой key, вызывает effect.apply и expandObject | Меняет вычисленные данные; сбрасывает overrides каждым вызовом; нет phase/shouldApplyChange, replacementData, try/catch или записи source |

### Выбор варианта атаки

Если все значения `Object.values(options)` ложны либо Set содержит меньше двух элементов, индекс 0. Иначе приоритет клавиш ctrl → alt → shift с индексами 3 → 2 → 1; индекс ограничивается `size - 1`. Это позиции в Set, а не жёсткое соответствие «alt = магия». При двух вариантах ctrl выбирает второй. Постороннее truthy поле options без клавиш может оставить индекс undefined/NaN; наличие таких данных у конкретного вызова требуется проверять отдельно. В [module/actor/mixins/weaponAttackMixin.js](../../../../../../module/actor/mixins/weaponAttackMixin.js) getItemAttack вызывается в строке 30; skillReplacement заменяет skill/alias в 31–34, проверка отсутствующего skill останавливает атаку в 36–38.

### Изготовление

`realCraft` сначала вызывает [module/scripts/rolls/extendedRoll.js](../../../../../../module/scripts/rolls/extendedRoll.js), затем считает успех как `roll.total > config.threshold`, независимо от reversal/defense. В текущих потребителях обе настройки false. При наличии associatedItem.name выбирает положительные компоненты: алхимия → девять веществ и Actor.getSubstance; обычный рецепт → craftingComponents и Actor.findNeededComponent. Для каждого требования набирает count из стопок с Number(quantity), ограничивая остаток через Math.min. Остаток != 0 отменяет локальный result и выдаёт уведомление. Списание и создание происходят только при локальном result=true. При отсутствии associatedItem.name компоненты не обрабатываются, в сообщение добавляется SuccessfulCraftForNothing.

Каждое требование резервируется отдельно; глобального резерва по id между строками нет. Наличие/обработка повторяющихся требований не проверялись. Списание при неуспешном броске отсутствует; соответствие правилам отдельно не утверждается. Если UUID результата перестал разрешаться после подготовки associatedItem, защиты до списания нет. Контракт отмены, одновременные действия игроков и транзакционность не реализуются самим этим методом.

### Генерация добычи

Поиск идёт в уже имеющихся `index` компедиумов типа RollTable с точным совпадением имени Item. Мировые `game.tables` не используются, несмотря на комментарий. getIndex для таблиц здесь не вызывается. Один найденный pack → getName(...)._id; несколько таблиц с тем же именем внутри одного pack не обнаруживаются как неоднозначность. При нескольких pack с совпадением возвращается уведомление.

Цикл `i < newQuantity` не нормализует аргумент: при 0/отрицательном числе шагов нет, но найденный генератор всё равно удаляется; при положительной дроби фактически выполняется ceil шагов. Берётся только первый результат каждого броска. Обрабатываются ссылки на документы компедиумов через legacy documentCollection/documentId; самостоятельные документы мира и текстовые результаты не разрешаются этим путём. Тип genItem явно не проверяется. Новая стопка создаётся из документа с его собственным quantity, существующая увеличивается на 1. Сопоставление — name+type, без isStored; getName и find зависят от коллекций Foundry.

Ядро 14.367 поддерживает legacy getters documentCollection/documentId и getChatText с предупреждениями совместимости: `/opt/foundryvtt/common/documents/table-result.mjs:102–123`, `/opt/foundryvtt/client/documents/table-result.mjs:120–124`. Само наличие старых имён не доказывает поломку. `/opt/foundryvtt/client/documents/roll-table.mjs:264–332` допускает пустой массив и несколько результатов. .roll не равнозначен .draw с отметкой drawn; состояние извлечения система здесь отдельно не сохраняет.

### Примеси: точный состав прототипа

| Порядок | Файл и объект | Подключённые определения | Граница ответственности |
| --- | --- | --- | --- |
| 1 | [consumeMixin](../../../../../../module/item/mixins/consumeMixin.js) | `consume`, `createConsumeMessage` | Расходник: лечение/статусы/эффекты и сообщение |
| 2 | [repairMixin](../../../../../../module/item/mixins/repairMixin.js) | `repair`, `restoreReliability` | Делегирование RepairSystem.process/restoreReliability |
| 3 | [dismantlingMixin](../../../../../../module/item/mixins/dismantlingMixin.js) | `canBeDismantled`, `dismantle`, `createDismantleMessage` | Разбор через связанный рецепт, выдача компонентов и сообщение |
| 4 | [damageUtilMixin](../../../../../../module/item/mixins/damageUtilMixin.js) | `createBaseDamageObject`, `rollDamage`, `createVariableDamageDialog` | Объект урона, бросок урона и диалог переменной формулы |
| 5 | [defenseOptionMixin](../../../../../../module/item/mixins/defenseOptionMixin.js) | `createDefenseOption` | Label/value предмета и делегирование system.createDefenseOption |

11 имён примесей уникальны и не перекрывают 10 собственных определений прототипа; ещё два собственных метода статические. `restoreReliability` вызывается динамически маршрутизатором Queries. RollConfig импортирован, но в witcherItem.js используется только в JSDoc; здесь он не создаётся.

### Эффекты Item и отличие от Actor

Общий prepareData ядра (`client/documents/abstract/client-document.mjs:313–319`) вызывает system.prepareBaseData → Item.prepareBaseData → Item.prepareEmbeddedDocuments → system.prepareDerivedData → Item.prepareDerivedData. Системный обработчик запускается внутри embedded-этапа после super, до производной подготовки модели. В отличие от [разобранного Actor](../actor/witcherActor.js.md), у него нет проходов initial/final. Все активные changes применяются здесь независимо от phase и applyAfterCalculations; при повторном ручном вызове applyActiveEffects базовые данные сам метод не восстанавливает.

[module/activeEffect/witcherActiveEffect.js](../../../../../../module/activeEffect/witcherActiveEffect.js) определяет isAppliedTemporaryItemImprovement как system.isTransferred, а не type или effect.transfer. Его isSuppressed учитывает isActive/equipped у родителя и applySelf/applyOnTarget/applyOnHit/applyOnDamage; core active учитывает disabled и isSuppressed. Затем старый instance `ActiveEffect.apply` вызывает static applyChange в ядре (1069–1072); это ещё действующий совместимый API. Настоящие подготовленные эффекты получают defaultPriority по change.type в core prepareBaseData:263–271; fallback `mode * 10` у Item не означает, что все современные changes сортируются с NaN. Замены @-данных Item в этот вызов явно не передаются.

Источник улучшения создаётся через [module/item/sheets/configurations/WitcherConfigurationSheet.js](../../../../../../module/item/sheets/configurations/WitcherConfigurationSheet.js) и [templates/partials/effect-part.hbs](../../../../../../templates/partials/effect-part.hbs). [module/actor/mixins/temporaryEffectMixin.js](../../../../../../module/actor/mixins/temporaryEffectMixin.js) выбирает оружие, копирует эффект, задаёт isTransferred=true и создаёт ActiveEffect на оружии. В этом соседнем передатчике объект system заменяется целиком и changes теряются — issue-00042. Пустой результат передачи и арифметика уже корректно заполненного Item-эффекта проверялись отдельно; успешный расчёт в изоляции не означает, что передатчик формирует такое содержимое.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| extendedRoll | [module/scripts/rolls/extendedRoll.js](../../../../../../module/scripts/rolls/extendedRoll.js) | Импорт/await | realCraft:186; вычисляет Roll, config успеха и меняет messageData | Определение 9–112 прочитано; оригинальная функция исполнена с контролируемым Roll |
| RollConfig | [module/scripts/rollConfig.js](../../../../../../module/scripts/rollConfig.js) | Импорт для JSDoc | Тип config у realCraft:179; нет new RollConfig в этом файле | Сверены обращение и поля constructor |
| WITCHER.skillMap | [module/setup/config.js](../../../../../../module/setup/config.js) | Импорт/lookup | getItemAttack:67 возвращает label как ключ локализации | Прямой доступ; проверены выбор и неизвестное значение |
| Пять объектов *Mixin | [consumeMixin](../../../../../../module/item/mixins/consumeMixin.js), [repairMixin](../../../../../../module/item/mixins/repairMixin.js), [dismantlingMixin](../../../../../../module/item/mixins/dismantlingMixin.js), [damageUtilMixin](../../../../../../module/item/mixins/damageUtilMixin.js), [defenseOptionMixin](../../../../../../module/item/mixins/defenseOptionMixin.js) | Импорт/Object.assign | 372–376, полный перечень выше | Определения всех 11 имён сверены; полный разбор файлов отложен |
| Item; Item.create | Foundry 14.367.0, client/documents/item.mjs и ClientDocumentMixin | Наследование, lifecycle, запись | super.migrateData, super.prepareEmbeddedDocuments, actor; создание добычи:287 | Прочитаны используемые участки ядра; создание заменено в сценарии |
| CommonItemData и специализированные модели | [module/data/item/commonItemData.js](../../../../../../module/data/item/commonItemData.js); [module/setup/registerDataModels.js](../../../../../../module/setup/registerDataModels.js) | Доступ через system | isConsumable; данные рецепта/атаки; свойства модели | Общая схема разобрана полностью; специализированные связи точечно |
| attackOptions() | [module/data/item/templates/combat/attackOptionsData.js](../../../../../../module/data/item/templates/combat/attackOptionsData.js) | Схема данных | SetField и четыре *AttackSkill для getItemAttack | Включён в [module/data/item/weaponData.js](../../../../../../module/data/item/weaponData.js) и [module/data/item/spellData.js](../../../../../../module/data/item/spellData.js) |
| DiagramData / craftingComponent | [module/data/item/diagramData.js](../../../../../../module/data/item/diagramData.js); [module/data/item/templates/craftingComponentData.js](../../../../../../module/data/item/templates/craftingComponentData.js) | Схема/подготовка данных | alchemyDC, craftingComponents, alchemyComponents, resultQuantity, associatedItemUuid; associatedItem через fromUuidSync | Прочитаны определения 6–64 и фабрика компонентов |
| Actor.getSubstance, findNeededComponent | [module/actor/mixins/craftingMixin.js](../../../../../../module/actor/mixins/craftingMixin.js) | Вызов | realCraft:201–202 ищет компоненты; getSubstance исключает stored, findNeededComponent собственного фильтра stored не имеет | Проверены обе функции |
| Actor.removeItem, addItem; items | [module/actor/witcherActor.js](../../../../../../module/actor/witcherActor.js) | Вызов/коллекция | realCraft:236/242; loot:285/309 | Карточки сверены; оригинальные методы Actor ожидают свои операции, вызывающий Item — нет |
| Модель.enrichedText | [module/data/item/raceData.js](../../../../../../module/data/item/raceData.js); [module/data/item/professionData.js](../../../../../../module/data/item/professionData.js); [module/data/item/criticalWoundData.js](../../../../../../module/data/item/criticalWoundData.js) | Необязательное делегирование | enrichedText:172–174 | Прямой поиск реализаций; они используют [createEnrichedText](../../../../../../module/data/dataUtils.js) |
| WitcherActiveEffect getters; apply | [module/activeEffect/witcherActiveEffect.js](../../../../../../module/activeEffect/witcherActiveEffect.js); Foundry client/documents/active-effect.mjs | Фильтрация/вызов | allApplicableEffects/applyActiveEffects | Исходные getters и apply/applyChangeField проверены отдельно |
| deepClone, expandObject | Foundry common/utils/helpers.mjs | Вызов | 351/368; копия изменений и структура overrides | Реальные utils; для expandObject в vm вход приведён к обычному объекту другого контекста |
| game.packs; RollTable.roll; TableResult; fromUuid | Foundry CompendiumCollection, RollTable и UUID API | Поиск/загрузка | 241; 259–276; 301 | Статика плюс контролируемые документы в сценариях; pack БД не открывались |
| game.i18n.localize; ui.notifications; game.user/users; ChatMessage.create | Foundry client API | Локализация, уведомления, чат | Алхимия, изготовление и сообщения GM о добыче | Проверены ключи/поля и вызовы; внешние действия подменены |
| Картинки веществ и ключи Inventory.* | systems/TheWitcherTRPG/assets/images/{vitriol,rebis,aether,quebrith,hydragenum,vermilion,sol,caelum,fulgur}.png; [lang/en.json](../../../../../../lang/en.json) / [lang/ru.json](../../../../../../lang/ru.json) | Ресурс/локализация | AlchemyComponent.content/alias; 98–167 | Пути прочитаны; assets вне границ пофайлового анализа; HTTP не проверялся |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/TheWitcherTRPG.js](../../../../../../module/TheWitcherTRPG.js) | WitcherItem | Импорт/регистрация класса при init; 11/32 | Карточка точки входа дополнена |
| [module/actor/sheets/mixins/itemMixin.js](../../../../../../module/actor/sheets/mixins/itemMixin.js) | WitcherItem; inherited create/update | instanceof в _onDropItem:11; Item.create для добавления, update полей | Прослежены границы документа и его модели |
| [module/actor/witcherActor.js](../../../../../../module/actor/witcherActor.js) | isConsumable, consume; system.calcWeight | useItem:225–243 выбирает weapon/spell/consumable, getTotalWeight:245–248 читает модель | Двусторонняя сверка карточки Actor |
| [module/actor/mixins/weaponAttackMixin.js](../../../../../../module/actor/mixins/weaponAttackMixin.js) | getItemAttack | weaponAttack:30; затем проверка/замена skill | Оригинальный потребитель прочитан точечно |
| [module/actor/mixins/castSpellMixin.js](../../../../../../module/actor/mixins/castSpellMixin.js) | getItemAttack | castSpell:240 создаёт данные attack без options | Проверено обращение; вся магия не разобрана |
| [module/actor/sheets/WitcherCharacterSheet.js](../../../../../../module/actor/sheets/WitcherCharacterSheet.js) | isAlchemicalCraft, realCraft; отсутствующий populateAlchemyCraftComponentsList | _alchemyCraft:258–349 и _craftingCraft:354–439; realCraft:336/424 | Определения сверены; изолированно воспроизведена ошибка интерфейсного вызова |
| [module/actor/sheets/WitcherMonsterSheet.js](../../../../../../module/actor/sheets/WitcherMonsterSheet.js) | checkIfItemHasRollTable | Экспорт добычи:190–209; await внутри async forEach; если falsy — update quantity | Прочитан потребитель; полный экспорт/Actor.create не запускался |
| [module/setup/queries.js](../../../../../../module/setup/queries.js) | restoreReliability из repairMixin | Whitelist:29; вызов entity[function] и entity.system[function]:41–42 | Исследован прямой и динамический маршрут; issue-00008 остаётся |
| [module/item/sheets/WitcherItemSheet.js](../../../../../../module/item/sheets/WitcherItemSheet.js) | Документ/system | _prepareContext:45–58; вызывает system.enrichedText?.() напрямую, не обёртку Item | Проверено отличие двух API |
| [module/actor/mixins/temporaryEffectMixin.js](../../../../../../module/actor/mixins/temporaryEffectMixin.js) | effects будущего WitcherItem | createEmbeddedDocuments('ActiveEffect') на выбранном weapon:46 | Источник system.isTransferred; обнаружена потеря changes |
| [module/item/sheets/configurations/WitcherConfigurationSheet.js](../../../../../../module/item/sheets/configurations/WitcherConfigurationSheet.js) | effects, isAppliedTemporaryItemImprovement | Группировка и создание эффектов:98–136 | Создание источника отличается от применения перенесённого улучшения |

Область поиска — `module`, `templates`, `packsJson`; прямого потребителя `item.enrichedText()` вне самого определения не найдено. Вместо него листы используют `system.enrichedText()`. Динамические макросы мира и внешние модули не исследованы. Подключение примеси не означает, что её полный алгоритм проверен в этой порции.

## Данные и изменения состояния

Миграция меняет source.type в памяти. Выбор атаки/списки/обогащение читают модель. Подготовка эффектов меняет подготовленную систему и overrides; updateSource/update документа в ней нет. realCraft меняет переданные config/messageData, инициирует Actor.removeItem/addItem и Roll.toMessage; генератор добычи инициирует Item.create/update/delete и ChatMessage.create. Родитель Actor не создаётся самим WitcherItem. Сам класс не вводит новую коллекцию эффектов — effects наследуется от Foundry.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Полнота | Полное чтение 376 строк; отражение прототипа; импорты и Object.assign | 12 собственных определений, локальный класс с 4 полями, 5 примесей/11 методов без повторов | Примеси прочитаны до определений и используемых действий; полного покрытия не заявлено |
| Миграция/атаки/алхимия | Оригинальный Item в vm; настоящая DiagramData и CommonItemData | Hexes/Rituals→hex/ritual; порядок клавиш; пустой Set; 9 веществ и обрезка quantity | Родитель ItemBase и локализация заменены; core миграция не исполнена |
| Изготовление | Оригинальные realCraft + extendedRoll; контролируемый Roll и Promise записи | Возврат при трёх pending операциях; нехватка 3 при наличии 2 оставляет success=true в сообщении | Не RNG, БД или UI; изолированный вход может моделировать устаревшую предварительную проверку |
| Таблицы добычи | Оригинальный checkIfItemHasRollTable; наборы [] / [A,B] / повтор A | Пустой массив→TypeError; [A,B]→только A; две записи quantity=2 вместо 3 из начальной1; ноль бросков удаляет генератор | game.packs/таблицы/документы/чат подменены; вероятности и реальная задержка сервера не измерялись |
| Item-эффекты | Оригинальные Item и getters эффекта; core active/apply/applyChangeField, реальные поля | weight8×0.5(final)+2(initial)=6 за один проход; sourceWeight8; overrides.system.weight6; disabled исключён | Static applyChange — адаптер к реальному fieldApply; полный ActiveEffect Document не создавался |
| Передача улучшения | Оригинальный applyTemporaryItemImprovements; подменены Dialog/запись/чат | Передаваемый system содержит 3 флага, changes отсутствует; вход не изменён | Подтверждены данные запроса, не результат сохранения документа |

## Непроверенные участки и открытые вопросы

Полный клиент, запись в мир, открытие компедиумов, реальные броски/чат, экспорт добычи и UI не запускались. Работа restoreReliability/ремонта/разбора/потребления и урона делегирована соседним файлам; здесь проверены определения и конкретные связи. Подробная совместимость phase/type/mode/replacementData и всей цепочки временных эффектов остаётся следующей порции TASK-0003.009. Последствия неоднозначных таблиц, частичного успеха генератора, устаревших UUID и параллельного изготовления требуют отдельного сценария. Игровые правила успеха, расхода компонентов и количества не пересматривались.

## Связанные проблемы

- [issue-00008](../../../../../issues/potential/issue-00008.md) — Queries не ожидает операцию, в том числе restoreReliability.
- [issue-00034](../../../../../issues/potential/issue-00034.md) — Actor.useItem не ожидает расходник; методы Actor.addItem/removeItem сами ожидают запись.
- [issue-00037](../../../../../issues/potential/issue-00037.md) — Интерфейс алхимии вызывает отсутствующий метод списка компонентов.
- [issue-00038](../../../../../issues/potential/issue-00038.md) — realCraft завершается до изменений инвентаря и отправки сообщения.
- [issue-00039](../../../../../issues/potential/issue-00039.md) — Генератор добычи предполагает единственный непустой результат таблицы.
- [issue-00040](../../../../../issues/potential/issue-00040.md) — Повторная генерация существующей стопки может терять количество.
- [issue-00041](../../../../../issues/potential/issue-00041.md) — Успешное сообщение изготовления сохраняется после обнаружения нехватки компонентов.
- [issue-00042](../../../../../issues/potential/issue-00042.md) — Передатчик временного улучшения теряет system.changes.

Все наблюдения остаются potential; их воспроизведение не заменяет подтверждения пользователя и не разрешает исправление.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.008 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.

## Уточнение TASK-0003.009

2026-09-10, `a33bf33add228ae93f96a52046c8feb4ee992921`. Исходник не изменился относительно указанного ранее среза.

[module/actor/mixins/temporaryEffectMixin.js](../../../../../../module/actor/mixins/temporaryEffectMixin.js) создаёт эффекты выбранного оружия, [module/activeEffect/witcherActiveEffect.js](../../../../../../module/activeEffect/witcherActiveEffect.js) задаёт isAppliedTemporaryItemImprovement через system.isTransferred, а [module/data/activeEffects/witcherTemporaryItemImprovementData.js](../../../../../../module/data/activeEffects/witcherTemporaryItemImprovementData.js) наследует changes от ядра. Эти связи подтверждают вход allApplicableEffects/applyActiveEffects Item. Нормализация фактического payload передачи настоящим BaseActiveEffect даёт changes=[] (issue-00042). Отдельно перенос start=null не включает эффект в isExpiryTrackable (issue-00050). Создание оружейных эффектов не ожидается перед рендером [templates/chat/item/appliedTemporaryItemImprovements.hbs](../../../../../../templates/chat/item/appliedTemporaryItemImprovements.hbs); сообщение использует подготовленные данные, не результат записи.

[Журнал сверки](../../../review-log.md) — TASK-0003.009; ограничения изолированного выполнения и неподтверждённые проблемы сохранены.
