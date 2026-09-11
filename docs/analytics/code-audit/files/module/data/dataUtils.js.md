# module/data/dataUtils.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/data/dataUtils.js](../../../../../../module/data/dataUtils.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `7b7788bc614e5b7a57f8c596fb64ca75ecabd8b7` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.001](../../../../../tasks/task-0003.001.md), одна порция из пяти файлов |
| Запись перекрёстной сверки | [TASK-0003.001](../../../review-log.md#task-0003001) |

## Назначение файла

Асинхронный помощник подготовки текстового поля для листа. Возвращает обработанный HTML, исходное значение и определение поля схемы. Используется моделями Actor и Item.

## Условия использования

Именованный экспорт `createEnrichedText`; собственного кода регистрации или вызова при импорте нет. Пять моделей вызывают его из `async enrichedText()`, всего 20 вызовов: персонаж — 1, монстр — 3, раса — 4, профессия — 11, критическая травма — 1.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| createEnrichedText | async function, строки 1–7 | Готовит данные одного текстового поля | Именованный ES export | На каждом вызове создаёт новый объект; возвращает Promise, не сохраняет документ. |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| createEnrichedText(system, field, fieldPath) | system.schema.getField; исходное значение field для TextEditor; строковый/массивный путь, принимаемый getField | Promise<{enriched, value, systemField}> | 1. await enrichHTML(field). 2. value = field. 3. getField(fieldPath). | Ошибка enrichHTML отклоняет Promise до вызова getField. Ошибка схемы также отклоняет Promise. Собственных catch, нормализации и записи нет. |

`systemField` — объект определения `DataField`, а не значение игрового поля и не копия схемы. Для неизвестного корректно заданного пути `getField` возвращает `undefined`; функция не проверяет его наличие. Для неверного типа пути ошибка приходит из API Foundry.

В `enrichHTML` передаётся только `field`: функция не задаёт `rollData`, настройки секретных блоков, ссылки на документ или локализацию. При стандартной реализации 14.367 действуют параметры API по умолчанию. Назначенную реализацию TextEditor могут заменить внешние модули; их конфигурация не проверялась.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| TextEditor.implementation.enrichHTML | Foundry 14.367.0, /opt/foundryvtt/client/applications/ux/text-editor.mjs:123–163 | Глобальный API; async-вызов | Строка 3, обработать текст | Прочитаны API и вызов; реальные DOM-обработчики не запускались. |
| SchemaField#getField | Foundry 14.367.0, /opt/foundryvtt/common/data/fields.mjs:1031–1050 | Метод переданной схемы | Строка 5, найти определение поля | Проверены обход пути и возврат undefined; в проверке использована настоящая схема Stats. |
| system, field, fieldPath | Аргументы пяти моделей из таблицы потребителей | Передача данных | Описывают владельца, исходный текст и путь | Прямых импортов из других файлов системы в dataUtils.js нет. |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/data/actor/characterData.js](../../../../../../module/data/actor/characterData.js) | createEnrichedText | enrichedText: general.background.value | Импорт 1; вызов 37. |
| [module/data/actor/monsterData.js](../../../../../../module/data/actor/monsterData.js) | createEnrichedText | enrichedText: common, academicKnowledge, monsterLore → lore | Импорт 2; вызовы 69–71. |
| [module/data/item/raceData.js](../../../../../../module/data/item/raceData.js) | createEnrichedText | enrichedText: perk1–perk4.description | Импорт 4; вызовы 25–28. |
| [module/data/item/professionData.js](../../../../../../module/data/item/professionData.js) | createEnrichedText | enrichedText: definingSkill.definition, notes, девять definition в skillPath1–3 | Импорт 4; вызовы 29–44. |
| [module/data/item/criticalWoundData.js](../../../../../../module/data/item/criticalWoundData.js) | createEnrichedText | enrichedText: description | Импорт 1; вызов 63. |

