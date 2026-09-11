# Общая промежуточная сверка № 1

**Статус: завершена.** Сопоставлен весь накопленный массив: 310 карточек файлов и 258 issues. Это вспомогательный материал для TASK-0004; статус самой задачи остаётся `draft`.

## Исходный срез и границы

| Поле | Значение |
| --- | --- |
| Дата | 2026-09-11 |
| Ветка | rusbar-main |
| Коммит | 411ab4004a2378a5f96ceeb19f003f834ff9d3d9 |
| Рабочее дерево на старте | Чистое |
| Исходники | 621 файл; базовый срез TASK-0001 15da5b225535e34af4e132c701b5353ef4eb667f |
| Документация | 310 карточек файлов; 258 issues, все potential |
| Хеш исходников | 52701d3d0a5f054319886ac2a9d45b42c26c80098858d02518579c6a1edfaec4 |
| Хеш метаданных 1318 отслеживаемых файлов | 958204c6f46becf0ddeb098ddc0378c25685e2011d1d2233be04b24bd06a5c03 |

Проверка включает актуальность и полноту реестра, описания против кода, определения/потребителей, взаимодействие частей системы, основания issues и возможные дубли. Для каждого наблюдения отдельно фиксируются факт кода, ранее выполненные проверки и новая проверка; отсутствие пользовательского подтверждения не заменяется выводом агента. Непроверенные браузерные/серверные сценарии указываются явно.

Изменяются только документы анализа и связанные указатели. Исходники, игровые данные, права и владельцы сохраняются; статусы issues не меняются. Полное описание оставшихся 311 исходников не входит в эту сверку; при необходимости они читаются как соседние определения и потребители.

## Методика и формальная сверка

Сверка исходного среза завершена: 621 исходник совпадает с HEAD и TASK-0001. Реестр соответствует 310 карточкам; 258 issues пронумерованы без пропусков, все potential. Сверены 352 прямых импорта (231 default; 114 named-операторов, 123 имени; 7 namespace), соответствующие exports/обратные упоминания и 198 буквальных HBS-связей. Для 693 выделенных определений классов/функций/методов есть упоминания в карточках. Эти автоматические проверки проверяют наличие связей и имён, но не заменяют содержательную сверку.

На старте с созданным протоколом проверены 641 Markdown-документ docs и корневые README/AGENTS: 15468 локальных ссылок и якорей без ошибок. Результат окончательной проверки приведён в последнем разделе. Найдены 135 карточек с формулировками о непроверенных/будущих участках; это кандидаты для проверки актуальности, а не автоматически ошибки.

## Журнал последовательных блоков

Журнал содержит завершённые блоки; каждый следующий блок дополняет охват.

### B01 — Инициализация, конфигурация и протоколы сообщений

Сопоставлены 11 начальных карточек и issue-00001–00010. Повторно выполнены S01–S07 в Node vm с исходными телами функций; импорты сняты при загрузке в vm, внешние API/запись/пользователи/сокет заменены фасадами. S01: pending/missing-method query; S02: socket; S03: statuscounter Array; S04: ready; S05: helpers/preload; S06: регистрации/настройки; S07: справочники конфигурации. Ошибка начального фасада registerHelper (не принимал объект нескольких helpers) исправлена только в тестовом процессе; это не проблема системы. Новых неисправностей не зарегистрировано. Исторические ограничения ранних карточек рассматриваются с учётом позднейших дополнений; повторное выполнение браузерных/серверных сценариев не заявлено.

### B02 — Базовые характеристики, навыки и их потребители

Сопоставлены14 карточек .001–.002 и issue-00011–00018. M01–M08 прошли с настоящими fields/DataModel/моделями, методами расчёта, Log/levelUpSkill и Handlebars; Actor.update, TextEditor/DOM и окружение заменены. M05 использует expandObject и Localization с en fallback для восьми системных языков. Подтверждены различия source/prepared, label/метаданных, конечного значения/запроса update и текущего/старого шаблона. D01 уточнил основное описание issue-00017 по конфликтующим балансам, D02 убрал из Stats обещание уже завершённых .007/.009. Исторические сценарии и статусы potential сохранены.

### B03 — Состояние, биография, журналы и сборка моделей Actor

Сверены 27 карточек .003–.006 и issue-00019–00032. C01–C06 прошли на настоящих моделях и выбранных методах листа/Actor/конвертера с заменёнными внешними API и записью. Повторены композиция схем, мутация lifeEvents только в prepared-данных, applyAP и кратность multiplication, отрицательный DOM-ввод через Log с pending update, иммунитет/статические локации, одинаковые валюты. В первом запуске отсутствовал тестовый фасад renderTemplate; дополнен только стенд, после чего все шесть групп прошли. Остальные выводы этого блока сверены по исходникам и прежним доказательствам, без заявления о повторном полном боевом цикле. Новых противоречий карточек не выявлено.

### B04 — Документы Actor/Item, исполнение и редактор эффектов

Сверены20 карточек .007–.010 и issue-00033–00056. E01–E06 прошли: реальные схемы AE и системный _preUpdate с разрешающим super; настоящая грамматика Roll; расчёт характеристики; фактический payload передачи улучшения; общий обработчик статуса с телом core toggle; ожидание useItem и каталог мастера. Внешние документы/окна/запись/сообщения заменены, работа сети, браузерный partial render и отсчёт длительности в мире не воспроизводились. Сопоставлены core active/isSuppressed, начальная и конечная фазы Actor и отдельный проход Item. D03 уточнил ошибочно двусмысленное описание isDisabled. Issues о содержимом эффекта, фазах, длительности, начале отсчёта и интерфейсе оставлены раздельными.

### B05 — Общие листы предметов, боевые схемы, оружие и броня

Сверены34 карточки .011–.014 и issue-00057–00090. I01–I06 прошли на реальных моделях/методах с заменёнными документными родителями и update: состав схем/defaults, миграции смешанных данных, границы улучшений/SP, prepared/source сопротивлений, общие ссылки свойств урона, ручное редактирование/drop. Родитель первоначального стенда заменён на DataModel-фасад в соответствии с требованием настоящего ядра; это ошибка стенда, не issue системы. Сопоставлены все заявленные поля, методы, PARTS и основные связи этих карточек; старые API не объявлены сломанными только по названию. Issues84/89 относятся к последовательным разным барьерам; 67/86/87 —разным миграциям; 74/75 —разным условиям рендера.

### B06 — Расходники, компоненты, рецепты и ремонт

Сверены32 карточки .015–.017 и issue-00091–00108. R01–R05 прошли: реальные модели и редактор расходных записей, контекст рецепта, настоящий HBS компонента, RepairData/repairItem/подготовка представления, расчёт цены и флаги чата. Внешние документы/UUID/render/update и DOM заменены явно; хранилище не изменялось. Для отделения issue104 от ранней ошибки102 damagedLocations добавлено только в диагностический вход, commonRepair заменён регистратором. Подтверждён различный уровень моделей, представления и операций: сохранённое имя компонента не потеряно в source, NaN цены не равнозначен списанию денег, успешный допуск изолированного метода не означает успешный ремонт.

### B07 — Расы, профессии, критические травмы и восстановление

Сверены30 карточек .018–.020 и issue-00109–00127. P01–P05 прошли: реальные схемы/enrichedText, разные способы поиска навыка и отбора защиты, выбор получателя/ошибки duration/порогов/stat, treat/heal с pending-записями, пересчёт отдыха и переданные в чат данные. Actor/Item-родители —DataModel-фасады, документные операции и DOM/диалоги заменены; источники мира не изменены. Для P05 проверен аргумент speaker и поиск по имени, без заявления о новом полном core-сценарии. Причины идентификации, недоступной конфигурации, расчёта и раннего завершения разделены. Старые предложения рефакторинга/правила не внесены: проверена только текущая версия форка.

### B08 — Магические предметы и жизненный цикл областей

Сверены 18 карточек .021–.022 и issue-00128–00147. G01–G04 прошли: настоящие модели/миграции, методы списков компонентов, создание Region-данных с заменённым API и countdown с регистрацией запросов. Некорректный UUID первоначального стенда заменён на синтаксически допустимый; source не менялся. Повторно прочитаны контракты core Token.scene/User.viewedScene/createTokenEmanation. G03 проверяет аргумент дальности, не полный перевод геометрии ядром; применение в canvas, сеть и таймер после смены сцены не воспроизводились. Причины размещения, потери флагов, выбора сцены, единиц и отсутствующего результата разделены.

### B09 — Расследования и контейнеры

Сверены 17 карточек .023–.024 и issue-00148–00163. Q01–Q03 прошли на настоящих моделях и системных методах: произвольные имена навыков, преобразование inline-текста, пропущенный threshold/отмена/pending roll, недоступный UUID, вложенный вес, помещение себя и извлечение чужой ссылки. Foundry-документы, обновления, окно выбора и UUID заменены фасадами. Контексты HBS и цепочка getInteractActor сопоставлены с ранее выполненными проверками. Типы расследования остаются зависимы от issue5; реальное удаление контейнера и серверные права не проверялись. Оснований объединять ошибки идентификации, веса, владения, циклов и ожидания в одну не обнаружено.

### B10 — Общие листы Actor, действия Item и инвентарь

Сверены 16 карточек .025–.027 и issue-00164–00180. J01–J05 прошли: Recovery V2/V1, обрезка подготовленных улучшений, три legacy callback, расходование количества0, настоящий HBS summary и создание Item, перезапись jQuery. В стенд добавлен отсутствовавший базовый класс V1; это не ошибка системы. Полностью сопоставлены различия двух ActorSheet и их подключения; core ContextMenu подтверждает два разных порядка аргументов. Исходные HBS-входы/потребители сверены с карточками. Проверки записи/рендера заменены фасадами; работа старого листа в текущем мире не заявляется. Причины ошибок кнопки, тела операции и prepared/source не объединены.

### B11 — Общие броски, навыки и редактор характеристик

Сверены 28 карточек .028–.030 и issue-00181–00198. K01–K04 прошли: настоящие Roll/extendedRoll и пороги, внутренние функции fumble в vm, HBS собственного навыка и редактора, схема IP, сумма max. Для fumble ожидание сопоставлено с локализованным текстом, для IP отрицательный ввод передан в source модели напрямую, regex поля учитывает одинарные кавычки: исправлены проверки стенда, не код. Запись сообщений, окна и документы заменены. D04 уточнил max/unmodifiedMax в назначении statMixin. Исторический отзыв части issue193 сохранён; en fallback и dotted JSON учитываются. Общее сравнение броска отделено от правил рулбука, которые не переопределялись.

### B12 — Листы персонажа/монстра, экспорт и заметки

Сверены 20 карточек .031–.033 и issue-00199–00213; issue29 повторно сопоставлена с200. L01–L04 прошли: реальный Roll с пустой аннотацией, контекст Monster, настоящая константа типа папок, экспорт с pending-операцией и отрицательным множителем, заметки/eachLimit, Handlebars+HTML5-parser заголовка. API Folder/Actor.create/update и окно подменены; БД, живой canvas и браузер не затронуты. Для assets проверены только существование12 ссылок старого HBS,11 отсутствуют. D05 выявил дубль200/29 и уточнил запрос баланса; исторические доказательства и potential сохранены.

### B13 — Материалы, добыча, покупка, обмен валюты и награды

Сверены 23 карточки .034–.037 и issue-00214–00235. N01–N04 прошли: dismantle/нулевой запас/неразрешённый компонент, четыре операции покупки, отрицательный обмен и устаревший кошелёк, настоящий producer наград и HBS. Для отсутствующего компонента resolver фасада явно возвращает null; все документные записи/диалоги/чат заменены. Повторно прочитаны core DragDrop и оба этапа DialogV2 content. D06 привёл основное объяснение issue226 в соответствие с уже записанной .036: cleanHTML предшествует innerHTML. Отрицательные числа в payload не выдаются за подтверждённое сохранение, бизнес-правила торговли и экономики не изменялись.

### B14 — Профессиональные действия, сотворение магии и сообщения

Сверены 20 карточек .038–.040 и issue-00236–00258. T01–T04 прошли: настоящие BaseChatMessage/TypeDataField/модели, реальные chat listeners с HTML-атрибутами, direct profession attack и full cast до ошибки переменного лечения, calcStaminaMulti. Начальный искусственный Holder требовал заполнения defaults, поэтому T01 выполнен через настоящий BaseChatMessage, который выполняет штатную подготовку. Actor/UUID/выбор/запись и публикация заменены; сохранение в мире и сетевой цикл не утверждаются. Проверены producer→типизированное сообщение→consumer для duration/critEffectModifier и различие data-атрибутов с system-полями. Все310 карточек и258 issues получили содержательный результат; это ещё требует итоговой сверки документации.

## Реестр сверки карточек файлов

Результат «сопоставлено» означает проверку описания с исходником и указанными связями в пределах этой сверки. Он не означает отсутствие ошибок системы или выполненный браузерный тест.

