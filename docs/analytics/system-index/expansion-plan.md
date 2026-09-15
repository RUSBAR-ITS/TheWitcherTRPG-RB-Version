# Остаток справочника и предложение расширения

2026-09-14; rusbar-main, `0c09df13984e021c24073926150dfd7a336b6ac5`. [TASK-0006.005](../../tasks/task-0006.005.md), [приёмка пилота](pilot-acceptance.md).

**Первая очередь:** .006–.010 выполнены 2026-09-15, следующая .011; .011 planned. Остальные области и порядок остаются предложением. B01–B20 служат учёту остатка, а не являются двадцатью задачами. Исходные таблицы .005 ниже сохранены с явной исторической отметкой; текущее покрытие указано отдельно.

## Что осталось

Все 615 файлов уже описаны в [аудите](../code-audit/registry.md). После .010 в компактном индексе 151 файл с частичными определениями (58 основных, 93 смежных), 464 — только каталог определений. Внутри 151 файла остаются существенные области. Минимальная запись импортированного класса не означает полного разбора файла. [Точные границы .010](coverage-010.md) и sources.jsonl определяют включения и остаток.

[Точный перечень](expansion-inventory.json) содержит каждую пару source ID/путь ровно один раз. pilot_role и исходные boundaries сохраняют срез .005; current_index и current_role отражают .010; три аспекта покрытия хранятся в sources.jsonl. Приложение сопоставлено с реестром и sources.jsonl, в manifest не подключено и формат графа не меняет.

Типы файлов: 214 JS, 2 MJS, 132 HBS, 36 CSS и 231 JSON. В JSON входят 226 экспортов семи компедиумов, en/ru, system.json, package.json и build.json. Границы исходного реестра сохранены: docs, assets, .github, packs и остальные языки сюда не добавляются.

Основная область файла нужна для отсутствия двойного счёта. Например, config.js закреплён за B01, но его боевые карты рассматриваются вместе с B06, а эффекты — с B02. WitcherActor, commonActorData, helper и общие листы также участвуют в нескольких предметных порциях. Это не запрет повторного чтения и не доказательство зависимости: конкретные рёбра берутся из кода и аудита.

## Что изменилось в .010

Раскрыты формы характеристик/навыков и внешний submit, общая запись CONFIG.statLabels, ручные luck/adrenaline, старые операции Item/modifiers, настоящий producer видимости и CSS адресат. 28 новых процессов — proc-000064–000091; накоплено 1008/2671/91 и 193 границы. [Покрытие](coverage-010.md) отделяет max/unmodifiedMax, disabled/readonly, строковый input/Number и запрос update/его завершение. IP/logs остаются B11; сохранение в мире и computed style не исполнялись. Следующая .011 — локализации en/ru и сверка накопленного расширения.

## Что изменилось в .009

Добавлены producers навыкового контекста V2/V1, текущие Character/Monster PARTS и listeners, builtin/Item partial, старый Item-ID selector и форма навыка. 14 новых процессов — proc-000050–000063; прежние roll-процессы сохранены. Накоплено 935/2399/63 и 185 границ. [Покрытие](coverage-009.md) различает девять атрибутов Item и семь выводимых групп, hash и отсутствующий контекст, имя и ID, регистрацию и предзагрузку. На этом этапе следующей оставалась .010; её результат приведён выше. IP и остальная механика больших листов остаются за границами.

## Что изменилось в .008

Добавлены категории/CRUD Actor, отдельные actions Item, копирование обычного эффекта и улучшения, статусы/counter/иммунитет, query-получатели, Item-проход и временные HP. 17 новых процессов — proc-000033–000049; накоплено 879/2211/49 и 168 границ. [Покрытие](coverage-008.md) отделяет отбор, видимость, применение, запрос записи и внешнее истечение. На этом этапе следующей оставалась .009; её результат приведён выше. Полные бой/магия/урон/профессии не покрыты ближайшими связями этой порции.

## Что изменилось в .007

Добавлены редактор/мастер AE, десять методов поставщиков подсказок, autocomplete, системные formGroup, выбор @skill и фактические CSS-связи общего списка. Новые процессы proc-000024–000032 связаны с прежним proc-000007 через границу ядра; сохранение не заявляется локальным вызовом. [Покрытие](coverage-007.md). Категории, перенос, применение и статусы на этом этапе оставались следующей .008; её выполненный охват описан выше. Остальная механика Item/Actor и боевые процессы сохраняются в очереди.