Поиск импортов и вызовов выполнен во всём `module/`. Дальнейшие связи проверены точечно:

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/actor/sheets/WitcherCharacterSheet.js](../../../../../../module/actor/sheets/WitcherCharacterSheet.js) | Результаты enrichedText моделей | Добавляет контекст персонажа, профессии и расы | 139–164; вызовы ожидаются через await. |
| [module/actor/sheets/WitcherMonsterSheet.js](../../../../../../module/actor/sheets/WitcherMonsterSheet.js) | lore с тройками полей | Добавляет результат модели в context.enrichedText | 123–125. |
| [module/item/sheets/WitcherItemSheet.js](../../../../../../module/item/sheets/WitcherItemSheet.js) | Результат модели Item | context.enrichedText = await system.enrichedText?.() | 52. |
| [module/actor/sheets/WitcherActorSheet.js](../../../../../../module/actor/sheets/WitcherActorSheet.js) | description травмы | Собирает criticalWounds по UUID | 165–173. |
| [templates/partials/character/tab-background.hbs](../../../../../../templates/partials/character/tab-background.hbs) | general.background: systemField/value/enriched | formGroup | 52. |
| [templates/sheets/item/race-sheet.hbs](../../../../../../templates/sheets/item/race-sheet.hbs) | perk1–4: systemField/value/enriched | formGroup | 29, 33, 39, 43. |
| [templates/sheets/item/profession-sheet.hbs](../../../../../../templates/sheets/item/profession-sheet.hbs) | definingSkill, notes, skillPath1–3 | formInput | 36–161; 11 полей. |
| [templates/sheets/item/criticalWound-sheet.hbs](../../../../../../templates/sheets/item/criticalWound-sheet.hbs) | description | formInput | 32. |
| [templates/sheets/actor/partials/character/tab-effects.hbs](../../../../../../templates/sheets/actor/partials/character/tab-effects.hbs) | criticalWounds[uuid].enriched | Отображение описания травмы | 19. |
| [templates/sheets/actor/partials/monster/tabs/partials/monster-knowledge.hbs](../../../../../../templates/sheets/actor/partials/monster/tabs/partials/monster-knowledge.hbs) | lore.*.value вместо lore.*.enriched | Передаёт исходный текст в параметр enriched | 7, 14, 21; [issue-00013](../../../../../issues/potential/issue-00013.md). |

## Данные и изменения состояния

Функция не вызывает `update`, `create` или `delete`. Она сохраняет исходный аргумент в `value` и возвращает результат внешней обработки в `enriched`. Редактирование и сохранение выполняют формы потребителей и ядро. Обработка TextEditor может разрешать ссылки и выполнять другие действия ядра; отсутствие записи в этом помощнике не описывает все внутренние действия внешнего API.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Контракт и порядок | Исходная функция; управляемый Promise вместо enrichHTML; настоящая схема Stats | getField вызван только после завершения enrichHTML; value сохранён; systemField — тот же объект поля | TextEditor подменён; DOM, UUID и inline-rolls не проверялись. |
| Ошибка и неизвестный путь | Исключение enrichHTML; реальный getField('unknown') | Promise отклонён; для неизвестного пути systemField равен undefined | Запуск только в памяти Node. |
| Передача данных монстра | Реальная MonsterData, исходный HBS, Handlebars 4.7.9; подмены TextEditor/formGroup/localize | Все три поля шаблона передали исходный текст вместо подготовленного HTML | Редактор Foundry в браузере не запускался. |
| Охват вызовов | rg по имени функции и импорту; чтение вызовов и контекстов | 5 прямых моделей-потребителей, 20 вызовов | Полный разбор самих моделей и листов остаётся другим задачам. |

## Непроверенные участки и открытые вопросы

Сам файл прочитан полностью. Не проверялись DOM-обогащение, разрешение реальных UUID, редакторы в браузере, пользовательские реализации TextEditor и сохранение полей. Отсутствие переданных опций не объявлено ошибкой без конкретного требуемого сценария.

## Связанные проблемы

