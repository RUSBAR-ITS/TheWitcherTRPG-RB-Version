# module/actor/rewardsSheet.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/actor/rewardsSheet.js](../../../../../../module/actor/rewardsSheet.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `639fde4bad4a7ba4c538d3b08ddc5cfd846ca75e` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.037](../../../../../tasks/task-0003.037.md), 8 файлов, 313 логических строк |
| Запись перекрёстной сверки | [TASK-0003.037](../../../review-log.md#task-0003037) |

## Назначение файла

Отдельное окно просмотра двух журналов персонажа: IP и валюты. Собственной выдачи, редактирования истории и пересчёта балансов здесь нет.

## Условия использования

WitcherCharacterSheet импортирует класс и создаёт rewards=new RewardsSheet({document:this.actor}); .open-rewards вызывает _renderRewards. Класс прямо наследует core ActorSheetV2 через HandlebarsApplicationMixin, не WitcherActorSheet. В registerSheets он не выбран листом по умолчанию.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| RewardsSheet | default class:4 | Окно журналов | Импорт CharacterSheet | render отдельного приложения |
| DEFAULT_OPTIONS | static:6–19 | Размер 520×480; resizable; classes witcher/extended-sheet/actor | Наследуемые опции Application | form.submitOnChange=true; closeOnSubmit=false |
| PARTS | static:21–38 | header/tabs/ip/currency | Рендер частей HBS | ip/currency scrollable:[пустая строка] |
| TABS.primary | static:40–46 | Вкладки ip/currency | initial ip; labelPrefix WITCHER.Actor.rewards | Навигация ядра |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| _prepareContext(options) | document.system; super context | Promise контекста | await super; добавляет config=CONFIG.WITCHER и system=this.document.system | Не пишет Actor; core готовит tabs; своей формы редактирования нет |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| ActorSheetV2/HandlebarsApplicationMixin | Foundry 14.367.0: client/applications/sheets/actor-sheet.mjs, api/document-sheet.mjs, api/application.mjs | Наследование | Подготовка context/tabs, render/submit | Сверены core _prepareContext/_prepareTabs; изолированное исполнение tabs |
| CONFIG.WITCHER | [module/setup/config.js](../../../../../../module/setup/config.js) | Чтение config | Для currency lookup в HBS | Присваивание context.config:51; конфигурация устанавливается main |
| CONFIG.WITCHER registration | [module/TheWitcherTRPG.js](../../../../../../module/TheWitcherTRPG.js) | Глобальная регистрация | Источник config | init |
| document.system.logs | [module/data/actor/characterData.js](../../../../../../module/data/actor/characterData.js) | Данные Actor | Источник context.system | CharacterData.logs EmbeddedDataField(Log) |
| Log.ipLog/currencyLog | [module/data/actor/templates/character/logData.js](../../../../../../module/data/actor/templates/character/logData.js) | Контекст | Массивы отображения | Нет изменений в _prepareContext |
| PARTS.header/ip/currency | [templates/sheets/actor/rewards/header.hbs](../../../../../../templates/sheets/actor/rewards/header.hbs); [templates/sheets/actor/rewards/ip.hbs](../../../../../../templates/sheets/actor/rewards/ip.hbs); [templates/sheets/actor/rewards/currency.hbs](../../../../../../templates/sheets/actor/rewards/currency.hbs) | Шаблоны | Четыре части с общей навигацией | Прямые пути21–38 |
| PARTS.tabs | Foundry 14.367.0: /opt/foundryvtt/templates/generic/tab-navigation.hbs | Внешний HBS | data-action=tab, tabs labels | Реальный HBS отрендерен |
| Локализация WITCHER.Actor.rewards | [lang/en.json](../../../../../../lang/en.json); [lang/ru.json](../../../../../../lang/ru.json) | Переводы | heading/ip/currency | expandObject + core Localization/fallback |
| .extended-sheet | [styles/character/sheet.css](../../../../../../styles/character/sheet.css); [styles/monster/sheet.css](../../../../../../styles/monster/sheet.css) | CSS | Исключает применение селекторов основного листа | Проверены селекторы :not(.extended-sheet) |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/actor/sheets/WitcherCharacterSheet.js](../../../../../../module/actor/sheets/WitcherCharacterSheet.js) | RewardsSheet | import6; field14; _renderRewards:460–462 | Открытие окна текущего Actor |
| [templates/sheets/actor/rewards/header.hbs](../../../../../../templates/sheets/actor/rewards/header.hbs) | Контекст PARTS | Шаблон заголовка | PARTS.header |
| [templates/sheets/actor/rewards/ip.hbs](../../../../../../templates/sheets/actor/rewards/ip.hbs) | system/tabs.ip | Шаблон журнала IP | PARTS.ip |
| [templates/sheets/actor/rewards/currency.hbs](../../../../../../templates/sheets/actor/rewards/currency.hbs) | system/config/tabs.currency | Шаблон валютного журнала | PARTS.currency |

Область поиска: module/ и templates/ текущего checkout; прямые импорты и места вызова сверены отдельно от динамических обращений. Типы и листы сверены с system.json, module/setup/registerDataModels.js и module/setup/registerSheets.js. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Контекст содержит system по ссылке и общий config. Core context включает document/model/source/editable/user; ActorSheetV2 не обязан задавать ключ actor, собственным HBS он не нужен. Отдельных _onSubmit/update действий класс не определяет. Во всех своих HBS нет input/select/textarea/name; generic tabs содержит ссылки, а не поля записи. Поэтому submitOnChange не превращает журнал в редактор. Нет удаления, сортировки, итоговой суммы, пересчёта баланса или даты записи.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Контекст/4PARTS | Группа20; настоящие core tabs и все HBS | ip active; currency.cssClass отсутствует до выбора; FormDataExtended даёт {} | Фасад базового листа; нативный render не запускался |
| История | Группы21–22 | Сохранён порядок, тип и bool; изменение массива не меняет баланс | Изменение модели памяти отдельно от сервера |

## Непроверенные участки и открытые вопросы

Файл прочитан целиком. Изолированные вызовы исполняют настоящий код, модели и Handlebars 4.7.9 на Foundry 14.367.0 / Node 24.16.0; Application, DOM и Actor.update/ChatMessage.create — фасады. Браузерное отображение/валидация, доступ службы по HTTP, серверные права, БД и несколько клиентов не проверялись. Реальные макросы миров и сторонние модули не исследовались.

## Связанные проблемы

[issue-00028](../../../../../issues/potential/issue-00028.md), [issue-00030](../../../../../issues/potential/issue-00030.md), [issue-00202](../../../../../issues/potential/issue-00202.md). Это связанные маршруты записи, неподходящая IP-вкладка монстра и повреждённая ссылка открытия в Character header. Собственная новая ошибка окна не зарегистрирована.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `639fde4bad4a7ba4c538d3b08ddc5cfd846ca75e`; полный файл | Первая карточка; [сверка порции](../../../review-log.md#task-0003037) |
