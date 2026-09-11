# module/data/actor/templates/character/generalData.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/data/actor/templates/character/generalData.js](../../../../../../../../../module/data/actor/templates/character/generalData.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `17eeb6ae9efccf7474b9ca1845b9ab6370671a26` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.004](../../../../../../../../tasks/task-0003.004.md), одна порция из восьми файлов |
| Запись перекрёстной сверки | [TASK-0003.004](../../../../../../review-log.md#task-0003004) |

## Назначение файла

Собирает общие сведения персонажа в system.general. Объединяет биографию, подробности, родину и события жизни с несколькими собственными полями. Параметры изменения урона в этот объект не входят.

## Условия использования

При импорте локальная const fields получает foundry.data.fields. Файл экспортирует фабрику определения схемы; значениями экземпляра и валидацией занимается Foundry, а не сама фабрика. CharacterData импортирует general и вызывает её в defineSchema. Общая модель CommonActorData и MonsterData не подключают general; у проверенного MonsterData поле general отсутствует.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| fields | const, 7 | Классы полей | Локальная | Читается фабрикой |
| general | function, 9–21 | Сборка общих сведений | Default export | Создаёт девять полей |
| background | SchemaField, 11 | HTML биографии | system.general.background | background() |
| details | SchemaField, 12 | Семь пар value/label | system.general.details | details() |
| homeland | SchemaField, 13 | value/otherValue | system.general.homeland | homeland() |
| reputation | SchemaField, 14 | Текстовая пара value/label | system.general.reputation | value=''; label='WITCHER.Reputation' |
| socialStanding | StringField, 15 | Ключ социального положения | system.general.socialStanding | initial=''; choices не заданы |
| name | StringField, 16 | Отдельная строка в general | system.general.name | initial=''; не равна автоматически Actor.name |
| race | StringField, 17 | Отдельная строка в general | system.general.race | initial=''; не ссылка на Item.race |
| age | NumberField, 18 | Возраст | system.general.age | initial=0; min/max/integer не заданы |
| lifeEvents | SchemaField, 19 | Двадцать записей | system.general.lifeEvents | lifeEvents() |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| general(); 9–21 | Доступен foundry.data.fields | Объект девяти определений полей | Создаёт новые определения полей при каждом вызове | Синхронно; без записи документов, обработчиков событий и собственного catch |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| valueLabel (default) | [module/data/actor/templates/valueLabelData.js](../../../../../../../../../module/data/actor/templates/valueLabelData.js) | Импорт/вызов | 1,14: текстовая reputation | valueLabel:3–8 |
| background (default) | [module/data/actor/templates/character/general/backgroundData.js](../../../../../../../../../module/data/actor/templates/character/general/backgroundData.js) | Импорт/вызов | 2,11 | HTMLField value |
| details (default) | [module/data/actor/templates/character/general/detailsData.js](../../../../../../../../../module/data/actor/templates/character/general/detailsData.js) | Импорт/вызов | 3,12 | Семь SchemaField(valueLabel) |
| homeland (default) | [module/data/actor/templates/character/general/homelandData.js](../../../../../../../../../module/data/actor/templates/character/general/homelandData.js) | Импорт/вызов | 4,13 | Два StringField |
| lifeEvents (default) | [module/data/actor/templates/character/general/lifeEventsData.js](../../../../../../../../../module/data/actor/templates/character/general/lifeEventsData.js) | Импорт/вызов | 5,19 | 20 SchemaField(lifeEvent) |
| SchemaField, StringField, NumberField | Foundry 14.367.0, /opt/foundryvtt/common/data/fields.mjs | Глобальный API | 7,11–19 | Настоящая модель и вложенные поля проверены |
| WITCHER.Reputation | [lang/en.json](../../../../../../../../../lang/en.json); [lang/ru.json](../../../../../../../../../lang/ru.json) | Начальное значение label | 14: ключ передаётся в valueLabel | Найден в обоих словарях; явное отображение general.reputation не найдено |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/data/actor/characterData.js](../../../../../../../../../module/data/actor/characterData.js) | general() | defineSchema включает general; enrichedText читает background.value | Импорт 3; 16; 34–40 |
| [module/actor/sheets/WitcherCharacterSheet.js](../../../../../../../../../module/actor/sheets/WitcherCharacterSheet.js) | Биография и альтернативные Item | Контекст general; lifeEvents преобразуется; race/homeland/profession берутся из Item | 122–148,151–165 |
| [templates/partials/character/tab-background.hbs](../../../../../../../../../templates/partials/character/tab-background.hbs) | homeland/details/age/socialStanding/background/lifeEvents | Форма биографии | 7–95 |
| [templates/partials/character-header.hbs](../../../../../../../../../templates/partials/character-header.hbs) | age/homeland/socialStanding | Показ шапки; имя из actor.name, раса из race.name | 2,6,18,22–42 |
| [module/actor/mixins/skillMixin.js](../../../../../../../../../module/actor/mixins/skillMixin.js) | general.socialStanding | addSocialStanding добавляет строки модификаторов для character | Вызов 67, метод 85–132 |
| [module/setup/config.js](../../../../../../../../../module/setup/config.js) | homelands/socialStanding | Словари для selectOptions; сами схемы не ограничены ими | 585–621 |

Поиск выполнен по именам файлов/экспортов, полным и относительным путям данных в module/, templates/ и packsJson/. В 226 JSON-компедиумах строковых путей, начинающихся с system.general или system.damageTypeModification, не найдено. Содержимое действующих БД packs и внешние макросы не проверялись.

## Данные и изменения состояния

