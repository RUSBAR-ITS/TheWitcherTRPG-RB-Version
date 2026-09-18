# module/activeEffect/effectFamilies.js

## Текущее состояние — 14.3.1.00068 (TASK-0010.009)

2026-09-18. **Назначение:** Несуммируемые семейства и порядок назначения.

**Методы, сущности, действия и зависимости:** effectFamily читает nonStacking/effectTypeId. isFamilySuppressed выбирает доступный источник по сохраняемому applicationOrder, при равенстве — ID; prepare ничего не пишет. createEffectDocuments/updateEffectDocuments заменяют применённые экземпляры, оставляют transfer-источники. assignedItemData обрабатывает вложенные AE при импорте Item и повторной активации. Scope обычного transfer — Actor, улучшения — конкретный Item. Семейство сравнивается только у nonStacking=true.

[Проверки доставки и пакетного истечения](../../../../task-0010-009-checks.md). Браузерная приёмка впереди. Ниже, если присутствуют, сохранены описания прежних срезов.


