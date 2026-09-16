# Покрытие TASK-0006.010 — редактирование характеристик и навыков

2026-09-15; rusbar-main, исходный HEAD eb54b0b80d45570dc3e2b24360dc88ed1176740c. [Задача](../../tasks/task-0006.010.md), [манифест](manifest.json), [протокол](review-log.md#task-0006010).

Добавлены **73 сущности, 272 отношения и 28 процессов**. Всего **615 источников, 1008 сущностей, 2671 отношение и 91 процесс**; 390 шагов/595 переходов. Частичные определения имеют 151 файл: 58 основных и 93 смежных; 464 без определений. Границ 193, из них 8 новых. Все прежние ID и процессы сохранены.

## Основные источники

| Источник | Включено |
| --- | --- |
| [WitcherModifiersConfiguration.js](../../../module/actor/sheets/configurations/WitcherModifiersConfiguration.js) — src-000032 | Весь прикладной класс: constructor, карты, options/PARTS/context/render/listeners и две примеси. |
| [statMixin.js](../../../module/actor/sheets/mixins/statMixin.js) — src-000046 | Шесть подписок, ручная удача/адреналин, сумма max, stat/reputation Roll-входы и отдельные callbacks. |
| [customSkillMixin.js](../../../module/actor/sheets/mixins/customSkillMixin.js) — src-000040 | Весь listener и пять старых операций Item/modifiers; roll-ветка переиспользована из .009/пилота. |
| [edit-skills.hbs](../../../templates/sheets/actor/configuration/app/edit-skills.hbs) — src-000542 | Lookup группы, числовой value, три Bool, level-up и только отображаемый AE. |
| [edit-stats.hbs](../../../templates/sheets/actor/configuration/app/edit-stats.hbs) — src-000543 | Оба условия type и аргументы общего partial. |
| [stats-block.hbs](../../../templates/sheets/actor/configuration/app/partials/stats-block.hbs) — src-000544 | Условие по локализованному label и enabled поля unmodifiedMax со значениями max. |
| [skillConfiguration.hbs](../../../templates/sheets/actor/configuration/partials/skillConfiguration.hbs) — src-000547 | Реальный PARTS отдельной конфигурации монстра, DataField/Bool и formGroup. |
| [modifier-configuration.css](../../../styles/configurations/modifier-configuration.css) — src-000453 | Два вложенных rule-узла/одна declaration, классы адресата и import. |

Смежно перечитаны входы Character/Monster, базовые listeners V2/V1, модели Skill/SkillItemData/stat/stats/derived/reputation/adrenaline, существующие расчёты Actor/CommonActorData и прямые потребители. Для skillConfiguration прочитаны контекст и _getSkills в WitcherMonsterConfigurationSheet. Sidebar и tab-stats использованы только как producers конкретных кнопок/полей. Полные recovery/death-save/IP/logs/бой и прочие области крупных листов не включены.

## Открытие, две части и подготовленный контекст

Character/Monster регистрируют openModifiers, читают target.dataset.type/skillKey и создают WitcherModifiersConfiguration с this.document. Constructor сохраняет оба параметра без валидации. Render(true) не ожидается и не возвращается вызывающему коду. В DEFAULT_OPTIONS редактора нет своего submit handler; actions пуст, события подключаются примесями.

PARTS содержит одновременно stats и skills. Локального фильтра частей нет; обычный внешний render без выбора частей берёт все descriptors. type выбирает только содержимое edit-stats; skillKey независимо выбирает группу edit-skills. Вызов с type=skill и заданным ключом не превращает его в отдельный класс формы.

_prepareContext ждёт super, затем context.config=CONFIG.WITCHER; присваивание context.config.statLabels меняет общий объект. Reduce использует все записи statMap и label ?? labelShort. Такое же присваивание есть в отдельной Monster configuration. context.system ссылается на подготовленную модель document.system; это не копия исходных данных. _onRender ожидает super, затем statListener/skillListener. Первый использует локальный html=$(html); второй сохраняет прежнее глобальное присваивание jQuery. [R003-10](../code-audit/cross-check-0002.md#r003-10), [R004-10](../code-audit/cross-check-0002.md#r004-10), [issue-00167](../../issues/potential/issue-00167.md).

## Поля формы и последующие читатели

| Поле / условие | Читает при рендере | Куда адресован ввод |
| --- | --- | --- |
| stats-block, type=stats/derivedStats | details.max | system.<root.type>.<stat>.unmodifiedMax, enabled Number |
| Репутация, только если передана | reputation.max | system.reputation.unmodifiedMax |
| edit-skills, lookup группы найден | Skill.value | system.skills.<skillKey>.<skillName>.value |
| Три checkbox | isProfession/isPickup/isLearned | Соответствующие Bool того же навыка |
| AE-строка при truthy activeEffectModifiers | Skill.activeEffectModifiers | Два disabled input без name; назначения записи нет |
| Видимость отдельной Monster configuration | DataField и отдельный prepared isVisibleValue | Имя берётся из DataField.fieldPath через core formGroup/toInput |

Toxicity исключается по равенству **локализованных подписей**, а не по ключу поля. Для неизвестного type edit-stats пуст; для неизвестного skillKey edit-skills пуст. Оба условия независимы. Stats-block сам не выводит readonly бонусы; disabled AE принадлежит edit-skills.

Input-узлы ссылаются на поле назначения и внешний submit через refers. Они не названы синхронными writers модели при рендере. Для поиска форм назначения использовать входящие refers поля; writes показывает реальные присваивания и явно отмеченные запросы update. Явный ресурсный update также отличается от окончательной записи в БД.

В установленном ядре change при submitOnChange запускает сбор **всей формы** через FormDataExtended. Unnamed/disabled элементы пропускаются; readonly по умолчанию включён, поэтому readonly сам по себе не доказывает отсутствие записи. Number input преобразуется в число (пустой — null), checkbox без специального value — Bool. Старый custom-edit читает element.value напрямую и этот маршрут преобразования не использует.

DocumentSheetV2 проверяет isEditable, разворачивает formData.object, валидирует и ждёт _processSubmitData; существующий документ обновляется. Условия permissions/create/ошибок остаются внешними. Соседний prepared max может попасть в исходный unmodifiedMax; [issue-00194](../../issues/potential/issue-00194.md) содержит прежний изолированный опыт. Он не повторялся.

Читатели баз уже представлены пилотом: CommonActorData.prepareBaseData, Stats.prepareBaseData, WitcherActor.calculateStats/calculateDerivedStat и общий stat().unmodifiedMax. Часть производных баз/максимумов пересчитывается; для HP/STA существенен customStat. Схема NumberField и enabled input не доказывают, что ввод сохранится после подготовки. [issue-00195](../../issues/potential/issue-00195.md), proc-000004/000005. Формулы не переписаны и не скопированы в новые процессы.

Кнопка level-up получает **skillName из модели** и прежним ent-000383 передаёт его Actor.levelUpSkill (ent-000300). IP/logs/стоимость — B11, здесь только вход. Commonspeech/commonsp и применение общей кнопки к Monster связаны с прежними [issue-00004](../../issues/potential/issue-00004.md) и [issue-00192](../../issues/potential/issue-00192.md), а не объявлены новыми проблемами.

## Ручные ресурсы и входы бросков

| Метод | Чтение и запрос | Ожидание / предел |
| --- | --- | --- |
| _onLuckMinus | Если luck.value>0: value−1 | await Actor.update |
| _onLuckReset | luck.value=prepared luck.max | await update; не unmodifiedMax, без ограничения max |
| _onAdrenalineMinus | Если value>0: value−1 | await update |
| _onAdrenalinePlus → addAdrenaline | При useOptionalAdrenaline: value+1 | Оба уровня не передают завершение update; потолок не задан |
| calc_total_stats | Сумма stats[*].max, кроме ключа toxicity | Без Number; вызывается _prepareCharacterData, не _prepareContext непосредственно |
| _onStatSaveRoll | Для luck порог max, для остальных value | Await custom prompt/extendedRoll; statValue — threshold, не слагаемое |
| Репутация t1 / t2 | t1: value как reversal threshold; t2: Number(reputation.value)+Number(WILL.value) | Раздельные callbacks с await extendedRoll; само открытие Dialog не ждёт выбора |

Декремент проверяет >0; это не общий clamp на неотрицательность дробных/неожиданных данных. Schema adrenaline.value не задаёт min/max. Sidebar вручную вводит luck/adrenaline.value через отдельные Number inputs; прямое изменение input и нажатие кнопки различны. Отображаемая репутация tab-stats имеет прежнее наблюдение [issue-00198](../../issues/potential/issue-00198.md); её полная разметка не стала новым процессом редактора. [R003-11](../code-audit/cross-check-0002.md#r003-11), [issue-00197](../../issues/potential/issue-00197.md).

## Старые собственные модификаторы

Сохраняется установленное в .009 разделение: текущая custom-строка не даёт старые .item/Item ID/selector. Старый monster partial содержит remove/open/roll и readonly AE, но кнопок add/edit/delete modifiers во всех текущих templates не найдено. Регистрация обработчика не подтверждает его достижимость.

| Метод | Адрес и операция | Барьер |
| --- | --- | --- |
| removeCustomSkill | items.get(closest .item ID).delete() | Нет Item guard/await/return |
| customSkillModifierDisplay | Item.find по ID → update isOpened=!isOpened | Поле объявлено; await отсутствует |
| add | modifiers ?? []; push {name:'Modifier', value:0}; update списка | Нет id; при существующем массиве меняется ссылка в памяти |
| remove | Object.values; findIndex строгого id по event.target; splice(index,1) | −1 не проверяется и для непустого массива удаляет последний |
| edit | ID у currentTarget.closest(.list-modifiers), field из dataset, value из input; loose findIndex | Значение остаётся строкой; нет whitelist/guard index; весь массив отправляется без await |

system.modifiers представлен динамической границей ent-000972, а не вымышленным полем SkillItemData. Все восемь полей модели перечитаны; modifiers в ней отсутствует. В прежнем опыте модель отбрасывала массив, а сценарии edit/remove использовали его явное внедрение. Новая порция не исполняет эти опыты и не утверждает наличие массива в мире. [R004-08](../code-audit/cross-check-0002.md#r004-08), [issue-00189](../../issues/potential/issue-00189.md).

## Видимость и CSS

skillConfiguration.hbs имеет реального потребителя: WitcherMonsterConfigurationSheet.PARTS.skills, а не только preload. Monster создаёт configuration с Actor; базовая .configure-actor подписка вызывает optional _renderConfigureDialog. _getSkills выбирает характеристики origin=stats и ключи skillMap по attribute.name, получает schema DataField/текущее Bool, удаляет пустые группы. Commonspeech DataField может отсутствовать; helper возвращает пустую строку с диагностикой. Текущая строка builtin не читает isVisible — это граница применения, уже описанная в .009. Имена и подписи formGroup зависят от родительской schema; отсутствие явного input.name в HBS не означает отсутствие имени.

CSS импортирован из styles/witcher-styles.css:38 после общей Actor-сетки. Селектор .application.sheet.witcher.actor.modifier-configuration:not(.extended-sheet) .window-content задаёт только display:inherit; значение берётся у непосредственного родителя. JS задаёт классы, ядро — application/window-content. CSS не определяет ширину 520, не сбрасывает grid tracks и не меняет данные. Computed style и HTTP-доступ не проверялись.

## Процессы

| ID | Выбранный участок |
| --- | --- |
| <a id="proc-000064"></a>proc-000064 | Редактор: параметры экземпляра. Только прикладной constructor; правила super и render снаружи. |
| <a id="proc-000065"></a>proc-000065 | Character: открыть редактор модификаторов. Оба аргумента читаются независимо; render не awaited. Полный внешний action dispatch вне процесса. |
| <a id="proc-000066"></a>proc-000066 | Monster: открыть редактор модификаторов. Оба аргумента читаются независимо; render не awaited. Полный внешний action dispatch вне процесса. |
| <a id="proc-000067"></a>proc-000067 | Редактор: подготовленный контекст и общие подписи. Общая CONFIG меняется по ссылке; обе PARTS, type и skillKey независимы. |
| <a id="proc-000068"></a>proc-000068 | Редактор: после рендера к listeners. Новый render и момент регистрации событий отделены от click. |
| <a id="proc-000069"></a>proc-000069 | Редактор: два listener. statListener локален; skillListener имеет историческое глобальное присваивание. |
| <a id="proc-000070"></a>proc-000070 | Форма: выбор характеристик или производных. Другие type дают пустой блок, но не исключают отдельную PARTS.skills. |
| <a id="proc-000071"></a>proc-000071 | Форма: max в имени unmodifiedMax. Отрисовка создаёт адрес записи для общего внешнего submit; локальной записи нет. |
| <a id="proc-000072"></a>proc-000072 | Форма: прямой ввод навыка и отдельная кнопка повышения. Value/Bool через общий submit; button через прежний callback. Disabled AE без name не пишет модель. |
| <a id="proc-000073"></a>proc-000073 | Ресурс luck: уменьшение. Проверка >0 перед абсолютным payload; нет общего clamp и сериализации конкурирующих запросов. |
| <a id="proc-000074"></a>proc-000074 | Ресурс adrenaline: уменьшение. Проверка >0 перед абсолютным payload; нет общего clamp и сериализации конкурирующих запросов. |
| <a id="proc-000075"></a>proc-000075 | Удача: сброс к подготовленному max. Ничего не ограничивает max; его prepared-расчёт уже в пилоте. |
| <a id="proc-000076"></a>proc-000076 | Адреналин: ручной вход. Не ожидает addAdrenaline; окончание метода не подтверждает запись. |
| <a id="proc-000077"></a>proc-000077 | Адреналин: настройка и запрос увеличения. Полный query/боевой вход вне .010; async не передаёт Promise update. |
| <a id="proc-000078"></a>proc-000078 | Старый навык: удаление Item. get ID → Item.delete; нет guard, подтверждения и возврата Promise. |
| <a id="proc-000079"></a>proc-000079 | Старый навык: раскрытие. Меняет schema isOpened; не создаёт отсутствующие кнопки CRUD modifiers. |
| <a id="proc-000080"></a>proc-000080 | Старый модификатор: добавление. Отсутствующий schema modifiers не подменён полем модели; add не задаёт ID. |
| <a id="proc-000081"></a>proc-000081 | Старый модификатор: удаление по target ID. Object.values делает новый массив, элементы по ссылке; промах -1 не проверяется. |
| <a id="proc-000082"></a>proc-000082 | Старый модификатор: строковый ввод. ID списка берётся у currentTarget; поле dynamic, нет Number/whitelist. |
| <a id="proc-000083"></a>proc-000083 | Видимость: поля из ключей карты. Ключ skillMap используется в schema/value путях; несовпадение commonspeech отмечено границей. |
| <a id="proc-000084"></a>proc-000084 | Видимость: контекст отдельного окна. General/tab-состав окна и его полный lifecycle вне выбранного skills участка. |
| <a id="proc-000085"></a>proc-000085 | Видимость: formGroup и внешний submit. DataField задаёт name через fieldPath; отсутствие поля обрабатывает core helper. |
| <a id="proc-000086"></a>proc-000086 | Спасбросок характеристики: вход в общий Roll. Только сборка параметров и вызов прежнего extendedRoll; новые боевые цепочки не создаются. |
| <a id="proc-000087"></a>proc-000087 | Репутация: диалог выбора броска. Callbacks исполняются после отдельного выбора; сам render не ожидает их. |
| <a id="proc-000088"></a>proc-000088 | Репутация: спасбросок. Прежние ChatMessageData/RollConfig/extendedRoll; отмена диалога сюда не входит. |
| <a id="proc-000089"></a>proc-000089 | Репутация: противостояние. Прежние ChatMessageData/RollConfig/extendedRoll; отмена диалога сюда не входит. |
| <a id="proc-000090"></a>proc-000090 | Сумма характеристик для отображения. Сумма max, не исходных баз/подготовленных value; типы не приводятся. |
| <a id="proc-000091"></a>proc-000091 | Монстр: optional окно конфигурации. Текущий Monster предоставляет configuration; произвольные подклассы могут оставить undefined. |

Все процессы partial: отдельные фрагменты не обещают охват каждого внешнего исключения. Render, выбор кнопки, подключение listener и его вызов разделены; update остаётся границей, даже если caller использует await. Новых процессов расхода IP/боевого разрешения не создано.

## Проверенные внешние контракты

Foundry 14.367.0. Хеш относится ко всему файлу, область — к прочитанным участкам. Эти источники не расширяют каталог системы из 615 файлов.

| Внешний файл | Прочитанная область | SHA256 |
| --- | --- | --- |
| /opt/foundryvtt/client/applications/api/document-sheet.mjs | 50–68, 465–544: handler, isEditable, validate/expand, update/create | 7925d81900eeea0d5e79606e12ce43539ae00714f50d8452c7305fe81394aa01 |
| /opt/foundryvtt/client/applications/api/application.mjs | 2134–2162: вся форма, await handler, submitOnChange | b5aef80d3e042a4a856be9dd875c72a5224988d62046ba770f25376f4291faa0 |
| /opt/foundryvtt/client/applications/api/handlebars-application.mjs | 69–78, 116–137: выбор всех PARTS и render по контексту | e253e0e76ab7f034f68d7055778a33e6935a7c94a6a05b0ca61188a23cea4f9d |
| /opt/foundryvtt/client/applications/ux/form-data-extended.mjs | 18–45, 105–127, 182–205, 239–242: disabled/readonly, name и Number/Bool | 0585d07f0ca067969b4dfdde6d187e7d8315abd1cb2dbf9dd55325c003175a01 |
| /opt/foundryvtt/client/applications/handlebars.mjs | 531–546: formGroup, отсутствующее поле/catch | 0c5959e0ebdf5847277fba3284d76ee535084e022d087659fd0791e5ccd3545c |
| /opt/foundryvtt/common/data/fields.mjs | 179–181, 632–637, 662–668: fieldPath/name и toFormGroup | efa8e3ccdf553ca826580e60bfbfc97db57bdeadaa954a50f6a55e0ab52c3e01 |

## Проверки и остаток

[Проверочные запросы](examples/expansion-010-queries.json) и [тесты](tests/test_expansion_010.py) сопоставляют исходные адреса, два конца связей, источники input и update, отсутствие writer у disabled, чужое/отсутствующее поле, старую ID-адресацию и процессы. Исторические A13/P08 оставлены на пилотном срезе; текущие новые читатели AE проверяются отдельно. SUI-11 проверяется на частях до .009, новые читатели Item ID — на текущем графе. Декларации .006 и счётчики .009 сохранены на их исторических частях; новые размеры проверяются отдельно.

[Протокол](review-log.md#task-0006010) содержит фактические результаты и сохранность. Исходники, query.py, аудит/issues, мир, БД, права и Git-история не менялись; JavaScript/Foundry/браузер не исполнялись. Следующая согласованная порция — [TASK-0006.011](../../tasks/task-0006.011.md), en/ru и их потребители, со сверкой накопленного расширения.