## Что изменилось в .006

Добавлены все назначения моделей, регистрации листов, девять настроек, init/ready/updateCombat, условный hotbarDrop, подключения API и адреса callback. Для entry остаются тела macros/Polyglot; для настроек — прочие потребители; для config — остальное содержимое боевых карт/эффектов. Модели и листы имеют минимальные адреса классов/баз и PARTS/template, их тела остаются предметным порциям. B01 ещё не завершена: упаковка, миграции, внутренние handlers/helpers/query/socket не раскрыты.

Текущее распределение определений: 27 primary / 81 neighbor / 507 catalog_only. 95 внешних/динамических границ; прежние 62 сохранены, новые 33 перечислены в added_boundaries_006. Новые 72 файла с определениями не считаются полностью покрытыми. Полный пофайловый остаток хранится в coverage соответствующего source.

## Исходный остаток внутри 23 основных файлов (.005)

Эта и следующая таблицы фиксируют исходное предложение .005. Включённые с тех пор области см. выше и в coverage-006; прежние требования регистрации не означают, что .006 не выполнена.

| Файл | ID | Что предстоит дополнить или проверить |
| --- | --- | --- |
| [module/TheWitcherTRPG.js](../../../module/TheWitcherTRPG.js) | src-000004 | Остальные hooks init/ready/chat/macros/API; связи со settings, sheets, socket и миграциями. |
| [module/activeEffect/witcherActiveEffect.js](../../../module/activeEffect/witcherActiveEffect.js) | src-000008 | Диалог chooseSkill, @skill/_preCreate, методы длительности; связи с мастером и Item-проходом. Ядро остаётся внешним контрактом. |
| [module/actor/mixins/modifierMixin.js](../../../module/actor/mixins/modifierMixin.js) | src-000019 | Полные связи addAttackModifiers/addDefenseModifiers с боем; содержимое групп в CONFIG и их источники. |
| [module/actor/mixins/skillMixin.js](../../../module/actor/mixins/skillMixin.js) | src-000022 | levelUpSkill/IP/logs и другие callers; социальные ветви, UI Item-навыка и привязки labels. Основные roll-процессы уже есть. |
| [module/actor/sheets/mixins/skillMixin.js](../../../module/actor/sheets/mixins/skillMixin.js) | src-000045 | Контекст skillMap/Actor в разных листах; подключение HBS, сохранение панелей и действия профессии/повышения уровня. |
| [module/actor/witcherActor.js](../../../module/actor/witcherActor.js) | src-000047 | Остальные методы и подключения mixin; входы через sheets/API/chat; процессы fixed/derived/attack за границами proc-000004/000005. |
| [module/data/activeEffects/witcherActiveEffectData.js](../../../module/data/activeEffects/witcherActiveEffectData.js) | src-000052 | Потребители полей применения/длительности и пути submit; схема уже представлена. Служебный fields не требует искусственных узлов. |
| [module/data/actor/commonActorData.js](../../../module/data/actor/commonActorData.js) | src-000055 | Вложенные модели вне stats/skills, поля Actor и миграции; обращения источника/prepared через полный lifecycle. |
| [module/data/actor/templates/common/skills/bodyData.js](../../../module/data/actor/templates/common/skills/bodyData.js) | src-000080 | Использование конкретных навыков в UI/картах/профессиях и входы миграции. Общая схема уже внесена; произвольный source[skillName] остаётся динамическим. |
| [module/data/actor/templates/common/skills/craData.js](../../../module/data/actor/templates/common/skills/craData.js) | src-000081 | Использование конкретных навыков в UI/картах/профессиях и входы миграции. Общая схема уже внесена; произвольный source[skillName] остаётся динамическим. |
| [module/data/actor/templates/common/skills/dexData.js](../../../module/data/actor/templates/common/skills/dexData.js) | src-000082 | Использование конкретных навыков в UI/картах/профессиях и входы миграции. Общая схема уже внесена; произвольный source[skillName] остаётся динамическим. |
| [module/data/actor/templates/common/skills/empData.js](../../../module/data/actor/templates/common/skills/empData.js) | src-000083 | Использование конкретных навыков в UI/картах/профессиях и входы миграции. Общая схема уже внесена; произвольный source[skillName] остаётся динамическим. |
| [module/data/actor/templates/common/skills/intData.js](../../../module/data/actor/templates/common/skills/intData.js) | src-000084 | Использование конкретных навыков в UI/картах/профессиях и входы миграции. Общая схема уже внесена; произвольный source[skillName] остаётся динамическим. |
| [module/data/actor/templates/common/skills/refData.js](../../../module/data/actor/templates/common/skills/refData.js) | src-000085 | Использование конкретных навыков в UI/картах/профессиях и входы миграции. Общая схема уже внесена; произвольный source[skillName] остаётся динамическим. |
| [module/data/actor/templates/common/skills/skillData.js](../../../module/data/actor/templates/common/skills/skillData.js) | src-000086 | Писатели/редакторы и шаблоны встроенного Skill, Item-навык отдельно; getter уже раскрыт. |
| [module/data/actor/templates/common/skills/skillsData.js](../../../module/data/actor/templates/common/skills/skillsData.js) | src-000087 | Все потребители контейнеров, отображение групп и миграции; не выводить рекурсивный prepareBaseData из вложенности. |
| [module/data/actor/templates/common/skills/willData.js](../../../module/data/actor/templates/common/skills/willData.js) | src-000088 | Использование конкретных навыков в UI/картах/профессиях и входы миграции. Общая схема уже внесена; произвольный source[skillName] остаётся динамическим. |
| [module/data/actor/templates/common/stats/derivedStatsData.js](../../../module/data/actor/templates/common/stats/derivedStatsData.js) | src-000089 | Полный набор потребителей/изменений derived-полей, включая лечение, урон и ограничения; фабрика и контейнер уже внесены. |
| [module/data/actor/templates/common/stats/statData.js](../../../module/data/actor/templates/common/stats/statData.js) | src-000090 | Различение конкретных экземпляров общей фабрики по paths; остальные потребители/писатели value/max. Отдельный процесс простому литералу не обязателен. |
| [module/data/actor/templates/common/stats/statsData.js](../../../module/data/actor/templates/common/stats/statsData.js) | src-000091 | Связи применения и редакторов всех характеристик; миграция и роль prepareBaseData в реальном lifecycle. |
| [module/scripts/rolls/extendedRoll.js](../../../module/scripts/rolls/extendedRoll.js) | src-000202 | Прочие callers, fumble/chat/postprocessing и поля RollConfig; внутреннее устройство Roll не становится частью локального графа. |
| [module/setup/config.js](../../../module/setup/config.js) | src-000209 | Содержимое statusEffects/armorEffects, боевые/предметные карты, настройки и ключи локализации; пилот не покрывает всю конфигурацию. |
| [module/setup/registerDataModels.js](../../../module/setup/registerDataModels.js) | src-000214 | Все типы Item/ChatMessage и их registries; типы манифеста, наследование и подключение sheets. |