| Исходник и карточка | Результат | Основание и ограничения |
| --- | --- | --- |
| [module/TheWitcherTRPG.js](files/module/TheWitcherTRPG.js.md) | Сопоставлено | B01: init/ready, callbacks чата, Polyglot и createMacro сопоставлены с исходником/регистраторами; S04. Макрос и внешний Polyglot не исполнялись. |
| [module/activeEffect/WitcherActiveEffectSheet.js](files/module/activeEffect/WitcherActiveEffectSheet.js.md) | Сверено | B04: PARTS/TABS ядра, wizard/autocomplete, несохранённые changes и partial render; source payload сопоставлен с issue43. |
| [module/activeEffect/mixins/baseMixin.js](files/module/activeEffect/mixins/baseMixin.js.md) | Сверено | B04: E06:109 вариантов при Actor; paths commonspeech/attacks расходятся со схемами, источник damage-модификаторов учитывается. |
| [module/activeEffect/mixins/temporaryItemImprovementMixin.js](files/module/activeEffect/mixins/temporaryItemImprovementMixin.js.md) | Сверено | B04: Три пути damage/oilEffect/silverDamage, без назначения операции/значения. |
| [module/activeEffect/witcherActiveEffect.js](files/module/activeEffect/witcherActiveEffect.js.md) | Сверено | B04: E01: флаги/частичные обновления; D03 уточнил isDisabled. Начало и фазы сопоставлены с ядром14.367. |
| [module/actor/mixins/adrenalineMixin.js](files/module/actor/mixins/adrenalineMixin.js.md) | Сверено | B11: Мировая настройка управляет +1; update не ожидается. |
| [module/actor/mixins/castSpellMixin.js](files/module/actor/mixins/castSpellMixin.js.md) | Сверено | B14: T04: весь castSpell и scaling, update раньше heal-failure; эффекты/область после Roll. |
| [module/actor/mixins/craftingMixin.js](files/module/actor/mixins/craftingMixin.js.md) | Сверено | B13: Три разных поиска компонентов: stored/sort/name/sourceUUID не эквивалентны. |
| [module/actor/mixins/currencyConverterMixin.js](files/module/actor/mixins/currencyConverterMixin.js.md) | Сверено | B13: N03: captured currencyData, rates, arithmetic, await update, detached chat. |
| [module/actor/mixins/healMixin.js](files/module/actor/mixins/healMixin.js.md) | Сверено | B07: Расчёт с parseInt и ограничением max, value может остаться строкой; сообщение передаёт this.actor. |
| [module/actor/mixins/modifierMixin.js](files/module/actor/mixins/modifierMixin.js.md) | Сверено | B04: Конкатенация модификаторов и потребители; E02 повторил parse-error для положительного значения. |
| [module/actor/mixins/professionMixin.js](files/module/actor/mixins/professionMixin.js.md) | Сверено | B14: T03: direct attack модификаторы/STA/UUID; поиск,threshold,tempHP сверены с B07. |
| [module/actor/mixins/rewardsMixin.js](files/module/actor/mixins/rewardsMixin.js.md) | Сверено | B13: Две обёртки API([this]) без await. |
| [module/actor/mixins/skillMixin.js](files/module/actor/mixins/skillMixin.js.md) | Сверено | B11: Стоимость/Log, skillMap и формулы обоих видов навыка; K03/K04, socialStanding условен. |
| [module/actor/mixins/temporaryEffectMixin.js](files/module/actor/mixins/temporaryEffectMixin.js.md) | Сверено | B04: E04: выбор оружия/потеря changes/start=null/пустой список; сообщение не является подтверждением записи. |
| [module/actor/rewardsSheet.js](files/module/actor/rewardsSheet.js.md) | Сверено | B13: Окно двух журналов, live system, без операций начисления. |
| [module/actor/sheets/WitcherActorSheet.js](files/module/actor/sheets/WitcherActorSheet.js.md) | Сверено | B10: V2:11 примесей, live system и последовательная подготовка; J01/J02. |
| [module/actor/sheets/WitcherActorSheetV1.js](files/module/actor/sheets/WitcherActorSheetV1.js.md) | Сверено | B10: V1:10 примесей, копия system, синхронная подготовка, дополнительный armor padding; импортов/регистрации нет. |
| [module/actor/sheets/WitcherCharacterSheet.js](files/module/actor/sheets/WitcherCharacterSheet.js.md) | Сверено | B12: Полный source: контекст/категории,17 методов, оба Craft callback; lifeEvents и Log сопоставлены. |
| [module/actor/sheets/WitcherLootSheet.js](files/module/actor/sheets/WitcherLootSheet.js.md) | Сверено | B13: N02: прямой ActorSheetV2, mutagens typo, отсутствующий totalCost, четыре операции покупки. |
| [module/actor/sheets/WitcherMonsterSheet.js](files/module/actor/sheets/WitcherMonsterSheet.js.md) | Сверено | B12: L01/L02: отсутствие totals, копирование всего Actor, folder и незавершённые quantities. |
| [module/actor/sheets/configurations/WitcherModifiersConfiguration.js](files/module/actor/sheets/configurations/WitcherModifiersConfiguration.js.md) | Сверено | B11: Две PARTS, общий CONFIG.statLabels и live system; отправка всей формы. |
| [module/actor/sheets/configurations/WitcherMonsterConfigurationSheet.js](files/module/actor/sheets/configurations/WitcherMonsterConfigurationSheet.js.md) | Сверено | B12: Четыре PARTS,52 isVisible записей, один commonspeech miss; global statLabels. |
| [module/actor/sheets/interactions/itemContextMenu.js](files/module/actor/sheets/interactions/itemContextMenu.js.md) | Сверено | B10: Core callback/onClick порядок сверён; J03; gift запускает получение/списание независимо. |
| [module/actor/sheets/investigation/WitcherMysterySheet.js](files/module/actor/sheets/investigation/WitcherMysterySheet.js.md) | Сверено | B09: Q01/Q02: CRUD, isGM-видимость, inline-конвертация и вызов rollClue. |
| [module/actor/sheets/mixins/activeEffectMixin.js](files/module/actor/sheets/mixins/activeEffectMixin.js.md) | Сверено | B04: Категории по isDisabled/type/isTemporary; управление через UUID и раскрытие описания; D03. |
| [module/actor/sheets/mixins/alchemyMixin.js](files/module/actor/sheets/mixins/alchemyMixin.js.md) | Сверено | B13: Девять записей со счётчиками контекста, не расчёт запаса. |
| [module/actor/sheets/mixins/criticalWoundMixin.js](files/module/actor/sheets/mixins/criticalWoundMixin.js.md) | Сверено | B07: Создание/лечение через UUID и listeners; отсутствующий delete-handler не имеет найденного текущего элемента. |
| [module/actor/sheets/mixins/currencyConverterMixin.js](files/module/actor/sheets/mixins/currencyConverterMixin.js.md) | Сверено | B13: bind при каждом вызове добавляет новый click listener. |
| [module/actor/sheets/mixins/customSkillMixin.js](files/module/actor/sheets/mixins/customSkillMixin.js.md) | Сверено | B11: Шесть listener, старый массив modifiers без поля/id; splice(-1) и pending writes. |
| [module/actor/sheets/mixins/deathSaveMixin.js](files/module/actor/sheets/mixins/deathSaveMixin.js.md) | Сверено | B11: Порог min(база,10)-deathSaves; K01 подтверждает обход сравнения при <0. |
| [module/actor/sheets/mixins/healMixin.js](files/module/actor/sheets/mixins/healMixin.js.md) | Сверено | B07: P05:глобальный DOM, несбрасываемые флаги, HP cap/полная STA/Vigor, незавершённые вложенные операции. |
| [module/actor/sheets/mixins/itemMixin.js](files/module/actor/sheets/mixins/itemMixin.js.md) | Сверено | B10: 23 listener, source/prepared Drop, уникальность/создание/слоты; J04, остальные тела сопоставлены с Actor. |
| [module/actor/sheets/mixins/noteMixin.js](files/module/actor/sheets/mixins/noteMixin.js.md) | Сверено | B12: L03: push/splice live массива и pending update; индекс не проверяется. |
| [module/actor/sheets/mixins/skillMixin.js](files/module/actor/sheets/mixins/skillMixin.js.md) | Сверено | B11: Четыре группы listener; сумма по label '(2)', а не costMultiplier; J05. |
| [module/actor/sheets/mixins/statMixin.js](files/module/actor/sheets/mixins/statMixin.js.md) | Сверено | B11: K04/D04: сумма подготовленных max; luck-save max, остальные value, разные await действий. |
| [module/actor/witcherActor.js](files/module/actor/witcherActor.js.md) | Сверено | B04: 17 примесей, формулы/порядок подготовки и операции Items; E03/E06, B02/B03. Контекст static и подмена defenseMixin учтены. |
| [module/app/htmlUtils.js](files/module/app/htmlUtils.js.md) | Сверено | B13: DOM label/input/select, без min/required, title innerHTML, options spread. |
| [module/app/reward/reward.js](files/module/app/reward/reward.js.md) | Сверено | B13: N04: получатели/Log/чат, amount/type без currency; GM gate. |
| [module/chatMessage/chatMessageData.js](files/module/chatMessage/chatMessageData.js.md) | Сверено | B11: Ссылочные поля конструктора и поверхностный append; не TypeDataModel. |
| [module/chatMessage/witcherChatMessage.js](files/module/chatMessage/witcherChatMessage.js.md) | Сверено | B14: Пустой подкласс ChatMessage, регистрация отдельно. |
| [module/data/activeEffects/witcherActiveEffectData.js](files/module/data/activeEffects/witcherActiveEffectData.js.md) | Сверено | B04: E01: changes ядра +пять флагов; phase/type/priority не подменены legacy mode. |
| [module/data/activeEffects/witcherTemporaryItemImprovementData.js](files/module/data/activeEffects/witcherTemporaryItemImprovementData.js.md) | Сверено | B04: E01: changes +три флага, отсутствует applyAfterCalculations; E04 перенос не сохраняет изменения. |
| [module/data/actor/characterData.js](files/module/data/actor/characterData.js.md) | Сверено | B03: C01: 29 полей; C02/C04: enrichedText отдельно от мутации листа и операций Log. |
| [module/data/actor/commonActorData.js](files/module/data/actor/commonActorData.js.md) | Сверено | B03: C01: 19 полей/13 импортов; базовые формулы, миграции и вес монет сопоставлены. |
| [module/data/actor/lootData.js](files/module/data/actor/lootData.js.md) | Сверено | B03: C01: самостоятельная модель из трёх полей; та же масса монет, без наследования CommonActorData. |
| [module/data/actor/monsterData.js](files/module/data/actor/monsterData.js.md) | Сверено | B03: C01: 53 поля, нет IP/logs/обучения; C05 проверил потребителей иммунитета/хвоста. |
| [module/data/actor/templates/character/attackData.js](files/module/data/actor/templates/character/attackData.js.md) | Сверено | B03: label/value punch/kick; формулы Actor и одноимённая схема ChatMessage различены. |
| [module/data/actor/templates/character/attackStatsData.js](files/module/data/actor/templates/character/attackStatsData.js.md) | Сверено | B03: Пять полей; миграция meleeBonus, прибавка B, копирование crit-модификаторов. |
| [module/data/actor/templates/character/currencyLogData.js](files/module/data/actor/templates/character/currencyLogData.js.md) | Сверено | B03: label/amount/type; нет собственного ID/времени/баланса. |
| [module/data/actor/templates/character/general/backgroundData.js](files/module/data/actor/templates/character/general/backgroundData.js.md) | Сверено | B03: HTMLField.value; контекст enrichedText отдельный, submit выполняет лист. |
| [module/data/actor/templates/character/general/damage/damageModificationData.js](files/module/data/actor/templates/character/general/damage/damageModificationData.js.md) | Сверено | B03: flat/multiplication/applyAP; C03 сверил контракт properties и обе ветки сопротивления. |
| [module/data/actor/templates/character/general/damage/damageTypeModificationData.js](files/module/data/actor/templates/character/general/damage/damageTypeModificationData.js.md) | Сверено | B03: Семь типов, по три поля; коэффициент не является самостоятельной стадией урона. |
| [module/data/actor/templates/character/general/detailsData.js](files/module/data/actor/templates/character/general/detailsData.js.md) | Сверено | B03: Семь пар value/label; данные label отличены от метаданных поля. |
| [module/data/actor/templates/character/general/homelandData.js](files/module/data/actor/templates/character/general/homelandData.js.md) | Сверено | B03: value/otherValue; свободные строки отдельно от Item.homeland. |
| [module/data/actor/templates/character/general/lifeEventData.js](files/module/data/actor/templates/character/general/lifeEventData.js.md) | Сверено | B03: decade/value/details/isOpened; key добавляет лист, не схема. |
| [module/data/actor/templates/character/general/lifeEventsData.js](files/module/data/actor/templates/character/general/lifeEventsData.js.md) | Сверено | B03: 20 фиксированных ключей 10–200; C02 проверил ошибку prepared-структуры без изменения _source. |
| [module/data/actor/templates/character/generalData.js](files/module/data/actor/templates/character/generalData.js.md) | Сверено | B03: Девять полей; общая биография отдельно от damageTypeModification и числовой репутации. |
| [module/data/actor/templates/character/ipLogData.js](files/module/data/actor/templates/character/ipLogData.js.md) | Сверено | B03: label/ip/isMagic; баланс выбирает Log до очистки записи. |
| [module/data/actor/templates/character/logData.js](files/module/data/actor/templates/character/logData.js.md) | Сверено | B03: push до update; C04 повторил потерю Promise и строковую сумму; M07 — конфликт с levelUpSkill. |
| [module/data/actor/templates/character/pannelsData.js](files/module/data/actor/templates/character/pannelsData.js.md) | Сверено | B03: 22 BooleanField; сохранённые флаги и использование старых/текущих шаблонов различены. |
| [module/data/actor/templates/character/skillTrainingData.js](files/module/data/actor/templates/character/skillTrainingData.js.md) | Сверено | B03: Четыре слота name/value; C04: DOM input.value остаётся строкой независимо от NumberField. |
| [module/data/actor/templates/common/adrenalineData.js](files/module/data/actor/templates/common/adrenalineData.js.md) | Сверено | B03: value/label; миграция current выполняется CommonActorData, не фабрикой. |
| [module/data/actor/templates/common/combatEffectsData.js](files/module/data/actor/templates/common/combatEffectsData.js.md) | Сверено | B03: attack/defense/turnStart/temporaryEffects; отдельные причины issues 6,21,22,23. |
| [module/data/actor/templates/common/currencyData.js](files/module/data/actor/templates/common/currencyData.js.md) | Сверено | B03: Семь валют; общий вес и Loot; C06 повторил коллизию ключа конвертера. |
| [module/data/actor/templates/common/focusData.js](files/module/data/actor/templates/common/focusData.js.md) | Сверено | B03: Четыре независимых слота name/value; расходуется STA, отдельный derivedStats.focus. |
| [module/data/actor/templates/common/lifepathData.js](files/module/data/actor/templates/common/lifepathData.js.md) | Сверено | B03: attacks хранит объекты value; потребитель удара и мастер читают иной контракт (issue-00019). |
| [module/data/actor/templates/common/noteData.js](files/module/data/actor/templates/common/noteData.js.md) | Сверено | B03: Массив title/details отличён от Item.note; запись принадлежит действиям листа. |
| [module/data/actor/templates/common/reputationData.js](files/module/data/actor/templates/common/reputationData.js.md) | Сверено | B03: stat('Rep'), max←unmodifiedMax; условная миграция аналогична issue-00011. |
| [module/data/actor/templates/common/skills/bodyData.js](files/module/data/actor/templates/common/skills/bodyData.js.md) | Сопоставлено | B02/M04: physique/endurance; schema labels и миграция существующих записей. Расчёты BODY вне модели. |
| [module/data/actor/templates/common/skills/craData.js](files/module/data/actor/templates/common/skills/craData.js.md) | Сопоставлено | B02/M04–M05: 7 навыков; внешние firstAid/pickLock/trapCrafting не разрешаются, миграция lower-case корректна. |
| [module/data/actor/templates/common/skills/dexData.js](files/module/data/actor/templates/common/skills/dexData.js.md) | Сопоставлено | B02/M04: 5 навыков; sleight → sleightOfHand при миграции; schema/skillMap согласованы по данным. |
| [module/data/actor/templates/common/skills/empData.js](files/module/data/actor/templates/common/skills/empData.js.md) | Сопоставлено | B02/M04: 10 навыков; finearts/grooming/perception переименовывают label; perception отличается от awareness. |
| [module/data/actor/templates/common/skills/intData.js](files/module/data/actor/templates/common/skills/intData.js.md) | Сопоставлено | B02/M04: 13 навыков, 6 замен label; commonsp/commonspeech сопоставлены с config и редактором. |
| [module/data/actor/templates/common/skills/refData.js](files/module/data/actor/templates/common/skills/refData.js.md) | Сопоставлено | B02/M04: 8 навыков; dodgeEscape — label поля dodge, не другое поле; динамические броски принадлежат Actor. |
| [module/data/actor/templates/common/skills/skillData.js](files/module/data/actor/templates/common/skills/skillData.js.md) | Сопоставлено | B02/M04: 7 полей; label не поступает через внешний EmbeddedDataField; modifiedValue — сумма без ограничений. |
| [module/data/actor/templates/common/skills/skillsData.js](files/module/data/actor/templates/common/skills/skillsData.js.md) | Сопоставлено | B02/M04: семь EmbeddedDataField дают52 навыка; фабрика не выполняет броски/обучение. |
| [module/data/actor/templates/common/skills/willData.js](files/module/data/actor/templates/common/skills/willData.js.md) | Сопоставлено | B02/M04: 7 навыков, 5 замен label; magicSkills определяется config, не схемой. |
| [module/data/actor/templates/common/stats/derivedStatsData.js](files/module/data/actor/templates/common/stats/derivedStatsData.js.md) | Сопоставлено | B02/M02: 12 полей, мигрируются6; таблица производных формул сверена с CommonActorData и WitcherActor; limits относятся к потребителям. |
| [module/data/actor/templates/common/stats/statData.js](files/module/data/actor/templates/common/stats/statData.js.md) | Сопоставлено | B02/M01: 5 полей, integer для max/base/modifiers, дробный value; фабрика не задаёт min/max1–10. |
| [module/data/actor/templates/common/stats/statsData.js](files/module/data/actor/templates/common/stats/statsData.js.md) | Сопоставлено; уточнён текст | B02/M01–M02: 10 статов, prepare/migrate, missing-vs-zero; D02 обновляет ссылку на уже завершённые .007/.009. |
| [module/data/actor/templates/common/temporaryEffectsData.js](files/module/data/actor/templates/common/temporaryEffectsData.js.md) | Сверено | B03: Словарь temporaryHp; источник AE, сумма листа и расход damageMixin различены. |
| [module/data/actor/templates/valueLabelData.js](files/module/data/actor/templates/valueLabelData.js.md) | Сопоставлено | B02/M01: два StringField; label — данные, не метаданные value; свежие поля, нет записи/локализации. |
| [module/data/chatMessage/attackMessageData.js](files/module/data/chatMessage/attackMessageData.js.md) | Сверено | B14: T01: четыре композиции+rollTotal; attackRoll getter, duration очищается ядром. |
| [module/data/chatMessage/baseMessageData.js](files/module/data/chatMessage/baseMessageData.js.md) | Сверено | B14: Только rollTotal:NumberField, metadata frozen, не вычислитель. |
| [module/data/chatMessage/damageMessageData.js](files/module/data/chatMessage/damageMessageData.js.md) | Сверено | B14: T01: properties effects заменены ArrayField с applied; duration отсутствует. |
| [module/data/chatMessage/defenseMessageData.js](files/module/data/chatMessage/defenseMessageData.js.md) | Сверено | B14: T01: собственная crit/location схема теряет critEffectModifier. |
| [module/data/chatMessage/templates/attackData.js](files/module/data/chatMessage/templates/attackData.js.md) | Сверено | B14: Четыре поля attack, nullable itemUuid; T03 direct attack его не задаёт. |
| [module/data/chatMessage/templates/critData.js](files/module/data/chatMessage/templates/critData.js.md) | Сверено | B14: Два modifier поля внутри damage.crit, не Defense.crit. |
| [module/data/chatMessage/templates/damageData.js](files/module/data/chatMessage/templates/damageData.js.md) | Сверено | B14: Восемь полей, duration/экранные heal/shield не входят; T01. |
| [module/data/chatMessage/templates/locationData.js](files/module/data/chatMessage/templates/locationData.js.md) | Сверено | B14: Четыре поля, formula initial1, modifier string; Defense.location другая схема. |
| [module/data/dataUtils.js](files/module/data/dataUtils.js.md) | Сопоставлено | B02/M03: enrichHTML → value/systemField, неизвестный путь даёт undefined; marker-enrichment и настоящая schema. TextEditor/DOM заменены. |
| [module/data/investigation/clueData.js](files/module/data/investigation/clueData.js.md) | Сверено | B09: Q01: десять полей и произвольные имена skillsUsed; DC не передаётся потребителю. |
| [module/data/investigation/mysteryActorData.js](files/module/data/investigation/mysteryActorData.js.md) | Сверено | B09: Q01: самостоятельная схема goal/complexity, без CommonActorData. |
| [module/data/investigation/obstacleData.js](files/module/data/investigation/obstacleData.js.md) | Сверено | B09: Q01: шесть полей; отдельный roll препятствия отсутствует. |
| [module/data/investigation/templates/complexityData.js](files/module/data/investigation/templates/complexityData.js.md) | Сверено | B09: Q01: два поля вложенной сложности, без расчётного метода. |
| [module/data/item/alchemicalData.js](files/module/data/item/alchemicalData.js.md) | Сверено | B06: 15 полей, consumable и возможность улучшения; time/toxicity — строки, consume их не исполняет. |
| [module/data/item/armorData.js](files/module/data/item/armorData.js.md) | Сверено | B05: 27 полей, последнее location побеждает; I02/I03/I04: миграции, ёмкость, SP, сопротивления; нет делегатов защиты. |
| [module/data/item/commonItemData.js](files/module/data/item/commonItemData.js.md) | Сверено | B04: Восемь полей, строковый quantity, calcWeight и два false-getter; схема и Item/Actor разделены. |
| [module/data/item/componentData.js](files/module/data/item/componentData.js.md) | Сверено | B06: 14 полей; шесть собственных строк, без особой миграции/расчёта. |
| [module/data/item/containerData.js](files/module/data/item/containerData.js.md) | Сверено | B09: Q03: storedWeight только прямых ссылок; нет null guard и рекурсивного веса. |
| [module/data/item/criticalWoundData.js](files/module/data/item/criticalWoundData.js.md) | Сверено | B07: P01/P04:девять полей, сроки8/12/15−BODY.max, heal/treat и последовательность create/delete. |
| [module/data/item/diagramData.js](files/module/data/item/diagramData.js.md) | Сверено | B06: 20 полей; R02: enrichment сохраняет неразрешённую запись, миграция переопределяет новые UUID/DC. |
| [module/data/item/enhancementData.js](files/module/data/item/enhancementData.js.md) | Сверено | B05: 16 полей; I02: конвертированный effects сохраняется, в отличие от ArmorData. |
| [module/data/item/hexData.js](files/module/data/item/hexData.js.md) | Сверено | B08: Общая схема, danger/liftRequirement и выбор hexweave; наследования SpellData нет. |
| [module/data/item/homelandData.js](files/module/data/item/homelandData.js.md) | Сверено | B07: P01:самостоятельные value/otherValue, без CommonItemData и enrichedText. |
| [module/data/item/mixin/spellRegionMixin.js](files/module/data/item/mixin/spellRegionMixin.js.md) | Сверено | B08: G03/G04 и core14.367: Promise/all, flags, Scene/ID, единицы, void и отдельный таймер. |
| [module/data/item/mountData.js](files/module/data/item/mountData.js.md) | Сверено | B13: Двенадцать полей, три строки и HP number; без Actor mount связи. |
| [module/data/item/mutagenData.js](files/module/data/item/mutagenData.js.md) | Сверено | B06: 15 полей и consumable; лист оставляет обычную конфигурацию, alchemyDC не описывает сам расход. |
| [module/data/item/noteData.js](files/module/data/item/noteData.js.md) | Сверено | B12: Восемь полей CommonItem с повторным description; не модель массива Actor.notes. |
| [module/data/item/professionData.js](files/module/data/item/professionData.js.md) | Сверено | B07: P01:14 полей/11 enrich; P02:защиты трёх путей без definingSkill/isDefense. |
| [module/data/item/raceData.js](files/module/data/item/raceData.js.md) | Сверено | B07: P01:13 полей/четыре enrich-вызова; description HTML, perk текст, эффекты —отдельные документы. |
| [module/data/item/ritualData.js](files/module/data/item/ritualData.js.md) | Сверено | B08: Две UUID-коллекции, fallback без item.uuid и перенос template; G01. |
| [module/data/item/skillItemData.js](files/module/data/item/skillItemData.js.md) | Сверено | B11: Восемь полей, без modifiers/modifiedValue; K03. |
| [module/data/item/spellData.js](files/module/data/item/spellData.js.md) | Сверено | B08: TypedObject selfEffects и миграция template сопоставлены с castSpell; G01. |
| [module/data/item/templates/armor/resistanceData.js](files/module/data/item/templates/armor/resistanceData.js.md) | Сверено | B05: OR с улучшениями в prepared boolean; I04 различил source и потенциальный обратный ввод формы. |
| [module/data/item/templates/armor/spData.js](files/module/data/item/templates/armor/spData.js.md) | Сверено | B05: Четыре числа, два неперсистентных; base копирует, derived прибавляет stopping при ненулевом max; I04. |
| [module/data/item/templates/associatedDiagramData.js](files/module/data/item/templates/associatedDiagramData.js.md) | Сверено | B06: String UUID и синхронное раскрытие; пустой UUID ничего не присваивает. |
| [module/data/item/templates/combat/attackOptionsData.js](files/module/data/item/templates/combat/attackOptionsData.js.md) | Сверено | B05: Восемь полей; I01: initial после очистки старого attackSkill, default spellcasting отсутствует в карте. |
| [module/data/item/templates/combat/damagePropertiesData.js](files/module/data/item/templates/combat/damagePropertiesData.js.md) | Сверено | B05: 18 полей, словарь effects, merge/preprocess/миграция; I02/I05, исходные и prepared effects различены. |
| [module/data/item/templates/combat/defenseOptionsData.js](files/module/data/item/templates/combat/defenseOptionsData.js.md) | Сверено | B05: Set вариантов защиты от атаки, initial из CONFIG; отличается от собственной DefenseProperties. |
| [module/data/item/templates/combat/defensePropertiesData.js](files/module/data/item/templates/combat/defensePropertiesData.js.md) | Сверено | B05: Три поля, has(attack), минимальный объект варианта без навыка; внешние делегаты сверены. |
| [module/data/item/templates/combat/skillAttackData.js](files/module/data/item/templates/combat/skillAttackData.js.md) | Сверено | B05: 13 полей: три собственных +общие attackOptions/DamageProperties/defenseOptions. |
| [module/data/item/templates/combat/skillDefenseData.js](files/module/data/item/templates/combat/skillDefenseData.js.md) | Сверено | B05: isDefense +DefenseProperties; отбор ProfessionData не читает флаг и definingSkill. |
| [module/data/item/templates/componentData.js](files/module/data/item/templates/componentData.js.md) | Сверено | B08: Только uuid/quantity, без id/img; получатель RitualData и обе строки HBS. |
| [module/data/item/templates/consumableData.js](files/module/data/item/templates/consumableData.js.md) | Сверено | B06: Фабрика isConsumable/consumeProperties без действий; три модели-потребителя. |
| [module/data/item/templates/consumePropertiesData.js](files/module/data/item/templates/consumePropertiesData.js.md) | Сверено | B06: R01: четыре поля, два массива itemEffect без id, addsTempHp отсутствует. |
| [module/data/item/templates/craftingComponentData.js](files/module/data/item/templates/craftingComponentData.js.md) | Сверено | B06: Четыре поля, initial randomID и необязательный DocumentUUID; ID строки отличается от UUID. |
| [module/data/item/templates/itemEffectData.js](files/module/data/item/templates/itemEffectData.js.md) | Сверено | B05: Четыре поля, percentage0–100; запись воздействия отличается от документа ActiveEffect, собственного id нет. |
| [module/data/item/templates/perkData.js](files/module/data/item/templates/perkData.js.md) | Сверено | B07: name/HTML description, фиксированное число слотов задаёт RaceData; числовые бонусы здесь не определены. |
| [module/data/item/templates/profession/skillUsageData.js](files/module/data/item/templates/profession/skillUsageData.js.md) | Сверено | B07: hasCustomEffect/applySelf/applyOnTarget/temporaryHealth; P03 показал фактическое чтение только applyOnTarget. |
| [module/data/item/templates/profession/temporaryHealthData.js](files/module/data/item/templates/profession/temporaryHealthData.js.md) | Сверено | B07: Default3/int/5 и d6/2*@level; P03 проверил несоответствие свободной duration потребителю. |
| [module/data/item/templates/profession/thresholdData.js](files/module/data/item/templates/profession/thresholdData.js.md) | Сверено | B07: Флаг и словарь name/value; P03:пустой включённый словарь не защищён потребителем. |
| [module/data/item/templates/professionPathData.js](files/module/data/item/templates/professionPathData.js.md) | Сверено | B07: pathName+три схемы навыка, фиксированная структура без правил развития. |
| [module/data/item/templates/professionSkillData.js](files/module/data/item/templates/professionSkillData.js.md) | Сверено | B07: Восемь полей и четыре импорта; схема общая для definingSkill/девяти навыков путей. |
| [module/data/item/templates/regions/regionBehavioursData.js](files/module/data/item/templates/regions/regionBehavioursData.js.md) | Сверено | B08: Четыре Macro UUID; подпись MoveWithin использует PreMove. |
| [module/data/item/templates/regions/regionPropertiesData.js](files/module/data/item/templates/regions/regionPropertiesData.js.md) | Сверено | B08: Делегирование GM и region.update без ожидания; миграция tokenMoveWithin затирает значение. |
| [module/data/item/templates/regions/templatePropertiesData.js](files/module/data/item/templates/regions/templatePropertiesData.js.md) | Сверено | B08: Четыре поля геометрии/визуального времени; duration боя хранится отдельно. |
| [module/data/item/templates/socialStandingData.js](files/module/data/item/templates/socialStandingData.js.md) | Сверено | B07: Пять строк регионов, без choices/выбора текущего региона/применения штрафа. |
| [module/data/item/templates/weaponTypeData.js](files/module/data/item/templates/weaponTypeData.js.md) | Сверено | B05: text и четыре независимых флага; текст собирает _onDamageTypeEdit. |
| [module/data/item/valuableData.js](files/module/data/item/valuableData.js.md) | Сверено | B06: 15 полей, consumable и улучшения; собственные effect/quality не выводятся основной формой. |
| [module/data/item/weaponData.js](files/module/data/item/weaponData.js.md) | Сверено | B05: 36 полей; I01/I02/I03: skill fallback, старые ID, Actor-контекст; repair не ждёт update. |
| [module/data/migrations/damagePropertiesMigration.js](files/module/data/migrations/damagePropertiesMigration.js.md) | Сверено | B05: Пять truthy-переносов; I02: новые поля перезаписываются, пустой старый effects[] тоже переносится. |
| [module/item/mixins/consumeMixin.js](files/module/item/mixins/consumeMixin.js.md) | Сверено | B06: heal/status/removeStatus/applySelf/чат; только расчёт лечения awaited, количество списывает внешний useItem. |
| [module/item/mixins/costEditMixin.js](files/module/item/mixins/costEditMixin.js.md) | Сверено | B06: R05: глобальные component-cost и первый total-price; parseInt('')??0 остаётся NaN. |
| [module/item/mixins/dismantlingMixin.js](files/module/item/mixins/dismantlingMixin.js.md) | Сверено | B13: N01: проверка recipe/количества, потеря name и ранний возврат после выдачи. |
| [module/item/mixins/repairMixin.js](files/module/item/mixins/repairMixin.js.md) | Сверено | B06: repair ждёт process, restoreReliability лишь делегирует; не обещает завершения model.update. |
| [module/item/sheets/WitcherAlchemicalSheet.js](files/module/item/sheets/WitcherAlchemicalSheet.js.md) | Сверено | B06: Основной PART, расходная конфигурация и четыре типа; config изменяется по общей ссылке. |
| [module/item/sheets/WitcherArmorSheet.js](files/module/item/sheets/WitcherArmorSheet.js.md) | Сверено | B05: Четыре типа/пять UI-локаций; общий CONFIG, recipes, действующий activateListeners. |
| [module/item/sheets/WitcherComponentSheet.js](files/module/item/sheets/WitcherComponentSheet.js.md) | Сверено | B06: Только ширина600 и PART, вся логика формы у родителя; R03. |
| [module/item/sheets/WitcherContainerSheet.js](files/module/item/sheets/WitcherContainerSheet.js.md) | Сверено | B09: Q03: self/owner/carry не проверяются; обновляются два исходных Item без await. |
| [module/item/sheets/WitcherCriticalWoundSheet.js](files/module/item/sheets/WitcherCriticalWoundSheet.js.md) | Сверено | B07: Основной PART/размеры; Drop пишет followUp UUID без ожидания update. |
| [module/item/sheets/WitcherDiagramSheet.js](files/module/item/sheets/WitcherDiagramSheet.js.md) | Сверено | B06: R02: недоступный UUID теряет имя в контексте; row ID/actions, два словаря и drop связей сверены. |
| [module/item/sheets/WitcherEnhancementSheet.js](files/module/item/sheets/WitcherEnhancementSheet.js.md) | Сверено | B05: Один PART main, локальный selects четырёх категорий, без записи CONFIG. |
| [module/item/sheets/WitcherHexSheet.js](files/module/item/sheets/WitcherHexSheet.js.md) | Сверено | B08: danger Low/Medium/High и несовпадающие ключи локализации. |
| [module/item/sheets/WitcherHomelandSheet.js](files/module/item/sheets/WitcherHomelandSheet.js.md) | Сверено | B07: Ширина600/PART, optional enrichedText даёт undefined; шаблон обходится без него. |
| [module/item/sheets/WitcherItemSheet.js](files/module/item/sheets/WitcherItemSheet.js.md) | Сверено | B05: Общий контекст/PARTS={}, drag/drop и ручные записи system.effects; I06, core-hook отдельно. |
| [module/item/sheets/WitcherMountSheet.js](files/module/item/sheets/WitcherMountSheet.js.md) | Сверено | B13: Только width/PARTS; обработчики наследуются. |
| [module/item/sheets/WitcherMutagenSheet.js](files/module/item/sheets/WitcherMutagenSheet.js.md) | Сверено | B06: Основной PART и три цвета; конфигурация унаследована от общего листа. |
| [module/item/sheets/WitcherProfessionSheet.js](files/module/item/sheets/WitcherProfessionSheet.js.md) | Сверено | B07: PART/config; список базовых навыков через skill.name и общий statOptions без none. |
| [module/item/sheets/WitcherRaceSheet.js](files/module/item/sheets/WitcherRaceSheet.js.md) | Сверено | B07: Ширина600/PART, контекст и config у родителя; форма использует value и enriched. |
| [module/item/sheets/WitcherRitualSheet.js](files/module/item/sheets/WitcherRitualSheet.js.md) | Сверено | B08: G02: первая совпавшая запись, удаление всех дублей, мутация массива и pending update. |
| [module/item/sheets/WitcherSkillItemSheet.js](files/module/item/sheets/WitcherSkillItemSheet.js.md) | Сверено | B11: Девять stat options, самостоятельный V2, повторный classes.push. |
| [module/item/sheets/WitcherSpellSheet.js](files/module/item/sheets/WitcherSpellSheet.js.md) | Сверено | B08: Семь словарей, конфигурация и PARTS; регистр Water и локализация. |
| [module/item/sheets/WitcherValuableSheet.js](files/module/item/sheets/WitcherValuableSheet.js.md) | Сверено | B06: Основной PART, расходная конфигурация и локальный selects семи типов. |
| [module/item/sheets/WitcherWeaponSheet.js](files/module/item/sheets/WitcherWeaponSheet.js.md) | Сверено | B05: PARTS/config, изменение type и локализованного text, рецепт weapon/elderfolk-weapon; общий CONFIG по ссылке. |
| [module/item/sheets/configurations/WitcherArmorConfigurationSheet.js](files/module/item/sheets/configurations/WitcherArmorConfigurationSheet.js.md) | Сверено | B05: Только замена general-PART; все действия/фильтры частей наследуются. |
| [module/item/sheets/configurations/WitcherConfigurationSheet.js](files/module/item/sheets/configurations/WitcherConfigurationSheet.js.md) | Сверено | B05: Четыре части/две вкладки; категоризация по disabled, возврат Promise управления AE; раскрытия описания нет. |
| [module/item/sheets/configurations/WitcherConsumableConfigurationSheet.js](files/module/item/sheets/configurations/WitcherConsumableConfigurationSheet.js.md) | Сверено | B06: R01: добавление percentage100 без ID, поиск obj.id для правки/удаления; массив мутирует до update. |
| [module/item/sheets/configurations/WitcherProfessionConfigurationSheet.js](files/module/item/sheets/configurations/WitcherProfessionConfigurationSheet.js.md) | Сверено | B07: P02:поиск первого имени в путях, действия/части; removeEffectDamageProperties не зарегистрирован; записи без ожидания. |
| [module/item/sheets/configurations/WitcherPropertiesConfigurationSheet.js](files/module/item/sheets/configurations/WitcherPropertiesConfigurationSheet.js.md) | Сверено | B05: Tabs и render parts используют разные условия региона; I06: общий дефект текстового on. |
| [module/item/sheets/configurations/WitcherSpellConfigurationSheet.js](files/module/item/sheets/configurations/WitcherSpellConfigurationSheet.js.md) | Сверено | B08: Собственных обработчиков нет; только подмена PARTS.general. |
| [module/item/sheets/investigation/WitcherClueSheet.js](files/module/item/sheets/investigation/WitcherClueSheet.js.md) | Сверено | B09: V1 defaultOptions/getData и skills; inline listener здесь не установлен. |
| [module/item/sheets/investigation/WitcherObstacleSheet.js](files/module/item/sheets/investigation/WitcherObstacleSheet.js.md) | Сверено | B09: V1 defaultOptions/getData и skills; отсутствие собственного броска. |
| [module/item/sheets/mixins/associatedDiagramMixin.js](files/module/item/sheets/mixins/associatedDiagramMixin.js.md) | Сверено | B06: Типы/область drop, снятие UUID, update без ожидания; ошибка offsetParent повторена I06. |
| [module/item/systems/repair.js](files/module/item/systems/repair.js.md) | Сверено | B06: Полный процесс/RepairData, DC−5+2*enchants, цена без оплаты; R04/R05 и последовательность ранних барьеров. |
| [module/item/witcherItem.js](files/module/item/witcherItem.js.md) | Сверено | B04: Выбор атаки, рецепты, генератор добычи, пять примесей и собственный проход эффектов без фаз; статическая сверка с issues37–42. |
| [module/scripts/chat.js](files/module/scripts/chat.js.md) | Сверено | B14: T02: три listener по первому button, data-атрибуты без проверки roll/type; repair owner до guard. |
| [module/scripts/helper.js](files/module/scripts/helper.js.md) | Сверено | B11: Выбор Actor/User, optional GM, addPart/getCustomModifier; потребители .023/.039/.040. |
| [module/scripts/investigation/rollClue.js](files/module/scripts/investigation/rollClue.js.md) | Сверено | B09: Q02: выбор Actor до навыков, отмена и threshold, detached rollSkill. |
| [module/scripts/regions/regionHooks.js](files/module/scripts/regions/regionHooks.js.md) | Сверено | B08: G04: active scene, пропущенная duration и отсутствие combatant; update-параметры не используются. |
| [module/scripts/rollConfig.js](files/module/scripts/rollConfig.js.md) | Сверено | B11: Defaults showResult и восемь фиксированных опций; options не общий merge. |
| [module/scripts/rolls/extendedRoll.js](files/module/scripts/rolls/extendedRoll.js.md) | Сверено | B11: K01: порядок крита/порога/публикации; flags без await, showSuccess не gate. |
| [module/scripts/rolls/fumble.js](files/module/scripts/rolls/fumble.js.md) | Сверено | B11: K02: границы, constructor-dispatch и UUID speaker; результат только текстовый. |
| [module/scripts/statusEffects/applyStatusEffect.js](files/module/scripts/statusEffects/applyStatusEffect.js.md) | Сверено | B04: E05: appliedEffects против core toggle; текущий listener отдельно от неиспользуемого пакетного export. |
| [module/scripts/temporaryEffects/applyActiveEffect.js](files/module/scripts/temporaryEffects/applyActiveEffect.js.md) | Сверено | B04: Маршруты ownership/query/clone; source/prepared длительность и отдельная передача улучшений различены. |
| [module/setup/config.js](files/module/setup/config.js.md) | Сопоставлено | B01: S07 сверил все 36 справочников и их размеры с карточкой, 52 skillMap, 26 уникальных статусов и JSON payload; правила книг и все эффекты не воспроизводились. |
| [module/setup/deprecations.js](files/module/setup/deprecations.js.md) | Сопоставлено | B01: пустая deprecationWarnings; импорт читает ссылку DialogV2, но тело не уведомляет и не меняет данные. |
| [module/setup/handlebars.js](files/module/setup/handlebars.js.md) | Сопоставлено | B01: все 17 helpers и 59 путей; S05, просмотр тел и контрактов HBS. Ранее описанные дефекты eachLimit/подсказок сохранены; браузер не запускался. |
| [module/setup/hooks.js](files/module/setup/hooks.js.md) | Сопоставлено | B01: updateCombat вызывает оба обработчика без фильтра update и без ожидания; сравнение с generalCombatHook/regionHooks и issue-00006. |
| [module/setup/queries.js](files/module/setup/queries.js.md) | Сопоставлено | B01: S01 проверил pending addItem, отсутствие вызова вложенного regionProperties и отклонение неизвестного метода; сетевой транспорт не запускался. |
| [module/setup/registerDataModels.js](files/module/setup/registerDataModels.js.md) | Сопоставлено | B01: S06 подтвердил 4 Actor / 22 Item / 2 ActiveEffect / 4 ChatMessage и отдельный documentClass; несогласованные типы — issue-00005. |
| [module/setup/registerSheets.js](files/module/setup/registerSheets.js.md) | Сопоставлено | B01: imports, общий/специальные Items, Actor types и ActiveEffectConfig сопоставлены; открытие окон/выбор default ядром не повторялись. |
| [module/setup/settings.js](files/module/setup/settings.js.md) | Сопоставлено | B01: S06 подтвердил 9 world-настроек, фильтр Item packs и отсутствие settings.set/onChange. |
| [module/setup/socketHook.js](files/module/setup/socketHook.js.md) | Сопоставлено | B01: S02 — known UUID маршрут, unknown TypeError и ранний выход неактивного GM; отдельный протокол от User.query. |
| [system.json](files/system.json.md) | Сопоставлено | B01: декларации ID, ресурсов, 7 packs, 8 языков и типов сопоставлены с регистрацией; S06. Фактическая загрузка Foundry не проверена. |
| [templates/chat/combat/heal.hbs](files/templates/chat/combat/heal.hbs.md) | Сверено | B07: Только подпись и heal, выбор speaker принадлежит producer. |
| [templates/chat/combat/spellItem.hbs](files/templates/chat/combat/spellItem.hbs.md) | Сверено | B14: Кнопки до броска, selfEffects array-display vs dictionary; T02 проверяет heal-потребителя. |
| [templates/chat/combat/statusEffect.hbs](files/templates/chat/combat/statusEffect.hbs.md) | Сверено | B04: name/img берутся из turnStartEffects; уведомление не содержит apply-status. |
| [templates/chat/currency-conversion.hbs](files/templates/chat/currency-conversion.hbs.md) | Сверено | B13: Декларативное сообщение результата, без перечитывания wallet/Log. |
| [templates/chat/heal/resting-status.hbs](files/templates/chat/heal/resting-status.hbs.md) | Сверено | B07: Исходные totalRec/isResting и условный actualWoundList; P05:producer не передаёт фактические результаты. |
| [templates/chat/item/appliedTemporaryItemImprovements.hbs](files/templates/chat/item/appliedTemporaryItemImprovements.hbs.md) | Сверено | B04: Контракт item/temporaryItemImprovements и пассивное уведомление; без выполнения переноса. |
| [templates/chat/item/consume.hbs](files/templates/chat/item/consume.hbs.md) | Сверено | B06: Пассивные name/heal/statusEffects; обработчиков применения в шаблоне нет. |
| [templates/chat/item/dismantle.hbs](files/templates/chat/item/dismantle.hbs.md) | Сверено | B13: foundItems означает resolver, не успешную запись; quantity не выводится. |
| [templates/chat/item/repair.hbs](files/templates/chat/item/repair.hbs.md) | Сверено | B06: Флаги запроса/заказа/компонентов, request-repair dataset; R05: unknown-only скрыты. |
| [templates/chat/rewards.hbs](files/templates/chat/rewards.hbs.md) | Сверено | B13: N04: monetary-блок скрыт при штатном producer; amount key отдельная проблема. |
| [templates/dialog/activeEffects/wizard.hbs](files/templates/dialog/activeEffects/wizard.hbs.md) | Сверено | B04: Один selectOptions; два потребителя wizard/chooseSkill, массив группы сериализуется выбором. |
| [templates/dialog/combat/profession-attack.hbs](files/templates/dialog/combat/profession-attack.hbs.md) | Сверено | B14: 14 полей, extra без STA-поля; meleeBonus preview не гарантирует участие в damage. |
| [templates/dialog/combat/spell-attack.hbs](files/templates/dialog/combat/spell-attack.hbs.md) | Сверено | B14: 2–6 полей, textSTA,оба фокуса из одного словаря; callback и оплата в Actor. |
| [templates/dialog/deprecations/lifepathModifiers.hbs](files/templates/dialog/deprecations/lifepathModifiers.hbs.md) | Сверено | B11: Только текст списка affectedActors; миграцию не исполняет. |
| [templates/dialog/deprecations/statSkillModifiers.hbs](files/templates/dialog/deprecations/statSkillModifiers.hbs.md) | Сверено | B11: Только текст списка affectedActors; действующий вызывающий код не найден. |
| [templates/dialog/heal/heal-rest.hbs](files/templates/dialog/heal/heal-rest.hbs.md) | Сверено | B07: Четыре фиксированных ID и два информационных элемента; немодальные окна делят глобальный поиск. |
| [templates/dialog/investigation/chooseEvidenceSkill.hbs](files/templates/dialog/investigation/chooseEvidenceSkill.hbs.md) | Сверено | B09: selectedSkill из CONFIG.skillMap, политика отмены определяется rollClue. |
| [templates/dialog/repair-dialog.hbs](files/templates/dialog/repair-dialog.hbs.md) | Сверено | B06: data.damagedLocations и общий components partial; HBS пустой список не вызывает JS-ошибку. |
| [templates/partials/associated-diagram.hbs](files/templates/partials/associated-diagram.hbs.md) | Сверено | B06: Верхний description вместо system.description, перепутанные add/remove titles, drop-markers. |
| [templates/partials/associated-item.hbs](files/templates/partials/associated-item.hbs.md) | Сверено | B06: Результат и resultQuantity; тот же неверный верхний description, действия отдельного листа. |
| [templates/partials/character/custom-skill-display.hbs](files/templates/partials/character/custom-skill-display.hbs.md) | Сверено | B11: K03: Item-контекст не содержит skill.*, data-action ведёт к builtin lookup. |
| [templates/partials/character/skill-display.hbs](files/templates/partials/character/skill-display.hbs.md) | Сверено | B11: modifiedValue и флаги, isVisible не читается. |
| [templates/partials/character/substances.hbs](files/templates/partials/character/substances.hbs.md) | Сверено | B13: Девять pannels/счётчиков/таблиц, subtype теряется в summary B10. |
| [templates/partials/character/tab-background.hbs](files/templates/partials/character/tab-background.hbs.md) | Сверено | B12: L03: eachLimit создаёт пустую запись при избытке; формы по ключу lifeEvent и индексу note. |
| [templates/partials/character/tab-magic.hbs](files/templates/partials/character/tab-magic.hbs.md) | Сверено | B14: Шесть tabs,12 списков,focus/vigor/IP; общая Monster-схема отличается. |
| [templates/partials/character/tab-profession.hbs](files/templates/partials/character/tab-profession.hbs.md) | Сверено | B14: Десять навыков,35 inline-путей с расой; dispatcher читает name, editors raw. |
| [templates/partials/character/tab-skills.hbs](files/templates/partials/character/tab-skills.hbs.md) | Сверено | B11: Семь групп system.skills и две проекции списков, IP/training отдельно. |
| [templates/partials/character/tab-stats.hbs](files/templates/partials/character/tab-stats.hbs.md) | Сверено | B11: max/value/разницы; репутация повторяет value вместо max. |
| [templates/partials/character-header.hbs](files/templates/partials/character-header.hbs.md) | Сверено | B12: L04: три восстановленные ссылки rewards; Item имена и родина только отображаются. |
| [templates/partials/components-list.hbs](files/templates/partials/components-list.hbs.md) | Сверено | B06: Готовые количества/required/cost; пустой ввод цены и общий total-price потребляет costEditMixin. |
| [templates/partials/crit-wounds-table.hbs](files/templates/partials/crit-wounds-table.hbs.md) | Сверено | B07: Документные критические травмы, inline daysHealed и treat UUID; дубль в tab-effects остаётся issue54. |
| [templates/partials/effect-part.hbs](files/templates/partials/effect-part.hbs.md) | Сверено | B04: Категории, suppression только при actor, кнопки и скрытое описание; разные listeners Actor/Item. |
| [templates/partials/item-header.hbs](files/templates/partials/item-header.hbs.md) | Сверено | B05: Общие именованные поля, mutagen-ветка и настройка clickableImage; I01: поля флага нет в схемах. |
| [templates/partials/item-image.hbs](files/templates/partials/item-image.hbs.md) | Сверено | B05: Условный .item-show относится к старому шаблонному пути; текущий инвентарь не подключает partial. |
| [templates/partials/monster/monster-custom-skill-display.hbs](files/templates/partials/monster/monster-custom-skill-display.hbs.md) | Сверено | B11: Правильный Item ID/#custom-rollable, value/активная добавка; массива modifiers нет. |
| [templates/partials/monster/monster-details-tab.hbs](files/templates/partials/monster/monster-details-tab.hbs.md) | Сверено | B12: Четыре строки whitespace, нет контекста/действий. |
| [templates/partials/monster/monster-inventory-tab.hbs](files/templates/partials/monster/monster-inventory-tab.hbs.md) | Сверено | B10: Старые SP/resistance и class-only export; не используется зарегистрированным V2. |
| [templates/partials/monster/monster-skill-display.hbs](files/templates/partials/monster/monster-skill-display.hbs.md) | Сверено | B11: Legacy isVisible и именной ввод value; действующий partial отличается. |
| [templates/partials/monster/monster-skill-tab.hbs](files/templates/partials/monster/monster-skill-tab.hbs.md) | Сверено | B11: Старые семь групп/pannels, собственные навыки через legacy partial. |
| [templates/partials/monster/monster-spell-tab.hbs](files/templates/partials/monster/monster-spell-tab.hbs.md) | Сверено | B14: Старый HBS/pannels/inlineSTA и фокусы; не текущий V2. |
| [templates/partials/spell-header.hbs](files/templates/partials/spell-header.hbs.md) | Сверено | B08: Классовые ветви и словари; editImage/configureItem присутствуют. |
| [templates/sheets/activeEffect/system-specific.hbs](files/templates/sheets/activeEffect/system-specific.hbs.md) | Сверено | B04: Безусловное applyAfterCalculations и условные apply*-поля; отсутствующее поле временного улучшения подтверждено E01. |
| [templates/sheets/actor/configuration/app/edit-skills.hbs](files/templates/sheets/actor/configuration/app/edit-skills.hbs.md) | Сверено | B11: level-up и поля встроенной модели; для Monster схема развития отсутствует. |
| [templates/sheets/actor/configuration/app/edit-stats.hbs](files/templates/sheets/actor/configuration/app/edit-stats.hbs.md) | Сверено | B11: Выбор stats/derivedStats, контекст @root.type. |
| [templates/sheets/actor/configuration/app/partials/stats-block.hbs](files/templates/sheets/actor/configuration/app/partials/stats-block.hbs.md) | Сверено | B11: K04: input показывает max8 и именован unmodifiedMax; полный FormData roundtrip здесь не повторялся. |
| [templates/sheets/actor/configuration/monster/general.hbs](files/templates/sheets/actor/configuration/monster/general.hbs.md) | Сверено | B12: customStat показывает три max; классификация монстра не редактируется. |
| [templates/sheets/actor/configuration/monster/header.hbs](files/templates/sheets/actor/configuration/monster/header.hbs.md) | Сверено | B12: Только локализованный заголовок настроек. |
| [templates/sheets/actor/configuration/partials/skillConfiguration.hbs](files/templates/sheets/actor/configuration/partials/skillConfiguration.hbs.md) | Сверено | B11: DataField isVisible/имена core; проблема commonsp ограничивает одну запись. |
| [templates/sheets/actor/currencyConverter/currencyConverter.hbs](files/templates/sheets/actor/currencyConverter/currencyConverter.hbs.md) | Сверено | B13: Четыре поля amount/from/to/fee; формовый тип отдельно от проверки метода. |
| [templates/sheets/actor/loot-sheet.hbs](files/templates/sheets/actor/loot-sheet.hbs.md) | Сверено | B13: Шесть таблиц/семь валют; нет editImage action. |
| [templates/sheets/actor/monster-sheet.hbs](files/templates/sheets/actor/monster-sheet.hbs.md) | Сверено | B12: Старый неподлежающий регистрации V2 шаблон;11 из12 буквальных image paths отсутствуют. |
| [templates/sheets/actor/partials/character/inventory/inventory-items-summary.hbs](files/templates/sheets/actor/partials/character/inventory/inventory-items-summary.hbs.md) | Сверено | B10: J04: поля itemType/spellType, отсутствует subtype. |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-alchemical.hbs](files/templates/sheets/actor/partials/character/inventory/tab-inventory-alchemical.hbs.md) | Сверено | B10: Количество/описание/мутации, отсутствующий Weapon.Availability. |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-armors.hbs](files/templates/sheets/actor/partials/character/inventory/tab-inventory-armors.hbs.md) | Сверено | B10: armorPartsInfo и текущая resistance; repair только Character, слоты используют общий chooser. |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-components.hbs](files/templates/sheets/actor/partials/character/inventory/tab-inventory-components.hbs.md) | Сверено | B10: subtype доходит до summary, но не до dataset; J04. |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-diagrams.hbs](files/templates/sheets/actor/partials/character/inventory/tab-inventory-diagrams.hbs.md) | Сверено | B10: isFormulae меняет показ DC, кнопка всегда crafting-craft. |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-mounts.hbs](files/templates/sheets/actor/partials/character/inventory/tab-inventory-mounts.hbs.md) | Сверено | B10: Четыре описательных параметра mount, quantity отдельно; дополнительных CRUD нет. |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-runes-glyphs.hbs](files/templates/sheets/actor/partials/character/inventory/tab-inventory-runes-glyphs.hbs.md) | Сверено | B10: Статусы/проценты только выводятся, применение через слоты других таблиц. |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-valuables.hbs](files/templates/sheets/actor/partials/character/inventory/tab-inventory-valuables.hbs.md) | Сверено | B10: Добыча/ценности/контейнеры; UUID вложенных строк не равен локальному Item ID. |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-weapons.hbs](files/templates/sheets/actor/partials/character/inventory/tab-inventory-weapons.hbs.md) | Сверено | B10: Оружие, prepared-улучшения, reliable/quantity; J02 связан с отображением. |
| [templates/sheets/actor/partials/character/sidebar.hbs](files/templates/sheets/actor/partials/character/sidebar.hbs.md) | Сверено | B12: HP icon сравнивает base, progress/max — prepared; десять input при включённых опциях. |
| [templates/sheets/actor/partials/character/spell-type-list.hbs](files/templates/sheets/actor/partials/character/spell-type-list.hbs.md) | Сверено | B14: Список/описания, item use и inherited summary, без изучения; вложенные component.name отсутствуют. |
| [templates/sheets/actor/partials/character/tab-effects.hbs](files/templates/sheets/actor/partials/character/tab-effects.hbs.md) | Сверено | B04: Partial травм плюс повторный each той же коллекции; общий список AE и действия листов. |
| [templates/sheets/actor/partials/loot/loot-item-display.hbs](files/templates/sheets/actor/partials/loot/loot-item-display.hbs.md) | Сверено | B13: dragable/data-id отличаются от core draggable/itemId; inline данные Item. |
| [templates/sheets/actor/partials/monster/header.hbs](files/templates/sheets/actor/partials/monster/header.hbs.md) | Сверено | B12: Имя редактируется; category/threat/difficulty только выводятся, bounty отсутствует. |
| [templates/sheets/actor/partials/monster/sidebar.hbs](files/templates/sheets/actor/partials/monster/sidebar.hbs.md) | Сверено | B12: HP/base и11–12 input, armorTailWing не скрывается; category path динамический. |
| [templates/sheets/actor/partials/monster/tabs/partials/monster-info.hbs](files/templates/sheets/actor/partials/monster/tabs/partials/monster-info.hbs.md) | Сверено | B12: Пять StringField сведений, weight не масса инвентаря. |
| [templates/sheets/actor/partials/monster/tabs/partials/monster-knowledge.hbs](files/templates/sheets/actor/partials/monster/tabs/partials/monster-knowledge.hbs.md) | Сверено | B12: Три HTML-поля получают raw *.value вместо *.enriched. |
| [templates/sheets/actor/partials/monster/tabs/partials/monster-notes.hbs](files/templates/sheets/actor/partials/monster/tabs/partials/monster-notes.hbs.md) | Сверено | B12: Item note и массив Actor.notes различны; each-контекст system.description корректен. |
| [templates/sheets/actor/partials/monster/tabs/partials/monster-status.hbs](files/templates/sheets/actor/partials/monster/tabs/partials/monster-status.hbs.md) | Сверено | B12: Текстовые immunities и массив statusEffectImmunities не одно поле. |
| [templates/sheets/actor/partials/monster/tabs/tab-details.hbs](files/templates/sheets/actor/partials/monster/tabs/tab-details.hbs.md) | Сверено | B12: Две вложенные вкладки и четыре partial, наследуют контекст. |
| [templates/sheets/actor/partials/monster/tabs/tab-inventory.hbs](files/templates/sheets/actor/partials/monster/tabs/tab-inventory.hbs.md) | Сверено | B10: Действующий V2 использует общие таблицы и exportLoot action; repair handler не добавлен. |
| [templates/sheets/actor/partials/monster/tabs/tab-profession.hbs](files/templates/sheets/actor/partials/monster/tabs/tab-profession.hbs.md) | Сверено | B14: Только definingSkill и notes; три inline-поля Item. |
| [templates/sheets/actor/rewards/currency.hbs](files/templates/sheets/actor/rewards/currency.hbs.md) | Сверено | B13: Просмотр label/amount/type, lookup currency корректен. |
| [templates/sheets/actor/rewards/header.hbs](files/templates/sheets/actor/rewards/header.hbs.md) | Сверено | B13: Статическая локализация заголовка журнала. |
| [templates/sheets/actor/rewards/ip.hbs](files/templates/sheets/actor/rewards/ip.hbs.md) | Сверено | B13: Просмотр label/ip/isMagic без редактирования. |
| [templates/sheets/actor/tabs/tab-inventory.hbs](files/templates/sheets/actor/tabs/tab-inventory.hbs.md) | Сверено | B10: Семь валют, вес/ENC и категории; общие обработчики .026 и Character. |
| [templates/sheets/investigation/clue-sheet.hbs](files/templates/sheets/investigation/clue-sheet.hbs.md) | Сверено | B09: Именованные поля Item, сохранение базовым V1, multi-select. |
| [templates/sheets/investigation/mystery-sheet.hbs](files/templates/sheets/investigation/mystery-sheet.hbs.md) | Сверено | B09: Структура двух таблиц, 12 заголовков улик против 13 ячеек строки, literal EN-подписи. |
| [templates/sheets/investigation/obstacle-sheet.hbs](files/templates/sheets/investigation/obstacle-sheet.hbs.md) | Сверено | B09: Шесть полей препятствия, сохранение базовым V1. |
| [templates/sheets/investigation/partials/clue-display.hbs](files/templates/sheets/investigation/partials/clue-display.hbs.md) | Сверено | B09: Контекст each сохраняет system.skillsUsed; 13 ячеек, действия GM и roll. |
| [templates/sheets/investigation/partials/obstacle-display.hbs](files/templates/sheets/investigation/partials/obstacle-display.hbs.md) | Сверено | B09: Контекст each, isHidden/CSS, действия GM; собственная кнопка roll отсутствует. |
| [templates/sheets/item/alchemical-sheet.hbs](files/templates/sheets/item/alchemical-sheet.hbs.md) | Сверено | B06: type/avail/time/effect и условная toxicity potion/decoction; header/config связи. |
| [templates/sheets/item/armor-sheet.hbs](files/templates/sheets/item/armor-sheet.hbs.md) | Сверено | B05: Шесть исходных SP/щиты, prepared сопротивления в именованных checkbox; два списка effects. |
| [templates/sheets/item/component-sheet.hbs](files/templates/sheets/item/component-sheet.hbs.md) | Сверено | B06: R03: реальный HBS останавливается на отсутствующем select; три таких блока. |
| [templates/sheets/item/configuration/partials/attackOptionsPart.hbs](files/templates/sheets/item/configuration/partials/attackOptionsPart.hbs.md) | Сверено | B05: Семь formGroup и три ветви; правильная подпись spell, itemUse также отсутствует. |
| [templates/sheets/item/configuration/partials/profession/profAttackOptionsPart.hbs](files/templates/sheets/item/configuration/partials/profession/profAttackOptionsPart.hbs.md) | Сверено | B07: Общий Set и только melee/ranged флаги; не полный выбор навыков обычного оружия. |
| [templates/sheets/item/configuration/partials/profession/skillPathPart.hbs](files/templates/sheets/item/configuration/partials/profession/skillPathPart.hbs.md) | Сверено | B07: Три явных включения skillPathSkillPart с соответствующими SchemaField/данными. |
| [templates/sheets/item/configuration/partials/profession/skillPathSkillPart.hbs](files/templates/sheets/item/configuration/partials/profession/skillPathSkillPart.hbs.md) | Сверено | B07: Условия attack/defense/usage/thresholds, ручные записи адресуются по skillName; P02/P03. |
| [templates/sheets/item/configuration/tabs/activeEffectConfiguration.hbs](files/templates/sheets/item/configuration/tabs/activeEffectConfiguration.hbs.md) | Сверено | B05: Обёртка списка effect-part, действия наследует конфигурация. |
| [templates/sheets/item/configuration/tabs/armorGeneral.hbs](files/templates/sheets/item/configuration/tabs/armorGeneral.hbs.md) | Сверено | B05: 12 formGroup SP; I04 подтвердил четыре EN-only подсказки, fallback не является отсутствием строки во всех языках. |
| [templates/sheets/item/configuration/tabs/consumablePropertiesConfiguration.hbs](files/templates/sheets/item/configuration/tabs/consumablePropertiesConfiguration.hbs.md) | Сверено | B06: R01: effect.id и addsTempHp не соответствуют модели; действия без form name. |
| [templates/sheets/item/configuration/tabs/damagePropertiesConfiguration.hbs](files/templates/sheets/item/configuration/tabs/damagePropertiesConfiguration.hbs.md) | Сверено | B05: Поля DamageProperties, silverTrait/silverDamage, условный cap; собственные effects редактируемы, улучшения disabled. |
| [templates/sheets/item/configuration/tabs/defensePropertiesConfiguration.hbs](files/templates/sheets/item/configuration/tabs/defensePropertiesConfiguration.hbs.md) | Сверено | B05: Три formGroup, defendsAgainst использует список attackOptions; методы модели Armor отсутствуют отдельно. |
| [templates/sheets/item/configuration/tabs/general.hbs](files/templates/sheets/item/configuration/tabs/general.hbs.md) | Сверено | B05: Условия существования полей и melee/ranged/spell; itemUse отсутствует, spell ошибочно подписан ranged. |
| [templates/sheets/item/configuration/tabs/header.hbs](files/templates/sheets/item/configuration/tabs/header.hbs.md) | Сверено | B05: Один локализованный заголовок, без данных/действий. |
| [templates/sheets/item/configuration/tabs/regionPropertiesConfiguration.hbs](files/templates/sheets/item/configuration/tabs/regionPropertiesConfiguration.hbs.md) | Сверено | B05: Четыре behaviours и отсутствующий createRegionFromTemplate; блокировка parts отдельна от ошибки поля. |
| [templates/sheets/item/configuration/tabs/spellGeneral.hbs](files/templates/sheets/item/configuration/tabs/spellGeneral.hbs.md) | Сверено | B08: Словари статусов с ID, inherited edit/add/remove и боевые partials. |
| [templates/sheets/item/container-sheet.hbs](files/templates/sheets/item/container-sheet.hbs.md) | Сверено | B09: Подготовленные itemContent и storedWeight/carry, listener удаления по UUID. |
| [templates/sheets/item/criticalWound-sheet.hbs](files/templates/sheets/item/criticalWound-sheet.hbs.md) | Сверено | B07: Степень/treatment/location/дни, enriched description, lesserEffect/followUp; эффект задаётся конфигурацией. |
| [templates/sheets/item/diagrams-sheet.hbs](files/templates/sheets/item/diagrams-sheet.hbs.md) | Сверено | B06: isFormulae выбирает форму, alchemyDC выбирает изготовление; known/unknown rows, пробелы ключей подсказок. |
| [templates/sheets/item/enhancement-sheet.hbs](files/templates/sheets/item/enhancement-sheet.hbs.md) | Сверено | B05: Бонусы SP/сопротивления только при type=armor; категории weapon/rune выбирают статусный справочник. |
| [templates/sheets/item/hex-sheet.hbs](files/templates/sheets/item/hex-sheet.hbs.md) | Сверено | B08: Нет editImage action; danger и liftRequirement соответствуют полям. |
| [templates/sheets/item/homeland-sheet.hbs](files/templates/sheets/item/homeland-sheet.hbs.md) | Сверено | B07: 26 вариантов value, otherValue только при other, configureItem у общего листа. |
| [templates/sheets/item/mount-sheet.hbs](files/templates/sheets/item/mount-sheet.hbs.md) | Сверено | B13: Описание и четыре поля mount плюс общая шапка. |
| [templates/sheets/item/mutagen-sheet.hbs](files/templates/sheets/item/mutagen-sheet.hbs.md) | Сверено | B06: source/effect/alchemyDC/minorMutation, цвет в общей шапке. |
| [templates/sheets/item/note-sheet.hbs](files/templates/sheets/item/note-sheet.hbs.md) | Сверено | B12: Старый неподключённый template, имя input=item.name, отдельное описание. |
| [templates/sheets/item/profession-sheet.hbs](files/templates/sheets/item/profession-sheet.hbs.md) | Сверено | B07: Десять навыков по устойчивым путям name,11 HTML formInput, professionSkills; механика definingSkill не редактируется. |
| [templates/sheets/item/race-sheet.hbs](files/templates/sheets/item/race-sheet.hbs.md) | Сверено | B07: Четыре formGroup с enriched/value, пять select, name/img/sourcebook; Actor-шаблон читает raw иначе. |
| [templates/sheets/item/ritual-sheet.hbs](files/templates/sheets/item/ritual-sheet.hbs.md) | Сверено | B08: Старые корневые пути области; идентификация строк по component.item.uuid. |
| [templates/sheets/item/skill-item-sheet.hbs](files/templates/sheets/item/skill-item-sheet.hbs.md) | Сверено | B11: Только имя/attribute; value и признаки здесь не редактируются. |
| [templates/sheets/item/spell-sheet.hbs](files/templates/sheets/item/spell-sheet.hbs.md) | Сверено | B08: Вложенные templateProperties, независимые causeDamages/createsShield/doesHeal. |
| [templates/sheets/item/valuable-sheet.hbs](files/templates/sheets/item/valuable-sheet.hbs.md) | Сверено | B06: type/avail/conceal/description, selects локальный; расход отдельно. |
| [templates/sheets/item/weapon-sheet.hbs](files/templates/sheets/item/weapon-sheet.hbs.md) | Сверено | B05: Ammo-ветви, базовые поля, damage-type checkbox без name и partial рецепта; действия определены листом. |

