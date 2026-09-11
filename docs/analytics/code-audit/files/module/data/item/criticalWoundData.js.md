# module/data/item/criticalWoundData.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/data/item/criticalWoundData.js](../../../../../../../module/data/item/criticalWoundData.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `b09f992960a76d1c75946f402e42d93fa0785008` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.020](../../../../../../tasks/task-0003.020.md), 10 файлов, 428 логических строк |
| Запись перекрёстной сверки | [TASK-0003.020](../../../../review-log.md#task-0003020) |

## Назначение файла

Схема system предмета criticalWound, расчёт длительности заживления, подготовка описания и переход к следующему Item. Механическое действие травмы задаётся отдельно встроенными ActiveEffect.

## Условия использования

CriticalWoundData — default export, прямой наследник Foundry TypeDataModel. registerDataModels назначает CONFIG.Item.dataModels.criticalWound; system.json объявляет тип и HTML description. Импорт определяет класс, fields и замороженную metadata.type; документов не создаёт. prepareDerivedData вызывается жизненным циклом модели. heal вызывается отдыхом, treat — кнопкой или heal.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| CriticalWoundData; fields; metadata.type | Класс 5–107, alias 3, metadata 6–8 | Модель типа criticalWound | Default export; type='criticalWound' | Наследует TypeDataModel, не CommonItemData |
| description | HTMLField, 12 | HTML-описание | initial='' | Читается enrichedText; собственных правил эффектов нет |
| criticalLevel; treatment; location | StringField, 14–19 | Степень, состояние лечения, локация | initial simple / none / torso | choices в схеме нет; UI предлагает словари CONFIG |
| lesserEffect | BooleanField, 20–24 | Признак меньшего эффекта для выбора из компедиума | initial=false; label/hint | Сам по себе не уменьшает штраф и не меняет ActiveEffect |
| daysHealed; healingTime; sterilized | NumberField/BooleanField, 26–28 | Счётчик дней, вычисляемая цель и использованная стерилизация | initial 0 / 0 / false; у чисел нет integer/min | daysHealed изменяется в памяти и отправляется update; healingTime пересчитывается без записи |
| followUp | DocumentUUIDField, 30–34 | Ссылка на следующий Item | type='Item'; initial=null в настоящей модели | Не ограничена подтипом criticalWound; состояние/дни из текущей травмы явно не переносятся |
| canHaveTemporaryItemImprovement | Getter, 104–106 | Запрет временного предметного улучшения | Всегда false | Не запрещает обычные переносимые ActiveEffect |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| static defineSchema():10–36 | foundry.data.fields | Объект девяти полей | Описание и восемь полей состояния/ссылок | Синхронно; произвольные строки и дробные дни принимаются моделью |
| prepareDerivedData():38–45 | this.parent — Item; его parent — Actor или null | void | super, затем calculateHealingTime(actor), если есть владелец | У отдельного Item срок не пересчитывается; при вызове модели без parent защита отсутствует |
| calculateHealingTime(actor):47–59 | actor.system.stats.body.max; criticalLevel | void | simple=max(8−BODY,1), complex=max(12−BODY,1), difficult=max(15−BODY,1) | Меняет только подготовленное healingTime; deadly и неизвестные строки не имеют case/default |
| async enrichedText():61–65 | description и schema | Promise<{description}> | await createEnrichedText(this,description,'description') | Не записывает Item; ошибка helper проходит вызывающему |
| async heal({sterilized}):67–92 | Объект параметров; счётчики и treatment | Promise<void> | При treated: +1 день; при новой стерилизации ещё +2 и запрос sterilized=true. Затем сравнение срока; не-deadly вызывает treat, иначе update | Сравнение срока вне проверки treatment. Ни treat, ни update не ожидаются; Object.keys(updates) всегда truthy, включая [] |
| async treat():94–102 | followUp; this.parent и его parent | Promise<void> | Если UUID есть: await fromUuid, затем actor.createEmbeddedDocuments('Item',[followUpItem]); в конце parent.delete() | Не проверяет найденный Item/Actor; создание и удаление не await/return. Отказ resolve прерывает метод, отказ create не удерживает удаление |
| get canHaveTemporaryItemImprovement():104–106 | Нет | false | Возвращает константу | Не изменяет документы |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| createEnrichedText | [module/data/dataUtils.js](../../../../../../../module/data/dataUtils.js) | Прямой import / await | 1, 63; описание → enriched/value/systemField | Helper читает schema.getField и TextEditor.enrichHTML |
| TypeDataModel; HTMLField, StringField, BooleanField, NumberField, DocumentUUIDField | Foundry 14.367.0: /opt/foundryvtt/common/abstract/type-data.mjs; common/data/fields.mjs | Наследование/схема | 3–36; построение/очистка модели | Настоящие классы исполнены в Node 24.16.0 |
| BODY.max | [module/data/actor/templates/common/stats/statsData.js](../../../../../../../module/data/actor/templates/common/stats/statsData.js) | Чтение Actor | 50–56; длительность | Путь stats.body определён схемой характеристик; источник max — общий цикл Actor |
| update/delete/createEmbeddedDocuments/fromUuid | Foundry 14.367.0: common/abstract/document.mjs; client/data/client-backend.mjs; common/abstract/data.mjs | API документов и UUID | 87–101; запись, замена Item | DataModel.cleanData принимает Document/DataModel; передача самого Item допустима. null не является допустимым объектом; запрос БД не запускался |
| Item.effects и transfer | [module/activeEffect/witcherActiveEffect.js](../../../../../../../module/activeEffect/witcherActiveEffect.js) | Соседний механизм воздействия | Обычные эффекты травмы применяются к Actor независимо от heal | Foundry actor.allApplicableEffects перечисляет transfer-эффекты принадлежащих Item; у модели нет собственной коррекции changes |
| criticalWound; htmlFields | [system.json](../../../../../../../system.json) | Декларация типа | documentTypes.Item.criticalWound | description совпадает с HTMLField |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/setup/registerDataModels.js](../../../../../../../module/setup/registerDataModels.js) | CriticalWoundData | import и CONFIG.Item.dataModels.criticalWound | 33, 52 |
| [module/item/sheets/WitcherItemSheet.js](../../../../../../../module/item/sheets/WitcherItemSheet.js) | schema, enrichedText | _prepareContext дочернего листа | systemFields/enrichedText/item/document |
| [module/item/sheets/WitcherCriticalWoundSheet.js](../../../../../../../module/item/sheets/WitcherCriticalWoundSheet.js) | followUp | Drop Item.uuid | _onDropItem |
| [templates/sheets/item/criticalWound-sheet.hbs](../../../../../../../templates/sheets/item/criticalWound-sheet.hbs) | Все поля кроме ручного sterilized | Форма травмы и computed healingTime | Имена system.* и formGroup |
| [module/actor/sheets/mixins/healMixin.js](../../../../../../../module/actor/sheets/mixins/healMixin.js) | heal | recoverActor перебирает все criticalWound | forEach без ожидания |
| [module/actor/sheets/mixins/criticalWoundMixin.js](../../../../../../../module/actor/sheets/mixins/criticalWoundMixin.js) | treat | _onTreat по UUID кнопки | Без обновления treatment в этом обработчике |
| [module/actor/sheets/WitcherActorSheet.js](../../../../../../../module/actor/sheets/WitcherActorSheet.js) | enrichedText | _prepareItems → criticalWounds[uuid] | Описание для вкладки эффектов |
| [templates/partials/crit-wounds-table.hbs](../../../../../../../templates/partials/crit-wounds-table.hbs) | Степень, лечение, локация, дни | Отображение Item и inline-edit | Таблица не меняет model сама |
| [module/actor/mixins/damageMixin.js](../../../../../../../module/actor/mixins/damageMixin.js) | criticalLevel/location/lesserEffect/treatment | applyCritWound фильтрует индекс; отдельно есть одноимённый calculateHealingTime | Точечный разбор 312–358; второй расчёт не вызван данной моделью |
| [module/TheWitcherTRPG.js](../../../../../../../module/TheWitcherTRPG.js) | Поля отбора травмы | ready запрашивает четыре поля индекса | getIndex не разрешает followUp и не лечит |

