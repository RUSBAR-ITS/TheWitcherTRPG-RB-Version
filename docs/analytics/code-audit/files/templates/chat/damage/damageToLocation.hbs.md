# templates/chat/damage/damageToLocation.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/chat/damage/damageToLocation.hbs](../../../../../../../templates/chat/damage/damageToLocation.hbs) |
| Тип файла | Handlebars |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-12 |
| Ветка и коммит | rusbar-main, 965132d5d7972a0edd73aaa62484a1b6ba15991f |
| Изменения относительно коммита | Нет; совпадает со срезом TASK-0001 15da5b225535e34af4e132c701b5353ef4eb667f |
| Задача и порция | [TASK-0003.044](../../../../../../tasks/task-0003.044.md), 9 файлов / 603 логических строк; данный файл — 40 |
| Запись перекрёстной сверки | [TASK-0003.044](../../../../review-log.md#task-0003044) |

## Назначение файла

Подробный вывод стадий урона одной локации и пояснений бронебойности/износа.

## Условия использования

Загружается по пути systems/TheWitcherTRPG/templates/chat/damage/damageToLocation.hbs через renderTemplate в [module/actor/mixins/damageMixin.js](../../../../../../../module/actor/mixins/damageMixin.js) (createDamageResultMessage:263–286; как partial из damageToAllLocations). Сам файл не регистрирует событий и не обращается к документам.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| div.witcherTRPG / div / span.error-display | HTML/Handlebars, Строки 1–40 | Контейнер и строки шести стадий | Шаблон | Создание HTML при рендере |
| {{#if damageProperties.improvedArmorPiercing}} | HTML/Handlebars, 8–10 | Пояснение уменьшения SP | Шаблон | Создание HTML при рендере |
| {{#if (or damageProperties.improvedArmorPiercing damageProperties.armorPiercing)}} | HTML/Handlebars, 22–24 | Пояснение бронебойности после сопротивлений | Шаблон | Создание HTML при рендере |
| {{#if damageProperties.ablating}} / crushingForce | HTML/Handlebars, 30–38 | Две условные строки с одним spDamage | Шаблон | Создание HTML при рендере |

## Основные функции и методы

Собственных JavaScript-функций нет. Вычисления, события и запись выполняет вызывающий JS. Это один общий partial и отдельный renderTemplate-ресурс. Его предварительно загружает module/setup/handlebars.js. Шаблон не выводит название локации: allLocations помещает его во внешний summary. Не вызывает DamageInstance.*Text и не читает damageInstances. Поэтому передача сырого result из общего сообщения оставляет числовые строки пустыми. Тройные скобки не локализуют source-ключи в квадратных скобках.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| Контекст | [module/actor/mixins/damageMixin.js](../../../../../../../module/actor/mixins/damageMixin.js) | Вход renderTemplate | createDamageResultMessage:263–286; как partial из damageToAllLocations | Сверены исходный producer и HBS; реальный рендер в Node |
| localize; if/each/or/partial при наличии | Foundry14.367.0 / Handlebars | Template API | Строковые подписи и ветви из таблицы выше | localize/or в тесте фасады; стандартные if/each/partial настоящие |
| Литералы переводов | [lang/en.json](../../../../../../../lang/en.json); [lang/ru.json](../../../../../../../lang/ru.json) | Чтение ключей | Подписи | Настоящий expandObject; всего 14 ключей пяти HBS этой порции существуют в обоих файлах |
| .error-display / .witcherTRPG при наличии | [styles/system-styles.css](../../../../../../../styles/system-styles.css) | Классы HTML/CSS | Обёртки и числа | Поиск стилей, не проверка браузерного cascade |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/actor/mixins/damageMixin.js](../../../../../../../module/actor/mixins/damageMixin.js) | Путь HBS | createDamageResultMessage:263–286; как partial из damageToAllLocations | renderTemplate |
| [module/setup/handlebars.js](../../../../../../../module/setup/handlebars.js) | Шаблон | preloadHandlebarsTemplates, строка 68, loadTemplates | Прямой путь |
| [templates/chat/damage/damageToAllLocations.hbs](../../../../../../../templates/chat/damage/damageToAllLocations.hbs) | Шаблон | Строка 11, inline partial с контекстом result | Прямой путь |

Поиск по module/, templates/ и styles/. Внешние модули и макросы не исследовались.

## Данные и изменения состояния

| Поле | Источник и тип | Использование/границы |
| --- | --- | --- |
| initialDamage / displaySP / afterSPReduction | Готовые строки стадий | Передаются JS; тройные фигурные скобки выводят HTML без escaping |
| afterLocation / afterResistance / finalDamage | Готовые строки стадий | Значения не суммируются и не пересчитываются HBS |
| damageProperties | Флаги AP/IAP/ablating/crushingForce | Producer читает result.damageProperties, хотя результат содержит properties |
| spDamage | Число/сумма износа | Видно только при соответствующем флаге |

Шаблон создаёт HTML; документов не изменяет, значений не сохраняет.

## Проверки и доказательства

Группа 25: одиночный producer дал числовые строки, но damageProperties=undefined и блоки ablating/crushingForce не показались; общий producer дал пустые текстовые поля partial. Группа 32: все локальные литеральные ключи перевода найдены en/ru. Все строки прочитаны. Настоящий Handlebars использует контексты исходного producer; DOM-представление разбиралось parse5 в соответствующих сценариях.

## Непроверенные участки и открытые вопросы

Браузер, реальный DialogV2/ChatMessage и серверная запись не запускались. Наличие шаблона и локальная компиляция не доказывают HTTP-доступ Foundry или работу сторонних UI-расширений.

## Связанные проблемы

[issue-00287](../../../../../../issues/potential/issue-00287.md). Причина в соответствующем producer/контракте; данный анализ не исправляет код.

## История актуализации

| Дата | Версия и область | Результат |
| --- | --- | --- |
| 2026-09-12 | 965132d5d7972a0edd73aaa62484a1b6ba15991f; полный файл | Первичная карточка; [перекрёстная сверка](../../../../review-log.md#task-0003044) |
