# module/data/actor/templates/common/stats/derivedStatsData.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/data/actor/templates/common/stats/derivedStatsData.js](../../../../../../../../../../module/data/actor/templates/common/stats/derivedStatsData.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `7b7788bc614e5b7a57f8c596fb64ca75ecabd8b7` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.001](../../../../../../../../../tasks/task-0003.001.md), одна порция из пяти файлов |
| Запись перекрёстной сверки | [TASK-0003.001](../../../../../../../review-log.md#task-0003001) |

## Назначение файла

Вложенная модель двенадцати производных параметров Actor. Содержит схему и частичную миграцию исходных значений. Сами формулы производных параметров находятся в CommonActorData и WitcherActor.

## Условия использования

Default export `DerivedStats extends foundry.abstract.DataModel`. [module/data/actor/commonActorData.js](../../../../../../../../../../module/data/actor/commonActorData.js) импортирует класс (11) и включает `EmbeddedDataField(DerivedStats)` как `system.derivedStats` (34). Модель наследуется персонажем и монстром через CommonActorData, отдельно в CONFIG.Actor.dataModels не регистрируется.

Собственных `prepareBaseData`, `prepareDerivedData`, обработчиков интерфейса и вызовов сохранения в файле нет.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| fields | const, 3 | Классы полей Foundry | Локальная ссылка | Построение схемы. |
| DerivedStats | class, 5–47 | Вложенная модель производных параметров | Default export | defineSchema и migrateData. |
| hp, shield, sta, resolve, focus, vigor, stun, run, leap, enc, rec, woundTreshold | SchemaField, 8–20 | Двенадцать наборов stat | system.derivedStats через CommonActorData | Пять полей в каждом наборе; все unmodifiedMax initial = 0. |

| Ключ | Ключ подписи | Есть перенос max → unmodifiedMax при == 0 | statMap |
| --- | --- | --- | --- |
| hp | WITCHER.Actor.DerStat.HP | Нет | derivedStats / hp |
| shield | WITCHER.Actor.DerStat.Shield | Нет | Отсутствует |
| sta | WITCHER.Actor.DerStat.Sta | Нет | derivedStats / sta |
| resolve | WITCHER.Actor.DerStat.Resolve | Нет | derivedStats / resolve |
| focus | WITCHER.Actor.DerStat.Focus | Нет | derivedStats / focus |
| vigor | WITCHER.Actor.DerStat.Vigor | Да | derivedStats / vigor |
| stun | WITCHER.Actor.DerStat.Stun | Да | derivedStats / stun |
| run | WITCHER.Actor.DerStat.Run | Да | derivedStats / run |
| leap | WITCHER.Actor.DerStat.Leap | Да | derivedStats / leap |
| enc | WITCHER.Actor.DerStat.Enc | Да | derivedStats / enc |
| rec | WITCHER.Actor.DerStat.Rec | Нет | derivedStats / rec |
| woundTreshold | WITCHER.Actor.DerStat.woundTreshold | Да | derivedStats / woundTreshold |

Написание `woundTreshold` сохранено по коду. Оно отличается от `healthState.woundThreshold`: это разные пути и сущности.

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| DerivedStats.defineSchema() | stat, SchemaField | Объект 12 SchemaField | Вызов stat(label) для каждой записи | Синхронно; формулы значений не выполняются. |
| DerivedStats.migrateData(source) | Объект исходных данных | Результат super.migrateData(source) | Для stun/run/leap/enc/woundTreshold/vigor при base == 0 копирует max | Изменяет source на месте; нет catch/записи документов. |

Отсутствующее поле и нулевая база различаются: `undefined == 0` ложно. Вход `{vigor:{max:7}}` после создания модели получает `unmodifiedMax:0`; при явно заданном `unmodifiedMax:0` миграция получает 7. Другие шесть записей метод не переносит вообще; нельзя приписывать ему миграцию всех производных параметров.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| stat | [module/data/actor/templates/common/stats/statData.js](../../../../../../../../../../module/data/actor/templates/common/stats/statData.js) | ES import; фабрика | 1, 8–20: форма каждого показателя | Определение и 12 вызовов сверены. |
| DataModel, SchemaField | Foundry 14.367.0, common/abstract/data.mjs и common/data/fields.mjs под /opt/foundryvtt | Наследование и конструктор | 5–20 | Проверено создание реальной модели. |
| DataModel.migrateData | /opt/foundryvtt/common/abstract/data.mjs:908–910 | Вызов superclass | 45 | Возвращает переданный source. |
| Ключи label | [lang/en.json](../../../../../../../../../../lang/en.json), [lang/ru.json](../../../../../../../../../../lang/ru.json) | Данные для локализации | 8–20 | Все 12 ключей есть в обоих файлах. |
| WITCHER.statMap | [module/setup/config.js](../../../../../../../../../../module/setup/config.js) | Сопоставление схемы и адресов; прямого импорта нет | 11 записей origin=derivedStats | Реальный getField подтвердил все пути; shield отсутствует в справочнике. |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/data/actor/commonActorData.js](../../../../../../../../../../module/data/actor/commonActorData.js) | DerivedStats; поля модели | Вложение, исходные формулы, vigor.max; отдельная миграция vigor из value | 11, 34, 77–90, 106–114. |
| [module/data/actor/characterData.js](../../../../../../../../../../module/data/actor/characterData.js) | Унаследованная derivedStats | Расширяет CommonActorData | 9–14. |
| [module/data/actor/monsterData.js](../../../../../../../../../../module/data/actor/monsterData.js) | derivedStats и customStat | Наследует модель; задаёт флаг ручных параметров | 6–11, 59. |
| [module/actor/witcherActor.js](../../../../../../../../../../module/actor/witcherActor.js) | Все производные кроме отдельной обработки shield | calculateStat читает hp/woundTreshold; calculateFixedDerivedStats/calculateDerivedStat записывают параметры | 87–188. |
| [module/actor/mixins/damageMixin.js](../../../../../../../../../../module/actor/mixins/damageMixin.js) | shield.value и derivedStats[derivedStat].value | Поглощение щитом и уменьшение ресурса | 37–56, 145. |
| [module/scripts/chat.js](../../../../../../../../../../module/scripts/chat.js) | shield.value, hp.value/max | Установка щита и лечение | 15, 36–39. |
| [module/actor/mixins/healMixin.js](../../../../../../../../../../module/actor/mixins/healMixin.js) | hp.value/max | Ограничение величины лечения | 7–8. |
| [module/item/mixins/consumeMixin.js](../../../../../../../../../../module/item/mixins/consumeMixin.js) | hp.value | Применение рассчитанного лечения | 9. |
| [module/actor/mixins/castSpellMixin.js](../../../../../../../../../../module/actor/mixins/castSpellMixin.js) | sta.value | Расход выносливости | 126–132. |
| [module/actor/mixins/weaponAttackMixin.js](../../../../../../../../../../module/actor/mixins/weaponAttackMixin.js) | sta.value | Расход на атаку | 144–150. |
| [module/actor/mixins/defenseMixin.js](../../../../../../../../../../module/actor/mixins/defenseMixin.js) | sta.value, stun.value | Расход на защиту; бросок оглушения | 259–265, 434. |
| [module/scripts/verbalCombat/verbalCombat.js](../../../../../../../../../../module/scripts/verbalCombat/verbalCombat.js) | resolve.value | Уменьшение решимости | 53–54. |
| [module/scripts/combat/generalCombatHook.js](../../../../../../../../../../module/scripts/combat/generalCombatHook.js) | hp.value/max | Регенерация и лечение по событию боя | 33–35, 83; [связанный разбор регистрации](../../../../../setup/hooks.js.md). |
| [module/actor/sheets/WitcherActorSheet.js](../../../../../../../../../../module/actor/sheets/WitcherActorSheet.js) | sta.value/max, rec.value | Действия восстановления | 270–288. |
| [module/actor/sheets/mixins/healMixin.js](../../../../../../../../../../module/actor/sheets/mixins/healMixin.js) | hp.value/max | Действия лечения и отдыха | 5, 80–85. |
| [module/actor/sheets/mixins/deathSaveMixin.js](../../../../../../../../../../module/actor/sheets/mixins/deathSaveMixin.js) | hp.value, woundTreshold.value | Проверка состояния здоровья | 18–19. |
| [module/setup/config.js](../../../../../../../../../../module/setup/config.js) | statMap и changes на sta.max | Адреса для потребителей; статус с изменением выносливости | 74–125, 2149. |
| [module/activeEffect/mixins/baseMixin.js](../../../../../../../../../../module/activeEffect/mixins/baseMixin.js) | derivedStats.*.totalModifiers | Мастер получает пути через statMap | 14–29. |
| [templates/partials/character/tab-stats.hbs](../../../../../../../../../../templates/partials/character/tab-stats.hbs) | derivedStats.* | Вывод по label/value/max с исключениями ресурсов | 72 и далее. |
| [templates/sheets/actor/partials/character/sidebar.hbs](../../../../../../../../../../templates/sheets/actor/partials/character/sidebar.hbs) | hp/sta/shield/resolve/focus и другие показатели | Поля текущих ресурсов и вывод максимумов | 6–37 и последующие блоки. |
| [templates/sheets/actor/partials/monster/sidebar.hbs](../../../../../../../../../../templates/sheets/actor/partials/monster/sidebar.hbs) | derivedStats | Поля и вывод ресурсов монстра | 5–36 и последующие блоки. |
| [templates/sheets/actor/configuration/app/edit-stats.hbs](../../../../../../../../../../templates/sheets/actor/configuration/app/edit-stats.hbs) | system.derivedStats | Передаёт набор в stats-block | 6–8. |
| [templates/sheets/actor/configuration/app/partials/stats-block.hbs](../../../../../../../../../../templates/sheets/actor/configuration/app/partials/stats-block.hbs) | max/label/unmodifiedMax | Динамическое редактирование исходных значений | 1–8. |
| [templates/sheets/actor/configuration/monster/general.hbs](../../../../../../../../../../templates/sheets/actor/configuration/monster/general.hbs) | hp/sta/resolve.unmodifiedMax | Поля при customStat | 3–6. |
| [templates/partials/character/tab-magic.hbs](../../../../../../../../../../templates/partials/character/tab-magic.hbs) | vigor | Отображение и ввод | 47–49. |
| [templates/sheets/actor/tabs/tab-inventory.hbs](../../../../../../../../../../templates/sheets/actor/tabs/tab-inventory.hbs) | enc | Отображение переносимого веса | 5–7. |
| [templates/chat/combat/regeneration.hbs](../../../../../../../../../../templates/chat/combat/regeneration.hbs) | hp.value | Вывод сообщения регенерации | 4. |

