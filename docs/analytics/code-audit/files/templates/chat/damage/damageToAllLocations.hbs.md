# templates/chat/damage/damageToAllLocations.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/chat/damage/damageToAllLocations.hbs](../../../../../../../templates/chat/damage/damageToAllLocations.hbs) |
| Тип файла | Handlebars |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-12 |
| Ветка и коммит | rusbar-main, 965132d5d7972a0edd73aaa62484a1b6ba15991f |
| Изменения относительно коммита | Нет; совпадает со срезом TASK-0001 15da5b225535e34af4e132c701b5353ef4eb667f |
| Задача и порция | [TASK-0003.044](../../../../../../tasks/task-0003.044.md), 9 файлов / 603 логических строк; данный файл — 15 |
| Запись перекрёстной сверки | [TASK-0003.044](../../../../review-log.md#task-0003044) |

## Назначение файла

Общий отчёт урона по всем локациям со сворачиваемыми подробностями каждой зоны.

## Условия использования

Загружается по пути systems/TheWitcherTRPG/templates/chat/damage/damageToAllLocations.hbs через renderTemplate в [module/actor/mixins/damageMixin.js](../../../../../../../module/actor/mixins/damageMixin.js) (applyDamageToAllLocations:103–116). Сам файл не регистрирует событий и не обращается к документам.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| div.witcherTRPG / details / summary | HTML/Handlebars, 1–15 | Внешний итог и вложенные раскрываемые зоны | Шаблон | Создание HTML при рендере |
| {{#each results as &#124;result&#124;}} | HTML/Handlebars, 6–13 | Итерация без пересчёта/сортировки | Шаблон | Создание HTML при рендере |
| partial damageToLocation с result | HTML/Handlebars, 11 | Передаёт сырой результат расчёта как новый контекст | Шаблон | Создание HTML при рендере |

## Основные функции и методы

Собственных JavaScript-функций нет. Вычисления, события и запись выполняет вызывающий JS. Шаблон не обрабатывает result.blockedBySp и не выбирает spAbsorbs: partial подробностей вызывается для каждой записи. JS рассчитывает итог до render, затем ожидает ChatMessage.create, затем updateDerivedStat. Ошибка общих экземпляров относится к расчёту (00285), а несовпадение контекста partial — отдельная 00287.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| Контекст | [module/actor/mixins/damageMixin.js](../../../../../../../module/actor/mixins/damageMixin.js) | Вход renderTemplate | applyDamageToAllLocations:103–116 | Сверены исходный producer и HBS; реальный рендер в Node |
| localize; if/each/or/partial при наличии | Foundry14.367.0 / Handlebars | Template API | Строковые подписи и ветви из таблицы выше | localize/or в тесте фасады; стандартные if/each/partial настоящие |
| Литералы переводов | [lang/en.json](../../../../../../../lang/en.json); [lang/ru.json](../../../../../../../lang/ru.json) | Чтение ключей | Подписи | Настоящий expandObject; всего 14 ключей пяти HBS этой порции существуют в обоих файлах |
| .error-display / .witcherTRPG при наличии | [styles/system-styles.css](../../../../../../../styles/system-styles.css) | Классы HTML/CSS | Обёртки и числа | Поиск стилей, не проверка браузерного cascade |
| damageToLocation | [templates/chat/damage/damageToLocation.hbs](../../../../../../../templates/chat/damage/damageToLocation.hbs); [module/setup/handlebars.js](../../../../../../../module/setup/handlebars.js) | Partial/preload | Вложенный result | Путь совпадает; preload строка 68 |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/actor/mixins/damageMixin.js](../../../../../../../module/actor/mixins/damageMixin.js) | Путь HBS | applyDamageToAllLocations:103–116 | renderTemplate |


Поиск по module/, templates/ и styles/. Внешние модули и макросы не исследовались.

## Данные и изменения состояния

| Поле | Источник и тип | Использование/границы |
| --- | --- | --- |
| totalAppliedDamage | Общее число от JS reduce | Тройные скобки; HBS не проверяет итог |
| results | Массив объектов calculateDamageWithLocation | Не содержит подготовленные текстовые строки |
| result.location.alias | Имя локации | Тройные скобки внутри summary |

Шаблон создаёт HTML; документов не изменяет, значений не сохраняет.

## Проверки и доказательства

Группы 19–20/25/34: получены шесть results с alias; итог 18 без SP и 0 со SP 5; вложенные строки стадий пусты. Отдельный расчёт зон сопоставлен с общим, копирование HBS этого не исправляет. Все строки прочитаны. Настоящий Handlebars использует контексты исходного producer; DOM-представление разбиралось parse5 в соответствующих сценариях.

## Непроверенные участки и открытые вопросы

Браузер, реальный DialogV2/ChatMessage и серверная запись не запускались. Наличие шаблона и локальная компиляция не доказывают HTTP-доступ Foundry или работу сторонних UI-расширений.

## Связанные проблемы

[issue-00285](../../../../../../issues/potential/issue-00285.md), [issue-00287](../../../../../../issues/potential/issue-00287.md). Причина в соответствующем producer/контракте; данный анализ не исправляет код.

## История актуализации

| Дата | Версия и область | Результат |
| --- | --- | --- |
| 2026-09-12 | 965132d5d7972a0edd73aaa62484a1b6ba15991f; полный файл | Первичная карточка; [перекрёстная сверка](../../../../review-log.md#task-0003044) |
