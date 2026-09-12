# module/item/sheets/WitcherRaceSheet.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/item/sheets/WitcherRaceSheet.js](../../../../../../../module/item/sheets/WitcherRaceSheet.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `29319a7a7e1dfc0663edbc15166f3b6a19682a2f` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.018](../../../../../../tasks/task-0003.018.md), одна порция из восьми файлов |
| Запись перекрёстной сверки | [TASK-0003.018](../../../../review-log.md#task-0003018) |

## Назначение файла

Специализированный лист расы: выбирает основной HBS и ширину окна, а подготовку контекста, настройку Item и действия наследует от WitcherItemSheet.

## Условия использования

Default class WitcherRaceSheet extends WitcherItemSheet. registerSheets регистрирует Items.registerSheet('witcher',WitcherRaceSheet,{makeDefault:true,types:['race']}). При импорте определяется класс; экземпляр создаётся при открытии Item нужного типа. Собственных обработчиков событий и переопределений контекста нет.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| WitcherRaceSheet | Класс,3–15 | Специализация общего Item-листа | Default export; makeDefault для race | Два static-реестра |
| DEFAULT_OPTIONS.position.width | Static object,4–8 | Ширина 600 | Дополнение конфигурации Application | Другие настройки поступают от предков |
| PARTS.main | Static object,9–14 | Шаблон и scrollable:[''] | template systems/TheWitcherTRPG/templates/sheets/item/race-sheet.hbs | HandlebarsApplicationMixin обслуживает часть |

## Основные функции и методы

Собственных функций, конструкторов и методов здесь нет. Унаследованный _prepareContext задаёт config,item,data,systemFields,enrichedText,showConfig; configuration создаётся как WitcherConfigurationSheet того же Item. _renderConfigureDialog открывает его. Обычные именованные поля формы обслуживает DocumentSheetV2. DEFAULT_OPTIONS/PARTS — декларации, не вызовы рендера.

enrichedText определяется RaceData и содержит четыре особенности. Основная форма имеет name/sourcebook, четыре имени/HTML и пять региональных select. editImage приходит из DocumentSheetV2, configureItem — из WitcherItemSheet.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| WitcherItemSheet | [module/item/sheets/WitcherItemSheet.js](../../../../../../../module/item/sheets/WitcherItemSheet.js) | Import/extends | 1,3 | Контекст, configuration, действия/формы, drag/drop наследуются; исходник сверён |
| RaceData | [module/data/item/raceData.js](../../../../../../../module/data/item/raceData.js) | Данные через Item.system | Унаследованный _prepareContext | Настоящая модель/контекст проверены; прямого импорта модели в листе нет |
| Основной шаблон | [templates/sheets/item/race-sheet.hbs](../../../../../../../templates/sheets/item/race-sheet.hbs) | PARTS | 11 | Путь существует и полностью разобран |
| WitcherConfigurationSheet | [module/item/sheets/configurations/WitcherConfigurationSheet.js](../../../../../../../module/item/sheets/configurations/WitcherConfigurationSheet.js) | Через свойство базового листа | configuration и showConfig | Общая general вкладка пуста для этих схем, ActiveEffect-действия доступны |
| ItemSheetV2 / HandlebarsApplicationMixin / DocumentSheetV2 | Foundry 14.367.0, client/applications/sheets/item-sheet.mjs, api/handlebars-application.mjs, api/document-sheet.mjs | Внешние предки | Рендер, разбор частей, поля формы, стандартные действия | В изоляции настоящий ItemSheetV2/HBM поверх DocumentSheet-фасада; полный Application lifecycle не запускался |
| config.socialStanding | [module/setup/config.js](../../../../../../../module/setup/config.js) | Через общий контекст | selectOptions собственного HBS | 6 вариантов проверены; контекст не создаёт новый справочник |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/setup/registerSheets.js](../../../../../../../module/setup/registerSheets.js) | WitcherRaceSheet | Импорт/регистрация типа race | Регистрация 83–87 |
| [module/actor/sheets/mixins/itemMixin.js](../../../../../../../module/actor/sheets/mixins/itemMixin.js) | item.sheet.render(true) | _onItemEdit147–154 по выбранному Item | Класс выбирает зарегистрированная Foundry sheet-конфигурация, не сам callback |

Область поиска: текущие module/ и templates/; регистрации сверены отдельно. Динамические обращения внешних модулей не исследовались.

## Данные и изменения состояния

Сам файл не изменяет Item, Actor, эффекты или настройки мира. При вызове общего _prepareContext к this.options.classes добавляется item-race — это поведение предка. configuration — отдельное приложение для того же документа, не отдельный Item. Настройка ActiveEffect хранится в Item.effects; она не кодируется в perk1–perk4.

Настоящая onManageActiveEffect(create) отправила запрос createEmbeddedDocuments('ActiveEffect',[{type:'base',name:item.name,icon:item.img,origin:item.uuid,duration:{value:null},disabled:false}]) для passive-категории. Запись заменена перехватом. Наличие формы не означает, что созданный эффект уже имеет changes или действует на Actor; перенос и применение зависят от настроек самого эффекта.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Весь класс | 15 строк, один import,2 static-свойства | Ширина 600, один PARTS.main, собственных методов нет | Инициализация всех merged options Application не проверена в браузере |
| Контекст и шестерёнка | Настоящие WitcherRaceSheet/WitcherItemSheet с DocumentSheet-фасадом | showConfig=true; configuration=WitcherConfigurationSheet; прямой вызов _renderConfigureDialog открыл её один раз | Не браузерный клик |
| Данные | Настоящая модель race | 4 enriched записи с system.perkN.description | TextEditor/элементы DOM подменены |
| Конфигурация/ActiveEffect | Настоящие _prepareContext/onManageActiveEffect; general HBS | В general — 0 именованных полей;4 категории effects; один запрос создания base | БД/разрешения клиента не проверены |

## Непроверенные участки и открытые вопросы

Файл прочитан полностью. Источники унаследованного поведения имеют собственные карточки; общие найденные ранее ограничения drop/ожидания не воспроизводились здесь повторно. Системные классы листов настоящие, DocumentSheet/DOM — фасады. Полный UI, редактирование изображения, submit, сохранение эффекта и внешние модули не запускались.

## Связанные проблемы

[issue-00005](../../../../../../issues/potential/issue-00005.md), [issue-00058](../../../../../../issues/potential/issue-00058.md), [issue-00059](../../../../../../issues/potential/issue-00059.md). 5 сопоставлена: тип race объявлен. 58/59 — ранее описанные ограничения унаследованного drop в WitcherItemSheet; новых ID для наследования не создаётся.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.018 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.

## Дополнительная сверка TASK-0003.047

2026-09-12, rusbar-main, 2f94c6c29e298ccf73d67ccc2e5fb8fc358dae2c; исходники не изменены.

[race-sheet.css](../../../styles/race-sheet.css.md) содержит один глобальный .perk .editor-content {height:150px}, а не размеры всего окна. Ширина 600 остаётся DEFAULT_OPTIONS этого класса. Группа 14 получила четыре .perk и четыре prose-mirror через фасад formGroup; группа 15 исполнила настоящий HTMLProseMirrorElement._buildElements на фасаде базового DOM: он создал div.editor-content. Поэтому отсутствие этого класса буквально в HBS не доказывает неиспользование стиля. Тот же CSS адресует расу на Character; сохранение rich text не запускалось.

[Сценарии, результаты и ограничения](../../../../review-log.md#task-0003047). Связанные файлы повторно не засчитываются в покрытие.
