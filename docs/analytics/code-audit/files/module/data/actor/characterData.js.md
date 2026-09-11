# module/data/actor/characterData.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/data/actor/characterData.js](../../../../../../../module/data/actor/characterData.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `fe7ea7420cd4dfa6ee51baf7520f7b0ad8f8b13d` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.006](../../../../../../tasks/task-0003.006.md), одна порция из четырёх файлов |
| Запись перекрёстной сверки | [TASK-0003.006](../../../../review-log.md#task-0003006) |

## Назначение файла

Специализация общей модели для Actor.character: добавляет биографию, пол, число отображаемых десятилетий, опыт, четыре слота обучения и журналы. Подготавливает объект обогащённого текста биографии для листа.

## Условия использования

Default export CharacterData extends CommonActorData. [module/setup/registerDataModels.js](../../../../../../../module/setup/registerDataModels.js) импортирует класс:4 и связывает его с CONFIG.Actor.dataModels.character:38. Тип character объявлен в [system.json](../../../../../../../system.json); [module/setup/registerSheets.js](../../../../../../../module/setup/registerSheets.js):105–108 назначает WitcherCharacterSheet. Модель содержится в Actor.system; имя, изображение, предметы и эффекты — поля документа Actor.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| fields | const:7 | Классы полей Foundry | Локальная | Чтение в defineSchema |
| CharacterData | class:9–41 | Модель персонажа | Default export; Actor.character | Создание схемы; enrichedText; наследуемые методы CommonActorData |

| Поле system | Тип / initial | Определение | Назначение и действия |
| --- | --- | --- | --- |
| 19 полей CommonActorData | ...commonData:14 | super.defineSchema:11; [полный перечень общей схемы](commonActorData.js.md) | Включаются без замены: currency, healthState, deathSaves, stats, derivedStats, reputation, adrenaline, skills, skillGroupModifiers, attackStats, combatEffects, damageTypeModification, focus1, focus2, focus3, focus4, notes, pannels, lifepathModifiers. |
| general | SchemaField(general()) | :16; [module/data/actor/templates/character/generalData.js](../../../../../../../module/data/actor/templates/character/generalData.js) | Девять полей биографии: background, details, homeland, reputation, socialStanding, name, race, age, lifeEvents. |
| gender | StringField, '' | :17; определение здесь | Пол для header и background формы. |
| lifeEventCounter | NumberField, 20 | :18; определение здесь | Количество отображаемых десятилетий; ограничение min1/max20 есть в форме, в NumberField не задано. |
| improvementPoints | NumberField, 0 | :20; определение здесь | Обычный опыт; операции Log и skillMixin. |
| magic | SchemaField | :21–23; определение здесь | Одно поле magicImprovementPoints:NumberField=0; отдельный запас магического опыта. |
| skillTraining1 | SchemaField(skillTraining()) | :25; [module/data/actor/templates/character/skillTrainingData.js](../../../../../../../module/data/actor/templates/character/skillTrainingData.js) | Независимый слот name/value для ручной записи обучения. |
| skillTraining2 | SchemaField(skillTraining()) | :26; [module/data/actor/templates/character/skillTrainingData.js](../../../../../../../module/data/actor/templates/character/skillTrainingData.js) | Независимый слот name/value для ручной записи обучения. |
| skillTraining3 | SchemaField(skillTraining()) | :27; [module/data/actor/templates/character/skillTrainingData.js](../../../../../../../module/data/actor/templates/character/skillTrainingData.js) | Независимый слот name/value для ручной записи обучения. |
| skillTraining4 | SchemaField(skillTraining()) | :28; [module/data/actor/templates/character/skillTrainingData.js](../../../../../../../module/data/actor/templates/character/skillTrainingData.js) | Независимый слот name/value для ручной записи обучения. |
| logs | EmbeddedDataField(Log) | :30; [module/data/actor/templates/character/logData.js](../../../../../../../module/data/actor/templates/character/logData.js) | Модель журналов ipLog/currencyLog; её методы используют parent CharacterData и parent.parent Actor. |

Итого 29 верхних полей: 19 общих + 10 собственных. У добавленных здесь чисел нет собственных min/max/integer; наличие поля не означает автоматическое начисление опыта или создание расы/профессии. general.reputation — текст биографии, общая system.reputation — отдельная числовая модель.

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| static defineSchema:10–32 | Доступны родительский класс, фабрики и Log | Объект 29 полей | super.defineSchema, spread, десять дополнений | Синхронно, без записи документов; родительские поля не переопределены. |
| async enrichedText:34–40 | this.general.background.value, schema | Promise<{general:{background:{enriched,value,systemField}}}> | await createEnrichedText(this, value, 'general.background.value') | Один последовательный async-вызов; собственных присваиваний/сохранения и catch нет; ошибка обогащения отклонит Promise. |

prepareBaseData, calcCurrencyWeight, migrateData, migrateCalculatedStats и migrateAdrenaline наследуются от CommonActorData; собственных overrides для них нет. prepareDerivedData остаётся пустым методом TypeDataModel. Вычисляемых getters, обработчиков событий и регистрации класса внутри файла нет.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| CommonActorData; super.defineSchema | [module/data/actor/commonActorData.js](../../../../../../../module/data/actor/commonActorData.js); [карточка](commonActorData.js.md) | Импорт:2 / наследование:9 / вызов:11 | Общие 19 полей и подготовка/миграции | Родитель полностью разобран в этой порции. |
| general | [module/data/actor/templates/character/generalData.js](../../../../../../../module/data/actor/templates/character/generalData.js); [карточка](templates/character/generalData.js.md) | Импорт:3 / вызов:16 | SchemaField(general()) | Пять прямых зависимостей general уже описаны; связность сверена. |
| Log | [module/data/actor/templates/character/logData.js](../../../../../../../module/data/actor/templates/character/logData.js); [карточка](templates/character/logData.js.md) | Импорт:4 / включение:30 | EmbeddedDataField; владелец двух журналов | Сами операции журналирования определены в Log, не здесь. |
| skillTraining | [module/data/actor/templates/character/skillTrainingData.js](../../../../../../../module/data/actor/templates/character/skillTrainingData.js); [карточка](templates/character/skillTrainingData.js.md) | Импорт:5 / четыре вызова:25–28 | Слоты обучения | Определения и текущие поля формы сверены с TASK-0003.005. |
| createEnrichedText | [module/data/dataUtils.js](../../../../../../../module/data/dataUtils.js); [карточка](../dataUtils.js.md) | Именованный импорт:1 / вызов:37 | Возвращает enriched, исходный value, systemField | Внутри helper: TextEditor.implementation.enrichHTML(field), system.schema.getField(path). |
| SchemaField, StringField, NumberField, EmbeddedDataField | Foundry 14.367.0: /opt/foundryvtt/common/data/fields.mjs | Глобальный API через fields:7 | defineSchema | Проверены реальные определения и экземпляры. |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/setup/registerDataModels.js](../../../../../../../module/setup/registerDataModels.js) | CharacterData | Регистрация Actor.character | 4,38 |
| [module/actor/sheets/WitcherCharacterSheet.js](../../../../../../../module/actor/sheets/WitcherCharacterSheet.js) | enrichedText; general.lifeEvents; lifeEventCounter | _prepareContext дополняет context.enrichedText; преобразует lifeEvents, подставляет counter | 134–142; результат модели await. |
| [templates/partials/character/tab-background.hbs](../../../../../../../templates/partials/character/tab-background.hbs) | general, gender, lifeEventCounter; enrichedText.general.background | Редактирование полей; eachLimit; formGroup с отдельно переданным .enriched | 36,52,62–66 |
| [templates/partials/character-header.hbs](../../../../../../../templates/partials/character-header.hbs) | gender | Показывает пол | 14 |
| [templates/partials/character/tab-skills.hbs](../../../../../../../templates/partials/character/tab-skills.hbs) | improvementPoints, skillTraining1–4 | IP-секция общей вкладки | 56–107; использование монстром не создаёт ему эти поля. |
| [module/actor/mixins/skillMixin.js](../../../../../../../module/actor/mixins/skillMixin.js) | magic.magicImprovementPoints, improvementPoints; logs | levelUpSkill проверяет/списывает опыт, вызывает Log | 1–39; issue-00017 описывает конфликтующие updates. |
| [module/data/actor/templates/character/logData.js](../../../../../../../module/data/actor/templates/character/logData.js) | parent = CharacterData; parent.parent = Actor | addIpLog/addCurrencyLog читают и меняют балансы | Полный контракт и подмены записи в карточке Log. |
| [module/actor/sheets/WitcherMonsterSheet.js](../../../../../../../module/actor/sheets/WitcherMonsterSheet.js); [module/data/actor/monsterData.js](../../../../../../../module/data/actor/monsterData.js) | Отсутствующие поля IP | Лист монстра использует общую вкладку; MonsterData не наследует CharacterData | issue-00030; это несоответствие потребителя, не наследование модели. |