[issue-00013](../../../../../issues/potential/issue-00013.md) — шаблон знаний монстра использует неверный элемент возвращаемой тройки. Проблема локализована в потребителе, а не в самой функции.


## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.001 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.

## Уточнение TASK-0003.004

2026-09-10, `17eeb6ae9efccf7474b9ca1845b9ab6370671a26`. Уточнена цепочка [backgroundData](actor/templates/character/general/backgroundData.js.md) → CharacterData.enrichedText:34–40 → createEnrichedText → WitcherCharacterSheet._prepareContext:139–142 → formGroup в tab-background:52. Исходные методы с подменой TextEditor передали HTML-строку как value, отдельный enriched и настоящий HTMLField с fieldPath system.general.background.value. Редактор и запись формы не запускались.

[Перекрёстная сверка TASK-0003.004](../../../review-log.md#task-0003004).

## Уточнение TASK-0003.006

2026-09-10, `fe7ea7420cd4dfa6ee51baf7520f7b0ad8f8b13d`. Полностью разобраны оба Actor-потребителя: один вызов из CharacterData.enrichedText и три последовательных await из MonsterData.enrichedText. Настоящие поля имеют пути system.general.background.value и system.common/academicKnowledge/monsterLore; source после изолированного обогащения не изменён. MonsterData не проверяет show* перед вызовами; скрытие выполняет шаблон.

Карточки сборки: [characterData](actor/characterData.js.md), [monsterData](actor/monsterData.js.md). [Сверка TASK-0003.006](../../../review-log.md#task-0003006).

## Уточнение TASK-0003.008

2026-09-10, `c5edcbadd05ff4038a174bd2e2a49785e40ea878`; исходник не изменился относительно исходного среза. CommonItemData не определяет enrichedText. Соответствующие методы RaceData, ProfessionData и отдельной CriticalWoundData используют createEnrichedText; WitcherItem.enrichedText лишь условно делегирует system.enrichedText. Лист Item обращается к модели напрямую. Связи точечно проверены, без полного разбора этих специализированных моделей.

Связанные карточки: [CommonItemData](item/commonItemData.js.md) и [WitcherItem](../item/witcherItem.js.md). [Перекрёстная сверка](../../../review-log.md#task-0003008). Новая запись уточняет связи; исторические результаты прежних порций сохранены.

## Уточнение TASK-0003.018

2026-09-10, `rusbar-main`, `29319a7a7e1dfc0663edbc15166f3b6a19682a2f`. [RaceData.enrichedText](../../../../../../module/data/item/raceData.js) последовательно вызывает createEnrichedText для perk1–perk4, в том числе с пустым описанием. Возвращаются исходный value, отдельно enriched и реальные поля schema с путями system.perkN.description; source не изменяется. [Форма Item](../../../../../../templates/sheets/item/race-sheet.hbs) передаёт все три части правильно. WitcherCharacterSheet также готовит enrichedText.race, но tab-profession.hbs читает raw description через editor: [issue-00109](../../../../../issues/potential/issue-00109.md).

[Перекрёстная сверка](../../../review-log.md#task-0003018). Исходники не изменены; это уточнение проверенных связей, а не повторный полный разбор файла.

## Уточнение TASK-0003.019

2026-09-10, `rusbar-main`, `c26eb64dd54cc434087f54c3c6b678b6092b15a2`. [ProfessionData.enrichedText](../../../../../../module/data/item/professionData.js) делает 11 последовательных вызовов createEnrichedText для notes и 10 definition. Настоящие поля дали полные system.* пути; source не меняется. [Item-форма](../../../../../../templates/sheets/item/profession-sheet.hbs) передаёт value/enriched правильно, а tab-profession через editor берёт raw тексты. Это расширение [issue-00109](../../../../../issues/potential/issue-00109.md) на профессию в том же шаблоне/механизме.

[Перекрёстная сверка](../../../review-log.md#task-0003019). Исходники не изменены; уточнение касается проверенных связей, не повторного полного разбора файла.
