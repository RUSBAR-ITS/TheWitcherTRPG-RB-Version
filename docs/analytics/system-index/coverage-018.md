# TASK-0006.018 — Броня, сопротивления и износ SP

2026-09-15; rusbar-main, исходный HEAD 79a558ed3fd347d0825d91608f6669750ac0c4b6; рабочее дерево в начале чистое. [Задача](../../tasks/task-0006.018.md).

## Область и остаток

Восемь основных исходников и выбранные смежные участки. Схема v1 и CLI сохранены; общий справочник partial. Это чтение исходников и проверка индекса, без исполнения игрового сценария.

| Основной источник | Область / остаток |
| --- | --- |
| [module/actor/mixins/armorMixin.js](../../../module/actor/mixins/armorMixin.js) (src-000010) | Все 11 методов; точные callers и стыки с .017/.019. Полное сохранение SP/HP и боевой lifecycle не проверены. |
| [module/data/item/armorData.js](../../../module/data/item/armorData.js) (src-000108) | Вся схема, подготовка, getters, локальные износ/repair и миграции. Общий ремонт, мир и полный lifecycle остаются вне порции. |
| [module/data/item/templates/armor/resistanceData.js](../../../module/data/item/templates/armor/resistanceData.js) (src-000126) | Вся схема и два метода подготовки; selected OR readers/writers и формы. Браузерный submit не исполнен. |
| [module/data/item/templates/armor/spData.js](../../../module/data/item/templates/armor/spData.js) (src-000127) | Четыре поля и все методы; раздельные исходные/modified SP. Все произвольные AE и жизненный цикл ядра не раскрыты. |
| [module/item/sheets/WitcherArmorSheet.js](../../../module/item/sheets/WitcherArmorSheet.js) (src-000164) | Все локальные методы/карты, PARTS и configuration; selected diagram suppliers. Полный общий drop/ремонт остаётся вне порции. |
| [module/item/sheets/configurations/WitcherArmorConfigurationSheet.js](../../../module/item/sheets/configurations/WitcherArmorConfigurationSheet.js) (src-000182) | Весь короткий subclass и PARTS.general; общий submit/TABS переиспользуют прежние области. |
| [templates/sheets/item/armor-sheet.hbs](../../../templates/sheets/item/armor-sheet.hbs) (src-000583) | Основные SP/resistance/EV/type/location/reliability controls, effects actions и associatedDiagram подключение; полный recipe partial/чат вне порции. |
| [templates/sheets/item/configuration/tabs/armorGeneral.hbs](../../../templates/sheets/item/configuration/tabs/armorGeneral.hbs) (src-000590) | Все 12 formGroup и буквальные hints; внешний submit и реальное отображение не исполнены. |

## Контракты и существенные различия

