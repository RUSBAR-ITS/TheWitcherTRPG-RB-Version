# system.json

| Поле | Значение |
| --- | --- |
| Исходный файл | [system.json](../../../../system.json) |
| Тип файла | JSON |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `3252300787c348e11f95098c345a6af7704b690c`; исходник совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f` |
| Изменения относительно коммита | Нет |
| Задача и порция | [TASK-0002](../../../tasks/task-0002-system-initialization.md); порция 1 |
| Запись перекрёстной сверки | [Журнал сверок](../review-log.md) — TASK-0002, порция 1 |

## Назначение файла

Манифест пакета системы: объявляет его идентичность, подключаемые ресурсы, компедиумы, локализации и подтипы документов. Сам файл не выполняет JavaScript и не регистрирует классы моделей.

## Условия использования

Читается загрузчиком пакетов Foundry. `esmodules` указывает единственную точку входа; `scripts` пуст. Объявления подтипов затем сопоставляются с регистрацией моделей и листов в `init`. Исследована версия манифеста в checkout; создание релизного архива и фактическая загрузка пакета не проверялись.

## Введённые сущности и действия с ними

| Поля и строки | Содержание и действие |
| --- | --- |
| `id`, `title`, `description`, `authors` — 2–19 | Идентификатор `TheWitcherTRPG`, название, описание и два автора. ID используется также строками пространства имён в коде. |
| `compatibility`, `version` — 5–10 | Минимум, проверенное и максимальное поколение — 14; версия содержит заготовку выпуска. Это декларация совместимости, а не результат проверки. |
| `scripts`, `esmodules`, `styles` — 21–23 | Нет обычных scripts; один ES-модуль и один главный CSS. |
| `packFolders`, `packs` — 24–88 | Иерархия папок и семь объявлений: Combat, criticalWounds, Character-gen, Character-gen_Sub-tables, Witcher_Lifepath_and_BG_Sub-tables, Life_Event_Sub-tables, Style_and_Values_Sub-tables. Типы — RollTable, кроме criticalWounds (Item). Папка связывает packs по их `name`, а не по имени каталога. |
| `languages` — 89–130 | Восемь языков: en, es, pt-BR, fr, de, it, ru, pl; код pt-BR связан с файлом ptbr.json. |
| `relationships` — 131–140 | Обязательных модулей нет; statuscounter рекомендован. Polyglot здесь не объявлен, хотя точка входа слушает его событие. |
| `socket`, `initiative`, `grid` — 141–146 | Разрешён системный сокет; инициатива 1d10; размер клетки 2 m. |
| `primaryTokenAttribute`, `secondaryTokenAttribute` — 147–148 | Пути resources.health и resources.power для интерфейса токена. |
| `url`, `manifest`, `download` — 149–151 | Заготовки URL выпуска; строка manifest заканчивается ACTIONn. Потребитель подстановки установлен в TASK-0003.050 по release.yml как справочному источнику; фактический выпуск не запускался. |
| `documentTypes` — 152–194 | Actor: character, monster, loot. Item: 18 типов от alchemical до weapon. ChatMessage: attack, defense, damage. ActiveEffect: temporaryItemImprovement. `htmlFields` заданы у monster, criticalWound, profession и race; это декларации полей, не содержимое их моделей. |

| Документ | Объявленные типы | htmlFields |
| --- | --- | --- |
| Actor | `character`, `monster`, `loot` | `monster`: `common`, `academicKnowledge`, `monsterLore` |
| Item | `alchemical`, `armor`, `component`, `container`, `criticalWound`, `diagrams`, `enhancement`, `hex`, `homeland`, `mount`, `mutagen`, `note`, `profession`, `race`, `ritual`, `spell`, `valuable`, `weapon` | `criticalWound`: `description`; `profession`: `notes`, `definingSkill.definition`, `*.*.definition`; `race`: `description`, `*.description` |
| ChatMessage | `attack`, `defense`, `damage` | Нет |
| ActiveEffect | `temporaryItemImprovement` | Нет |

## Основные функции и методы

Функций и методов нет. Значимые операции над этими данными выполняют Foundry и код регистрации.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| Точка входа | [module/TheWitcherTRPG.js](../../../../module/TheWitcherTRPG.js) | ES-модуль | Поле esmodules, строка 22 | Путь существует; модуль полностью разобран в этой порции |
| Главные стили | [styles/witcher-styles.css](../../../../styles/witcher-styles.css) | Ресурс CSS | Поле styles, строка 23 | Путь существует; все 36 CSS полностью разобраны к TASK-0003.050, см. уточнение ниже |
| en | [lang/en.json](../../../../lang/en.json) | Локализация | languages, строки 89–130 | Путь существует; полный разбор выполнен в TASK-0003.051; уточнение ниже |
| es | [lang/es.json](../../../../lang/es.json) | Локализация | languages, строки 89–130 | Путь существует; вне текущих границ пофайлового анализа по решению пользователя 2026-09-12 |
| ptbr | [lang/ptbr.json](../../../../lang/ptbr.json) | Локализация | languages, строки 89–130 | Путь существует; вне текущих границ пофайлового анализа по решению пользователя 2026-09-12 |
| fr | [lang/fr.json](../../../../lang/fr.json) | Локализация | languages, строки 89–130 | Путь существует; вне текущих границ пофайлового анализа по решению пользователя 2026-09-12 |
| de | [lang/de.json](../../../../lang/de.json) | Локализация | languages, строки 89–130 | Путь существует; вне текущих границ пофайлового анализа по решению пользователя 2026-09-12 |
| it | [lang/it.json](../../../../lang/it.json) | Локализация | languages, строки 89–130 | Путь существует; вне текущих границ пофайлового анализа по решению пользователя 2026-09-12 |
| ru | [lang/ru.json](../../../../lang/ru.json) | Локализация | languages, строки 89–130 | Путь существует; полный разбор выполнен в TASK-0003.051; уточнение ниже |
| pl | [lang/pl.json](../../../../lang/pl.json) | Локализация | languages, строки 89–130 | Путь существует; вне текущих границ пофайлового анализа по решению пользователя 2026-09-12 |
| Данные семи компедиумов | `packs/combat.db`, `packs/criticalWounds.db`, `packs/character-generator.db`, `packs/character-generator-sub-tables.db`, `packs/witcher-lifepath.db`, `packs/lifepath.db`, `packs/style.db` | Объявленные пути | packs, строки 44–88 | Буквальные пути с .db не существуют; в TASK-0003.050 проверено удаление суффикса ядром, нормализованные пути совпадают с выходами CLI |
| Загрузка и типизация пакета | Foundry 14.367.0; `/opt/foundryvtt/common/packages/base-system.mjs` | Внешний API | Схема BaseSystem содержит documentTypes | Версия прочитана из package.json установленного ядра; запуск мира не проверен |

## Известные потребители

| Файл-потребитель | Используемая сущность | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/setup/registerDataModels.js](../../../../module/setup/registerDataModels.js) | Типы документов | Регистрирует классы по ключам подтипов | Сопоставлены ключи с documentTypes; есть дополнительные mystery/clue/obstacle/skill; сверка завершена в порции 3 (issue-00005) |
| [module/setup/registerSheets.js](../../../../module/setup/registerSheets.js) | Подтипы | Регистрирует листы для подтипов | Встречаются те же дополнительные пользовательские типы |
| [build.json](../../../../build.json) | Путь system.json | Включает манифест в сборку | Поле includes; сборка не запускалась |
| [module/setup/settings.js](../../../../module/setup/settings.js) | TheWitcherTRPG.criticalWounds | Значение настройки по умолчанию образовано из ID и имени pack | Строки 2–14 |
| Foundry | Объявления пакета | Читает манифест | Внешний потребитель; не файл системы |

## Данные и изменения состояния

Хранит декларации. Сам по себе не изменяет документы мира, не создаёт ActiveEffect и не выполняет миграции. Серверная обработка пакетов и смысл htmlFields зависят от Foundry; наличие значений здесь не доказывает успешность их применения.

## Проверки и доказательства

Прочитаны все 195 строк, JSON разобран стандартным парсером. Проверены существование ES-модуля, CSS и восьми локализаций, а также отсутствие семи буквальных путей packs. Имена из packFolders сопоставлены с packs. Источники классов регистрации сверены в порции 3; ссылки на отсутствующие пути намеренно представлены текстом.

## Непроверенные участки и открытые вопросы

Файл прочитан полностью. Выпуск, загрузка мира и модулей не проверены. Потребитель подстановки заготовок и нормализация pack-путей установлены в TASK-0003.050 ниже; исполнение CI/серверной загрузки не проверялось. Для дополнительных типов выполнена сверка с локальными Document.TYPES, DocumentTypeField и DocumentSheetConfig ядра; создание этих типов в мире не воспроизводилось. Отсутствие собранных баз в checkout не приравнивается к дефекту кода.

## Связанные проблемы

[issue-00001](../../../issues/potential/issue-00001.md) — ранее зарегистрированное различие имени каталога и ID. [issue-00002](../../../issues/potential/issue-00002.md) — обработчик ready не переносит отсутствие выбранного компедиума; это отдельная проблема точки входа.

[issue-00005](../../../issues/potential/issue-00005.md) — четыре типа регистрируются в коде, но отсутствуют в documentTypes.

## История актуализации

2026-09-10 — первичный разбор полного файла на указанном коммите; сверка порции 1 отражена в журнале. Файлы зависимостей проверены в пределах определений и обращений, без объявления их полного разбора.

## Уточнение TASK-0003.006

2026-09-10, `fe7ea7420cd4dfa6ee51baf7520f7b0ad8f8b13d`. Три типа Actor character/monster/loot присутствуют в documentTypes и registerDataModels. У monster три htmlFields совпали с тремя HTMLField и путями enrichedText. Отсутствие mystery в манифесте относится к ранее зарегистрированной issue-00005; модель mystery не включена в текущую четвёрку.

Карточки сборки: [characterData](module/data/actor/characterData.js.md), [monsterData](module/data/actor/monsterData.js.md), [lootData](module/data/actor/lootData.js.md). [Сверка TASK-0003.006](../review-log.md#task-0003006).

## Уточнение TASK-0003.018

2026-09-10, `rusbar-main`, `29319a7a7e1dfc0663edbc15166f3b6a19682a2f`. Типы Item.race и Item.homeland объявлены и совпадают с ключами регистрации моделей и листов. Для race указаны htmlFields description и *.description; фактическая [RaceData](../../../../module/data/item/raceData.js) содержит HTMLField общего описания и четыре HTMLField описаний особенностей. [HomelandData](../../../../module/data/item/homelandData.js) задаёт два строковых поля. Эти два типа не расширяют перечень отсутствующих деклараций в [issue-00005](../../../issues/potential/issue-00005.md).

[Перекрёстная сверка](../review-log.md#task-0003018). Исходники не изменены; это уточнение проверенных связей, а не повторный полный разбор файла.

## Уточнение TASK-0003.019

2026-09-10, `rusbar-main`, `c26eb64dd54cc434087f54c3c6b678b6092b15a2`. Item.profession объявлен с htmlFields notes, definingSkill.definition, *.*.definition. [ProfessionData](../../../../module/data/item/professionData.js) соответствует этим 11 HTML-полям; общее description наследуется StringField. Модель и лист зарегистрированы под тем же типом.

[Перекрёстная сверка](../review-log.md#task-0003019). Исходники не изменены; уточнение касается проверенных связей, не повторного полного разбора файла.

## Уточнение TASK-0003.020

2026-09-11, `rusbar-main`, `b09f992960a76d1c75946f402e42d93fa0785008`; проверены связи с критическими травмами, лечением и отдыхом. Полный первоначальный разбор и его ограничения сохранены.

| Связь | Файл | Результат проверки |
| --- | --- | --- |
| criticalWound / htmlFields | [module/data/item/criticalWoundData.js](../../../../module/data/item/criticalWoundData.js) | Декларация documentTypes.Item.criticalWound сопоставлена с девятью полями модели; description — HTMLField. criticalWound наследует TypeDataModel напрямую, не общую Item-модель. |
| criticalWounds | [module/setup/settings.js](../../../../module/setup/settings.js) | Pack объявлен в манифесте; ready индексирует поля отбора. Действующие DB и содержимое компедиума не проверялись. |

[Сверка порции и итоговая сверка 96 файлов второй серии](../review-log.md#task-0003020); браузер, мир и записи в БД не запускались.

## Уточнение TASK-0003.023

2026-09-11, `538dbac9bb9432c123fe4f3c00ab788b58517afb`; исходник не изменился. Повторно сверены Actor.mystery и Item.clue/obstacle: модели и листы зарегистрированы, но ключей в documentTypes нет. Изолированная строгая проверка настоящего DocumentTypeField с перечнем Item-типов манифеста отвергает clue, принимает spell. Это проверка поля с заданным перечнем, а не создание документов через сервер; реальные game.model/мир не менялись. Наблюдение остаётся issue-00005.

Связанные карточки: [module/data/investigation/mysteryActorData.js](module/data/investigation/mysteryActorData.js.md), [module/data/investigation/clueData.js](module/data/investigation/clueData.js.md), [module/data/investigation/obstacleData.js](module/data/investigation/obstacleData.js.md).

[Перекрёстная сверка порции](../review-log.md#task-0003023). БД, мир, исходники и права доступа не менялись.

## Уточнение TASK-0003.024

2026-09-11, `66cd03705dbc398eba0026284a298b5fbe337035`; исходник не изменился. Все девять значений storableItems (weapon, armor, enhancement, valuable, alchemical, component, diagrams, mutagen, container) присутствуют в documentTypes.Item. Это сравнение имён, не утверждение, что любой из них должен быть допустим по правилам. ContainerData и WitcherContainerSheet зарегистрированы по ключу container; расхождения типа для этой порции не обнаружено.

Связанные карточки: [module/data/item/containerData.js](module/data/item/containerData.js.md), [module/item/sheets/WitcherContainerSheet.js](module/item/sheets/WitcherContainerSheet.js.md).

[Перекрёстная сверка порции](../review-log.md#task-0003024). Мир, БД, код и метаданные доступа не менялись.

## Уточнение TASK-0003.033

2026-09-11, `12055fee62f01c6de49967044aedef9d7cfe0632`. Item.note:174 сопоставлен с полностью описанной NoteData и отсутствием отдельной регистрации листа. Сам тип действителен; пустой интерфейс отдельной заметки относится к WitcherItemSheet.PARTS и не означает отсутствия модели.

Связи: [module/data/item/noteData.js](module/data/item/noteData.js.md); [templates/sheets/item/note-sheet.hbs](templates/sheets/item/note-sheet.hbs.md). [Результаты и пределы проверки](../review-log.md#task-0003033).

### Дополнительная сверка TASK-0003.040

2026-09-11, `rusbar-main`, `74322e91edac106c82668f4a47eef53ce1889dc1`; исходники прежние. В documentTypes.ChatMessage объявлены attack/defense/damage. Базовый base разрешён common BaseChatMessage через baseTypeAllowed и coreTypes; отсутствие явного base в manifest не означает ошибку. Типы system сопоставлены настоящим TypeDataField (группа02). Пустой WitcherChatMessage не добавляет ограничений. Клиентский старт не проверен.

Сопоставленные исходники: [module/chatMessage/witcherChatMessage.js](../../../../module/chatMessage/witcherChatMessage.js), [module/data/chatMessage/baseMessageData.js](../../../../module/data/chatMessage/baseMessageData.js), [module/data/chatMessage/attackMessageData.js](../../../../module/data/chatMessage/attackMessageData.js), [module/data/chatMessage/defenseMessageData.js](../../../../module/data/chatMessage/defenseMessageData.js), [module/data/chatMessage/damageMessageData.js](../../../../module/data/chatMessage/damageMessageData.js). Полные новые описания: [witcherChatMessage.js](module/chatMessage/witcherChatMessage.js.md), [baseMessageData.js](module/data/chatMessage/baseMessageData.js.md), [attackMessageData.js](module/data/chatMessage/attackMessageData.js.md), [defenseMessageData.js](module/data/chatMessage/defenseMessageData.js.md), [damageMessageData.js](module/data/chatMessage/damageMessageData.js.md).

[Сверка порции и всей серии .031–.040](../review-log.md#task-0003040). Уточнение связи не означает повторной проверки всех сценариев соседнего файла; мир/БД и браузер не запускались.

## Дополнительная сверка TASK-0003.041

2026-09-12, rusbar-main, d5c7a4b871dce3aa55f4b8b589e62c3c9450f2d3; исходник не изменён.

Первые две полные CSS-карточки: [attack-sheet.css](styles/attack-sheet.css.md) и [weapon-roll.css](styles/weapon-roll.css.md). Они подключены косвенно через witcher-styles.css (@import строки 3/17), не отдельными entries manifest.styles. Остальные ресурсы файла импорта не считаются полностью разобранными.

[Сверка и ограничения](../review-log.md#task-0003041). Уточнение связи не увеличивает пофайловое покрытие; исправления не выполнялись.

## Дополнительная сверка TASK-0003.050

2026-09-12, rusbar-main, 3f78cbf0372e1da3d5a840e41b456d954c64e403; исходник не изменён.

Маршрут styles:23 → [входной CSS](styles/witcher-styles.css.md) → 35 импортов теперь описан целиком: 36 CSS, 690 rule-узлов, 1708 declarations в правилах и два в @font-face. Все импорты уникальны, без дочерних циклов; единственный url — существующий исключённый шрифт.

Pack paths: настоящий PackageCompendiumPacks._cleanElement в /opt/foundryvtt/common/packages/base-package.mjs:163–167 удаляет окончание .db. Отдельно исполнено его тело с фасадом базовой очистки для всех семи записей манифеста; нормализованные пути совпадают с cwd/packs/<pack> у [compile-скрипта](utils/packs.mjs.md). В текущем packs пять каталогов; combat/criticalWounds не найдены. Это наблюдение файловой системы без чтения DB и без доказательства неисправности запущенного мира; issue-00001/00002 остаются отдельными.

[build.json](build.json.md) потребляется .github/workflows/get-includes.js → release.yml → zip. Workflow после сборки заменяет version/url/manifest/download манифеста; исходное ACTIONn не доказывает неправильный опубликованный URL. .github прочитан только как справочный потребитель, не добавлен в реестр. Выпуск и установка не запускались.

[Перекрёстная сверка серии и пределы проверки](../review-log.md#task-0003050). Связанные файлы повторно в покрытие не засчитывались; серверная запись, браузер и HTTP системы не проверялись.

## Дополнительная сверка TASK-0003.051

2026-09-12, rusbar-main, 4b9951094106e26d9274bbd5d5e8e7a709cfcf24. Исходник не менялся.

languages сохраняет все восемь объявлений. В текущем пофайловом аудите полностью разобраны только [en](lang/en.json.md) и [ru](lang/ru.json.md); шесть других языков и контент компедиумов исключены пользователем. Исполненный setLanguage Foundry подтвердил выбор ru, загрузку en fallback и порядок system → module → world. HTTP подменён локальными данными в памяти. 22 объявленных типа Actor/Item/ActiveEffect имеют TYPES-подписи; ещё четыре подписи mystery/clue/obstacle/skill соответствуют зарегистрированным моделям вне манифеста (прежняя issue-00005). Изменение границ документации не меняет манифест.

[Результаты и ограничения сверки](../review-log.md#task-0003051). Правки относятся к документации; мир, браузер, БД и исходники не менялись.

## Уточнение TASK-0003.052

2026-09-12, rusbar-main, 2a3f197019c96225c0b6bedfb7c322ab9cc734bc; исходник не изменён.

Подробно разобраны семь экспортов packsJson/style: пакет Style_and_Values_Sub-tables, тип RollTable, путь packs/style.db и семь ID согласованы. Прямая ссылка на каждую таблицу находится в Style_and_Values_CjaIcLRWSlzwI6ly.json основного Character-gen. Все семь UUID разрешены при изолированном рекурсивном броске; наличие экспорта не подтверждает установку/доступ к живому pack. Изменения манифеста, зависимости от better-rolltables и новые требования к локализациям не вводились.

[Семь карточек style](README.md#таблицы-стиля-и-ценностей--task-0003052), [перекрёстная сверка и пределы исполнения](../review-log.md#task-0003052).

## Уточнение TASK-0003.053

2026-09-12, rusbar-main, 93beea0953821c9d8f080f815e686dc4da0c6f9e; исходник не изменён.

Подробно разобраны 21 экспорт packsJson/lifepath, зарегистрированные как Life_Event_Sub-tables, тип RollTable, packs/lifepath.db. Все 18 внутренних ссылок и четыре входящие ссылки из Character-gen/Witcher_Lifepath_and_BG_Sub-tables сопоставлены по ID, имени и типу. Полная глубина внутри пакета — два перехода; цикл не найден. Проверка экспортов не подтверждает состояние действующей БД.

[21 карточка lifepath](README.md#таблицы-жизненных-событий--task-0003053), [перекрёстная сверка и пределы проверки](../review-log.md#task-0003053).

## Уточнение TASK-0003.054

2026-09-12, rusbar-main, 63e9a79fefa7743fcf709b2fa19ddbe144f353a0; исходник не изменён.

Разобраны все 35 JSON / 313 результатов Character-gen_Sub-tables, зарегистрированного как RollTable в packs/character-generator-sub-tables.db. Все 79 исходящих ссылок остаются в этом пакете; 27 входящих прямых ссылок приходят из пяти документов Character-gen. Дополнительный RandomCharacter обращается к расовым генераторам: некоторые семейные пути достигают глубины 6 и вызывают исключение ядра (issue-00320). ID/имена/тип согласованы; действующая БД не проверялась.

[35 карточек подтаблиц](README.md#подтаблицы-создания-персонажа--task-0003054), [перекрёстная сверка и пределы](../review-log.md#task-0003054).

## Уточнение TASK-0003.055

2026-09-12, rusbar-main cd2743d0548d5c129065c970d4aa5c43cc9632e2; исходник не изменён.

Проверен зарегистрированный пакет Witcher_Lifepath_and_BG_Sub-tables: 41 RollTable / 321 result, путь packs/witcher-lifepath.db, каталог экспорта packsJson/witcher-lifepath. Из 95 исходящих ссылок 94 остаются внутри пакета, одна ведёт на Enemies: Gender из Life_Event_Sub-tables. Входящих ссылок из пяти Character-gen — 18; все ID, имена и типы согласованы. Содержание установленного пакета не проверено.

[41 карточка биографии ведьмака](README.md#таблицы-биографии-ведьмака--task-0003055), [перекрёстная сверка и пределы](../review-log.md#task-0003055).
