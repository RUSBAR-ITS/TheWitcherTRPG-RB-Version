# Журнал перекрёстных сверок

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