## Реестр сверки issues

Результат проверки здесь отделён от статуса issue. Все карточки остаются `potential` до решения пользователя.

| Issue | Результат | Основание, связи и ограничения |
| --- | --- | --- |
| [issue-00001](../../issues/potential/issue-00001.md) | Наблюдение; нужен запуск Foundry | B01: локальный ID и каталог различаются; конкретного сбоя загрузчика не получено. Карточка корректно не заявляет подтверждённую неисправность. |
| [issue-00002](../../issues/potential/issue-00002.md) | Основание подтверждается | B01/S04: ready без pack падает до hotbar/socket/deprecations; контроль с pack проходит. Запуск мира не выполнен. |
| [issue-00003](../../issues/potential/issue-00003.md) | Основание подтверждается | B01/S03: statusEffects — массив без querySelector; до API EffectCounter выполнение не доходит. Внешний модуль не исследован. |
| [issue-00004](../../issues/potential/issue-00004.md) | Основание подтверждается кодом | B01: skillMap.commonspeech.name=commonsp, chooseSkill строит путь по ключу, intData объявляет commonsp. Последующие симптомы навыков/редакторов имеют ту же причину. |
| [issue-00005](../../issues/potential/issue-00005.md) | Расхождение подтверждается; последствия условны | B01/S06: mystery/clue/obstacle/skill отсутствуют в manifest, но зарегистрированы. base — отдельный штатный тип. Серверная сборка game.model не проверена. |
| [issue-00006](../../issues/potential/issue-00006.md) | Основание подтверждается кодом | B01: update не фильтруется; current Actor/active regions обрабатываются и при flags. Предыдущее изолированное воспроизведение отделено от нового чтения. |
| [issue-00007](../../issues/potential/issue-00007.md) | Основание подтверждается | B01/S05: leftLeg/rightLeg имеют обратные подписи; значения SP и цвета идут по исходной части. Это ошибка подсказки, не расчёта SP. |
| [issue-00008](../../issues/potential/issue-00008.md) | Основание подтверждается | B01/S01: true возвращается при pending addItem и при отсутствующем методе вложенной модели. Граница async отдельно от правильности маршрута issue-00009. |
| [issue-00009](../../issues/potential/issue-00009.md) | Основание подтверждается кодом и частичным прогоном | B01/S01: query не достигает regionProperties; deleteSpellVisualEffect не разрешён. В примеси uuid:item.uuid без определения item; полное удаление области не запускалось. |
| [issue-00010](../../issues/potential/issue-00010.md) | Условный дефект входа подтверждается | B01/S02: unknown вызывает TypeError на активном GM; штатные два типа проходят соответствующую ветвь. Встречаемость unknown в мире не установлена. |
| [issue-00011](../../issues/potential/issue-00011.md) | Основание подтверждается | B02/M02: max7 при отсутствующей/нулевой/существующей базе →0/7/4; CommonActorData сбрасывает vigor.max при отсутствии base. Старые миры не импортировались. |
| [issue-00012](../../issues/potential/issue-00012.md) | Основание подтверждается | B02/M06: два calculateStats дают luck14 и toxicity110; порядок двух вызовов сверён в prepareDerivedData. Полный Actor lifecycle не воспроизводился. |
| [issue-00013](../../issues/potential/issue-00013.md) | Основание подтверждается кодом | B02/M03: createEnrichedText разделяет raw/enriched; три formGroup monster-knowledge читают raw .value. Прежние HBS-прогоны учтены, браузер не запускался. |
| [issue-00014](../../issues/potential/issue-00014.md) | Основание подтверждается | B02/M05: Rep отсутствует во всех8 словарях после expandObject и en fallback; schema label и потребитель autocomplete сопоставлены. |
| [issue-00015](../../issues/potential/issue-00015.md) | Основание подтверждается | B02/M04: свежие52 label undefined; после повторной модели заполнены; isVisible.label остаётся undefined. Полный Actor.create не проверен. |
| [issue-00016](../../issues/potential/issue-00016.md) | Основание подтверждается | B02/M05: три camelCase CRA-ключа отсутствуют во всех8 локалях, lower-case существуют; skillMap и миграция дают разные ключи. |
| [issue-00017](../../issues/potential/issue-00017.md) | Основание подтверждается; описание уточнено | B02/M07: настоящий Log и levelUpSkill дают magic6/magic10. D01 уточняет конфликт payload вместо гарантированного несписания в базе; связан с issue-00028. |
| [issue-00018](../../issues/potential/issue-00018.md) | Основание подтверждается | B02/M08: текущий skill-display выводит скрытый навык; прежний monster-шаблон скрывает. PARTS текущего MonsterSheet указывает общий шаблон. |
| [issue-00019](../../issues/potential/issue-00019.md) | Основание сохранено | B03: SchemaField(value) против интерполяции записи и путей мастера; исправление формы не выбиралось. |
| [issue-00020](../../issues/potential/issue-00020.md) | Основание сохранено | B03: C06: 100 crown→обмен 10 crown в crown отправляет 110; это коллизия computed key. |
| [issue-00021](../../issues/potential/issue-00021.md) | Основание сохранено | B03: generalCombatHook не переносит damage.type; applyDamageFromStatus читает отсутствующее поле. Не тождественно issue-00006. |
| [issue-00022](../../issues/potential/issue-00022.md) | Основание сохранено | B03: В лечение передаётся heal.amount, modifier не читается; назначение ожидаемой добавки не подменяет правило. |
| [issue-00023](../../issues/potential/issue-00023.md) | Основание сохранено | B03: Фильтрация по наличию temporaryHp выбирает эффект целиком; внутренний цикл расходует все changes. Полный жизненный цикл AE отдельно. |
| [issue-00024](../../issues/potential/issue-00024.md) | Основание сохранено | B03: C02: настоящий _prepareContext и CharacterData дают ключу 10 запись 110 в toObject(false); _source остался прежним. |
| [issue-00025](../../issues/potential/issue-00025.md) | Основание сохранено | B03: C03: applyAP=true при штатном properties вызывает TypeError до проверки брони; AP-ветка возвращается раньше. |
| [issue-00026](../../issues/potential/issue-00026.md) | Основание сохранено | B03: C03: damage20,multiplier3 →20 без сопротивления,30 с одним,45 с двумя. Назначение коэффициента требует решения. |
| [issue-00027](../../issues/potential/issue-00027.md) | Основание сохранено | B03: flat возвращается со знаком, но ветка только >0; независим от ошибки пути applyAP и кратности multiplication. |
| [issue-00028](../../issues/potential/issue-00028.md) | Основание сохранено | B03: C04: await обработчика расхода завершается при pending Actor.update; это отдельный контракт от issue-00017. |
| [issue-00029](../../issues/potential/issue-00029.md) | Дублируется issue-00200 | B03/B12: одна причина и один сценарий; предложена основная29, статусы обеих potential сохранены. |
| [issue-00030](../../issues/potential/issue-00030.md) | Основание сохранено | B03: C01: в MonsterData нет девяти редактируемых путей обучения/IP; общий tab-skills и регистрация вкладки сверены. |
| [issue-00031](../../issues/potential/issue-00031.md) | Основание сохранено | B03: C05: непустые иммунитеты приводят к ReferenceError statusEffectId; отдельный scripts-обработчик имеет свой параметр. |
| [issue-00032](../../issues/potential/issue-00032.md) | Основание сохранено | B03: C05: wrapper возвращает 6 зон монстру с флагом, явный контекст static —7; связь с applyDamageToAllLocations сохранена. |
| [issue-00033](../../issues/potential/issue-00033.md) | Основание сохранено | B04: E02 повторил недопустимую формулу положительной добавки; оба определения defense читаются одинаково. |
| [issue-00034](../../issues/potential/issue-00034.md) | Основание сохранено | B04: E06: consumable-ветвь не ожидает операции; removeItemsOfType также без return/await, addItem/removeItem ожидают. |
| [issue-00035](../../issues/potential/issue-00035.md) | Основание сохранено | B04: E03: REF8→6 при P1/нулевой броне за один calculateStat; правило не устанавливалось. |
| [issue-00036](../../issues/potential/issue-00036.md) | Основание сохранено | B04: E03: BODY.max2 не влияет на value8 при unmodifiedMax8; перезапись STA и initial/final сверены отдельно. |
| [issue-00037](../../issues/potential/issue-00037.md) | Основание сохранено | B04: Вызов populateAlchemyCraftComponentsList отсутствует среди класса/примесей; существует getter. |
| [issue-00038](../../issues/potential/issue-00038.md) | Основание сохранено | B04: removeItem/addItem/toMessage не ожидаются в realCraft; успешный бросок не подтверждает запись. |
| [issue-00039](../../issues/potential/issue-00039.md) | Основание сохранено | B04: Прямое results[0], отсутствие проверки []; ядро допускает несколько результатов. Legacy getters поддержаны, не отдельная ошибка API. |
| [issue-00040](../../issues/potential/issue-00040.md) | Основание сохранено | B04: Цикл генерации ожидает roll, но не quantity.update; ++ локальной переменной не обновляет system синхронно. |
| [issue-00041](../../issues/potential/issue-00041.md) | Основание сохранено | B04: realCraft меняет локальный result, не готовые flavor/options.success; отдельная причина от async issue38. |
| [issue-00042](../../issues/potential/issue-00042.md) | Основание сохранено | B04: E04: созданный payload теряет system.changes при полной замене system. |
| [issue-00043](../../issues/potential/issue-00043.md) | Основание сохранено | B04: E01: system без changes падает; changes без флага получают initial. Позднее уточнение .010 связывает это с payload мастера. |
| [issue-00044](../../issues/potential/issue-00044.md) | Основание сохранено | B04: Присваивание prepared duration.rounds перед clone не меняет _source; контракт нового duration/core migration сверён, сетевой итог неизвестен. |
| [issue-00045](../../issues/potential/issue-00045.md) | Основание сохранено | B04: Ветка отсутствующего Item повторяет тот же запрос activeGM; нет локальной остановки. Реальная петля не запускалась. |
| [issue-00046](../../issues/potential/issue-00046.md) | Основание сохранено | B04: E04: отсутствие выбранного weapon приводит к TypeError на name; не маскируется типом улучшения. |
| [issue-00047](../../issues/potential/issue-00047.md) | Основание сохранено | B04: getCurrentCharacter может вернуть undefined; onApplyStatus читает uuid без проверки. |
| [issue-00048](../../issues/potential/issue-00048.md) | Основание сохранено | B04: DOM.querySelector(...).each и передача jQuery в DOM-listener несовместимы; внутренний штатный вызов другого export. |
| [issue-00049](../../issues/potential/issue-00049.md) | Основание сохранено | B04: E05 связал helper с настоящим core toggle: disabled существующий статус удаляется. |
| [issue-00050](../../issues/potential/issue-00050.md) | Основание сохранено | B04: E04 сохраняет start=null; core инициализирует start для Actor, получатель Item; истечение в мире не проверено. |
| [issue-00051](../../issues/potential/issue-00051.md) | Основание сохранено | B04: autocomplete выбирает config по parent.documentName, transfer не читает; мастер пути выбирает другим способом. |
| [issue-00052](../../issues/potential/issue-00052.md) | Основание сохранено | B04: wizardAction изменяет document.system.changes и update({changes}), основную несохранённую форму не собирает. |
| [issue-00053](../../issues/potential/issue-00053.md) | Основание сохранено | B04: E01 подтвердил отсутствие applyAfterCalculations; HBS обращается к нему без условия. |
| [issue-00054](../../issues/potential/issue-00054.md) | Основание сохранено | B04: Два перебора одной коллекции: include crit-wounds-table и локальный each; общая причина для двух листов. |
| [issue-00055](../../issues/potential/issue-00055.md) | Основание сохранено | B04: Повторная вставка wizard/datalist без очистки; ограничение частичным рендером сохранённых частей остаётся. |
| [issue-00056](../../issues/potential/issue-00056.md) | Основание сохранено | B04: Item-конфигурация подключает управление, но не раскрытие effect-description; Actor-listener содержит его отдельно. |
| [issue-00057](../../issues/potential/issue-00057.md) | Основание сохранено | B05: I06: PARTS={} у общего листа; NoteData/шаблон сами не регистрируют специальный лист. |
| [issue-00058](../../issues/potential/issue-00058.md) | Основание сохранено | B05: I06: маршрут Actor вызывает отсутствующий метод; границы Item-наследников и ActiveEffect-метода ядра сохранены. |
| [issue-00059](../../issues/potential/issue-00059.md) | Основание сохранено | B05: Системный _onDrop не вызывает super/Hook; наличие hook в текущем ItemSheetV2 ранее проверено, код не изменён. |
| [issue-00060](../../issues/potential/issue-00060.md) | Основание сохранено | B05: I06: обе реализации принимают текст 'on' за checkbox и отправляют false; один дефект двух копий. |
| [issue-00061](../../issues/potential/issue-00061.md) | Основание сохранено | B05: itemUse присутствует в схеме/каталоге/getItemAttack, поля навыка нет в двух общих формах. |
| [issue-00062](../../issues/potential/issue-00062.md) | Основание сохранено | B05: Заголовок spell в general —ranged; отдельный attackOptionsPart уже правильный, они не смешаны. |
| [issue-00063](../../issues/potential/issue-00063.md) | Основание сохранено | B05: I01: clickableImage отсутствует в схемах; текущий путь инвентаря не использует старый partial. |
| [issue-00064](../../issues/potential/issue-00064.md) | Основание сохранено | B05: I01: spellAttackSkill='spellcasting', CONFIG знает spellcast; редактор может выбрать корректный ключ отдельно. |
| [issue-00065](../../issues/potential/issue-00065.md) | Основание сохранено | B05: I01: WeaponData({attackSkill:'swordsmanship'}) получает пустой Set после очистки старого поля. |
| [issue-00066](../../issues/potential/issue-00066.md) | Основание сохранено | B05: applyRangedMeleeBonus определяется/редактируется, боевой расчёт использует applyMeleeBonus; назначение правила не установлено. |
| [issue-00067](../../issues/potential/issue-00067.md) | Основание сохранено | B05: I02: truthy старые поля/пустой массив заменяют новые вложенные значения; отдельная функция миграции. |
| [issue-00068](../../issues/potential/issue-00068.md) | Основание сохранено | B05: I02: Armor конвертирует массив и удаляет effects; Enhancement/DamageProperties сохраняют результат. |
| [issue-00069](../../issues/potential/issue-00069.md) | Основание сохранено | B05: I05: mergeDamageProperties пропускает объект effects; причины отдельно от prepared-ссылки issue70. |
| [issue-00070](../../issues/potential/issue-00070.md) | Основание сохранено | B05: I05: properties===Item.system.damageProperties, addEffects меняет prepared-данные, source прежний. |
| [issue-00071](../../issues/potential/issue-00071.md) | Основание сохранено | B05: ProfessionData обходит defendsAgainst без isDefense; флаг формы не выполняет фильтрацию модели. |
| [issue-00072](../../issues/potential/issue-00072.md) | Основание сохранено | B05: Перебираются только skillPath1–3/skill1–3, definingSkill не включён; отдельно от isDefense. |
| [issue-00073](../../issues/potential/issue-00073.md) | Основание сохранено | B05: На source: damageInstances[0].setType='silver' заменяет метод; основной тип не присваивается. |
| [issue-00074](../../issues/potential/issue-00074.md) | Основание сохранено | B05: _prepareTabs проверяет regionProperties, _configureRenderParts —корневой createTemplate; у SpellData поле вложено. |
| [issue-00075](../../issues/potential/issue-00075.md) | Основание сохранено | B05: HBS запрашивает отсутствующий createRegionFromTemplate; RegionProperties объявляет только behaviours. |
| [issue-00076](../../issues/potential/issue-00076.md) | Основание сохранено | B05: migrateData безусловно копирует tokenPreMove поверх tokenMoveWithin; повторное присутствие старого поля не требуется. |
| [issue-00077](../../issues/potential/issue-00077.md) | Основание сохранено | B05: I03: Weapon/Armor с ID улучшения и actor=null дают TypeError; поле без ID —другой путь. |
| [issue-00078](../../issues/potential/issue-00078.md) | Основание сохранено | B05: I02: существующий ['a'] плюс старый enhancementItems._id='a' даёт ['a','a']; старый источник не удалён. |
| [issue-00079](../../issues/potential/issue-00079.md) | Основание сохранено | B05: I01: пустой meleeAttackSkill останавливает ?? перед заполненным rangedAttackSkill. |
| [issue-00080](../../issues/potential/issue-00080.md) | Основание сохранено | B05: I06: offsetParent=null даёт TypeError; wrappers не возвращают Promise. |
| [issue-00081](../../issues/potential/issue-00081.md) | Основание сохранено | B05: Оба repair вызывают parent.update без return/await; сохранение не следует из завершения метода. |
| [issue-00082](../../issues/potential/issue-00082.md) | Основание сохранено | B05: I03: отрицательная/дробная ёмкость даёт RangeError в new Array; NumberField это не ограничивает. |
| [issue-00083](../../issues/potential/issue-00083.md) | Основание сохранено | B05: I03: при SP3 урон4 не записывает ничего, урон2 записывает1; правило остатка требует решения. |
| [issue-00084](../../issues/potential/issue-00084.md) | Основание сохранено | B05: Словарь ArmorData.effects остаётся одним объектом после flat, filter(statusEffect) не извлекает записи. |
| [issue-00085](../../issues/potential/issue-00085.md) | Основание сохранено | B05: I01: у ArmorData нет isApplicableDefense/createDefenseOption, несмотря на встроенную модель и форму. |
| [issue-00086](../../issues/potential/issue-00086.md) | Основание сохранено | B05: I02: старые SP2/max4 перезаписывают новые8/10; отдельная миграция, не дубль damageProperties. |
| [issue-00087](../../issues/potential/issue-00087.md) | Основание сохранено | B05: I02: старое slashing=true перезаписывает актуальное resistance.slashing=false; старое false пропускается. |
| [issue-00088](../../issues/potential/issue-00088.md) | Основание сохранено | B05: I04: OR улучшения меняет prepared resistance, source сохраняет false; обычный именованный checkbox показывает true. Реальное сохранение не заявлено. |
| [issue-00089](../../issues/potential/issue-00089.md) | Основание сохранено | B05: После разворачивания словаря остаётся следующий барьер: armorEffects записи не содержат statusEffect. Отдельно от issue84. |
| [issue-00090](../../issues/potential/issue-00090.md) | Основание сохранено | B05: I04: четыре ключа отсутствуют в ru, присутствуют в en; английский fallback учтён, не заявляется полная недоступность подсказки. |
| [issue-00091](../../issues/potential/issue-00091.md) | Основание сохранено | B06: R01: модель без id и пустой data-id дают findIndex=-1 и TypeError; удаление также сравнивает несовместимые ID. |
| [issue-00092](../../issues/potential/issue-00092.md) | Основание сохранено | B06: R01: addsTempHp отсутствует в четырёхполевой схеме, HBS запрашивает его при isConsumable. |
| [issue-00093](../../issues/potential/issue-00093.md) | Основание сохранено | B06: MutagenSheet не переопределяет configuration, в отличие от Alchemical/Valuable; данные расхода в модели есть. |
| [issue-00094](../../issues/potential/issue-00094.md) | Основание сохранено | B06: R03 повторил рендер настоящего component-sheet и Missing helper select; selectOptions существует отдельно. |
| [issue-00095](../../issues/potential/issue-00095.md) | Основание сохранено | B06: R02: неразрешённый UUID сохраняет Saved в модели, но knownCraftingComponents теряет name; источник ошибки —лист. |
| [issue-00096](../../issues/potential/issue-00096.md) | Основание сохранено | B06: Оба partial читают верхний description, модель хранит system.description; не путать с обогащением текста. |
| [issue-00097](../../issues/potential/issue-00097.md) | Основание сохранено | B06: R02: старый associatedItem и alchemyDC перезаписывают новые UUID/craftingDC при isFormulae=false. |
| [issue-00098](../../issues/potential/issue-00098.md) | Основание сохранено | B06: В исходнике три вызова с пробелом перед WITCHER; lookup строки не нормализует этот ключ автоматически. |
| [issue-00099](../../issues/potential/issue-00099.md) | Основание сохранено | B06: remove-ссылка имеет actions.add, пустая add-ссылка —actions.remove; действие удаления определяется классом. |
| [issue-00100](../../issues/potential/issue-00100.md) | Основание сохранено | B06: R05: parseInt пустой строки остаётся NaN после ??0 и портит сумму. |
| [issue-00101](../../issues/potential/issue-00101.md) | Основание сохранено | B06: R02: isFormulae=true/alchemyDC0 не выбирает алхимию в Item; форма использует отдельный флаг. |
| [issue-00102](../../issues/potential/issue-00102.md) | Основание сохранено | B06: R04: настоящий RepairData не имеет damagedLocations, обычный repairItem падает; getRestoreReliabilityData также отсутствует ниже. |
| [issue-00103](../../issues/potential/issue-00103.md) | Основание сохранено | B06: Незарегистрированная woundsAffectSkillBase читается до Roll; дополнительная незакрытая скобка только при внешнем true. Полный ремонт не заявлен. |
| [issue-00104](../../issues/potential/issue-00104.md) | Основание сохранено | B06: R04: owned quantity0 отмечается нехваткой, но допуск проходит только после диагностической подстановки damagedLocations; раньше мешает issue102. |
| [issue-00105](../../issues/potential/issue-00105.md) | Основание сохранено | B06: R04: missingComponents=[null] приводит к TypeError oc.img; prepareData добавляет неразрешённый результат без проверки. |
| [issue-00106](../../issues/potential/issue-00106.md) | Основание сохранено | B06: R05: суммы глобальных полей пишутся в первый total-price; подписи listener не ограничены конкретным окном. |
| [issue-00107](../../issues/potential/issue-00107.md) | Основание сохранено | B06: R05: unknown-only даёт showComponents0, блок HBS скрыт; списки данных при этом не исчезают. |
| [issue-00108](../../issues/potential/issue-00108.md) | Основание сохранено | B06: owner.items читается до owner-guard; собственно repair process —следующий независимый этап, см. дополнение .040. |
| [issue-00109](../../issues/potential/issue-00109.md) | Основание сохранено | B07: P01 и source: Race/Profession готовят enriched; Item-формы передают его, Actor tab-profession использует raw editor. Отдельно от monster issue13. |
| [issue-00110](../../issues/potential/issue-00110.md) | Основание сохранено | B07: P02: одинаковое имя в editor выбирает skillPath1.skill1, Actor предпочитает definingSkill; проблема идентификации, не диапазона уровня. |
| [issue-00111](../../issues/potential/issue-00111.md) | Основание сохранено | B07: P02: data-action removeEffectDamageProperties отсутствует в actions; handler также использует event.currentTarget. |
| [issue-00112](../../issues/potential/issue-00112.md) | Основание сохранено | B07: PARTS/контекст редактора включают только три пути; definingSkill имеет ту же полную модель. |
| [issue-00113](../../issues/potential/issue-00113.md) | Основание сохранено | B07: P03: applySelf=false/applyOnTarget=false всё равно выбирает себя; флаг target имеет приоритет. |
| [issue-00114](../../issues/potential/issue-00114.md) | Основание сохранено | B07: P03: duration='1' даёт null match/TypeError; формула обрабатывается regexp+eval, не общим Roll-парсером. |
| [issue-00115](../../issues/potential/issue-00115.md) | Основание сохранено | B07: P03: пустой thresholds открывает пустой select, затем чтение выбранной value падает. |
| [issue-00116](../../issues/potential/issue-00116.md) | Основание сохранено | B07: Drop itemMixin ищет attr по ключу без проверки; unknown формирует system.skills.undefined.*; StringSet не ограничен картой. |
| [issue-00117](../../issues/potential/issue-00117.md) | Основание сохранено | B07: Исходник вручную интерполирует skillName в JSON value; кавычки не экранируются. Полная передача AE/ядровая очистка не повторялась. |
| [issue-00118](../../issues/potential/issue-00118.md) | Основание сохранено | B07: P03: stat='' приводит к TypeError до броска; HBS скрывает только точное none. |
| [issue-00119](../../issues/potential/issue-00119.md) | Основание сохранено | B07: Три ключа ru отсутствуют при en-наличии; это локализация с fallback, не доказанная поломка порогов. |
| [issue-00120](../../issues/potential/issue-00120.md) | Основание сохранено | B07: Шесть CRUD-методов вызывают update без return/await, в отличие от завершённой записи; причины отдельно от имени/action. |
| [issue-00121](../../issues/potential/issue-00121.md) | Основание сохранено | B07: P04: при followUp=null в create передаётся [null], parent.delete начинается при pending create; успех перехода не подтверждён. |
| [issue-00122](../../issues/potential/issue-00122.md) | Основание сохранено | B07: P04: treatment=none/healingTime0 запускает treat; deadly не переходит. Проверка срока расположена вне treated. |
| [issue-00123](../../issues/potential/issue-00123.md) | Основание сохранено | B07: Все ID/поиски глобальные, диалог modal=false; несколько окон не разделяют поля, как отдельный DOM-дефект. |
| [issue-00124](../../issues/potential/issue-00124.md) | Основание сохранено | B07: P05: true→false checkbox меняет сумму, но isResting/isSterilized остаются true. |
| [issue-00125](../../issues/potential/issue-00125.md) | Основание сохранено | B07: P05: фактический HP9→10, чат totalRec4; actualWoundList отсутствует, daysHealed фиксирован. |
| [issue-00126](../../issues/potential/issue-00126.md) | Основание сохранено | B07: P05: recoverActor передаёт найденного по совпадающему имени другого Actor; createHealMessage передаёт this.actor. Speaker/содержимое различены. |
| [issue-00127](../../issues/potential/issue-00127.md) | Основание сохранено | B07: P04 и source recoverActor: heal/treat/обёртки и ChatMessage.create не ждут записи; не объявлено успешным реальным отдыхом. |
| [issue-00128](../../issues/potential/issue-00128.md) | Основание сохраняется | B08: Смешанный перенос заменяет templateProperties; G01; numeric0 пропускается. |
| [issue-00129](../../issues/potential/issue-00129.md) | Основание сохраняется | B08: Ritual HBS пишет прежние корневые пути, потребитель читает вложенные. |
| [issue-00130](../../issues/potential/issue-00130.md) | Основание сохраняется | B08: G01: UUID остаётся в source, но теряется в fallback для DOM. |
| [issue-00131](../../issues/potential/issue-00131.md) | Основание сохраняется | B08: G02: редактируется первый дубль UUID, удаляются все. |
| [issue-00132](../../issues/potential/issue-00132.md) | Основание сохраняется | B08: G02: изменение prepared-массива и ранний возврат при pending update. |
| [issue-00133](../../issues/potential/issue-00133.md) | Основание сохраняется | B08: G01 и castSpell: отсутствует показ selfEffects; применение Object.values отдельно работает. |
| [issue-00134](../../issues/potential/issue-00134.md) | Основание сохраняется | B08: Неопределённый heal после запроса списания STA; выполнение полного cast повторяется позднее. |
| [issue-00135](../../issues/potential/issue-00135.md) | Основание сохраняется | B08: Чат интерполирует alternateRitualComponents как объекты, основной список перебирается. |
| [issue-00136](../../issues/potential/issue-00136.md) | Основание сохраняется | B08: Отсутствует editImage action именно у hex/ritual; общий listener не заменяет его. |
| [issue-00137](../../issues/potential/issue-00137.md) | Основание сохраняется | B08: Danger/Water отличаются регистром; emanation есть в en fallback, отсутствует в ru. |
| [issue-00138](../../issues/potential/issue-00138.md) | Основание сохраняется | B08: G03: Promise.all получает Promise обычного drawPreview. |
| [issue-00139](../../issues/potential/issue-00139.md) | Основание сохраняется | B08: G03: options не попадает в flagOptions; фактическая цепочка имен сопоставлена. |
| [issue-00140](../../issues/potential/issue-00140.md) | Основание сохраняется | B08: G03 и core: Scene-объект сравнивается с ID; оба токена проходят. |
| [issue-00141](../../issues/potential/issue-00141.md) | Основание сохраняется | B08: G03 проверяет вход range=1; формула radius в core повторно прочитана; полный core-перевод здесь не исполнялся. |
| [issue-00142](../../issues/potential/issue-00142.md) | Основание сохраняется | B08: G04: цепочка не ожидается; catch пуст; записи региона также не ожидаются. |
| [issue-00143](../../issues/potential/issue-00143.md) | Основание сохраняется | B08: G03: void createTokenEmanation приводит к TypeError; void разрешён core. |
| [issue-00144](../../issues/potential/issue-00144.md) | Основание сохраняется | B08: Оба места выбирают текущую сцену; таймер после смены canvas отдельно не запускался. |
| [issue-00145](../../issues/potential/issue-00145.md) | Основание сохраняется | B08: G04: нет combatant вызывает TypeError; остальные guards сверены по коду. |
| [issue-00146](../../issues/potential/issue-00146.md) | Основание сохраняется | B08: G04: undefined duration приводит к запросу удаления; flags и castSpell согласованы. |
| [issue-00147](../../issues/potential/issue-00147.md) | Основание сохраняется | B08: Подпись PreMove отличается от фактического события MoveWithin; не дубль миграции issue87. |
| [issue-00148](../../issues/potential/issue-00148.md) | Основание сохраняется | B09: Q02: cancel передан в rollSkill; close=null имеет тот же отсутствующий guard. |
| [issue-00149](../../issues/potential/issue-00149.md) | Основание сохраняется | B09: getInteractActor/chooseFromAvailableActors прочитаны: нет результата/отмена не обработаны. |
| [issue-00150](../../issues/potential/issue-00150.md) | Основание сохраняется | B09: Q01: неизвестные строки допустимы; lookup потребителя без guard. |
| [issue-00151](../../issues/potential/issue-00151.md) | Основание сохраняется | B09: Q02: rollSkill получает только имя, DC20 не передан. |
| [issue-00152](../../issues/potential/issue-00152.md) | Основание сохраняется | B09: Q02: pending rollSkill не ожидается; Hide/обёртка также без return. |
| [issue-00153](../../issues/potential/issue-00153.md) | Основание сохраняется | B09: Q01: false→true, true/checked→false даже у name. |
| [issue-00154](../../issues/potential/issue-00154.md) | Основание сохраняется | B09: Шаблон заголовка и partial дают 12/13 ячеек; прежний DOM-тест сопоставлен. |
| [issue-00155](../../issues/potential/issue-00155.md) | Основание сохраняется | B09: Три буквальные английские подписи подтверждены исходным HBS. |
| [issue-00156](../../issues/potential/issue-00156.md) | Основание сохраняется | B09: Q03: null resolver прерывает prepare; remove также не проверяет Item. |
| [issue-00157](../../issues/potential/issue-00157.md) | Основание сохраняется | B09: Q03: push до update, два независимых запроса; реальная атомарность БД не проверялась. |
| [issue-00158](../../issues/potential/issue-00158.md) | Основание сохраняется | B09: Q03: remove отсутствующего UUID сбрасывает isStored; членство глобально не проверяется. |
| [issue-00159](../../issues/potential/issue-00159.md) | Основание сохраняется | B09: Q03: self принимается; цикл из двух разрешён той же проверкой, рекурсивного обхода нет. |
| [issue-00160](../../issues/potential/issue-00160.md) | Основание сохраняется | B09: Q03: внешняя сумма3 игнорирует storedWeight30 вложенного, его calcWeight0. |
| [issue-00161](../../issues/potential/issue-00161.md) | Основание сохраняется | B09: Исходный UUID сохраняется и update вызывается у источника; серверные права не обходились. |
| [issue-00162](../../issues/potential/issue-00162.md) | Основание сохраняется | B09: Нет очистки в модели/документе; ссылки не являются embedded-владением контейнера. |
| [issue-00163](../../issues/potential/issue-00163.md) | Основание сохраняется | B09: carry отсутствует в Drop/calcWeight; Q03 допускает self даже при carry0. |
| [issue-00164](../../issues/potential/issue-00164.md) | Основание сохраняется | B10: J01:9/10+REC3 отправляет12, Full10; обе версии, правило рулбука не утверждается. |
| [issue-00165](../../issues/potential/issue-00165.md) | Основание сохраняется | B10: allApplicableEffects + дополнительная выборка допускают один объект дважды; условный фасад прежнего теста соответствует геттерам. |
| [issue-00166](../../issues/potential/issue-00166.md) | Основание сохраняется | B10: J02: prepared enhancementItems обрезается, source IDs не изменяются; не дубль Armor RangeError82. |
| [issue-00167](../../issues/potential/issue-00167.md) | Основание сохраняется | B10: J05: imported ES module перезаписывает global jQuery; реальная библиотека браузера не запускалась. |
| [issue-00168](../../issues/potential/issue-00168.md) | Основание сохраняется | B10: J03 + core617–621: три legacy callback имеют переставленные аргументы; delete callback корректен. |
| [issue-00169](../../issues/potential/issue-00169.md) | Основание сохраняется | B10: giftItem не ждёт addItem/emit перед remove; барьер входа168 отделён от тела. |
| [issue-00170](../../issues/potential/issue-00170.md) | Основание сохраняется | B10: Пустой chooser оставляет OK, который читает отсутствующее поле. |
| [issue-00171](../../issues/potential/issue-00171.md) | Основание сохраняется | B10: Три операции установки и предварительный push не объединены; не дубль166. |
| [issue-00172](../../issues/potential/issue-00172.md) | Основание сохраняется | B10: Monster меняет prepared equipped перед source toObject; фактическая цепочка Actor.addItem сопоставлена. |
| [issue-00173](../../issues/potential/issue-00173.md) | Основание сохраняется | B10: J04: HTML summary теряет subtype, создаётся общий component. |
| [issue-00174](../../issues/potential/issue-00174.md) | Основание сохраняется | B10: J03: quantity0 не мешает consume/remove; эффект расходования в тесте pending. |
| [issue-00175](../../issues/potential/issue-00175.md) | Основание сохраняется | B10: getSpeaker получает name; core instanceof Actor и прежние tests20 подтверждают fallback. |
| [issue-00176](../../issues/potential/issue-00176.md) | Основание сохраняется | B10: crafting-craft единственный selector и listener ремесла; продолжение проверяется в B13. |
| [issue-00177](../../issues/potential/issue-00177.md) | Основание сохраняется | B10: Monster не наследует Character с единственным item-repair listener. |
| [issue-00178](../../issues/potential/issue-00178.md) | Основание сохраняется | B10: Weapon.Availability и десять подтипов diagrams не имеют keys en; область локалей сохранена. |
| [issue-00179](../../issues/potential/issue-00179.md) | Основание сохраняется | B10: Literal Carry/Weight HBS не обращаются к localize. |
| [issue-00180](../../issues/potential/issue-00180.md) | Основание сохраняется | B10: Относится к preload старого шаблона; текущая ArmorData и новый inventory используют вложенные пути. |
| [issue-00181](../../issues/potential/issue-00181.md) | Основание сохраняется | B11: K02: unarmed9 отсутствует, ranged7 попадает8–9; остальные границы сопоставлены с en/ru. |
| [issue-00182](../../issues/potential/issue-00182.md) | Основание сохраняется | B11: K02: UUID передаётся без fromUuid; core getSpeaker контракт проверен ранее. |
| [issue-00183](../../issues/potential/issue-00183.md) | Основание сохраняется | B11: visible не фильтрует constructor; base/damage могут иметь fumble без apply-ветки. |
| [issue-00184](../../issues/potential/issue-00184.md) | Основание сохраняется | B11: K01: toMessage завершён, setFlag pending; не утверждается потеря данных на сервере. |
| [issue-00185](../../issues/potential/issue-00185.md) | Основание сохраняется | B11: helper возвращает отсутствующий activeGM; consumers вызывают query без guard. |
| [issue-00186](../../issues/potential/issue-00186.md) | Основание сохраняется | B11: ru key отсутствует, en fallback есть; нельзя утверждать полностью пустую подпись. |
| [issue-00187](../../issues/potential/issue-00187.md) | Основание сохраняется | B11: K03: data-skill содержит Item.name, нет ID, поля skill пусты. |
| [issue-00188](../../issues/potential/issue-00188.md) | Основание сохраняется | B11: Семь system.skills-групп исключают spd/luck, хотя подготовлены девять. |
| [issue-00189](../../issues/potential/issue-00189.md) | Основание сохраняется | B11: K03: modifiers не в схеме; старые handlers/id не соответствуют, кнопок нет. |
| [issue-00190](../../issues/potential/issue-00190.md) | Основание сохраняется | B11: K03: ранний return для неизвестного имени пропускает allSkills; Item.activeEffectModifiers не читается. |
| [issue-00191](../../issues/potential/issue-00191.md) | Основание сохраняется | B11: K04: модель принимает IP−3; levelUp не проверяет остаток до Log/update. |
| [issue-00192](../../issues/potential/issue-00192.md) | Основание сохраняется | B11: Monster использует общий editor/listener без magic/logs/IP; схема сверена в B03. |
| [issue-00193](../../issues/potential/issue-00193.md) | Основание сохраняется | B11: Два ru key отсутствуют; семь dotted Skill keys после expandObject существуют, отзыв прежнего вывода сохранён. |
| [issue-00194](../../issues/potential/issue-00194.md) | Основание сохраняется | B11: K04: input отправляет max как unmodifiedMax; прежний полный FormData roundtrip не повторялся. |
| [issue-00195](../../issues/potential/issue-00195.md) | Основание сохраняется | B11: Actor fixed derived и customStat ветви сопоставлены; не все derived игнорируют ввод. |
| [issue-00196](../../issues/potential/issue-00196.md) | Основание сохраняется | B11: K01: threshold−1 пропускает success/rollOver; смерть передаёт min(база,10)−счётчик. |
| [issue-00197](../../issues/potential/issue-00197.md) | Основание сохраняется | B11: addAdrenaline/plus/death+reset без await, соседние luck/adrenaline− ожидают update. |
| [issue-00198](../../issues/potential/issue-00198.md) | Основание сохраняется | B11: Обе span репутации читают value, разница использует max. |
| [issue-00199](../../issues/potential/issue-00199.md) | Основание сохраняется | B12: L01: Monster не добавляет totalStats; общий tab-stats читает его. |
| [issue-00200](../../issues/potential/issue-00200.md) | Дублирует issue-00029 | B12: D05: дубль29; тот же запрос 10-3, не сохранённый строковый баланс. |
| [issue-00201](../../issues/potential/issue-00201.md) | Основание сохраняется | B12: Оба callback читают associatedItem.name при нехватке; более ранний алхимический барьер37 сохранён. |
| [issue-00202](../../issues/potential/issue-00202.md) | Основание сохраняется | B12: L04: parse5 создаёт три anchors; видимые последствия в браузере не утверждаются. |
| [issue-00203](../../issues/potential/issue-00203.md) | Основание сохраняется | B12: HP/base и HP/max выбирают разные состояния; обе боковые панели сопоставлены. |
| [issue-00204](../../issues/potential/issue-00204.md) | Основание сохраняется | B12: L01: исходный addActiveEffects выдаёт +1[], настоящий Roll отвергает. |
| [issue-00205](../../issues/potential/issue-00205.md) | Основание сохраняется | B12: Четыре ru keys отсутствуют, en fallback есть; связь с обоими sidebar. |
| [issue-00206](../../issues/potential/issue-00206.md) | Основание сохраняется | B12: L02: реальная CONST[0] ActiveEffect, Folder.create payload; сервер Actor.create не запускался. |
| [issue-00207](../../issues/potential/issue-00207.md) | Основание сохраняется | B12: L02: export возвращается при pending checkIfItemHasRollTable, update также не ждёт. |
| [issue-00208](../../issues/potential/issue-00208.md) | Основание сохраняется | B12: L02: множитель−2 даёт quantity−4; dice-ветка при отрицательном не входит в цикл. |
| [issue-00209](../../issues/potential/issue-00209.md) | Основание сохраняется | B12: Текущие PARTS/config не редактируют category/threat/difficulty/bounty; старый HBS содержит поля. |
| [issue-00210](../../issues/potential/issue-00210.md) | Основание сохраняется | B12: Проверено существование путей:11 отсутствуют из12; анализ содержимого assets не выполнялся. |
| [issue-00211](../../issues/potential/issue-00211.md) | Основание сохраняется | B12: L03: массив меняется до двух pending-запросов; runtime source/БД не изменены. |
| [issue-00212](../../issues/potential/issue-00212.md) | Основание сохраняется | B12: L03: индекс−1 удаляет последнюю; остальные coercion splice подтверждены кодом. |
| [issue-00213](../../issues/potential/issue-00213.md) | Основание сохраняется | B12: L03: limit2 при одной записи создаёт [a][]; Character counter не ограничен моделью. |
| [issue-00214](../../issues/potential/issue-00214.md) | Основание сохраняется | B13: N01: add/remove/message не await; menu callback-барьер168 отдельно. |
| [issue-00215](../../issues/potential/issue-00215.md) | Основание сохраняется | B13: N01: canBeDismantled возвращает UUID, missing recipe→TypeError. |
| [issue-00216](../../issues/potential/issue-00216.md) | Основание сохраняется | B13: N01: null UUID-компонент теряет name, чат восстановить его не может. |
| [issue-00217](../../issues/potential/issue-00217.md) | Основание сохраняется | B13: N01: quantity0 не мешает добавлению материалов; removeItem запускается позже. |
| [issue-00218](../../issues/potential/issue-00218.md) | Основание сохраняется | B13: getList('mutagens') не совпадает с manifest mutagen; экспорт не фильтрует этот тип. |
| [issue-00219](../../issues/potential/issue-00219.md) | Основание сохраняется | B13: Прямой ActorSheetV2 не устанавливает totalCost, HBS читает. |
| [issue-00220](../../issues/potential/issue-00220.md) | Основание сохраняется | B13: N02: zero stock, qty3, цена−4 принимаются телом; реальные права не обходились. |
| [issue-00221](../../issues/potential/issue-00221.md) | Основание сохраняется | B13: N02: четыре pending операции после await диалога; состояние БД не проверялось. |
| [issue-00222](../../issues/potential/issue-00222.md) | Основание сохраняется | B13: После выбора отсутствующий buyer разыменовывается без guard. |
| [issue-00223](../../issues/potential/issue-00223.md) | Основание сохраняется | B13: Core _dragDrop селектор.draggable и _onDragStart dataset сверены; строка dragable/data-id. |
| [issue-00224](../../issues/potential/issue-00224.md) | Основание сохраняется | B13: HBS data-edit без data-action; собственного listener нет. |
| [issue-00225](../../issues/potential/issue-00225.md) | Основание сохраняется | B13: Общий professionDrop требует skills после удаления старой, LootData содержит только три поля. |
| [issue-00226](../../issues/potential/issue-00226.md) | Основание сохраняется | B13: D06: главный барьер cleanHTML до innerHTML; старый vm-тест явно не lifecycle браузера. |
| [issue-00227](../../issues/potential/issue-00227.md) | Основание сохраняется | B13: N03: amount−10 увеличивает source до110 и уменьшает target; нет проверок fee/finite. |
| [issue-00228](../../issues/potential/issue-00228.md) | Основание сохраняется | B13: Проверяется объект rates, не валидность keys/значений; unknown/zero дают NaN/Infinity. |
| [issue-00229](../../issues/potential/issue-00229.md) | Основание сохраняется | B13: N03: захваченные100 заменены500 во время диалога, запрос всё равно90. |
| [issue-00230](../../issues/potential/issue-00230.md) | Основание сохраняется | B13: Новый bind/addEventListener при каждом вызове; условие повторного DOM сохранено. |
| [issue-00231](../../issues/potential/issue-00231.md) | Основание сохраняется | B13: N03: await update/render есть, ChatMessage.create pending не удерживает метод. |
| [issue-00232](../../issues/potential/issue-00232.md) | Основание сохраняется | B13: N04: реальный producer не передаёт currency, HTML не содержит amount17. |
| [issue-00233](../../issues/potential/issue-00233.md) | Основание сохраняется | B13: N04: отсутствующий UUID→TypeError; getPlayerActors не проверяет model.logs. |
| [issue-00234](../../issues/potential/issue-00234.md) | Основание сохраняется | B13: amount keys отсутствуют en/ru, currency keys существуют; условный денежный HBS барьер232 отдельно. |
| [issue-00235](../../issues/potential/issue-00235.md) | Основание сохраняется | B13: type без проверки попадает в Log; undefined currency + amount→NaN, не сохранённый валидный баланс. |
| [issue-00236](../../issues/potential/issue-00236.md) | Основание сохраняется | B14: Обычный profession skillRoll передаёт this.actor, у Actor отсутствует; direct attack передаёт this. |
| [issue-00237](../../issues/potential/issue-00237.md) | Основание сохраняется | B14: T03: addActiveEffects(undefined), addAttackModifiers0; weapon skillReplacement обходит общий конструктор. |
| [issue-00238](../../issues/potential/issue-00238.md) | Основание сохраняется | B14: T03: extra−3 в формуле, Actor.update0; оружейная оплата отдельная. |
| [issue-00239](../../issues/potential/issue-00239.md) | Основание сохраняется | B14: T03: кнопка damage есть, attack.itemUuid нет; combat.onDamage требует разрешённый Item. |
| [issue-00240](../../issues/potential/issue-00240.md) | Основание сохраняется | B14: Строка 5+2 вставляется в JSON без Roll при отсутствии d; ошибка отделена от duration121. |
| [issue-00241](../../issues/potential/issue-00241.md) | Основание сохраняется | B14: Обёртки/threshold/weapon/toMessage/query не возвращают операции; B07/T03 не заявляют сетевой цикл. |
| [issue-00242](../../issues/potential/issue-00242.md) | Основание сохраняется | B14: Фильтр первого attackOption и пустой chooser; weaponAttack(undefined) возможен. |
| [issue-00243](../../issues/potential/issue-00243.md) | Основание сохраняется | B14: Payload ActiveEffect использует icon; настоящая схема img, перенос icon отсутствует в исследованном core. |
| [issue-00244](../../issues/potential/issue-00244.md) | Основание сохраняется | B14: У monster.addMeleeBonusfalse preview meleeBonus может быть ненулевой, формула его пропускает. |
| [issue-00245](../../issues/potential/issue-00245.md) | Основание сохраняется | B14: Стоимость NaN обходит обе проверки; отрицательный origStaCost сохраняется при плате1; исходный textinput. |
| [issue-00246](../../issues/potential/issue-00246.md) | Основание сохраняется | B14: T04:3×2d6+1→6d6+1,2.9×2→4,арифметическая строка→NaN. |
| [issue-00247](../../issues/potential/issue-00247.md) | Основание сохраняется | B14: Общая ссылка DamageProperties из B05; cast изменяет percentage напрямую в prepared. |
| [issue-00248](../../issues/potential/issue-00248.md) | Основание сохраняется | B14: Hex/Ritual onCastEffects нет; targets.size>0 вызывает Object.values(undefined) в отдельном async helper. |
| [issue-00249](../../issues/potential/issue-00249.md) | Основание сохраняется | B14: T02:1d6 лечит1; щит передаёт строку в NumberField, Roll не вызывается. |
| [issue-00250](../../issues/potential/issue-00250.md) | Основание сохраняется | B14: replace нецифр объединяет числа; NdM anywhere приводит к броску первого токена без единиц. |
| [issue-00251](../../issues/potential/issue-00251.md) | Основание сохраняется | B14: T04: STA update уже pending при heal failure; успешный Roll тоже не ждёт эффекты/область. |
| [issue-00252](../../issues/potential/issue-00252.md) | Основание сохраняется | B14: Ritual DC только выводится; new RollConfig({showResult:false}) оставляет threshold−1. |
| [issue-00253](../../issues/potential/issue-00253.md) | Основание сохраняется | B14: HBSдоextendedRoll, эффекты gated !fumble, heal/shield callback не читают Roll. |
| [issue-00254](../../issues/potential/issue-00254.md) | Основание сохраняется | B14: cast при armorEnc>0 добавляет весь ignoredEv, возможен положительный остаток. |
| [issue-00255](../../issues/potential/issue-00255.md) | Основание сохраняется | B14: T02: missing source вызывает TypeError после target.update; onShield name guard также отсутствует. |
| [issue-00256](../../issues/potential/issue-00256.md) | Основание сохраняется | B14: T02:−8 даёт HP−3, bad→NaN; это запросы, не доказанное сохранение. |
| [issue-00257](../../issues/potential/issue-00257.md) | Основание сохраняется | B14: T01: настоящий BaseChatMessage очищает duration attack/damage; onHit/onDamage читают позже. |
| [issue-00258](../../issues/potential/issue-00258.md) | Основание сохраняется | B14: T01: Defense.crit теряет modifier, location.critEffect сохраняется; producer/consumer найдены. |

