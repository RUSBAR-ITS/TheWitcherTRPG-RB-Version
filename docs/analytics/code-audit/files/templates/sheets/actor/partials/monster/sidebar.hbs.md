# templates/sheets/actor/partials/monster/sidebar.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/sheets/actor/partials/monster/sidebar.hbs](../../../../../../../../../templates/sheets/actor/partials/monster/sidebar.hbs) |
| Тип файла | Handlebars |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `8b938d44a042749df027d8b58e28bb1d79638091` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.032](../../../../../../../../tasks/task-0003.032.md), 13 файлов, 973 логические строки |
| Запись перекрёстной сверки | [TASK-0003.032](../../../../../../review-log.md#task-0003032) |

## Назначение файла

Боковая панель текущего монстра: две картинки, состояние HP, ресурсы, четыре области брони, Vigor/щит и два флага игнорирования состояний. Все 154 строки прочитаны.

## Условия использования

PARTS.sidebar; предзагрузка отдельным путём. Изображение Actor использует core editImage, категория — зависимость assets/images/Monsters/<category>.png.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| .cat-img/.monster-img | 2–14 | Категория и портрет | system.category/actor.img | 12 корректных динамических имён, title/tooltip; портрет data-action=editImage/data-edit=img |
| .wound-state | 4–12 | Иконка HP | hp.value/unmodifiedMax, woundTreshold.value | Целое зелёное при >=base; иначе зелёное треснувшее при >=threshold, иначе оранжевое |
| .status-section | 16–80 | HP/STA/toxicity/focus/resolve | Именованные Number input и progress | HP/STA max99; toxicity из stats; resolve условен useVerbalCombat |
| .monster-armor-list | 81–102 | Броня головы/верха/низа/хвоста-крыла | armorHead/armorUpper/armorLower/armorTailWing | Четыре number input без min/max, независимо от hasTailWing |
| .optional-stats-section | 103–154 | Vigor.max, shield.value и ignored | system.derivedStats/system.healthState | Vigor отображается по truthy max; щит editable; два checkbox, applied не редактируется |

## Основные функции и методы

Программных функций и экспортов нет. Ниже описаны поля/условия разметки и их контракт с моделями и обработчиками; собственной записи документа файл не выполняет.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| MonsterData и CommonActorData | [module/data/actor/monsterData.js](../../../../../../../../../module/data/actor/monsterData.js); [module/data/actor/commonActorData.js](../../../../../../../../../module/data/actor/commonActorData.js) | модель/поля | system и systemFields | Пути сверены с определениями, использованы настоящие модели |
| Контекст листа | [module/actor/sheets/WitcherMonsterSheet.js](../../../../../../../../../module/actor/sheets/WitcherMonsterSheet.js); [module/actor/sheets/WitcherActorSheet.js](../../../../../../../../../module/actor/sheets/WitcherActorSheet.js) | PARTS/подготовка | actor/document/system, опции, записи enrichedText | Полный _prepareContext выполнен с Application-фасадом |
| helpers и переводы | [module/setup/handlebars.js](../../../../../../../../../module/setup/handlebars.js); [lang/en.json](../../../../../../../../../lang/en.json); [lang/ru.json](../../../../../../../../../lang/ru.json) | Handlebars/локализация | localize, concat, eq/gte, checked, selectOptions, formGroup/editor по месту | Системные helpers и core helpers сверены; DOM-элементы формы заменены |
| stats/derivedStats/healthState/temporaryHpSum | [module/data/actor/templates/common/stats/statsData.js](../../../../../../../../../module/data/actor/templates/common/stats/statsData.js); [module/data/actor/templates/common/stats/derivedStatsData.js](../../../../../../../../../module/data/actor/templates/common/stats/derivedStatsData.js); [module/data/actor/commonActorData.js](../../../../../../../../../module/data/actor/commonActorData.js); [module/data/actor/templates/common/combatEffectsData.js](../../../../../../../../../module/data/actor/templates/common/combatEffectsData.js) | схема/подготовка | Пути ресурсов и флаги | База суммирует temporary HP; значения input/progress не включают сумму |
| calculateStat/calculateDerivedStat | [module/actor/witcherActor.js](../../../../../../../../../module/actor/witcherActor.js) | расчёт/чтение ignored | healthState и текущие максимумы | Числовые методы выполнены изолированно |
| CSS-селекторы | [styles/monster/sidebar.css](../../../../../../../../../styles/monster/sidebar.css) | оформление | .monster-sidebar/.img-view/ресурсы | Прочитаны нужные селекторы; полный CSS вне порции |
| editImage/FormDataExtended | Foundry 14.367.0 ActorSheetV2/DocumentSheetV2 | внешняя форма | Портрет и payload | Запись в БД/изменение изображения не выполнялись |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/actor/sheets/WitcherMonsterSheet.js](../../../../../../../../../module/actor/sheets/WitcherMonsterSheet.js) | HBS sidebar | PARTS.sidebar | Путь/обращение сверены в исходнике |
| [module/setup/handlebars.js](../../../../../../../../../module/setup/handlebars.js) | путь | preloadHandlebarsTemplates | Путь/обращение сверены в исходнике |

Область поиска: module/ и templates/ текущего checkout; прямые импорты и места вызова сверены отдельно от динамических обращений. Типы и листы сверены с system.json, module/setup/registerDataModels.js и module/setup/registerSheets.js. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Без resolve —11 именованных input (9 числовых+2 bool), с resolve —12 (10+2). Удачи и адреналина на этой панели нет. HP120 и toxicity−2 могут присутствовать в payload; max99 не объявлен доказанным серверным ограничением. hasTailWing не скрывает поле брони хвоста/крыла. Категорийные assets исключены из карточек; проверено только существование 12 путей.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Поля/пути/опции | 07 | 12 полей при resolve, HP120/toxicity−2/armorTailWing9; 12 путей картинок существуют | FormDataExtended и DOM-фасад, не браузер |
| Иконка | 08 | 40/60/base40 — целая; 35/35/base40 — треснувшая | Повторное наблюдение issue-00203 |
| Переводы | 25 | Четыре ignore/ignoreHint отсутствуют в ru, fallback en | Те же ключи issue-00205 |

## Непроверенные участки и открытые вопросы

Файл прочитан целиком. Мир, браузер, HTTP-доступ, Document.update и работа нескольких клиентов не запускались. Настоящие модели, Handlebars, core helpers и вычисления использовались с фасадами Application/DOM и перехватом записи; подробные границы — в журнале .032. CSS и ресурсы проверены только как зависимости, соседние файлы вне порции не засчитываются в покрытие.

## Связанные проблемы

[issue-00203](../../../../../../../../issues/potential/issue-00203.md), [issue-00205](../../../../../../../../issues/potential/issue-00205.md). Исправления не выполнялись; вывод ограничен указанными проверками.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `8b938d44a042749df027d8b58e28bb1d79638091`; полный файл | Первая карточка; [сверка порции](../../../../../../review-log.md#task-0003032) |