Область поиска — module/, templates/, packsJson/, регистрации и прежние карточки. Остальные потребители вложенных general/logs/training перечислены в их карточках; их исходники не получают новый статус в этой порции.

## Данные и изменения состояния

defineSchema собирает определения; значения создаёт Foundry. enrichedText создаёт объект контекста с одним HTMLField, не заменяет general.background.value и не делает Actor.update. Проверенный systemField.fieldPath равен system.general.background.value. Выбор расы/профессии листом через actor.getList относится к предметам Actor, а не новым определениям в этой модели.

Подготовка листа использует живую модель: WitcherActorSheet:70 присваивает context.system=actor.system; последующее преобразование lifeEvents в массив описано issue-00024. Оно не выполняется CharacterData.enrichedText. Унаследованная подготовка также меняет память; сохранение опыта делают потребители через Actor.update и Log. Это разные действия.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Сборка | 41 строка, пять импортов; настоящие CharacterData/CommonActorData | 29 полей, из них 10 собственных; все 19 общих сохранены | Без регистрации реального Actor в мире. |
| Обогащение | Оригинальный enrichedText и createEnrichedText; TextEditor подменён async s=>'ENRICHED:'+s | Сохранены исходный value и snapshot; отдельный enriched; systemField совпал с schema.getField | Сам редактор/рендер HTML не запускался. |
| Наследуемая подготовка | Прямой prepareBaseData настоящей CharacterData | Результаты совпали с формулами CommonActorData; source не изменился | Не весь жизненный цикл Actor. |
| Предыдущие карточки | general, valueLabel, background/details/homeland/lifeEvents, Log/ipLog/currencyLog, training, dataUtils | Пути, владельцы и способы использования согласованы | Полный UI оставлен следующим порциям. |

