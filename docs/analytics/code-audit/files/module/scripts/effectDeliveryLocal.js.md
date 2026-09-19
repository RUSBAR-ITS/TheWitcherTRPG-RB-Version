# module/scripts/effectDeliveryLocal.js

**14.3.1.00106, 2026-09-19, TASK-0011.006.** [Исходник](../../../../../../module/scripts/effectDeliveryLocal.js).

## Назначение, методы и зависимости

Локальные примитивы применения подготовленных AE и статусов. Не выбирают пользователя и не отправляют query.

| Сущность | Назначение и действия |
| --- | --- |
| applyLocalActiveEffects | Копирует serializeEffect; ожидает actor.applyTemporaryItemImprovements; обычные AE готовит через appliedEffectData и ожидает createEmbeddedDocuments. Возвращает UUID результатов. Число семей может быть меньше исходного числа записей |
| hasStatus | Проверяет активные appliedEffects и Set statuses |
| applyLocalStatus | Пустой ID/present → завершённый no-op; иначе ожидает toggleStatusEffect(active:true), counter, затем при иммунитете задержку1000ms и toggleStatusEffect(active:false). Возвращает applied/immune; неполученная запись выбрасывает ошибку |
| handleStatusCounterIntegration | Прежние guards модуля/длительности и lookup; теперь ожидает setValue/changeType. Неверный querySelector массива из issue-00003 сохранён и при срабатывании даёт unknown в сервисе |

**Зависимости:** activeEffect/effectApplication.js/serializeEffect, appliedEffectData; actor/mixins/temporaryEffectMixin.js/applyTemporaryItemImprovements через Actor; ActiveEffect implementation в activeEffect/witcherActiveEffect.js и effectFamilies.js через createEmbeddedDocuments. Внешние Actor.toggleStatusEffect/appliedEffects, game.modules, CONFIG.WITCHER.statusEffects, EffectCounter и таймер. Сервис effectDelivery.js вызывает оба примитива внутри одной withParameterChanges; самостоятельные примитивы не вводят протокол и не показывают успех до завершения записи.

**Границы:** правила статусов/иммунитета и выбор оружия не переработаны. Прежняя ошибка statuscounter может прервать путь до снятия по иммунитету; это отдельная issue-00003, не исправление .006. Реальное ядро проверено для семей/параметров, сеть и запись БД в локальном стенде заменены.

[Проверки и ограничения](../../../../task-0011-static-checks.md#task-0011006).
