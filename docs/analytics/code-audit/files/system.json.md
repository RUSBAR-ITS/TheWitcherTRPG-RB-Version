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
| `url`, `manifest`, `download` — 149–151 | Заготовки URL выпуска; строка manifest заканчивается ACTIONn. Подстановка не исследована: .github исключён. |
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
| Главные стили | [styles/witcher-styles.css](../../../../styles/witcher-styles.css) | Ресурс CSS | Поле styles, строка 23 | Путь существует; содержательный разбор CSS вне порции |
| en | [lang/en.json](../../../../lang/en.json) | Локализация | languages, строки 89–130 | Путь существует; полное описание словаря вне этапа |
| es | [lang/es.json](../../../../lang/es.json) | Локализация | languages, строки 89–130 | Путь существует; полное описание словаря вне этапа |
| ptbr | [lang/ptbr.json](../../../../lang/ptbr.json) | Локализация | languages, строки 89–130 | Путь существует; полное описание словаря вне этапа |
| fr | [lang/fr.json](../../../../lang/fr.json) | Локализация | languages, строки 89–130 | Путь существует; полное описание словаря вне этапа |
| de | [lang/de.json](../../../../lang/de.json) | Локализация | languages, строки 89–130 | Путь существует; полное описание словаря вне этапа |
| it | [lang/it.json](../../../../lang/it.json) | Локализация | languages, строки 89–130 | Путь существует; полное описание словаря вне этапа |
| ru | [lang/ru.json](../../../../lang/ru.json) | Локализация | languages, строки 89–130 | Путь существует; полное описание словаря вне этапа |
| pl | [lang/pl.json](../../../../lang/pl.json) | Локализация | languages, строки 89–130 | Путь существует; полное описание словаря вне этапа |
| Данные семи компедиумов | `packs/combat.db`, `packs/criticalWounds.db`, `packs/character-generator.db`, `packs/character-generator-sub-tables.db`, `packs/witcher-lifepath.db`, `packs/lifepath.db`, `packs/style.db` | Объявленные пути | packs, строки 44–88 | Ни один из семи буквальных путей в checkout не существует; это не подтверждает ошибку релизной сборки или загрузчика |
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

Файл прочитан полностью. Не проверены выпуск, подстановка заготовок, интерпретация отсутствующих путей packs загрузчиком, загрузка мира и модулей. Для дополнительных типов выполнена сверка с локальными Document.TYPES, DocumentTypeField и DocumentSheetConfig ядра; создание этих типов в мире не воспроизводилось. Отсутствие собранных баз в checkout не приравнивается к дефекту кода.

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
