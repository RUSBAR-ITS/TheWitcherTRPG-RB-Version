# templates/sheets/actor/partials/monster/tabs/partials/monster-status.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/sheets/actor/partials/monster/tabs/partials/monster-status.hbs](../../../../../../../../../../../templates/sheets/actor/partials/monster/tabs/partials/monster-status.hbs) |
| Тип файла | Handlebars |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `8b938d44a042749df027d8b58e28bb1d79638091` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.032](../../../../../../../../../../tasks/task-0003.032.md), 13 файлов, 973 логические строки |
| Запись перекрёстной сверки | [TASK-0003.032](../../../../../../../../review-log.md#task-0003032) |

## Назначение файла

Текстовые сопротивления, иммунитеты, уязвимости и чувства плюс список иммунитетов к статусам. Все 14 строк прочитаны.

## Условия использования

Подключается первой частью detailTabs.notes, отдельно предзагружается.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| .monster-status text inputs | 1–5, 10–14 | Четыре текстовых свойства | system.resistances/immunities/susceptibilities/senses | StringField, поля общей формы |
| multi-select | 6–9 | Иммунитеты к статусам | system.statusEffectImmunities | selectOptions config.statusEffects с id/name, selected массивом, localize=true |

## Основные функции и методы

Программных функций и экспортов нет. Ниже описаны поля/условия разметки и их контракт с моделями и обработчиками; собственной записи документа файл не выполняет.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| MonsterData и CommonActorData | [module/data/actor/monsterData.js](../../../../../../../../../../../module/data/actor/monsterData.js); [module/data/actor/commonActorData.js](../../../../../../../../../../../module/data/actor/commonActorData.js) | модель/поля | system и systemFields | Пути сверены с определениями, использованы настоящие модели |
| Контекст листа | [module/actor/sheets/WitcherMonsterSheet.js](../../../../../../../../../../../module/actor/sheets/WitcherMonsterSheet.js); [module/actor/sheets/WitcherActorSheet.js](../../../../../../../../../../../module/actor/sheets/WitcherActorSheet.js) | PARTS/подготовка | actor/document/system, опции, записи enrichedText | Полный _prepareContext выполнен с Application-фасадом |
| helpers и переводы | [module/setup/handlebars.js](../../../../../../../../../../../module/setup/handlebars.js); [lang/en.json](../../../../../../../../../../../lang/en.json); [lang/ru.json](../../../../../../../../../../../lang/ru.json) | Handlebars/локализация | localize, concat, eq/gte, checked, selectOptions, formGroup/editor по месту | Системные helpers и core helpers сверены; DOM-элементы формы заменены |
| WITCHER.statusEffects | [module/setup/config.js](../../../../../../../../../../../module/setup/config.js) | словарь статусов | selectOptions id/name | Настоящий helper обработал 26 опций, stun выбран |
| applyStatus; applyStatusEffect | [module/actor/witcherActor.js](../../../../../../../../../../../module/actor/witcherActor.js); [module/scripts/statusEffects/applyStatusEffect.js](../../../../../../../../../../../module/scripts/statusEffects/applyStatusEffect.js) | потребители иммунитетов | Применение состояний Actor | Отдельные пути: issue-00031 в Actor, это не отсутствие поля формы |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [templates/sheets/actor/partials/monster/tabs/tab-details.hbs](../../../../../../../../../../../templates/sheets/actor/partials/monster/tabs/tab-details.hbs) | partial | detailTabs.notes | Путь/обращение сверены в исходнике |
| [module/setup/handlebars.js](../../../../../../../../../../../module/setup/handlebars.js) | путь | preloadHandlebarsTemplates | Путь/обращение сверены в исходнике |

Область поиска: module/ и templates/ текущего checkout; прямые импорты и места вызова сверены отдельно от динамических обращений. Типы и листы сверены с system.json, module/setup/registerDataModels.js и module/setup/registerSheets.js. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Текстовое immunities и массив statusEffectImmunities — разные поля. Здесь нет расчёта сопротивления урону и обработки статуса. Массив отправляет custom element Foundry; простое чтение HTML option не доказывает работу этого элемента в браузере.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Поля и опции | 12 | senses='Dark vision'; multi-select с нужным name; stun присутствует и selected | Настоящий selectOptions, custom element не запущен |

## Непроверенные участки и открытые вопросы

Файл прочитан целиком. Мир, браузер, HTTP-доступ, Document.update и работа нескольких клиентов не запускались. Настоящие модели, Handlebars, core helpers и вычисления использовались с фасадами Application/DOM и перехватом записи; подробные границы — в журнале .032. CSS и ресурсы проверены только как зависимости, соседние файлы вне порции не засчитываются в покрытие.

## Связанные проблемы

[issue-00031](../../../../../../../../../../issues/potential/issue-00031.md). Ранее найденная ошибка applyStatus сохраняется; эта порция проверяет доступный источник массива, не повторяет весь lifecycle статусов.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `8b938d44a042749df027d8b58e28bb1d79638091`; полный файл | Первая карточка; [сверка порции](../../../../../../../../review-log.md#task-0003032) |
