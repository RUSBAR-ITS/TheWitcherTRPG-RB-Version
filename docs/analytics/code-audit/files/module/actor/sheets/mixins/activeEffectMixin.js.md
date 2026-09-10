# module/actor/sheets/mixins/activeEffectMixin.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/actor/sheets/mixins/activeEffectMixin.js](../../../../../../../../module/actor/sheets/mixins/activeEffectMixin.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `247d3d86e344238a1445377c686eb6455146693c` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.010](../../../../../../../tasks/task-0003.010.md), одна порция из восьми файлов |
| Запись перекрёстной сверки | [TASK-0003.010](../../../../../review-log.md#task-0003010) |

## Назначение файла

Группирует эффекты для листов Actor и связывает элементы списка с созданием, открытием, переключением, удалением и раскрытием описания.

## Условия использования

Mixin подключён к WitcherActorSheet и WitcherActorSheetV1. В V2 listener получает DOM html, в V1 — html[0]. this.actor — документ листа. Конфигурация Item использует собственный обработчик, а не эту примесь.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| activeEffectMixin | export let; 1–101 | Четыре метода листа | Object.assign двух классов Actor | Подготовка данных и установка DOM-слушателей |
| categories | Локальный объект prepareActiveEffectCategories | temporary/passive/inactive/temporaryItemImprovement | Контекст effects шаблона | У каждой категории type/label/effects |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| prepareActiveEffectCategories; 7–40 | Итерируемая коллекция effects | Объект четырёх групп | Сначала isDisabled; затем непереданное улучшение; затем isTemporary; иначе passive | Сохраняет ссылки/порядок; не удаляет дубликаты и не фильтрует isSuppressed |
| onManageActiveEffect; 49–77 | event, caller; ближайший li с dataset | Результат create/render/delete/update либо уведомление | create создаёт ActiveEffect; edit открывает sheet; toggle меняет disabled; delete разрешён только при parentUuid==caller.uuid | По effectId разрешает родителя fromUuidSync; отсутствующие li/UUID/эффект не защищены |
| _onActiveEffectDisplayInfo; 81–89 | event на .effect-display | Promise<undefined> | preventDefault/stopPropagation; ближайший .effect-row; jQuery .effect-description; при непустом html переключает invisible | Не пишет документ; пустое описание оставляет скрытым |
| activeEffectListener; 91–100 | DOM html | undefined | click на .effect-control → onManageActiveEffect(event,this.actor); .effect-display → раскрытие описания | Callback не возвращает результат действия; снятия/защиты повторной регистрации нет |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| isDisabled/isTemporaryItemImprovement/isAppliedTemporaryItemImprovement/isSuppressed | [module/activeEffect/witcherActiveEffect.js](../../../../../../../../module/activeEffect/witcherActiveEffect.js) | Геттеры документа | Группировка использует первые три; suppression фильтруется позднее шаблоном | isTemporary наследуется от ядра |
| DOM dataset и selectors | [templates/partials/effect-part.hbs](../../../../../../../../templates/partials/effect-part.hbs) | Контракт разметки | effectType, effectId, parentUuid, action; effect-row/description | Все действия и поля сопоставлены |
| fromUuidSync, ActiveEffect sheet/update/delete, caller.createEmbeddedDocuments | Внешний Foundry Document API | Работа с документами | Создание/переключение/открытие/удаление | Запись и разрешение UUID подменены в проверке |
| $, DOM API, game.i18n, ui.notifications | jQuery, браузер и Foundry | Слушатели и сообщения | format DOCUMENT.New, WITCHER.activeEffect.*, belongsToItem | Подписи системы: [lang/en.json](../../../../../../../../lang/en.json); [lang/ru.json](../../../../../../../../lang/ru.json) |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/actor/sheets/WitcherActorSheet.js](../../../../../../../../module/actor/sheets/WitcherActorSheet.js) | Все методы через примесь | Импорт/Object.assign; _prepareContext вызывает categories; _onRender — activeEffectListener(html) | Эффекты из allApplicableEffects плюс улучшения Item |
| [module/actor/sheets/WitcherActorSheetV1.js](../../../../../../../../module/actor/sheets/WitcherActorSheetV1.js) | Все методы через примесь | Импорт/Object.assign; getData и activateListeners(html[0]) | Наследуемые листы V1 получают эту функциональность |
| [templates/partials/effect-part.hbs](../../../../../../../../templates/partials/effect-part.hbs) | Результат categories и действия | Отображение groups, кнопок и описаний | Разметка общая с Item, обработчики Item другие |

## Данные и изменения состояния

create передаёт name=DOCUMENT.New, legacy icon='icons/svg/aura.svg', origin=caller.uuid, duration.value=1 только для temporary, иначе null; disabled=true только для inactive. type не задаётся, то есть по ядру это base. Создание источника temporaryItemImprovement на Item выполняет другой обработчик с явным type.

Удаление эффекта чужого Item из Actor-листа запрещается сообщением belongsToItem; открытие и toggle того же эффекта используют его реального родителя и не содержат такого собственного запрета. Фактические права записи дополнительно проверяет ядро. Значения характеристик здесь не пересчитываются вручную.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Полнота/регистрация | 101 строка; обе точки Object.assign и вызовы listener | 4 метода; V1 адаптирует jQuery к DOM | Полные листы вне порции |
| Категории | Четыре входных эффекта разных признаков | a→inactive, b→temporaryItemImprovement, c→temporary, d→passive | Геттеры заданы в фикстуре |
| Действия | Исходный обработчик, наблюдаемые create/render/update/delete/notification | temporary создаёт value1; edit render(true); disabled true→false; своё удаляется; чужое выдаёт ошибку | БД и права Foundry не исполнялись |
| Слушатели/описание | Исходные методы; минимальные DOM/jQuery doubles | Установлены два click-слушателя; непустое описание переключило invisible | Не браузер/повторный рендер |

## Непроверенные участки и открытые вопросы

Не проверены недействительные UUID/удалённые документы, drag/drop и реальные права нескольких клиентов. Сообщение об источнике не заменяет политику владения ядра. Отсутствующий обработчик раскрытия в Item-конфигурации относится к другому использованию общего partial.

## Связанные проблемы

[issue-00056](../../../../../../../issues/potential/issue-00056.md) — на стороне Item нет обработчика раскрытия, присутствующего здесь. Системная категоризация связана с ранее описанными геттерами; отдельных новых проблем четырём методам этой порции не назначено.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.010 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.
