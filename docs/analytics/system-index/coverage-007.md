# Покрытие TASK-0006.007 — редактор ActiveEffect и мастер изменений

2026-09-15; rusbar-main, исходный HEAD 3770b84f90ed1230abba5e1f133e5ccd716be3c8. [Задача](../../tasks/task-0006.007.md), [манифест](manifest.json), [протокол](review-log.md#task-0006007).

Добавлены **132 сущности, 304 отношения и 9 процессов**. Накоплено **615 источников, 768 сущностей, 1905 отношений и 32 процесса**; 187 шагов, 269 переходов. Частичные определения имеют 120 файлов: 33 основных и 87 смежных; 495 пока без определений. Все старые ID сохранены. Уточнены класс листа ent-000446 и refs chooseSkill ent-000318; процесс назначения фазы proc-000007 используется без дублирования.

## Включённые области

| Источник | Индексированная область |
| --- | --- |
| [WitcherActiveEffectSheet.js](../../../module/activeEffect/WitcherActiveEffectSheet.js) — src-000005 | WitcherActiveEffectConfig, DEFAULT_OPTIONS/actions.wizard, прежний PARTS, TABS, _prepareContext, _onRender, wizardAction/ok.callback и autocomplete/schema callback. |
| [baseMixin.js](../../../module/activeEffect/mixins/baseMixin.js) — src-000006 | Все восемь методов; семь групп базового коллектора, пути и типы адресатов. |
| [temporaryItemImprovementMixin.js](../../../module/activeEffect/mixins/temporaryItemImprovementMixin.js) — src-000007 | Коллектор и три подсказки формул оружия. |
| [wizard.hbs](../../../templates/dialog/activeEffects/wizard.hbs) — src-000506 | select#path без name, selectOptions/selects; два разных потребителя результата. |
| [system-specific.hbs](../../../templates/sheets/activeEffect/system-specific.hbs) — src-000541 | Пять formGroup, schema/значение/имя поля и условия isItemEffect/isTemporaryItemImprovement. |
| [activeEffect.css](../../../styles/activeEffect.css) — src-000445 | 17 правил, включая вложенный h3; сопоставлены с общей разметкой effect-part, а не с core changes. |

Смежно прочитаны AE-документ и обе его модели, реестры моделей/листов, соответствующие карты config, модели адресатов и общая разметка. Новые определения за пределами основных шести файлов ограничены фабриками lifepathData/attackStats/damageModification/damageTypeModification, классом DamageProperties и конкретными полями, двумя полями WeaponData, callback chooseSkill, DOM-узлами effect-part и правилом invisible. Полный lifecycle смежных файлов не заявлен. Подключение activeEffect.css отмечено на строке 21 witcher-styles.css.

## Каталог подсказок и реальные адресаты

Все варианты имеют label/value/group. Базовый коллектор объединяет результаты spread; массив сопротивлений становится свойствами с числовыми ключами. Наличие пути в списке не является выполнением изменения Actor/Item.

| Метод и ID | Возвращаемые пути и ограничения |
| --- | --- |
| getActiveEffectsBasePaths — ent-000639 | Последовательно вызывает семь методов ниже; отдельный процесс proc-000031. |
| getStatSuggestions — ent-000640 | statMap → system.(origin).(key).totalModifiers; текущие 9 основных и 11 производных характеристик адресуют поле фабрики stat(). reputation без origin отсекается. Динамический выбор — ent-000670. |
| getToxSuggestions — ent-000641 | system.stats.toxicity.totalModifiers; числовое поле общей фабрики. |
| getSkillGroupSuggestions — ent-000642 | skillGroups → массив paths. Именованные группы читают соответствующие массивы CONFIG.WITCHER; allSkills отдельно вызывает getSkillSuggestions. HTML сериализует массив значений в строку с запятыми, wizardAction делает split. |
| getSkillSuggestions — ent-000643 | system.skills.(skill.attribute.name).(ключ skillMap).activeEffectModifiers. Из 52 текущих ключей 51 соответствует Skill; commonspeech расходится с объявленным commonsp. ent-000672 сохраняет неразрешённую цель. |
| getLifepathSuggestions — ent-000644 | attacks.strong/joint адресуют SchemaField-объекты внутри TypedObjectField, без .value; четыре остальных поля — NumberField. Произвольное наличие ключа attacks не предполагается. |
| getOtherSuggestions — ent-000645 | attackStats.meleeBonus, critLocationModifier, critEffectModifier — NumberField. |
| getDamageModifcators — ent-000646 | Ключи берутся из текущего parent.system.damageTypeModification либо parent.parent; flat/multiplication — NumberField, applyAP — BooleanField. Семь типов объявлены в общей модели; любой иной ключ остаётся динамическим. Нулевой parent не защищён вторым обращением. |
| getActiveEffectsItemImprovementPaths — ent-000647 | Один вызов getItemDamageSuggestions, отдельный каталог для type=temporaryItemImprovement. |
| getItemDamageSuggestions — ent-000648 | system.damage, system.damageProperties.oilEffect/silverDamage — StringField формул в WeaponData/DamageProperties. Наличие этих полей у любого Item не предполагается. |

Основание — [R005-02](../code-audit/cross-check-0002.md#r005-02), поздние уточнения [issue-00004](../../issues/potential/issue-00004.md#уточнение-task-0003010), [issue-00051](../../issues/potential/issue-00051.md), [issue-00052](../../issues/potential/issue-00052.md). Исторические числовые пробы аудита не запускались заново; здесь сопоставлены объявления и пути по коду.

## Форма, prepared, _source и запрос обновления

| Вход | Что читает и изменяет | Граница |
| --- | --- | --- |
| Обычная core-кнопка addChange — ent-000709 | FormDataExtended текущей формы → обработанные system.changes → начальная строка схемы → submit с updateData. | Внешнее ядро; локальных шагов с вымышленными строками нет. |
| Мастер wizardAction — ent-000697 / callback ent-000699 | Читает select#path, берёт ссылку на prepared document.system.changes (ent-000715), push добавляет только key. Отправляет корневой payload changes (ent-000718). | Несохранённая текущая форма не читается. Нет явных type/value/phase/приоритета или настройки потолка. prompt и update вызываются без await/return. |
| Создание с @skill — ent-000318 / callback ent-000736 | _preCreate перебирает _source.system.changes; при includes('@skill') ждёт chooseSkill. Тот заменяет change.key целиком строкой выбора. | render и prompt ожидаются; rejectClose=true отклоняет закрытие без OK. Перезаписывается переданная source-строка, без prepared push. |
| _preUpdate — прежние ent-000319 / proc-000007 | После super определяет phase только по data.system?.applyAfterCalculations и обходит data.system?.changes. | Корневой changes заранее переносится ядром в system.changes. Отсутствующий флаг не подставляется из сохранённого документа; system без changes может привести к ошибке обхода. Сохранение в БД не подтверждено. |

Переход callback → _preUpdate — отношение **refers** с явным внешним Document.update/cleanData; прямого локального calls нет. Позднее [уточнение issue-00043](../../issues/potential/issue-00043.md#уточнение-task-0003010) и [R005-03](../code-audit/cross-check-0002.md#r005-03) сохранены. Вход подтверждения отделён от регистрации prompt: чтения и push callback не прикреплены к шагу открытия диалога.

## Автодополнение, системная вкладка и CSS

autocomplete выбирает CONFIG.Actor или CONFIG.Item только по parent.documentName и проходит все модели этого реестра. Это 4 Actor + 22 Item регистрационных слота текущего кода; проверка transfer/текущего типа отсутствует. schema.apply пропускает SchemaField как вариант, собирает fieldPath/локализованную label, затем сортирует ключи и создаёт datalist. Runtime-ключи TypedObject без переданных данных не раскрываются. DOM меняется, документ эффекта — нет. Отсутствие нужной секции/parent/config и повторное добавление datalist остаются ограничениями.

systemFields берётся из document.system.schema.fields после await super._prepareContext. Имена input формирует core DataField.fieldPath. Поле applyAfterCalculations вызывается без условия HBS; в temporary-модели его нет, formGroup журналирует ошибку и возвращает пустой фрагмент. applySelf/applyOnTarget требуют isItemEffect; applyOnHit/applyOnDamage дополнительно требуют невременный тип. Флаг isItemEffect подготавливается core details-part; проверен полный последовательный рендер с общим context, произвольный отдельный рендер части не доказан. Отсутствующее поле отличается от отсутствующего перевода: [R005-12](../code-audit/cross-check-0002.md#r005-12), [issue-00053](../../issues/potential/issue-00053.md), [issue-00318](../../issues/potential/issue-00318.md).

activeEffect.css оформляет [effect-part.hbs](../../../templates/partials/effect-part.hbs): заголовки, строки, имя/изображение, источник, длительность, controls и описание. Правило для h4 внутри effect-name не совпадает с текущим p имени, поэтому прямое соответствие не внесено. Класс invisible определён отдельно в system-styles.css. CSS не устанавливает обработчики, не изменяет numbers/changes; категории и действия общего списка остаются TASK-0006.008. [R005-13](../code-audit/cross-check-0002.md#r005-13), [issue-00056](../../issues/potential/issue-00056.md).

## Процессы и границы

| Процесс | Локальная область |
| --- | --- |
| <a id="proc-000024"></a>proc-000024 | _prepareContext: await super → системная схема → return. |
| <a id="proc-000025"></a>proc-000025 | _onRender: super → autocomplete без await → кнопка → вставка возле core addChange. |
| <a id="proc-000026"></a>proc-000026 | Выбор base/temporary/иного типа → каталог → await render → prompt без await. Отмена не запускает callback. |
| <a id="proc-000027"></a>proc-000027 | Отдельный OK-вход: split → prepared → цикл push → запрос update без ожидания результата. |
| <a id="proc-000028"></a>proc-000028 | DOM → родитель → цикл моделей/schema → сортировка → datalist. async-метод не содержит await. |
| <a id="proc-000029"></a>proc-000029 | chooseSkill: skillMap → await render/prompt → OK или отмена → замена ключа. |
| <a id="proc-000030"></a>proc-000030 | Только цикл _preCreate строк 66–70; более ранние разрешение super и длительность — предусловия входа. |
| <a id="proc-000031"></a>proc-000031 | Семь вызовов базового коллектора, порядок spread и выход при исключении поставщика. |
| <a id="proc-000032"></a>proc-000032 | HBS: безусловный phase-formGroup → isItemEffect → self/target → временность → hit/damage. |

Все процессы partial. Не развёрнуты произвольные исключения внешних API/DOM, сохранение/синхронизация документов, browser event dispatch, длительности и категории эффектов. Отсутствие ребра при partial не доказывает отсутствие пути в системе. Применение самих бонусов относится к прежнему пилоту и последующим областям; каталог UI не меняет его семантику.

## Проверенные внешние контракты

Установленная Foundry 14.367.0. Ниже — прочитанные участки и SHA256 целого соответствующего файла на этом срезе. Они остаются внешними границами графа, не пополняют каталог 615 файлов. Стандартная check --freshness проверяет package; отдельный тест .007 сверяет эти файлы с зафиксированными отпечатками и ключевые условия. При другой установке требуется повторная проверка контракта.

| Внешний файл | Прочитанная область | SHA256 |
| --- | --- | --- |
| /opt/foundryvtt/client/applications/sheets/active-effect-config.mjs | 34–35, 80–87, 195–207, 246–266: actions, context, FormData/submit | 6384d0b979ce9daa46079450a4aab042afbff01463a4c7c86571d8cecaa605e2 |
| /opt/foundryvtt/client/data/client-backend.mjs | 214–240: cleanData до _preUpdate | 8ffe114bca601980bf2f4582ce1f6e27c555d76586470f1a16ac23f6f021b9c5 |
| /opt/foundryvtt/common/documents/active-effect.mjs | 168–184: changes → system.changes | e8a1c26a2c84e415f814146f3e632f28fe6f3504920262e324c9ef071dfc5bf5 |
| /opt/foundryvtt/common/data/active-effect.mjs | 15–24: поля строки changes | d15b7279756b40ce25c7739fa5292fc142b53e9bf948f52f6881f7ca3d2dbc54 |
| /opt/foundryvtt/client/applications/handlebars.mjs | 460–499, 531–546: selectOptions, отсутствующее поле formGroup | 0c5959e0ebdf5847277fba3284d76ee535084e022d087659fd0791e5ccd3545c |
| /opt/foundryvtt/client/applications/forms/fields.mjs | 225–235, 290–330: select и String(value) | 92e1ac0b69f0c37beeb36d9171146790c4551978e29e4e2ee9f0d0190d316202 |
| /opt/foundryvtt/client/applications/api/dialog.mjs | 264–275, 369–377, 405–424: callback, prompt, rejectClose | 4e2d299eaa931d96df1839e64a2defc60b6b95ee89a3e1d32d60b99040899343 |
| /opt/foundryvtt/client/applications/api/handlebars-application.mjs | 116–137: context и порядок PARTS | e253e0e76ab7f034f68d7055778a33e6935a7c94a6a05b0ca61188a23cea4f9d |
| /opt/foundryvtt/common/data/fields.mjs | 179–180, 633, 1370–1378, 2252–2263: fieldPath, input name, Schema/TypedObject apply | efa8e3ccdf553ca826580e60bfbfc97db57bdeadaa954a50f6a55e0ab52c3e01 |
| /opt/foundryvtt/templates/sheets/active-effect/changes.hbs | 1–16: addChange и контейнер строк | 224f1461bab80d2782e7eacd934ea66c7b53d1cefbead9d8d4db32b185b0cf49 |
| /opt/foundryvtt/templates/sheets/active-effect/change.hbs | 1–26: key/type/value/phase и имена полей | 8fb416bc61a724c95700f14490f58ba36e2e4763136a86a244cb3a283e5147e4 |

## Проверки и дальнейший остаток

[20 примеров](examples/expansion-007-queries.json) отвечают на IQ-01–IQ-08. [Тесты](tests/test_expansion_007.py) сопоставляют определения/вызовы с буквальными строками, типы адресатов, prepared/source/payload, ожидание/отмену, HBS/CSS и локальные шаги. Общий приёмочный тест проверяет оба направления всех отношений.

Фиксированные размеры .006 считаются по её исходным частям, двенадцать исторических случаев процессов — по пилотному срезу; остальные прежние проверки и новая порция используют текущий набор. Дополнения не отменяют старые доказательные случаи. Фактические результаты команд и сохранность записаны в [протоколе](review-log.md#task-0006007).

Игровой JavaScript, ядро, браузер, мир и БД не исполнялись. Аудит и issues используются как источники; их содержимое и статусы не менялись. Следующая согласованная порция — [TASK-0006.008](../../tasks/task-0006.008.md), категории, перенос и статусы эффектов.
