# module/actor/sheets/mixins/criticalWoundMixin.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/actor/sheets/mixins/criticalWoundMixin.js](../../../../../../../../module/actor/sheets/mixins/criticalWoundMixin.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `b09f992960a76d1c75946f402e42d93fa0785008` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.020](../../../../../../../tasks/task-0003.020.md), 10 файлов, 428 логических строк |
| Запись перекрёстной сверки | [TASK-0003.020](../../../../../review-log.md#task-0003020) |

## Назначение файла

Действия листа Actor: создать критическую травму и вызвать переход по кнопке лечения; регистрация DOM-слушателей.

## Условия использования

Named export criticalWoundMixin присоединяется Object.assign к WitcherActorSheet и WitcherActorSheetV1. Их activateListeners вызывают criticalWoundListener. Современные CharacterSheet/MonsterSheet наследуют базовый лист и включают tab-effects. Импорт не регистрирует слушателей сам.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| criticalWoundMixin | Экспортируемый объект, 1–32 | Три метода примеси | Object.assign к прототипам листов | Работает с this.actor |
| Слушатели click | 19–30 | Маршрутизация трёх CSS-селекторов | На каждый найденный DOM-элемент | Замыкания вызывают методы в контексте листа; снятия слушателей в файле нет |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| _onCriticalWoundAdd(event):2–10 | Лист Actor; event.preventDefault | Promise<void> | Создаёт Item с type='criticalWound', локализованным name | createEmbeddedDocuments не await/return; system/effects/img не задаёт |
| _onTreat(event):12–17 | event.target.dataset.id — UUID | Promise<void> | preventDefault; fromUuidSync; crit.system.treat() | Нет проверки UUID или документа; treat не await/return; treatment не изменяется здесь |
| criticalWoundListener(html):19–31 | DOM-элемент с querySelectorAll | void | Привязывает add-crit, delete-crit и [data-action=treatCriticalWound] | delete-crit вызывает отсутствующий _onCriticalWoundRemove; сам такой элемент в текущих templates не найден |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| CriticalWoundData.treat | [module/data/item/criticalWoundData.js](../../../../../../../../module/data/item/criticalWoundData.js) | Динамический вызов | 16; замена/удаление Item | Модель разобрана полностью; treat не означает просто установить treated |
| Разметка действий | [templates/sheets/actor/partials/character/tab-effects.hbs](../../../../../../../../templates/sheets/actor/partials/character/tab-effects.hbs) | DOM-контракт | add-crit и data-action/data-id | Кнопка добавления и две области вывода лечения |
| data-id UUID / data-item-id | [templates/partials/crit-wounds-table.hbs](../../../../../../../../templates/partials/crit-wounds-table.hbs) | DOM-контракт | Кнопка treat | Лечение берёт uuid, inline-edit соседа — локальный item.id |
| fromUuidSync; createEmbeddedDocuments; game.i18n.localize | Foundry 14.367.0; DOM addEventListener | Внешнее разрешение UUID/создание/локализация | 4–16, 20–29 | Запись и UUID перехвачены в опыте |
| TYPES.Item.criticalWound | [lang/en.json](../../../../../../../../lang/en.json); [lang/ru.json](../../../../../../../../lang/ru.json) | Локализация | 6 | Ключ присутствует в обеих локализациях |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/actor/sheets/WitcherActorSheet.js](../../../../../../../../module/actor/sheets/WitcherActorSheet.js) | criticalWoundMixin; criticalWoundListener | import 2, вызов 241, Object.assign 318 | Текущий V2 лист |
| [module/actor/sheets/WitcherActorSheetV1.js](../../../../../../../../module/actor/sheets/WitcherActorSheetV1.js) | criticalWoundMixin; criticalWoundListener | import 2, вызов html[0] 219, Object.assign 298 | Совместимый старый класс; его фактический выбор листом не устанавливался |
| [templates/sheets/actor/partials/character/tab-effects.hbs](../../../../../../../../templates/sheets/actor/partials/character/tab-effects.hbs) | _onCriticalWoundAdd / _onTreat через CSS | Кнопки вкладки Character/Monster | Обработчик назначения лечения один на каждую найденную кнопку |

Область поиска: module/ и templates/ текущего checkout; регистрация сверена с system.json. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Создание вручную не делает проверку получения повторной травмы и не ищет существующий Item. Переходы лечения полностью делегированы модели. Слушатель .delete-crit — незадействованная ветвь в проверенной разметке; обычное удаление Item остаётся контекстному меню. Смешивать её с кнопкой treat нельзя.

В _onTreat используется target, а не currentTarget: тест без dataset.id дал TypeError. В текущей кнопке только текст/пробелы, вложенного значка нет; реальная ошибка по клику на вложенный элемент этой разметкой не доказана. Дублирование строк из issue-00054 не доказывает два вызова treat от одного клика.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Действия | Настоящая примесь с записью/UUID-фасадами | Добавление передало name/type; лечение вызвало system.treat один раз | Не создавались документы |
| Слушатели и крайние входы | DOM-фасад querySelectorAll/addEventListener | 3 селектора; отсутствующий id → TypeError; вызов искусственной delete-crit → отсутствующий метод | Живой потребитель delete-crit не найден, отдельная проблема по этой ветви не заведена |
| Кнопки/таблица | Рендер исходного tab-effects/partial | На один Item две строки и две treat-кнопки | Повторённая разметка, не два документа |

## Непроверенные участки и открытые вопросы

Все 32 строки прочитаны. Браузерный порядок событий, перерисовка листа, повторные клики и разрешение UUID компедиума не проверялись. Отсутствующий _onCriticalWoundRemove описан как незавершённая ветвь без найденного текущего DOM-входа.

## Связанные проблемы

[issue-00054](../../../../../../../issues/potential/issue-00054.md), [issue-00121](../../../../../../../issues/potential/issue-00121.md), [issue-00127](../../../../../../../issues/potential/issue-00127.md). Повторный вывод уже зарегистрирован ранее; операции перехода и завершение Promise разобраны в этой порции.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `b09f992960a76d1c75946f402e42d93fa0785008`; полный файл | Первая карточка; [сверка порции и второй серии](../../../../../review-log.md#task-0003020) |

## Уточнение TASK-0003.025

2026-09-11, `rusbar-main`, `a2670a0a10c62b28d836b1a57577c4836f14cf20`. Оба общих листа копируют criticalWoundMixin через Object.assign и вызывают criticalWoundListener с DOM. Селекторы — .add-crit, .delete-crit и data-action=treatCriticalWound. V2 заранее ждёт enrichedText каждой травмы и кладёт description по UUID в context.criticalWounds; сами Item не преобразуются. Дубли строк tab-effects остаются issue-00054; этот поток лишь даёт обогащённое описание.

Общие определения: [module/actor/sheets/WitcherActorSheet.js](../../../../../../../../module/actor/sheets/WitcherActorSheet.js) и [module/actor/sheets/WitcherActorSheetV1.js](../../../../../../../../module/actor/sheets/WitcherActorSheetV1.js). [Методика и перекрёстная сверка](../../../../../review-log.md#task-0003025). Это точечное уточнение связей; полный разбор новых соседних файлов не засчитывается.
