# TASK-0006.031 — Магические Item, редакторы и компоненты ритуалов

**Актуализация .00035:** затронутые контейнерные/ритуальные сущности, отношения, процессы и адресные тесты обновлены по [issue-00333](../../issues/closed/issue-00333.md#implementation-00035). Описание ниже — исторический результат исходной порции; прежние отсутствие каскада/несогласованные записи контейнера и потеря UUID строки ритуала больше не описывают текущий код. Игровая приёмка нового поведения ожидается.

2026-09-16; rusbar-main, исходный HEAD `8b7368b866e67a126d8daabb298cc4a48dc8952f`, дерево в начале чистое. [Задача](../../tasks/task-0006.031.md), [запросы](examples/expansion-031-queries.json), [тесты](tests/test_expansion_031.py).

## Результат и пределы

Добавлены 170 сущностей, 602 отношения и 15 процессов. Всего 5169 сущностей, 14419 отношений, 440 процессов (1436 шагов, 2701 переходов), 398 границ. Определения в 301/615 файлах: два словаря en/ru complete, 299 файлов partial. Роли: 222 основных/79 смежных/314 без определений. Отношения в 305 файлах, локальные шаги процессов в 154.

Сохранены все прежние ID/владельцы, 13817 отношений и 425 процессов. Уточнены девять прежних сущностей: три DataModel, три листа, focus(), конфигуратор Spell и spellGeneral HBS. Новая детализация не объявляет файлы complete. Игровые исходники, мир, аудит и issues не изменялись.

| Файл | Включённая область и остаток |
| --- | --- |
| [module/data/item/hexData.js](../../../module/data/item/hexData.js) (src-000115) | Все schema/getUsedSkill; внешние schema cleaning, cast и AE/полный lifecycle partial. |
| [module/data/item/ritualData.js](../../../module/data/item/ritualData.js) (src-000123) | Все собственные методы, поля и prepared списки; региональная примесь .033, расход компонентов не найден в cast. |
| [module/data/item/spellData.js](../../../module/data/item/spellData.js) (src-000125) | Все собственные schema/methods/migrations; attack/defense/shared factories прежние, full cast .032, Region .033. |
| [module/item/sheets/WitcherHexSheet.js](../../../module/item/sheets/WitcherHexSheet.js) (src-000170) | Полный class/PARTS/selects/context; общий form core и browser partial. |
| [module/item/sheets/WitcherRitualSheet.js](../../../module/item/sheets/WitcherRitualSheet.js) (src-000177) | Полный class и два набора CRUD; реальные документы/запись/concurrent UI не исполнялись. |
| [module/item/sheets/WitcherSpellSheet.js](../../../module/item/sheets/WitcherSpellSheet.js) (src-000179) | Полный class/selects/context/configuration; динамический UI и cast partial. |
| [module/item/sheets/configurations/WitcherSpellConfigurationSheet.js](../../../module/item/sheets/configurations/WitcherSpellConfigurationSheet.js) (src-000187) | Полный adapter PARTS, родительские методы прежние; региональная форма .033. |
| [templates/partials/spell-header.hbs](../../../templates/partials/spell-header.hbs) (src-000540) | Именованные controls, включение, class условия и image/config boundaries; полный browser partial. |
| [templates/sheets/item/hex-sheet.hbs](../../../templates/sheets/item/hex-sheet.hbs) (src-000602) | Все именованные поля и описание own header; image/локализация имеют прежние границы. |
| [templates/sheets/item/ritual-sheet.hbs](../../../templates/sheets/item/ritual-sheet.hbs) (src-000609) | Named fields, legacy template paths, оба prepared списка и события; active browser/DB partial. |
| [templates/sheets/item/spell-sheet.hbs](../../../templates/sheets/item/spell-sheet.hbs) (src-000611) | Все именованные поля/условия и header; formula default HTML не initial модели, полный cast .032. |
| [templates/sheets/item/configuration/tabs/spellGeneral.hbs](../../../templates/sheets/item/configuration/tabs/spellGeneral.hbs) (src-000597) | Два TypedObject списка/CRUD, shared attackOptions и formGroup damage/defense; отдельная AE вкладка прежняя. |
| [templates/chat/item/partials/item-description/spell-description.hbs](../../../templates/chat/item/partials/item-description/spell-description.hbs) (src-000502) | Все три текстовых поля и type guard; общий producer включён, поздний core enrichment не исполнялся. |
| [module/data/item/templates/regions/templatePropertiesData.js](../../../module/data/item/templates/regions/templatePropertiesData.js) (src-000151) | Все четыре поля и input/migration/direct readers; геометрия/таймер/scene .033. |
| [module/data/actor/templates/common/focusData.js](../../../module/data/actor/templates/common/focusData.js) (src-000076) | Фабрика name/value, четыре Actor поля/forms/cast читатели; полный расчет стоимости .032. |
| [module/data/item/templates/componentData.js](../../../module/data/item/templates/componentData.js) (src-000135) | Полная фабрика uuid/quantity и ритуальные consumers; core resolver/cleaning ограничены прочитанными контрактами. |
| [module/data/item/mixin/spellRegionMixin.js](../../../module/data/item/mixin/spellRegionMixin.js) (src-000117) | Адреса createSpellRegion/fromItem/deleteSpellVisualEffect и чтение template полей; полный lifecycle .033. |
| [module/data/item/templates/regions/regionBehavioursData.js](../../../module/data/item/templates/regions/regionBehavioursData.js) (src-000149) | Адрес regionBehaviours factory как настройки; поля/исполнение/редактор .033. |
| [module/data/item/templates/regions/regionPropertiesData.js](../../../module/data/item/templates/regions/regionPropertiesData.js) (src-000150) | Схема behaviours связана с моделью; прежние methods сохранены, полный lifecycle .033. |
| [module/actor/mixins/castSpellMixin.js](../../../module/actor/mixins/castSpellMixin.js) (src-000011) | Добавлены непосредственные читатели magic/focus и model dispatch; полный процесс cast .032. |
| [templates/partials/character/tab-magic.hbs](../../../templates/partials/character/tab-magic.hbs) (src-000525) | Focus name/value forms добавлены к прежним IP; остальные spells/vigor/list связи .032. |
| [templates/chat/combat/spellItem.hbs](../../../templates/chat/combat/spellItem.hbs) (src-000487) | Текстовые/компонентные readers и адрес template; полный producer/кнопки .032. |
| [templates/chat/item/item-description.hbs](../../../templates/chat/item/item-description.hbs) (src-000498) | Включение spell-description от Item message; прочие partials/экспорт за пределами порции. |
| [module/setup/config.js](../../../module/setup/config.js) (src-000209) | Карта magic для трех getUsedSkill; прежние skill/cost карты сохранены, прочий config partial. |

## Тип документа и возможности

| Модель | Собственная схема и поведение | Лист / конфигурация |
| --- | --- | --- |
| HexData | danger, stamina, effect, liftRequirement и defenseOptions; свой getUsedSkill | WitcherHexSheet + собственный HBS; обычный WitcherConfigurationSheet |
| RitualData | level, STA/variable, описания range/duration/defence/components/preparationTime/DC, два UUID списка, template/region, defenseOptions; derived/migrations/getUsedSkill | WitcherRitualSheet + CRUD двух списков; обычный конфигуратор |
| SpellData | class/level/source/domain/sideEffect, STA/описания, damage/shield/heal, self/onCast TypedObject, attack/defense/template/region; выбор навыка, защита, миграции, temporary improvement getter | WitcherSpellSheet + WitcherSpellConfigurationSheet/PropertiesConfiguration |

Все наследуют восемь полей CommonItemData. Четыре class Spells/Invocations/Witcher/MagicalGift — значения одного типа spell, не четыре типа документов. Регистрации моделей и листов сохранены. Hex не получает методы области Spell/Ritual по сходству имени. Только Spell из этих трёх переопределяет canHaveTemporaryItemImprovement в true; это разрешение категории UI, не применение улучшения. Текст defence отделён от defenseOptions и DefenseProperties: два собственных метода Spell делегируют структурированной защите.

<a id="skill"></a>
## Выбор навыка

У каждой из трёх моделей собственный getUsedSkill с приоритетом `skillMap[spellAttackSkill] ?? magic[parent.type]?.skill ?? magic[class].skill`. Первый найденный объект возвращается; это не проверка согласованности выбранной характеристики. Последний доступ без optional chaining может бросить исключение.

У Hex/Ritual нет объявленных class/spellAttackSkill, зато штатный parent.type выбирает hexweave/ritcraft. У Spell attackOptions задаёт initial spellAttackSkill='spellcasting', тогда как карта содержит spellcast. Допустимый class обеспечивает fallback; пустой или неизвестный class при неверном override приводит к TypeError. HTML select сам не присваивает первый option в исходную модель. getItemAttack использует отдельный путь метаданных и не обязан повторять getUsedSkill (issue64).

<a id="migration"></a>
## Миграция исходных данных

WitcherItem.migrateSpells меняет type на hex/ritual по прежнему system.class Hexes/Rituals; исходный class этим методом не удаляется. Это документная миграция до выбора модели, не прямой вызов SpellData/RitualData из метода.

SpellData.migrateData копирует dificultyCheck→difficultyCheck, обращается к static this.effects, вызывает migrateDamageProperties, преобразование self/onCast и migrateTemplate, затем super. Static this не является source; this.effects обычно отсутствует. difficultyCheck в конечной Spell schema не объявлен. Ни один из этих методов не вызывает Item.update.

Непустые массивы selfEffects/onCastEffects становятся словарями с randomID для каждой записи. Два условия независимы; объект и пустой массив самим методом не переписываются. Очистка TypedObjectField — следующий внешний этап, не миграция с записью БД.

Обе migrateTemplate срабатывают только при truthy legacy templateSize, полностью заменяют templateProperties и удаляют четыре прежних поля. Numeric 0 пропускает перенос; строка '0' проходит guard. Spell применяет parseInt||0 (строка '2.75' становится 2); Ritual передаёт строку далее NumberField. Смешанные новые/старые данные могут потерять уже заполненные nested значения (issue128). Эти правила переноса описаны по коду, не изменены.

<a id="forms"></a>
## Основные формы и сохранение

Собственные _prepareContext ожидают общий Item context и добавляют createSelects. Словари вариантов не являются schema choices или initial. Через PARTS формы получают item/systemFields; именованные inputs передаются в унаследованный submitOnChange. В прочитанном ядре для редактируемого существующего документа выполняются expandObject, validation с cleaning и await document.update. Unsaved create, полный браузерный lifecycle и мировая БД не проверялись.

Spell header задаёт class/level/source, а основная форма — duration/range/defence/sideEffect, STA и четыре независимых флага области/урона/щита/лечения. Скрытие поля не удаляет сохранённое значение. Формульное '1d6+0' в input — отображаемый fallback, не initial модели: damage=null, shield/heal=''. Текстовые STA/размеры проходят NumberField cleaning; наличие type=text не означает строковое хранилище.

Spell пишет актуальные system.templateProperties.*. Ritual HBS использует прежние root createTemplate/templateSize/templateType/visualEffectDuration и проверяет root createTemplate. Они адресованы как запрос к отсутствующим полям, не как writers актуальной TemplateProperties (issue129). Наличие migrateTemplate не доказывает корректный современный submit.

У Spell img содержит data-action=editImage, у Hex/Ritual только data-edit; собственных image listeners в их классах нет (issue136). Checkbox clickableImage во всех трёх формах не соответствует объявленной Common/конкретной schema (issue63). DangerLow/Medium/High, Water и ru emanation имеют прежние ограничения локализации (issue137); справочник en/ru переиспользуется, переводы не меняются. Ошибка общего tabs/general из issue62 не переносится на специализированный attackOptionsPart Spell.

<a id="configuration"></a>
## Конфигуратор и область

SpellConfiguration заменяет только PARTS.general, остальные методы принадлежат PropertiesConfiguration/Configuration. Общий родитель выбирает вкладки по regionProperties, но удаляет region PART по старому system.createTemplate (issue74). Отдельное несуществующее createRegionFromTemplate в региональной форме — прежняя issue75; её полный разбор относится к .033. Hex/Ritual не создают SpellConfiguration.

TemplateProperties хранит createTemplate=false, templateSize=0, templateType='', visualEffectDuration без explicit initial. Нет schema enum/min/max/integer; варианты формы не ограничивают прямой ввод. RegionProperties.behaviours ссылается на фабрику четырёх Macro UUID. Здесь зафиксирован адрес настроек, не полный редактор/исполнитель регионов.

Spell/Ritual получают spellRegionMixin через Object.assign. createSpellRegion читает вложенные create/type/size; fromItem читает type/size; deleteSpellVisualEffect — visualEffectDuration. Вход запускает Promise chain без return/await, callback ожидает addBehaviorsToRegions и затем удаление визуализации, catch пустой. Геометрия/таймер/сцена/сеть остаются .033. visualEffectDuration измеряется отдельным секундным механизмом, не является duration заклинания.

<a id="components"></a>
## Списки компонентов ритуала

component() — фабрика строки {uuid,quantity}; самостоятельный алхимический ComponentData Item — другой источник. UUIDField не ограничен типом Item и не проверяет существование документа; quantity initial0 без min/max/integer. В строке нет собственного ID, name или img.

ritualComponentUuids и alternateRitualComponentUuids хранят исходные записи. prepareDerivedData сбрасывает ritualComponents/alternateRitualComponents и строит {item,quantity,img}; fromUuidSync либо возвращает документ/index entry, либо null, либо бросает для неподдержанного синхронного embedded compendium UUID. Метод не выполняет async загрузку. Fallback {name:uuid} сохраняет отображаемое имя, но не item.uuid. component.img не объявлен в schema. Эти prepared массивы не являются дополнительными source полями.

HBS берёт row data-uuid из component.item.uuid, target выбирает исходный массив. quantity имеет type=number/data-field, но не name. При fallback dataset теряет исходный UUID: edit получает index−1, remove не находит сохранённую ссылку (issue130). Живой cold-pack не проверялся.

Свободный текст components, два массива UUID и prepared представления независимы. Combat HBS перебирает основной список, но альтернативный выводит целиком (issue135). Чтение полного castSpell и поиск module/templates не обнаружили расхода этих массивов или количества referenced Item. Это ограниченное отрицательное наблюдение, не доказательство отсутствия внешнего макроса.

<a id="component-edit"></a>
## Drop, изменение и удаление

| Операция | Выбор и мутация | Запись / граница |
| --- | --- | --- |
| Drop | Общий родитель проверяет editable и разрешает Item. Child принимает любой truthy item; closest .alternateComponents выбирает alternate, любой другой участок — main. Push {uuid,quantity:1}, без проверки типа/повторов | Prepared массив меняется до update; дочерний async метод не возвращает/не ожидает Promise записи |
| Blur quantity | По row uuid/target выбирает массив, findIndex первого UUID; components[index][field]=element.value | Значение строковое даже при data-dtype Number; NumberField очищает в числовое. Index−1 прерывает метод до update |
| Remove | filter всех записей с тем же UUID; создаётся новый массив | update полного массива без await/return; referenced Item не удаляется |

Дублирование UUID допустимо при Drop, но edit/remove не различают строки (issue131). Родительский await _onDropItem ждёт локальный метод, а не его потерянный update; несколько операций не транзакция (issue132). Количественная строка сама по себе не новая ошибка. События, отказ БД и конкурентная работа здесь не исполнялись.

<a id="effects"></a>
## Четыре канала воздействий

- effect — строковое описание, не автоматический ActiveEffect.
- selfEffects/onCastEffects — TypedObject(itemEffect) с name/statusEffect/percentage/varEffect; spellGeneral выбирает только statusEffect и передаёт target/ID. Add создаёт percentage0, edit пишет target.id.field, remove использует -=; все три update запускаются без await/return.
- damageProperties.effects — отдельные воздействия урона с прежними consumers .014–.018.
- Item.effects — embedded ActiveEffect, отдельная унаследованная вкладка и CRUD, условия applySelf/applyOnTarget.

Поля ConsumablePropertiesData.heal/effects не вложены в эти магические модели. Spell.cast self preview проверяет length/forEach, а применение использует Object.values; словарь не попадает в preview (issue133). UI не редактирует percentage/varEffect и не превращает этот канал в проверку процента на прямом cast. Полное исполнение статусов/AE — .032 и прежняя .008.

<a id="focus"></a>
## Focus Actor

CommonActorData создаёт четыре независимых пары focus1–4.name/value. В tab-magic их восемь именованных text inputs идут через Actor submit; NumberField очищает value. Это отдельные данные от derivedStats.focus. castSpell предлагает только слоты с value>0; поле имени формирует подпись. Он читает выбор для снижения цены STA, а сами focusN.value не расходует. Полный расчёт цены и диалог остаются .032.

<a id="cast"></a>
## Стыки с применением и сообщениями

В граф добавлены конкретные readers castSpell для стоимости, duration, source, damage/shield/heal, self/onCast и defenseOptions; общий createBaseDamageObject читает Spell.damageProperties. Значение Ritual.difficultyCheck здесь связано с выводом combat HBS, а не вымышленным guard броска. Собственный getUsedSkill и общий Item.getItemAttack сохраняют разные контракты.

Длительность передаётся в raw damage.duration до очистки сообщения; прежняя issue257 относится к потере на schema границе. doesHeal+staminaIsVar имеет отдельную issue134 об undefined heal. Здесь эти ограничения адресованы, полный cast процесс не продублирован раньше .032.

Общий _onItemMessage → item-description → spell-description показывает effect/sideEffect/liftRequirement для трёх типов. Обычное {{}} экранирует разметку первого HBS; последующее core enrichment сообщения — отдельная граница. Показ описания не вызывает cast, не списывает STA/компоненты и не создаёт эффект.

## Источники доказательств

Прочитаны перечисленные исходники, относящиеся к ним разделы всех 16 карточек и позднего аудита R009-01–R009-06/R011-02. Связанные issue128/129/130/131/132/133/136/137/257 прочитаны полностью; дополнительно62/63/64/74/75/134/135 для общих editor/consumer границ. Их даты, potential статусы и исторические фасады сохранены. Новое игровое воспроизведение не заявляется, аудит/issues не изменены.

Установленное ядро Foundry 14.367.0 проверено чтением конкретных участков. Хеш фиксирует файл, не клиентский запуск или сохранение БД.

| Файл | Строки | Контракт | SHA256 |
| --- | --- | --- | --- |
| `/opt/foundryvtt/common/data/fields.mjs` | 1471–1552,3399–3457 | NumberField cast/clean/constraints и DocumentUUIDField: syntax/type/ID, без проверки существования документа. | `efa8e3ccdf553ca826580e60bfbfc97db57bdeadaa954a50f6a55e0ab52c3e01` |
| `/opt/foundryvtt/client/utils/helpers.mjs` | 177–216 | fromUuidSync: document/index entry/null; strict embedded compendium UUID может бросить, асинхронной загрузки нет. | `21d7b80e8f7ac7b8e4c53aef622f36ec1867ca6be75ae7bb21c959df733d314c` |
| `/opt/foundryvtt/client/applications/api/document-sheet.mjs` | 383–434,465–531 | editImage отдельно от data-edit; editable submit→expand/validate/clean→await update существующего Item. | `7925d81900eeea0d5e79606e12ce43539ae00714f50d8452c7305fe81394aa01` |
| `/opt/foundryvtt/client/applications/ux/form-data-extended.mjs` | 168–222 | Чтение именованных controls, Number/checkbox/dtype; прямой blur .value не проходит этот путь. | `0585d07f0ca067969b4dfdde6d187e7d8315abd1cb2dbf9dd55325c003175a01` |

## Процессы

<a id="proc-000426"></a>
### proc-000426 — Выбор навыка SpellData

Вызов собственного getUsedSkill; cast/defense читают возвращённую запись карты.

Шаги: override → type → class. Условия ветвления/выходы и ожидание — в JSONL.

<a id="proc-000427"></a>
### proc-000427 — Выбор навыка HexData

Вызов собственного getUsedSkill; cast/defense читают возвращённую запись карты.

Шаги: override → type → class. Условия ветвления/выходы и ожидание — в JSONL.

<a id="proc-000428"></a>
### proc-000428 — Выбор навыка RitualData

Вызов собственного getUsedSkill; cast/defense читают возвращённую запись карты.

Шаги: override → type → class. Условия ветвления/выходы и ожидание — в JSONL.

<a id="proc-000429"></a>
### proc-000429 — Source миграция SpellData

Ядро вызывает model migration; мир и автоматическое сохранение не исполнялись.

Шаги: source → guard → replace → super. Условия ветвления/выходы и ожидание — в JSONL.

<a id="proc-000430"></a>
### proc-000430 — Source миграция RitualData

Ядро вызывает model migration; мир и автоматическое сохранение не исполнялись.

Шаги: source → guard → replace → super. Условия ветвления/выходы и ожидание — в JSONL.

<a id="proc-000431"></a>
### proc-000431 — Именованные поля HexData через Item форму

DOM→типизированные значения→унаследованный submit; literals и объявленная schema различены.

Шаги: input → submit. Условия ветвления/выходы и ожидание — в JSONL.

<a id="proc-000432"></a>
### proc-000432 — Именованные поля RitualData через Item форму

DOM→типизированные значения→унаследованный submit; literals и объявленная schema различены.

Шаги: input → submit. Условия ветвления/выходы и ожидание — в JSONL.

<a id="proc-000433"></a>
### proc-000433 — Именованные поля SpellData через Item форму

DOM→типизированные значения→унаследованный submit; literals и объявленная schema различены.

Шаги: input → submit. Условия ветвления/выходы и ожидание — в JSONL.

<a id="proc-000434"></a>
### proc-000434 — Подготовка двух списков компонентов ритуала

Lifecycle prepareDerivedData; исходные массивы и отображение отдельны.

Шаги: reset → main → alternate. Условия ветвления/выходы и ожидание — в JSONL.

<a id="proc-000435"></a>
### proc-000435 — Добавление ссылки на компонент ритуала

Общий editable Drop уже разрешил Item; child не проверяет subtype и дубликаты.

Шаги: guard → alternate → main. Условия ветвления/выходы и ожидание — в JSONL.

<a id="proc-000436"></a>
### proc-000436 — Количество компонента: blur и первый UUID

Input без name использует direct listener, не общий form submit.

Шаги: dom → lookup → update. Условия ветвления/выходы и ожидание — в JSONL.

<a id="proc-000437"></a>
### proc-000437 — Удаление компонентов: все совпадения UUID

click direct listener; удаляется ссылка самого ритуала, не referenced Item.

Шаги: dom → filter → update. Условия ветвления/выходы и ожидание — в JSONL.

<a id="proc-000438"></a>
### proc-000438 — Статусы self/onCast: keyed редактор

Выбор действия HBS и system.selfEffects/system.onCastEffects target; отдельный от ActiveEffect CRUD.

Шаги: action → add → edit → remove. Условия ветвления/выходы и ожидание — в JSONL.

<a id="proc-000439"></a>
### proc-000439 — Focus слоты: форма и чтение при cast

Настройка name/value четырёх слотов; cast может произойти позднее отдельным действием.

Шаги: form → reader. Условия ветвления/выходы и ожидание — в JSONL.

<a id="proc-000440"></a>
### proc-000440 — Миграция массивов selfEffects/onCastEffects в словари

Два независимых непустых Array guard; empty array/object остаются до schema cleaning.

Шаги: self-guard → self-convert → cast-guard → cast-convert. Условия ветвления/выходы и ожидание — в JSONL.

## Проверки

Проверены все 266 тестовых методов в 30 модулях и 812 примеров CLI, включая 43 новых по IQ-01–IQ-08; ошибок в итоговых результатах нет. Исторические проверки выполняются на предусмотренных прежними тестами срезах. Это проверки справочника по исходникам, без запуска игрового сценария. Перекрёстно сверены исходные адреса/владельцы, оба конца отношений, readers/writers, ветви и выходы, refs/facets/роли. [Протокол](review-log.md#task-0006031). Следующая — [TASK-0006.032](../../tasks/task-0006.032.md); родитель in-progress.