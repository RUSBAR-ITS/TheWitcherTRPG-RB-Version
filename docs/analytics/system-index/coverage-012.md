# Покрытие TASK-0006.012

2026-09-15; rusbar-main, f3fb4869c73e00011e3238e0609d3b651dc5b337. Основание — чтение неизменённых исходников и позднего аудита; прежние игровые исполнения не повторялись.

## Что добавлено

Общий каркас документов и листов связан с прежними расчётами/эффектами; модели и документы имеют разных владельцев. CommonActorData использует prepareBaseData, WitcherActor — prepareDerivedData. Лист V2 передаёт live system, V1 — копию toObject(false); оба контекста содержат живые Item. Общий лист Item редактирует записи свойств через data-target, а отдельная configuration управляет ActiveEffect.

Переиспользованы proc-000003/004 (расчёты), proc-000044 (Item-эффекты), proc-000048/049 (категории/улучшения), proc-000050–054 (навыки/рендер), proc-000091 (окно конфигурации). Их фрагменты не объявляются всем lifecycle. Схема v1 и CLI не меняются.

## Основные источники

| Источник | Включённые области / остаток |
| --- | --- |
| [module/actor/witcherActor.js](../../../module/actor/witcherActor.js) (src-000047) | Методы add/remove/useItem, полный бой/локации и прочие предметные цепочки .013–.022 остаются частичными. Основные определения и выбранные процессы указаны ниже и в sources.jsonl. |
| [module/data/actor/commonActorData.js](../../../module/data/actor/commonActorData.js) (src-000055) | Вложенные фабрики, потребители currency/notes/pannels и все экземплярные пути не раскрыты полностью; конструкторы полей остаются внешними. Основные определения и выбранные процессы указаны ниже и в sources.jsonl. |
| [module/data/actor/characterData.js](../../../module/data/actor/characterData.js) (src-000054) | Вложенные general/Log/skillTraining, их операции и остальные потребители остаются B10/B11; параметры/метаданные полей не выделены полностью. Основные определения и выбранные процессы указаны ниже и в sources.jsonl. |
| [module/data/actor/lootData.js](../../../module/data/actor/lootData.js) (src-000056) | Полные callers Loot-sheet/наград/контейнеров и унаследованные API остаются вне порции; конструкторы и метаданные полей не выделены полностью. Основные определения и выбранные процессы указаны ниже и в sources.jsonl. |
| [module/data/actor/monsterData.js](../../../module/data/actor/monsterData.js) (src-000057) | Полные потребители брони/регенерации/лора и прочие методы Monster-листа остаются предметным порциям; метаданные полей не раскрыты полностью. Основные определения и выбранные процессы указаны ниже и в sources.jsonl. |
| [module/data/item/commonItemData.js](../../../module/data/item/commonItemData.js) (src-000109) | Внутренние constructor/field metadata, все переопределения и входящие потребители общей модели не раскрыты полностью. Основные определения и выбранные процессы указаны ниже и в sources.jsonl. |
| [module/item/witcherItem.js](../../../module/item/witcherItem.js) (src-000192) | getItemAttack/use/craft/генератор и полные тела подключённых примесей остаются .013–.022/B09/B14–B20. Основные определения и выбранные процессы указаны ниже и в sources.jsonl. |
| [module/actor/sheets/WitcherActorSheet.js](../../../module/actor/sheets/WitcherActorSheet.js) (src-000027) | Игровые тела callbacks инвентаря/восстановления/биографии и часть динамических receiver остаются следующей очереди; UI в браузере не исполнялся. Основные определения и выбранные процессы указаны ниже и в sources.jsonl. |
| [module/item/sheets/WitcherItemSheet.js](../../../module/item/sheets/WitcherItemSheet.js) (src-000172) | Конкретные controls/потребители data-target и специализированные Drop handlers/формы остаются предметным порциям; ядро и запись — внешняя граница. Основные определения и выбранные процессы указаны ниже и в sources.jsonl. |