## Выявленные расхождения и уточнения

| ID | Вид | Результат | Материалы |
| --- | --- | --- | --- |
| D01 | Уточнение доказанного влияния | Первоначальная формулировка о несписании магических IP не учитывала последующие проверки настоящего Log. M07 повторно показал два противоречивых запроса: magic6 и magic10. Основной вывод уточнён до противоречивых обновлений; окончательный серверный баланс неизвестен. Исторические сценарии/статус potential сохраняются. Уточнено в документации; код прежний | [docs/issues/potential/issue-00017.md](../../issues/potential/issue-00017.md), [docs/issues/README.md](../../issues/README.md) |
| D02 | Устаревшее указание будущего этапа | В описании Stats после .040 оставалось указание на будущий разбор расчёта Actor в .007/.009. Обе порции завершены. Ссылка уточнена как уже выполненный разбор; математические выводы сохранены. Уточнено в документации; код прежний | [docs/analytics/code-audit/files/module/data/actor/templates/common/stats/statsData.js.md](files/module/data/actor/templates/common/stats/statsData.js.md) |
| D03 | Неточная формулировка условия | В таблице isDisabled «отсутствие equipped» можно было прочесть как причину отключения. E01 и код показывают обратное: отсутствующее поле заменяется true, поэтому само по себе не отключает. Формулировка уточнена; подавление и категоризация различены. | [witcherActiveEffect.js](files/module/activeEffect/witcherActiveEffect.js.md) |
| D04 | Термин базы вместо подготовленного значения | Назначение statMixin называло сумму max суммой исходных максимумов. Код и K04 показывают чтение подготовленных max; описание исправлено, расчёт сохранён. | [statMixin.js](files/module/actor/sheets/mixins/statMixin.js.md) |
| D05 | Повторная регистрация одного дефекта | issue-00200 повторяет issue-00029: тот же ввод, producer, Log и отказ числовой схемы. Добавлены взаимные ссылки; предложена основная карточка29. Заголовок200 уточнён до невалидного запроса, без утверждения о сохранённом строковом балансе. Статусы сохранены. | [issue-00029](../../issues/potential/issue-00029.md), [issue-00200](../../issues/potential/issue-00200.md) |
| D06 | Основное объяснение не учитывало позднюю проверку | В issue226 перенесён в основной текст уже установленный в .036 первичный барьер cleanHTML до innerHTML. Исторический тест сырого content не объявляется полным lifecycle диалога. | [issue-00226](../../issues/potential/issue-00226.md) |