Файл создаёт определения, не сохраняет Actor и не связывает строки с предметами автоматически. name/race/general.reputation.value не имеют найденных явных потребителей вне определения в module/templates/packsJson; это не доказательство ненужности данных. Имя редактируется по name документа, раса отображается по первому Item.race, а числовая system.reputation определяется отдельной моделью [module/data/actor/templates/common/reputationData.js](../../../../../../../../../module/data/actor/templates/common/reputationData.js). gender и lifeEventCounter определяет CharacterData рядом с general.

Социальное положение участвует в механике: только для type=character. При attribute.name='emp' навыки charisma/leadership/persuasion/seduction получают -1 для tolerated/toleratedFeared или -2 для hated/hatedFeared; charisma дополнительно -1 при feared/toleratedFeared/hatedFeared. Для will/intimidation последние три состояния дают +1. Это фактический код addSocialStanding, не проверка соответствия рулбуку. Возраст в найденных обращениях лишь читается/редактируется и не пересчитывает события.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Сборка и границы | Настоящие CharacterData/MonsterData/CommonActorData | Девять полей general только у CharacterData; damageTypeModification находится отдельно | Не запуск подготовки Actor |
| Социальные модификаторы | Исходный addSocialStanding с подменой settings/i18n | tolerated/emp/charisma → -1; hatedFeared → -2-1; feared/will/intimidation → +1; equal → пусто | Без Roll и проверки правил |
| Схема ↔ шаблоны | Установлены конкретные имена form inputs и контекст | Различены general.name и name; general.race и race Item; две reputation | Внешние потребители не проверены |
| Допустимые значения | CharacterData с age=-1.5, homeland='custom' | Значения приняты; своих диапазонов/choices нет | Само отсутствие диапазона не зарегистрировано ошибкой |

## Непроверенные участки и открытые вопросы

Полностью прочитан исходник и точечно проверены определения и потребители перечисленных связей. Мир, браузер, сохранение форм и применение реального ActiveEffect не запускались. Полный анализ соседних файлов остаётся их порциям; просмотр связи не повышает их статус в реестре. Полные правила социальных модификаторов и назначение неиспользуемых строк остаются за рамками этой порции.

## Связанные проблемы

[issue-00024](../../../../../../../../issues/potential/issue-00024.md) — лист заменяет general.lifeEvents массивом. [issue-00014](../../../../../../../../issues/potential/issue-00014.md) касается другой, числовой system.reputation; ключ WITCHER.Reputation этой фабрики найден.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.004 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.

## Уточнение TASK-0003.006

2026-09-10, `fe7ea7420cd4dfa6ee51baf7520f7b0ad8f8b13d`. CharacterData.general:16 включает девять полей. CharacterData добавляет рядом gender и lifeEventCounter, а enrichedText читает general.background.value. Схема CommonActorData не включает general: у монстра и loot этой биографии нет.

Карточки сборки: [characterData](../../characterData.js.md). [Сверка TASK-0003.006](../../../../../../review-log.md#task-0003006).

## Уточнение TASK-0003.018

2026-09-10, `rusbar-main`, `29319a7a7e1dfc0663edbc15166f3b6a19682a2f`. general.race (строка), general.socialStanding (строка) и general.homeland (вложенная модель Actor) независимы от [race Item](../../../../../../../../../module/data/item/raceData.js) и [homeland Item](../../../../../../../../../module/data/item/homelandData.js). CharacterSheet выводит выбранные Item; подстановка названия расы и родины не переписывает Actor.general. skillMixin.addSocialStanding читает именно general.socialStanding: таблица пяти регионов race и homeland не выбирают его автоматически. Изолированное изменение socialStanding.north у Item не изменило Actor.general.socialStanding.

[Перекрёстная сверка](../../../../../../review-log.md#task-0003018). Исходники не изменены; это уточнение проверенных связей, а не повторный полный разбор файла.

## Уточнение TASK-0003.029

2026-09-11, `273a6d7db0b7c866399db3ecd4f7191817ae6f10`. addSocialStanding читает единое general.socialStanding только при Actor.type=character. Шесть состояний проверены на пяти социальных навыках; feared комбинируется с tolerated/hated. Региональные поля Race Item этим методом не читаются; автоматического переноса при поиске по module/templates не найдено.

Сверенные связи: [module/actor/mixins/skillMixin.js](../../../../../../../../../module/actor/mixins/skillMixin.js); [module/data/item/raceData.js](../../../../../../../../../module/data/item/raceData.js); [module/data/item/templates/socialStandingData.js](../../../../../../../../../module/data/item/templates/socialStandingData.js). Полные карточки новых файлов — в [указателе порции](../../../../../README.md#навыки-броски-развитие-и-пользовательские-навыки--task-0003029). [Проверки, ограничения и версия](../../../../../../review-log.md#task-0003029). Исходники и статус проблем не менялись.

## Уточнение TASK-0003.031

2026-09-11, `928ce4e537c6a3fdc34f8b6fa3fcfdb5a669f68d`. Character читает age/socialStanding/legacy homeland, header отдаёт приоритет отдельному homeland Item. Подготовка lifeEvents выполняется прямо в общем system, counter при falsy заменяется длиной массива; обогащение general.background получено через CharacterData.enrichedText.

Связи: [module/actor/sheets/WitcherCharacterSheet.js](../../../../actor/sheets/WitcherCharacterSheet.js.md); [templates/partials/character-header.hbs](../../../../../templates/partials/character-header.hbs.md). [Методика и ограничения сверки](../../../../../../review-log.md#task-0003031).
