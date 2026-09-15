# TASK-0006.014 — Настройки оружия, атаки, защиты и свойств урона

2026-09-15, rusbar-main, исходный HEAD db4a9d63faabdfe75227f6f77d24d768c66b6571. Рабочее дерево в начале чистое. [Задача](../../tasks/task-0006.014.md).

## Область и остаток

Справочник текущего кода; схема v1 и CLI сохранены. Изучены 14 основных исходников и выбранные смежные участки. Все новые области partial; определение не означает полного перечня callers.

| Основной исходник | Остаток |
| --- | --- |
| [module/data/item/weaponData.js](../../../module/data/item/weaponData.js) (src-000155) | Схема/подготовка/миграция/выбранные getters раскрыты; repair и содержимое связанных рецептов, все callers и lifecycle остаются частичными. |
| [module/data/item/templates/combat/attackOptionsData.js](../../../module/data/item/templates/combat/attackOptionsData.js) (src-000129) | Фабрика/default callbacks и выбранные UI/consumers раскрыты; не все включения схемы, очистка ядра и внешние модули. |
| [module/data/item/templates/combat/skillAttackData.js](../../../module/data/item/templates/combat/skillAttackData.js) (src-000133) | Выбранные объявления/поля/формы/локальные операции раскрыты; полные callers, внешний lifecycle и бой остаются partial. Бой .015–.019, Armor SP .018, рецепты и прочие Item вне .014. |
| [module/data/item/templates/combat/damagePropertiesData.js](../../../module/data/item/templates/combat/damagePropertiesData.js) (src-000130) | Поля и локальные getters/migrations раскрыты; все consumers урона, сериализация сообщения и сохранение мира не развёрнуты. |
| [module/data/item/templates/combat/defenseOptionsData.js](../../../module/data/item/templates/combat/defenseOptionsData.js) (src-000131) | Выбранные объявления/поля/формы/локальные операции раскрыты; полные callers, внешний lifecycle и бой остаются partial. Бой .015–.019, Armor SP .018, рецепты и прочие Item вне .014. |
| [module/data/item/templates/combat/defensePropertiesData.js](../../../module/data/item/templates/combat/defensePropertiesData.js) (src-000132) | Выбранные объявления/поля/формы/локальные операции раскрыты; полные callers, внешний lifecycle и бой остаются partial. Бой .015–.019, Armor SP .018, рецепты и прочие Item вне .014. |
| [module/data/item/templates/combat/skillDefenseData.js](../../../module/data/item/templates/combat/skillDefenseData.js) (src-000134) | Выбранные объявления/поля/формы/локальные операции раскрыты; полные callers, внешний lifecycle и бой остаются partial. Бой .015–.019, Armor SP .018, рецепты и прочие Item вне .014. |
| [module/item/sheets/WitcherWeaponSheet.js](../../../module/item/sheets/WitcherWeaponSheet.js) (src-000181) | Выбранные объявления/поля/формы/локальные операции раскрыты; полные callers, внешний lifecycle и бой остаются partial. Бой .015–.019, Armor SP .018, рецепты и прочие Item вне .014. |
| [module/item/sheets/configurations/WitcherConfigurationSheet.js](../../../module/item/sheets/configurations/WitcherConfigurationSheet.js) (src-000183) | Контекст/AE переиспользованы, добавлены form/PARTS; унаследованный submit внешняя граница, прочие наследники частичны. |
| [module/item/sheets/configurations/WitcherPropertiesConfigurationSheet.js](../../../module/item/sheets/configurations/WitcherPropertiesConfigurationSheet.js) (src-000186) | Выбранные объявления/поля/формы/локальные операции раскрыты; полные callers, внешний lifecycle и бой остаются partial. Бой .015–.019, Armor SP .018, рецепты и прочие Item вне .014. |
| [templates/sheets/item/configuration/partials/attackOptionsPart.hbs](../../../templates/sheets/item/configuration/partials/attackOptionsPart.hbs) (src-000585) | Семь controls и включение spellGeneral; общий general — отдельная разметка. Полные callers и локализация вне .014. |
| [templates/sheets/item/configuration/tabs/damagePropertiesConfiguration.hbs](../../../templates/sheets/item/configuration/tabs/damagePropertiesConfiguration.hbs) (src-000592) | Выбранные объявления/поля/формы/локальные операции раскрыты; полные callers, внешний lifecycle и бой остаются partial. Бой .015–.019, Armor SP .018, рецепты и прочие Item вне .014. |
| [templates/sheets/item/configuration/tabs/defensePropertiesConfiguration.hbs](../../../templates/sheets/item/configuration/tabs/defensePropertiesConfiguration.hbs) (src-000593) | Выбранные объявления/поля/формы/локальные операции раскрыты; полные callers, внешний lifecycle и бой остаются partial. Бой .015–.019, Armor SP .018, рецепты и прочие Item вне .014. |
| [templates/sheets/item/weapon-sheet.hbs](../../../templates/sheets/item/weapon-sheet.hbs) (src-000613) | Выбранные объявления/поля/формы/локальные операции раскрыты; полные callers, внешний lifecycle и бой остаются partial. Бой .015–.019, Armor SP .018, рецепты и прочие Item вне .014. |