## Связи между issues и возможные дубли

При сопоставлении учитывались условие возникновения, место ошибки, путь данных и наблюдаемый результат. Дополнительно отобраны и сопоставлены 32 наиболее близкие пары по тексту общего описания среди карточек с общими файлами локализации. Это способ найти кандидатов, а не критерий дубля. Полный перечень исходных выводов находится в матрице 258 issues выше.

**Установлен один явный дубль: [issue-00200](../../issues/potential/issue-00200.md) повторяет [issue-00029](../../issues/potential/issue-00029.md).** В обоих случаях отрицательная строка из одного обработчика списания IP попадает в Log, образует нечисловое значение и не проходит числовую схему. В карточках добавлены взаимные ссылки. Предложение для обсуждения — сохранить issue-00029 основной; решение о закрытии дубля не принято, обе карточки остаются в potential.

Другие сопоставленные пересечения имеют разные условия, обработчики или стадии. Таблица ниже выделяет связи для дальнейшего исследования, а не назначает задачи и приоритеты.

| Связанные записи | Соотношение и граница |
| --- | --- |
| [00017](../../issues/potential/issue-00017.md), [00029](../../issues/potential/issue-00029.md), [00191](../../issues/potential/issue-00191.md), [00200](../../issues/potential/issue-00200.md) | Развитие и журналы IP: противоречивые обновления магических IP, невалидное ручное списание и отсутствие проверки достаточности обычных IP. Дублируются только 00029/00200. Серверный порядок конкурирующих записей отдельно не проверен. |
| [00030](../../issues/potential/issue-00030.md), [00192](../../issues/potential/issue-00192.md) | Одна граница модели Monster/Character, но два интерфейса: вкладка IP с отсутствующими полями и отдельный редактор навыков с действием повышения. Это связанные точки входа, а не повторное описание одного обработчика. |
| [00034](../../issues/potential/issue-00034.md), [00038](../../issues/potential/issue-00038.md), [00127](../../issues/potential/issue-00127.md), [00169](../../issues/potential/issue-00169.md), [00214](../../issues/potential/issue-00214.md), [00221](../../issues/potential/issue-00221.md), [00241](../../issues/potential/issue-00241.md), [00251](../../issues/potential/issue-00251.md) | Общий признак — вызывающий метод не ждёт завершения операции. Различаются расходование, изготовление, лечение, передача, разбор, покупка, профессия и магия. Исправление одного вызывающего метода не исправляет остальные; завершение Promise и согласованность нескольких записей — разные требования. |
| [00036](../../issues/potential/issue-00036.md), [00194](../../issues/potential/issue-00194.md), [00195](../../issues/potential/issue-00195.md) | Подготовка и редактирование характеристик: потеря изменения в фазах расчёта, сохранение подготовленного max как базы, перезапись производных. Нужно прослеживать исходное значение → подготовку → форму → сохранение. |
| [00044](../../issues/potential/issue-00044.md), [00257](../../issues/potential/issue-00257.md), [00258](../../issues/potential/issue-00258.md) | Разные потери данных: копирование эффекта, очистка duration моделью сообщения и очистка модификатора критического эффекта в Defense. Для процесса важны все границы схем, а не только объект до ChatMessage.create. |
| [00087](../../issues/potential/issue-00087.md), [00180](../../issues/potential/issue-00180.md) | Миграция сопротивлений и устаревший интерфейс брони используют близкие поля, но ошибки возникают при разных действиях. Старый шаблон не следует автоматически считать текущим зарегистрированным интерфейсом. |
| [00072](../../issues/potential/issue-00072.md), [00112](../../issues/potential/issue-00112.md) | Основной навык профессии: перебор доступных защит и доступность настройки в редакторе — отдельные ограничения. Отсутствие настройки в UI не доказывает отсутствия поля в модели. |
| [00095](../../issues/potential/issue-00095.md), [00105](../../issues/potential/issue-00105.md), [00216](../../issues/potential/issue-00216.md) | Недоступный UUID компонента: потеря имени в редакторе рецепта, исключение в подготовке ремонта, потеря имени в сообщении разбора. Одинаковое внешнее условие, разные потребители и результаты. |
| [00128](../../issues/potential/issue-00128.md), [00129](../../issues/potential/issue-00129.md) | Миграция параметров области и форма ритуала со старыми путями. Это переход данных и текущая запись формы; одна коррекция не покрывает обе стадии. |
| [00138](../../issues/potential/issue-00138.md), [00143](../../issues/potential/issue-00143.md), [00144](../../issues/potential/issue-00144.md), [00145](../../issues/potential/issue-00145.md) | Области: неверный аргумент Promise.all, отсутствие результата при отмене, выбор сцены, отсутствующие участники/Actor. Более ранний сбой может мешать дойти до следующего; изолированная проверка нижней ветви не означает прохождение всего процесса. |
| [00148](../../issues/potential/issue-00148.md), [00149](../../issues/potential/issue-00149.md), [00151](../../issues/potential/issue-00151.md), [00152](../../issues/potential/issue-00152.md) | Улика: отмена выбора навыка, выбор Actor, передача DC и ожидание результата. Это разные контракты одного действия. |
| [00168](../../issues/potential/issue-00168.md), [00169](../../issues/potential/issue-00169.md), [00214](../../issues/potential/issue-00214.md) | Неверные аргументы обработчиков меню могут блокировать штатный вход в передачу/разбор. Проверки самих методов показывают отдельные ошибки ниже этой границы. |
| [00174](../../issues/potential/issue-00174.md), [00217](../../issues/potential/issue-00217.md), [00220](../../issues/potential/issue-00220.md) | Нулевой запас и числовые ограничения: расходование, разбор и покупка имеют разные точки допуска и записи. Общая тема не делает их дублями. |
| [00232](../../issues/potential/issue-00232.md), [00234](../../issues/potential/issue-00234.md), [00235](../../issues/potential/issue-00235.md) | Награды: отсутствие данных для показа валюты, отсутствующие ключи локализации количества, неизвестный тип при записи. Первый дефект может скрывать визуальное проявление второго. |
| [00249](../../issues/potential/issue-00249.md), [00253](../../issues/potential/issue-00253.md), [00255](../../issues/potential/issue-00255.md), [00256](../../issues/potential/issue-00256.md) | Лечение/щит из чата: вычисление формулы, доступность кнопки после провала, отсутствующий источник, отрицательное/нечисловое значение. Условия независимы; запрос update не равнозначен успешной записи. |

