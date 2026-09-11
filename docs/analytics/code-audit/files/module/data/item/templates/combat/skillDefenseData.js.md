# module/data/item/templates/combat/skillDefenseData.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/data/item/templates/combat/skillDefenseData.js](../../../../../../../../../module/data/item/templates/combat/skillDefenseData.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `d20d821e3a8a0a989ec503b0e97413a5a1431ad9` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.012](../../../../../../../../tasks/task-0003.012.md), одна порция из десяти файлов |
| Запись перекрёстной сверки | [TASK-0003.012](../../../../../../review-log.md#task-0003012) |

## Назначение файла

Фабрика двух полей защиты профессиональным навыком: флага isDefense и вложенной модели DefenseProperties. Она задаёт конфигурацию, а отбор доступных защит выполняет ProfessionData.

## Условия использования

skillDefense() — default export, вызывается из professionSkill() и включается SchemaField. Вложенный DefenseProperties создаётся Foundry; отдельного типа документа для skillDefense нет.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| fields | Локальная константа, строка 3 | Псевдоним foundry.data.fields | Не экспортируется | Инициализируется при импорте |
| skillDefense() | Функция, 5–13 | Собрать схему | Default export | Возвращает два DataField |
| isDefense | BooleanField, 7–10 | Настройка защитного применения навыка | initial:false, label WITCHER.profession.skillPath.skill.skillDefense.isDefense | В UI скрывает/открывает дополнительные поля |
| defenseProperties | EmbeddedDataField, 11 | Применимость и modifier | Класс DefenseProperties | Значения не удаляются автоматически при isDefense:false |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| skillDefense() | Импорт DefenseProperties; foundry.data.fields | Object {isDefense,defenseProperties} | Создаёт флаг и EmbeddedDataField | Синхронно, без проверки применимости, записи или броска |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| DefenseProperties | [module/data/item/templates/combat/defensePropertiesData.js](../../../../../../../../../module/data/item/templates/combat/defensePropertiesData.js) | ES import и EmbeddedDataField | Строки1,11; поля и методы защиты | Класс и реальные экземпляры сверены |
| fields.BooleanField/EmbeddedDataField | Foundry 14.367.0, common/data/fields.mjs | Глобальный API | Два поля | Реальная инициализация ProfessionData |
| WITCHER.profession.skillPath.skill.skillDefense.isDefense | [lang/ru.json](../../../../../../../../../lang/ru.json); [lang/en.json](../../../../../../../../../lang/en.json) | Локализация | label флага | Определение и применение формы |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/data/item/templates/professionSkillData.js](../../../../../../../../../module/data/item/templates/professionSkillData.js) | skillDefense() | SchemaField в каждом навыке | Строки1,16 |
| [module/data/item/professionData.js](../../../../../../../../../module/data/item/professionData.js) | skillDefense.defenseProperties | isApplicableDefenseInPath/findDefensePathData/findDefenseSkillData | 49–114; isDefense не читается |
| [templates/sheets/item/configuration/partials/profession/skillPathSkillPart.hbs](../../../../../../../../../templates/sheets/item/configuration/partials/profession/skillPathSkillPart.hbs) | isDefense, defendsAgainst, modifier | Флаг и условный вывод formGroup | 67–71 |

## Данные и изменения состояния

Фабрика ничего не сохраняет. Переключение isDefense не очищает defendsAgainst/modifier. Это допустимая структура данных сама по себе; рассогласование возникает у потребителя: ProfessionData проверяет defendsAgainst без isDefense и не включает definingSkill в перебор.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Два поля | Настоящий ProfessionData | skillDefense имеет ровно isDefense и defenseProperties | Без UI |
| Выключенная защита | skillPath1.skill1: isDefense:false, defendsAgainst:[melee], modifier:2 | ProfessionData.isApplicableDefense(melee)→true; createDefenseOption вернул этот навык | Запись формы/диалог не запускались |
| Особый слот | Те же свойства с isDefense:true в definingSkill | isApplicableDefense→false, createDefenseOption→undefined | Проверка модели, не игрового правила |

## Непроверенные участки и открытые вопросы

Полный UI definingSkill и всего листа профессии остаётся TASK-0003.019. Для примера definingSkill данные переданы модели напрямую; наличие конкретного пользовательского сценария редактирования этой защиты не заявляется. Поиск — module/ и templates/.

## Связанные проблемы

[issue-00071](../../../../../../../../issues/potential/issue-00071.md) и [issue-00072](../../../../../../../../issues/potential/issue-00072.md) — соответственно игнорирование isDefense и исключение definingSkill из отбора.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.012 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.

## Уточнение TASK-0003.019

2026-09-10, `rusbar-main`, `c26eb64dd54cc434087f54c3c6b678b6092b15a2`. Полный [разбор ProfessionData](../../../../../../../../../module/data/item/professionData.js) повторно подтвердил issue-00071/00072: isDefense=false не исключил Guard, а defining-only защита не найдена. createDefenseOption корректно передаёт attack; получены modifier3 и skillOverride ref/2 через модель, WitcherItem и Actor до skillDefense. [Форма](../../../../../../../../../templates/sheets/item/configuration/partials/profession/skillPathSkillPart.hbs) скрывает defendsAgainst/modifier при выключенном isDefense, не удаляя данные.

[Перекрёстная сверка](../../../../../../review-log.md#task-0003019). Исходники не изменены; уточнение касается проверенных связей, не повторного полного разбора файла.
