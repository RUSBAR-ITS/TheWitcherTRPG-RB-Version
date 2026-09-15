# Покрытие TASK-0006.009 — текущие и старые входы навыка

2026-09-15; rusbar-main, исходный HEAD 135c66796ae69f62ee8f9954e8c37c484acda59b. [Задача](../../tasks/task-0006.009.md), [манифест](manifest.json), [протокол](review-log.md#task-0006009).

Добавлены **56 сущностей, 188 отношений и 14 процессов**. Накоплено **615 источников, 935 сущностей, 2399 отношений и 63 процесса**; 316 шагов и 476 переходов. Частичные определения имеют 142 файла: 50 основных и 92 смежных; 473 пока без определений. Границ — 185, из них 17 новых. Старые ID сохранены; формулы бросков и proc-000009–000013 повторно не созданы.

## Включённые области

| Основной источник | Область |
| --- | --- |
| [WitcherActorSheet.js](../../../module/actor/sheets/WitcherActorSheet.js) — src-000027 | DEFAULT_OPTIONS.form, prepared system, _prepareCustomSkills, _onRender, skill/custom listeners и их примеси. Прежние effects/HP сохранены. |
| [WitcherActorSheetV1.js](../../../module/actor/sheets/WitcherActorSheetV1.js) — src-000028 | getData, toObject(false), отдельная группировка, html[0] listeners; отсутствие собственного template/PARTS и текущей регистрации. |
| [WitcherCharacterSheet.js](../../../module/actor/sheets/WitcherCharacterSheet.js) — src-000029 | Унаследованные context/listeners, PARTS.skills/TABS.skillTabs и context.skillTabs. Прочие helpers частичны. |
| [WitcherMonsterSheet.js](../../../module/actor/sheets/WitcherMonsterSheet.js) — src-000031 | Тот же общий skills PARTS, TABS/context.skillTabs и унаследованный listener. Экспорт добычи вне порции. |
| [WitcherSkillItemSheet.js](../../../module/item/sheets/WitcherSkillItemSheet.js) — src-000178 | DEFAULT_OPTIONS.form, PARTS.main, весь _prepareContext, stats/item/system. |
| [skill-display.hbs](../../../templates/partials/character/skill-display.hbs) — src-000522 | Hash Skill/name/stat, modifiedValue, label, флаги и DOM-команда. |
| [custom-skill-display.hbs](../../../templates/partials/character/custom-skill-display.hbs) — src-000521 | Текущий Item-context без hash, отсутствующий skill.*, Item.name в builtin-команде. |
| [tab-skills.hbs](../../../templates/partials/character/tab-skills.hbs) — src-000527 | Навигация и два прохода групп/Items, строки 1–54. openModifiers/IP — границы следующих областей. |
| [skill-item-sheet.hbs](../../../templates/sheets/item/skill-item-sheet.hbs) — src-000610 | Имя документа и select атрибута; внешняя граница submit. |

Смежно проверены обе skillMixin, customSkillMixin, Skill/SkillItemData/семь групп skills, statMap/регистратор листов, preload шаблонов, старые monster partial и включение старого monster-sheet на строке 289. У customSkillMixin в .009 раскрыт только listener броска; прочие пять подписок собраны в границу ent-000905 для .010. Старые HBS прочитаны ради подключения, Item-контекста и readonly данных, без полного индексирования всех редактирующих действий.

## Регистрация и контекст

Character и Monster зарегистрированы как default листы соответствующих типов; оба наследуют WitcherActorSheet и выбирают character/tab-skills через PARTS.skills. Эти буквальные ссылки уже были внесены в .006 и сохранены как refers: наличие адреса PARTS не означает вызова render. Внешний HandlebarsApplicationMixin исполняет выбранные части с подготовленным контекстом.

WitcherActorSheet._onRender ожидает super, затем вызывает virtual activateListeners. У Character сначала выполняется override, который вызывает base; Monster наследует base напрямую. В base skillListener и customSkillListener получают this.element. У V1 те же примеси получают html[0], но импортов/регистрации V1 в текущем module не найдено; своего template/PARTS в классе нет. Старый monster-sheet предзагружается и включает старый monster-skill-tab, однако не приписан V1 автоматически.

| Producer | Данные и различие |
| --- | --- |
| Базовый V2 context | context.system — ссылка на подготовленный actor.system. Отдельный context.items исключает isStored, но группировщик навыков его не использует. |
| V1 getData | system из actor.toObject(false); группировка всё равно читает this.actor.items. |
| _prepareCustomSkills V2/V1 | Все Items type=skill; девять statMap.name при origin=stats; строгий system.attribute===stat; без проверки stored/сортировки. |
| SkillItemSheet context.stats | Девять записей той же карты по исходным ключам, значения переданы по ссылке. |
| Общий tab-skills | Два прохода семи system.skills: int/ref/dex/body/emp/cra/will. В каждом lookup customSkills по ключу группы. spd/luck не выводятся, неизвестный attribute не попадает в подготовленные группы. |
| Character/Monster skillTabs | all, семь групп, ip; это девять элементов навигации, а не девять встроенных групп навыков. |

Основание: [R002-03](../code-audit/cross-check-0002.md#r002-03), [R004-06](../code-audit/cross-check-0002.md#r004-06), [issue-00188](../../issues/potential/issue-00188.md). Пользовательский выбор листа, внешний override и реальный браузерный lifecycle не исполнялись.

## Три строки и два маршрута броска

| Строка | Контекст и представление | Команда и продолжение |
| --- | --- | --- |
| Текущая builtin — ent-000915 | Hash skill/name/stat задан явно на строках 21/45 родителя. Показывает Skill.label/modifiedValue и три флага; isVisible не читает. | data-action=rollSkill, data-skill=name. Прежний ent-000382 выбирает skillMap[key]; proc-000009 → proc-000011. data-stat callback не читает. |
| Текущая custom — ent-000916 | Родитель вызывает partial на Item без hash на 25/49. skill.label/value/флаги не предоставлены; stat отсутствует, name берётся из документа. | Тот же rollSkill с Item.name. Обычное имя не даёт entry, совпавшее адресует builtin. Нет .item/data-item-id/#custom-rollable. |
| Старая custom — ent-000919 | .item/data-item-id={{id}}; name и system.*. Один из трёх td#custom-rollable определяется флагами. | customSkillListener привязывает Actor.rollCustomSkillCheck через bind; event.currentTarget.closest('.item').dataset.itemId адресует Item. Продолжение — прежний proc-000013. |

Отсутствующий hash — граница ent-000923; неподготовленный skill.* — ent-000928. Они не подменяются полями SkillItemData. Для неизвестного имени builtin-метод отклоняет Promise при чтении skillMapEntry.attribute; вызов из DOM не ждёт результата. Совпадение Item.name со встроенным ключом не является выбором Item по ID.

Прямой rollCustomSkillCheck — другое наблюдение: читает Item.system.value и attribute, но addActiveEffects получает Item.name. Его собственный activeEffectModifiers не читается. Эта формула уже раскрыта в пилоте; наличие старого readonly вывода не доказывает включения добавки в бросок. Подробности: [R004-07](../code-audit/cross-check-0002.md#r004-07), [issue-00187](../../issues/potential/issue-00187.md), [issue-00190](../../issues/potential/issue-00190.md).

skillListener присваивает jQuery без локального объявления; customSkillListener локально заменяет параметр html. Это прежнее наблюдение [R004-10](../code-audit/cross-check-0002.md#r004-10); порядок вызовов сохранён. Полный браузерный эффект повторной регистрации не воспроизводился.

## Форма Item и границы редактирования

SkillItemData содержит восемь полей: attribute, value, label, isOpened, activeEffectModifiers, isProfession/isPickup/isLearned. Имя и ID принадлежат документу. Схема не задаёт modifiedValue/modifiers/isVisible; числовые поля без min/max/integer, attribute — StringField без choices.

Форма содержит ровно два управляющих name: name и system.attribute. Для selectOptions передаются stats, selected=item.system.attribute и localize=true; ядро использует ключ объекта как option.value, label берёт из записи. Наличие остальных полей в модели не делает их редактируемыми в этой форме.

DEFAULT_OPTIONS включает submitOnChange=true и closeOnSubmit=false. Своего handler, кнопки submit и локального вызова Item.update нет. Установленный DocumentSheetV2 проверяет isEditable, разворачивает formData.object, валидирует и ожидает _processSubmitData. Существующий документ обновляется; для несохранённого действует ветка canCreate/ошибки. Это внешний контракт, не подтверждение сохранения из одного HBS/input.

openModifiers, повышение, собственные модификаторы и IP/training остаются следующими областями. Readonly totalSkills/totalProfSkills и старый activeEffectModifiers не записывают значения при рендере. [R004-08](../code-audit/cross-check-0002.md#r004-08), [issue-00189](../../issues/potential/issue-00189.md), [issue-00192](../../issues/potential/issue-00192.md#дополнительная-сверка-task-0003032). Семь переводов WITCHER.Actor.Skill.* не объявлены отсутствующими; позднее исправление [issue-00193](../../issues/potential/issue-00193.md) прочитано, en/ru подробно остаются .011.

## Процессы и границы

| Процесс | Выбранный участок |
| --- | --- |
| <a id="proc-000050"></a>proc-000050 | V2: группировка собственных навыков. Группируются все Actor Items skill, а не context.items; собственная сортировка/isStored отсутствуют. |
| <a id="proc-000051"></a>proc-000051 | V1: старая группировка собственных навыков. Синхронная копия группировки; наличие файла не доказывает активного листа. |
| <a id="proc-000052"></a>proc-000052 | V2: подготовка входных данных навыков. Только69–79: prepared system, отдельный context.items и await группировки; весь prepare с effects/gear не дублируется. |
| <a id="proc-000053"></a>proc-000053 | V2: от рендера к virtual listener. Inherited method вызывает virtual activateListeners: Character override→base, Monster→base; неизвестные override динамические. |
| <a id="proc-000054"></a>proc-000054 | V2: подключение двух listeners навыка. Только два вызова; skillListener захватывает actor/map и меняет глобальный jQuery. Выполнение click отдельно в proc-000009/000011/000013. |
| <a id="proc-000055"></a>proc-000055 | Item skill: контекст формы и девять характеристик. Прикладной метод не сохраняет Item; Object записи statMap передаются по ссылке. Нет ограничения attribute по схеме StringField. |
| <a id="proc-000056"></a>proc-000056 | Общий tab: встроенные группы и собственные Items. Фрагмент1–54; IP56–108 вне процесса. Все/по-группам выводят одни данные повторно; spd/luck не входят в system.skills. |
| <a id="proc-000057"></a>proc-000057 | Текущая строка встроенного Skill. Только отображение и DOM-команда; щелчок выполняется прежним proc-000009, формула proc-000011. isVisible не проверяется. |
| <a id="proc-000058"></a>proc-000058 | Текущая строка Item: несовпавший DOM-контракт. data-skill получает Item.name, skill.* и stat отсутствуют. Отдельного Item ID/старого selector нет; builtin callback продолжает proc-000009/000011. |
| <a id="proc-000059"></a>proc-000059 | Старая строка Item: ID и команда собственного броска. У текущих Character/Monster PARTS другой tab. Этот процесс не доказывает его достижимости из зарегистрированного листа; дальнейший бросок proc-000013. |
| <a id="proc-000060"></a>proc-000060 | Старый selector: привязка события к Actor-методу. Начальный фрагмент2–6; при отсутствии #custom-rollable подписка не делает текущий custom partial рабочим. Остальные операции .010. |
| <a id="proc-000061"></a>proc-000061 | Item skill: поля формы до внешнего submit. Локальных вызовов document.update нет. Change→FormData/expand/validate/submit — внешний DocumentSheetV2 с isEditable и create/update ветвями. |
| <a id="proc-000062"></a>proc-000062 | Character: контекст навигации навыков. Только primary/skillTabs; продолжение подготовки прочих полей вне процесса. |
| <a id="proc-000063"></a>proc-000063 | Monster: контекст навигации навыков. Только primary/skillTabs; продолжение подготовки прочих полей вне процесса. |

Все новые процессы partial. Регистрация, выбор PARTS, render, установка listener и click разделены; источники core не получают вымышленных локальных строк. Процессы строк заканчиваются DOM-границей, callback/roll уже представлены прежними proc-000009/000011/000013. Чужое/пустое имя, отсутствующие hash/attribute, неизвестный Item и неполный внешний контекст описаны как ограничения; новый браузерный прогон не заявлен.

## Проверенные внешние контракты

Foundry 14.367.0. SHA256 относится ко всему файлу; ниже перечислены прочитанные участки. Каталог системы остаётся 615, исходники ядра представлены внешними границами. check --freshness проверяет package, отдельный тест .009 — перечисленные файлы.

| Внешний файл | Прочитанная область | SHA256 |
| --- | --- | --- |
| /opt/foundryvtt/client/applications/api/document-sheet.mjs | 50–68, 172–185, 465–544: handler, context, guard, validate и create/update | 7925d81900eeea0d5e79606e12ce43539ae00714f50d8452c7305fe81394aa01 |
| /opt/foundryvtt/client/applications/api/application.mjs | 704–727, 1610–1630, 1931–1941, 1974–1981, 2134–2162: tabs/click, submit/change, ожидание handler и catch | b5aef80d3e042a4a856be9dd875c72a5224988d62046ba770f25376f4291faa0 |
| /opt/foundryvtt/client/applications/handlebars.mjs | 460–499: selectOptions, ключ/запись и локализация | 0c5959e0ebdf5847277fba3284d76ee535084e022d087659fd0791e5ccd3545c |
| /opt/foundryvtt/client/applications/api/handlebars-application.mjs | 116–137: PARTS и последовательный part context/render | e253e0e76ab7f034f68d7055778a33e6935a7c94a6a05b0ca61188a23cea4f9d |
| /opt/foundryvtt/client/applications/sheets/item-sheet.mjs | 1–32: наследование DocumentSheetV2, item/actor getters | 20a6427810422668d19dafcea1418d68b5faf4d9ef96b8196a2e1bc6b5e236cb |
| /opt/foundryvtt/client/applications/sheets/actor-sheet.mjs | 1–65, 131–134: наследование DocumentSheetV2, actor getter и super/dragDrop после render | 060e65ed9746a1ade375e61b45330dd083b3102c73d5be8b16e6637c2a89350b |

## Проверки и дальнейший остаток

[22 примера](examples/expansion-009-queries.json) и [тесты](tests/test_expansion_009.py) сверяют определения/адреса, обе стороны связей, PARTS против preload, девять/семь групп, hash/dataset, имя/ID, старую подписку, form-поля и внешние контракты. Ожидания заданы по исходникам, не скопированы из CLI.

Размеры .008 проверяются на её исторических частях; прежние случаи сохранены, включая A23/P13 на пилотном срезе. Формулы игровых бросков не исполнялись. Фактические команды, результаты и сохранность — в [протоколе](review-log.md#task-0006009).

Исходники системы, ядро, мир, БД, сеть, аудит/issues и их статусы не менялись. Следующая согласованная порция — [TASK-0006.010](../../tasks/task-0006.010.md), редактирование характеристик и навыков.