Повторная сверка сохранила ранее исправленное основание [issue-00193](../../issues/potential/issue-00193.md): семь ключей Actor.Skill присутствуют после expandObject; остаются два пропуска русского перевода. Первоначальный, уже отозванный вывод из исторического журнала не восстановлен как актуальная проблема. Сам исторический журнал сохранён.

## Материалы для дальнейшей TASK-0004

[Задача](../../tasks/task-0004-cross-checks.md) остаётся draft. Этот протокол предоставляет входные данные для её последующей детализации:

| Материал | Как использовать |
| --- | --- |
| Матрица 310 файлов | Найти проверенную карточку, блок сопоставления и конкретную границу поведения. Сопоставлять с полным [реестром 621 файла](registry.md), где 311 ещё не разобраны. |
| Матрица 258 issues и таблица пересечений | Отделять основание наблюдения, ограничения доказательств, дубли и связанные стадии процесса. Число карточек не равно числу независимых дефектов. |
| Блоки B01–B14 | Воспроизводимые по указанным входам и методам контрольные примеры, использованные модели, подменённые границы и результаты. Выполнена 71 новая группа изолированных проверок; это не 71 сквозной сценарий в мире. |
| D01–D06 | Пять уточнений актуальных описаний и одна повторная регистрация дефекта. Уточнены три карточки файлов и четыре карточки issues; исправлений игрового кода нет. |
| Проверки связей | 352 прямых импорта и 198 буквальных HBS-связей с определениями/упоминаниями потребителей. Это основа для сверки графа, но не полный граф динамических вызовов. |