## Различия, существенные для поиска

- Реальные классы называются DamageProperties и DefenseProperties. attackOptions/defenseOptions/skillAttack/skillDefense — фабрики схем. Defaults не являются отдельным prepare-методом. label/hint остаются метаданными.
- attackOptions и defenseOptions — SetField непустых строк без choices. Настройки UI предлагают config значения, но не ограничивают ими схему. Явный пустой Set сохраняется; getItemAttack не превращает его в none, как отсутствие поля.
- initial attackOptions собирает melee/ranged/spell по legacy attackSkill, isThrowable и level. Очистка ядра удаляет неизвестный attackSkill до defaults. Spell default spellcasting отличается от config spellcast; полный getUsedSkill магии здесь не переопределяется.
- Локальный getItemAttack использует порядок Set: default0, shift1, alt2, ctrl3 с ограничением размером. Truthy дополнительные options без клавиш могут оставить индекс NaN. Полный weaponAttack и защита остаются .015/.016.
- WeaponData включает общие attack/defense фабрики и отдельные embedded models. skillAttack не включает defenseProperties, skillDefense включает. Armor имеет defenseProperties, но не делегирующие методы отбора; штатный shield путь отдельный.
- WeaponData.createDefenseOption выбирает навык через ??, поэтому пустая строка блокирует fallback. DefenseProperties проверяет только defendsAgainst.has и возвращает modifier/пустые skills/itemTypes; isDefense не является его guard.
- Weapon prepared enhancementItems разрешается через actor.items, требует владельца при непустых IDs, сохраняет повторы и live system. Миграция дописывает старые IDs без дедупликации. Recipe helper адресован границей, repair не развёрнут.
- DamageProperties.effects — TypedObjectField со словарным ключом ID; itemEffect не содержит id. Это отличается от массивов расходника .013. addEffects мутирует prepared словарь, правый ключ заменяет левый; createBaseDamageObject отдаёт модель по ссылке.
- getPreprocessedEffects создаёт массив shallow copies; объединяет только truthy одинаковый статус, складывает percentage без clamp, остальные свойства остаются от первой записи. Последующая типизация сообщения и реальное применение .017–.019 не объявлены исполненными.
- Миграция урона переносит truthy старые поля поверх nested, включая пустой массив effects. Вложенная миграция переводит только непустой массив в словарь randomID. Static WeaponData.this.effects не равен sourceData.effects.
- mergeDamageProperties последовательно выполняет AP/IAP ветви, затем primitive/Array merge. TypedObject effects пропускается. Отдельный addEffects вызывается для ammo/улучшений, но не внутри этого helper.
- WeaponSheet.configuration → PropertiesConfiguration → общий general.hbs. general не включает attackOptionsPart; его включает spellGeneral специализированной конфигурации. Обе формы не имеют itemUseAttackSkill, spell-заголовок partial правильный; у general используется ranged.
- Именованные schema controls сохраняет унаследованная форма. Ручные effects rows не имеют name: dataset.target/field и ключ строки поступают в _onChangeForm → _onEditEffect → update dot-path. Числовая строка проходит внешнюю очистку; on заменяется checked. Добавление percentage:0, удаление target.-=id:null, без await.
- Улучшения в damagePropertiesConfiguration показаны disabled, отдельными писателями не являются. Silver controls зависят от настройки мира; varEffect от staminaIsVar. Наличие поля/галочки не доказывает поддержку расчёта, в частности applyRangedMeleeBonus не имеет отдельного module consumer.
- Навигация и PARTS фильтруются отдельно: damage PART имеет дополнительный causeDamages guard, region PART читает устаревший верхний createTemplate. Эти callbacks не вызываются последовательно из _prepareContext.
- Тип урона Weapon редактируется отдельным change .damage-type: Bool инвертируется по id, text собирается через localize, update всей копии system.type не ожидается. Контролы без name не приписаны обычному submit.