Смежные источники: регистрации .006, V1/Character/Monster/конфигурация, dataUtils, фабрики схем и объявления объектов примесей. Вход примеси не означает полный разбор её методов. Сохраняются partial; два complete словаря .011 не изменяются.

## Различия, важные для поиска

- Модель CommonItemData объявляет строковую quantity и числовой weight; calcWeight не читает isHidden. У LootData своя схема и calcCurrencyWeight, без наследования CommonActorData.
- SchemaField(factory()) и EmbeddedDataField(Class) — разные формы композиции. CommonActorData не вызывает рекурсивно prepareBaseData вложенных Stats/Reputation.
- Прямое присваивание prepared значения, mutation входного migration source, optional enrichment и Document.update представлены раздельно.
- Object.assign подключает 17 примесей Actor, 5 Item и примеси листа; поздний defenseMixin заменяет одноимённый addDefenseModifiers. Владельцы определений не переносятся в Actor.
- В V2 подготовка weapon-слотов пишет live Item.enhancementItems; V1 имеет отдельные реализации, в том числе другое поведение брони. Изменение source/БД этим не утверждается.
- ItemSheet._prepareContext вызывает system.enrichedText напрямую; документный wrapper — отдельный возможный вход. createEnrichedText ждёт HTML, затем получает schema field.
- Общая настройка form.submitOnChange идёт в ядро; _onChangeForm дополнительно запускает ручной editor свойства Item. Слово effect не означает embedded ActiveEffect.
- Drop содержит editable guard, raw data branch, fromDropData, четыре диспетчеризуемых типа и default null. Core ActiveEffect handler, отсутствующие общие handlers и специализированные Item overrides различаются.
- HP-эффекты, навыковые фрагменты и полные игровые callbacks остаются отдельными процессами. Пустая выдача при partial не доказывает отсутствия зависимости.

## Прежние доказательства и issues

Прочитаны относящиеся разделы карточек и R003-01/06/09/12, R006-01/02, R013-01–05. Для выбранных границ сопоставлены полные issues 00011/00024/00030/00031/00057/00058/00059/00063/00165/00166 с поздними уточнениями. Статусы не менялись. Воспроизведения относятся к датированному аудиту; здесь выполнена индексация текущего кода.

## Проверенные внешние контракты

Это чтение установленного ядра 14.367.0, а не новый запуск мира. Внешние методы имеют boundary.external/location=null; их реализации не добавляются к 615 source.

| Файл ядра | Прочитанный участок | SHA-256 |
| --- | --- | --- |
| /opt/foundryvtt/client/documents/abstract/client-document.mjs | 313–319: system/document preparation; 338–342: embedded documents | a007180e3cf8d465dffe43b11272f289b4cf77a9e301c7d431f48267dfad8e9e |
| /opt/foundryvtt/client/documents/actor.mjs | 428–475: initial/final вокруг локального override | e82580bf9cef39d934c972dee859a3b9ba7ab5f3ebdc7502319dfed1bc214bb3 |
| /opt/foundryvtt/common/abstract/data.mjs | 820–826: toObject(source=true/false) | 11bb7f848c707803607accfa9f6b946c7cbfe8b17781ff562b468bdc77b934e5 |
| /opt/foundryvtt/client/applications/api/document-sheet.mjs | 172–185: context; 431–434: form; 525–532: update/create | 7925d81900eeea0d5e79606e12ce43539ae00714f50d8452c7305fe81394aa01 |
| /opt/foundryvtt/client/applications/sheets/item-sheet.mjs | 127–139: core Drop hook; 151–174: ActiveEffect handler | 20a6427810422668d19dafcea1418d68b5faf4d9ef96b8196a2e1bc6b5e236cb |

## Новые процессы

<a id="proc-000098"></a>

### proc-000098 — CommonActorData: композиция схемы

Вызов defineSchema; локальная композиция полей и вложений, создание экземпляра/clean/prepare остаётся ядру.

schema. Ветви, ожидание и выходы хранятся в записи процесса.

<a id="proc-000099"></a>

### proc-000099 — CharacterData: композиция схемы