Для дальнейшей постановки задачи полезно отдельно рассмотреть регистрацию и доступность обработчика; прохождение данных через DataModel; порядок подготовки Actor и эффектов; сохранение формы; результат броска и его потребителей в чате; завершение асинхронных записей. Это направления сопоставления, а не утверждённые подзадачи или план исправлений.

Границы результата:

- Все 310 имеющихся карточек и все 258 issues охвачены таблицами и содержательными блоками. Полный пофайловый разбор оставшихся 311 исходников не выполнен.
- Проверены актуальные описания, методы, схемы, связи и основания наблюдений. Исторические записи прежних запусков не объявляются новыми проверками; все прежние тесты повторно не запускались.
- В 71 новой группе использовались исходные методы, настоящие модели/части Foundry и Handlebars, где это указано в блоке. Документы, интерфейс, запись, сокеты и другие границы местами подменены фасадами. Ошибки фасада исправлялись в изолированном процессе, не регистрировались как дефекты системы.
- Мир, браузерные сценарии, реальная БД и многопользовательская сеть не проверялись. Очерёдность запросов не доказывает итоговое состояние сервера; очистка схемы не доказывает всё поведение интерфейса.
- Статические импорты, буквальные пути и упоминания имён не покрывают все регистрации, динамические вызовы и внешние модули.
- Potential означает отсутствие пользовательского подтверждения проблемы. Результат анализа не меняет этот статус, не разрешает исправление и не закрывает найденный дубль.