## Непроверенные участки и открытые вопросы

Файл прочитан полностью. Browser UI, работа formGroup/TextEditor, запись в БД и актуальность старых игровых документов не проверены. Изолированный enrichment проверяет структуру возврата и пути, не визуальное представление. Механика расы/профессии и правила начисления опыта здесь не определяются.

## Связанные проблемы

- [issue-00017](../../../../../../issues/potential/issue-00017.md) — списание магического опыта в levelUpSkill и Log.
- [issue-00024](../../../../../../issues/potential/issue-00024.md) — изменение формы lifeEvents при подготовке листа.
- [issue-00028](../../../../../../issues/potential/issue-00028.md) — потерянный Promise операций Log.
- [issue-00029](../../../../../../issues/potential/issue-00029.md) — отрицательный строковый ручной расход IP.
- [issue-00030](../../../../../../issues/potential/issue-00030.md) — использование персонажной вкладки IP монстром.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.006 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.

## Уточнение TASK-0003.007

2026-09-10, `b8b89a7e3392235f993c21f3c6d277a4a2e7a55f`. 19 собственных определений Actor и порядок подключения примесей сопоставлены с CharacterData. Расчёты проверены с настоящей моделью; схемы/биография/журналы не стали частью документа Actor. Унаследованный addItem ожидает update/create, removeItemsOfType — нет (issue-00034).

