# templates/partials/character/tab-skills.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/partials/character/tab-skills.hbs](../../../../../../../templates/partials/character/tab-skills.hbs) |
| Тип файла | Handlebars |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `273a6d7db0b7c866399db3ecd4f7191817ae6f10` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.029](../../../../../../tasks/task-0003.029.md), 14 файлов, 763 логических строк |
| Запись перекрёстной сверки | [TASK-0003.029](../../../../review-log.md#task-0003029) |

## Назначение файла

Действующая общая вкладка встроенных и собственных навыков персонажа и монстра: общий список, группы характеристик, доступ к редактору и область развития IP.

## Условия использования

PARTS.skills обоих V2 листов указывает на этот HBS. Получает system, customSkills, tabs/skillTabs, totalSkills/totalProfSkills. Встроенные навыки — system.skills из семи групп, собственные — embedded Item из _prepareCustomSkills; они передаются в разные partial.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| Навигация skillTabs | Строки 1–7 | Вкладки all, семь групп и ip | data-action=tab; data-group=skillTabs | Активность задаётся cssClass контекста |
| Два прохода system.skills | Строки 9–54 | Общий список и отдельные группы | Встроенный и собственный partial | Каждый навык представлен в двух секциях; details открыты |
| IP / skillTraining1–4 / итоги | Строки 56–108 | Баланс, четыре ручные записи, просмотр журнала и суммы | Полями и классами связаны с CharacterSheet | Не условны по типу Actor |

## Основные функции и методы

Собственных JS-функций нет. Два вызова character/skill-display передают hash skill/name/stat; два вызова character/custom-skill-display передают текущий Item без hash. lookup ../customSkills skillKey возвращает Items нужной группы; @root здесь не используется. openModifiers передаёт data-type='skill' и data-skill-key. manualIpReward, saveIpSpending и open-rewards обслуживаются CharacterSheet.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| Встроенная строка | [templates/partials/character/skill-display.hbs](../../../../../../../templates/partials/character/skill-display.hbs) | Буквальный partial | skill=skill name=name stat=skillKey в двух проходах | Строки 20–21 и 44–45 |
| Собственная строка | [templates/partials/character/custom-skill-display.hbs](../../../../../../../templates/partials/character/custom-skill-display.hbs) | Буквальный partial | Текущий Item из lookup ../customSkills skillKey, без skill/system hash | Строки 24–26 и 48–50 |
| WitcherCharacterSheet / WitcherMonsterSheet | [module/actor/sheets/WitcherCharacterSheet.js](../../../../../../../module/actor/sheets/WitcherCharacterSheet.js); [module/actor/sheets/WitcherMonsterSheet.js](../../../../../../../module/actor/sheets/WitcherMonsterSheet.js) | PARTS, tabs и actions | skillTabs; openModifiers; только Character готовит суммы и обработчики IP | PARTS.skills; _prepareContext; _prepareCharacterData; activateListeners |
| _prepareCustomSkills | [module/actor/sheets/WitcherActorSheet.js](../../../../../../../module/actor/sheets/WitcherActorSheet.js) | Подготовка контекста | Группирует actor.items type=skill по 9 originstat | Строки 103–115 |
| Skills / CharacterData / SkillTraining / Log | [module/data/actor/templates/common/skills/skillsData.js](../../../../../../../module/data/actor/templates/common/skills/skillsData.js); [module/data/actor/characterData.js](../../../../../../../module/data/actor/characterData.js); [module/data/actor/templates/character/skillTrainingData.js](../../../../../../../module/data/actor/templates/character/skillTrainingData.js); [module/data/actor/templates/character/logData.js](../../../../../../../module/data/actor/templates/character/logData.js) | Схемы и журнал | 7 групп, improvementPoints, skillTraining1.name/value до skillTraining4.name/value | Пути input и CharacterSheet обработчики |
| MonsterData | [module/data/actor/monsterData.js](../../../../../../../module/data/actor/monsterData.js) | Сопоставление модели | Не содержит IP, skillTraining, magic и logs персонажа | Тот же PARTS.skills используется и монстром |
| calc_total_skills / calc_total_skills_profession | [module/actor/sheets/mixins/skillMixin.js](../../../../../../../module/actor/sheets/mixins/skillMixin.js); [module/actor/mixins/professionMixin.js](../../../../../../../module/actor/mixins/professionMixin.js) | Расчёт контекста через CharacterSheet | totalSkills и totalProfSkills — readonly disabled input без сохранения | _prepareCharacterData |
| capitalize / concat; localize / lookup / each | [module/setup/handlebars.js](../../../../../../../module/setup/handlebars.js) | Системные helper и регистрация; встроенные Handlebars/core helper | Заголовок WITCHER.St + capitalize(skillKey), циклы и выбранные классы | Регистрация helper и preload текущего HBS |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/actor/sheets/WitcherCharacterSheet.js](../../../../../../../module/actor/sheets/WitcherCharacterSheet.js) | Весь HBS | PARTS.skills | Буквальная ссылка |
| [module/actor/sheets/WitcherMonsterSheet.js](../../../../../../../module/actor/sheets/WitcherMonsterSheet.js) | Весь HBS | PARTS.skills | Буквальная ссылка; старый monster-skill-tab здесь не указан |
| [module/setup/handlebars.js](../../../../../../../module/setup/handlebars.js) | Весь HBS | Предзагрузка шаблона | Строка списка preload; сама по себе не выбирает лист |

