# module/data/item/professionData.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/data/item/professionData.js](../../../../../../../module/data/item/professionData.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `c26eb64dd54cc434087f54c3c6b678b6092b15a2` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.019](../../../../../../tasks/task-0003.019.md), одна порция из двенадцати файлов |
| Запись перекрёстной сверки | [TASK-0003.019](../../../../review-log.md#task-0003019) |

## Назначение файла

Модель профессии Item: основной навык, три пути по три навыка, заметки, список базовых профессиональных навыков, подготовка HTML и выбор первого применимого защитного навыка.

## Условия использования

Default export ProfessionData extends CommonItemData; registerDataModels назначает CONFIG.Item.dataModels.profession. system.json объявляет HTML notes/definingSkill.definition/*.*.definition. При импорте определяется класс; подготовку HTML вызывают листы, защиту — документ Item и Actor.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| ProfessionData / fields | Класс 8; alias6 | Схема/HTML/защита | Default export; CONFIG.Item.dataModels.profession | 7 собственных методов |
| commonData | defineSchema:10–13 | 8 полей CommonItemData | Spread | description остаётся StringField; quantity='1', weight/cost=0, sourcebook='', isHidden/isStored=false, isCarried=true |
| notes | HTMLField14 | Заметки | initial='' | Обогащается отдельно |
| definingSkill | SchemaField15 | Основной навык | professionSkill() | Та же 8-полевая схема, что у навыков путей |
| skillPath1/skillPath2/skillPath3 | SchemaField16–18 | Три пути | professionPath() | Всего 9 навыков путей; фиксированные слоты |
| professionSkills | SetField20–23 | Ключи обычных навыков Actor | StringField без choices; label/hint | Подготовленный Set; при Drop меняет isProfession, не уровень навыков |
| Результаты enrichedText / защиты | Объекты 27–46/79–101 | 11 текстов либо вариант защиты | Возврат вызывающему коду | Не отдельные Item/ActiveEffect |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| static defineSchema():9–25 | CommonItemData и две фабрики | 14 верхнеуровневых полей | 8 общих + notes, definingSkill, 3 пути, professionSkills | Синхронно; собственных migrateData/prepare* нет |
| async enrichedText():27–47 | 10 definition и notes, schema | Promise объекта definingSkill/notes/skillPath1–3 | 11 последовательных createEnrichedText; вложенная структура трёх путей | Без catch; source не изменяется, общее description не включено |
| isApplicableDefense(attack):49–55 | Строка вида melee | boolean | OR путей 1→2→3 | definingSkill и isDefense не проверяются; short circuit |
| isApplicableDefenseInPath(attack,path):57–63 | Существующий skillPath | boolean | OR defenseProperties.isApplicableDefense для skill1→2→3 | Невалидный path не защищён; уровень не проверяется |
| findDefensePathData(attack,path):65–77 | Вид атаки/существующий путь | Первый подходящий option либо undefined | Порядок skill1→skill2→skill3; findDefenseSkillData | Синхронно; не возвращает все возможные навыки |
| findDefenseSkillData(path,skill,attack):79–102 | Путь/слот навыка | label,value,modifier,skills:[],itemTypes:[],skillOverride | Добавляет skillName, stat и уровень; labelShort через первую заглавную букву stat | Сам применимость не проверяет. Аргумент attack передаётся вложенному createDefenseOption, который его не использует |
| createDefenseOption(attack):104–114 | Строка вида атаки | Первый option либо undefined | Проверяет путь и передаёт attack,path в findDefensePathData | Аргумент передаётся корректно; прежние issue-00071/00072 сохраняют применимость |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| CommonItemData | [module/data/item/commonItemData.js](../../../../../../../module/data/item/commonItemData.js) | Import/extends/super | 1/8/10; общие поля/getters/calcWeight | Полная прежняя карточка и текущая схема |
| professionPath() | [module/data/item/templates/professionPathData.js](../../../../../../../module/data/item/templates/professionPathData.js) | Import/SchemaField | 2/16–18 | Полная фабрика |
| professionSkill() | [module/data/item/templates/professionSkillData.js](../../../../../../../module/data/item/templates/professionSkillData.js) | Import/SchemaField | 3/15 | Полная фабрика |
| createEnrichedText | [module/data/dataUtils.js](../../../../../../../module/data/dataUtils.js) | Import/await | 4/29–43 | value/enriched/schema.getField; 11 реальных вызовов |
| DataModel/fields/Item lifecycle | Foundry 14.367.0: /opt/foundryvtt/common/data/fields.mjs; common/abstract/data.mjs; common/abstract/type-data.mjs | Внешний API | Типизированные поля/Set | Настоящий WitcherItem поверх common BaseItem, не client Item |
| DefenseProperties | [module/data/item/templates/combat/defensePropertiesData.js](../../../../../../../module/data/item/templates/combat/defensePropertiesData.js) | Через skillDefense | 59–83; Set.has и option | Вложенный класс целиком известен из .012 |
| Item.profession | [system.json](../../../../../../../system.json) | HTML-декларация | 175–177 | Пути согласованы с моделью |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/setup/registerDataModels.js](../../../../../../../module/setup/registerDataModels.js) | ProfessionData | Импорт 15/реестр Item.profession | Регистрация сверена |
| [module/item/sheets/WitcherProfessionSheet.js](../../../../../../../module/item/sheets/WitcherProfessionSheet.js) | system/enrichedText/professionSkills | Общий контекст и основной HBS | 47 полей, 11 HTML |
| [module/item/sheets/configurations/WitcherProfessionConfigurationSheet.js](../../../../../../../module/item/sheets/configurations/WitcherProfessionConfigurationSheet.js) | skillPath1–3 / поля навыков | Контекст и CRUD | Основной навык в конфигурации отсутствует |
| [module/item/mixins/defenseOptionMixin.js](../../../../../../../module/item/mixins/defenseOptionMixin.js) | createDefenseOption | Делегирует attack.attackOption, добавляет имя Item | Возвращённые label/value навыка перекрывают имя Item |
| [module/actor/mixins/defenseMixin.js](../../../../../../../module/actor/mixins/defenseMixin.js) | isApplicableDefense / option | Отбор дополнительных защит и skillOverride | Реальный путь до вызова skillDefense проверен с Dialog-фасадом |
| [module/actor/mixins/professionMixin.js](../../../../../../../module/actor/mixins/professionMixin.js) | definingSkill/skillPath/настройки | Сумма 10 уровней, выбор по имени, применение/броски | Конкретные ветви прочитаны и исполнены в изоляции |
| [module/actor/sheets/mixins/itemMixin.js](../../../../../../../module/actor/sheets/mixins/itemMixin.js) | professionSkills | Drop: сброс и установка isProfession | Неизвестная строка формирует undefined-путь |
| [module/actor/sheets/WitcherCharacterSheet.js](../../../../../../../module/actor/sheets/WitcherCharacterSheet.js) | enrichedText / первый profession Item | _prepareCharacterData:154/160–162 | HTML готовится, но Actor-шаблон его не использует |

Область поиска: текущие module/ и templates/; регистрации сверены отдельно. Динамические обращения внешних модулей не исследовались.

## Данные и изменения состояния

Модель ничего не записывает и не создаёт эффектов. Список professionSkills — обычные навыки, помечаемые isProfession при Drop; это не десять собственных навыков профессии. Подготовленный Set устраняет дубликаты, toObject сохраняет исходный массив до записи. Ключи не ограничены схемой; 52 варианта основной формы найдены в схеме character.

Защита возвращает один навык по порядку путей/слотов, независимо от isDefense и level. В проверке Guard/ref/2/modifier3 прошёл от ProfessionData через WitcherItem и prepareAndExecuteDefense до аргумента skillOverride. Отсутствующая защита даёт undefined. Defining-only защита не рассматривается.

Actor-потребитель различает isAttack → hasCustomEffect → hasThresholds → обычный бросок. Текст definition сам не исполняется. Временные HP создаются отдельным методом Actor, а effects в damageProperties — записи предметных воздействий, не ActiveEffect.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Схема/HTML | Реальная модель и enrichedText | 14 полей;11 результатов, правильные fieldPath и source unchanged | TextEditor-маркер |
| Защита | Настоящие модели/примесь Item/метод Actor | Guard, modifier3, ref/2, правильный skillOverride; isDefense=false не исключён; defining-only=false | Выбор диалога подменён; полный бросок защиты не запускался |
| Список навыков | 52 UI-варианта и Drop | Все штатные ключи найдены; custom missing → system.skills.undefined.missing.isProfession | Actor/update-фасад |
| Показ Actor | Настоящий _prepareCharacterData, HBS/editor | 11 подготовленных HTML не используются; @UUID осталась raw | Обогащение/DOM подменены; дополнение issue-00109 |

## Непроверенные участки и открытые вопросы

Исходник прочитан полностью. Изолированно использованы настоящие модели Foundry и системные методы; UI, TextEditor, Actor, Roll, запись и query частично заменены фасадами. Браузер, мир, БД и реальные броски не запускались. Связанные Actor-файлы прочитаны в пределах конкретных потребителей, не объявлены полностью разобранными.

## Связанные проблемы

[issue-00071](../../../../../../issues/potential/issue-00071.md), [issue-00072](../../../../../../issues/potential/issue-00072.md), [issue-00109](../../../../../../issues/potential/issue-00109.md), [issue-00110](../../../../../../issues/potential/issue-00110.md), [issue-00112](../../../../../../issues/potential/issue-00112.md), [issue-00116](../../../../../../issues/potential/issue-00116.md), [issue-00118](../../../../../../issues/potential/issue-00118.md). Наблюдения относятся к указанным ветвям; отсутствие автоматического повышения уровней не объявлено ошибкой.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.019 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.

## Уточнение TASK-0003.026

2026-09-11, `rusbar-main`, `45a63062a2bd55939fef430609fc5dddc350b0e9`. Полный _onDropItem ожидает сброс всех флагов system.skills.*.isProfession, затем отдельно запускает установку выбранных и addItem без ожидания. Настоящая ProfessionData с awareness/unknown дала правильный int.awareness и system.skills.undefined.unknown (issue-00116). Смена уникальной профессии наследует раннее завершение removeItemsOfType (issue-00034); модель сама unknown не валидирует по справочнику.

Определения: [module/actor/sheets/mixins/itemMixin.js](../../../../../../../module/actor/sheets/mixins/itemMixin.js) и [module/actor/sheets/interactions/itemContextMenu.js](../../../../../../../module/actor/sheets/interactions/itemContextMenu.js). [Методика и перекрёстная сверка](../../../../review-log.md#task-0003026). Полный разбор новых соседних файлов вне порции не засчитывается.

## Уточнение TASK-0003.031

2026-09-11, `928ce4e537c6a3fdc34f8b6fa3fcfdb5a669f68d`. В полном Character-контексте вызван настоящий enrichedText профессии: definingSkill, notes и девять навыков ветвей; getList выбирает первый нестored Item. Header читает только имя профессии. Все методы табличного представления профессии не объявляются проверенными этой порцией.

Связи: [module/actor/sheets/WitcherCharacterSheet.js](../../actor/sheets/WitcherCharacterSheet.js.md); [templates/partials/character-header.hbs](../../../templates/partials/character-header.hbs.md). [Методика и ограничения сверки](../../../../review-log.md#task-0003031).

## Дополнительная сверка TASK-0003.038

2026-09-11, `rusbar-main`, `b47ba02cdaebc6a66ad14a5638213b6eb24460b4`; исходники не менялись.

Первая профессия используется калькулятором/поиском Actor. Group01: defining2+path1.skill1=3 дают 5; вторая профессия 10 не учитывается. Защита по-прежнему отдельный процесс через isApplicableDefense/createDefenseOption; группа 23 подтвердила isDefense=false не исключает defendsAgainst и definingSkill пропущен(71/72). Actor HBS не заменяет редактор Item.

[module/actor/mixins/professionMixin.js](../../actor/mixins/professionMixin.js.md), [templates/partials/character/tab-profession.hbs](../../../templates/partials/character/tab-profession.hbs.md), [templates/sheets/actor/partials/monster/tabs/tab-profession.hbs](../../../templates/sheets/actor/partials/monster/tabs/tab-profession.hbs.md), [templates/dialog/combat/profession-attack.hbs](../../../templates/dialog/combat/profession-attack.hbs.md).

[Сверка и ограничения](../../../../review-log.md#task-0003038). Связанные файлы повторно в покрытии не учитывались; код и статусы issues не изменены.