Область поиска: module/ и templates/ текущего checkout; регистрация сверена с system.json. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Травма — один Item с собственными effects, не массив специальной модели правил. Здесь нет ruleId, таблицы штрафов, проверки лечения или автомата none→stabilized→treated. Ручной выбор treatment меняет строку; кнопка treat заменяет/удаляет документ по followUp. Лечение не переносит дни, sterilized или effects вручную: новый документ получает данные найденного Item. Пустой followUp означает удаление исходного Item.

На BODY=5 срок simple равен 3 в подготовленных данных, а source healingTime остаётся 0. На standalone Item без Actor остаётся исходный срок; вызов heal при начальных 0/0 может перейти к delete даже при treatment=none. При treated счётчик в памяти увеличивается раньше записи; sterilized становится true только через update. После сохранения флага следующая стерилизация не добавляет ещё два дня. Завершённая deadly-травма автоматически не удаляется, но ручной treat не проверяет степень.

Эффекты исходного Item перестают быть встроенными эффектами текущего Actor вместе с удалением Item по обычной модели владения Foundry. Отдельные уже созданные Actor.effects здесь не ищутся и не удаляются. Числовое применение effects и изменение текущего HP находятся вне этого файла.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Схема и сроки | Настоящая CriticalWoundData + TypeDataModel/fields; родители — DataModel-фасады | 9 полей; BODY=5 → 3/7/10; BODY=20 → минимум 1; deadly/unknown сохраняют заданные 99; standalone=0 | Не полный client Item/Actor |
| Заживление | Исходный heal; update/delete перехвачены | none/stabilized дают update({}); treated без прежней стерилизации +3; после сохранения флага следующий день +1; deadly сохраняется | Имитировано завершение сохранения флага, затем снова prepareDerivedData |
| Переходы/ошибки | treat с pending create/delete и fromUuid-фасадом | Метод возвращается при незавершённых записях; null передан как [null], delete вызван; rejected resolve останавливает удаление; без Actor TypeError | Не утверждается факт потери реального Item в мире |
| Типы и текст | Настоящая очистка NumberField и настоящий createEnrichedText | '2.5'→2.5, отрицательный healingTime допустим; описание получает system.description | TextEditor возвращал маркер; ссылки HTML не разрешались |