### Пути воздействий в данных компедиума

Проверены `key` с префиксом `system.derivedStats.`. Полный разбор эффектов и документов компедиума не выполнен; существование пути не подтверждает фактическое применение эффекта.

| Файл данных | Пути в changes |
| --- | --- |
| [packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Minor_Head_Wound_wPRuwd7RdLWnWmnb.json](../../../../../../../../../../packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Minor_Head_Wound_wPRuwd7RdLWnWmnb.json) | `system.derivedStats.stun.totalModifiers` |
| [packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Ruptured_Spleen__Treated__kFcie7Io28kKittg.json](../../../../../../../../../../packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Ruptured_Spleen__Treated__kFcie7Io28kKittg.json) | `system.derivedStats.stun.totalModifiers` |
| [packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Heart_Damage_PVraD16y2VWkOH6J.json](../../../../../../../../../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Heart_Damage_PVraD16y2VWkOH6J.json) | `system.derivedStats.sta.max` |
| [packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Heart_Damage__Stabilized__O8EM4quPU4A5VOHH.json](../../../../../../../../../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Heart_Damage__Stabilized__O8EM4quPU4A5VOHH.json) | `system.derivedStats.sta.max` |
| [packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Spetic_Shock__Stabilized__LM6Kkh0ib6ux4WQp.json](../../../../../../../../../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Spetic_Shock__Stabilized__LM6Kkh0ib6ux4WQp.json) | `system.derivedStats.sta.max` |
| [packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Spetic_Shock__Treated__vkr5MXhnalPp8yJJ.json](../../../../../../../../../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Spetic_Shock__Treated__vkr5MXhnalPp8yJJ.json) | `system.derivedStats.sta.totalModifiers` |
| [packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Spetic_Shock_tF3hsi4yZOMJ6xuW.json](../../../../../../../../../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Spetic_Shock_tF3hsi4yZOMJ6xuW.json) | `system.derivedStats.sta.max` |
| [packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Cracked_Ribs__Treated__oe4y6zxH2WUR9gSj.json](../../../../../../../../../../packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Cracked_Ribs__Treated__oe4y6zxH2WUR9gSj.json) | `system.derivedStats.enc.totalModifiers` |