Не требуется превращать каждую локальную переменную или декларацию fields в сущность. Полнота определяется заявленной областью и полезными адресами определений/связей/процессов. Статус complete после расширения должен иметь проверенную границу, а не назначаться по совпадению числа файлов.

## Остаток внутри 13 смежных файлов

| Файл | ID | Неохваченная область |
| --- | --- | --- |
| [module/actor/mixins/armorMixin.js](../../../module/actor/mixins/armorMixin.js) | src-000010 | Остальные методы брони и consumers; getArmorEcumbrance остаётся связующим методом расчётов/бросков. |
| [module/actor/sheets/WitcherActorSheet.js](../../../module/actor/sheets/WitcherActorSheet.js) | src-000027 | Остальные context/actions/listeners/PARTS/updates и подмешанные реализации. |
| [module/actor/sheets/WitcherActorSheetV1.js](../../../module/actor/sheets/WitcherActorSheetV1.js) | src-000028 | Старый лист целиком по областям; проверять его регистрацию отдельно от действующего. |
| [module/actor/sheets/configurations/WitcherModifiersConfiguration.js](../../../module/actor/sheets/configurations/WitcherModifiersConfiguration.js) | src-000032 | Редактирование модификаторов и формирование контекста; сейчас выбран только участок skillListener. |
| [module/chatMessage/chatMessageData.js](../../../module/chatMessage/chatMessageData.js) | src-000050 | Полный состав ChatMessageData и consumers; подготовка speaker, типизация и отправка. |
| [module/data/activeEffects/witcherTemporaryItemImprovementData.js](../../../module/data/activeEffects/witcherTemporaryItemImprovementData.js) | src-000053 | Полный жизненный цикл временного улучшения Item, transfer и удаление/истечение. |
| [module/data/actor/characterData.js](../../../module/data/actor/characterData.js) | src-000054 | Остальная Character-схема, миграции, документы/листы/действия. |
| [module/data/actor/lootData.js](../../../module/data/actor/lootData.js) | src-000056 | Схема Loot, лист и операции содержимого. |
| [module/data/actor/monsterData.js](../../../module/data/actor/monsterData.js) | src-000057 | Остальная Monster-схема, миграции и специфический UI. |
| [module/data/investigation/mysteryActorData.js](../../../module/data/investigation/mysteryActorData.js) | src-000104 | Схема Mystery, лист, улики/препятствия и процессы расследования. |
| [module/data/item/skillItemData.js](../../../module/data/item/skillItemData.js) | src-000124 | Лист, UI и все читатели/писатели Item-навыка; числовая схема не делает его встроенным Skill. |
| [module/scripts/helper.js](../../../module/scripts/helper.js) | src-000198 | Остальные helpers и их callers; getCustomModifier/addPart уже имеют proc-000014. |
| [module/scripts/rollConfig.js](../../../module/scripts/rollConfig.js) | src-000201 | Потребители всех настроек RollConfig в бою/магии; не считать showSuccess реализованной проверкой. |