Вызов defineSchema; локальная композиция полей и вложений, создание экземпляра/clean/prepare остаётся ядру.

schema. Ветви, ожидание и выходы хранятся в записи процесса.

<a id="proc-000100"></a>

### proc-000100 — MonsterData: композиция схемы

Вызов defineSchema; локальная композиция полей и вложений, создание экземпляра/clean/prepare остаётся ядру.

schema. Ветви, ожидание и выходы хранятся в записи процесса.

<a id="proc-000101"></a>

### proc-000101 — LootData: композиция схемы

Вызов defineSchema; локальная композиция полей и вложений, создание экземпляра/clean/prepare остаётся ядру.

schema. Ветви, ожидание и выходы хранятся в записи процесса.

<a id="proc-000102"></a>

### proc-000102 — CommonItemData: композиция схемы

Вызов defineSchema; локальная композиция полей и вложений, создание экземпляра/clean/prepare остаётся ядру.

schema. Ветви, ожидание и выходы хранятся в записи процесса.

<a id="proc-000103"></a>

### proc-000103 — CommonItemData: вклад в вес

Вызов calcWeight; только вычисление, без update.

guard → multiply. Ветви, ожидание и выходы хранятся в записи процесса.

<a id="proc-000104"></a>

### proc-000104 — CommonActorData: вес монет

Вызов calcCurrencyWeight; семь Number с коэффициентом 0.001, округление Actor отдельно.

sum. Ветви, ожидание и выходы хранятся в записи процесса.

<a id="proc-000105"></a>

### proc-000105 — LootData: вес монет

Вызов calcCurrencyWeight; семь Number с коэффициентом 0.001, округление Actor отдельно.

sum. Ветви, ожидание и выходы хранятся в записи процесса.

<a id="proc-000106"></a>

### proc-000106 — CommonActorData: миграция source

Вызов migrateData(source); меняется входной объект, defaults/clean и сохранение документа вне локального тела.

vigor → calculated → adrenaline → super. Ветви, ожидание и выходы хранятся в записи процесса.

<a id="proc-000107"></a>

### proc-000107 — CommonActorData: migrateCalculatedStats

Прямой вызов helper миграции; изменения source и guard, без update.

migrate. Ветви, ожидание и выходы хранятся в записи процесса.

<a id="proc-000108"></a>

### proc-000108 — CommonActorData: migrateAdrenaline

Прямой вызов helper миграции; изменения source и guard, без update.

migrate. Ветви, ожидание и выходы хранятся в записи процесса.

<a id="proc-000109"></a>

### proc-000109 — WitcherItem: миграция типа

Вызов migrateData(source); преобразование старого class до core migration.

subtype → super. Ветви, ожидание и выходы хранятся в записи процесса.

<a id="proc-000110"></a>

### proc-000110 — WitcherItem: Hexes/Rituals

Вызов migrateSpells; два независимых if по source.system?.class.

hex → ritual. Ветви, ожидание и выходы хранятся в записи процесса.

<a id="proc-000111"></a>

### proc-000111 — createEnrichedText: текст и поле схемы

Вызов helper(system, field, fieldPath); отдельный результат, без записи в system.

html → result. Ветви, ожидание и выходы хранятся в записи процесса.

<a id="proc-000112"></a>

### proc-000112 — CharacterData: background

Вызов enrichedText; возвращает general.background, не преобразует lifeEvents.

background. Ветви, ожидание и выходы хранятся в записи процесса.

<a id="proc-000113"></a>

### proc-000113 — MonsterData: три блока lore

Вызов enrichedText; три последовательных await.

common → academic → lore. Ветви, ожидание и выходы хранятся в записи процесса.

<a id="proc-000114"></a>

### proc-000114 — WitcherItem: optional делегирование

Вызов document.enrichedText; модель Item определяет доступность метода.

optional. Ветви, ожидание и выходы хранятся в записи процесса.

<a id="proc-000115"></a>

### proc-000115 — Actor V2: общий контекст до возврата

Вход _prepareContext(options); локальный конвейер, внешняя база и тела смежных helpers имеют отдельные границы.

