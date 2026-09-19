# templates/sheets/actor/configuration/partials/skillConfiguration.hbs

## Текущее состояние — 14.3.1.00077

2026-09-19, TASK-0010.014–.018. formGroup isVisible получает label=skillProperties.label из _getSkills; не рассчитывает подпись по общим метаданным поля. Существующие названия полей/флаги и группы прежние.

[Исходник](../../../../../../../../../templates/sheets/actor/configuration/partials/skillConfiguration.hbs), [реализация и проверки](../../../../../../../task-0010-ui-fixes.md). Локальная проверка пройдена; реальная игровая/визуальная приёмка ожидается (HTTP502). Следующие датированные разделы описывают прежние срезы.


| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/sheets/actor/configuration/partials/skillConfiguration.hbs](../../../../../../../../../templates/sheets/actor/configuration/partials/skillConfiguration.hbs) |
| Тип файла | Handlebars |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `273a6d7db0b7c866399db3ecd4f7191817ae6f10` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.029](../../../../../../../../tasks/task-0003.029.md), 14 файлов, 763 логических строк |
| Запись перекрёстной сверки | [TASK-0003.029](../../../../../../review-log.md#task-0003029) |

## Назначение файла

Вкладка конфигурации монстра для выбора видимости встроенных навыков через настоящие DataField и core formGroup.

## Условия использования

PARTS.skills WitcherMonsterConfigurationSheet. Контекст _getSkills перебирает originstat/skillMap, берёт из модели поле isVisible и его текущее значение; _prepareContext передаёт skillConfig, config.statLabels и tabs.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| section.tab skills | Весь HBS, 14 строк | Вкладка primary/skills | tabs.skills.cssClass | Группы skillConfig |
| each skills/attr и skillProperties | Строки 2–12 | details с названием характеристики и таблицей | lookup ../config.statLabels attr | Для каждой записи вызывается formGroup с DataField |
| formGroup isVisible | Строка 9 | Checkbox модели | value=skillProperties.isVisibleValue, localize=true | Имя и подпись определяет DataField, а не буквальный name HBS |

## Основные функции и методы

Собственных функций и статических имён input нет. localize заголовка использует правильный родительский ../config. formGroup вызывает DataField.toFormGroup/toInput; поля/подписи зависят от привязки модели к родителю. При отсутствии DataField core helper сообщает ошибку и не создаёт строку.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| _getSkills / _prepareContext / PARTS.skills | [module/actor/sheets/configurations/WitcherMonsterConfigurationSheet.js](../../../../../../../../../module/actor/sheets/configurations/WitcherMonsterConfigurationSheet.js) | Производитель и владелец формы | skillConfig содержит пары isVisible/isVisibleValue; statLabels и tabs | Прямое чтение определений |
| WITCHER.skillMap / statMap | [module/setup/config.js](../../../../../../../../../module/setup/config.js) | Конфигурация через класс листа | 52 ключа навыков, девять originstat; непустых групп семь | _getSkills |
| Skill.isVisible / IntSkills.commonsp | [module/data/actor/templates/common/skills/skillData.js](../../../../../../../../../module/data/actor/templates/common/skills/skillData.js); [module/data/actor/templates/common/skills/intData.js](../../../../../../../../../module/data/actor/templates/common/skills/intData.js) | DataField-схемы | Поле видимости; commonsp в схеме против commonspeech карты | Путь getField в _getSkills |
| formGroup / DataField.toFormGroup / BooleanField.toInput | Foundry VTT 14.367; Handlebars 4.7.9 | Внешний API | Построение checkbox и подписи по полному fieldPath | Исполнены настоящие core helper и поля; низкоуровневое создание DOM подменено |
| Предзагрузка | [module/setup/handlebars.js](../../../../../../../../../module/setup/handlebars.js) | Регистрация шаблона | Буквальная ссылка на этот HBS | Список preload |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/actor/sheets/configurations/WitcherMonsterConfigurationSheet.js](../../../../../../../../../module/actor/sheets/configurations/WitcherMonsterConfigurationSheet.js) | Весь HBS | PARTS.skills | Буквальный путь |
| [module/setup/handlebars.js](../../../../../../../../../module/setup/handlebars.js) | Весь HBS | preload | Буквальная ссылка |