Поиск выполнен в `module/`, `templates/`, `packsJson/`, включая динамическую индексацию и statMap. В старых [module/actor/sheets/WitcherActorSheetV1.js](../../../../../../../../../../module/actor/sheets/WitcherActorSheetV1.js) и [templates/sheets/actor/monster-sheet.hbs](../../../../../../../../../../templates/sheets/actor/monster-sheet.hbs) найдены дополнительные обращения; достижимость этих представлений не подтверждена этой порцией.

## Данные и изменения состояния

Формулы ниже локализованы в потребителях и приведены для различения роли полей. Они не являются методами DerivedStats.

Обозначения: `B0/W0/S0/I0` — unmodifiedMax BODY/WILL/SPD/INT; `B/W/S/I` — текущие value; `A0=floor((B0+W0)/2)`. В WitcherActor `A=floor((B+W)/2)`, а `AM=floor((BODY.max+WILL.max)/2)`; `m` — totalModifiers соответствующей записи.

| Показатель | CommonActorData.prepareBaseData | WitcherActor и другие потребители |
| --- | --- | --- |
| stun | unmodifiedMax = clamp(A0,1,10) | value = clamp(A,1,10)+m; max = clamp(AM,1,10). Модификатор value прибавляется после clamp. |
| run | unmodifiedMax = S0*3 | value = S*3+m; max = S*3. |
| leap | unmodifiedMax = floor(S0*3/5) | value = floor(S*3/5+m); max = floor(SPD.max*3/5). |
| enc | unmodifiedMax = B0*10 | value = B*10+m; max = B*10. |
| rec | unmodifiedMax = A0 | value = A+m; max = AM. |
| woundTreshold | unmodifiedMax = A0 | value = AM+m; max = AM. |
| resolve | unmodifiedMax = (W0+I0)*5 | Без customStat: max = floor((W+I)/2)*5+m. С customStat: unmodifiedMax+m. |
| focus | unmodifiedMax = (W+I)*3, именно value | Без customStat: max = floor((W+I)/2)*3+m. С customStat: unmodifiedMax+m. |
| hp, sta | Здесь не рассчитываются | Без customStat: unmodifiedMax=A*5, max=floor(A*5+m). С customStat: max=unmodifiedMax+m. |
| vigor | max = unmodifiedMax | max = unmodifiedMax+m. |
| shield | Здесь не рассчитывается | value устанавливается из чата и уменьшается при поглощении урона; calculateDerivedStat его не вызывает. |