## Ранее заведённые границы

В [приложении](expansion-inventory.json) отдельно перечислены все 62 boundary ID: 36 динамических и 26 внешних, с исходным выражением и основной областью дальнейшего чтения. ID при разрешении цели нельзя молча переиспользовать под другое определение.

- Динамические миграционные source[skillName].label сопоставляются с формой входа; совпадение label не доказывает общего владельца.
- Поля payload changes/phase/applyAfterCalculations относятся к B02; конкретный change зависит от входного массива.
- Lookup Item, skillMapEntry, группы CONFIG, customStat/attackStats/reputation, поля Roll и контекст Sheet раскрываются вместе с соответствующими потребителями. Если адресат всё ещё зависит от исполнения, выражение остаётся явной границей.
- 26 внешних API — Foundry/окружение. Индекс реализации всего ядра не предлагается: достаточен проверенный контракт версии, входов, результата и ограничений.
- Единственная связь с catalog_only-файлом — renders к [wizard.hbs](../../../templates/dialog/activeEffects/wizard.hbs), src-000506. У него есть адрес входящей связи, но нет собственных определений/процессов. В расширении он становится полноценным участником B02; новый source ID не нужен.

Процессы явно представлены шагами в 10 файлах. Покрытие processes отмечено partial у 11 файлов и not_indexed у 604: statData.js сохраняет историческую partial-запись без собственного процесса. Это объяснимое ограничение учёта, а не одиннадцать полностью разобранных процессных файлов. Создавать искусственный процесс фабрики для выравнивания чисел не предлагается.

## Области полного реестра

Третий столбец — общий объём области, четвёртый — основные/смежные/только каталог. Полные имена каждого файла доступны в [приложении](expansion-inventory.json), без неявных glob-исключений.

