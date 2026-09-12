# Журнал перекрёстных сверок

## TASK-0003.048

Дата: 2026-09-12. Ветка rusbar-main, коммит ee24c2605f4db98fad1ff6db024d2b0c26883670. Продолжение согласованной очереди по поручению пользователя; [задача](../../tasks/task-0003.048.md). Исходный срез TASK-0001 — 15da5b225535e34af4e132c701b5353ef4eb667f.

Полностью разобраны 16 файлов / **920 логических строк**: шесть HBS (433 строки) и десять CSS (487 строк). Весь состав — таблица задачи и новые карточки в [docs/analytics/code-audit/files/README.md](files/README.md). Состав не расширялся; соседние определения и consumers проверены в пределах связи.

### Методика и границы

Локальный Node через stdin, без создания стенда. Реальные DataModel/TypeDataModel/fields и primitives Foundry 14.367.0 (/opt/foundryvtt/package.json), Node 24.16.0. Исполнялись настоящие модели 13 типов, Handlebars 4.7.9, системный registerHandelbarHelpers и core concat/localize из client/applications/handlebars.mjs, полный Localization из client/helpers/localization.mjs с expandObject/ru/en fallback. HBS компилировались из файлов без изменения текста, вложенные пять partial — настоящие. Методы _onItemMessage/_onSubstanceDisplay исполнялись из исходного itemMixin; импорты для VM заменены окружением.

fromUuidSync — карта «доступный документ / null»; Actor/items, DOM event и ChatMessage.getSpeaker/create — фасады. Для модели не передавался поддельный parent. IDs UUID соответствуют схеме ядра (16 символов). Дополнительные service HBS использовали фасад selectOptions; панель веществ — явную замену вложенного component-list, а не полный второй аудит списка. Построение HTML проверялось parse5, CSS — PostCSS 8.5.12. PostCSS сохраняет AST, но не подтверждает допустимость значения CSS или конечный вид. Мир, браузер, computed styles, HTTP, БД, установка/сборка не запускались.

### Сценарии — 16 успешных групп

| № | Проверка | Фактический результат |
| --- | --- | --- |
| 01 | Defaults 13 реальных моделей, unknown | Все поддержанные типы рендерятся; unknown оставляет шапку/пустые контейнеры. Тип модели рецепта установлен по регистрации, не имени JS-файла. |
| 02 | Зарегистрированный diagrams | Manifest/registerDataModels используют diagrams; описание, материалы и шесть тегов появляются. Незарегистрированный diagram проверен как отрицательный вход. |
| 03 | Компоненты/подготовка/пустые требования | Доступный UUID → ResolvedName/resolved.png, quantity 0 сохраняется; недоступный → SavedUnknown без img. Schema удаляет исходный img. vitriol=2 показан, rebis=0/aether=-1 скрыты. Пустой рецепт оставляет заголовок из-за truthy alchemyComponents, строк 0. |
| 04 | Сопротивления ArmorData | resistance.slashing/piercing/bludgeoning=true не создают три тега; плоский контроль создаёт. Новая 00306. |
| 05 | Escaping текста | effect/minorMutation/location/description/sideEffect/liftRequirement с <b>RichText</b> дают &lt;b&gt; в HTML-строке. Нет вывода о невозможности последующего core enrichment @UUID/roll. |
| 06 | 0/false/пустая строка | Условные числовые теги исчезают; Mount.dex Number 0 преобразуется StringField в '0' и виден, hp=0 скрыт. Container даёт четыре безусловных тега, даже при пустых значениях. |
| 07 | Weapon accuracy и hands | -2/0/+2 → 0/0/1 тег точности; положительный содержит +2. hands='both' переводится через настоящий справочник. Новая 00307; отрицательное значение в формуле weaponAttack сверено статически. |
| 08 | TypedObject effects улучшения | Словарь даёт bleeding/35%; процент 0 скрыт, name не печатается. Это itemEffect, не ActiveEffect.changes. |
| 09 | Все статические и configured dynamic переводы | 66 ключей шести HBS: 65 доступны в ru, WITCHER.Weapon.Availability отсутствует и в ru, и в en. concat/capitalize с Inventory.Vitriol работают через core helper. Дополнена 00178. |
| 10 | CSS AST/импорты/дочерние selectors | Все десять файлов имеют единственный прямой @import; 91 rule-узел / 216 declarations. Обе ветви chat.css:45 не достигают h4 из-за section; новая 00308. |
| 11 | Полный producer сообщения | Настоящий _onItemMessage передаёт prepared Item/type='diagrams'/WITCHER; отрендеренный текст содержит актуальное имя компонента. getSpeaker получает OwnerName строкой; 00175 сохранена. Запись чата перехвачена. |
| 12 | Ремонт/компоненты/таблицы | Реальный repair-dialog с components-list даёт обе таблицы/цену, repair-chat — две секции и кнопку запроса. Глобальный th:nth-child второй ветви components-list.css и более ранний table th сверены статически; новая 00309. |
| 13 | Скрытые строки Loot/расследования | Все три настоящих row-partials сохраняют имя в HTML при isHidden=true; GM получает hidden-view, игрок — hidden-from-view. Видимость отделена от прав документа. |
| 14 | Currency/Rewards | Четыре label полей конвертера, отдельная сетка остатков; результат currency-conversion без этого корня. Обе вкладки журнала дают одну logEntry для одной записи. |
| 15 | Девять веществ | _onSubstanceDisplay формирует девять корректных update-путей pannels.<key>IsOpen. Каждый отдельный true даёт одну sub-open, девять иконок. PNG всех девяти веществ существуют; assets вне полного аудита. |
| 16 | Заполненные реальные схемы | Число тегов: alchemical 6, mutagen 4, armor 3, component 6, container/valuable 4, diagrams 6, enhancement 4, mount 4, spell 5, hex 1, ritual 6, weapon 6. Разный состав моделей в общих ветвях сохранён. |

Диагностические ошибки первоначального запуска (plain parent, короткий UUID и неверный контрольный hands='two') исправлены во входах изолированной проверки. Они не являются issues системы. В предварительной оценке ошибочно сопоставлялись diagram/diagrams и неверно складывались строки; окончательный результат сверен с manifest/registerDataModels и точным подсчётом: **diagrams корректен, 920 строк**. Документы задачи/исходники по этим предположениям не изменялись.

### Полнота CSS и связи

| Файл | Строки | Rule-узлы | Declarations |
| --- | --- | --- | --- |
| [styles/chat.css](../../../styles/chat.css) | 74 | 14 | 31 |
| [styles/item-header.css](../../../styles/item-header.css) | 77 | 15 | 33 |
| [styles/item-sheets.css](../../../styles/item-sheets.css) | 117 | 22 | 51 |
| [styles/container-sheet.css](../../../styles/container-sheet.css) | 33 | 6 | 14 |
| [styles/components-list.css](../../../styles/components-list.css) | 20 | 4 | 8 |
| [styles/substances.css](../../../styles/substances.css) | 73 | 12 | 38 |
| [styles/loot-sheet.css](../../../styles/loot-sheet.css) | 27 | 6 | 10 |
| [styles/repair.css](../../../styles/repair.css) | 23 | 5 | 8 |
| [styles/currency-converter.css](../../../styles/currency-converter.css) | 39 | 6 | 21 |
| [styles/rewards.css](../../../styles/rewards.css) | 4 | 1 | 2 |
| **Итого CSS** | **487** | **91** | **216** |

Таблицы карточек сохраняют каждый selector/declaration, !important и вложенный scope. @import в главном CSS: currency 8, loot 11, item-sheets 15, substances 16, container 18, chat 19, item-header 20, repair 23, components 24, rewards 27. Глобальные item-table/hidden-view/item-tag и scoped item-header/.repair различены. Настоящий core sidebar/chat-message.hbs:1/24 задаёт .chat-message/.flavor-text. Классы editor могут создаваться helper; textarea само по себе не .editor.

Не найдены текущие совпадения item-row/item-second-column; в панели веществ нет .substances/.substance-type-subheader и прямых .substances-section > span/table. Это не зарегистрировано как самостоятельная ошибка. substance-img также используется diagrams-sheet и alchemyCraftComponentsList. Loot CSS используется clue/obstacle/mystery. RewardsSheet — extended-sheet, собственный CSS не выполняет выдачу наград. .item-tag background-color в соседнем tab-inventory.css содержит '1px solid' перед цветом; 00310 зарегистрирована по статическому синтаксису, не по несуществующей браузерной проверке.

### Перекрёстная сверка и issues

Прочитаны и сопоставлены целиком, включая поздние уточнения, десять связанных карточек: itemMixin, DiagramData, ArmorData, components-list, item-header, substances, loot-item-display, inventory weapons, currencyConverter HBS и RewardsSheet. В них добавлены встречные ссылки/уточнения. У itemMixin ограничено прежнее утверждение о @UUID: первая HTML-строка и дальнейший ChatMessage.renderHTML/enrichHTML — разные стадии. У inventory weapons убрана недоказанная оценка намерения автора скрывать отрицательную accuracy.

Реестр прежних 305 issues проверен перед регистрацией. Новые [00306](../../issues/potential/issue-00306.md), [00307](../../issues/potential/issue-00307.md), [00308](../../issues/potential/issue-00308.md), [00309](../../issues/potential/issue-00309.md), [00310](../../issues/potential/issue-00310.md) относятся к пяти конкретным наблюдениям. Дополнены [00175](../../issues/potential/issue-00175.md) и [00178](../../issues/potential/issue-00178.md). 00306 отделена от старого пути 00180; недоступное имя компонента в сообщении не повторяет ошибку листа 00095. Ссылки 00200/00029 и историческая общая сверка № 1 сохранены. Все **310 issues** остаются potential, open/closed пусты.

### Итоговая формальная сверка

16 новых карточек, 10 уточнённых; реестр **367 из 621**, не разобраны **254**. В пятой серии **57 из 77** проверены, **20** файлов в очереди .049–.050; **234** вне детализации. TASK-0003 остаётся in-progress, TASK-0004/0005 — draft. Следующая задача — [docs/tasks/task-0003.049.md](../../tasks/task-0003.049.md).

Проверены состав/уникальность 621 пути, соответствие карточек статусам, все 50 подзадач/376 назначенных файлов, локальные ссылки/якоря, таблицы и сохранность исторических записей. Все 621 исходник сравнены с базовым срезом; контрольная сумма набора (path UTF-8 + NUL + bytes в сортировке) — 52701d3d0a5f054319886ac2a9d45b42c26c80098858d02518579c6a1edfaec4. Метаданные mode/uid/gid/inode 1417 отслеживаемых файлов сверены с началом работы. Фактическая проверка завершена: 367 карточек соответствуют 367 строкам «Проверено»; 254 строки «Не начат» без карточек, 376 назначенных файлов уникальны. Проверены 17870 локальных ссылок/якорей — ошибок нет; 112 таблиц в 21 новом документе — без ошибок структуры. Изменены 23 прежних документа, созданы 16 карточек и пять issues; все изменения внутри docs. git diff --check прошёл. Mode/uid/gid/inode всех 1417 прежних отслеживаемых файлов сохранены; предыдущий журнал и общая сверка № 1 не изменены. Контрольная сумма всех 621 исходника совпала с приведённой выше.

## TASK-0003.047

Дата: 2026-09-12. [Способности, эффекты и модификаторы: поля и оформление](../../tasks/task-0003.047.md). Ветка rusbar-main; HEAD 2f94c6c29e298ccf73d67ccc2e5fb8fc358dae2c. Перед началом рабочее дерево чистое. Все 621 исходник совпадают со срезом TASK-0001 15da5b225535e34af4e132c701b5353ef4eb667f; SHA-256 отсортированных UTF-8 путей + NUL + байтов файлов — 52701d3d0a5f054319886ac2a9d45b42c26c80098858d02518579c6a1edfaec4.

### Состав и перекрёстная сверка

| Полностью прочитанный файл | Строки | Предмет проверки |
| --- | --- | --- |
| [module/data/item/templates/effectDerivedStatData.js](files/module/data/item/templates/effectDerivedStatData.js.md) | 9 | effectDerivedStat: id/modifier/derivedStat; default modifier='0'; подключений не найдено |
| [module/data/item/templates/effectSkillData.js](files/module/data/item/templates/effectSkillData.js.md) | 9 | effectSkill: id/modifier/skill; default modifier=''; подключений не найдено |
| [module/data/item/templates/effectStatData.js](files/module/data/item/templates/effectStatData.js.md) | 9 | modifierStat: id/modifier/stat; default modifier='0'; подключений не найдено |
| [styles/activeEffect.css](files/styles/activeEffect.css.md) | 96 | 17 rule-узлов / 35 declarations |
| [styles/configurations/modifier-configuration.css](files/styles/configurations/modifier-configuration.css.md) | 5 | 2 rule-узлов / 1 declarations |
| [styles/crit-wounds-table.css](files/styles/crit-wounds-table.css.md) | 134 | 26 rule-узлов / 52 declarations |
| [styles/profession-sheet.css](files/styles/profession-sheet.css.md) | 240 | 44 rule-узлов / 106 declarations; @keyframes vibrate |
| [styles/special-skill-table.css](files/styles/special-skill-table.css.md) | 51 | 8 rule-узлов / 27 declarations |
| [styles/race-sheet.css](files/styles/race-sheet.css.md) | 3 | 1 rule-узлов / 1 declarations |
| [styles/character/tab-profession.css](files/styles/character/tab-profession.css.md) | 105 | 22 rule-узлов / 35 declarations |
| **Всего** | **661** | **Три фабрики полей и семь CSS;120 CSS rule-узлов и 257 declarations** |

В каждой CSS-карточке перечислены все селекторы и declarations с исходной строкой и полной цепочкой вложенности. В счёт rule-узлов включены контейнеры вложенности без declarations и пять шагов keyframes. Семь файлов содержат один @keyframes и не содержат собственных @import/URL; их подключение находится в witcher-styles.css. special-skill-table.css имеет CRLF; исходные байты сохранены.

Пути и имена трёх фабрик найдены только в собственных определениях. Проверены CommonItemData, registerDataModels, WitcherActiveEffectData, WitcherActiveEffect и мастер WitcherActiveEffectConfig/baseMixin: действующий маршрут использует system.changes и пути totalModifiers/activeEffectModifiers; он не собирается из этих трёх фабрик. Отсутствие вызова ограничено текущим репозиторием и не зарегистрировано проблемой.

Селекторы сопоставлены с исходным HBS, JS-подключением и динамическими классами Foundry. Не считались HTML-потребителями совпадения имён partial/CSS-файлов. В частности, crit-wounds-table.hbs выводит ol/li без .crit-wounds-table; специальный special-skill список не имеет найденных элементов/обработчиков. Напротив, .editor-content и profession active создаются динамически и имеют действующие маршруты.

Уточнены 10 прежних карточек: CommonItemData, WitcherActiveEffectSheet, WitcherModifiersConfiguration, WitcherProfessionSheet, WitcherRaceSheet, effect-part, crit-wounds-table, обе вкладки профессии и Actor activeEffectMixin. Учтены поздние уточнения об Item-раскрытии, legacy monster-sheet и дублях перенесённых улучшений; это проверка связей, не новый полный runtime-аудит прежних файлов. Общие styles/witcher-styles/system-styles/character-sheet и регистрации прочитаны в пределах подключений; собственные полные карточки им здесь не назначены.

### Методика и выполненные проверки

Изолированная команда node --input-type=module с кодом через stdin; файлы стенда не создавались. Импортированы настоящие фабрики, CommonItemData, baseMixin, activeEffectMixin, fields/DataModel/TypeDataModel и randomID установленного Foundry14.367.0. Временный subclass DataModel в памяти служил потребителем каждой фабрики; он не зарегистрирован системой. Счётчик оборачивал настоящий randomID, не заменял алгоритм генерации.

PostCSS8.5.12 разобрал весь CSS в AST; Handlebars4.7.9 и parse5 — исходные шаблоны в структурный HTML. Данные Actor/Item/эффектов, selectOptions, editor, formInput/formGroup, локализация и jQuery представлены фасадами. Поэтому эти рендеры проверяют классы/ветви, не сохранение полей или полноту перевода.

Отдельно извлечён и исполнен настоящий ApplicationV2._prepareTabs: /opt/foundryvtt/client/applications/api/application.mjs:704–717. Полный исходный HTMLProseMirrorElement из client/applications/elements/prosemirror-editor.mjs исполнен с заменёнными базовым InputElement, TextEditor и document.createElement; его настоящий constructor/_buildElements создал классы и дочерние элементы. Редактор ProseMirror/DOM lifecycle не запускался. Defaults StringField проверены по common/data/fields.mjs:160–174,1639–1725, а не выведены из коротких фабрик.

| Группа | Сценарий | Результат |
| --- | --- | --- |
|01 | Два вызова каждой фабрики | Новые словари и 9 независимых пар StringField; randomID ещё не вызван |
|02 | Два экземпляра каждой контрольной DataModel | Отложенные ID: два вызова генератора, разные 16-символьные строки; точные defaults modifier/цели |
|03 | modifier0/−2/12/' /2 '/'2+3'/'wrong'/'' и неизвестная цель | Строки/trim/cast; нет арифметики, диапазона или choices |
|04 | id='own'/''; modifier/цель=null; свойства StringField | Явные id сохраняются; null заменён initial; required=false, nullable=false, blank/trim=true, choices=undefined |
|05 | CommonItemData и подсказки мастера | Нет полей фабрик в общей схеме; настоящий мастер выдаёт пути stats.int.totalModifiers и skills.emp.charisma.activeEffectModifiers |
|06 | Все семь CSS через PostCSS | Структура/nesting сохранены; race1 rule/1 declaration; modifier2 rule/1 declaration; special-skill CRLF |
|07 | Порядок импорта и конфликтующие declarations | Каждый CSS импортирован один раз; profession общий column против Actor row; modifier display:inherit после общей grid-сетки. Специфичность сопоставлена статически, не browser cascade |
|08 | Анимация и состояния | Все пять шагов vibrate; две important-ширины травм; прямой ребёнок remove в hover специального навыка |
|09 | Категории/partial эффекта | Четыре headers, одна row; имя p, не h4; description invisible; suppressed скрыт при actor и виден без него |
|10 | Настоящий _onActiveEffectDisplayInfo | Непустой текст переключил invisible; пустой сохранил состояние. jQuery-фасад |
|11 | Одна травма в текущей вкладке и Item-редакторе | Две строки/поля дней в tab-effects, одна пара в редакторе; классов crit-wounds-table/critwound-display нет |
|12 | Настоящий _prepareTabs | profession active для выбранной вкладки, profession для невыбранной |
|13 | Профессии Character/Monster/Item с заданными навыками |10 карточек и 10 кнопок Character;1 карточка Monster без трёх путей;10 карточек Item,0 кнопок и 3 skill-path-name |
|14 | Раса Character/Item | По 4 perk; legacy editor-фасад у Character,4 prose-mirror-заглушки у Item |
|15 | Настоящий HTMLProseMirrorElement._buildElements | Динамические editor/prosemirror/inactive, div.editor-content и button.icon.toggle |
| **Итог** | **15 групп** | **PASS, exit0; Node24.16.0** |

Дополнительно выполнены rg-поиск всех имён фабрик/классов, чтение текущих/legacy consumers и сопоставление @import с system.json. Отрицательный результат текстового поиска проверен по реальным class-атрибутам и источникам динамических классов. На этапе настройки сценария ожидание nullable=true было исправлено по фактическому DataField default=false и результату очистки null; для исполнения полного класса ядра добавлен отсутствовавший в VM CustomEvent. Это исправления окружения проверки, не системы.

### Сверка каскада и границы

activeEffect.css импортируется позже armor-sheet.css: его .effect-list margin0 заменяет margin-left10px, flex1 остаётся. system-styles .invisible скрывает описание независимо от отступов activeEffect.css. Правило .effect-name > h4 не адресует текущий p; само по себе это не доказанный сбой UI.

Общее profession-sheet.css задаёт column/gap10 для profession-path; более поздний Actor/Monster-scope в character/tab-profession.css — row/gap0 только внутри активной вкладки. Основной Item этот scope не получает. У Monster HBS нет трёх путей/расы, хотя некоторые CSS-ветви их описывают. Фиксированные размеры и -webkit-fill-available перечислены как declarations, а не измеренная геометрия.

modifier-configuration.css имеет более специфичный селектор, чем общая сетка Actor: заменяет только display на inherit; width520 находится в JS. race-sheet.css задаёт height150px внутреннему editor-content, не ширину 600 окна и не весь .perk. Источник --color-shadow-primary для тени травм найден в /opt/foundryvtt/public/css/foundry2.css:95/255; все пользовательские темы не обследованы.

### Issues

Новых issues нет. Уточнены [00054](../../issues/potential/issue-00054.md) (два списка травм создаёт HBS, не старые табличные стили) и [00056](../../issues/potential/issue-00056.md) (CSS не добавляет отсутствующее раскрытие Item). Остальные наблюдения о неподключённых фабриках/селекторах не превращены в требования удаления или новые задачи.

Все 305 issues остаются potential; open/closed без карточек. [109](../../issues/potential/issue-00109.md) об enriched тексте и [165](../../issues/potential/issue-00165.md) о дублях улучшений не объявлены опровергнутыми рендером обычных данных этой порции. Подтверждение пользователем и исправления не выполнялись.

### Формальная сверка и результат

Реестр:351 из 621 файлов проверены,270 не начаты. В пятой серии 41 из 77 проверены,36 в очереди;234 требуют следующего планирования. Все 50 подзадач охватывают 376 уникальных файлов без пересечений. Десять новых карточек имеют обязательные разделы, ссылки на источники и сверку; проверены состав/статусы, 17 434 локальные ссылки/якоря по всему docs и структура 46 таблиц новых документов.

Исходники совпадают с базовым срезом, изменена только документация; метаданные доступа 1407 существовавших tracked-путей (mode/uid/gid/inode) сохранены. Исторические записи review-log и cross-check-0001 сохранены; git diff --check выполнен. Полный браузер, вычисленные стили/раскладка, мир, HTTP-доступ службы, БД, сборка/извлечение компедиумов и установка зависимостей не запускались.

[TASK-0003.047](../../tasks/task-0003.047.md) выполнена; следующая — [TASK-0003.048](../../tasks/task-0003.048.md). TASK-0003 остаётся in-progress, TASK-0004/0005 — draft. Материал дополняет будущую TASK-0004, не заменяет её.

## TASK-0003.046

Дата: 2026-09-12. Порция: [Словесный бой: атака, защита, сообщения и Resolve](../../tasks/task-0003.046.md). Ветка rusbar-main; HEAD a69f11d2e4c4318cfbf635dabad97b0062c63c20. Перед началом рабочее дерево чистое. Все 621 исходник совпадают со срезом TASK-0001 15da5b225535e34af4e132c701b5353ef4eb667f; SHA-256 списка путей и содержимого — 52701d3d0a5f054319886ac2a9d45b42c26c80098858d02518579c6a1edfaec4 (отсортированный UTF-8 путь + NUL + байты файла).

### Состав и перекрёстная сверка

| Полностью прочитанный файл | Строки | Проверенная связь и результат |
| --- | --- | --- |
| [verbalCombatMixin.js](files/module/actor/mixins/verbalCombatMixin.js.md) |101 | Object.assign Actor → общий лист/Counterargue → prompt → все 16 действий CONFIG → addPart/addActiveEffects → damage DTO → extendedRoll/два flags |
| [verbalCombat.js](files/module/scripts/verbalCombat/verbalCombat.js.md) |55 | Render/menu Hooks → message closure → getFlag → обычный Roll → сообщение; выбор Actor/DOM total → update Resolve; старый массовый listener не имеет найденных внешних вызовов |
| [verbalCombatDefense.js](files/module/scripts/verbalCombat/verbalCombatDefense.js.md) |118 | Menu → scalar totalAttack → Dialog V1 → четыре защиты → base DTO/flags; Counterargue открывает общий action |
| [verbal-combat.hbs](files/templates/dialog/verbal-combat.hbs.md) |14 | Два each,5 групп/16 radio, checked у каждого, group/value и текстовый customModifiers |
| [verbal-combat-defense.hbs](files/templates/dialog/verbal-combat-defense.hbs.md) |13 |4 radio без checked; producer передаёт только defenses, cssClass/groupName отсутствуют |
| **Всего** | **301** | **Пять карточек;12 именованных функций/методов JS и существенные callbacks описаны. У обоих HBS нет завершающего newline.** |

Сопоставлены определения и обращения: CONFIG skillMap/statMap/verbalCombat, modifierMixin.addActiveEffects, helper.addPart/getInteractActor, RollConfig, extendedRoll, ChatMessageData, DamageMessageData/BaseMessageData, регистрация Hooks в TheWitcherTRPG, Object.assign и расчёт Resolve Actor, общий лист V2 и аналог V1. Проверены оба producer шаблонов, имена полей, кнопки/маркеры и consumers flags; область поиска — module/templates, без внешних макросов. Уточнены 10 связанных карточек: TheWitcherTRPG, config, witcherActor, WitcherActorSheet, helper, modifierMixin, extendedRoll, RollConfig, ChatMessageData и DamageMessageData. Старые номера строк verbalCombat/защиты в нескольких таблицах приведены к текущему срезу. Соседи не засчитаны повторно.

Матрица 16 действий дана в карточке Actor. Особо сверены deceit/perception/gambling на EMP; характеристика навыка не обязана совпадать с dmgStat. Persuade делит d6, затем прибавляет EMP. Общий диалог включает Defenses/Tools; специальный callback Counterargue открывает новую атаку без прежнего threshold. Строки effect только показываются: автоматическое создание ActiveEffect/Status/Item этими файлами отсутствует. Соответствие книги и расширение автоматизации не оценивались.

### Методика

Выполнена изолированная команда node --input-type=module с JS через stdin, без создания файлов стенда. Три полных JS-файла прочитаны и исполнены в VM после снятия import/export; исходные тела не переписывались. CONFIG, RollConfig, ChatMessageData, addPart, modifierMixin и extendedRoll импортированы из системы. Настоящие Foundry14.367.0 DataModel/TypeDataModel/fields, DMD/BMD, Roll/термы/parser использованы локально; Handlebars, parse5 и peggy взяты из уже установленных зависимостей Foundry. Не выполнялись npm install/build и извлечение packs.

Кубики запускались через настоящий evaluate с заданными minimize/maximize; Roll.toMessage/getSpeaker/setFlag заменены захватом. Actor, формы/радио, getInteractActor, DialogV2.prompt и создание Dialog V1 — фасады. Для проверок завершения использованы управляемые Promise. Отдельно извлечены и исполнены настоящие core concat, ContextMenu._onClickItem и Dialog V1.submit; у них UI/render/close представлены фасадами. Поэтому проверка callback-контракта не равна полному browser lifecycle.

Первичные локальные источники ядра: /opt/foundryvtt/client/client.mjs:170 (global Dialog), client/appv1/api/dialog-v1.mjs:215–224 (submit и jQuery), client/applications/ux/context-menu.mjs (_onClickItem), applications/api/application.mjs:2230–2235 и applications/sidebar/tabs/chat.mjs:398–403 (DOM target), client/applications/handlebars.mjs:199 (concat). Legacy Dialog существует в 14, устаревает до 16; html.find в его callback допустим. li.find в меню ChatLog относится к другому контракту.

Локализация использовала словари en/ru, настоящий expandObject/getProperty и en fallback. Проверены 14 буквальных ключей и все динамические варианты имени/урона в 16 действиях. Полный Localization service не создавался.

### Выполненные сценарии

| Группа | Сценарий и наблюдаемый результат |
| --- | --- |
|01 | Все 16 CONFIG-записей: точные навыки/характеристики/формулы/flags; общий HBS даёт 16 radio и 5 групп, checked у каждого |
|02 | EMP7/навык 2/d10=1: custom0/−2/+2/2+3 →10/8/12/15; детали дают [Empathy], формула разбирается настоящим Roll |
|03 | Настоящий modifierMixin: прямой 3 + allSkills2 добавляются к 10 →15; Counterargue без skill оставляет 1d10 |
|04 | Атака: нет radio/неизвестное действие → TypeError; отказ prompt останавливает до Roll |
|05 | Глобальный Intimidate из другого окна сочетается с custom4 текущей формы Seduce:1d10+5+2+4 |
|06 | await Actor.verbalCombat завершается при pending extendedRoll; verbalCombat flag хранит тот же объект CONFIG |
|07 | Настоящая DamageMessageData очищает vcDamage, сохраняет rollTotal10; base имеет rollTotal, flags находятся вне system-схемы |
|08 | Настоящий extendedRoll создаёт сообщение до завершения двух setFlag; немедленный consumer видит отсутствующий damage; после разрешения флаг доступен |
|09 | Текущий listener связывает первую кнопку, замыкает message и игнорирует вложенный target; повторная привязка добавляет второй listener; отсутствие кнопки безопасно |
|10 | Неиспользуемый массовый helper падает на .each у Element/null; текущая регистрация его не вызывает |
|11 | Оба predicates меню возвращают undefined для существующего DOM-маркера; принудительные callbacks падают на [0].innerText либо .find |
|12 | Настоящий dispatch ContextMenu14 передаёт HTMLElement в callback; реальные predicates скрывают пункты. Полный render не исполнялся |
|13 | Настоящие Roll2+3=5,1d6/2+7=7.5 при minimize,−2=−2; parse5 обнаружил атрибут '<h1' вместо h1 в словесном flavor |
|14 | Нет name/formula либо формула NONE → отклонение; rollDamage ждёт toMessage, но не последующий setFlag |
|15 | Resolve10: урон 3.8/'3.8' →7,0→10,−2→12,15→−5,'?'→NaN в запросе update; без Actor ошибка, статусы/эффекты не применяются |
|16 | Два ожидаемых метода урона 3/4 возвращаются до update, готовят 7/6 из Resolve10; разрешённые записи оставляют 6. Это фасад записи, не реальный сетевой конфликт |
|17 | Защита: нет Actor → нет окна; Cancel без callback; нет radio → нет броска;4 radio без checked, data-group='/' из незаполненного unquoted атрибута |
|18 | Все 4 защиты:3 обычных base DTO/defense=true/threshold20 и потерянный thresholdDesc; Counterargue запускает actor.verbalCombat без передачи прежнего 99/custom4 |
|19 | Defense custom0/−2/+2 →8/6/10 при заданных Actor/минимальном d10; строка 2+3 пропускается сравнением с 0; детали содержат [Custom] |
|20 | Глобальный Seduce из окна атаки не существует в Defenses → TypeError; допустимый ChangeSubject работает в изоляции |
|21 | createRollConfig получает numeric skill, label undefined; настоящий extendedRoll:8=8 успех,8<9 провал,8>7 успех; подпись заменяется числом порога |
|22 | Настоящая защита с контролируемыми кубиками: fumble7<8 неуспешен, крит 18=18 успешен |
|23 | Обычный defense callback ждёт extendedRoll; executeDefense только открывает окно, messageId не используется |
|24 |16 вариантов в en/ru: кнопки у девяти baseDmg; None/CounterargueDmg не создают кнопку; отсутствующий ru customModifier показывает en fallback |
|25 | Настоящий Dialog V1.submit передаёт jQuery и закрывает окно, не ожидая async callback |
|26 |14 буквальных ключей: все есть в en, в ru отсутствует только уже известный WITCHER.Dialog.customModifier |
| **Результат** | **26 групп PASS; exit0. Настоящая логика отделена от фасадов и статического чтения.** |

Ожидаемые числа заданы отдельно от проверяемых функций. При настройке проверок ошибочные ожидания характеристик deceit/perception/gambling были сверены с CONFIG и исправлены в памяти; ожидание пустого data-group уточнено до фактического '/' по parse5. Это поправки сценария, не изменения системы и не выявленные дефекты CONFIG.

### Issues и пределы вывода

Новые potential: [302](../../issues/potential/issue-00302.md) — меню DOM/jQuery; [303](../../issues/potential/issue-00303.md) — глобальный выбор из другого окна; [304](../../issues/potential/issue-00304.md) — возврат до броска/Resolve-update; [305](../../issues/potential/issue-00305.md) — числовой skill вместо описания в конфигурации результата.

Уточнены пять прежних: [184](../../issues/potential/issue-00184.md) (post-message flags), [149](../../issues/potential/issue-00149.md) (нет Actor), [186](../../issues/potential/issue-00186.md) (ru customModifier), [293](../../issues/potential/issue-00293.md) (второй producer malformed HTML), [127](../../issues/potential/issue-00127.md) (внешняя обёртка листа против нижнего метода). Дубли не создавались для этих наблюдений; все 305 карточек остаются potential. Воспроизведение агентом не заменяет подтверждения пользователя.

Скрытые пункты 302 — ранний барьер штатного UI. Прямые проверки последующих функций не объявлены успешным полным словесным боем. Очистка vcDamage не означает потерю используемой формулы: consumer читает flags. Потерянная подпись 305 не изменяет правило равенства. Ввод 2+3 в защите и значения Resolve за границами описаны как контракт входа; новые игровые ограничения не предлагались как принятые. Мир, браузер, БД, HTTP-доступ службы, сетевой порядок нескольких клиентов и реальные права не проверялись.

### Формальная сверка и результат

Реестр и карточки:341 из 621 проверены,280 не начаты. В пятой серии 31 из 77 проверены,46 в очереди;234 файла требуют последующего планирования. Все 50 подзадач по-прежнему охватывают 376 уникальных файлов. Полные исходники, назначения/ссылки/статусы, шаблонные разделы и таблицы новых документов сверены; проверены 17 195 локальных ссылок/якорей по всему docs и структура 41 таблицы новых документов. Исторические записи журнала и cross-check-0001 сохранены. Метаданные доступа 1398 существовавших tracked-путей (mode, uid, gid, inode) сохранены; git diff --check выполнен. Менялась только документация;9 новых документов — пять карточек и четыре issues.

[TASK-0003.046](../../tasks/task-0003.046.md) выполнена; следующая — [TASK-0003.047](../../tasks/task-0003.047.md). TASK-0003 остаётся in-progress, TASK-0004/0005 — draft. Общая сверка .045 остаётся вспомогательным материалом для TASK-0004; данная запись дополняет материал связями словесного боя, не заменяет общий этап.

## TASK-0003.045

Дата:2026-09-12. Ветка rusbar-main, HEAD 20ce99a1218a82bf46c84570e55587253d0cfbc3; на старте дерево чистое. Все 621 исходник совпадают со срезом TASK-0001 15da5b225535e34af4e132c701b5353ef4eb667f. SHA256(sorted path UTF-8 + NUL + bytes):52701d3d0a5f054319886ac2a9d45b42c26c80098858d02518579c6a1edfaec4.

### Область и результат

Выполнена [TASK-0003.045](../../tasks/task-0003.045.md):5 файлов /336 логических строк,19 именованных функций и существенные callbacks,1 HBS. Карточки перечислены в последних пяти строках общей матрицы ниже. Покрытие 331→336 из 621, остаток 285; пятая серия 26 из 77 проверены,51 в очереди,234 вне детализированного плана. TASK-0003 in-progress, TASK-0004/0005 draft; следующая .046.

Выполнены **32 группы проверок**, общая сверка 26 файлов .041–.045 и документированных связей с прежними 310 карточками. Уточнены 11 связанных карточек и 11 прежних issues; добавлены 3 новых potential issues299–301. Исправления кода/игровых данных и подтверждение проблем не выполнялись.

### Методика и пределы

Чтение исходников целиком, rg/rg --files для определений, импортов/регистраций, вызовов, моделей и consumers. Локальные Foundry14.367.0 и Node24.16.0. Исполнение: node --input-type=module через quoted stdin heredoc; код проверок существует в памяти инструмента, файлы стенда не создавались.

Настоящие полные тела четырёх JS текущей порции загружены vm с удалением import/export только для задания явных зависимостей; дополнительно реальные setup/hooks.js/socketHook.js. Импортированы настоящие DamageInstance, DamageMessageData, DefenseMessageData, MonsterData, фабрика combatEffects и healMixin, Foundry DataModel/fields и utils, CONFIG.WITCHER, Handlebars. Настоящий ContextMenu импортирован из ядра: _onActivate/_onClickItem исполнялись на минимальном DOM, render/close заменены. Факт jQuery:false установлен чтением ApplicationV2 factory и ChatLog. Реальный Socket.IO4.8.3 создан autoConnect:false, emit/буфер проверены без соединения.

Группы 29–31 используют полный настоящий Actor.damageMixin, armorMixin, damageUtilMixin, DamageInstance/ArmorData/MonsterData и извлечённые неизменённые location static/getList. Функции эффектов/UUID, Actor/Item-документы, ChatMessage, game/settings/user/коллекции, prompt и update — фасады. Обычный update применяет поля в памяти; для очередиHP update возвращает управляемый Promise. Это позволяет установить аргументы/ожидания и результат определённого порядка, но не моделирует серверную очередь или весь prepareData lifecycle. Получение getInteractActor в этой порции задано фасадом; прежние проверки выбора/отмены helper не объявлены повторёнными.

В первичном адаптере ожидание одного setImmediate не гарантировало завершения асинхронного чтения HBS: шаблоны предварительно скомпилированы в памяти, результат проверен повторно. В интеграционной группе 30 shield-update первоначально попал в списокHP как undefined; фильтр выделил HP-записи, щитовые применены отдельно. Изменены только проверки, не исходник. Итоговые запуски 28+3+1 завершились exit0.

### Сценарии текущей порции

| Группа | Наблюдаемый результат |
| --- | --- |
| 01 | Attack listener: первая button.damage, вложенный event.target не меняет замкнутое сообщение; повторная регистрация добавляет второй listener, отсутствие кнопок допустимо. |
| 02 | Старый/отсутствующий UUID → onDamage TypeError; одиночный listener не принимает jQuery. Старый массовый wrapper проверен на пропуске неизвестного сообщения; прямых callers не найдено. |
| 03 | Все button.stun/crit-stun связаны; две обычные передали 4, критическая — undefined; вложенный target не влияет. |
| 04 | Отсутствующий Actor: executeDefense выходит, stun и три critical callbacks отклоняются. |
| 05 | Меню передало пять исходных полей защиты и identity crit; неизвестное сообщение ломает visible/executeDefense. |
| 06 | Настоящий ContextMenu14._onClickItem вызвал callback(target,event) и onClick(event,target). ApplicationV2._createContextMenu задаёт jQuery:false, ChatLog использует этот factory. |
| 07 | Первый DOM total7.9 →7 вопреки rolls99/1 и второму DOM99; normal→HP, isNonLethal→STA, forced→STA. |
| 08 | Маркер damage-message без dice-total проходит visible и даёт TypeError; текст? даёт NaN в DamageInstance. |
| 09 | ApplyNormalDamage возвращается при pending prompt; applyDamageFromMessage/applyDamageFromStatus — при pending Actor.applyDamage. |
| 10 | Настоящий callback inline prompt:8 options, monster controls/checked и пять выходных полей; rejectClose:true. |
| 11 | Отмена prompt отклоняет внутренний applyDamageFromMessage до Actor; отсутствующие message/Actor дают ошибки на соответствующих границах. |
| 12 | Настоящий DamageMessageData удалил duration; первый выбор head/oil некрофага изменил prepared, _source остался torso/пусто; следующий Actor с Empty/без масла получил прежние head/oil. |
| 13 | Исходный registerHooks одинаково вызывает общий handler при flags/start/turn; неактивный GM отсекается; пустой combatant вызывает ошибку. |
| 14 | Character/zero/dead останавливают регенерацию; dead не останавливает отдельный status damage. |
| 15 | HP19/max20+regen2 запросил 20; сообщение показывает 19/2, escaped name и whisper текущего GM; при полномHP повторно сообщение/update20. |
| 16 | Настоящая MonsterData принимает regeneration−3; при HP1 consumer запросил−2. Это граница без выбора нового правила. |
| 17 | Регенерация/root завершаются при pending update; отсутствие Actor отдельно отклоняет обе внутренние ветви. |
| 18 | Настоящая turnStartEffects схема:damage5+2→7, type fire потерян, heal3/modifier2→+3; allLocations/ignoreArmor/bypassesShield/spDamage передаются. |
| 19 | Modifier-only при amount0 пропускается; amount−1 создаёт status-message без урона; amount2/modifier−5→damage−3 в STA. |
| 20 | Реальное calculateHealValue:HP19/max20,heal3→1; при полномHP heal-message нет; heal-ветвь ждёт pending update. |
| 21 | С facade Actor.applyDamage два статуса 3/4 изHP10 подготовили 7/6, затем итог 6. Это проверка очереди, повторённая настоящими методами в 30. |
| 22 | Регенерация 2 и heal3 запустили записи 12/13 изHP10 до завершения regen update. |
| 23 | Настоящий DefenseMessageData удалил critEffectModifier6; critical menu передал этот же очищенный crit. |
| 24 | Socket sender: guards socket/user/users, GM,нет activeGM; допустимый envelope сохраняет reference data, канал точный, ack-аргумента нет. |
| 25 | Настоящий Socket.IO4.8.3 с autoConnect:false:emit возвращает Socket, два события остаются sendBuffer, acks пуст; соединение не создавалось. |
| 26 | Настоящий receiver игнорирует другого GM/игрока; activeGM вызывает addItem/restoreReliability, data.shift удаляет UUID из полученного массива. |
| 27 | Unknown type,null message/data,пустой UUID/нет документа отклоняют callback; следующий правильный запрос исполняется. |
| 28 | Receiver завершается при pending addItem; _createMessage содержит только type/data, результата операции нет. |
| 29 | Настоящий status→Actor.damageMixin:при fire.flat4 потерянный тип даёт урон 5 (HP100→95), контроль с type fire даёт 9 (95→86). |
| 30 | Настоящие status/Actor.damageMixin/armorMixin/locationMixin/DamageInstance:два pending HP update97/96 из 100, итог 96 после записи; математически последовательный урон 3+4 оставил бы 93. Щитовые update исполнялись сразу. |
| 31 | Настоящий положительный status.amount2/modifier−5 дал damage−3, shield5→8,HP100 неизменён; уточнение 291. |
| 32 | 22 буквальных ключа локализации трёх файлов проверены штатными expandObject/getProperty:все есть в en/ru; динамическое DamageType по произвольному input этим не покрыто. |

### Общая сверка .041–.045 с предыдущими карточками

Точный состав:26 файлов /2423 строки (687+477+320+603+336). Для всех 26 проверены существование полных карточек, исходные определения/импорты и направления к producers/consumers, описанные ниже. Машинно прочитаны ссылки всех 310 прежних карточек; объединение прямых и обратных документированных пересечений включает 79 из них. Остальные 231 не имеют найденного ссылочного пересечения с этими 26; это не доказательство отсутствия динамической зависимости.

Числа «назад/вперёд» — количество прежних карточек, которые ссылаются на файл, и количество прежних файлов, на которые ссылается его карточка; срез перед добавлением уточнений .045. Они включают ссылки на исходник и карточку с устранением дублей, не являются числами вызовов. Все явные относительные JS-import этих 26 отражены в карточках; пропусков нет. Полный повторный runtime-разбор 79 или 310 файлов не выполнялся: содержательная сверка ограничена обозначенными границами. Исторические результаты .041–.044 используются с их исходными пределами.

| Файл / карточка | Строк | Назад / вперёд | Сопоставленная связь и пределы |
| --- | --- | --- | --- |
| [module/actor/mixins/weaponAttackMixin.js](files/module/actor/mixins/weaponAttackMixin.js.md) | 382 | 29 / 20 | weaponAttack → AttackMessageData → кнопка/combat.js; serialized rollOnlyDmg отдельно (297), не проходящий контролем обычной атаки. |
| [templates/dialog/combat/weapon-attack.hbs](files/templates/dialog/combat/weapon-attack.hbs.md) | 270 | 4 / 4 | Контекст/controls weaponAttack и две группы CSS; ammo raw HTML (266); составной Roll и массив отдельных Roll не смешаны. |
| [styles/weapon-roll.css](files/styles/weapon-roll.css.md) | 19 | 2 / 1 | @import witcher-styles и .weapon_roll_sheet; профиль .041 сохранён, computedStyle не повторялся. |
| [styles/attack-sheet.css](files/styles/attack-sheet.css.md) | 16 | 2 / 2 | Общий attack-sheet и глобальный h2 img; невалидность word-wrap из 267 остаётся прежним наблюдением. |
| [module/actor/mixins/defenseMixin.js](files/module/actor/mixins/defenseMixin.js.md) | 457 | 38 / 21 | Item options/подготовленные Actor-поля → defense → очищенный crit; фактический menu consumer проверен в 05/23. |
| [module/item/mixins/defenseOptionMixin.js](files/module/item/mixins/defenseOptionMixin.js.md) | 9 | 5 / 5 | Item wrapper → createDefenseOption модели; коллизии value одинаковых имён (268) не исправлены. |
| [templates/chat/combat/defense/defense.hbs](files/templates/chat/combat/defense/defense.hbs.md) | 2 | 1 / 3 | defenseName/displayFormula из producer; ChatMessageData.append добавляет HTML. |
| [templates/chat/combat/defense/defenseCrit.hbs](files/templates/chat/combat/defense/defenseCrit.hbs.md) | 6 | 0 / 2 | crit-taken/crit-stun доступны menu/listener; critEffectModifier теряется в модели, не в HBS. |
| [templates/chat/combat/defense/defenseStun.hbs](files/templates/chat/combat/defense/defenseStun.hbs.md) | 3 | 0 / 2 | button.stun привязан ко всем кнопкам; число из attackWeaponProperties, для shield ранняя проблема 272 сохранена. |
| [module/actor/mixins/armorMixin.js](files/module/actor/mixins/armorMixin.js.md) | 285 | 12 / 10 | Данные ArmorData/SP/resistance и Actor; общий тип статуса теперь прослежен до getter, полная матрица слоёв .043 не повторялась. |
| [module/actor/mixins/locationMixin.js](files/module/actor/mixins/locationMixin.js.md) | 11 | 5 / 5 | Actor static/getLocationObject, all-locations wrapper теряет monster this (32); ручной tailWing допустим отдельно. |
| [styles/armor-sheet.css](files/styles/armor-sheet.css.md) | 24 | 1 / 9 | Фактические armor/effects классы и legacy monster partial различены; нового UI-вывода нет. |
| [module/item/mixins/damageUtilMixin.js](files/module/item/mixins/damageUtilMixin.js.md) | 109 | 13 / 11 | Item.rollDamage → DamageMessageData → menu; методы DamageProperties есть в AttackMessageData, отсутствуют у plain DTO (297). |
| [module/scripts/damageInstance.js](files/module/scripts/damageInstance.js.md) | 52 | 1 / 0 | Один экземпляр на menu/status; type undefined передан реально; общий mutable массив всех зон остаётся 285. |
| [templates/dialog/combat/variableDamage.hbs](files/templates/dialog/combat/variableDamage.hbs.md) | 6 | 0 / 0 | Контекст currentDamage/окно принадлежит rollDamage; отдельный диалог применения урона — inline JS .045. |
| [module/actor/mixins/damageMixin.js](files/module/actor/mixins/damageMixin.js.md) | 356 | 20 / 17 | Actor.applyDamage → shield/SP/location/modifiers/HP/effects; новая проверка очереди реальных методов 29–31. |
| [module/actor/mixins/damageUtilMixin.js](files/module/actor/mixins/damageUtilMixin.js.md) | 17 | 3 / 5 | getFlatDamageMod читает damage.type; отсутствующий fire пропускает flat4 (21); applyAP неверный путь 25 остаётся. |
| [templates/chat/damage/damageToLocation.hbs](files/templates/chat/damage/damageToLocation.hbs.md) | 40 | 1 / 1 | Контекст detail damageToLocation с ошибкой 287; подмена сообщений в .045 не подтверждает исправный HTML. |
| [templates/chat/damage/damageToAllLocations.hbs](files/templates/chat/damage/damageToAllLocations.hbs.md) | 15 | 0 / 1 | Общий итог/массив результатов с ошибкой 287 и shared instances285; не смешан с несколькими turnStartEffects299. |
| [templates/chat/damage/shieldAbsorbs.hbs](files/templates/chat/damage/shieldAbsorbs.hbs.md) | 5 | 0 / 0 | Сообщение поглощения не означает завершённый update щита;292 отдельно от 299. |
| [templates/chat/damage/spAbsorbs.hbs](files/templates/chat/damage/spAbsorbs.hbs.md) | 3 | 0 / 0 | Раннее поглощение SP и информационное сообщение; эффекты applyOnDamage после SP (290) не исправлены. |
| [module/scripts/combat/combat.js](files/module/scripts/combat/combat.js.md) | 96 | 8 / 10 | Два render-listener и два menu extender; HTMLElement, target, UUID и выбранный Actor — группы 01–06/23. |
| [module/scripts/combat/applyDamage.js](files/module/scripts/combat/applyDamage.js.md) | 124 | 9 / 8 | Меню/inline prompt → HP/STA/DamageInstance; cleaned/prepared/source и ожидаемость —07–12. |
| [module/scripts/combat/generalCombatHook.js](files/module/scripts/combat/generalCombatHook.js.md) | 87 | 8 / 11 | Hook/current Actor → regen/status → реальные расчёты;13–22/29–31. |
| [templates/chat/combat/regeneration.hbs](files/templates/chat/combat/regeneration.hbs.md) | 8 | 1 / 2 | Контекст {actor} до update, escaped name и GM whisper;15. |
| [module/scripts/socket/socketMessage.js](files/module/scripts/socket/socketMessage.js.md) | 21 | 3 / 8 | Только repair/gift → общий канал → activeGM receiver;24–28, отдельно от User.query. |

### Сопоставление issues и противоречий

Машинно прочитаны 301 документа potential для привязки путей к матрице; статус не заменён результатом теста. Для содержательной сверки причин использованы карточки и прежние журналы:

| Граница | Issues / решение сверки |
| --- | --- |
| Запуск и пустой контекст Combat | [6](../../issues/potential/issue-00006.md) — любое update; [145](../../issues/potential/issue-00145.md) дополнена общей ветвью. Новая[299](../../issues/potential/issue-00299.md) про ожидание записей имеет другую причину. |
| Выбор Actor и устаревшая кнопка | [149](../../issues/potential/issue-00149.md) уже включала combat/applyDamage, дополнена исполнением без нового дубля; [239](../../issues/potential/issue-00239.md) — Item у onDamage. [108](../../issues/potential/issue-00108.md) — другой repair handler/event.target, не переносится на боевые closures. |
| Схемы до и после сообщения | [257](../../issues/potential/issue-00257.md) — duration; [258](../../issues/potential/issue-00258.md) — critEffectModifier; [297](../../issues/potential/issue-00297.md) — plain properties в rollOnlyDmg. Успешный обычный AttackMessageData-контроль не устраняет ранний барьер rollOnlyDmg. |
| Форма предметных воздействий | [70](../../issues/potential/issue-00070.md) — producer/преобразование; [295](../../issues/potential/issue-00295.md) — неизвестный ID; applied-array после сообщения и Item TypedObject различены. |
| Тип и интенсивность статуса | [21](../../issues/potential/issue-00021.md), [22](../../issues/potential/issue-00022.md) повторены; [291](../../issues/potential/issue-00291.md) получила реальный источник отрицательного итогового damage. |
| Броня/щиты/общий массив | [282](../../issues/potential/issue-00282.md), [292](../../issues/potential/issue-00292.md) — отдельные SP/shield-записи; [285](../../issues/potential/issue-00285.md) — shared DamageInstance по локациям; [299](../../issues/potential/issue-00299.md) — несколько отдельных status-запросов HP. Это не один дефект. |
| Модификаторы и типы сопротивлений | [25](../../issues/potential/issue-00025.md), [26](../../issues/potential/issue-00026.md), [27](../../issues/potential/issue-00027.md), [280](../../issues/potential/issue-00280.md), [286](../../issues/potential/issue-00286.md): неверный путь, кратность, flat и разные типы имеют разные условия; статус без fire отдельно 21. |
| Перечисление локаций | [32](../../issues/potential/issue-00032.md): getAllLocations теряет контекст. Корректный единичный tailWing в dialog/location не опровергает дефект списка. |
| Масло/локация сообщения | Новая[300](../../issues/potential/issue-00300.md): воспроизведены два последовательных применения DamageMessageData. Прежняя .042 описывала изменение location в критической защите без повторного consumer; это иной участок, не новый вывод о правилах крита. |
| HTML и итог броска | [287](../../issues/potential/issue-00287.md) — поля detail; [293](../../issues/potential/issue-00293.md) — malformed flavor; новая[301](../../issues/potential/issue-00301.md) — отсутствие/нечисловой DOM total. parseInt первого итога не объявлен ошибкой обычной составной формулы. |
| Травма и временные HP | [288](../../issues/potential/issue-00288.md), [289](../../issues/potential/issue-00289.md), [294](../../issues/potential/issue-00294.md): quantity/выбор Item/миграция AE — самостоятельные причины. Передача crit menu не доказывает успешность этих downstream операций. |
| Сокет и ремонт/передача | [10](../../issues/potential/issue-00010.md), [169](../../issues/potential/issue-00169.md) дополнены guards/receiver/буфером. Это другой протокол, чем User.query и [8](../../issues/potential/issue-00008.md). |
| Сохранённый дубль | [200](../../issues/potential/issue-00200.md) и[29](../../issues/potential/issue-00029.md) остаются potential, как в [протоколе 1](cross-check-0001.md). В новой порции аналогичные уже зарегистрированным наблюдения 149/145/239/21/22 не размножались. |

Противоречие между «старый callback» и «меню сломано» разрешено чтением/исполнением настоящего ContextMenu: этот callback ещё поддерживается. Поведение первой damage-кнопки и неиспользуемого legacy wrapper описано отдельно от штатной регистрации. Старые карточки со словами «будет разобрано позже» дополнены актуальным состоянием и конкретными пределами; прошлые протоколы не переписаны.

### Изменения документов и контроль

Добавлены 5 карточек и 3 issues299–301; обновлены 11 связанных карточек: hooks, socketHook, helper, combatEffectsData, DamageMessageData, DefenseMessageData, Actor.damageMixin, Actor.defenseMixin, Item.damageUtilMixin, itemContextMenu, healMixin. Дополнены 11 прежних issues:6,10,21,22,145,149,169,239,257,258,291. Задача .045, родитель, указатели, реестры, журнал и CHANGELOG согласованы.

Формальная проверка:336 карточек соответствуют 336 строкам «Проверено»,285 «Не начат»;50 подзадач сохраняют 376 уникальных назначенных файлов,51 в .046–.050. Все 301 issues остаются potential, open/closed без issues. Локальные ссылки и якоря проверены после правок; исходники 621, прежний журнал и метаданные доступа 1390 отслеживаемых путей сохранены. Итог: 16 964 локальные ссылки/якоря — ошибок нет; 40 таблиц восьми новых документов имеют корректные разделители и число ячеек; git diff --check прошёл. Изменены 33 прежних документа, добавлены 8; всё внутри docs. У всех 1390 исходно отслеживаемых путей совпали mode/uid/gid/inode. Агрегат исходников совпал с приведённым выше; прежний журнал сохранён побайтово после новой записи.

Границы результата: не запускались мир/браузер/БД, сборка, HTTP-служба, реальная сеть/доставка сокета и межклиентские сценарии. Никакие правила игры, код, настройки, права или ветки не менялись; коммит агент не создавал. Общая сверка — вспомогательный материал для TASK-0004, которая остаётся draft.

## TASK-0003.044

Дата: 2026-09-12. Ветка rusbar-main; HEAD 965132d5d7972a0edd73aaa62484a1b6ba15991f. Перед работой дерево чистое. Все 621 исходник реестра побайтово совпадают со срезом TASK-0001 15da5b225535e34af4e132c701b5353ef4eb667f; агрегат SHA256 по sorted(path UTF-8 + NUL + bytes): 52701d3d0a5f054319886ac2a9d45b42c26c80098858d02518579c6a1edfaec4.

### Область и результат

Выполнена [TASK-0003.044](../../tasks/task-0003.044.md):9 файлов /603 логические строки. Четыре JS: Item.damageUtilMixin (3 метода), DamageInstance (10 определений), Actor.damageMixin (12 методов), Actor.damageUtilMixin (2 метода); пять HBS. Полные карточки:

| Файл | Строк | Карточка |
| --- | --- | --- |
| module/actor/mixins/damageMixin.js | 356 | [Описание](files/module/actor/mixins/damageMixin.js.md) |
| module/item/mixins/damageUtilMixin.js | 109 | [Описание](files/module/item/mixins/damageUtilMixin.js.md) |
| module/scripts/damageInstance.js | 52 | [Описание](files/module/scripts/damageInstance.js.md) |
| module/actor/mixins/damageUtilMixin.js | 17 | [Описание](files/module/actor/mixins/damageUtilMixin.js.md) |
| templates/dialog/combat/variableDamage.hbs | 6 | [Описание](files/templates/dialog/combat/variableDamage.hbs.md) |
| templates/chat/damage/damageToLocation.hbs | 40 | [Описание](files/templates/chat/damage/damageToLocation.hbs.md) |
| templates/chat/damage/damageToAllLocations.hbs | 15 | [Описание](files/templates/chat/damage/damageToAllLocations.hbs.md) |
| templates/chat/damage/shieldAbsorbs.hbs | 5 | [Описание](files/templates/chat/damage/shieldAbsorbs.hbs.md) |
| templates/chat/damage/spAbsorbs.hbs | 3 | [Описание](files/templates/chat/damage/spAbsorbs.hbs.md) |

Покрытие 322→331 из 621, остаток 290. В пятой серии 21 из 77 проверены,56 в очереди;234 требуют последующей детализации. TASK-0003 остаётся in-progress; TASK-0004/0005 — draft; следующая .045.

### Методика и пределы

Исходники читались целиком с nl/cat; определения, callers, Object.assign, схемы, шаблоны, styles и локализации проверялись rg/rg --files. Соседи прочитаны в пределах связей, их полные карточки не засчитаны повторно. Использованы существующие файлы Foundry14.367.0 в /opt/foundryvtt, Node24.16.0. Запуск: node --input-type=module через quoted stdin heredoc; код проверок существовал только в памяти инструмента, стенд/файлы тестов не создавались.

Настоящие импорты: DamageInstance, DamageProperties, DamageMessageData, AttackMessageData, CriticalWoundData, ArmorData, armorMixin, Actor damageUtilMixin, ChatMessageData; исходные полные объекты Actor.damageMixin и Item.damageUtilMixin загружены vm с подменой импортированных документов/эффектов. Тела static location/getList/addItem извлечены без изменения арифметики. Foundry DataModel/fields, Roll/evaluate (цифровые кубы minimize), ActiveEffectTypeDataModel, BaseActiveEffect.migrateData, Handlebars и parse5 настоящие. @common разрешён к локальному ядру. CONFIG.WITCHER из исходника. Переводы проверены штатным expandObject и getProperty.

Actor/Item-владельцы, game/ui/settings, окно DialogV2, UUID/Compendium.index, callbacks эффектов, ChatMessage/toMessage/setFlag и update/create — фасады. Для обычной арифметики update применяет переданные поля к минимальному объекту; для проверки ожидания возвращает управляемый pending Promise. В тестах схемы payload vm сначала сериализуется в JSON, как plain data, чтобы не спутать cross-realm объект с отказом Foundry. Исходники не исправлялись. Первоначальные ошибки адаптера (cross-realm object, тестовый ID bleeding вместо штатного bleed, перекрытое имя фабрики item и короткий тестовый UUID для валидации AttackMessageData) устранены только в коде проверки; итоговый запуск ниже завершился exit0.

Итог: **40 групп проверок прошли**. Это проверка текущего поведения, включая ожидаемые исключения, а не утверждение исправности функций.

### Проверенные сценарии

| Группа | Фактический результат |
| --- | --- |
| 01 | createBaseDamageObject сохраняет identity properties/item/defenseOptions; addEffects виден следующему prepared-чтению, source неизменен; без parent исключение. |
| 02 | Все 10 определений DamageInstance: defaults, цепочка setters, строки 7[src]/5[src]/15[src]/7[src]/7[src]; null-стадия выводится как null. |
| 03 | Настоящий Roll:4→4,2+3→5,2d6+1 при minimize→3,strong4→8, пустая строка→0 с одним уведомлением. |
| 04 | Диалог получает currentDamage1d6; newDamage2+3→5. Отмена, '???' и отсутствующая location отклоняют выполнение до нового сообщения. |
| 05 | Настоящая DamageProperties: bleed30+20→50; фиксированный 50 проходит,51 нет; poison0 получает applied=false при очистке сообщения; source не меняется. Неизвестный ID вызывает чтение img у undefined. |
| 06 | rollDamage ждёт toMessage, но не setFlag. После очистки DamageMessageData duration7 исчез, в запросе flag остаётся; critEffectModifier6 внутри damage.crit сохранён. |
| 07 | parse5 разобрал исходный flavor: div.damage-message имеет атрибут '<h1'; отдельный h1 не создан. Имя с HTML остаётся в сыром flavor; sanitization не проверена. |
| 08 | Общий shield 5: входы 3/5/8/[3,4] дают damage[0]/[0]/[3]/[0,2]. Сообщение только в первом случае, где остался щит. |
| 09 | bypassesShield=true,damage 3,shield 5→shield 2,HP 100. Обход не отключает handleShield. |
| 10 | Отрицательный damage−3 увеличивает shield 5→8. updateDerivedStat105.9 снижает HP 100→−5; damage−3 увеличивает STA 30→33. Эти последние границы записаны без оценки правил. |
| 11 | Два await handleShield3 при held updates из shield 5 отправляют 2 и 2, оба поглощают 3. Контекст сообщения читает прежний 5. |
| 12 | Одно попадание 10 в голову, SP 2→24; HP 100→76 и STA 30→6. SP-отбор в этой группе задан фасадом. |
| 13 | При damage 10/SP 20/HP 100 внешний applyDamage всё равно вызывает status bleed и Item applyOnDamage с duration7. Сами эффекты перехвачены. |
| 14 | Полное поглощение shield 20 при damage 10 прекращает внешний applyDamage до добавления масла и обоих видов эффектов. |
| 15 | Масло совпавшей категории добавляет 5 после щита: damage 10/shield 2→[8,5],HP 87. |
| 16 | Строковые temporaryHp3 и attackModifier5 одного эффекта поглощают 6, чужой бонус становится 2,HP 100. Два отдельные источника 3+4 и damage 10 оставляют HP 97. |
| 17 | Некорректный JSON временных HP прекращает HP-путь до записи; STA не читает эти изменения и уменьшается 30→27. |
| 18 | SP 10 расходуется один раз на экземпляры 6+8→0+4; серебряные 4 по обычной цели→2. AlwaysSP вызван и при полном блоке; normalSP только в положительной ветке. |
| 19 | allLocations без SP:16→общий остаток 3, шесть ссылок results на один массив, total18,HP 82; damage.location после цикла leftLeg. |
| 20 | allLocations со SP 5 и входом 10: общий массив обнуляется до продолжений, все шесть результатов blocked, total0. |
| 21 | silverTrait присваивает строку setType, сохраняя type=slashing; при сопротивлении несеребру итог 5 из 10. Это не ожидаемая правильная серебряная формула. |
| 22 | Настройка silverTrait=false, silverDamage2d6 и minimize: обычный удар→[10,2], strong→[10,4]. Наличие silverDamage не даёт основной порции пройти ветку half за несеребро. |
| 23 | flat−3/0/+3 дают[10]/[10]/[10,3]. Положительный flat при resistNonSilver вызывает TypeError likeSilver из-за null-типа. |
| 24 | multiplication3 без сопротивления брони не используется; nonMeteorite+vulnerable превращают 9→4→8. applyAP=true со штатным properties вызывает TypeError, AP-флаг обходит helper. |
| 25 | Контекст одиночного HBS теряет damageProperties; блоки IAP/ablating/crushingForce скрыты. Общий partial не получает готовые тексты стадий. spAbsorbs выводит 5[S] и 8. |
| 26 | Критический и бонусный урон передают 8/4, torso,hp, обход обеих броней,type=null; оба метода возвращаются при pending applyDamage. |
| 27 | Отбор none/torso/simple: critEffect5→greater; d6=1+modifier0→lesser; +modifier6→greater; единственный кандидат выбирается без случайности. |
| 28 | Отсутствующий pack→index; пустой список→uuid; resolve=null передаётся в addItem, затем name-ошибка. addItem в null-сценарии перехвачен отдельно. |
| 29 | Общий addItem при повторе name/type травмы отправляет quantity=NaN; treatment=stabilized,daysHealed3 остаются, create не вызывается. |
| 30 | Actor helper и CriticalWoundData: BODY 5→3/7/10;BODY 20→1/1/1. Для deadly/unknown Actor возвращает undefined, модель сохраняет 99. |
| 31 | Настоящие ActiveEffectTypeDataModel/WitcherActiveEffectData: changes располагается в system, type=add,phase=initial; value допускает строковый JSON. |
| 32 | Настоящий expandObject локализаций en/ru: все 14 литеральных ключей пяти HBS найдены; WITCHER.Item.properties.variableDamage из JS отсутствует в обеих. |
| 33 | Прямой applyDamage с TypedObject effects падает на filter после HP 100→97. Обычная DamageMessageData имеет Array; этот прямой сценарий не объявлен штатным UI-маршрутом. |
| 34 | Настоящая ArmorData Light SP 5: allLocations10 оставляет HP 100; отдельные свежие расчёты дают 15/5/2/2/2/2. SP-записи перехвачены. |
| 35 | Настоящий BaseActiveEffect.migrateData переводит корневой changes и JSON value в system.changes с object value; updateDerivedStat2 затем отклоняется на JSON.parse до HP. |
| 36 | Два lesser-кандидата при запросе greater вызывают uuid-ошибку. Single location завершается при pending ChatMessage.create, allLocations ожидает create. |
| 37 | Полный applyCritWound→addItem: первый вызов передаёт копию с quantity 1 и создаёт сообщение при pending Item.create; повторный совпавший Item отправляет quantity=NaN. |
| 38 | Граница rollOnlyDmg: toObject(false) убирает getPreprocessedEffects; настоящий consumer отклоняется. Настоящая AttackMessageData восстанавливает модель и даёт Roll4. Полный weaponAttack/диалог не исполнялся. |
| 39 | strong silverDamage1d6+1 с minimize: native1d6+1*2→3; контроль (1d6+1)*2→4. Простая формула из 22 работала иначе по структуре. |
| 40 | Полный applyDamage с oil и resistNonSilver отклоняется на likeSilver до HP. Настоящая CriticalWoundData убирает незаявленный quantity 1 из prepared/source. |

### Перекрёстная сверка

| Связь | Проверка и вывод |
| --- | --- |
| Item → properties → attack/damage message | createBaseDamageObject передаёт prepared ссылку; preprocessing копирует записи; DMD меняет контейнер effects на Array. Сырой flag не исправляет duration в system. |
| DamageInstance → Actor → armor | Стадии пишутся напрямую; один totalSP расходуется между экземплярами. Сравнены raw result и его HBS-адаптеры. Полный allLocations проверен с настоящей ArmorData. |
| applyOnHit / applyOnDamage | Флаги объявлены раздельно; после blockedBySp внешний метод всё равно вызывает applyOnDamage. Подтвержден вызов, не применение эффекта в мире. |
| Временные HP → ядро 14 → расход | system.changes — правильный путь; миграция строки value в объект создаёт несовпадение с JSON.parse consumer. Строковой тест 23 не доказывает расход мигрированного эффекта. |
| Crit → индекс → Item | Не RollTable: ready заранее загружает четыре поля индекса; applyCritWound выбирает/разрешает запись. Общий addItem пытается складывать quantity даже у травмы. |
| Лечение травмы | Расчёт срока в Actor и в модели — разные определения, не взаимные вызовы. none/stabilized/treated/followUp не изменяются методом получения. |
| HBS / локализация / HTML | Все поля пяти шаблонов сопоставлены с контекстами; partial зарегистрирован preload.14 HBS-ключей en/ru существуют; JS title ключ отсутствует; начальный h1 flavor некорректен. |

Уточнены шесть прежних карточек: DamageProperties, DamageMessageData, CriticalWoundData, WitcherActiveEffectData, armorMixin, weaponAttackMixin. Дополнены десять прежних issues:00023/00025/00026/00027/00070/00073/00117/00184/00257/00262. Прежние 00032/00258/00280/00282/00283 сопоставлены по действующим определениям; исторические результаты не объявляются новыми тестами.

### Проблемы

Зарегистрированы 15 новых potential issues — всего 298, все по-прежнему potential:

| ID | Наблюдение |
| --- | --- |
| [issue-00284](../../issues/potential/issue-00284.md) | Обход щита проверяется после поглощения урона и расходования щита |
| [issue-00285](../../issues/potential/issue-00285.md) | Урон по всем локациям повторно изменяет один массив экземпляров |
| [issue-00286](../../issues/potential/issue-00286.md) | Дополнительный урон flat и oil не имеет записи типа для проверки сопротивлений |
| [issue-00287](../../issues/potential/issue-00287.md) | Контексты сообщений урона не соответствуют полям шаблона подробностей |
| [issue-00288](../../issues/potential/issue-00288.md) | Повторное получение одноимённой травмы попадает в изменение отсутствующего quantity |
| [issue-00289](../../issues/potential/issue-00289.md) | Выбор критической травмы не обрабатывает отсутствие подходящего Item |
| [issue-00290](../../issues/potential/issue-00290.md) | Полное поглощение бронёй не прекращает применение эффектов applyOnDamage |
| [issue-00291](../../issues/potential/issue-00291.md) | Отрицательный входящий урон увеличивает запас щита |
| [issue-00292](../../issues/potential/issue-00292.md) | Повторное поглощение щитом может использовать прежний незаписанный запас |
| [issue-00293](../../issues/potential/issue-00293.md) | Начальный HTML сообщения урона превращает h1 в атрибут div |
| [issue-00294](../../issues/potential/issue-00294.md) | Расход временных HP повторно разбирает объект value после миграции Foundry 14 |
| [issue-00295](../../issues/potential/issue-00295.md) | Неизвестный ID статусного воздействия прерывает бросок урона |
| [issue-00296](../../issues/potential/issue-00296.md) | Заголовок окна переменного урона запрашивает отсутствующий ключ перевода |
| [issue-00297](../../issues/potential/issue-00297.md) | Режим только урона передаёт сериализованные свойства без getPreprocessedEffects |
| [issue-00298](../../issues/potential/issue-00298.md) | Сильный удар умножает только последний член составного серебряного урона |

Не оформлялись как установленные нарушения правил: допустимость отрицательных HP, назначение отрицательного flat/multiplication, требуемый общий итог AoE, кратность сопротивлений, нулевой процент воздействия и контактные эффекты. Для 290 ожидание явно условно до решения пользователя. Прямой TypedObject-вход в applyDamage описан как отличный от найденного штатного маршрута. Новые наблюдения не дублируют прежние 25/26/27/73/184/257; ссылки добавлены к соответствующим карточкам.

### Итоговые проверки документов

Проверены точный состав 9 карточек/603 строки, наличие всех собственных методов и таблиц зависимостей/потребителей, соответствие путей исходникам. Реестр содержит 621 строку,331 «Проверено» и 290 «Не начат»; карточек 331. Пятьдесят подзадач сохраняют 376 уникальных назначенных файлов; .001–.044 done, .045–.050 planned; в очереди 56. Новых документов 24 (9 карточек+15 issues); изменяются только docs. Старые записи журнала сохранены.

Финальная сверка: 16 699 локальных ссылок/якорей — без ошибок; 107 новых таблиц имеют заголовки, разделители и согласованное число столбцов. Все 27 собственных определений JS найдены в карточках; девять путей и 603 строки совпадают с задачей. git diff --check завершился exit0. Изменены 27 существующих документов и созданы 24; вне docs изменений нет. У всех 1366 файлов исходного tracked-набора сохранены mode, uid, gid и inode. Агрегат 621 исходника остался прежним; исторические записи журнала сохранены побайтово.

Мир/браузер/серверная запись, HTTP-доступ ресурсов и несколько клиентов не запускались. Реальные компедиумы, права службы и соответствие рулбукам не исследовались. Исходники, игровые данные и настройки не менялись; коммит агентом не создавался.

## TASK-0003.043

| Поле | Результат |
| --- | --- |
| Дата / ветка | 2026-09-12 / rusbar-main |
| Коммит | 929ac4c6d90509ce06ef0795be380925e8b59e69; рабочее дерево на старте чистое |
| Состав | armorMixin.js — 285 строк; locationMixin.js — 11; armor-sheet.css — 24; всего 3 файла / 320 логических строк |
| Покрытие | 322 из 621; 299 не разобраны. В пятой серии 12 из 77 выполнены, 65 в очереди; 234 вне очереди |
| Проверки | 31 группа изолированного запуска; все итоговые assertions выполнены |
| Связанные документы | Четыре прежние карточки и шесть прежних issues уточнены; семь новых potential issues 00277–00283 |
| Границы изменений | Только docs; исходники, игровые данные и права не менялись; коммит не создавался |

### Состав и перекрёстные связи

[Задача](../../tasks/task-0003.043.md). Полные карточки: [armorMixin.js](files/module/actor/mixins/armorMixin.js.md), [locationMixin.js](files/module/actor/mixins/locationMixin.js.md), [armor-sheet.css](files/styles/armor-sheet.css.md).

Прочитаны 11 методов armorMixin, два wrapper locationMixin, все шесть селекторов и восемь CSS declarations. Сопоставлены ArmorData/SpData/ResistanceData, поля MonsterData и DamageProperties, DamageInstance, getList/static locations/calculateStat Actor, getMultiDamageMod и calculateDamageWithLocation; пути EV в castSpell/rollSkillCheck. Для CSS сверены manifest/imports, более поздний .effect-list и текущий/старый HBS. Прямое поле spDamage проверено до producer generalCombatHook и combatEffectsData.

Прежние карточки ArmorData, SpData, ResistanceData и armor-sheet.hbs прочитаны вместе с поздними уточнениями и дополнены обратными связями. Соседи вне состава порции не получили полного покрытия. В частности, damageMixin, damageUtilMixin и DamageInstance остаются в очереди своего полного разбора; исполнение отдельных методов не заменяет его.

### Методика и фиксированные входы

Команда одноразового запуска: node --no-warnings --input-type=module, код через stdin. Node v24.16.0; Foundry 14.367.0 по /opt/foundryvtt/package.json. Постоянных тестовых файлов, установки зависимостей, сборки и игрового мира не создавалось.

Использованы настоящие common DataModel/TypeDataModel/fields/primitives Foundry, ArmorData, MonsterData, DamageProperties, SpData/ResistanceData внутри ArmorData, DamageInstance, CONFIG.WITCHER и импортированные armorMixin/damageUtilMixin. Parent Item — подкласс DataModel с пустой схемой и TYPES=[], полями type/id/actor и перехваченным update. Родитель удовлетворяет контракту модели, но не является Foundry Item Document. У персонажа Actor.system — минимальный объект; у монстра — настоящая MonsterData.

SP готовились настоящими base/derived каждой вложенной модели; enhancementItems задан в памяти как объект с system.stopping. Полный ArmorData lifecycle/поиск улучшений по Actor.items не выполнялся. Типичная броня: equipped=true, location=FullCover, current=max=заданному SP всех шести зон, иначе указаны изменения.

Точные тела getList, двух static Actor, calculateStat, calculateDamageWithLocation и applyDamageToAllLocations извлечены из исходников в vm. locationMixin исполнен с заменой импортированного класса классом с исходными static. Метод расчёта каждой зоны в группе 26 заменён фасадом: проверяются имена и прохождение consumer, а не полный общий урон. Группа 31 исполняет только исходный участок построения формулы EV castSpell.

Настоящие Roll/parser/terms и peggy-грамматика из Foundry работают в памяти; evaluate получает minimize либо maximize. Для случайной локации getRandomInt фиксирован на 10. Это не проверка распределения RNG. Actor/Item.update возвращают незавершённые Promise и регистрируют аргументы; никакая запись в БД не исполнялась.

PostCSS разобрал CSS; Handlebars и parse5 — HBS. Helpers localize/eq/or/checked/selectOptions и header/diagram partial заменены фасадами; значения модели переданы HBS собственными полями отдельного объекта. Браузер, полный рендер листа, штатные localize/expandObject/fallback, computedStyle и HTTP не запускались.

Первые запуски одноразового кода обнаружили ошибки его сборки (лишняя скобка, отсутствующий TYPES у тестового parent), затем предупреждение Handlebars о доступе к prototype getter. Исправлены только фасады/вход HBS. Эти результаты не зарегистрированы как ошибки системы; итоговый запуск 31 группы завершился с кодом 0.

### Результаты групп

| № | Сценарий | Наблюдение |
| --- | --- | --- |
| 01 | пустая броня и локации | Все шесть пустых локаций: totalSP=0, displaySP='0'; EV=0. |
| 02 | EV и исключение хранения | EV надетых Light=2 и stored Medium=3 равен 5, SP берёт только Light=10; игнорирование 8 ограничивает EV нулём. |
| 03 | отбор по modifiedMax вместо имени локации | location='Head' с head.max=0/torso.max=10 даёт head SP=0, torso SP=3. |
| 04 | щит и надёжность отделены от SP | Щит reliability=20 сам не даёт SP; EV=2 учитывается. Добавленное torso SP=5 участвует в расчёте. |
| 05 | слои и естественная броня предметом | Light=10+Medium=15+Heavy=20+Natural=3 дают SP=33; текст содержит два бонуса слоёв. |
| 06 | пороги бонуса разницы | Разницы 0/5/6/9/10/15/16/20/21 дают 5/5/4/4/3/3/2/2/0; обратная разница и неположительные SP проверены. |
| 07 | повреждённый тяжёлый слой снижает SP | Light=10+повреждённый Heavy=1 дают SP=5; снятие Heavy возвращает SP=10. |
| 08 | повтор класса и выбор последнего Natural | Два Light: предупреждение, затем TypeError. Два Natural с SP=9/3: последний по sort даёт SP=3. |
| 09 | монстр и независимые bypass flags | Поля монстра по семи зонам с предметами дают 15/17/17/17/19/19/8; флаги обхода в torso — 17/7/10/0. |
| 10 | AP сохраняет числовой расчёт SP в примеси | В getLocationArmor обычная/AP/improvedAP атаки получают одинаковый SP=10. |
| 11 | сопротивление изменяет тот же экземпляр | slashing=21 → 10 при сопротивлении двух носимых слоёв; изменён тот же экземпляр, afterResistance ещё null. |
| 12 | multiplier кратность и applyAP | multiplication=3: 20/30/45 без/с одним/двумя сопротивлениями; applyAP вызывает TypeError, AP/IAP обходят helper. |
| 13 | Natural читает тип общей атаки | При основном slashing порция silver=20 не меняется носимым сопротивлением slashing, но Natural уменьшает её до 10. |
| 14 | bypass и сопротивление с нулевым SP | Броня current=0/max=10 сохраняет сопротивление: урон 20 → 10; bypassWorn/AP оставляют 20. |
| 15 | износ меньше равен больше SP через Actor | SP=3, прямой износ 2/3/4 → запрос 1/0/отсутствие запроса. |
| 16 | улучшение и исходный SP | База 1+улучшение 2, износ 2 → запрос stoppingPower=-1; _source остаётся 1. |
| 17 | ablating и crushing реальный Roll | Обычный/удвоенный/ablation min/max/max×crushing износ: 1/2/1/4/8 на настоящем Roll. |
| 18 | bypassWorn прекращает обычный износ монстра | bypassWorn у монстра останавливает обычный износ; без флага armorUpper5 → запрос 4. |
| 19 | постоянный износ игнорирует worn bypass | Прямой spDamage2 при bypassWorn и crushing запрашивает Item10→8 и Monster5→3; не удваивается; Natural Item пропущен. |
| 20 | локации монстра и ограничение нулём | Семь зон адресуют четыре правильных поля монстра с ограничением 0; bypassNatural и type=character не пишут. |
| 21 | два запроса используют прежний SP | Износ 2, затем 1: pending Item/Actor.update запросили 8/8, затем 9/9 при прежних 10. |
| 22 | consumer блок и пробитие | Настоящий calculateDamageWithLocation: урон 10/SP=10 блокирован, износ 0; урон 20/SP=10 оставил 10, обычный износ 1. Нулевой прямой износ также вызвал update. |
| 23 | improvedAP NaN только в отображении | Heavy=20+Light=10: SP=23, IAP →12, урон 30 →afterSp=18; displaySP=NaN. |
| 24 | getAllLocations теряет this но объект хвоста доступен | Monster hasTailWing=true: wrapper=6, static.call(actor)7; false→6; отдельный объект хвоста доступен. |
| 25 | все объекты локаций и random | Проверены семь пар formula/modifier; random d10=10 →leftLeg/tailWing; неизвестное name сохраняется и ломает последующий расчёт брони. |
| 26 | потребитель списка локаций | Настоящий applyDamageToAllLocations с подменённым расчётом зон передал шесть имён, сумма 6; хвост не включён. |
| 27 | EV и prepared REF DEX | calculateStat с базами 8, EV=2 и подменённым штрафом массы 1 дал REF=4/DEX=4/SPD=7. |
| 28 | CSS declarations и подключение | PostCSS: шесть селекторов, восемь declarations; armor-sheet импортирован раньше activeEffect. |
| 29 | CSS потребители и HBS условия | Настоящие Handlebars/parse5 с фасадами helpers/partials: .location-table есть у FullCover, отсутствует у Shield. |
| 30 | все сочетания носимых слоёв | Все восемь наборов Light=4/Medium=8/Heavy=12: 0/4/8/13/12/16/17/22; Natural=3 прибавляет 3 к каждому. |
| 31 | EV в исходном участке формулы сотворения | Исходный участок castSpell: EV=2/ignoredEv=4 → 'BASE -2 +4'; без надетой брони → 'BASE'. |

### Проблемы и сопоставление с прежним массивом

Уточнены [25](../../issues/potential/issue-00025.md) (applyAP), [26](../../issues/potential/issue-00026.md) (кратность multiplication), [32](../../issues/potential/issue-00032.md) (список локаций и consumer), [35](../../issues/potential/issue-00035.md) (перегруз отдельно от EV), [83](../../issues/potential/issue-00083.md) (превышение SP) и [254](../../issues/potential/issue-00254.md) (вклад EV в сотворение). Учтены поздние уточнения и [общая промежуточная сверка](cross-check-0001.md). Дубль 00200/00029 и прежние статусы не менялись.

- [issue-00277](../../issues/potential/issue-00277.md) — Броня на хранении учитывается в штрафе EV.
- [issue-00278](../../issues/potential/issue-00278.md) — Повторный класс надетой брони вызывает исключение после предупреждения.
- [issue-00279](../../issues/potential/issue-00279.md) — Добавление повреждённого тяжёлого слоя уменьшает суммарный SP.
- [issue-00280](../../issues/potential/issue-00280.md) — Сопротивление Natural использует общий тип атаки вместо типа порции урона.
- [issue-00281](../../issues/potential/issue-00281.md) — Обход носимой брони прекращает обычный износ естественной брони монстра.
- [issue-00282](../../issues/potential/issue-00282.md) — Последовательные запросы износа SP используют прежнее значение.
- [issue-00283](../../issues/potential/issue-00283.md) — Улучшенная бронебойность превращает пояснение составного SP в NaN.

Всего 283 issues, все potential. Регистрация разрешена пунктом 9 TASK-0003; подтверждение пользователем, исправление и закрытие не выполнялись. Сопротивления при SP=0, выбор последнего Natural, отсутствие износа Natural Item и отрицательные исходные SP описаны отдельно от подтверждённого правила игры; самостоятельные issues по этим неоднозначным ожиданиям не создавались.

### Формальная сверка и пределы

Реестр 621 файлов сопоставлен с 322 карточками и 299 строками «Не начат». Перечни всех 50 подзадач содержат 376 уникальных исходников; .001–.043 done, .044–.050 planned. В очереди 65, ещё 234 вне неё. TASK-0003 in-progress, TASK-0004/TASK-0005 draft.

Ссылки, якоря, новые Markdown-таблицы и git diff --check проверены. Изменения ограничены docs. Все 621 исходник совпадают со срезом TASK-0001 15da5b225535e34af4e132c701b5353ef4eb667f. Совокупный SHA256 (сортированные пути UTF-8 + NUL + байты) — 52701d3d0a5f054319886ac2a9d45b42c26c80098858d02518579c6a1edfaec4. mode/uid/gid/inode всех 1356 ранее отслеживаемых файлов сохранены; прежний журнал ниже не изменён.

Не проверены настоящий Actor lifecycle, мир, HP/БД, межклиентский порядок записей, ActiveEffect поверх SP, полный урон по всем локациям, фактический чат и соответствие чисел рулбуку. Статус карточки «Проверено» означает пофайловый анализ с указанными пределами.

## TASK-0003.042

| Поле | Результат |
| --- | --- |
| Дата / ветка | 2026-09-12 / rusbar-main |
| Коммит | 16695cbfc7fec3e0de56660c7cab21bc0304e94b; рабочее дерево на старте чистое |
| Состав | defenseMixin.js — 457, defenseOptionMixin.js — 9, defense.hbs — 2, defenseCrit.hbs — 6, defenseStun.hbs — 3: 5 файлов / 477 логических строк |
| Покрытие | 319 из 621; 302 не разобраны; в пятой серии 9 из 77 выполнены, 68 в очереди; 234 вне очереди |
| Проверки | 33 группы изолированного запуска; итоговые assertions выполнены |
| Связанные документы | 21 прежняя карточка и 10 прежних issues уточнены; 9 новых potential issues 00268–00276 |
| Сохранность | Только docs; 621 исходник и mode/uid/gid/inode всех 1342 ранее отслеживаемых файлов сохранены; коммит не создавался |

### Состав и перекрёстные связи

[Задача](../../tasks/task-0003.042.md). Полные карточки: [defenseMixin.js](files/module/actor/mixins/defenseMixin.js.md), [defenseOptionMixin.js](files/module/item/mixins/defenseOptionMixin.js.md), [defense.hbs](files/templates/chat/combat/defense/defense.hbs.md), [defenseCrit.hbs](files/templates/chat/combat/defense/defenseCrit.hbs.md), [defenseStun.hbs](files/templates/chat/combat/defense/defenseStun.hbs.md).

Полностью прочитаны все пять файлов: 11 методов Actor, один Item wrapper, callbacks обоих окон, все три шаблона. В качестве связанных определений проверены Actor/Item prototype, модели Weapon/Armor/Profession/DefenseProperties, skillDefense/lifepath, CONFIG/settings, RollConfig/extendedRoll, сообщения, helper/queries и точки применения эффектов. Обратные связи внесены в 21 прежнюю карточку. Файлы combat.js, damageMixin.js, adrenalineMixin.js и styles/chat.css проверены только до нужных определений/селекторов; полного покрытия им не присвоено.

Особенно сопоставлены: дополнительная модельная защита против штатного выбора щита; одинаковый addDefenseModifiers в двух примесях и порядок Object.assign; полный raw crit против HTML-контекста и schema сообщения; getInteractActor при клике против defender UUID; совпадение action с именем и свёртка кнопок ядром.

### Методика и фиксированные входы

Одноразовый Node v24.16.0 через node --no-warnings --input-type=module, код в stdin. Постоянный стенд/тестовые файлы, установка пакетов, сборка и игровой мир не создавались. Foundry 14.367.0 установлен по /opt/foundryvtt/package.json.

Настоящие common DataModel/TypeDataModel/fields/primitives и модели WeaponData, ArmorData, ProfessionData, DamageProperties, AttackMessageData, DefenseMessageData. CONFIG.WITCHER, RollConfig, ChatMessageData/append и modifierMixin импортированы из системы. defenseMixin исполнялся исходным текстом в vm с заменой только импортируемых зависимостей/экспорта. DefenseOptionMixin импортирован как есть. getList/static getLocationObject/getActorOwner/applyCritWound и callback кнопок чата извлечены с неизменными телами.

Настоящий Handlebars рендерил три HBS, parse5 разбирал HTML. localize возвращал ключ; настоящие expandObject/fallback не прогонялись. Окна wait/prompt и form.elements/selectedOptions были фасадами. Для конфликта action выполнен исходный DialogV2._initializeApplicationOptions из /opt/foundryvtt/client/applications/api/dialog.mjs; super и cleanHTML заменены фасадами. Поэтому доказана свёртка buttons, но не браузерная очистка и отрисовка окна.

Настоящий Roll/parser/terms и грамматика grammar.pegjs (peggy в памяти) разбирали построенные строки. Roll.evaluate принудительно получал minimize; для боковой локации getRandomInt=1 либо 2. Большинство исходов extendedRoll задавались на границе функции: total=15, чтобы раздельно проверить ветви примеси. Эти исходы не выдаются за вычисленный настоящим helper бросок. Группа 19 использовала настоящий extendedRoll и проверила options.success: 10[Stun] против 10 успешно; d10=1 при пороге stunSave=1 провален. toMessage во всех случаях — фасад без документа/БД.

Actor fixture: REF=5/DEX=6/WILL=7, dodge=3, swordsmanship=4, brawling=2, melee=1, athletics=4, resistmagic=5; STA=10, stun=7, shieldParryBonus=2, shieldParryThrownBonus=3; пустые statuses/effects/combatEffects. Damage: torso, originalLocation torso, critLocationModifier=0, critEffectModifier=6, действительные по формату фиктивные UUID, настоящая DamageProperties. Обычный defenseOptions=['dodge'], totalAttack=15; выбор первого пункта, extra=false, custom='0'. Отклонения перечислены в группах/карточках.

Actor/Item документы, User/GM, UUID lookup, update/query/applyStatus/removeStatus и helper эффектов — фасады с журналом аргументов и pending Promise. Базовый статус full:false не проверяет свойства настоящего Roll.options: они проверены отдельно в группе 19. Каталог травм в группе 32 содержит две фиксированные torso/complex записи; fromUuid/addItem/ChatMessage.create заменены границами. Проверена функция выбора травмы, а не создание игрового документа.

### Результаты групп

| № | Сценарий | Наблюдение |
| --- | --- | --- |
| 01 | штатные варианты | dodge: 1d10+5+3; reposition: 1d10+6+4; magicResist: 1d10+7+5. |
| 02 | block/parry/parryThrown с предметом | block: 1d10+5+4 и запрос износа; parry: 1d10+5+4−3 и staggered; parryThrown: 1d10+5+4−5, без этих реакций. |
| 03 | парирующее оружие и модификаторы | Отрицательный штраф parry компенсирован, custom−2 принимается; положительный modifier=2 добавлен |
| 04 | weapon/profession/armor sources | Доступны dodge, оружие Blade и навык профессии Guard с isDefense=false. ArmorData дополнительный вариант не дала. |
| 05 | definingSkill не включён | Только dodge |
| 06 | профессиональный skillOverride | Формула 1d10+5+4+1; defense остаётся undefined; thresholdDesc='Guard'. |
| 07 | одинаковые имена кнопок ядро | 3 исходные кнопки → 2 после настоящего initializer; Same использует последний modifier=4 |
| 08 | crushingForce отбор | Из исходных dodge/parry/parryThrown остались dodge и parryThrown. |
| 09 | пустые/неизвестные options и пустой chooser | Пустой список, неизвестный option и parryThrown без предмета завершились исключениями до броска. |
| 10 | отмена обоих окон | Оба отказа до расхода |
| 11 | пустой/неизвестный skill оружия | Отказ в CONFIG.skillMap[skill].label при создании chooser |
| 12 | stored предметы | Stored weapon — отдельная кнопка; stored shield — штатный parryThrown |
| 13 | износ при block, crushing и равенстве | При начальной надёжности 3: обычный block запрашивает 2, crushingForce — 1; проверены weapon.reliable и armor.reliability. |
| 14 | block голыми руками | Чат защиты создан, затем item.type на undefined |
| 15 | shield lifepath case и знак | parry добавляет +2; штатный parryThrown не добавляет +3; контроль с parrythrown добавляет +3. |
| 16 | extraDefense STA и поздний отказ | 0 отказ; 1→0; 10→9; пустой chooser parryThrown запрашивает STA=9 до TypeError |
| 17 | положительный defenseModifier и AE | AE+2/penalty−2 допустимы; положительный+2 без оператора → ошибка Roll |
| 18 | stun фиксация и resistmagic | dodge фиксирован 10; resistmagic сохраняет бросок |
| 19 | реальное равенство defense и stunSave | Защита 10 против 10 успешна; stunSave d10=1 при пороге 1 провален: reversal strict < |
| 20 | пороги критов | Разности 0/6: null; 7/9: simple, урон 3/бонус 5; 10/12: complex, 5/10; 13/14: difficult, 8/15; 15/20: deadly, 10/20. |
| 21 | критическая локация все интервалы | Итоги 2/4/6/9/11/12: leftLeg/leftArm/torso/torso/head/head; critEffect отсутствует для конечностей, затем 1/6/1/6. Правая сторона проверена отдельно. |
| 22 | крит полный путь, query и модель | Сырой crit: complex, torso, critdamage=5, bonusdamage=10, critEffectModifier=6. После DefenseMessageData последнее поле отсутствует. Зафиксированы query, applyOnHit и removeStatus. |
| 23 | нет владельца/GM и удалён Actor | Ошибка до toMessage при обоих отсутствиях; активный OWNER предпочтён GM |
| 24 | stun кнопка после успеха | При равенстве 15/15 кнопка stun=−2 остаётся; arms/tailWing без кнопки |
| 25 | applyOnHit, remove stun, stagger и ожидания | При попадании applyOnHit/removeStatus; при parry запрос staggered с duration=1. Promise дочерних операций остаются pending |
| 26 | stunSave ± и успех/провал | Порог 5/7/9; на провале applyStatus не ожидается; успех сам не снимает stun |
| 27 | HBS ветви и экранирование | Условные crit-stun/stun; пустые ветви пусты; текст экранируется |
| 28 | сырое имя chooser | Два исходных пункта brawling и swordsmanship превратились в три: HTML имени добавил fake без Item ID. |
| 29 | сообщение/износ при сломанном предмете | Запрошен reliable−1; broken notification; фильтра неисправного предмета нет |
| 30 | контекстные функции чата | Обычная кнопка читает attackWeaponProperties.stun, crit-stun вызывает без аргумента; event.target не используется |
| 31 | duration граница attack → защита | Raw duration=4 очищен настоящей AttackMessageData; applyOnHit получает undefined, UUID сохраняется |
| 32 | critEffectModifier и consumer травмы | При getRandomInt=1 сырой crit с модификатором +6 выбрал greater; тот же crit после очистки модели — lesser. |
| 33 | подготовленная локация исходного сообщения | Критическая защита меняет prepared attack.damage.location torso→leftLeg; _source остаётся torso; DB не записывается |

Группа 31 проверяет именно верхний damage.duration: после AttackMessageData он отсутствует; прежняя .041 дополнительно проверяла вложенный effects.duration. Группа 33 отделяет изменение prepared location от _source и БД. Последствия повторной защиты по тому же сообщению не воспроизведены и не зарегистрированы как отдельная доказанная ошибка.

### Проблемы и сопоставление с прежним массивом

Дополнены десять прежних issues: 31 (только связь вызова applyStatus, без повторного воспроизведения иммунитетов),33 (реальное определение defense modifier),71/72 (полный отбор профессии),79 (ошибка chooser),85 (отличие дополнительной защиты брони от штатного Shield),182 (граница отправителя, fumble-handler не повторён),185 (отсутствующий получатель),257 (duration),258 (critEffectModifier и выбор травмы). Прежние уточнения из общей промежуточной сверки учтены; дубль 00200/00029 и статусы оставлены прежними.

- [issue-00268](../../issues/potential/issue-00268.md) — Совпадающие названия вариантов защиты объединяются в одну кнопку.
- [issue-00269](../../issues/potential/issue-00269.md) — Выбор защиты не обрабатывает отсутствие пригодного варианта.
- [issue-00270](../../issues/potential/issue-00270.md) — Успешный блок голыми руками обращается к отсутствующему предмету.
- [issue-00271](../../issues/potential/issue-00271.md) — Бонус парирования метательного оружия щитом не находит штатный action.
- [issue-00272](../../issues/potential/issue-00272.md) — Кнопка оглушения появляется после успешной защиты.
- [issue-00273](../../issues/potential/issue-00273.md) — Защита не ожидает завершения расходов, запросов и применения статусов.
- [issue-00274](../../issues/potential/issue-00274.md) — Защита предлагает предметы, помещённые на хранение.
- [issue-00275](../../issues/potential/issue-00275.md) — Имя предмета защиты вставляется в chooser как необработанный HTML.
- [issue-00276](../../issues/potential/issue-00276.md) — Дополнительная защита запрашивает STA до проверки выбранного навыка.

В реестре 276 issues, все potential. Регистрация разрешена пунктом 9 TASK-0003; подтверждение, исправление и закрытие не выполнялись. Где вывод требует подтверждения правил (условие оглушения, доступность stored и последствия блока навыком), это записано отдельно от наблюдаемой ошибки исполнения.

### Формальная сверка и пределы

Реестр 621 файлов сопоставлен с 319 карточками и 302 строками «Не начат». Все 50 перечней подзадач проверены: 376 уникальных назначенных исходников; .001–.042 done, .043–.050 planned; 68 файлов в очереди, 234 вне неё. TASK-0003 in-progress; TASK-0004/TASK-0005 draft. Названия задач и первоначальные объёмы серий сохранены.

Ссылки/якоря, новые Markdown-таблицы, реестр issues и git diff --check проверены. Изменения ограничены docs. Все 621 исходник совпадают с TASK-0001 15da5b225535e34af4e132c701b5353ef4eb667f. Совокупный SHA256 (сортированные пути UTF-8 + NUL + байты файла) — 52701d3d0a5f054319886ac2a9d45b42c26c80098858d02518579c6a1edfaec4. Метаданные доступа 1342 прежних файлов сохранены; прежнее содержимое журнала ниже не изменено.

Не проверены полный Actor lifecycle, браузер/DOM/CSS, штатная локализация, права и таймауты query, реальная запись/создание эффектов, распределение случайных бросков, полный расчёт брони/HP и соответствие всех чисел рулбуку. Статус карточки «Проверено» означает выполненный пофайловый анализ с указанными пределами.

## TASK-0003.041

| Поле | Результат |
| --- | --- |
| Дата / ветка | 2026-09-12 / rusbar-main |
| Коммит проверки | d5c7a4b871dce3aa55f4b8b589e62c3c9450f2d3; дерево на старте чистое |
| Полный состав | weaponAttackMixin.js382, weapon-attack.hbs270, weapon-roll.css19, attack-sheet.css16 — четыре файла / 687 логических строк |
| Версия источников | Все 621 файла совпадают с TASK-0001, 15da5b225535e34af4e132c701b5353ef4eb667f |
| Покрытие | 314 из 621;307 не разобраны; в пятой серии 4 из 77 выполнены,73 в очереди,234 вне очереди |
| Проверки поведения | 28 групп изолированного запуска; итоговые assertions выполнены |
| Связанные документы | Уточнены 19 прежних карточек и 14 прежних issues; новые potential issues 00259–00267 |
| Сохранность | Только docs; исходники, данные и метаданные доступа 1329 ранее отслеживаемых файлов сохранены; коммит не создавался |

### Состав, методы и границы

[Задача](../../tasks/task-0003.041.md). Полные карточки: [weaponAttackMixin.js](files/module/actor/mixins/weaponAttackMixin.js.md), [weapon-attack.hbs](files/templates/dialog/combat/weapon-attack.hbs.md), [weapon-roll.css](files/styles/weapon-roll.css.md), [attack-sheet.css](files/styles/attack-sheet.css.md). Все четыре файла прочитаны целиком; учтены пять методов, вложенные callbacks, 20 полей формы, восемь CSS-правил/13 declarations.

Проверены оба прямых потребителя weaponAttack (Actor.useItem и professionMixin), четыре helper, Item.getItemAttack/createBaseDamageObject, DamageProperties и расход, контекст/имена полей HBS, конфигурация, подключение CSS, schema сообщений и дальнейшие точки чтения. Соседние defenseMixin, Item.damageUtilMixin, scripts/combat/combat.js прочитаны до нужных методов, а не объявлены полностью разобранными.

### Методика и окружение

Node v24.16.0; Foundry 14.367.0 по /opt/foundryvtt/package.json. Одноразовый сценарий запускался через node --no-warnings --input-type=module с исходником в stdin; стенд, пакеты, постоянные тестовые файлы и игровой мир не создавались.

Настоящие common DataModel/TypeDataModel/fields/primitives из /opt/foundryvtt; ES-модули WeaponData, DamageProperties, AttackMessageData, DefenseMessageData, ChatMessageData, modifierMixin, CONFIG.WITCHER. weaponAttackMixin исполнен из исходного текста в vm: заменены только import-связи и экспорт для доступа к объекту. getItemAttack, createBaseDamageObject и static getLocationObject извлечены без изменения тел; они выполнялись на фасадах владельцев. Полный WitcherActor/WitcherItem lifecycle не запускался.

Настоящий Roll/parser/terms и грамматика /opt/foundryvtt/client/dice/grammar.pegjs (скомпилирована peggy в памяти) разбирали формулы; minimize давал фиксированные результаты. В большинстве групп extendedRoll был границей захвата, после которой отдельно проверялся Roll. Группа 26 исполнила настоящий extendedRoll с default RollConfig до подменённого toMessage; evaluate принудительно получал minimize. Это не проверка случайных бросков, реальной доставки, чат-рендера или БД.

Настоящий Handlebars и исходные системные eq/or обрабатывали HBS. Фасад localize возвращал ключ; selectOptions возвращал экранированные ключи/labels из config в исходном порядке. Штатный selectOptions v14 делегирует createSelectInput; его полный DOM-путь не исполнялся. parse5 разбирал HTML; form.elements восстановлен из input/select и дополнен фиксированным выбором. Исходный prompt callback читал этот фасад. Actor.system/коллекция items/UI/getSpeaker/update/rollDamage на границах были контролируемыми фасадами; update/rollDamage Promise оставлялись pending без записи. Для случайной локации getRandomInt возвращал 1.

Базовый вход: Actor REF5/DEX6, swordsmanship3/archery4, STA10, meleeBonus 2, critLocationModifier1/critEffectModifier2; WeaponData.damage2d6, quantity строка 1, melee/swordsmanship, slashing, torso/normal, ручные добавки 0. Группы ниже явно меняют эти значения. Базовые lifepath/combatEffects пусты — это свойство фикстуры, не доказательство defaults настоящего Actor.

Модельная граница проверялась на сериализуемом снимке: документные ссылки Item/ammunition представлены простыми объектами; UUID заменены на валидные фиктивные шестнадцатисимвольные ID. effects.duration добавлен вручную после WeaponData, которая сама этот ключ не объявляет. Очистка реальной моделью не равна сохранению сервером.

При подготовке сценария исправлены только входы/окружение проверки: ctrl/alt/shift вместо ctrlKey/altKey/shiftKey, передача plain object между realm, валидные UUID и пробел в inline CSS. Ошибки этих первых запусков не зарегистрированы как ошибки системы. Итоговый запуск содержит 28 успешных групп.

### Фактические сценарии

| Группа | Вход / действие | Результат |
| --- | --- | --- |
| 01 | Обычная melee: REF5, swordsmanship3, damage2d6, torso | Формула 1d10+5+3−1; урон 2d6; sender ACTOR, attacker/itemUuid присутствуют; critEffectModifier2. |
| 02 | accuracy и meleeBonus: −2/0/+2 | Знаки сохранены в атаке и уроне; ноль не дописывается. |
| 03 | Каждый из 12 checkbox отдельно | Получены −3/−3/+3/−3/−2/+4/−2/−3/+5/−5/−3/+2 согласно именам в карточке; real Roll minimize подтверждает суммы. |
| 04 | ranged/archery: DEX6, skill4; шесть дальностей | none/close без добавки; pointBlank+5, medium−2, long−4, extreme−6. |
| 05 | customAim/customAtt: −2/0/+2 | Aim−2 игнорируется; customAtt−2 даёт +-2, который настоящий Roll принимает. |
| 06 | fast; customDmg0/2/−2/1d6 | Всегда два вызова; ноль не накапливается, остальные повторно дописываются ко второй формуле: 2d6+2 → 2d6+2+2. |
| 07 | Все пять strike и девять location | fast2, остальные 1; strong/joint−3; head−6, torso−1, arms−3, legs−2, tailWing/random+0. Random принудительно 1, распределение не проверялось. |
| 08 | displayRollsDetails=true; accuracy2, melee2, aim1, customAtt−2, customDmg2, medium,strong,ambush | Формулы с ключами-подписями принимает real Roll; минимальная атака 9, минимальный урон 6 до dmgMulti. |
| 09 | Отмена, пустой skill, undefined weapon | Фасад закрытия отклоняет prompt до расходов; пустой skill → notification до окна; undefined weapon → TypeError до окна. |
| 10 | Extra: STA2/3/10; update-Promise остаётся pending | STA2 — отказ;3→запрос 0;10→запрос 7; атака завершается до update. |
| 11 | usingAmmo без isAmmo и с quantity 0/1 | noAmmo=1 не блокирует бросок;0→запрос−1;1→запрос 0. Сохранение не выполнялось. |
| 12 | fast и ammo/throwable quantity 2 | Два броска, один запрос quantity 1 до цикла в каждой ветке; игровые правила кратности не проверены. |
| 13 | Throwable ranged quantity 0 + extra + ammo1 | Сначала запросы STA7 и ammo0, затем return; бросков 0. Сочетание допускается моделью, игровое назначение не утверждается. |
| 14 | unknown skill / unknown strike + extra + ammo | В обеих ветках два запроса update, затем TypeError, без броска; отсутствие/неизвестность skill — разные условия. |
| 15 | rollOnlyDmg, fast, customDmg2; rollDamage-Promise pending | Два не ожидаемых вызова с одним объектом; его formula меняется с 2d6+2 на 2d6+2+2. |
| 16 | Настоящие DamageProperties: AP+AP, AP+IAP, IAP+AP, none+AP | Первые три возвращают +3d6; AP+AP уже имеет IAP. none+AP без добавки. Default defenseMultiplierCap5+5=10. Ожидаемое сочетание по правилам не установлено. |
| 17 | TypedObject effects при merge/ammo/enhancement | merge сохраняет только left.one; ammo.two и enhancement.three появляются в prepared properties, отсутствуют в _source. enhancementItems задан вручную, {},null пропущены. |
| 18 | Профессиональное замещение и обычный контроль с AE+2/attack−2 | replacement REF5/level4 →1d10+5+4−1; обычный REF5/skill3 →1d10+5+3 +2 −2[Penalty]−1. |
| 19 | Два режима оружия; options с профессиональными данными | skillReplacement оставляет attackOption undefined, а skill восстанавливает; ranged throwable не списывается. Только additionalDamageProperties → noAttackSkill. |
| 20 | Четыре attackOptions и {},shift,alt,ctrl | Индексы 0/1/2/3 соответственно. spell default='spellcasting', alias undefined; itemUse без настроенного skill — отдельный старый контракт. |
| 21 | lifepath.strong={value:2}; положительный attackModifier2 | Настоящий Roll отвергает [object Object] и строку положительного модификатора без оператора; старые 19/33. |
| 22 | Monster-фасад addMeleeBonus=false, WeaponData.applyMeleeBonus=true, bonus2 | context.meleeBonus 2, displayDmgFormula2d6, damage.formula2d6; расширяет 244. |
| 23 | Все 16 комбинаций четырёх типов, настоящий Handlebars и исходные eq/or | unavailable появляется ровно при piercing=false, в том числе рядом с slashing/bludgeoning/elemental. |
| 24 | Имя ammo содержит закрывающий option и новый option FAKE | После Handlebars и parse5 два пункта AMMO/FAKE вместо одного Item; browser sanitization/XSS не проверялись. |
| 25 | range/usingAmmo/isThrowable включены | 20 уникальных имён;9 location,5 strike,6 range; callback исходной функции читает восстановленные элементы. |
| 26 | Настоящий extendedRoll/Roll с minimize; toMessage — фасад | Сумма 8, fumble extra1, rollTotal7; одно attack-сообщение. Реальный критический случай 10/взрывной RNG здесь не тестировался. |
| 27 | Сериализуемый снимок производителя с валидными фиктивными UUID → реальные Attack/DefenseMessageData | В attack UUID и critEffectModifier2 сохраняются; item/ammunition и вручную добавленный effects.duration удалены. Defense отдельно удаляет critEffectModifier. |
| 28 | CSS-исходники, классы HTML и inline customDmg | По 4 правила CSS; width:auto/max-width50% на customDmg; word-wrap:break-all найден, невалидность сверена с W3C. ComputedStyle не проверялся. |

### Перекрёстная сверка и issues

Исходящие связи примеси сопоставлены с определениями в Actor/Item, моделях, helpers, CONFIG/settings и сообщениях; обратные ссылки добавлены в 19 прежних карточек. getItemAttack уже описывал возможность truthy сторонних options: теперь установлен штатный источник professionMixin, поэтому создана issue 00264 с конкретным маршрутом. Предыдущие предупреждения о частичном чтении других примесей не считаются анализом этих файлов.

Согласованы границы прежних issues:19/33 (формулы),32 (getAllLocations отдельно),64/66 (настройки оружия),69/70 (effects/prepared),182 (последующий fumble),237/238/242 (профессия),244 (оба preview),257/258 (очистка схемой). Эти 14 карточек дополнены. Issues61/65 проверены как уже описанные источники пустого/неизвестного skill, новой записи/повторного теста миграции нет. Дубль 00200/00029 из промежуточной сверки сохранён без смены статусов.

- [issue-00259](../../issues/potential/issue-00259.md) — Ручная добавка к урону накапливается между ударами одной быстрой атаки.
- [issue-00260](../../issues/potential/issue-00260.md) — Оружейная атака допускает отсутствующие и нулевые боеприпасы.
- [issue-00261](../../issues/potential/issue-00261.md) — Оружейная атака запрашивает расход до поздних отказов и ошибок.
- [issue-00262](../../issues/potential/issue-00262.md) — weaponAttack завершается до сохранения ресурсов и бросков rollOnlyDmg.
- [issue-00263](../../issues/potential/issue-00263.md) — Слияние бронебойности одновременно повышает уровень свойства и добавляет 3d6.
- [issue-00264](../../issues/potential/issue-00264.md) — Служебные options профессиональной атаки сбивают выбор режима оружия.
- [issue-00265](../../issues/potential/issue-00265.md) — Вариант unavailable в типе урона зависит только от piercing.
- [issue-00266](../../issues/potential/issue-00266.md) — Имя боеприпаса вставляется в select как необработанный HTML.
- [issue-00267](../../issues/potential/issue-00267.md) — В стилях таблиц атаки задано недопустимое значение word-wrap.

Все 267 issues остаются potential. Для 263 доказано фактическое сочетание AP/IAP, ожидаемая игровая таблица ещё требует подтверждения. Для 267 грамматика проверена по [W3C CSS Text Level3 §5.4](https://www.w3.org/TR/2026/CRD-css-text-3-20260814/#overflow-wrap-property); визуальный дефект не заявляется без браузера.

### Формальная проверка и пределы результата

Сверены 621 строка реестра,314 полных карточек,307 строк «Не начат», состав всех 50 подзадач, отсутствие пересечений и актуальные указатели. .041 завершена; .042–.050 planned, TASK-0003 in-progress, TASK-0004/TASK-0005 draft. Новые группы анализа не добавлялись в план.

Проверены локальные ссылки и якоря, соответствие каждого issue реестру, git diff --check, изменения только docs. Все 621 исходника совпадают с исходным срезом; совокупный SHA256 по сортированным путям (путь UTF-8 + NUL + байты файла) — 52701d3d0a5f054319886ac2a9d45b42c26c80098858d02518579c6a1edfaec4. Mode/uid/gid/inode всех 1329 ранее отслеживаемых файлов сохранены; прежнее содержимое журнала осталось ниже без изменения.

Не проверены реальный Dialog/DOM/css layout, штатные локализация/fallback и selectOptions, права/запись/конкурентность Foundry, изменение подготовленных данных после update, полная защита/урон/лечение и допустимость игровых сочетаний. Проверенные карточки описывают код и границы, а не обещают исправность системы.

## Пересборка TASK-0003.041–TASK-0003.050

| Поле | Результат |
| --- | --- |
| Дата / ветка | 2026-09-11 / rusbar-main |
| Коммит | 697c6fcb4d3a87aeb20427d696c4faf97613ba80; исходники не изменены |
| Рабочее дерево на старте | Семь изменённых указателей/реестров и десять новых файлов задач первоначального плана; пересборка работает с этими же 17 документами |
| Основание | Пользователь поручил укрупнить небольшие блоки и включить следующие связанные файлы |
| Актуальная серия | 77 уникальных файлов / 7065 строк: 19 JS, 18 HBS, 36 CSS, два JSON, два MJS |
| Сохранение объёма | Все 37 первоначальных файлов сохранены, добавлены 40; пересечений с прежними 310 карточками и внутри плана нет |
| Статусы | Десять существующих ID .041–.050 и planned сохранены; все исходники «Не начат» |
| Покрытие | 310 из 621; 311 не разобраны, из них 77 в очереди и 234 без подзадач |
| Сохранность | Код, карточки анализа, issues, реестр файлов и прежние выполненные задачи не изменены; метаданные всех 1329 существовавших файлов сохранены |

### Новый состав и перенос прежних блоков

[Актуальный план](../../tasks/task-0003-remaining-files.md#пятая-серия-task-0003041task-0003050): .041 атака (4/687), .042 защита (5/477), .043 броня/локации (3/320), .044 формирование/получение урона (9/603), .045 доставка/исполнение действий (5/336), .046 словесный бой (5/301), .047 способности/модификаторы (10/661), .048 представление предметов (16/920), .049 стили Actor (13/2178), .050 подключение ресурсов/инструменты (7/582). В скобках количество файлов/логических строк.

Из первоначального плана .043 и .045 объединены в новую .044; броня перенесена из .044 в .043. Боевые сообщения/Combat и сокет (.046/.047) объединены в .045 с отдельными маршрутами для каждого механизма. Словесный бой перемещён в .046, фабрики эффектов — в .047, сообщение Item — в .048. Дополнены связанные стили и поставлены блоки CSS Actor/инфраструктуры пакета. Нумерация остаётся последовательной, новых ID не вводилось.

Сверка первой половины теперь охватывает 26 файлов, всей серии — 77; обе с прежними 310 карточками. В .049 предусмотрены внутренние сверки общих вкладок, персонажа и монстра. [Промежуточный протокол № 1](cross-check-0001.md) остаётся вспомогательным материалом, TASK-0004 — draft.

### Проверка плана и границы

Списки извлечены из разделов «Исследуемые файлы», сверены с реестром, содержимым исходников, количеством строк, прежними карточками и друг с другом. Проверены перенос всех 37 файлов, состав дополнительных 40, наличие ссылок, актуальные названия/номера в указателях, условия общих сверок и остаток 234 (226 packsJson + восемь локализаций).

CSS группировались по прочитанным селекторам и цепочке из 35 @import входного файла, а не только по именам каталогов. Это предварительная ориентация для планирования; полный анализ каскада и визуальный прогон не выполнялись. Для package/build/utils прочитаны команды, includes и тела скриптов; сборка, извлечение и установка зависимостей не запускались.

Проверены локальные ссылки/якоря, таблицы задач, git diff --check, неизменность исходников и метаданных доступа. Состав 17 документов остался прежним, файлы не заменялись. Полные карточки новых исходников не создавались; анализ задач не начинался. Все записи журнала, существовавшие перед пересборкой, сохранены ниже без изменения. Они описывают историческую разбивку; актуальные перечни находятся в задачах.

## Планирование TASK-0003.041–TASK-0003.050

| Поле | Результат |
| --- | --- |
| Дата / ветка | 2026-09-11 / rusbar-main |
| Коммит проверки | 697c6fcb4d3a87aeb20427d696c4faf97613ba80; рабочее дерево на старте чистое |
| Основание | Поручение пользователя составить следующие десять подзадач TASK-0003 |
| Исходный срез | Все 621 исходник совпадают с TASK-0001, 15da5b225535e34af4e132c701b5353ef4eb667f |
| Новая серия | 37 уникальных файлов: 19 JS из module, 18 HBS; 3125 логических строк |
| Статусы | Десять задач planned; все 37 исходников «Не начат», полных карточек нет |
| Пересечения | Между новыми списками и с 299 файлами прежних подзадач TASK-0003 / 11 файлами TASK-0002 пересечений нет |
| Покрытие | 310 из 621; 311 не разобраны, из них 37 в очереди и 274 без конкретных подзадач |
| Сохранность | Исходники, реестр файлов, прежние задачи .001–.040, issues и прошлые записи журнала не изменены; метаданные 1319 ранее отслеживаемых файлов сохранены |

### Состав и порядок

[Точный план](../../tasks/task-0003-remaining-files.md#пятая-серия-task-0003041task-0003050): .041 атака (2/652), .042 защита (5/477), .043 формирование урона (3/167), .044 броня/локации (2/296), .045 получение урона (6/436), .046 боевые сообщения/Combat (4/315), .047 сокетный отправитель (1/21), .048 словесный бой (5/301), .049 фабрики полей эффектов (3/27), .050 описание Item в чате (6/433). В скобках количество файлов/логических строк.

Первичная ориентация по определениям, прямым вызовам, шаблонам, регистрации и уже описанным потребителям использована для выделения границ. Каждая центральная примесь разбирается полностью в своей порции, включая callbacks. Сокетный отправитель связан с ремонтом и передачей Item; он не добавлен к Combat только из-за расположения в scripts. Дополнительные фабрики проверяются отдельно на наличие подключения.

Общая сверка предусмотрена в .045 для всех 18 файлов первой половины и в .050 для всех 37; обе — с прежними 310 карточками. [Промежуточный протокол № 1](cross-check-0001.md) используется как исходный материал по схемам, ожиданию записей, ранним барьерам и дублям issues. TASK-0004 остаётся заготовкой.

### Проверки плана и ограничения

Списки извлечены из разделов «Исследуемые файлы», сопоставлены с реестром, наличием исходников и карточек, прежними порциями и друг с другом. Проверены количество строк, ссылки на определения/наблюдения, соседние номера задач, критерии общей сверки и статусы planned. Все оставшиеся module JS и HBS включены ровно один раз.

Остаток 274: 226 packsJson, 36 CSS, восемь локализаций, build.json/package.json и два utils. Документация, assets, .github и служебные файлы остаются исключёнными по прежним правилам.

Проверены 651 Markdown-документ docs и корневые README/AGENTS: 15 803 локальные ссылки и якоря без ошибок. Проверены 20 таблиц новых задач, git diff --check, неизменность исходного среза, всех прежних статусов задач и метаданных доступа. Это проверка постановки задач, не полный анализ 37 файлов и не запуск сценариев Foundry. Новые карточки анализа/issues не создавались; игровые тесты, сборка и мир не запускались.

## Общая промежуточная сверка № 1

| Поле | Результат |
| --- | --- |
| Дата / ветка | 2026-09-11 / rusbar-main |
| Коммит на старте | 411ab4004a2378a5f96ceeb19f003f834ff9d3d9; рабочее дерево чистое |
| Основание | Отдельное поручение пользователя проверить весь накопленный массив; вспомогательный материал для TASK-0004 |
| Охват | Все 310 карточек и 258 issues после .040; реестр 621 исходника |
| Содержательная проверка | 14 блоков B01–B14; 71 новая группа изолированных сценариев |
| Документация | Пять уточнений описаний и один установленный дубль 00200/00029; три карточки файлов и четыре issues уточнены |
| Статусы | Все 258 issues — potential; TASK-0004 — draft; новые задачи и проблемы не регистрировались |
| Сохранность | Все 621 исходник совпадают с HEAD и базовым срезом; права, владельцы, группы и inode 1318 ранее отслеживаемых файлов сохранены |

[Полный протокол](cross-check-0001.md) содержит матрицу каждого файла и issue, способы проверки, обнаруженные расхождения, связи между проблемами и ограничения. Прямые импорты/exports, буквальные HBS-связи, локальные ссылки и реестры проверены отдельно от семантики.

Мир, браузер, БД и многопользовательская сеть не запускались. Изолированные проверки используют настоящие модели/методы и явно обозначенные подмены; они не подтверждают успешное прохождение целого игрового процесса. Ранее выполненные сценарии не объявляются повторёнными без нового запуска. Все прежние записи ниже сохранены без изменений.

## TASK-0003.040

| Поле | Результат |
| --- | --- |
| Дата / ветка | 2026-09-11 / rusbar-main |
| Коммит проверки | `74322e91edac106c82668f4a47eef53ce1889dc1`; рабочее дерево на старте чистое |
| Базовый срез | `15da5b225535e34af4e132c701b5353ef4eb667f`; все 621 исходник сохраняют байтовое совпадение |
| Порция | [TASK-0003.040](../../tasks/task-0003.040.md); 10 файлов / 237 строк |
| Покрытие | 300 → 310 из 621; не разобраны311. Четвёртая серия:63 из 63, очередь0, вне конкретных подзадач311. |
| Окружение | Foundry 14.367.0 из /opt/foundryvtt; Node 24.16.0. Проверки запускались через node --input-type=module (stdin); тестовые файлы/стенд в репозитории не создавались. |
| Документация | 10 новых полных карточек, уточнения 17 связанных и 17 прежних issues; 4 новых potential issues. |

### Точный состав

| Исходник | Строк | Карточка |
| --- | --- | --- |
| [module/chatMessage/witcherChatMessage.js](../../../module/chatMessage/witcherChatMessage.js) | 3 | [Описание](files/module/chatMessage/witcherChatMessage.js.md) |
| [module/data/chatMessage/baseMessageData.js](../../../module/data/chatMessage/baseMessageData.js) | 16 | [Описание](files/module/data/chatMessage/baseMessageData.js.md) |
| [module/data/chatMessage/attackMessageData.js](../../../module/data/chatMessage/attackMessageData.js) | 31 | [Описание](files/module/data/chatMessage/attackMessageData.js.md) |
| [module/data/chatMessage/defenseMessageData.js](../../../module/data/chatMessage/defenseMessageData.js) | 42 | [Описание](files/module/data/chatMessage/defenseMessageData.js.md) |
| [module/data/chatMessage/damageMessageData.js](../../../module/data/chatMessage/damageMessageData.js) | 37 | [Описание](files/module/data/chatMessage/damageMessageData.js.md) |
| [module/data/chatMessage/templates/attackData.js](../../../module/data/chatMessage/templates/attackData.js) | 10 | [Описание](files/module/data/chatMessage/templates/attackData.js.md) |
| [module/data/chatMessage/templates/critData.js](../../../module/data/chatMessage/templates/critData.js) | 8 | [Описание](files/module/data/chatMessage/templates/critData.js.md) |
| [module/data/chatMessage/templates/damageData.js](../../../module/data/chatMessage/templates/damageData.js) | 18 | [Описание](files/module/data/chatMessage/templates/damageData.js.md) |
| [module/data/chatMessage/templates/locationData.js](../../../module/data/chatMessage/templates/locationData.js) | 10 | [Описание](files/module/data/chatMessage/templates/locationData.js.md) |
| [module/scripts/chat.js](../../../module/scripts/chat.js) | 62 | [Описание](files/module/scripts/chat.js.md) |

### Методика и границы исполнения

Прочитаны полные десять файлов, прямые определения и места регистрации; боевые/ремонтные соседи — в пределах полей и вызовов. Статические imports, SchemaField/EmbeddedDataField/TypeDataField, metadata, внешние API, HTML атрибуты, локализация и потребители сверены отдельно. Подробные методы, defaults, записи и ошибочные границы перечислены в карточках.

В Node загружены настоящие DataModel/fields из /opt/foundryvtt/common, четыре модели системы и common BaseChatMessage. Локальные правила DocumentUUIDField/TypeDataField изучены по исходникам этой установленной версии: UUID не доказывает существование документа; обычный DataModel допустим; base является разрешённым типом ядра. Конфигурация типов и минимальные game.model/users/release заданы явно. Это не запуск клиентского WitcherChatMessage, базы данных и миграции старой истории.

Callbacks чата исполнялись через реальную регистрацию chatMessageListeners; HTML получен настоящим Handlebars и разобран parse5, вместо DOM использован адаптер getAttribute/dataset/querySelector/addEventListener. Коллекции Actor/Item, UUID resolver, canvas/targets, DialogV2, update, addItem и ChatMessage.create — фасады; контролируемые Promise показывают границы ожидания. Из соседнего кода исполнены контекст передачи защиты, applyCritWound, processRequest и ранний участок prepareData. Удержание/восстановление методов prototype Repair выполнялось только в памяти процесса. Все 24 группы после уточнения ожиданий для очистки полей прошли.

Книги правил, браузерные события, серверные права и сохранение, несколько клиентов, полный боевой цикл и успешный полный ремонт не проверялись. Исследование не меняет игровые значения или архитектуру.

### Изолированные сценарии

| Группа | Сценарий | Наблюдаемый результат | Пределы |
| --- | --- | --- | --- |
| 01 | Определения, metadata и пустой класс документа | У WitcherChatMessage только constructor в prototype; модели имеют frozen type; Base.rollTotal default undefined. | Клиентский ChatMessage заменён фасадом; методы модели настоящие. |
| 02 | Четыре модели в настоящем common BaseChatMessage | base/attack/defense/damage выбраны по CONFIG; rollTotal '7'→7; parent связывает модель с документом. Отсутствующий type даёт base. | game.model/CONFIG/users и release — минимальные данные окружения; не клиент и не DB. |
| 03 | Числа, getter и source | −3/0/1.5 принимаются; 'abc' отклоняется. attackRoll отражает prepared rollTotal; toObject(true) сохраняет исходное значение. | Сохранение через update не выполнялось. |
| 04 | UUID | Синтаксически допустимы Actor/Item/embedded UUID, даже не разрешающиеся resolver. Неверный/относительный UUID отвергнут; пустое поле null. | UUID не ограничены типом Actor/Item; resolver перехвачен. |
| 05 | Четыре фабрики и локации | Новые поля при каждом вызове. damage.location.modifier — строка, formula initial1; defense.crit.location.modifier — число, formula default undefined; нечисловой текст отклонён. | Проверены данные, не все формулы выбора локаций. |
| 06 | defenseOptions | Шесть default-элементов; явный пустой Set сохраняется; custom допустим, пустая строка отклонена. | Наличие custom-защиты в боевом UI не подтверждено. |
| 07 | properties и эффекты | Attack.properties — DamageProperties/словарь; Damage.properties — обычный объект/массив; applied defaultfalse. | Это записи itemEffect, не встроенные документы ActiveEffect. |
| 08 | Очистка массива и вероятности | effects-словарь в damage очищается в []; percentage101→100, −1→0, '25'→25; старый массив attack-effects мигрирует в словарь. | Ожидание ошибки для словаря/101 уточнено по настоящему ArrayField/NumberField: выполняется очистка, не исключение. |
| 09 | Потеря полей damage при создании документа | У настоящих attack/damage ChatMessage удалены duration, heal, shield, item и вложенный defenseOptions из prepared/source. | Только duration имеет установленного последующего потребителя system.damage; корневой defenseOptions атаки сохраняется. |
| 10 | Схема критического результата защиты | Сырой critEffectModifier удалён из prepared и source; crit.location.critEffect остаётся undefined, если не задан. | Настоящий common-документ; не DB. |
| 11 | Выбор критической травмы | Настоящий applyCritWound при двух кандидатах и modifier+6 выбирает greater; после DefenseMessageData выбирает lesser из-за NaN. | Пак/UUID/addItem/ChatMessage — фасады; при явном critEffect или одном кандидате другая ветвь. |
| 12 | Контекст защиты | Настоящий combat.addDefenseOptionsContextMenu передаёт prepared attack/Set/damage, attackRoll17 и attackerUUID. | Actor.prepareAndExecuteDefense заменён приёмником аргументов; сам бой не исполняется. |
| 13 | Привязка кнопок | Без элементов — нет callback; при нескольких однотипных — привязывается первая кнопка каждого класса. | DOM адаптер parse5; текущие HBS содержат по одной такой кнопке. |
| 14 | Щит | 7/0/−2 передаются строкой в shield.value; сообщение имеет speaker источника, explicit type не задан. | update/create перехвачены; допустимость отрицательного щита как правила не оценивалась. |
| 15 | Цель лечения | Приоритет targets.first.actor → controlled[0].actor → user.character; при отсутствии всех — выход; speaker остаётся источником. | Коллекции и canvas заменены; это отдельный алгоритм, не getInteractActor. |
| 16 | Величина лечения | HP5/max20: heal50→20, 0→5, −9→−4, '2.8'→7; пустое/abc→NaN. При HP25/max20 heal0→20. | Зафиксирован payload update, не подтверждена запись отрицательных/NaN значений в серверную модель. |
| 17 | Отсутствующий источник | Щит падает без update; лечение с доступной целью сначала вызывает update, затем падает на actor.name. | Источник не удалялся в реальном мире; resolver вернул undefined. |
| 18 | Формулы в кнопках | Лечение '1d6' превращается в1; щит '2d6' передаётся строкой, числовая модель такую строку не принимает. | Продолжение issue-00249; это не проверка Roll.evaluate. |
| 19 | Граница завершения | onShield вернул undefined и создал сообщение при ещё pending update. | Promise удерживался локально; реальный отказ/гонка клиентов не проверялись; heal без await установлен статически. |
| 20 | Успешная передача запроса ремонта | Реальный callback и processRequest получают owner/item/artisan в правильном порядке и ждут renderDialog. | На prototype Repair заменены prepareData/renderDialog с восстановлением; не полная операция ремонта. |
| 21 | Устаревший запрос и target | Нет owner — TypeError до guard; нет Item при существующем owner — выход; вложенный target без dataset повторяет missing-owner. | Текущий HBS имеет текстовую кнопку, не иконку; последний случай — граница DOM-контракта. |
| 22 | Выбор исполнителя | Отсутствие исполнителя не защищает от missing-owner; DialogV2.input=null при нескольких Actor вызывает TypeError внутри helper. | Результат отмены управляемого DialogV2, не браузерный сценарий. |
| 23 | Настоящий ранний отказ ремонта | processRequest/prepareData при отсутствующей ссылке диаграммы уведомляют и не выполняют ремонтные записи. | Стоимость/skillBase/полный ремонт не достигнуты; issue-00103 не объявлена перепроверенной полным циклом. |
| 24 | HBS, атрибуты, ключи | Реальный repair.hbs рендерится с data-owner/item; кнопка текстовая. Ключи shieldApplied/healed доступны в en/ru. | DOM/события/создание чата заменены; служба Foundry не проверялась. |

### Итоговая сверка TASK-0003.031–TASK-0003.040

Перечни десяти задач сопоставлены друг с другом, исходниками и реестром: **63 уникальных файла (29 JS /34 HBS), 5046 строк**. Пересечений с прежними 247 нет:247+63=310. Все 63 имеют полные карточки с 11 обязательными разделами; собственные определения/методы и поля сверены. Десять новых карточек включают все определения нынешней порции. Для прежних 53 использованы их полные карточки, доказательства завершённых порций и неизменность исходников; прежние игровые сценарии всех десяти задач повторно не запускались.

| Часть серии | Опорные исходники | Перекрёстная проверка |
| --- | --- | --- |
| .031 — персонаж | [module/actor/sheets/WitcherCharacterSheet.js](../../../module/actor/sheets/WitcherCharacterSheet.js); [templates/partials/character-header.hbs](../../../templates/partials/character-header.hbs); [templates/sheets/actor/partials/character/sidebar.hbs](../../../templates/sheets/actor/partials/character/sidebar.hbs) | WitcherActorSheet, регистрация листа, CharacterData, itemMixin и Handlebars-поля. Собственные методы/контекст/действия сверены по карточкам и определениям; 26 групп .031 сохраняют свои ограничения. |
| .032 — монстр | [module/actor/sheets/WitcherMonsterSheet.js](../../../module/actor/sheets/WitcherMonsterSheet.js); [module/actor/sheets/configurations/WitcherMonsterConfigurationSheet.js](../../../module/actor/sheets/configurations/WitcherMonsterConfigurationSheet.js) | Наследование текущего V2-листа и конфигурации, MonsterData, действующие PARTS и исторические HBS разделены. Не все хранящиеся шаблоны являются зарегистрированными путями. |
| .033 — биография/заметки | [module/actor/sheets/mixins/noteMixin.js](../../../module/actor/sheets/mixins/noteMixin.js); [module/data/item/noteData.js](../../../module/data/item/noteData.js); [templates/partials/character/tab-background.hbs](../../../templates/partials/character/tab-background.hbs) | Actor.notes и Item.note — разные структуры; lifeEvents, редакторы и их запись связаны с Actor sheet/CharacterData/CommonItemData. Изменение prepared не приравнено к сохранению source. |
| .034 — ремесло/алхимия | [module/actor/mixins/craftingMixin.js](../../../module/actor/mixins/craftingMixin.js); [module/actor/sheets/mixins/alchemyMixin.js](../../../module/actor/sheets/mixins/alchemyMixin.js); [module/item/mixins/dismantlingMixin.js](../../../module/item/mixins/dismantlingMixin.js) | Object.assign Actor/Item, поиск компонентов, шаблон веществ и отчёт разбора. Критерии поиска и прямой метод отделены от дефектных UI/меню путей. |
| .035 — добыча/торговля | [module/actor/sheets/WitcherLootSheet.js](../../../module/actor/sheets/WitcherLootSheet.js); [module/data/item/mountData.js](../../../module/data/item/mountData.js); [module/item/sheets/WitcherMountSheet.js](../../../module/item/sheets/WitcherMountSheet.js) | Loot Actor sheet, контекст торговца и mount Item/ItemSheet; world/synthetic и query не смешаны. Историческая общая сверка первых31 файлов сохранена. |
| .036 — валюта | [module/actor/mixins/currencyConverterMixin.js](../../../module/actor/mixins/currencyConverterMixin.js); [module/actor/sheets/mixins/currencyConverterMixin.js](../../../module/actor/sheets/mixins/currencyConverterMixin.js) | Две одноимённые примеси имеют разные точки Object.assign. Курсы/выбранная валюта/форма/сообщение и границы save/query сопоставлены с config и Actor-данными. |
| .037 — награды | [module/actor/mixins/rewardsMixin.js](../../../module/actor/mixins/rewardsMixin.js); [module/actor/rewardsSheet.js](../../../module/actor/rewardsSheet.js); [module/app/reward/reward.js](../../../module/app/reward/reward.js); [module/app/htmlUtils.js](../../../module/app/htmlUtils.js) | Акторная примесь, Application, диалоги и HBS связаны с журналом наград/валютой/IP. Повторно проверены переводы; две missing amount-подписи остаются issue-00234. |
| .038 — профессия | [module/actor/mixins/professionMixin.js](../../../module/actor/mixins/professionMixin.js); [templates/dialog/combat/profession-attack.hbs](../../../templates/dialog/combat/profession-attack.hbs) | Кнопки текущих листов → Actor.applyProfession → ChatMessageData/extendedRoll → AttackMessageData. Новая схема не заполняет отсутствующий itemUuid; подтверждена связь issue-00239. |
| .039 — магия | [module/actor/mixins/castSpellMixin.js](../../../module/actor/mixins/castSpellMixin.js); [templates/chat/combat/spellItem.hbs](../../../templates/chat/combat/spellItem.hbs) | Текущие/старые списки и форма → castSpell → сырой damage и flavor → модель атаки. Автоматические эффекты до/после сообщения и HTML data-* разделены; новая потеря duration не подменяет старую проблему clone. |
| .040 — чат | [module/chatMessage/witcherChatMessage.js](../../../module/chatMessage/witcherChatMessage.js); [module/data/chatMessage/baseMessageData.js](../../../module/data/chatMessage/baseMessageData.js); [module/data/chatMessage/attackMessageData.js](../../../module/data/chatMessage/attackMessageData.js); [module/data/chatMessage/defenseMessageData.js](../../../module/data/chatMessage/defenseMessageData.js); [module/data/chatMessage/damageMessageData.js](../../../module/data/chatMessage/damageMessageData.js); [module/data/chatMessage/templates/attackData.js](../../../module/data/chatMessage/templates/attackData.js); [module/data/chatMessage/templates/critData.js](../../../module/data/chatMessage/templates/critData.js); [module/data/chatMessage/templates/damageData.js](../../../module/data/chatMessage/templates/damageData.js); [module/data/chatMessage/templates/locationData.js](../../../module/data/chatMessage/templates/locationData.js); [module/scripts/chat.js](../../../module/scripts/chat.js) | WitcherChatMessage — класс документа; ChatMessageData — обычный отправляемый объект; четыре DataModel — system; четыре фабрики — вложенные поля; chat.js — три HTML-действия. Бой, защита, ремонт и эффекты проверены только на указанных границах. |

Среди 310 описанных исходников сверены352 прямых относительных импорта (231 default, 114 named-операторов с 123 именами, 7 namespace) и198 буквальных связей на HBS. Новая порция добавляет 14 импортов и ни одного пути HBS. Исходник каждого импорта и соответствующий export существуют; карточка отправителя указывает источник, а описанная карточка источника — потребителя. Литералы шаблонов сопоставлены с существующими файлами и обратными упоминаниями. Это счётчик синтаксических связей, а не готовый граф всех динамических вызовов.

У серии 63 файлов — 39 прямых импортов, из них 27 в прежние247; прежние карточки имеют 24 импорта в серию. В серии 47 буквальных связей на HBS, из них 15 в прежние247; в обратную сторону 18. Динамические Object.assign, registration/PARTS/TABS, Hooks, form/action, пути system и цепочки отправитель→модель→потребитель сверены содержательно по таблице; внешние модули, миры и пользовательские макросы не охвачены. Неразобранный сосед с просмотренным вызовом не получает карточку или статус полного анализа.

Проверка переводов использовала настоящие expandObject и Localization.localize с английским fallback, а не плоский поиск JSON. Из63 файлов извлечены 255 уникальных литеральных кандидатов WITCHER.*. Восемь — префиксы (Actor.tabs/settings/rewards; Homelands., socialStanding., Monster.Type., Currency., Spell.), а не самостоятельные ключи. Среди 247 конкретных литералов доступны 245, отсутствуют только WITCHER.rewards.dialog.amount и WITCHER.rewards.chat.amount в обоих языках — существующая [issue-00234](../../issues/potential/issue-00234.md). Дополнительно разрешились 62 конкретных ключа вкладок и config-справочников homelands/socialStanding/currency/MonsterTypes. Динамические spell source/level/danger сохраняют проверки .039; произвольные пользовательские суффиксы, внешние словари и все восемь языков не объявлены проверенными.

### Сопоставление проблем

| Новая карточка | Наблюдение |
| --- | --- |
| [issue-00255](../../issues/potential/issue-00255.md) | Кнопки щита и лечения обращаются к отсутствующему Actor-источнику |
| [issue-00256](../../issues/potential/issue-00256.md) | Лечение из чата передаёт отрицательные и нечисловые значения в HP |
| [issue-00257](../../issues/potential/issue-00257.md) | Схема сообщений удаляет длительность эффектов из damage |
| [issue-00258](../../issues/potential/issue-00258.md) | Сообщение защиты теряет модификатор тяжести критической травмы |

Дополнены [issue-00005](../../issues/potential/issue-00005.md), [issue-00008](../../issues/potential/issue-00008.md), [issue-00025](../../issues/potential/issue-00025.md), [issue-00033](../../issues/potential/issue-00033.md), [issue-00044](../../issues/potential/issue-00044.md), [issue-00103](../../issues/potential/issue-00103.md), [issue-00108](../../issues/potential/issue-00108.md), [issue-00126](../../issues/potential/issue-00126.md), [issue-00127](../../issues/potential/issue-00127.md), [issue-00133](../../issues/potential/issue-00133.md), [issue-00134](../../issues/potential/issue-00134.md), [issue-00183](../../issues/potential/issue-00183.md), [issue-00184](../../issues/potential/issue-00184.md), [issue-00234](../../issues/potential/issue-00234.md), [issue-00239](../../issues/potential/issue-00239.md), [issue-00249](../../issues/potential/issue-00249.md), [issue-00253](../../issues/potential/issue-00253.md). Границы сравнений записаны в каждой карточке: base допускается ядром; chat.getSpeaker корректно получает источник; schema-очистка duration предшествует clone; formula/fumble проблемы прежние; async-кнопки дополняют issue-00127. Предыдущие проверки query, формул, flags и полного ремонта не объявлены выполненными заново.

Все 258 карточек остаются potential. Регистрация входит в [пункт9 TASK-0003](../../tasks/task-0003-remaining-files.md#общие-требования-к-каждой-подзадаче) и поручение продолжить анализ; это не подтверждение проблемы пользователем, не разрешение исправлять и не закрытие.

### Формальная проверка и остаток

Проверены состав и статусы реестра:621 исходник,310 карточек «Проверено», 311 «Не начат»; все40 подзадач завершены без двойного учёта. Проверены структура карточек, обязательные разделы issues, последовательная нумерация1–258 и отсутствие карточек open/closed. Все источники импортов, имена exports, буквальные HBS-пути и обратные упоминания сопоставлены; результаты содержательной сверки приведены выше.

Проверены 640 Markdown-файлов docs и корневые README/AGENTS:14897 локальных ссылок, существование целей/якорей, ширина таблиц и отсутствие хвостовых пробелов в изменённых документах. git diff --check проходит. Ровно 59 Markdown-документов в согласованном объёме изменены или созданы: 45 существующих и 14 новых (10 карточек файлов + 4 issues). Старые записи review-log и текст исторического плана сохранены без изменений.

Все 621 исходник байтово совпадают и с HEAD проверки, и со срезом TASK-0001; хеш совокупности исходников 52701d3d0a5f054319886ac2a9d45b42c26c80098858d02518579c6a1edfaec4. Для всех 1304 ранее отслеживаемых файлов сохранены mode/uid/gid/inode. Правки существующих документов выполнены на месте; права, владельцы, группы и служба не менялись. Сборка, извлечение компедиумов, создание стенда, изменение миров/БД, коммит и push не выполнялись.

TASK-0003.040 закрыта по критериям анализа; все .001–.040 выполнены. TASK-0003 остаётся in-progress, TASK-0004/TASK-0005 — draft. **311 оставшихся файлов требуют следующего согласованного планирования**; новых подзадач в этой порции не создано. Направления: остальные боевые примеси/обработчики, словесный бой, сокетные отправители, дополнительные модели/шаблоны, CSS, локализации, компедиумные данные и сборочные инструменты. Полные процессы и окончательный граф зависимостей остаются будущими этапами.

## TASK-0003.039

| Поле | Результат |
| --- | --- |
| Дата/задача | 2026-09-11; [TASK-0003.039](../../tasks/task-0003.039.md) |
| Версия | `rusbar-main`, `c598d74e34f4be51535de78b38f0601c286c5407`; рабочее дерево на старте чистое |
| Состав | Шесть полных файлов, 870 логических строк; castSpellMixin — 287, tab-magic — 80, spell-type-list — 174, monster-spell-tab — 223, spell-attack — 35, spellItem — 71 |
| Среда | Foundry 14.367.0 (/opt/foundryvtt/package.json), Node 24.16.0, Handlebars 4.7.9 |
| Исходники | 621 файл совпадает с HEAD и срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`; SHA256 `52701d3d0a5f054319886ac2a9d45b42c26c80098858d02518579c6a1edfaec4` |
| Доступ | До правок сняты mode/uid/gid/inode для 1288 отслеживаемых файлов; исходный metadata SHA256 `dddc588feb6b43f016eca061b340e56637cb191911d1373b2045aa1c4eb44932` |
| Результат | 6 новых карточек,34 уточнённые связанные,10 новых potential issues (00245–00254),17 уточнённых прежних; покрытие 300 / 621, остаток 321 |

### Методика и пределы

Все шесть исходников прочитаны целиком через cat/nl, определения и потребители найдены rg по module/templates. Проверены импорты, Object.assign, PARTS/TABS, подготовка списков и схемы данных, контекст partial-включений, listeners, автоматические эффекты, кнопки сообщения и граница области. Соседи прочитаны в пределах связи, их частичный разбор не увеличивает покрытие. Старый monster-spell-tab имеет consumer в старом монолите; зарегистрированный текущий MonsterSheet использует общий tab-magic.

Команда изолированных сценариев — `node --input-type=module` с программой через stdin, без создания тестовых файлов. Загружены настоящие модели SpellData/HexData/RitualData/CharacterData/MonsterData/DamageProperties/AttackMessageData, WitcherItem и тела методов Actor/листов, castSpellMixin, extendedRoll/RollConfig, status/ActiveEffect helpers, chat listeners и spellRegionMixin. Поля/очистка DataModel, RollParser/грамматика и броски Foundry настоящие; выдача кубов контролируется. Handlebars использует исходные HBS, core selectOptions/concat/localize и раскрытые expandObject en/ru с настоящим Localization/fallback.

Подменены Application и базовые документы окружения, Dialog/HTMLForm.elements, генераторы HTML input/select, итоговый Roll.toAnchor (только показ, не расчёт duration), отправка сообщений/запись Actor/Item, UUID resolver, ActiveEffect.clone/создание, canvas.placeRegion и User.query. parse5 — проверка разметки, не браузер. Управляемые Promise проверяют порядок завершения, не транзакции БД. Для .039 не запускались HTTP, мир, служба, компедиумы, полный бой/защита/урон, жизненный цикл ActiveEffect, statuscounter, настоящая сеть и несколько клиентов. Сохранённые материалы .009/.022 о core clone/области не выданы за повторное выполнение здесь.

### Сценарии

33 группы завершились успешно. Первые технические прогоны выявили недостающую инициализацию tabGroups в фасаде и неточную ожидаемую английскую подпись; исправлены только условия проверки в stdin. Эти отказы не приписаны системе. Код системы не менялся.

| Группа | Предмет | Вход/метод | Результат |
| --- | --- | --- | --- |
| 01 | Типы/навыки/speaker | Реальные spell четырёх class, hex, ritual | spellcast/hexweave/ritcraft; total 15; Actor speaker и attack.itemUuid корректны |
| 02 | Пустой Item/класс/навык | useItem missing; castSpell undefined; class пустой; явный melee | useItem→undefined; прямые несовместимые входы TypeError до диалога/STA |
| 03 | Списки | Три class×три level, MagicalGift, неизвестный class/level, hex/ritual, пустой Actor | 6 групп; 12 видимых Item дают 24 кнопки в двух представлениях; unknown не выводятся |
| 04 | Монстр/старый HBS | Настоящая MonsterData, PARTS и рендер обоих HBS | Текущий общий tab-magic; старый шаблон 6 панелей/8focus-полей |
| 05 | Вложенный partial | tab-magic→spell-type-list→summary→_onItemAdd | spellType не теряется; spellNovice даёт class Spells/level novice |
| 06 | Поля диалога | Минимальная/полная форма, actual selectOptions, focus2 | 2 или 6 полей; основной value 2, второй пустой; STA 5−2=3, сила 5 |
| 07 | Отмена/нехватка STA | Отмена prompt; цена 21 при STA 20 | Нет update/сообщения; недостаток даёт notification |
| 08 | Минимум/extra/фокусы | Нулевая цена; два выбора одного focus 2 и extra | Минимум 1; цена 6−2−2+3=5, бросок 15−3=12 |
| 09 | Модификаторы/EV | active+2, group+1, combat−2, EV 1, ignore3, custom−1 | Итог 17; EV даёт −1+3 без ограничения компенсации |
| 10 | Custom/details | Custom2/−2/1d6, подписи включены | 17/13/15; нечисловая строка custom не добавляется |
| 11 | Неверная STA | Ввод abc и −2 | Запрос NaN; отрицательная исходная сила даёт щит−4 при оплате 1 |
| 12 | Множитель | Числа, /STA, кубы, составные/дробные/пустые входы | 3×2d6+1→6d6+1; 2.9→множитель 2; 2+1→NaN; null→TypeError |
| 13 | Урон/тип сообщения | Урон 2d6, torso, настоящая AttackMessageData | Итог 14; formula/location/itemUuid сохранены; spellcasting в metadata против spellcast в броске |
| 14 | Повтор процента | Реальная DamageProperties, percentage 10,varEffect, STA 2 дважды | 20→40 в подготовленной модели; _source 10; запись Item не вызывается |
| 15 | Лечение | Fixed1d6 и variable1d6 | Fixed кнопка содержит формулу; variable ReferenceError heal после STA update, без сообщения |
| 16 | Кнопка лечения | Реальный onHeal, формула 1d6 и число 30 | parseInt даёт 1: HP 5→6; числовое лечение ограничено HP.max20 |
| 17 | Кнопка щита | Реальный onShield, щит 2d6, Actor.system.updateSource | update получает строку, числовая модель её отвергает; damageData не хранит shield/heal |
| 18 | Варианты щита | Fixed7, variable2/STA, variable1d6/STA при STA 3 | 7,6,3d6; вычисление кубов на границе кнопки отсутствует |
| 19 | Выбор цели лечения | Нет цели; затем selected target против user.character | При отсутствии update нет; первая цель имеет приоритет |
| 20 | selfEffects словарь | Реальная SpellData с fire и percentage 0 | Статус передан helper/toggle-фасаду, ссылки в HTML нет |
| 21 | Legacy-массив | Подготовленные selfEffects массивом с именем без статуса и fire | Показана лишь запись со статусом; не миграция мировых данных |
| 22 | Статусы/ActiveEffect | self/target/onHit с настоящими helpers | Self/target выбраны; onHit не включён; clone/запись — фасады |
| 23 | Цель hex/ritual | Реальные типы без onCastEffects и непустой targets | Бросок 15/сообщение возвращены, отсоединённый TypeError Object.values(undefined) |
| 24 | Fumble | d10=1, extra d10=5, shield/heal/self-status | Итог 6,fumble=true; статус пропущен, область вызвана, heal-кнопка всё ещё запросила HP 7 из 5 |
| 25 | DC ритуала | difficultyCheck25, итог 15 | DC есть в HTML; threshold−1, options.success undefined |
| 26 | Duration | Пустая, instant, 2 rounds, 1 hour 30 minutes, 1d6 rounds и for 1d6 rounds | undefined/пустая строка/2/130/куб 4; последний вариант отказал после STA update |
| 27 | Завершение | Удержанные Promise update/toggle/создания эффектов | castSpell вернул Roll до завершения; контрольное разрешение завершило фасады |
| 28 | Цена области | STA 5, focus2, перехват createSpellRegion | Оплата 3; options.stamina передана исходной строкой 5 |
| 29 | Компоненты | Подготовленные primary3×Known/alternate4×Alternative | Чат: главный список читаемый, alternate object Object; Actor-list показывает имя альтернативы без quantity |
| 30 | Локализация | Настоящие expandObject/Localization; literal scan6 файлов и source Water | Единственный literal ru-пропуск customModifier→Custom Modifiers; Water не найден в обоих языках |
| 31 | Редактирование/useItem | Настоящие editItem.onClick и _onItemRoll | sheet.render(true); ID/клавиши переданы useItem; запись/UI заменены |
| 32 | Настоящая цепочка области | castSpell→createSpellRegion→fromItem(circle)→placeRegion-фасад | flags.options пусты; прежняя ошибка Promise.all(Promise) поглощена; сообщение создано |
| 33 | Не владелец | Реальные helpers с isOwner=false | Захвачены status/ActiveEffect query; локального toggle/создания нет, сеть не выполнялась |

### Перекрёстная сверка

- Путь .spell-roll → itemMixin._onItemRoll → WitcherActor.useItem → castSpell проверен по определениям. Современное редактирование доступно через itemContextMenu.editItem; кнопки item-learned в обоих списках отсутствуют. Существование внешнего метода обучения не названо реализованным действием этого UI.
- Схемы magics → группы _prepareSpells → 12 включений списка → summary и поля диалога сопоставлены с их чтением. Наследуемый spellType сохраняется. У монстра общая вкладка показывает поле magicImprovementPoints без поля модели; уточнена прежняя issue-00192, запись не проверялась.
- Formula/STA/исходная сила разделены: фокус и extra меняют оплату, calcStaminaMulti использует исходную цену с parseInt. Бонусы берутся из уже подготовленной WILL, навыка, ActiveEffect/group и attackModifiers; прежняя проблема положительного attackModifier сохраняется. EV-компенсация не ограничена величиной EV.
- DamageProperties и selfEffects — разные словари: первый изменяется по ссылке до toObject(false), второй применяется через Object.values, но описание ошибочно ждёт массив. Типизированный attack несёт оба UUID; shield/heal/duration хранятся в HTML, не в damageData.
- Автоматические эффекты проверяют fumble; сообщение и вызов области выполнены раньше. Конкретные onHeal/onShield/onDamage и status-link consumers сопоставлены с атрибутами; только heal/shield обработчики выполнены изолированно, полный боевой цикл не заявляется. Тело chat.js целиком остаётся задачей .040.
- Область принимает исходную STA; прежние issues9/128/138/139/142/146 сохранены и уточнены на соответствующих границах. Изолированный успех запроса не назван созданием/настройкой региона.

Уточнены 34 ранее существовавшие карточки. Новые исходники и определения связаны в обе стороны; последующая формальная проверка дополнительно охватывает все уже документированные прямые импорты и literal HBS-пути. Историческая [общая сверка .031–.035](review-log.md#task-0003035) (31 файл/2497 строк с прежними 247 карточками) сохранена. Итоговая сверка всех 63 файлов четвёртой серии остаётся .040, здесь не заявляется выполненной.

### Проблемы

Новые potential:

| ID | Наблюдение |
| --- | --- |
| [issue-00245](../../issues/potential/issue-00245.md) | Переменная стоимость заклинания допускает NaN и отрицательную исходную силу |
| [issue-00246](../../issues/potential/issue-00246.md) | Множитель STA обрезает дробную стоимость и не масштабирует составные формулы |
| [issue-00247](../../issues/potential/issue-00247.md) | Переменный процент эффекта накапливается в подготовленных данных заклинания |
| [issue-00248](../../issues/potential/issue-00248.md) | Сотворение ритуала или порчи с выбранной целью передаёт отсутствующие onCastEffects |
| [issue-00249](../../issues/potential/issue-00249.md) | Кнопки лечения и щита не вычисляют переданные формулы заклинания |
| [issue-00250](../../issues/potential/issue-00250.md) | Длительность заклинания извлекается из текста без сохранения единиц и границ чисел |
| [issue-00251](../../issues/potential/issue-00251.md) | castSpell завершается до сохранения STA и применения эффектов |
| [issue-00252](../../issues/potential/issue-00252.md) | Сложность ритуала выводится в сообщении, но не участвует в проверке броска |
| [issue-00253](../../issues/potential/issue-00253.md) | Сообщение проваленного заклинания сохраняет действующие кнопки лечения и щита |
| [issue-00254](../../issues/potential/issue-00254.md) | Игнорирование EV при сотворении может превратиться в положительный бонус |

Уточнены прежние: [issue-00003](../../issues/potential/issue-00003.md), [issue-00008](../../issues/potential/issue-00008.md), [issue-00009](../../issues/potential/issue-00009.md), [issue-00033](../../issues/potential/issue-00033.md), [issue-00044](../../issues/potential/issue-00044.md), [issue-00064](../../issues/potential/issue-00064.md), [issue-00128](../../issues/potential/issue-00128.md), [issue-00133](../../issues/potential/issue-00133.md), [issue-00134](../../issues/potential/issue-00134.md), [issue-00135](../../issues/potential/issue-00135.md), [issue-00137](../../issues/potential/issue-00137.md), [issue-00138](../../issues/potential/issue-00138.md), [issue-00139](../../issues/potential/issue-00139.md), [issue-00142](../../issues/potential/issue-00142.md), [issue-00146](../../issues/potential/issue-00146.md), [issue-00186](../../issues/potential/issue-00186.md), [issue-00192](../../issues/potential/issue-00192.md). Ни один статус не переводился в open/closed. Регистрация разрешена общим пунктом 9 TASK-0003; исправлений и решений по игровым правилам нет.

### Формальная проверка

Проверки Python из stdin и `git diff --check` завершились успешно:

- Состав реестра совпал с Git и фактическим деревом: 621 исходный файл после исключений; 300 карточек со статусом «Проверено», 321 файл «Не начат». Порция содержит ровно 6 файлов и 870 строк, все 11 разделов карточек заполнены.
- Исходные байты всех 621 файлов совпали с текущим HEAD и базовым срезом; SHA256 не изменился. Для всех 1288 отслеживаемых файлов сохранены mode, uid, gid и inode. Новые права/владельцы отдельно не назначались.
- Проверены 338 прямых импортов из документированных JS: 218 default, 113 named-операторов (122 имени), 7 namespace; определения экспортов и обратные упоминания согласованы. В порции 5 прямых импортов. Проверены 198 literal HBS-связей, в порции 4 уникальные пары источник–шаблон (12 повторов include считаются одной парой).
- Проверены 626 Markdown-документов docs и корневые README/AGENTS: 14 529 локальных ссылок с целевыми файлами и якорями. Проверены таблицы и отсутствие пробелов в конце строк в изменённых документах.
- Изменены ровно 78 согласованных Markdown-документов: 62 существующих и 16 новых (6 карточек + 10 issues). Рабочий diff содержит только docs; исходники/игровые данные не затронуты.
- Issue ID образуют непрерывный диапазон 00001–00254, все 254 карточки остаются potential. Уточнения 17 прежних issues не дублируются. Статусы и перечни 40 подзадач согласованы с покрытием; новой задачи не создано.
- Предыдущая часть review-log сохранена без изменений; контрольный SHA256 исходного журнала `df26269144dce8b31577ce10a931bc90d61315fe23d4926ee37f1f84733cbc8d`. Исторические план и общая сверка .031–.035 не переписаны.

В четвёртой серии выполнены 53 из 63 файлов;10 в очереди, ещё 311 требуют детализации. TASK-0003.039 — done; .040 — planned, TASK-0003 — in-progress, TASK-0004/0005 — draft. Изменена только документация. Коммит не создавался.

## TASK-0003.038

Дата:2026-09-11. Ветка `rusbar-main`, HEAD `b47ba02cdaebc6a66ad14a5638213b6eb24460b4`; стартовое дерево чистое,1275 отслеживаемых файлов. Основание — [TASK-0003.038](../../tasks/task-0003.038.md) и продолжение согласованного пофайлового анализа.

### Состав и результат

Полностью прочитаны **четыре файла,965 строк**: один JS415 строк и три HBS550 строк. Девять собственных методов, все callbacks, десять ячеек Character дерева, defining Monster и 14 полей attack диалога описаны отдельно.

| Файл | Строк | Карточка |
| --- | --- | --- |
| [module/actor/mixins/professionMixin.js](../../../module/actor/mixins/professionMixin.js) | 415 | [Описание](files/module/actor/mixins/professionMixin.js.md) |
| [templates/partials/character/tab-profession.hbs](../../../templates/partials/character/tab-profession.hbs) | 337 | [Описание](files/templates/partials/character/tab-profession.hbs.md) |
| [templates/sheets/actor/partials/monster/tabs/tab-profession.hbs](../../../templates/sheets/actor/partials/monster/tabs/tab-profession.hbs) | 50 | [Описание](files/templates/sheets/actor/partials/monster/tabs/tab-profession.hbs.md) |
| [templates/dialog/combat/profession-attack.hbs](../../../templates/dialog/combat/profession-attack.hbs) | 163 | [Описание](files/templates/dialog/combat/profession-attack.hbs.md) |

Подготовлены четыре карточки; уточнены **29 связанных карточек и 13 прежних issues**. Покрытие **294/621**, остаток 327; в четвёртой серии 47/63, в очереди 16, ещё 311 требуют распределения. Следующая .039 не начата. Код, игровые правила/данные и права не менялись.

### Методика и ограничения

Запуск `node --input-type=module` со сценарием через stdin, без добавления исполняемого стенда в репозиторий. Настоящие professionMixin, item/skill/modifier методы, ProfessionData и вложенные модели, CharacterData/MonsterData/RaceData, DamageProperties, AttackMessageData, RollConfig/ChatMessageData/extendedRoll. Использованы реальные core Roll/грамматика/управляемые кубы, getSpeaker, Handlebars4.7.9/corehelpers и Localization с раскрытием словарей expandObject. Отдельно выполнена BaseActiveEffect.migrateData ядра.

**24 группы прошли** на Foundry14.367.0 (`/opt/foundryvtt/package.json`) и Node24.16.0. Dialog/HTMLFormElement/editor DOM, Application, конструктор ActiveEffect, UUID/коллекции/проверки владельца, запись Item/Actor/ChatMessage и query — фасады. Ожидаемые 15/16/12/9 заданы арифметически независимо от проверяемого метода. Отдельный callback onDamage исполнен на настоящей модели сообщения. Полные weaponAttack/defense/damage, клиентский constructor/clone effect, нативный render/validity, сервисные права, сеть/БД/несколько клиентов не запускались. Неутверждённые игровые правила не использованы для исправления кода.

Первоначальные ожидания тестов уточнены по ядру: пустой speaker.actor равен null, именованная torso имеет штраф−1; migrateData не переносит icon→img. Итоговые проверки прошли с настоящими соответствующими методами; исходники ради результата не менялись. Предупреждение MODULE_TYPELESS_PACKAGE_JSON не мешало запуску.

### Изолированные проверки

| Группа | Сценарий | Результат | Предел |
| --- | --- | --- | --- |
| 01 | Сумма/поиск | Нет профессии→сумма 0, поиск→TypeError; defining2+ветка 3→5; вторая профессия 10 игнорируется; дубликат Aid выбирает defining, пустое имя — первый пустой. | Первые Item через настоящий getList, без БД. |
| 02 | Dispatcher | Приоритет attack→custom→threshold→roll; неизвестное имя→TypeError; внешний await не держит внутренний Promise. | Внутренние действия заменены управляемыми Promise. |
| 03 | Обычный бросок/speaker | die5+int8+level2=15, default threshold0/rollOver15; speaker.actor=null без выбора, B при user.character=B для бросавшего A. | Настоящий core getSpeaker, toMessage перехвачен. |
| 04 | Stat/custom/равенство | empty/none/unknown stat→TypeError; custom2 дал 17 при threshold17: success=false/rollOver0, showResultfalse сохранил messageData без чата. | Custom prompt/форма — фасады. |
| 05 | Пороги | Одна запись 0 без окна; две — выбор 20; пустой словарь→TypeError после пустого select. | Доступ form.elements по id threshold воспроизведён фасадом. |
| 06 | Отмена | Прямые skill/attack/weapon/threshold отклоняют Promise до сообщений/записей. | Подставлен rejection prompt; DOM dispatcher не ждёт его. |
| 07 | Direct attack/форма | 14 полей; die5+stat8+level2+custom2−torso1=16; damage2d6+melee2+custom3; attack type/speaker A/attacker UUID. | Реальные методы, Roll и HBS; запись чата заменена. |
| 08 | Все флаги/STA | 10 флагов в сумме−2, итог 12 с torso−1; isExtraAttack штрафует, STA10 не меняется, update0. | Сравнение с кодом оружейной стоимости 3, не подтверждение правила рулбука. |
| 09 | Модификаторы | При AE навыка awareness+4 и attackModifier−2 вызван addActiveEffects(undefined); итог 14 без добавок. | Настоящий modifierMixin; generic weapon ветка отдельно прочитана. |
| 10 | Monster/detail | monster.addMeleeBonus=false: preview meleeBonus2, displayDamage1d6 и actual damage без+2; бросок 14 с деталями. | Визуальное окно браузера не запускалось. |
| 11 | Выбор оружия/ожидание | Set[ranged,melee] предлагает только ranged weapon; переданы skillReplacement и additionalDamageProperties, внешний Promise завершён раньше weaponAttack. | Последний consumer заменён удержанным Promise. |
| 12 | Пустое оружие/merge | Пустой chooser делегирует undefined; настоящий mergeDamageProperties не перенёс effects object. | Полный weaponAttack не исполнялся; TypeError его первого чтения установлен кодом. |
| 13 | Custom без HP/безцели | addTemporaryHealth=false — без броска; applyOnTarget без targets — уведомление и выход. | UI notifications перехвачены. |
| 14 | Цель и HP | Другой Actor maxINT12/value1 при multiplier1 дал DC12; roll15/rollOver3 и 3d6[2,3,4]→9HP; duration4; origin A, query B. applySelf=true не добавил себя. | Конструктор ActiveEffect/query — фасады. |
| 15 | Неуспех/cap | DC15/16 при 15 — без effect; DC1 даёт rollOver14,cap5 →5d6 и 5HP при единицах. | Реальные Roll/extendedRoll; не применение эффекта к Actor. |
| 16 | Длительность/имя | duration2→TypeError;10 проходит. Имя Aid "quote" делает raw JSON невалидным. | Полный цикл эффектов не исполнялся. |
| 17 | Не-dice HP/query | value+2 даёт выражение 5+2 внутри JSON, JSON.parse отклоняет; doProfessionSkillUsage завершён при pending query. | Только исходный payload и Promise-фасад. |
| 18 | Два дерева/нулевойуровень | Без Item:2add Character (race/profession),1Monster; с профессией:10/1 кнопка,30/3inline; none скрывает defining кнопку. | Истинный HBS, DOM разобран parse5. |
| 19 | Поля/редактирование | Все 35data-field Character и 3Monster принадлежат соответствующим Item schemas. Inlinelevel "0" передан строкой, модель дала Number0. | Item.update применял updateSource в памяти. |
| 20 | HTML/языки | Character не использует enriched marker, оставляет raw@UUID; с race35inline. Все literal attack-HBS ключи найдены EN/RU после expandObject/fallback. | Core editor с фасадом DOM; сохранение rich text не проверено. |
| 21 | Typed message/кнопка damage | Настоящая AttackMessageData: rollTotal14, attack.itemUuid=null,damage.itemUuid=null; лишний damage.item отсутствует; onDamage бросает TypeError. | Реальный onDamage с UUID-map; браузерного клика нет. |
| 22 | Self/порог/details | Оба target/self=false →query this; skillRoll даёт 15 при details=false/true; threshold−1 не создаёт success. | Полный серверный lifecycle не исполнялся. |
| 23 | Защиты/перевод | isDefense=false всё ещё допускает defendsAgainst; только definingSkill не даёт защиту. Три threshold RU ключа отсутствуют, EN fallback доступен. | Реальная ProfessionData, не полный defenseRoll. |
| 24 | Миграция AE ядра | Реальная BaseActiveEffect.migrateData переносит changes→system.changes, mode→type, JSON value и duration.rounds→value/units; icon не становится img. | Полный constructor/clone/UI не запускались. |

### Перекрёстная сверка

| Связь | Что сопоставлено | Граница результата |
| --- | --- | --- |
| Регистрация/поиск | witcherActor import12/Object.assign438; skillListener31→_onProfessionRoll; getList250+→первая не помещённая на хранение профессия по sort. | Поиск по имени отделён от устойчивого data-field редактирования; повторные имена не уникальны. |
| Контекст/представление | Character PARTS→10 навыков/раса; Monster PARTS→defining/notes. Config/statTypes/socialStanding и Item schemas сопоставлены с 35/3 полями. | Первый HBS включён в preload, другие загружаются через PARTS/прямой render. Сохранение rich text вложенного Item в браузере не проверено. |
| Бросок/порог | stat.value+level+getCustomModifier→ChatMessageData/RollConfig→extendedRoll. | Strict >, threshold0 по умолчанию; диспетчер не ожидает; общий skill/attack AE явно не добавляется в skillRoll. |
| Атаки/стоимость | Direct callback→14 полей→формула/damage→attack message. Weapon chooser→weaponAttack(skillReplacement,additionalDamageProperties). | STA/ammo/strike оружия не принадлежат direct ветви; их полная проверка вне порции. Отмечены пропуски модификаторов/UUID. |
| Сообщение/защита/урон | AttackMessageData принимает payload; combat.onDamage требует attack.itemUuid; executeDefense передаёт attack/options/damage/attackRoll/attacker. | Сама примесь не отправляет запрос защиты: он возникает в позднем действии чата. Полные защита/урон не выполнялись. |
| HP/effect/query | Target max→DC; rollOver/cap→HP; legacy newActiveEffect payload→core migration→owner.query→whitelist→applyActiveEffectToActor. | Не прямое пополнение hp. Миграция старых полей проверена отдельно от некорректного JSON и icon. Query/clone/persistence не исполнены полностью. |
| Прежние проблемы | 69/71/72 и 110/113/118/119 сверены; дополнительно 8/109/114/115/117/153. | Исполнение нового маршрута не подтверждает все прошлые симптомы. Статус каждого issue остаётся potential. |

Уточнены следующие связанные карточки:

- [module/actor/witcherActor.js](files/module/actor/witcherActor.js.md)
- [module/actor/sheets/WitcherCharacterSheet.js](files/module/actor/sheets/WitcherCharacterSheet.js.md)
- [module/actor/sheets/WitcherMonsterSheet.js](files/module/actor/sheets/WitcherMonsterSheet.js.md)
- [module/actor/sheets/WitcherActorSheet.js](files/module/actor/sheets/WitcherActorSheet.js.md)
- [module/actor/sheets/mixins/itemMixin.js](files/module/actor/sheets/mixins/itemMixin.js.md)
- [module/actor/sheets/mixins/skillMixin.js](files/module/actor/sheets/mixins/skillMixin.js.md)
- [module/data/item/professionData.js](files/module/data/item/professionData.js.md)
- [module/data/item/templates/professionSkillData.js](files/module/data/item/templates/professionSkillData.js.md)
- [module/data/item/templates/professionPathData.js](files/module/data/item/templates/professionPathData.js.md)
- [module/data/item/templates/profession/skillUsageData.js](files/module/data/item/templates/profession/skillUsageData.js.md)
- [module/data/item/templates/profession/temporaryHealthData.js](files/module/data/item/templates/profession/temporaryHealthData.js.md)
- [module/data/item/templates/profession/thresholdData.js](files/module/data/item/templates/profession/thresholdData.js.md)
- [module/data/item/templates/combat/skillAttackData.js](files/module/data/item/templates/combat/skillAttackData.js.md)
- [module/data/item/templates/combat/attackOptionsData.js](files/module/data/item/templates/combat/attackOptionsData.js.md)
- [module/data/item/templates/combat/defenseOptionsData.js](files/module/data/item/templates/combat/defenseOptionsData.js.md)
- [module/data/item/templates/combat/damagePropertiesData.js](files/module/data/item/templates/combat/damagePropertiesData.js.md)
- [module/actor/mixins/modifierMixin.js](files/module/actor/mixins/modifierMixin.js.md)
- [module/scripts/rolls/extendedRoll.js](files/module/scripts/rolls/extendedRoll.js.md)
- [module/scripts/rollConfig.js](files/module/scripts/rollConfig.js.md)
- [module/chatMessage/chatMessageData.js](files/module/chatMessage/chatMessageData.js.md)
- [module/scripts/helper.js](files/module/scripts/helper.js.md)
- [module/setup/config.js](files/module/setup/config.js.md)
- [module/setup/settings.js](files/module/setup/settings.js.md)
- [module/setup/handlebars.js](files/module/setup/handlebars.js.md)
- [module/data/item/raceData.js](files/module/data/item/raceData.js.md)
- [module/setup/queries.js](files/module/setup/queries.js.md)
- [module/scripts/temporaryEffects/applyActiveEffect.js](files/module/scripts/temporaryEffects/applyActiveEffect.js.md)
- [module/data/actor/templates/common/temporaryEffectsData.js](files/module/data/actor/templates/common/temporaryEffectsData.js.md)
- [module/data/activeEffects/witcherActiveEffectData.js](files/module/data/activeEffects/witcherActiveEffectData.js.md)

Модели attackMessageData/damageData/attackData, weaponAttack, defenseMixin, combat.js и locationMixin служили источниками нужных определений; новые полные карточки им не создавались. Их частичное изучение не увеличивает покрытие. Карточки Actor, Item и конфигурации не заменялись, уточнения добавлены отдельными разделами.

### Потенциальные проблемы

| Issue | Наблюдение | Статус |
| --- | --- | --- |
| [issue-00236](../../issues/potential/issue-00236.md) | Бросок профессии выбирает отправителя через отсутствующий Actor.actor | potential |
| [issue-00237](../../issues/potential/issue-00237.md) | Профессиональные атаки обходят модификаторы навыка и общие модификаторы атаки | potential |
| [issue-00238](../../issues/potential/issue-00238.md) | Дополнительная профессиональная атака без оружия не списывает STA | potential |
| [issue-00239](../../issues/potential/issue-00239.md) | Кнопка урона профессиональной атаки не получает UUID предмета | potential |
| [issue-00240](../../issues/potential/issue-00240.md) | Формула временного здоровья без кубов попадает в JSON без вычисления | potential |
| [issue-00241](../../issues/potential/issue-00241.md) | Обработчики профессии завершаются до вызванных бросков и применения эффекта | potential |
| [issue-00242](../../issues/potential/issue-00242.md) | Выбор оружия способности продолжает выполнение при пустом списке | potential |
| [issue-00243](../../issues/potential/issue-00243.md) | Временное здоровье передаёт изображение эффекта в устаревшем поле icon | potential |
| [issue-00244](../../issues/potential/issue-00244.md) | Диалог атаки монстра показывает неиспользуемый бонус ближнего боя | potential |

Дополнены [issue-00008](../../issues/potential/issue-00008.md), [issue-00069](../../issues/potential/issue-00069.md), [issue-00071](../../issues/potential/issue-00071.md), [issue-00072](../../issues/potential/issue-00072.md), [issue-00109](../../issues/potential/issue-00109.md), [issue-00110](../../issues/potential/issue-00110.md), [issue-00113](../../issues/potential/issue-00113.md), [issue-00114](../../issues/potential/issue-00114.md), [issue-00115](../../issues/potential/issue-00115.md), [issue-00117](../../issues/potential/issue-00117.md), [issue-00118](../../issues/potential/issue-00118.md), [issue-00119](../../issues/potential/issue-00119.md), [issue-00153](../../issues/potential/issue-00153.md). Основание регистрации — пункт 9 TASK-0003. Подтверждение/перевод статуса/исправление не выполнялись. Отсутствие ветвей в Monster UI и действие уровня 0 описаны как поведение, не как автоматически ошибочные правила.

### Формальная проверка документов и сохранности

Проверка Python через stdin и `git diff --check` прошла. Реестр содержит 621 файл после согласованных исключений; карточки и строки реестра согласованы:294 «Проверено»,327 «Не начат». Точный состав .038 — четыре файла/965 строк. Перечни сорока подзадач не пересекаются: .001–.038 done, .039–.040 planned, родительская in-progress. Четвёртая серия —47 проверенных из 63,16 в очереди;311 ещё не распределены. TASK-0004/TASK-0005 остаются draft.

Сверены 333 прямые локальные import-связи описанных JS:217 default,109 named-выражений (116 имён),7 namespace. У новой порции четыре imports; имена/экспорты и обратные упоминания сопоставлены. Проверены 194 уникальные для каждой карточки ссылки на репозиторные HBS, одна из новой примеси; уже существующие producer-ссылки на два новых HBS также сверены в обратную сторону. Динамические зависимости и callbacks разобраны отдельно выше.

Проверены **14 060 локальных ссылок** в 610 Markdown-файлах docs и двух корневых README/AGENTS: цели, якоря, столбцы изменённых таблиц, обязательные 11 разделов новых карточек и имена всех собственных методов. Issues имеют уникальныеID1–244, все potential и включены в индекс. Состав изменений — **66 Markdown-документов:53 существующих и 13 новых** (четыре карточки и девять issues); вне docs изменений нет.

Все 621 исходник побайтно совпали с HEAD и срезом TASK-0001. Контрольные суммы совокупности исходников и метаданных доступа совпали со стартовыми. Сохранены mode/uid/gid/inode всех 1275 отслеживаемых файлов, ветка/HEAD и исходный хвост журнала. Историческая общая сверка .031–.035 с прежними 247 карточками сохранена без переписывания результатов. Новые файлы созданы обычной записью без отдельного назначения прав.

Исторические записи журнала, включая общую сверку .031–.035, сохранены. Полная сверка всех 63 файлов серии остаётся в .040; TASK-0004/TASK-0005 draft. Исходники не исправлялись, коммит не создавался.

## TASK-0003.037

Дата: 2026-09-11. Ветка `rusbar-main`, HEAD `639fde4bad4a7ba4c538d3b08ddc5cfd846ca75e`; стартовое дерево чистое, отслеживаются 1263 файла. Основание — [TASK-0003.037](../../tasks/task-0003.037.md) и поручение продолжать согласованный пофайловый анализ.

### Состав и результат

Полностью прочитаны **восемь файлов, 313 логических строк**: четыре JS (267 строк) и четыре HBS (46 строк). Документированы десять собственных функций/методов, статические PARTS/TABS/DEFAULT_OPTIONS, callbacks выбора и выдачи, поля обоих диалогов и все четыре шаблона.

| Файл | Строк | Карточка |
| --- | --- | --- |
| [module/actor/mixins/rewardsMixin.js](../../../module/actor/mixins/rewardsMixin.js) | 9 | [Описание](files/module/actor/mixins/rewardsMixin.js.md) |
| [module/actor/rewardsSheet.js](../../../module/actor/rewardsSheet.js) | 55 | [Описание](files/module/actor/rewardsSheet.js.md) |
| [module/app/reward/reward.js](../../../module/app/reward/reward.js) | 178 | [Описание](files/module/app/reward/reward.js.md) |
| [module/app/htmlUtils.js](../../../module/app/htmlUtils.js) | 25 | [Описание](files/module/app/htmlUtils.js.md) |
| [templates/sheets/actor/rewards/header.hbs](../../../templates/sheets/actor/rewards/header.hbs) | 3 | [Описание](files/templates/sheets/actor/rewards/header.hbs.md) |
| [templates/sheets/actor/rewards/ip.hbs](../../../templates/sheets/actor/rewards/ip.hbs) | 11 | [Описание](files/templates/sheets/actor/rewards/ip.hbs.md) |
| [templates/sheets/actor/rewards/currency.hbs](../../../templates/sheets/actor/rewards/currency.hbs) | 12 | [Описание](files/templates/sheets/actor/rewards/currency.hbs.md) |
| [templates/chat/rewards.hbs](../../../templates/chat/rewards.hbs) | 20 | [Описание](files/templates/chat/rewards.hbs.md) |

Добавлены восемь карточек; уточнены **19 связанных карточек и три прежних issues**. Покрытие — **290/621**, остаток331; в четвёртой серии проверены43/63, в очереди20, ещё311 требуют распределения. Следующая .038 не начата. Исходники, игровые правила, данные и права не менялись.

### Методика и ограничения

Изолированный сценарий выполнен командой `node --input-type=module` через stdin; исполняемые файлы/стенд в репозиторий не добавлялись. Импортированы настоящие Rewards, rewardsMixin, RewardsSheet, htmlUtils, CharacterData/MonsterData/LootData/Log и core TypeDataModel/fields; использованы Handlebars4.7.9, parse5, FormDataExtended core helpers localize/concat и отдельно извлечённые методы DialogV2.input, core builders, multi-select _initialize/_getValue, Application._prepareTabs/_getTabsConfig, inherited hasPlayerOwner. Везде проверялся наблюдаемый результат; ожидаемые12/6/105/13 заданы независимо от вычисляющего метода.

**24 группы прошли** на Foundry14.367.0 (`/opt/foundryvtt/package.json`) / Node24.16.0. DOM-конструкторы/HTMLFormElement, prompt/ответ диалога, базовый ActorSheet, коллекция/UUID, проверки владения и Actor.update/ChatMessage.create — фасады. В обычном сценарии update применяет patch к настоящей модели в памяти; удержанные/отклонённые Promise проверяют конкретный порядок. Тестовый catch отклонений нужен только для учёта результата, его нет в коде системы. Нативный custom element, browser validity/render/полный sanitizer, сеть, права сервера, БД и несколько клиентов не запускались. Core Dialog очищает строковый content до render; этот этап прочитан ранее в .036, здесь его не подменяли утверждением об исполнении HTML. Предупреждение Node MODULE_TYPELESS_PACKAGE_JSON не помешало выполнению.

При первой сборке проверки уточнены два ожидания: core не задаёт cssClass неактивной вкладке, а amount-переводы действительно отсутствуют. Итоговые assertions отражают прочитанный код и отдельные проверки результата; исходники ради прохождения не менялись.

### Изолированные проверки

| Группа | Сценарий | Результат | Предел |
| --- | --- | --- | --- |
| 01 | htmlUtils и builders | input number с name без min/max/step/required/dtype; title допускает HTML. options.name перекрывает name select; core экранирует подписи options. | DOM — минимальный фасад; title в реальном вызове — локализация. |
| 02 | Получатели по умолчанию | hasPlayerOwner=true включён, false исключён; отсутствие actors подбирает список, явный [] остаётся пустым. | Коллекция Actor подменена. |
| 03 | Повторные options и HTML имени | Два одинаковых UUID дали два option, но actual multi _initialize/_getValue вернул один UUID через Set; имя экранировано. | Изолированные core методы; браузер custom element целиком не запускался. |
| 04 | Типы FormDataExtended | DialogV2.input с фасадом prompt/form: пустой number→null; 0/−2/1.5→Number; isMagic→Boolean; label пустая строка. | Это преобразование значений, не native constraint validation. |
| 05 | Currency select | Семь ключей CONFIG, включая falsecoin; первый вариант bizant; пустая amount→null. | Нативный выбор первого option воспроизведён в фасаде формы. |
| 06 | GM guard | Оба публичных handout для не-GM завершились до диалога/записи; прямой ipRewardDialog([]) сформировал окно. | Серверные permissions не проверены; диалог сам не начисляет. |
| 07 | Отмена/пустой выбор | null/false/{} либо actors:[] останавливают оба handout до рендера и записи. | Ответ Dialog.input подставлен; реальные cancel/close не нажимались. |
| 08 | 0/null награда | При валидном Actor — 0 update,0 chat, но 1 renderTemplate. | Числовой payload; строка "0" не моделирует штатный number input. |
| 09 | Обычные/магические IP | Обычные10→12 при magic4; либо magic4→6 при обычных10. История1→2; старый элемент сохранён. В чат не переданы isMagic/speaker. | Настоящие CharacterData/Log, запись модели в памяти. |
| 10 | Несколько денежных получателей | Оба crown100→105, история1→2; один chat. context amount5/type=crown без currency скрывает денежный блок. currency=true в контроле показывает сумму. | Контроль HBS не изменение системы. |
| 11 | Отрицательные/дробные значения | −2/1.5 применены обоими handout к числу баланса без собственной валидации. | Допустимость корректировок по правилам не оценивалась. |
| 12 | Повторы в подменённом ответе | Один UUID дважды в values.actors: два начисления IP,10→14, две записи, имя дважды в контексте. | В штатном multi-checkbox повторы убирает Set; не обычный способ выбора. |
| 13 | Исчезнувший UUID | [Character, missing] инициирует один update, затем TypeError; до чата не доходит. | fromUuidSync — map; удаление Actor при открытом UI не воспроизводилось. |
| 14 | Monster/Loot | Настоящие модели не содержат logs; hasPlayerOwner отбор их не исключает. Оба handout дают TypeError. | Фасады Actor с реальными system-моделями. |
| 15 | Неизвестная валюта | Подменённый type=unknown дал NaN в patch, историю с unknown, неизменный crown100 и вызов chat. updateSource не добавил unknown в currency. | Штатный select unknown не предлагает; неизвестна серверная обработка patch. |
| 16 | Обёртки Actor | await addIpReward/addCurrencyReward завершился при удержанном game.api.rewards Promise. | API заменён управляемым Promise. |
| 17 | Завершение handout | handout завершился, когда Actor.update и ChatMessage.create ещё pending; исходный IP10 до разрешения, затем12. | Задержки фасадов, не сеть. |
| 18 | Повтор до окончания записи | +2/+3 приIP10 создали абсолютные patches12/13. Выбранный порядок оставил13 и две новые записи вместо суммы15. | Конкретный порядок фасада; не доказательство всех серверных гонок. |
| 19 | Частичный отказ | Rejected update первого Actor не остановил второго/чат; первый кошелёк100, второй105; prepared история первого уже увеличена push. | Тест перехватил rejection сам; система не содержит этой обработки. |
| 20 | RewardsSheet и четыре PARTS | config/system по ссылке, core tabs ip active/currency без cssClass. Все HBS, включая core tab-navigation, дали форму без полей: FormDataExtended={}. | Base Application/DOM — фасады. |
| 21 | История/остаток/дата | Порядок old→новая запись, isMagic literal true; HTML label экранирован. Замена истории на IP99 не пересчитала обычные10 или magic6. Даты в записи нет. | updateSource модели, не серверная форма редактирования. |
| 22 | EN/RU и escaped text | Существующие подписи/типы валют доступны после expandObject и core fallback; имена/label не стали HTML-элементами. | Рендер Handlebars, не внешний модуль/браузер. |
| 23 | Два отсутствующих ключа | dialog.amount и chat.amount возвращаются ключами в EN/RU. Диалог показывает первый; второй появляется в контроле currency=true. | Обычную денежную ветку скрывает отдельная issue232. |
| 24 | Точный смысл ownership | Inherited hasPlayerOwner=true для неактивного не-GM OWNER, false для только GM owner. | Настоящее тело getter; users и testUserPermission — фасады. |

### Перекрёстная сверка

| Связь | Что сопоставлено | Граница результата |
| --- | --- | --- |
| Регистрация → UI | main22/39–41 → Rewards handout; Actor import15/Object.assign450 → две wrapper; CharacterSheet116/448–450 → addIpReward. | Прямой currency wrapper UI consumer не найден. GM gate у handout; листы/развитие не наследуют его автоматически. |
| Просмотр → PARTS | CharacterSheet import6/field14/_renderRewards460–462 → RewardsSheet → header/ip/currency + core generic tabs. | В своих HBS нет полей формы, несмотря на submitOnChange. Общая IP-вкладка Monster не создаёт методы CharacterSheet. |
| Форма → значения | htmlUtils → actual builders → options actors UUID/name selected:true → multi-checkbox Set; input label/ip/amount/isMagic; select type. | DialogV2.input/FormDataExtended отделены от нативной формы. Числа/boolean не выводятся из названий полей. |
| Выбор → модель | hasPlayerOwner с non-GM OWNER → список всех типов → fromUuidSync → system.logs.add*. | CharacterData имеет logs/IP/magic; Monster/Loot нет. Явный массив не фильтруется заранее. |
| Журнал → баланс | Log.push → update целого массива и абсолютного остатка; обычный или magic пул/одна валюта. | Нет суммы истории как источника баланса, даты записи, rollback или результатов по получателям. Конвертация/покупка не обязаны попадать в этот журнал. |
| Обновление → сообщение | forEach Log без ожидания → await render → create OTHER без await. | Нет isMagic, speaker, timestamp в собственном payload; amount/type без currency. ChatMessage метаданные не являются датами ipLog/currencyLog. |
| Локализация/ресурсы | config.currency → select/lookup; localize/concat core; EN/RU expandObject/fallback; .logEntry ← styles/rewards.css. | rates/excluded не участвуют. Шаблоны вне preload грузятся прямыми путями. CSS и языки целиком не добавлены в покрытие. |
| Прежние issues | 17 — затенённая magicalCost развития;28 — потеря Promise журнала;30 — IP-форма Monster. | Прямое magic начисление работает; это не исправление17. Расширены28/30 с отделением разных входов. Issue202 остаётся дефектом ссылки header. |

Уточнены связанные карточки:

- [module/TheWitcherTRPG.js](files/module/TheWitcherTRPG.js.md)
- [module/actor/witcherActor.js](files/module/actor/witcherActor.js.md)
- [module/actor/sheets/WitcherCharacterSheet.js](files/module/actor/sheets/WitcherCharacterSheet.js.md)
- [module/data/actor/characterData.js](files/module/data/actor/characterData.js.md)
- [module/data/actor/commonActorData.js](files/module/data/actor/commonActorData.js.md)
- [module/data/actor/monsterData.js](files/module/data/actor/monsterData.js.md)
- [module/data/actor/lootData.js](files/module/data/actor/lootData.js.md)
- [module/data/actor/templates/character/logData.js](files/module/data/actor/templates/character/logData.js.md)
- [module/data/actor/templates/character/ipLogData.js](files/module/data/actor/templates/character/ipLogData.js.md)
- [module/data/actor/templates/character/currencyLogData.js](files/module/data/actor/templates/character/currencyLogData.js.md)
- [module/data/actor/templates/common/currencyData.js](files/module/data/actor/templates/common/currencyData.js.md)
- [module/setup/config.js](files/module/setup/config.js.md)
- [module/setup/handlebars.js](files/module/setup/handlebars.js.md)
- [module/actor/mixins/skillMixin.js](files/module/actor/mixins/skillMixin.js.md)
- [module/actor/sheets/mixins/skillMixin.js](files/module/actor/sheets/mixins/skillMixin.js.md)
- [module/actor/sheets/WitcherMonsterSheet.js](files/module/actor/sheets/WitcherMonsterSheet.js.md)
- [templates/partials/character-header.hbs](files/templates/partials/character-header.hbs.md)
- [templates/partials/character/tab-skills.hbs](files/templates/partials/character/tab-skills.hbs.md)
- [templates/sheets/actor/tabs/tab-inventory.hbs](files/templates/sheets/actor/tabs/tab-inventory.hbs.md)

### Потенциальные проблемы

| Issue | Наблюдение | Статус |
| --- | --- | --- |
| [issue-00232](../../issues/potential/issue-00232.md) | Сообщение о денежной награде скрывает сумму и валюту | potential |
| [issue-00233](../../issues/potential/issue-00233.md) | Выдача наград не проверяет совместимость и существование получателей | potential |
| [issue-00234](../../issues/potential/issue-00234.md) | Денежная награда обращается к отсутствующим ключам перевода количества | potential |
| [issue-00235](../../issues/potential/issue-00235.md) | Неизвестный тип денежной награды доходит до журнала и некорректного баланса | potential |

Дополнены [issue-00017](../../issues/potential/issue-00017.md), [issue-00028](../../issues/potential/issue-00028.md), [issue-00030](../../issues/potential/issue-00030.md). Регистрация разрешена пунктом9 родительской TASK-0003; подтверждение, изменение статуса и исправление не выполнялись. Отрицательная/дробная награда, отсутствие редактора/дат и неразличение magic в чате описаны как факты/ограничения; новые требования к правилам из них не выведены.

### Формальная проверка документов и сохранности

Проверка Python через stdin и `git diff --check` прошла. Состав реестра совпал с Git и фактическим деревом: 621 файл после исключений, 290 карточек «Проверено», 331 «Не начат». Точный состав .037 — восемь файлов/313 строк; перечни сорока подзадач не пересекаются, .001–.037 done, .038–.040 planned. Родительская задача in-progress, TASK-0004/TASK-0005 draft.

Проверены 329 прямых локальных import-связей всех описанных JS: 216 default, 106 named import-выражений (112 имён) и 7 namespace; у .037 один named import с двумя exports. Сверены пути/имена определений и обратные упоминания в уже существующих карточках. Проверены 193 уникальные для каждой карточки ссылки на репозиторные HBS, из них четыре в новой порции; внешний generic/tab-navigation в это количество не включён. Динамические пути API/Log/контекста сверены отдельно в таблице выше.

Проверены **13 595 локальных ссылок** в 597 Markdown-файлах docs и двух корневых README/AGENTS, якоря, столбцы изменённых таблиц и отсутствие хвостовых пробелов. Issues имеют уникальные ID1–235, все potential и отражены в индексе. Состав изменений — **45 Markdown-документов: 33 существующих и 12 новых** (восемь карточек и четыре issues); вне docs изменений нет.

Все 621 исходник побайтно совпали с HEAD и базовым срезом TASK-0001. Совпали стартовые SHA256 совокупности исходников и метаданных доступа; mode/uid/gid/inode всех1263 отслеживаемых файлов сохранены. Ветка/HEAD не изменились; исходный хвост review-log совпадает с HEAD и стартовой контрольной суммой. Новые файлы созданы обычной записью, отдельного назначения прав не было.

Исторические записи журнала, включая общую сверку .031–.035 с прежними247 карточками, сохранены побайтно. Полная сквозная сверка всех63 файлов предусмотрена в .040, а TASK-0004/TASK-0005 остаются draft. В рамках .037 исходники не исправлялись; коммит не создавался.

## TASK-0003.036

Дата: 2026-09-11. Ветка `rusbar-main`, HEAD `32d8fdd029ce4c6401db25f0d9645445ac0f8ca2`; стартовое дерево чистое, отслеживаются 1254 файла. Основание — [TASK-0003.036](../../tasks/task-0003.036.md) и поручение продолжить согласованный пофайловый анализ.

### Состав и результат

Полностью прочитаны **четыре файла, 164 логические строки**: два JS на 114 строк и два HBS на 50. Actor-примесь определяет три метода, примесь листа — один регистратор с forEach callback. Одинаковые имена export сохранены с точными путями.

| Файл | Строк | Карточка |
| --- | --- | --- |
| [module/actor/mixins/currencyConverterMixin.js](../../../module/actor/mixins/currencyConverterMixin.js) | 107 | [Описание](files/module/actor/mixins/currencyConverterMixin.js.md) |
| [module/actor/sheets/mixins/currencyConverterMixin.js](../../../module/actor/sheets/mixins/currencyConverterMixin.js) | 7 | [Описание](files/module/actor/sheets/mixins/currencyConverterMixin.js.md) |
| [templates/sheets/actor/currencyConverter/currencyConverter.hbs](../../../templates/sheets/actor/currencyConverter/currencyConverter.hbs) | 33 | [Описание](files/templates/sheets/actor/currencyConverter/currencyConverter.hbs.md) |
| [templates/chat/currency-conversion.hbs](../../../templates/chat/currency-conversion.hbs) | 17 | [Описание](files/templates/chat/currency-conversion.hbs.md) |

Добавлены четыре карточки, уточнены **15 связанных карточек и три прежних issues**. Покрытие — **282/621**, остаток 339; в четвёртой серии проверены 35/63, в очереди 28, ещё 311 файлов требуют распределения. Код, игровые данные, курсы и правила комиссии/округления не менялись.

### Методика и ограничения

Проверка выполнена командой `node --input-type=module` со сценарием через stdin; в репозиторий исполняемые файлы/стенд не добавлялись. Импортированы настоящие обе currencyConverterMixin, WitcherActor/WitcherItem, CharacterData/MonsterData/LootData и core TypeDataModel/fields. Использованы Handlebars 4.7.9, parse5, core DialogV2.input/FormDataExtended и отдельно извлечённый _onSubmit. Регистрация клика проверена настоящим EventTarget Node.

**21 группа прошла.** Dialog.input/prompt, HTMLFormElement, базовое Application и запись Actor/ChatMessage — фасады. При обычных сценариях patch применяется к настоящей модели; при изучении invalid payload часть update намеренно только фиксировалась, что не доказывает сохранение NaN/Infinity в Foundry. Подменённые Promise удерживались/отклонялись; конкурентные результаты описаны только для выбранного порядка фасада. Browser constraints/event pipeline, полный render/DOMParser/sanitizer, мир, сеть и серверные транзакции не запускались. Предупреждение Node MODULE_TYPELESS_PACKAGE_JSON не мешало успешному запуску.

### Изолированные проверки

| Группа | Сценарий | Результат | Предел |
| --- | --- | --- | --- |
| 01 | Курсы | Шесть ставок 4/⅓/2/3/1/1; getCurrencyRates возвращает ту же ссылку. Falsy объект вызывает явный Error. | Неполные/испорченные настройки подставлены только локально. |
| 02 | Контекст и форма | Шесть options без falsecoin, балансы из модели. Настоящий core input/FormDataExtended дал {amount:1,from:crown,to:oren,fee:0}. | Dialog.prompt и HTMLFormElement — фасады. |
| 03 | Отсутствующие данные | CONFIG.currency отсутствует→TypeError; нет actor.system.currency→явный Error; до рендера. | Unsupported конфигурация, не ошибка штатного набора. |
| 04 | Excluded/пустые options | Все исключены→0options, оба select пусты. Нет currencyConverter→7options, falsecoin без курса. | Нет проверки состояния настоящей БД или настроек мира. |
| 05 | Character/Monster/Loot | Три реальные модели: crown100/oren5→90/15; один update; OTHER chat с правильным speaker.actor. | Метод доступен на Actor; кнопка найдена только в текущем Character HBS. |
| 06 | Формула/комиссия/floor | bizant3→crown12; crown2→ducat6; ducat2→crown0; bizant2→floren,fee10→2; fee100→0; floren1→lintar1. | Все исходные суммы списываются; не оценка правил рулбука. |
| 07 | Нехватка/отмена | 101 из100→локализованный warn/0update/0chat; null input возвращается даже при отсутствующих rates. | Отмена не вызывает getCurrencyRates; реальный close UI не запускался. |
| 08 | Same currency | crown100/amount10: fee0→110; fee50→105; fee100→100; один ключ в update. | Дополнение issue20, не новый ID. |
| 09 | Сумма/комиссия вне диапазона | amount−10→110/−5;0→100/5;0.5→99.5/5. fee−10→90/16;150→90/0;100.5→90/4. | Контролируемый ввод; допустимость нулей/дробей как правил не решалась. |
| 10 | Некорректные ставки | target0→Infinity; bad/missing→NaN; source0→списание без получения; source−1→отрицательный result. Реальная модель при пустом rates отклонила запись, чата нет. | В вариантах с перехватом без валидации виден только invalid payload, не испорченная БД. |
| 11 | Неизвестный/исключённый ключ | Программные unknown/falsecoin from/to доходят до payload с NaN. | Штатные select не предлагают unknown и исключённый falsecoin. |
| 12 | Типы и ограничения формы | NumberField формы: отрицательные/дробные значения приведены; blank numeric→null. HTML amount min1/step1, fee min0/max100/step1; required нет. | Настоящий FormDataExtended не выполняет диапазонную валидацию. |
| 13 | Ожидание/отказ update | Pending update держит Promise и не даёт chat; rejected update прекращает до рендера результата. | Операции записи — фасады; права сервера не обходились. |
| 14 | Сообщение | Pending ChatMessage.create не удерживает возвращаемый Promise; деньги уже обновлены. | Сетевая ошибка чата не воспроизводилась. |
| 15 | Два обмена до записи | Оба рассчитали одинаковый update90/15; после выбранного порядка фасада два сообщения и один абсолютный итог90/15. | Контролируемый interleaving, не универсальное доказательство серверной гонки. |
| 16 | Замена модели при открытом окне | Захвачено100/5; model заменена на2/40; после ввода10 update всё равно90/15, без warn. | Реальные CharacterData, подмена lifecycle Actor и persistence. |
| 17 | Event adapter | preventDefault выполнен, this=Actor; handleCurrencyConverter ждёт Promise open. | Отдельно от регистрации/ожидания DOM события. |
| 18 | Listeners | Пустой NodeList безопасен; одна регистрация/клик→1; две на том же узле/клик→2; новый узел→1. | Настоящий Node EventTarget; не реальный browser render. |
| 19 | Core submit | Настоящий direct _onSubmit вызывает callback и close, не вызывает подставленный checkValidity; buttons временно отключены. | Это проверка метода. _onClickButton и его регистрация прочитаны, browser event pipeline не выполнялся. |
| 20 | Chat HBS | fee10%, amount/result, динамические локализованные from/to; вход actor не выводится; опасная разметка экранирована. | Настоящий Handlebars, не визуальный чат. |
| 21 | Локализация/HTML allowlist | 16 ключей маршрута доступны EN/RU после expandObject+Localization. input/select разрешены, script/onchange отсутствуют в реальных константах. | cleanNode и Dialog normalization прочитаны; DOMParser/полный sanitizer не исполнялись. |

### Перекрёстная сверка

| Связь | Что сопоставлено | Граница результата |
| --- | --- | --- |
| Конфигурация/регистрация | module/TheWitcherTRPG.init→CONFIG.WITCHER; config.currency/rates/excluded→Actor-примесь; WitcherActor Object.assign17/452. | Курсы статические, без world setting/сети. Один и тот же export-name двух примесей различён полным путём. |
| Кнопка/наследование | Character PARTS inventory→.open-currency-converter→WitcherActorSheet.activateListeners→sheet mixin→Actor.handleCurrencyConverter. | V1 и Loot не подключают sheet mixin; Monster наследует listener, но его HBS не содержит кнопку. Прямой метод у моделей есть. |
| Поля/форма/сохранение | CommonActorData/LootData→currency()→currencies; options→два select; Dialog.input→FormDataExtended→расчёт→два пути одного update. | Number/String/null отделены от HTML min/max/step и от model validation. Ссылку currencyData до await и ставки после input сверили раздельно. |
| Формула/сообщение | floor(amount×fromRate/toRate×(1−fee/100)); await update→render chat→create OTHER/speaker Actor. | amount не уменьшается на комиссию; result уже округлён; HBS не вычисляет; actor label передан, но не читается. Кошелёк не пишется в currencyLog. |
| Предыдущие проблемы | issue20 повторён; покупка issue221 сопоставлена: конвертер ожидает update. Issue226 уточнён более ранней очисткой DialogV2.content. | Историческое исполнение _renderHTML из .035 не проверяло normalization; исправлений кода нет. |
| Подписки и части HBS | V2._onRender снова зовёт activateListeners на всём элементе; core HandlebarsApplicationMixin заменяет entries только отрендеренных частей. | Две регистрации на сохранённой кнопке дают две функции bind; полный render с новой кнопкой не объявлен проблемным. Частичный render в браузере не запускался. |
| Границы | Четыре новых полных файла, 15 связанных описаний; оба HBS не preloaded, вызываются напрямую renderTemplate. CSS/locales/core — только зависимости. | .037 награды, последующие профессии/магия/чат не начаты. TASK0004/0005 остаются draft. |

### Уточнение прежнего анализа DialogV2

При разборе .036 прочитан этап **до** _renderHTML: /opt/foundryvtt/client/applications/api/dialog.mjs:_initializeApplicationOptions184–199 вызывает foundry.utils.cleanHTML для строкового content. Реализация /opt/foundryvtt/client/utils/helpers.mjs:15–19,68–107 очищает узлы/атрибуты по common/constants.mjs:1845+. Script и inline onchange не входят в allowlist, обычные form/input/select/option и атрибуты name/min/max/step/data-* поддержаны. Проверены настоящие константы; полная очистка через DOMParser не исполнялась.

Это уточняет [issue-00226](../../issues/potential/issue-00226.md) и карточку LootSheet: в .035 исполнялся _renderHTML на уже переданном сыром content без normalization. Нельзя считать, что этот тест доказал попадание script в настоящее окно. По источникам очистка удаляет script/onChange раньше стадии innerHTML; ручной vm-запуск .035 по-прежнему доказывает только арифметику функций после явного исполнения. Историческая запись сохранена с её пределами; утверждение о проверенном браузерном дефекте не добавлено.

### Проблемы

| Новая карточка | Наблюдение |
| --- | --- |
| [issue-00227](../../issues/potential/issue-00227.md) | Обмен валюты не проверяет диапазон суммы и комиссии |
| [issue-00228](../../issues/potential/issue-00228.md) | Обмен не проверяет выбранные валюты и значения курсов |
| [issue-00229](../../issues/potential/issue-00229.md) | Открытый конвертер может перезаписать изменившиеся остатки |
| [issue-00230](../../issues/potential/issue-00230.md) | Повторная привязка конвертера дублирует обработчик кнопки |
| [issue-00231](../../issues/potential/issue-00231.md) | Обмен возвращает завершение до создания сообщения чата |

Уточнены [issue-00020](../../issues/potential/issue-00020.md), [issue-00221](../../issues/potential/issue-00221.md), [issue-00226](../../issues/potential/issue-00226.md). Все **231 карточка остаются potential**. Регистрация не означает подтверждения, решения об исправлении или закрытия. Корректные default ставки и принятый кодом floor сами по себе не объявлены нарушениями правил.

### Формальная проверка

Выполнены Python-проверки дерева/Git/Markdown и `git diff --check`. Реестр содержит 621 уникальный исходник: 282 карточки «Проверено», 339 «Не начат». Новые четыре файла не пересекаются с прежними 278; для них проверены все 11 разделов карточки, собственные методы и поля формы. В серии .031–.040 проверены 35 из 63, 28 остаются planned; ещё 311 без детализации. Первые 31 файл общей сверки .035 по-прежнему имеют отдельную границу с прежними 247.

Во всех 282 карточках проверены 328 прямых импортов и export-имена: 216 default, 105 named statements/110 имён, 7 namespace. Обе стороны связей сопоставлены с определениями/потребителями. Литеральных связей JS/HBS с шаблонами 189; эта порция добавила 0 импортов и 2 HBS-пути. Проверены **13 276 локальных ссылок и якорей** во всех 587 Markdown (585 в docs плюс README/AGENTS), таблицы и конечные пробелы изменённых файлов.

Изменены **38 Markdown**: 29 прежних и 9 новых (4 карточки и 5 issues). Перечень совпал с согласованными материалами. Статусы всех 40 подзадач, parent in-progress, будущих задач draft/planned и всех 231 potential issues проверены; новых задач/статусов open/closed нет.

Все 621 исходника побайтно совпадают с текущим HEAD `32d8fdd029ce4c6401db25f0d9645445ac0f8ca2` и срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`; SHA256 содержимого реестра: `52701d3d0a5f054319886ac2a9d45b42c26c80098858d02518579c6a1edfaec4`. mode/uid/gid/inode всех 1254 отслеживаемых файлов сохранены; SHA256 метаданных: `afd7d44fd392ecb3fea189448d38b5d20178a3590c620ca772ec37aba1e70a4a`. Исторический хвост review-log и раздел планирования .031–.040 сохранены побайтно; уточнение прежнего исследования добавлено новой записью и дополнениями карточек. Только docs изменены; коммит/сборка/данные мира не затрагивались.

**Переход:** TASK-0003.036 выполнена; следующая — [TASK-0003.037](../../tasks/task-0003.037.md) (награды). .037–.040 остаются planned, TASK-0003 in-progress, TASK-0004/TASK-0005 draft. Коммит не создавался.

## TASK-0003.035

Дата: 2026-09-11. Ветка `rusbar-main`, HEAD `1d29f681ffed1c46b9c05b0eff09935300c3bf7d`; рабочее дерево на старте чистое, отслеживаются 1239 файлов. Основание — согласованная [TASK-0003.035](../../tasks/task-0003.035.md) и поручение пользователя продолжить.

### Состав и результат

Полностью прочитаны **шесть файлов, 384 логические строки**: три JS (209 строк) и три HBS (175 строк). Шесть собственных методов Loot, MountData.defineSchema, два определения функций внутри строки script и callback prompt разобраны отдельно от наследуемых методов MountSheet и mixins.

| Файл | Строк | Карточка |
| --- | --- | --- |
| [module/actor/sheets/WitcherLootSheet.js](../../../module/actor/sheets/WitcherLootSheet.js) | 175 | [Описание](files/module/actor/sheets/WitcherLootSheet.js.md) |
| [templates/sheets/actor/loot-sheet.hbs](../../../templates/sheets/actor/loot-sheet.hbs) | 130 | [Описание](files/templates/sheets/actor/loot-sheet.hbs.md) |
| [templates/sheets/actor/partials/loot/loot-item-display.hbs](../../../templates/sheets/actor/partials/loot/loot-item-display.hbs) | 25 | [Описание](files/templates/sheets/actor/partials/loot/loot-item-display.hbs.md) |
| [module/data/item/mountData.js](../../../module/data/item/mountData.js) | 19 | [Описание](files/module/data/item/mountData.js.md) |
| [module/item/sheets/WitcherMountSheet.js](../../../module/item/sheets/WitcherMountSheet.js) | 15 | [Описание](files/module/item/sheets/WitcherMountSheet.js.md) |
| [templates/sheets/item/mount-sheet.hbs](../../../templates/sheets/item/mount-sheet.hbs) | 20 | [Описание](files/templates/sheets/item/mount-sheet.hbs.md) |

Добавлены шесть карточек; уточнены **17 связанных карточек и 12 прежних issues**. Покрытие **278/621**, осталось 343; в четвёртой серии проверен 31 из 63 файлов, 32 в очереди, 311 ещё не распределены. Только Markdown в docs; исходники и игровые правила не исправлялись.

### Методика и пределы

Команда проверки — `node --input-type=module` с переданным через stdin кодом; служебные файлы/стенд в репозитории не создавались. Импортированы настоящие WitcherLootSheet/MountData/LootData/WitcherMountSheet, WitcherActor/WitcherItem, itemMixin/itemContextMenu и core TypeDataModel/fields. Формы рендерились установленным Handlebars 4.7.9, HTML разбирался parse5. Настоящие FormDataExtended/_processFormData и выборочные тела core testUserPermission/_toggleDisabled/_onDragStart/Dialog._renderHTML выполнены с минимальными фасадами.

**26 групп прошли.** Диалог возвращал заданные строки callback; операции embedded create/update/delete перехватывались в памяти, часть Promise удерживалась до явного разрешения. Базовый Application, форма/DOM, коллекции и persistence — фасады. Script пересчёта цены исполнялся явно в vm, его автоматическое подключение браузером не проверялось. Браузерная валидация дробных/пустых чисел, нативный drag/drop, FilePicker, серверные разрешения/транзакции/гонки и игровой мир не запускались. Существование старого issue не доказывает неисправность каждого нового маршрута.

При настройке изолированной проверки исправлены только фасады: вложенный patch system.currency, отступ извлекаемого core-метода, тип CSV-настройки и источник metadata permissions; исходники системы не менялись. Для права Actor сверено именно /opt/foundryvtt/common/documents/actor.mjs:#canUpdate134–146 (OWNER и дополнительные проверки wildcard), а не только metadata базового Document. Предупреждение Node о MODULE_TYPELESS_PACKAGE_JSON не мешало успешному запуску.

### Проверки этой порции

| Группа | Сценарий | Фактический результат | Предел |
| --- | --- | --- | --- |
| 01 | MountData | 12 полей, dex/control/speed строки; hp0/−2.5; bad HP отклонён; общий вес6 и inherited false. | Реальная схема, не правила верхового боя. |
| 02 | Пустой Loot | Шесть массивов/таблиц, семь валют, totalWeight0, totalCost undefined. | Контекст/рендер без окна. |
| 03 | Смешанные типы | 18 Item,9 строк; loot=mount/container/alchemical/diagrams; mutagen пропущен; applied и stored не показаны; вес17. | Специальные поля Mount/Enhancement — реальные модели, прочие типы — CommonItemData для общих свойств. |
| 04 | Вес и hidden | При6/6 overweight,6/7 progress, max0 без шкалы. GM/nonGM разные CSS-классы, hidden имя остаётся в HTML. | CSS статически; DOM видимость не исполнялась. |
| 05 | Нормальная покупка | qty3→2 у продавца,1 у покупателя; crown5→15 и100→90. OWNER список включает seller/buyer, выбран user.character; шесть валют без falsecoin. | Dialog callback и persistence подменены. |
| 06 | Нехватка/неизвестная валюта | Money9 при total10 и unknown coin дают Not Enough Coins; записей0. | Неизвестный coin вводился программно, штатный select его не предлагает. |
| 07 | Отмена | Отклонённый prompt при rejectClose приводит к rejected handler до записей. | Настоящий UI закрытия не выполнялся. |
| 08 | Отсутствующий покупатель/Item | Пустой select character → TypeError; stale itemId падает до prompt. | Записей0, отключение кнопки в браузере не моделировалось. |
| 09 | Запас/количество | Stock2/request5 → delete+create5, stock0/request1 → create1; request0/−1/0.5 проходит; −1 повышает seller2→3. | Нативные constraints Number input не исполнялись; количество в callback строковое. |
| 10 | Стоимость | Итоги0/−10/0.5 и цена0.25 проходят;−10 даёт buyer110/seller−5. | Допустимость бесплатной/дробной покупки как игрового правила не решалась. |
| 11 | Одноимённый Item | name/type merge: qty4→5, cost старого2 сохраняется. | Это контракт Actor.addItem, не копирование всех свойств при merge. |
| 12 | Ожидание/повтор | Четыре записи pending при resolved handler; повтор создаёт те же seller qty2 и buyer crown90. Выбранный порядок фасада создаёт две копии. | Не доказательство неизбежной серверной гонки. |
| 13 | Покупка самим продавцом | Payload delete,qty2,crown90,crown110; выбранный порядок фасада оставил без Item с crown110. | Проверен конкретный interleaving с одной последней единицей. |
| 14 | Отказ записи продавца | Подменённые rejected remove/update не остановили buyer create и crown100→90. | Не обход серверного OWNER; полномочия core сверены отдельно. |
| 15 | Скрытие | Только system.isHidden=true; Promise handler разрешён до item.update. | Фасад записи; кнопка в HBS только GM, собственного GM guard нет. |
| 16 | Item Drop | Без actor.isOwner false/0write; владелец копирует чужой mount; свой Item сортируется; uniqueTypes три. | Прямой _onDropItem, внешние события/Folder/ActiveEffect не воспроизводились. |
| 17 | Profession в Loot | deleteMany типа profession, затем TypeError отсутствующих skills до add. | Предыдущей профессии в фасаде не было; фактическая потеря не доказана. |
| 18 | Drag | Рендер0 .draggable, img .dragable/data-id. Core _onDragStart не пишет payload; контроль data-item-id пишет UUID. | Тело core с event-фасадом, не browser drag. |
| 19 | Изображение и MountSheet | Loot img без action; mount header с editImage; mount PARTS/width600/context.item верны. | FilePicker/окно не создавались. |
| 20 | Форма mount | FormDataExtended + _processFormData + MountData сохранили dex/control/speed строки, hp0 число, quantity снова String; textarea экранирована. | Form-фасад не воспроизводит textarea.value, сохранение описания им не доказано. |
| 21 | Inline/actions | qty0.5 обновлён строкой; buy/hide связаны с DEFAULT_OPTIONS, prototype содержит настоящие mixins. | Не полный dispatch окна. |
| 22 | Script арифметики | Вручную исполненные функции дали20 для qty2/cost10;125%→unit13,total26; Actor.name вставлен raw. | Это явный vm execution, не автоматическое исполнение script окна. |
| 23 | Права/отключение формы | Настоящие core testUserPermission и _toggleDisabled: GM/owner/observer; inputs отключены, buy anchors существуют в HBS. | Element/document фасады, не серверная авторизация. |
| 24 | Render hooks | Настоящий Loot._onRender вызвал itemListener→itemContextMenu с element. | super Application — фасад; действия меню не выполнялись. |
| 25 | Переводы | 29 прямых ключей шести файлов доступны EN/RU после expandObject и настоящего Localization с fallback. | Соседние helper keys не включены в эти29; другие языки не проверены. |
| 26 | Вставка Dialog | Настоящее тело core _renderHTML присваивает content со script/inline onChange в innerHTML и регистрирует submit. | document.createElement — фасад; автоматическое выполнение script и браузерная ошибка не воспроизводились. |

### Общая перекрёстная сверка TASK-0003.031–TASK-0003.035

Сверены карточки 31 нового файла с исходниками и прежними 247 описаниями, направления зависимости→определение→consumer и реальные пути данных. Записи .031–.034 и их результаты сохранены как исторические: совпадение исходников проверено вновь, но весь прежний набор runtime-сценариев заново не исполнялся. Формальные проверки ниже охватывают весь текущий массив 278 карточек; содержательная сверка процессов отражена отдельно в таблице.

| Связь/область | Проверенный контракт и результат | Что этим не утверждается |
| --- | --- | --- |
| Состав пяти порций | TASK0003.031/.032/.033/.034/.035:3+13+4+5+6=31; JS11/HBS20;2497строк. Прежние247 и новые31 не пересекаются; текущие278 =247+31. | Исходники всех621 совпали со стартовым HEAD и базовым срезом; прежние runtime-сценарии не объявлены заново исполненными. |
| Регистрация → модель → лист | registerDataModels/registerSheets/system.json сопоставлены с Character/Monster/Loot/Mount. Character и Monster используют WitcherActorSheet; Loot core ActorSheetV2; Mount WitcherItemSheet. | Разница наследования объясняет отсутствие totalCost/skills в Loot и отсутствие _prepareWeapons; поля специализаций не приписаны общим классам. |
| Числа и боковые панели .031/.032 | stats/derivedStats/currency/commonActorData и ранее описанные модели связаны с Character header/sidebar и Monster header/sidebar. Жизненные события/temporary HP сохраняют границу source/prepared data. | Прежние issues24/203/205 и ограничения .031 сохранены. В .035 не пересчитывались характеристики или heal; эти процессы не переписывались. |
| Контексты → HBS → обработчики | PARTS, literal partial, data-action, jQuery selector, dataset и путь schema сверены отдельно. Покупка использует (event,element), меню по-прежнему имеет issue168. Mount имеет PARTS, note-sheet отдельно не подключён. | Наличие HBS/предварительная загрузка не равны активному листу; старый monster-sheet и пустой monster-details-tab сохраняют прежние границы .032. |
| Экспорт монстра → Loot | Monster.exportLoot копирует все items Actor.toObject, меняет quantity и зовёт checkIfItemHasRollTable; Loot собирает собственные категории. mutagen существует в экспортном payload, но отсутствует в новом списке из-за mutagens. | Issues206/207/208,39/40 по-прежнему potential; export Actor.create/БД не запускались в .035. Покупка не повторяет генерацию таблиц. |
| Биография/заметки .033 | Character context → Actor.notes/lifeEvents → background HBS → noteMixin/FormData; Item.note → NoteData и отдельно note-sheet. Array actor.notes не является коллекцией embedded Item.note. | Issues211/212/213 и24/57/153 сохранены. Поток Item.note не подменяет Actor.notes; source/prepared и сохранение формы различаются. |
| Ремесло/алхимия .031/.034 | Character.craft/Item.realCraft/repair → CraftingMixin.getSubstance/findNeededComponent; direct counts + pannels → substances HBS → component partial. AlchemyMixin.alchemyComponentsList не имеет найденного HBS consumer. | getSubstance исключает stored и сортирует, findNeededComponent ищет также stored/нулевые; findComponentByUuid не имеет внутреннего caller. Полный сценарий мира повторно не запускался. |
| Разбор → инвентарь/чат | WitcherItem.dismantle → associatedDiagramUuid/craftingComponents → fromUuid → Actor.addItem/removeItem → dismantle HBS. Покупка Loot использует те же Actor helper, но другую последовательность/вход. | Issues214–217 не исправлены; .034 исполнял direct dismantle, не заблокированное issue168 меню. В .035 добавлены отдельные наблюдения покупки220/221. |
| Улучшения и общие Item-поля | Weapon/Armor preparation в прежних карточках влияет на enhancementItems; Loot только исключает enhancement.applied из массива, не перестраивает enhancementItems. CommonItemData задаёт Mount quantity/weight/cost/hidden. | Issue166 к Loot по одному соседнему applied Item не переносится. Hidden CSS — визуальное отображение, не гарантированное сокрытие данных от клиента. |
| Прямые импорты/обратные связи | У первых31 файлов15 прямых импортов:12 связей в9 файлов прежних247, две внутри31, одна в пока не разобранный module/actor/rewardsSheet.js. Проверены export имена, места consumer и обратные ссылки во всех278 карточках. | rewardsSheet остаётся dependency-only до .037; полная карточка не создана. Контекст/HBS/модели проверены дополнительно, не сведены к одним import. |
| Остаток и внешние границы | 32 файла стоят в .036–.040;311 ещё не распределены. В ближайших порциях обмен валюты, награды, профессии, магия, чат. CSS, локализации, core Foundry, assets и packs рассматриваются как точечные зависимости. | Исключённые docs/assets/.github/.git не получили строк реестра. TASK0004/TASK0005 остаются draft; общая проверка не объявляет весь аудит завершённым. |

### Проблемы

| Новая карточка | Наблюдение |
| --- | --- |
| [issue-00218](../../issues/potential/issue-00218.md) | Лист добычи не включает предметы типа mutagen |
| [issue-00219](../../issues/potential/issue-00219.md) | Общая стоимость в листе добычи выводится без значения |
| [issue-00220](../../issues/potential/issue-00220.md) | Покупка не проверяет запас, количество и итог оплаты |
| [issue-00221](../../issues/potential/issue-00221.md) | Покупка завершается до записей и не согласует их результаты |
| [issue-00222](../../issues/potential/issue-00222.md) | Покупка не обрабатывает отсутствие доступного покупателя |
| [issue-00223](../../issues/potential/issue-00223.md) | Строка добычи не формирует штатные данные перетаскивания Item |
| [issue-00224](../../issues/potential/issue-00224.md) | Изображение добычи не связано с действием editImage |
| [issue-00225](../../issues/potential/issue-00225.md) | Перенос профессии в Loot обращается к отсутствующим навыкам |
| [issue-00226](../../issues/potential/issue-00226.md) | Пересчёт покупки зависит от script внутри HTML диалога |

Сопоставлены и дополнены [issue-00034](../../issues/potential/issue-00034.md), [issue-00039](../../issues/potential/issue-00039.md), [issue-00040](../../issues/potential/issue-00040.md), [issue-00063](../../issues/potential/issue-00063.md), [issue-00116](../../issues/potential/issue-00116.md), [issue-00136](../../issues/potential/issue-00136.md), [issue-00166](../../issues/potential/issue-00166.md), [issue-00168](../../issues/potential/issue-00168.md), [issue-00169](../../issues/potential/issue-00169.md), [issue-00206](../../issues/potential/issue-00206.md), [issue-00207](../../issues/potential/issue-00207.md), [issue-00208](../../issues/potential/issue-00208.md). Наблюдение 226 основано на вставке script через innerHTML и требует проверки чистого клиента; оно не описано как уже воспроизведённая браузерная ошибка. Raw Actor.name в строке выбора отмечен в карточке листа как неэкранированный HTML; инъекция/влияние на работу клиента не исследовались. Новые и прежние **226 карточек остаются potential**; подтверждения, исправления и закрытия отсутствуют.

### Формальная проверка документов

Проверка выполнена Python по рабочему дереву/Git и Markdown, с `git diff --check`. Реестр: 621 уникальный исходник, 278 карточек «Проверено», 343 «Не начат»; новые шесть файлов не пересекаются с прежними 272, а первые 31 файл серии — с базовыми 247. Проверены все 11 разделов новых карточек, собственные методы и name/data-field HBS.

Проверены 328 прямых импортов всех карточек (216 default, 105 named statements/110 имён, 7 namespace), определения export и обе стороны ссылок; 187 литеральных связей JS/HBS с шаблонами. В .035 добавились 4 импорта и 4 связи с HBS; для первых 31 файла проверены 15 импортов и 36 литеральных связей с HBS. Из прямых зависимостей первых 31 файла без полной карточки остаётся только rewardsSheet.js; сохранена граница dependency-only.

13 070 локальных ссылок и якорей прошли проверку во всех 578 Markdown (576 в docs плюс README/AGENTS). Таблицы и пробелы в изменённых документах проверены. Изменены 55 Markdown: 40 прежних и 15 новых (6 карточек и 9 issues). Перечень изменений совпал с согласованными материалами.

Все 621 исходника побайтно совпадают с HEAD `1d29f681ffed1c46b9c05b0eff09935300c3bf7d` и срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. SHA256 содержимого реестра: `52701d3d0a5f054319886ac2a9d45b42c26c80098858d02518579c6a1edfaec4`. mode/uid/gid/inode всех 1239 отслеживаемых файлов сохранены; SHA256 снимка метаданных: `8fc4f9e5e86f2061d07ffc8014225afb4ffcc8581c1d776404d2b6642b98df6d`. Историческая часть review-log, включая план .031–.040, сохранена побайтно. Исключённые пути и остаток .036–.040 без новых карточек проверены.

**Переход:** TASK-0003.035 выполнена, следующая — [TASK-0003.036](../../tasks/task-0003.036.md) (обмен валюты). TASK-0003 остаётся in-progress, .036–.040 planned, TASK-0004/TASK-0005 draft. Коммит не создавался.

## TASK-0003.034

Дата: 2026-09-11. Ветка `rusbar-main`, HEAD `7dbb31bdbd094f58c77c9e58dd5a684df6bb942c`; рабочее дерево на старте чистое, отслеживаются 1230 файлов. Основание — согласованная [TASK-0003.034](../../tasks/task-0003.034.md) и поручение пользователя продолжить.

### Состав и результат

Полностью прочитаны **пять файлов, 251 логическая строка**: три JS-примеси на 124 строки и два HBS на 127. Примеси вводят семь методов: getSubstance/findNeededComponent/findComponentByUuid, _prepareAlchemyComponentsList, canBeDismantled/dismantle/createDismantleMessage. Все вложенные callbacks поиска, разрешения и выдачи также разобраны.

| Файл | Строк | Карточка |
| --- | --- | --- |
| [module/actor/mixins/craftingMixin.js](../../../module/actor/mixins/craftingMixin.js) | 45 | [Описание](files/module/actor/mixins/craftingMixin.js.md) |
| [module/actor/sheets/mixins/alchemyMixin.js](../../../module/actor/sheets/mixins/alchemyMixin.js) | 15 | [Описание](files/module/actor/sheets/mixins/alchemyMixin.js.md) |
| [module/item/mixins/dismantlingMixin.js](../../../module/item/mixins/dismantlingMixin.js) | 64 | [Описание](files/module/item/mixins/dismantlingMixin.js.md) |
| [templates/partials/character/substances.hbs](../../../templates/partials/character/substances.hbs) | 106 | [Описание](files/templates/partials/character/substances.hbs.md) |
| [templates/chat/item/dismantle.hbs](../../../templates/chat/item/dismantle.hbs) | 21 | [Описание](files/templates/chat/item/dismantle.hbs.md) |

Добавлены пять карточек, уточнена 21 связанная. Покрытие выросло с 267 до **272 из 621 файла**, осталось **349**. В четвёртой серии выполнены 25 из 63 файлов, 38 стоят в очереди; ещё 311 требуют распределения. TASK-0003.001–.034 имеют done, .035–.040 planned; родительская задача in-progress, TASK-0004/TASK-0005 draft. Общая сверка первых 31 файла серии остаётся в .035, итоговая всех 63 — в .040.

### Методика и внешние границы

Node 24.16.0; установленная Foundry VTT 14.367.0 в /opt/foundryvtt. Проверки исполнены через `node --input-type=module` со stdin; постоянного стенда и тестовых файлов не создано. Настоящие craftingMixin/alchemyMixin/dismantlingMixin, WitcherActor/WitcherItem, WitcherCharacterSheet с базовым контекстом, itemMixin/itemContextMenu, CharacterData/ComponentData/DiagramData/WeaponData/CommonItemData и вложенные поля импортированы без правок исходников.

Для изготовления выполнены исходные _craftingCraft и callback, realCraft, extendedRoll, Roll/Peggy с управляемым кубиком. Handlebars 4.7.9 и системные helpers, настоящая Localization с expandObject en/ru использованы для рендера. Substances включает настоящие components и inventory-items-summary partial. getSpeaker исполнен из client/documents/chat-message.mjs; CONST из common/constants.mjs. Порядок callback(target,event) отдельно прочитан в client/applications/ux/context-menu.mjs:611–624; в этой порции core _onClickItem не исполнялся повторно, вызван настоящий системный entry с таким порядком.

Application/Document-оболочки, DOM/jQuery, диалоги, fromUuid/fromUuidSync, Actor/Item-записи и ChatMessage.create заменены фасадами. fromUuid возвращает объекты контролируемой карты, null или rejection. Для addItem использованы настоящие методы Actor; сериализация материала явно задана name/type/img/system.toObject, окончательная серверная нормализация ID/прав не воспроизводилась. createEmbeddedDocuments-фасад возвращает payload без пополнения коллекции, а проверка общей стопки отдельно обновляет настоящую модель через updateSource после управляемой задержки. Числа результата относятся к этой модели в памяти, не к действующей БД.

Первые сценарии выявили недостающий game.packs в окружении валидации DocumentUUIDField; добавлена пустая Map в фасад. Поле из common/data/fields.mjs:3399 осталось настоящим. _stats.compendiumSource (поле ядра:4039) задан на fixture вручную; процесс импорта компедиума не тестировался. После дополнения окружения итоговый запуск 21 группы прошёл. Предупреждение Node о неуказанном type пакета не является отказом проверок.

Мир, браузер, HTTP, действующие packs, несколько клиентов, отказ реальной записи и компенсация операции не запускались. Девять PNG проверены только на существование; связанные CSS-селекторы прочитаны как зависимости, ресурсы не получили карточек. Нормы разбора по книгам не устанавливались: max(1,floor(quantity/2)) зафиксирован как поведение кода. В самом dismantle нет диалога отмены; проверены остановка при отклонении UUID-запроса и отсутствие ожидания последующих операций.

### Изолированные сценарии

| № | Сценарий | Фактический результат | Пределы |
| --- | --- | --- | --- |
| 01 | Поиск вещества | Stored исключён, sort соблюдён; quantity0 остаётся; другой type/substanceType/регистр и неизвестный ключ не совпадают | Настоящие getList/getSubstance и ComponentData |
| 02 | Имя и количество | Два Iron вернулись в порядке коллекции, включая stored/0; iron и пробел не совпали; getOwnedComponentCount дал 3 | Применён настоящий helper/sum, не фильтр UUID |
| 03 | Локализованные вещества | Все девять веществ находятся по переводу имени в en и ru | Текущая локаль, не автоматическая поддержка иноязычного имени |
| 04 | UUID происхождения | Первый по sort с нужным _stats.compendiumSource; собственный Item.uuid не подходит; stored исключён | _stats задан фасадом; импорт компедиума не выполнялся |
| 05 | Алхимическая примесь | Девять key/label/image/count, значения 0…8; context неизменён; при {} count undefined; 9 PNG существуют | Потребителя alchemyComponentsList в module/templates не найдено |
| 06 | Панель веществ | Пустая: 9 иконок/нулей, 0 таблиц; полная: 9 открытых таблиц, 10 строк, vitriol 1+2=3, stored100 скрыт | Полный HBS, два настоящих partial; parse5 вместо браузера |
| 07 | Toggle и добавление | preventDefault, update vitriolIsOpen; после открытия add-item не содержит subtype, создаётся обычный component | Запись Actor/Item перехвачена; прежняя issue-00173 |
| 08 | Обычное изготовление | Настоящий callback/_craftingCraft/realCraft: требование 5, стопки 2 и stored4 → списания 2+3 и создание результата | Реальный Roll с управляемым кубиком; инвентарь/чат не записывались |
| 09 | Алхимическое изготовление | isFormulae=false/alchemyDC10 выбрал getSubstance; списано 2 вне хранения. Отдельный _alchemyCraft дал TypeError до Dialog | Прямой realCraft не доказывает работу блокированного интерфейса |
| 10 | Допуск и меню разбора | Weapon с UUID возвращает строку, без UUID — ''; component — false. Callback(target,event) даёт TypeError до resolve | Порядок аргументов прочитан в ядре; настоящий entry вызван с DOM/event-фасадами |
| 11 | Смешанный разбор | Требование 5 связанного Iron → 2, name-only 3 → 1; исходник 3→2. В чате два раздела, OTHER и Actor speaker | UUID/создание/удаление/чат подменены, имена экранирует настоящий HBS |
| 12 | Округление и запас | −2/0/1/2/3 → 1, 4/5 → 2, 6 → 3; исходная стопка 9 уменьшается до 8 | Алгоритм установлен по коду, не по книге правил |
| 13 | Недоступный рецепт | Null, пустой UUID и объект без craftingComponents дали TypeError; rejection резолвера передан наружу; записей не начато | Отказ внешнего API смоделирован |
| 14 | Недоступный компонент | UUID→null вернул {item:null,quantity:2}, потеряв Remembered; name-only сохранился. Исходник удаляется, выдачи нет | UUID API и удаление подменены |
| 15 | Пустые требования/отказ компонента | [] всё равно списывает источник и создаёт чат без разделов; rejection UUID компонента прерывает до записей | Нет собственного диалога отмены в dismantle |
| 16 | Нулевой/отрицательный источник | При quantity='0'/'-1' canBeDismantled остаётся truthy, выдаёт 2 компонента и удаляет источник | Допуск возвращает UUID, количество не читает; вызов напрямую |
| 17 | Порядок основной операции | dismantle вернул components при pending add/remove/render; порядок старта create→source-delete→render | После ручного разрешения появился чат; не серверная транзакция |
| 18 | Чат и обёртка | createDismantleMessage вернулся при pending ChatMessage.create; корректный прямой dismantleItem — при pending dismantle | Сбой обычного menu callback остаётся отдельным |
| 19 | Повторные требования | Два компонента по 2 для одной стопки=5 отправили update [7,7]; после разрешения в фасаде 7 | Настоящий addItem, отложенный Item.update; реальная гонка БД не проверена |
| 20 | Контракт HBS сообщения | Пустые массивы скрывают разделы; quantity987/654 не выводятся; found/unfound дают два заголовка | Наличие обязательного количества по правилам не оценивалось |
| 21 | Переводы и Object.assign | 12 основных ключей HBS/поиска существуют в en/ru; 3+3+1 метода прототипов совпадают с примесями | Другие локали и внешние потребители не исследованы |

### Перекрёстная сверка

- Три способа поиска сопоставлены с определениями getList, моделями Component/CommonItem, метаданными происхождения и всеми найденными вызовами. getSubstance/UUID-поиск исключают stored и сортируют, findNeededComponent этого не делает. Реальный внутренний вызов findComponentByUuid в module/templates не найден; метод не подменяет подбор ресурсов по имени.
- WitcherCharacterSheet._prepareSubstances формирует девять массивов/сумм через getSubstance/sum. alchemyMixin строит отдельный массив описаний, но шаблон substances его не читает. Полный контекст, девять элементов, флаги и вложенные таблицы сопоставлены с pannelsData и двумя partial.
- Контракт .item-substance-display/data-subtype доходит до _onSubstanceDisplay и preventDefault. Передача subtype в components/summary также есть, но кнопка add-item его не выводит — прежняя issue-00173. Регистр/пробелы имени и текущие локализованные названия проверены отдельно от UUID.
- Обычный ремесленный диалог и realCraft прослежены до двух списаний компонентов. Прямой алхимический realCraft выбирает getSubstance по alchemyDC независимо от isFormulae. Интерфейс _alchemyCraft по-прежнему прерывается на отсутствующем populateAlchemyCraftComponentsList; новый адаптер не добавлялся. Полный ремонт не запускался, только сверены его критерии и первый результат поиска.
- DismantlingMixin сопоставлен с Object.assign WitcherItem, Item/Weapon/Armor/Diagram-моделями, craftingComponent и associatedDiagramUuid. Все branches resolver/name-only/null/empty/rejection отделены. Значение количества исходника не участвует в выходе, списывается одна единица; canBeDismantled не проверяет запас и возвращает строку UUID.
- Found/unfound означают разрешение ссылки, а не завершённую выдачу. Сообщение выводит имя/иконку найденного и имя неизвестного, но не количество. Null-UUID теряет name/uuid раньше HBS; отдельный контекст листа рецепта из issue-00095 не смешан с этим producer.
- Порядок resolve → Promise.all → add/remove/message сопоставлен с ожиданием внутри Actor и отсутствием ожидания у caller. Pending-сценарии и два update=7 одной стопки отделены от непроверенной серверной гонки. Основной dismantle вызван напрямую: неисправный menu callback issue-00168 не исправлен и не объявлен работающим.
- Уточнена **21 прежняя карточка**: Actor/Item/Character/базовый лист, общие/компонентные/рецептные/оружейные модели и поля, pannels, itemMixin/контекстное меню, RepairSystem, Handlebars и четыре инвентарных HBS. Соседние файлы не засчитаны повторно в покрытие.

### Потенциальные проблемы

| ID | Наблюдение |
| --- | --- |
| [issue-00214](../../issues/potential/issue-00214.md) | Разбор предмета завершается до записей инвентаря и чата |
| [issue-00215](../../issues/potential/issue-00215.md) | Разбор предмета не проверяет доступность связанного рецепта |
| [issue-00216](../../issues/potential/issue-00216.md) | Недоступный компонент теряет имя в результате разбора |
| [issue-00217](../../issues/potential/issue-00217.md) | Разбор выдаёт материалы при нулевом запасе исходного предмета |

Четыре новые карточки зарегистрированы по пункту 9 TASK-0003, все potential. Дополнены [issue-00037](../../issues/potential/issue-00037.md), [issue-00038](../../issues/potential/issue-00038.md), [issue-00041](../../issues/potential/issue-00041.md), [issue-00095](../../issues/potential/issue-00095.md), [issue-00101](../../issues/potential/issue-00101.md), [issue-00104](../../issues/potential/issue-00104.md), [issue-00168](../../issues/potential/issue-00168.md), [issue-00173](../../issues/potential/issue-00173.md), [issue-00176](../../issues/potential/issue-00176.md). Старые сбои API/меню/режимов/подтипа не продублированы; в уточнениях прямо указано, какие прежние сценарии не повторялись. Всего **217 potential issues**, подтверждений пользователя, исправлений и закрытий нет.

### Формальная проверка и сохранность

Проверены все 621 строки реестра: 272 имеют полные карточки, 349 остаются «Не начат». Новая порция содержит ровно пять карточек; её семь методов сверены с определениями. Все 217 issues последовательно пронумерованы и остаются potential. У задач .001–.034 статус done, у .035–.040 planned; четвёртая серия содержит 25 разобранных и 38 запланированных файлов, ещё 311 вне очереди.

Проверены 12 717 локальных ссылок и якорей в 563 Markdown-файлах (561 в docs и два корневых документа). Сопоставлены 324 прямых импорта и 183 буквальные шаблонные связи описанных исходников с определениями и обратными упоминаниями; текущая порция не содержит импортов и добавляет две шаблонные связи. Девять вызовов одного components partial считаются одной связью файлов. Структура карточек и таблиц, состав изменений и git diff --check проверку прошли. При сверке исправлена лишняя колонка таблицы потребителей в карточке dismantlingMixin; исходник не менялся.

Изменены 50 Markdown-документов: 41 существующий и девять новых (пять карточек файлов, четыре issues). Содержимое всех 621 исходного файла совпадает с HEAD на старте и базовым срезом TASK-0001. Права, владельцы, группы и inode всех 1230 ранее отслеживаемых файлов сохранены. Историческая часть журнала совпадает с HEAD побайтово. Итоговый запуск 21 группы изолированных сценариев прошёл в указанных выше границах.

Изменения ограничены документацией. Следующая — [TASK-0003.035](../../tasks/task-0003.035.md), включая общую сверку .031–.035; её выполнение не начиналось. Исторические записи журнала сохранены.

## TASK-0003.033

Дата: 2026-09-11. Ветка `rusbar-main`, HEAD `12055fee62f01c6de49967044aedef9d7cfe0632`; рабочее дерево на старте чистое, отслеживаются 1223 файла. Основание — согласованная [TASK-0003.033](../../tasks/task-0003.033.md) и поручение пользователя продолжить.

### Состав и результат

Полностью прочитаны **четыре файла, 178 логических строк**: noteMixin — 25, NoteData — 16, tab-background — 129, note-sheet — 8. Примесь вводит три метода, класс — один собственный static defineSchema; программных функций в HBS нет.

| Файл | Строк | Карточка |
| --- | --- | --- |
| [module/actor/sheets/mixins/noteMixin.js](../../../module/actor/sheets/mixins/noteMixin.js) | 25 | [Описание](files/module/actor/sheets/mixins/noteMixin.js.md) |
| [module/data/item/noteData.js](../../../module/data/item/noteData.js) | 16 | [Описание](files/module/data/item/noteData.js.md) |
| [templates/partials/character/tab-background.hbs](../../../templates/partials/character/tab-background.hbs) | 129 | [Описание](files/templates/partials/character/tab-background.hbs.md) |
| [templates/sheets/item/note-sheet.hbs](../../../templates/sheets/item/note-sheet.hbs) | 8 | [Описание](files/templates/sheets/item/note-sheet.hbs.md) |

Добавлены четыре карточки, уточнены 25 связанных. Покрытие выросло с 263 до **267 из 621 файла**, осталось **354**. В четвёртой серии выполнены 20 из 63 файлов, 43 стоят в очереди; ещё 311 требуют распределения. TASK-0003.001–.033 имеют done, .034–.040 planned; родительская задача in-progress, TASK-0004/TASK-0005 draft. Общие сверки .035/.040 ещё предстоят.

### Методика и пределы проверки

Node 24.16.0; установленные исходники Foundry VTT 14.367.0 в /opt/foundryvtt. Сценарии исполнены через `node --input-type=module` со stdin; постоянный стенд и тестовый файл не создавались. Использованы настоящие NoteData/CommonItemData/CharacterData и вложенные схемы, noteMixin/itemMixin, WitcherCharacterSheet с полным базовым контекстом, методы Actor.getList и модели родины. V1 импортирован целиком поверх фасада ActorSheet для сопоставления прототипа и обработчиков, его регистрация в клиенте не утверждается.

Handlebars 4.7.9, core formGroup/editor/selectOptions, DataField.toFormGroup, HTMLField.toInput, FormDataExtended, _processFormData, Localization и методы _prepareTabs/_getTabsConfig исполнены из установленных исходников. Конкретные внешние источники: common/data/fields.mjs; client/applications/handlebars.mjs (editor:225); client/applications/ux/form-data-extended.mjs; client/applications/api/document-sheet.mjs и application.mjs; client/helpers/localization.mjs. Системные JS импортированы без изменения их файлов; тела отдельных функций ядра исполнены в vm.

Application/Document-оболочки, DOM/jQuery, createSelectInput/createFormGroup/HTMLProseMirrorElement.create и TextEditor.enrichHTML заменены фасадами; HTML разобран parse5. Для формы inputs/select/textarea получены из отрендеренной разметки, а значение prose-mirror — из перехваченных параметров editor с заданными правками. Это проверяет имена, преобразование формы и обновление модели, но не пользовательский ввод и внутреннюю работу ProseMirror. Item.create/update/delete и Actor.update заменены сборщиками/управляемыми Promise. updateSource применяется только к новым моделям в памяти, не к игровым документам.

Отрицательные/дробные индексы и счётчики заданы программно. Для lifeEventCounter исходный HTML имеет min=1,max=20; нормальная браузерная валидация/step не запускались. Пустой lifeEvents задан prepared-данным искусственно, не загружен как штатная запись схемы. Нет запуска мира, HTTP, службы, БД, одновременных клиентов и генераторов packsJson. CSS прочитан лишь по связанным селекторам, не получил карточки. Отдельная предыдущая проверка core _renderHTML в issue-00057 здесь не повторялась.

При подготовке сценария исправлена синтаксическая опечатка в fixture родины/пола; исходники системы не затронуты. После этого итоговый запуск всех 15 групп прошёл. Предупреждение Node о неуказанном type пакета не является отказом тестов.

### Изолированные сценарии

| № | Сценарий | Фактический результат | Пределы |
| --- | --- | --- | --- |
| 01 | NoteData | Восемь общих полей; description StringField, HTML-строка проходит roundtrip; quantity='2',weight=3 → вес 6; can*-геттеры false | Настоящие модели и поля, без Item-БД |
| 02 | Примесь и кнопки | Три метода совпадают с функциями V1/V2; bound .add-note добавляет запись; актуальный HBS не содержит .add-note, имеет .add-item | Регистрация jQuery смоделирована; кнопка добавления массива вызвана программно |
| 03 | Штатные операции массива | Добавление пустой записи; удаление первого/последнего/из пустого массива; source прежний при уже изменённом prepared | Actor.update перехвачен |
| 04 | Некорректный индекс | [A,B,C]: undefined/'bad' → [B,C], '-1' → [A,B], '1.5' → [A,C], '99' → исходный массив | Нештатные dataset переданы программно |
| 05 | Promise и отказ | Оба метода завершены при pending update; source прежний; отдельное отклонение update не возвращается через Promise метода | Отказ наблюдался отдельным catch; БД не запускалась |
| 06 | Смешанные заметки | Одна видимая Item-note и одна array-note; stored исключён, заголовки/textarea экранированы, editor получает raw details | Создание редактора — фасад; HTML-безопасность не исследована |
| 07 | Действия Item | Создание {name:'new note',type:'note'} с parent Actor; inline HTML-строка неизменна, false/true/checked преобразуются; удаление не меняет array-notes | Item.create/update/delete подменены |
| 08 | Старый note-sheet | Изолированный render: одна form, имя item.name, описание system.description; общий ItemSheet.PARTS пуст | Активный потребитель HBS не найден, submit не выполнялся |
| 09 | Родина/сведения/background | Семь inputs деталей; Item-родина заменяет select и otherValue; formGroup получает правильные raw/enriched background | enrichHTML и создание editor input заменены |
| 10 | Жизненные события | Две карточки с ключами 10/20, открытое поле 10, корректный toggle; повторный контекст сохраняет UI-ключи, prepared-схема нарушена как в issue-00024 | toObject() source неизменён; не сохранение искажённых данных в БД |
| 11 | V1 и границы counter | V1 toggle по исходному объекту; 0/1/20/21/−1/1.5 → 20/1/20/21/0/2 карточки; пустой prepared список → 0; у 21-й data-event='', toggle даёт TypeError | Программные значения; number min/max/step в браузере не проверены |
| 12 | Форма массива/переиндексация | FormDataExtended/_processFormData и updateSource сохраняют новые title/details второй записи; после удаления первой остаются пути notes.0.* | DOM и значения custom element заданы фасадом |
| 13 | Форма событий | Правка value события 10 сохраняется; скрытые details события 20 и details закрываемого события 10 остаются; в модели 20 ключей | Модель в памяти, без сервера |
| 14 | Регистрация V1/V2 | Оба activateListeners связали add/delete-note, add/delete-item, inline-edit и life-event-display; привязанный delete-note выполнен | Посторонние listeners заглушены; V1 не объявлен зарегистрированным UI |
| 15 | Переводы/разделение данных | 45 уникальных ключей найдены в en и ru после expandObject; два формата заметок не объединяются | Настоящий Localization; другие языки и генераторы не исследованы |

### Перекрёстная сверка

- noteMixin сопоставлен с двумя Object.assign и вызовами noteListener V2/V1. Текущие HBS имеют .delete-note, но не .add-note. .add-item/note, Item ID и data-field обрабатывает itemMixin; эти действия не преобразуют массив Actor.notes.
- NoteData сопоставлен с CommonItemData, registerDataModels и Item.note в system.json. Повторное description не меняет его тип StringField. Отдельный note-sheet не найден среди PARTS/template/render/partial/preload в module/templates; его имя формы item.name описано как требующее проверки при будущем подключении, не как текущая ошибка активного сохранения.
- oldNotes=getList('note') и notes=system.notes доведены до обоих each в tab-background и сравнены с ранее описанным monster-notes. Вложенный system.description корректно берётся у Item. Поля без name не входят в Actor-form; редакторы массива имеют индексные name/target. Их изменения и переиндексация после удаления проверены на модели.
- Все поля биографии сопоставлены с generalData, details/background/homeland/lifeEvents/lifeEvent и CharacterData. Родина Item заменяет редактируемую родину Actor только в представлении. Семь details подписей и варианты двух конфигурационных словарей проверены вместе с прямыми ключами.
- Цепочка createEnrichedText → CharacterData.enrichedText → formGroup передаёт корректный background raw/enriched. Для notes.details вызывается editor с исходной строкой; вызова enrichHTML на массивных заметках в этом пути нет. Реальная безопасность/обработка произвольного HTML не утверждается.
- У событий UI-key 10/20 отличается от индекса массива и поля decade. V1 toggle использует объект, V2 — find по key. Повторная подготовка сохраняет UI-ключи, но не исправляет нарушение prepared-схемы из issue-00024. Скрытые поля сохраняются при частичной правке; counter не удаляет события.
- Уточнены **25 прежних карточек**: базовые листы, Character/Monster/Item-листы, Actor/getList и itemMixin; CommonActor/Character/общие заметки, general и его пять вложенных схем; CommonItem/Homeland/dataUtils; config/регистрации/Handlebars/манифест и monster-notes. Исходники соседей проверены в пределах связей и не засчитаны повторно. Исторические ограничения дополнены результатами .033.

### Потенциальные проблемы

| ID | Наблюдение |
| --- | --- |
| [issue-00211](../../issues/potential/issue-00211.md) | Методы массива заметок завершаются до сохранения изменений |
| [issue-00212](../../issues/potential/issue-00212.md) | Удаление заметки не проверяет индекс перед splice |
| [issue-00213](../../issues/potential/issue-00213.md) | Счётчик событий выше длины списка создаёт пустые карточки |

Три новые карточки зарегистрированы по пункту 9 TASK-0003, все potential. Дополнены [issue-00024](../../issues/potential/issue-00024.md), [issue-00057](../../issues/potential/issue-00057.md), [issue-00153](../../issues/potential/issue-00153.md). Наблюдения искажённого prepared lifeEvents, пустого отдельного листа note и преобразования текстов false/true не продублированы. Всего **213 potential issues**, подтверждений пользователя, исправлений и закрытий нет.

### Формальная проверка и сохранность

Проверены все 621 строки реестра: 267 имеют полные карточки, 354 остаются «Не начат». Состав текущей порции — ровно четыре новых карточки. В каталоге issues — 213 последовательно пронумерованных документов, все potential; у задач .001–.033 статус done, у .034–.040 planned. Четвёртая серия содержит 20 разобранных и 43 запланированных файла, вне очереди остаются 311.

Проверены 12 507 локальных ссылок и якорей в 554 Markdown-файлах (552 в docs и два корневых документа). Сопоставлены 324 прямых импорта и 181 буквальная шаблонная связь описанных исходников с определениями и обратными упоминаниями в карточках; текущая порция добавила один прямой импорт, новых буквальных шаблонных связей нет. Структура карточек и таблиц, статусы, точный перечень изменённых документов и git diff --check проверку прошли.

Изменены 46 Markdown-документов: 39 существующих и семь новых (четыре карточки файлов, три issues). Содержимое всех 621 исходного файла совпадает с HEAD на старте и базовым срезом TASK-0001. Права, владельцы, группы и inode всех 1223 ранее отслеживаемых файлов сохранены; историческая часть журнала совпадает с HEAD побайтово. Итоговые 15 групп изолированных сценариев прошли в указанных выше границах.

Изменения ограничены документацией. Следующая — [TASK-0003.034](../../tasks/task-0003.034.md), её выполнение не начиналось. Исторические записи журнала сохранены.

## TASK-0003.032

Дата: 2026-09-11. Ветка `rusbar-main`, HEAD `8b938d44a042749df027d8b58e28bb1d79638091`; рабочее дерево на старте чистое, отслеживаются 1205 файлов. Основание — согласованная [TASK-0003.032](../../tasks/task-0003.032.md) и поручение пользователя продолжить.

### Состав и результат

Полностью прочитаны **13 файлов, 973 логические строки**: WitcherMonsterSheet — 224, WitcherMonsterConfigurationSheet — 91, одиннадцать HBS — 658. У классов 8 собственных методов, внутри экспорта 2 callback. Старый monster-details-tab содержит четыре пустые строки; его разбор завершён, а не пропущен. Все текущие и старые шаблонные маршруты указаны отдельно.

| Файл | Строк | Карточка |
| --- | --- | --- |
| [module/actor/sheets/WitcherMonsterSheet.js](../../../module/actor/sheets/WitcherMonsterSheet.js) | 224 | [Описание](files/module/actor/sheets/WitcherMonsterSheet.js.md) |
| [module/actor/sheets/configurations/WitcherMonsterConfigurationSheet.js](../../../module/actor/sheets/configurations/WitcherMonsterConfigurationSheet.js) | 91 | [Описание](files/module/actor/sheets/configurations/WitcherMonsterConfigurationSheet.js.md) |
| [templates/sheets/actor/partials/monster/header.hbs](../../../templates/sheets/actor/partials/monster/header.hbs) | 42 | [Описание](files/templates/sheets/actor/partials/monster/header.hbs.md) |
| [templates/sheets/actor/partials/monster/sidebar.hbs](../../../templates/sheets/actor/partials/monster/sidebar.hbs) | 154 | [Описание](files/templates/sheets/actor/partials/monster/sidebar.hbs.md) |
| [templates/sheets/actor/partials/monster/tabs/tab-details.hbs](../../../templates/sheets/actor/partials/monster/tabs/tab-details.hbs) | 18 | [Описание](files/templates/sheets/actor/partials/monster/tabs/tab-details.hbs.md) |
| [templates/sheets/actor/partials/monster/tabs/partials/monster-info.hbs](../../../templates/sheets/actor/partials/monster/tabs/partials/monster-info.hbs) | 22 | [Описание](files/templates/sheets/actor/partials/monster/tabs/partials/monster-info.hbs.md) |
| [templates/sheets/actor/partials/monster/tabs/partials/monster-knowledge.hbs](../../../templates/sheets/actor/partials/monster/tabs/partials/monster-knowledge.hbs) | 23 | [Описание](files/templates/sheets/actor/partials/monster/tabs/partials/monster-knowledge.hbs.md) |
| [templates/sheets/actor/partials/monster/tabs/partials/monster-notes.hbs](../../../templates/sheets/actor/partials/monster/tabs/partials/monster-notes.hbs) | 22 | [Описание](files/templates/sheets/actor/partials/monster/tabs/partials/monster-notes.hbs.md) |
| [templates/sheets/actor/partials/monster/tabs/partials/monster-status.hbs](../../../templates/sheets/actor/partials/monster/tabs/partials/monster-status.hbs) | 14 | [Описание](files/templates/sheets/actor/partials/monster/tabs/partials/monster-status.hbs.md) |
| [templates/sheets/actor/configuration/monster/header.hbs](../../../templates/sheets/actor/configuration/monster/header.hbs) | 3 | [Описание](files/templates/sheets/actor/configuration/monster/header.hbs.md) |
| [templates/sheets/actor/configuration/monster/general.hbs](../../../templates/sheets/actor/configuration/monster/general.hbs) | 22 | [Описание](files/templates/sheets/actor/configuration/monster/general.hbs.md) |
| [templates/sheets/actor/monster-sheet.hbs](../../../templates/sheets/actor/monster-sheet.hbs) | 334 | [Описание](files/templates/sheets/actor/monster-sheet.hbs.md) |
| [templates/partials/monster/monster-details-tab.hbs](../../../templates/partials/monster/monster-details-tab.hbs) | 4 | [Описание](files/templates/partials/monster/monster-details-tab.hbs.md) |

Добавлены 13 карточек, уточнена 31 связанная. Покрытие выросло с 250 до **263 из 621 файлов**, осталось **358**. В четвёртой серии .031/.032 выполнены 16 из 63 файлов, 47 стоят в очереди; 311 ещё требуют распределения. TASK-0003.001–.032 имеют done, .033–.040 planned; родительская задача in-progress, TASK-0004/TASK-0005 draft. Общие сверки .035/.040 ещё предстоят.

### Методика и внешние границы

Node v24.16.0, установленная Foundry VTT 14.367.0 в /opt/foundryvtt. Сценарии выполнены через `node --input-type=module` со stdin; постоянного стенда/тестового файла не создано. Исходники не менялись, мир и серверные операции не запускались.

Настоящие MonsterData/CommonActorData, вложенные схемы, WitcherMonsterSheet, WitcherMonsterConfigurationSheet и общий WitcherActorSheet импортированы целиком. У Actor выполнены реальные getList/числовые методы/обёртка локаций, у Item — checkIfItemHasRollTable. Foundry DataField.toFormGroup, Handlebars 4.7.9, core formGroup/editor/selectOptions/not, FormDataExtended/_processFormData, Localization и Roll/Peggy использованы из установленного ядра. _prepareTabs/_getTabsConfig также выполнялись из настоящих тел core Application. Для единственной группы конфигурации tabs подготавливает базовый API: отсутствие отдельного вызова в самой конфигурации не является ошибкой.

Application/Document-оболочки и состав базового document-context смоделированы по core document-sheet.mjs: 172–183. DOM/jQuery, createInput/createFormGroup/HTMLProseMirrorElement.create, TextEditor.enrichHTML и окна заменены фасадами. В изолированном экспорте actor.toObject возвращает контролируемую полную сериализацию; Folder.create/Actor.create возвращают объекты fixture, Item.update и сообщения перехвачены. Это проверяет payload и последовательность метода, не серверную нормализацию ID/прав/схем и не поведение реального каталога. В отдельной группе 22 pack/Item.create/чат также подменены и не пополняют коллекцию автоматически.

Константа типов папок импортирована из настоящего common/constants.mjs: 542: первый элемент ActiveEffect, второй Actor. Права создания не выводятся из отсутствия проверки в action: common/documents/actor.mjs: 112 использует hasPermission('ACTOR_CREATE'); UI/серверная авторизация не запускались. DialogV2 использует форму с submit и rejectClose; отрицательный множитель не ограничен min, дробный 1.5 в тесте передан программно. Нативный шаг number-input и окончательная валидация браузера не проверены.

Предупреждение core formGroup о несуществующем поле в группе 03 ожидаемо для commonspeech (issue-00004); это не незавершённый тест. При подготовке фасада были уточнены значения схемы и API: семь primary вкладок, isVisible=false, 10/13 полей конфигурации, custom resolve = 80, ID stun, core HTMLProseMirrorElement/not. Эти изменения относились только к тестовому окружению. Итоговый запуск всех 25 групп прошёл.

### Изолированные сценарии

| Группа | Что проверено | Результат | Пределы |
| --- | --- | --- | --- |
| 01 | Полный контекст/класс | 10 PARTS; группы 7/9/6/2; configuration того же Actor; totalStats отсутствует при расчётной сумме 72 | Настоящие super+child и модели; базовый Application-контекст фасад |
| 02 | Профессия/добыча | Первый нестored profession по sort; 9 типов loots, без stored, weapon/armor; enriched профессии не готовится | Часть legacy item types задана сырыми fixture, не валидирована как разрешённые типы мира |
| 03 | Настройка навыков | 52 записи/51 поле; commonspeech undefined; awareness true→false отражён повторной подготовкой | Настоящие schema/getField/formGroup; DOM input фасад |
| 04 | Форма конфигурации | 10 input без customStat, 13 с ним; bool и три max переданы через FormDataExtended/_processFormData в MonsterData.updateSource | Сам Document.update и сохранение сервера не запускались |
| 05 | Обычные/пользовательские ресурсы | При BODY/WILL8 обычный HP40; customStat сохраняет HP90/STA70/resolve80 | Настоящие числовые методы; lifecycle Actor вызван вручную по проверенной цепочке |
| 06 | Заголовки и подписи | <Name> экранирован; Vampire/hard/complex переведены; один name input; verbal-button условен; configuration header локализован | Рендер без браузера; наличие редакторов проверено поиском всей разметки |
| 07 | Sidebar | HP120/toxicity−2/armorTailWing9 в payload; 12 полей с resolve, без luck/adrenaline; 12 актуальных category src существуют | FormDataExtended и DOM фасад; assets проверены только на наличие |
| 08 | Иконка HP | 40/60/base40→целая; 35/35/base40→треснувшая | Повторный контракт issue-00203, без изменения игровых правил |
| 09 | Общие сведения | Пять StringField-путей; <weight> экранирован в HTML, payload строковый | Не масса Item и не проверка записи БД |
| 10 | Знания | Три HTMLField и 3 порога; visibility false скрывает; enriched параметр получает raw @UUID, producer имел отличающийся HTML | enrichHTML и HTMLProseMirrorElement.create фасады; методы моделей/formGroup настоящие |
| 11 | Заметки | Item textarea корректно читает текущий each.system.description; 2 array notes, add-item вместо add-note; удаление 0 оставляет Second | Item add/editor-save в браузере не выполнялись; noteDelete update перехвачен |
| 12 | Статусы | Четыре текстовых input, multi-select с 26 опциями, stun выбран | Core selectOptions; custom element не запускался, applyStatus не выполнялся |
| 13 | Сборка details/старый пустой partial | Одна nav, 4 полных partial; старый details trim/read/render пуст; старый общий HBS компилируется | Core _prepareTabs/_getTabsConfig реальные; переключение вкладок не проверено в DOM |
| 14 | Listeners/конфигурации | configure/death наследуются; item-repair/saveIpSpending отсутствуют; конфигурация и openModifiers открываются | jQuery/DOM/contextMenu и render фасады; действие openModifiers настоящее |
| 15 | Папка экспорта | CONST.FOLDER_DOCUMENT_TYPES[0]=ActiveEffect; Actor-папка нужного имени пропущена, запрошена ActiveEffect; существующая ActiveEffect найдена | Настоящая константа и метод; Folder.create подменён |
| 16 | Пустой/повторный экспорт | Два экспорта дают два вызова Actor.create; type/name/folder заменены, effects/ownership/flags/_id в payload сохранены | Полная сериализация Actor задана fixture, окончательное поведение создающей подсистемы ядра не воспроизводилось |
| 17 | Фиксированные количества/состав | Множитель 2: 0/1/3→0/2/6; weapon и note также скопированы и умножены; исходная сериализация не меняется | Actor/create/update фасады, не реальная запись |
| 18 | Количество формулой | Два настоящих Roll('1d6') с 2/3 дают 5 | Управляемая генерация кубиков и запись Item; async завершение дождались отдельно в тесте |
| 19 | Множители | '-2': qty2→−4, 1d6→0; 0/пусто→0; программное 1.5: qty2→3, 1d6→два броска 2+3=5 | Прохождение дробного ввода через native step не утверждается; отрицательное значение не ограничено min |
| 20 | Ожидание экспорта | Отдельно удержаны table Promise/update Promise; action и render завершены раньше, qty ещё 3; после разрешения 6 | Управляемые задержки, без многоклиентных гонок |
| 21 | Генератор/отмена | true от checkIfItemHasRollTable исключает обычный update; отклонение prompt не создаёт Actor/Folder | Результат генератора подменён; штатная ошибка dismiss прочитана в DialogV2 |
| 22 | Настоящий Item-генератор | Без pack→false; один pack/один результат на итерацию, quantity2→два запроса Item.create, два сообщения и удаление генератора | Pack/Item.create/chat подменены; create не пополняет коллекцию fixture, поэтому накопление существующей стопки не проверяется |
| 23 | Старый полный HBS | Render всех 334 строк с настоящими partial/core not; редакторы 4 полей есть, readonly stat value; 11 из 12 category src отсутствуют | Активный потребитель старого HBS не найден; HTTP и браузер не запускались |
| 24 | Видимость/локации/сумма | Текущий awareness anchor есть при isVisible=false; hasTailWing true: wrapper без tailWing, static.call(actor) с tailWing; totalStats нет | Настоящие методы/шаблон; полный бой не выполнялся |
| 25 | Локализация | 67 полных ключей и 2 префикса; все 67 есть в en, в ru отсутствуют лишь 4 прежних ignore/ignoreHint | Настоящий Localization и expandObject/fallback; остальные языки не исследованы |

### Перекрёстная сверка исходников и карточек

- Регистрация makeDefault monster сопоставлена с полным WitcherMonsterSheet: три прямых default-import и 9 системных PARTS. Десятая часть — core generic/tab-navigation. ConfigurationSheet не зарегистрирован самостоятельным листом: создаётся полем configuration и открывается базовым _renderConfigureDialog.
- Конфигурация связывает statMap/skillMap со схемой и BooleanField.isVisible, передаёт statLabels по общей ссылке CONFIG.WITCHER. Общий шаблон навыков и его IP-часть не становятся корректными для Monster от наличия конфигурации; прежние issue-00018/00030/00192 сохранены.
- Current header/sidebar/details и четыре partial сведены с MonsterData/CommonActorData. В header только name input и текстовая классификация. Sidebar использует toxicity из stats, ресурсы из derivedStats, 4 поля брони и 2 ignored; luck/adrenaline отсутствуют. general конфигурации даёт 10/13 input, 3 visibility-флага и боевые опции; реальные потребители флагов найдены, полный бой не выполнялся.
- Связь createEnrichedText→MonsterData.enrichedText→MonsterSheet→monster-knowledge доведена до настоящего HTMLField.toInput: HBS передаёт raw value в enriched. notes/oldNotes различены; {{system.description}} внутри each oldNotes корректно читает Item, а не Actor. Статусы используют известный ID stun и 26 опций.
- Экспорт не использует context.loots как фильтр: передаёт полный actor.toObject, меняет type/name/folder и обрабатывает все Items. Тип Folder/порядок Promise/обычные и формульные количества сопоставлены с core константой, Roll и Item-генератором. Прежняя проблема накопления общей стопки не выдана за повторно проверенную новой выдачей двух Item.
- Старый monster-sheet.hbs и пустой monster-details-tab найдены в предзагрузке; действующего template-потребителя старого полного HBS в module/templates не найдено. Пять его partial существуют и рендерятся в изоляции; непроцитированный путь effect-part допустим для Handlebars. Сведения/бонусы/иконки старого маршрута не приписаны текущему V2.
- Сверены ресурсы вне покрытия: все 12 текущих динамических иконок существуют; 11 старых plural-путей отсутствуют. Картинки не анализировались и не получили карточек. CSS прочитан по нужным селекторам, внешнее представление браузера не проверено.
- Уточнена **31 прежняя карточка**: базовые листы, Actor/Item/Loot/Monster/CommonActor/общие поля и dataUtils; config/registerSheets/handlebars/settings; stat/death/item/skill-примеси и WitcherModifiersConfiguration; общие/старые вкладки навыков/инвентаря/эффектов. У базового листа снято ограничение о непрочитанном полном Monster; полный Loot остаётся .035.

### Потенциальные проблемы

| ID | Наблюдение |
| --- | --- |
| [issue-00206](../../issues/potential/issue-00206.md) | Экспорт добычи выбирает тип папки ActiveEffect вместо Actor |
| [issue-00207](../../issues/potential/issue-00207.md) | Экспорт добычи завершается до пересчёта количества предметов |
| [issue-00208](../../issues/potential/issue-00208.md) | Экспорт добычи допускает отрицательный множитель количества |
| [issue-00209](../../issues/potential/issue-00209.md) | Текущий лист монстра не предлагает редактировать категорию и оценку угрозы |
| [issue-00210](../../issues/potential/issue-00210.md) | Старый шаблон монстра ссылается на отсутствующие изображения категорий |

Новые пять карточек зарегистрированы по пункту 9 TASK-0003; все potential. Дополнены 16 прежних: [issue-00004](../../issues/potential/issue-00004.md), [issue-00013](../../issues/potential/issue-00013.md), [issue-00015](../../issues/potential/issue-00015.md), [issue-00018](../../issues/potential/issue-00018.md), [issue-00030](../../issues/potential/issue-00030.md), [issue-00031](../../issues/potential/issue-00031.md), [issue-00032](../../issues/potential/issue-00032.md), [issue-00039](../../issues/potential/issue-00039.md), [issue-00040](../../issues/potential/issue-00040.md), [issue-00167](../../issues/potential/issue-00167.md), [issue-00177](../../issues/potential/issue-00177.md), [issue-00180](../../issues/potential/issue-00180.md), [issue-00192](../../issues/potential/issue-00192.md), [issue-00199](../../issues/potential/issue-00199.md), [issue-00203](../../issues/potential/issue-00203.md), [issue-00205](../../issues/potential/issue-00205.md). Наблюдения sidebar HP/переводов дополнены в существующих issue-00203/00205, дубликаты не создавались. Всего **210 potential issues**, подтверждений пользователя, исправлений и закрытий нет.

### Формальная проверка и сохранность

Проверены все 621 строки реестра: 263 имеют полные карточки, 358 остаются «Не начат». В этой порции добавлены 13 карточек; в каталоге issues находятся 210 документов со статусом potential. Состав четвёртой серии согласован с задачами: 63 файла, из них 16 разобраны, 47 запланированы; ещё 311 файлов требуют распределения.

Проверены 12 329 локальных ссылок и якорей в 547 Markdown-файлах (545 в docs и два корневых документа). Для описанных исходников сверены 323 прямых импорта и 181 буквальная шаблонная связь; текущая порция добавляет три импорта и 21 шаблонную связь. Проверки структуры таблиц, статусов задач, точного состава карточек, реестра и git diff --check прошли.

Изменены 76 Markdown-документов: 58 существующих и 18 новых (13 карточек файлов и пять issues). Содержимое всех 621 исходного файла совпадает с состоянием до анализа; права, владельцы, группы и inode всех 1205 ранее отслеживаемых файлов сохранены. Историческая часть журнала совпадает с HEAD побайтово. Итоговые 25 групп изолированных сценариев выполнены успешно в указанных выше границах.

Изменения ограничены документацией. Следующая — [TASK-0003.033](../../tasks/task-0003.033.md), её выполнение не начиналось. Исторические записи журнала сохранены.

## TASK-0003.031

Дата: 2026-09-11. Ветка `rusbar-main`, HEAD `928ce4e537c6a3fdc34f8b6fa3fcfdb5a669f68d`. На старте рабочее дерево чистое, отслеживаются 1196 файлов. Основание — согласованная [TASK-0003.031](../../tasks/task-0003.031.md) и поручение пользователя продолжить.

### Состав и результат

Полностью прочитаны три файла, 711 логических строк: весь WitcherCharacterSheet (481), character-header.hbs (69) и character/sidebar.hbs (161). Подготовлены три полные карточки:

| Исходник | Карточка |
| --- | --- |
| [module/actor/sheets/WitcherCharacterSheet.js](../../../module/actor/sheets/WitcherCharacterSheet.js) | [Описание](files/module/actor/sheets/WitcherCharacterSheet.js.md) |
| [templates/partials/character-header.hbs](../../../templates/partials/character-header.hbs) | [Описание](files/templates/partials/character-header.hbs.md) |
| [templates/sheets/actor/partials/character/sidebar.hbs](../../../templates/sheets/actor/partials/character/sidebar.hbs) | [Описание](files/templates/sheets/actor/partials/character/sidebar.hbs.md) |

Класс разобран целиком: 17 собственных методов, два вложенных Craft callback, поле rewards, uniqueTypes, DEFAULT_OPTIONS/PARTS/TABS и Object.assign alchemyMixin. Ремесленные вычисления не отложены до .034; эта порция позже сверит контракты соседей. Раса/профессия присутствуют в заголовке и контексте, не в sidebar: предположение краткого плана уточнено по полному исходнику.

Покрытие выросло с 247 до **250 из 621 файла**, остаток — **371**. TASK-0003.001–.031 имеют done, .032–.040 — planned; в четвёртой серии 3 из63 проверены, 60 в очереди, ещё 311 исходников без конкретных подзадач. TASK-0003 остаётся in-progress, TASK-0004/TASK-0005 — draft. Общие сверки .035/.040 ещё не наступили.

### Среда и пределы воспроизведения

Node v24.16.0, локальная Foundry VTT 14.367.0 в /opt/foundryvtt. Команда — `node --input-type=module` со сценарием через stdin; постоянный тестовый стенд/файл не создавался. Запуск не подключался к миру и не записывал игровые документы.

Использованы настоящие DataModel/TypeDataModel/fields/utils Foundry и модели системы; WitcherCharacterSheet и базовый WitcherActorSheet импортированы целиком. Методы прототипов Actor/Item и примесей исполнялись на контролируемых документах. Настоящие Roll, dice и Peggy проверяли формулы при управляемых результатах d10; Handlebars 4.7.9 и parse5 — шаблоны/HTML5. FormDataExtended и метод core DocumentSheet._processFormData использованы для payload, настоящий Localization — для en/ru после expandObject.

Границы Application/Document, _prepareTabs, Dialog, DOM/jQuery и окна конфигурации заменены фасадами; TextEditor.enrichHTML выдаёт контролируемое обогащение. UUID resolver работает по карте fixture, запись Actor/Item и отправка ChatMessage перехвачены. Контекстное меню отключено для узкой проверки listeners. Это не запуск листа в браузере и не проверка записи БД, HTTP-доступа, нескольких клиентов или внешних модулей.

Штатная алхимия и условные ветви разделены: группа12 использует неизменённый вход и фиксирует отсутствующий метод. Только группы13–15 добавляют в fixture адаптер populateAlchemyCraftComponentsList к существующему getter, чтобы исследовать остальной callback. Код системы не исправлялся. Свежие label=undefined рассмотрены в группе23; обычные броски используют модель после повторного создания из toObject, заполняющего label миграциями.

Для локализации используется реальный string fallback ядра: объект на пути префикса не считается переводом. При проверке max99 прочитан core application.mjs:2134–2161: onchange идёт в _onSubmitForm без checkValidity; поэтому буквальный HTML-атрибут не объявлен доказанным ограничением сохранения. Группа25 проверяет только разбор данных и updateSource.

### Изолированные сценарии

Все **26 групп** выполнены; 01–25 прошли единым запуском с настоящим Localization, 26 проверена отдельно. Нумерация ниже соответствует проверкам. Ожидаемые ошибки — явные assert.rejects/assert.throws, не неудачный прогон.

| Группа | Сценарий | Результат | Ограничения |
| --- | --- | --- | --- |
| 01 | Класс, DEFAULT_OPTIONS, PARTS, TABS и действия | 10 PARTS, группы 7/9/6; uniqueTypes=profession/race/homeland; RewardsSheet получает Actor; два приватных action пустые, openModifiers получает тип/ключ | Настоящий класс; базовые Application и окна конфигурации заменены |
| 02 | Полный контекст super+child и повторная подготовка | Девять max8 дают totalStats72, totalSkills/totalProfSkills=0; 20 lifeEvents становятся массивом; toObject(false).10 читает прежнее событие110, _source неизменён | Настоящие модели/методы; это подготовленные данные, не БД |
| 03 | Уникальные Item и обогащение | Раса с меньшим sort выбрана первой, stored исключён; homeland/profession переданы, вызываются модели enrichedText расы/профессии и Character | Настоящие модели; enrichHTML возвращает контролируемый HTML |
| 04 | Классификация рецептов | 15 значений type и отдельный stored Item; 13 именованных групп, unknown остаётся только в diagrams | Заполнение групп по type, отдельно от режима isFormulae |
| 05 | Материалы, алхимия, ценности | Сверены component/alchemical/valuable/mount и подтипы, в том числе старые genera/пустой type; mutagen — отдельный Item type | Часть устаревших подтипов задана raw записями, не объявлена прошедшей валидацию |
| 06 | Вещества и количество | Настоящие getSubstance и Array.sum: 2+3=5, stored99 исключён; пустой список0; raw quantity='bad' даёт NaN | Последнее — программный некорректный вход, не сохранённая модель |
| 07 | Пробное ремесло с подробностями и диаграммой | CRA4+crafting3+модификатор1+d10=5: 13; галочка диаграммы даёт15; подробный и краткий режимы проходят, записей инвентаря нет | Настоящие extendedRoll/Roll/парсер; подходящий именованный эффект присутствует |
| 08 | Неуспех, равенство DC и отсутствие выбора | 9 и10 при DC10 неуспешны; без вызова Craft после открытия диалога нет броска/записей | Нажатие Cancel в браузере не моделировалось; callback Cancel в конфигурации отсутствует |
| 09 | Нехватка компонентов и пустой associatedItem | Требуется3, запас0: при realCraft=true и пустой связи TypeError до уведомления; при связанной вещи одно уведомление | Сам callback настоящий; UI/UUID resolver перехвачены |
| 10 | Настоящий realCraft обычного рецепта | Требуется2, запас3: total10 при DC10 без расхода; total12 вызывает списание2 и выдачу resultQuantity2; одно сообщение на ветку | Actor.removeItem/addItem и сообщение перехвачены; вложенный realCraft дождались отдельно в тесте |
| 11 | Ожидание изготовления | Craft callback завершается, пока подменённый realCraft удерживает Promise | Проверка контракта ожидания, не серверной гонки |
| 12 | Штатный вход алхимии | Настоящий _alchemyCraft падает на отсутствующем populateAlchemyCraftComponentsList до создания Dialog; getter alchemyCraftComponentsList есть | Никакого адаптера в этой группе нет |
| 13 | Остальной алхимический callback | CRA4+alchemy2+модификатор1+d10=5+диаграмма2=14 в обоих режимах подробностей | Явный адаптер populate...→getter только в fixture; штатный вход блокирует issue-00037 |
| 14 | Неалхимический fallback из _alchemyCraft | При alchemyDC0 берётся crafting3, но остаются алхимические порог0/модификатор2/имя; total14 вместо использования crafting-модификатора7 | Условный callback после того же адаптера |
| 15 | Алхимические нехватка и передача realCraft | Требование vitriol2 без запаса/связи даёт ошибку, со связью — уведомление; достаточная ветка делегирует realCraft | Условный callback; полноценный расход алхимии здесь не воспроизводился |
| 16 | Списание IP с настоящим Log | Из10 ввод '3' даёт7, '-3' даёт '10-3', '0' сохраняет10; CharacterData.updateSource отвергает '10-3'; 'bad' даёт NaN | Запись Actor перехвачена; строка bad задана программно |
| 17 | Ремонт и награды | _repairItem ждёт held Promise item.repair; _addIpReward не ждёт Actor wrapper; _renderRewards вызывает render | Соседние операции заменены; сам ремонт не повторно тестировался |
| 18 | Полные listeners super+child | Шесть собственных click-селекторов, базовые обработчики и death-roll зарегистрированы; глобальная jQuery заменяется объектом | jQuery/DOM и itemContextMenu заменены; не реальная повторная привязка |
| 19 | Заголовок, родина и кнопки | HTML в имени экранирован; отдельный homeland.system.value/otherValue заменяет legacy general.homeland; verbal-button условна | Настоящий Handlebars, подготовленный контекст |
| 20 | Восстановление незакрытого <a> | parse5 создал три open-rewards: с иконкой в improvement-points, пустую в char-actions, пустую в death-section | Пустые ссылки не содержат счётчик смертей; геометрия/клики браузера не проверены |
| 21 | Боковая панель и значения формы | Переданы HP120, STA−2, luck−1 и bool-флаг; HP max=99 буквальный; vigor0 скрыт, −1 виден; useAdrenaline/useVerbalCombat управляют блоками | Подготовленные значения; это не подтверждение разрешения всех отрицательных значений моделью |
| 22 | Сердце и текущий максимум | HP40/max60/base40 — целое; HP35/max35/base40 — треснувшее; HP7/threshold8 — оранжевое | Проверка представления, не новое правило ранения |
| 23 | Свежие label и пустые lifeEvents | У свежей CharacterData label undefined; Craft падает на replace. Искусственно пустой prepared lifeEvents/counter0 даёт []/0 | Основные броски используют повторную модель с мигрированными label; реальный create Actor не проверен |
| 24 | Ненулевой модификатор без подписи | activeEffectModifiers1/appliedEffects[]/подробности включены → +1[] → ошибка настоящего парсера Roll | Источник такого несогласованного Actor в мире не установлен |
| 25 | Настоящий разбор формы и модель | FormDataExtended и core _processFormData передают name, HP120 и оба healthState.*.ignored; CharacterData.updateSource принимает HP120 | DOM заменён; настоящий Document.update/БД/native validation не запускались |
| 26 | Локализация после раскрытия ключей | 52 строки: 49 полных ключей, три префикса; все49 есть в en, четыре ignore/ignoreHint отсутствуют в ru; en fallback доступен | Настоящие словари expandObject и Localization; префиксы не считаются отсутствующими переводами |

### Перекрёстная сверка

- Сверены семь прямых импортов класса (четыре default, три named), определения экспортов, назначение makeDefault в registerSheets и унаследованный _onRender→activateListeners.
- Все девять системных HBS из PARTS сопоставлены с данными/действиями; десятая часть — core generic/tab-navigation. В preload присутствует header, sidebar выбирается непосредственно PARTS. Новые две HBS прочитаны целиком; ещё не описанные вкладки просмотрены по контракту.
- getList/items/isStored/sort связаны с реальными фильтрами и моделями Item, все13 групп рецептов и девять веществ перечислены. Алхимический Item type mutagen не подменён названием группы mutagens.
- Модели Character/общих данных/журнала/навыков и Race/Profession/Homeland связаны с фактическим контекстом. У homeland используется value/otherValue, у расы и профессии — name для заголовка и отдельное enrichedText для вкладок.
- Обычный и алхимический Craft сопоставлены с RollConfig, addActiveEffects, extendedRoll, realCraft и предикатом isAlchemicalCraft. Отдельно обозначены strict > для успеха, +2 диаграммы, ожидание Promise, предварительный запас и повторная проверка ресурса.
- Кнопки header сопоставлены с WitcherActorSheet, deathsaveMixin и healListeners; luck/adrenaline sidebar — с statListener. Проверены реальные селекторы и расположение незакрытого a. В issue-00176 уточнено прежнее название метода локализации: activateListeners вместо _onRender.
- Числовые input и checkbox связаны с фактическими путями модели: toxicity/luck в stats, остальные ресурсы панели в derivedStats, healthState — отдельно. Временные HP выводятся отдельной суммой. Иконка сравнивает unmodifiedMax, а progress — max.
- Дополнены **30 связанных карточек**: базовый лист и Actor/Item; Character/CommonActor и вложенные general/lifeEvents/log/Skill/CRA/derivedStats; Race/Profession/Homeland/Diagram/Component; modifierMixin/RollConfig/extendedRoll/ChatMessageData; registerSheets/handlebars/settings; stat/death/heal-примеси; прежние tab-stats/tab-skills/tab-inventory/tab-effects. У базового листа снят прежний предел о непрочитанном полном Character; полные Monster/Loot остаются следующим порциям.

### Потенциальные проблемы

| ID | Наблюдение |
| --- | --- |
| [issue-00200](../../issues/potential/issue-00200.md) | Отрицательный ввод списания IP превращает баланс в строку |
| [issue-00201](../../issues/potential/issue-00201.md) | Уведомление о нехватке компонентов падает без связанного результата рецепта |
| [issue-00202](../../issues/potential/issue-00202.md) | Незакрытая ссылка наград создаёт лишние ссылки в заголовке |
| [issue-00203](../../issues/potential/issue-00203.md) | Индикатор здоровья использует исходный максимум вместо текущего |
| [issue-00204](../../issues/potential/issue-00204.md) | Пустая подпись модификатора делает формулу броска некорректной |
| [issue-00205](../../issues/potential/issue-00205.md) | Флаги игнорирования состояний здоровья не имеют русского перевода |

Регистрация разрешена пунктом9 родительской задачи; все новые карточки potential. Дополнены [issue-00015](../../issues/potential/issue-00015.md), [issue-00024](../../issues/potential/issue-00024.md), [issue-00028](../../issues/potential/issue-00028.md), [issue-00037](../../issues/potential/issue-00037.md), [issue-00038](../../issues/potential/issue-00038.md), [issue-00041](../../issues/potential/issue-00041.md), [issue-00101](../../issues/potential/issue-00101.md), [issue-00109](../../issues/potential/issue-00109.md), [issue-00167](../../issues/potential/issue-00167.md), [issue-00176](../../issues/potential/issue-00176.md). Прежние репродукции не названы повторно выполненными, если запускался только соседний контракт. Языковая корректировка issue-00193 из .030 сохранена; новые четыре пропуска ru выделены в issue-00205. Подтверждений пользователя, исправлений и закрытий нет; всего **205 potential issues**.

### Формальная проверка документов и сохранности

Проверка Python через stdin и git diff --check завершена успешно:

- Реестр: 621 уникальный путь, 250 карточек со статусом «Проверено», 371 «Не начат»; точный перечень .031 — три файла и 711 строк. Все новые карточки содержат 11 обязательных разделов, определения методов и поля шаблонов.
- Четыре серии: 61+96+79+63 = 299 различных назначенных файлов без пересечений; 40 подзадач, первые31 done, остальные9 planned. В четвёртой серии 3 проверены, 60 в очереди; 311 исходников ещё не распределены.
- По всем250 карточкам сверены **320 прямых импортов** (210 default, 103 named-выражения/108 имён, семь namespace), фактические экспорты и обратные упоминания в уже описанных соседях. Для порции — семь импортов. Сверены **160 буквальных системных HBS-связей**, девять из нового класса, и обратные связи при наличии карточки.
- Проверены **11 808 локальных ссылок** в 527 Markdown-документах docs плюс корневые README/AGENTS, включая якоря; битых ссылок не найдено. Таблицы и отсутствие хвостовых пробелов проверены во всех затронутых документах. В реестре205 уникальных issues, все в potential; новые200–205 заполнены по семи разделам шаблона.
- Изменены только **60 Markdown-документов в docs**: 51 существующий и девять новых (три карточки, шесть issues). Состав соответствует этой порции; задачи .032–.040, правила, исходники и конфигурация не менялись.
- Все621 исходник побайтно совпали с HEAD проверки и исходным срезом TASK-0001. Общая SHA256 содержимого/путей: `52701d3d0a5f054319886ac2a9d45b42c26c80098858d02518579c6a1edfaec4`. Состав реестра сопоставлен с git ls-files и фактическим деревом с согласованными исключениями.
- Для всех **1196 отслеживаемых файлов** сохранены mode/uid/gid/inode; SHA256 набора метаданных — `bab7dc7c9b557e9e8febadc4d255e83b49acab67c5be030628d6a7d170b5ea97`. Старое содержимое журнала после его заголовка сохранено без изменений; исходная SHA256 журнала — `2b3153fbf2715f5334eab615cfea687285f365f9e860323f91f622a8fde89bf0`.
- Ветка и HEAD остались прежними; git diff --check проходит. Коммит не создавался.

Сверка ограничена текущим checkout и указанными API ядра. Исходники, сохранённые игровые данные и метаданные доступа не менялись. Следующая задача — [TASK-0003.032](../../tasks/task-0003.032.md); в этой порции её выполнение не начиналось.

## Планирование TASK-0003.031–TASK-0003.040

Дата: 2026-09-11. Ветка `rusbar-main`, HEAD `bdde25700fedbd21cfb05501e4b88a4c90ff9fac`. На старте рабочее дерево чистое; отслеживаются 1186 файлов. Основание — поручение пользователя написать следующие десять задач после выполнения .030.

### Состав и границы

Подготовлены [десять подзадач](../../tasks/task-0003-remaining-files.md#четвёртая-серия-task-0003031task-0003040) planned на 63 различных файла. Проверены перечни реестра, размеры, импорты/методы и обращения к шаблонам, необходимые для выбора границ. Это проверка постановки, а не полный разбор или воспроизведение поведения.

| Порция | JS | HBS | Всего файлов | Строк |
| --- | --- | --- | --- | --- |
| [TASK-0003.031](../../tasks/task-0003.031.md) | 1 | 2 | 3 | 711 |
| [TASK-0003.032](../../tasks/task-0003.032.md) | 2 | 11 | 13 | 973 |
| [TASK-0003.033](../../tasks/task-0003.033.md) | 2 | 2 | 4 | 178 |
| [TASK-0003.034](../../tasks/task-0003.034.md) | 3 | 2 | 5 | 251 |
| [TASK-0003.035](../../tasks/task-0003.035.md) | 3 | 3 | 6 | 384 |
| [TASK-0003.036](../../tasks/task-0003.036.md) | 2 | 2 | 4 | 164 |
| [TASK-0003.037](../../tasks/task-0003.037.md) | 4 | 4 | 8 | 313 |
| [TASK-0003.038](../../tasks/task-0003.038.md) | 1 | 3 | 4 | 965 |
| [TASK-0003.039](../../tasks/task-0003.039.md) | 1 | 5 | 6 | 870 |
| [TASK-0003.040](../../tasks/task-0003.040.md) | 10 | 0 | 10 | 237 |
| **Всего** | **29** | **34** | **63** | **5046** |

Все 63 файла имеют в реестре статус «Не начат», отсутствуют среди 247 полных карточек и прежних 236 файлов TASK-0003.001–.030. Между новыми порциями пересечений нет. Всего в сорока подзадачах распределены 299 файлов из 610, оставшихся после TASK-0002; ещё 311 требуют детализации. Повторные ссылки на соседей в разделах зависимостей не являются повторным включением в объём.

Проверены точные пути исходников и начальных зависимостей; они существуют в исследуемом срезе. Начальные связи не объявлены исчерпывающими: при выполнении нужно читать определения, находить потребителей и уточнять карточки. Наличие импорта, предзагрузки или имени шаблона не доказывает достижимость интерфейса; особенно это относится к старым monster-sheet, monster-details-tab, monster-spell-tab и note-sheet.

### Содержательная сверка постановки

- .031 включает весь WitcherCharacterSheet, в том числе все ремесленные callbacks. .034 проверяет их связи с поиском компонентов и разбором предметов, не откладывая часть класса и не считая его повторно.
- .032 связывает конфигурацию/контекст монстра с экспортом добычи; .035 продолжает путь в LootSheet и проверяет mount как Item, включённый в список loot.
- .033 различает биографию, старые note Item и массив notes Actor. .036 отделяет обмен валюты от покупки .035 и выдачи наград .037.
- .038 и .039 продолжают уже разобранные модели/редакторы профессии и магии до их применения. Боевые защита/урон проверяются до нужных определений, но их полные файлы остаются за границей серии.
- .040 различает подготовку ChatMessageData, документ WitcherChatMessage и модели system сообщения; замыкает связи действий щита/лечения с .039 и ремонта с прежними карточками.
- У каждой задачи есть точный состав, ожидаемый результат, границы, порядок, начальные связи, специальные сценарии и критерии приёмки. Где уместно, указаны прежние potential issues для сверки, без их подтверждения и без задач на исправление.
- Проверка переводов учитывает штатное expandObject и fallback после уточнения .030. Изолированные сценарии, браузер, серверная запись и сетевое выполнение должны быть различены в будущих результатах.

В .035 запланирована общая сверка первых 31 файла с прежними 247, в .040 — всех 63 с прежними 247. Эти проверки дополняют обязательную сверку каждой порции и пока не выполнены.

### Формальная проверка и сохранность

Автоматическая проверка сопоставила все 40 списков подзадач: 299 различных файлов, из них 236 уже разобраны и 63 поставлены в новую очередь. Пересечений между перечнями нет. Критерии новых задач не отмечены выполненными, .031–.040 имеют статус planned; проверены числа в обеих сводных таблицах, последовательность зависимостей и наличие обязательных разделов.

Проверены 518 Markdown-документов в docs и два корневых файла: 11 507 локальных ссылок, включая якоря. Существование путей, структура изменённых таблиц и git diff --check — без ошибок. Созданы десять задач, обновлены семь существующих документов. Реестр файлов, все 247 карточек анализа, 199 potential issues и ранее выполненные задачи сохранены без изменений.

Состав и байты всех 621 исходника совпадают со стартовым HEAD и базовым срезом TASK-0001. Контрольная сумма набора исходников — `52701d3d0a5f054319886ac2a9d45b42c26c80098858d02518579c6a1edfaec4`. Для всех 1186 ранее отслеживаемых файлов сохранены mode, uid, gid и inode; контрольная сумма метаданных — `d3a17507581a639c8bb57960593828d863dd45f86096f93a214b4dc864823b14`. Общие требования TASK-0003 и исторические записи журнала/CHANGELOG сохранены; SHA-256 прежнего журнала — `fb1894baf35adc8cc3b2fb8078a6dccc63066a7b3140e3749bc6b535ada9c82a`.

Игровые сценарии не запускались: изменение Markdown проверено как постановка задач. Сборка, служба, игровые данные и права не менялись; коммит не создавался.

Покрытие остаётся **247 из 621**, не разобраны **374**: 63 поставлены в очередь, 311 не распределены. TASK-0003 остаётся in-progress; .031–.040 — planned; TASK-0004/0005 — draft. Первая следующая задача — [TASK-0003.031](../../tasks/task-0003.031.md), её выполнение не начиналось.

## TASK-0003.030

| Поле | Результат |
| --- | --- |
| Дата / версия | 2026-09-11; `rusbar-main`, `aa6af106e86a9c75fe050d599f961c8fadb74f1b`; Foundry 14.367.0 и Node 24.16.0. |
| Задача | [TASK-0003.030](../../tasks/task-0003.030.md): 9 файлов, 424 строки (4 JS/5 HBS); итоговая сверка третьей серии. |
| Результат | 9 новых карточек, 25 уточнённых; 247/621 проверены, 374 не разобраны. Все 79 файлов третьей серии проверены, очередь исчерпана; новые задачи не созданы. |
| Проблемы | 6 новых potential issue-00194–00199; дополнены 8 прежних: 00008/00011/00012/00035/00036/00167/00186/00193. Подтверждение, исправление и закрытие не выполнялись. |

### Полный разбор и определения

| Исходник | Строк | Карточка |
| --- | --- | --- |
| [module/actor/sheets/mixins/statMixin.js](../../../module/actor/sheets/mixins/statMixin.js) | 132 | [Описание](files/module/actor/sheets/mixins/statMixin.js.md) |
| [module/actor/sheets/configurations/WitcherModifiersConfiguration.js](../../../module/actor/sheets/configurations/WitcherModifiersConfiguration.js) | 71 | [Описание](files/module/actor/sheets/configurations/WitcherModifiersConfiguration.js.md) |
| [module/actor/sheets/mixins/deathSaveMixin.js](../../../module/actor/sheets/mixins/deathSaveMixin.js) | 51 | [Описание](files/module/actor/sheets/mixins/deathSaveMixin.js.md) |
| [module/actor/mixins/adrenalineMixin.js](../../../module/actor/mixins/adrenalineMixin.js) | 7 | [Описание](files/module/actor/mixins/adrenalineMixin.js.md) |
| [templates/partials/character/tab-stats.hbs](../../../templates/partials/character/tab-stats.hbs) | 114 | [Описание](files/templates/partials/character/tab-stats.hbs.md) |
| [templates/sheets/actor/configuration/app/edit-stats.hbs](../../../templates/sheets/actor/configuration/app/edit-stats.hbs) | 11 | [Описание](files/templates/sheets/actor/configuration/app/edit-stats.hbs.md) |
| [templates/sheets/actor/configuration/app/partials/stats-block.hbs](../../../templates/sheets/actor/configuration/app/partials/stats-block.hbs) | 17 | [Описание](files/templates/sheets/actor/configuration/app/partials/stats-block.hbs.md) |
| [templates/dialog/deprecations/statSkillModifiers.hbs](../../../templates/dialog/deprecations/statSkillModifiers.hbs) | 11 | [Описание](files/templates/dialog/deprecations/statSkillModifiers.hbs.md) |
| [templates/dialog/deprecations/lifepathModifiers.hbs](../../../templates/dialog/deprecations/lifepathModifiers.hbs) | 10 | [Описание](files/templates/dialog/deprecations/lifepathModifiers.hbs.md) |

Все 424 строки прочитаны полностью. Сверены 9 прямых импортов, Object.assign, callbacks репутации, поля/методы конфигурации и две PARTS. Для источников значений прочитаны Stats/DerivedStats/Reputation/adrenaline/CommonActorData и необходимые методы WitcherActor; для событий — оба базовых листа, PARTS/actions и producer контекста Character/Monster, headers/sidebar и query/defense-потребитель адреналина. Предзагрузка различена с фактическим выбором листа. Для обоих deprecations-HBS поиск exact path/stem/построения каталога в module/templates не обнаружил внутреннего потребителя; deprecationWarnings пуст.

Уточнённые карточки: [module/actor/witcherActor.js](files/module/actor/witcherActor.js.md); [module/actor/sheets/WitcherActorSheet.js](files/module/actor/sheets/WitcherActorSheet.js.md); [module/actor/sheets/WitcherActorSheetV1.js](files/module/actor/sheets/WitcherActorSheetV1.js.md); [module/data/actor/templates/common/stats/statData.js](files/module/data/actor/templates/common/stats/statData.js.md); [module/data/actor/templates/common/stats/statsData.js](files/module/data/actor/templates/common/stats/statsData.js.md); [module/data/actor/templates/common/stats/derivedStatsData.js](files/module/data/actor/templates/common/stats/derivedStatsData.js.md); [module/data/actor/templates/common/reputationData.js](files/module/data/actor/templates/common/reputationData.js.md); [module/data/actor/templates/common/adrenalineData.js](files/module/data/actor/templates/common/adrenalineData.js.md); [module/data/actor/commonActorData.js](files/module/data/actor/commonActorData.js.md); [module/data/actor/characterData.js](files/module/data/actor/characterData.js.md); [module/data/actor/monsterData.js](files/module/data/actor/monsterData.js.md); [module/setup/config.js](files/module/setup/config.js.md); [module/setup/settings.js](files/module/setup/settings.js.md); [module/setup/handlebars.js](files/module/setup/handlebars.js.md); [module/setup/deprecations.js](files/module/setup/deprecations.js.md); [module/setup/queries.js](files/module/setup/queries.js.md); [module/scripts/rollConfig.js](files/module/scripts/rollConfig.js.md); [module/scripts/rolls/extendedRoll.js](files/module/scripts/rolls/extendedRoll.js.md); [module/chatMessage/chatMessageData.js](files/module/chatMessage/chatMessageData.js.md); [module/scripts/helper.js](files/module/scripts/helper.js.md); [module/actor/sheets/mixins/skillMixin.js](files/module/actor/sheets/mixins/skillMixin.js.md); [templates/sheets/actor/configuration/app/edit-skills.hbs](files/templates/sheets/actor/configuration/app/edit-skills.hbs.md); [templates/partials/monster/monster-skill-tab.hbs](files/templates/partials/monster/monster-skill-tab.hbs.md); [templates/partials/character/tab-skills.hbs](files/templates/partials/character/tab-skills.hbs.md); [module/scripts/investigation/rollClue.js](files/module/scripts/investigation/rollClue.js.md). Старые текущие ограничения по WitcherModifiersConfiguration уточнены; исторические результаты предыдущих порций не переписаны.

### Изолированные проверки и подмены

19 новых групп завершены успешно: 18 основного прогона и отдельно группа 19 после проверки producer монстра. Дополнительно повторены все 22 группы .029 с исправленной загрузкой локализации —22/22 прошли. Сценарии выполнялись из памяти через `node --input-type=module`, без создания стенда/тестовых файлов. Использованы настоящие Foundry DataModel/TypeDataModel/fields/utils, Roll/terms/Peggy, Handlebars 4.7.9, parse5, системные методы и модели, FormDataExtended и DocumentSheet._processFormData. Грани кубиков заданы; отправка сообщений и update перехвачены.

Подменены базовые Sheet/Application/Document оболочки, Dialog, DOM-форма/элементы/window, fulfillment/RollResolver и записывающие API. Настоящий FormDataExtended прочитал все именованные enabled поля этой формы и привёл Number; _processFormData выполнил expandObject; system.updateSource принял данные, после чего исполнялись настоящие методы подготовки Actor в нужном порядке. Это не browser submit и не серверный Document.update. Исправлялись только фасады проверок: window и сохранённые исходные данные fixture; customStat проверен на MonsterData, где он действительно объявлен. Предупреждение Node MODULE_TYPELESS_PACKAGE_JSON не устранялось изменением системы.

| Группа | Проверка | Фактический результат |
| --- | --- | --- |
| 01 | Восемь характеристик и luck.max | При value3/max8 и кубике 5 успех только у luck; speaker Actor, type base; метод возвращает void. |
| 02 | Модификатор/границы/крит/отмена stat-save | Равенство порогу неуспешно;5−1<5 успешно;threshold0 сравнивается, −1 нет;10+2=12,1 с провалом→0; отмена/неизвестный stat отклоняются. |
| 03 | Репутация | Диалог не ждёт выбора; save по value5 с кубиком 5 неуспешен; face-down5+rep5+WILL4=14 без порога; save при 0 и провале до 0 тоже неуспешен. |
| 04 | Сумма максимумов | Девять max8 дают 72; toxicity999 исключена по ключу; расход luck.value не меняет сумму; отрицательный max учитывается; пустая модель даёт 0. |
| 05 | Минус удачи/адреналина и reset | 0/−1 не пишут,0.5→−0.5,1→0,3→2; decrement ждёт update. Luck reset копирует max14. |
| 06 | Плюс адреналина | Опция false не пишет; true добавляет 1 к 0/10/−1/0.5; await листового плюса завершается с ожидающим update. |
| 07 | Счётчик смерти | Плюс+1 для 0/3/−1/0.5; минус сбрасывает 0; оба метода завершаются при двух неразрешённых update. |
| 08 | Ветви смерти/порог | HP1/0/−1, STUN0/5/7/14, BODY/WILL7/8/12, счётчик 0/2/5/6/7/−2. Верхний clamp10 до счётчика;0 даётfalse, −1/−2 — отсутствие success; счётчик сам не изменяется. |
| 09 | Смерть без критов | HP0 читает BODY/WILL.max8 при value1; кубики 1/10 остаются одним результатом, успех 1<8 и неуспех 10<8. |
| 10 | DOM-события | Шесть stat и три death click-контракта; методы привязаны к листу; death-minus пишет 0. |
| 11 | Конфигурация | Настоящий класс на базовом фасаде; type stats/derivedStats/skill/неизвестный/undefined даёт 10/12/52/0/0 полей. Общий CONFIG.statLabels заменён; maps/system ссылки;8 jQuery-селекторов; skillListener меняет глобальную jQuery. |
| 12 | Вкладка характеристик | 9 stat/6 derived; isGM/displayRep определяют репутацию;0 и отрицательные оформлены со знаками. Изменение label toxicity меняет фильтрацию, ключ остаётся прежним. |
| 13 | Репутация max/value | При value3/max8 span.max показывает+3, разница−5. |
| 14 | FormDataExtended и исходная база | База luck8/max12; изменён соседний INT. Настоящая форма отправляет luck.unmodifiedMax12, модель принимает; после тех же+2 и двух calculateStats max16. |
| 15 | Редактирование derived | Настоящая MonsterData customStatfalse/true; ввод 99: STUN8/RUN24 в обоих режимах;HP40/99, Vigor99. Полная нужная последовательность подготовки после updateSource. |
| 16 | Два уведомления | affectedActors undefined/[]→пусто; два имени и HTML-имя→экранированный список; оба языка дают перевод. |
| 17 | Связь с прежними расчётами | Повторный luck+=2, перегруз 81 при вместимости 80→REF6/DEX6/SPD7; отрицательная база INT сохраняет−2; BODY/SPD.max2 не меняют value8 при базе 8. |
| 18 | Правильная локализация | После core expandObject все буквальные ключи новой порции есть в en; ru не содержит savingThrow. Семь старых Actor.Skill.* есть в en/ru; levelUp отсутствует в ru. |
| 19 | Сумма монстра | Настоящий _prepareCharacterData Monster не задаёт totalStats; HBS выводит только Total Stats:; helper для тех же данных даёт 72. |

### Исправление проверки переводов .029

Установленный Foundry в client/helpers/localization.mjs:368 применяет `foundry.utils.expandObject(json)` до lookup. Прежний отдельный поиск .029 пропустил этот этап: семь WITCHER.Actor.Skill.* были ошибочно названы отсутствующими. После раскрытия они найдены в en/ru. Утверждение отозвано в карточке старого monster-skill-tab и issue-00193; историческая запись .029 ниже сохранена как история с этой явной поправкой. Issue-00193 остаётся potential: ru не содержит levelUp, а новая порция добавила savingThrow; en fallback есть.

Повторная статическая сверка всех 79 файлов выделила 269 буквальных WITCHER-строк:266 полных ключей и 3 динамических префикса (WITCHER.Inventory., WITCHER.fumbleResults., WITCHER.St), которые не являются самостоятельными отсутствующими переводами. У полных ключей отсутствуют 4 en и 8 ru записей: DangerLow/Medium/High и Weapon.Availability в обоих языках; дополнительно ru emanation/customModifier/levelUp/savingThrow. Это согласуется с issue-00137/00178/00186/00193. Динамические составные ключи не объявляются полностью проверенными одной такой выборкой; их условия остаются в карточках соответствующих процессов.

### Итоговая перекрёстная сверка 79 файлов с прежними 168

Сопоставлены все 30 списков задач и 247 карточек. Для всех 79 файлов третьей серии извлечены 607 относительных ссылок из таблиц используемых сущностей/зависимостей на 170 различных исходников: пути существуют, статус полного разбора отделён от частичного чтения. Это ссылки разных видов, включая схемы, контекст и сравнение контрактов, а не 607 подтверждённых runtime-вызовов. Общая автоматическая проверка импортов/HBS ниже сверяет обе стороны среди описанных файлов; известные динамические цепочки сверены по указанным producer/consumer определениям. Не выполнялся повторный запуск всех старых сценариев .021–.028 или полный игровой процесс.

| Порция | Файлов | Ссылок в таблицах | Разных источников из прежних 168 | Из серии 79 | Вне полного покрытия |
| --- | --- | --- | --- | --- | --- |
| .021 | 13 | 88 | 14 | 16 | 3 |
| .022 | 5 | 10 | 2 | 4 | 3 |
| .023 | 14 | 63 | 3 | 16 | 4 |
| .024 | 3 | 13 | 5 | 3 | 2 |
| .025 | 2 | 64 | 19 | 12 | 3 |
| .026 | 2 | 40 | 17 | 5 | 10 |
| .027 | 12 | 154 | 21 | 13 | 11 |
| .028 | 5 | 27 | 7 | 3 | 6 |
| .029 | 14 | 94 | 15 | 21 | 5 |
| .030 | 9 | 54 | 13 | 13 | 3 |

Содержательные границы сведены по процессам: магические модели/листы и создание регионов → castSpell/ядро регионов; расследования → helper и rollSkill; контейнер → UUID и копирование Items; базовые листы → примеси/дочерние producers; инвентарь → схемы, контекст, callbacks и шаблоны; общий Roll → навыки и спасброски; редактор → модели и повторная подготовка Actor. Новые полные карточки .028–.030 закрыли прежние точечные границы helper, skill/stat/death и конфигурации. Прочитанные только частично Character/MonsterSheet и боевые примеси не повышены до полного покрытия. Сверка выявила и исправила описанную выше языковую неточность, остальные указанные в проверках .029 результаты сохранились.

33 источника из таблиц зависимостей этой серии остаются без полной карточки: [lang/en.json](../../../lang/en.json); [lang/ru.json](../../../lang/ru.json); [module/actor/mixins/armorMixin.js](../../../module/actor/mixins/armorMixin.js); [module/actor/mixins/castSpellMixin.js](../../../module/actor/mixins/castSpellMixin.js); [module/actor/mixins/craftingMixin.js](../../../module/actor/mixins/craftingMixin.js); [module/actor/mixins/currencyConverterMixin.js](../../../module/actor/mixins/currencyConverterMixin.js); [module/actor/mixins/professionMixin.js](../../../module/actor/mixins/professionMixin.js); [module/actor/mixins/verbalCombatMixin.js](../../../module/actor/mixins/verbalCombatMixin.js); [module/actor/sheets/WitcherCharacterSheet.js](../../../module/actor/sheets/WitcherCharacterSheet.js); [module/actor/sheets/WitcherLootSheet.js](../../../module/actor/sheets/WitcherLootSheet.js); [module/actor/sheets/WitcherMonsterSheet.js](../../../module/actor/sheets/WitcherMonsterSheet.js); [module/actor/sheets/configurations/WitcherMonsterConfigurationSheet.js](../../../module/actor/sheets/configurations/WitcherMonsterConfigurationSheet.js); [module/actor/sheets/mixins/alchemyMixin.js](../../../module/actor/sheets/mixins/alchemyMixin.js); [module/actor/sheets/mixins/currencyConverterMixin.js](../../../module/actor/sheets/mixins/currencyConverterMixin.js); [module/actor/sheets/mixins/noteMixin.js](../../../module/actor/sheets/mixins/noteMixin.js); [module/data/chatMessage/attackMessageData.js](../../../module/data/chatMessage/attackMessageData.js); [module/data/chatMessage/baseMessageData.js](../../../module/data/chatMessage/baseMessageData.js); [module/data/chatMessage/defenseMessageData.js](../../../module/data/chatMessage/defenseMessageData.js); [module/data/chatMessage/templates/attackData.js](../../../module/data/chatMessage/templates/attackData.js); [module/data/item/mountData.js](../../../module/data/item/mountData.js); [module/item/mixins/dismantlingMixin.js](../../../module/item/mixins/dismantlingMixin.js); [module/scripts/socket/socketMessage.js](../../../module/scripts/socket/socketMessage.js); [styles/loot-sheet.css](../../../styles/loot-sheet.css); [styles/tab-inventory.css](../../../styles/tab-inventory.css); [styles/witcher-styles.css](../../../styles/witcher-styles.css); [templates/chat/item/item-description.hbs](../../../templates/chat/item/item-description.hbs); [templates/chat/item/partials/item-description/alchemicals.hbs](../../../templates/chat/item/partials/item-description/alchemicals.hbs); [templates/chat/item/partials/item-description/crafting-items.hbs](../../../templates/chat/item/partials/item-description/crafting-items.hbs); [templates/chat/item/partials/item-description/description.hbs](../../../templates/chat/item/partials/item-description/description.hbs); [templates/chat/item/partials/item-description/spell-description.hbs](../../../templates/chat/item/partials/item-description/spell-description.hbs); [templates/chat/item/partials/item-description/tags.hbs](../../../templates/chat/item/partials/item-description/tags.hbs); [templates/partials/character/substances.hbs](../../../templates/partials/character/substances.hbs); [templates/sheets/actor/partials/character/sidebar.hbs](../../../templates/sheets/actor/partials/character/sidebar.hbs). Этот список — ближайшие задокументированные соседи; он не подменяет полный остаток 374 файлов и не формирует будущие задачи автоматически.

### Проблемы и пределы выводов

| Проблема | Наблюдение |
| --- | --- |
| [issue-00194](../../issues/potential/issue-00194.md) | Редактор сохраняет изменённый максимум характеристики как исходную базу |
| [issue-00195](../../issues/potential/issue-00195.md) | Редактор предлагает ввод производных параметров, который перезаписывается расчётом |
| [issue-00196](../../issues/potential/issue-00196.md) | Отрицательный порог спасброска отключает определение успеха и провала |
| [issue-00197](../../issues/potential/issue-00197.md) | Действия адреналина и счётчика смерти завершаются до записи Actor |
| [issue-00198](../../issues/potential/issue-00198.md) | Строка репутации показывает текущее значение на месте максимума |
| [issue-00199](../../issues/potential/issue-00199.md) | Вкладка характеристик монстра не получает сумму totalStats |

Модель/форма/вычисление/запись различены. Нет нового общего минимума 1 или потолка 10; clamp смерти применяется локально до счётчика, другие характеристики могут остаться 0/отрицательными. Ресурсные Promise проверены при удержанной записи, но потери данных/исход гонки на сервере не утверждаются. Репутация max/value проверена на явно разных подготовленных значениях; частота такого состояния в мире не исследовалась. Сравнение labels по переводу и мутация CONFIG сами по себе не зарегистрированы как ошибки.

Исследование не включает реальные миры/компедиумы, браузерные формы, все языки, внешние модули и сетевую синхронизацию. Служба, сборка, игровые данные и исходники не изменялись. Третья серия завершена; TASK-0003 остаётся in-progress до исследования остатка, TASK-0004/0005 остаются draft.

### Формальная проверка документации и сохранности

Проверены 247 карточек и 30 списков подзадач без пересечений: .001–.030 выполнены. Реестр содержит 621 исходник, не разобраны 374. Все 79 файлов третьей серии проверены; сформированной очереди больше нет. TASK-0003 остаётся in-progress, TASK-0004/0005 — draft.

Встречная проверка охватила 313 прямых импортов: 206 default, 100 named-import statements со 105 именами и 7 namespace; новая порция содержит 9 импортов. Проверены существование целей, определения экспортов, исходящие ссылки и обратные ссылки уже описанных потребителей. Аналогично проверена 151 буквальная ссылка на HBS; новой порцией добавлены 3 связи.

Проверены 508 Markdown-документов в docs и два корневых файла: 11 178 локальных ссылок, включая якоря; структура таблиц и git diff --check без ошибок. Изменены 44 существующих документа, созданы 15 новых — девять карточек и шесть potential issues. Всего 59 документов; номера 199 potential issues уникальны и согласованы с реестром.

Состав и байты всех 621 исходника совпадают как со стартовым HEAD, так и со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. Контрольная сумма набора исходников — `52701d3d0a5f054319886ac2a9d45b42c26c80098858d02518579c6a1edfaec4`. Для всех 1171 ранее отслеживаемых файлов сохранены mode, uid, gid и inode; контрольная сумма метаданных — `8f944510481c4cadd92d8c85b9ea34a282105249ae6445195df69e62bcec1f9d`. Прежняя часть журнала сохранена побайтово; SHA-256 прежнего файла — `b16e6fab28baea2b87a05d8ead09f4cf75af33458b67f7b82f3b2d17199114be`. HEAD и ветка не менялись; коммит не создавался.

## TASK-0003.029

| Поле | Результат |
| --- | --- |
| Дата / версия | 2026-09-11; `rusbar-main`, `273a6d7db0b7c866399db3ecd4f7191817ae6f10`; исходники совпадают со срезом TASK-0001. |
| Основание | [Согласованная подзадача](../../tasks/task-0003.029.md) и поручение продолжить; 14 файлов, 763 строки, 5 JS и 9 HBS. |
| Результат | 14 новых карточек, 27 уточнённых; покрытие 238/621, не разобраны 383. В третьей серии 70/79; .030 planned, 9 файлов; ещё 374 не распределены. |
| Проблемы | Новые potential issue-00187–00193; дополнены 00004/00015/00016/00017/00018/00028/00030/00167/00186. Подтверждение и исправление не выполнялись. |
| Окружение | Foundry 14.367.0 (/opt/foundryvtt/package.json), Node.js 24.16.0; Linux, без мира/браузера/записи документов. |

### Состав и перекрёстные связи

| Исходник | Строк | Полная карточка |
| --- | --- | --- |
| [module/actor/mixins/skillMixin.js](../../../module/actor/mixins/skillMixin.js) | 174 | [Описание](files/module/actor/mixins/skillMixin.js.md) |
| [module/actor/sheets/mixins/skillMixin.js](../../../module/actor/sheets/mixins/skillMixin.js) | 42 | [Описание](files/module/actor/sheets/mixins/skillMixin.js.md) |
| [module/actor/sheets/mixins/customSkillMixin.js](../../../module/actor/sheets/mixins/customSkillMixin.js) | 62 | [Описание](files/module/actor/sheets/mixins/customSkillMixin.js.md) |
| [module/data/item/skillItemData.js](../../../module/data/item/skillItemData.js) | 16 | [Описание](files/module/data/item/skillItemData.js.md) |
| [module/item/sheets/WitcherSkillItemSheet.js](../../../module/item/sheets/WitcherSkillItemSheet.js) | 43 | [Описание](files/module/item/sheets/WitcherSkillItemSheet.js.md) |
| [templates/sheets/item/skill-item-sheet.hbs](../../../templates/sheets/item/skill-item-sheet.hbs) | 12 | [Описание](files/templates/sheets/item/skill-item-sheet.hbs.md) |
| [templates/partials/character/tab-skills.hbs](../../../templates/partials/character/tab-skills.hbs) | 108 | [Описание](files/templates/partials/character/tab-skills.hbs.md) |
| [templates/partials/character/skill-display.hbs](../../../templates/partials/character/skill-display.hbs) | 24 | [Описание](files/templates/partials/character/skill-display.hbs.md) |
| [templates/partials/character/custom-skill-display.hbs](../../../templates/partials/character/custom-skill-display.hbs) | 23 | [Описание](files/templates/partials/character/custom-skill-display.hbs.md) |
| [templates/partials/monster/monster-skill-tab.hbs](../../../templates/partials/monster/monster-skill-tab.hbs) | 141 | [Описание](files/templates/partials/monster/monster-skill-tab.hbs.md) |
| [templates/partials/monster/monster-skill-display.hbs](../../../templates/partials/monster/monster-skill-display.hbs) | 13 | [Описание](files/templates/partials/monster/monster-skill-display.hbs.md) |
| [templates/partials/monster/monster-custom-skill-display.hbs](../../../templates/partials/monster/monster-custom-skill-display.hbs) | 44 | [Описание](files/templates/partials/monster/monster-custom-skill-display.hbs.md) |
| [templates/sheets/actor/configuration/partials/skillConfiguration.hbs](../../../templates/sheets/actor/configuration/partials/skillConfiguration.hbs) | 14 | [Описание](files/templates/sheets/actor/configuration/partials/skillConfiguration.hbs.md) |
| [templates/sheets/actor/configuration/app/edit-skills.hbs](../../../templates/sheets/actor/configuration/app/edit-skills.hbs) | 47 | [Описание](files/templates/sheets/actor/configuration/app/edit-skills.hbs.md) |

Все файлы перечня прочитаны полностью. Для связи использовались `rg -n`, `rg --files`, чтение определений и проверка импортов/partial по `module/` и `templates/`; исключения реестра сохранены. Ни хеширование, ни просмотр соседнего определения не повышали его статус. Проверены: Object.assign Actor и двух базовых листов; registerDataModels/Sheets; все четыре прямых импорта actor/skillMixin; Skill/Character/Monster/Item schemas; Log.addIpReward; addActiveEffects и getArmorEcumbrance; _prepareCustomSkills; PARTS и openModifiers обоих текущих листов; конфигурации, IP listeners и inline Item-edit; все буквальные шаблонные зависимости.

Различены встроенный Skill в Actor, Item type skill и профессиональные навыки. Установлено, что текущие Character/Monster используют общий character/tab-skills. Старые monster partial имеют HBS-родителя monster-sheet и preload, но не выбраны текущими V2 PARTS. Проверка .029 уточняет две прежние границы: настоящий formGroup с Actor-родителем формирует правильные полные пути (технические подписи остаются), а Log сам отправляет обновление IP помимо финального update levelUpSkill. Социальный обработчик читает одно поле Actor.general, не пять региональных полей Race.

Уточнённые карточки: [module/actor/witcherActor.js](files/module/actor/witcherActor.js.md); [module/actor/mixins/modifierMixin.js](files/module/actor/mixins/modifierMixin.js.md); [module/actor/sheets/WitcherActorSheet.js](files/module/actor/sheets/WitcherActorSheet.js.md); [module/actor/sheets/WitcherActorSheetV1.js](files/module/actor/sheets/WitcherActorSheetV1.js.md); [module/actor/sheets/mixins/itemMixin.js](files/module/actor/sheets/mixins/itemMixin.js.md); [module/data/actor/characterData.js](files/module/data/actor/characterData.js.md); [module/data/actor/monsterData.js](files/module/data/actor/monsterData.js.md); [module/data/actor/commonActorData.js](files/module/data/actor/commonActorData.js.md); [module/data/actor/templates/common/skills/skillData.js](files/module/data/actor/templates/common/skills/skillData.js.md); [module/data/actor/templates/common/skills/intData.js](files/module/data/actor/templates/common/skills/intData.js.md); [module/data/actor/templates/common/skills/craData.js](files/module/data/actor/templates/common/skills/craData.js.md); [module/data/actor/templates/common/skills/skillsData.js](files/module/data/actor/templates/common/skills/skillsData.js.md); [module/data/actor/templates/character/logData.js](files/module/data/actor/templates/character/logData.js.md); [module/data/actor/templates/character/pannelsData.js](files/module/data/actor/templates/character/pannelsData.js.md); [module/data/actor/templates/character/skillTrainingData.js](files/module/data/actor/templates/character/skillTrainingData.js.md); [module/data/actor/templates/character/generalData.js](files/module/data/actor/templates/character/generalData.js.md); [module/data/item/raceData.js](files/module/data/item/raceData.js.md); [module/data/item/templates/socialStandingData.js](files/module/data/item/templates/socialStandingData.js.md); [module/setup/config.js](files/module/setup/config.js.md); [module/setup/registerDataModels.js](files/module/setup/registerDataModels.js.md); [module/setup/registerSheets.js](files/module/setup/registerSheets.js.md); [module/setup/handlebars.js](files/module/setup/handlebars.js.md); [module/scripts/helper.js](files/module/scripts/helper.js.md); [module/scripts/rollConfig.js](files/module/scripts/rollConfig.js.md); [module/scripts/rolls/extendedRoll.js](files/module/scripts/rolls/extendedRoll.js.md); [module/chatMessage/chatMessageData.js](files/module/chatMessage/chatMessageData.js.md); [module/scripts/investigation/rollClue.js](files/module/scripts/investigation/rollClue.js.md). Исторические записи предыдущих проверок сохранены; устаревшие текущие ограничения ActorSheet/rollClue и контекст issue-00015 уточнены.

### Изолированное исполнение

Одноразовые сценарии выполнялись из памяти через `node --input-type=module`; тестовые файлы/стенд в репозитории не создавались. Загрузчик использовал установленные Foundry common DataModel/TypeDataModel/fields/utils, Roll и term-классы, Peggy-парсер, Handlebars 4.7.9 и parse5. Выполнены настоящие системные модели и методы, включая Log, modifierMixin, _prepareCustomSkills и _onItemInlineEdit. `getArmorEcumbrance`, core getSpeaker, selectOptions/prepareSelectOptionGroups/formGroup и системные helpers прочитаны до определений и подключены к сценариям. Последний прогон завершился успешно: **22 группы / 22 пройдены**; предупреждение Node MODULE_TYPELESS_PACKAGE_JSON относится к способу импорта исходников.

Подменены документные Actor/Item и коллекции, Application/Sheet/HandlebarsApplicationMixin-оболочки, диалоги, запись Actor/Item/ChatMessage, fulfillment/RollResolver и низкоуровневые createSelectInput/createCheckboxInput/createFormGroup. Оболочка родителя моделей наследует настоящий DataModel, чтобы fieldPath отражал system. Грани кубиков задавались очередью; случайное распределение не проверялось. Roll/парсер, расчёт моделей и вызываемые методы не переписаны под ожидаемый результат. Список modifiers в старых сценариях внедрялся явно: это вход для проверки ветвей, не поддерживаемая схема.

| Группа | Проверка | Наблюдённый результат |
| --- | --- | --- |
| 01 | SkillItemData: 8 полей, default/coercion, неизвестный modifiers | attribute='' и value=0; произвольный атрибут и value='-1.5' приняты; NaN отклонён; modifiers отброшен и при new, и при updateSource. |
| 02 | WitcherSkillItemSheet и core selectOptions | 9 исходных характеристик; dex selected; два поля name/system.attribute; два prepare добавляют два класса item-skill (визуальный дефект не установлен). |
| 03 | Встроенные броски семи характеристик | По awareness/brawling/athletics/physique/charisma/alchemy/courage: грань 5 + характеристика 7 + навык 2 =14; threshold=14 даёт false. |
| 04 | Monster.dontAddAttr | При тех же значениях результат 5+2=7; характеристика по исходнику всё равно читается до сборки формулы. |
| 05 | EC, эффекты и пользовательская добавка | EC=3 вычтен из трёх магических навыков, не из контрольного обычного; реальный modifierMixin, группа allSkills и запрос −1 дали составной результат 18. Проверены flavor-детали. |
| 06 | Социальная матрица и Race | equal/tolerated/hated/feared/toleratedFeared/hatedFeared: charisma 0/−1/−2/−1/−2/−3; остальные три EMP-навыка 0/−1/−2/0/−1/−2; intimidation 0/0/0/+1/+1/+1. Monster пуст; Race.north=hated сам не меняет Actor.general. |
| 07 | Собственный бонус, имя и старый массив | 5+8+3=16 при собственных activeEffectModifiers=4; Item.name=awareness подключил встроенные +7 и дал 23; неизвестное имя проигнорировало allSkills=2. Явно внедрённый старый modifiers +2/−1 дал 17. |
| 08 | Ошибки и отмена собственного броска | Пустой/неизвестный attribute, отсутствующий Item ID и неверное событие дали TypeError; отмена getCustomModifier отклонила Promise без сообщения. |
| 09 | Обычные IP и стоимость | Уровни 0/2/10/−2, max(value,1), costMultiplier. При уровне 2/IP=0 payload уровня 3 и баланса −2; alchemy=2 стоит 4. Уровень 10 повышается до 11 как факт кода, без утверждения о правиле потолка. |
| 10 | Магические IP и настоящий Log | Стоимость 4 при magic=10: Log.update на 6, затем levelUpSkill.update на 10; при magic=1: 0 и 1, обычный расход 3; при magic=0 стоимость покрывают обычные IP. |
| 11 | Ожидание обновлений | Оба update удержаны незавершёнными Promise; levelUpSkill завершился до записей. Исход гонки на сервере не установлен. |
| 12 | Неизвестный ключ и общий язык | rollSkill('commonspeech') считает 14, но не включает собственную +4 из-за addActiveEffects(commonsp); helper с commonspeech находит добавку. rollSkill('commonsp') и оба написания в levelUpSkill ломаются в разных lookup. |
| 13 | Сумма навыков и подписи | 52 свежих модели уровня 1 дают 52 при отсутствующем label; сериализованные данные с заполненными миграцией подписями дают 64 в en/ru. isVisible/флаги не влияют, пустая коллекция даёт 0. |
| 14 | Листовые события | Привязаны rollSkill/level-up и старые события; pannels инвертирован. Глобальная jQuery стала объектом; отсутствие binding в отдельном ES-module сценарии дало ReferenceError; unknown custom key не прошёл builtin lookup. |
| 15 | Собственные события и схема | Проверены шесть регистраций; toggle isOpened; delete вызван без ожидания; add payload {name:'Modifier',value:0} без ID, модель modifiers не принимает. |
| 16 | CRUD старого массива с некорректными ID | Массив внедрён явно в обход модели: отсутствие списка бросает TypeError, неизвестный ID удаления снимает последний элемент; edit пишет строку '-3', неизвестная строка бросает TypeError. |
| 17 | Действующий tab-skills и Items | 52 встроенных навыка дают 104 строки (all+группа). int Item даёт две пустые строки с именем как builtin key; подготовленные spd/luck Items не выводятся. |
| 18 | Встроенные строки текущая/старая | Проверены знаки 0/отрицательных значений, приоритет класса и независимые три иконки. isVisible=false не скрывает текущую строку, но полностью скрывает старую monster-строку. |
| 19 | Старый monster-skill-tab и Item-строка | 7 таблиц, pannels, Item ID и custom-rollable, inline value, открытый отрицательный activeEffectModifiers. Нулевой бонус скрыт; add/edit/delete modifiers кнопок нет. |
| 20 | Конфигурация видимости и настоящий formGroup | Настоящая MonsterData с Actor DataModel-родителем: 51 checkbox с полными system.skills.*.isVisible именами и техническими подписями; один пропущенный commonspeech DataField и ошибка helper. |
| 21 | edit-skills и повышение монстра | Правильные @root.skillKey пути value/трёх флагов, число кнопок по группе, commonsp; неизвестная группа пустая. У Monster кнопки есть, обычный/магический levelUpSkill бросают TypeError из-за logs/magic. |
| 22 | Числовое inline-редактирование Item | Настоящий _onItemInlineEdit выдал payload system.value='-2.5'; настоящая NumberField привела к −2.5. |

Дополнительно разобраны JSON en/ru для всех буквальных WITCHER-ключей 14 файлов: семь старых WITCHER.Actor.Skill.* отсутствуют в обоих языках, текущий WITCHER.skills.levelUp — только в ru. Существующие CRA label и общий язык сопоставлены с прежними issues. parse5 удаляет tr/td внутри div редактора, сохраняя input; без установленного влияния на пользователя отдельное issue для этого не создавалось. Повторное добавление CSS-класса листа также не объявлено подтверждённым дефектом.

### Проблемы и границы результата

| Проблема | Наблюдение |
| --- | --- |
| [issue-00187](../../issues/potential/issue-00187.md) | Текущая строка собственного навыка использует контекст и бросок встроенного навыка |
| [issue-00188](../../issues/potential/issue-00188.md) | Собственные навыки со СКОР и УДАЧЕЙ не попадают на текущую вкладку навыков |
| [issue-00189](../../issues/potential/issue-00189.md) | Обработчики модификаторов собственного навыка не согласованы со схемой Item |
| [issue-00190](../../issues/potential/issue-00190.md) | Бросок собственного навыка игнорирует его активную добавку и зависит от имени встроенного навыка |
| [issue-00191](../../issues/potential/issue-00191.md) | Повышение навыка списывает обычные IP при недостаточном балансе |
| [issue-00192](../../issues/potential/issue-00192.md) | Редактор навыков монстра предлагает повышение без необходимых данных развития |
| [issue-00193](../../issues/potential/issue-00193.md) | В шаблонах навыков отсутствуют отдельные ключи локализации |

Старый CRUD не представлен текущими кнопками; issue-00189 описывает несогласованные методы и схему, а не действующий сценарий кликов. issue-00192 касается кнопки автоматического повышения в отдельной конфигурации; прежняя issue-00030 — общей IP-вкладки. Ни один issue не переведён в open/closed. Предложения решений не считаются согласованными.

Не запускались мир/служба, браузерные формы, сохранение в БД, многоклиентская синхронизация и сторонние модули. Не установлен итог гонки двух Actor.update. Нет выводов о правилах максимума навыков, допустимости отрицательных/дробных уровней и выбранной политике IP сверх того, что делает код. Character/MonsterSheet, WitcherModifiersConfiguration и полный бой не получают полного покрытия через этот анализ; .030 продолжит предусмотренную часть. Все новые JS-сущности и методы описаны; partial/поля и найденные потребители сверены встречным чтением.

### Формальная проверка документации и сохранности

Проверка одноразовым Python-скриптом завершена: 621 путь реестра совпадает с Git и фактическим деревом после исключений; каждый исходник побайтно совпадает с HEAD и срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. SHA256 набора исходников — `52701d3d0a5f054319886ac2a9d45b42c26c80098858d02518579c6a1edfaec4`, без изменений. Сохранены mode/uid/gid/inode всех 1150 отслеживаемых файлов; SHA256 снимка метаданных — `b672b83132a0ee76f848b865cc3ac959dba9c39ae5312ac690404274b9ab45f4`.

Проверены 238 карточек, 30 подзадач и отсутствие пересечений их списков; .001–.029 done, .030 planned. Встречная сверка охватила 304 прямых импорта: 204 default, 93 named-import statements с 98 именами и 7 namespace; в новой порции 4 импорта. Все 148 буквальных ссылок на HBS существуют, новой порцией добавлены 5 связей. Для импортов и шаблонов проверены исходящие ссылки, определения экспортов и обратные ссылки уже описанных потребителей.

Проверены 493 Markdown-документа под docs и два корневых документа: 10793 локальные ссылки и якоря разрешаются; таблицы и завершающие пробелы проверены, `git diff --check` прошёл. Изменены 68 документов: 47 существующих и 21 новый (14 карточек, 7 issues); все изменения ограничены docs. Старый журнал сохранён побайтно после добавления новой записи; исходный SHA256 — `20176c3877c9dc9aa0fcc8e5c8e3d04d6fed65cef782f18d62a3a585cc9f5a6a`. Исходники, игровые данные и метаданные доступа не менялись; коммит, сборка и запуск службы не выполнялись.

## TASK-0003.028

2026-09-11. Выполнена [TASK-0003.028](../../tasks/task-0003.028.md) на `rusbar-main`, `9f16a7ae4bc942df85a105fd37d9a3cb3ef99f4b`. На старте рабочее дерево чистое: 1139 отслеживаемых файлов, 219 карточек из 621, 180 potential issues. Перечень пяти файлов и 372 логических строк совпал с планом; записи кода не выполнялись.

### Полный охват

| Исходник | Строк | Описание | Результат |
| --- | --- | --- | --- |
| [module/scripts/rollConfig.js](../../../module/scripts/rollConfig.js) | 19 | [Карточка](files/module/scripts/rollConfig.js.md) | Полностью прочитан и сверен |
| [module/scripts/rolls/extendedRoll.js](../../../module/scripts/rolls/extendedRoll.js) | 107 | [Карточка](files/module/scripts/rolls/extendedRoll.js.md) | Полностью прочитан и сверен |
| [module/scripts/rolls/fumble.js](../../../module/scripts/rolls/fumble.js) | 119 | [Карточка](files/module/scripts/rolls/fumble.js.md) | Полностью прочитан и сверен |
| [module/scripts/helper.js](../../../module/scripts/helper.js) | 106 | [Карточка](files/module/scripts/helper.js.md) | Полностью прочитан и сверен |
| [module/chatMessage/chatMessageData.js](../../../module/chatMessage/chatMessageData.js) | 21 | [Карточка](files/module/chatMessage/chatMessageData.js.md) | Полностью прочитан и сверен |

Созданы пять полных карточек, уточнены 13 связанных: [module/item/witcherItem.js](files/module/item/witcherItem.js.md), [module/item/systems/repair.js](files/module/item/systems/repair.js.md), [module/actor/witcherActor.js](files/module/actor/witcherActor.js.md), [module/scripts/investigation/rollClue.js](files/module/scripts/investigation/rollClue.js.md), [module/scripts/statusEffects/applyStatusEffect.js](files/module/scripts/statusEffects/applyStatusEffect.js.md), [module/scripts/temporaryEffects/applyActiveEffect.js](files/module/scripts/temporaryEffects/applyActiveEffect.js.md), [module/TheWitcherTRPG.js](files/module/TheWitcherTRPG.js.md), [module/actor/sheets/WitcherActorSheetV1.js](files/module/actor/sheets/WitcherActorSheetV1.js.md), [module/actor/sheets/WitcherActorSheet.js](files/module/actor/sheets/WitcherActorSheet.js.md), [module/setup/config.js](files/module/setup/config.js.md), [module/setup/settings.js](files/module/setup/settings.js.md), [module/setup/queries.js](files/module/setup/queries.js.md), [module/setup/registerDataModels.js](files/module/setup/registerDataModels.js.md). Соседние модели сообщений, боевые/словесные примеси и полные листы просматривались до используемых определений, без добавления к покрытию.

### Среда и границы исполнения

Сценарии выполнены одноразовым `node --input-type=module` через stdin, без файлов тестового стенда. Node 24.16.0; `/opt/foundryvtt/package.json` — Foundry 14.367.0. Импортированы настоящие пять файлов и AttackMessageData/DefenseMessageData/BaseMessageData с настоящими DataModel/fields Foundry. Настоящие Roll, RollParser, RollTerm/DiceTerm/Die/NumericTerm/OperatorTerm и другие term-классы загружены из `/opt/foundryvtt/client/dice`; parser скомпилирован в памяти Peggy из установленной `grammar.pegjs`. Формулы и вычисления не переписаны в проверке.

Грани задавались через CONFIG.Dice.fulfillment handler с проверкой допустимого значения и исчерпания очереди; приложение RollResolver представлено фасадом. Это проверка арифметики и повторного x10 с заданными гранями, не проверка генератора случайности. Roll.toMessage, ChatMessage.create/setFlag заменены наблюдаемыми фасадами, часть Promise удерживалась до явного разрешения. Для speaker выполнены оригинальные getSpeaker и три private helper из `client/documents/chat-message.mjs`; Actor/Token/Scene представлены минимальными классами, а game/canvas/коллекции — контролируемыми данными.

DialogV2.input/prompt представлены фасадами; обработчик кнопки getCustomModifier исполнен из настоящего helper. Поведение закрытия input отдельно сверено с `client/applications/api/dialog.mjs:369–427`: default rejectClose=false → null. Проверены регистрации меню ChatLog и ApplicationV2._createContextMenu: jQuery=false; legacy callback получает HTMLElement. Сам ContextMenu в браузере не запускался. Локализация возвращала ключи для проверки ветвей; содержимое таблиц сопоставлено статически с en/ru. getRandomInt проверен с временной заменой Math.random и её восстановлением.

### Фактические сценарии

| Группа | Предмет | Вход / действие | Наблюдаемый результат |
| --- | --- | --- | --- |
| 01 | RollConfig | Девять default-полей, options={}, {showResult:false,threshold:99}, null | {} даёт undefined showResult; дополнительные options не применяются; null → TypeError. |
| 02 | ChatMessageData | Ссылки входных system/flags, append, speaker/type | append поверхностный: вложенные ссылки общие, namespace заменяется; незаданный flavor + строка даёт undefinedsuffix. |
| 03 | Обычный/числовой бросок | 1d10+8 при 5; константа 0 | 13 с исходными dice; константа 0 без критической ветви. |
| 04 | Повторный крит | 1d10+8 при гранях 10;10,10,3; reversal | 41; options.crit=true, итоговый Roll без dice. Reversal меняет CSS, знак прибавления сохраняет. |
| 05 | Провал и минимум | 1d10+8 при 1;10,10,3 и 1;3; 1d10-8 при 1;2 | 0 с fumbleAmount=23; 6 с amount=3; отрицательный исходный total также ограничивается нулём. |
| 06 | Первый результат / showCrit | Отключённый крит; d20=10, d6=1, 2d10kh1 с первым неактивным 1 | showCrit=false оставляет исходный итог; faces/active не проверяются. Это контракт общего метода, не заявленный сбой стандартного 1d10. |
| 07 | Сравнения | 4/5/6 при threshold=5 × defense/reversal: 12 комбинаций | Строгие >/< для обычного режима, >=/<= для defense; rollOver и тексты успеха/неудачи соответствуют направлению. |
| 08 | Крайние пороги и showSuccess | threshold 0/-1/-3/undefined; showSuccess=false | При 0 сравнение включено; отрицательные/undefined отключают options.success и оформление; showSuccess не читается. |
| 09 | Отложенное сообщение | showResult=false, отдельный flags и mutation system | toMessage не вызывается; roll.messageData === входной объект; отдельный аргумент flags не применяется. |
| 10 | Ожидание сообщения и флагов | Удержанные Promise toMessage/setFlag; array/object/null | toMessage удерживает extendedRoll, setFlag — нет. После разрешения setFlag данные появляются; обе формы flags работают при showResult=true. |
| 11 | Настоящий парсер | +-2, ++-2, ++2, (-2), пропущенный оператор и незакрытая скобка; отсутствующий system | Корректные знаки дали 3/3/7/3 при грани 5; два неверных выражения отклонены. Отсутствие messageData.system → TypeError. |
| 12 | Все таблицы провала | 70 случаев: 7 маршрутов × 0/1/5/6/7/8/9/10/11/23; все melee/rangedSkills | Выявлены сдвиги ranged 7/9, armed defense 9 и пропуск unarmed 9. Spell перекрывает обычную таблицу; неизвестный skill без spell → undefined. |
| 13 | Контекстное меню | BaseMessageData/неизвестный/subclass, rolls=[], отсутствие message, неверный event | При fumble=true неподдерживаемые constructor видимы, callback без действия; пустой rolls скрывает; неверное сообщение/dataset → TypeError. |
| 14 | speaker | Реальные UUID-поля моделей и getSpeaker ядра; Actor A/назначенный B/без character | UUID A в fumble даёт B либо пользователя; корректный объект A в контрольном вызове даёт A; отсутствующий UUID также fallback. |
| 15 | Выбор Actor/токена | Первый controlled, character, 0/1/>1 кандидатов, NPC без player owner, отмена/удалённый ID | 0 → уведомление и undefined; null input → TypeError; >1 выбор ID работает; нет character для getCurrentToken → TypeError. |
| 16 | Владелец и query | Активный OWNER/GM/отсутствие обоих; настоящий applyStatusEffectToActor | OWNER приоритетнее GM; без обоих null. Не-owner Actor приводит к TypeError до query, если получателя нет. |
| 17 | Случайное целое | Math.random=0 и 1−EPSILON; max=2/6/10/100, дополнительно 0/undefined | Корректные границы 1..max; max=0 → 1, undefined → NaN. Распределение случайности не проверено. |
| 18 | Модификатор | addPart:0/'0'/-2, детализация, callback prompt и отмена | Ноль скрывается, -2 → '+-2' с опциональной подписью. Prompt получает title/rejectClose=true, отмена отклоняет Promise. |

Все 18 групп завершились без падения утверждений после настройки фасадов. Первые подготовительные попытки bootstrap потребовали исправить синтаксис фасада, добавить CONFIG.Dice.termTypes и RollResolver.addTerm; эти ошибки относились к окружению проверки и не регистрировались как дефекты системы. Node вывел MODULE_TYPELESS_PACKAGE_JSON при импорте ES-модулей: файлы успешно разобраны, package.json не изменён.

### Перекрёстная сверка

- RollConfig сопоставлен со всеми 12 импортирующими файлами: extendedRoll читает восемь полей, showSuccess оставлен без потребителя; WitcherItem импортирует класс для JSDoc. Передаваемые конфигурации обычных навыков, спасбросков, защиты, заклинаний, изготовления и ремонта сверены по местам вызова.
- extendedRoll имеет 12 импортирующих файлов. Разделены собственно вычисление, отложенный вывод в defense/castSpell/realCraft/repair и дополнительные flags словесного боя. Пропущенный оператор issue-00033 и незакрытая скобка условной ветви issue-00103 сопоставлены с настоящим парсером; штатный ремонт не исполнялся и по-прежнему останавливается раньше на настройке.
- ChatMessageData сверена с 13 импортирующими файлами и двумя append в защите. speaker/type после append сохраняются; system/flags сливаются поверхностно. Текущие append в защите не получают содержательных конфликтующих flags, поэтому отдельная issue о потере их namespace не заведена. _onCritRoll обоих базовых листов не использует append/extendedRoll: отсутствие flavor там не объявлено видимым undefinedsuffix.
- fumble: два default import доведены до настоящих классов и UUID/StringField; CONFIG.WITCHER.meleeSkills/rangedSkills — до определений, таблицы — до переводов. Строгое сравнение constructor, видимость, диапазоны и fallback speaker проверены независимо. Обработчик создаёт только текст; правила книги и фактическое применение последствий не исследовались.
- helper: проверены все восемь экспортов и 16 импортирующих файлов, включая randomHuman/randomMonster (10), случайную сторону защиты (2), последствия травмы (6), вероятность Item-эффекта (100), модификаторы, улики, ремонт, боевые/словесные действия, статусы и временные эффекты. getCurrentToken не имеет найденного внешнего вызова. Некорректный max не передаётся найденными потребителями. Guard выбора Actor в executeDefense/repair отделён от отсутствующих guard в других действиях; отмена внутри helper предшествует им.

Структурная проверка точных WITCHER-ключей пяти файлов нашла все используемые строки в en и один пропуск в ru: WITCHER.Dialog.customModifier. Регистрация ru подтверждена system.json; стандартный английский fallback сверён с client/helpers/localization.mjs:234–236, 434–445. Это отдельная статическая проверка, не девятнадцатая группа исполнения и не проверка переводов сторонних модулей.

### Проблемы и ограничения

Зарегистрированы [issue-00181](../../issues/potential/issue-00181.md) — границы таблиц провала пропускают и сдвигают отдельные результаты; [issue-00182](../../issues/potential/issue-00182.md) — результат провала передаёт UUID вместо Actor при выборе отправителя; [issue-00183](../../issues/potential/issue-00183.md) — пункт результата провала виден у сообщений без поддерживаемого обработчика; [issue-00184](../../issues/potential/issue-00184.md) — общий бросок завершается до сохранения дополнительных флагов сообщения; [issue-00185](../../issues/potential/issue-00185.md) — делегирование действия не обрабатывает отсутствие активного владельца или GM; [issue-00186](../../issues/potential/issue-00186.md) — подпись модификатора отсутствует в русском словаре. Дополнены [issue-00008](../../issues/potential/issue-00008.md), [issue-00033](../../issues/potential/issue-00033.md), [issue-00103](../../issues/potential/issue-00103.md), [issue-00126](../../issues/potential/issue-00126.md), [issue-00149](../../issues/potential/issue-00149.md), [issue-00175](../../issues/potential/issue-00175.md). Все 186 карточек остаются potential; воспроизведение агентом не заменяет подтверждение пользователя и не разрешает исправления.

Полный разбор skillMixin и остальных примесей/схем не завершался за рамками пяти файлов. Мир, браузер, службы и сетевые клиенты не запускались; игровые документы и БД не читались и не менялись. Не утверждаются соответствие рулбуку, качество случайного распределения, продолжительность гонки setFlag или доступ службы к ресурсам. Итоговые ограничения перенесены в карточки и задачу.

### Формальная проверка

Проверка одноразовым Python-скриптом завершена: 621 путь реестра совпадает с Git и фактическим деревом после исключений; каждый исходник побайтно совпадает с HEAD и срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. SHA256 набора исходников — `52701d3d0a5f054319886ac2a9d45b42c26c80098858d02518579c6a1edfaec4`, без изменений. Сохранены mode/uid/gid/inode всех 1139 отслеживаемых файлов; SHA256 снимка метаданных — `632c31aa8e12a78a2991eae5cfb13e1a619f2967911a86f394aab926aba77f28`.

Проверены 224 карточки, 30 подзадач и отсутствие пересечений их списков; .001–.028 done, .029–.030 planned. Встречная сверка охватила 300 прямых импортов: 203 default, 90 named-import statements с 95 именами и 7 namespace; в новой порции 3 импорта. Все 143 буквальные ссылки на HBS существуют, новой порцией они не добавлены. Для импортов и шаблонов проверены исходящие ссылки, определения экспортов и обратные ссылки уже описанных потребителей.

Проверены 472 Markdown-документа под docs и два корневых документа: 10247 локальных ссылок и якорей разрешаются; таблицы и завершающие пробелы проверены, `git diff --check` прошёл. Изменён 41 документ: 30 существующих и 11 новых (5 карточек, 6 issues); все изменения ограничены docs. Старый журнал сохранён побайтно после добавления новой записи; исходный SHA256 — `161e8362cc9b69186ad5ac842c8ce7db4dfe0b4e05491930fe54025d523d257d`. Исправлений кода, прав доступа, коммитов, сборки и запуска службы не выполнялось.

Покрытие: **224 из 621**, **397** не разобраны. В третьей серии выполнены .021–.028 на **56 из 79** файлов, две задачи на **23** файла остаются planned; ещё **374** требуют детализации. [Следующая задача — TASK-0003.029](../../tasks/task-0003.029.md); она не начиналась. TASK-0003 остаётся in-progress, TASK-0004/0005 — draft.

## TASK-0003.027

Дата: 2026-09-11. Ветка `rusbar-main`, HEAD `ce0c7eb7069b215b641d725913b3aae21502e811`. На старте рабочее дерево чистое; отслеживаются 1122 файла. Исходники сверяются со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`.

### Объём и результат

По [TASK-0003.027](../../tasks/task-0003.027.md) полностью прочитаны 12 HBS-файлов, 1375 логических строк. Созданы 12 карточек, уточнены 25 связанных. Покрытие — 219 из 621, не разобраны 402. В третьей серии проверен 51 из 79 файлов; в очереди 28, ещё 374 требуют детализации. Следующая задача — [TASK-0003.028](../../tasks/task-0003.028.md), общий бросок, критические результаты и вспомогательные функции; выполнение не начато.

| Файл | Карточка | Логических строк |
| --- | --- | --- |
| [templates/sheets/actor/tabs/tab-inventory.hbs](../../../templates/sheets/actor/tabs/tab-inventory.hbs) | [Описание](files/templates/sheets/actor/tabs/tab-inventory.hbs.md) | 247 |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-alchemical.hbs](../../../templates/sheets/actor/partials/character/inventory/tab-inventory-alchemical.hbs) | [Описание](files/templates/sheets/actor/partials/character/inventory/tab-inventory-alchemical.hbs.md) | 88 |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-armors.hbs](../../../templates/sheets/actor/partials/character/inventory/tab-inventory-armors.hbs) | [Описание](files/templates/sheets/actor/partials/character/inventory/tab-inventory-armors.hbs.md) | 135 |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-components.hbs](../../../templates/sheets/actor/partials/character/inventory/tab-inventory-components.hbs) | [Описание](files/templates/sheets/actor/partials/character/inventory/tab-inventory-components.hbs.md) | 75 |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-diagrams.hbs](../../../templates/sheets/actor/partials/character/inventory/tab-inventory-diagrams.hbs) | [Описание](files/templates/sheets/actor/partials/character/inventory/tab-inventory-diagrams.hbs.md) | 114 |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-mounts.hbs](../../../templates/sheets/actor/partials/character/inventory/tab-inventory-mounts.hbs) | [Описание](files/templates/sheets/actor/partials/character/inventory/tab-inventory-mounts.hbs.md) | 65 |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-runes-glyphs.hbs](../../../templates/sheets/actor/partials/character/inventory/tab-inventory-runes-glyphs.hbs) | [Описание](files/templates/sheets/actor/partials/character/inventory/tab-inventory-runes-glyphs.hbs.md) | 67 |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-valuables.hbs](../../../templates/sheets/actor/partials/character/inventory/tab-inventory-valuables.hbs) | [Описание](files/templates/sheets/actor/partials/character/inventory/tab-inventory-valuables.hbs.md) | 101 |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-weapons.hbs](../../../templates/sheets/actor/partials/character/inventory/tab-inventory-weapons.hbs) | [Описание](files/templates/sheets/actor/partials/character/inventory/tab-inventory-weapons.hbs.md) | 131 |
| [templates/sheets/actor/partials/character/inventory/inventory-items-summary.hbs](../../../templates/sheets/actor/partials/character/inventory/inventory-items-summary.hbs) | [Описание](files/templates/sheets/actor/partials/character/inventory/inventory-items-summary.hbs.md) | 23 |
| [templates/sheets/actor/partials/monster/tabs/tab-inventory.hbs](../../../templates/sheets/actor/partials/monster/tabs/tab-inventory.hbs) | [Описание](files/templates/sheets/actor/partials/monster/tabs/tab-inventory.hbs.md) | 16 |
| [templates/partials/monster/monster-inventory-tab.hbs](../../../templates/partials/monster/monster-inventory-tab.hbs) | [Описание](files/templates/partials/monster/monster-inventory-tab.hbs.md) | 313 |

### Методика и пределы

Все шаблоны прочитаны целиком, включая повторные блоки прежней брони. Выписаны введённая разметка, поля, each/if/unless/partial, контексты ../ и ../../, DOM-селекторы и внешние методы. Проверены определения моделей, producer-методов Character/Monster/общего ActorSheet, helpers, регистрации листов и загрузки шаблонов. Эти точечные чтения не добавили полных карточек соседей; MountData, листы Character/Monster, алхимия/производство, валюта/награды и экспорт остаются за дальнейшими порциями.

Изолированные сценарии исполнялись через node --input-type=module со stdin, без тестовых файлов. Использовались настоящие Handlebars 4.7.9/parse5, Foundry DataModel/fields, модели Item системы, itemMixin/ContextMenu, registerHandelbarHelpers, craftingMixin/alchemyMixin, выбранные исходные методы подготовки контекста и Actor.getTotalWeight. Для проверки формулы исполнялись настоящее тело _craftingCraft и callback, ChatMessageData и RollConfig; realCraft заменён приёмником аргументов. Core concat/localize извлечены из /opt/foundryvtt/client/applications/handlebars.mjs без изменения тела, _loc/game.i18n представлены словарным фасадом. Core Localization.localize просмотрен локально для fallback. Версии Foundry 14.367.0, Node 24.16.0.

Actor/Item базовые документы, коллекции, settings, DOM-события, окна и операции записи представлены ограниченными фасадами. Типы system-моделей настоящие; полная подготовка документов/листов не запускалась. Имена навыков для callback заданы явно, поскольку фасад не выполняет всю подготовку Actor. Browser, DragDrop, внешний CSS-рендер, эффекты, бросок, списание/изготовление/ремонт, экспорт Actor, мир, БД и сеть не запускались.

При настройке сценариев исправлены только входные подмены: граница извлечения Array.prototype, некорректный короткий UUID, ожидание общего числа input вместо семи валют, закрытые флаги девяти панелей, Boolean вместо CSV настройки и отсутствующая подготовленная label навыка. После этого завершены все 19 групп. Эти ошибки сценариев не зарегистрированы как ошибки системы.

### Изолированные проверки

| Группа | Сценарий | Результат |
| --- | --- | --- |
| 01 | 12 шаблонов; 8 категорий × 0/1/2 Item × false/true флаги; 32 комбинации summary | Все компилируются. Количество строк/inline quantity совпало; hasQuantity влияет на заголовок, не ввод строки; subtype не становится атрибутом. |
| 02 | Weapon: accuracy -2/0/2, equipped, isAmmo, ремонт и description | Положительная accuracy имеет +, остальные скрыты. type.text показан; описание экранировано; hasQuantity наследуется summary. |
| 03 | Armor: SP, resistance, цвета, отсутствие data-type | SP7/10,5/10,0/10 дали green/orange/red, подписи ног перепутаны. Undefined dataset.type привёл реальный выбор улучшения в armor/glyph. |
| 04 | Вложенные улучшения и TypedObject effects | 25% показаны, 0% скрыты, оба name сохранены; img-запись и пустой объект дают Item/слот. Текущий Item.type=enhancement скрывает блок улучшений. |
| 05 | Алхимия/мутаген | Effect label по ../itemType, minorMutation, время и токсичность показаны; effect HTML экранирован. |
| 06 | Компоненты/нулевые значения | Quantity='0', строковые rarity/forage='0' остаются; location показано. Data-subtype отсутствует после двух partial. |
| 07 | Рецепт: ../ и ../../, UUID/компоненты/вещества | getOwnedComponentCount получил Actor и вывел 6/3, включая stored; алхимический count дал 5/2. Выключение isFormulae скрыло только список веществ; HTML description сохранён. |
| 08 | MountData | dex='0'/control/speed дали 3 тега при hp=0; hp5 добавил четвёртый. |
| 09 | ContainerData | 2×3 веса → storedWeight6/max12. Вложенный details несёт UUID, не имеет .item и отдельного ввода quantity. |
| 10 | Character: пустые данные, валюты, stored/hidden/carried | 0 строк Item и 7 currency-input. Hidden carried учитывается; stored скрыт, not-carried не даёт веса. Вес 4, totalCost6; цена не отображается отдельным итогом. |
| 11 | Все категории Character и 9 панелей веществ | 45 Item по подтипам рецептов/ценностей/алхимии/компонентов/mount/mutagen/container/enhancement: при открытых панелях каждый показан один раз. При weight9/10/11 и ENC10 overweight включён при 10/11. |
| 12 | Современный Monster | Две ремонтные кнопки и один data-action exportLoot; регистрация ремонта найдена только Character. Свободный weapon-enhancement появился в weapons и loots. |
| 13 | Старый Monster, все 5 location и пустой список | Head/Torso/Leg/FullCover/Shield отрендерены. Quantity добычи '1d6' читается правильно через текущий system. Старые flat SP отсутствуют в модели; экспортная ссылка без data-action. |
| 14 | Локализация | 114 статических ключей, WITCHER.Weapon.Availability отсутствует в en/ru. У 10 из 13 подтипов рецепта нет TYPES.Item.* в en. Четыре подписи веса — строковые литералы. |
| 15 | Кнопка изготовления формулы | Настоящий _craftingCraft при CRA5/crafting2/alchemy8 передал realCraft-приёмнику 5+2 и craftingDC; пять требуемых vitriol не участвовали в предварительной проверке. |
| 16 | Core concat/localize | Настоящие helper из Foundry с фасадом _loc/game.i18n: tooltip остался WITCHER.Weapon.Availability, тип формулы — TYPES.Item.potion. |
| 17 | Отрендеренные поля → itemMixin | Восемь таблиц направили quantity='3' в Item.update; equipped/isCarried/learned переключены. Img='' остаётся пустым, шаблон fallback не добавляет. |
| 18 | Неизвестные lookup/нули/валюта | Отсутствующие поля не сломали рендер; hp0 скрыт, dex='0' показан. Настоящий calcCurrencyWeight для 1001 монеты с Actor.getTotalWeight дал 2. При отсутствии itemType плюсика нет. |
| 19 | Все корректные словари и legacy resistance | Проверены 4 Availability,4 Concealment,4 hands,5 craftingLevels. Реальное head.stoppingPower5/max10 не заполнило старый headStopping; resistance.slashing=true не отметило старый checkbox. |

### Перекрёстная сверка и поправка к прежней записи

Современная строка брони не содержит data-type="armor". В TASK-0003.026 DOM-фасад задавал этот атрибут явно; описание в карточках itemMixin/ArmorData и формулировка журнала .026 ошибочно перенесли его в HBS. По полному чтению и рендеру .027 установлено: dataset.type=undefined, поэтому _chooseEnhancement выбирает else с armor/glyph. У оружия data-type=weapon есть. Две прежние карточки исправлены; исторический текст журнала сохранён, данная запись уточняет его. CSS-класс enhancement-weapon-slot у брони сам по себе не является причиной неправильного выбора.

Проверены 25 связанных карточек: [module/actor/sheets/WitcherActorSheet.js](files/module/actor/sheets/WitcherActorSheet.js.md); [module/actor/witcherActor.js](files/module/actor/witcherActor.js.md); [module/data/actor/commonActorData.js](files/module/data/actor/commonActorData.js.md); [module/data/item/commonItemData.js](files/module/data/item/commonItemData.js.md); [module/data/item/containerData.js](files/module/data/item/containerData.js.md); [module/data/actor/templates/common/currencyData.js](files/module/data/actor/templates/common/currencyData.js.md); [module/setup/handlebars.js](files/module/setup/handlebars.js.md); [module/setup/config.js](files/module/setup/config.js.md); [module/actor/sheets/mixins/itemMixin.js](files/module/actor/sheets/mixins/itemMixin.js.md); [module/data/item/alchemicalData.js](files/module/data/item/alchemicalData.js.md); [module/data/item/mutagenData.js](files/module/data/item/mutagenData.js.md); [module/data/item/valuableData.js](files/module/data/item/valuableData.js.md); [module/actor/sheets/interactions/itemContextMenu.js](files/module/actor/sheets/interactions/itemContextMenu.js.md); [module/data/item/armorData.js](files/module/data/item/armorData.js.md); [module/data/item/templates/armor/spData.js](files/module/data/item/templates/armor/spData.js.md); [module/data/item/templates/armor/resistanceData.js](files/module/data/item/templates/armor/resistanceData.js.md); [module/data/item/enhancementData.js](files/module/data/item/enhancementData.js.md); [module/data/item/componentData.js](files/module/data/item/componentData.js.md); [module/data/item/diagramData.js](files/module/data/item/diagramData.js.md); [module/item/witcherItem.js](files/module/item/witcherItem.js.md); [module/data/item/templates/itemEffectData.js](files/module/data/item/templates/itemEffectData.js.md); [module/data/item/weaponData.js](files/module/data/item/weaponData.js.md); [module/data/item/templates/weaponTypeData.js](files/module/data/item/templates/weaponTypeData.js.md); [templates/partials/item-image.hbs](files/templates/partials/item-image.hbs.md); [module/setup/registerSheets.js](files/module/setup/registerSheets.js.md). Сведения о вызовах и полях дополнены встречными ссылками на полные карточки новых шаблонов. Строки реестра соседей вне порции не меняли статус.

Сводный partial не суммирует инвентарь: он выводит header и условные подписи. Непереданные явно hasQuantity/spellType наследуются от контекста; subtype доходит до summary, но отсутствует в DOM. HBS современных категорий не фильтрует stored/hidden; это делает producer, причём hidden сохраняется. Вложенный UUID контейнера не является ID встроенного Item, а .stored-item не является .item. Кнопка рецепта использует .crafting-craft, не обработчик associated-diagram; issue-00080 не переносилась на этот путь.

Из улучшений отображаются словари effects, но рендер не вызывает applyStatus и не устраняет issue-00084/00089. В текущем Monster есть data-action=exportLoot; в старом partial только class export-loot. Сам preload старого шаблона не доказывает его использование в зарегистрированном V2. Разные представления/исходы отделены от предположений об игровых правилах.

### Наблюдения

Пять новых карточек зарегистрированы только в potential:

| Issue | Наблюдение |
| --- | --- |
| [issue-00176](../../issues/potential/issue-00176.md) | Кнопка изготовления формулы запускает ремесленный обработчик |
| [issue-00177](../../issues/potential/issue-00177.md) | Кнопки ремонта инвентаря монстра не имеют подключённого обработчика |
| [issue-00178](../../issues/potential/issue-00178.md) | Подписи инвентаря обращаются к отсутствующим ключам локализации |
| [issue-00179](../../issues/potential/issue-00179.md) | Подписи веса инвентаря и контейнеров обходят локализацию |
| [issue-00180](../../issues/potential/issue-00180.md) | Старый инвентарь монстра читает и редактирует устаревшие поля брони |

Дополнены [issue-00007](../../issues/potential/issue-00007.md), [issue-00063](../../issues/potential/issue-00063.md), [issue-00080](../../issues/potential/issue-00080.md), [issue-00084](../../issues/potential/issue-00084.md), [issue-00089](../../issues/potential/issue-00089.md), [issue-00101](../../issues/potential/issue-00101.md), [issue-00166](../../issues/potential/issue-00166.md), [issue-00173](../../issues/potential/issue-00173.md). Воспроизведение агентом не заменяет подтверждения пользователя. Изменение статуса и исправление не выполнялись.

Отсутствующий заголовок Quantity у современной брони, скрытая неположительная accuracy и пересечение enhancement в списках Monster описаны как фактические особенности; отдельная необходимость изменения этих представлений не объявлялась доказанной. Тройные скобки description рецепта и экранирование StringField других таблиц зафиксированы, но сами по себе не квалифицированы как ошибка.

### Формальная проверка

Автоматическая сверка завершена без ошибок:

- Реестр содержит 621 исходник и совпадает с Git/файловой системой после согласованных исключений. Все исходники побайтово совпали с текущим HEAD и срезом TASK-0001.
- 219 карточек соответствуют статусу «Проверено», 402 файла имеют статус «Не начат». Для 12 новых карточек проверены обязательные разделы, версия и буквальные поля name/data-field. Списки 30 подзадач не пересекаются: .001–.027 выполнены, .028–.030 остаются planned.
- Проверены 297 прямых импортов уже описанных JS: 201 default, 89 именованных statements с 94 именами и 7 namespace; в новой порции JS нет. Проверены существование целей, экспорты и встречные упоминания в описанных карточках.
- Проверены 143 буквальные связи с HBS, в том числе 21 связь из новой порции. Все цели существуют, исходящие ссылки и встречные связи уже описанных потребителей согласованы.
- Все 180 ID проблем последовательны и находятся в potential. Пять новых карточек имеют обязательные разделы; 25 дополнений карточек файлов и восемь дополнений issues присутствуют по одному разу.
- Проверены 461 Markdown-документ внутри docs и два корневых справочных документа: 9977 локальных ссылок и их якоря. Таблицы изменённых файлов и git diff --check прошли.
- Изменены только 61 документ: 44 ранее отслеживаемых и 17 новых. Mode/uid/gid/inode всех 1122 отслеживаемых файлов совпадают со стартовыми. Общие хеши исходников/метаданных не изменились; прежний журнал, включая .026, сохранён дословно.

SHA-256 набора исходников: `52701d3d0a5f054319886ac2a9d45b42c26c80098858d02518579c6a1edfaec4`. Формальные проверки подтверждают целостность документации и неизменность кода, а не работу игрового мира.

Исходники и игровые данные не менялись. Сборка, запуск службы, коммит и изменение прав не выполнялись. Историческая часть журнала сохранена дословно.

## TASK-0003.026

Дата: 2026-09-11. Ветка `rusbar-main`, HEAD `45a63062a2bd55939fef430609fc5dddc350b0e9`. На старте рабочее дерево чистое; отслеживаются 1112 файлов. Исходники сверяются со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`.

### Объём и результат

По [TASK-0003.026](../../tasks/task-0003.026.md) полностью разобраны два JS-файла, 528 логических строк. Созданы две карточки, уточнены 13 связанных. Покрытие — 207 из 621; не разобраны 414. В третьей серии выполнены 39 из 79, в очереди 40; ещё 374 требуют детализации. Следующая порция — [TASK-0003.027](../../tasks/task-0003.027.md), вкладки и таблицы инвентаря Actor; выполнение не начато.

| Файл | Карточка | Логических строк |
| --- | --- | --- |
| [module/actor/sheets/mixins/itemMixin.js](../../../module/actor/sheets/mixins/itemMixin.js) | [Описание](files/module/actor/sheets/mixins/itemMixin.js.md) | 344 |
| [module/actor/sheets/interactions/itemContextMenu.js](../../../module/actor/sheets/interactions/itemContextMenu.js) | [Описание](files/module/actor/sheets/interactions/itemContextMenu.js.md) | 184 |

### Методика и пределы

Оба файла прочитаны целиком: 19 методов itemMixin, 23 привязки событий, 15 методов itemContextMenu и шесть пунктов меню. Проверены импорты, композиция в листах, селекторы/dataset/closest, условия, вызовы, возвращаемые Promise и изменения Item/Actor. Внешние определения просмотрены до используемого поведения. Частичное чтение WitcherLootSheet, dismantlingMixin, socketMessage и HBS не создаёт полных карточек и не увеличивает покрытие; таблицы инвентаря остаются за .027.

Изолированные сценарии запускались через node --input-type=module со stdin, без создания тестовых файлов. Импортированы реальные itemMixin, itemContextMenu, WitcherItem, emitForGM, socketHook, модели Item и общие модели Foundry; методы getList/addItem/removeItem/removeItemsOfType/useItem Actor извлечены из исходника. Настоящие ContextMenu._onClickItem и ChatMessage.getSpeaker с вспомогательными приватными методами исполнялись в минимальных классах. Базовый Item построен на реальном DataModel с дополнительными полями/доступом к родителю; Actor, коллекции, DOM/$, окна, игровые глобальные объекты и операции записи представлены фасадами. Реальный Handlebars и parse5 проверяли выход шаблонов.

Версии: Foundry VTT 14.367.0, Node 24.16.0, Handlebars 4.7.9. Локально проверены /opt/foundryvtt/client/applications/ux/context-menu.mjs, applications/api/dialog.mjs, applications/sheets/actor-sheet.mjs, appv1/sheets/actor-sheet.mjs и documents/chat-message.mjs. Полный core ContextMenu не создавался и не рисовался; выполнялся метод его диспетчеризации. Полный алгоритм core сортировки прочитан, а в сценарии проверена делегация к нему.

Ранняя неполнота Item.implementation в фасаде и ошибочное ожидание 24 вместо 23 listener исправлены только во входных сценариях; затем прошла 21 группа. Мир, браузер, настоящие документы/БД, эффекты лечения, сетевой обмен и службу не запускали. Последствия gift/removeEnhancement/dismantle проверялись также прямым вызовом, поскольку обычный вход через контекстное меню блокируется перепутанными аргументами. Синхронно завершающаяся подмена update использована только для границ порядка; её результат не доказательство такого порядка настоящего Foundry update.

### Изолированные проверки

| Группа | Сценарий | Фактический результат |
| --- | --- | --- |
| 01 | Построение ContextMenu | Шесть пунктов, два onClick и четыре callback, jQuery=false, selector .item. |
| 02 | Настоящий core _onClickItem | Edit/delete получают нужную цель; removeEnhancement выдаёт TypeError, async gift/dismantle отклоняются из-за неверного второго аргумента. |
| 03 | Предикаты меню | Отсутствующий Item безопасно скрывает условные пункты; consume зависит от isConsumable, remove от applied, gift от девяти типов, dismantle от associatedDiagramUuid. |
| 04 | Drop/права/сортировка | Не owner→false; документ того же Actor делегируется сортировке; преобразование legacy drop в toObject теряет parent; неразрешимый drop приводит к TypeError. |
| 05 | Monster/weapon | Подготовленное equipped становится true, но source/toObject и переданная в создание копия сохраняют false; количество нового экземпляра по умолчанию 1. |
| 06 | Уникальные типы/профессия | Проверены race/profession/homeland; pending delete не ожидается обёрткой. Неизвестный professionSkill формирует путь с undefined, повторяя прежнее наблюдение. |
| 07 | Создание Item | Проверены presets spell, component, valuable и ветка diagram; реальная модель показывает различие singular diagram и зарегистрированного diagrams. |
| 08 | HBS кнопки добавления | Подтип компонента не попадает в dataset из сводного partial; spellType=Master сохраняется через унаследованный контекст. |
| 09 | Переключатели/inline | Переключаются equipped/isCarried/learned; строка false становится true, строка true — false; остальные значения передаются без такого преобразования. |
| 10 | DOM/listeners | 23 привязки, сворачивание через заданные классы; показ картинки обращается к preventDefault без вызова. Текущий маршрут старого partial ограничен статической сверкой. |
| 11 | Roll/delete/pannels | Передаются alt/ctrl/shift; вложенные операции не ожидаются; проверены пути pannels по spelltype/subtype. |
| 12 | Выбор улучшения | Фильтры weapon/rune и armor/glyph, stored/applied; пустой список сохраняет OK, callback падает при отсутствии select. Отмена с rejectClose по умолчанию даёт null. |
| 13 | Установка/стек/повтор | Количество применяемого экземпляра становится 1, остаток клонируется через addItem(force=true). Повтор добавляет тот же ID, количество 0 тоже меняется на 1. Разные подмены момента завершения update отделены от реального порядка. |
| 14 | Снятие улучшения | Прямой вызов снимает applied и удаляет ID из родительского Item; без внешнего DOM-родителя первая запись инициирована до ошибки второй. |
| 15 | Передача | Прямой gift не ждёт создания у получателя; нет GM→списание продолжается; при передаче себе на последней единице возможно удаление по прежнему остатку. Отмена rejectClose=true и отсутствующий GM-получатель проверены отдельно. |
| 16 | Socket | Настоящие emitForGM/socketHook формируют/разбирают envelope addItem; получение не подтверждается отправителю. Сеть и выполнение на другом клиенте заменены фасадами. |
| 17 | Расходование | При количествах 2/1/0 обёртка инициирует consume и затем уменьшение/удаление, не дожидаясь завершения consume; реальные лечащие эффекты не исполнялись. |
| 18 | Разборка | Настоящий метод разрешает recipe/components через подменённый fromUuid; количества 5→2 и 0→1, найденный компонент передаётся addItem, источник — removeItem. Контекстная обёртка не ждёт результата. |
| 19 | Сообщение Item | Настоящий item-description.hbs получает item/type/config; текст effect экранируется. Обработчик передаёт в speaker имя Actor; отсутствие .list-item выявляется отдельно. |
| 20 | Настоящий getSpeaker | Строка имени не распознаётся как Actor: используется контролируемый токен/персонаж пользователя/пользователь; экземпляр Actor сохраняет отправителя владельца Item. |
| 21 | Частичный отказ/устаревшие ссылки | Pending/rejected parent update не препятствует обновлению улучшения; ID заранее меняется в живом массиве. Исчезнувший выбранный Item вызывает ошибку после push; отсутствующие Item у прямых consume/remove дают TypeError. |

### Контракт ContextMenu Foundry 14.367.0

| Пункт | Свойство меню | Фактический вызов core | Сигнатура системы | Результат сверки |
| --- | --- | --- | --- | --- |
| Edit | onClick | event, target | pointerEvent, target | Совпадает |
| Consume | onClick | event, target | pointerEvent, target | Совпадает |
| Remove enhancement | callback | target, event | pointerEvent, target | Перепутано |
| Gift | callback | target, event | pointerEvent, target | Перепутано |
| Dismantle | callback | target, event | pointerEvent, target | Перепутано |
| Delete | callback | target, event | event — один аргумент | Работает с DOM-целью, несмотря на имя аргумента |

Условия visible получают target и не страдают от этой перестановки. jQuery=false означает DOM, а не jQuery-объект. Эти выводы основаны на установленном коде core и исполнении его метода, а не на сходстве названий callback/onClick.

### Перекрёстная сверка связей

Уточнены 13 ранее разобранных карточек: WitcherActorSheet, WitcherActorSheetV1, witcherActor, witcherItem, config, socketHook, consumeMixin, EnhancementData, WeaponData, ArmorData, ComponentData, ProfessionData, DiagramData. Встречные сведения описывают конкретного потребителя/операцию; полные карточки не создавались для точечно прочитанных соседей.

Проверены три прямых импорта порции: WITCHER из config, default WitcherItem и named emitForGM. Прослежены Object.assign, вызовы document methods, UUID/socket, поля моделей и пути pannels. Единственная буквальная HBS-ссылка внутри этих двух исходников — item-description.hbs; DOM-контракты других шаблонов сверены по местам их определения. Путь .list-item в действующих строках существует. Класс enhancement-weapon-slot в броне сам по себе не меняет выбор: тип берётся у внешнего .item с data-type=armor. Эти случаи не зарегистрированы как ошибки.

Из известных проблем дополнены [issue-00034](../../issues/potential/issue-00034.md), [issue-00045](../../issues/potential/issue-00045.md), [issue-00049](../../issues/potential/issue-00049.md), [issue-00063](../../issues/potential/issue-00063.md), [issue-00080](../../issues/potential/issue-00080.md), [issue-00116](../../issues/potential/issue-00116.md), [issue-00153](../../issues/potential/issue-00153.md), [issue-00166](../../issues/potential/issue-00166.md). Заголовок issue-00153 обобщён на inline-редакторы улик и инвентаря; прежнее наблюдение сохранено.

### Новые наблюдения

Все восемь карточек имеют статус potential, без пользовательского подтверждения и исправления.

| Issue | Наблюдение |
| --- | --- |
| [issue-00168](../../issues/potential/issue-00168.md) | Три callback контекстного меню ожидают аргументы в порядке onClick. |
| [issue-00169](../../issues/potential/issue-00169.md) | Передача списывает источник без подтверждения получения; отсутствие GM и передача себе рассмотрены отдельно. |
| [issue-00170](../../issues/potential/issue-00170.md) | При отсутствии доступных улучшений остаётся кнопка с callback, которому нужен отсутствующий select. |
| [issue-00171](../../issues/potential/issue-00171.md) | Установка улучшения меняет несколько документов независимо; нет проверки количества/повтора и общего результата. |
| [issue-00172](../../issues/potential/issue-00172.md) | Monster drop устанавливает equipped только на подготовленной модели, копия использует source. |
| [issue-00173](../../issues/potential/issue-00173.md) | Кнопка создания компонента не передаёт subtype своей группы. |
| [issue-00174](../../issues/potential/issue-00174.md) | Контекстное расходование не ограничивается положительным количеством. |
| [issue-00175](../../issues/potential/issue-00175.md) | Сообщение Item передаёт имя вместо документа Actor в getSpeaker. |

Plain StringField/textarea для effect/description и двойные скобки HBS не доказывают обещания rich text; экранирование не оформлялось как отдельная неисправность. Различие имён singular diagram/diagrams описано как фактическая недостижимая специализация текущего preset, без вывода, что общая кнопка рецепта обязана создавать алхимическую формулу. Старый маршрут показа картинки и missing preventDefault() отмечены в issue-00063 с ограничением достижимости.

### Формальная проверка

Автоматическая сверка пакета завершена без ошибок:

- Реестр содержит ровно 621 исходник; множество совпадает с Git и файловой системой после согласованных исключений. Для всех проверено побайтовое совпадение с текущим HEAD и срезом TASK-0001.
- 207 карточек соответствуют статусу «Проверено», у 414 файлов разбор не начат. У двух новых карточек проверены 11 разделов, версия и охват собственных методов. Перечни 30 подзадач не пересекаются: .001–.026 выполнены, .027–.030 стоят в очереди.
- Проверены 297 прямых импортов описанных JS: 201 default, 89 именованных statements с 94 именами и 7 namespace; в новой порции три импорта. Проверены определения экспортов, исходящие и встречные ссылки для уже описанных соседей. Также сверены 122 буквальные связи с HBS, из них одна в новой порции.
- Реестр проблем содержит 175 последовательных ID в potential. Все восемь новых карточек имеют обязательные разделы; 13 уточнений прежних карточек файлов и восемь дополнений issues присутствуют ровно по одному разу.
- Проверены 444 Markdown-документа внутри docs и два справочных корневых документа: 9400 локальных ссылок, файлы-цели и Markdown-якоря. Таблицы изменённых документов и git diff --check прошли. Один фрагмент динамического JS-вызова оформлен как код, чтобы он не интерпретировался как Markdown-ссылка.
- Изменены только 42 документа: 32 ранее отслеживаемых и 10 новых. mode/uid/gid/inode всех 1112 отслеживаемых файлов совпадают со стартом; хеши исходников и метаданных не изменились. Прежний текст журнала, включая планирование и сверку .025, сохранён дословно.

SHA-256 общего набора исходников: `52701d3d0a5f054319886ac2a9d45b42c26c80098858d02518579c6a1edfaec4`. Эти проверки подтверждают целостность документации и неизменность кода; они не являются проверкой запуска мира.

Исходники, игровые данные, Git-история, mode/uid/gid/inode отслеживаемых файлов не изменялись. Историческая часть журнала сохранена дословно. Сборка, запуск мира, исправление кода и коммит не выполнялись.

## TASK-0003.025

Дата: 2026-09-11. Ветка `rusbar-main`, HEAD `a2670a0a10c62b28d836b1a57577c4836f14cf20`. На старте рабочее дерево чистое; отслеживаются 1106 файлов. Исходники сверяются со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`.

### Объём и результат

По [TASK-0003.025](../../tasks/task-0003.025.md) полностью разобраны два JS-файла, 625 логических строк. Созданы две карточки, уточнены 13 связанных. Покрытие — 205 из 621; не разобраны 416. В третьей серии выполнены 37 из 79, в очереди 42; ещё 374 требуют детализации. Следующая порция — [TASK-0003.026](../../tasks/task-0003.026.md), выполнение не начато.

| Файл | Карточка | Логических строк |
| --- | --- | --- |
| [module/actor/sheets/WitcherActorSheet.js](../../../module/actor/sheets/WitcherActorSheet.js) | [Описание](files/module/actor/sheets/WitcherActorSheet.js.md) | 323 |
| [module/actor/sheets/WitcherActorSheetV1.js](../../../module/actor/sheets/WitcherActorSheetV1.js) | [Описание](files/module/actor/sheets/WitcherActorSheetV1.js.md) | 302 |

### Методика и пределы

Оба файла прочитаны целиком: собственные методы, поля, Array.prototype, Object.assign, порядок подготовки, события и внешние определения. Прослежены регистрации, два наследника V2 и отдельные Loot/Mystery, актуальные PARTS и контекст HBS. Все 11 объектов примесей проверены по export и точкам listener; полное покрытие ещё не разобранных примесей не добавлялось.

Изолированные сценарии запускались через `node --input-type=module` со stdin, без создания тестовых файлов. Исполнялись собственные тела классов: строки import/экспорт заменены для помещения в минимальное окружение, внешние базовые классы заменены фасадами. Реальные модели Foundry и системы импортированы из checkout, реальные getList/getTotalWeight и core Actor.allApplicableEffects извлечены из исходников; ChatMessageData импортирован. Примеси извлечены как объекты; skillMixin для отдельной проверки импортирован настоящим ES module. Game/Actor/коллекции/DOM/$/TextEditor/Roll/DialogV2/update/toMessage представлены явно заданными фасадами; ни одна игровая запись не выполнялась. Ранняя ошибка синтаксиса фасада, форма documentTypes и отсутствовавшие TYPES/_onSkillDisplay исправлены только во входном сценарии; затем все 17 групп прошли. Код системы не менялся.

Версии: Foundry VTT 14.367.0 из /opt/foundryvtt/package.json, Node 24.16.0. Foundry API просмотрен локально: ActorSheetV2._onRender/_canDragDrop, V1 ActorSheet.getData, Actor.allApplicableEffects/rollInitiative, DocumentSheetV2._onRender. Наличие доступа к коду не подтверждает работу HTTP/службы. Мир, браузер, настоящие записи, полный combat, внешние модули и частичный рендер не запускались. Отмена prompt словесного боя проверена только статически до rejectClose=true; сам общий handler лишь делегирует и не ждёт Promise.

### Изолированные проверки

| Группа | Сценарий | Фактический результат |
| --- | --- | --- |
| 01 | Класс, поля, опции, Object.assign | 11 примесей V2, 10 V1 без currency; имена не пересекаются. statMap/skillMap ссылаются на CONFIG. |
| 02 | Пустые Character/Monster и оба API | Списки и суммы пусты/0; у V2 system совпадает с моделью, у V1 — отдельная копия. Только V2 имеет criticalWounds. |
| 03 | isStored/isHidden/isCarried, sort, вес/стоимость | stored исключён; hidden остаётся. Не carried входит в цену, но не вес. Цена 10, вес 2; actor.items не переставлен. |
| 04 | Array.sum/cost | Пустой массив→0; строковые числа преобразуются; дробная цена округляется по итогу. Нечисловое значение→NaN; нет system→TypeError; оба свойства enumerable. |
| 05 | Собственные навыки | int-группа сохраняет исходный порядок, не sort. Пустой и неизвестный attribute не попадают в группы. spd создаёт группу, но основной HBS перебирает семь system.skills. |
| 06 | Магия | 20 сочетаний четырёх level/пяти class; по 3 novice/journeyman/master, 4 MagicalGift. stored исключён, hex/ritual выделены. |
| 07 | Оружие, броня, улучшения, контейнеры | weapon/armor и unapplied enhancement с соответствующим type; rune/glyph отдельно, applied исключён, контейнер найден. |
| 08 | Слоты оружия и воздействия | Реальные WeaponData/EnhancementData/DamageProperties: 2 улучшения и эффекта до подготовки, 1 после при enhancements=1. Source и 2 ID сохранены. Пустые 2 слота и повтор проверены. |
| 09 | Броня V1/V2 | V1 создаёт [{},{}], V2 не меняет enhancementItems. Это различие собственных методов, не вывод о подключении V1. |
| 10 | Обогащение травм | Реальные CriticalWoundData/createEnrichedText: value/enriched/systemField по UUID; отказ enrich отклоняет подготовку V2. V1 обогащение не вызывает. |
| 11 | Категории ActiveEffect | Реальный core allApplicableEffects и категории: один e при transfer+isTransferred даёт [e,e]. Комбинации transfer/stored и disabled проверены. |
| 12 | События жизни | Оба настоящих handler для key=10 сформировали isOpened=true. V2 ожидает массив с key и падает на неизвестном key; V1 читает объект. Преобразование массива задано отдельно, полный CharacterSheet не запускался. |
| 13 | STA | При 9/10, REC=3 передаётся 12; Full Recovery→10; при >=max — уведомление без записи. Callback завершён при pending update. Реальная модель принимает 12 при max=10. |
| 14 | Инициатива, критический бросок, словесный бой, конфигурация | Переданы createCombatants/rerollInitiative=true, формула 1d10x10, evaluate({async:true}), ChatMessageData(type=base,speaker.actor=a). Вложенные операции/диалог не ожидаются. Отсутствие configuration безопасно. |
| 15 | DOM-контракт | V2 передаёт DOM, V1 html[0]. Семь общих привязок: шесть click и focusin; 11/10 входов примесей, super render/listeners и select проверены. Сами внешние listeners в этой группе перехвачены. |
| 16 | Реальный ES module skillMixin | skillListener заменил глобальный jQuery объектом, после чего jQuery(el) дал TypeError. $ и DOM подменены; это не выполненный сценарий реального browser. |
| 17 | temporaryHpSum и повтор | 2+3→5; в V2 сумма на подготовленной модели, в V1 только на копии. Повтор даёт 5, source обоих вариантов неизменен. |

### Отличия V2 и V1

| Свойство | WitcherActorSheet V2 | WitcherActorSheetV1 |
| --- | --- | --- |
| Подключение | Character/Monster через extends и registerSheets | Импорт/наследник/регистрация не найдены |
| Основной контекст | async _prepareContext, await шести _prepare* | Синхронный getData и синхронные _prepare* |
| system | Ссылка actor.system; systemFields | Копия actor.toObject(false).system; без systemFields |
| Item и notes | Живые ссылки | Тоже живые ссылки, несмотря на копию system |
| Травмы | Promise.all enrichedText, словарь description по UUID | Обогащения нет |
| Броня | Фильтр без padding | Фильтр и padding enhancementItems |
| События жизни | find по key в массиве от CharacterSheet | Индексирование объекта по dataset.event |
| Listeners | DOM; 11 примесей, включая валюту; _onRender ждёт super | jQuery; 10 примесей получают html[0]; super.activateListeners |
| Array | Определяет enumerable sum/cost при загрузке | Только использует cost; не импортирует определение |
| Drop | Внешний V2 _canDragDrop=isEditable; itemMixin._onDropItem дополнительно проверяет owner | Override _canDragStart/_canDragDrop всегда true; itemMixin проверяет owner |

### Промежуточная сверка TASK-0003.021–TASK-0003.025

Сопоставлены полные перечни 37 файлов пяти порций, карточки и реестр. Прежние 168 карточек — отдельное непересекающееся множество, вместе ровно 205. Для всех 37 повторно прочитаны определения экспортов и наличие соответствующего описания; для всех 205 проверяются направления прямых imports и literal HBS. Содержательно сопоставлены следующие границы:

| Порция | Файлов | Связь | Результат и предел |
| --- | --- | --- | --- |
| .021 | 13 | Магические Item → листы/конфигурация → Actor.getList → общий контекст | SpellData.class/level и type hex/ritual сверены с _prepareSpells; description/enriched не создаёт числовых эффектов. Общие Item/attack/defense и прежние карточки не пересчитаны как новые. |
| .022 | 5 | Магия → регионы → события → Actor/Token | Региональный pipeline остаётся отдельным от подготовки списка заклинаний. Полные карточки .022 и связи с .021 проверены; их прежние воспроизведения сохранены, регионы заново не создавались. |
| .023 | 14 | Расследование → отдельный MysterySheet → Item clue/obstacle → rollSkill | MysterySheet не наследует общий WitcherActorSheet. Наличие общего WitcherActor не означает одинаковый UI/контекст; карточки и регистрация типов сопоставлены. |
| .024 | 3 | Container.content/isStored → CommonItem.calcWeight → Actor → лист | Основной список листа исключает stored; вес использует общий расчёт, стоимость — свой список. Ссылки на исходный Item и потеря вложенного веса остаются выводами .024, не устранены контекстом. |
| .025 | 2 | CommonActor/Item/ActiveEffect → общий V2 → Character/Monster | Обогащение травм, группы effects, живые system/Item, padding оружия, DOM-примеси; V1 без потребителя. Полные соседние Character/Monster/Loot и новые примеси ещё не засчитаны. |

Это промежуточная сверка документации и выбранных процессов; она не объявляет заново исполненными все сценарии .021–.024. Содержательные результаты прежних порций сохранены в их записях ниже. Уже назначенные .026–.030 остаются planned, новые задачи не создавались. Неизвестные полного разбора: Character/Monster/Loot, itemMixin/contextMenu, stat/skill/customSkill/note/currency и потребители чата — по дальнейшему согласованному плану.

### Уточнённые карточки и проблемы

| Карточка | Область сверки |
| --- | --- |
| [module/setup/registerSheets.js](files/module/setup/registerSheets.js.md) | Встречные связи общего листа; уточнение TASK-0003.025 |
| [module/setup/handlebars.js](files/module/setup/handlebars.js.md) | Встречные связи общего листа; уточнение TASK-0003.025 |
| [module/actor/witcherActor.js](files/module/actor/witcherActor.js.md) | Встречные связи общего листа; уточнение TASK-0003.025 |
| [module/actor/sheets/mixins/activeEffectMixin.js](files/module/actor/sheets/mixins/activeEffectMixin.js.md) | Встречные связи общего листа; уточнение TASK-0003.025 |
| [module/actor/sheets/mixins/criticalWoundMixin.js](files/module/actor/sheets/mixins/criticalWoundMixin.js.md) | Встречные связи общего листа; уточнение TASK-0003.025 |
| [module/actor/sheets/mixins/healMixin.js](files/module/actor/sheets/mixins/healMixin.js.md) | Встречные связи общего листа; уточнение TASK-0003.025 |
| [module/data/item/weaponData.js](files/module/data/item/weaponData.js.md) | Встречные связи общего листа; уточнение TASK-0003.025 |
| [module/data/item/armorData.js](files/module/data/item/armorData.js.md) | Встречные связи общего листа; уточнение TASK-0003.025 |
| [module/data/item/criticalWoundData.js](files/module/data/item/criticalWoundData.js.md) | Встречные связи общего листа; уточнение TASK-0003.025 |
| [module/data/actor/characterData.js](files/module/data/actor/characterData.js.md) | Встречные связи общего листа; уточнение TASK-0003.025 |
| [module/data/actor/monsterData.js](files/module/data/actor/monsterData.js.md) | Встречные связи общего листа; уточнение TASK-0003.025 |
| [templates/sheets/actor/partials/character/tab-effects.hbs](files/templates/sheets/actor/partials/character/tab-effects.hbs.md) | Встречные связи общего листа; уточнение TASK-0003.025 |
| [module/activeEffect/witcherActiveEffect.js](files/module/activeEffect/witcherActiveEffect.js.md) | Встречные связи общего листа; уточнение TASK-0003.025 |

Новые [issue-00164](../../issues/potential/issue-00164.md) — Восстановление STA за действие может превысить максимум; [issue-00165](../../issues/potential/issue-00165.md) — Список эффектов листа дублирует перенесённое временное улучшение; [issue-00166](../../issues/potential/issue-00166.md) — Подготовка листа оружия обрезает установленные улучшения и их воздействия; [issue-00167](../../issues/potential/issue-00167.md) — Обработчик навыков заменяет глобальную функцию jQuery объектом. Все остаются potential. Дополнены [issue-00024](../../issues/potential/issue-00024.md), [issue-00054](../../issues/potential/issue-00054.md), [issue-00084](../../issues/potential/issue-00084.md), [issue-00109](../../issues/potential/issue-00109.md), [issue-00127](../../issues/potential/issue-00127.md). Регистрация входит в пункт 9 TASK-0003; подтверждение пользователем и исправления отсутствуют.

### Формальная проверка и сохранность

Python-сверка прошла: 621 путь реестра совпадает с Git и фактическим деревом после согласованных исключений. Все 621 исходник побайтово совпадают с HEAD и срезом TASK-0001; SHA-256 набора `52701d3d0a5f054319886ac2a9d45b42c26c80098858d02518579c6a1edfaec4` сохранён. Для 1106 отслеживаемых файлов сохранены mode/uid/gid/inode; хеш метаданных `3b0cd5df2f149e2f2bb3c52b7b9dd6ceb5b4e6d5bb502c974c9755b02a3991da` не изменился.

Проверены 205 карточек и 416 строк «Не начат», 30 подзадач (.001–.025 done, .026–.030 planned), родитель in-progress и заготовки TASK-0004/TASK-0005. По третьей серии: 37 проверены, 42 в очереди, 374 не распределены. 167 issues имеют непрерывные ID и остаются в potential.

Сверены 294 прямые import-связи, включая 23 у новых файлов: 200 default, 87 именованных import-выражений с 92 именами, 7 namespace. Проверены существование экспортов и встречные записи уже описанных потребителей. Сохранены 121 literal HBS-связь; у двух общих классов собственных путей HBS нет. Определения и зависимости в карточках проверялись отдельно от поведения.

Проверены 434 Markdown-документа внутри docs и два корневых: 9183 локальные ссылки, якоря, колонки изменённых таблиц, завершающие пробелы и git diff --check — без ошибок. Изменены ровно 35 согласованных документов: 29 существующих и 6 новых (2 карточки и 4 issues). Прежний хвост журнала и разделы планирования сохранены побайтово. Коммит, сборка, исправления исходников, изменение службы/БД и метаданных доступа не выполнялись.

## TASK-0003.024

Дата: 2026-09-11. Ветка `rusbar-main`, HEAD `66cd03705dbc398eba0026284a298b5fbe337035`. На старте рабочее дерево чистое, отслеживаются 1095 файлов. Код сверяется со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`.

### Объём и результат

По [TASK-0003.024](../../tasks/task-0003.024.md) полностью разобраны три файла: два JS и один HBS, 136 логических строк. Созданы три карточки, уточнены восемь связанных. Реестр содержит 203 проверенных файла и 418 неразобранных. В третьей серии проверены 35 из 79, 44 в очереди; 374 требуют дальнейшей детализации. Следующая задача — [TASK-0003.025](../../tasks/task-0003.025.md), выполнение не начато.

| Файл | Карточка | Логических строк |
| --- | --- | --- |
| [module/data/item/containerData.js](../../../module/data/item/containerData.js) | [Описание](files/module/data/item/containerData.js.md) | 43 |
| [module/item/sheets/WitcherContainerSheet.js](../../../module/item/sheets/WitcherContainerSheet.js) | [Описание](files/module/item/sheets/WitcherContainerSheet.js.md) | 54 |
| [templates/sheets/item/container-sheet.hbs](../../../templates/sheets/item/container-sheet.hbs) | [Описание](files/templates/sheets/item/container-sheet.hbs.md) | 39 |

### Методика и пределы

Все три файла прочитаны полностью. Сопоставлены наследование CommonItemData/WitcherItemSheet, определения моделей/листов, поддерживаемые типы манифеста, prepared itemContent, поля и кнопки HBS, общий Drop, isStored, getList/getTotalWeight, добавление и удаление Item. Действия инвентаря проверены точечно, полный разбор itemMixin.js не выполнялся и покрытие его файла не увеличено.

Изолированный запуск: `node --input-type=module` со скриптом через stdin. Node **24.16.0**, Foundry **14.367.0**, Handlebars **4.7.9**, parse5. Настоящие CommonItemData/ContainerData и поля Foundry, WitcherItemSheet/WitcherContainerSheet/WitcherConfigurationSheet. Базовый ItemSheetV2 и HandlebarsApplicationMixin заменены фасадами; _prepareContext, _onDrop, _onDropDocument и контейнерные методы исполнялись без переписывания их тела.

Подменены родители и коллекции Item/Actor, UUID-источники, create/update/delete, fromDropData, DragDrop, UI/DOM и helpers настроек общей шапки. Управляемые Promise фиксировали pending и отказ каждой записи; отклонения перехватывала проверка, не система. Настоящие Actor.getList/getTotalWeight и _onItemDelete из itemMixin извлечены целиком для локальных сценариев. Валюта Actor заменена нулевым вкладом. Реальная БД, мир, сетевые операции, изменение документов и прав не выполнялись.

fromUuidSync ядра дополнительно исполнен с parseUuid/CompendiumCollection-фасадами: холодная коллекция возвращала индекс без system. Это проверка ветви ядра после разбора UUID, не валидности тестовых UUID и не загрузка действующего pack. Настоящий _safePrepareData ядра исполнен с Hooks.onError-фасадом и зарегистрировал ошибку подготовки без повторного выброса. Частичный itemContent/storedWeight не объявлен отказом создания или загрузки всего Item.

Настоящий контейнерный HBS и общий item-header скомпилированы вместе. parse5 проверял HTML-строки, поля, disabled-значения и data-uuid. Custom elements, click и submitOnChange в браузере не исполнялись. Вместимость carry не трактовалась как согласованный запрет перегрузки.

### Контракты ядра и зависимостей

| Источник | Проверенное свойство |
| --- | --- |
| `/opt/foundryvtt/common/abstract/type-data.mjs`:153, 250 | Базовые prepareDerivedData и _onDelete пусты |
| `/opt/foundryvtt/client/documents/abstract/client-document.mjs`:276–285, 313–320 | Вызов system.prepareDerivedData; _safePrepareData журналирует исключение |
| `/opt/foundryvtt/client/utils/helpers.mjs`:188–214 | fromUuidSync возвращает документ, индекс или null; strict embedded-компедиум может бросить исключение |
| `/opt/foundryvtt/client/documents/abstract/client-document.mjs`:539–556 | Удаление передаётся TypeDataModel._onDelete |
| `/opt/foundryvtt/client/documents/item.mjs`:100–103 | Item._onDelete вызывает super и очищает реестр ActiveEffect; семантики content здесь нет |
| `/opt/foundryvtt/client/applications/sheets/item-sheet.mjs`:127–139 | Базовый Drop вызывает dropItemSheetData и учитывает false; системный override его пропускает |

Поиск module/templates показал: content/isStored изменяются контейнерным листом, специальной очистки связей при удалении контейнера нет. Это не утверждение об обработчиках внешних модулей или данных мира. Регистрация ContainerData/ContainerSheet и девять допустимых типов сверены статически; регистрационные API в этой порции не запускались.

### Изолированные проверки

Завершены **14 групп**:

| Группа | Сценарий | Фактический результат |
| --- | --- | --- |
| 01 | Схема и defaults | 11 полей: 8 общих + carry/storedWeight/content; defaults 0/0/[]; строковая quantity; malformed/повторные ссылки и отрицательная дробная carry допускаются |
| 02 | Пустой/валидный контейнер, повторная подготовка и двойной UUID | Пустой список []; предмет 2×3 даёт 6; повторный prepare не накапливает вес; две одинаковые ссылки дают 12 и две строки |
| 03 | Missing UUID, индекс компедиума, safe-wrapper | После валидной ссылки остаются вес 6/одна строка, missing даёт TypeError; индекс без system также даёт TypeError; ядро перехватывает ошибку подготовки |
| 04 | Флаги, quantity и общий вес Actor | Оболочка 2×2 + содержимое 6 даёт 10; !isCarried/isStored обнуляет вклад; quantity контейнера 0 оставляет содержимое 6; isCarried содержимого не участвует в storedWeight |
| 05 | Типы, повторный Drop и вместимость | Все девять типов объявлены; null/spell пропущены; повтор в том же content не добавлен; carry1 не помешала storedWeight6 |
| 06 | Две незавершённые/отклонённые записи | Drop/извлечение вернулись раньше update, prepared-массив уже изменён; отказ каждой записи не формирует общий возвращаемый результат |
| 07 | Один Item в двух контейнерах | Обе ссылки остаются; вес 17 при оболочках 2/3 и одном содержимом 6; снятие первой ссылки сбрасывает flag при сохранённой второй |
| 08 | Самоссылка и цикл | Допущены; stored-флаги исключают контейнеры из прямого веса; рекурсивного вычисления/переполнения стека нет |
| 09 | Вложенный заполненный контейнер | Outer1 + inner2 + leaf6 дают итог 3: содержимое inner не входит в сумму outer |
| 10 | Внешний источник и parent | World Item и Item другого Actor с isOwner=false переданы в update как исходные документы; UUID/parent сохранены, копии нет |
| 11 | Извлечение valid/missing/nonmember/duplicate | Удаляется первая ссылка; nonmember всё равно получает isStored=false; missing меняет массив и запускает update контейнера до TypeError |
| 12 | Удаление контейнера | Настоящий _onItemDelete с фасадом delete оставил Item stored; getList его не показывает, вес 0; базовый _onDelete модели не освобождает содержимое |
| 13 | Общий Drop, права листа, hook и Actor-ветвь | isEditable=false останавливает; Item-override работает и dispatcher даёт null; вызовов hook0; Actor даёт ошибку отсутствующего метода |
| 14 | Контекст, HBS и listener | data===item.system; UUID совпадает; поля входят в схему; пустое содержимое без кнопок; описание экранировано; click listener назначен, базовый DragDrop привязан; два ключа локализации есть в en/ru |

Сценарии записи исполнялись с фасадами, которые сохраняли переданный payload в памяти либо оставляли Promise незавершённым. Они не доказывают успешного изменения чужого документа, серверного обхода разрешений или точного порядка сетевых операций. Неисправность по правам описана как отсутствие локального контракта двух записей и необходимость проверки реального результата.

### Перекрёстная сверка

Уточнены восемь ранее разобранных карточек:

- [module/data/item/commonItemData.js](files/module/data/item/commonItemData.js.md)
- [module/item/sheets/WitcherItemSheet.js](files/module/item/sheets/WitcherItemSheet.js.md)
- [module/item/witcherItem.js](files/module/item/witcherItem.js.md)
- [module/actor/witcherActor.js](files/module/actor/witcherActor.js.md)
- [module/setup/registerDataModels.js](files/module/setup/registerDataModels.js.md)
- [module/setup/registerSheets.js](files/module/setup/registerSheets.js.md)
- [templates/partials/item-header.hbs](files/templates/partials/item-header.hbs.md)
- [system.json](files/system.json.md)

Проверены оба импорта новых JS-файлов, оба буквальных HBS-пути, поля формы и подготовленного списка, все собственные методы, определения и потребители. itemContent не имеет поля схемы; storedWeight имеет и пересчитывается без Document.update. Контейнер хранит ссылки на исходные Items, не собственную embedded-коллекцию. Простой согласованный случай не считает leaf дважды: общий calcWeight исключает stored Item, контейнер включает его raw quantity*weight. Ошибки членства и вложенности отделены от этого рабочего случая.

[issue-00034](../../issues/potential/issue-00034.md) сопоставлена по асинхронности: контейнер не вызывает removeItemsOfType/useItem, его два update имеют собственную проблему. Для [issue-00058](../../issues/potential/issue-00058.md) подтверждено наличие собственного Item-обработчика и оставшаяся Actor-ветвь без метода. [issue-00059](../../issues/potential/issue-00059.md) дополнена контейнерным маршрутом без стандартного hook.

### Проблемы

Зарегистрированы восемь potential issues:

| Карточка | Наблюдение |
| --- | --- |
| [issue-00156](../../issues/potential/issue-00156.md) | Недоступная ссылка содержимого прерывает подготовку и извлечение из контейнера |
| [issue-00157](../../issues/potential/issue-00157.md) | Контейнер меняет два Item без ожидания и обработки общего результата |
| [issue-00158](../../issues/potential/issue-00158.md) | Принадлежность предмета контейнеру не согласована с isStored |
| [issue-00159](../../issues/potential/issue-00159.md) | Контейнер допускает ссылку на себя и циклическое хранение |
| [issue-00160](../../issues/potential/issue-00160.md) | Вес содержимого вложенного контейнера не входит в общий вес |
| [issue-00161](../../issues/potential/issue-00161.md) | Drop в контейнер обновляет исходный Item другого владельца |
| [issue-00162](../../issues/potential/issue-00162.md) | Удаление контейнера не освобождает помеченное содержимое |
| [issue-00163](../../issues/potential/issue-00163.md) | Вместимость контейнера не участвует в проверке помещения предмета |

Все прежние и новые проблемы остаются potential. Предложения не согласованы как исправления. Для carry отдельно оставлен вопрос о нужном поведении: справка, предупреждение или ограничение; игровое правило не назначалось.

### Техническая сверка и сохранность

Все 621 исходник побайтно совпадают с HEAD порции и срезом TASK-0001. Совокупный SHA-256 — `52701d3d0a5f054319886ac2a9d45b42c26c80098858d02518579c6a1edfaec4`, без изменений. Для 1095 ранее отслеживаемых файлов сохранены mode, uid, gid и inode. Историческая часть журнала начиная с TASK-0003.023 сохранена побайтно; SHA-256 всего журнала до новой записи — `f7ac8fe8a7af999f42605c830d075f1eaafdb5ec13a462233e2b62ddf39114c2`.

Проверены фактическое дерево и Git, 621 строка реестра и 203 карточки, собственные методы/поля и обязательные разделы новой порции. Все 30 списков подзадач согласованы с реестром: .001–.024 имеют done, .025–.030 — planned. TASK-0003 остаётся in-progress, TASK-0004/TASK-0005 — draft. В трёх сериях назначены 236 разных файлов; в третьей проверены 35 из 79, 44 в очереди; 374 вне назначенных порций.

У 203 разобранных файлов сверены 271 прямой относительный импорт: 198 default, 66 named-деклараций с 71 именем, 7 namespace. Цели и экспорты существуют; связи в карточках разобранных источников/целей согласованы в обе стороны. В порции два импорта: CommonItemData и WitcherItemSheet. Проверена 121 буквальная связь с HBS, из них две у новой порции: форма контейнера и общая шапка.

Проверены 428 Markdown-файлов docs и два корневых указателя: **8967 локальных ссылок/якорей** разрешаются. Примеры внутри кода не считаются навигацией. Таблицы изменённых документов согласованы по числу столбцов, `git diff --check` проходит. У 163 potential issues последовательные уникальные ID; статусы не менялись.

Изменены ровно 33 Markdown-документа: 11 новых (три карточки, восемь issues) и 22 прежних (восемь связанных карточек, три issues, одиннадцать документов навигации/отчётности). Других изменений нет. Проверка выполнена чтением исходников, rg, git status/rev-parse/ls-files/show/diff и Python через stdin; постоянный проверочный скрипт не создавался.

Код, игровые данные, службы, ветки Git, права и владельцы не менялись; коммит не создавался. Мир, HTTP/браузер, БД, сборка и сохранённый тестовый стенд не входили в поручение.

## TASK-0003.023

Дата: 2026-09-11. Ветка `rusbar-main`, HEAD `538dbac9bb9432c123fe4f3c00ab788b58517afb`. На старте рабочее дерево чистое, отслеживаются 1073 файла. Исследуемый код сверяется со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`.

### Объём и результат

По [TASK-0003.023](../../tasks/task-0003.023.md) полностью разобраны 14 файлов: 8 JS и 6 HBS, 449 логических строк. Созданы 14 карточек, уточнены шесть ранее разобранных связанных. Реестр содержит 200 проверенных файлов и 421 неразобранный. В третьей серии завершены 32 из 79 файлов, 47 в очереди; 374 требуют дальнейшей детализации. Следующая задача — [TASK-0003.024](../../tasks/task-0003.024.md), выполнение не начато.

| Файл | Карточка | Логических строк |
| --- | --- | --- |
| [module/data/investigation/mysteryActorData.js](../../../module/data/investigation/mysteryActorData.js) | [Описание](files/module/data/investigation/mysteryActorData.js.md) | 12 |
| [module/data/investigation/clueData.js](../../../module/data/investigation/clueData.js) | [Описание](files/module/data/investigation/clueData.js.md) | 22 |
| [module/data/investigation/obstacleData.js](../../../module/data/investigation/obstacleData.js) | [Описание](files/module/data/investigation/obstacleData.js.md) | 17 |
| [module/data/investigation/templates/complexityData.js](../../../module/data/investigation/templates/complexityData.js) | [Описание](files/module/data/investigation/templates/complexityData.js.md) | 8 |
| [module/actor/sheets/investigation/WitcherMysterySheet.js](../../../module/actor/sheets/investigation/WitcherMysterySheet.js) | [Описание](files/module/actor/sheets/investigation/WitcherMysterySheet.js.md) | 115 |
| [module/item/sheets/investigation/WitcherClueSheet.js](../../../module/item/sheets/investigation/WitcherClueSheet.js) | [Описание](files/module/item/sheets/investigation/WitcherClueSheet.js.md) | 30 |
| [module/item/sheets/investigation/WitcherObstacleSheet.js](../../../module/item/sheets/investigation/WitcherObstacleSheet.js) | [Описание](files/module/item/sheets/investigation/WitcherObstacleSheet.js.md) | 30 |
| [module/scripts/investigation/rollClue.js](../../../module/scripts/investigation/rollClue.js) | [Описание](files/module/scripts/investigation/rollClue.js.md) | 44 |
| [templates/sheets/investigation/mystery-sheet.hbs](../../../templates/sheets/investigation/mystery-sheet.hbs) | [Описание](files/templates/sheets/investigation/mystery-sheet.hbs.md) | 55 |
| [templates/sheets/investigation/clue-sheet.hbs](../../../templates/sheets/investigation/clue-sheet.hbs) | [Описание](files/templates/sheets/investigation/clue-sheet.hbs.md) | 23 |
| [templates/sheets/investigation/obstacle-sheet.hbs](../../../templates/sheets/investigation/obstacle-sheet.hbs) | [Описание](files/templates/sheets/investigation/obstacle-sheet.hbs.md) | 20 |
| [templates/sheets/investigation/partials/clue-display.hbs](../../../templates/sheets/investigation/partials/clue-display.hbs) | [Описание](files/templates/sheets/investigation/partials/clue-display.hbs.md) | 37 |
| [templates/sheets/investigation/partials/obstacle-display.hbs](../../../templates/sheets/investigation/partials/obstacle-display.hbs) | [Описание](files/templates/sheets/investigation/partials/obstacle-display.hbs.md) | 28 |
| [templates/dialog/investigation/chooseEvidenceSkill.hbs](../../../templates/dialog/investigation/chooseEvidenceSkill.hbs) | [Описание](files/templates/dialog/investigation/chooseEvidenceSkill.hbs.md) | 8 |

### Методика и пределы

Все 14 файлов прочитаны полностью. Сопоставлены схемы, регистрации, разные базовые API трёх листов, контекст HBS/partial, локальные ID Items, поля и действия, получение Actor и вызов skillMixin. Соседние helper.js и skillMixin.js проверены точечно до нужных методов; они не получили полные карточки и остаются в планах .028/.029.

Изолированный запуск: `node --input-type=module` со скриптом через stdin, Node **24.16.0**, Foundry **14.367.0**, Handlebars **4.7.9**, parse5. Настоящие DataModel/TypeDataModel/fields, три модели расследований, фабрика complexity, классы листов, rollClue, getInteractActor/getCurrentCharacter/chooseFromAvailableActors. Настоящие getList, rollSkill и rollSkillCheck извлечены целиком и исполнены с изолированным окружением; rollSkillCheck доходил только до отказа неизвестной записи либо заменялся на границе для захвата threshold.

Настоящие registerDataModels/registerSheets исполнены в vm с тремя моделями/классами листов порции и подменами остальных импортов/API регистрации. Реальный DocumentTypeField проверен в DataModel-фасаде с TYPES из documentTypes.Item манифеста: clue отклонён при строгой проверке, spell принят. Это проверка конкретного списка типов, не серверной подготовки game.model. Недостающие типы mystery/clue/obstacle в работающую систему не добавлялись.

Базовые ActorSheetV2, ItemSheet V1 и HandlebarsApplicationMixin заменены фасадами; исходные методы системных листов не переписывались. Подменены game/user/actors/canvas/UI, источники и коллекции Actor/Item, Item.create/update/delete/sheet.render, диалоги и конечный Actor.rollSkill. Управляемые Promise фиксировали ожидание записи/броска. Реальный мир, БД, сетевые запросы, случайные броски и сообщения не создавались.

Скомпилированы настоящие HBS. selectOptions и prepareSelectOptionGroups извлечены целиком из ядра; DOM-append заменён фасадом HTML option с тем же условием наличия value/label, проверенным в _appendOption. parse5 разбирал строки HTML для подсчёта ячеек, атрибутов и выбранных options. Это не браузерное исполнение custom element multi-select и не проверка submitOnChange. getData базы ItemSheet V1 проверен чтением ядра; он синхронен, поэтому отсутствие await в двух системных листах не зарегистрировано как ошибка.

### Сверенные контракты ядра

| Источник Foundry 14.367.0 | Проверенное свойство |
| --- | --- |
| `/opt/foundryvtt/common/data/fields.mjs`:4172–4200 | DocumentTypeField использует Document.TYPES; строгая проверка неизвестного типа отклоняется |
| `/opt/foundryvtt/common/abstract/document.mjs`:237 и 286–288 | Источник TYPES и getter id, возвращающий _id |
| `/opt/foundryvtt/client/appv1/sheets/item-sheet.mjs`:62–66 | Синхронный getData добавляет item=document |
| `/opt/foundryvtt/client/applications/api/document-sheet.mjs`:46–54, 269–272 | tag=form по умолчанию; базовый лист отключает ввод при !isEditable |
| `/opt/foundryvtt/client/applications/api/dialog.mjs`:261–276, 405–428 | _onSubmit возвращает callback либо action; wait при закрытии по умолчанию возвращает null |
| `/opt/foundryvtt/client/applications/handlebars.mjs`:460–500 | selectOptions нормализует selected и делегирует создание select |
| `/opt/foundryvtt/client/applications/forms/fields.mjs`:290–360, 371–386 | prepareSelectOptionGroups формирует value/label/selected; _appendOption пропускает варианты без value/label |
| `/opt/foundryvtt/client/applications/elements/multi-select.mjs`:122–124 | _getValue возвращает массив из внутреннего Set |

Чтение DialogV2.input/prompt (dialog.mjs:369–394) подтвердило передачу результата через wait и null при закрытии; helper не задаёт rejectClose. wait/_onSubmit дополнительно исполнены настоящими методами ядра на фасаде окна: выбрано deduction → 'deduction', нажата cancel → 'cancel', окно закрыто → null. Системный rollClue проверен отдельно на этих результатах.

### Изолированные проверки

Успешно завершены **17 групп**:

| Группа | Что проверено | Фактический результат |
| --- | --- | --- |
| 01 | Три схемы и фабрика сложности | Mystery: 2 поля, Clue: 10, Obstacle: 6; defaults 25/Easy, DC 14, focusDamage 1d6, successDamage 2/failDamage 1d6+2. Отрицательные дроби DC/complexity и неизвестные имена навыков допускаются |
| 02 | Реестры и поле типа | Регистрация указывает ожидаемые классы; ключи отсутствуют в манифесте; строгий DocumentTypeField со списком Item-типов отвергает clue и принимает spell |
| 03 | Контекст и getList | Пустые/разные типы, sort и isStored обработаны; isHidden не исключает Item из списка |
| 04 | Два листа Item V1 | Опции 520×480, ожидаемые пути и синхронный контекст; самостоятельные формы показывают сохранённые навыки |
| 05 | Настоящие методы DialogV2 | Выбор возвращает имя, cancel — строку 'cancel', закрытие — null |
| 06 | 0/1/несколько навыков и DC | 0 — без броска, 1 — без диалога, несколько — с выбором; dc=99 не передаётся, порог rollSkill по умолчанию -1 |
| 07 | Отмена выбора навыка | 'cancel'/null передаются в rollSkill; дальнейшее обращение к отсутствующему skillMapEntry даёт TypeError |
| 08 | Выбор Actor | Токен приоритетнее назначенного персонажа; единственный доступный Actor выбирается; несколько допускают выбор; отсутствие Actor даёт уведомление и отказ rollClue, null выбора Actor ломает values.actor |
| 09 | Неизвестные и пустые имена | Модель принимает их, один навык доходит до отказа rollSkillCheck; неизвестные записи в нескольких вариантах не дают пригодных options |
| 10 | Promise броска | rollClue завершается раньше управляемого Promise Actor.rollSkill |
| 11 | Основная форма и partial | 0 записей даёт 2 заголовка; 2 улики+1 препятствие — 5 строк; selected=system.skillsUsed работает через each; data-itemtype нормализован; ячейки улик 12/13, препятствий 8/8 |
| 12 | Hidden/GM/owner | Класс скрытой строки зависит от isGM; сами данные остаются в HTML; GM-кнопки зависят только от isGM, owner не читается шаблоном |
| 13 | CRUD и локальный ID | create получает parent Actor; add/delete ждут API; edit вызывает sheet.render(true); hide не ждёт update; отсутствующий Item не защищён |
| 14 | Inline value и multi-select | Текст 'false' → true, 'true'/'checked' → false; обычные строки/массив навыков передаются без изменения; настоящий _getValue multi-select возвращает массив |
| 15 | Регистрация действий и change | Пять data-action сопоставлены с методами; .inline-edit получает listener; _onRollClue вызывает правильный Item и возвращает undefined |
| 16 | Поля HBS, статические переводы и preload | Все system-пути совпали со схемами; статические localize-ключи есть в en/ru; основная форма/partial предзагружаются; Goal/Difficulty/Complexity буквальные |
| 17 | Динамические label всех 52 навыков | В en/ru не разрешаются label picklock/trapcraft, остальные 50 найдены; это прежняя issue-00016 |

Обнаруженные исключения — ожидаемые наблюдения исходного кода в отдельных сценариях. Ни успешное исполнение фасадов, ни рендер HBS в Node не доказывают штатную доступность типов расследований в мире, успешное сохранение или отсутствие прочих ошибок.

### Перекрёстная сверка

Уточнены шесть ранее разобранных карточек:

- [system.json](files/system.json.md)
- [module/setup/registerDataModels.js](files/module/setup/registerDataModels.js.md)
- [module/setup/registerSheets.js](files/module/setup/registerSheets.js.md)
- [module/setup/handlebars.js](files/module/setup/handlebars.js.md)
- [module/setup/config.js](files/module/setup/config.js.md)
- [module/actor/witcherActor.js](files/module/actor/witcherActor.js.md)

Новая связь не присваивает соседнему файлу полного статуса анализа. Проверены импорт complexity → MysteryActorData, импорт rollClue → лист тайны, импорт getInteractActor → rollClue; регистрации моделей/листов, preload и буквальные HBS-пути; skillMap, getList, локальные ID, data-action и data-field. Данные system у обоих partial унаследованы от текущего Item в each; ложное наблюдение о потере selected не зарегистрировано.

ClueData и ObstacleData не наследуют CommonItemData. MysteryActorData хранит только goal/complexity; имя, права и Items принадлежат Actor. Поиск module/templates установил, что complexity, время и текстовые последствия в текущем пути броска не применяются. Это описание границ реализации, не вывод о правилах TRPG. DC улики выделена в отдельную potential issue, поскольку её назначение в броске требует уточнения.

Hidden-строки не вырезаются из HTML. .hidden-from-view скрывается display:none, .hidden-view имеет серебристый фон; стили импортируются witcher-styles.css. Это представление данных, не проверка разграничения доступа. Внешняя форма DocumentSheetV2 и внутренний <form> HBS зафиксированы как структура; отказ сохранения только из этого факта не утверждается. Фактические права observer/owner и поведение формы остаются непроверенными.

### Проблемы

В рамках согласованной регистрации TASK-0003 созданы восемь potential issues:

| Карточка | Наблюдение |
| --- | --- |
| [issue-00148](../../issues/potential/issue-00148.md) | Отмена выбора навыка улики всё равно запускает rollSkill |
| [issue-00149](../../issues/potential/issue-00149.md) | Выбор Actor для улики не обрабатывает отсутствие персонажа и отмену |
| [issue-00150](../../issues/potential/issue-00150.md) | Навыки расследования допускают неизвестные имена без проверки перед броском |
| [issue-00151](../../issues/potential/issue-00151.md) | DC улики не передаётся в бросок навыка |
| [issue-00152](../../issues/potential/issue-00152.md) | Действия скрытия и броска расследования завершаются до результата |
| [issue-00153](../../issues/potential/issue-00153.md) | Inline-редактор расследования преобразует текст false и true в булевы значения |
| [issue-00154](../../issues/potential/issue-00154.md) | Число столбцов заголовка и строки улики различается |
| [issue-00155](../../issues/potential/issue-00155.md) | Основные подписи тайны обходят локализацию |

Дополнены [issue-00005](../../issues/potential/issue-00005.md) и [issue-00016](../../issues/potential/issue-00016.md). Все карточки остаются potential; подтверждение пользователя, изменение статусов и исправление не выполнялись. Строки реестра проблем собраны в одну таблицу, включая прежние строки, оказавшиеся после завершающего текста.

### Техническая сверка и сохранность

Все 621 исходник побайтно совпадают с HEAD порции и срезом TASK-0001. Совокупный SHA-256 — `52701d3d0a5f054319886ac2a9d45b42c26c80098858d02518579c6a1edfaec4`, без изменений. Для 1073 ранее отслеживаемых файлов сохранены mode, uid, gid и inode. Историческая часть журнала начиная с TASK-0003.022 сохранена побайтно; SHA-256 всего журнала до новой записи — `47392ff431c41311b79c878be38f17137aa9ef3fbe2f4775877e4b7725b769a5`.

Сверены фактическое дерево и Git, 621 строка реестра и 200 карточек, обязательные разделы и собственные методы/поля новой порции. Все 30 списков подзадач согласованы с реестром: .001–.023 имеют done, .024–.030 — planned. Родительская TASK-0003 остаётся in-progress, TASK-0004/TASK-0005 — draft. В трёх сериях назначены 236 разных файлов; третья содержит 79, из них 32 проверены, 47 в очереди; 374 ещё требуют детализации.

У 200 разобранных файлов проверены 269 прямых относительных импортов: 196 default, 66 named-деклараций с 71 именем, 7 namespace. Цели и экспорты существуют; карточки разобранных источников и целей согласованы в обе стороны. В порции три импорта: complexityData, rollClue и helper. Проверены 119 буквальных связей с HBS, из них шесть у новой порции. Эта проверка не подменяет полный анализ ещё не описанных зависимостей.

Проверены 417 Markdown-файлов docs и два корневых указателя: **8800 локальных ссылок/якорей** разрешаются; примеры внутри кода не считаются навигацией. Таблицы изменённых документов согласованы по числу столбцов, `git diff --check` проходит. У 155 potential issues последовательные уникальные ID; статусы не менялись.

Изменён 41 Markdown-документ: 22 новых (14 карточек, восемь issues) и 19 прежних (шесть связанных карточек, две issues, одиннадцать документов навигации/отчётности). Других изменений нет. Проверка выполнена чтением кода, rg, git status/rev-parse/ls-files/show/diff и Python через stdin; постоянный скрипт не создавался.

Код, игровые данные, службы, ветки Git, права и владельцы не менялись; коммит не создавался. Мир, HTTP/браузер, БД, сборка и сохранённый тестовый стенд не входили в эту порцию.

## TASK-0003.022

Дата: 2026-09-11. Ветка `rusbar-main`, HEAD `ef8117ba6e5a184989e65761d47a068381056e4a`. На старте рабочее дерево чистое, отслеживаются 1058 файлов. Исследуемый код сверяется со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`.

### Объём и результат

По [TASK-0003.022](../../tasks/task-0003.022.md) полностью разобраны пять JS-файлов, 289 логических строк. Созданы пять карточек, уточнены десять ранее разобранных связанных. Реестр содержит 186 проверенных файлов и 435 неразобранных. В третьей серии завершены 18 из 79 файлов, 61 в очереди; 374 требуют дальнейшей детализации. Следующая задача — [TASK-0003.023](../../tasks/task-0003.023.md), её выполнение не начато.

| Исходник | Карточка | Логических строк |
| --- | --- | --- |
| [module/data/item/templates/regions/templatePropertiesData.js](../../../module/data/item/templates/regions/templatePropertiesData.js) | [Описание](files/module/data/item/templates/regions/templatePropertiesData.js.md) | 13 |
| [module/data/item/templates/regions/regionPropertiesData.js](../../../module/data/item/templates/regions/regionPropertiesData.js) | [Описание](files/module/data/item/templates/regions/regionPropertiesData.js.md) | 56 |
| [module/data/item/templates/regions/regionBehavioursData.js](../../../module/data/item/templates/regions/regionBehavioursData.js) | [Описание](files/module/data/item/templates/regions/regionBehavioursData.js.md) | 26 |
| [module/data/item/mixin/spellRegionMixin.js](../../../module/data/item/mixin/spellRegionMixin.js) | [Описание](files/module/data/item/mixin/spellRegionMixin.js.md) | 176 |
| [module/scripts/regions/regionHooks.js](../../../module/scripts/regions/regionHooks.js) | [Описание](files/module/scripts/regions/regionHooks.js.md) | 18 |

### Методика и пределы

Все пять файлов прочитаны полностью. Сопоставлены определения, схемы, импорты, примесь на прототипах SpellData/RitualData, вызов из castSpell, настройки листов/HBS, query и регистрация updateCombat. Соседние файлы проверены до нужных определений и потребителей; полный разбор им автоматически не присваивался.

Изолированный запуск: `node --input-type=module` со скриптом через stdin. Использованы настоящие DataModel/TypeDataModel/fields Foundry **14.367.0**, Node **24.16.0**, модели и методы системы, настоящий ExecuteMacroRegionBehaviorType. В окружении загружен Handlebars **4.7.9**; браузерный интерфейс этой порции не проверялся. Методы Actor.getDependentTokens и RegionDocument.createTokenEmanation извлечены целиком из локального ядра и исполнены с подменёнными зависимостями. Реализация исследуемых методов не переписывалась.

Подменены родитель Item, game/user/users/settings/i18n, резолверы UUID, Macro и его execute, документы/коллекции Scene/Region/Token, API create/update/setFlag/deleteEmbeddedDocuments, canvas/placeRegion/legend, приложения/minimize, query и таймеры. Регистрация Hooks проверена через изолированную шину; соседний общий обработчик боя заменён заглушкой. Управляемые Promise и таймеры фиксировали порядок завершения без ожидания реального времени. Записи перехватывались в памяти: мир, БД, реальные регионы, сцены, макросы и сетевые запросы не затронуты.

Настоящее конструирование моделей может запускать migrateData через migrateDataSafe. Поэтому независимая проверка четырёх UUID-полей использовала фабрику regionBehaviours в отдельной модели, а сценарии миграции — настоящие RegionProperties/SpellData/RitualData. Для пустого regionProperties ошибка миграции логируется и перехватывается ядром; затем применяются значения по умолчанию. Это не подтверждение отказа загрузки всего Item. Logger в сценарии заменён сборщиком сообщений.

Контракты ядра проверены чтением следующих локальных файлов:

| Файл ядра Foundry 14.367.0 | Проверенный контракт |
| --- | --- |
| `/opt/foundryvtt/client/canvas/layers/regions.mjs`, placeRegion: 688–781, 1162–1206 | Promise одного Region; отмена возвращает null; это не массив |
| `/opt/foundryvtt/client/documents/region.mjs`, createTokenEmanation: 1306–1337 | Диапазон переводится в пиксели через сцену токена; создаются shape/attachment/elevation; результат может отсутствовать при отмене создания |
| `/opt/foundryvtt/client/documents/actor.mjs`, getDependentTokens: 584–616 | По умолчанию TokenDocument из зависимых сцен; метод не ограничивает результат текущей сценой |
| `/opt/foundryvtt/client/documents/token.mjs`, scene: 105; обработчик движения: 2973–2999 | scene — объект Scene; tokenMoveWithin обрабатывается по завершённому движению |
| `/opt/foundryvtt/client/documents/user.mjs`, viewedScene: 47–51 | viewedScene — ID сцены либо null |
| `/opt/foundryvtt/client/documents/scene.mjs`, подготовка dimensions: 507 | distancePixels = grid.size / grid.distance |
| `/opt/foundryvtt/client/data/region-behaviors/execute-macro.mjs` | executeMacro принимает events/uuid/everyone; разрешает Macro и формирует аргументы события |
| `/opt/foundryvtt/common/documents/region.mjs`, schema и права: 111–135 | Поля Region и ограничение обновления непустых behaviors для GM; top-level uuid/user не входят в схему |
| `/opt/foundryvtt/common/abstract/data.mjs`, migrateDataSafe: 890–899 | Исключение миграции перехватывается с журналированием |
| `/opt/foundryvtt/client/documents/combat.mjs`, _onUpdate: 633–647, _getCurrentState: 822–829 | combatantId может быть null; ядро отдельно проверяет смену состояния для своих событий хода |

Отправленный массив behaviors проверен как payload. Слияние с уже сохранённой коллекцией RegionBehavior, сериализация ссылок Item/Roll в flags и разрешения живого клиента при создании региона не проверялись. Чтение проверок прав ядра не равно проверке нескольких клиентов.

### Изолированные проверки

Успешно завершены **20 групп**. Ошибки ниже — ожидаемые наблюдения исходного кода в сценариях, а не исправления.

| Группа | Что проверено | Фактический результат |
| --- | --- | --- |
| 01 | Схемы, значения по умолчанию, UUID и события | Четыре поля Macro UUID; корректный 16-символьный ID принимается, Item UUID отвергается; все имена событий существуют |
| 02 | createRegionBehaviour и настоящий тип executeMacro ядра | Структура events/uuid принимается; everyone по умолчанию false; разрешённый Macro-фасад получает контекст события; отсутствующий Macro не исполняется |
| 03 | Миграция новых, старых, смешанных и пустых данных | Новый tokenMoveWithin затирается старым полем либо становится null; пустые настройки логируют перехваченную ошибку и получают defaults |
| 04 | GM, адаптер UUID, обновления behaviors | Передаётся ожидаемый payload; адаптеры завершаются до управляемых записей; отсутствующий Region не отфильтрован |
| 05 | Игрок, activeGM и настоящий маршрутизатор query | Вложенный addBehaviorsToRegionUuids не найден, несмотря на ответ true; deleteSpellVisualEffect отсутствует в allowlist и содержит неопределённый item; отсутствующий GM не обработан |
| 06 | Условия createSpellRegion и завершение цепочки | Выключенная/неполная настройка пропускается; метод не возвращает цепочку создания; отказ поглощается catch |
| 07 | circle, cone, rect, ray | До ожидания сформированы соответствующие shapes; каждый обычный маршрут затем отвергает Promise как неитерируемый аргумент Promise.all |
| 08 | Контекст fromItem | Проверены отсутствие сцены и Item без владельца; обращение к нужному контексту не защищено |
| 09 | Настоящий drawPreview при подтверждении, отмене и отказе | Минимизирует приложения; возвращает одиночный результат или null; обратное восстановление окон не реализовано |
| 10 | Отложенное завершение preview | Размещение уже запущено и может завершиться после отказа fromItem; продолжение настройки области не выполняется |
| 11 | Сцены зависимых токенов и единицы эманации | Сравнение Scene с ID пропускает обе сцены; для неизменного целевого токена смена сетки canvas меняет радиус создаваемой эманации |
| 12 | Параметры применения | createSpellRegion передаёт options, fromItem читает flagOptions; переданный stamina не попадает в flags.options |
| 13 | Прерванное создание эманации | Возвращённый undefined остаётся в массиве, последующее присваивание region.item вызывает исключение |
| 14 | Визуальные таймеры и смена сцены | Задержка считается в секундах; callback удаляет ID через canvas.scene на момент срабатывания |
| 15 | Границы счётчика длительности | 3 → 2, строка '2' → 1; 1/0/отрицательное/undefined/нечисловая строка попадают в удаление; чужой actorUuid пропускается |
| 16 | Произвольные повторные updateCombat | Счётчик уменьшается повторно без смены хода; уточнение прежней issue-00006 |
| 17 | Пустой контекст боя и активный GM | Неактивный GM сразу выходит; отсутствие участника, Actor или активной сцены приводит к исключению |
| 18 | Сцена боя и активная сцена | Отсчёт выбирает game.scenes.active вместо сцены combat |
| 19 | Завершение countdownDurationOfRegions | Promise функции разрешается до setFlag и deleteEmbeddedDocuments |
| 20 | Локализация и регистрация | Подпись tokenMoveWithin использует ключ tokenPreMove; updateCombat зарегистрирован и вызывает региональный обработчик |

Пример группы 11: целевая сцена с grid.size = 100, grid.distance = 5 и templateSize = 10. При grid.distance текущего canvas = 5 переданный range равен 1, итоговый радиус — 20 px; при canvas grid.distance = 10 тот же целевой токен получает range 0.5 и радиус 10 px. Это доказывает влияние посторонней сетки. Должен ли templateSize означать радиус или диаметр по правилам, эта проверка не устанавливает.

Визуальный таймер visualEffectDuration и flags.duration, уменьшаемый updateCombat, рассмотрены раздельно. Корректные правила длительности, постоянных областей и повторного отсчёта требуют решения пользователя; числовые ветви текущего кода не объявляются правилами TRPG.

### Перекрёстная сверка и связанные карточки

Проверены импорт фабрики событий, embedding региональных моделей, Object.assign примеси, методы назначения поведения, query с Item UUID, вызов castSpell, HBS-пути и условия конфигурации. Уточнены десять карточек:

- [module/data/item/spellData.js](files/module/data/item/spellData.js.md)
- [module/data/item/ritualData.js](files/module/data/item/ritualData.js.md)
- [module/item/sheets/WitcherSpellSheet.js](files/module/item/sheets/WitcherSpellSheet.js.md)
- [module/item/sheets/WitcherRitualSheet.js](files/module/item/sheets/WitcherRitualSheet.js.md)
- [templates/sheets/item/spell-sheet.hbs](files/templates/sheets/item/spell-sheet.hbs.md)
- [templates/sheets/item/ritual-sheet.hbs](files/templates/sheets/item/ritual-sheet.hbs.md)
- [module/item/sheets/configurations/WitcherPropertiesConfigurationSheet.js](files/module/item/sheets/configurations/WitcherPropertiesConfigurationSheet.js.md)
- [templates/sheets/item/configuration/tabs/regionPropertiesConfiguration.hbs](files/templates/sheets/item/configuration/tabs/regionPropertiesConfiguration.hbs.md)
- [module/setup/queries.js](files/module/setup/queries.js.md)
- [module/setup/hooks.js](files/module/setup/hooks.js.md)

Связи сверены в обе стороны с существующими определениями и потребителями. Отсутствие поля createRegionFromTemplate, старый system.createTemplate у конфигурационного листа и старые поля ритуальной формы сопоставлены с ранее зарегистрированными наблюдениями; новые ID для них не выдавались.

### Проблемы

В рамках согласованной регистрации TASK-0003 созданы десять карточек potential:

| Карточка | Наблюдение |
| --- | --- |
| [issue-00138](../../issues/potential/issue-00138.md) | Обычное размещение области передаёт Promise в Promise.all |
| [issue-00139](../../issues/potential/issue-00139.md) | Параметры применения магии теряются при записи options региона |
| [issue-00140](../../issues/potential/issue-00140.md) | Фильтр эманации сравнивает объект Scene со строковым ID |
| [issue-00141](../../issues/potential/issue-00141.md) | Размер эманации зависит от масштаба сетки просматриваемой сцены |
| [issue-00142](../../issues/potential/issue-00142.md) | Асинхронные операции регионов завершаются до создания и записей |
| [issue-00143](../../issues/potential/issue-00143.md) | Отмена создания эманации приводит к обращению к отсутствующему региону |
| [issue-00144](../../issues/potential/issue-00144.md) | Отсчёт и удаление регионов используют текущую сцену вместо связанной |
| [issue-00145](../../issues/potential/issue-00145.md) | Отсчёт регионов падает при отсутствии участника, Actor или активной сцены |
| [issue-00146](../../issues/potential/issue-00146.md) | Регион без числовой длительности считается истёкшим при отсчёте |
| [issue-00147](../../issues/potential/issue-00147.md) | Подпись tokenMoveWithin обещает исполнение макроса до движения |

Дополнены [issue-00006](../../issues/potential/issue-00006.md), [issue-00008](../../issues/potential/issue-00008.md), [issue-00009](../../issues/potential/issue-00009.md), [issue-00074](../../issues/potential/issue-00074.md), [issue-00075](../../issues/potential/issue-00075.md), [issue-00076](../../issues/potential/issue-00076.md), [issue-00128](../../issues/potential/issue-00128.md), [issue-00129](../../issues/potential/issue-00129.md), [issue-00137](../../issues/potential/issue-00137.md). Статусы всех проблем остаются potential. Предложения в карточках не являются согласованными исправлениями.

### Техническая сверка и сохранность

Все 621 исходник побайтно совпадают с HEAD порции и срезом TASK-0001. Их совокупный SHA-256 — `52701d3d0a5f054319886ac2a9d45b42c26c80098858d02518579c6a1edfaec4`, без изменений. Для всех 1058 ранее отслеживаемых файлов сохранены mode, uid, gid и inode. Историческая часть журнала начиная с TASK-0003.021 сохранена побайтно; SHA-256 всего журнала до добавления записи — `eab65f291965ff7f01ea7172ea1422098dc10e2ff517872ea9c4bfb8bd5e61cf`.

Проверены состав файлов на диске и в Git, взаимное соответствие 621 строки реестра и 186 карточек, обязательные разделы новых карточек, собственные методы и поля, статусы и списки всех 30 подзадач. .001–.022 имеют done, .023–.030 — planned; родительская задача остаётся in-progress, TASK-0004/TASK-0005 — draft. В трёх сериях назначены 236 различных файлов; в третьей из 79 проверены 18, в очереди 61, вне назначенных порций остаются 374.

У 186 разобранных файлов проверены 266 прямых относительных импортов: 195 default, 64 named-декларации с 69 именами, 7 namespace. Цели существуют, именованные/default экспорты найдены; связи в карточках разобранных источников и целей согласованы в обе стороны. В новой порции один импорт — RegionProperties → regionBehaviours. Дополнительно сверены 113 буквальных связей с HBS; у этой пятёрки таких путей нет.

Проверены 395 Markdown-файлов в docs и два корневых указателя: **8425 локальных ссылок/якорей** разрешаются. Примеры внутри кода не учитываются как навигация. Таблицы изменённых документов согласованы по числу столбцов; `git diff --check` проходит. Все 147 issues имеют последовательные уникальные ID и остаются в potential.

Изменены ровно 45 Markdown-документов: 15 новых (пять карточек, десять issues) и 30 прежних (десять связанных карточек, девять issues и одиннадцать документов навигации/отчётности). Других изменений нет. Проверка выполнена средствами rg, чтением исходников, git status/rev-parse/ls-files/show/diff и Python через stdin; постоянный проверочный скрипт не создавался.

Код, игровые данные, службы, ветки Git, права и владельцы не менялись; коммит не создавался. Запуск мира, работа с БД, сборка, HTTP/браузерная проверка, живой вызов Macro и сохранённый тестовый стенд не входили в эту порцию.

## TASK-0003.021

Дата: 2026-09-11. Ветка `rusbar-main`, HEAD `a29234e7c42ef5f9d8095c2b5470e5e3c95824cc`. На старте рабочее дерево чистое, отслеживаются 1035 файлов. Исследуемый код сверяется со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`.

### Объём и результат

По [TASK-0003.021](../../tasks/task-0003.021.md) полностью разобраны 13 файлов: 8 JS и 5 HBS, 936 логических строк. Создано 13 карточек, уточнены 17 ранее разобранных связанных. Реестр содержит 181 проверенный файл и 440 неразобранных. В третьей серии завершены 13 из 79 файлов, 66 в очереди; 374 требуют дальнейшей детализации. Следующая задача — [TASK-0003.022](../../tasks/task-0003.022.md), её выполнение не начато.

| Исходник | Карточка | Логических строк |
| --- | --- | --- |
| [module/data/item/spellData.js](../../../module/data/item/spellData.js) | [Описание](files/module/data/item/spellData.js.md) | 137 |
| [module/data/item/hexData.js](../../../module/data/item/hexData.js) | [Описание](files/module/data/item/hexData.js.md) | 29 |
| [module/data/item/ritualData.js](../../../module/data/item/ritualData.js) | [Описание](files/module/data/item/ritualData.js.md) | 91 |
| [module/data/item/templates/componentData.js](../../../module/data/item/templates/componentData.js) | [Описание](files/module/data/item/templates/componentData.js.md) | 8 |
| [module/item/sheets/WitcherSpellSheet.js](../../../module/item/sheets/WitcherSpellSheet.js) | [Описание](files/module/item/sheets/WitcherSpellSheet.js.md) | 65 |
| [module/item/sheets/WitcherHexSheet.js](../../../module/item/sheets/WitcherHexSheet.js) | [Описание](files/module/item/sheets/WitcherHexSheet.js.md) | 28 |
| [module/item/sheets/WitcherRitualSheet.js](../../../module/item/sheets/WitcherRitualSheet.js) | [Описание](files/module/item/sheets/WitcherRitualSheet.js.md) | 82 |
| [module/item/sheets/configurations/WitcherSpellConfigurationSheet.js](../../../module/item/sheets/configurations/WitcherSpellConfigurationSheet.js) | [Описание](files/module/item/sheets/configurations/WitcherSpellConfigurationSheet.js.md) | 11 |
| [templates/sheets/item/spell-sheet.hbs](../../../templates/sheets/item/spell-sheet.hbs) | [Описание](files/templates/sheets/item/spell-sheet.hbs.md) | 125 |
| [templates/sheets/item/hex-sheet.hbs](../../../templates/sheets/item/hex-sheet.hbs) | [Описание](files/templates/sheets/item/hex-sheet.hbs.md) | 66 |
| [templates/sheets/item/ritual-sheet.hbs](../../../templates/sheets/item/ritual-sheet.hbs) | [Описание](files/templates/sheets/item/ritual-sheet.hbs.md) | 161 |
| [templates/sheets/item/configuration/tabs/spellGeneral.hbs](../../../templates/sheets/item/configuration/tabs/spellGeneral.hbs) | [Описание](files/templates/sheets/item/configuration/tabs/spellGeneral.hbs.md) | 49 |
| [templates/partials/spell-header.hbs](../../../templates/partials/spell-header.hbs) | [Описание](files/templates/partials/spell-header.hbs.md) | 84 |

### Методика и пределы

Все 13 файлов прочитаны полностью, сопоставлены определения, схемы, наследование, регистрации, HBS-поля/условия и обработчики. Соседние файлы прочитаны до определений/потребителей нужных сущностей; им не присваивались полные карточки автоматически. Особо разделены: описание effect; словари selfEffects/onCastEffects; damageProperties.effects; документы Item.effects; настройки области и её последующее создание.

Изолированный запуск: `node --input-type=module` со скриптом через stdin. Использованы настоящие DataModel/TypeDataModel/fields Foundry **14.367.0**, Node **24.16.0**, системные модели и классы листов, Handlebars **4.7.9**, parse5 для HTML. Статические миграции верхней модели вызывались явно там, где проверялся перенос source; очистка и подготовка вложенных моделей использовали настоящие поля Foundry.

Подменены родители Item (DataModel-фасад с type), базовый ItemSheetV2 и HandlebarsApplicationMixin, game/settings/i18n, resolver UUID, jQuery/DOM-события, helpers selectOptions/formGroup, Item.update, диалог/ChatMessageData/RollConfig/extendedRoll и применения эффектов на границе castSpell. Код системных методов не переписывался; castSpell целиком исполнен в vm с изолированными зависимостями. Схемы/модели/HBS настоящие, подмены UI не доказывают работу ApplicationV2. Управляемые Promise позволили проверить момент возврата Drop и отказ записи без обращения к БД. Тестовые UUID имеют корректный 16-символьный ID; пробная короткая ссылка была отвергнута настоящим DocumentUUIDField, исправлен только вход сценария.

Чтением ядра установлены контракты selectOptions/formGroup, DocumentSheetV2.editImage и делегирование кликов ApplicationV2 (`/opt/foundryvtt/client/applications/handlebars.mjs`, `api/document-sheet.mjs`, `api/application.mjs`). Факт отсутствия action в HBS установлен статически; FilePicker/браузер не запускались. JSON en/ru проверены с раскрытием dotted ключей; реальная цепочка i18n fallback не исполнялась. Английская emanation существует, русская отсутствует.

### Изолированные проверки

Успешно завершены **18 групп**: 01–17 и дополнительная 11b. Номера сохранены для связи с карточками; 11b добавляет контроль выключенных/независимых флагов.

| Группа | Сценарий | Фактический результат |
| --- | --- | --- |
| 01–02 | Модели и навыки/защита | 4 класса spell → spellcast; hex → hexweave; ritual → ritcraft; пустой/неизвестный class spell с default даёт TypeError, явный ritcraft имеет приоритет. Spell делегирует защиту, у Hex/Ritual методов защиты нет. |
| 03 | Словари и миграции эффектов | Пустые массивы остаются массивами в migrateEffectsToTypedField, затем превращаются в {} при очистке настоящим TypedObjectField. Непустые массивы получают randomID; повторная миграция словаря сохраняет ID; percentage'42' становится 42. static this.effects обычно undefined; difficultyCheck после переноса не объявлено в схеме spell. |
| 04 | Области, смешанные поля и нули | Обе миграции заменяют новый объект четырьмя старыми полями; новые настройки теряются. Числовой 0 пропускает перенос, при очистке прежние поля исчезают. Строка'2.75' у spell становится 2, у ritual —2.75; актуальное вложенное 2.75 сохраняется у обоих. |
| 05 | Общие фабрики/миграции | Старый attackSkill не задаёт новый meleeAttackSkill; level даёт вариант spell, defaultskill остаётся spellcasting. Старый armorPiercing=true заменяет новый false. При единственном новом tokenMoveWithin обе настоящие вложенные региональные модели получают null. |
| 06 | Подготовка компонентов | Оба массива строятся заново без дублей от повторного prepare. Известная ссылка возвращает документ; отсутствующая — {name: uuid}. img в фабрике не объявлен, quantity очищается числом, производные массивы отсутствуют в toObject. |
| 07–08 | Адресация строк | Отсутствующая ссылка имеет пустой data-uuid: edit даёт TypeError, remove не удаляет запись. Две записи одного UUID: изменение второй редактирует первую; remove убирает обе. Проверены оба списка. |
| 09 | Запись, типы и Drop | Вне alternateComponents Drop идёт в основной массив; внутри — в альтернативный. Promise Drop завершается при pending update; искусственный отказ не откатывает push в памяти. quantity передаётся строкой, но очищается NumberField. |
| 10 | Наследование и события | Все контексты содержат selects/showConfig. У spell конфигурация специализирована, hex/ritual используют базовую. Проверены blur/click-селекторы ритуала. Региональная вкладка spell остаётся без PART по старому условию. |
| 11 и 11b | Условия spell/header | 4 класса×2 STA-режима; все независимые флаги в выключенном/включённом состоянии. Согласованы видимость стоимости, sideEffect, range/defence/domain, поля области/урона/щита/лечения и UI-default1d6+0. |
| 12 | Ritual/Hex формы | Актуальный nested createTemplate=true не включает устаревшие поля ritual HBS. У Hex выбран Medium и есть liftRequirement; данные моделей не получают отсутствующий legacy checkbox. |
| 13–14 | Конфигурация статусов | Оба typed словаря сохраняют ID/target и выбранный id статуса. percentage не редактируется этой формой. Настоящие inherited CRUD вызывают пути ID/field/-=ID; ActiveEffect CRUD с этими записями не смешан. |
| 15 | Локализация и изображения | В обоих языках нет DangerLow/DangerMedium/DangerHigh и ключа RemoveComponent с пробелом; в ru нет emanation. Отдельно проверен динамический Water-ключ. У всех 3 моделей отсутствует clickableImage, у картинок hex/ritual нет editImage action, у spell есть. |
| 16 | Граница castSpell | Полное исходное тело метода с подменами зависимостей: selfEffects передаётся применению через Object.values, но не попадает в templateInfo из-за length-ветви. Фиксированное лечение работает до передачи формулы, переменное бросает ReferenceError heal после вызова façade update STA. |
| 17 | Граница чата ритуала | Настоящий HBS показывает основной компонент '3x Known', альтернативный — '[object Object]'. Полный пофайловый разбор внешнего чат-шаблона этим не подменён. |

### Перекрёстная сверка и issues

Цепочки регистрации модель→лист→HBS и общие определения прослежены в обе стороны. Уточнены 17 прежних карточек: CommonItemData, damagePropertiesMigration, attackOptionsData, damagePropertiesData, defenseOptionsData, defensePropertiesData, itemEffectData, config, registerDataModels, WitcherItem, WitcherItemSheet, registerSheets, две базовые конфигурации, handlebars, settings, attackOptionsPart. Статическая сверка импортов/буквальных путей шаблонов распространена на все подготовленные карточки. Внешние региональные файлы остаются для .022; исполнение магии/полный чат — для последующих порций.

Созданы 10 отдельных potential issues:

| Проблема | Наблюдение |
| --- | --- |
| [issue-00128](../../issues/potential/issue-00128.md) | Миграции области заклинания и ритуала теряют параметры при смешанном или нулевом вводе |
| [issue-00129](../../issues/potential/issue-00129.md) | Форма ритуала редактирует прежние пути параметров области |
| [issue-00130](../../issues/potential/issue-00130.md) | Недоступный компонент ритуала теряет UUID для редактирования и удаления |
| [issue-00131](../../issues/potential/issue-00131.md) | Повторные компоненты ритуала нельзя независимо изменить или удалить |
| [issue-00132](../../issues/potential/issue-00132.md) | Обработчики компонентов ритуала не ожидают сохранение и заранее меняют массив |
| [issue-00133](../../issues/potential/issue-00133.md) | Словарь selfEffects заклинания не попадает в описание эффектов сообщения |
| [issue-00134](../../issues/potential/issue-00134.md) | Переменное лечение заклинанием обращается к неопределённой переменной heal |
| [issue-00135](../../issues/potential/issue-00135.md) | Сообщение ритуала выводит альтернативные компоненты как объекты |
| [issue-00136](../../issues/potential/issue-00136.md) | Изображения порчи и ритуала не привязаны к действию editImage |
| [issue-00137](../../issues/potential/issue-00137.md) | Часть подписей магии использует несовпадающие или отсутствующие ключи локализации |

Дополнены девять прежних issues: [issue-00062](../../issues/potential/issue-00062.md), [issue-00063](../../issues/potential/issue-00063.md), [issue-00064](../../issues/potential/issue-00064.md), [issue-00065](../../issues/potential/issue-00065.md), [issue-00067](../../issues/potential/issue-00067.md), [issue-00074](../../issues/potential/issue-00074.md), [issue-00075](../../issues/potential/issue-00075.md), [issue-00076](../../issues/potential/issue-00076.md), [issue-00098](../../issues/potential/issue-00098.md). Issue-00062 **не воспроизводится в специальной конфигурации spell**: она использует корректный attackOptionsPart, а прежняя ошибка находится в общей general. Issue-00098 покрывает повторный ключ с пробелом; новая карточка для него не создавалась. Всего 137 issues, все остаются potential; подтверждение, изменение статуса и исправление не выполнялись.

### Техническая проверка документов и сохранности

Проверка Python через stdin завершилась успешно: **621 исходник**, **181 карточка**, **440** неразобранных файлов; **137** issues, все в potential. Состав реестра совпал с Git и фактическим деревом. Все 621 исходник побайтно совпали с HEAD и срезом TASK-0001; общая SHA-256 содержимого **52701d3d0a5f054319886ac2a9d45b42c26c80098858d02518579c6a1edfaec4** не изменилась. Для всех **1035** ранее отслеживаемых файлов сохранены mode, uid, gid и inode.

Проверены **380 Markdown-документов в docs** и 2 корневых указателя, **8177 локальных ссылок** с существованием целей/якорей, структура таблиц, обязательные разделы карточек, имена собственных методов/полей, соответствие source→card и статусов задач. Для всех подготовленных карточек сверены **265 прямых относительных импортов** (в новой порции 23): **194 default**, **64 named-выражения с 69 именами**, **7 namespace**. Проверены определения экспортов и встречное упоминание источника в ранее разобранной цели. Для **113 буквальных связей с HBS** (в новой порции 6) подтверждены файлы и встречные ссылки там, где обе карточки уже существуют. Это статическая проверка связей, не запуск всех потребителей.

Изменены **60 документов**: 23 новых (13 карточек файлов и 10 issues), 37 ранее отслеживаемых (17 связанных карточек, 9 issues, 11 документов навигации/реестров/задачи/журнала). `git diff --check` прошёл. Весь прежний журнал, начиная с записи планирования третьей серии, сохранён побайтно; добавлена только текущая запись. TASK-0003.001–.021 имеют done, .022–.030 — planned; первая и вторая серии 61/96 файлов, третья 79 (13 выполнены/66 в очереди), 374 вне детализации. Новые задачи и карточки для прочитанных фрагментов соседних файлов не создавались.

### Ограничения и следующий шаг

Не выполнялись запуск мира, HTTP-загрузка системы, создание регионов, запись документов/сообщений, чтение действующих миров/компедиумных БД, сборка, npm test, установка стенда, изменение прав или коммит. Миграционные наблюдения не доказывают наличие затронутых записей у пользователя; вызов façade update STA не доказывает списание. Результат — проверенная документация данной версии, а не подтверждение исправности магии или правил книг. Продолжение по очереди — TASK-0003.022.

## Планирование TASK-0003.021–TASK-0003.030

Дата: 2026-09-11. Ветка `rusbar-main`, HEAD `8cddfd69723128588ab90357c95f0ecf6fc2419b`. На старте рабочее дерево чистое, отслеживаются 1025 файлов. Базовый срез TASK-0001 — `15da5b225535e34af4e132c701b5353ef4eb667f`; все 621 включённый исходник совпадают с ним.

### Основание и состав плана

Пользователь согласовал следующую серию из десяти подзадач и увеличение ориентиров: 12–16 связанных файлов, до 20 небольших однотипных моделей/шаблонов, 2–5 файлов сложных центральных обработчиков. Объём выбирается по связности и числу ветвей, а не для достижения квоты.

| Подзадача | Порция | Файлов | Логических строк |
| --- | --- | --- | --- |
| [TASK-0003.021](../../tasks/task-0003.021.md) | Магические предметы: модели, формы и компоненты ритуалов | 13 | 936 |
| [TASK-0003.022](../../tasks/task-0003.022.md) | Области заклинаний и события регионов | 5 | 289 |
| [TASK-0003.023](../../tasks/task-0003.023.md) | Расследования: тайны, улики и препятствия | 14 | 449 |
| [TASK-0003.024](../../tasks/task-0003.024.md) | Контейнеры и хранение предметов | 3 | 136 |
| [TASK-0003.025](../../tasks/task-0003.025.md) | Общие листы Actor и подготовка контекста | 2 | 625 |
| [TASK-0003.026](../../tasks/task-0003.026.md) | Действия инвентаря и контекстное меню Item | 2 | 528 |
| [TASK-0003.027](../../tasks/task-0003.027.md) | Инвентарь Actor: вкладки и таблицы предметов | 12 | 1375 |
| [TASK-0003.028](../../tasks/task-0003.028.md) | Общий бросок, критические результаты и вспомогательные функции | 5 | 372 |
| [TASK-0003.029](../../tasks/task-0003.029.md) | Навыки: броски, развитие и пользовательские навыки | 14 | 763 |
| [TASK-0003.030](../../tasks/task-0003.030.md) | Характеристики, модификаторы и проверки состояния | 9 | 424 |
| **Всего** | **Третья серия** | **79** | **5897** |

В списках 41 JS и 38 HBS. Число логических строк получено через read_bytes().splitlines(); оно используется для оценки объёма, не для определения завершённости анализа. Полные списки находятся в подзадачах, сводка — в [TASK-0003](../../tasks/task-0003-remaining-files.md#третья-серия-task-0003021task-0003030).

В .025 включена промежуточная сверка первых 37 файлов .021–.025 с прежними 168; в .030 — итоговая сверка всех 79 с прежними 168. Сверка каждой отдельной порции также обязательна. Чтение соседнего определения при выполнении задачи не даёт полной карточки этому соседу.

### Фактически выполненная проверка

План составлялся по текущему реестру, перечню файлов, числу строк, определениям/импортам JS, полям и включениям HBS, местам регистрации и найденным потребителям. Проверены конкретные границы: модели/формы магии отделены от создания регионов и выполнения castSpell; модели/редакторы расследования — от общего броска; контейнер — от общих действий инвентаря; классы листов, обработчики и таблицы Actor — от будущего полного разбора специализированных листов и боя.

Использованы rg, чтение локальных исходников/документов, git status/rev-parse/ls-files/show и Python через stdin для проверки состава, байтов и ссылок. Код игровых методов не исполнялся, мир/браузер не запускались. Подробные карточки исходников не создавались. Строки списка и формулировки «предмет разбора» являются заданием на исследование; полного содержательного анализа 79 файлов пока нет.

Проверка списков и сохранности завершена: десять новых задач имеют planned, первые двадцать остаются done. Все 79 новых путей существуют, имеют статус «Не начат», не повторяются между порциями и не пересекаются с прежними 157 файлами TASK-0003 или 11 файлами TASK-0002. После распределения 79 из 453 неразобранных файлов остаются 374 без подзадач. Проверены 71 прямой относительный путь импорта и 44 буквальные связи с HBS в новых списках; цели существуют. Это проверка адресов для плана, не завершённая проверка поведения этих зависимостей.

Все 621 исходник побайтно совпадают с текущим HEAD и срезом TASK-0001. Реестр файлов, 168 карточек и все issues остались неизменными. Для 1025 ранее отслеживаемых файлов сохранены mode, uid, gid и inode. Историческая часть журнала начиная с TASK-0003.020 сохранена побайтно.

Проверены 357 Markdown-файлов в docs и два корневых указателя: 7675 локальных ссылок/якорей разрешаются; примеры ссылок внутри кода не считаются навигацией. Таблицы изменённых документов имеют согласованное число столбцов, git diff --check проходит. Изменены ровно 17 документов: десять новых задач, родительская задача, реестр задач, README проекта/аналитики/исследования, CHANGELOG и журнал. Код, игровые данные, ветки Git, службы и права не изменялись; коммит не создавался.

### Решения о размере и ограничениях

Магические предметы, расследования, навыки и таблицы инвентаря образуют порции по 12–14 файлов. Два общих листа Actor занимают 625 строк, а два файла действий инвентаря — 528 строк с многочисленными методами, поэтому их объём оставлен небольшим. Контейнер образует отдельную трёхфайловую цепочку с записью двух документов. Порция характеристик включает девять связанных файлов; дополнительные темы ради количества не добавлялись.

В списки включены старые варианты листов/таблиц и два deprecations-шаблона, уже входящие в реестр: задачи требуют установить реальных потребителей, а не выводить активность по имени или расположению. Более поздние задачи серии могут полностью разбирать зависимости предыдущих: для расследования helper/rollSkill до .028/.029 проверяются только точечно. Порядок выполнения не представлен как топологическая сортировка всех зависимостей.

Существующие issues указаны как ориентиры будущей сверки, а не как уже подтверждённые результаты новых подзадач. Новые проблемы и задачи исправления при планировании не регистрировались. Запросы в GitHub, проверка правил рулбука, изменения игровых данных и тестовый стенд в эту работу не входили.

### Результат

Созданы TASK-0003.021–TASK-0003.030 со статусом `planned`. Обновлены [реестр задач](../../tasks/README.md), родительская задача, README проекта/аналитики/исследования и CHANGELOG. В общем порядке исследования отражены новые согласованные ориентиры размера. Устранена устаревшая формулировка текущего итога родительской задачи после .019: добавлен уже выполненный результат .020; исторические проверки в журнале сохранены.

Покрытие осталось **168 из 621**, не разобраны **453**. Из них **79** стоят в очереди, **374** требуют дальнейшей детализации. После выполнения серии прогнозируется **247** проверенных и **374** неразобранных файла; это не достигнутый результат. Следующая задача — [TASK-0003.021](../../tasks/task-0003.021.md), выполнение не начато. TASK-0003 остаётся `in-progress`, TASK-0004/TASK-0005 — `draft`.

## TASK-0003.020

Дата: 2026-09-11. Ветка `rusbar-main`, HEAD `b09f992960a76d1c75946f402e42d93fa0785008`; рабочее дерево на старте чистое, отслеживаются 1008 файлов. Все 621 исходник совпадают со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. Foundry 14.367.0 по /opt/foundryvtt/package.json, Node 24.16.0.

### Полный охват порции

| Файл | Логических строк |
| --- | --- |
| [module/data/item/criticalWoundData.js](../../../module/data/item/criticalWoundData.js) | 107 |
| [module/item/sheets/WitcherCriticalWoundSheet.js](../../../module/item/sheets/WitcherCriticalWoundSheet.js) | 22 |
| [module/actor/sheets/mixins/criticalWoundMixin.js](../../../module/actor/sheets/mixins/criticalWoundMixin.js) | 32 |
| [module/actor/mixins/healMixin.js](../../../module/actor/mixins/healMixin.js) | 25 |
| [module/actor/sheets/mixins/healMixin.js](../../../module/actor/sheets/mixins/healMixin.js) | 123 |
| [templates/sheets/item/criticalWound-sheet.hbs](../../../templates/sheets/item/criticalWound-sheet.hbs) | 36 |
| [templates/partials/crit-wounds-table.hbs](../../../templates/partials/crit-wounds-table.hbs) | 40 |
| [templates/dialog/heal/heal-rest.hbs](../../../templates/dialog/heal/heal-rest.hbs) | 17 |
| [templates/chat/heal/resting-status.hbs](../../../templates/chat/heal/resting-status.hbs) | 23 |
| [templates/chat/combat/heal.hbs](../../../templates/chat/combat/heal.hbs) | 3 |

Полностью прочитаны 10 файлов, 428 логических строк: 5 JS и 5 HBS. Подготовлены 10 карточек; уточнены 18 ранее разобранных: [system.json](files/system.json.md), [module/setup/registerDataModels.js](files/module/setup/registerDataModels.js.md), [module/setup/registerSheets.js](files/module/setup/registerSheets.js.md), [module/setup/settings.js](files/module/setup/settings.js.md), [module/TheWitcherTRPG.js](files/module/TheWitcherTRPG.js.md), [module/setup/config.js](files/module/setup/config.js.md), [module/setup/handlebars.js](files/module/setup/handlebars.js.md), [module/data/dataUtils.js](files/module/data/dataUtils.js.md), [module/actor/witcherActor.js](files/module/actor/witcherActor.js.md), [module/item/witcherItem.js](files/module/item/witcherItem.js.md), [module/item/sheets/WitcherItemSheet.js](files/module/item/sheets/WitcherItemSheet.js.md), [module/item/sheets/configurations/WitcherConfigurationSheet.js](files/module/item/sheets/configurations/WitcherConfigurationSheet.js.md), [templates/sheets/actor/partials/character/tab-effects.hbs](files/templates/sheets/actor/partials/character/tab-effects.hbs.md), [module/data/actor/templates/common/stats/derivedStatsData.js](files/module/data/actor/templates/common/stats/derivedStatsData.js.md), [module/data/actor/templates/common/stats/statsData.js](files/module/data/actor/templates/common/stats/statsData.js.md), [module/data/actor/templates/common/combatEffectsData.js](files/module/data/actor/templates/common/combatEffectsData.js.md), [module/item/mixins/consumeMixin.js](files/module/item/mixins/consumeMixin.js.md), [module/activeEffect/witcherActiveEffect.js](files/module/activeEffect/witcherActiveEffect.js.md). Соседние Actor-листы, itemMixin, damageMixin и generalCombatHook прочитаны только в пределах связей и не получили полного статуса.

### Методика и выполненные сценарии

Исполнены исходные CriticalWoundData, обе healMixin, criticalWoundMixin, дочерний WitcherCriticalWoundSheet, createEnrichedText и выделенный _onItemInlineEdit. Модель использовала настоящие TypeDataModel/DataModel/fields Foundry; родители — минимальные DataModel-фасады, не client Actor/Item. Конкретные методы вызваны из исходников, их тела не заменялись переписанной реализацией.

Команда — `node --input-type=module` с программой через stdin. Записи Item/Actor и чата, UUID-поиск, DialogV2, DOM/querySelector/addEventListener и базовый класс листа представлены регистраторами/управляемыми Promise. TextEditor возвращал отличимый HTML-маркер. Roll был фасадом с заданным total=6; случайные кубики/парсер не проверялись. Handlebars 4.7.9 и parse5 настоящие; formInput/formGroup регистрировали аргументы поля, не создавали реальные виджеты. Для speaker из /opt/foundryvtt/client/documents/chat-message.mjs исполнены getSpeaker и три private helper над фасадами Actor/canvas/user. Common Document.createEmbeddedDocuments, ClientDatabaseBackend и DataModel.cleanData прочитаны для контракта создания; полноценные DB-операции не запускались.

| Группа | Способ | Фактический результат |
| --- | --- | --- |
| 1. Схема/сроки | Настоящая CriticalWoundData и классы Foundry | 9 полей; BODY 5→simple3/complex7/difficult10; BODY 20→минимум1. deadly/unknown сохраняют 99; Item без Actor остаётся на исходном0. Source healingTime при расчёте не переписан. |
| 2. Валидация | Настоящие поля модели | daysHealed='2.5'→2.5; healingTime=−1 и произвольные criticalLevel/treatment/location принимаются. Это факты схемы без решения о допустимых игровых границах. |
| 3. Обогащение | Настоящий createEnrichedText, TextEditor-маркер | description получает value/enriched/systemField с fieldPath=system.description; source не записывается. |
| 4. Ветки heal | Настоящий heal, операции Item перехвачены | none/stabilized с 0 днями →update({}); treated +1 и ещё +2 при новой стерилизации; достигнутый срок→delete. none с днями3/сроком3 тоже→delete. deadly не удаляется. |
| 5. Стерилизация | Два heal; между ними применены флаг/счётчик через updateSource, reset и prepareDerivedData | BODY 1/simple: первый день3, после фиксации sterilized второй день4. Второй update содержит только daysHealed=4; флаг не даёт ещё +2. |
| 6. Item без Actor | Настоящий prepareDerivedData/heal | Начальная none-травма с 0/0 дала delete. Это прямой вызов модели; кнопка такого heal у standalone Item не найдена. |
| 7. Переход/pending | Настоящий treat, UUID-фасад и отложенные create/delete | Запрошены create затем delete, но treat уже завершён при обоих pending. Поля/effects followUp переданы как часть найденного Item; ручного копирования прежних дней нет. |
| 8. Недоступная ссылка | fromUuid→null, создание возвращает контролируемый rejected Promise | create('Item',[null]) и delete уже вызваны. Ошибка создания не удерживает удаление; реальная БД не запускалась. |
| 9. Ошибка разрешения | fromUuid отклоняет Promise | treat завершился ошибкой до create/delete. Этот случай отличается от ошибки создания после разрешения. |
| 10. Переход без Actor | Standalone Item с непустым followUp | После resolve TypeError на createEmbeddedDocuments; delete не вызван. |
| 11. Заживление/pending | heal при незавершённом update | Метод вернулся; дни в подготовленной модели1, source0. Исходный update не ожидается. |
| 12. Лист травмы | Исходный дочерний класс, superclass/Item — фасады | Размер600×620, один PARTS.main; Drop weapon сохранил его UUID как followUp, вернулся до update. |
| 13. Слушатели травмы | Исходная примесь и DOM/UUID-фасады | Добавление передало name/type; treat вызван один раз. Зарегистрированы 3 селектора; неизвестный id→TypeError. Искусственный delete-crit→отсутствующий _onCriticalWoundRemove; текущая разметка с таким элементом не найдена. |
| 14. Inline-edit | Исходный _onItemInlineEdit и настоящая очистка модели | Запрос system.daysHealed='2.5', модель получает число2.5. data-dtype не преобразует вручную в этом handler, но ошибка типа сохранения не установлена. |
| 15. Открытие/отмена | Исходный _onHeal с DialogV2/DOM-фасадами | modal=false, render force=true, 4 change-слушателя; открытие и callback cancel не записали Actor. |
| 16. Переключение | Исходный updateHealAmount, REC 7 | Все флаги→14; все выключены→3, isResting/isSterilized остались true. isHealingHand/isHealingTent остаются false; сейчас чат их не читает. |
| 17. Несколько окон | Два _onHeal при REC 7/20 | Глобальный querySelector получил первые поля; на одном resting 2 listener, один extra-info в конце показывает +20. Это проверка изолированной адресации, не открытые браузерные окна. |
| 18. Восстановление/сообщение | recoverActor + HBS, записи/коллекция/чат — фасады | HP 9/10,totalRec3→update HP10,STA20,Vigor3; критическая травма получила heal(false). Метод и чат завершились до её pending heal. Чат сообщает3 и resting, уведомление active, раздел дней скрыт; speaker ищется по name. |
| 19. Величина лечения | Actor.calculateHealValue; Roll-фасад возвращал6 | HP 5/10: 1d6→5; строка'2' остаётся строкой, '2+3' не вычисляется, отрицательное не ограничено снизу. HP 12/10→−2; null/undefined→TypeError includes. Это не проверка Roll-парсера. |
| 20. Speaker Actor | Исходный createHealMessage и 4 метода core ChatMessage | Для лечимого id=healed при character пользователя id=other получилось speaker.actor=other. У Actor нет this.actor для переданного аргумента; ядро выбирает запасной источник. |
| 21. Пять шаблонов | Handlebars 4.7.9, parse5; formInput/formGroup — регистраторы полей | 3 поля helper адресованы system.description/lesserEffect/followUp; value/enriched переданы. Один partial→1 строка, родитель→2 строки/2 кнопки. heal='<x>' экранирован. Штатный resting-status не показывает дней. |
| 22. Локализация | Раскрытие JSON en/ru, буквальные ключи порции плюс 3 словаря CONFIG | 44 разных ключа, пропусков нет в обеих локализациях. Старый WITCHER.CritWound.HealingTime.Label существует как составной ключ; не зарегистрирован ложный issue о его отсутствии. |

Все 22 группы завершены. В подготовке диагностики исправлены две неверные предпосылки самого сценария: пробная строка с буквой d попадала в Roll-ветку фасада, а старый ключ подписи существует в локализации. Между двумя днями стерилизации после reset повторён prepareDerivedData, как требует проверяемая модель; окончательный результат — update до 4 дней, не удаление по устаревшему нулевому сроку. Эти уточнения не меняли код системы. Временные исполняемые файлы и тестовый стенд не создавались.

### Перекрёстная сверка текущих процессов

| Цепочка | Что сверено |
| --- | --- |
| Тип/регистрация → модель → форма | system.json → registerDataModels/registerSheets → CriticalWoundData/WitcherCriticalWoundSheet → основной HBS. 9 полей и source/derived healingTime разделены; общая configuration предоставляет Item.effects. |
| Индекс → получение травмы | ready индексирует criticalLevel/location/lesserEffect/treatment; applyCritWound читает их из выбранного pack, разрешает Item и вызывает addItem. Эта ветвь не запускает heal/treat и не определяет переходы followUp. |
| Actor-вкладка → кнопка/inline → Item | CriticalWoundListener берёт UUID кнопки; itemMixin берёт id строки. Ручной ввод дней очищается NumberField; duplicate partial относится к отображению. Современные Character/Monster используют один tab-effects. |
| Отдых → HP/STA/Vigor → дни Item → переход | recoverActor ждёт запись шкал, затем запускает heal для всех травм без ожидания. heal начисляет дни только treated, сравнивает срок для всех и вызывает treat; create/delete в treat не ожидаются. |
| Item → ActiveEffect → Actor | Модель травмы не содержит таблицы бонусов и не интерпретирует treatment как changes. Foundry Actor.allApplicableEffects перечисляет transfer-эффекты Item; WitcherActiveEffect определяет подавление. Отдельные Actor.effects не очищаются лечением автоматически. |
| Регенерация/расходование → calculateHealValue | GeneralCombatHook и consume используют общую примесь Actor. У каждого отдельная запись HP; дни травм не участвуют. Rest использует собственную сумму REC. Известная issue-00022 сохранена. |
| Контекст → сообщения/локализация | HBS потребляет actualWoundList, которого нет в producer; totalRec не равен гарантированному приросту. Speaker отдельно от видимого actor.name. Все проверенные en/ru подписи найдены. |

### Итоговая сверка второй серии с прежними 72 файлами

Перечни TASK-0003.011–TASK-0003.020 объединены по полным путям: 96 различных файлов (60 JS, 36 HBS), пересечение с 72 ранее разобранными пустое. Текущая совокупность — 168 карточек. Сопоставлены исторические итоги каждой порции, определения импортируемых сущностей, таблицы зависимостей и известные потребители; прежние сценарии не запускались повторно и не объявлены новыми успешными тестами.

| Порция | Файлов | Сопоставленные связи |
| --- | --- | --- |
| [TASK-0003.011](../../tasks/task-0003.011.md) | 7 | База ItemSheet/configuration, PARTS/TABS, FormData и встроенные ActiveEffect; CriticalWoundSheet использует тот же контекст, не отдельный обработчик эффектов. |
| [TASK-0003.012](../../tasks/task-0003.012.md) | 10 | Вложенные attack/defense/damage-модели и миграция остаются общими для разных Item/профессии. Их числовые и формальные контракты сверены с карточками потребителей, а лечение их не использует. |
| [TASK-0003.013](../../tasks/task-0003.013.md) | 8 | WeaponData/лист/боевые формы читают вложенные модели .012; Item/Actor вызывают методы предмета. Настроенные воздействия и ActiveEffect — разные структуры. |
| [TASK-0003.014](../../tasks/task-0003.014.md) | 9 | Armor/Enhancement и itemEffect связаны с подготовкой Item/Actor и .012. Прежние риски миграции/передачи effects сохраняются; повторные игровые проверки не объявлены. |
| [TASK-0003.015](../../tasks/task-0003.015.md) | 15 | ConsumableProperties→consume→Actor.calculateHealValue и applyActiveEffectToActorViaId. Полный новый разбор heal уточнил прежний точечный consumer; расходование не двигает дни травм. |
| [TASK-0003.016](../../tasks/task-0003.016.md) | 12 | Component/Diagram, recipe/item UUID, состав компонентов и редакторы сопоставлены с repair .017. Разрешение ссылок — отдельный шаг от наличия строки UUID; сама ссылка не копирует документ. |
| [TASK-0003.017](../../tasks/task-0003.017.md) | 5 | RepairSystem/RepairData, repairMixin, costEdit и сообщения: передача UUID/стоимости, отдельные socket/query. Прежние блокировки ремонта сохраняются; похожий глобальный DOM отдыха имеет отдельный issue. |
| [TASK-0003.018](../../tasks/task-0003.018.md) | 8 | Race/Homeland, фиксированные особенности и регионы, enrichment и Actor-показ. Текстовые поля не превращаются автоматически в changes. CommonItemData наследуется расой, но не Homeland/CriticalWound. |
| [TASK-0003.019](../../tasks/task-0003.019.md) | 12 | Profession/пути/usage/thresholds и конфигурация: вложенные .012, временные HP и Actor-потребители. Временные HP не очищаются новым отдыхом; заживление Item — другой процесс. |
| [TASK-0003.020](../../tasks/task-0003.020.md) | 10 | CriticalWoundData→форма/таблица→treat/heal→отдых/чат; общие классы Item, Actor и ActiveEffect сверены с 72 прежними карточками. |

Автоматизированная часть сверки охватила 242 прямых относительных import-связи всех описанных JS: 77 исходят из второй серии, 42 соединяют вторую серию с прежними 72 файлами. Проверены 174 default-импорта и 66 имён экспортов в 61 именованном import; ещё 7 namespace-import проверены как ссылки на модули. Все пути существуют, исходящие ссылки присутствуют в карточках, обратные упоминания есть у уже описанных получателей. Дополнительно сверены 107 разных пар «описанный источник → буквальный путь HBS системы» с теми же проверками направления и известных потребителей. Расхождений этих указателей не найдено; это проверка структуры связей, не доказательство правильности функций.

57 различных целей импортов ещё не разобраны целиком: среди них большие примеси Actor (бой, профессия, навыки, изготовление), листы Actor и оставшихся Item, модели заклинаний/контейнеров/расследований, сообщения, rollConfig/extendedRoll, combat и регионы. Их определения для отдельных вызовов проверялись, но полный разбор не засчитан. Внешние вызовы модулей/макросов, динамические UUID/followUp/таблицы действующих миров, вычисляемые пути и браузерный жизненный цикл остаются за пределами установленного графа. Отсутствие найденного потребителя, например .delete-crit, не означает отсутствия внешних вызовов.

Остаток — 453 файла, все пока вне детализированных подзадач: module 89, templates 90, packsJson 226, styles 36, lang 8, utils 2 и два корневых файла (build.json/package.json). Новые подзадачи этой сверкой не создавались. TASK-0003 остаётся in-progress; TASK-0004/TASK-0005 — draft.

### Проблемы и пределы выводов

Добавлены 7 отдельных potential issues: [issue-00121](../../issues/potential/issue-00121.md) — переход к следующей травме удаляет исходный item до завершения создания; [issue-00122](../../issues/potential/issue-00122.md) — завершение заживления проверяется вне условия treatment=treated; [issue-00123](../../issues/potential/issue-00123.md) — несколько диалогов отдыха используют поля первого окна; [issue-00124](../../issues/potential/issue-00124.md) — сообщение отдыха сохраняет флаг после снятия галочки; [issue-00125](../../issues/potential/issue-00125.md) — отчёт об отдыхе не получает фактические результаты восстановления; [issue-00126](../../issues/potential/issue-00126.md) — сообщения лечения могут выбирать другого actor как отправителя; [issue-00127](../../issues/potential/issue-00127.md) — методы лечения и отдыха завершаются до вложенных записей. Дополнены issue-00022/00034/00054/00106. Все 127 проблем остаются в potential; подтверждение, исправление и закрытие не выполнялись.

Не объявлены новыми проблемами: допустимая передача Document в createEmbeddedDocuments; существующий ключ HealingTime.Label; числовая очистка inline-строки; отсутствие ограничений choices/min/max само по себе; неиспользуемая текущими шаблонами ветвь delete-crit; передача строки без d без отдельного согласованного контракта формулы. Исследование описывает код, а не утверждает его соответствие правилам рулбука.

### Структурная проверка и сохранность

Проверка через Python/stdin и git diff --check завершена без ошибок: 621 строка реестра, 168 карточек в точном соответствии проверенным строкам, 453 неразобранных файла; все 20 подзадач имеют done, родитель in-progress. Состав Git и фактического дерева совпадает после согласованных исключений. Все 621 исходник побайтно равны HEAD и срезу TASK-0001; сводная SHA256 неизменна. Для всех 1008 ранее отслеживаемых файлов сохранены mode, uid, gid и inode.

Проверены 347 Markdown-файлов в docs и два корневых указателя: 7289 локальных ссылок и якорей разрешаются; примеры ссылок внутри кода не считаются навигацией. Таблицы изменённых документов имеют согласованное число столбцов, лишних конечных пробелов нет. Новые карточки содержат все 11 разделов, методы и поля текущих исходников. Реестр issues содержит непрерывные ID 00001–00127, все в potential. Состав изменений строго соответствует 50 документам: 10 новых карточек файлов, 18 связанных, 7 новых issues, 4 прежних issues и 11 документов навигации/задач/журнала. Историческая часть журнала начиная с TASK-0003.019 сохранена побайтно.

Структурные проверки импортов и HBS описаны выше отдельно от исполнения 22 групп сценариев. Запуск мира, браузерные сохранения, сеть, игровые БД, сборка и изменения прав не выполнялись.

### Результат

TASK-0003.020 завершена; вторая серия полностью разобрана и сверена. Покрытие — **168 из 621 файла**, не разобраны **453**. Изменена только документация. Код системы, игровые данные, Git-ветки, служба и права доступа не менялись; коммит не создавался.

## TASK-0003.019

Дата: 2026-09-10. Ветка rusbar-main, HEAD `c26eb64dd54cc434087f54c3c6b678b6092b15a2`; рабочее дерево на старте чистое, отслеживаются 985 файлов. Все 621 исходник совпадают со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. Foundry 14.367.0 по /opt/foundryvtt/package.json, Node 24.16.0.

### Полный охват порции

| Файл | Логических строк |
| --- | --- |
| [module/data/item/professionData.js](../../../module/data/item/professionData.js) | 115 |
| [module/data/item/templates/professionPathData.js](../../../module/data/item/templates/professionPathData.js) | 12 |
| [module/data/item/templates/professionSkillData.js](../../../module/data/item/templates/professionSkillData.js) | 21 |
| [module/data/item/templates/profession/skillUsageData.js](../../../module/data/item/templates/profession/skillUsageData.js) | 23 |
| [module/data/item/templates/profession/temporaryHealthData.js](../../../module/data/item/templates/profession/temporaryHealthData.js) | 37 |
| [module/data/item/templates/profession/thresholdData.js](../../../module/data/item/templates/profession/thresholdData.js) | 18 |
| [module/item/sheets/WitcherProfessionSheet.js](../../../module/item/sheets/WitcherProfessionSheet.js) | 35 |
| [module/item/sheets/configurations/WitcherProfessionConfigurationSheet.js](../../../module/item/sheets/configurations/WitcherProfessionConfigurationSheet.js) | 212 |
| [templates/sheets/item/profession-sheet.hbs](../../../templates/sheets/item/profession-sheet.hbs) | 169 |
| [templates/sheets/item/configuration/partials/profession/skillPathPart.hbs](../../../templates/sheets/item/configuration/partials/profession/skillPathPart.hbs) | 5 |
| [templates/sheets/item/configuration/partials/profession/skillPathSkillPart.hbs](../../../templates/sheets/item/configuration/partials/profession/skillPathSkillPart.hbs) | 122 |
| [templates/sheets/item/configuration/partials/profession/profAttackOptionsPart.hbs](../../../templates/sheets/item/configuration/partials/profession/profAttackOptionsPart.hbs) | 12 |

Всего **12 файлов, 781 логическая строка**. Полностью разобраны ProfessionData (7 методов), две фабрики пути/навыка, три вложенные DataModel, основной лист (1 метод), конфигурация (11 методов) и 4 HBS. Сверены 13 прямых относительных импортов, регистрация, контекст, поля и все собственные действия. Подготовлены 12 новых карточек; уточнены 18 связанных.

Внешние Actor-потребители (professionMixin, defenseMixin, itemMixin, _prepareCharacterData и tab-profession), примесь Item-защиты, редактор/диспетчер ядра, CSS и локализация прочитаны в пределах проверяемых связей. Их полный аудит не заявлен и статус не повышен. Компедиумы и игровые данные не менялись.

### Методика и подмены

JavaScript выполнен через Node stdin, без файлов стенда. Настоящие DataModel/TypeDataModel/fields/common BaseItem Foundry и системные модели/фабрики загружены по registerDataModels. Настоящий WitcherItem работал поверх common BaseItem, не client Item. Источник контрольного документа сравнен до/после через toObject.

Настоящие ItemSheetV2/HandlebarsApplicationMixin/DragDrop исполнены поверх DocumentSheet-фасада; специализированные классы системы импортированы без правок. _prepareTabs/_getTabsConfig взяты из ядра Application. _onChangeForm родительского фасада только фиксирует coreSubmit: обработка реального FormData/сохранение не моделируется. Полное слияние опций/жизненный цикл окон и клиентские права не проверялись.

Handlebars 4.7.9/parse5, formInput/formGroup/selectOptions/prepareSelectOptionGroups и системный has настоящие. HTMLField.toInput и 11 входов редактора реально вызваны; ProseMirror.create заменён HTML-регистратором. Для formGroup конфигурации/SetField использованы фасады реальных DataField с фиксацией path,label,value,options: это проверка связывания/условий, не реализация виджетов Foundry. Для Actor-editor вызваны настоящие editor/createEditorInput и минимальный DOM; TextEditor.enrichHTML возвращал отличимый маркер. Реальные UUID не разрешались.

Выполнены настоящие выбранные методы professionMixin/itemMixin/defenseMixin и модельные методы защиты. Actor/коллекции/цели/запись представлены фасадами. Dialog возвращал контролируемый выбор или пустую строку. doProfessionSkillRoll в проверках использования заменён заданным rollOver; настоящий метод отдельно вызван для отсутствующего stat. Roll временных HP сохранял формулу и возвращал total7, без случайных кубиков. ActiveEffect сохранял переданный payload; query/toMessage фиксировались, без сети/БД. Это не проверка реального получения/расхода временных HP.

Шесть update-проверок возвращали pending Promise, чтобы отделить завершение метода от записи; Promise затем разрешены. Диспетчер #onClickAction ядра выполнен как извлечённое тело с переименованием приватного метода для вызова, остальное тело сохранено; событие/элемент подменены. Это не click в браузере.

### Выполненные сценарии

| Группа | Фактический результат |
| --- | --- |
| 1. Схема/значения | 14 верхних полей ProfessionData;4 поля пути;8 полей навыка;10 независимых слотов. Начальные строки/level0 и вложенные defaults сверены. Произвольный stat и level=-2 приняты; у HP.stat blank запрещён. ProfessionSkills в памяти Set устраняет дубликаты, toObject сохраняет входной массив. |
| 2. Обогащение/основная форма | 11 реальных createEnrichedText для 10 definition и notes; source сохранён. Основной HBS дал 47 именованных элементов и 11 HTML-входов с нужными fieldPath/value/enriched. |
| 3. Обычные навыки/Drop | 52 UI-ключа найдены в схеме character. На фасаде Actor _onDropItem сначала сбросил флаги, затем передал awareness=true и неизвестный system.skills.undefined.missing.isProfession=true; remove/add profession зафиксированы. |
| 4. Листы/вкладки | Фактическое имя класса WitcheProfessionSheet; специальная конфигурация;9 statOptions записаны в общий CONFIG.WITCHER. Пять вкладок, названия путей берутся как есть, включая пустые. General не вывел полей;4 категории ActiveEffect доступны. |
| 5. Ветви конфигурации | Путь 1 с 2 полными навыками и 1 пустым дал 74 formGroup; пустые пути 2/3 —по 12. Четыре главных флага у выключенного навыка,35 полей у полного. DefiningSkill не появился ни в одной части конфигурации. Проверены raw row id/target/field. |
| 6. CRUD/pending | Шесть методов дали expected system.skillPath1.skill1 пути: add effects percentage0;edit on→false;delete -=fx;add threshold value0;edit value строка 9;delete -=th. Все завершились до разрешения update; это не доказанная потеря записей. |
| 7. Change-handler | _onChangeForm сначала вызвал coreSubmit-фасад, затем спецupdate thresholds.th.value='12'. Реальная обработка FormData не исполнялась. |
| 8. Удаление по click | Действие removeEffectDamageProperties отсутствует в actions (есть removeEffect); core dispatcher отправил его в fallback, update0. Прямой remove с currentTarget приложения дал TypeError dataset; контроль с currentTarget строки дал правильный payload. |
| 9. Идентификация навыка | Два Dup в путях и Dup в definingSkill: конфигурация выбрала path1.skill1, Actor — definingSkill. Пустое имя выбрало первый пустой слот; неизвестное→undefined, addThreshold→TypeError path. Defining-only Main не найден конфигурацией. |
| 10. Защита | Guard/ref/level2/defendsAgainst melee/modifier3/isDefense=false дал true и полноценный option; он сохранён через WitcherItem и Actor до вызова skillDefense. Из двух защит выбран первый Guard; отсутствие даёт undefined, defining-only не подходит. Attack передаётся корректно. |
| 11. Маршрут использования | Реальный _onProfessionRoll выбрал attack→custom usage→threshold→обычный roll согласно флагам; выбранные операции были регистраторами, полный бой не запускался. |
| 12. Пустая характеристика | Actor-HBS свежей профессии дал 10 кнопок profession-roll, поскольку stat='' отличается от none. Настоящий doProfessionSkillRoll прочитал stats[''].value и бросил TypeError до кубика. |
| 13. Пороги | Пустой словарь дал пустой select и TypeError value после выбора ''. Один Easy5 передан без prompt; два — выбор b передал B8. |
| 14. Получатель | [applySelf,applyOnTarget] false/false,true/false,false/true,true/true дали caster,caster,target,target и DC24/24/12/12. Нет цели при applyOnTarget=true→noTarget, ранний возврат. |
| 15. Временные HP | rollOver0 не создал эффекта;3→3d6,9 при cap5→5d6. Принудительный total7 вошёл в JSON name/value; level2 с default duration→4 раунда. Создан один ADD-change и query на applyActiveEffectToActor. |
| 16. Длительность | level3:2*@level→6;10→10;строки 2 и 2+@level→TypeError чтения match[0] у null. Это парсинг текущего кода, не сверка игровых правил. |
| 17. JSON/модель результата | Aid дал JSON{name:Aid,value:7}, принятый настоящей TemporaryEffects. Имя Aid с двойными кавычками создало невалидную JSON-строку; JSON.parse→SyntaxError. Применение/расход эффекта в клиенте не проверялись. |
| 18. Actor-описания | Реальный _prepareCharacterData подготовил 11 HTML профессии;11 editor в исходном tab-profession использовали raw, маркер потерян, @UUID осталась. То же место/helper дополняет issue-00109. |
| 19. Локализация | 157 ключей из порции, схем и вариантов. В en отсутствуют 2 прежних skillMap label;в ru —те же 2 и 3 thresholds. Все 52 значения professionSkills сопоставлены с ключами навыков character. |

Все 19 групп завершены. Первое предположение о потере attack было опровергнуто исполнением настоящей модели и повторным чтением строки 106: createDefenseOption передаёт аргумент. Это ошибка первоначального прочтения, не проблема системы; прежняя issue-00071 описывает верный результат. Недостающий logCompatibilityWarning добавлен только в фасад окружения; первая выдача большого JSON была усечена инструментом, повторная выдача сохранена полностью. Код системы и журнал прежних проверок из-за этих ошибок не менялись.

### Перекрёстная сверка связей

| Цепочка | Сопоставление |
| --- | --- |
| Регистрация → модель → формы | system.json Item.profession → registerDataModels → ProfessionData → WitcheProfessionSheet и специальная конфигурация. Восемь общих полей+шесть новых;11 HTML-путей совпадают с декларацией. |
| Модель навыка → разные потребители | definingSkill и 9 слотов имеют одну professionSkill-схему. Основная форма редактирует все 10; конфигурация и модельный выбор защиты только 9 путей; Actor.findSkillWithName сначала definingSkill. |
| DataField → formGroup → CRUD | Полные path именованных полей получаются из схемы. Ручные effects/threshold rows передают ID записи и skillName. Поиск по имени, actions и ожидание update проверены независимо от рендера. |
| Профессиональный список → Actor | professionSkills — Set обычных навыков из 52 вариантов; Drop меняет isProfession, не уровень. Сначала сброс, затем установка выбранных флагов; неизвестный ключ не защищён. Это не десятка собственных профессиональных навыков. |
| Защита → Item → Actor | defendsAgainst.has(attack) → первый path/slot → option с modifier/skillOverride → defenseOptionMixin → prepareAndExecuteDefense → skillDefense. isDefense и definingSkill пропущены в прежних границах; аргументы не теряются. |
| Атака → оружие/собственный бросок | isAttack имеет приоритет. usesWeapon → выбор оружия и additionalDamageProperties; иначе stat/level/formula и первый attackOptions. applyRangedMeleeBonus не читается; merge effects остаётся прежней issue-00069, повторный числовой бой не выполнялся. |
| Использование → временные HP | hasCustomEffect → выбор цели по applyOnTarget → target.stat.max×multiplier → профессиональный rollOver → capped formula и duration → отдельный ActiveEffect → owner.query. Это не вызов эффектов Item по applySelf. |
| Временные HP → общая модель/расход | Payload name/value соответствует TemporaryEffects. Производитель имеет один change; прежняя issue-00023 относится к расходу всех changes выбранного эффекта. Полный pipeline клиента в этой порции не исполнялся. |
| Порог → выбор → бросок | TypedObjectField thresholds → ID/name/value таблицы → Object.entries/одно значение либо prompt → threshold/thresholdDesc для doProfessionSkillRoll. Пустой список и неверный ID не защищены. |
| Текст → enriched → редактор | 11 createEnrichedText → Item.formInput корректно; Actor.enrichedText.profession приготовлен, но тот же tab-profession.editor использует raw. Сохранение редактора не проверено. |
| Шаблоны → helpers/локализация/CSS | Два partial предзагружены, skillPathPart является PARTS; has использует Set.has.157 ключей проверены. CSS-селекторы profession/card/input/editor связаны с разметкой, визуальное отображение не проверялось. |

### Проблемы и пределы выводов

Добавлены 11 отдельных [potential issues](../../issues/README.md): issue-00110 — адресация одноимённых навыков;00111 — удаление воздействия;00112 — отсутствие настроек definingSkill;00113 — applySelf не участвует в выборе цели;00114 — разбор duration;00115 — пустой порог;00116 — неизвестный professionSkills при Drop;00117 — кавычка в JSON HP;00118 — бросок пустого stat;00119 — три русские подписи;00120 — завершение 6 CRUD до записи.

Дополнены 9 прежних карточек: issue-00016/00023/00034/00060/00066/00069/00071/00072/00109. Для последних HTML-потребителей issue-00109 расширена на профессию в том же шаблоне, без дубля. Прежние сценарии, которые не выполнялись повторно, явно отделены от новых проверок связей.

Пустые названия вкладок, фиксированные 3 пути и 10 навыков, отсутствие min/max уровней, наличие полей схемы без представления в этом partial и выбор первого защитного навыка описаны как факты. Игровая необходимость их изменения не установлена. Не спроектированы новые правила или профессии; найденные проблемы не подтверждены пользователем и не исправлены.

### Структурная проверка и сохранность

Python через stdin сопоставил Git, фактическое дерево, реестр и Markdown. Результаты:

| Проверка | Результат |
| --- | --- |
| Реестр и карточки | 621 уникальный исходник; 158 карточек «Проверено», 463 строки «Не начат» |
| Новая порция | Ровно 12 файлов TASK-0003.019, 781 логическая строка; 11 обязательных разделов, определения полей/методов и версия присутствуют |
| Импорты | 240 прямых относительных импортов всех описанных JS разрешены и представлены в карточках; 13 относятся к новой порции |
| Markdown | 330 документов, 6816 локальных ссылок; цели/якоря существуют, таблицы согласованы, завершающих пробелов нет |
| Задачи | .001–.019 done; .020 planned, её 10 файлов ещё «Не начат»; TASK-0003 in-progress |
| Проблемы | 120 последовательных ID, все в potential; 11 новых карточек имеют обязательные разделы и текущий коммит |
| Состав изменений | 61 документ: 12 новых и 18 уточнённых карточек файлов, 11 новых и 9 дополненных issues, 11 указателей/задач/журналов |
| Исходники | Все 621 файл побайтно совпадают с HEAD и TASK-0001; SHA256 сводного снимка 9de49bf9b75194490fcfd7bfc80e2b1c8bcd9d90dd26f3603faf21d92b3d0e1e |
| Метаданные доступа | Для 985 отслеживаемых файлов сохранены mode, uid, gid и inode; SHA256 снимка b20166e770b42b9bd0ee330d4a9af608b4978c8d19387e6f33906a1e0c18b9f8 |
| История и diff | Журнал начиная с TASK-0003.018 сохранён побайтно; git diff --check прошёл; HEAD/ветка не менялись |

Хеш всего журнала на старте: 28548b1ae99abbd93f49e8a29b7f9c78f948b4d9a2e577bc6ce02d22e84ffff4. Строки текущих итогов и затронутые указатели прочитаны после обновления; исторические результаты прежних порций сохранены. Структурные проверки дополняют содержательную сверку выше и не доказывают работу системы в клиенте.

### Результат и ограничения

[TASK-0003.019](../../tasks/task-0003.019.md) завершена в согласованном объёме: **158 из 621 файла** проверены, **463** не разобраны. Во второй серии разобраны **86 из 96**, в очереди 10 файлов [TASK-0003.020](../../tasks/task-0003.020.md) (planned);453 требуют дальнейшей детализации.

Изменена только документация. Исходники, права/владельцы/группы существующих файлов, миры, сервис и БД сохранены; браузер и клиентский игровой процесс не запускались. Коммит не создавался.

## TASK-0003.018

Дата: 2026-09-10. Ветка rusbar-main, HEAD `29319a7a7e1dfc0663edbc15166f3b6a19682a2f`; рабочее дерево на старте чистое, отслеживаются 976 файлов. Все 621 исходник совпадают со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. Foundry 14.367.0 по /opt/foundryvtt/package.json, Node 24.16.0.

### Полный охват порции

| Файл | Логических строк |
| --- | --- |
| [module/data/item/raceData.js](../../../module/data/item/raceData.js) | 31 |
| [module/data/item/homelandData.js](../../../module/data/item/homelandData.js) | 14 |
| [module/data/item/templates/perkData.js](../../../module/data/item/templates/perkData.js) | 8 |
| [module/data/item/templates/socialStandingData.js](../../../module/data/item/templates/socialStandingData.js) | 11 |
| [module/item/sheets/WitcherRaceSheet.js](../../../module/item/sheets/WitcherRaceSheet.js) | 15 |
| [module/item/sheets/WitcherHomelandSheet.js](../../../module/item/sheets/WitcherHomelandSheet.js) | 15 |
| [templates/sheets/item/race-sheet.hbs](../../../templates/sheets/item/race-sheet.hbs) | 84 |
| [templates/sheets/item/homeland-sheet.hbs](../../../templates/sheets/item/homeland-sheet.hbs) | 16 |

Всего **8 файлов, 194 логические строки**. Описаны обе модели, две фабрики вложенных полей, два класса листов и оба шаблона целиком. Сверены все 6 прямых относительных импортов, регистрация, контекст, именованные поля, методы и внешние потребители. Подготовлены 8 новых карточек; уточнены 14 связанных: system.json, registerDataModels, registerSheets, config, CommonItemData, dataUtils, WitcherItemSheet, WitcherConfigurationSheet, WitcherItem, WitcherActor, generalData, фабрика родины Actor, WitcherActiveEffect и общий шаблон конфигурации general.

Лист персонажа, его itemMixin, skillMixin, header/tab-background/tab-profession, внешние классы Foundry и CSS прочитаны для проверки конкретных связей. Их чтение не заявлено полным пофайловым разбором. При проверке верхнеуровневого type в 226 JSON-файлах packsJson не обнаружены race/homeland Item; это просмотр метаданных типов, без анализа содержимого всех компедиумов. Базы packs и миров не открывались.

### Методика и подмены

Диагностический JavaScript передан Node через stdin, без создания файлов стенда. Использованы настоящие DataModel/TypeDataModel/поля/common BaseItem Foundry и системные модели, подключённые registerDataModels. Настоящий WitcherItem выполнен поверх common BaseItem, не client Item. Проверены экземпляры race/homeland, фабрики полей, enrichedText и dataUtils; TextEditor.enrichHTML заменён функцией, возвращающей отличимый HTML-маркер. Источник документов до и после сравнен через toObject; обогащение не записывало данные.

Настоящие ItemSheetV2, HandlebarsApplicationMixin и DragDrop загружены поверх фасада DocumentSheetV2; классы WitcherItemSheet, обоих специализированных листов и WitcherConfigurationSheet настоящие. Общий lifecycle Application, слияние всех опций, события браузера и сохранение формы не исполнялись. Вызовы render, update и createEmbeddedDocuments перехватывались; ни одного документа БД не создано.

Handlebars 4.7.9 и parse5 настоящие. Вызваны исходные formGroup, HTMLField.toFormGroup/toInput, selectOptions и prepareSelectOptionGroups; ProseMirror.create и окончательные DOM-обёртки заменены регистраторами. Для Actor-описаний отдельно исполнены настоящие editor и createEditorInput с минимальным document.createElement и пустым CONFIG.TextEditor.engines, как в стандартном config ядра. Helper eq представлен эквивалентным a===b; его источник установлен в /opt/foundryvtt/client/applications/handlebars.mjs:140. localize читает настоящие en/ru после expandObject. Отсутствие явно selected option не объявлено проверкой автоматического выбора браузером.

Настоящие тела WitcherCharacterSheet._prepareCharacterData и WitcherActor.getList исполнены на фасадах контекста/коллекции; расчёт totals/statTotal заменён нулевыми заглушками. Вызваны настоящие itemMixin._onDropItem/_onItemInlineEdit и skillMixin.addSocialStanding. Операции Actor удаления/добавления и запись Item представлены журналом вызовов; прежняя гонка удаления не воспроизводилась заново.

Для эффектов исполнены настоящий generator core Actor.allApplicableEffects на фасаде коллекций и getter WitcherActiveEffect.isSuppressed на фасадах родителей. Числовой pipeline applyActiveEffects, active/shouldApplyChange и сохранение созданного эффекта не запускались; соответствующие исходники ядра прочитаны для определения границы.

### Выполненные сценарии

| Группа | Фактический результат |
| --- | --- |
| 1. Схемы и регистрация | RaceData: 13 верхнеуровневых полей, description HTMLField вместо StringField базы; HomelandData: 2 StringField, metadata.type=homeland и Object.isFrozen=true. Обе модели/листа согласованы с system.json. |
| 2. Вложенные фабрики | Четыре независимые пары name/description; пять регионов north/nilfgaard/skellige/dolBlathanna/mahakam. Начальные строки пусты, общие значения Race соответствуют CommonItemData. |
| 3. Обогащение | Четыре последовательных вызова: UUID-текст и 3 пустых описания. Получены свои value/enriched/systemField с system.perkN.description; общего description в результате нет, source не изменён. |
| 4. Значения модели | customStanding/customPlace приняты без choices. otherValue сохраняется при другом value. Лишняя quantity родины отсутствует в подготовленных данных и toObject. |
| 5. Форма расы | 15 именованных элементов, 4 HTML-входа передали верные value/enriched/path; socialStanding.north=hated/nilfgaard=equal явно selected. Общего description нет. configureItem/editImage присутствуют. |
| 6. Форма родины | Для other два именованных поля; для пустого/nilfgaard/customPlace одно. Всегда 26 вариантов. Явное selected только у other/nilfgaard; showConfig включает действие конфигурации. |
| 7. Конфигурация и создание AE | Оба configureItem открыли render-фасад. General даёт 0 именованных полей; 4 категории эффектов доступны. Passive-create передал 2 запроса с type=base/name/icon/origin/duration/disabled; явных transfer/changes в запросах нет. |
| 8. Контекст Actor и заголовок | Первый race/homeland Item выбран, enrichedText.race содержит 4 результата. Item-родина other/AuditPlace показана при неизменном Actor.homeland=aedirn; без Item показано значение Actor. general.race не переписана. |
| 9. Описания на Actor | Все четыре editor получили исходный race.system.perkN.description. HTML-маркер отсутствует, @UUID осталась в результате. Контрольная Item-форма передавала enriched правильно: issue-00109. |
| 10. Социальные модификаторы | addSocialStanding читает Actor.general.socialStanding. Для tolerated/hated/feared/toleratedFeared/hatedFeared charisma дала -1/-2/-1/-1-1/-2-1; leadership -1/-2/пусто/-1/-2; intimidation пусто/пусто/+1/+1/+1. Пусто/equal не добавляют строк. |
| 11. Inline-редактирование | Изменение региона north передало Item.update({'system.socialStanding.north':'feared'}); Actor.general.socialStanding осталась equal. |
| 12. Drop | Настоящие _onDropItem с race и homeland вызвали последовательно remove(type), add(item) на фасаде. Это проверка маршрута, не завершения настоящего удаления. |
| 13. Выбор Item и эффекты | getList исключил stored race и вернул Empty Race. Core generator собрал Actor/race/homeland effects с transfer; transfer=false исключён. isSuppressed для обоих типов false, при applySelf=true — true. |
| 14. Локализация | 26 значений homelands, 6 socialStanding и 7 буквальных ключей: 39 ключей найдены в en и ru, отсутствующих нет. |

Все 14 групп завершены. Первоначальные ошибки диагностического окружения (неопределённый global Actor и невалидный ID входного документа) исправлены в коде проверки; итоговый прогон прошёл. Это ошибки стенда в памяти, не новые проблемы системы. Предупреждение Node о типе модуля не устранялось изменением package.json.

### Перекрёстная сверка связей

| Цепочка | Сопоставление |
| --- | --- |
| Тип → схема → лист | system.json → registerDataModels/registerSheets → RaceData/HomelandData → общий WitcherItemSheet. Объявления race/homeland полны; Home не наследует CommonItemData. |
| Особенность → HTML → показ | perk() → RaceData.enrichedText → createEnrichedText → ItemSheet.enrichedText → четыре formGroup. Другой consumer CharacterSheet готовит enrichedText.race, но tab-profession.editor берёт исходный description. |
| Регионы → выбор → бросок | socialStanding() определяет 5 строк, config — 6 UI-вариантов. Race-форма/inline меняют Item. Биография отдельно выбирает general.socialStanding; skillMixin читает это значение, не таблицу расы. |
| Родина → представление | Item.value/otherValue и Actor.general.homeland — разные схемы. getList('homeland')[0] переключает ветку показа; копирования в Actor не найдено. other определяет наличие текстового поля. |
| Drop → хранение → выбор | uniqueTypes на листах → itemMixin._onDropItem → removeItemsOfType/addItem. getList сортирует по sort и исключает isStored; CharacterSheet берёт первый. Прежняя async-граница отражена в issue-00034. |
| Конфигурация → ActiveEffect → Actor | Общие WitcherConfigurationSheet/ActiveEffect CRUD доступны обоим типам. Сбор transfer-эффектов выполняет core Actor, подавление — WitcherActiveEffect/ядро. Тексты perk сами effects/changes не создают. |
| Поля → словари → локализация | Все именованные поля согласованы со схемами; варианты существуют в config и en/ru. choices в строковых моделях отсутствуют. Регистр dolBlathanna таблицы расы отличается от dolblathanna родины; автоматического соответствия не найдено. |
| Шаблоны → стиль/ресурсы | PARTS.main ведёт к прочитанным HBS. .perk/.editor-content и классы родины сопоставлены с CSS только как селекторы; работу визуального редактора и загрузку изображений проверка не подтверждает. |

### Проблемы и границы вывода

Зарегистрирована одна новая [issue-00109](../../issues/potential/issue-00109.md) в potential: лист персонажа не использует приготовленный HTML расовых особенностей. Исполненный стандартный editor-helper не обогащает его сам; реальные UUID не разрешались. Сохранение target=race.system.perkN.description отдельно не проверялось и не объявлено сломанным.

Дополнены [issue-00005](../../issues/potential/issue-00005.md) (оба типа согласованы), [issue-00013](../../issues/potential/issue-00013.md) (другой consumer HTML) и [issue-00034](../../issues/potential/issue-00034.md) (уточнён Drop расы/родины). Унаследованные ограничения листа из issue-00058/00059 обозначены в карточках без нового воспроизведения или дублей.

Фиксированные четыре perk, отсутствие общего description в рассмотренной форме, произвольные значения без choices и отсутствие автопереноса социального положения записаны как фактические границы, без навязывания новой механики. Игровые правила и числовые расовые бонусы не проектировались. Потенциальные проблемы не подтверждены пользователем и не исправлены.

### Структурная проверка и сохранность

Проверка Python через stdin сопоставила Git, фактическое дерево, реестр и документы:

| Проверка | Результат |
| --- | --- |
| Состав и статусы реестра | 621 уникальный исходник; 146 карточек со статусом «Проверено», 475 строк «Не начат» |
| Новая порция | Ровно 8 файлов из TASK-0003.018, 194 логические строки; все 11 разделов карточки, поля/методы и версия присутствуют |
| Связи | 227 прямых относительных импортов всех описанных JS разрешены в существующие файлы и представлены в карточках; 6 относятся к новой порции |
| Markdown | 307 документов, 6459 локальных ссылок; цели и якоря существуют, таблицы согласованы, нет завершающих пробелов |
| Задачи | .001–.018 done, .019–.020 planned; в очереди 22 различных файла, все ещё «Не начат»; TASK-0003 in-progress |
| Проблемы | 109 последовательных ID, все в potential; issue-00109 имеет обязательные разделы и текущую версию |
| Сохранность исходников | Все 621 файл побайтно совпадают и с HEAD, и со срезом TASK-0001; сводный SHA256 9de49bf9b75194490fcfd7bfc80e2b1c8bcd9d90dd26f3603faf21d92b3d0e1e |
| Доступ существующих файлов | Для 976 отслеживаемых файлов сохранены mode, uid, gid и inode; SHA256 снимка edfd1bbcddee92a21f6c26b6d6bdfdac0fc5efc9aa03c9c2eed35c6460dc9c72 |
| Состав изменений | 37 документов: 8 новых карточек, 14 уточнённых, 1 новая issue, 3 дополненных issue и 11 указателей/задач/журналов; git diff --check прошёл |

Исходная часть журнала начиная с TASK-0003.017 сохранена без изменений; хеш всего журнала на старте 733281e292433688e9b723313ca85c83bf46ca01a72f3a7ea55e2b34f6ecbf49. Указатели, текущие итоги и восемь строк реестра дополнительно прочитаны после обновления; исторические результаты порций сохранены. Эти структурные проверки дополняют содержательное сопоставление выше, не заменяют его.

### Результат и ограничения

[TASK-0003.018](../../tasks/task-0003.018.md) завершена в согласованном объёме. Покрытие — **146 из 621 файла**, не разобраны **475**. Во второй серии разобраны **74 из 96**, в очереди **22**; следующие [TASK-0003.019](../../tasks/task-0003.019.md) и [TASK-0003.020](../../tasks/task-0003.020.md) остаются planned. Остальные 453 файла требуют дальнейшей детализации.

Изменена только документация. Мир, браузер, сервис, БД, реальные клиентские документы/UUID, сохранение форм и эффекты в игре не запускались. Права/владельцы/группы/содержимое исходников сохранены; код не исправлялся, коммит не создавался.

## TASK-0003.017

Дата: 2026-09-10. Ветка rusbar-main, HEAD `c7cd9d71dcb1714cdccb175aee351a3f1df95c5b`; рабочее дерево на старте чистое, отслеживаются 964 файла. Все 621 исходник совпадают со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. Foundry 14.367.0 по /opt/foundryvtt/package.json, Node 24.16.0.

### Полный охват порции

| Файл | Логических строк |
| --- | --- |
| [module/item/systems/repair.js](../../../module/item/systems/repair.js) | 347 |
| [module/item/mixins/repairMixin.js](../../../module/item/mixins/repairMixin.js) | 12 |
| [module/item/mixins/costEditMixin.js](../../../module/item/mixins/costEditMixin.js) | 20 |
| [templates/dialog/repair-dialog.hbs](../../../templates/dialog/repair-dialog.hbs) | 33 |
| [templates/chat/item/repair.hbs](../../../templates/chat/item/repair.hbs) | 73 |

Всего **5 файлов, 485 логических строк**. Полностью описаны Repair (15 собственных методов), RepairData (конструктор/8 полей/7 getters), 2 метода repairMixin, 2 метода costEditMixin и оба HBS. Сверены все 5 прямых относительных импортов, регистрации, шаблоны, вызовы и поля контекста. Подготовлены 5 новых карточек и уточнены 12 связанных: WitcherItem, WitcherActor, modifierMixin, WeaponData, ArmorData, DiagramData, settings, handlebars, socketHook, queries, TheWitcherTRPG, components-list.

Чат, helper выбора Actor, поиск/списание ресурсов, extendedRoll, RollConfig, socketMessage и границы CSS прочитаны для проверки связей. Их полный пофайловый разбор не заявлен, статус реестра от такого чтения не повышен.

### Методика и подмены

Диагностический JavaScript передан Node через stdin, без создания файлов тестового стенда. Импортированы настоящий RepairSystem, обе примеси, extendedRoll/RollConfig, sender/receiver сокета, chatMessageListeners и их прямые зависимости. Использованы DataModel/TypeDataModel/fields/common BaseItem Foundry и реальные модели Component/Diagram/Weapon/Armor. Это документы и модели в памяти, не client WitcherItem и не документы игрового мира.

Actor, инвентарь, canvas, UUID, права, DOM, DialogV2.wait, ChatMessage и запись update/removeItem представлены фасадами. Изменения сохранялись только в журнале вызовов и возвращали контролируемые pending Promise; в конце все они разрешены. DialogV2.wait фиксировал конфигурацию, вызывал render callback и возвращал null: исследовались состав/отмена и callbacks по исходнику, не браузерные окна. Core wait:405–425 в /opt/foundryvtt/client/applications/api/dialog.mjs отдельно подтверждает null при закрытии без rejectClose.

Для настройки выполнены настоящие registerSettings и ClientSettings из /opt/foundryvtt/client/helpers/client-settings.mjs; world/client storage и Setting-документ заменены. После доказательства незарегистрированного ключа get временно подменён только для исследования дальнейших ветвей. Две формулы с подписями/без проверены настоящими RollParser и grammar.pegjs, скомпилированной Peggy в памяти. Roll для extendedRoll был фасадом с заданным total и некритическим результатом d10=5; реальные случайные броски/crit/fumble не запускались.

Handlebars 4.7.9 и parse5 настоящие; использованы оба HBS и исходный components-list. localize читает настоящие en/ru после utils.expandObject; and/eq представлены простыми эквивалентными helpers для этих проверок. Socket.IO заменён перехватом сообщения и прямым вызовом зарегистрированного callback активного GM, без сети.

### Выполненные сценарии

| Группа | Фактический результат |
| --- | --- |
| 1. Рецепт/исполнитель | Пустой/неразрешённый рецепт дал уведомление noDiagram и undefined. Owned Leather quantity='0'/isStored=true; отсутствующий Steel разрешён по UUID; Unknown без UUID попал в unknown. Artisan использует свой инвентарь. |
| 2. Вычисления | craftingDC20 и enhancementItemIds[a,'',a] дали enchantsCount2, enchantsDC4, repairDC19; cost3+5+additional4 дали 12. Конструктор содержит 8 полей и не содержит damagedLocations. |
| 3. Диалог/отмена | Четыре сочетания GM/artisan: собственный ремонт всегда repair/sim-repair/request-repair; artisan без GM repair/sim-repair; artisan с GM добавляет gm-repair. modal=true; отмена-фасад не вызвала записей. В HTML только строка DC, без повреждений. |
| 4. Guard обычного ремонта | На подготовленном data без missing/unknown получен TypeError чтения damagedLocations.length. Missing/unknown отклоняются раньше. В отдельном опыте вручную добавленный [] дал alreadyRepaired; [{}] с owned0 допустил вызов commonRepair-регистратора. |
| 5. Нижнее восстановление | Прямой _doRepair(true) при праве update вызвал removeItem и затем TypeError getRestoreReliabilityData is not a function. Метод отсутствует в системе. Это не доказательство достижения этой точки штатной кнопкой. |
| 6. Настройки | Настоящий registerSettings создал 9 ключей; displayRollsDetails прочитан как false. prepareRollFormula с реальным ClientSettings дал Error неизвестной TheWitcherTRPG.woundsAffectSkillBase. |
| 7. Строка броска | С временным get=false обе формы 1d10+6+5+2[bonus] с подписями/без прошли реальный парсер. С true добавлена только открывающая скобка, обе формы дали SyntaxError; исходный addActiveEffects скобку не закрывает. |
| 8. Симуляция/порог | Настоящие commonRepair/extendedRoll, total18/19/20 против DC19: success=false/false/true. Каждый сценарий создал только Roll.toMessage, не списывал и не восстанавливал; сообщение оставалось pending после возврата. |
| 9. GM/модели/примесь | gmRepair: ChatMessage.create→WeaponData.repair→update reliable10, без remove/броска. Возврат при pending create/update. Прямые restoreReliability RepairSystem/repairMixin вызвали тот же метод. ArmorData передала reliability8 и 6 SP максимумов (head6/torso7/прочие 0). |
| 10. Неразрешённый материал | Реальный рецепт с валидным Item.unknowncomponent при fromUuid=null дал missing=[null]; prepareDialogTemplate упал на oc.img. |
| 11. Чат и списки | При owned/missing=[] и только unknown UNIQUE_UNKNOWN таблица/название/цена скрыты, кнопка запроса присутствует. Контроль со смешанным списком отобразил unknown и цену заказа. |
| 12. Пустая цена | Настоящий costEditMixin: поля 2/3, база 15→additional5,total20; одно пустое поле→NaN. Это дополнение issue-00100, не новый ID. |
| 13. Глобальный DOM | После подписки A с полем 2 добавлено поле B3 и подписка B. Change A вызвал оба callback с суммой 5; listeners[2,1], первый total20, второй остался 40. Два реальных модальных окна не открывались. |
| 14. Сокет | _doRepair(true) без права update передал type restoreReliability/data[uuid] на system.TheWitcherTRPG. Настоящий receiver активного GM сделал shift и вызвал Item.restoreReliability→weapon.update; запись осталась pending. Generic query не запускался. |
| 15. Кнопка/Item-вход | Настоящие chatMessageListeners/onRepairRequest с world-owner/item открыли processRequest для artisan. Пустая game.actors дала TypeError owner.items. Настоящий repairMixin.repair отдельно дождался отмены новой конфигурации диалога. |
| 16. Локализация | 18 буквальных ключей порции и 2 значения из statMap/skillMap найдены в en/ru (20 в каждом языке). Подписи формулы получены из настоящей CONFIG.WITCHER. |

Все 16 групп завершены. В первом диагностическом входе один UUID имел 15 символов и очищался моделью в null; сценарий исправлен на валидный 16-символьный ID и выполнен заново. Это ошибка входа проверки, не проблема системы. Предупреждение Node о module type не устранялось изменением package.json.

### Перекрёстная сверка связей

| Цепочка | Сопоставление |
| --- | --- |
| Инвентарь → Item → RepairSystem | canBeRepaired моделей управляет видимостью .item-repair; CharacterSheet._repairItem442–446 вызывает item.repair; примесь передаёт actor/item. UI-видимость не добавляет проверок в прямые методы. |
| Рецепт/Actor → требования | craftingComponents(name/uuid)→findNeededComponent(name)[0] либо fromUuid; quantity требования игнорируется, required всегда 1. quantity0 отображён как нехватка, guard это не учитывает. |
| RepairData → HBS → обычный ремонт | Ни конструктор/7 getters, ни примесь не задают damagedLocations. HBS просто пропускает each, guard бросает. getRestoreReliabilityData нигде не определён; модели имеют отдельный system.repair. |
| Настройка → формула → extendedRoll | Регистрация не содержит старого ключа. modifierMixin добавляет слагаемые; CONFIG связывает CRA/crafting. prepareRollConfig выставляет DC/флаги, extendedRoll считает успех по > при defense=false; commonRepair также использует >. |
| Диалог → цена → чат | components-list даёт поля/базу, глобальный costEditMixin возвращает сумму, render присваивает additionalCost; repairPrice прибавляет owned/missing. Платежей/изменений валюты в пяти файлах нет. |
| Сообщение → исполнитель → предмет | RepairSystem создаёт content либо flavor; HBS хранит owner/item ID; hook→chat listener→getInteractActor→processRequest. Чтение owner.items предшествует guard; неизвестные-only материалы выключены верхним showComponents. |
| Списание/восстановление → завершение | Actor.removeItem ждёт delete/update, но _doRepair не ждёт его. Модельные repair не ждут parent.update; примесь/GM/socket обёртки не восстанавливают ожидание. Сообщения также запускаются без ожидания записи. |
| Socket и query | _doRepair использует emitForGM, активный GM разрешает UUID и вызывает документный метод. queries.js отдельно разрешает restoreReliability; подтверждение true от query и отсутствие прикладного ответа сокета — разные контракты. |

Все описания нового блока сверены с текущими определениями и 12 обновлёнными карточками. Прямой фрагмент определения не считается полным анализом файла. Поиск потребителей охватывает module/ и templates/; внешние модули не исследованы.

### Issues и ограничения

Зарегистрированы [issue-00102](../../issues/potential/issue-00102.md), [issue-00103](../../issues/potential/issue-00103.md), [issue-00104](../../issues/potential/issue-00104.md), [issue-00105](../../issues/potential/issue-00105.md), [issue-00106](../../issues/potential/issue-00106.md), [issue-00107](../../issues/potential/issue-00107.md), [issue-00108](../../issues/potential/issue-00108.md). Дополнены issue-00008/00010/00081/00100; issue-00034 сопоставлена без нового воспроизведения её собственных ветвей. Всего **108 issue, все potential**. Воспроизведение агентом не заменяет подтверждения пользователя; исправления не выполнялись.

Ремонт не объявлен работающим по итогам изолированных ветвей: штатный путь содержит issue-00102/00103. Ветвь zero-quantity проверена с вручную добавленным damagedLocations; симуляция — после подмены отсутствующей настройки; _doRepair — отдельным вызовом. Эти условия явно записаны в карточках. Для issue-00106 установлена глобальная область DOM, но достижимость нескольких modal окон в обычном UI не проверялась.

Не запускались мир, реальный браузер/клиент, сеть, БД, кошелёк, полные случайные броски, конкурирующие изменения и права сервера. Synthetic Actor/удаление Actor в мире, реальный compendium resolver и полный жизненный цикл диалогов не проверены. Соответствие количества материалов/DC рулбуку не исследовалось и игровые правила не менялись.

### Контроль документов и исходников

Проверки прошли: 621 уникальный исходник в реестре, 138 строк «Проверено» соответствуют 138 карточкам, 483 остаются «Не начат». Все 5 новых карточек содержат обязательные разделы, собственные методы/поля, дату и коммит; перечень совпадает с задачей. Проверены 221 прямой относительный импорт всех описанных JS-файлов и 6269 локальных ссылок/якорей в 298 Markdown-документах. Все 108 issue находятся в potential, ID последовательны и представлены в реестре.

Все 621 исходник побайтно совпали с текущим HEAD и срезом TASK-0001. Сумма SHA256 по путям/байтам осталась `9de49bf9b75194490fcfd7bfc80e2b1c8bcd9d90dd26f3603faf21d92b3d0e1e`. У 964 отслеживаемых до порции файлов сохранены mode/uid/gid/inode; итоговая проверка метаданных совпала со стартовой. `git diff --check`, структура таблиц и согласованность указателей прошли. Изменены 39 документов (27 существующих и 12 новых); вне docs изменений нет. Предыдущие записи журнала, начиная с TASK-0003.016, сохранены побайтно. Коммит не создавался.

Следующая порция — [TASK-0003.018](../../tasks/task-0003.018.md): раса и родина. Во второй серии проверены 66 из 96 файлов, в трёх следующих задачах остаются 30; ещё 453 требуют детализации. TASK-0004/0005 остаются заготовками.

## TASK-0003.016

Дата: 2026-09-10. Ветка rusbar-main, HEAD `53f74994011383cb544cabac96285430f00cb38a`; рабочее дерево на старте чистое, отслеживаются 944 файла. Все 621 исходник совпадают со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. Foundry 14.367.0 по /opt/foundryvtt/package.json, Node 24.16.0.

### Полный охват порции

| Файл | Логических строк |
| --- | --- |
| [module/data/item/componentData.js](../../../module/data/item/componentData.js) | 21 |
| [module/data/item/diagramData.js](../../../module/data/item/diagramData.js) | 81 |
| [module/data/item/templates/craftingComponentData.js](../../../module/data/item/templates/craftingComponentData.js) | 10 |
| [module/data/item/templates/associatedDiagramData.js](../../../module/data/item/templates/associatedDiagramData.js) | 14 |
| [module/item/sheets/WitcherComponentSheet.js](../../../module/item/sheets/WitcherComponentSheet.js) | 15 |
| [module/item/sheets/WitcherDiagramSheet.js](../../../module/item/sheets/WitcherDiagramSheet.js) | 111 |
| [module/item/sheets/mixins/associatedDiagramMixin.js](../../../module/item/sheets/mixins/associatedDiagramMixin.js) | 21 |
| [templates/sheets/item/component-sheet.hbs](../../../templates/sheets/item/component-sheet.hbs) | 51 |
| [templates/sheets/item/diagrams-sheet.hbs](../../../templates/sheets/item/diagrams-sheet.hbs) | 136 |
| [templates/partials/components-list.hbs](../../../templates/partials/components-list.hbs) | 43 |
| [templates/partials/associated-diagram.hbs](../../../templates/partials/associated-diagram.hbs) | 38 |
| [templates/partials/associated-item.hbs](../../../templates/partials/associated-item.hbs) | 43 |

Всего **12 файлов, 584 логические строки**; подготовлены 12 карточек. Все собственные методы, фабрики, поля и пять HBS прочитаны целиком. Сверены 5 прямых относительных импортов порции, пути partial/PARTS и обработчики. Уточнены 13 связанных карточек: CommonItemData, WitcherItem, WitcherActor, WeaponData, ArmorData, их листы, WitcherItemSheet, registerDataModels, registerSheets, config, handlebars, item-header.

Изготовление, алхимия, поиск инвентаря, разборка, ремонт и обработчик цены просмотрены как потребители. Их частичное или полное чтение для проверки связи не увеличивает покрытие реестра. Следующая TASK-0003.017 по-прежнему включает полный разбор ремонта/costEditMixin.

### Методика и подмены

Один диагностический сценарий передан Node через stdin, без создания тестовых файлов. Использованы настоящие DataModel/TypeDataModel/DataFields/DocumentUUIDField и primitives Foundry; все модели системы подключены по registerDataModels. Для связанного материала создан настоящий common BaseItem с моделью ComponentData; документ мира и client WitcherItem не создавались. Это позволило проверить реальный enumerable spread: id документа не затёр id строки, name/img/system доступны.

Исполнены настоящие модели, классы листов, associatedDiagramMixin/associatedDiagramData, craftingMixin и _calculateAdditionalCost. isAlchemicalCraft извлечён из исходника без изменения тела. Core ItemSheetV2/HandlebarsApplicationMixin и подготовка контекста работают с DocumentSheet/DOM-фасадом. UUID API заменён картой с BaseItem/null; Item.update не записывает данные и возвращает pending Promise. Очистка сформированных payload выполняется новой настоящей DiagramData.

Handlebars и parse5 настоящие. Общий header и пять HBS использованы из исходников. editor представлен простым фасадом с target/content; selectOptions — ограниченный генератор. Системные getSetting/window/includes/has используются из исходного setup. Сначала component-sheet выполнен без select и дал Missing helper. Затем только для изучения остальных блоков временно зарегистрирован helper, возвращающий тело select без выбора options; после проверки он удалён из диагностического Handlebars. Успешность штатного рендера этим не утверждается.

fromUuid/fromUuidSync сверены с /opt/foundryvtt/client/utils/helpers.mjs:161–210: синхронная версия может вернуть индекс и бросает на embedded Compendium при strict=true. Эти ветви ядра не запускались с реальным pack. Локализация en/ru проверена после настоящего utils.expandObject, как в загрузчике /opt/foundryvtt/client/helpers/localization.mjs; localize не обрезает пробел ключа.

### Выполненные сценарии

| Группа | Фактический результат |
| --- | --- |
| 1. Схемы и ID | ComponentData имеет 14 верхних полей, DiagramData — 20. craftingComponent содержит id/name/quantity/uuid. Новые строки получают разные 16-символьные ID, uuid по умолчанию null. |
| 2. Обогащение | Для доступного Item имя обновилось в prepared-массиве, добавлены img/type; toObject() сохранил исходное имя, toObject(false) не сериализует внесхемные img/type. Недоступный/пустой UUID сохранил запись. undefined→undefined, []→[], quantity0 осталось0. |
| 3. Контекст листа | Из трёх записей две known по наличию UUID и одна unknown. У доступного BaseItem ID строки сохранён; у недоступного UUID остались только id/quantity, сохранённое имя потерялось. |
| 4. CRUD и повторный drop | Edit quantity '4' очистился в4; remove row1 сохранил row2; add quantity='' очистился в null и получил ID. Два drop одного UUID дали две строки с разными ID. |
| 5. Drop результата | Область associatedItem записала associatedItemUuid; другая область добавила компонент. Нулевой offsetParent дал TypeError до update. Удаление результата записало пустой UUID. |
| 6. Обратная ссылка | Примесь пропустила пустой item/чужую область, отклонила неправильный Item.type/категорию, приняла weapon; null offsetParent дал TypeError. Удаление записало ''. unwrap с пустой строкой не менял прежнее свойство, с доступным UUID присвоил объект, с недоступным — null. |
| 7. Слушатели | Настоящий базовый _onRender вызвал activateListeners DiagramSheet: click/blur/click/click для add/edit/remove/remove-result. |
| 8. Форма компонента | Без select — Missing helper. С временной подменой пять категорий дали 10/10/10/10/11 именованных полей; substances добавляет substanceType. Выбранный option подменой не проверен. |
| 9. Форма рецепта | Со связанным результатом режимы isFormulae=false/true дали 12/20 именованных полей, editor.description учитывается отдельно. Списки craftingComponents есть в обоих режимах. |
| 10. Связанные представления | С настоящим BaseItem имя/картинка присутствуют, system.description не выводится обоими partial из-за верхнего пути. resultQuantity видим только при имени результата. Подсказки add/remove рецепта переставлены. |
| 11. Миграция | Старый associatedItem заменил современный UUID жёстким Compendium.TheWitcherTRPG.gear.Item.ID. alchemyDC12/craftingDC20 стали12/12 даже при isFormulae=false; контроль без старых данных сохранил современное значение. |
| 12. Таблица и цена | showCost/canEditCost false/false,true/false,true/true дали 0/0/1 editable inputs при cost0/cost7; data-price15. Исходный costEditMixin с '2','3' дал additional5/total20; с пустым значением — NaN/NaN. |
| 13. Поиск компонентов | findNeededComponent нашёл точное имя даже isStored=true; актуальное другое имя не нашёл. getSubstance и локализованное имя vitriol нашли субстанцию, findComponentByUuid — compendiumSource. |
| 14. Режим изготовления | Настоящий isAlchemicalCraft: isFormulae=false/alchemyDC12→true, isFormulae=true/alchemyDC0→0. Выбор массивов/поиска realCraft установлен по исходнику, полный craft заново не запускался. |
| 15. Локализация | Проверены 49 буквальных ключей в en/ru. Не найдены только два ключа с начальным пробелом AddComponent/RemoveComponent; без пробела переводы существуют. Тексты противоположных подсказок рецепта проверены отдельно. |

Все группы завершены. Пустая числовая строка дала null, а не предполагавшийся 0: ожидание диагностического сценария исправлено по результату настоящей модели; ошибкой системы это не объявлено. Предупреждение Node о module type оставлено без изменения package.json.

### Перекрёстная сверка связей

| Цепочка | Сопоставление |
| --- | --- |
| Component Item → требование рецепта | ComponentData описывает Item; craftingComponent — отдельную строку id/name/quantity/uuid. ID нужен UI, UUID — обогащению/связанным документам; realCraft ищет по имени. |
| Модель рецепта → лист → update → модель | Enrich сохраняет fallback имени; последующий known-map теряет его. CRUD адресует сохранённые ID; тип quantity и initial id формируются при очистке payload, не вручную листом. |
| Результат → обратный рецепт | DiagramData.associatedItemUuid и Weapon/Armor.associatedDiagramUuid независимы. Изменение одной ссылки автоматически не создаёт другую. UI-drop ограничивает категорию обратного рецепта; resolver модели её не проверяет. |
| Prepared данные → описание | Оба partial получают документ/индекс, но читают description вне system. Дополнительная загрузка индекса — отдельная граница, не объяснение неудачи с полным BaseItem. |
| Рецепт → изготовление/разборка | realCraft использует положительные quantities, поиск имени и resultQuantity/UUID результата; dismantle разрешает UUID материалов и возвращает вычисленные количества. Полный сценарий разборки не запускался. |
| Рецепт → ремонт → components-list | Repair получает рецепт через await fromUuid, ищет имя, затем UUID недостающего материала; передаёт required=1, цены и итог в partial. HBS не рассчитывает эти значения. Обработчик цены проверен отдельно, весь ремонт остаётся следующей задачей. |
| Формула → фактический режим | isFormulae управляет UI, alchemyDC управляет isAlchemicalCraft. Миграция дополнительно переносит alchemyDC в craftingDC; эти два разрыва не объединены в одно исправление. |

Область поиска потребителей — module/ и templates/, регистрации проверены отдельно. Для исключённых изображений указана справочная зависимость; карточки assets не создавались.

### Issues и ограничения

Зарегистрированы [issue-00094](../../issues/potential/issue-00094.md), [issue-00095](../../issues/potential/issue-00095.md), [issue-00096](../../issues/potential/issue-00096.md), [issue-00097](../../issues/potential/issue-00097.md), [issue-00098](../../issues/potential/issue-00098.md), [issue-00099](../../issues/potential/issue-00099.md), [issue-00100](../../issues/potential/issue-00100.md), [issue-00101](../../issues/potential/issue-00101.md). Дополнены issue-00037/00038/00041/00080. Всего **101 issue, все potential**; пользователь не подтверждал их и не согласовывал исправления.

Старые проблемы изготовления не воспроизводились заново и не получили повторных ID. Новый разбор не меняет количество ресурсов, правила режима, миграции, права или систему. Не проверены браузерный submit, ProseMirror, серверная валидация документов, пакеты/сеть, реальные броски, полный процесс изготовления/ремонта/разборки, кошелёк и многопользовательские изменения. Ручной повтор resolver с пустым UUID не считается проверкой полного Foundry reset.

### Контроль документов и исходников

Проверки прошли: в реестре 621 уникальный исходник, 133 строки «Проверено» связаны с карточками, 488 остаются «Не начат». Все 12 новых карточек содержат обязательные разделы, методы/поля, дату и коммит; состав задачи совпадает с перечнем. Во второй серии разобран 61 файл, в четырёх следующих задачах остаются 35. Все 101 issue находятся в potential, нумерация последовательна.

Проверены 216 прямых относительных импортов во всех 133 карточках и 6028 локальных ссылок/якорей в 286 Markdown-документах. Изменены 48 документов: 28 существующих и 20 новых. Реестры, статусы и навигация согласованы; git diff --check завершился без ошибок.

Все 621 исходник побайтово совпали с HEAD и базовым срезом TASK-0001; фактическое дерево соответствует согласованным исключениям и реестру. Сохранены mode/uid/gid/inode всех 944 ранее отслеживаемых файлов. SHA256 исходников (путь + NUL + байты + NUL в порядке реестра) — `9de49bf9b75194490fcfd7bfc80e2b1c8bcd9d90dd26f3603faf21d92b3d0e1e`; SHA256 sorted JSON метаданных — `9782790e47267ff80ccad0e7499d81dafeff0dac4041ebdc93eee0e99891cbb3`. Историческая часть журнала с TASK-0003.015 сохранена дословно.

Покрытие — **133 из 621 файла**, остаются **488**. Во второй серии разобран **61 файл из 96**, в очереди .017–.020 находятся **35**, ещё **453** требуют детализации. Следующая задача — [TASK-0003.017 — Ремонт предметов: расчёт, диалог и сообщения](../../tasks/task-0003.017.md).

## TASK-0003.015

Дата: 2026-09-10. Ветка rusbar-main, HEAD `7edb814aa870da75c7ad7633536e899a8d07e205`; на старте рабочее дерево чистое, отслеживаются 926 файлов. Все 621 исходник совпадают со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. Foundry 14.367.0 по /opt/foundryvtt/package.json, Node 24.16.0.

### Полный охват порции

| Файл | Логических строк |
| --- | --- |
| [module/data/item/alchemicalData.js](../../../module/data/item/alchemicalData.js) | 27 |
| [module/data/item/mutagenData.js](../../../module/data/item/mutagenData.js) | 22 |
| [module/data/item/valuableData.js](../../../module/data/item/valuableData.js) | 25 |
| [module/data/item/templates/consumableData.js](../../../module/data/item/templates/consumableData.js) | 10 |
| [module/data/item/templates/consumePropertiesData.js](../../../module/data/item/templates/consumePropertiesData.js) | 15 |
| [module/item/sheets/WitcherAlchemicalSheet.js](../../../module/item/sheets/WitcherAlchemicalSheet.js) | 31 |
| [module/item/sheets/WitcherMutagenSheet.js](../../../module/item/sheets/WitcherMutagenSheet.js) | 27 |
| [module/item/sheets/WitcherValuableSheet.js](../../../module/item/sheets/WitcherValuableSheet.js) | 35 |
| [module/item/sheets/configurations/WitcherConsumableConfigurationSheet.js](../../../module/item/sheets/configurations/WitcherConsumableConfigurationSheet.js) | 79 |
| [module/item/mixins/consumeMixin.js](../../../module/item/mixins/consumeMixin.js) | 42 |
| [templates/sheets/item/alchemical-sheet.hbs](../../../templates/sheets/item/alchemical-sheet.hbs) | 36 |
| [templates/sheets/item/mutagen-sheet.hbs](../../../templates/sheets/item/mutagen-sheet.hbs) | 20 |
| [templates/sheets/item/valuable-sheet.hbs](../../../templates/sheets/item/valuable-sheet.hbs) | 31 |
| [templates/sheets/item/configuration/tabs/consumablePropertiesConfiguration.hbs](../../../templates/sheets/item/configuration/tabs/consumablePropertiesConfiguration.hbs) | 60 |
| [templates/chat/item/consume.hbs](../../../templates/chat/item/consume.hbs) | 22 |

Всего 15 файлов, 482 логические строки, 15 новых карточек. Проверены все собственные определения, методы, поля и шаблоны. Уточнены 14 связанных карточек: CommonItemData, itemEffectData, WitcherItem, WitcherActor, WitcherItemSheet, WitcherConfigurationSheet, item-header, general, effect-part, applyActiveEffect, registerDataModels, registerSheets, config, handlebars. Внешние healMixin и itemContextMenu прослежены в пределах вызываемых методов; полного статуса анализа этим файлам не присвоено.

### Метод и границы изолированного выполнения

Сценарий передан Node через stdin, без добавления тестовых файлов. Использованы настоящие common DataModel/TypeDataModel/DataFields, EffectModel, BaseActiveEffect и primitives Foundry; реальные модели системы зарегистрированы через registerDataModels. Настоящие классы листов/configuration и методы consumeMixin, calculateHealValue, applyActiveEffect helper; useItem/removeItem/applyStatus/removeStatus извлечены из WitcherActor без изменения тел.

Core ItemSheetV2/HandlebarsApplicationMixin и подготовка вкладок использованы с DocumentSheet/DOM-фасадом. Handlebars и parse5 настоящие, formGroup — оригинальная функция /opt/foundryvtt/client/applications/handlebars.mjs; toFormGroup фиксирует реальный путь/значение вместо создания widgets. selectOptions — ограниченный генератор по valueAttr/labelAttr, не полный тест core helper. Системные getSetting/window/includes/has исполнялись из исходного handlebars.js; стандартная настройка clickableImageItemTypes включает valuable/mutagen.

Actor представлен небольшим DataModel-контекстом, Item — фасадом с настоящей system-моделью. UUID-хранилище, коллекции, update/delete/toggleStatusEffect/createEmbeddedDocuments, GM query, ChatMessage и временные улучшения перехватываются. Обычный ActiveEffect действительно клонируется оригинальным кодом, но его запись не исполняется. Неоконченные Promise служат проверке ожидания операций, а не имитацией их успешного завершения.

Локализация: 33 уникальных буквальных ключа этой порции проверены в en/ru после настоящего utils.expandObject, как при загрузке /opt/foundryvtt/client/helpers/localization.mjs:368. Все определены; Short.Availability — ключ с точкой внутри JSON, поэтому прямой обход необработанного объекта не подходит. Это не новая проблема перевода.

### Выполненные сценарии

| Группа | Фактический результат |
| --- | --- |
| 1. Три модели | По 15 верхних полей; isConsumable=false; consumeProperties имеет doesHeal/heal/effects/removesEffects. Входные id/addsTempHp отброшены. Временные улучшения: true/false/true. |
| 2. Конфигурации листов | Alchemical/Valuable используют WitcherConsumableConfigurationSheet с 3 вкладками и 5 частями. Mutagen — обычную configuration с 2 вкладками и 4 частями. |
| 3. Основные формы | 14 вариантов: алхимия alchemical/potion/decoction/oil даёт 9/10/10/9 именованных полей, 3 цвета мутагена и 7 категорий valuable — по 10. Тип мутагена выбирается в header. |
| 4. Условия formGroup | isConsumable/doesHeal: false/false, true/false, true/true → 1/2/3 корректных группы; 0/1/1 ошибок отсутствующего addsTempHp. Остальная форма рендерится. |
| 5. Два массива и CRUD | HBS даёт data-id=''. edit name/effects и statusEffect/removesEffects бросает TypeError до update; remove оставляет массив; add добавляет {percentage:100} и меняет prepared-массив. |
| 6. Слушатели | _onRender подключает focusout к input[data-action=editEffect] и input к select[data-action=editEffect]. |
| 7. Текст on | После ручного добавления временного id в prepared-запись исходный _onEditEffect передал name=false. Это условная ветвь за проблемой ID, не штатно сохраняемый документ. |
| 8. Расчёт лечения | При HP8/10 входы '5','1','0','2.9','' дали 2,'1','0','2.9',''. Это результаты calculateHealValue; consume затем применяет parseInt. Невалидные HP-пayload и серверная валидация не проверены. |
| 9. Применение | HP8/10+5→запрос10; fire с percentage0 вызвал toggle, poison снят. Из 2 ActiveEffect перенесён один applySelf; флаги копии сброшены, duration.value3 сохранена. quantity2 и токсичность не изменились. |
| 10. Flag и прямой вызов | useItem(false) ничего не выполняет; прямой consume при false всё равно доходит до сообщения. |
| 11. Контекстное меню/количество | visible/guard учитывают isConsumable; true при quantity2 вызвал update quantity1, false не списывал. Настоящие методы menu и removeItem, запись перехвачена. |
| 12. Последняя единица/Promise | При задержанном calculateHealValue Actor.useItem удалил quantity1 из UUID-фасада, затем consume запросил HP-update, GM query и чат. Локального createEmbeddedDocuments не было. Все основные записи могут оставаться pending после завершения consume/useItem. |
| 13. Item без Actor | consume с doesHeal=false дал TypeError на applyStatus, с true — на calculateHealValue. Защиты от отсутствующего владельца нет. |
| 14. Чат | [] не даёт картинок; name-only, fire и unknown дают по одной. У fire корректный src, у двух других src=''. ChatMessage.create не ожидается. |

Все группы утверждений завершены. Неподходящие фасады Actor/DOM, первоначально неполный учёт header и нераскрытых ключей локализации исправлены в диагностическом сценарии; они не зарегистрированы как проблемы системы. Предупреждение Node о module type оставлено без изменения package.json.

### Дополнительная сверка TASK-0003.011–TASK-0003.015

Пять перечней сопоставлены: **49 разных файлов**, пересечений нет. Карточки и исходники повторно сопоставлены по определениям методов, объявленным DataFields, прямым импортам и буквальным путям HBS: **46 прямых относительных импортов** этой серии разрешены и отражены в карточках. Это включает новые 15; прежние 34 не объявляются повторно выполненными runtime-тестами.

| Связь | Сопоставленные файлы и вывод |
| --- | --- |
| Общий лист → configuration | WitcherItemSheet создаёт базовую configuration; Weapon и Armor заменяют её специализированной боевой, Alchemical/Valuable — расходуемой. Mutagen/Enhancement сохраняют базовую. Настройки Item.effects остаются документами ActiveEffect во всех этих окнах. |
| Вложенная схема → специализированная модель | TASK-0003.012/013: attackOptions/damageProperties/defenseProperties определяют данные боя; .014 включает SP/resistance/itemEffect в броню/улучшение; .015 включает consumable/consumeProperties в три модели. Наличие схемы не означает подключения всех полей к UI или вызовам Actor. |
| itemEffect → разные коллекции | Armor/Enhancement/DamageProperties используют TypedObjectField с ключом записи; consumeProperties — два массива SchemaField без id. Общий shape записи не делает совместимыми перебор flat(), поиск obj.id или словарные update. issues-00084/00089/00091 описывают разные разрывы. |
| Основная форма → shared header | Header обслуживает поля и configureItem. Тип мутагена выведен именно там. Стандартный clickableImage остаётся условным полем header и связан с ранее зарегистрированным issue-00063. |
| Configuration → эффекты | Боевой редактор и базовый ItemSheet адресуют словари; consumable configuration ищет ID в массивах. Документы ActiveEffect создаёт базовый WitcherConfigurationSheet; их изменения/длительность не являются полями itemEffect. |
| Подготовка → применение | Бонус SP/сопротивления — расчёт prepared модели брони; расходование — отдельное действие, запрашивающее HP/status/effect записи Actor. Подготовленное значение формы не следует считать исходным, а раннее завершение Promise — завершением записи. |
| Caller → списание → helper → чат | Actor.useItem и menu списывают количество отдельно от Item.consume. Три вида результатов consume — лечение, списки статусов, applySelf ActiveEffect; time/toxicity в этот процесс не входят. У последней единицы существует показанный порядок удаления источника до поиска UUID. |

Уточнения записаны в связанные карточки. Исторические результаты .011–.014 сохранены в следующих разделах журнала; Foundry, исходники системы и формы за время серии не менялись. Исправления схем, интерфейса и правил не выбирались.

### Наблюдения и ограничения

Добавлены [issue-00091](../../issues/potential/issue-00091.md), [issue-00092](../../issues/potential/issue-00092.md), [issue-00093](../../issues/potential/issue-00093.md): отсутствующий ID записи, отсутствующее addsTempHp и неподключённая configuration мутагена. Дополнены issue-00008/00031/00034/00045/00049/00060; все **93 issues остаются potential**. Наличие регистрации не подтверждает проблему пользователем и не разрешает исправление.

Связь расходования с issue-00049 установлена статически по toggle без active:true; disabled-документ в новых тестах не использовался. GM query перехвачен один раз: удалённая доставка/повторение не запускались. Отсутствие автоматизации токсичности, времени и вероятности записано как факт кода, без вывода о нарушении правил. Пустая иконка неизвестного статуса — граница представления; отдельная issue не создавалась.

Не исполнялись мир, браузерный submit/FormDataExtended, серверная запись/валидация Item и Actor, реальные Roll с кубиками, сеть, изготовление алхимии, полные правила мутаций и внешний UI. Никаких игровых данных, runtime-файлов, сборок, настроек сервиса или прав доступа не изменено.

### Контроль документов и исходников

Проверки прошли: реестр содержит 621 уникальный исходник; 121 карточка связана со строками «Проверено», 500 строк остаются «Не начат». Подсчёт задач даёт 49 выполненных и 47 ожидающих файлов второй серии. Все 93 issues находятся в potential, ID последовательны; новых карточек проблем три.

Во всех 121 описаниях сверены 211 прямых относительных импортов с существующими исходниками. В 266 Markdown-документах проверены 5708 локальных ссылок и якорей. Все новые карточки содержат 11 обязательных разделов, собственные методы/поля и дату/коммит; задачи и указатели согласованы. Изменены 49 документов (31 существующий, 18 новых); git diff --check завершился без ошибок.

Все 621 исходник побайтово совпадают с HEAD и базовым срезом TASK-0001; фактическое дерево и исключения согласованы с реестром. Сохранены mode/uid/gid/inode всех 926 ранее отслеживаемых файлов. SHA256 набора исходников (путь + NUL + байты + NUL, порядок реестра) — `9de49bf9b75194490fcfd7bfc80e2b1c8bcd9d90dd26f3603faf21d92b3d0e1e`; SHA256 sorted JSON метаданных — `eb8f3c27a24727a4949872dc5c675abc522990fbf0ad53050bb6749e2be44f1b`. Историческая часть журнала, начиная с TASK-0003.014, сохранена дословно.

Покрытие — **121 из 621 файла**, не разобраны **500**. Во второй серии выполнены **49 из 96**, в очереди TASK-0003.016–TASK-0003.020 остаются **47**; ещё **453** требуют детализации. Следующая порция — [TASK-0003.016 — Компоненты и рецепты: данные, связи и редактор](../../tasks/task-0003.016.md).

## TASK-0003.014

Дата: 2026-09-10. Ветка rusbar-main, HEAD `0fa589bd300856ff309f362afcb66d6fa43401ab`; на старте рабочее дерево чистое, отслеживаются 908 файлов. Все 621 исходник совпадают со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. Foundry 14.367.0 по /opt/foundryvtt/package.json, Node 24.16.0.

### Полный охват порции

| Файл | Логических строк |
| --- | --- |
| [module/data/item/armorData.js](../../../module/data/item/armorData.js) | 267 |
| [module/data/item/enhancementData.js](../../../module/data/item/enhancementData.js) | 42 |
| [module/data/item/templates/itemEffectData.js](../../../module/data/item/templates/itemEffectData.js) | 10 |
| [module/item/sheets/WitcherArmorSheet.js](../../../module/item/sheets/WitcherArmorSheet.js) | 55 |
| [module/item/sheets/WitcherEnhancementSheet.js](../../../module/item/sheets/WitcherEnhancementSheet.js) | 29 |
| [module/item/sheets/configurations/WitcherArmorConfigurationSheet.js](../../../module/item/sheets/configurations/WitcherArmorConfigurationSheet.js) | 11 |
| [templates/sheets/item/armor-sheet.hbs](../../../templates/sheets/item/armor-sheet.hbs) | 175 |
| [templates/sheets/item/enhancement-sheet.hbs](../../../templates/sheets/item/enhancement-sheet.hbs) | 73 |
| [templates/sheets/item/configuration/tabs/armorGeneral.hbs](../../../templates/sheets/item/configuration/tabs/armorGeneral.hbs) | 20 |
| **Всего** | **682** |

Полностью описаны ArmorData, EnhancementData, фабрика itemEffect, два листа, специализация конфигурации и три HBS. У Armor 27 верхних полей, у Enhancement 16, у itemEffect 4. Проверены все собственные методы, обе формы словаря/массива воздействий у потребителей, 13 прямых ES-import связей, все поля и ветви форм.

### Перекрёстная сверка

- ArmorData → CommonItemData, SpData ×6, ResistanceData, DefenseProperties, itemEffect, associatedDiagramUuid/unwrapAssociatedDiagram. Два определения location: последнее StringField заменяет ArrayField. Shield — значение location; getList('shield') не использует дополнительный контракт защиты.
- prepareBaseData → разрешение ID улучшений → freeEnhancements → derived сопротивлений и SP → рецепт. Исходные ID могут отличаться от разрешённых Items; свободные ячейки считают исходную длину. Повторы не устраняются, system улучшения остаётся общей ссылкой.
- EnhancementData → itemEffect и внешняя установка через _chooseEnhancement/removeEnhancement. applied, переименование и разделение quantity выполняются вне модели; настоящее системное улучшение Item не является temporaryItemImprovement ActiveEffect.
- ArmorData.effectsWithEnhancements/enhancementsEffects объединяют словари по ID, последняя запись перекрывает предыдущую. Getter объединённых воздействий не найден среди прямых потребителей Actor. Его prepareDerivedData ожидает массив effects, а затем передаёт в applyStatus объекты CONFIG.armorEffects с несовместимым набором полей.
- Поля defenseProperties доступны в ArmorConfig, но ArmorData не предоставляет вызываемые Actor/Item isApplicableDefense/createDefenseOption. Это не отменяет отдельный штатный путь щита через CONFIG.defenseOptions/getList.
- applySpDamage проверяет modifiedStoppingPower, пишет исходный stoppingPower и полностью пропускает слишком большой урон. При бонусе улучшения исходный остаток может стать отрицательным; самостоятельное нарушение правил этим не объявлено. Внешние armorMixin/defenseMixin/RepairData прочитаны в пределах вызовов, не помечены полностью разобранными.
- Миграции: старые ID добавляются к новым; Armor удаляет преобразованный непустой effects, Enhancement сохраняет; SP переносится при truthy старом максимуме, сопротивления — при truthy старом флаге. При смешанных данных новые значения не защищены от прежних.
- ArmorSheet меняет общий CONFIG.WITCHER через context.config, EnhancementSheet добавляет отдельный context.selects. Броня наследует CRUD effects и подключает примесь рецепта; её конфигурация меняет только general PARTS.
- armor-sheet.hbs показывает SP по location и надёжность для Shield. armorGeneral всегда выводит 12 SP-полей. Стороны leftLeg/rightLeg и поле максимума торса правильные; прежняя issue-00007 относится к helper инвентаря.
- Форма сопротивлений получает вычисленные boolean вместо исходных; смоделированный submit закрепляет вклад улучшения в source. Для эффектов брони выведены name/statusEffect, для улучшений также percentage; varEffect в этих двух формах не редактируется.
- Проверены 50 буквальных ключей девяти файлов и двух вложенных моделей: все найдены в en, 46 в ru. Четыре отсутствующих русских hint из armorGeneral оформлены issue-00090. В локальном Localization.localize есть английский fallback, поэтому ожидается английский текст при штатной загрузке, а не обязательно сырой ключ.

Уточнены 12 прежних карточек: SpData, ResistanceData, WeaponData, DamageProperties, WitcherActor, WitcherItem, WitcherItemSheet, WitcherPropertiesConfigurationSheet, registerDataModels, registerSheets, config и handlebars. Уточнения не повышают статус соседних непрочитанных файлов.

### Изолированные проверки

Команда: `node --input-type=module`, код через stdin, файлов стенда нет. Использованы настоящие common DataModel/TypeDataModel, поля, utilities, модели системы, классы листов, локальные ItemSheetV2, DragDrop и HandlebarsApplicationMixin. DocumentSheetV2/окружение Application, DOM/jQuery, Item.update, fromUuidSync и действия Actor представлены фасадами. Для методов ArmorData родительский Item-контекст задан после создания модели; полноценный Foundry Item не конструировался.

Исходные _prepareTabs/_getTabsConfig и _processFormData ядра исполнены отдельно. Handlebars/parse5 настоящие; formGroup из ядра, toFormGroup учитывает реальные пути/значения вместо создания браузерных widgets. selectOptions — ограниченный генератор с valueAttr/labelAttr и SafeString. Это не тест полного внешнего helper. Доступ к getter разрешён теми же опциями прототипа, которые использует renderTemplate Foundry.

| Группа | Проверка и результат |
| --- | --- |
| 1. Схемы и улучшения | Armor 27 / Enhancement 16 / itemEffect 4; location StringField. Из ID e1/missing/пустой/e2 разрешены e1/e2, свободных 0. SP 4/10 +2/+1 →7/13; max 0 пропускает бонус. OR сопротивлений и перекрытие равного ID проверены, source.effects сохранён |
| 2. Свободные ячейки | enhancements0 с одним ID, −1 и 1.5 дают RangeError; контроль 2 без ID даёт 2 |
| 3. Владелец | Непустые ID без Actor дают TypeError чтения items |
| 4. Урон SP | SP 5 с уроном 2/5/6 → запрос 3/0/нет; SP 1+2 с уроном 2/4 → исходный−1/нет |
| 5. Ремонт | Проверена каждая из шести частей и надёжность; без UUID возвращается '', неповреждённая с UUID false. repair отправляет семь правильных максимумов, завершается раньше pending update |
| 6. SP/сопротивления | Все шесть старых пар перенесены; конфликт 9/15 с прежними 2/4 даёт 2/4. Старый max 0 пропущен. Старое true перекрывает новый false во всех трёх сопротивлениях |
| 7. Воздействия и проценты | Старый непустой effects у Armor исчезает, у Enhancement сохраняется с новым ID. Пустой массив Enhancement очищается в{}. Значения −1/25/101 очищаются до 0/25/100; строка 25 становится числом; varEffect сохраняется |
| 8. Сбор воздействий Actor | Настоящая ArmorData с заполненным statusEffect передаёт []; контроль старого массива доходит до CONFIG.armorEffects |
| 9. Дополнительная защита | Вложенная модель с melee применима, два метода на ArmorData отсутствуют, общий отбор даёт 0 |
| 10. Контекст/слушатель | У Armor4 типа,5 локаций, shared CONFIG=true; настоящий _onRender подключает recipe-remove |
| 11. Форма брони | '',Head,Torso,Leg,FullCover,Shield →15/17/21/19/27/17 именованных controls с header. Одно собственное воздействие даёт два editable-поля, две записи улучшения — четыре disabled |
| 12. Форма улучшения | '',weapon,rune,armor,glyph →6/6/6/11/6 именованных controls; три editable-поля effects. Списки statusEffects/armorEffects выбраны по категории |
| 13. Конфигурация | FullCover/Shield:12 SP-полей,3 вкладки,5 частей, правильные пары локаций |
| 14. CRUD effects | Имя on передаёт false, add создаёт percentage0, remove формирует -= ключ; преобразование deletion ядром проверено в предыдущей порции и не объявлено новым браузерным тестом |
| 15. Рецепт | armor/elderfolk-armor приняты, weapon отклонён; fromUuidSync разрешил подготовленный рецепт |
| 16. Checkbox сопротивления | Исходный slashing=false, prepared=true от улучшения, checkbox отмечен |
| 17. Модель сохранения формы | FormData.object собран из rendered resistance-checkbox и encumb; исходный _processFormData и ArmorData.updateSource сохранили true, новая модель без ID улучшения осталась true |
| 18. Вход applyStatus | CONFIG.armorEffects с id/fire не вызвал toggleStatusEffect; контроль {statusEffect:fire} вызвал один раз. Это проверка формата, не предложение накладывать fire вместо сопротивления |

Все 18 групп утверждений завершены. Ошибки настройки диагностического окружения (подходящий родитель модели, сериализация prepared значений через toObject(false), учёт clickableImage в header, ограниченный selectOptions) устранены в переданном через stdin сценарии и не отнесены к ошибкам системы. Стандартное предупреждение Node о module type не исправлялось.

### Наблюдения и ограничения

Добавлены [issue-00082–00090](../../issues/README.md): длина массива ячеек, пропуск повреждения SP, форма коллекции воздействий Actor, неподключённая защита, приоритет миграции SP и сопротивлений, сохранение prepared сопротивления, формат входа applyStatus и русские подсказки. Дополнены issue-00007/00042/00060/00068/00077/00078/00080/00081. Все 90 issues остаются potential; подтверждение, исправление и закрытие не выполнялись.

Браузерный submit/FormDataExtended, validate/update реального документа, БД, мир, сеть, игровые броски, полный бой/ремонт и установка/снятие через интерфейс не запускались. Не утверждается, что одна поправка миграции либо воздействия исправит все звенья. Игровая трактовка исходного отрицательного SP, свойств сопротивления и дополнительных защит не выбрана.

### Контроль документов и исходников

Проверены 248 Markdown-документов и 5379 локальных ссылок с якорями. В реестре ровно 621 исходный файл после исключений; 106 строк «Проверено» соответствуют 106 карточкам, 515 файлов не разобраны. Для девяти новых карточек проверены обязательные разделы, собственные методы, поля и прямые импорты; всего в описанных JS проверены 196 относительных ES-import связей. Перечни девяти файлов/682 строк, статусы двадцати подзадач, очередь из 62 файлов и 90 potential issues согласованы.

Все 621 исходник побайтово совпадают с HEAD и базовым срезом. SHA256 последовательности path + NUL + bytes + NUL в порядке реестра: `9de49bf9b75194490fcfd7bfc80e2b1c8bcd9d90dd26f3603faf21d92b3d0e1e`. Для всех 908 ранее отслеживаемых файлов сохранены mode/uid/gid/inode; SHA256 отсортированного JSON метаданных: `343c64aa9fa4b850afe60b92c9934dc28c1616add628841cf57f926ad0ef7f0a`. История журнала от TASK-0003.013 сохранена побайтово. Изменены только 49 документов; `git diff --check` прошёл. Тестовые файлы, игровые документы и коммиты не создавались, права не менялись.

Покрытие — 106 из 621 файла, не разобраны 515. Во второй серии выполнены 34 из 96, в очереди TASK-0003.015–TASK-0003.020 остаются 62 файла; ещё 453 требуют детализации. Следующая порция — [TASK-0003.015](../../tasks/task-0003.015.md).

## TASK-0003.013

Дата: 2026-09-10. Ветка rusbar-main, HEAD `8cca18e14b75ec53028ee6bc49a837597de4d9af`; рабочее дерево на старте чистое, отслеживались 892 файла. Все 621 исходник совпали со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. Проверенное ядро — Foundry 14.367.0 по /opt/foundryvtt/package.json, Node 24.16.0.

### Полный охват порции

| Файл | Логических строк |
| --- | --- |
| [module/data/item/weaponData.js](../../../module/data/item/weaponData.js) | 115 |
| [module/item/sheets/WitcherWeaponSheet.js](../../../module/item/sheets/WitcherWeaponSheet.js) | 57 |
| [module/item/sheets/configurations/WitcherPropertiesConfigurationSheet.js](../../../module/item/sheets/configurations/WitcherPropertiesConfigurationSheet.js) | 116 |
| [templates/sheets/item/weapon-sheet.hbs](../../../templates/sheets/item/weapon-sheet.hbs) | 113 |
| [templates/sheets/item/configuration/partials/attackOptionsPart.hbs](../../../templates/sheets/item/configuration/partials/attackOptionsPart.hbs) | 33 |
| [templates/sheets/item/configuration/tabs/damagePropertiesConfiguration.hbs](../../../templates/sheets/item/configuration/tabs/damagePropertiesConfiguration.hbs) | 93 |
| [templates/sheets/item/configuration/tabs/defensePropertiesConfiguration.hbs](../../../templates/sheets/item/configuration/tabs/defensePropertiesConfiguration.hbs) | 19 |
| [templates/sheets/item/configuration/tabs/regionPropertiesConfiguration.hbs](../../../templates/sheets/item/configuration/tabs/regionPropertiesConfiguration.hbs) | 28 |
| **Всего** | **574** |

Полностью разобраны модель WeaponData, два класса листов и пять HBS. Описаны 36 верхних полей модели со всеми подключёнными фабриками, собственные методы, данные и действия, зависимости и потребители. Проверены 12 прямых относительных ES-import связей этих трёх JS. У HBS перечислены все поля, условия, partials, helpers и data-action.

### Перекрёстная сверка

- WeaponData → CommonItemData, weaponType, attackOptions/defenseOptions, DamageProperties/DefenseProperties, associatedDiagramUuid. Количество наследуется как StringField; NumberField надёжности и вместимости улучшений не задают минимум/максимум. canBeRepaired возвращает пустую строку либо boolean, не проверяет разрешение UUID.
- WeaponData.prepareDerivedData → коллекция Items владельца → enhancementItems → потребители улучшений и RepairData. Отсутствующие ID пропускаются, повторы сохраняются, system передаётся по ссылке. Миграция прежнего enhancementItems дополняет существующий enhancementItemIds без устранения повторов. Сопоставление с подсчётом enchantsCount/enchantsDC выполнено статически; полный ремонт оставлен TASK-0003.017.
- WeaponData.createDefenseOption → вложенная DefenseProperties → навыки → Item/Actor защиты. Проверена передача modifier и применимости; выбор навыка с пустой строкой и initial spellcasting описан отдельно. Полный бросок не запускался.
- WitcherWeaponSheet → WitcherItemSheet._onRender → activateListeners → обработчик четырёх checkbox типа урона. Их id используются как ключи, name отсутствует; инвертируется значение модели, формируется локализованный text. Предыдущий открытый вопрос карточки weaponType о подключении слушателя уточнён.
- Связанный рецепт: main → associated-diagram.hbs → associatedDiagramMixin → system.associatedDiagramUuid → unwrapAssociatedDiagram. Сверены weapon/elderfolk-weapon, отказ для неподходящего типа и удаление ссылки. DOM-проверка offsetParent исследована отдельно от разрешения UUID.
- Конфигурация свойств наследует WitcherConfigurationSheet, а не системный WitcherItemSheet. PARTS и TABS проверены раздельно для Weapon/Armor/Spell. Старый system.createTemplate в фильтре не совпадает с текущим system.templateProperties.createTemplate; отсутствующее createRegionFromTemplate в самом HBS — второй разрыв.
- Все schema/value пути пяти форм сопоставлены с настоящими моделями. attackOptionsPart содержит семь formGroup и включается spellGeneral; weapon использует общую general-разметку. Вариант itemUse доступен, но поля его навыка нет — дополнена issue-00061. Заголовок spell в partial корректный, прежняя issue-00062 относится к другому шаблону.
- Редактор damageProperties: собственные записи effects используют target/id/field и действия общего конфигуратора; enhancementEffects выводятся disabled. Это объекты предметных воздействий, а не документы ActiveEffect. Пять полей регионального HBS включают один отсутствующий флаг и четыре действительных DocumentUUIDField типа Macro.
- Локализация и конфигурационные списки сопоставлены по используемым ключам с config/settings и en/ru. Новая context.config.attackSkills содержит восемь навыков и изменяет общий CONFIG.WITCHER; отдельный потребитель этого списка не найден. Это наблюдение само по себе не объявлено проблемой.

Уточнены десять прежних карточек: WitcherItemSheet, WitcherConfigurationSheet, attackOptionsData, damagePropertiesData, defensePropertiesData, weaponTypeData, damagePropertiesMigration, registerSheets, registerDataModels и config. Региональные модели, примесь рецепта, полный ремонт и боевые процессы прочитаны в пределах связей и не получили полного статуса анализа.

### Изолированное выполнение

Команда: `node --input-type=module`, сценарий передан через stdin, файлов стенда не создавалось. Загружены настоящие common DataModel/TypeDataModel, поля, utilities, зарегистрированные системные модели и классы листов. Использованы локальные ItemSheetV2, DragDrop и HandlebarsApplicationMixin; DocumentSheetV2 и окружение Application представлены фасадом. Исходные _prepareTabs/_getTabsConfig ApplicationV2 исполнялись отдельно. Это проверяет тела методов и согласованность данных, но не полный жизненный цикл окна.

Handlebars и parse5 настоящие. formGroup взят из ядра; field.toFormGroup заменён учётом путей и значений, selectOptions — ограниченным генератором options. DOM/jQuery, game.settings, fromUuidSync, Item-контекст и update подменены. Рендер использовал разрешения доступа к свойствам прототипа, которые настоящее renderTemplate задаёт в /opt/foundryvtt/client/applications/handlebars.mjs; getter enhancementEffects при них доступен.

| Сценарий | Результат | Предел |
| --- | --- | --- |
| _onRender → listeners → _onDamageTypeEdit | Зарегистрированы .damage-type/change и .remove-associated-diagram/click; payload содержит slashing=true, piercing=true, text «Режущий, Колющий» | DOM и запись представлены фасадом |
| Рецепт: принять, отклонить, убрать, offsetParent=null | Сохранён UUID weapon-рецепта; armor-рецепт дал уведомление без update; удаление записало ''; null вызвал перехваченный unhandledRejection | Геометрия реальных целей сброса не проверена |
| TABS/PARTS для Weapon, Armor и Spell с createTemplate=false/true | У Weapon 4 вкладки/6 частей, у Armor 3/5; у обоих Spell 5/6, региональная вкладка есть, части нет | Сравниваются структуры, не экран браузера |
| Региональный HBS | Один console.error от formGroup, отсутствующее поле пропущено, остальные четыре UUID-поля сформированы | Прямой диагностический рендер в обход фильтра PARTS |
| Миграция макроса движения | Только новый ключ → null; только старый → перенесён; оба → старое значение побеждает | Модели в памяти, без Macro/Region в мире |
| Подготовка улучшений | С владельцем существующий ID разрешается; отсутствующий пропускается; повторы остаются; без владельца TypeError чтения items | Родитель Item — фасад |
| Миграция улучшений | Смешанные старые/новые данные дали два одинаковых ID; второй вызов на том же сыром объекте — три; новая модель из смешанного входа — два | Наличие таких записей в БД неизвестно |
| Завершение repair | Promise метода завершился, пока parent.update оставался pending; payload надёжности корректный, prepared reliable ещё 2 | Управляемый update, без записи |
| Выбор защиты и количество | Пустой melee блокирует archery; без melee выбирается archery; itemUse при начальном spellcasting даёт spellcasting. Throwable: 1 → true; 0/-1/abc/выключенный флаг → false | Без броска и расходования предметов |
| Форма оружия / боеприпаса | С общим header 19/13 именованных controls; четыре checkbox типа и область рецепта сохранены в обоих вариантах | Настройка clickableImageItemTypes задана штатной строкой |
| attackOptionsPart и действия effects | Семь schema-полей; itemUseAttackSkill отсутствует. Add создаёт запись percentage=0; имя on превращается в false; процент передаётся строкой до очистки; -= удаляет запись | Настоящая модель дала name='false'; legacy deletion преобразован ядром с compatibility warning |
| Матрица silverTrait × staminaIsVar × defenseDifferenceMultiplier | Проверены все 8 сочетаний: silverTrait либо silverDamage, условный cap, условный varEffect, 3/4 disabled-поля одного улучшения | 16 formGroup в исходнике, 14/15 реально выведенных schema-полей; не полный DOM-виджет |

Успешно завершены 12 групп утверждений. Ошибки первоначальных диагностических фасадов (тип настройки, межконтекстный Array.filterJoin, опции доступа Handlebars к прототипу и подсчёт ammo-полей) исправлены только в передаваемом через stdin сценарии и не зарегистрированы как проблемы системы.

### Наблюдения и границы выводов

Добавлены [issue-00074–00081](../../issues/README.md): два разрыва региональной формы, перезапись макроса миграцией, подготовка улучшений без Actor, повтор ID при миграции, пустой навык защиты, зависимость drop от offsetParent и преждевременное завершение Promise ремонта. Дополнены [issue-00060](../../issues/potential/issue-00060.md) и [issue-00061](../../issues/potential/issue-00061.md). Все 81 карточка остаются potential; ни подтверждения, ни исправления этим этапом не оформляются.

Не доказано удвоение боевого эффекта повторным ID. Повторный ручной вызов prepareDerivedData без обычного reset не доказывает сохранение «призрачного» улучшения в клиенте. Отсутствие createRegionFromTemplate не прерывает весь рендер: helper пишет ошибку и возвращает пустой SafeString. Старый синтаксис удаления effects в этом ядре работает. Полный браузер, мир, база данных, реальные компедиумы, сеть, боевые броски и ремонт не запускались.

### Контроль документов и исходников

Проверены 230 Markdown-документов и 5074 локальные ссылки с якорями. Реестр содержит ровно 621 исходный файл после исключений; 97 карточек соответствуют 97 строкам «Проверено», оставшиеся 524 имеют статус «Не начат». Перечни текущей порции (8 файлов / 574 строки), всех двадцати подзадач, очереди из 71 файла и 81 potential issue согласованы; для новых карточек проверены все обязательные разделы, собственные методы и поля. В 97 карточках проверены 183 прямых относительных ES-import связи до файлов определений. Все 77 буквальных ключей локализации восьми исходников и четырёх подключённых схем найдены в en/ru.

Все 621 исходник побайтово совпадают с HEAD и базовым срезом. SHA256 последовательности path + NUL + bytes + NUL в порядке реестра: `9de49bf9b75194490fcfd7bfc80e2b1c8bcd9d90dd26f3603faf21d92b3d0e1e`. Для всех 892 ранее отслеживаемых файлов сохранены mode/uid/gid/inode; SHA256 отсортированного JSON этих метаданных: `ba2bf09fb49eb2f7e8192aa807bc23d07faaa81eb4e174f861797d97cfa2f2a9`. Исходная история журнала от TASK-0003.012 сохранена побайтово. Изменены только 39 документов; `git diff --check` прошёл. Тестовые файлы, игровые документы и коммиты не создавались, права не менялись.

Покрытие — 97 из 621 файла, не разобраны 524. Во второй серии выполнены 25 из 96 файлов; 71 ожидает TASK-0003.014–TASK-0003.020, ещё 453 требуют детализации. Следующая согласованная порция — [TASK-0003.014](../../tasks/task-0003.014.md), броня и улучшения предметов.

## TASK-0003.012

Дата: 2026-09-10. Ветка rusbar-main, HEAD `d20d821e3a8a0a989ec503b0e97413a5a1431ad9`; рабочее дерево на старте чистое, отслеживались 872 файла. Все 621 исходник совпали со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. Проверенное ядро — Foundry 14.367.0 из /opt/foundryvtt/package.json, Node 24.16.0.

### Полный охват порции

| Файл | Логических строк |
| --- | --- |
| [module/data/item/templates/combat/attackOptionsData.js](../../../module/data/item/templates/combat/attackOptionsData.js) | 49 |
| [module/data/item/templates/combat/damagePropertiesData.js](../../../module/data/item/templates/combat/damagePropertiesData.js) | 116 |
| [module/data/item/templates/combat/defenseOptionsData.js](../../../module/data/item/templates/combat/defenseOptionsData.js) | 11 |
| [module/data/item/templates/combat/defensePropertiesData.js](../../../module/data/item/templates/combat/defensePropertiesData.js) | 26 |
| [module/data/item/templates/combat/skillAttackData.js](../../../module/data/item/templates/combat/skillAttackData.js) | 25 |
| [module/data/item/templates/combat/skillDefenseData.js](../../../module/data/item/templates/combat/skillDefenseData.js) | 13 |
| [module/data/item/templates/weaponTypeData.js](../../../module/data/item/templates/weaponTypeData.js) | 11 |
| [module/data/item/templates/armor/resistanceData.js](../../../module/data/item/templates/armor/resistanceData.js) | 23 |
| [module/data/item/templates/armor/spData.js](../../../module/data/item/templates/armor/spData.js) | 41 |
| [module/data/migrations/damagePropertiesMigration.js](../../../module/data/migrations/damagePropertiesMigration.js) | 25 |
| **Всего** | **340** |

Полностью описаны четыре класса DataModel, пять фабрик схем и одна миграционная функция. Указаны все поля, defaults, ограничения, callbacks, методы, импорты, потребители и места изменения состояния. Пять прямых относительных ES-import связей десяти файлов проверены до определений; это не заменяет регистрации и динамических связей.

### Перекрёстная сверка

- Weapon/Spell → attackOptions, defenseOptions, DamageProperties, DefenseProperties. Классы не создают отдельные типы документов. У Weapon дополнительно weaponType.
- ProfessionData → professionSkill → skillAttack/skillDefense → общие фабрики и вложенные модели. Реальный parent DamageProperties внутри skillAttack — ProfessionData. Выбор атаки использует характеристику/уровень профессионального навыка; варианты защиты формируются внешней ProfessionData.
- ArmorData → ResistanceData и шесть SpData. Сначала создаются enhancementItems, затем выполняется derived для сопротивлений/SP; base отдельно копирует исходный SP. Сопоставлены шесть локаций и armorPartsInfo; tailWing обрабатывается естественной бронёй монстра.
- Item.system.damageProperties → createBaseDamageObject.properties → сообщение атаки. DamageData и DefenseMessageData включают EmbeddedDataField, а DamageMessageData использует SchemaField с ArrayField effects и полем applied. Методы модели нельзя автоматически приписывать итоговому объекту сообщения.
- DefenseProperties.createDefenseOption даёт modifier и пустые skills/itemTypes; Weapon/Spell заполняют skills, Profession добавляет skillOverride, Item — label/value, Actor — выбор и формулу. В эту модель не включены isDefense и перечень всех защит.
- Миграция старых свойств имеет два caller: WeaponData и SpellData. Последующая миграция массива effects принадлежит DamageProperties. Отдельная миграция ArmorData сравнивалась только в пределах эффекта.
- Шаблоны настроек сверены с schema-путями и ключами en/ru: все label/hint этих десяти файлов найдены в обоих языках. Отдельные labels прямо помечают damageIsAblation, defenseDifferenceMultiplier и defenseMultiplierCap как неработающие; расчёт этих возможностей не домысливался.
- WeaponType.text в схеме свободная строка, но _onDamageTypeEdit листа при вызове формирует её из четырёх флагов. Исправлена первоначальная формулировка черновика карточки о текстовом input после проверки конкретного обработчика; исходник не менялся.

Уточнены девять уже существующих карточек: config, handlebars, settings, registerDataModels, WitcherItem, CommonItemData, WitcherActor, general.hbs и damageTypeModificationData. На основе новых определений дополнена issue-00025; её прежний исполняемый тест applyAP не повторялся. Фрагменты соседних файлов не объявлены полностью разобранными.

### Изолированное выполнение

Команда: `node --input-type=module`, сценарий передан через stdin, файлов стенда не создавалось. Через registerHooks разрешены @common-импорты установленного ядра. Использованы настоящие common DataModel/TypeDataModel, поля, utilities, системные фабрики/модели и DamageInstance. Системные типы загружены по registerDataModels; это инициализация схем, а не запуск Actor/Item мира.

Тела getItemAttack, constructBaseAttackFormula, mergeDamageProperties, createBaseDamageObject и calculateDamageWithLocation взяты из текущих файлов и исполнены без переписывания логики. game/CONFIG/parent и необходимые внешние методы заданы фасадами; реальные документы, DOM, Roll, сеть и БД не вызывались. Для ветки silverTrait подменены getLocationArmor и applyAlwaysSpDamage, выбран ранний выход blockedBySp. Найденные обращения к шаблонам — статические связи, а не проверка доступности этих элементов в браузере.

| Проверка | Результат |
| --- | --- |
| Пустой Weapon | attackOptions=[], spellAttackSkill='spellcasting', melee/ranged/itemUse навыки undefined, бонусы false |
| Старый attackSkill | swordsmanship и archery не дали новых вариантов/навыков: поле удалено SchemaField до defaults |
| Прямой callback и явные новые поля | callback с swordsmanship/throwable дал [melee,ranged]; явно заданные новые поля сохранились |
| Spell с level | [spell], getItemAttack.skill='spellcasting'; общий справочник не содержит ключ |
| Специальный getUsedSkill | class Spells с parent.type spell вернул spellcast; fallback работает |
| Неизвестный skill в формуле | constructBaseAttackFormula получил undefined и выбросил TypeError чтения attribute |
| defenseOptions | Default шесть ключей; явный [] сохранился; непустой неизвестный ключ принят схемой без choices |
| DefenseProperties | melee→true; ranged/undefined/объект→false; createDefenseOption с modifier -2 вернул два пустых массива |
| Defaults DamageProperties | 18 ключей; stun undefined, cap5; effects={} |
| addEffects/getter | Коллизия ID заменяет запись последней; значения по ссылке. Getter не меняет собственные effects |
| Preprocessing | Два bleeding 60 дали 120 и объединённое имя; varEffect от первой записи; безстатусная запись отдельно; исходные effects не изменились |
| Очистка сообщения | Настоящий DamageMessageData ограничил120 до 100, applied=false, invalid=false. Ошибка валидации на этом входе не обнаружена |
| Миграция массива | Непустой array→randomID object; пустой array helper оставил, модель очистила до{}; готовый object сохранил ID |
| Смешанные поля | Старое true заменило новое false; прежний effects=[] заменил вложенный объект; полностью новые данные сохранились |
| Повторное изменение нового флага | После миграции WeaponData.updateSource nested false дал false: постоянного старого shadow после очистки не осталось |
| Эффекты ArmorData | Непустой прежний массив потерян: миграция удаляет только что сформированный объект |
| SP | 7/10 с улучшением 2→9/12; max 0 не получает бонус; повтор derived→11, base+derived→9 |
| Сериализация SP | toObject() содержит базовые поля; toObject(false) также modified; отрицательные числа допустимы схемой |
| Сопротивления | Улучшение slashing:true дало false/true/false, enumerable keys — ровно три resistance |
| Профессия | isDefense:false в ветке всё равно доступен; та же защита в definingSkill не найдена |
| Слияние профессии | armorPiercing присоединён; effects второго объекта пропущен; cap 5+5 дал 10 |
| Ссылка на свойства Item | Повторный createBaseDamageObject до reset видит ammo; source toObject по-прежнему содержит только base |
| SilverTrait | После ветки instance.type остался slashing, instance.setType стал строкой silver |

В окончательном сценарии assert-проверками закреплены одиннадцать групп существенных результатов, включая контрольные противоположные случаи. Диагностический первый запуск показал необходимость копировать входы/результат preprocessing перед передачей моделям: Foundry чистит переданный объект в памяти. Также минимальный контекст проверки формулы дополнен system.stats/system.skills, чтобы изолировать именно ошибку отсутствующего skill.attribute. Эти исправления относились только к сценарию; предварительные диагностические значения не использованы как окончательные выводы.

### Проблемы и границы

Зарегистрированы десять [potential issues-00064–00073](../../issues/README.md): неверный магический default; утрата старого attackSkill; неиспользуемый applyRangedMeleeBonus; приоритет старых свойств; удаление effects брони; пропуск effects профессии при слиянии; изменение подготовленного Item; игнорирование isDefense; пропуск definingSkill; присваивание имени метода вместо изменения серебряного типа. Дополнена issue-00025. Всего **73** карточки, все potential. Подтверждение пользователя и исправления не выполнялись.

Повторный derived SP без base показан как требование порядка фаз, а не как доказательство повторного бонуса в штатном клиенте. Отсутствие части damageTypes у сопротивлений/weaponType не объявлено нарушением игровых правил. Не заявляется отказ любого заклинания из-за spellcasting: специальный fallback проверен. Поведение подготовленного Item до reset не приравнивается к постоянному изменению БД. Для definingSkill проверена модель, полный редактор остаётся TASK-0003.019.

### Охват и контроль изменений

Покрытие — **89 из 621 файла**, не разобраны **532**. Во второй серии проверены 17 из 96; TASK-0003.013–TASK-0003.020 содержат ещё 79 файлов; 453 пока не распределены по конкретным порциям. Следующая задача — [TASK-0003.013](../../tasks/task-0003.013.md). TASK-0003 остаётся in-progress.

Итоговая техническая проверка: 621 исходник совпадает и со срезом TASK-0001, и с HEAD; сводная SHA256 по путям/байтам — `9de49bf9b75194490fcfd7bfc80e2b1c8bcd9d90dd26f3603faf21d92b3d0e1e`. У всех 872 ранее отслеживаемых файлов сохранены mode/uid/gid/inode; контрольная сумма метаданных — `87ddf97b98ce8ceb34bf50042430e2487f32b849513bdb520ab5eee7ff4a6008`. Проверены 89 карточек, пять новых и 171 общая прямая относительная import-связь, 214 Markdown-документов и 4827 локальных ссылок с якорями. В рабочем дереве изменён 41 Markdown-файл, из них 20 новых; исходники не изменены. Проверки таблиц, обязательных разделов, полей/методов, охвата, очереди 79 файлов, статусов 20 подзадач и 73 potential issues пройдены; git diff --check без замечаний. История журнала от TASK-0003.011 и ниже сохранена без изменений. Коммит не создавался.

## TASK-0003.011

Дата: 2026-09-10. Ветка rusbar-main, HEAD `07237960627bf7debc2b4283aa55d1a8c5d1bb8b`; на старте рабочее дерево чистое, отслеживались 858 файлов. Все 621 исходник совпали со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. Локальное ядро Foundry 14.367.0, Node 24.16.0.

### Полный охват порции

| Файл | Логических строк |
| --- | --- |
| [module/item/sheets/WitcherItemSheet.js](../../../module/item/sheets/WitcherItemSheet.js) | 171 |
| [module/item/sheets/configurations/WitcherConfigurationSheet.js](../../../module/item/sheets/configurations/WitcherConfigurationSheet.js) | 143 |
| [templates/partials/item-header.hbs](../../../templates/partials/item-header.hbs) | 71 |
| [templates/partials/item-image.hbs](../../../templates/partials/item-image.hbs) | 8 |
| [templates/sheets/item/configuration/tabs/header.hbs](../../../templates/sheets/item/configuration/tabs/header.hbs) | 3 |
| [templates/sheets/item/configuration/tabs/general.hbs](../../../templates/sheets/item/configuration/tabs/general.hbs) | 45 |
| [templates/sheets/item/configuration/tabs/activeEffectConfiguration.hbs](../../../templates/sheets/item/configuration/tabs/activeEffectConfiguration.hbs) | 4 |
| **Всего** | **445** |

Два JS-файла полностью прочитаны: 13 собственных методов/getter у WitcherItemSheet и три у WitcherConfigurationSheet. Описаны aliases, static-опции, части, вкладки, configuration и callbacks. Пять HBS разобраны целиком: контекст, поля, условия, helpers, действия, родительская разметка и потребители.

### Перекрёстная сверка определений и обращений

- Регистрация → классы: у WitcherItemSheet 17 прямых наследников, шесть замен configuration и шесть собственных _onDropItem. У базовой конфигурации три прямых наследника и два через Properties. У note в системных регистрациях остаётся общий класс с PARTS={}.
- Основной лист → ядро: обычная форма сохраняется через DocumentSheetV2/FormDataExtended, картинка редактируется через editImage/FilePicker. Системный лист вручную редактирует system.effects; отдельная конфигурация создаёт/обновляет документы ActiveEffect. Она напрямую наследует ItemSheetV2 и не получает системный Drop-router.
- Шаблоны → контекст: item-header имеет десять прямых предметных потребителей. item-image имеет один прямой вызов в прежнем monster-inventory-tab; текущий MonsterSheet использует новые PARTS инвентаря. Прежний шаблон предзагружается, но это не делает его текущим рендером.
- General → схемы/потребители: на настоящих 22 моделях Item сверены условные поля. Weapon при включённых всех вариантах даёт 8 полей, Spell — 9, Hex/Ritual — по одному defenseOptions, остальные — ноль. Это диагностическая проверка схем; фактически Armor/Spell заменяют general собственными шаблонами.
- ActiveEffects → действия: четыре категории согласованы с disabled/типом/длительностью; create читает type заголовка, другие actions — effectId строки. Parent UUID вложенного partial не используется Item-handler. Описание остаётся скрытым; listener раскрытия у Item-конфигурации не найден.

Прямой ES import в двух исходниках один: WitcherItemSheet → WitcherConfigurationSheet. Наследование ядра, регистрации, динамические методы, HTML-атрибуты, схемы, стили и локализации описаны отдельными связями. Уточнены девять ранее созданных карточек: registerSheets, handlebars, settings, config, WitcherItem, CommonItemData, effect-part, ActiveEffectSheet и ActiveEffect.

### Изолированные сценарии

Команда исполнения: `node --input-type=module` с переданным через stdin сценарием, без создания файла стенда. Загружены настоящие common-модели/поля/утилиты Foundry, все зарегистрированные системные модели Item, полные системные классы этой порции, полные CoreItemSheetV2/DragDrop/HandlebarsApplicationMixin и исходный formGroup. DocumentSheetV2 и контекст Application представлены фасадом; DOM-элементы, fromDropData, Hook, запись документов, Dialog и рендер поля toFormGroup подменены явно.

| Проверка | Фактический результат | Ограничения |
| --- | --- | --- |
| Drop Actor/Item/Folder | На общем листе три TypeError отсутствующего метода; Other→null, isEditable=false→undefined | Шесть специализированных Item-handler не исполнялись целиком |
| Drop ActiveEffect | Core-handler дошёл до create с parent=item; тот же родитель и isOwner=false остановили вызов | create перехвачен, БД отсутствует |
| Hook отмены Drop | Core _onDrop вызвал dropItemSheetData и остановился при false; override не вызвал hook и дошёл до создания | Это проверка стандартной точки расширения, не установленного внешнего модуля |
| Повторный рендер | После двух _onRender вызовов drop выполнился один раз; draggable=false | Настоящий DragDrop заменяет свойства ondrop; слушатели наследников отдельно не моделировались |
| Контекст | config/data остаются ссылками; два prepare добавляют две одинаковые строки options.classes | Видимое влияние повторного класса не устанавливалось |
| Редактирование воздействия | Текст on передан как false, настоящая модель дала строку false; checkbox→true, percentage→строка25 в payload | Элемент/запись подменены; очистка типа проверена на реальной модели |
| Удаление воздействия | Старый ключ -=fx преобразован в ForcedDeletion; запись удалена из EnhancementData | Только updateSource в памяти; compatibility warning перехвачен |
| Завершение ручного action | _onAddEffect завершился, пока update оставался pending | Проверка Promise, не DB-сохранение |
| Категории/управление FX | Проверены шесть комбинаций свойств, четыре create-payload и edit/toggle/delete | units/start/transfer/changes не заданы create-payload; фактическое сохранение defaults не исполнялось |
| Шапка Item | 12 комбинаций GM/ограничения/трёх типов и отдельный showConfig=false; всегда один editImage, mutagen выводит type вместо cost | Helpers настоящие, полноценный FilePicker/submit не запускался |
| Картинка инвентаря | Четыре комбинации допустимости типа/флага; .item-show только при true/true; _onItemShow сформировал Dialog картинки | Флаг передан вручную; не сохранялся в Item |
| Поле clickableImage | В реальных Valuable/Armor/Weapon/Mutagen поле отсутствует; входной true не попал в prepared/toObject | Не моделировалось изменение схем сторонним модулем |
| Заголовок настроек | Handlebars с ru.json дал h1 «Настройки» | Без окна браузера |
| itemUse | getItemAttack на новом WeaponData дал itemUse без skill; начало weaponAttack выдало «Атакующий навык не настроен» | Проверена ранняя ветвь; бой/броски не запускались |
| Заголовок spell | Три раздела дали «Ближний бой», «Дальний бой», «Дальний бой» | Сверены en/ru, остальные языки не проверялись |
| Note | Перехват регистраций оставил WitcherItemSheet; настоящие HBM options.parts=[] и _renderHTML={} | Подмена Application/DocumentSheet; пользовательская регистрация листа не проверялась |

Сценарий содержит assert-проверки значимых результатов, матриц, маршрутов и схем. Первые запуски потребовали исправить только изолированный сценарий: убрать JSON-сериализацию циклических схем, передать ui в vm и перехватить compatibility logger. Эти ошибки окружения не записаны как ошибки системы. Итоговый запуск завершился успешно. Код системы, зависимости и тестовые файлы не менялись.

### Проблемы, границы и следующий шаг

Зарегистрированы [issue-00057–00063](../../issues/README.md) в potential: note без содержимого листа; отсутствующие Drop-handler; обход Drop-hook; преобразование текста on; недоступный выбор навыка itemUse; подпись spell; разрывы настройки кликабельной картинки. Дополнены issue-00005 и issue-00056. Всего 63 проблемы, все остаются potential; исправления не выполнялись.

Полностью описаны только семь файлов перечня. Определения и вызовы в соседних моделях, специализированных листах, Actor-mixin, стилях и локализациях прочитаны в пределах связи; их статусы полного разбора не менялись. Мир, реальный браузер/DOM, FormDataExtended и сетевые/DB-операции не запускались. Динамические сторонние регистрации/шаблоны и права записи в реальном клиенте не проверены.

Покрытие — **79 из 621 файла**, не разобраны **542**. Вторая серия выполнена на 7 из 96 файлов; в TASK-0003.012–TASK-0003.020 остаются 89 файлов, ещё 453 требуют детализации. Следующая порция — [TASK-0003.012](../../tasks/task-0003.012.md). TASK-0003 остаётся in-progress.

### Итоговая проверка документации и сохранности

Python-проверка подтвердила: 621 исходник совпадает с базовым срезом и HEAD, набор файлов в Git/дереве/реестре одинаков; 79 карточек соответствуют статусам «Проверено», 542 строки — «Не начат». Проверены обязательные разделы семи новых карточек, имена всех собственных методов и 166 прямых относительных импортов всех описанных JS-файлов.

Проверены 194 Markdown-файла и 4514 локальных ссылок, таблицы, 20 статусов подзадач, 89 файлов оставшейся очереди и 63 issues в potential. `git diff --check` прошёл. Изменены 36 Markdown-документов: семь новых карточек и семь новых issues, девять прежних карточек, две прежние issues и одиннадцать документов задач/реестров/навигации.

SHA256 исходного набора: `9de49bf9b75194490fcfd7bfc80e2b1c8bcd9d90dd26f3603faf21d92b3d0e1e`. SHA256 JSON-снимка mode/uid/gid/inode всех 858 ранее отслеживаемых файлов: `fea599dce3471f005a3a3dc9677253b84a80271d3ba8d9cbc315cbd6ce20faca`; оба значения совпали с замером перед работой. Ветка и HEAD не изменены. Исторический журнал, начиная с планирования второй серии, сохранён без редактирования.

<a id="планирование-task-0003011task-0003020"></a>

## Планирование TASK-0003.011–TASK-0003.020

Дата: 2026-09-10. Ветка rusbar-main, HEAD `a2d62819ebb9727368fc523b0142315d4854b9ba`; на старте рабочее дерево чистое, отслеживаются 848 файлов. Пользователь поручил оформить следующие десять задач и согласовал увеличение небольших связанных порций.

### Состав и проверка плана

| Подзадача | Файлов | Логических строк |
| --- | --- | --- |
| [TASK-0003.011](../../tasks/task-0003.011.md) | 7 | 445 |
| [TASK-0003.012](../../tasks/task-0003.012.md) | 10 | 340 |
| [TASK-0003.013](../../tasks/task-0003.013.md) | 8 | 574 |
| [TASK-0003.014](../../tasks/task-0003.014.md) | 9 | 682 |
| [TASK-0003.015](../../tasks/task-0003.015.md) | 15 | 482 |
| [TASK-0003.016](../../tasks/task-0003.016.md) | 12 | 584 |
| [TASK-0003.017](../../tasks/task-0003.017.md) | 5 | 485 |
| [TASK-0003.018](../../tasks/task-0003.018.md) | 8 | 194 |
| [TASK-0003.019](../../tasks/task-0003.019.md) | 12 | 781 |
| [TASK-0003.020](../../tasks/task-0003.020.md) | 10 | 428 |
| **Всего** | **96** | **4995** |

Проверены `git status --short`, `git branch --show-current`, `git rev-parse HEAD`, актуальный реестр и списки первой серии. Планировочное чтение схем, импортов, методов, регистраций PARTS и ссылок на шаблоны использовано для выбора связанных групп. Это не полный разбор 96 файлов и не проверка их поведения.

Python-проверка сопоставила пути с реестром и прежними порциями: 96 уникальных файлов существуют, все имеют статус «Не начат» и ещё не имеют карточек; пересечений с 72 разобранными файлами нет. Первые десять подзадач содержат 61 различный файл, новая серия — 96, общий объём детализации TASK-0003 — 157 из 610 файлов.

Все 621 исходник побайтово сопоставлены с Git-объектами среза TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. Расхождений нет; SHA256 последовательности `путь + NUL + содержимое + NUL` в порядке реестра: `9de49bf9b75194490fcfd7bfc80e2b1c8bcd9d90dd26f3603faf21d92b3d0e1e`.

### Документы и ограничения

Созданы TASK-0003.011–TASK-0003.020 со статусом planned. Для каждой определены полные перечни, назначение проверки, исходные точки зависимостей, границы, ожидаемые материалы и перекрёстная сверка. Обновлены родительская задача, указатели задач/аналитики, README и CHANGELOG; в README исследования уточнён согласованный ориентир размера порций.

Фактическое покрытие осталось **72 из 621**, не разобраны **549**. Из них 96 поставлены в очередь и 453 ещё не распределены. При завершении серии покрытие составит 168, остаток — 453; это прогноз, а не результат анализа. TASK-0003 остаётся in-progress; TASK-0004/0005 — draft. Новые issues не создавались, все 56 прежних остаются potential.

Исходники, данные, реестр файлов и прежние карточки при планировании не изменяются. Изолированные методы, браузер и мир не запускались. Исторические записи журнала ниже сохранены без редактирования.

Заключительная проверка документации: проверены 180 Markdown-файлов и 4235 локальных ссылок, структура таблиц, статусы и совпадение списков задач с реестром. `git diff --check` прошёл. Изменены 17 Markdown-документов: десять новых задач и семь связанных документов. Содержимое всех 621 исходника сохранено; mode/uid/gid/inode всех 848 ранее отслеживаемых файлов совпадают с замером перед изменениями. Ветка и HEAD не изменены.

## TASK-0003.010

Дата: 2026-09-10. Ветка rusbar-main, HEAD `247d3d86e344238a1445377c686eb6455146693c`. На старте рабочее дерево чистое, отслеживались 834 файла. Все 621 исходник совпадают со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. Ядро Foundry 14.367.0 проверено локально, Node 24.16.0.

### Полный охват порции

| Файл | Логических строк |
| --- | --- |
| [module/activeEffect/WitcherActiveEffectSheet.js](../../../module/activeEffect/WitcherActiveEffectSheet.js) | 141 |
| [module/activeEffect/mixins/baseMixin.js](../../../module/activeEffect/mixins/baseMixin.js) | 172 |
| [module/activeEffect/mixins/temporaryItemImprovementMixin.js](../../../module/activeEffect/mixins/temporaryItemImprovementMixin.js) | 27 |
| [module/actor/sheets/mixins/activeEffectMixin.js](../../../module/actor/sheets/mixins/activeEffectMixin.js) | 101 |
| [templates/dialog/activeEffects/wizard.hbs](../../../templates/dialog/activeEffects/wizard.hbs) | 3 |
| [templates/sheets/activeEffect/system-specific.hbs](../../../templates/sheets/activeEffect/system-specific.hbs) | 11 |
| [templates/partials/effect-part.hbs](../../../templates/partials/effect-part.hbs) | 53 |
| [templates/sheets/actor/partials/character/tab-effects.hbs](../../../templates/sheets/actor/partials/character/tab-effects.hbs) | 60 |
| Всего | 568 |

Разобраны четыре JS и четыре HBS. У WitcherActiveEffectConfig четыре собственных метода, три static-конфигурации и два Object.assign; baseMixin содержит восемь методов, temporaryItemImprovementMixin — два, activeEffectMixin — четыре. Класс и методы описаны без приписывания им наследуемого submit/вычисления бонусов. HBS не имеют собственных JS-функций. Tab-effects использует CRLF; исходники не перезаписывались.

### Интерфейс, обработчики, схемы и применение

| Связь | Установленный результат |
| --- | --- |
| registerSheets → ActiveEffectConfig | Системный класс зарегистрирован по умолчанию без ограничения types; наследует ядровые стандартные части формы, добавляет systemSpecific и wizard. |
| Wizard → selects | base: 20 stat + 1 toxicity + 6 групп навыков + 52 навыка + 6 lifepath + 3 other + 21 damage = 109 вариантов. Без damageTypeModification у источника — 88. Temporary: 3 пути строковых полей WeaponData. |
| Группы → пути | all/melee/ranged/magic/verbal/empathetic: 52/5/3/3/7/6. После раскрытия групп base-мастера 179 вхождений: commonspeech не разрешается дважды, strong/joint разрешаются в SchemaField; остальные пути — поля CharacterData. |
| selectOptions → callback | Core selectOptions/prepareSelectOptionGroups преобразуют массив value в строку через запятую; wizardAction делит её и добавляет {key}. У шаблона только select#path: ни значения/операции, ни флага потолка. |
| Wizard → update → phase | Мастер берёт подготовленную document.system.changes, не форму. update({changes}) мигрируется cleanData в system.changes; type/value/phase получают defaults. _preUpdate при отсутствии флага в payload выбирает initial (уточнение issue-00043). |
| Автодополнение → реестр | schema.apply обходит 4 модели Actor либо 22 Item, исключая SchemaField; fieldPath уже содержит system. Выбор реестра по parent.documentName не учитывает transfer/type эффекта — issue-00051. |
| Системная вкладка → модели | Base Item: пять флагов; Actor: applyAfterCalculations; temporary Item: два флага. Безусловный formGroup applyAfterCalculations у temporary получает undefined, пишет ошибку и возвращает пустой фрагмент. |
| Контекст частей ядра | Core details устанавливает isItemEffect; HandlebarsApplicationMixin использует общий изменяемый контекст частей. Поэтому обычный полный рендер передаёт флаг в systemSpecific; отсутствие этого флага во всём UI не заявляется. |
| Actor-лист → категории → partial | V2 и V1 подключают activeEffectMixin, вызывают prepareActiveEffectCategories и activeEffectListener(DOM). Приоритет групп: isDisabled → непереданное улучшение → isTemporary → passive. Suppression фильтруется позднее в partial при @root.actor. |
| Действия → документы | create задаёт icon/origin/duration.value/disabled, без type; edit/toggle разрешают реального родителя по UUID, delete блокирует чужой parentUuid. Item-конфигурация использует собственные actions и задаёт type улучшения явно. |
| Описание → listener | Actor listener раскрывает непустое .effect-description через invisible. Item-конфигурация использует тот же partial, но соответствующий обработчик в module/item/sheets не найден. |
| Травмы → вкладка → обработчики | Оба V2-листа используют tab-effects; criticalWoundMixin обслуживает add/treat, itemMixin — daysHealed. Включён crit-wounds-table, затем повторён тот же цикл; одна травма выводится дважды. |
| Шаблон → реальные потребители | wizard: лист + chooseSkill; system-specific: PARTS листа; effect-part: tab-effects, monster-sheet V1, Item activeEffectConfiguration; tab-effects: Character/Monster V2 и preload. |

### Выполненные способы проверки и ограничения

Применены `rg` по точным именам методов/полей/путей, полное чтение восьми файлов и связанных определений, `git ls-files -z`, сопоставление реестра с деревом и побайтовое сравнение исходников с HEAD/срезом TASK-0001. Прямые относительные imports проверены до существующего файла определения и его явного упоминания в карточке.

Для спорных ветвей выполнен Node stdin-сценарий с assertions. Загружены настоящие common primitives, поля, DataModel/TypeDataModel, BaseActiveEffect, обе модели эффекта, все 4/22 зарегистрированные модели Actor/Item и исходные JS этой порции. Для ядрового ActiveEffectConfig использовано исходное тело с малым базовым классом; действия сохранения, prompt, DOM, jQuery и UI подменены. Проверка BaseActiveEffect.cleanData использует те же migrate/sanitize/partial параметры, что прочитанный ClientDatabaseBackend перед _preUpdate.

Настоящие Handlebars, selectOptions, prepareSelectOptionGroups и formGroup использованы из установленного ядра; создание DOM select и toFormGroup существующих полей заменены фасадами. Отсутствующее поле обработано настоящим formGroup. HTML вкладки разобран установленным parse5. Полный браузер, мир, БД и реальный submit/сетевые запросы не запускались.

Проверенные внешние участки:

- /opt/foundryvtt/client/applications/sheets/active-effect-config.mjs: части формы, контекст, стандартные addChange/deleteChange, обработка value/phase/priority и submit.
- /opt/foundryvtt/client/applications/api/handlebars-application.mjs: общий контекст частей, options.parts и рендер.
- /opt/foundryvtt/client/applications/handlebars.mjs и /opt/foundryvtt/client/applications/forms/fields.mjs: formGroup, selectOptions и группы вариантов.
- /opt/foundryvtt/templates/sheets/active-effect/changes.hbs и change.hbs: кнопка addChange, ключ/тип/значение/priority, скрытая phase.
- /opt/foundryvtt/client/data/client-backend.mjs и /opt/foundryvtt/common/documents/active-effect.mjs: очистка/миграция частичного update.
- /opt/foundryvtt/common/data/fields.mjs: fieldPath/schema.apply; /opt/foundryvtt/client/documents/active-effect.mjs: разрешение пути system.* и применение.

| Выполненный сценарий | Фактический результат | Предел проверки |
| --- | --- | --- |
| Настоящие модели и все варианты мастера | 109/88 base-вариантов, 3 temporary; 179 вхождений путей, два отсутствующих commonspeech и два объектных attacks; три Item-пути — StringField | Проверка схемы не заменяет все игровые операции с полями |
| Автодополнение Actor/Item | 718/701 уникальных ключей; все имеют system. Item base transfer=true предлагает system.damage, но не system.stats.ref.totalModifiers | DOM datalist подменён, schema.apply настоящий |
| Мастер, исходный value=1, несохранённое значение9, выбор двух путей | Payload сохраняет1, добавляет два {key}; prepared длина1→3, _source остаётся1; callback не ждёт update | Форма/prompt/запись подменены; потеря текста на реальном экране не наблюдалась |
| Очистка payload мастера и hook | Корневой changes стал system.changes; defaults add/пустая строка/initial; прежний applyAfterCalculations=true не учитывается _preUpdate | Настоящая очистка и исходный hook, без БД |
| Два _onRender на сохранённом DOM | 2 wizard-кнопки и 2 datalist с одинаковым id | Сценарий повторного/частичного рендера; полного браузерного инициатора не устанавливали |
| Форма base и temporary | 5 input без ошибок; 2 input и 1 console.error отсутствующего поля соответственно | Настоящий formGroup, facade для существующих input |
| Рендер wizard | Строка массива путей с запятыми; группы поддерживаются ядровым helper, checkbox нет | Настоящий helper и Handlebars, DOM обёртка подменена |
| Категории и четыре действия Actor | a inactive, b improvement, c temporary, d passive; create value1, edit render(true), toggle true→false, своё удаление, чужое уведомление | Документный API подменён |
| Listeners/описание/suppression | Зарегистрированы .effect-control и .effect-display click; непустое описание переключает invisible; suppressed-строка скрыта при actor | DOM/jQuery doubles |
| Одна травма в обоих исходных partial | parse5 нашёл 2 строки data-item-id и 2 кнопки лечения; enriched выведен новым циклом | Дублирование разметки, не документов/выполнения лечения |

Итоговый сценарий завершился с exit 0 и пройденными assertions. Предварительное предположение об отсутствующем system. в автодополнении опровергнуто настоящими моделями; оно не зарегистрировано как проблема. Недостающие глобальные значения и DOM-контекст исправлялись только в изолированном окружении, исходные функции не менялись. Предупреждение Node о MODULE_TYPELESS_PACKAGE_JSON не устранялось изменением package.json.

### Заключительная сверка первой серии с TASK-0002

| Порция | Файлов | Прямых относительных imports | Проверенная граница связи |
| --- | --- | --- | --- |
| TASK-0002 | 11 | 84 | Манифест/точка входа → конфигурация, регистрации моделей/листов/hooks/helpers/Queries |
| TASK-0003.001 | 5 | 2 | Общие поля/характеристики → вложенные модели и пути totalModifiers |
| TASK-0003.002 | 9 | 14 | Навыки → группы/CharacterData → 52 пути мастера и issue-00004 |
| TASK-0003.003 | 8 | 2 | Данные состояния → общая модель Actor и потребители, включая effects |
| TASK-0003.004 | 8 | 8 | Биография/изменение урона → common Actor → подсказки и реальные типы полей |
| TASK-0003.005 | 7 | 3 | Журналы/обучение/панели/атаки → специализированные модели и пути attackStats |
| TASK-0003.006 | 4 | 21 | Сборка Actor-моделей → CONFIG.Actor.dataModels → schema.apply |
| TASK-0003.007 | 2 | 19 | Документ Actor/примеси → перечисление эффектов, подготовка и применения фаз |
| TASK-0003.008 | 2 | 8 | CommonItemData/Item → реестр 22 моделей, временные улучшения и список эффектов |
| TASK-0003.009 | 8 | 2 | Документ/модели/маршруты ActiveEffect → поля формы и payload мастера |
| TASK-0003.010 | 8 | 2 | Конфигурация/мастер/partials → поля, listeners и документные действия |
| Всего | 72 | 165 | 61 уникальный файл первой серии + 11 файлов TASK-0002, без повторного учёта |

Для всех 72 карточек проверены состав, наличие исходника, применимость версии и прямые импорты: 165 обращений разрешаются в существующие файлы, явно указанные в соответствующей карточке. Чтение зависимостей не присваивает им статус «Проверено». Уточнены десять ранее созданных карточек (регистрации листов/helpers/config, документ Actor/Item/ActiveEffect, две модели эффекта, statData и lifepathData).

Эта заключительная сверка не является повторным исполнением всех поведенческих сценариев прежних порций и не закрывает TASK-0004/0005. Сохранены следующие точные границы дальнейшего исследования:

| Непроверенная целиком связь | Файлы/способ продолжения |
| --- | --- |
| Полные листы Actor и Item, частичный рендер и права | WitcherActorSheet/V1, WitcherCharacterSheet, WitcherMonsterSheet, WitcherItemSheet и configurations/WitcherConfigurationSheet: полностью разобрать классы/наследование/actions, затем согласовать браузерные сценарии. |
| Травмы/лечение/заживление | module/data/item/criticalWoundData.js, actor/sheets/mixins/criticalWoundMixin.js, itemMixin.js и templates/partials/crit-wounds-table.hbs: полностью проследить treat/heal/inline-edit и источники таблиц. |
| Боевые формулы и изменения урона | actor/mixins/weaponAttackMixin.js, defenseMixin.js, damageMixin.js, castSpellMixin.js, armorMixin.js и scripts/combat: проверить полный путь от выбранного поля до формулы/документной записи. |
| Специализированные модели Item | module/data/item/* и templates/combat/*: schema была исполнена для путей, но все методы/подготовка/потребители этих файлов не разобраны. |
| Общий чат, Queries и реальные клиенты | scripts/chat.js, helper.js, chatMessage/* и отправители: после полного разбора отдельно согласовать проверки реальной доставки, UI и сохранения. |
| Статусы/длительности в мире и statuscounter | Внешнее ядро и /var/lib/foundryvtt/Data/modules/statuscounter: в этой порции модуль не читался, прежнее ограничение доступа сохраняется; реальный scheduler не запускался. |
| Оставшиеся ресурсы | Остальные строки реестра: шаблоны/CSS/локализации/компедиумы/инструменты/конфигурация сборки; 549 файлов ещё требуют порционного полного разбора. |

### Проблемы и итоговая проверка документов

Созданы [issue-00051–00056](../../issues/README.md): схема получателя автодополнения, несохранённая форма, отсутствующее поле temporary, двойной список травм, повторный рендер элементов и отсутствие раскрытия описания на Item. Дополнены issue-00004/00019/00043. Все 56 проблем остаются potential; исправления и пользовательское подтверждение не выполнялись.

Проверка Python stdin и git diff --check прошла: реестр содержит 621 уникальный файл, 72 проверенные карточки и 549 статусов «Не начат». Для восьми новых карточек проверены 11 обязательных разделов, версия и определения; все 56 номеров issues уникальны и находятся в potential. Проверены 170 Markdown-документов и 3882 локальные ссылки с якорями, структура таблиц и указанные абсолютные пути файлов ядра.

Все 621 исходник побайтово совпадают с HEAD и срезом TASK-0001. Сводная SHA256 содержимого исходников: 9de49bf9b75194490fcfd7bfc80e2b1c8bcd9d90dd26f3603faf21d92b3d0e1e. Mode/uid/gid/inode всех 834 ранее отслеживаемых файлов сохранены; SHA256 метаданных b3614d203db4414d8a569dceb6405361fefb5bcee51047e8fb9cab6b5692c55a. Изменения ограничены 38 Markdown-файлами в docs, включая 14 новых; ветка/HEAD не менялись, коммит не создавался. История журнала начиная с TASK-0003.009 сохранена побайтово.

Первая серия TASK-0003.001–TASK-0003.010 завершена. Общее покрытие — 72 из 621 файла, 549 не разобраны; родительская TASK-0003 остаётся in-progress. Следующие задачи не создавались автоматически. Изменена только документация, исходники/настройки/мир не изменялись.

## TASK-0003.009

Дата: 2026-09-10. Ветка rusbar-main, HEAD `a33bf33add228ae93f96a52046c8feb4ee992921`. Рабочее дерево на старте чистое; отслеживались 818 файлов. Все 621 исходник совпали со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. Локальное ядро Foundry 14.367.0 проверено по /opt/foundryvtt/package.json; Node 24.16.0.

### Порция и содержательная сверка

| Полностью прочитанный файл | Логических строк | Проверенный состав |
| --- | --- | --- |
| [witcherActiveEffect.js](../../../module/activeEffect/witcherActiveEffect.js) | 120 | Класс: четыре геттера, три async-метода; ссылка DialogV2 |
| [witcherActiveEffectData.js](../../../module/data/activeEffects/witcherActiveEffectData.js) | 29 | defineSchema, пять BooleanField и унаследованные changes |
| [witcherTemporaryItemImprovementData.js](../../../module/data/activeEffects/witcherTemporaryItemImprovementData.js) | 22 | metadata.type, defineSchema, три BooleanField и унаследованные changes |
| [temporaryEffectMixin.js](../../../module/actor/mixins/temporaryEffectMixin.js) | 62 | Объект примеси, один async-метод выбора оружия/передачи |
| [applyActiveEffect.js](../../../module/scripts/temporaryEffects/applyActiveEffect.js) | 80 | Три export async, одна локальная async-функция; импорт getActorOwner |
| [applyStatusEffect.js](../../../module/scripts/statusEffects/applyStatusEffect.js) | 84 | Пять export и одна локальная функция; импорты getActorOwner/getCurrentCharacter |
| [appliedTemporaryItemImprovements.hbs](../../../templates/chat/item/appliedTemporaryItemImprovements.hbs) | 15 | Контекст item/temporaryItemImprovements, each, img/name, localize |
| [statusEffect.hbs](../../../templates/chat/combat/statusEffect.hbs) | 3 | Контекст status из turnStartEffects; img/name/localize без событий |
| Всего | 415 | Восемь карточек; HBS без завершающего перевода строки, поэтому сумма wc -l отличается на два |

Внешние определения прочитаны в пределах установления связи. Helper, боевые mixin-файлы, листы, generalCombatHook, ядро и локализации от этого не получили статус полного пофайлового анализа.

| Связь | Фактический результат |
| --- | --- |
| Регистрация ↔ модели | CONFIG.ActiveEffect.dataModels.base / temporaryItemImprovement — два прямых наследника ActiveEffectTypeDataModel. Вторая модель не наследуется от первой. fields changes ядра: key/type/value/phase/priority; начальные add/initial/пустая строка, priority undefined до prepareBaseData. |
| Регистрация ↔ документ | TheWitcherTRPG.js назначает documentClass, публикует ViaId и вызывает отдельный chatMessageListeners. isDisabled служит категориям листа; core active читает disabled и isSuppressed. |
| Флаги ↔ применение | applySelf/OnTarget/OnHit/OnDamage подавляют исходный эффект; вызывающие mixin-файлы отбирают их для копирования. isTransferred определяет улучшения в Actor/Item и не тождественен корневому transfer. applyAfterCalculations преобразуется _preUpdate в phase, которую читает ядро. |
| Item ↔ улучшения | Actor-примесь выбирает Item weapon, задаёт origin=Actor.uuid и три system-флага; создаёт его embedded ActiveEffect. Item читает changes у isTransferred. Замена system теряет changes; источник start=null также остаётся без начала отсчёта. |
| Отправители ↔ Queries | getActorOwner выбирает активного владельца/GM; обычный и отдельный запросы улучшений идут разными путями. Generic data обычного эффекта не содержит отдельного duration. Query и обёртки не ждут завершения вложенных операций. |
| Статусы ↔ иммунитеты | applyStatusEffectToActor — отдельная функция от WitcherActor.applyStatus. statusEffectImmunities определены у MonsterData; counter вызывается после toggle и до таймера иммунитета. |
| Шаблон улучшений ↔ renderer | Единственный найденный renderTemplate в temporaryEffectMixin; передаёт подготовленный temps, не созданные документы. Запись оружия не ожидается перед сообщением. |
| Шаблон статуса ↔ renderer | Единственный найденный renderTemplate в generalCombatHook.applyCombatEffect; контекст — status из turnStartEffects с heal/damage. Шаблон ничего не применяет; a.apply-status отсутствует в обоих шаблонах. |
| Слушатели ↔ HTML | Рабочий hook отдельного сообщения ищет a.apply-status. Производители: spellItem.hbs (status/duration) и damageUtilMixin.js (status). Внутренних вызовов addStatusEffectChatListeners в module/templates/packsJson не найдено. |

### Источники и выполненные способы проверки

Использованы `git status --short`, `git rev-parse HEAD`, `git ls-files -z`, `rg -n` по именам функций/полей/шаблонов, полное чтение восьми исходников и связанных тел. Состав реестра сопоставлен с Git и фактическим деревом с согласованными исключениями; каждый включённый файл побайтово сравнен с HEAD и срезом TASK-0001.

Для существенных ветвей выполнен Node stdin-сценарий с assertions. Исходный applyActiveEffect.js импортирован как ES-модуль. Для отдельных hooks/методов тела извлечены без изменения алгоритма; parent/super и глобальные зависимости заданы явно. Загружены настоящие primitives, fields, DataModel, TypeDataModel, ActiveEffectTypeDataModel, BaseActiveEffect и Document ядра, обе системные модели и WITCHER. Common-модули разрешались через Node registerHooks. Вместо полного Actor использован малый объект с прототипом BaseActor и явно заданными свойствами; создание документов, query, выбор, чат и таймеры перехватывались. Это не запуск клиента Foundry.

Проверенные внешние определения:

- /opt/foundryvtt/common/data/active-effect.mjs — схема changes; /opt/foundryvtt/common/data/fields.mjs — поля и нормализация.
- /opt/foundryvtt/common/documents/active-effect.mjs — schema, common _preCreate, legacy migration/shimData; /opt/foundryvtt/common/abstract/document.mjs — clone и toObject.
- /opt/foundryvtt/client/documents/active-effect.mjs — active/isSuppressed/isTemporary/isExpiryTrackable, подготовка changes, getEffectStart и hooks.
- /opt/foundryvtt/client/documents/actor.mjs — применимые эффекты/фазы и toggleStatusEffect; /opt/foundryvtt/client/documents/combat.mjs — getCombatantsByActor.
- /opt/foundryvtt/client/helpers/active-effect-registry.mjs — допуск к отслеживанию и обработка expiryAction; /opt/foundryvtt/client/documents/abstract/client-document.mjs — порядок подготовки.
- /opt/foundryvtt/node_modules/handlebars/lib/index.js — настоящий компилятор двух шаблонов; localize подменён функцией, возвращающей L:ключ либо пустую строку.

### Изолированные сценарии и результаты

| Сценарий и вход | Фактический результат | Предел проверки |
| --- | --- | --- |
| Начальные system двух моделей, запись changes с key | Base: changes=[] и 5 false; temporary: changes=[] и 3 false. Новая change: type=add, phase=initial, value='', priority не сериализуется | Настоящие модели и схема; без серверного сохранения |
| Обычный эффект value=5, units=rounds; запрошены undefined/0/2 | source и clone остаются value=5. Подготовленный duration.rounds получил 0/2, но source не изменился | Настоящие BaseActiveEffect/clone; Actor.createEmbeddedDocuments подменён |
| Вход effect.toObject и JSON-roundtrip | Прямой toObject даёт TypeError при записи getter-only rounds; JSON-данные с modern value=5 тоже дают копию value=5 при запросе 2 | Различены формы аргумента; реальная сеть не моделируется сериализатором |
| Контролируемый pending create; ToTargets/ViaId/прямой owned | Обёртки возвращаются при одной pending записи; прямой owned ждёт обычную запись; улучшения не ожидает | Управляемые Promise, без сетевых задержек |
| !actor.isOwner | Записаны два query: отдельный со всем списком и общий с UUID/обычными эффектами без третьего duration | Получатели/query подменены |
| Отсутствующий Item, три ручных приёма ViaId | Три одинаковых повторных запроса GM | Не автоматический и не реальный бесконечный цикл |
| Матрица active/isDisabled | Обычный true/false; disabled false/true; equipped=false false/true; isActive=false false/false; каждый apply-флаг true даёт false/false; expired=true сам по себе true/false | Исходные геттеры + core active; registry может удалять отслеживаемые эффекты отдельно |
| Частичный _preUpdate | name-only проходит; system без changes → TypeError forEach; changes-only при прежнем applyAfterCalculations=true → initial; changes+true → final; super=false прекращает обработку | Метод с малым super-контекстом; полная форма UI не запускалась |
| _preCreate: текущий ход1, turnNumber0/1/2, expiryStart/End, value2 | Длительности 2/2/2/1/1/1; найденному Actor-combatant назначается start.combatant | Исходный метод; Combat API и контекст заданы явно |
| _preCreate Item и начало отсчёта | С start.combat и Item-родителем getCombatantsByActor не находит Actor-комбатанта; updateSource получает {}. При start=null он не инициализируется | Тело getCombatantsByActor — из ядра; не полный lifecycle |
| @skill и выбор swordsmanship | 52 варианта; ключ стал system.skills.ref.swordsmanship.activeEffectModifiers; прочие поля/ключи сохранены; отмена отклоняет Promise | Исходный chooseSkill, WITCHER, подмены render/prompt |
| Исходный документ улучшения: одна changes, start=null, duration3rounds | Передатчик создаёт system только с тремя флагами; настоящая модель нормализует changes=[]; start остаётся null. Чат запущен, запись оружия ещё pending | Источник и нормализация — настоящие; UI/запись/чат подменены |
| Цепочка common/client/system preCreate Item-улучшения, persisted=true | start=null, active=true, temporary=true, isExpiryTrackable=false | Исходные hooks/getters в малой цепочке наследования; полный scheduler не выполнялся |
| Улучшение без weapon; отдельно отмена выбора | Принятый пустой выбор → TypeError чтения name; отмена → rejection | Prompt-подмена; реальный диалог не запускался |
| Статус отсутствует / уже активен / Actor или ID отсутствует | Один toggle / ноль / ноль; активному статусу срок не обновляется | Коллекции Actor заданы явно |
| Статус fire disabled в effects, appliedEffects пуст | Оригинальный core toggle вызывает deleteEmbeddedDocuments с disabled-fire | Исходное ядро; запись перехвачена |
| Иммунитет, statuscounter выключен | Один toggle, таймер 1000 ms; при ручном запуске callback второй toggle | Таймер перехвачен |
| Иммунитет, statuscounter включён, duration='2' | Один toggle, TypeError CONFIG.WITCHER.statusEffects.querySelector is not a function, таймеров 0 | Сам API модуля не достигнут |
| Чат: отдельный listener, нет текущего Actor, пакетный listener | click зарегистрирован; onApplyStatus читает uuid у undefined; пакетный export падает на .each | Минимальные DOM doubles; не браузер |
| Компиляция двух HBS с фактическими полями | Выведены имена и img; у improvement effect.statusEffect.name отсутствует, mock localize даёт пустой span. Ссылок a.apply-status нет | Настоящий Handlebars, подмена localize; не проверка оформления |

Итоговый Node-сценарий завершился с exit 0 и пройденными assertions. Предупреждение MODULE_TYPELESS_PACKAGE_JSON относится к способу импорта в Node; package.json не изменялся. Во время подготовки минимального окружения корректировались только подмены и ожидания тестового сценария, не исходные функции.

### Проблемы и границы

Зарегистрированы восемь карточек [issue-00043–00050](../../issues/README.md): частичный update/phase, длительность копии, повторная пересылка отсутствующего Item, отсутствие оружия, отсутствие Actor при клике, DOM/jQuery пакетного слушателя, переключение disabled-статуса и start улучшения. Дополнены issue-00003 (ошибка до таймера иммунитета), issue-00008 (ожидание маршрутов) и issue-00042 (настоящая нормализация потери changes). Все 50 проблем остаются potential; исправления и пользовательское подтверждение не получены.

Чтение /var/lib/foundryvtt/Data/modules/statuscounter завершилось Permission denied. Права не менялись; версия и API самого модуля остаются неизвестными. Это не препятствует проверке ошибочного querySelector у массива самой системы. Не выполнялись запуск мира/браузера, запись в БД, реальные Queries, настоящие таймеры боя и полное истечение эффектов. expiryAction=delete и реестр ядра существуют; вывод о бессрочности всех эффектов не делался.

Уточнены девять ранее созданных карточек: TheWitcherTRPG.js, registerDataModels.js, queries.js, config.js, hooks.js, WitcherActor, WitcherItem, combatEffectsData и MonsterData. Новые карточки сохраняют точные источники, потребителей, используемые поля и ограничения; интерфейс/wizard остаётся TASK-0003.010.

### Итоговая техническая сверка

Проверка Python stdin + git diff --check прошла: 621 строка реестра без повторов, 64 карточки и 557 статусов «Не начат»; точный состав порции — восемь файлов и 415 логических строк. У восьми карточек проверены все 11 обязательных разделов, собственные определения класса и поля схем. Реестр issues содержит 50 уникальных номеров, все в potential. Проверены 156 Markdown-документов и 3663 локальные ссылки, включая якоря; таблицы и существование указанных файлов ядра проверены.

Все 621 исходник побайтово совпадают с HEAD и срезом TASK-0001. Контрольная сумма содержимого реестра исходников: 9de49bf9b75194490fcfd7bfc80e2b1c8bcd9d90dd26f3603faf21d92b3d0e1e. Mode/uid/gid/inode всех 818 ранее отслеживаемых файлов сохранились (сводная SHA256 cb2f382166a97e7554c6ea3772b57a10267a94b4e1b6f0f4c5efd589fd4ac2a0). Изменения ограничены 39 Markdown-файлами в docs, включая 16 новых. История журнала начиная с TASK-0003.008 сохранена побайтово; ветка и HEAD не изменились.

Покрытие: 64 карточки проверены, 557 файлов не разобраны. В первой серии TASK-0003 выполнены 53 из 61 файла; осталось 8 в TASK-0003.010, за пределами серии — 549. Родительская TASK-0003 остаётся in-progress, TASK-0003.009 — done. Исходники, мир и настройки системы не изменялись.

## TASK-0003.008

Дата: 2026-09-10. Ветка rusbar-main, HEAD `c5edcbadd05ff4038a174bd2e2a49785e40ea878`. Рабочее дерево на старте чистое, отслеживались 810 файлов. Все 621 исходник совпали со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. Проверено локальное ядро Foundry 14.367.0 (/opt/foundryvtt/package.json), Node 24.16.0.

Полностью прочитаны [CommonItemData](../../../module/data/item/commonItemData.js) — 29 строк и [WitcherItem](../../../module/item/witcherItem.js) — 376 строк, всего 405. Созданы две карточки. Чтение определений в наследниках, примесях, листах и ядре служит проверкой связи, а не завершением пофайлового анализа этих файлов.

### Содержательная и перекрёстная сверка

| Направление | Фактический результат |
| --- | --- |
| Реестр моделей ↔ наследование | 22 типа Item: CommonItemData как base, 16 прямых наследников и 5 независимых TypeDataModel. Восемь общих полей не приписаны независимым моделям. |
| CommonItemData ↔ поля | description/quantity/sourcebook — StringField; weight/cost — NumberField; isHidden/isStored/isCarried — BooleanField. quantity='1'; isCarried=true; остальные initial перечислены в карточке. |
| Масса ↔ потребители | 3×2=6; hidden оставляет 6, stored или !carried дают 0. '1d6'×2=NaN, '-2'×2=-4. Container 2×3+7=13. Actor.getTotalWeight делегирует calcWeight, экспорт монстра отдельно вычисляет quantity через Roll. |
| Возможности ↔ интерфейс | Базовые canHaveTemporaryItemImprovement/canBeRepaired=false; первое переопределено true у Alchemical/Valuable/Spell, второе условно у Armor/Weapon. Первое управляет созданием источника улучшения в шаблоне, не запретом оружию принять эффект. |
| Item ↔ собственные определения | Два static, десять собственных определений прототипа (включая два getters и generator), локальный AlchemyComponent с четырьмя полями/constructor; все методы описаны. Восемь импортов, из них RollConfig нужен только JSDoc. |
| Примеси ↔ прототип | Пять Object.assign в порядке consume, repair, dismantling, damageUtil, defenseOption; 11 уникальных имён, без пересечения с собственными методами. Проверены все определения, полный алгоритм каждой примеси не заявлен. |
| Атака ↔ модель/потребители | Set сохраняет порядок; без клавиш индекс0, shift1/alt2/ctrl3 с ограничением size-1 и приоритетом ctrl. Два варианта+ctrl→второй. Отсутствующий Set→none; пустой Set→undefined option/skill/alias. WeaponAttack и castSpell сверены до места вызова. |
| Миграция ↔ класс | Исходный migrateSpells меняет source.type для Hexes/Rituals, затем migrateData делегирует родителю; system.class сохраняется. Проверка с минимальным родителем не считается миграцией настоящего Item ядром. |
| Алхимия ↔ UI | Девять строк getter alchemyCraftComponentsList: vitriol, rebis, aether, quebrith, hydragenum, vermilion, sol, caelum, fulgur. _alchemyCraft вызывает отсутствующее populateAlchemyCraftComponentsList; исходный обработчик получил TypeError. Issue-00037. |
| Изготовление ↔ Promise | realCraft + extendedRoll исполнялись с контролируемым Roll. После await realCraft removeItem/addItem/toMessage оставались pending; инициирование операций не обеспечивает порядок завершения. Issue-00038; Actor.addItem/removeItem сами ждут свою запись. |
| Изготовление ↔ сообщение | Успешный бросок 11 при DC 10, требование 3 при доступных 2: ошибка о компонентах, нет списания/выдачи, но сообщение success=true с текстом успеха. Issue-00041; вход может моделировать устаревшую проверку листа. |
| Таблицы ↔ коллекции | Поиск в индексах компедиумов RollTable по имени Item; game.tables не используется. Core .roll допускает [] и несколько результатов. [A,B] обработан только как A, затем генератор удалён; [] вызвал TypeError. Issue-00039. |
| Количество добычи ↔ запись | Два результата A в существующую стопку quantity='1' с отложенным update дали патчи 2 и 2; после применения итог 2 вместо 3. Генератор удалён до завершения обоих update. Issue-00040. |
| Legacy API ↔ ядро | ActiveEffect.apply, TableResult.documentCollection/documentId/getChatText ещё существуют в 14.367 и выдают compatibility warning; отсутствие современной формы не объявлено автоматической поломкой. |
| Item ↔ подготовка эффектов | После super.prepareEmbeddedDocuments система применяет активные system.isTransferred эффекты одним проходом, до system.prepareDerivedData; phase/shouldApplyChange здесь не проверяются. Подготовка priority ядром и fallback mode*10 разделены. |
| Арифметика ↔ source | Реальный CommonItemData.weight 8, change multiply0.5(final)/priority10 и add2(initial)/20 → weight 6; sourceWeight 8; overrides.system.weight 6. Disabled исключён, isTransferred=false не включён. Подменены родитель документа и static dispatcher, но не исходная арифметика поля. |
| Передача ↔ получатель улучшения | Исходный applyTemporaryItemImprovements передал createEmbeddedDocuments объект system из трёх флагов, без changes. Источник имел одну запись, она сохранилась во входе, но потерялась в запросе. Issue-00042; полный lifecycle эффекта остаётся TASK-0003.009. |
| Локализация ↔ строки | Все 16 уникальных буквальных ключей game.i18n.localize из WitcherItem найдены в en.json и ru.json. Проверено наличие, а не качество переводов. Девять asset-путей прочитаны как ссылки вне объёма анализа; HTTP не проверялся. |
| Двусторонние карточки | Уточнены восемь карточек: TheWitcherTRPG.js, registerDataModels.js, queries.js, config.js, registerSheets.js, handlebars.js, dataUtils.js, witcherActor.js. Связи схемы, документа, отображения и действий разделены; добавлены обратные ссылки. |
| Issues ↔ область | Зарегистрированы issue-00037–00042; дополнены issue-00008/00034. Все 42 остаются potential; задачи исправления не создавались. |

### Команды и изолированные сценарии

Перед порцией: git status --short, git rev-parse HEAD, git branch --show-current, git ls-files -z. Python сохранил SHA256 содержимого 621 исходника по путям registry и mode/uid/gid/inode 810 отслеживаемых файлов. В конце байты каждого исходника сопоставлены с git show HEAD:<path> и git show 15da5b225535e34af4e132c701b5353ef4eb667f:<path>. Полное чтение исходников через cat/nl, rg по точным определениям, всем наследникам и потребителям в module/templates/packsJson, по нужным методам установленного ядра. Python сверил 16 ключей локализации в en/ru.

Сценарий `node --input-type=module` передан через stdin, файл стенда не создавался. Загрузил настоящие primitives, DataModel, TypeDataModel, fields, utils из /opt/foundryvtt/common, а также исходные CommonItemData, ContainerData, AlchemicalData, ValuableData, DiagramData и WITCHER. Локальный registerHooks разрешал alias @common. Для выполнения WitcherItem и пяти примесей в vm сняты только import/export-обёртки; тела методов и Object.assign сохранены. Родитель ItemBase заменял migrateData и prepareEmbeddedDocuments минимальными функциями; его Item.create перехватывался. Поэтому это не запуск настоящего lifecycle Item или его БД.

Использованы оригинальные RollConfig и extendedRoll. Roll — управляемый объект с total=11, dice=[], options, evaluate→self; RNG, критические броски и настоящая отправка сообщений не запускались. game.i18n/settings, коллекции pack/table/Actor.items, fromUuid, create/update/delete, notifications, ChatMessage и Dialog заменены. Для realCraft заданы recipe/result UUID, количество компонентов 2 и требование2/3, DC 10; Promise списания/выдачи/сообщения разрешались вручную. Для таблицы результаты [A,B], [], дважды A и newQuantity0 проверены отдельно; повторная запись существующей стопки откладывалась до конца метода. Ожидаемые результаты — существование обоих результатов, увеличение1+1+1=3 и ожидание вложенной записи — не вычислялись исследуемыми методами.

Исходный _alchemyCraft извлечён из WitcherCharacterSheet целиком: предметом был оригинальный WitcherItem с настоящей DiagramData, DOM target и ChatMessageData — двойники. Получена ошибка до открытия Dialog. Поиск старого имени подтвердил, что в системе есть один вызов и нет определения; исходный getter дал девять ожидаемых веществ.

Для Item-эффектов использованы исходные WitcherActiveEffect getters, core ActiveEffect.active, совместимый apply и applyChangeField. Static applyChange заменён адаптером выбора настоящего поля и вызова исходного applyChangeField; сама DataField.applyChange/арифметика не подменялись. Effects — управляемые объекты, не полные документы ядра. Вход expandObject приведён через JSON к обычному объекту основного контекста, затем обработан настоящим utility, чтобы сравнение plain object между vm-контекстами не искажало структуру overrides. Приоритеты/type/phase переданы явно, автоматическая миграция legacy changes не моделировалась. Исходный applyTemporaryItemImprovements отдельно выполнил выбор оружия через двойник Dialog и передал перехваченный запрос создания эффекта.

Первый прогон дошёл до передачи улучшения и остановился из-за отсутствующего CONST в окружении сценария; добавлен явный двойник только CHAT_MESSAGE_STYLES.OTHER, исходники системы не менялись. Исправлен межконтекстный вход expandObject; итоговый прогон со всеми утверждениями завершился с exit 0. Отдельный сбор JSON-вывода сначала натолкнулся на предупреждение Node после объекта; парсер результата уточнён, это не ошибка исследуемой системы. Node выдал MODULE_TYPELESS_PACKAGE_JSON для ES modules; package.json не менялся.

```text
Common schema:8; direct subclasses:16; independent registered models:5; Item types:22
Lines:29+376=405; Item own definitions:12; local AlchemyComponent:4 fields
Mixins:5; mixed methods:11; collisions:0
Common weights:6,6,0,0,NaN,-4; Container weight:13
Attack options:melee,ranged,spell,itemUse; ctrl wins; empty Set has undefined attack
Alchemy UI:TypeError item.populateAlchemyCraftComponentsList is not a function
Craft:remove-start,add-start,message,returned; pending:3
Missing components:available2/required3; no inventory changes; message success=true
Loot [A,B]:create A,deleteGenerator; []:TypeError
Loot stack1 + two draws:update2,update2,deleteGenerator; final2 (expected3)
Item changes:weight 8 -> multiply0.5(final) -> add2(initial) -> weight 6; source8
Transferred effect.system:{isTransferred:true,applySelf:false,applyOnTarget:false}; no changes
```

### Итоговая проверка документов и сохранности

Итоговая сверка пройдена: реестр содержит 621 файл; 56 карточек соответствуют строкам «Проверено», 565 файлов ещё не разобраны. Проверены все 140 Markdown-документов и 3409 локальных ссылок, таблицы и обязательные разделы, точный состав порции (405 строк), восемь полей общей модели, 12 собственных определений Item, 11 методов примесей, 16 наследников и 22 регистрации типов Item. Индекс согласован со всеми 42 потенциальными проблемами; TASK-0003.008 завершена, TASK-0003.009/010 ещё в очереди.

Изменены только 29 документов: 21 существующий и восемь новых. Проверка git diff --check пройдена; все исходники совпадают с HEAD и базовым срезом. Права, владельцы, группы и inode всех 810 отслеживаемых файлов сохранены.

SHA256 621 исходников (path+NUL+bytes+NUL по порядку registry): `9de49bf9b75194490fcfd7bfc80e2b1c8bcd9d90dd26f3603faf21d92b3d0e1e`. SHA256 mode/uid/gid/inode 810 отслеживаемых файлов: `9f32a256fa93f91bfdcfbe3174c4392cae5bd1e46ce02d2df9fec91981652502`. Историческая часть журнала, начиная с TASK-0003.007, сохранена побайтно; текущий HEAD не изменялся.

### Итог и границы

TASK-0003.008 завершена: 56/621 файла, 565 ещё не разобраны. Первая серия — 45/61 файла, осталось 16, вне серии 549. Следующая — [TASK-0003.009](../../tasks/task-0003.009.md). Исходники, сборка, миры, компедиумные БД и права доступа не менялись. Полный клиент, серверные запросы, реальные броски/сообщения и UI не запускались. Политика количеств, расход компонентов и другие игровые правила не утверждались и не исправлялись.

## TASK-0003.007

Дата: 2026-09-10. Ветка rusbar-main, HEAD `b8b89a7e3392235f993c21f3c6d277a4a2e7a55f`. Рабочее дерево на старте чистое; отслеживались 804 файла. Все 621 исходник совпали со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. Локальное ядро Foundry 14.367.0, Node 24.16.0.

Полностью прочитаны [witcherActor.js](../../../module/actor/witcherActor.js) (454 строки) и [modifierMixin.js](../../../module/actor/mixins/modifierMixin.js) (53 строки), всего 507. Созданы две карточки. Полный анализ остальных примесей не заявлен: проверены определения подключаемых имён и тела конкретных потребителей для установления связи.

### Содержательная и перекрёстная сверка

| Направление | Фактический результат |
| --- | --- |
| Класс ↔ определения | 19 собственных определений: getter temporaryEffects, 16 методов экземпляра, два static. 19 импортов; 17 Object.assign после класса. Все перечислены с входами, возвратами и изменениями состояния. |
| Примеси ↔ прототип | Оригинальные 17 объектов содержат 76 свойств/75 разных имён. Единственный повтор — addDefenseModifiers; defenseMixin перезаписывает modifierMixin. Тела совпали; итоговый метод принадлежит defenseMixin. Статические/экземплярные getLocationObject/getAllLocations — разные уровни. |
| Модели ↔ подготовка | 19 общих полей сопоставлены с чтениями/записями Actor; схема не определяется документом повторно. Loot/mystery выходят после super.prepareDerivedData. CommonActorData базовые значения и производные расчёты Actor различены. |
| Ядро ↔ этапы | system.prepareBaseData → Actor.prepareBaseData → вложения/initial эффекты → system.prepareDerivedData → WitcherActor.prepareDerivedData → final эффекты. Собственный порядок stats→fixed→stats→derived→attacks; applyStatus запускается перед ним без await. |
| Характеристики ↔ ограничения | Восемь значений берутся из unmodifiedMax+модификаторы и floor/делитель. При HP40/7/0, пороге8 и базах8: INT8/4/2, BODY8/8/2. Общего min1/max10 в calculateStat нет. Stun clamp применяется до добавки. |
| Перегруз ↔ расчёт | Оригинальные getTotalWeight/calculateWeigthEncumbrance: масса81, вместимость80→штраф1; REF/DEX из8→6, SPD→7 при нулевой броне. Зарегистрирована potential issue-00035 без заключения о рулбуке. |
| Два прохода ↔ max | Настоящая CharacterData и оригинальный Actor: luck.max10+modifier2→14; toxicity100+5→110. Уточнена issue-00012. |
| Эффекты ↔ фильтрация | Прочитаны исходные allApplicableEffects, active, системный isSuppressed: собственные плюс transfer Item, затем active. В проверке disabled/isActive=false/equipped=false/applySelf/applyOnTarget/applyOnHit/applyOnDamage исключали эффект. |
| Фазы ↔ приоритеты | Числовой пример BODY.max8: multiply0.5/priority10 → add2/20 → переносимый add3/20 =9 в initial; final add1 дал10. Непереносимый Item и disabled/suppressed не внесли добавку. Приоритеты ядра multiply10/add20 прочитаны из constants.mjs. |
| Max ↔ следующий расчёт | Initial multiply0.25 по SPD.max/BODY.max/STA.max:2/2/10; следующий Actor.prepareDerivedData оставил SPD/BODY.value8 и восстановил STA.max40. Такие три пути найдены в JSON Heart Damage. Issue-00036; реальная миграция JSON и игровой packs не запускались. |
| Подписи ↔ формулы | addActiveEffects с +2 и A/B даёт ' +2[A & B]' при details; allSkills=-2 добавляет ' +-2[L:disease]' при обоих значениях настройки. Неизвестный skill→'', неизвестный group→TypeError. Методы читают готовое число, не вычисляют эффекты. |
| Атака/защита ↔ грамматика | Оригинальные modifierMixin/weaponAttackMixin: -2 и0 создают допустимые строки, +2 даёт '8+0 2[L:bonus]' и SyntaxError в оригинальной грамматике/Parser Foundry. Issue-00033. Итоговая защита использует совпадающий метод defenseMixin. |
| Предметы ↔ Promise | AddItem ожидает update/create. RemoveItemsOfType возвращается при pending delete; следующий addItem той же расы обновляет старый предмет quantity2, после завершения удаления остаётся0. UseItem consumable вызывает consume/remove и возвращается при обеих pending операциях. Issue-00034. |
| Списки ↔ поля | Обычный getList исключает stored, shield — нет; масса берётся со всех items через их calcWeight плюс монеты; maxWeight не ограничивает добавление в самом Actor. Особенности описаны, не все объявлены отдельными проблемами. |
| Локации ↔ источники | Проверены восемь фиксированных/неизвестных входов и 20 контрольных случайных исходов. Unknown name сохраняется с параметрами торса. getAllLocations теряет this через обёртку — ранее issue-00032; случайная таблица monster отдельно содержит tailWing. |
| Динамические маршруты | CONFIG.Actor.documentClass, макрос fromUuidSync(...).useItem, query whitelist addItem/две примеси, специальный query улучшений. game.TheWitcherTRPG не найден в module/; есть game.api. AddItem ждёт свою запись, query её не ждёт (issue-00008). |
| Двусторонние карточки | Дополнены 15 связанных карточек (точка входа, queries/config/settings, четыре модели, stat/derived/reputation/attackStats/skill/skills/combatEffects). Данные прошлых проверок сохранены; уточнения имеют текущую версию и обратные ссылки. |
| Issues ↔ результат | Новые issue-00033–00036; дополнены issue-00008/00012/00031/00032. Всего 36, все potential. Исходники и правила не изменены. |

### Команды и изолированные сценарии

Исходный срез: git status --short, git rev-parse HEAD, git branch --show-current, git ls-files -z; Python сверил пути registry с Git/деревом, байты 621 исходника с базовым git show, сохранил hash mode/uid/gid/inode 804 отслеживаемых файлов. Полное чтение 507 строк, rg по всем собственным именам/импортам/потребителям и объявлениям примесей; отдельно проверены system-пути, Queries, игровые макросы, grammar.pegjs и конкретные методы ядра.

Первый сценарий (`node --input-type=module` через stdin, без файла стенда): реальные primitives, DataModel, TypeDataModel, fields, utils из установленного Foundry; настоящие CharacterData/MonsterData и WITCHER. С исходных 17 примесей сняты import/export-обёртки для выполнения в vm, сами тела сохранены. Оригинальный класс WitcherActor выполнен с минимальным родителем ActorBase (пустой prepareDerivedData и контролируемый getter temporaryEffects); Object.assign сохранены. Внешние game.settings/i18n, RNG, документы Item/update/create/delete и сетевые действия подменены. Исполнялись только перечисленные в таблице методы; загрузка определений примеси не считается проверкой всей её логики.

Проверены полная собственная последовательность подготовки, здоровый/раненый/умирающий вход, повтор luck/toxicity, перегруз, getList, строки, локации, ожидание addItem и раннее завершение removeItemsOfType/useItem. Для проверки изменений max используются явные современные числовые changes; это не запуск миграции старого JSON. Для примерной записи первоначально выполнена подготовка CharacterData/Actor до STA.max40, затем применены три изменения и повторно выполнен исходный этап Actor; полный reset/подготовка документа Foundry не имитировались.

Грамматика: peggy из /opt/foundryvtt/node_modules/peggy сгенерировала в памяти parser из исходной /opt/foundryvtt/client/dice/grammar.pegjs. Использован оригинальный /opt/foundryvtt/client/dice/parser.mjs; Node registerHooks разрешал только локальный alias @common. CONFIG.debug.rollParsing=false добавлен в окружение сценария. Не вызывались Roll.evaluate, RNG кубов, ChatMessage и браузер.

Второй сценарий выполнил исходные core Actor.applyActiveEffects/allApplicableEffects, ActiveEffect.shouldApplyChange/active/applyChangeField и системный WitcherActiveEffect.isSuppressed с настоящими полями. Static applyChange подменён небольшим адаптером к оригинальному applyChangeField; _shimChanges — пустым обработчиком для заранее современных type/phase/priority. Замена field.applyChange или арифметики не делалась. Эффекты — управляемые объекты с перечисленными флагами; отдельной модели/коллекции ActiveEffect Document и записей нет. Так проверены выбор фаз, priority, transfer и suppression, а не полный клиент.

Первые прогоны уточняли bootstrap (CONFIG.debug, сравнение объектов разных vm-контекстов, расположение core-методов в одном контексте с helpers); итоговые сценарии завершились успешно. Node выдал MODULE_TYPELESS_PACKAGE_JSON для ES modules системы; package.json не изменялся. Незавершённые Promise двойников не запускали фоновые записи и не держали Node-процесс.

```text
Own definitions:19; mixins:17; mixed properties:76; distinct names:75
Collision: Actor.addDefenseModifiers === defenseMixin.addDefenseModifiers
Preparation: applyStatus, calculateStats, calculateFixedDerivedStats, calculateStats, calculateDerivedStats, calculateAttackStats
HP40/7/0: INT8/4/2, BODY8/8/2
Weight81, capacity80, penalty1: REF6, DEX6, SPD7 (base8)
Luck10+2=>14; toxicity100+5=>110
Skill false:' +2 +-2[L:disease]'; true:' +2[A & B] +-2[L:disease]'
Attack suffix -2:' -2[L:bonus]'; 0:''; +2:' 2[L:bonus]'
Grammar:'8+0 -2[L:bonus]' valid; '8+0' valid; '8+0 2[L:bonus]' SyntaxError
Delete sequence:deleteStarted,awaitReturned,updateOld(quantity2),deleteDone; remaining0
UseItem:consume,remove,returned while operations pending
Initial effect order:multiply0.5,add2,transferred add3 =>9; final add1=>10
Initial max quarter:SPD2/BODY2/STA10; after Actor:SPD.value8/BODY.value8/STA.max40
```

### Итоговая проверка документов и сохранности

Итоговая сверка пройдена: реестр содержит 621 файл, подробные карточки проверены для 54 файлов, анализ 567 файлов ещё не начат. Состав этой порции — два исходника, 507 строк; в карточках сверены все 19 собственных определений Actor, три метода modifierMixin и 17 подключаемых примесей с 76 именами методов (75 уникальных).

Проверены 132 Markdown-документа и 3226 локальных ссылок, структура таблиц, обязательные разделы карточек, статусы задач и соответствие индекса всем 36 потенциальным проблемам. Изменены только 36 документов: 30 существующих и шесть новых. Проверка `git diff --check` пройдена. Содержимое всех 621 исходников совпадает с исходной базой аудита и HEAD; права, владельцы, группы и inode всех 804 отслеживаемых файлов сохранены.

SHA256 621 исходников по порядку registry (path+NUL+bytes+NUL): `9de49bf9b75194490fcfd7bfc80e2b1c8bcd9d90dd26f3603faf21d92b3d0e1e`. SHA256 mode/uid/gid/inode 804 отслеживаемых файлов: `16d99050a898917af2c63175082868d108a724ce96c176da0b4674b8c16cf523`. Предыдущая часть журнала, начиная с TASK-0003.006, сохраняется побайтно. Новые файлы — только Markdown в docs; исходный HEAD не менялся.

### Итог и границы

TASK-0003.007 завершена: 54/621 файла, не разобраны 567; в первой серии 43/61, осталось 18, за её пределами 549. Следующая порция — [TASK-0003.008](../../tasks/task-0003.008.md). Мир, браузер, реальные документы/БД, сетевые Query, полный reset/prepareData и полные боевые примеси не проверялись. Воспроизведения описывают текущий код; ни порядок эффектов, ни правила перегруза, ни компедиумы не исправлялись.

## TASK-0003.006

Дата: 2026-09-10. Ветка rusbar-main, HEAD `fe7ea7420cd4dfa6ee51baf7520f7b0ad8f8b13d`. Рабочее дерево на старте чистое, отслеживались 798 файлов. Все 621 исходник совпали со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. Foundry 14.367.0 по /opt/foundryvtt/package.json, Node 24.16.0.

Полностью прочитаны четыре файла [TASK-0003.006](../../tasks/task-0003.006.md), 275 строк: commonActorData.js134, characterData.js41, monsterData.js75, lootData.js25. Созданы четыре карточки с полным составом верхних полей, всеми собственными методами, наследованием, подготовкой, миграциями, зависимостями и потребителями. Соседние Actor/листы/mixins прочитаны для проверки конкретных обращений, не получают статус «Проверено» за точечный просмотр. Mystery не входит в эту порцию.

### Содержательная и перекрёстная сверка

| Направление | Источник и результат |
| --- | --- |
| Схемы ↔ сборка | Common 19; Character 29=19+10; Monster 53=19+34; Loot 3. У обеих специализаций все общие поля сохранены; Loot наследует TypeDataModel самостоятельно. У монстра нет general/logs/magic/опыта/training. |
| Поля ↔ определения | Все 19 общих, 10 собственных полей персонажа, 34 поля монстра и 3 поля loot связаны с локальным определением либо фабрикой/EmbeddedDataField. Три htmlFields манифеста monster совпали с HTMLField и enrichedText. |
| Регистрация ↔ манифест/листы | Actor.character/monster/loot присутствуют в registerDataModels, system.json и registerSheets. Общий класс не регистрируется отдельным типом. Issue-00005 не относится к отсутствию декларации этих трёх типов. |
| Подготовка ↔ ядро | ClientDocument.prepareData:313–319 вызывает system.prepareBaseData, Actor.prepareBaseData, prepareEmbeddedDocuments (начальные эффекты), system.prepareDerivedData, WitcherActor.prepareDerivedData. Actor.prepareData после super вызывает финальные эффекты. Полный runtime не запускался. |
| Вложенные DataModel ↔ prepareBaseData | Stats/Reputation не получают рекурсивный вызов одноимённого метода через этот путь; копирование максимумов CommonActorData выполняет явно. Подготовка модели не равна миграции source и не пишет БД. |
| Формулы ↔ память | BODY base7/value2, WILL5/3, INT9/4, SPD6/1: stun.base6, run18, leap3, enc70, rec6, woundTreshold6, resolve70, focus21. vigor.max4, reputation.max3. Обычные value не пересчитаны методом Common; исходный снимок модели сохранился; повторный вызов дал тот же результат. |
| Ограничения ↔ назначение | При BODY/WILL0 и20 base stun1/10. Это ограничение одной производной базы; общая политика потолка характеристик этим файлом не вводится. |
| Миграции ↔ условия | Vigor при отсутствующем base не переносится, при base0/value7 становится7, base4 сохраняется. Adrenaline: current3→3, value0/current3→3, value2/current3→2, value0 без current→свойство undefined до очистки. Обнуления meleeBonus/девяти totalModifiers сверены; toxicity/reputation этим методом не обнуляются. |
| Масса ↔ общий потребитель | По одной монете каждого вида:0.007 во всех четырёх моделях. Actor.getTotalWeight прибавляет массу предметов и делает Math.ceil; метод модели не округляет. maxWeight loot по проверенному шаблону управляет индикацией. |
| EnrichedText ↔ helper/формы | Один вызов у персонажа, три последовательных у монстра. Возврат содержит отдельные value/enriched/systemField, реальные пути system.general.background.value и system.common/academicKnowledge/monsterLore. Подменён только TextEditor для проверки передачи. Issue-00013 остаётся ошибкой аргумента формы, не отсутствием enrichment в модели. |
| Поля монстра ↔ поведение | Сверены armorMixin, regen hook, диалог сопротивлений, oilEffect/category, skillMixin/dontAddAttr, bonus BODY/addMeleeBonus, customStat и 10 label en/ru. Текстовые описания отличены от структурированных модификаторов. |
| Иммунитеты ↔ обработчик | Исходный applyStatus для пустого списка прошёл; при ['bleeding'] и ['unrelated'] после одного toggle возник ReferenceError statusEffectId is not defined. Зарегистрирована issue-00031; реальный toggle и БД не выполнялись. |
| Хвост/крыло ↔ контекст | Оригинальный locationMixin вызывает статический метод на классе: при this экземпляра monster/hasTailWing=true получены 6 локаций без tailWing. Контрольный вызов того же static с явным this=actor дал 7. Issue-00032; потребитель applyDamageToAllLocations найден, полный урон не запускался. |
| Двусторонние карточки | Дополнены 17 прямых зависимостей моделей, карточки registerDataModels/registerSheets/system.json; исходные реквизиты предыдущих проверок сохранены. В новых карточках указаны обратные ссылки и точные источники. |
| Issues ↔ полнота наблюдений | Созданы issue-00031/00032; дополнены issue-00005/00011/00030. Сопоставлены остальные относящиеся к моделям существующие issues без дублей. Все 32 остаются potential. |

### Сводная сверка первых шести порций

| Порция | Файлов | Цепочки и результат |
| --- | --- | --- |
| TASK-0003.001 | 5 | dataUtils — Character/Monster.enrichedText; valueLabel — general/details; stat — Stats/DerivedStats/Reputation → Common. Порядок подготовки и владельцы подтвердились. |
| TASK-0003.002 | 9 | skillsData → семь групп → Skill → Common.skills. Семь групп и52 навыка; поля modifiers отдельно от словаря skillGroupModifiers. |
| TASK-0003.003 | 8 | currency — Common/Loot; adrenaline/focus/note/lifepath/reputation/combatEffects — Common; temporaryEffects — combatEffects. Контракты и области действия согласованы. |
| TASK-0003.004 | 8 | general → background/details/homeland/lifeEvents → lifeEvent — Character; damageTypeModification → damageModification — Common. Две цепочки не объединены по расположению папок. |
| TASK-0003.005 | 7 | Log → ipLog/currencyLog и training — Character; pannels и attackStats → attack — Common. Граница опыта монстра повторно проверена. |
| TASK-0003.006 | 4 | Две специализированные модели с общим родителем, независимая LootData; три регистрации Actor. Точная совокупность первых шести порций: 41 файл. |

Рекурсивный обход явных относительных импортов из четырёх моделей дал ровно 41 файл и 50 рёбер. После исключения четырёх корней получено в точности множество 37 файлов из таблиц TASK-0003.001–005. Для каждого ребра проверены существование исходника/карточки и ссылка на определение в карточке потребителя. Это сверка статических импортов, не готовый граф всех динамических связей системы. Рёбра ниже фиксируют точные имена импортов; символы, применение и динамические потребители описаны в карточках.

| Файл-потребитель | Импорт | Файл определения |
| --- | --- | --- |
| [module/data/actor/commonActorData.js](files/module/data/actor/commonActorData.js.md) | currency | [module/data/actor/templates/common/currencyData.js](files/module/data/actor/templates/common/currencyData.js.md) |
| [module/data/actor/commonActorData.js](files/module/data/actor/commonActorData.js.md) | adrenaline | [module/data/actor/templates/common/adrenalineData.js](files/module/data/actor/templates/common/adrenalineData.js.md) |
| [module/data/actor/commonActorData.js](files/module/data/actor/commonActorData.js.md) | skills | [module/data/actor/templates/common/skills/skillsData.js](files/module/data/actor/templates/common/skills/skillsData.js.md) |
| [module/data/actor/templates/common/skills/skillsData.js](files/module/data/actor/templates/common/skills/skillsData.js.md) | Body | [module/data/actor/templates/common/skills/bodyData.js](files/module/data/actor/templates/common/skills/bodyData.js.md) |
| [module/data/actor/templates/common/skills/bodyData.js](files/module/data/actor/templates/common/skills/bodyData.js.md) | Skill | [module/data/actor/templates/common/skills/skillData.js](files/module/data/actor/templates/common/skills/skillData.js.md) |
| [module/data/actor/templates/common/skills/skillsData.js](files/module/data/actor/templates/common/skills/skillsData.js.md) | Craft | [module/data/actor/templates/common/skills/craData.js](files/module/data/actor/templates/common/skills/craData.js.md) |
| [module/data/actor/templates/common/skills/craData.js](files/module/data/actor/templates/common/skills/craData.js.md) | Skill | [module/data/actor/templates/common/skills/skillData.js](files/module/data/actor/templates/common/skills/skillData.js.md) |
| [module/data/actor/templates/common/skills/skillsData.js](files/module/data/actor/templates/common/skills/skillsData.js.md) | Dexterity | [module/data/actor/templates/common/skills/dexData.js](files/module/data/actor/templates/common/skills/dexData.js.md) |
| [module/data/actor/templates/common/skills/dexData.js](files/module/data/actor/templates/common/skills/dexData.js.md) | Skill | [module/data/actor/templates/common/skills/skillData.js](files/module/data/actor/templates/common/skills/skillData.js.md) |
| [module/data/actor/templates/common/skills/skillsData.js](files/module/data/actor/templates/common/skills/skillsData.js.md) | Empathy | [module/data/actor/templates/common/skills/empData.js](files/module/data/actor/templates/common/skills/empData.js.md) |
| [module/data/actor/templates/common/skills/empData.js](files/module/data/actor/templates/common/skills/empData.js.md) | Skill | [module/data/actor/templates/common/skills/skillData.js](files/module/data/actor/templates/common/skills/skillData.js.md) |
| [module/data/actor/templates/common/skills/skillsData.js](files/module/data/actor/templates/common/skills/skillsData.js.md) | Intelligence | [module/data/actor/templates/common/skills/intData.js](files/module/data/actor/templates/common/skills/intData.js.md) |
| [module/data/actor/templates/common/skills/intData.js](files/module/data/actor/templates/common/skills/intData.js.md) | Skill | [module/data/actor/templates/common/skills/skillData.js](files/module/data/actor/templates/common/skills/skillData.js.md) |
| [module/data/actor/templates/common/skills/skillsData.js](files/module/data/actor/templates/common/skills/skillsData.js.md) | Reflex | [module/data/actor/templates/common/skills/refData.js](files/module/data/actor/templates/common/skills/refData.js.md) |
| [module/data/actor/templates/common/skills/refData.js](files/module/data/actor/templates/common/skills/refData.js.md) | Skill | [module/data/actor/templates/common/skills/skillData.js](files/module/data/actor/templates/common/skills/skillData.js.md) |
| [module/data/actor/templates/common/skills/skillsData.js](files/module/data/actor/templates/common/skills/skillsData.js.md) | Will | [module/data/actor/templates/common/skills/willData.js](files/module/data/actor/templates/common/skills/willData.js.md) |
| [module/data/actor/templates/common/skills/willData.js](files/module/data/actor/templates/common/skills/willData.js.md) | Skill | [module/data/actor/templates/common/skills/skillData.js](files/module/data/actor/templates/common/skills/skillData.js.md) |
| [module/data/actor/commonActorData.js](files/module/data/actor/commonActorData.js.md) | focus | [module/data/actor/templates/common/focusData.js](files/module/data/actor/templates/common/focusData.js.md) |
| [module/data/actor/commonActorData.js](files/module/data/actor/commonActorData.js.md) | note | [module/data/actor/templates/common/noteData.js](files/module/data/actor/templates/common/noteData.js.md) |
| [module/data/actor/commonActorData.js](files/module/data/actor/commonActorData.js.md) | attackStats | [module/data/actor/templates/character/attackStatsData.js](files/module/data/actor/templates/character/attackStatsData.js.md) |
| [module/data/actor/templates/character/attackStatsData.js](files/module/data/actor/templates/character/attackStatsData.js.md) | attack | [module/data/actor/templates/character/attackData.js](files/module/data/actor/templates/character/attackData.js.md) |
| [module/data/actor/commonActorData.js](files/module/data/actor/commonActorData.js.md) | pannels | [module/data/actor/templates/character/pannelsData.js](files/module/data/actor/templates/character/pannelsData.js.md) |
| [module/data/actor/commonActorData.js](files/module/data/actor/commonActorData.js.md) | lifepathData | [module/data/actor/templates/common/lifepathData.js](files/module/data/actor/templates/common/lifepathData.js.md) |
| [module/data/actor/commonActorData.js](files/module/data/actor/commonActorData.js.md) | damageTypeModification | [module/data/actor/templates/character/general/damage/damageTypeModificationData.js](files/module/data/actor/templates/character/general/damage/damageTypeModificationData.js.md) |
| [module/data/actor/templates/character/general/damage/damageTypeModificationData.js](files/module/data/actor/templates/character/general/damage/damageTypeModificationData.js.md) | damageModification | [module/data/actor/templates/character/general/damage/damageModificationData.js](files/module/data/actor/templates/character/general/damage/damageModificationData.js.md) |
| [module/data/actor/commonActorData.js](files/module/data/actor/commonActorData.js.md) | combatEffects | [module/data/actor/templates/common/combatEffectsData.js](files/module/data/actor/templates/common/combatEffectsData.js.md) |
| [module/data/actor/templates/common/combatEffectsData.js](files/module/data/actor/templates/common/combatEffectsData.js.md) | TemporaryEffects | [module/data/actor/templates/common/temporaryEffectsData.js](files/module/data/actor/templates/common/temporaryEffectsData.js.md) |
| [module/data/actor/commonActorData.js](files/module/data/actor/commonActorData.js.md) | DerivedStats | [module/data/actor/templates/common/stats/derivedStatsData.js](files/module/data/actor/templates/common/stats/derivedStatsData.js.md) |
| [module/data/actor/templates/common/stats/derivedStatsData.js](files/module/data/actor/templates/common/stats/derivedStatsData.js.md) | stat | [module/data/actor/templates/common/stats/statData.js](files/module/data/actor/templates/common/stats/statData.js.md) |
| [module/data/actor/commonActorData.js](files/module/data/actor/commonActorData.js.md) | Stats | [module/data/actor/templates/common/stats/statsData.js](files/module/data/actor/templates/common/stats/statsData.js.md) |
| [module/data/actor/templates/common/stats/statsData.js](files/module/data/actor/templates/common/stats/statsData.js.md) | stat | [module/data/actor/templates/common/stats/statData.js](files/module/data/actor/templates/common/stats/statData.js.md) |
| [module/data/actor/commonActorData.js](files/module/data/actor/commonActorData.js.md) | Reputation | [module/data/actor/templates/common/reputationData.js](files/module/data/actor/templates/common/reputationData.js.md) |
| [module/data/actor/templates/common/reputationData.js](files/module/data/actor/templates/common/reputationData.js.md) | stat | [module/data/actor/templates/common/stats/statData.js](files/module/data/actor/templates/common/stats/statData.js.md) |
| [module/data/actor/characterData.js](files/module/data/actor/characterData.js.md) | { createEnrichedText } | [module/data/dataUtils.js](files/module/data/dataUtils.js.md) |
| [module/data/actor/characterData.js](files/module/data/actor/characterData.js.md) | CommonActorData | [module/data/actor/commonActorData.js](files/module/data/actor/commonActorData.js.md) |
| [module/data/actor/characterData.js](files/module/data/actor/characterData.js.md) | general | [module/data/actor/templates/character/generalData.js](files/module/data/actor/templates/character/generalData.js.md) |
| [module/data/actor/templates/character/generalData.js](files/module/data/actor/templates/character/generalData.js.md) | valueLabel | [module/data/actor/templates/valueLabelData.js](files/module/data/actor/templates/valueLabelData.js.md) |
| [module/data/actor/templates/character/generalData.js](files/module/data/actor/templates/character/generalData.js.md) | background | [module/data/actor/templates/character/general/backgroundData.js](files/module/data/actor/templates/character/general/backgroundData.js.md) |
| [module/data/actor/templates/character/generalData.js](files/module/data/actor/templates/character/generalData.js.md) | details | [module/data/actor/templates/character/general/detailsData.js](files/module/data/actor/templates/character/general/detailsData.js.md) |
| [module/data/actor/templates/character/general/detailsData.js](files/module/data/actor/templates/character/general/detailsData.js.md) | valueLabel | [module/data/actor/templates/valueLabelData.js](files/module/data/actor/templates/valueLabelData.js.md) |
| [module/data/actor/templates/character/generalData.js](files/module/data/actor/templates/character/generalData.js.md) | homeland | [module/data/actor/templates/character/general/homelandData.js](files/module/data/actor/templates/character/general/homelandData.js.md) |
| [module/data/actor/templates/character/generalData.js](files/module/data/actor/templates/character/generalData.js.md) | lifeEvents | [module/data/actor/templates/character/general/lifeEventsData.js](files/module/data/actor/templates/character/general/lifeEventsData.js.md) |
| [module/data/actor/templates/character/general/lifeEventsData.js](files/module/data/actor/templates/character/general/lifeEventsData.js.md) | lifeEvent | [module/data/actor/templates/character/general/lifeEventData.js](files/module/data/actor/templates/character/general/lifeEventData.js.md) |
| [module/data/actor/characterData.js](files/module/data/actor/characterData.js.md) | Log | [module/data/actor/templates/character/logData.js](files/module/data/actor/templates/character/logData.js.md) |
| [module/data/actor/templates/character/logData.js](files/module/data/actor/templates/character/logData.js.md) | currencyLog | [module/data/actor/templates/character/currencyLogData.js](files/module/data/actor/templates/character/currencyLogData.js.md) |
| [module/data/actor/templates/character/logData.js](files/module/data/actor/templates/character/logData.js.md) | ipLog | [module/data/actor/templates/character/ipLogData.js](files/module/data/actor/templates/character/ipLogData.js.md) |
| [module/data/actor/characterData.js](files/module/data/actor/characterData.js.md) | skillTraining | [module/data/actor/templates/character/skillTrainingData.js](files/module/data/actor/templates/character/skillTrainingData.js.md) |
| [module/data/actor/monsterData.js](files/module/data/actor/monsterData.js.md) | CommonActorData | [module/data/actor/commonActorData.js](files/module/data/actor/commonActorData.js.md) |
| [module/data/actor/monsterData.js](files/module/data/actor/monsterData.js.md) | { createEnrichedText } | [module/data/dataUtils.js](files/module/data/dataUtils.js.md) |
| [module/data/actor/lootData.js](files/module/data/actor/lootData.js.md) | currency | [module/data/actor/templates/common/currencyData.js](files/module/data/actor/templates/common/currencyData.js.md) |

### Выполненные команды и изолированные сценарии

На старте: git status --short, git rev-parse HEAD, git branch --show-current, git ls-files -z; Python-сверка 621 путей из registry.md с файловой системой, HEAD и базовым git show; снимок mode/uid/gid/inode всех 798 отслеживаемых файлов. Полное чтение 275 строк; rg по именам классов, методов и system-путям в module/, templates/, packsJson/; локальное чтение соответствующих участков ядра /opt/foundryvtt.

Сценарий Node запускался через stdin (`node --input-type=module`), без файлов стенда. Импортированы настоящие primitives, fields.mjs, DataModel, TypeDataModel, utils/helpers.mjs Foundry 14.367.0; собран глобальный foundry для загрузки исходных четырёх моделей. Не создавались Actor-документы или коллекции мира. Модели и их методы оригинальные; TextEditor.enrichHTML заменён async преобразованием строки с меткой, toggleStatusEffect — записью вызовов; setTimeout — контролем недостижимости. Схемы, источники, равенство повторной подготовки, формулы, миграции, масса и возврат enrichedText проверены assert. Первое ожидание числа полей Monster в самом сценарии было ошибочно55; после сопоставления определений исправлено на53, окончательный сценарий прошёл.

Для applyStatus тело исходного метода извлечено без изменений, выполнено в vm с реальной MonsterData и Set. Для getAllLocations в отдельном сценарии сохранено точное статическое тело, помещённое в минимальный класс; исходный locationMixin получил этот класс вместо импорта. Контроль с явным this подтвердил причину расхождения списка. Подмены не выполняли сетевые/серверные записи и не подтверждают состояние игрового эффекта.

Фактические ключевые результаты:

```text
schemaCounts: Common=19, Character=29, Monster=53, Loot=3
prepare: stun6 run18 leap3 enc70 rec6 woundTreshold6 resolve70 focus21 vigor.max4 reputation.max3
sourceUnchanged=true; repeatIdentical=true; stun bounds=[1,10]
currency: Common=Character=Monster=Loot=0.007
labels: en10/10, ru10/10
immunity []: toggle('bleeding'), resolved
immunity ['bleeding'] / ['unrelated']: toggle('bleeding'), ReferenceError: statusEffectId is not defined
locations through original mixin: 6; same static with actor this: 7 (tailWing included)
import closure: 41 files, 50 edges, previous portions exactly37
```

Node выдал стандартное MODULE_TYPELESS_PACKAGE_JSON при загрузке ES modules; package.json не изменялся. Повторные исполнения уточняли ожидание количества полей и убирали избыточный вывод очищенного конструкторами входа; это не изменения исследуемой системы.

### Итоговая проверка документов и сохранности

Проверка Python и git diff --check прошла: 621 уникальный исходный путь, 52 карточки со статусом «Проверено», 569 строк «Не начат», четыре новые карточки строго по перечню порции и все обязательные разделы. Сверены 126 Markdown-документов и 3045 локальных ссылок/якорей, структура таблиц, отсутствие хвостовых пробелов и непрерывная нумерация 32 potential issues. TASK-0003.006 — done, TASK-0003 — in-progress, TASK-0003.007–010 — planned. Изменены только 40 документов: 34 существующих и 6 новых (4 карточки, 2 issues). Содержимое всех исходников, HEAD и метаданные всех 798 ранее отслеживаемых файлов сохранены.

SHA256 621 исходника (путь+NUL+байты+NUL, порядок registry): `9de49bf9b75194490fcfd7bfc80e2b1c8bcd9d90dd26f3603faf21d92b3d0e1e`. SHA256 сериализованных mode/uid/gid/inode 798 отслеживаемых файлов: `05ee1196f64deca4de0933de844ca64022ea70a36c3d9978a15b1b5596f976d9`. Исходный HEAD сохраняется; новые файлы — только Markdown в docs. Историческая часть журнала, начиная с TASK-0003.005, сохранена побайтно.

### Итог и границы

TASK-0003.006 завершена. Общее покрытие 52/621, не разобраны 569; первая серия 41/61, осталось 20, вне первой серии 549. Всего 32 issues, все potential. Следующая подзадача — [TASK-0003.007](../../tasks/task-0003.007.md).

Полный Actor/ActiveEffect, формы в браузере, запись документов, запуск мира, миграция реальных старых данных, правила игры и внешние модули не проверялись. Найденные ошибки не исправлялись. На файлы системы, игровые данные и права доступа изменения не вносились.

## TASK-0003.005

Дата: 2026-09-10. Ветка rusbar-main, HEAD `c9eac1ffb28fdf69935d500fff26d4d0ad1d1609`. Рабочее дерево на старте чистое, отслеживались 788 файлов. Все 621 исходник совпали со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. Foundry 14.367.0 по /opt/foundryvtt/package.json, Node 24.16.0.

Полностью прочитаны семь файлов [TASK-0003.005](../../tasks/task-0003.005.md), всего 118 строк: currencyLogData.js (9), ipLogData.js (9), logData.js (38), skillTrainingData.js (9), pannelsData.js (31), attackData.js (9), attackStatsData.js (13). Результат — семь карточек с определениями, методами, изменениями состояния и таблицами зависимостей. Соседние файлы прочитаны в пределах установления связи и не получают завершённый статус за точечный просмотр.

### Содержательная и перекрёстная сверка

| Направление | Источник и фактический результат |
| --- | --- |
| Фабрики ↔ поля | Проверены все определения семи файлов, единственный класс Log, три его метода и default exports. Схемы не подменены описанием поведения UI. |
| Журналы ↔ вложение | currencyLog/ipLog → SchemaField в ArrayField Log → EmbeddedDataField CharacterData.logs. Настоящая модель подтвердила Log.parent=CharacterData и Log.parent.parent=двойник Actor. У MonsterData блока logs нет. |
| Log ↔ операции | push живого массива предшествует update. Обычные +2 от10→12; magic+3 от8→11; обычный расход -2 от10→8; crown+5 от100→105. Захвачены и записи истории, и остатки. |
| Log ↔ асинхронность | Документ ядра возвращает Promise из async update; Log возвращает undefined. Два await вызова Log при отложенном сохранении сформировали остатки IP12/13 и crown102/103; два запроса оставались pending. Серверная потеря данных не утверждается. |
| Обучение ↔ форма ↔ журнал | Четыре независимых name/value. _saveIpSpending читает DOM, не сам слот: ввод '3' даёт числовой остаток7, '-3' — строку '10-3'. Настоящий updateSource(dryRun) принял первый и отверг второй с ошибкой NumberField. |
| MonsterData ↔ общий skills-шаблон | Текущий WitcherMonsterSheet включает skillTabs.ip и общий tab-skills.hbs. Девять путей ввода (IP и восемь training) найдены в CharacterData, отсутствуют в MonsterData. Рендер/сохранение не запускались. |
| Навыки ↔ настоящий Log | levelUpSkill spellcast2, magic10 с настоящим Log сформировал сначала update magic6 из Log, затем update magic10 из levelUpSkill. Issue-00017 дополнена конфликтом запросов; предыдущая проверка со stub журнала сохранена как историческая. |
| Панели ↔ модели и динамические ключи | 22 флага из CommonActorData у персонажа и монстра; 9 substance/6 spell/7 skill dataset-значений совпали с полями. Исходные обработчики для false/true дали 44 соответствующих update. |
| Панели ↔ выбор шаблонов | 9 substance-флагов связаны с текущим inventory персонажа. 13 skill/spell-флагов читаются старыми monster-* шаблонами; текущие листы выбирают новые общие tab-skills/tab-magic. Наличие старого шаблона не признано текущим использованием. |
| Атаки ↔ подготовка | BODY1/6/8 при предварительной добавке melee3 дали итог -1/3/5. punch строки 1d6+-4 / 1d6+0 / 1d6+2; kick 1d6+0 / 1d6+4 / 1d6+6. Входной source.meleeBonus=3 обнулён миграцией CommonActorData. |
| Параметры атак ↔ потребители | meleeBonus используется условно в weaponAttack/doProfessionAttackRoll. crit-поля копируются в damage.crit и применяются для случайной локации и выбора травмы; точные условия описаны. Punch/kick за пределами определения/присваивания не имеют найденных явных читателей в исследованной области. |
| Мастер/переводы/JSON ↔ схемы | Все три пути getOtherSuggestions найдены в CommonActorData; 11 ключей переводов en/ru после expandObject существуют. В 226 JSON нет строковых путей префиксов logs/skillTrainingN/pannels/attackStats. |
| Двусторонние связи | Дополнены карточки currencyData, statsData, skillData, config, registerDataModels, registerSheets и TheWitcherTRPG.js; новые карточки ссылаются на проверенные определения. Версии предыдущих проверок сохранены. |
| Issues ↔ наблюдения | Созданы issue-00028–issue-00030, уточнена issue-00017; все 30 карточек остаются potential. Поведение миграции meleeBonus, отсутствие читателей punch/kick и сохранение старых флагов не объявлены ошибками без дополнительного основания. |

### Выполненные команды и изолированный сценарий

Исходное состояние: git status --short, git rev-parse HEAD, git branch --show-current; сверка всех 621 файла с git show базового коммита и вычисление SHA256. Полный нумерованный вывод семи исходников. Поиск rg по currencyLog/ipLog/addIpReward/addCurrencyReward, skillTraining, pannels, attackStats, punch/kick, calculateAttackStats и crit-модификаторам в module/, templates/, packsJson/. При отдельных поисках были указаны несуществующий старый путь tab-inventory.hbs и нераскрывшийся glob module/item/mixins/weapon*: эти попытки вернули exit2. После этого проверены реальные пути из rg --files/найденных imports и нужные определения; выводы не основаны на отсутствующих файлах. Обрезанные соседние фрагменты дополнялись точечными чтениями.

Из корня репозитория выполнено без создания файла скрипта:

```sh
node --input-type=module - <<'JS'
import fs from 'node:fs';
import vm from 'node:vm';
import assert from 'node:assert/strict';
await import('/opt/foundryvtt/common/primitives/_module.mjs');
const fields=await import('/opt/foundryvtt/common/data/fields.mjs');
const {default:DataModel}=await import('/opt/foundryvtt/common/abstract/data.mjs');
const {default:TypeDataModel}=await import('/opt/foundryvtt/common/abstract/type-data.mjs');
const utils=await import('/opt/foundryvtt/common/utils/helpers.mjs');
globalThis.foundry={data:{fields},abstract:{DataModel,TypeDataModel},utils,applications:{api:{DialogV2:{}}}};
const {default:Character}=await import('./module/data/actor/characterData.js');
const {default:Monster}=await import('./module/data/actor/monsterData.js');
const {default:Common}=await import('./module/data/actor/commonActorData.js');
const {default:Log}=await import('./module/data/actor/templates/character/logData.js');
const {WITCHER}=await import('./module/setup/config.js');
const game={settings:{get:()=>false},i18n:{localize:k=>k}};
const baseGlobals={foundry,game,CONFIG:{WITCHER}};
const copy=o=>JSON.parse(JSON.stringify(o));
function source(file,names,extra={}){
 const code=fs.readFileSync(file,'utf8').replace(/^import .*;\r?$/gm,'').replace(/^export (?=(?:async )?(?:function|let|const|class))/gm,'');
 const ctx={...baseGlobals,...extra};
 vm.runInNewContext("'use strict';\n"+code+'\nthis.result={'+names.join(',')+'};',ctx,{filename:file});
 return ctx.result;
}
const fresh=new Character({});
assert(fresh.logs instanceof Log);assert.equal(fresh.logs.parent,fresh);
assert.deepEqual(fresh.logs.toObject(),{ipLog:[],currencyLog:[]});
const log=new Log({ipLog:[{}],currencyLog:[{}]});
assert.deepEqual(log.toObject(),{ipLog:[{label:'',ip:0,isMagic:false}],currencyLog:[{label:'',amount:0,type:''}]});
for(let i=1;i<=4;i++)assert.deepEqual(fresh['skillTraining'+i],{name:'',value:0});
fresh.skillTraining1.value=3;assert.equal(fresh.skillTraining2.value,0);
const pannels=Object.keys(fresh.pannels);
assert.equal(pannels.length,22);assert(Object.values(fresh.pannels).every(v=>v===false));
for(const Model of [Common,Character,Monster]){
 const model=new Model({});assert.deepEqual(Object.keys(model.pannels),pannels);
 assert.deepEqual(model.attackStats,{meleeBonus:0,punch:{label:'WITCHER.Actor.DerStat.Punch',value:''},kick:{label:'WITCHER.Actor.DerStat.Kick',value:''},critLocationModifier:0,critEffectModifier:0});
}
const monster=new Monster({});
for(const key of ['logs','improvementPoints','magic','skillTraining1','skillTraining2','skillTraining3','skillTraining4'])assert.equal(monster[key],undefined);
const r={defaults:{logs:log.toObject(),trainingSlots:4,pannels:pannels.length,attackStats:copy(fresh.attackStats)},monsterAbsent:['logs','improvementPoints','magic','skillTraining1','skillTraining2','skillTraining3','skillTraining4']};
function actorWithQueue(){
 const pending=[],updates=[];
 const actor=new (class ActorDouble extends DataModel {static TYPES=[];static defineSchema(){return {}}})({});
 actor.update=data=>{
   updates.push(copy(data));
   return new Promise(resolve=>pending.push(()=>resolve(actor)));
 };
 actor.system=new Character({improvementPoints:10,magic:{magicImprovementPoints:8},currency:{crown:100}},{parent:actor});
 assert.equal(actor.system.logs.parent.parent,actor);
 return {actor,updates,pending};
}
r.rewards=[];
for(const [name,call,key,expected] of [
 ['normal',log=>log.addIpReward('reward',2,false),'system.improvementPoints',12],
 ['magic',log=>log.addIpReward('reward',3,true),'system.magic.magicImprovementPoints',11],
 ['spend',log=>log.addIpReward('spend',-2),'system.improvementPoints',8],
 ['currency',log=>log.addCurrencyReward('reward',5,'crown'),'system.currency.crown',105]
]){
 const c=actorWithQueue(),result=call(c.actor.system.logs);
 assert.equal(result,undefined);assert.equal(c.pending.length,1);assert.equal(c.updates[0][key],expected);
 r.rewards.push({name,result:'undefined',pending:1,update:c.updates[0]});c.pending.forEach(done=>done());
}
r.pendingRewards={};
for(const kind of ['ip','currency']){
 const c=actorWithQueue();
 const log=c.actor.system.logs;
 if(kind==='ip'){await log.addIpReward('a',2,false);await log.addIpReward('b',3,false)}
 else{await log.addCurrencyReward('a',2,'crown');await log.addCurrencyReward('b',3,'crown')}
 const key=kind==='ip'?'system.improvementPoints':'system.currency.crown';
 r.pendingRewards[kind]={writes:c.updates.map(v=>v[key]),pending:c.pending.length};
 assert.deepEqual(r.pendingRewards[kind].writes,kind==='ip'?[12,13]:[102,103]);
 c.pending.forEach(done=>done());
}
const text=fs.readFileSync('module/actor/sheets/WitcherCharacterSheet.js','utf8');
const method=text.slice(text.indexOf('    async _saveIpSpending(event) {'),text.indexOf('    async _renderRewards() {'));
const context={};vm.runInNewContext('this.Sheet=class {\n'+method+'\n}',context);
r.manual=[];
for(const value of ['3','-3']){
 const c=actorWithQueue();
 await context.Sheet.prototype._saveIpSpending.call({actor:c.actor},{currentTarget:{parentElement:{children:{item:i=>({value:i===0?'training':value})}}}});
 const write=c.updates[0],balance=write['system.improvementPoints'];
 let valid=true,message='';
 try{
   const delta=Object.fromEntries(Object.entries(write).map(([k,v])=>[k.replace(/^system\./,''),v]));
   c.actor.system.updateSource(delta,{dryRun:true});
 }catch(e){valid=false;message=e.message}
 r.manual.push({input:value,balance,balanceType:typeof balance,valid,message,log:write['system.logs.ipLog']});
 assert.equal(balance,value==='3'?7:'10-3');assert.equal(valid,value==='3');
 c.pending.forEach(done=>done());
}
const {skillMixin}=source('module/actor/mixins/skillMixin.js',['skillMixin']);
const trained=actorWithQueue();trained.actor.system.skills.will.spellcast.value=2;trained.actor.system.magic.magicImprovementPoints=10;
await skillMixin.levelUpSkill.call(trained.actor,'spellcast');
assert.equal(trained.updates.length,2);
assert.equal(trained.updates[0]['system.magic.magicImprovementPoints'],6);
assert.equal(trained.updates[1]['system.magic.magicImprovementPoints'],10);
r.levelUpWithRealLog=trained.updates;
trained.pending.forEach(done=>done());
const {itemMixin}=source('module/actor/sheets/mixins/itemMixin.js',['itemMixin'],{WITCHER});
const {skillMixin:sheetSkills}=source('module/actor/sheets/mixins/skillMixin.js',['skillMixin']);
const cases=[
 ['templates/partials/character/substances.hbs','subtype',itemMixin._onSubstanceDisplay],
 ['templates/partials/monster/monster-spell-tab.hbs','spelltype',itemMixin._onSpellDisplay],
 ['templates/partials/monster/monster-skill-tab.hbs','skilltype',sheetSkills._onSkillDisplay]
];
const writes=[];
for(const [file,attribute,fn] of cases){
 const names=[...fs.readFileSync(file,'utf8').matchAll(new RegExp('data-'+attribute+'="([^"]+)"','g'))].map(m=>m[1]);
 for(const name of names){
  const key=name+'IsOpen';assert(Character.schema.getField('pannels.'+key));
  const actor={system:new Character({}),update:data=>writes.push(copy(data))};
  for(const old of [false,true]){
   actor.system.pannels[key]=old;
   fn.call({actor},{preventDefault(){},currentTarget:{closest:()=>({dataset:{[attribute]:name}})}});
   assert.equal(writes.at(-1)['system.pannels.'+key],!old);
  }
 }
}
assert.equal(writes.length,44);r.panelToggle={fields:22,writes:44};
const actorText=fs.readFileSync('module/actor/witcherActor.js','utf8');
const calc=actorText.slice(actorText.indexOf('    calculateAttackStats() {'),actorText.indexOf('    async applyStatus('));
const ctx={};vm.runInNewContext('this.Calculator=class {\n'+calc+'\n}',ctx);
r.attack=[];
for(const body of [1,6,8]){
 const model=new Common({});model.stats.body.value=body;model.attackStats.meleeBonus=3;
 ctx.Calculator.prototype.calculateAttackStats.call({system:model});
 r.attack.push({body,...copy(model.attackStats)});
}
assert.deepEqual(r.attack.map(v=>v.meleeBonus),[-1,3,5]);
assert.deepEqual(r.attack.map(v=>v.punch.value),['1d6+-4','1d6+0','1d6+2']);
assert.equal(new Common({attackStats:{meleeBonus:3}}).attackStats.meleeBonus,0);
r.savedMeleeMigration=0;
const {baseMixin}=source('module/activeEffect/mixins/baseMixin.js',['baseMixin']);
const suggestions=Object.values(baseMixin.getOtherSuggestions());
assert.equal(suggestions.length,3);
for(const s of suggestions)assert(Common.schema.getField(s.value.slice(7)));
r.attackSuggestions=suggestions.map(v=>v.value);
const missing=[];
const trainingText=fs.readFileSync('templates/partials/character/tab-skills.hbs','utf8');
for(const match of trainingText.matchAll(/name="(system\.(?:skillTraining\d\.(?:name|value)|improvementPoints))"/g)){
 const path=match[1].slice(7);
 assert(Character.schema.getField(path));
 if(!Monster.schema.getField(path))missing.push(match[1]);
}
assert.equal(missing.length,9);r.monsterFormFieldsMissing=missing;
const labels=['WITCHER.Actor.DerStat.Punch','WITCHER.Actor.DerStat.Kick',...suggestions.map(v=>v.label),'WITCHER.rewards.dialog.label','WITCHER.rewards.dialog.ip','WITCHER.rewards.dialog.magicIp','WITCHER.rewards.dialog.currency','WITCHER.rewards.dialog.currencyType','WITCHER.Actor.SkillName'];
r.labels={};
for(const lang of ['en','ru']){
 const data=utils.expandObject(JSON.parse(fs.readFileSync('lang/'+lang+'.json')));
 const absent=labels.filter(k=>utils.getProperty(data,k)===undefined);
 assert.equal(absent.length,0);r.labels[lang]={checked:labels.length,absent};
}
const files=[],refs=[];
function walk(dir){for(const e of fs.readdirSync(dir,{withFileTypes:true})){const p=dir+'/'+e.name;if(e.isDirectory())walk(p);else if(p.endsWith('.json'))files.push(p)}}
walk('packsJson');
function scan(value,file,path=''){
 if(typeof value==='string'&&/^system\.(?:logs(?:\.|$)|skillTraining\d(?:\.|$)|pannels(?:\.|$)|attackStats(?:\.|$))/.test(value))refs.push({file,path,value});
 else if(value&&typeof value==='object')for(const [k,v] of Object.entries(value))scan(v,file,path+'.'+k);
}
for(const file of files)scan(JSON.parse(fs.readFileSync(file)),file);
for(const ref of refs)assert(Character.schema.getField(ref.value.slice(7)),ref.value);
r.packs={files:files.length,refs};
console.log(JSON.stringify(r));

JS
```

Результат: exit 0. Вывод:

```text
{"defaults":{"logs":{"ipLog":[{"label":"","ip":0,"isMagic":false}],"currencyLog":[{"label":"","amount":0,"type":""}]},"trainingSlots":4,"pannels":22,"attackStats":{"meleeBonus":0,"punch":{"label":"WITCHER.Actor.DerStat.Punch","value":""},"kick":{"label":"WITCHER.Actor.DerStat.Kick","value":""},"critLocationModifier":0,"critEffectModifier":0}},"monsterAbsent":["logs","improvementPoints","magic","skillTraining1","skillTraining2","skillTraining3","skillTraining4"],"rewards":[{"name":"normal","result":"undefined","pending":1,"update":{"system.logs.ipLog":[{"label":"reward","ip":2,"isMagic":false}],"system.improvementPoints":12}},{"name":"magic","result":"undefined","pending":1,"update":{"system.logs.ipLog":[{"label":"reward","ip":3,"isMagic":true}],"system.magic.magicImprovementPoints":11}},{"name":"spend","result":"undefined","pending":1,"update":{"system.logs.ipLog":[{"label":"spend","ip":-2}],"system.improvementPoints":8}},{"name":"currency","result":"undefined","pending":1,"update":{"system.logs.currencyLog":[{"label":"reward","amount":5,"type":"crown"}],"system.currency.crown":105}}],"pendingRewards":{"ip":{"writes":[12,13],"pending":2},"currency":{"writes":[102,103],"pending":2}},"manual":[{"input":"3","balance":7,"balanceType":"number","valid":true,"message":"","log":[{"label":"training","ip":-3}]},{"input":"-3","balance":"10-3","balanceType":"string","valid":false,"message":"CharacterData validation errors: SchemaField#_updateDiff\n  improvementPoints: must be a number","log":[{"label":"training","ip":"-3"}]}],"levelUpWithRealLog":[{"system.logs.ipLog":[{"label":"WITCHER.skills.spellCasting.label 2 -> 3","ip":-4,"isMagic":true}],"system.magic.magicImprovementPoints":6},{"system.skills.will.spellcast.value":3,"system.magic.magicImprovementPoints":10,"system.improvementPoints":10}],"panelToggle":{"fields":22,"writes":44},"attack":[{"body":1,"meleeBonus":-1,"punch":{"label":"WITCHER.Actor.DerStat.Punch","value":"1d6+-4"},"kick":{"label":"WITCHER.Actor.DerStat.Kick","value":"1d6+0"},"critLocationModifier":0,"critEffectModifier":0},{"body":6,"meleeBonus":3,"punch":{"label":"WITCHER.Actor.DerStat.Punch","value":"1d6+0"},"kick":{"label":"WITCHER.Actor.DerStat.Kick","value":"1d6+4"},"critLocationModifier":0,"critEffectModifier":0},{"body":8,"meleeBonus":5,"punch":{"label":"WITCHER.Actor.DerStat.Punch","value":"1d6+2"},"kick":{"label":"WITCHER.Actor.DerStat.Kick","value":"1d6+6"},"critLocationModifier":0,"critEffectModifier":0}],"savedMeleeMigration":0,"attackSuggestions":["system.attackStats.meleeBonus","system.attackStats.critLocationModifier","system.attackStats.critEffectModifier"],"monsterFormFieldsMissing":["system.improvementPoints","system.skillTraining1.name","system.skillTraining1.value","system.skillTraining2.name","system.skillTraining2.value","system.skillTraining3.name","system.skillTraining3.value","system.skillTraining4.name","system.skillTraining4.value"],"labels":{"en":{"checked":11,"absent":[]},"ru":{"checked":11,"absent":[]}},"packs":{"files":226,"refs":[]}}
(node:672219) [MODULE_TYPELESS_PACKAGE_JSON] Warning: Module type of file:///var/lib/foundryvtt/Data/systems/TheWitcherTRPG-RB-Version/module/data/actor/characterData.js is not specified and it doesn't parse as CommonJS.
Reparsing as ES module because module syntax was detected. This incurs a performance overhead.
To eliminate this warning, add "type": "module" to /var/lib/foundryvtt/Data/systems/TheWitcherTRPG-RB-Version/package.json.
(Use `node --trace-warnings ...` to show where the warning was created)
```

При настройке изолированного сценария первоначально передан простой объект parent; DataModel его отверг. Двойник заменён подклассом настоящего DataModel с defineSchema и TYPES=[], чтобы TypeDataModel не искал провайдера вымышленного типа документа. Это исправления окружения проверки по /opt/foundryvtt/common/abstract/data.mjs:46–51,159 и /opt/foundryvtt/common/data/fields.mjs:4234–4242, не ошибки системы. Предупреждение Node MODULE_TYPELESS_PACKAGE_JSON относится к загрузке ES modules; package.json не менялся.

Подменены: Actor как минимальный DataModel-владелец, update как очередь записанных аргументов с управляемым Promise, DOM children/item/value и closest/dataset, game.settings/i18n. Настоящие: DataModel/TypeDataModel/fields/CharacterData/CommonActorData/MonsterData/Log и фабрики, три метода переключения флагов, levelUpSkill, _saveIpSpending, calculateAttackStats, getOtherSuggestions. Два метода классов извлечены из исходного текста без изменения тел. updateSource(...,{dryRun:true}) проверяет данные в памяти, без сохранения. Родительская цепочка проверена на настоящих моделях, но полного Document Actor нет.

Не проверены: игровой мир, DOM/браузер, реальные формы/диалоги, права и HTTP-доступ Foundry, отказ/порядок обработки серверных обновлений, полный цикл подготовки Actor, настоящий ActiveEffect, броски и соответствие игровым правилам. Отложенные Promise сценария разрешены вручную после записи наблюдений.

### Проверка документации и состава

Проверки после оформления: соответствие 621 пути Git и фактическому дереву; байты каждого исходника против среза TASK-0001 и HEAD; SHA256 исходников; mode/uid/gid/inode всех 788 ранее отслеживаемых файлов; 48 карточек/строк реестра и семь новых исходников порции; обязательные разделы/поля; уникальные issues и состояния задач; локальные ссылки/якоря; таблицы Markdown; git diff --check. История журнала до этой порции сравнивается с HEAD без изменений.

Итог проверки: exit 0. Реестр — 621 исходник, 48 проверенных карточек, 573 файла не разобраны; добавлены семь карточек. Все 30 issues находятся в potential. Проверены 120 Markdown-документов и 2712 локальных ссылок; изменены или созданы 29 документов. Содержимое исходников и mode/uid/gid/inode всех 788 ранее отслеживаемых файлов сохранены; git diff --check прошёл. Историческая часть журнала совпала с HEAD. TASK-0003.005 завершена, родительская TASK-0003 остаётся in-progress; следующая TASK-0003.006 — planned.

## TASK-0003.004

Дата: 2026-09-10. Ветка rusbar-main, HEAD `17eeb6ae9efccf7474b9ca1845b9ab6370671a26`. На старте рабочее дерево чистое, отслеживались 776 файлов. Все 621 исходник совпали со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. Foundry 14.367.0 по /opt/foundryvtt/package.json, Node 24.16.0.

Полностью прочитаны восемь файлов [TASK-0003.004](../../tasks/task-0003.004.md), всего 116 строк: backgroundData.js (7), detailsData.js (16), homelandData.js (9), lifeEventData.js (10), lifeEventsData.js (29), generalData.js (21), damageModificationData.js (9), damageTypeModificationData.js (15). Соседние модели, обработчики и шаблоны проверены до определений используемых сущностей; отдельными завершёнными карточками они не считаются.

### Содержательная и перекрёстная сверка

| Направление | Источники и фактический результат |
| --- | --- |
| Схемы ↔ включение | background/details/homeland/lifeEvents → general → CharacterData; damageModification → damageTypeModification → CommonActorData → CharacterData/MonsterData. Восьми карточкам соответствуют восемь строк реестра. |
| Биография ↔ enrichedText ↔ форма | CharacterData:34–40 и createEnrichedText передают исходную строку, отдельный enriched и HTMLField в formGroup tab-background:52. TextEditor подменён сборщиком аргументов; редактор не запускался. |
| Подробности ↔ valueLabel | Семь пар value/label, динамические inputs tab-background:27–33; текстовая general.reputation отличается от числовой system.reputation. Карточка valueLabel дополнена. |
| Родина ↔ Item ↔ шаблоны | В отсутствие Item.homeland используются general.homeland.value/otherValue; при наличии Item оба шаблона выбирают его данные. WITCHER.homelands содержит 26 вариантов, schema choices не ограничены. |
| Социальное положение ↔ формула | Шесть вариантов CONFIG, строковый socialStanding. Исходный addSocialStanding: tolerated/emp/charisma → -1, hatedFeared → -2-1, feared/will/intimidation → +1, equal → пусто. Это код, не проверка рулбука. |
| События ↔ контекст ↔ схема | Двадцать ключей 10–200 и decade=1–20. Подготовка контекста заменяет объект живой модели массивом; toObject(false) читает ключ 10 как исходную запись 110, ключ 20=undefined. _source/toObject() сохранены; toggle формирует update для ключа 10. |
| Счётчик ↔ eachLimit | Реальная модель принимает 21; HTML-ввод ограничен 1–20. Исходный helper при 2 выдаёт записи key10/20, при 21 — один undefined. Достижимость обхода ограничений обычной формы не установлена. |
| Типы урона ↔ мастер эффектов | Семь типов × три поля =21 путь; исходный getDamageModifcators выдаёт их для Actor и принадлежащего ему Item, 0 для самостоятельного Item. Все 21 пути найдены в схеме. В CONFIG есть дополнительный silver; отсутствие его в схеме оставлено вопросом. |
| Параметры ↔ обработчики | applyAP=true без AP вызывает TypeError из-за damageProperties вместо properties; AP даёт ранний выход. multiplication=0.5 для damage10 даёт 10/2/2/0 без брони/с надетой/с естественной/с обеими. flat=-3/0/+3 даёт [10]/[10]/[10,3]. |
| Переводы ↔ реальные правила чтения | 51 ключ en/ru найден после foundry.utils.expandObject; составной background.other также найден. Источник нормализации: /opt/foundryvtt/client/helpers/localization.mjs:365–368. |
| JSON-компедиумы ↔ пути | Рекурсивно просмотрены строковые значения 226 packsJson/*.json: путей с префиксами system.general или system.damageTypeModification нет. Бинарные packs/БД не исследовались. |
| Уже описанные зависимости ↔ новые карточки | Дополнены valueLabelData, dataUtils, config, handlebars, registerDataModels; сохранены версии и предыдущие записи. Issue-00021 дополнена связью потерянного damage.type с fallback getters. |
| Наблюдения ↔ issues | Зарегистрированы issue-00024–issue-00027; 27 карточек остаются potential. Отдельные issues для серебра, произвольных строк, счётчика вне HTML-диапазона и отсутствия прямых потребителей name/race/reputation не создавались без достаточного основания. |

### Фактически выполненные проверки

Чтение: git status --short; git rev-parse HEAD; git branch --show-current; полный вывод восьми исходников с номерами строк. Поиск rg по именам фабрик, general.*, lifeEvents, lifeEventCounter, getDamageModifcators, getFlatDamageMod/getMultiDamageMod, calculateArmorResistances, applyAP и consumers в module/, templates/, packsJson/. Первичный поиск включал несуществующий корневой scripts/ и вернул exit 2; далее использовался реальный каталог module/, включающий module/scripts/. Вывод с обрезанными соседними фрагментами дополнен точечными чтениями нужных определений.

Изолированный запуск выполнен из корня репозитория, без создания стенда и файлов скрипта:

```sh
node --input-type=module - <<'JS'
import fs from 'node:fs';
import vm from 'node:vm';
import assert from 'node:assert/strict';
await import('/opt/foundryvtt/common/primitives/_module.mjs');
const fields=await import('/opt/foundryvtt/common/data/fields.mjs');
const {default:DataModel}=await import('/opt/foundryvtt/common/abstract/data.mjs');
const {default:TypeDataModel}=await import('/opt/foundryvtt/common/abstract/type-data.mjs');
const utils=await import('/opt/foundryvtt/common/utils/helpers.mjs');
globalThis.foundry={data:{fields},abstract:{DataModel,TypeDataModel},utils,applications:{api:{DialogV2:{}}}};
const {default:Character}=await import('./module/data/actor/characterData.js');
const {default:Monster}=await import('./module/data/actor/monsterData.js');
const {default:Common}=await import('./module/data/actor/commonActorData.js');
const {default:Loot}=await import('./module/data/actor/lootData.js');
const {WITCHER}=await import('./module/setup/config.js');
const {DamageInstance}=await import('./module/scripts/damageInstance.js');
const game={settings:{get:()=>false},i18n:{localize:k=>k}};
const baseGlobals={foundry,game,CONFIG:{WITCHER},DamageInstance};
function source(file,names,extra={}){
 const code=fs.readFileSync(file,'utf8').replace(/^import .*;\r?$/gm,'').replace(/^export (?=(?:async )?(?:function|let|const|class))/gm,'');
 const ctx={...baseGlobals,...extra};
 vm.runInNewContext("'use strict';\n"+code+'\nthis.result={'+names.join(',')+'};',ctx,{filename:file});
 return ctx.result;
}
const char=new Character({});
const obj=char.toObject();
assert.equal(char.general.background.value,'');
assert.equal(Character.schema.getField('general.background.value').constructor.name,'HTMLField');
assert.equal(Object.keys(char.general.details).length,7);
for(const detail of Object.values(char.general.details)){assert.equal(detail.value,'');assert(detail.label.startsWith('WITCHER.'))}
assert.deepEqual(char.general.homeland,{value:'',otherValue:''});
assert.deepEqual(char.general.reputation,{value:'',label:'WITCHER.Reputation'});
assert.equal(char.general.age,0);
for(const k of ['name','race','socialStanding'])assert.equal(char.general[k],'');
const lifeKeys=Array.from({length:20},(_,i)=>String((i+1)*10));
assert.deepEqual(Object.keys(char.general.lifeEvents),lifeKeys);
lifeKeys.forEach((key,i)=>assert.deepEqual(char.general.lifeEvents[key],{decade:i+1,value:'',details:'',isOpened:false}));
const damageKeys=['slashing','piercing','bludgeoning','elemental','electricity','fire','ice'];
for(const Model of [Common,Character,Monster]){
 const model=new Model({});
 assert.deepEqual(Object.keys(model.damageTypeModification),damageKeys);
 for(const v of Object.values(model.damageTypeModification))assert.deepEqual(v,{flat:0,multiplication:1,applyAP:false});
}
assert.equal(new Monster({}).general,undefined);
assert.equal(new Loot({}).damageTypeModification,undefined);
const odd=new Character({general:{age:-1.5,homeland:{value:'custom'},lifeEvents:{10:{decade:1.5}}},lifeEventCounter:21,damageTypeModification:{fire:{flat:-3.5,multiplication:-0.5,applyAP:true}}});
assert.equal(odd.general.age,-1.5);assert.equal(odd.general.homeland.value,'custom');
assert.equal(odd.general.lifeEvents[10].decade,1.5);assert.equal(odd.lifeEventCounter,21);
assert.equal(odd.damageTypeModification.fire.flat,-3.5);assert.equal(odd.damageTypeModification.fire.multiplication,-0.5);
const r={defaults:{generalKeys:Object.keys(char.general),detailsKeys:Object.keys(char.general.details),lifeKeys,decades:lifeKeys.map(k=>char.general.lifeEvents[k].decade),damageKeys},numberAndStringConstraints:'negative/fractional age, decade and damage values; arbitrary homeland; counter=21 accepted'};
const {baseMixin}=source('module/activeEffect/mixins/baseMixin.js',['baseMixin']);
const paths=baseMixin.getDamageModifcators.call({document:{parent:{system:char}}}).map(v=>v.value);
assert.equal(paths.length,21);
for(const p of paths)assert(Character.schema.getField(p.slice(7)),p);
const nested=baseMixin.getDamageModifcators.call({document:{parent:{system:{},parent:{system:char}}}});
assert.equal(nested.length,21);
assert.equal(baseMixin.getDamageModifcators.call({document:{parent:{system:{},parent:null}}}).length,0);
r.wizard={actor:21,ownedItem:21,unownedItem:0};
const get=(o,p)=>p.split('.').reduce((v,k)=>v?.[k],o);
const labelKeys=[...Object.values(char.general.details).map(d=>d.label),char.general.reputation.label,...Object.values(WITCHER.homelands),...Object.values(WITCHER.socialStanding),...damageKeys.map(k=>'WITCHER.DamageType.'+k),'WITCHER.Effect.wizard.flat','WITCHER.Effect.wizard.multi','WITCHER.Effect.wizard.applyAP','WITCHER.Effect.wizard.resistances'];
r.localizations={};
for(const lang of ['en','ru']){
 const content=utils.expandObject(JSON.parse(fs.readFileSync('lang/'+lang+'.json')));
 const missing=labelKeys.filter(k=>get(content,k)===undefined);assert.equal(missing.length,0);
 r.localizations[lang]={checked:labelKeys.length,missing};
}
let enrichArgs;
foundry.applications.ux={TextEditor:{implementation:{enrichHTML:async field=>{enrichArgs=field;return '<processed>'+field+'</processed>'}}}};
char.general.background.value='<p>History</p>';
const enriched=(await char.enrichedText()).general.background;
assert.equal(enrichArgs,'<p>History</p>');
assert.equal(enriched.value,enrichArgs);
assert.equal(enriched.systemField,Character.schema.getField('general.background.value'));
r.enrichment={value:enriched.value,enriched:enriched.enriched,field:enriched.systemField.fieldPath};
const lifeModel=new Character({general:{lifeEvents:{10:{value:'first'},110:{value:'eleventh'}}}});
const before=lifeModel.toObject();
const updates=[];
const actor={system:lifeModel,update:data=>{updates.push(data);return Promise.resolve(data)}};
class FakeBase {async _prepareContext(){return {actor,system:actor.system}}}
const sheetText=fs.readFileSync('module/actor/sheets/WitcherCharacterSheet.js','utf8');
const method=sheetText.slice(sheetText.indexOf('    async _prepareContext(options) {'),sheetText.indexOf('    async _prepareCharacterData(context) {'));
const context={...baseGlobals,FakeBase};
vm.runInNewContext('this.Sheet=class extends FakeBase {\n'+method+'\n};',context);
const sheet=new context.Sheet();
for(const name of ['_prepareCharacterData','_prepareDiagramFormulas','_prepareCrafting','_prepareSubstances','_prepareAlchemy','_prepareValuables'])sheet[name]=()=>{};
sheet._prepareAlchemyComponentsList=()=>[];sheet._prepareTabs=()=>({});
sheet.document={system:lifeModel};
const prepared=await sheet._prepareContext({});
assert.equal(prepared.system,lifeModel);
assert(Array.isArray(lifeModel.general.lifeEvents));
assert.equal(lifeModel.toObject(false).general.lifeEvents['10'].value,'eleventh');
assert.equal(lifeModel.toObject(false).general.lifeEvents['20'],undefined);
assert.deepEqual(lifeModel.toObject(),before);
const parentText=fs.readFileSync('module/actor/sheets/WitcherActorSheet.js','utf8');
const toggle=parentText.slice(parentText.indexOf('    _onLifeEventDisplay(event) {'),parentText.indexOf('\n}\n',parentText.indexOf('    _onLifeEventDisplay(event) {')));
vm.runInNewContext('this.Toggle=class {\n'+toggle+'\n};',context);
context.Toggle.prototype._onLifeEventDisplay.call({actor},{preventDefault(){},currentTarget:{closest:()=>({dataset:{event:'10'}})}});
assert.equal(updates[0]['system.general.lifeEvents.10.isOpened'],true);
r.lifeEvents={preparedIsArray:true,derivedKey10:lifeModel.toObject(false).general.lifeEvents['10'].value,derivedKey20:String(lifeModel.toObject(false).general.lifeEvents['20']),sourceUnchanged:true,toggleUpdate:updates[0]};
const {damageUtilMixin}=source('module/actor/mixins/damageUtilMixin.js',['damageUtilMixin']);
const {armorMixin}=source('module/actor/mixins/armorMixin.js',['armorMixin']);
const {damageMixin}=source('module/actor/mixins/damageMixin.js',['damageMixin']);
const damageActor={system:new Common({}),...damageUtilMixin,...armorMixin,...damageMixin};
const properties={armorPiercing:false,improvedArmorPiercing:false,bypassesWornArmor:false,bypassesNaturalArmor:false};
const damage={type:'fire',properties,location:{name:'torso',formula:1}};
const armor={system:{resistance:{fire:true}}};
damageActor.system.damageTypeModification.fire={flat:0,multiplication:0.5,applyAP:true};
let error;
try{damageActor.calculateArmorResistances(DamageInstance.create(10).setType('fire'),damage,{})}catch(e){error={name:e.name,message:e.message}}
assert.equal(error?.name,'TypeError');
assert.equal(damageActor.calculateArmorResistances(DamageInstance.create(10).setType('fire'),{...damage,properties:{...properties,armorPiercing:true}},{}).damage,10);
r.applyAP={nonPiercing:error,piercingDamage:10};
damageActor.system.damageTypeModification.fire.applyAP=false;
r.multiplication={};
for(const [name,armorSet] of Object.entries({none:{},worn:{lightArmor:armor},natural:{naturalArmor:armor},both:{lightArmor:armor,naturalArmor:armor}})){
 r.multiplication[name]=damageActor.calculateArmorResistances(DamageInstance.create(10).setType('fire'),damage,armorSet).damage;
}
assert.deepEqual(r.multiplication,{none:10,worn:2,natural:2,both:0});
damageActor.getLocationArmor=()=>({armorSet:{},totalSP:0,displaySP:0});
damageActor.applyAlwaysSpDamage=async()=>0;damageActor.applySpDamage=async()=>0;
r.flat=[];
damageActor.system.damageTypeModification.fire.multiplication=1;
for(const flat of [-3,0,3]){
 damageActor.system.damageTypeModification.fire.flat=flat;
 const result=await damageActor.calculateDamageWithLocation({},damage,[DamageInstance.create(10).setType('fire')]);
 r.flat.push({flat,result:result.damageInstances.map(i=>i.damage),types:result.damageInstances.map(i=>i.type)});
}
assert.deepEqual(r.flat.map(v=>v.result),[[10],[10],[10,3]]);
const {skillMixin}=source('module/actor/mixins/skillMixin.js',['skillMixin'],{});
r.social=[];
for(const [standing,attribute,skill,expected] of [['tolerated','emp','charisma','-1'],['hatedFeared','emp','charisma','-2-1'],['feared','will','intimidation','+1'],['equal','emp','charisma','']]){
 const value=skillMixin.addSocialStanding.call({type:'character',system:{general:{socialStanding:standing}}},{name:attribute},skill);
 assert.equal(value,expected);r.social.push({standing,attribute,skill,value});
}

const helpers={};
const Handlebars={registerHelper:(name,fn)=>{if(typeof name==='object')Object.assign(helpers,name);else helpers[name]=fn},createFrame:d=>({...d})};
const {registerHandelbarHelpers}=source('module/setup/handlebars.js',['registerHandelbarHelpers'],{Handlebars});
await registerHandelbarHelpers();
const emitted=[];
helpers.eachLimit(prepared.system.general.lifeEvents,2,{fn:v=>{emitted.push(v.lifeEvent.key);return ''}});
assert.deepEqual(emitted,['10','20']);
let overflow=0;
helpers.eachLimit(prepared.system.general.lifeEvents,21,{fn:v=>{if(v.lifeEvent===undefined)overflow++;return ''}});
assert.equal(overflow,1);
r.eachLimit={firstTwo:emitted,undefinedAt21:overflow};
const jsonFiles=[];
function walk(dir){for(const e of fs.readdirSync(dir,{withFileTypes:true})){const p=dir+'/'+e.name;if(e.isDirectory())walk(p);else if(p.endsWith('.json'))jsonFiles.push(p)}}
walk('packsJson');
const refs=[];
function scan(value,file,path=''){
 if(typeof value==='string'&&/^system\.(?:general(?:\.|$)|damageTypeModification(?:\.|$))/.test(value))refs.push({file,path,value});
 else if(value&&typeof value==='object')for(const [k,v] of Object.entries(value))scan(v,file,path+'.'+k);
}
for(const file of jsonFiles)scan(JSON.parse(fs.readFileSync(file)),file);
assert.equal(refs.length,0);r.packs={files:jsonFiles.length,refs};

console.log(JSON.stringify(r));

JS
```

Результат: exit 0. Вывод:

```text
{"defaults":{"generalKeys":["background","details","homeland","reputation","socialStanding","name","race","age","lifeEvents"],"detailsKeys":["clothing","personality","hairStyle","affectations","valuedPerson","value","feelingsOnPeople"],"lifeKeys":["10","20","30","40","50","60","70","80","90","100","110","120","130","140","150","160","170","180","190","200"],"decades":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],"damageKeys":["slashing","piercing","bludgeoning","elemental","electricity","fire","ice"]},"numberAndStringConstraints":"negative/fractional age, decade and damage values; arbitrary homeland; counter=21 accepted","wizard":{"actor":21,"ownedItem":21,"unownedItem":0},"localizations":{"en":{"checked":51,"missing":[]},"ru":{"checked":51,"missing":[]}},"enrichment":{"value":"<p>History</p>","enriched":"<processed><p>History</p></processed>","field":"system.general.background.value"},"lifeEvents":{"preparedIsArray":true,"derivedKey10":"eleventh","derivedKey20":"undefined","sourceUnchanged":true,"toggleUpdate":{"system.general.lifeEvents.10.isOpened":true}},"applyAP":{"nonPiercing":{"name":"TypeError","message":"Cannot read properties of undefined (reading 'armorPiercing')"},"piercingDamage":10},"multiplication":{"none":10,"worn":2,"natural":2,"both":0},"flat":[{"flat":-3,"result":[10],"types":["fire"]},{"flat":0,"result":[10],"types":["fire"]},{"flat":3,"result":[10,3],"types":["fire",null]}],"social":[{"standing":"tolerated","attribute":"emp","skill":"charisma","value":"-1"},{"standing":"hatedFeared","attribute":"emp","skill":"charisma","value":"-2-1"},{"standing":"feared","attribute":"will","skill":"intimidation","value":"+1"},{"standing":"equal","attribute":"emp","skill":"charisma","value":""}],"eachLimit":{"firstTwo":["10","20"],"undefinedAt21":1},"packs":{"files":226,"refs":[]}}
(node:654963) [MODULE_TYPELESS_PACKAGE_JSON] Warning: Module type of file:///var/lib/foundryvtt/Data/systems/TheWitcherTRPG-RB-Version/module/data/actor/characterData.js is not specified and it doesn't parse as CommonJS.
Reparsing as ES module because module syntax was detected. This incurs a performance overhead.
To eliminate this warning, add "type": "module" to /var/lib/foundryvtt/Data/systems/TheWitcherTRPG-RB-Version/package.json.
(Use `node --trace-warnings ...` to show where the warning was created)
```

При первом запуске проверки переводов использовался поиск по необработанному JSON: составной background.other оказался ложно отмечен как отсутствующий. Проверен загрузчик Foundry, сценарий исправлен на настоящий foundry.utils.expandObject и повторён успешно. Проблема локализации не регистрировалась. Предупреждение Node MODULE_TYPELESS_PACKAGE_JSON относится к загрузке ES modules в изолированном сценарии; package.json не менялся.

Подмены: game.settings/i18n; базовый контекст листа и соседние подготовки; Actor.update как запись аргументов в массив; TextEditor; регистрация Handlebars/createFrame; данные брони и операции SP. Импортированы настоящие DataModel/TypeDataModel/fields и фабрики системы, методы вычислений и DamageInstance. _prepareContext и _onLifeEventDisplay взяты из исходного текста без изменения тел. Сохранение, HTTP/DOM, полный лист, бой, правила игры, длительность эффектов и весь цикл подготовки Actor не проверены.

### Проверка документации и состава

После оформления выполнены сверка 621 пути с Git/фактическим деревом и байтов с базовым срезом/HEAD; контроль SHA256 исходников; сравнение mode/uid/gid/inode всех ранее отслеживаемых файлов; соответствие карточек строкам реестра; обязательные разделы и поля всех восьми карточек; уникальные issues/status potential; состояния задач; существование локальных Markdown-ссылок и якорей; структура таблиц и git diff --check. Существующие записи журнала сверены с HEAD без изменений.

Итог проверки: exit 0. Реестр — 621 исходник, 41 проверенная карточка, 580 файлов не разобраны; добавлены восемь карточек. Все 27 issues находятся в potential. Проверены 110 Markdown-документов и 2547 локальных ссылок; изменены или созданы 29 документов. Содержимое исходников и mode/uid/gid/inode всех 776 ранее отслеживаемых файлов сохранены; git diff --check прошёл. Историческая часть журнала совпала с HEAD. TASK-0003.004 завершена, родительская TASK-0003 остаётся in-progress; следующая TASK-0003.005 — planned.

## TASK-0003.003

Дата: 2026-09-10. Ветка `rusbar-main`, HEAD `c34b790379fd98cd7e33ccbeeca085e49297a40f`. Рабочее дерево на старте чистое; отслеживались 763 файла. Все 621 исходник совпали со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. Foundry 14.367.0 по /opt/foundryvtt/package.json, Node 24.16.0.

Прочитаны полностью восемь файлов из module/data/actor/templates/common, всего 129 строк: adrenalineData.js (8), currencyData.js (13), focusData.js (9), lifepathData.js (15), noteData.js (9), reputationData.js (20), temporaryEffectsData.js (14), combatEffectsData.js (41). Полное покрытие соседних моделей, листов и обработчиков из этих точечных чтений не выводится.

### Содержательная и перекрёстная сверка

| Направление | Источники и фактический результат |
| --- | --- |
| Файлы ↔ карточки | Сверены все поля восьми файлов, default exports, методы Reputation, наследование DataModel, прямые импорты и внешние вызовы фабрик. |
| Вложение ↔ владельцы | CommonActorData содержит семь непосредственно подключаемых структур порции; TemporaryEffects вложена через combatEffects. Currency дополнительно используется LootData; focus() вызывается четыре раза; notes — ArrayField. |
| Адреналин ↔ потребители | value/label, миграция current→value, настройка useOptionalAdrenaline, кнопки +/- и query из ветки crit. addAdrenaline при разрешении сформировал update value=1; при запрете записи нет. |
| Валюты ↔ модель, курсы и операции | Семь ключей совпали с WITCHER.currency; шесть курсов, falsecoin исключён. Сумма 28 монет даёт вес 0.028 в Common/Loot. Нормальный обмен crown100, amount10→oren дал 90/10; crown→crown дал 110. |
| Focus ↔ форма и castSpell | Четыре независимых слота name/value, чтение положительных значений в focusOptions, два выбора, вычитание из стоимости STA, минимум итоговой стоимости 1. Полный castSpell не запускался. |
| Notes ↔ формы и обработчики | Пустой ArrayField, push/splice и запись массива проверены исходными методами. Шаблоны показывают отдельно Item.note (oldNotes) и массивные записи. Кнопки создания текущих шаблонов — add-item, .add-note вне listener не найдена. |
| Lifepath ↔ schema/подсказки/формула | Четыре скалярных поля и attacks.<ключ>.value. Схемное strong={value:2} дало ` -3+[object Object]`; подсказки strong/joint не содержат .value. |
| Reputation ↔ stat/подготовка/бросок | Пять полей stat; миграция и подготовка на трёх входах дали max 0/7/4. Common.prepareBaseData сам копирует базу, Actor.calculateStats — max в value; два режима броска прочитаны. |
| Локализация ↔ label | WITCHER.Actor.DerStat.Rep отсутствует в восьми языках. WITCHER.Actor.Adrenaline есть в семи, отсутствует в it; en/ru содержат перевод. Fallback клиента не запускался. |
| Боевые записи ↔ config/JSON | 11 changes statusEffects под combatEffects: 5 записей начала хода, 6 модификаторов. 17 строковых путей из 226 JSON, в 17 файлах, все соответствуют схемам; 16 целых записей и один damage.modifier. |
| attack/defenseModifier ↔ формулы | Записи -2/-3 дают строки ` -2[a]` / ` -3[d]`, ноль пропускается. defenseMixin повторно определяет addDefenseModifiers после modifierMixin. |
| turnStartEffects ↔ обработчик | Урон 5+2=7, флаги повреждения переданы, но тип fire потерян до DamageInstance. nonLethal выбирает sta. При heal.amount3/modifier2, HP5/20 записывается 8. |
| TemporaryEffects ↔ лист/расход | Только словарь temporaryHp; temporaryHpSum добавляет лист, не схема. Два значения 3/4 дают сумму 7. При расходе составного эффекта (tempHP3 + attack5) урон6 меняет attack до2 и сохраняет HP10. |
| Ранее описанные зависимости ↔ новые карточки | Уточнены config, registerDataModels, settings, hooks и statData. Дополнены issue-00006/00011/00014 без дубликатов. |

Основные поиски выполнялись через rg по именам фабрик/классов и полям adrenaline, currency, focus1–4, lifepathModifiers, notes, reputation, combatEffects, turnStartEffects, temporaryHp в module/templates. Каждый найденный существенный потребитель прочитан до конкретного обращения; индексы JSON приведены в карточке combatEffectsData.js. Отсутствие прямого пути в JSON не исключает динамическое построение.

В ядре прочитаны DataModel/TypedObjectField/SchemaField и Actor.applyActiveEffects: активные документы собираются через allApplicableEffects, изменения применяются к подготовленным данным в фазах initial/final. Управление документом-источником в системе сверено с onManageActiveEffect delete/toggle. Автоматическое истечение и полный пересчёт после удаления в клиенте не воспроизводились.

### Изолированные проверки

Следующая команда выполнена из корня репозитория. Реальны классы данных/поля и utils Foundry, модели системы, config.js, DamageInstance и указанные исходные методы. Код методов загружается в vm со строгим режимом. Подменены GUI, i18n/settings, ChatMessage и запись Actor/ActiveEffect. В цепочке урона настоящий applyDamageFromStatus доходит до перехваченного Actor.applyDamage; итоговые сопротивления/HP не вычисляются. В проверке смешанного временного эффекта настоящим является updateDerivedStat, документы заменены минимальными объектами.

```bash
node --input-type=module <<'JS'
import fs from 'node:fs';
import vm from 'node:vm';
import assert from 'node:assert/strict';
await import('/opt/foundryvtt/common/primitives/_module.mjs');
const fields=await import('/opt/foundryvtt/common/data/fields.mjs');
const {default:DataModel}=await import('/opt/foundryvtt/common/abstract/data.mjs');
const {default:TypeDataModel}=await import('/opt/foundryvtt/common/abstract/type-data.mjs');
const utils=await import('/opt/foundryvtt/common/utils/helpers.mjs');
globalThis.foundry={data:{fields},abstract:{DataModel,TypeDataModel},utils,applications:{api:{DialogV2:{}}}};
const {default:Common}=await import('./module/data/actor/commonActorData.js');
const {default:Loot}=await import('./module/data/actor/lootData.js');
const {default:Reputation}=await import('./module/data/actor/templates/common/reputationData.js');
const {default:TemporaryEffects}=await import('./module/data/actor/templates/common/temporaryEffectsData.js');
const {WITCHER}=await import('./module/setup/config.js');
const CONFIG={WITCHER};
const get=(o,p)=>p.split('.').reduce((v,k)=>v?.[k],o);
const copy=o=>JSON.parse(JSON.stringify(o));
const fresh=new Common({});
const r={defaults:Object.fromEntries(['adrenaline','currency','focus1','focus2','focus3','focus4','lifepathModifiers','notes','reputation','combatEffects'].map(k=>[k,copy(fresh[k])]))};
assert.equal(fresh.notes.length,0);
assert.equal(fresh.currency.crown,0);
assert.equal(fresh.combatEffects.temporaryEffects.temporaryHpSum,undefined);
assert.equal(fresh.focus1.name,'');assert.equal(fresh.focus1.value,0);
fresh.focus1.value=3;assert.equal(fresh.focus2.value,0);
assert.deepEqual(Object.keys(fresh.currency),Object.keys(WITCHER.currency));
assert.deepEqual(Object.keys(WITCHER.currencyRates),Object.keys(fresh.currency).filter(k=>k!=='falsecoin'));
const wallet={bizant:1,ducat:2,lintar:3,floren:4,crown:5,oren:6,falsecoin:7};
assert.equal(new Common({currency:wallet}).calcCurrencyWeight(),0.028);
assert.equal(new Loot({currency:wallet}).calcCurrencyWeight(),0.028);
r.currencyWeight=0.028;
r.reputation=[];
for(const input of [{max:7},{max:7,unmodifiedMax:0},{max:7,unmodifiedMax:4}]){
 const model=new Reputation({...input});model.prepareBaseData();
 const common=new Common({reputation:{...input}});common.prepareBaseData();
 assert.equal(model.max,common.reputation.max);
 r.reputation.push({input,max:model.max,unmodifiedMax:model.unmodifiedMax});
}
assert.deepEqual(r.reputation.map(v=>v.max),[0,7,4]);
assert.equal(new Common({adrenaline:{current:3}}).adrenaline.value,3);
assert.equal(new Common({adrenaline:{value:2,current:3}}).adrenaline.value,2);
assert.equal(new Common({adrenaline:{value:0,current:3}}).adrenaline.value,3);
r.adrenalineMigration=[3,2,3];
let settings={useOptionalAdrenaline:true};
const game={settings:{get:(s,k)=>settings[k]??false},i18n:{localize:k=>k,format:k=>k},user:{isActiveGM:true,id:'test'}};
const baseGlobals={foundry,CONFIG,game,CONST:{CHAT_MESSAGE_STYLES:{OTHER:0}},ChatMessage:{create:()=>{},getSpeaker:()=>({}),applyMode:()=>{}}};
function source(file,names,extra={}){
 const code=fs.readFileSync(file,'utf8').replace(/^import .*;\r?$/gm,'').replace(/^export \{[^\n]*\};?\r?$/gm,'').replace(/^export (?=(?:async )?(?:function|let|const|class))/gm,'');
 const ctx={...baseGlobals,...extra};vm.runInNewContext("'use strict';\n"+code+'\nglobalThis.result={'+names.join(',')+'};',ctx);return ctx.result;
}
const {adrenalineMixin}=source('module/actor/mixins/adrenalineMixin.js',['adrenalineMixin']);
const adrenalineUpdates=[];
const adrenalineActor={system:fresh,update:u=>adrenalineUpdates.push(u)};
await adrenalineMixin.addAdrenaline.call(adrenalineActor);
settings.useOptionalAdrenaline=false;await adrenalineMixin.addAdrenaline.call(adrenalineActor);
assert.equal(adrenalineUpdates.length,1);assert.equal(adrenalineUpdates[0]['system.adrenaline.value'],1);
const {noteMixin}=source('module/actor/sheets/mixins/noteMixin.js',['noteMixin']);
const noteWrites=[],noteActor={system:fresh,update:u=>noteWrites.push(copy(u))};
await noteMixin._onNoteAdd.call({actor:noteActor});
assert.deepEqual(copy(fresh.notes),[{title:'',details:''}]);
await noteMixin._onNoteDelete.call({actor:noteActor},{currentTarget:{dataset:{noteIndex:'0'}}});
assert.equal(fresh.notes.length,0);r.noteWrites=noteWrites;
const {baseMixin}=source('module/activeEffect/mixins/baseMixin.js',['baseMixin']);
r.lifepathSuggestions=baseMixin.getLifepathSuggestions();
const attackData=new Common({lifepathModifiers:{attacks:{strong:{value:2}}}});
const {weaponAttackMixin}=source('module/actor/mixins/weaponAttackMixin.js',['weaponAttackMixin']);
r.strikeFormula=weaponAttackMixin.handleStrikeType.call({system:attackData},'strong',false);
assert(r.strikeFormula.includes('[object Object]'));
r.strikeFieldClasses={outer:attackData.schema.getField('lifepathModifiers.attacks').constructor.name,element:attackData.schema.getField('lifepathModifiers.attacks').element.constructor.name};
assert(attackData.schema.getField('lifepathModifiers.attacks').element instanceof fields.SchemaField);
assert(attackData.schema.getField('lifepathModifiers.attacks').element.fields.value instanceof fields.NumberField);
const {modifierMixin}=source('module/actor/mixins/modifierMixin.js',['modifierMixin']);
const mods=new Common({combatEffects:{attackModifier:{a:{name:'a',value:-2},zero:{name:'zero',value:0}},defenseModifier:{d:{name:'d',value:-3}}}});
r.modifierStrings={attack:modifierMixin.addAttackModifiers.call({system:mods}),defense:modifierMixin.addDefenseModifiers.call({system:mods})};
assert.equal(r.modifierStrings.attack,' -2[a]');assert.equal(r.modifierStrings.defense,' -3[d]');
let dialogResult;
foundry.applications={api:{DialogV2:{input:async()=>dialogResult}},handlebars:{renderTemplate:async()=>''}};
const {currencyConverterMixin}=source('module/actor/mixins/currencyConverterMixin.js',['currencyConverterMixin']);
r.conversions=[];
for(const to of ['oren','crown']){
 const updates=[],data=new Common({currency:{crown:100}});
 dialogResult={amount:10,from:'crown',to,fee:0};
 await currencyConverterMixin.openCurrencyConverter.call({system:data,name:'test',getCurrencyRates:currencyConverterMixin.getCurrencyRates,update:async u=>updates.push(copy(u))});
 r.conversions.push({to,updates});
 assert.equal(updates[0]['system.currency.crown'],to==='oren'?90:110);
}
const {DamageInstance}=await import('./module/scripts/damageInstance.js');
const {applyDamageFromStatus}=source('module/scripts/combat/applyDamage.js',['applyDamageFromStatus'],{DamageInstance});
const {applyCombatEffect,applyCombatEffects,applyGeneralCombatHooks}=source('module/scripts/combat/generalCombatHook.js',['applyCombatEffect','applyCombatEffects','applyGeneralCombatHooks'],{applyDamageFromStatus});
const {healMixin}=source('module/actor/mixins/healMixin.js',['healMixin']);
const statusData=new Common({derivedStats:{hp:{value:5,max:20}},combatEffects:{turnStartEffects:{
 fire:{name:'fire',damage:{amount:5,modifier:2,type:'fire',allLocations:true,ignoreArmor:true,bypassesShield:true,spDamage:1}},
 heal:{name:'heal',heal:{amount:3,modifier:2}}
}}});
const damageCalls=[],healUpdates=[];
const statusActor={system:statusData,type:'character',getLocationObject:()=>({name:'torso'}),applyDamage:(dialog,instances,props,stat)=>damageCalls.push({instances:instances.map(i=>({damage:i.damage,type:i.type??null})),props,stat}),update:async u=>healUpdates.push(copy(u)),calculateHealValue:healMixin.calculateHealValue,createHealMessage:async()=>{}};
await applyCombatEffect(statusActor,statusData.combatEffects.turnStartEffects.fire);
await applyCombatEffect(statusActor,statusData.combatEffects.turnStartEffects.heal);
assert.equal(damageCalls[0].instances[0].damage,7);assert.equal(damageCalls[0].instances[0].type,null);
assert.equal(healUpdates[0]['system.derivedStats.hp.value'],8);
const nonlethal=new Common({combatEffects:{turnStartEffects:{test:{damage:{amount:1,modifier:2,nonLethal:true}}}}});
await applyCombatEffect(statusActor,nonlethal.combatEffects.turnStartEffects.test);
assert.equal(damageCalls[1].stat,'sta');
r.statusDamage=damageCalls;r.statusHeal=healUpdates;
const tempData=new TemporaryEffects({temporaryHp:{one:{name:'one',value:3},two:{name:'two',value:4}}});
assert.equal(Object.values(tempData.temporaryHp).reduce((s,t)=>s+t.value,0),7);
const {damageMixin}=source('module/actor/mixins/damageMixin.js',['damageMixin']);
const effectWrites=[],hpWrites=[];
const effect={system:{changes:[
 {key:'system.combatEffects.temporaryEffects.temporaryHp.test',value:'{"name":"temp","value":3}'},
 {key:'system.combatEffects.attackModifier.test',value:'{"name":"attack","value":5}'}
]},update:async u=>effectWrites.push(copy(u))};
await damageMixin.updateDerivedStat.call({system:{derivedStats:{hp:{value:10}}},temporaryEffects:[effect],update:async u=>hpWrites.push(copy(u))},6,'hp');
assert.equal(JSON.parse(effect.system.changes[1].value).value,2);
assert.equal(hpWrites[0]['system.derivedStats.hp.value'],10);
r.mixedTemporaryEffect={changes:effect.system.changes,updates:effectWrites,hpWrites};
r.statusDefinitions=WITCHER.statusEffects.flatMap(s=>(s.changes??[]).filter(c=>c.key.startsWith('system.combatEffects.')).map(c=>({status:s.id,key:c.key,value:JSON.parse(c.value)})));
import path from 'node:path';
const files=[];function list(dir){for(const e of fs.readdirSync(dir,{withFileTypes:true})){const p=path.posix.join(dir,e.name);if(e.isDirectory())list(p);else if(p.endsWith('.json'))files.push(p);}}list('packsJson');
const prefixes=['system.adrenaline','system.currency','system.focus','system.lifepathModifiers','system.notes','system.reputation','system.combatEffects'];
const refs=[];function walk(o,file,p=''){if(!o||typeof o!=='object')return;for(const[k,v]of Object.entries(o)){if(typeof v==='string'&&prefixes.some(x=>v.startsWith(x)))refs.push({file,path:p+'.'+k,key:v,change:o});walk(v,file,p+'.'+k);}}
for(const f of files)walk(JSON.parse(fs.readFileSync(f,'utf8')),f);
assert.equal(files.length,226);assert.equal(refs.length,17);
const errors=[];
for(const ref of refs){
 const relative=ref.key.slice('system.'.length);
 const field=fresh.schema.getField(relative,{source:fresh.toObject()});
 if(!field)errors.push(ref.key);
 if(relative.endsWith('.modifier')){assert(field instanceof fields.NumberField);continue;}
 const id=relative.split('.').at(-1);
 const data=new Common({combatEffects:{turnStartEffects:{[id]:JSON.parse(ref.change.value)}}});
 assert.equal(typeof data.combatEffects.turnStartEffects[id].damage.amount,'number');
}
assert.deepEqual(errors,[]);
r.packRefs={files:files.length,references:refs.length,sourceFiles:new Set(refs.map(x=>x.file)).size,paths:[...new Set(refs.map(x=>x.key))],invalid:errors};
const samples=new Common({combatEffects:{attackModifier:{test:{}},turnStartEffects:{test:{}}}});
r.emptyEntries={modifier:copy(samples.combatEffects.attackModifier.test),turn:copy(samples.combatEffects.turnStartEffects.test)};
const langKeys=['WITCHER.Actor.Adrenaline','WITCHER.Actor.DerStat.Rep'];
const langs=fs.readdirSync('lang').filter(f=>f.endsWith('.json'));
r.localizations=Object.fromEntries(langKeys.map(key=>[key,langs.filter(file=>get(JSON.parse(fs.readFileSync('lang/'+file,'utf8')),key)===undefined)]));
assert.equal(r.localizations['WITCHER.Actor.DerStat.Rep'].length,8);

for(const d of r.statusDefinitions){
 const data=utils.expandObject({[d.key.slice(7)]:d.value});
 const model=new Common(data);
 const value=get(model,d.key.slice(7));
 assert(value && typeof value==='object');
}
assert.equal(r.statusDefinitions.length,11);
console.log(JSON.stringify(r,null,2));
JS
```

Результат: **exit 0**, все assert прошли. Основные результаты записаны в таблице выше и карточках issues. Для сериализации перехваченного типа урона undefined заменён null; это не утверждение, что исходный DamageInstance.type равен null.

На этапе настройки сценария непустой TypedObjectField потребовал foundry.utils.isDeletionKey: после чтения определения подключён настоящий common/utils/helpers.mjs. Проверка getField по динамическому ключу без source также потребовала уточнения API: схема записи проверяется через element либо getField с source. Эти промежуточные ограничения запуска не зарегистрированы как проблемы системы. Node сообщает MODULE_TYPELESS_PACKAGE_JSON и автоматически распознаёт ES module; package.json не менялся.

### Проверка документов и сохранности

Проверяются состав реестра по Git/дереву, совпадение всех исходников с HEAD и базовым срезом, начальные хеши содержимого/метаданных, карточки, связи, статусы и Markdown. Применяются прежние исключения; ни docs, ни assets/.github не включаются в покрытие исходников.

```bash
python3 - <<'PY'
import hashlib, json, os, re, subprocess
from pathlib import Path
from urllib.parse import unquote
base='15da5b225535e34af4e132c701b5353ef4eb667f'
expected_head='c34b790379fd98cd7e33ccbeeca085e49297a40f'
registry=Path('docs/analytics/code-audit/registry.md').read_text()
rows=[line for line in registry.splitlines() if re.match(r'^\| \[[^\]]+\]\(\.\./\.\./\.\./',line)]
paths=[re.match(r'^\| \[([^\]]+)\]',r).group(1) for r in rows]
assert len(paths)==len(set(paths))==621
assert sum(r.endswith('| Проверено |') for r in rows)==33
assert sum(r.endswith('| Не начат |') for r in rows)==588
excluded={'README.md','AGENTS.md','LICENSE','.gitignore','.prettierrc','.prettierignore','jsconfig.json.default','package-lock.json','styles/fonts/thewitcher2.ttf'}
def keep(p):
 return p.split('/')[0] not in {'.git','docs','assets','.github'} and p not in excluded and not (p.startswith('packs/') and p.endswith('/LOCK'))
tracked=[p for p in subprocess.check_output(['git','ls-files','-z'],text=True).split('\0') if p]
assert set(filter(keep,tracked))==set(paths)
actual=[]
for d,dirs,files in os.walk('.'):
 if d=='.':dirs[:]=[x for x in dirs if x not in {'.git','docs','assets','.github'}]
 for f in files:
  p=(Path(d)/f).as_posix()
  if keep(p):actual.append(p)
assert set(actual)==set(paths)
assert subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip()==expected_head
for p in paths:
 b=Path(p).read_bytes()
 assert b==subprocess.check_output(['git','show',base+':'+p]),p
 assert b==subprocess.check_output(['git','show',expected_head+':'+p]),p
digest=lambda b:hashlib.sha256(b).hexdigest()
assert digest(b''.join(p.encode()+b'\0'+Path(p).read_bytes()+b'\0' for p in paths))=='9de49bf9b75194490fcfd7bfc80e2b1c8bcd9d90dd26f3603faf21d92b3d0e1e'
meta={p:[Path(p).stat().st_mode,Path(p).stat().st_uid,Path(p).stat().st_gid,Path(p).stat().st_ino] for p in tracked if Path(p).is_file()}
assert digest(json.dumps(meta,sort_keys=True).encode())=='599982e66c22b2595e038ca2d56a439cb28eb6946a1f5cd9fd522e777d2abb2d'
cards=[p for p in Path('docs/analytics/code-audit/files').rglob('*.md') if p.name!='README.md']
assert len(cards)==33
for row in rows:
 p=re.match(r'^\| \[([^\]]+)\]',row).group(1)
 c=Path('docs/analytics/code-audit/files')/(p+'.md')
 assert c.is_file()==row.endswith('| Проверено |'),p
titles=['Назначение файла','Условия использования','Введённые сущности и действия с ними','Основные функции и методы','Используемые сущности и зависимости','Известные потребители','Данные и изменения состояния','Проверки и доказательства','Непроверенные участки и открытые вопросы','Связанные проблемы','История актуализации']
for p in ["module/data/actor/templates/common/adrenalineData.js","module/data/actor/templates/common/currencyData.js","module/data/actor/templates/common/focusData.js","module/data/actor/templates/common/lifepathData.js","module/data/actor/templates/common/noteData.js","module/data/actor/templates/common/reputationData.js","module/data/actor/templates/common/temporaryEffectsData.js","module/data/actor/templates/common/combatEffectsData.js"]:
 t=Path('docs/analytics/code-audit/files/'+p+'.md').read_text()
 for title in titles:assert '## '+title in t,(p,title)
 assert expected_head in t and '| Статус анализа | Проверено |' in t
issues=list(Path('docs/issues').glob('*'+'/issue-*.md'))
assert len(issues)==23
assert {p.stem for p in issues}=={f'issue-{n:05}' for n in range(1,24)}
assert all(p.parent.name=='potential' for p in issues)
task=Path('docs/tasks/task-0003.003.md').read_text()
assert '| Статус | `done` |' in task and '- [ ]' not in task
assert '| Статус | `in-progress` |' in Path('docs/tasks/task-0003-remaining-files.md').read_text()
for n in range(4,11):
 assert '| Статус | `planned` |' in Path(f'docs/tasks/task-0003.{n:03}.md').read_text()
# Сверка точного состава порции и методов.
task_paths=re.findall(r'\[module/[^]]+\]\(\.\./\.\./(module/[^)]+)\)',task)
portion=[p for p in task_paths if '/templates/common/' in p]
assert len(portion)==len(set(portion))==8
assert sum(len(Path(p).read_text().splitlines()) for p in portion)==129
for p in portion:
 raw=Path(p).read_text()
 card=Path('docs/analytics/code-audit/files/'+p+'.md').read_text()
 for field in re.findall(r'(\w+): new fields\.',raw):
  assert field in card,(p,field)
for n in [1,2]:
 assert '| Статус | '+chr(96)+'done'+chr(96)+' |' in Path(f'docs/tasks/task-0003.{n:03}.md').read_text()
checked_links=0
mdfiles=list(Path('docs').rglob('*.md'))
def text_only(text):
 return re.sub(r'^```[^\n]*\n.*?^```[ \t]*$', '',text,flags=re.M|re.S)
def headings(text):
 out=set()
 for h in re.findall(r'^#{1,6}\s+(.+)$',text,flags=re.M):
  h=re.sub(r'\[([^\]]+)\]\([^)]+\)',r'\1',h)
  out.add(re.sub(r'[^\w\-\s]','',h.replace('`','').lower()).replace(' ','-'))
 out.update(re.findall(r'\bid=["\']([^"\']+)',text))
 return out
for f in mdfiles:
 text=re.sub(r'`+[^`]*`+', 'code', text_only(f.read_text()))
 for label,url in re.findall(r'\[([^\]\n]+)\]\(([^)\n]+)\)',text):
  if re.match(r'\w+://',url):continue
  target,_,anchor=url.partition('#')
  dest=(f.parent/unquote(target)).resolve() if target else f.resolve()
  assert dest.exists(),(str(f),url)
  if anchor:assert unquote(anchor) in headings(text_only(dest.read_text())),(str(f),url)
  checked_links+=1
changed=subprocess.check_output(['git','status','--porcelain','--untracked-files=all'],text=True).splitlines()
for row in changed:
 p=row[3:]
 assert p.startswith('docs/'),p
 raw=Path(p).read_text()
 assert all(l==l.rstrip() for l in raw.splitlines()),p
 for block in re.findall(r'(?:^\|.*\n)+',text_only(raw),flags=re.M):
  assert len({len(l.split('|')) for l in block.strip().splitlines()})==1,p
subprocess.run(['git','diff','--check'],check=True)
print(json.dumps({'source_files':621,'cards':33,'not_started':588,'new_cards':8,'potential_issues':23,'tracked_metadata_preserved':len(meta),'markdown_files':len(mdfiles),'local_links':checked_links,'changed_docs':len(changed),'source_and_metadata_hashes':'unchanged','diff_check':'passed'},ensure_ascii=False))
PY
```

Итог проверки: exit 0. Реестр — 621 исходник, 33 проверенные карточки, 588 файлов не разобраны; добавлены восемь карточек. Все 23 issues находятся в potential. Проверены 98 Markdown-документов и 2372 локальные ссылки; изменены или созданы 32 документа. Содержимое исходников и mode/uid/gid/inode всех 763 ранее отслеживаемых файлов сохранены; git diff --check прошёл. TASK-0003.003 завершена, родительская TASK-0003 остаётся in-progress; следующая TASK-0003.004 — planned.

### Наблюдения и пределы

Новые [issue-00019](../../issues/potential/issue-00019.md), [issue-00020](../../issues/potential/issue-00020.md), [issue-00021](../../issues/potential/issue-00021.md), [issue-00022](../../issues/potential/issue-00022.md), [issue-00023](../../issues/potential/issue-00023.md) находятся в potential. Дополнены [issue-00006](../../issues/potential/issue-00006.md), [issue-00011](../../issues/potential/issue-00011.md) и [issue-00014](../../issues/potential/issue-00014.md). Подтверждения пользователем и исправления не выполнялись.

Проверки не включают запуск мира/браузера, запись документов, сетевые запросы, импорт компедиумов, полный боевой цикл, экономику и соответствие рулбуку. Исходники и игровые данные не изменялись. Карточки фиксируют реальные обращения и пределы их изучения; это основание для дальнейших порций, а не доказательство исправности всей системы.

## TASK-0003.002

Дата: 2026-09-10. Ветка `rusbar-main`, HEAD `52acddd5fb7d67e993eed1ad2c89b335aef6fd1d`. На старте рабочее дерево было чистым, отслеживались 750 файлов. Все 621 исходник исследования совпали со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. Foundry 14.367.0 по `/opt/foundryvtt/package.json`; Node 24.16.0.

Полностью прочитаны девять файлов и 262 строки из module/data/actor/templates/common/skills: skillData.js (19), skillsData.js (21), bodyData.js (23), craData.js (28), dexData.js (30), empData.js (35), intData.js (41), refData.js (31), willData.js (34). Карточки и статусы соседних файлов не менялись на «Проверено» из-за чтения отдельных обращений.

### Содержательная и перекрёстная сверка

| Направление | Доказательство и результат |
| --- | --- |
| Девять исходников ↔ карточки | Полные определения, импорт Skill в 7 группах, импорт всех групп в skills(); таблицы каждого поля, подписи, миграции и способы чтения/изменения сверены. |
| Группы ↔ CommonActorData | Единственный прямой вызов skills() — CommonActorData.defineSchema:39; CharacterData и MonsterData наследуют общую модель. Семь групп содержат 13/8/5/2/10/7/7 навыков: всего 52. |
| Схема ↔ skillMap | Все 52 пары attribute.name/name существуют; каждый схемный навык имеет запись. У commonsp ключ справочника commonspeech — единственное несовпадение имён. |
| Skill ↔ поля и вычисление | 7 сохраняемых полей, getter modifiedValue=value+activeEffectModifiers; пять независимых числовых примеров, отсутствие getter в toObject. Ограничение диапазона/целочисленности в Skill не задано. |
| Группы ↔ жизненный цикл Foundry | Реальный DataModelSchemaField вызывает Skill.defineSchema() без label. В свежей CommonActorData 52 label отсутствуют; после toObject/повторной загрузки 52 подписи заполнены миграциями. Метаданные isVisible.label остаются undefined. |
| Миграции ↔ сохранность данных | Все 52 существующие записи проверены с произвольной подписью, value=3 и true-флагами: label заменяется, числовое значение и флаги сохраняются. Пустой source не получает навыков от migrateData. |
| Подписи ↔ lang | Три внешних ключа CRA отсутствуют во всех 8 языках; в skillMap отсутствуют picklock.label и trapcraft.label/rollLabel. Все 52 label после повторного создания разрешаются в en. |
| Формы ↔ поле видимости | Реальный DataField.toFormGroup с подставленным input выбирает label=isVisible. _getSkills возвращает undefined для int.commonspeech и поля для остальных 51 записи. |
| Шаблоны ↔ текущий лист монстра | PARTS.skills выбирает character/tab-skills; он передаёт навык в character/skill-display без фильтра isVisible. Изолированный HTML одинаков при false/true. Отдельный monster-skill-display скрывает запись при false. |
| Бросок ↔ модификаторы | Реальный rollSkillCheck берёт value, затем отдельно вызывает addActiveEffects. Для commonsp с value=3 и модификатором 2 сформировано 1d10 +0 +3; для awareness — 1d10 +0 +3 +2. |
| Повышение ↔ update и журнал | У spellcast 2→3 при магических очках 10 журнал -4, но update сохраняет 10; при 1 — журнал -1 magic/-3 обычных, update сохраняет magic=1 и обычные=17. |
| JSON ↔ реальные поля | Рекурсивно разобраны 226 JSON: 267 строковых ссылок в 37 файлах, 54 различных пути. 264 разрешаются в модель; 3 неверных commonspeech находятся в Torn Stomach и двух состояниях. Индекс файлов — в карточке skillsData.js. |
| Прежние карточки ↔ новые | Уточнены config.js, registerDataModels.js и TheWitcherTRPG.js: полное покрытие skillMap, вложенный Skill отдельно от Item.skill, Polyglot и языковые поля. |

Основные поиски: `rg -n 'system\.skills|skills\(\)|skillData.js|skillsData.js' module`; поиск isVisible/modifiedValue/data-action и ссылок на skill-display в templates и sheets; чтение девяти файлов целиком с номерами строк. Внешние определения прочитаны по фактически установленному ядру: `common/data/fields.mjs` (DataModelSchemaField и DataField.toFormGroup), `common/abstract/data.mjs`, `client/applications/handlebars.mjs` (renderTemplate/formGroup), `client/helpers/localization.mjs` (localize). Эти файлы не входят в реестр системы.

### Изолированные проверки

Команда выполняется из корня системы; отдельный файл сценария не добавлялся. Реальны DataModel/TypeDataModel, поля Foundry, код моделей, config.js, методы формирования путей, навыка и модификаторов, а также два шаблона. Подменены GUI-базовые классы, DOM input/createFormGroup, i18n/settings, ChatMessageData/RollConfig, пользовательский модификатор, социальные/броневые добавки, бросок, журнал и update. Формула перехватывается строкой; очки проверяются по аргументам update. В проверке повышения используется минимальный объект данных, в проверке схем и формул — настоящая CommonActorData.

```bash
node --input-type=module <<'JS'
import fs from 'node:fs';
import vm from 'node:vm';
import assert from 'node:assert/strict';
import {createRequire} from 'node:module';
await import('/opt/foundryvtt/common/primitives/_module.mjs');
const fields=await import('/opt/foundryvtt/common/data/fields.mjs');
const {default:DataModel}=await import('/opt/foundryvtt/common/abstract/data.mjs');
const {default:TypeDataModel}=await import('/opt/foundryvtt/common/abstract/type-data.mjs');
globalThis.foundry={data:{fields},abstract:{DataModel,TypeDataModel}};
const {default:Skill}=await import('./module/data/actor/templates/common/skills/skillData.js');
const {default:Common}=await import('./module/data/actor/commonActorData.js');
const {default:skills}=await import('./module/data/actor/templates/common/skills/skillsData.js');
const {WITCHER}=await import('./module/setup/config.js');
const get=(o,p)=>p?.split('.').reduce((v,k)=>v?.[k],o);
const en=JSON.parse(fs.readFileSync('lang/en.json','utf8'));
const game={i18n:{localize:k=>get(en,k)??k},settings:{get:()=>false}};
const CONFIG={WITCHER};
const models=Object.fromEntries(Object.entries(skills()).map(([g,f])=>[g,f.model]));
const fresh=new Common({});
const reload=new Common(fresh.toObject());
const result={};
const rows=Object.entries(models).flatMap(([g,M])=>Object.keys(M.schema.fields).map(k=>({g,k,field:M.schema.fields[k],fresh:fresh.skills[g][k],reload:reload.skills[g][k]})));
assert.equal(rows.length,52);
assert.deepEqual(Object.keys(Skill.schema.fields),['value','label','isVisible','activeEffectModifiers','isProfession','isPickup','isLearned']);
assert.equal(rows.filter(r=>r.fresh.label===undefined).length,52);
assert.equal(rows.filter(r=>r.reload.label&&get(en,r.reload.label)).length,52);
assert.equal(rows.filter(r=>r.fresh.schema.fields.isVisible.label===undefined).length,52);
result.schema={groups:Object.fromEntries(Object.entries(models).map(([g,M])=>[g,Object.keys(M.schema.fields).length])),skills:52,freshLabelsMissing:52,reloadedLabelsPresent:52,visibilityFieldLabelsMissing:52};
result.modifiedValues=[];
for(const [value,mod,expected] of [[0,0,0],[4,3,7],[1,-4,-3],[12,3,15],[2.5,0.5,3]]) {
 const s=new Skill({value,activeEffectModifiers:mod});
 assert.equal(s.modifiedValue,expected);assert(!Object.hasOwn(s.toObject(),'modifiedValue'));
 result.modifiedValues.push({value,mod,result:s.modifiedValue});
}
for(const [g,M]of Object.entries(models)){
 const keys=Object.keys(M.schema.fields), source=Object.fromEntries(keys.map(k=>[k,{label:'custom',value:3,isVisible:true,isProfession:true,isPickup:true,isLearned:true}]));
 const migrated=M.migrateData(source);
 assert.equal(migrated,source);
 for(const k of keys){assert.equal(source[k].label,reload.skills[g][k].label);assert.equal(source[k].value,3);for(const flag of ['isVisible','isProfession','isPickup','isLearned'])assert.equal(source[k][flag],true);}
 const empty={};M.migrateData(empty);assert.deepEqual(empty,{});
}
const langs=Object.fromEntries(fs.readdirSync('lang').filter(p=>p.endsWith('.json')).map(p=>[p,JSON.parse(fs.readFileSync('lang/'+p,'utf8'))]));
const missingFor=key=>Object.entries(langs).filter(([,l])=>typeof get(l,key)!=='string').map(([n])=>n);
result.missingOuterLabels=rows.filter(r=>missingFor(r.field.label).length===8).map(r=>({path:r.g+'.'+r.k,label:r.field.label,missingIn:missingFor(r.field.label)}));
result.missingConfigLabels=Object.entries(WITCHER.skillMap).flatMap(([id,s])=>['label','rollLabel'].filter(f=>s[f]&&missingFor(s[f]).length===8).map(f=>({id,field:f,label:s[f]})));
assert.equal(result.missingOuterLabels.length,3);
assert.equal(result.missingConfigLabels.length,3);
result.skillMap=Object.entries(WITCHER.skillMap).map(([id,s])=>({id,name:s.name,group:s.attribute.name,pathExists:!!fresh.skills[s.attribute.name]?.[s.name],sameKey:id===s.name}));
assert.equal(result.skillMap.filter(s=>s.pathExists).length,52);
assert.deepEqual(result.skillMap.filter(s=>!s.sameKey).map(s=>s.id),['commonspeech']);
foundry.applications={fields:{createFormGroup:config=>config}};
const visible=Skill.schema.fields.isVisible;
const form=visible.toFormGroup({input:{outerHTML:'stub'}}, {});
result.formLabel=form.label;
assert.equal(form.label,'isVisible');
const {baseMixin}=await import('./module/activeEffect/mixins/baseMixin.js');
globalThis.CONFIG=CONFIG;globalThis.game=game;
const suggestions=Object.values(baseMixin.getSkillSuggestions());
result.invalidSuggestions=suggestions.filter(s=>!get({system:fresh},s.value.replace('.activeEffectModifiers',''))).map(s=>s.value);
assert.deepEqual(result.invalidSuggestions,['system.skills.int.commonspeech.activeEffectModifiers']);
foundry.applications.api={HandlebarsApplicationMixin:C=>C};foundry.applications.sheets={ActorSheetV2:class{}};
foundry.utils={getProperty:get};
const {default:MonsterConfig}=await import('./module/actor/sheets/configurations/WitcherMonsterConfigurationSheet.js');
const visConfig=MonsterConfig.prototype._getSkills.call({actor:{system:fresh}});
result.missingConfigFields=Object.entries(visConfig).flatMap(([g,ss])=>Object.entries(ss).filter(([,s])=>!s.isVisible).map(([k])=>g+'.'+k));
assert.deepEqual(result.missingConfigFields,['int.commonspeech']);
const {modifierMixin}=await import('./module/actor/mixins/modifierMixin.js');
const context={CONFIG,game,ChatMessageData:class{},RollConfig:class{},getCustomModifier:async()=>'',extendedRoll:async formula=>formula};
vm.runInNewContext(fs.readFileSync('module/actor/mixins/skillMixin.js','utf8').replace(/^import .*;\r?$/gm,'').replace('export let skillMixin','const skillMixin')+'\nglobalThis.result=skillMixin;',context);
const actor={system:reload,appliedEffects:[],...modifierMixin,...context.result,addSocialStanding:()=>'',getArmorEcumbrance:()=>0};
reload.skills.int.commonsp.value=3;reload.skills.int.commonsp.activeEffectModifiers=2;
reload.skills.int.awareness.value=3;reload.skills.int.awareness.activeEffectModifiers=2;
result.formulas={commonsp:await actor.rollSkill('commonspeech'),awareness:await actor.rollSkill('awareness')};
assert(!result.formulas.commonsp.endsWith(' +2'));assert(result.formulas.awareness.endsWith(' +2'));
await assert.rejects(()=>actor.rollSkillCheck(WITCHER.skillMap.commonsp),/Cannot read properties of undefined/);
await assert.rejects(()=>actor.levelUpSkill('commonsp'),/Cannot read properties of undefined/);
await assert.rejects(()=>actor.levelUpSkill('commonspeech'),/Cannot read properties of undefined/);
result.commonspFailures=['rollSkillCheck(skillMap.commonsp)','levelUpSkill(commonsp)','levelUpSkill(commonspeech)'];
result.levelUps=[];
for(const magic of [10,1]){
 const updates=[],logs=[];
 const system={skills:{will:{spellcast:{value:2}}},magic:{magicImprovementPoints:magic},improvementPoints:20,logs:{addIpReward:(...a)=>logs.push(a)}};
 await context.result.levelUpSkill.call({system,update:u=>updates.push(u)},'spellcast');
 assert.equal(updates.length,1);assert.equal(updates[0]['system.skills.will.spellcast.value'],3);
 assert.equal(updates[0]['system.magic.magicImprovementPoints'],magic);
 assert.equal(updates[0]['system.improvementPoints'],magic===10?20:17);
 result.levelUps.push({magicBefore:magic,update:updates[0],logs});
}
const require=createRequire(import.meta.url), H=require('/opt/foundryvtt/node_modules/handlebars').create();
H.registerHelper('localize',game.i18n.localize);H.registerHelper('gte',(a,b)=>a>=b);H.registerHelper('or',(...a)=>a.slice(0,-1).some(Boolean));
const current=H.compile(fs.readFileSync('templates/partials/character/skill-display.hbs','utf8'));
const legacy=H.compile(fs.readFileSync('templates/partials/monster/monster-skill-display.hbs','utf8'));
const opt={allowProtoMethodsByDefault:true,allowProtoPropertiesByDefault:true},data={skill:reload.skills.int.awareness,name:'awareness',stat:'int'};
data.skill.isVisible=false;const hidden=current(data,opt),oldHidden=legacy(data,opt);
data.skill.isVisible=true;const shown=current(data,opt),oldShown=legacy(data,opt);
assert.equal(hidden,shown);assert(hidden.includes('data-skill="awareness"'));assert.equal(oldHidden.trim(),'');assert(oldShown.includes('awareness'));
result.visibility={currentIdentical:true,legacyHidden:true,handlebars:H.VERSION};
import path from 'node:path';
const files=[];function list(dir){for(const e of fs.readdirSync(dir,{withFileTypes:true})){const p=path.posix.join(dir,e.name);if(e.isDirectory())list(p);else if(p.endsWith('.json'))files.push(p);}}list('packsJson');
const refs=[];function walk(o,file,p=''){if(!o||typeof o!=='object')return;for(const[k,v]of Object.entries(o)){if(typeof v==='string'&&v.startsWith('system.skills.'))refs.push({file,path:p+'.'+k,key:v});walk(v,file,p+'.'+k);}}
for(const f of files)walk(JSON.parse(fs.readFileSync(f,'utf8')),f);
const invalid=refs.filter(r=>get({system:fresh},r.key)===undefined);
assert.equal(files.length,226);assert.equal(refs.length,267);assert.equal(invalid.length,3);
assert(invalid.every(r=>r.key==='system.skills.int.commonspeech.activeEffectModifiers'));
result.packPaths={jsonFiles:files.length,refs:refs.length,sourceFiles:new Set(refs.map(r=>r.file)).size,uniquePaths:new Set(refs.map(r=>r.key)).size,valid:refs.length-invalid.length,invalid};
result.skillMap={entries:result.skillMap.length,validPaths:result.skillMap.filter(s=>s.pathExists).length,mismatchedKeys:result.skillMap.filter(s=>!s.sameKey).map(s=>s.id)};
console.log(JSON.stringify(result,null,2));
JS
```

**Результат:** exit 0, все assert прошли. Фактические числа и строки записаны в таблице выше и карточках issues. Node выдал MODULE_TYPELESS_PACKAGE_JSON и автоматически распознал ES module; конфигурация пакета не изменялась.

При подготовке проверки первый вызов toFormGroup дошёл до отсутствующего DOM createCheckboxInput. Сценарий уточнён: готовый input передаётся в groupConfig, поэтому проверяется выбор label без имитации рендеринга checkbox. Ошибки первого пробного запуска не объявляются ошибками системы.

### Проверка документов и сохранности исходников

Сценарий проверяет состав путей по реестру, Git и дереву, содержимое относительно HEAD/базового среза, метаданные ранее отслеживаемых файлов (mode/uid/gid/inode), девять новых карточек, их таблицы и статусы задач, issues и локальные Markdown-ссылки. Хеши зафиксированы на старте порции.

```bash
python3 - <<'PY'
import hashlib, json, os, re, subprocess
from pathlib import Path
from urllib.parse import unquote
base='15da5b225535e34af4e132c701b5353ef4eb667f'
expected_head='52acddd5fb7d67e993eed1ad2c89b335aef6fd1d'
registry=Path('docs/analytics/code-audit/registry.md').read_text()
rows=[line for line in registry.splitlines() if re.match(r'^\| \[[^\]]+\]\(\.\./\.\./\.\./',line)]
paths=[re.match(r'^\| \[([^\]]+)\]',r).group(1) for r in rows]
assert len(paths)==len(set(paths))==621
assert sum(r.endswith('| Проверено |') for r in rows)==25
assert sum(r.endswith('| Не начат |') for r in rows)==596
excluded={'README.md','AGENTS.md','LICENSE','.gitignore','.prettierrc','.prettierignore','jsconfig.json.default','package-lock.json','styles/fonts/thewitcher2.ttf'}
def keep(p):
 return p.split('/')[0] not in {'.git','docs','assets','.github'} and p not in excluded and not (p.startswith('packs/') and p.endswith('/LOCK'))
tracked=[p for p in subprocess.check_output(['git','ls-files','-z'],text=True).split('\0') if p]
assert set(filter(keep,tracked))==set(paths)
actual=[]
for d,dirs,files in os.walk('.'):
 if d=='.':dirs[:]=[x for x in dirs if x not in {'.git','docs','assets','.github'}]
 for f in files:
  p=(Path(d)/f).as_posix()
  if keep(p):actual.append(p)
assert set(actual)==set(paths)
assert subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip()==expected_head
for p in paths:
 b=Path(p).read_bytes()
 assert b==subprocess.check_output(['git','show',base+':'+p]),p
 assert b==subprocess.check_output(['git','show',expected_head+':'+p]),p
digest=lambda b:hashlib.sha256(b).hexdigest()
assert digest(b''.join(p.encode()+b'\0'+Path(p).read_bytes()+b'\0' for p in paths))=='9de49bf9b75194490fcfd7bfc80e2b1c8bcd9d90dd26f3603faf21d92b3d0e1e'
meta={p:[Path(p).stat().st_mode,Path(p).stat().st_uid,Path(p).stat().st_gid,Path(p).stat().st_ino] for p in tracked if Path(p).is_file()}
assert digest(json.dumps(meta,sort_keys=True).encode())=='3b4ce984634e9b72300e49903549c6834564986c0ed6a5662f8ff8a0b631e0a9'
cards=[p for p in Path('docs/analytics/code-audit/files').rglob('*.md') if p.name!='README.md']
assert len(cards)==25
for row in rows:
 p=re.match(r'^\| \[([^\]]+)\]',row).group(1)
 c=Path('docs/analytics/code-audit/files')/(p+'.md')
 assert c.is_file()==row.endswith('| Проверено |'),p
titles=['Назначение файла','Условия использования','Введённые сущности и действия с ними','Основные функции и методы','Используемые сущности и зависимости','Известные потребители','Данные и изменения состояния','Проверки и доказательства','Непроверенные участки и открытые вопросы','Связанные проблемы','История актуализации']
for p in ["module/data/actor/templates/common/skills/bodyData.js","module/data/actor/templates/common/skills/craData.js","module/data/actor/templates/common/skills/dexData.js","module/data/actor/templates/common/skills/empData.js","module/data/actor/templates/common/skills/intData.js","module/data/actor/templates/common/skills/refData.js","module/data/actor/templates/common/skills/skillData.js","module/data/actor/templates/common/skills/skillsData.js","module/data/actor/templates/common/skills/willData.js"]:
 t=Path('docs/analytics/code-audit/files/'+p+'.md').read_text()
 for title in titles:assert '## '+title in t,(p,title)
 assert expected_head in t and '| Статус анализа | Проверено |' in t
issues=list(Path('docs/issues').glob('*'+'/issue-*.md'))
assert len(issues)==18
assert {p.stem for p in issues}=={f'issue-{n:05}' for n in range(1,19)}
assert all(p.parent.name=='potential' for p in issues)
task=Path('docs/tasks/task-0003.002.md').read_text()
assert '| Статус | `done` |' in task and '- [ ]' not in task
assert '| Статус | `in-progress` |' in Path('docs/tasks/task-0003-remaining-files.md').read_text()
for n in range(3,11):
 assert '| Статус | `planned` |' in Path(f'docs/tasks/task-0003.{n:03}.md').read_text()
# Содержательная сверка таблиц групп с определениями файлов.
skill_dir=Path('module/data/actor/templates/common/skills')
assert sum(len(p.read_text().splitlines()) for p in skill_dir.glob('*.js'))==262
for p in skill_dir.glob('*Data.js'):
 if p.name in {'skillData.js','skillsData.js'}:continue
 fields=re.findall(r"(\w+): new fields\.EmbeddedDataField\(Skill, \{ label: '([^']+)'",p.read_text())
 card=Path('docs/analytics/code-audit/files')/(str(p)+'.md')
 table_rows=[l for l in card.read_text().splitlines() if l.startswith('| '+chr(96))]
 assert len(fields)==len(table_rows),(p,len(fields),len(table_rows))
 for key,label in fields:
  assert any('| '+chr(96)+key+chr(96)+' | '+chr(96)+label+chr(96)+' |' in row for row in table_rows),(p,key)
assert len(re.findall(r"import .* from './", (skill_dir/'skillsData.js').read_text()))==7
assert '| Статус | '+chr(96)+'done'+chr(96)+' |' in Path('docs/tasks/task-0003.001.md').read_text()
checked_links=0
mdfiles=list(Path('docs').rglob('*.md'))
def text_only(text):
 return re.sub(r'^```[^\n]*\n.*?^```[ \t]*$', '',text,flags=re.M|re.S)
def headings(text):
 out=set()
 for h in re.findall(r'^#{1,6}\s+(.+)$',text,flags=re.M):
  h=re.sub(r'\[([^\]]+)\]\([^)]+\)',r'\1',h)
  out.add(re.sub(r'[^\w\-\s]','',h.replace('`','').lower()).replace(' ','-'))
 out.update(re.findall(r'\bid=["\']([^"\']+)',text))
 return out
for f in mdfiles:
 text=re.sub(r'`+[^`]*`+', 'code', text_only(f.read_text()))
 for label,url in re.findall(r'\[([^\]\n]+)\]\(([^)\n]+)\)',text):
  if re.match(r'\w+://',url):continue
  target,_,anchor=url.partition('#')
  dest=(f.parent/unquote(target)).resolve() if target else f.resolve()
  assert dest.exists(),(str(f),url)
  if anchor:assert unquote(anchor) in headings(text_only(dest.read_text())),(str(f),url)
  checked_links+=1
changed=subprocess.check_output(['git','status','--porcelain','--untracked-files=all'],text=True).splitlines()
for row in changed:
 p=row[3:]
 assert p.startswith('docs/'),p
 raw=Path(p).read_text()
 assert all(l==l.rstrip() for l in raw.splitlines()),p
 for block in re.findall(r'(?:^\|.*\n)+',text_only(raw),flags=re.M):
  assert len({len(l.split('|')) for l in block.strip().splitlines()})==1,p
subprocess.run(['git','diff','--check'],check=True)
print(json.dumps({'source_files':621,'cards':25,'not_started':596,'new_cards':9,'potential_issues':18,'tracked_metadata_preserved':len(meta),'markdown_files':len(mdfiles),'local_links':checked_links,'changed_docs':len(changed),'source_and_metadata_hashes':'unchanged','diff_check':'passed'},ensure_ascii=False))
PY
```

**Фактический итог:** exit 0. Реестр содержит 621 исходник: 25 карточек проверены, 596 файлов не разобраны; добавлены девять карточек. Все 18 issues находятся в potential. Проверены 85 Markdown-документов и 2130 локальных ссылок; изменены или созданы 28 документов. Содержимое 621 исходника и mode/uid/gid/inode всех 750 ранее отслеживаемых файлов сохранены. `git diff --check` прошёл. TASK-0003.002 завершена, родительская TASK-0003 остаётся in-progress; следующая TASK-0003.003 сохраняет статус planned.

### Наблюдения и пределы

Зарегистрированы [issue-00015](../../issues/potential/issue-00015.md), [issue-00016](../../issues/potential/issue-00016.md), [issue-00017](../../issues/potential/issue-00017.md), [issue-00018](../../issues/potential/issue-00018.md); дополнена [issue-00004](../../issues/potential/issue-00004.md). Все остаются potential, подтверждение пользователем и исправления не выполнялись.

Мир, браузерные клики, сохранение документов/компедиумов и полный процесс применения ActiveEffect не проверялись. Наблюдение new CommonActorData({}) не доказывает окончательное состояние Actor после клиентского/серверного цикла создания. Совпадение строковых JSON-путей не доказывает исполнение эффектов или корректность механик по рулбуку. Полный анализ соседних файлов остаётся следующим порциям.

## TASK-0003.001

Дата: 2026-09-10. Ветка `rusbar-main`, HEAD `7b7788bc614e5b7a57f8c596fb64ca75ecabd8b7`. На старте рабочее дерево было чистым; 741 отслеживаемый файл. Все 621 исходник исследования совпали со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. Версия Foundry — 14.367.0 по `/opt/foundryvtt/package.json`.

Полностью прочитаны пять файлов, 143 строки: dataUtils.js (7), valueLabelData.js (8), statData.js (11), statsData.js (70), derivedStatsData.js (47). Соседние определения и потребители проверялись в пределах связей и не получили статуса завершённого пофайлового анализа.

### Содержательная и перекрёстная сверка

| Проверка | Результат | Пределы |
| --- | --- | --- |
| Определения и импорты | createEnrichedText: 5 импортирующих моделей и 20 вызовов; valueLabel: 2 импортирующие фабрики и 8 вызовов; stat: 3 модели и 23 вызова; Stats/DerivedStats импортируются CommonActorData | Поиск по module и чтение определений/обращений; не анализ внешних модулей и макросов миров |
| Поля | Stats содержит 10 записей, DerivedStats — 12; stat создаёт 5 полей каждой записи; valueLabel — 2 | Наличие поля не подтверждает правильность всех потребителей |
| Пределы чисел | Фабрика stat не задаёт min/max; настоящие NumberField сохраняют -3, 0 и 15; integer округляет 2.6 до 3, value=2.5 сохраняется | Это поведение модели, не вывод о правилах игры |
| Подготовка | Stats.prepareBaseData только копирует unmodifiedMax в max, не меняет value/totalModifiers и идемпотентен; основной путь Actor выполняет копирование в CommonActorData | Прямой вызов Stats в проверке не означает автоматический вызов вложенной модели ядром |
| Миграция | Все 10 статов и ровно 6 производных записей имеют перенос при ==0; отсутствующее поле его не вызывает | Установлено на реальных моделях; реальные старые документы мира не исследовались |
| statMap | 9 stats + 11 derivedStats с непустым origin имеют корректные пути totalModifiers; reputation имеет пустой origin; toxicity и shield отсутствуют в справочнике | Для toxicity проверен отдельный getToxSuggestions; различия не объявлены ошибкой |
| Чтение и запись | Разделены построение схем, вычисления подготовленных значений, source-миграция и update ресурсов у потребителей | Полный Actor/Item, бой, формы и эффекты остаются будущим порциям |
| Контракт текста | createEnrichedText ожидает enrichHTML, затем получает поле схемы; исходное value сохранено; исключение распространяется; неизвестный путь даёт undefined | TextEditor подменён, схема и getField настоящие |
| Шаблоны | Прослежены результаты моделей через листы в формы; исходный HBS знаний монстра передаёт value вместо enriched в 3 полях | Handlebars 4.7.9 настоящий; formGroup/localize/TextEditor подменены |
| Локализация | Из 31 проверенного ключа фабрик 30 есть в en/ru; отсутствующий WITCHER.Actor.DerStat.Rep не найден во всех 8 языках | Переводы остальных ключей в других языках и UI локализации не проверялись |
| Компедиумы | В 48 JSON найдены точные key-пути к исследуемым данным: 45 файлов с system.stats и 8 с system.derivedStats, с пересечением | Документы и effects целиком не разобраны; пути перечислены в карточках моделей |
| Взаимная согласованность | Карточка config дополнена соответствием statMap схемам; карточка registerDataModels — вложением Stats/DerivedStats и отсутствием отдельной регистрации этих классов/фабрик | Не расширяет завершённый разбор на CommonActorData или другие соседние файлы |

### Наблюдения

Зарегистрированы только в `potential`:

- [issue-00011](../../issues/potential/issue-00011.md): отсутствие unmodifiedMax не обрабатывается переносом max; в реальной CommonActorData входные int.max=7 и vigor.max=7 без базы после подготовки дали 0.
- [issue-00012](../../issues/potential/issue-00012.md): два прохода calculateStats дали luck.max=14 при базе 10/+2 и toxicity.max=110 при базе 100/+5. Проверены исходные prepareDerivedData/calculateStats, соседние методы подменены.
- [issue-00013](../../issues/potential/issue-00013.md): в аргумент enriched формы знаний монстра попал исходный текст, несмотря на подготовленный результат модели.
- [issue-00014](../../issues/potential/issue-00014.md): отсутствующий ключ подписи числовой репутации передаётся в метаданные поля, которые использует автодополнение ActiveEffect.

С существующими issue-00001–issue-00010 совпадений по установленной локализации не обнаружено. Подтверждение проблем, исправления, смена статусов и новые задачи на исправление не выполнялись.

### Результат и пределы

Подготовлены пять [карточек](files/README.md); в реестре теперь **16 проверенных файлов и 605 неразобранных**. TASK-0003.001 завершена; родительская TASK-0003 остаётся in-progress, следующие девять подзадач первой серии — planned.

Проверены состав и содержимое исходников, локальные ссылки, обязательные разделы карточек, таблицы, статусы и отсутствие изменений вне docs. Для всех 741 существовавших отслеживаемых файлов сохранены mode, uid, gid и inode. Соседние файлы не получили новых карточек. Успешные проверки не подтверждают загрузку мира, доступ службы по HTTP, работу полного жизненного цикла документов, редактора в браузере или обмен между клиентами.

Первый пробный импорт моделей в Node выявил недостающие расширения Array.filterJoin; после подключения штатного `common/primitives/_module.mjs` модели работали без подмен полей или миграции. Предупреждение Node MODULE_TYPELESS_PACKAGE_JSON относится к этому способу локального запуска; package.json не менялся. Результаты реальных моделей и проверки с подменами разделены ниже.

### Проверка схем, миграции и потребителей

Команда выполнялась из корня системы. Импортирует только классы/примитивы ядра и код моделей; не запускает сервер и не записывает документы. В блоке Actor исполняются исходные prepareDerivedData/calculateStats, но родительский метод и соседние расчёты подменены, как указано в коде.

```bash
node --input-type=module <<'JS'
import assert from 'node:assert/strict';
import fs from 'node:fs';
import vm from 'node:vm';
await import('/opt/foundryvtt/common/primitives/_module.mjs');
const fields=await import('/opt/foundryvtt/common/data/fields.mjs');
const {default:DataModel}=await import('/opt/foundryvtt/common/abstract/data.mjs');
const {default:TypeDataModel}=await import('/opt/foundryvtt/common/abstract/type-data.mjs');
globalThis.foundry={data:{fields},abstract:{DataModel,TypeDataModel}};
const {default:stat}=await import('./module/data/actor/templates/common/stats/statData.js');
const {default:valueLabel}=await import('./module/data/actor/templates/valueLabelData.js');
const {default:Stats}=await import('./module/data/actor/templates/common/stats/statsData.js');
const {default:DerivedStats}=await import('./module/data/actor/templates/common/stats/derivedStatsData.js');
const {default:CommonActorData}=await import('./module/data/actor/commonActorData.js');
const {createEnrichedText}=await import('./module/data/dataUtils.js');
const result={};
assert.deepEqual(Object.keys(stat('test')),['max','unmodifiedMax','value','label','totalModifiers']);
assert.deepEqual(Object.keys(valueLabel('test')),['value','label']);
const single=stat('test',100);
assert.equal(single.unmodifiedMax.initial,100);
assert.equal(single.unmodifiedMax.label,'test');
for(const key of ['max','unmodifiedMax','value','totalModifiers']){
 assert.equal(single[key].min,undefined);assert.equal(single[key].max,undefined);
}
assert.equal(single.value.integer,false);assert.equal(single.max.integer,true);
const defaults=new Stats({});
assert.equal(defaults.toxicity.unmodifiedMax,100);
defaults.prepareBaseData();
assert.equal(defaults.toxicity.max,100);
result.schema={stats:Object.keys(Stats.schema.fields),derived:Object.keys(DerivedStats.schema.fields),numberLimits:'not defined'};
const inputs=[-3,0,7,15,2.6];
result.preparation=inputs.map(n=>{
 const s=new Stats({int:{unmodifiedMax:n,value:2.5,totalModifiers:4}});
 s.prepareBaseData();
 const once=JSON.stringify(s.toObject(false));
 s.prepareBaseData();
 assert.equal(JSON.stringify(s.toObject(false)),once);
 assert.equal(s.int.max,Math.round(n));
 assert.equal(s.int.value,2.5);assert.equal(s.int.totalModifiers,4);
 return {input:n,max:s.int.max,value:s.int.value};
});
result.migration=[];
for(const old of [{max:7},{max:7,unmodifiedMax:0},{max:7,unmodifiedMax:4}]){
 const s=new Stats({int:structuredClone(old)});
 const before={...s.int};
 s.prepareBaseData();
 result.migration.push({input:old,afterConstruction:before,afterPreparation:{...s.int}});
}
assert.equal(result.migration[0].afterPreparation.max,0);
assert.equal(result.migration[1].afterPreparation.max,7);
assert.equal(result.migration[2].afterPreparation.max,4);
for(const key of result.schema.stats){
 const source={[key]:{max:7,unmodifiedMax:0}};
 assert.equal(Stats.migrateData(source),source); assert.equal(source[key].unmodifiedMax,7);
}
const migrated=['stun','run','leap','enc','woundTreshold','vigor'];
for(const key of result.schema.derived){
 const s=new DerivedStats({[key]:{max:7,unmodifiedMax:0}});
 assert.equal(s[key].unmodifiedMax,migrated.includes(key)?7:0);
}
const oldVigor=new DerivedStats({vigor:{max:7}});
assert.equal(oldVigor.vigor.unmodifiedMax,0);
assert.equal(typeof oldVigor.prepareBaseData,'undefined');
result.derivedMigration={migrated,missingVigorBase:oldVigor.vigor.unmodifiedMax};
const legacyActorData=new CommonActorData({stats:{int:{max:7}},derivedStats:{vigor:{max:7}}});
legacyActorData.prepareBaseData();
assert.equal(legacyActorData.stats.int.max,0);
assert.equal(legacyActorData.derivedStats.vigor.max,0);
result.legacyActorData={intMax:legacyActorData.stats.int.max,vigorMax:legacyActorData.derivedStats.vigor.max};
const common=new CommonActorData({stats:{body:{unmodifiedMax:6},will:{unmodifiedMax:4},spd:{unmodifiedMax:5},int:{unmodifiedMax:7,value:3}}});
common.prepareBaseData();
assert.equal(common.derivedStats.stun.unmodifiedMax,5);
assert.equal(common.derivedStats.run.unmodifiedMax,15);
assert.equal(common.derivedStats.leap.unmodifiedMax,3);
assert.equal(common.derivedStats.enc.unmodifiedMax,60);
assert.equal(common.derivedStats.rec.unmodifiedMax,5);
assert.equal(common.derivedStats.resolve.unmodifiedMax,55);
assert.equal(common.derivedStats.focus.unmodifiedMax,9);
result.commonPreparation=Object.fromEntries(Object.entries(common.derivedStats).map(([k,v])=>[k,v.unmodifiedMax]));
const configSource=fs.readFileSync('module/setup/config.js','utf8');
const block=configSource.slice(configSource.indexOf('WITCHER.statMap ='),configSource.indexOf('//Skills'));
const ctx={WITCHER:{}};vm.runInNewContext(block,ctx);
const missing=[];const seen={stats:[],derivedStats:[]};
for(const [key,entry] of Object.entries(ctx.WITCHER.statMap)){
 if(!entry.origin)continue;
 const model=entry.origin==='stats'?Stats:DerivedStats;
 if(!model.schema.getField(key+'.totalModifiers'))missing.push(key);
 seen[entry.origin].push(key);
}
assert.deepEqual(missing,[]);
result.statMap={entries:Object.keys(ctx.WITCHER.statMap).length,missing,
 uncoveredStats:result.schema.stats.filter(k=>!seen.stats.includes(k)),
 uncoveredDerived:result.schema.derived.filter(k=>!seen.derivedStats.includes(k)),
 reputation:ctx.WITCHER.statMap.reputation};
assert.deepEqual(result.statMap.uncoveredStats,['toxicity']);
assert.deepEqual(result.statMap.uncoveredDerived,['shield']);
let calls=[];let complete;
foundry.applications={ux:{TextEditor:{implementation:{enrichHTML:async raw=>{
 calls.push(['enrich',raw]); await new Promise(resolve=>complete=resolve);return '<b>enriched</b>';
}}}}};
const model={schema:{getField:path=>{calls.push(['getField',path]);return Stats.schema.getField('int.value');}}};
const original='@UUID[Actor.example]';
const promise=createEnrichedText(model,original,'int.value');
assert.deepEqual(calls,[['enrich',original]]);
complete();
const enriched=await promise;
assert.equal(enriched.value,original);
assert.equal(enriched.enriched,'<b>enriched</b>');
assert.equal(enriched.systemField,Stats.schema.getField('int.value'));
assert.deepEqual(calls,[['enrich',original],['getField','int.value']]);
foundry.applications.ux.TextEditor.implementation.enrichHTML=async ()=>{throw Error('enrich failed');};
await assert.rejects(createEnrichedText(model,'text','int.value'),/enrich failed/);
assert.equal(calls.length,2);
foundry.applications.ux.TextEditor.implementation.enrichHTML=async ()=>'<p>result</p>';
const unknown=await createEnrichedText(new Stats({}),'text','unknown');
assert.equal(unknown.systemField,undefined);
result.enrichedText={order:['enrich awaited','getField'],originalPreserved:true,fieldIdentity:true,rejectionPropagates:true,unknownPath:unknown.systemField??null};
const actorSource=fs.readFileSync('module/actor/witcherActor.js','utf8');
let actorClass=actorSource.slice(actorSource.indexOf('export default class'),actorSource.indexOf('Object.assign(')).replace('export default class','class');
const actorContext={Actor:class{prepareDerivedData(){}},Math,WITCHER:{armorEffects:[]}};
vm.createContext(actorContext);
vm.runInContext(actorClass+'\nglobalThis.Subject=WitcherActor;',actorContext);
const a=new actorContext.Subject();
a.type='character';a.system=common;a.getList=()=>[];a.applyStatus=()=>{};
a.calculateStat=()=>{};a.calculateFixedDerivedStats=()=>{};a.calculateDerivedStats=()=>{};a.calculateAttackStats=()=>{};
common.stats.luck.max=10;common.stats.luck.totalModifiers=2;
common.stats.toxicity.max=100;common.stats.toxicity.totalModifiers=5;
a.prepareDerivedData();
assert.equal(common.stats.luck.max,14);assert.equal(common.stats.toxicity.max,110);
result.actorDoublePass={luck:{base:10,modifier:2,actual:14},toxicity:{base:100,modifier:5,actual:110},scope:'actual prepareDerivedData and calculateStats; other methods stubbed'};
console.log(JSON.stringify(result));

JS
```

Результат: все assert прошли. В частности, при входах Stats `{max:7}`, `{max:7,unmodifiedMax:0}`, `{max:7,unmodifiedMax:4}` после подготовки max равен 0, 7, 4. CommonActorData с отсутствующей базой int/vigor также дала 0. Для BODY=6, WILL=4, SPD=5, INT=7 (исходные), INT.value=3 и WILL.value=0 базовая подготовка дала stun=5, run=15, leap=3, enc=60, rec=5, woundTreshold=5, resolve=55, focus=9 в unmodifiedMax.

### Проверка передачи данных в шаблон

```bash
node --input-type=module <<'JS'
import assert from 'node:assert/strict';
import fs from 'node:fs';
import {createRequire} from 'node:module';
await import('/opt/foundryvtt/common/primitives/_module.mjs');
const fields=await import('/opt/foundryvtt/common/data/fields.mjs');
const {default:DataModel}=await import('/opt/foundryvtt/common/abstract/data.mjs');
const {default:TypeDataModel}=await import('/opt/foundryvtt/common/abstract/type-data.mjs');
globalThis.foundry={data:{fields},abstract:{DataModel,TypeDataModel},applications:{ux:{TextEditor:{implementation:{enrichHTML:async raw=>'<b>PROCESSED</b>'+raw}}}}};
const {default:MonsterData}=await import('./module/data/actor/monsterData.js');
const raw='<p>@UUID[Actor.example]</p>';
const monster=new MonsterData({common:raw,academicKnowledge:raw,monsterLore:raw});
const enrichedText=await monster.enrichedText();
const require=createRequire(import.meta.url), H=require('/opt/foundryvtt/node_modules/handlebars').create();
H.registerHelper('localize',key=>key);
const captures=[];
H.registerHelper('formGroup',(_field,options)=>{captures.push(options.hash);return '';});
const tpl=fs.readFileSync('templates/sheets/actor/partials/monster/tabs/partials/monster-knowledge.hbs','utf8');
const system=monster.toObject(false);
H.compile(tpl)({system,document:{system},systemFields:monster.schema.fields,enrichedText});
assert.equal(captures.length,3);
for(const c of captures){assert.equal(c.value,raw);assert.equal(c.enriched,raw);}
assert.notEqual(enrichedText.lore.common.enriched,captures[0].enriched);
console.log(JSON.stringify({modelCreatesProcessedHtml:true,templatePassesOriginalInstead:true,fields:captures.length,handlebars:require('/opt/foundryvtt/node_modules/handlebars/package.json').version,stubs:['TextEditor.enrichHTML','formGroup','localize'],browser:false}));

JS
```

Результат: все assert прошли; 3 вызова formGroup получили исходный текст вместо обработанного. Подмены: TextEditor.enrichHTML, formGroup и localize. Настоящие: MonsterData и вложенные модели, Handlebars 4.7.9, исходный шаблон. Это не рендер настоящего редактора Foundry.

### Повторная проверка состава и документации

Этот контроль относится к зафиксированному HEAD и метаданным текущего checkout до последующих коммитов. При дальнейшем развитии исследования изменение ожидаемых количеств, HEAD или inode требует осознанного пересмотра проверки; исторические результаты TASK-0001/TASK-0002 ниже сохраняются.

```bash
python3 - <<'PY'
import hashlib, json, os, re, subprocess
from pathlib import Path
from urllib.parse import unquote
base='15da5b225535e34af4e132c701b5353ef4eb667f'
expected_head='7b7788bc614e5b7a57f8c596fb64ca75ecabd8b7'
registry=Path('docs/analytics/code-audit/registry.md').read_text()
rows=[line for line in registry.splitlines() if re.match(r'^\| \[[^\]]+\]\(\.\./\.\./\.\./',line)]
paths=[re.match(r'^\| \[([^\]]+)\]',r).group(1) for r in rows]
assert len(paths)==len(set(paths))==621
assert sum(r.endswith('| Проверено |') for r in rows)==16
assert sum(r.endswith('| Не начат |') for r in rows)==605
excluded={'README.md','AGENTS.md','LICENSE','.gitignore','.prettierrc','.prettierignore','jsconfig.json.default','package-lock.json','styles/fonts/thewitcher2.ttf'}
def keep(p):
 return p.split('/')[0] not in {'.git','docs','assets','.github'} and p not in excluded and not (p.startswith('packs/') and p.endswith('/LOCK'))
tracked=[p for p in subprocess.check_output(['git','ls-files','-z'],text=True).split('\0') if p]
assert set(filter(keep,tracked))==set(paths)
actual=[]
for d,dirs,files in os.walk('.'):
 if d=='.':dirs[:]=[x for x in dirs if x not in {'.git','docs','assets','.github'}]
 for f in files:
  p=(Path(d)/f).as_posix()
  if keep(p):actual.append(p)
assert set(actual)==set(paths)
assert subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip()==expected_head
for p in paths:
 b=Path(p).read_bytes()
 assert b==subprocess.check_output(['git','show',base+':'+p]),p
 assert b==subprocess.check_output(['git','show',expected_head+':'+p]),p
digest=lambda b:hashlib.sha256(b).hexdigest()
assert digest(b''.join(p.encode()+b'\0'+Path(p).read_bytes()+b'\0' for p in paths))=='9de49bf9b75194490fcfd7bfc80e2b1c8bcd9d90dd26f3603faf21d92b3d0e1e'
meta={p:[Path(p).stat().st_mode,Path(p).stat().st_uid,Path(p).stat().st_gid,Path(p).stat().st_ino] for p in tracked if Path(p).is_file()}
assert digest(json.dumps(meta,sort_keys=True).encode())=='4f60b7857ee562cacd2e8973e002e71c26ac63cd57a9a750903adf5c442d40f9'
cards=[p for p in Path('docs/analytics/code-audit/files').rglob('*.md') if p.name!='README.md']
assert len(cards)==16
for row in rows:
 p=re.match(r'^\| \[([^\]]+)\]',row).group(1)
 c=Path('docs/analytics/code-audit/files')/(p+'.md')
 assert c.is_file()==row.endswith('| Проверено |'),p
titles=['Назначение файла','Условия использования','Введённые сущности и действия с ними','Основные функции и методы','Используемые сущности и зависимости','Известные потребители','Данные и изменения состояния','Проверки и доказательства','Непроверенные участки и открытые вопросы','Связанные проблемы','История актуализации']
for p in ["module/data/dataUtils.js","module/data/actor/templates/valueLabelData.js","module/data/actor/templates/common/stats/statData.js","module/data/actor/templates/common/stats/statsData.js","module/data/actor/templates/common/stats/derivedStatsData.js"]:
 t=Path('docs/analytics/code-audit/files/'+p+'.md').read_text()
 for title in titles:assert '## '+title in t,(p,title)
 assert expected_head in t and '| Статус анализа | Проверено |' in t
issues=list(Path('docs/issues').glob('*'+'/issue-*.md'))
assert len(issues)==14
assert {p.stem for p in issues}=={f'issue-{n:05}' for n in range(1,15)}
assert all(p.parent.name=='potential' for p in issues)
task=Path('docs/tasks/task-0003.001.md').read_text()
assert '| Статус | `done` |' in task and '- [ ]' not in task
assert '| Статус | `in-progress` |' in Path('docs/tasks/task-0003-remaining-files.md').read_text()
for n in range(2,11):
 assert '| Статус | `planned` |' in Path(f'docs/tasks/task-0003.{n:03}.md').read_text()
checked_links=0
mdfiles=list(Path('docs').rglob('*.md'))
def text_only(text):
 return re.sub(r'^```[^\n]*\n.*?^```[ \t]*$', '',text,flags=re.M|re.S)
def headings(text):
 out=set()
 for h in re.findall(r'^#{1,6}\s+(.+)$',text,flags=re.M):
  h=re.sub(r'\[([^\]]+)\]\([^)]+\)',r'\1',h)
  out.add(re.sub(r'[^\w\-\s]','',h.replace('`','').lower()).replace(' ','-'))
 out.update(re.findall(r'\bid=["\']([^"\']+)',text))
 return out
for f in mdfiles:
 text=re.sub(r'`+[^`]*`+', 'code', text_only(f.read_text()))
 for label,url in re.findall(r'\[([^\]\n]+)\]\(([^)\n]+)\)',text):
  if re.match(r'\w+://',url):continue
  target,_,anchor=url.partition('#')
  dest=(f.parent/unquote(target)).resolve() if target else f.resolve()
  assert dest.exists(),(str(f),url)
  if anchor:assert unquote(anchor) in headings(text_only(dest.read_text())),(str(f),url)
  checked_links+=1
changed=subprocess.check_output(['git','status','--porcelain','--untracked-files=all'],text=True).splitlines()
for row in changed:
 p=row[3:]
 assert p.startswith('docs/'),p
 raw=Path(p).read_text()
 assert all(l==l.rstrip() for l in raw.splitlines()),p
 for block in re.findall(r'(?:^\|.*\n)+',text_only(raw),flags=re.M):
  assert len({len(l.split('|')) for l in block.strip().splitlines()})==1,p
subprocess.run(['git','diff','--check'],check=True)
print(json.dumps({'source_files':621,'cards':16,'not_started':605,'new_cards':5,'potential_issues':14,'tracked_metadata_preserved':len(meta),'markdown_files':len(mdfiles),'local_links':checked_links,'changed_docs':len(changed),'source_and_metadata_hashes':'unchanged','diff_check':'passed'},ensure_ascii=False))
PY
```

Результат контрольной команды: 621 исходник, 16 карточек, 605 файлов со статусом «Не начат», 14 potential issues. Проверены 72 Markdown-документа и 1799 локальных ссылок. Изменены/созданы 22 документа; исходники и метаданные 741 отслеживаемого файла не изменились. `git diff --check` прошёл. При проверке ссылок учитываются ссылки на существующие каталоги, а примеры JavaScript в строковом коде не трактуются как Markdown-навигация.

## TASK-0002 — итоговая перекрёстная сверка

Дата: 2026-09-10. Ветка rusbar-main; HEAD проверки `3252300787c348e11f95098c345a6af7704b690c`. Все исследуемые исходники совпали со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. Установленное ядро — 14.367.0; это отдельно прочитанная версия, не вывод из compatibility манифеста.

| Проверка | Результат и пределы |
| --- | --- |
| Git и независимый обход дерева с согласованными исключениями | 621 одинаковый путь; исключённые файлы не получили строк реестра |
| Реестр и карточки | Ровно 11 файлов TASK-0002 имеют существующие карточки и статус «Проверено»; остальные 610 — «Не начат» |
| Полнота карточек | Все 11 исходников прочитаны полностью; обязательные разделы, версии и условия проверки присутствуют |
| Связи | Проверены импорты/определения/вызовы и реестры, примеси Actor/Item, helper sum, отправители query/socket, потребители настроек |
| Согласованность порций | Итог проверки четырёх дополнительных типов перенесён в манифест; языковые поля и namespace-импорты уточнены в точке входа; номера строк сверены |
| Конфигурация и шаблоны | Описаны 36 разделов, 21 ключ statMap, 52 навыка, 24 записи Crit, 26 статусов; сверены 59 путей шаблонов и 17 helpers |
| Проблемы | Девять новых карточек issue-00002–issue-00010; вместе с существовавшей issue-00001 — десять уникальных ID, все potential |
| Markdown | Проверены локальные пути ссылок, число столбцов таблиц, обязательные разделы и концевые пробелы; код не трактуется как навигация |
| Неизменность системы | Все 621 исходник совпали с Git blob обеих указанных версий; изменены и созданы только файлы docs |
| Метаданные доступа | Для 726 существовавших на старте путей проверены mode, uid, gid и inode: различий и пропавших путей нет; после завершающих правок проверка повторена |
| Пределы | Статическое чтение и изолированное выполнение с подменами не подтверждают запуск мира, браузер, межклиентскую доставку и игровую корректность всех механик |

Контрольные суммы состава и содержимого равны TASK-0001: `f6291adae3b89183f60336e7cee8c74afe45ed8dddd3d5a19b68e2e458a4f3d8` и `ff62af9c097bf62087f4a67485e78fab808a46008067a323f7478c0d56e9e88f`. Их вычисление приведено ниже.

TASK-0002 завершена; README, реестр, задача и CHANGELOG согласованы с результатом. TASK-0003–TASK-0005 остаются заготовками. Регистрация potential issues не является подтверждением пользователя, исправлением или постановкой задачи.

### Повторная проверка результата TASK-0002

Запуск из корня системы. Команда проверяет именно указанный HEAD и результат этапа. После нового коммита сначала сопоставить исследуемые исходники, прежде чем менять ожидаемую версию. Метаданные доступа проверялись отдельно относительно снимка начала работы; этот снимок не добавлялся в репозиторий.

```bash
python3 - <<'PY'
from pathlib import Path
from urllib.parse import unquote
import collections, hashlib, json, os, re, subprocess

BASE = "15da5b225535e34af4e132c701b5353ef4eb667f"
HEAD = "3252300787c348e11f95098c345a6af7704b690c"
audit = Path("docs/analytics/code-audit")
expected_cards = {
    "system.json", "module/TheWitcherTRPG.js",
    *("module/setup/" + name + ".js" for name in (
        "config", "registerDataModels", "registerSheets", "settings", "hooks",
        "handlebars", "queries", "socketHook", "deprecations"
    ))
}
excluded_files = {
    "README.md", "AGENTS.md", "LICENSE", ".gitignore", ".prettierrc",
    ".prettierignore", "jsconfig.json.default", "package-lock.json",
    "styles/fonts/thewitcher2.ttf"
}
def excluded(p):
    return (p.split("/")[0] in {"docs", "assets", ".github", ".git"}
            or p in excluded_files
            or (p.startswith("packs/") and Path(p).name == "LOCK"))
def git(*args):
    return subprocess.check_output(["git", *args])
assert git("rev-parse", "HEAD").decode().strip() == HEAD
tracked = git("ls-files", "-z").decode().split("\0")[:-1]
included = sorted(p for p in tracked if not excluded(p))
assert len(included) == 621
actual = []
for directory, dirs, files in os.walk("."):
    dirs[:] = [d for d in dirs if not excluded(str((Path(directory)/d).as_posix()))]
    actual.extend(str((Path(directory)/f).as_posix()) for f in files
                  if not excluded(str((Path(directory)/f).as_posix())))
assert sorted(actual) == included
rows = {}
for line in (audit/"registry.md").read_text().splitlines():
    m = re.match(r"\| \[([^]]+)\]\([^)]*\) \| (.*?) \| (.*?) \| (.*?) \|$", line)
    if m:
        path, purpose, desc, status = m.groups()
        assert path not in rows
        rows[path] = (purpose, desc, status)
assert sorted(rows) == included
assert {p for p, r in rows.items() if r[2] == "Проверено"} == expected_cards
assert all(r[2] == "Не начат" for p, r in rows.items() if p not in expected_cards)
cards = {str(p.relative_to(audit/"files"))[:-3]: p
         for p in (audit/"files").rglob("*.md") if p.name != "README.md"}
assert set(cards) == expected_cards
headings = [
    "Назначение файла", "Условия использования", "Введённые сущности и действия с ними",
    "Основные функции и методы", "Используемые сущности и зависимости",
    "Известные потребители", "Данные и изменения состояния", "Проверки и доказательства",
    "Непроверенные участки и открытые вопросы", "Связанные проблемы", "История актуализации"
]
for source, path in cards.items():
    text = path.read_text()
    assert all("\n## " + h + "\n" in text for h in headings)
    assert HEAD in text and BASE in text and "| Статус анализа | Проверено |" in text
    assert rows[source][1] == "[Карточка](files/" + source + ".md)"
for commit in (BASE, HEAD):
    blobs = {}
    for entry in git("ls-tree", "-rz", commit).split(b"\0")[:-1]:
        info, path = entry.split(b"\t", 1)
        blobs[path.decode()] = info.decode().split()[2]
    for path in included:
        data = Path(path).read_bytes()
        assert hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest() == blobs[path]
path_hash = hashlib.sha256(("\n".join(included)+"\n").encode()).hexdigest()
data_hash = hashlib.sha256(b"".join(
    p.encode()+b"\0"+hashlib.sha256(Path(p).read_bytes()).digest()+b"\n"
    for p in included)).hexdigest()
assert path_hash == "f6291adae3b89183f60336e7cee8c74afe45ed8dddd3d5a19b68e2e458a4f3d8"
assert data_hash == "ff62af9c097bf62087f4a67485e78fab808a46008067a323f7478c0d56e9e88f"
issues = list(Path("docs/issues").glob("*/issue-*.md"))
assert len(issues) == 10
assert {p.stem for p in issues} == {"issue-" + str(n).zfill(5) for n in range(1, 11)}
assert all(p.parent.name == "potential" for p in issues)
issue_registry = Path("docs/issues/README.md").read_text()
assert all("[{0}](potential/{0}.md)".format(p.stem) in issue_registry for p in issues)
links = 0
for p in Path("docs").rglob("*.md"):
    text = p.read_text()
    assert all(line == line.rstrip() for line in text.splitlines()), str(p)
    clean = re.sub(r"^\x60\x60\x60[^\n]*\n.*?^\x60\x60\x60\s*$", "", text, flags=re.M|re.S)
    no_code = re.sub(r"\x60[^\x60\n]*\x60", "", clean)
    for url in re.findall(r"\[[^]\n]+\]\(([^\s)]+)\)", no_code):
        if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", url):
            continue
        target = unquote(url.split("#", 1)[0])
        assert (p.parent/target if target else p).exists(), (str(p), url)
        links += 1
    width = None
    for line in clean.splitlines():
        if line.startswith("|"):
            columns = len(re.split(r"(?<!\\)\|", line))-2
            if width is None: width = columns
            assert width == columns, (str(p), line)
        else: width = None
git("diff", "--check")
changes = git("diff", "--name-only").decode().splitlines()
untracked = git("ls-files", "--others", "--exclude-standard").decode().splitlines()
assert all(p.startswith("docs/") for p in changes + untracked)
print(json.dumps({
    "included": len(included), "cards": len(cards), "notStarted": 610,
    "issuesPotential": len(issues), "localLinks": links,
    "pathHash": path_hash, "dataHash": data_hash,
    "sourceMatches": [BASE, HEAD], "onlyDocsChanged": True
}, ensure_ascii=False))
PY
```

## TASK-0002 — порция 1: манифест и точка входа

Дата: 2026-09-10. Коммит проверки: `3252300787c348e11f95098c345a6af7704b690c`; исходники совпадают со срезом `15da5b225535e34af4e132c701b5353ef4eb667f`. Между срезом и HEAD изменена только документация. Рабочее дерево на старте чистое. Установленное ядро — 14.367.0 по `/opt/foundryvtt/package.json`.

Полностью прочитаны system.json (195 строк) и module/TheWitcherTRPG.js (172 строки). Проверены 21 импорт и экспорты источников, соответствие ES-модуля манифесту, существование CSS и восьми локализаций, имена packFolders. Семь буквальных путей packs отсутствуют в checkout; сборка и обработка путей ядром не проверялись, поэтому это не объявлено ошибкой релиза.

Сверены вызовы регистрации и определения обработчиков чата, классов документов, API наград/эффектов, метод WitcherActor.useItem и потребители game.api в rewardsMixin. Проверка зависимого определения не считается полным разбором его файла. Типы данных и листов дополнительно сверяются в порции 3.

Изолированно выполнен исходный ready callback в Node vm с подменой импортов и Foundry API: без pack — TypeError и отсутствие дальнейших шагов; контрольный pack дал getIndex, hotbarDrop, socket, deprecations. Зарегистрирована [issue-00002](../../issues/potential/issue-00002.md). Браузерные сценарии и исполнение макроса не проверялись.

Результат: две карточки, две строки «Проверено». Исходники не изменялись. Итоговая проверка ссылок и покрытия выполняется также после всех порций.

## TASK-0002 — порция 2: конфигурация

Дата: 2026-09-10; HEAD `3252300787c348e11f95098c345a6af7704b690c`, исходник равен срезу TASK-0001. Полностью прочитаны 2431 строка config.js последовательными частями. Сверены все 36 свойств WITCHER, в том числе 52 навыка, 24 записи Crit, 26 статусов. Модуль без импортов выполнен из строки в Node: подсчитаны ключи и разобраны все JSON-строки в changes статусов.

Буквальные обращения CONFIG.WITCHER и шаблонного config сопоставлены с определениями; динамические группы проверены в modifierMixin/baseMixin. Сверены поля Stat, Skill, combatEffects и intData. Прямой буквальный потребитель Crit не найден; damageMixin.applyCritWound читает компедиум. Недостижимость Crit через динамический доступ не утверждается.

Изолированные вызовы настоящего кода с подменой Foundry API: handleStatusCounterIntegration при активном statuscounter и duration=2 даёт TypeError; chooseSkill для общего языка возвращает путь с commonspeech вместо существующего commonsp. Зарегистрированы [issue-00003](../../issues/potential/issue-00003.md) и [issue-00004](../../issues/potential/issue-00004.md). Реальный statuscounter, сохранение эффекта и бросок в мире не запускались.

В ядре 14.367.0 дополнительно проверен setter CONFIG.statusEffects (/opt/foundryvtt/client/client.mjs:30–38), копирующий переданный массив в реестр ядра: присваивание в init само по себе не объявлено ошибкой. Строковые типы changes сверены с миграцией формата в /opt/foundryvtt/common/documents/active-effect.mjs.

Результат: карточка и её связи сверены; пределы поиска и динамические связи явно отмечены. Проверка зависимых определений не выдана за полный разбор их файлов.

## TASK-0002 — порция 3: модели, листы и настройки

Дата: 2026-09-10; тот же HEAD и базовый срез. Полностью прочитаны registerDataModels.js (81 строка), registerSheets.js (145), settings.js (96). Проверены определения 33 импортов моделей/документа чата и 26 импортов листов. Оба регистратора сопоставлены между собой, с манифестом и вызовами из init.

В Node vm выполнены исходные функции с подменой классов и регистрационных API: 4 модели Actor, 22 Item с base, 2 ActiveEffect, 4 ChatMessage; отдельный класс WitcherChatMessage. Листы: 21 Item, 4 Actor, unregister/register ActiveEffect. Настройки: 9 ключей; callback choices на фиктивных Item/Actor pack вернул только Item.

Actor.mystery и Item.clue/obstacle/skill отсутствуют в documentTypes — [issue-00005](../../issues/potential/issue-00005.md). По ядру проверено: Document.TYPES читает game.model; DocumentTypeField проверяет этот список; DocumentSheetConfig допускает отдельную запись sheetClasses[type]. Падение регистрации листов не утверждается. Создание документов в действующем мире не проверено.

Буквальные чтения девяти настроек сверены с module/templates, включая helper getSetting. Наличие чтений в V1-файле не выдано за используемый интерфейс. Карточки разделяют регистрацию, создание модели и рендер. Результат: три карточки и их связи сверены; реальные Foundry-классы и UI не запускались.

## TASK-0002 — порция 4: события, шаблоны, запросы и сокет

Дата: 2026-09-10; тот же HEAD `3252300787c348e11f95098c345a6af7704b690c` и срез TASK-0001. Полностью прочитаны hooks.js (13 строк), handlebars.js (217), queries.js (51), socketHook.js (24), deprecations.js (7). Разделены импорт, регистрация и вызов обработчика. Проверены источники импортов, динамические методы Actor/Item, их подключение примесями, отправители запросов и сокета.

В handlebars сверены 59 существующих шаблонов и 17 helpers; буквальные потребители собраны по templates/**/*.hbs и сопоставлены с регистрацией. Неявная зависимость getOwnedComponentCount → findNeededComponent → Array.prototype.sum подтверждена определениями craftingMixin/ActorSheet и подключением к Actor. Это не утверждение полного разбора зависимых файлов.

Изолированные проверки исходных функций в Node vm с подменой API:

- hooks + два настоящих зависимых обработчика: update флагов без round/turn записал HP 5→7 и duration региона 3→2 — [issue-00006](../../issues/potential/issue-00006.md).
- Helpers: получены 59 путей и 17 регистраций; проверены сравнение, CSV, разность, and/or, capitalize, eachLimit за числом ключей и перепутанные подписи ног — [issue-00007](../../issues/potential/issue-00007.md). eachLimit описан без утверждения достижимости ошибочного входа из UI.
- Query: true до разрешения Promise цели и при отсутствии метода; unknown=false, constructor=true — [issue-00008](../../issues/potential/issue-00008.md). Цели подменены управляемыми заглушками; реальные операции не выполнялись.
- Query регионов: вложенный метод не вызван при true, deleteSpellVisualEffect=false. Настоящий deleteSpellVisualEffect при isGM=false даёт ReferenceError: item is not defined — [issue-00009](../../issues/potential/issue-00009.md).
- Сокет: addItem передал аргументы нужному UUID и удалил его из message.data; unknown на активном GM дал TypeError, другой пользователь проигнорирован — [issue-00010](../../issues/potential/issue-00010.md).

Пустой deprecationWarnings проверен чтением; запуск функции без тела не выдаётся за отдельный тест. Для внешнего поведения дополнительно прочитаны локальные User.query и loadTemplates ядра 14.367.0. Мир, сеть между клиентами, настоящий statuscounter, Handlebars-рендер и canvas не запускались.

Результат: пять карточек сверены с первичными исходниками, регистрациями/вызовами в точке входа и установленными потребителями. Найденные проблемы зарегистрированы только как potential; исходники и данные не исправлялись.

## 2026-09-10 — TASK-0001: состав исследуемого среза

| Поле | Значение |
| --- | --- |
| Задача | [TASK-0001](../../tasks/task-0001-code-inventory.md) |
| Ветка | `rusbar-main` |
| Коммит | `15da5b225535e34af4e132c701b5353ef4eb667f` |
| Начальная проверка состава | `2026-09-10 07:12:58 UTC` |
| Рабочее дерево до записи материалов | Чистое |
| Область проверки | Полный перечень файлов после согласованных исключений; существование и версия исходников |

### Выполненная сверка источников перечня

| Проверка | Способ | Полученный результат |
| --- | --- | --- |
| Исходная версия | `git rev-parse HEAD`, `git branch --show-current`, `git status --porcelain=v1` | Коммит и ветка выше; вывод статуса на старте пустой |
| HEAD и индекс Git | `git ls-tree -rz --name-only HEAD` и `git ls-files -z` | По 706 путей; разность множеств пуста |
| Применение исключений | Сопоставление путей с согласованными 14 правилами | 85 отслеживаемых файлов исключены, 621 включён |
| Фактическое дерево без правил Git ignore | `rg --files --hidden --no-ignore --null` с исключением служебных каталогов, затем согласованных файлов | 621 включённый путь |
| Независимый обход каталогов | `os.walk` с теми же явными исключениями | 621 путь; разности с Git и `rg` пусты |
| Игнорируемые файлы | `git ls-files --others --ignored --exclude-standard -z` | На старте не найдено |
| Неотслеживаемые файлы | `git ls-files --others --exclude-standard -z` | На старте не найдено |
| Чтение и тип включённых файлов | `lstat` и чтение байтов каждого файла | Ошибок чтения и обхода нет; все 621 файла обычные, без символических ссылок |
| Содержимое относительно коммита | Сопоставление Git blob SHA-1 прочитанных байтов с объектами `git ls-tree -rz HEAD` | Все 621 файла совпали с коммитом |

### Учёт исключений

Количество относится к отслеживаемым файлам зафиксированного коммита. Содержимое `.git/` не перечислялось и в Git-перечень не входит.

| Правило | Исключено отслеживаемых файлов |
| --- | --- |
| `docs/` | 28 |
| `assets/` | 39 |
| `.github/` | 4 |
| `.git/` | 0 |
| `README.md` | 1 |
| `AGENTS.md` | 1 |
| `LICENSE` | 1 |
| `.gitignore` | 1 |
| `.prettierrc` | 1 |
| `.prettierignore` | 1 |
| `jsconfig.json.default` | 1 |
| `package-lock.json` | 1 |
| `styles/fonts/thewitcher2.ttf` | 1 |
| `packs/**/LOCK` | 5 |
| **Всего** | **85** |

Рост относительно оценки 701 / 80 обусловлен пятью добавленными файлами задач в `docs/`. Анализируемый состав остался прежним: 621 файл.

### Контрольные суммы

| Проверяемый набор | SHA-256 |
| --- | --- |
| Отсортированный перечень 621 пути | `f6291adae3b89183f60336e7cee8c74afe45ed8dddd3d5a19b68e2e458a4f3d8` |
| Пути и содержимое 621 файла | `ff62af9c097bf62087f4a67485e78fab808a46008067a323f7478c0d56e9e88f` |

Для первой суммы пути сортируются лексикографически, соединяются переводами строки с завершающим переводом строки и кодируются UTF-8. Для второй в том же порядке объединяются UTF-8 путь, нулевой байт, 32 байта SHA-256 содержимого и перевод строки; затем считается SHA-256 объединения.

### Повторная проверка реестра

Команда запускается из корня системы. Она проверяет именно результат TASK-0001 с ещё не начатым пофайловым разбором. После появления карточек ожидаемые статусы и их количество должны проверяться по результатам соответствующей порции; исходная запись этой сверки сохраняется.

```bash
python3 - <<'PY'
from pathlib import Path, PurePosixPath
from urllib.parse import unquote
import collections, hashlib, json, os, re, subprocess

SNAPSHOT = "15da5b225535e34af4e132c701b5353ef4eb667f"
audit = Path("docs/analytics/code-audit")
expected_rules = [
    "docs/", "assets/", ".github/", ".git/",
    "README.md", "AGENTS.md", "LICENSE", ".gitignore", ".prettierrc",
    ".prettierignore", "jsconfig.json.default", "package-lock.json",
    "styles/fonts/thewitcher2.ttf", "packs/**/LOCK",
]

def output(*args):
    return subprocess.check_output(args).decode()

def excluded(path):
    for rule in expected_rules:
        if rule.endswith("/") and path.startswith(rule):
            return True
        if rule == "packs/**/LOCK":
            if path.startswith("packs/") and PurePosixPath(path).name == "LOCK":
                return True
        elif path == rule:
            return True
    return False

def documented_rules(path):
    text = path.read_text()
    section = text.split("## Согласованные исключения\n", 1)[1].split("\n## ", 1)[0]
    return re.findall(r"^\| `([^`]+)` \|", section, re.M)

assert documented_rules(audit / "README.md") == expected_rules
assert documented_rules(Path("docs/tasks/task-0001-code-inventory.md")) == expected_rules
tree = [p for p in output("git", "ls-tree", "-rz", "--name-only", SNAPSHOT).split("\0") if p]
expected = sorted(p for p in tree if not excluded(p))
current_git = {p for p in output("git", "ls-files", "-z").split("\0") if p and not excluded(p)}
rg_paths = {
    p for p in output("rg", "--files", "--hidden", "--no-ignore", "--null",
                      "-g", "!.git/**", "-g", "!docs/**", "-g", "!assets/**", "-g", "!.github/**").split("\0")
    if p and not excluded(p)
}
walk_paths, walk_errors = set(), []
for directory, dirs, files in os.walk(".", followlinks=False, onerror=lambda e: walk_errors.append(str(e))):
    base = Path(directory)
    dirs[:] = [d for d in dirs if not excluded((base / d).as_posix() + "/")]
    for name in files:
        path = base / name
        if not excluded(path.as_posix()):
            assert path.is_file() and not path.is_symlink(), path
            walk_paths.add(path.as_posix())
assert not walk_errors, walk_errors
assert set(expected) == current_git == rg_paths == walk_paths
rows = re.findall(
    r"^\| \[([^\]]+)\]\(([^)]+)\) \| ([^|]+) \| ([^|]+) \| ([^|]+) \|$",
    (audit / "registry.md").read_text(), re.M
)
paths = [row[0] for row in rows]
assert len(paths) == len(set(paths)) and paths == expected
assert all(row[2:] == ("Не установлено", "Не подготовлено", "Не начат") for row in rows)
for path, target, *_ in rows:
    assert (audit / unquote(target)).resolve() == Path(path).resolve()
cards = [p for p in (audit / "files").rglob("*.md") if p != audit / "files/README.md"]
assert not cards, cards

digest = hashlib.sha256()
for path in expected:
    digest.update(path.encode() + b"\0" + hashlib.sha256(Path(path).read_bytes()).digest() + b"\n")
paths_hash = hashlib.sha256(("\n".join(expected) + "\n").encode()).hexdigest()
assert paths_hash == "f6291adae3b89183f60336e7cee8c74afe45ed8dddd3d5a19b68e2e458a4f3d8"
assert digest.hexdigest() == "ff62af9c097bf62087f4a67485e78fab808a46008067a323f7478c0d56e9e88f"

links, anchors, errors = 0, 0, []
markdown = [Path("README.md"), Path("AGENTS.md"), *sorted(Path("docs").rglob("*.md"))]
for file in markdown:
    text = file.read_text()
    lines = text.splitlines()
    for index, line in enumerate(lines):
        if line.rstrip() != line:
            errors.append(f"{file}:{index + 1}: trailing whitespace")
        if line.startswith("#") and index + 1 < len(lines) and lines[index + 1].strip():
            errors.append(f"{file}:{index + 1}: no blank line after heading")
    for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
        target = target.strip().strip("<>")
        if re.match(r"^[a-zA-Z][\w+.-]*:", target):
            continue
        name, sep, fragment = target.partition("#")
        destination = file.parent / unquote(name) if name else file
        if not destination.exists():
            errors.append(f"{file}: missing {target}")
        elif destination.is_file() and destination.suffix == ".md" and sep and fragment:
            headings = re.findall(r"^#+\s+(.+)$", destination.read_text(), re.M)
            slugs = {re.sub(r"[^\w\s-]", "", h.lower()).replace(" ", "-") for h in headings}
            if unquote(fragment) not in slugs:
                errors.append(f"{file}: missing heading {target}")
            anchors += 1
        links += 1
assert not errors, errors
subprocess.run(["git", "diff", "--check"], check=True)
print(json.dumps({
    "snapshot": SNAPSHOT,
    "tracked_in_snapshot": len(tree),
    "excluded_in_snapshot": len(tree) - len(expected),
    "registry_rows": len(paths),
    "git_rg_walk_equal": True,
    "file_cards": len(cards),
    "content_unchanged": True,
    "local_links": links,
    "heading_anchors": anchors,
    "markdown_files": len(markdown),
    "groups": dict(sorted(collections.Counter(p.split("/")[0] if "/" in p else "(root)" for p in paths).items())),
    "errors": []
}, ensure_ascii=False, indent=2))
PY
```

### Результат проверки готовых документов

Приведённая команда выполнена после создания материалов и повторно после оформления итогов; оба запуска завершились с кодом 0. Итоговая проверка охватила 35 Markdown-документов, 813 локальных ссылок и 5 ссылок на заголовки. Состав реестра и контрольные суммы повторно совпали с исходной проверкой.

| Проверка | Результат |
| --- | --- |
| Строки реестра против Git, `rg` и обхода каталогов | 621 уникальная строка; множества путей совпали в обе стороны; порядок соответствует сортировке |
| Исключения в задаче и README | Все 14 согласованных правил совпадают; исключённых файлов в реестре нет |
| Ссылки на исходники | Каждый путь ведёт к соответствующему существующему файлу |
| Назначения, карточки и статусы | Во всех 621 строках «Не установлено», «Не подготовлено», «Не начат»; карточек исходников нет; `files/README.md` учитывается как указатель |
| Шаблон карточки | Сверен с требованиями: назначение, определения, функции и методы, действия с данными, зависимости, потребители, доказательства, ограничения и проблемы предусмотрены |
| Контрольные суммы исходников | Перечень и содержимое совпали с начальной проверкой |
| Локальные ссылки и якоря заголовков | Ошибок не выявлено; ссылки на каталоги также проверены |
| Markdown и `git diff --check` | Пробелов в конце строк и ошибок проверяемого оформления нет |
| Метаданные доступа существующих файлов | Права, владельцы, группы и inode сохранены |

TASK-0001 завершена как инвентаризация и подготовка основы. Появление 621 строки не означает завершения пофайлового анализа. Реестр и документы результатов находятся в исключённой папке `docs/` и не увеличивают исследуемый состав.

### Пределы вывода

Совпадение путей и содержимого подтверждает состав и версию исследуемых файлов. В этом этапе не проверялись назначения отдельных файлов, функции, межфайловые связи, загрузка системы или игровые сценарии. Базы компедиумов не собирались и не извлекались.

Новых проблем системы при сверке состава не выявлено. Отсутствие новых карточек проблем на этапе инвентаризации не означает исправности кода.