- ArmorData.location реально StringField: повторный ключ на строке 34 заменяет ранний ArrayField. Shield — location предмета armor, а ресурс Actor shield отдельный. ArmorData не делегирует дополнительные защиты только из-за наличия DefenseProperties; прежняя граница .014/.016 сохранена.
- SpData хранит два исходных и два persisted:false modified Number без числовых ограничений. Base копирует текущий/максимум; derived при max==0 выходит, иначе добавляет stopping каждого разрешённого улучшения в оба modified поля. ResistanceData OR меняет prepared Boolean; его собственный base пуст.
- ArmorData вызывает base/derived вложенных моделей явно. ID разрешаются через parent.actor.items, неизвестные пропускаются, дубли сохраняются, system остаётся ссылкой. Free slots считают исходную длину ID, включая пустые/неразрешённые; fill({}) использует общий объект. Нет Actor и недопустимая длина Array прерывают подготовку до SP/resistance. Пустой список не сбрасывает ранее имевшийся enhancementItems в самом методе; полный reset ядра отдельно.
- EV = max(сумма encumb всех equipped armor − ignoredArmorEncumbrance,0), включая stored и Shield. SP берёт getList(armor), который исключает stored. calculateStat использует EV для REF/DEX; castSpell и магические skill checks имеют отдельные callers. Атака/защита используют уже подготовленные характеристики.
- Покрытие выбирается по modifiedMaxStoppingPower>0 каждой зоны, независимо от строки ArmorData.location и текущего SP. Несколько Light/Medium/Heavy дают уведомление и undefined; caller продолжает getArmorSp. Последний Natural выигрывает без проверки дублей. tailWing использует пустой Item-набор.
- Натуральные поля Monster читаются отдельно: head→armorHead; torso/руки→armorUpper; ноги→armorLower; tailWing→armorTailWing. Чтение использует ??0 без type-guard. Natural Item добавляется независимо от этих полей. bypassNatural убирает оба источника, bypassWorn — Light/Medium/Heavy.
- Слои берут Heavy, затем Medium, затем Light по truthy текущему SP, без сортировки по числу. Бонус абсолютной разницы двух положительных SP: 0–5→5, >5–9→4, >9–15→3, >15–20→2, >20→0; при SP<=0 →0. Light сравнивается с Medium при его наличии, иначе Heavy. Natural прибавляется целиком. Это таблица кода, не решение о правилах.
- getLocationArmor возвращает Item-ссылки armorSet и разные totalSP/displaySP; дважды вызывает getArmorSp. AP не делит SP здесь; IAP делит totalSP в calculateDamageWithLocation. Тот же consumer делит готовое текстовое displaySP, поэтому составное пояснение может дать NaN при отдельном числовом результате.
- AP/IAP немедленно обходят calculateArmorResistances и helper multiplier. Иначе multiplier читается по общему damage.type; носимая resistance[DamageInstance.type] применяется один раз, Natural resistance[damage.type] — отдельной половиной. Каждая ветка повторно умножает и округляет вниз. Без сработавшей ветки multiplier не меняет damage. Helper applyAP обращается к альтернативному damageObject.damageProperties; штатный properties отличается.
- Прямой износ берёт properties.spDamage??0 без bypassWorn/ablating/crushing; обычный сразу выходит при bypassWorn, иначе 1 либо floor(Roll(1d6/2+1)), затем crushing×2. Item-путь включает только Light/Medium/Heavy, Natural Item пропущен. Monster-путь требует type monster и !bypassNatural, ограничивает результат нулём.
- ArmorData.applySpDamage проверяет modifiedStoppingPower−урон>=0, а пишет исходный stoppingPower−урон. Превышение остатка пропускает запись; улучшение допускает запрос отрицательной базы. Ни обёртки, ни модель не ждут дочерние update. Возвращаемый размер износа и завершённая запись — разные результаты.
- В consumer SP расходуется по массиву DamageInstance; applyAlwaysSpDamage стоит до проверки полного поглощения, applySpDamage — после положительного остатка, локации и сопротивлений. В .018 добавлены интерфейс и поля этого участка; полный HP/STA, щит, allLocations и порядок сохранения остаются .019.
- Статус turnStartEffects.damage.spDamage объявлен в combatEffects, а applyCombatEffect передаёт его в plain properties при damage.amount>0. Это поле не объявлено в DamageProperties; выбранный статусный путь не создаёт DamageMessageData. Отсутствие поля в схеме сообщения не доказывает его потери здесь. Полный ход и статус остаются .020.
- Основная armor-sheet редактирует базовые SP по location и reliability для Shield; resistance-checkbox читают prepared OR. Конфигурационная armorGeneral содержит только все 12 базовых SP controls, без фильтра по location/Shield. EV/location находятся в основном листе; при постановке задачи их размещение было лишь ориентиром, фактический индекс следует исходнику.
- Контекст WitcherArmorSheet меняет общий CONFIG через ссылку super; карта armorLocations содержит Shield. PARTS конфигурации наследует свойства и заменяет general. Форма effects использует общий add/remove/edit, улучшения показывает read-only. Нового обработчика SP лист не вводит.
- Современный инвентарь читает prepared сопротивления/EV и armorPartsInfo. Helper использует modified SP, для shield — reliability fallback; пороги цвета >66/>33. Ключи чисел ног верны, ключи названий поменяны. Четыре limb hint armorGeneral отсутствуют в ru, существуют в en; это отдельные проблемы.
- Миграции работают с сырым source: append старых ID без dedup; непустой effects-массив преобразуется и тут же удаляется; truthy старые maxSP и resistance перекрывают новые значения, старые нули/false пропускаются. Локальный repair только запрашивает семь базовых максимумов; общий ремонт и перенос рецепта не считаются полностью раскрытыми.

## Доказательства и границы

Прочитаны восемь основных исходников целиком, выбранные поставщики/потребители, поздние карточки TASK-0004.006/.010 и R006-09/10, R010-14–19. Прежние опыты .014/.027/.043/.044 сохраняют даты и подмены; новых запусков JS, браузера, мира или БД нет. Связанные issues прочитаны целиком: 00007/00025/00026/00068/00077/00078/00082/00083/00084/00086/00087/00088/00089/00090 и 00277–00283. Статусы potential сохранены, новые карточки не создавались.

