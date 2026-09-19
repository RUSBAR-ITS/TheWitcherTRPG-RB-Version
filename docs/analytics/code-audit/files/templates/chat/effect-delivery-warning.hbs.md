# templates/chat/effect-delivery-warning.hbs

**14.3.1.00108, 2026-09-19, TASK-0011.008.** [Исходник](../../../../../../templates/chat/effect-delivery-warning.hbs).

## Назначение и использование

Предупреждение о неподтверждённом последствии уже выполненного действия. Контекст готовит reportDeliveryConsequence в [effectDelivery.js](../../../../../../module/scripts/effectDelivery.js); видимость сообщения сохраняет исходные whisper/blind. Этот шаблон сам ничего не применяет и не запускает новый бросок.

## Сущности и действия

actorUuid/actorName, itemUuid, messageUuid — обычные native content links. actionLabel/reasonLabel — локализованные вид последствия и причина. unknown включает требование сначала проверить персонажа; adrenaline показывает инструкцию по существующей кнопке листа. statusId/duration/statusName формируют ручную apply-status ссылку с data-actor-uuid: исходный атакующий, staggered и1 раунд. Никакой подмены выделенным токеном. Все значения экранируются двойными скобками.

## Зависимости

Native HBS localize/if и ru/en WITCHER.EffectDelivery; обработчик [statusEffects/applyStatusEffect.js](../../../../../../module/scripts/statusEffects/applyStatusEffect.js)/onApplyStatus проверяет право и статус, его listener вызывается существующим renderChatMessageHTML hook. Адреналин меняет пользователь кнопкой statMixin на листе; новая кнопка начисления не создаётся. Для закрытого сообщения native видимость ограничивает доступ к содержимому.

[S08 и границы B08](../../../../task-0011-static-checks.md#task-0011008).
