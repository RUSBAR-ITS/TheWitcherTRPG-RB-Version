# TASK-0011 — Смежные исправления расчётов, интерфейса и доставки эффектов

| Поле | Значение |
| --- | --- |
| Статус | `planned` — согласован состав очереди; реализация не начата |
| Создана | 2026-09-18, 14.3.1.00057 |
| Основание | Прямое поручение пользователя выделить смежные issues TASK-0010 в отдельную ближайшую задачу |
| Срез анализа | `dev`, HEAD `0537500936de736ce898b0173670c82714b72f23`; текущие рабочие исходники, Foundry14.367 |

## Цель и границы

Устранить смежные дефекты, которые формируют неверные исходные значения или мешают пользоваться результатами [TASK-0010](task-0010-parameter-limits.md#related-issues). Не расширять этим заданием общий контракт модификаторов. Состав после переноса 00015 — **11 issues** ниже; карточки пока остаются в прежних каталогах. Точные способы исправления и спорные значения подтверждаются перед кодом. Большинство карточек содержит более ранние воспроизведения: перед каждой порцией сверить актуальные исходники и затронутые связи графа.

Обычный порядок — после TASK-0010. Если один из дефектов блокирует её приёмку, можно вынести соответствующую порцию раньше по отдельному поручению пользователя. Зависимости от вычислителя требуют его актуального контракта, а не завершения всех независимых подпунктов.

**Уточнение 2026-09-19, .00076:** [issue-00015](../issues/potential/issue-00015.md) перенесена в [TASK-0010.014](task-0010-parameter-limits.md#task-0010014) по поручению пользователя. Подписи новой модели, карточки и настройки монстра входят в эту подзадачу; повторно выполнять их здесь не требуется. Компоновка редакторов — [TASK-0010.015](task-0010-parameter-limits.md#task-0010015). Issue-00167 остаётся отдельной работой этой очереди; перенос 00015 не означает исправления или закрытия обеих карточек.

## Порции работы

| Порция | Issues | План и граница | Проверка после исправления |
| --- | --- | --- | --- |
| 01. Ресурсы | [00164](../issues/potential/issue-00164.md), [00203](../issues/potential/issue-00203.md) | Ограничение действия восстановления действующим максимумом STA; уточнить смысл сердечка и используемый максимум HP | REC у полного/неполного/изменённого max; согласованный индикатор под эффектом и после reload |
| 02. Редактор навыков | [00167](../issues/potential/issue-00167.md) | Устранение присваивания объектом глобальной jQuery; подписи и компоновка переданы в TASK-0010.014/.015 | После редактирования работают другие окна; не дублировать приёмку 00015 |
| 03. Словесный бой | [00302](../issues/potential/issue-00302.md), [00303](../issues/potential/issue-00303.md) | Актуальные DOM-обработчики контекстного меню и чтение выбранной радиокнопки из собственного диалога | Атака/защита через чат; два открытых окна с разными выборами не влияют друг на друга |
| 04. Алхимия и ремонт | [00037](../issues/potential/issue-00037.md), [00102](../issues/potential/issue-00102.md) | Согласовать вызовы с существующими методами Item/моделей; данные повреждений и результат ремонта | Получить список компонентов, провести крафт/ремонт; отмена не расходует ресурсы. Формула ремонта 00103 остаётся в TASK-0010 |
| 05. Штраф брони | [00254](../issues/potential/issue-00254.md), [00277](../issues/potential/issue-00277.md) | Перепроверить компенсацию EV и выбор экипированной брони на хранении; закрепить ожидаемое поведение до кода | EV0/1/3 с меньшей/равной/большей компенсацией; броня надета, в сумке, извлечена |
| 06. Доставка | [00045](../issues/potential/issue-00045.md), [00185](../issues/potential/issue-00185.md) | Конечный отказ при недоступном источнике/получателе; отсутствие активного владельца/GM; не допустить рекурсии перенаправления | Один успешный вызов или понятный отказ; недоступный Item, GM offline, владелец/GM, без повторных эффектов |

<a id="armor"></a>
## Что осталось после контейнеров

В текущем containerOperations.locationPatches перемещение устанавливает isStored, но оставляет equipped. getArmorEcumbrance выбирает броню по type/equipped непосредственно из this.items; getLocationArmor берёт getList и исключает хранение. Поэтому 00277 **не закрыта** контейнерным рефакторингом: например, ранее надетая броня с EV3 после помещения в сумку может продолжать давать EV3. Это вывод чтения текущих методов, нового игрового воспроизведения на шаге планирования не было.

Предпочтительный предмет следующего согласования — единый критерий действующей брони у потребителей. Фильтровать isStored или автоматически снимать equipped при помещении в контейнер — разные решения с разным поведением после извлечения; второе не считать принятой частью завершённого рефакторинга. Общий вес содержимого контейнера при этом сохраняется по существующим правилам.

00254 независима: при положительном EV castSpell вычитает штраф, затем прибавляет всю компенсацию. EV1 и ignoredEvWhenCasting3 дают+2. Предложение ограничить компенсацию фактическим штрафом требует закрепления ожидаемого результата; произвольные и условные бонусы TASK-0010 не ограничиваются этим исправлением автоматически.

## Файлы и зависимости

Список ниже получен из локализации включённых карточек; это область повторной проверки, не обещание изменить каждый файл. Номера строк старых воспроизведений могут измениться. Для контейнерного пункта дополнительно проверять containerOperations/containerTemplates → isStored/equipped → armorMixin → расчёт Actor/колдовство.

| Файл | Причина проверки / изменения |
| --- | --- |
| [module/actor/sheets/WitcherActorSheet.js](../../module/actor/sheets/WitcherActorSheet.js) | [00164](../issues/potential/issue-00164.md), [00167](../issues/potential/issue-00167.md) |
| [module/actor/sheets/WitcherActorSheetV1.js](../../module/actor/sheets/WitcherActorSheetV1.js) | [00164](../issues/potential/issue-00164.md), [00167](../issues/potential/issue-00167.md) |
| [module/data/actor/templates/common/stats/statData.js](../../module/data/actor/templates/common/stats/statData.js) | [00164](../issues/potential/issue-00164.md) |
| [module/actor/witcherActor.js](../../module/actor/witcherActor.js) | [00164](../issues/potential/issue-00164.md), [00203](../issues/potential/issue-00203.md), [00277](../issues/potential/issue-00277.md) |
| [templates/partials/character-header.hbs](../../templates/partials/character-header.hbs) | [00164](../issues/potential/issue-00164.md) |
| [templates/sheets/actor/partials/character/sidebar.hbs](../../templates/sheets/actor/partials/character/sidebar.hbs) | [00203](../issues/potential/issue-00203.md) |
| [module/data/actor/templates/common/stats/derivedStatsData.js](../../module/data/actor/templates/common/stats/derivedStatsData.js) | [00203](../issues/potential/issue-00203.md) |
| [module/actor/sheets/mixins/skillMixin.js](../../module/actor/sheets/mixins/skillMixin.js) | [00167](../issues/potential/issue-00167.md) |
| [module/scripts/verbalCombat/verbalCombat.js](../../module/scripts/verbalCombat/verbalCombat.js) | [00302](../issues/potential/issue-00302.md) |
| [module/scripts/verbalCombat/verbalCombatDefense.js](../../module/scripts/verbalCombat/verbalCombatDefense.js) | [00302](../issues/potential/issue-00302.md), [00303](../issues/potential/issue-00303.md) |
| [module/TheWitcherTRPG.js](../../module/TheWitcherTRPG.js) | [00302](../issues/potential/issue-00302.md) |
| [module/actor/mixins/verbalCombatMixin.js](../../module/actor/mixins/verbalCombatMixin.js) | [00303](../issues/potential/issue-00303.md) |
| [templates/dialog/verbal-combat.hbs](../../templates/dialog/verbal-combat.hbs) | [00303](../issues/potential/issue-00303.md) |
| [templates/dialog/verbal-combat-defense.hbs](../../templates/dialog/verbal-combat-defense.hbs) | [00303](../issues/potential/issue-00303.md) |
| [module/actor/sheets/WitcherCharacterSheet.js](../../module/actor/sheets/WitcherCharacterSheet.js) | [00037](../issues/potential/issue-00037.md) |
| [module/item/witcherItem.js](../../module/item/witcherItem.js) | [00037](../issues/potential/issue-00037.md) |
| [module/item/systems/repair.js](../../module/item/systems/repair.js) | [00102](../issues/potential/issue-00102.md) |
| [templates/dialog/repair-dialog.hbs](../../templates/dialog/repair-dialog.hbs) | [00102](../issues/potential/issue-00102.md) |
| [templates/chat/item/repair.hbs](../../templates/chat/item/repair.hbs) | [00102](../issues/potential/issue-00102.md) |
| [module/data/item/weaponData.js](../../module/data/item/weaponData.js) | [00102](../issues/potential/issue-00102.md) |
| [module/data/item/armorData.js](../../module/data/item/armorData.js) | [00102](../issues/potential/issue-00102.md) |
| [module/actor/mixins/castSpellMixin.js](../../module/actor/mixins/castSpellMixin.js) | [00254](../issues/potential/issue-00254.md) |
| [module/actor/mixins/armorMixin.js](../../module/actor/mixins/armorMixin.js) | [00254](../issues/potential/issue-00254.md), [00277](../issues/potential/issue-00277.md) |
| [module/data/actor/templates/common/lifepathData.js](../../module/data/actor/templates/common/lifepathData.js) | [00254](../issues/potential/issue-00254.md) |
| [module/scripts/temporaryEffects/applyActiveEffect.js](../../module/scripts/temporaryEffects/applyActiveEffect.js) | [00045](../issues/potential/issue-00045.md), [00185](../issues/potential/issue-00185.md) |
| [module/setup/queries.js](../../module/setup/queries.js) | [00045](../issues/potential/issue-00045.md) |
| [module/scripts/helper.js](../../module/scripts/helper.js) | [00185](../issues/potential/issue-00185.md) |
| [module/scripts/statusEffects/applyStatusEffect.js](../../module/scripts/statusEffects/applyStatusEffect.js) | [00185](../issues/potential/issue-00185.md) |
| [module/actor/mixins/defenseMixin.js](../../module/actor/mixins/defenseMixin.js) | [00185](../issues/potential/issue-00185.md) |
| [module/actor/mixins/professionMixin.js](../../module/actor/mixins/professionMixin.js) | [00185](../issues/potential/issue-00185.md) |
| [module/item/containerOperations.js](../../module/item/containerOperations.js) | [00277](../issues/potential/issue-00277.md) |
| [module/item/containerTemplates.js](../../module/item/containerTemplates.js) | [00277](../issues/potential/issue-00277.md) |

## Проверки и приёмка

По каждой порции сначала проверить исходный дефект на текущем коде, затем небольшой набор настоящих методов: границы чисел, отсутствие побочных записей при отказе, контракт DOM/формы/получателя. Если историческая причина уже отсутствует, зафиксировать факт и не переписывать работающий путь.

Игровые сценарии таблицы выполнять после перезапуска/прав пользователем. Для доставки нужны QA-GM/QA-Player и конечный отказ без активного адресата; для UI — события штатного листа/чата, а не только прямой вызов метода. Падение из другой карточки отделять от результата проверяемой порции. Не запускать полный набор графа из-за локальной правки.

- [ ] Все 12 карточек имеют проверенный результат или явно согласованный перенос.
- [ ] Действующие ресурсы/EV, интерфейсные действия и доставка согласованы с контрактом TASK-0010.
- [ ] Изменённые файлы описаны, адресные статические и браузерные проверки записаны; пользователь принял результат.

Открытые решения перед кодом: смысл индикатора HP; учёт/снятие экипировки при хранении; предел компенсации EV; конкретный отказ при недоступном адресате; актуальная цепочка ремонта. Постановка очереди не означает, что эти решения уже приняты.

## Документация и итог

При реализации обновить эту задачу, связанные карточки issues и их реестр при согласованной смене статуса; README/CHANGELOG/версию. По изменённым исходникам обновить карточки в docs/analytics/code-audit/files и соответствующие records/рёбра/процессы docs/analytics/system-index; контрольные хеши и один check --freshness. Существующие идентификаторы графа сохранять; новые добавлять по фактическому коду. Тесты графа выбирать адресно по затронутым разделам.

На этапе .00057 создана только задача и связи. Игровой код, мир и компедиумы не изменены, перечисленные тесты пока не выполнены. Issues автоматически не переводились и не закрывались.