## Итоговая проверка сохранности и документов

| Проверка | Результат |
| --- | --- |
| Полнота протокола | 310 уникальных строк файлов; 258 строк issues без пропусков ID; 14 завершённых блоков; шесть записей D01–D06 |
| Реестр и карточки | 621 исходник в реестре; ровно 310 имеют карточки и статус «Проверено»; оставшиеся 311 не засчитаны как разобранные |
| Статические связи | 352 прямых импорта с проверкой целей, exports и упоминаний потребителей; 198 буквальных HBS-связей; 693 выделенных определения упомянуты в карточках |
| Ссылки | 641 Markdown-документ в docs плюс корневые README/AGENTS; 15 544 локальные ссылки и якоря проверены, ошибок нет |
| Issues | 258 карточек с обязательными разделами; все в potential, open/closed пусты; номера и актуальные названия уточнённых карточек согласованы с реестром |
| Задачи | Статусы всех 45 задач/подзадач совпадают с HEAD; TASK-0004 остаётся draft |
| Исходники | Все 621 файл побайтно совпадают с HEAD и базовым срезом TASK-0001; совокупный SHA256 совпадает с зафиксированным выше |
| Ветка и коммит | rusbar-main и 411ab4004a2378a5f96ceeb19f003f834ff9d3d9 сохранены |
| Метаданные существующих файлов | Для всех 1318 ранее отслеживаемых файлов совпал хеш mode/uid/gid/inode; права, владельцы, группы и сами inode сохранены |
| История сверок | Новый блок добавлен после заголовка review-log; весь прежний текст сохранён побайтно, исходный SHA256 b018fd22602999c878da7ef3b187de068671bfa9fae20a8bd9a33b064b1095b2 |
| Состав изменений | Изменены 14 существующих Markdown-файлов только внутри docs; добавлен один новый протокол; других неотслеживаемых файлов нет |
| Формат | Проверены таблицы протокола и git diff --check; ошибок не обнаружено |

Совокупный хеш исходников вычислен из конкатенации отсортированных путей: UTF-8 путь, нулевой байт, содержимое файла. Хеш метаданных — SHA256 стандартной JSON-сериализации словаря отсортированных путей со значениями [st_mode, st_uid, st_gid, st_ino]. Это позволяет сопоставить именно текущие файлы с зафиксированным начальным состоянием; время чтения/изменения не входит в проверку метаданных доступа.

Сверка завершена в согласованных границах. Новых issues не зарегистрировано, статусы проблем и задач не изменены. Выводы предназначены для дальнейшей детализации TASK-0004 и не означают проверки всего поведения системы в Foundry.
