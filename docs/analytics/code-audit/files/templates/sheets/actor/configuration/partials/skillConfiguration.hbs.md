# templates/sheets/actor/configuration/partials/skillConfiguration.hbs

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

Браузерное отображение table/formGroup и сохранение checkbox в мире не проверены. Флаг видимости и его использование текущей строкой — отдельные этапы; настройка здесь существует, но character/skill-display не читает isVisible.

## Связанные проблемы

[issue-00004](../../../../../../../../issues/potential/issue-00004.md), [issue-00015](../../../../../../../../issues/potential/issue-00015.md), [issue-00018](../../../../../../../../issues/potential/issue-00018.md). Прежние issues дополнены контекстом настоящей модели; нового issue о неверных именах input нет.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `273a6d7db0b7c866399db3ecd4f7191817ae6f10`; полный файл | Первая карточка; [сверка порции](../../../../../../review-log.md#task-0003029) |

## Уточнение TASK-0003.032

2026-09-11, `8b938d44a042749df027d8b58e28bb1d79638091`. Полный provider WitcherMonsterConfigurationSheet._getSkills даёт 52 записи/51 настоящее поле. Повторная подготовка отражает awareness true→false, core formGroup пропускает undefined commonspeech с предупреждением. tabs.skills автоматически подготовлен core для единственной primary-группы конфигурации.

Связи: [module/actor/sheets/configurations/WitcherMonsterConfigurationSheet.js](../../../../../module/actor/sheets/configurations/WitcherMonsterConfigurationSheet.js.md). [Результаты и пределы проверки](../../../../../../review-log.md#task-0003032).