Внешние границы формы, DataModel, Roll и Document.update переиспользованы из проверенных предыдущих порций. Их наличие не превращает подготовленное значение, возврат Promise обёртки или именованный input в доказательство сохранения. Проверка установленного package подтверждает версию, а не весь lifecycle. Проверены также вызовы ArmorData.repair из module/item/systems/repair.js:202 (gmRepair) и 290 (restoreReliability); оба не ждут модельный Promise. Полные процессы и другие методы RepairSystem остаются вне графа этой порции. Полные произвольные consumers улучшений, рецепта, ремонта, магии и чата остаются вне этой порции.

## Процессы

<a id="proc-000231"></a>

### proc-000231 — Броня: сумма EV

Все equipped armor, включая stored/Shield; результат используется характеристиками и магическими checks.

<a id="proc-000232"></a>

### proc-000232 — Броня: набор и SP локации

location.name + properties; ссылки на Item, поля Monster и раздельные число/текст.

<a id="proc-000233"></a>

### proc-000233 — Броня: выбор класса слоя

Ссылки на последние Item; повторы носимого класса обрабатываются отдельным return undefined.

<a id="proc-000234"></a>

### proc-000234 — Броня: извлечение SP слоёв

Модельные modified значения выбранной зоны → getStackedArmorSp.

<a id="proc-000235"></a>

### proc-000235 — Броня: сочетание SP

Heavy→Medium→Light без сортировки; Natural отдельно; AP/IAP здесь не применяются.

<a id="proc-000236"></a>

### proc-000236 — Броня: бонус разницы SP

Два числа; таблица текущего кода, не проверка правила рулбука.

<a id="proc-000237"></a>

### proc-000237 — Броня: сопротивления порции

Изменяется тот же DamageInstance; afterResistance остаётся caller.

<a id="proc-000238"></a>

### proc-000238 — Броня: обычный износ SP

Обёртка возвращает размер износа, не результат сохранения; bypassWorn прекращает оба пути.

<a id="proc-000239"></a>

### proc-000239 — Броня: прямой износ SP

spDamage??0, независимо от bypassWorn/ablating/crushing; два запуска без ожидания.

<a id="proc-000240"></a>

### proc-000240 — Броня: износ предметов набора

Три носимых слоя; Natural Item не включён. Возвращается Promise<void> до дочерних записей.

<a id="proc-000241"></a>

### proc-000241 — Броня: износ полей монстра

Четыре базовых поля; torso/arms и legs делят значения.

<a id="proc-000242"></a>

### proc-000242 — ArmorData: схема брони

27 верхних полей с CommonItemData; шесть SpData и отдельная ResistanceData.

<a id="proc-000243"></a>

### proc-000243 — ArmorData: подготовка базы

Вложенные prepareBaseData вызваны явно после super.

<a id="proc-000244"></a>

### proc-000244 — ArmorData: подготовка улучшений и SP

Prepared ссылки и слоты; последующие SP/resistance зависят от успешной подготовки улучшений.

<a id="proc-000245"></a>

### proc-000245 — ArmorData: effectsWithEnhancements

Новый верхний словарь, вложенные effect записи по ссылке; без статусов Actor.

<a id="proc-000246"></a>

### proc-000246 — ArmorData: enhancementsEffects

Новый верхний словарь, вложенные effect записи по ссылке; без статусов Actor.

<a id="proc-000247"></a>

### proc-000247 — ArmorData: запрос изменения базового SP

Guard modified, цель исходная; превышение остатка полностью пропускает update.

<a id="proc-000248"></a>

### proc-000248 — ArmorData: признак повреждения

Локальный getter; не исполнение ремонта/разрешение UUID.

<a id="proc-000249"></a>

### proc-000249 — ArmorData: локальная запись максимумов

Только метод модели; общий RepairSystem остаётся вне .018.

<a id="proc-000250"></a>

### proc-000250 — ArmorData: вход миграции

Мутация сырого source; не изменение уже созданного документа.

<a id="proc-000251"></a>

### proc-000251 — ArmorData: перенос прежних effects

Только непустой Array; современный словарь и пустой Array ветку пропускают.

<a id="proc-000252"></a>

### proc-000252 — ArmorData: перенос шести старых SP

Шесть независимых if, не произвольная новая миграция данных мира.

<a id="proc-000253"></a>

### proc-000253 — ArmorData: перенос старых сопротивлений

