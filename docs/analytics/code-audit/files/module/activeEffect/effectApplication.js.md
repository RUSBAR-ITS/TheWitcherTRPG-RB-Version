# module/activeEffect/effectApplication.js

## Текущее состояние — 14.3.1.00068 (TASK-0010.009)

2026-09-18. **Назначение:** Сериализация и часы назначенного эффекта.

**Методы, сущности, действия и зависимости:** serializeEffect глубоко копирует toObject; appliedEffectData сбрасывает служебные триггеры, ID/старый start, сохраняет system/changes и срок шаблона. validateEffectDuration допускает целые неотрицательные раунды, null/undefined означают отсутствие override. initializeEffectStart использует native getEffectStart, Actor владельца и одну коррекцию очереди; requireEffectWrite сообщает о неполной записи.

[Проверки доставки и пакетного истечения](../../../../task-0010-009-checks.md). Браузерная приёмка впереди. Ниже, если присутствуют, сохранены описания прежних срезов.