## Непроверенные участки и открытые вопросы

Полностью прочитаны все 107 строк. Жизненный цикл client Item, успешная запись followUp с эффектами, отказ серверных hooks, повторные клики/гонки и реальные компедиумы не запускались. Документ-ссылка может вести на любой Item; необходимость ограничения подтипом требует отдельного решения. Числа длительности описывают код, их соответствие рулбуку не оценивалось.

## Связанные проблемы

[issue-00121](../../../../../../issues/potential/issue-00121.md), [issue-00122](../../../../../../issues/potential/issue-00122.md), [issue-00127](../../../../../../issues/potential/issue-00127.md). Неожидаемое завершение операций, отсутствие проверки результата перехода и условия окончания заживления. Регистрация не означает подтверждение или исправление.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `b09f992960a76d1c75946f402e42d93fa0785008`; полный файл | Первая карточка; [сверка порции и второй серии](../../../../review-log.md#task-0003020) |

## Уточнение TASK-0003.025

2026-09-11, `rusbar-main`, `a2670a0a10c62b28d836b1a57577c4836f14cf20`. В реальном _prepareItems общего V2 await Promise.all вызывает system.enrichedText у всех document.itemTypes.criticalWound, затем context.criticalWounds[uuid]=description. Проверены value/enriched/systemField и распространение отказа enrich. V1 этого шага не имеет; его getData не используется текущими Character/Monster. Обогащение не изменяет source и не создаёт эффекты/changes.

Общие определения: [module/actor/sheets/WitcherActorSheet.js](../../../../../../../module/actor/sheets/WitcherActorSheet.js) и [module/actor/sheets/WitcherActorSheetV1.js](../../../../../../../module/actor/sheets/WitcherActorSheetV1.js). [Методика и перекрёстная сверка](../../../../review-log.md#task-0003025). Это точечное уточнение связей; полный разбор новых соседних файлов не засчитывается.