У hp/sta/resolve/focus/vigor `calculateDerivedStat` меняет максимум, не восстанавливает автоматически текущий ресурс до этого максимума. Данные `value` читают и обновляют обработчики действий. Модель не задаёт универсальных min/max и не проверяет `value <= max`.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Схема | Реальная DerivedStats в Node с классами Foundry 14.367 | 12 наборов по 5 полей; собственных методов подготовки нет | Не полный Actor. |
| Миграция | Каждая из 12 записей: max=7/base=0 | Копирование только для шести перечисленных ключей | Недостающая база проверена отдельно для vigor. |
| Внешние формулы основы | Реальная CommonActorData: B0=6,W0=4,S0=5,I0=7,I=3,W=0 | stun=5,run=15,leap=3,enc=60,rec=5,woundTreshold=5,resolve=55,focus=9 в unmodifiedMax | Только prepareBaseData; формулы WitcherActor в этой таблице проверены чтением. |
| Справочник и подписи | getField 11 записей statMap; JSON en/ru | Пути и подписи существуют; shield в statMap отсутствует | Отсутствие shield в справочнике не объявлено ошибкой. |
| Записи ресурсов | Чтение обработчиков урона, расхода, лечения и форм | Различены расчёт полей и update документов | Сценарии сохранения, боя и интерфейса не запускались. |

## Непроверенные участки и открытые вопросы

Непрочитанных частей файла нет. Полный цикл Actor/ActiveEffect, все ветви customStat, сохранение ресурсов и влияние реальных данных мира будут проверяться отдельно. Отсутствие миграции остальных шести показателей само по себе не признано ошибкой: назначение и происхождение их исходных значений различаются.

## Связанные проблемы

[issue-00011](../../../../../../../../../issues/potential/issue-00011.md) — перенос исходной базы не срабатывает при отсутствующем unmodifiedMax, в том числе у vigor.


## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.001 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.

## Уточнение TASK-0003.006

2026-09-10, `fe7ea7420cd4dfa6ee51baf7520f7b0ad8f8b13d`. Полностью сверены базовые присваивания CommonActorData:79–90: stun/run/leap/enc/rec/woundTreshold/resolve/focus и vigor.max. База focus использует текущие value, resolve — unmodifiedMax. hp/sta/shield этим методом не рассчитываются; конечные max/value рассчитывает Actor. У MonsterData.customStat внешний calculateDerivedStat отключает автоматические ветки также для resolve/focus.

Карточки сборки: [commonActorData](../../../commonActorData.js.md), [monsterData](../../../monsterData.js.md). [Сверка TASK-0003.006](../../../../../../../review-log.md#task-0003006).