super → options → documents → temporary-hp → general → skills → weapons → armor → spells → items → effects → return. Ветви, ожидание и выходы хранятся в записи процесса.

<a id="proc-000116"></a>

### proc-000116 — Actor V1: копия system и живые Item

Прямой вызов getData; V1 не зарегистрирован, это локальный метод старого листа, не доказанный текущий UI.

super → settings → copy → hp → helpers → effects → return. Ветви, ожидание и выходы хранятся в записи процесса.

<a id="proc-000117"></a>

### proc-000117 — Actor V2: общие заметки

Вызов helper контекста; Item-note и массив notes модели различаются.

notes. Ветви, ожидание и выходы хранятся в записи процесса.

<a id="proc-000118"></a>

### proc-000118 — Actor V2: группы заклинаний

Вызов helper контекста; только группировка Item, без castSpell/расхода ресурсов.

list → levels → separate. Ветви, ожидание и выходы хранятся в записи процесса.

<a id="proc-000119"></a>

### proc-000119 — Actor V2: totals и описания травм

Вызов helper контекста; без операций добавления/лечения/удаления Item.

groups → totals → enrich → map. Ветви, ожидание и выходы хранятся в записи процесса.

<a id="proc-000120"></a>

### proc-000120 — Actor V2: prepared слоты оружия

Вызов _prepareWeapons; live Item-модель, source/update в методе не записывается.

select → guard → slots → next. Ветви, ожидание и выходы хранятся в записи процесса.

<a id="proc-000121"></a>

### proc-000121 — Actor V2: список брони

Вызов helper контекста; только фильтр, без подготовки SP/слотов.

filter. Ветви, ожидание и выходы хранятся в записи процесса.

<a id="proc-000122"></a>

### proc-000122 — Array.cost: цена списка Item

Вызов cost на массиве; определение выполнено модулем V2, V1 использует ту же функцию.

sum → ceil. Ветви, ожидание и выходы хранятся в записи процесса.

<a id="proc-000123"></a>

### proc-000123 — Item V2: контекст и конфигурация

Вход _prepareContext; Item может быть world или owned, actor не требуется этим телом.

super → fields → enrich → return. Ветви, ожидание и выходы хранятся в записи процесса.

<a id="proc-000124"></a>

### proc-000124 — Item V2: render и регистрация Drop

Вход _onRender; привязка DOM callbacks, не доказательство события или записи.

super → drag → listeners. Ветви, ожидание и выходы хранятся в записи процесса.

<a id="proc-000125"></a>

### proc-000125 — Item V2: изменение формы и свойство effect

Вход _onChangeForm; общий submit и ручная запись свойства — отдельные пути.

super → condition → edit. Ветви, ожидание и выходы хранятся в записи процесса.

<a id="proc-000126"></a>

### proc-000126 — Item V2: _onAddEffect

Вызов action/handler свойства Item; внутренний update не ожидается.

payload. Ветви, ожидание и выходы хранятся в записи процесса.

<a id="proc-000127"></a>

### proc-000127 — Item V2: _onEditEffect

Вызов action/handler свойства Item; внутренний update не ожидается.

input → checkbox → checked → write. Ветви, ожидание и выходы хранятся в записи процесса.

<a id="proc-000128"></a>

### proc-000128 — Item V2: _oRemoveEffect

Вызов action/handler свойства Item; внутренний update не ожидается.

payload. Ветви, ожидание и выходы хранятся в записи процесса.

<a id="proc-000129"></a>

### proc-000129 — Item V2: разрешение Drop-документа

Вход drop callback; собственный путь не вызывает dropItemSheetData.

editable → data → resolve → dispatch → raw. Ветви, ожидание и выходы хранятся в записи процесса.

<a id="proc-000130"></a>

### proc-000130 — Item V2: четыре типа Drop

Вход _onDropDocument; конкретные наследники могут менять доступность handlers.

type → ae → actor → item → folder → other. Ветви, ожидание и выходы хранятся в записи процесса.

<a id="proc-000131"></a>

### proc-000131 — Item V2: открыть отдельную конфигурацию

