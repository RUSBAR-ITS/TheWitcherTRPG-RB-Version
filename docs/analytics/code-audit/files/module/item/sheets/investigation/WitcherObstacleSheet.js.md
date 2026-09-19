# module/item/sheets/investigation/WitcherObstacleSheet.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/item/sheets/investigation/WitcherObstacleSheet.js](../../../../../../../../module/item/sheets/investigation/WitcherObstacleSheet.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-16: актуализация технических обращений по issue-00001 |
| Ветка и коммит | `dev`, база `d8e0e1ad1159cb71a8769b0353f812de6f1ed4d8` + незакоммиченное исправление issue-00001 |
| Изменения относительно коммита | issue-00001; текущие технические обращения актуализированы. Прежние опыты ниже относятся к своим датам. |
| Задача и порция | [TASK-0003.023](../../../../../../../tasks/task-0003.023.md), 14 файлов, 449 логических строк |
| Запись перекрёстной сверки | [TASK-0003.023](../../../../../review-log.md#task-0003023) |

Актуализация [issue-00001](../../../../../../../issues/closed/issue-00001.md), 2026-09-16: Обращения к ресурсам и/или техническим namespaces переведены на TheWitcherTRPG-RB-Version. Формулы и порядок действий сохранены. Датированные проверки ниже выполнены до смены ID.

## Назначение файла

Лист отдельного Item obstacle на API ApplicationV1. Добавляет словарь навыков к базовому контексту и выбирает специализированный шаблон.

## Условия использования

registerSheets импортирует класс и регистрирует для Item.obstacle с makeDefault:true. Наследует foundry.appv1.sheets.ItemSheet непосредственно; WitcherItemSheet V2 не участвует. Отсутствие типа в манифесте рассматривается отдельно от существования класса.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| WitcherObstacleSheet | default class, 1–30 | Редактор obstacle | Items.registerSheet | Настройки/получение данных |
| defaultOptions | static getter, 3–16 | classes; 520×480; tabs; dragDrop | ApplicationV1 | Слияние с super.defaultOptions |
| template | getter, 18–20 | Путь obstacle-sheet.hbs | ItemSheet V1 | Читается при рендере |
| skills | getData:26 | CONFIG.WITCHER.skillMap | Контекст HBS | Добавляется к данным super |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| static get defaultOptions() | super.defaultOptions | Слитый объект | mergeObject; tabs .sheet-tabs/.sheet-body initial description; dragSelector '.items-list .item', dropSelector null | Названных контейнеров tabs/dragDrop в текущем HBS нет |
| get template() | Без аргументов | systems/TheWitcherTRPG-RB-Version/templates/sheets/investigation/obstacle-sheet.hbs | Возвращает строку | Нет записи |
| getData() | Базовый ItemSheet V1 | Контекст с item/document и skills | Синхронный super.getData(); добавляет skills | Собственных activateListeners, update, обработчика multi-select нет |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| ItemSheet / mergeObject | Foundry 14.367.0, client/appv1/sheets/item-sheet.mjs:62–66; utils.mergeObject | Наследование/опции | defaultOptions/getData | Базовый getData синхронен; в проверке база фасад |
| WITCHER.skillMap | [module/setup/config.js](../../../../../../../../module/setup/config.js) | Данные через CONFIG | getData:26 | Словарь выбора навыков |
| ClueData/ObstacleData | [module/data/investigation/obstacleData.js](../../../../../../../../module/data/investigation/obstacleData.js) | Поля Item | item.system | Полная схема порции |
| obstacle-sheet.hbs | [templates/sheets/investigation/obstacle-sheet.hbs](../../../../../../../../templates/sheets/investigation/obstacle-sheet.hbs) | Путь template | getter:19 | Шаблон прочитан/скомпилирован |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/setup/registerSheets.js](../../../../../../../../module/setup/registerSheets.js) | WitcherObstacleSheet | default import; регистрация Item.obstacle | 10; 126–129 |
| [templates/sheets/investigation/obstacle-sheet.hbs](../../../../../../../../templates/sheets/investigation/obstacle-sheet.hbs) | item/cssClass/skills | Контекст getData | Сопоставлены поля и выбранные options |
| [module/actor/sheets/investigation/WitcherMysterySheet.js](../../../../../../../../module/actor/sheets/investigation/WitcherMysterySheet.js) | item.sheet.render(true) | Динамическое открытие редактора | _onItemEdit, выбор sheet зависит от регистрации |

Область поиска: module/ и templates/ текущего checkout; регистрация сверена с system.json. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Изменение системных данных делегировано базовой форме ItemSheet V1. getData не копирует system самостоятельно; item — документ, полученный от super. Опции tabs/dragDrop не создают отсутствующие элементы формы. Признаков самостоятельного CRUD или бросков в этом файле нет.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Опции и контекст | Группа 04 | 520×480, ожидаемый путь, item и skillMap сохранены, результат getData не Promise | Базовый ItemSheet заменён фасадом, API V1 проверен чтением ядра |
| Форма | Группы 04/16 | Именованные поля схемы совпали; список показывает сохранённые навыки | Браузерная отправка формы не запускалась |

## Непроверенные участки и открытые вопросы

Все 30 строк прочитаны. Смешение V1/V2 не объявлено новой проблемой. Тип/создание — [U015-01](../../../../../cross-check-0002.md#u015-01); реальная форма/multi-select — [U015-02](../../../../../cross-check-0002.md#u015-02); сохранение — [U015-03](../../../../../cross-check-0002.md#u015-03); внешний запуск/применение последствий — [U015-08](../../../../../cross-check-0002.md#u015-08).

## Связанные проблемы

[issue-00005](../../../../../../../issues/closed/issue-00005.md). Регистрация листа для типа вне манифеста; отдельная ошибка синхронного getData не обнаружена.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `538dbac9bb9432c123fe4f3c00ab788b58517afb`; полный файл | Первая карточка; [сверка порции](../../../../../review-log.md#task-0003023) |

## Сквозная сверка TASK-0004.015

2026-09-14; rusbar-main, 7e0d53944f3089cd61667670377aa6770fabc8cf. Исходник совпадает со срезом TASK-0001; изменено только описание.

Регистрация ведёт к самостоятельному core ItemSheet V1; общий WitcherItemSheet V2 не наследуется. template/getData подают obstacle-sheet и skillMap; super.getData синхронен в прочитанном ядре. Данные сохраняются named form, а inline MysterySheet — отдельный consumer того же Item. Настройки tabs/dragDrop сами не создают отсутствующие в HBS элементы. В классе нет метода броска или применения successDamage/failDamage.

Сопоставленные определения и потребители: [module/data/investigation/obstacleData.js](../../../data/investigation/obstacleData.js.md), [templates/sheets/investigation/obstacle-sheet.hbs](../../../../templates/sheets/investigation/obstacle-sheet.hbs.md), [module/actor/sheets/investigation/WitcherMysterySheet.js](../../../actor/sheets/investigation/WitcherMysterySheet.js.md), [module/setup/registerSheets.js](../../../setup/registerSheets.js.md), [module/setup/config.js](../../../setup/config.js.md).

[Протокол и границы](../../../../../review-log.md#task-0004015) — TASK-0004.015; процессы [R015-01](../../../../../cross-check-0002.md#r015-01), [R015-04](../../../../../cross-check-0002.md#r015-04), [R015-14](../../../../../cross-check-0002.md#r015-14), [R015-16](../../../../../cross-check-0002.md#r015-16). В этой порции выполнена статическая сверка; прежние опыты сохраняют свои даты и фасады. Новых поведенческих запусков нет; браузер, мир, сеть и запись в БД не запускались.
