# templates/sheets/actor/configuration/app/partials/stats-block.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/sheets/actor/configuration/app/partials/stats-block.hbs](../../../../../../../../../../templates/sheets/actor/configuration/app/partials/stats-block.hbs) |
| Тип файла | Handlebars |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `aa6af106e86a9c75fe050d599f961c8fadb74f1b` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.030](../../../../../../../../../tasks/task-0003.030.md), 9 файлов, 424 логических строк |
| Запись перекрёстной сверки | [TASK-0003.030](../../../../../../../review-log.md#task-0003030) |

## Назначение файла

Общие числовые поля редактора: показывает max, отправляет unmodifiedMax выбранной группы; отдельно добавляет репутацию.

## Условия использования

Получает stats и необязательную reputation из edit-stats; @root.type должен быть stats/derivedStats. Исключает toxicity сравнением локализованной подписи. Предзагружается setup/handlebars.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| each stats | 1–9 | Поле для каждой записи кроме toxicity | name=system.{{@root.type}}.{{stat}}.unmodifiedMax | value={{details.max}}, type=number,data-dtype=Number |
| if reputation | 11–17 | Поле репутации | name=system.reputation.unmodifiedMax | value={{reputation.max}} |

## Основные функции и методы

Собственных JavaScript-функций нет. localize выводит подпись; unless/eq фильтруют toxicity; @root.type сохраняет выбор группы. Поля не имеют min/max/readonly, даже если параметр вычисляется Actor. Сохранение — общая форма Foundry владельца.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| edit-stats.hbs | [templates/sheets/actor/configuration/app/edit-stats.hbs](../../../../../../../../../../templates/sheets/actor/configuration/app/edit-stats.hbs) | Producer hash/context | stats/reputation; @root.type | Два вызова partial |
| WitcherModifiersConfiguration | [module/actor/sheets/configurations/WitcherModifiersConfiguration.js](../../../../../../../../../../module/actor/sheets/configurations/WitcherModifiersConfiguration.js) | Владелец формы | submitOnChange=true, штатная отправка всех полей | DEFAULT_OPTIONS |
| stat / Stats / DerivedStats / Reputation | [module/data/actor/templates/common/stats/statData.js](../../../../../../../../../../module/data/actor/templates/common/stats/statData.js); [module/data/actor/templates/common/stats/statsData.js](../../../../../../../../../../module/data/actor/templates/common/stats/statsData.js); [module/data/actor/templates/common/stats/derivedStatsData.js](../../../../../../../../../../module/data/actor/templates/common/stats/derivedStatsData.js); [module/data/actor/templates/common/reputationData.js](../../../../../../../../../../module/data/actor/templates/common/reputationData.js) | Схемы | max и unmodifiedMax разные числовые поля; база integer, общих min/max нет | Имена и значения input |
| prepareBaseData / расчёты Actor | [module/data/actor/commonActorData.js](../../../../../../../../../../module/data/actor/commonActorData.js); [module/actor/witcherActor.js](../../../../../../../../../../module/actor/witcherActor.js) | Потребители отправленных полей | Фиксированные derived базы пересоздаются; HP/STA зависят от customStat; vigor использует заданную базу | CommonActorData:64–90; calculateFixedDerivedStats/calculateDerivedStat |
| preload / eq / localize | [module/setup/handlebars.js](../../../../../../../../../../module/setup/handlebars.js) | Регистрация и helpers | Буквальная предзагрузка 46; сравнения/перевод | Системные helpers и core Handlebars |
| FormDataExtended / _processFormData | Foundry14.367 client/applications/ux/form-data-extended.mjs и api/document-sheet.mjs | Внешняя отправка формы | Все enabled именованные поля, приведение Number, expandObject | Настоящие классы/метод выполнены на фасаде формы |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [templates/sheets/actor/configuration/app/edit-stats.hbs](../../../../../../../../../../templates/sheets/actor/configuration/app/edit-stats.hbs) | Весь partial | stats и derivedStats | 4,8 |
| [module/setup/handlebars.js](../../../../../../../../../../module/setup/handlebars.js) | Весь HBS | preload | 46 |

Область поиска: module/ и templates/ текущего checkout; прямые импорты и места вызова сверены отдельно от динамических обращений. Типы и листы сверены с system.json, module/setup/registerDataModels.js и module/setup/registerSheets.js. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Максимум после воздействия не совпадает с исходной базой, но input отправляет показанный максимум именно как базу. Даже неизменённое поле входит в общую отправку при изменении другого поля. Отдельно: ввод stun/run/leap/enc/rec/woundTreshold.unmodifiedMax перезаписывается подготовкой, независимо от customStat; HP/STA также вычисляются при !customStat. customStat определён в MonsterData, не CharacterData.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Полные 17 строк и schema/Actor | Пути input, значения и lifecycle подготовки | Два разных поля max/unmodifiedMax; поля фиксированных derived не отключены | Не выбиралась новая семантика |
| Roundtrip | Группа 14: исходная luck8, подготовленный max12, изменение соседнего INT | Настоящий FormDataExtended отправил luck.unmodifiedMax12; модель приняла; с теми же +2 и двумя проходами max стал 16 | Максимум 12 был явно задан как подготовленное состояние, не применение AE в мире |
| Вычисляемые поля | Группа 15 на настоящей MonsterData customStatfalse/true | Ввод 99 для STUN/RUN после подготовки даёт 8/24 в обоих режимах; HP40/99; vigor99 | Настоящие методы подготовки, без server save |

## Непроверенные участки и открытые вопросы

Отправка и очистка модели проверены изолированно; не запускался браузерный submit. Этот результат не означает, что все производные поля игнорируются: показаны различающиеся ветви.

## Связанные проблемы

[issue-00011](../../../../../../../../../issues/potential/issue-00011.md), [issue-00012](../../../../../../../../../issues/potential/issue-00012.md), [issue-00036](../../../../../../../../../issues/potential/issue-00036.md), [issue-00194](../../../../../../../../../issues/potential/issue-00194.md), [issue-00195](../../../../../../../../../issues/potential/issue-00195.md). Прежние миграционные/эффектные наблюдения не смешиваются с двумя новыми ошибками редактора.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `aa6af106e86a9c75fe050d599f961c8fadb74f1b`; полный файл | Первая карточка; [сверка порции](../../../../../../../review-log.md#task-0003030) |