Truthy старые значения имеют приоритет; false оставляется прежним ключом.

<a id="proc-000254"></a>

### proc-000254 — SpData: исходные и вычисленные поля

Два базовых и два persisted:false Number; без min/max.

<a id="proc-000255"></a>

### proc-000255 — SpData: сброс вычисленных SP

Копирование базы, без Document.update.

<a id="proc-000256"></a>

### proc-000256 — SpData: прибавление улучшений

Изменение только modified полей; parent — ArmorData.

<a id="proc-000257"></a>

### proc-000257 — ResistanceData: три физических сопротивления

Boolean initial: false, общая модель всех экземпляров брони.

<a id="proc-000258"></a>

### proc-000258 — ResistanceData: пустая базовая подготовка

Метод пуст; сам не восстанавливает source и не очищает OR.

<a id="proc-000259"></a>

### proc-000259 — ResistanceData: OR улучшений

Prepared флаги; базовый/source результат не переписывается этим методом.

<a id="proc-000260"></a>

### proc-000260 — Лист брони: контекст

super передаёт CONFIG по ссылке; собственные карты используются основной формой.

<a id="proc-000261"></a>

### proc-000261 — Лист брони: getTypes

Возвращает локальный объект значений и ключей локализации.

<a id="proc-000262"></a>

### proc-000262 — Лист брони: getArmorLocations

Возвращает локальный объект значений и ключей локализации.

<a id="proc-000263"></a>

### proc-000263 — Лист брони: установка recipe listener

Только вход associatedDiagram, общая lifecycle _onRender переиспользована.

<a id="proc-000264"></a>

### proc-000264 — Лист брони: передача рецепта

armor/elderfolk-armor, вызов без ожидания; полный общий drop вне .018.

<a id="proc-000265"></a>

### proc-000265 — Форма брони: базовые SP и надёжность

Видимость по строковому location, не критерий защиты Actor.

<a id="proc-000266"></a>

### proc-000266 — Конфигурация брони: все исходные SP

12 formGroup независимо от location; поля EV/location отсутствуют в этом шаблоне.

<a id="proc-000267"></a>

### proc-000267 — Инвентарь: подсказки состояния брони

Modified SP и отдельный shield/reliability fallback; не расчёт поглощения.

<a id="proc-000268"></a>

### proc-000268 — Урон: получение множителя сопротивлений

Общий тип damageObject; helper сам не меняет DamageInstance.

## Проверки

Пройдены все 143 тестовых метода (unittest, 980.173 с), включая 32 новых CLI-случая; накоплено 389 CLI-примеров. Это проверки справочника по исходникам, без исполнения игрового сценария.

~~~bash
python3 -B -m unittest discover -s docs/analytics/system-index/tests -v
python3 -B docs/analytics/system-index/query.py check --freshness --format json
git diff --check
~~~

До общего прогона прошли все 32 новых ожидания поиска и восемь отдельных проверок новой порции: схемы/владельцы, порядок подготовки, source-миграции, EV/отбор/слои, сопротивления/износ/ожидания, формы/инвентарь, интерфейс damage/status и накопленный граф.

Прежние 357 поисковых примеров сопоставлены с предыдущим набором; проверяемые списки ID и концов связей не изменились. Численные итоги .017 сохранены в её тесте как исторический диапазон ID, содержательные проверки сохранены. На итоговой сверке добавлены два буквальных include основной формы и уточнён тип связи создания configuration; затем повторены предварительные проверки. Полный прогон выполнен после всех изменений данных/тестов.

Проверены обе стороны всех 10834 отношений, принадлежность шагов/отношений, достижимость выходов и три аспекта покрытия 615 sources. Ссылки, окончательная актуальность и сохранность после обновления навигации записаны в журнале. Браузер, JavaScript боя, БД и порядок подтверждения записей этими тестами не исполняются.


## Итог и следующая порция

Добавлены 139 сущностей, 821 отношение и 38 процессов; восемь новых динамических границ. Накоплено 4330 сущностей, 10834 связи и 268 процессов (923 шага, 1645 переходов); 292 границы. Определения есть в 235/615 файлах: два словаря complete по строковым ключам, 233 файла partial; роли 119 основных/116 смежных, 380 без определений.

TASK-0006.018 done; следующая — [TASK-0006.019](../../tasks/task-0006.019.md), применение урона, щит и изменение ресурсов. Родитель остаётся in-progress. Окончательная сверка — в [журнале](review-log.md#task-0006018).
