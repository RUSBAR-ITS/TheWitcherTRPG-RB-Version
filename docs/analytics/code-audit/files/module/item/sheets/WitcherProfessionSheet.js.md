# module/item/sheets/WitcherProfessionSheet.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/item/sheets/WitcherProfessionSheet.js](../../../../../../../module/item/sheets/WitcherProfessionSheet.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `c26eb64dd54cc434087f54c3c6b678b6092b15a2` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.019](../../../../../../tasks/task-0003.019.md), одна порция из двенадцати файлов |
| Запись перекрёстной сверки | [TASK-0003.019](../../../../review-log.md#task-0003019) |

## Назначение файла

Основной лист профессии: шаблон, специальная конфигурация, список обычных навыков и варианты характеристик.

## Условия использования

Default export класса с фактическим именем WitcheProfessionSheet (без r). registerSheets импортирует default под именем WitcherProfessionSheet и регистрирует тип profession; различие локальных имён не мешает импорту. Наследует WitcherItemSheet.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| WitcheProfessionSheet | Класс 4–35 | Специализация Item-листа | Default export; makeDefault profession | Один собственный метод |
| DEFAULT_OPTIONS.position.width | Static5–9 | Ширина 600 | Дополнение параметров предков | Полное слияние Application не моделировалось |
| configuration | Поле 11 | WitcherProfessionConfigurationSheet | document:this.item | После базовой инициализации заменяет общую конфигурацию специализированной |
| PARTS.main | Static13–18 | Основной шаблон | profession-sheet.hbs; scrollable:[''] | Других собственных частей нет |
| professionSkills / config.statOptions | Контекст 23–31 | Варианты выбора | 52 обычных навыка и 9 характеристик | statOptions записывается в общий CONFIG.WITCHER |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| async _prepareContext(options):21–34 | Контекст WitcherItemSheet/CONFIG.WITCHER | Расширенный context | super; Object.values(skillMap)→{value:name,label}; statTypes без none→statOptions | Ждёт super/enrichedText. context.config — ссылка на CONFIG.WITCHER, поэтому statOptions изменяет общий объект в памяти, не настройки мира |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| WitcherItemSheet | [module/item/sheets/WitcherItemSheet.js](../../../../../../../module/item/sheets/WitcherItemSheet.js) | Import/extends | 1/4/22 | Контекст, стандартные действия и формы |
| WitcherProfessionConfigurationSheet | [module/item/sheets/configurations/WitcherProfessionConfigurationSheet.js](../../../../../../../module/item/sheets/configurations/WitcherProfessionConfigurationSheet.js) | Import/new | 2/11 | Отдельное приложение того же Item |
| PARTS.main | [templates/sheets/item/profession-sheet.hbs](../../../../../../../templates/sheets/item/profession-sheet.hbs) | Шаблон | 15 | Путь существует и полностью разобран |
| skillMap/statTypes | [module/setup/config.js](../../../../../../../module/setup/config.js) | Global CONFIG | 23–31 | 52 навыка/10 statTypes, none исключён из 9 statOptions |
| ProfessionData | [module/data/item/professionData.js](../../../../../../../module/data/item/professionData.js) | Через Item.system | super._prepareContext | 11 enriched описаний и реальные поля |
| ItemSheetV2/HBM/DocumentSheetV2 | Foundry 14.367.0, /opt/foundryvtt/client/applications/sheets/item-sheet.mjs; client/applications/api/document-sheet.mjs; client/applications/api/handlebars-application.mjs | Внешние предки | Рендер/форма/editImage | Исполнение с фасадом DocumentSheet; действия исходников сверены |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/setup/registerSheets.js](../../../../../../../module/setup/registerSheets.js) | Default class | Импорт 17, регистрация 72–75 | types profession, makeDefault |
| [templates/sheets/item/profession-sheet.hbs](../../../../../../../templates/sheets/item/profession-sheet.hbs) | item/config/systemFields/enrichedText/professionSkills/showConfig | Основная форма | Рендер 47 полей |
| [module/item/sheets/configurations/WitcherProfessionConfigurationSheet.js](../../../../../../../module/item/sheets/configurations/WitcherProfessionConfigurationSheet.js) | CONFIG.WITCHER.statOptions | Косвенное чтение при рендере путей | После подготовки основного листа список уже установлен |
| [module/actor/sheets/mixins/itemMixin.js](../../../../../../../module/actor/sheets/mixins/itemMixin.js) | item.sheet.render(true) | Редактирование профессии с Actor | Фактический класс выбирает регистрация |

Область поиска: текущие module/ и templates/; регистрации сверены отдельно. Динамические обращения внешних модулей не исследовались.

## Данные и изменения состояния

Лист не помечает навыки Actor самостоятельно: он лишь редактирует Set professionSkills, который читает Drop в itemMixin. Базовые поля навыка и HTML доступны для definingSkill и всех путей; механические настройки находятся в configuration, где definingSkill отсутствует. Shared statOptions не является записью game.settings. Прямое создание конфигурации вне основного листа может не иметь подготовленного списка; штатный путь через лист проверен.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Контекст | Настоящие классы/модель | configuration специализирована;52 choices;9 statOptions;config===CONFIG.WITCHER | DocumentSheet-фасад |
| Форма | Handlebars/formInput/HTMLField | 47 именованных элементов,11 value/enriched/path | SetField-финальный DOM заменён регистратором |
| Список навыков | Сравнение 52 вариантов со схемой character | Все ключи присутствуют | Динамические внешние навыки не исследованы |

## Непроверенные участки и открытые вопросы

Исходник прочитан полностью. Системные классы листов настоящие, ItemSheetV2/HandlebarsApplicationMixin работают поверх DocumentSheet-фасада. Рендер проверяет контекст/поля и маршруты; реальный браузер, права, сохранение Item и работа нескольких клиентов не проверены.

## Связанные проблемы

[issue-00016](../../../../../../issues/potential/issue-00016.md), [issue-00112](../../../../../../issues/potential/issue-00112.md), [issue-00116](../../../../../../issues/potential/issue-00116.md). issue-00016 уточняется по двум отсутствующим подписям вариантов; unknown professionSkills касается импортированных/изменённых данных.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.019 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.