Вызов configureItem action; конфигурация создана для того же Item.

render. Ветви, ожидание и выходы хранятся в записи процесса.

<a id="proc-000132"></a>

### proc-000132 — Character: продолжение общего контекста

Вход дочернего _prepareContext; тела предметных helpers только как делегированные участки.

base → character → helpers → events → enrich → tabs. Ветви, ожидание и выходы хранятся в записи процесса.

<a id="proc-000133"></a>

### proc-000133 — Monster: продолжение общего контекста

Вход дочернего _prepareContext; персонажные general/logs не добавляются наследованием.

base → helpers → schema → enrich → return. Ветви, ожидание и выходы хранятся в записи процесса.

<a id="proc-000134"></a>

### proc-000134 — Item: контекст конфигурации

Вход _prepareContext конфигурации; отдельный класс того же Item, не основной ItemSheet.

base → fields → effects → return. Ветви, ожидание и выходы хранятся в записи процесса.

## Итоговые показатели

Добавлено 231 сущностей, 512 отношений, 37 процессов. Накоплено 3554 / 7907 / 134; определения в 179/615 источниках, роли 65/114/436. Все новые/расширенные исходники остаются partial.

## Проверки и пределы

Пройдены 95 тестов (unittest, 389.996 с), включая 24 новых CLI-случая; накоплено 221 CLI-пример. Это проверки справочника, без исполнения игровых сценариев.

~~~bash
python3 -B -m unittest discover -s docs/analytics/system-index/tests -v
python3 -B docs/analytics/system-index/query.py check --freshness --format json
git diff --check
~~~

Новый набор проверяет владельцев/декларации полей, String quantity и условный вес, наследование Loot, порядок миграций/Object.assign, прямой вызов enrichment модели, await и live/copy context, запись свойств Item и ветви Drop. Сверены оба направления всех отношений, адреса и достижимость новых процессов, участие сущностей и три аспекта coverage. Отдельно прочитаны пять внешних контрактов с хешами выше. Старые количественные итоги .010/.011 проверяются по их историческим частям; поведенческие проверки поиска используют накопленный граф. Формат v1 и query.py сохранены.

Первичные прогоны выявили неточные тестовые цитаты и неверное название типа связи в двух примерах (правильное — extends). Они сверены с исходниками и исправлены; описание работы движка по результату поиска не подменялось. При сверке отдельно добавлена запись в CharacterData.lifeEventCounter через live context.system, чтобы поиск писателей находил поле модели, и уточнён payload преобразования lifeEvents.

## Матрица справочных запросов

| Запрос | Примеры | Проверенный результат |
| --- | --- | --- |
| IQ-01 | DOC-01 | quantity принадлежит CommonItemData, тип StringField |
| IQ-02 | DOC-02/03 | calcWeight и canBeRepaired имеют разные определения и роли |
| IQ-03 | DOC-07/08 | Loot наследует TypeDataModel, Character — CommonActorData; регистрации сохраняют ID .006 |
| IQ-04 | DOC-04/14 | Вес читает четыре поля; лист Item вызывает enrichment модели напрямую |
| IQ-05 | DOC-06/09 | Читатели quantity и три обратные связи от Monster enrichment |
| IQ-06 | DOC-05/18 | Пустые writers внутри схемы не доказывают отсутствия записи; editor свойства вызывает Item.update |
| IQ-07 | DOC-10–13/16–17/19–22/24 | Порядок, guards, await, live/copy, ветви Drop и callback формы |
| IQ-08 | DOC-15/23 | Dynamic receiver, issue-00058 и границы неподтверждённого runtime |

[24 точных примера](examples/expansion-012-queries.json), [проверки](tests/test_expansion_012.py). Содержательное покрытие новых исходников остаётся partial; наличие процесса не обещает полный список входящих зависимостей.

## Следующая порция

TASK-0006.012 выполнена. [TASK-0006.013](../../tasks/task-0006.013.md) — инвентарь, количество и использование расходников — остаётся planned. Переход к реализации новых игровых правил не выполнялся.
