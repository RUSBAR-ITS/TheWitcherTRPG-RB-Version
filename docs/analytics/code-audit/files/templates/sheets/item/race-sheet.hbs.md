# templates/sheets/item/race-sheet.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/sheets/item/race-sheet.hbs](../../../../../../../templates/sheets/item/race-sheet.hbs) |
| Тип файла | Handlebars, HTML-шаблон |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `29319a7a7e1dfc0663edbc15166f3b6a19682a2f` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.018](../../../../../../tasks/task-0003.018.md), одна порция из восьми файлов |
| Запись перекрёстной сверки | [TASK-0003.018](../../../../review-log.md#task-0003018) |

## Актуализация N01–N08 — 14.3.1.00010

2026-09-16, dev, база aeb527c6e6402e8a5f940a2c3ad0020d7e5b35e4. Отображаемые placeholder/tooltip используют `WITCHER.Name`. Привязки name/data-field, классы действий, условия шаблона и введённые имена сохранены.

[Реализация и адресные проверки](../../../../../../issues/closed/issue-00330.md#реализация-n01n08--143100010). Датированные разборы ниже сохраняют результаты прежних срезов.


## Назначение файла

Основная форма расы: имя и картинка Item, источник, четыре особенности с HTML-редакторами и таблица социального положения по регионам.

## Условия использования

Подключается только через WitcherRaceSheet.PARTS.main. Контекст готовит WitcherItemSheet с RaceData.enrichedText. Кнопка configureItem открывает отдельную конфигурацию; editor-функции самой формы не объявлены.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| section.{{item.type}}.scrollable / header.sheet-header | HTML,1–22 | Корневая часть/шапка | item.type/name/img; showConfig | Прямой HBS, не include общего item-header |
| input name / input system.sourcebook | 3–5/17 | Имя Item и источник | Текстовые именованные поля | Сохраняет внешний обработчик формы |
| configureItem / editImage | data-action6/10 | Настройка Item и изменение картинки | Действия предков | img также data-edit='img' |
| Четыре .perk блока | 26–44 | Имя и описание каждой особенности | system.perkN.name; formGroup enrichedText.perkN.* | 4 строки имени +4 HTML-входа |
| Пять select регионов | 46–81 | north,nilfgaard,skellige,dolBlathanna,mahakam | system.socialStanding.<region>, config.socialStanding | У каждого собственный id; данные целевого Item |

## Основные функции и методы

Программных функций/классов нет. formGroup получает настоящий HTMLField, value с исходным текстом, enriched с обработанным HTML и toggled=true. selectOptions использует один справочник 6 значений с selected для каждого региона и localize=true. if showConfig контролирует шестерёнку.

Форма не содержит общего system.description, полей quantity/weight/cost/flags, кнопок добавления/удаления слотов perk или changes эффектов. Это граница имеющегося UI, а не утверждение о необходимости удалить соответствующие данные.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| PARTS.main | [module/item/sheets/WitcherRaceSheet.js](../../../../../../../module/item/sheets/WitcherRaceSheet.js) | Подключение | 9–14 | Полная карточка листа |
| item/config/enrichedText/showConfig; configureItem | [module/item/sheets/WitcherItemSheet.js](../../../../../../../module/item/sheets/WitcherItemSheet.js) | Контекст/действие | _prepareContext и _renderConfigureDialog | Настоящий контекст и прямой handler проверены |
| perk1–4, socialStanding, sourcebook | [module/data/item/raceData.js](../../../../../../../module/data/item/raceData.js) | Схема/данные | Все именованные поля | 13 полей модели, 4 результата helper |
| name/description особенности; регионы | [module/data/item/templates/perkData.js](../../../../../../../module/data/item/templates/perkData.js); [module/data/item/templates/socialStandingData.js](../../../../../../../module/data/item/templates/socialStandingData.js) | Вложенные определения | 4 пары и 5 регионов | Фабрики и регистр ключей сверены |
| config.socialStanding | [module/setup/config.js](../../../../../../../module/setup/config.js) | selectOptions | 58/63/68/73/78 | 6 вариантов; строки arbitrary допустимы схемой, но не входят в options |
| WITCHER.Item.SourceBook / Actor.Perks / socialStanding.<region> | [lang/en.json](../../../../../../../lang/en.json); [lang/ru.json](../../../../../../../lang/ru.json) | localize | Заголовки/подписи | 7 буквальных ключей и 6 значений справочника найдены; полный итог порции 39 ключей |
| formGroup/selectOptions/HTMLField→prose-mirror | Foundry 14.367.0, /opt/foundryvtt/client/applications/handlebars.mjs и /opt/foundryvtt/common/data/fields.mjs | Helpers/создание элемента | 4 поля HTML и 5 select | Helpers, optionGroups и DataField.toInput настоящие; ProseMirror/DOM заменены |
| editImage / обработка именованных полей | Foundry 14.367.0, /opt/foundryvtt/client/applications/api/document-sheet.mjs | Внешние действия/submit | data-action и name | Декларация стандартного действия и _processFormData/_prepareSubmitData прочитаны; реальный submit не исполнялся |
| .perk .editor-content; .perk | [styles/race-sheet.css](../../../../../../../styles/race-sheet.css); [styles/system-styles.css](../../../../../../../styles/system-styles.css) | CSS | Высота 150px у editor-content, margin5px у perk | Прочитаны связанные селекторы; соответствие реальному DOM ProseMirror/внешний вид не тестировались |
| item.img | Ресурс Document Item | Изображение | img.src/title | Загрузка изображения не выполнялась; assets исключены из исследования |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/item/sheets/WitcherRaceSheet.js](../../../../../../../module/item/sheets/WitcherRaceSheet.js) | Основная HBS-часть | PARTS.main | Единственная найденная ссылка на путь шаблона в module/templates |

Область поиска: текущие module/ и templates/; регистрации сверены отдельно. Динамические обращения внешних модулей не исследовались.

## Данные и изменения состояния

Сама разметка не сохраняет данные и не создаёт эффекты. В итоговом HTML15 именованных элементов: name,sourcebook,4 имени,4 описания и 5 социальных select. editImage — действие над документом; изображение не является текстовым input. Источником description каждого perk служит отдельный объект enrichedText, source остаётся неизменным.

У пустых регионов нет явно выбранного option и нет blank option в вызове selectOptions. Конкретное визуальное значение select определяется браузером и не утверждается по фасаду. При hated/equal исходные выбранные ключи верно переданы optionGroups. Неизвестное значение не становится choices-ограничением модели.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Охват/пути | 84 строки, весь HBS; реальная RaceData/ItemSheet | 15 имён соответствуют Item/schema; data-actions configureItem/editImage | Проверен итог рендера и контекст, не browser submit |
| HTML | Настоящий formGroup/HTMLField.toFormGroup/toInput | 4 входа system.perkN.description; свои value/enriched, toggled=true; общее description отсутствует | HTMLProseMirrorElement.create — фасад, настоящий редактор не запускался |
| Варианты выбора | Настоящие selectOptions/prepareSelectOptionGroups | 5 списков по 6 options; явные selected hated/equal соответствуют двум заданным регионам | DOM-обёртка/добавление options в настоящий select не проверены |
| Действия/эффекты | Сверка предков и ConfigSheet | Отдельная конфигурация доступна и посылает createEmbeddedDocuments | Нет изменений документов в тесте |

## Непроверенные участки и открытые вопросы

В TASK-0004.008 текущий файл и его связи сопоставлены с датированными протоколами TASK-0003.018/.019 (2026-09-10) и .038 (2026-09-11), в пределах относящихся к нему сценариев. Новых поведенческих запусков нет; прежние настоящие модели/методы и фасады различены в протоколе. Браузерный submit, мир, сеть и запись в БД не проверены. Установлены процессы R008-02, R008-05, R008-20; оставшиеся границы: [U008-01](../../../../cross-check-0002.md#u008-01), [U008-06](../../../../cross-check-0002.md#u008-06), [U008-07](../../../../cross-check-0002.md#u008-07). Полный пофайловый разбор соседей в TASK-0003 не равен проверке клиентского lifecycle.

## Связанные проблемы

[issue-00109](../../../../../../issues/potential/issue-00109.md), [issue-00013](../../../../../../issues/potential/issue-00013.md). Этот Item-шаблон передаёт enriched корректно. 109 относится к другому отображению той же расы на Actor-листе;13 сопоставлена как контроль правильного контракта HTML, а не ошибка данной формы.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.018 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.

## Сквозная сверка TASK-0004.008

2026-09-14; rusbar-main, f96434101e0e827838c2e6a3e09da8933a9801ef. Исходник совпадает со срезом TASK-0001; изменено только описание.

Пятнадцать именованных полей включают имя Item, sourcebook, четыре name/description и пять регионов. Четыре formGroup получают enriched; встроенных числовых бонусов из perk или смены Actor.socialStanding в HBS нет.

Сопоставленные определения и потребители: [module/item/sheets/WitcherRaceSheet.js](../../../module/item/sheets/WitcherRaceSheet.js.md), [module/item/sheets/WitcherItemSheet.js](../../../module/item/sheets/WitcherItemSheet.js.md), [module/data/item/raceData.js](../../../module/data/item/raceData.js.md), [module/data/item/templates/perkData.js](../../../module/data/item/templates/perkData.js.md), [module/data/item/templates/socialStandingData.js](../../../module/data/item/templates/socialStandingData.js.md), [module/setup/config.js](../../../module/setup/config.js.md), [lang/en.json](../../../lang/en.json.md), [lang/ru.json](../../../lang/ru.json.md), [styles/race-sheet.css](../../../styles/race-sheet.css.md), [styles/system-styles.css](../../../styles/system-styles.css.md).

[Протокол и границы](../../../../review-log.md#task-0004008) — TASK-0004.008; процессы [R008-02](../../../../cross-check-0002.md#r008-02), [R008-05](../../../../cross-check-0002.md#r008-05), [R008-20](../../../../cross-check-0002.md#r008-20). В этой порции выполнена статическая сверка; прежние опыты сохраняют свои даты и фасады. Новых поведенческих запусков нет; браузер, мир, сеть и запись в БД не запускались.