Карточки: [WitcherActor](../../actor/witcherActor.js.md), [modifierMixin](../../actor/mixins/modifierMixin.js.md). [Сверка TASK-0003.007](../../../../review-log.md#task-0003007).

## Уточнение TASK-0003.025

2026-09-11, `rusbar-main`, `a2670a0a10c62b28d836b1a57577c4836f14cf20`. Полный общий _prepareContext V2 присваивает context.system=actor.system; V1 getData берёт actor.toObject(false).system. Пустая настоящая CharacterData проходит оба потока с фасадом Actor; temporaryHpSum добавляется в подготовленную модель только у V2, source не меняется. Преобразование lifeEvents в массив находится в дочернем CharacterSheet, а V2 handler затем ожидает find по key (issue-00024).

Общие определения: [module/actor/sheets/WitcherActorSheet.js](../../../../../../../module/actor/sheets/WitcherActorSheet.js) и [module/actor/sheets/WitcherActorSheetV1.js](../../../../../../../module/actor/sheets/WitcherActorSheetV1.js). [Методика и перекрёстная сверка](../../../../review-log.md#task-0003025). Это точечное уточнение связей; полный разбор новых соседних файлов не засчитывается.

## Уточнение TASK-0003.029

2026-09-11, `273a6d7db0b7c866399db3ecd4f7191817ae6f10`. Развитие навыка использует improvementPoints, magic.magicImprovementPoints и logs. Реальный levelUpSkill/Log подтвердил конкурирующие payload магического баланса и отсутствие проверки достаточности обычных IP. tab-skills выводит четыре skillTraining и итоги, подготовленные CharacterSheet.

Сверенные связи: [module/actor/mixins/skillMixin.js](../../../../../../../module/actor/mixins/skillMixin.js); [templates/partials/character/tab-skills.hbs](../../../../../../../templates/partials/character/tab-skills.hbs); [templates/sheets/actor/configuration/app/edit-skills.hbs](../../../../../../../templates/sheets/actor/configuration/app/edit-skills.hbs). Полные карточки новых файлов — в [указателе порции](../../../README.md#навыки-броски-развитие-и-пользовательские-навыки--task-0003029). [Проверки, ограничения и версия](../../../../review-log.md#task-0003029). Исходники и статус проблем не менялись.

## Уточнение TASK-0003.030

2026-09-11, `aa6af106e86a9c75fe050d599f961c8fadb74f1b`. Текущий CharacterSheet готовит totalStats через statMixin; Monster этого не делает. В CharacterData нет customStat, поэтому HP/STA идут по вычисляемому маршруту Actor; показанный общий редактор сам не ограничивает ввод этих баз.

Сверенные источники: [module/actor/sheets/mixins/statMixin.js](../../../../../../../module/actor/sheets/mixins/statMixin.js); [templates/partials/character/tab-stats.hbs](../../../../../../../templates/partials/character/tab-stats.hbs); [templates/sheets/actor/configuration/app/partials/stats-block.hbs](../../../../../../../templates/sheets/actor/configuration/app/partials/stats-block.hbs). [Итоговая сверка третьей серии, сценарии и ограничения](../../../../review-log.md#task-0003030). Код и статусы проблем не менялись.

## Уточнение TASK-0003.031

2026-09-11, `928ce4e537c6a3fdc34f8b6fa3fcfdb5a669f68d`. Настоящая модель использована в полном контексте дочернего листа. _prepareContext меняет подготовленное general.lifeEvents на массив; _source при этом не меняется. _saveIpSpending('-3') при IP10 передаёт '10-3', и NumberField отвергает результат (issue-00200). Значение HP120 прошло FormDataExtended/_processFormData и updateSource; буквальный max99 в HTML сам по себе не ограничивает модель.

Связи: [module/actor/sheets/WitcherCharacterSheet.js](../../actor/sheets/WitcherCharacterSheet.js.md); [templates/partials/character-header.hbs](../../../templates/partials/character-header.hbs.md); [templates/sheets/actor/partials/character/sidebar.hbs](../../../templates/sheets/actor/partials/character/sidebar.hbs.md). [Методика и ограничения сверки](../../../../review-log.md#task-0003031).