## Доказательства и границы

Сопоставлены текущие исходники, поздние карточки TASK-0004.006 и R006-03–08. Прочитаны связанные issues 00060/00061/00064/00065/00066/00067/00068/00069/00070/00071/00072/00073/00074/00075/00077/00078/00079/00085/00264 с поздними уточнениями. Их даты, потенциал и пределы прежних опытов сохранены; новые игровые опыты и исправления не выполнялись. Issues 00071/00072/00073/00075/00085 адресуют соседние границы, а не обещание полного процесса профессии/региона/урона.

Смежные источники: weaponType/itemEffect, damagePropertiesMigration, professionSkill inclusion, config maps, Item getItemAttack, weaponAttack merge и выбранные calls, Item damageUtil producer/вход preprocessing, Item/Actor defense entry, Armor поле, general/spellGeneral и специализированная spell конфигурация. Полные рецепты, прочие Item, боевые формулы/chooser/применение урона вне этой порции.

Ядро Foundry 14.367.0 — внешние границы. Локально сверена очистка SchemaField до initial и поддержка -=null; сохранение формы переиспользует прежний внешний контракт.

| Путь ядра | Участок | SHA-256 |
| --- | --- | --- |
| /opt/foundryvtt/common/data/fields.mjs | 1073–1085, 1109–1143: clean/prune, legacy ForcedDeletion | efa8e3ccdf553ca826580e60bfbfc97db57bdeadaa954a50f6a55e0ab52c3e01 |

## Процессы

<a id="proc-000156"></a>

### proc-000156 — Схема атаки: defaults и граница legacy очистки

Ядро запрашивает initial поля attackOptions; source.attackSkill мог быть удалён перед callback.

<a id="proc-000157"></a>

### proc-000157 — Схема защиты: начальный набор вариантов

initial SetField defenseOptions; явно пустое значение не заменяется.

<a id="proc-000158"></a>

### proc-000158 — Оружие: подготовленные улучшения

Локальная подготовка модели; рецепты только вызов границы, БД не пишется.

<a id="proc-000159"></a>

### proc-000159 — Оружие: миграция смешанного source

migrateData(sourceData), не повторный update документа.

<a id="proc-000160"></a>

### proc-000160 — Свойства урона: перенос прежних полей

Прямой migrateDamageProperties; старые ключи не удаляются локально.

<a id="proc-000161"></a>

### proc-000161 — Воздействия урона: массив в словарь

До типизированной очистки effects; пустой Array здесь не преобразуется.

<a id="proc-000162"></a>

### proc-000162 — Свойства урона: добавить словарь воздействий

Мутация prepared модели; не update или создание ActiveEffect.

<a id="proc-000163"></a>

### proc-000163 — Свойства урона: словарь воздействий улучшений

Prepared getter читает parent.enhancementItems; UI показывает результат disabled.

<a id="proc-000164"></a>

### proc-000164 — Свойства урона: группировка воздействий по статусу

Локальный массив копий для rollDamage; последующая очистка сообщения вне порции.

<a id="proc-000165"></a>

### proc-000165 — Оружие: дополнительный вариант защиты

Локальный producer skills/modifier; не chooser защиты.

<a id="proc-000166"></a>

### proc-000166 — Лист оружия: изменение типа урона

change .damage-type; отсутствие name компенсирует отдельный listener.

<a id="proc-000167"></a>

### proc-000167 — Конфигурация свойств: контекст и доступность частей