Область поиска: module/ и templates/ текущего checkout; прямые импорты и места вызова сверены отдельно от динамических обращений. Типы и листы сверены с system.json, module/setup/registerDataModels.js и module/setup/registerSheets.js. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Форма редактирует system.skills.<attribute>.<skill>.isVisible на Actor. В модели с настоящим DataModel-родителем Actor core формирует полные имена полей правильно. Метаданные label для isVisible не заданы, поэтому default подпись становится техническим полным путём. commonsp/commonspeech даёт undefined DataField одной строки, а не ошибочный name остальных 51.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Полный шаблон и подготовка | 14 строк; _getSkills и statLabels | 7 групп из 9 originstat; 52 обращения карты к схеме | Класс конфигурации проверен в пределах потребляемых методов |
| Настоящие поля и formGroup | MonsterData с Actor DataModel-родителем; настоящий _getSkills; Handlebars/core formGroup | 51 checkbox с правильными system.skills.*.isVisible именами; 51 техническая подпись; одна ошибка отсутствующего поля commonspeech | createFormGroup/createCheckboxInput DOM-фасады; сохранение формы не исполнялось |
| Сопоставление старого наблюдения | issue-00015 и проверка непривязанного DataField | Уточнено: короткий isVisible в прежнем опыте зависел от родителя; в Actor путь полный, локализованной подписи всё равно нет | Прежний опыт не перенесён на живую форму без этой оговорки |

## Непроверенные участки и открытые вопросы

Контракт формы установлен прежним настоящим formGroup; браузерный checkbox/таблица и серверное сохранение — [U004-01](../../../../../../cross-check-0002.md#u004-01). Связь видимости не менялась; ru/en — [U004-06](../../../../../../cross-check-0002.md#u004-06).

## Связанные проблемы

[issue-00004](../../../../../../../../issues/closed/issue-00004.md), [issue-00015](../../../../../../../../issues/potential/issue-00015.md), [issue-00018](../../../../../../../../issues/potential/issue-00018.md). Прежние issues дополнены контекстом настоящей модели; нового issue о неверных именах input нет.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `273a6d7db0b7c866399db3ecd4f7191817ae6f10`; полный файл | Первая карточка; [сверка порции](../../../../../../review-log.md#task-0003029) |

## Уточнение TASK-0003.032

2026-09-11, `8b938d44a042749df027d8b58e28bb1d79638091`. Полный provider WitcherMonsterConfigurationSheet._getSkills даёт 52 записи/51 настоящее поле. Повторная подготовка отражает awareness true→false, core formGroup пропускает undefined commonspeech с предупреждением. tabs.skills автоматически подготовлен core для единственной primary-группы конфигурации.

Связи: [module/actor/sheets/configurations/WitcherMonsterConfigurationSheet.js](../../../../../module/actor/sheets/configurations/WitcherMonsterConfigurationSheet.js.md). [Результаты и пределы проверки](../../../../../../review-log.md#task-0003032).

## Сквозная сверка TASK-0004.004

2026-09-14; rusbar-main, f31a2541770dddb23c01b5284c16f31989c5d1e5. Исходник совпадает со срезом TASK-0001; изменено только описание.

Производитель _getSkills отдаёт реальные DataField и isVisibleValue; formGroup строит полные Actor.system пути при настоящем родителе модели. Ошибка commonsp/commonspeech оставляет одну undefined DataField, не неверные имена всех51 остальных. Поле label isVisible не задано; технический путь может служить подписью. Текущий навык игнорирует Bool, старый partial использует.

Сопоставленные определения и потребители: [module/actor/sheets/configurations/WitcherMonsterConfigurationSheet.js](../../../../../module/actor/sheets/configurations/WitcherMonsterConfigurationSheet.js.md), [module/setup/config.js](../../../../../module/setup/config.js.md), [templates/partials/character/skill-display.hbs](../../../../partials/character/skill-display.hbs.md), [templates/partials/monster/monster-skill-display.hbs](../../../../partials/monster/monster-skill-display.hbs.md).

[Протокол и границы](../../../../../../review-log.md#task-0004004) — TASK-0004.004; процессы [R004-10](../../../../../../cross-check-0002.md#r004-10). В этой порции выполнена статическая сверка; поведенческие опыты принадлежат датированным прежним протоколам, а не новому прогону.