| Область | Предмет | Файлов | Роли | Ожидаемые справочные ответы |
| --- | --- | ---: | ---: | --- |
| B01 | Запуск, реестры, hooks, настройки, миграции и упаковка | 19 | 3/0/16 | Кто регистрирует документ/тип/лист? Какие hooks, settings, query/socket и импорты запускают работу? Упаковка и сборка описываются без запуска. |
| B02 | Эффекты: редактор, применение, статусы и временные улучшения | 23 | 2/1/20 | Как строка мастера превращается в change? Кто переносит/подавляет/применяет/удаляет эффект? Какие flags/статусы и шаблоны участвуют? |
| B03 | Характеристики, навыки, модификаторы и общий бросок | 41 | 18/4/19 | Какие поля читает конкретный бросок/форма? Где проходят source/prepared/update? Все callers и существующие процессы расчётов. |
| B04 | Модели и листы Actor, заметки и инвентарь | 50 | 0/5/45 | Какие PARTS и listeners действуют у Character/Monster/Loot/V1? Где готовится контекст и запрашивается обновление Actor? |
| B05 | Основы Item, конфигурация и расходуемые предметы | 45 | 0/0/45 | Кто определяет поля Item, отображает формы, расходует/переносит/изменяет предмет? Какие связи ведут к Actor/effects? |
| B06 | Бой: атака, защита, урон, броня и сообщения | 66 | 0/2/64 | Вход атаки → защита → сообщение → урон/броня/локации; роли моделей и UUID, поздние действия чата, флаги провалов. |
| B07 | Критические травмы, лечение, восстановление и смерть | 13 | 0/0/13 | Получение травмы → стабилизация/лечение/заживление и связанные обновления/сообщения. Текущая механика, без проектирования новой. |
| B08 | Магия, заклинания и регионы | 25 | 0/0/25 | Кто выбирает spell/hex/ritual, строит атаку и регион? Источники стоимости/площади/сопротивления и границы Foundry. |
| B09 | Ремесло, алхимия, рецепты, разборка и ремонт | 30 | 0/0/30 | Какие ссылки связывают рецепт и компоненты? Потребление/разборка/ремонт: вход, расчёт, update и сообщение. |
| B10 | Раса, профессия, происхождение и биография | 34 | 0/0/34 | Раса/профессия/биография: поля, умения/пути, формы и таблицы; объявленное влияние отдельно от реально читаемого. |
| B11 | Валюта, награды, IP и журналы | 18 | 0/0/18 | Выдача/расход валюты и IP, конвертация и журналы; роли Actor/Sheet/API и границы сохранения. |
| B12 | Расследование и словесный бой | 19 | 0/1/18 | Улика/препятствие/сложность и социальный бой — две самостоятельные цепочки с общими бросками, без их смешения. |
| B13 | Локализации en/ru и общие средства отображения | 6 | 0/0/6 | Ключ en/ru → место использования, fallback/отсутствие; общие CSS/import/selector и htmlUtils без семантических догадок. |
| B14 | Экспорт компедиума character-generator | 13 | 0/0/13 | RollTable/Folder/results → прямые ссылки, UUID/followUp и consumers генератора/боя; различать хранение и разрешение. |
| B15 | Экспорт компедиума character-generator-sub-tables | 35 | 0/0/35 | RollTable/Folder/results → прямые ссылки, UUID/followUp и consumers генератора/боя; различать хранение и разрешение. |
| B16 | Экспорт компедиума lifepath | 21 | 0/0/21 | RollTable/Folder/results → прямые ссылки, UUID/followUp и consumers генератора/боя; различать хранение и разрешение. |
| B17 | Экспорт компедиума witcher-lifepath | 41 | 0/0/41 | RollTable/Folder/results → прямые ссылки, UUID/followUp и consumers генератора/боя; различать хранение и разрешение. |
| B18 | Экспорт компедиума style | 7 | 0/0/7 | RollTable/Folder/results → прямые ссылки, UUID/followUp и consumers генератора/боя; различать хранение и разрешение. |
| B19 | Экспорт компедиума combat | 11 | 0/0/11 | RollTable/Folder/results → прямые ссылки, UUID/followUp и consumers генератора/боя; различать хранение и разрешение. |
| B20 | Экспорт компедиума criticalWounds | 98 | 0/0/98 | Item/Folder/ActiveEffect/changes → потребители травм, UUID и ограничения применения; возможны порции по тяжести. |

B04 (50 файлов), B05 (45), B06 (66) и B20 (98) не следует брать целиком за один проход. Для B06 естественны порции: объявления атаки/защиты; построение и отправка сообщений; применение урона/брони; критические исходы и поздние действия чата. Для B04 — модели, context/PARTS, listener/update и инвентарь. Для B05 — общая модель/документ, конфигурация, расходование и конкретные формы. Синтаксически однотипные JSON допускают более крупные порции, но 98 экспортов травм лучше разделять по типу записи/тяжести.

## Первые порции расширения

Порции 1–6 оформлены как задачи .006–.011. Размер относится к основным адресам; уже индексированные модели/методы используются как смежные источники без дублирования ID.

| Порция | Задача | Основных файлов | Состояние |
| --- | --- | ---: | --- |
| 1 | [TASK-0006.006 — Подключение документов и интерфейсов](../../tasks/task-0006.006.md) | 7 | done |
| 2 | [TASK-0006.007 — Редактор ActiveEffect и мастер изменений](../../tasks/task-0006.007.md) | 6 | done |
| 3 | [TASK-0006.008 — Категории, перенос и статусы эффектов](../../tasks/task-0006.008.md) | 8 | done |
| 4 | [TASK-0006.009 — Текущие и старые входы навыка](../../tasks/task-0006.009.md) | 9 | done |
| 5 | [TASK-0006.010 — Редактирование характеристик и навыков](../../tasks/task-0006.010.md) | 8 | done |
| 6 | [TASK-0006.011 — Локализации en/ru и их потребители](../../tasks/task-0006.011.md) | 2 | planned |

