# module/scripts/effectDelivery.js

## Текущее состояние — 14.3.1.00108 / TASK-0011.008

2026-09-19. Сервис дополнен deliveryVisibility (исходные whisper/blind либо native текущий messageMode), reportDeliveryConsequence (HBS-предупреждение, при невозможности записи notification), createItemEffectDelivery (resolveEffectSource → createEffectDelivery только готовых AE), applyParryStagger (duration1 на заданного Actor) и applyCriticalAdrenaline (optional off/no-op, местное право, прежний whitelist query). Ошибка источника не создаёт пустую повторяемую карточку; предупреждение содержит UUID источника/адресата/исходного сообщения. createDeliverySnapshot допускает отсутствие оригинального сообщения и хранит null; список действует по прежней машине .007. Новые потребители: professionMixin, defenseMixin, damageMixin, consumeMixin; новый шаблон effect-delivery-warning.hbs. Парирование/адреналин не возвращают расходы и не меняют исходный бросок.

[Локальные проверки и границы B08](../../../../task-0011-static-checks.md#task-0011008). Ниже — прежние датированные срезы; утверждения о прямых query/неожидаемой доставке заменены этим разделом.

**14.3.1.00107, 2026-09-19, TASK-0011.006–.007.** [Исходник](../../../../../../module/scripts/effectDelivery.js).

## Назначение, методы и зависимости

Общий сервис чтения источника, доставки на одного Actor и групповой отправки сохранённого результата. castSpell и общий chat listener используют карточку .007; остальные потребители присоединяются в .008.

| Сущность | Назначение и результат |
| --- | --- |
| SOURCE_QUERY / DELIVERY_QUERY | Два отдельных ключа Foundry Queries; зарегистрированы в setup/queries.js |
| resolveDocument | Асинхронный fromUuid и проверка documentName; неверный/недоступный документ → null |
| readEffectSource | Только чтение доступного Item и фильтрация applySelf/applyOnTarget/applyOnHit/applyOnDamage; сериализованный снимок или refused, без пересылки |
| resolveEffectSource | Локальное чтение; при недоступности ровно один запрос другому активному GM. Самому себе не отправляет |
| getEffectExecutor | Локальное canUserModify(update), иначе прежний getActorOwner; нет активного исполнителя → refused |
| prepareEntries | Проверка вида записи, статуса и длительности всего набора до записи; копирование AE; отсутствующая длительность и явный0 различаются |
| receiveEffectDelivery | Проверка местного права, withParameterChanges вокруг всего набора, последовательные локальные примитивы; никогда не пересылает |
| deliverActorEffects | Один местный вызов или один query выбранному пользователю; ждёт ответ, автоматически не повторяет |
| notifyEffectDelivery | Возвращает результат, при отказе/неподтверждённом исходе показывает ключ ru/en WITCHER.EffectDelivery.* |

**Контракт:** complete + results для завершённых записей; причины applied/present/immune/empty; refused до записи; unknown при исключении в начатой операции или потере/неверном ответе. results содержит только ранее подтверждённые записи; часть последней могла сохраниться. Это не транзакция и не разрешение повторять неизвестный исход. Отмена выбора улучшения внутри существующего метода консервативно даёт unknown: этот метод не сообщает отдельную фазу отказа.

**Зависимости:** helper.js/getActorOwner; activeEffect/effectApplication.js/serializeEffect и validateEffectDuration; actor/parameterPersistence.js/withParameterChanges; effectDeliveryLocal.js/оба локальных примитива. Внешние границы — fromUuid, User.query, права Actor, CONFIG.statusEffects, локализация/уведомления. Обратного импорта обёрток нет.

**Потребители:** обёртки temporaryEffects/applyActiveEffect.js и statusEffects/applyStatusEffect.js; registerQueries в setup/queries.js. Локальные эффекты не изменяют источник; подготовленные AE используют прежнюю модель system.changes и семейства.

[Проверки и ограничения](../../../../task-0011-static-checks.md#task-0011006).

## Группа целей и карточка (.007)

| Сущность | Назначение |
| --- | --- |
| createDeliverySnapshot | JSON-копия действия/целей/строк; одинаковые записи повторных токенов объединяются по Actor UUID |
| collectSpellEffects | Четыре канала self/target, фиксированные AE и duration; без бросков и записи |
| deliverySnapshot / canSendDelivery | Чтение версии1 flags; только автор и обычное право update сообщения |
| renderDelivery | HBS карточки, локализованные состояния/причины, явный duration0 |
| saveDelivery | Ожидаемые content и flags одним update; отмена без Document считается ошибкой |
| interruptedDelivery | Прерванное sending → needsReview; подтверждённое сохраняется, неизвестное не повторяется |
| sendEffectDelivery | Проверка всех исполнителей; waiting при любом отказе до записи; сохранить sending, затем последовательные ожидаемые Actor-пакеты; complete или needsReview |
| createEffectDelivery | Нет воздействий → нет карточки; ChatMessage типа base со speaker/author и исходными whisper/blind; первая отправка автоматически |
| bindEffectDelivery | Кнопка инициатора, WeakSet от повторной подписки, activeSends от местного двойного нажатия; reload sending требует проверки |

Схема flags: `version/authorId/state/action/targets`; action содержит actorUuid/itemUuid/name/messageUuid, targets — actorUuid/name/entries/result, entries — entry/result. Это снимок исходного результата без документов, Roll и ресурсного журнала. Длительности/величины не пересчитываются, переключение целей не изменяет сохранённые UUID. Прежние методы доставки .006 остаются доступны.

Дополнительные зависимости: [templates/chat/effect-delivery.hbs](../../../../../../templates/chat/effect-delivery.hbs), native ChatMessage.create/update/getFlag/canUserModify и Handlebars, ru/en WITCHER.EffectDelivery, CONFIG.statusEffects. Потребители: [castSpellMixin.js](../../../../../../module/actor/mixins/castSpellMixin.js) и [chat.js](../../../../../../module/scripts/chat.js).

Blind карточка сохраняет native скрытие списка. Если инициатору список скрыт, hook добавляет только нейтральные состояние/кнопку без целей/значений. Завершённая или неизвестная отправка кнопки повтора не имеет. Никакой распределённой блокировки, автоматического отката или повторного списания ресурсов; это не атомарная транзакция нескольких Actor.

[S07, регрессия и границы B07](../../../../task-0011-static-checks.md#task-0011007).