Application callbacks подготовки контекста; _prepareTabs/_configureRenderParts вызываются ядром отдельно, не из _prepareContext.

<a id="proc-000168"></a>

### proc-000168 — Конфигурация свойств: вкладки

Ядро вызывает _prepareTabs(group); только primary фильтруется.

<a id="proc-000169"></a>

### proc-000169 — Конфигурация свойств: рендеримые части

Ядро вызывает _configureRenderParts; условия отличаются от навигационных.

<a id="proc-000170"></a>

### proc-000170 — Редактор урона: добавить запись словаря

Action addEffect; dataset.target=system.damageProperties.effects.

<a id="proc-000171"></a>

### proc-000171 — Редактор урона: изменить поле записи

_onChangeForm вызывает handler для editEffect; ключ из .list-item, не поиск по effect.id.

<a id="proc-000172"></a>

### proc-000172 — Редактор урона: удалить ключ словаря

Action removeEffect; legacy ForcedDeletion синтаксис поддерживается текущим ядром.

<a id="proc-000173"></a>

### proc-000173 — Item: выбор варианта и payload атаки

Локальный getItemAttack, полный weaponAttack остаётся .015.

<a id="proc-000174"></a>

### proc-000174 — Оружейный потребитель: слияние дополнительных свойств

Только локальный helper; порядок AP/IAP сохраняется, полного оружейного броска здесь нет.

<a id="proc-000175"></a>

### proc-000175 — Item: базовый объект урона

Producer для weaponAttack: prepared ссылки, не независимая модель атаки.

<a id="proc-000176"></a>

### proc-000176 — Конфигурация: именованные поля и внешнее сохранение

Именованные controls general.hbs; manual effects/type controls идут отдельными обработчиками. Внутренний submit ядра не раскрыт.

## Проверки

Пройдены 111 тестовых методов (unittest, 550.549 с), включая 26 новых CLI-случаев; накоплено 273 CLI-примера. После переиспользования прежнего узла сохранения формы повторно пройдены все 7 тестов .014 (57.587 с), включая те же 26 запросов. Это проверки справочника, без исполнения игрового сценария.

~~~bash
python3 -B -m unittest discover -s docs/analytics/system-index/tests -v
python3 -B docs/analytics/system-index/query.py check --freshness --format json
git diff --check
~~~

Сверены декларации полей/владельцев, точные строки вызовов и записей, разделение schema/source/prepared/payload, формы general/attackOptionsPart, словарь effects и массив расходника. Проверены 8995 отношений в обоих направлениях, диапазоны строк, участие в процессах, достижимость всех шагов/выходов новых процессов и три аспекта покрытия каждого source.

Предварительные проверки исправили в самом индексе вид action-узла на поддерживаемый event, вид внешнего выхода, соседние номера строк вызовов, поле prepared enhancementItems.id и переход цикла без повторного сброса массива. Тест literal исправлен на фактический existingStatus. Поиск DefenseProperties ограничен kind=class, а aliases controls содержат полный путь system.damageProperties/defenseProperties. Новый дублирующий внешний узел сохранения формы удалён из неопубликованной части; связи и шаг используют прежний ent-000910 DocumentSheetV2.#onSubmitDocumentForm. ID прежних порций и счётчик следующего ID сохранены. Эти изменения не затрагивают код системы. Численный итог .013 проверяется отдельно по его историческому диапазону ID; прежние семантические проверки сохранены.

Сохранение формы и TypedObject очистка — внешние контракты. Работа DOM, мира/БД, нескольких клиентов и соответствие чисел книгам правил не проверялись.


## Итог и следующая порция

Добавлены 197 сущностей, 536 отношений, 21 процесс. Накоплено 3893 сущности, 8995 связей и 176 процессов (631 шаг, 1063 перехода). Определения есть в 213/615 файлах: два словаря complete по строковым ключам, 211 файлов partial; роли 88 основных/125 смежных, 402 без определений.

TASK-0006.014 done; следующая — [TASK-0006.015](../../tasks/task-0006.015.md), оружейная атака. Родитель остаётся in-progress. Проверки сохранности и финальная актуальность записаны в [журнале](review-log.md#task-0006014).