Детальные границы, смежные адреса, результаты и проверки находятся в соответствующих задачах. Новые подзадачи за пределами этих шести ещё не созданы.

1. **Подключение документов и интерфейсов — 7 файлов.** system.json; module/TheWitcherTRPG.js; module/setup/registerDataModels.js, registerSheets.js, hooks.js, settings.js, config.js. Выбранная область: registries, типы, init/ready, подключение sheets и используемые настройки. Остальной config и все hooks не объявляются законченными. Ответы: IQ-02/03/05/08 по ключу типа и классу; пределы версии Foundry.
2. **Редактор ActiveEffect и мастер — 6 файлов.** module/activeEffect/WitcherActiveEffectSheet.js; module/activeEffect/mixins/baseMixin.js, temporaryItemImprovementMixin.js; templates/dialog/activeEffects/wizard.hbs; templates/sheets/activeEffect/system-specific.hbs; styles/activeEffect.css. Смежные _preCreate/_preUpdate и модели уже существуют. Ответы: выбранный путь поля → строка changes → частичный update → phase, с issue-00043/поздним уточнением.
3. **Категории, перенос и статусы эффектов — 8 файлов.** module/actor/sheets/mixins/activeEffectMixin.js; module/actor/mixins/temporaryEffectMixin.js; module/scripts/statusEffects/applyStatusEffect.js; module/scripts/temporaryEffects/applyActiveEffect.js; module/data/actor/templates/common/temporaryEffectsData.js; module/item/witcherItem.js (область подготовки/эффектов); templates/partials/effect-part.hbs; templates/sheets/actor/partials/character/tab-effects.hbs. Ответы: transfer/isTransferred, собственный/предметный эффект, категории против suppression, запрос удаления/применения. Ядро — внешняя граница.
4. **Текущие и старые входы навыка — 9 файлов.** module/actor/sheets/WitcherActorSheet.js, WitcherActorSheetV1.js, WitcherCharacterSheet.js, WitcherMonsterSheet.js; module/item/sheets/WitcherSkillItemSheet.js; templates/partials/character/skill-display.hbs, custom-skill-display.hbs, tab-skills.hbs; templates/sheets/item/skill-item-sheet.hbs. Область sheets — PARTS/context/listener навыков, а не весь класс. Ответы: HBS → dataset → callback → встроенный/Item-навык, связь с R004-06/07.
5. **Редактирование характеристик и навыков — 8 файлов.** module/actor/sheets/configurations/WitcherModifiersConfiguration.js; module/actor/sheets/mixins/statMixin.js, customSkillMixin.js; templates/sheets/actor/configuration/app/edit-skills.hbs, edit-stats.hbs, partials/stats-block.hbs; templates/sheets/actor/configuration/partials/skillConfiguration.hbs; styles/configurations/modifier-configuration.css. Ответы: кто пишет поле, prepared против update, UI-настройка против изменения схемы. Повышение уровня/IP раскрывается позднее с B11.
6. **Локализации — 2 файла.** lang/en.json и lang/ru.json. Подключение языка и потребители из предыдущих порций используются как смежные. Ответы: точный ключ/подпись → места употребления; существующий fallback/отсутствие; UI aliases не подменяют реальные локализованные ключи.

После них предлагается расширять предметные цепочки B04–B12, затем технические связи семи экспортов B14–B20. B13 общих CSS/helpers дополняется вместе с затронутыми интерфейсами. Очередность между предметными блоками определяется при согласовании; приоритет травм, боя или предметов здесь не принят за пользователя.

Для каждой будущей порции нужны адреса определений/обращений из существующих карточек и кода, явные динамические/внешние границы, короткие процессы с ветвями и независимые IQ-примеры. Шаблоны связываются с реальными callers/PARTS/context, локализации — с ключами и потребителями, экспорты — с UUID и фактическим разрешением ссылок. Новая интерпретация игровых правил не входит в наполнение.

## Проверка предложения

Историческая проверка .005: перечень 615/615, роли 23/13/579 и 62 границы соответствовали пилоту. После .010 те же 615/615 путей, роли 58/93/464 и 193 границы; раздельные сведения в inventory. .006–.010 выполнены, .011 ожидает исполнения; остальные области требуют дальнейшей постановки. TASK-0006 остаётся in-progress.
