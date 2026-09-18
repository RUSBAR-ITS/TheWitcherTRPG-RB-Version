# module/data/actor/derivedStatData.js

## Текущее состояние — 14.3.1.00063

2026-09-18, TASK-0010.005. **Назначение:** Общие формулы и граница ручной базы.

**Методы, сущности, действия и зависимости:** RESOURCE_STATS отделяет текущие запасы от значений производных. isManualDerivedStat разрешает vigor/shield всегда, hp/sta/resolve/focus при customStat. derivedStatBase вычисляет неокруглённую базу через callbacks: BODY/WILL→HP/STA/REC/STUN/порог, BODY→ENC, SPD→Run→Leap, INT/WILL→Resolve/Focus. Потребители: CommonActorData.prepareBaseData, derivedPreparation, parameterPreparation и WitcherModifiersConfiguration. Нет Foundry-зависимостей или записи состояния.

[Исходник](../../../../../../../module/data/actor/derivedStatData.js), [проверки и границы](../../../../../task-0010-005-checks.md). Браузерная приёмка отложена. Ниже, если есть, сохранены датированные предыдущие срезы; изменённые расчёты описаны здесь.