Область поиска: module/ и templates/ текущего checkout; прямые импорты и места вызова сверены отдельно от динамических обращений. Типы и листы сверены с system.json, module/setup/registerDataModels.js и module/setup/registerSheets.js. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Редактируемые пути: system.improvementPoints и восемь полей system.skillTraining1–4.name/value. totalSkills/totalProfSkills отключены и только показывают контекст. Для собственных навыков перебор ограничен семью ключами system.skills: наличие подготовленных customSkills.spd/luck не создаёт им раздел. Четыре manual training строки записываются через CharacterSheet/Log; наличие DOM у монстра не означает наличие модели и обработчиков.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Весь HBS и маршруты | 108 строк; оба PARTS; схема и оба partial | 52 встроенных навыка ×2 =104 строки; общий HBS активен для двух типов Actor | Реальный браузер не запускался |
| Контекст собственных навыков | Настоящие Handlebars и _prepareCustomSkills с Item-навыками int/spd/luck | int Item попал в две пустые custom-строки с именем как builtin key; spd/luck подготовлены, но не отображены | Items/Actor document-оболочки контролируются |
| IP и конфигурация | Определения Character/Monster; CharacterSheet handlers; настоящий render edit-skills | Кнопки повышения доступны через общий редактор и монстру без модели развития | Сохранение полей общего IP tab не проверено в Foundry |

## Непроверенные участки и открытые вопросы

Управление вкладками и submit формы проверены по исходникам, без браузерного взаимодействия. Полные классы CharacterSheet/MonsterSheet и конфигурации не входят в 14 файлов. Видимость isVisible определяется строкой partial, а не этим циклом.

## Связанные проблемы

[issue-00018](../../../../../../issues/potential/issue-00018.md), [issue-00187](../../../../../../issues/potential/issue-00187.md), [issue-00188](../../../../../../issues/potential/issue-00188.md), [issue-00192](../../../../../../issues/potential/issue-00192.md). Проблемы контекста Item, двух групп и монстра разделены; ранее найденная видимость уточнена.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `273a6d7db0b7c866399db3ecd4f7191817ae6f10`; полный файл | Первая карточка; [сверка порции](../../../../review-log.md#task-0003029) |

## Уточнение TASK-0003.030

2026-09-11, `aa6af106e86a9c75fe050d599f961c8fadb74f1b`. Итоговая сверка связала оба openModifiers с полностью разобранным классом. Политика type/skillKey находится в HBS, не в фильтре PARTS. После раскрытия dotted JSON все 22 прежних сценария .029 повторно прошли; отсутствие русского levelUp подтверждено, отсутствие семи старых заголовков не подтвердилось.

Сверенные источники: [module/actor/sheets/configurations/WitcherModifiersConfiguration.js](../../../../../../../module/actor/sheets/configurations/WitcherModifiersConfiguration.js); [module/actor/sheets/mixins/statMixin.js](../../../../../../../module/actor/sheets/mixins/statMixin.js). [Итоговая сверка третьей серии, сценарии и ограничения](../../../../review-log.md#task-0003030). Код и статусы проблем не менялись.

## Уточнение TASK-0003.031

2026-09-11, `928ce4e537c6a3fdc34f8b6fa3fcfdb5a669f68d`. PARTS.skills Character с _prepareTabs('skillTabs') передаёт девять групп. Нижняя .saveIpSpending вызывает _saveIpSpending: отрицательная строка остаётся строкой (issue-00200). _addIpReward, привязанный к .manualIpReward, вызывает Actor.addIpReward без ожидания.

Связи: [module/actor/sheets/WitcherCharacterSheet.js](../../../module/actor/sheets/WitcherCharacterSheet.js.md); [templates/partials/character-header.hbs](../character-header.hbs.md). [Методика и ограничения сверки](../../../../review-log.md#task-0003031).

## Уточнение TASK-0003.032

2026-09-11, `8b938d44a042749df027d8b58e28bb1d79638091`. Текущий MonsterSheet.PARTS.skills выбирает эту вкладку, включая IP и общую строку без isVisible. Полный класс не определяет _saveIpSpending/_addIpReward/_renderRewards; базовый listener не привязывает .saveIpSpending. Настройки skillConfig — другое окно, не фильтр этого HBS.

Связи: [module/actor/sheets/WitcherMonsterSheet.js](../../../module/actor/sheets/WitcherMonsterSheet.js.md); [module/actor/sheets/configurations/WitcherMonsterConfigurationSheet.js](../../../module/actor/sheets/configurations/WitcherMonsterConfigurationSheet.js.md). [Результаты и пределы проверки](../../../../review-log.md#task-0003032).
