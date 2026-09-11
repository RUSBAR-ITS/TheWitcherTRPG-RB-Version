# module/data/item/templates/professionPathData.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/data/item/templates/professionPathData.js](../../../../../../../../module/data/item/templates/professionPathData.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `c26eb64dd54cc434087f54c3c6b678b6092b15a2` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.019](../../../../../../../tasks/task-0003.019.md), одна порция из двенадцати файлов |
| Запись перекрёстной сверки | [TASK-0003.019](../../../../../review-log.md#task-0003019) |

## Назначение файла

Фабрика схемы одного пути профессии: название и три фиксированных навыка.

## Условия использования

Default function professionPath импортируется ProfessionData и вызывается для skillPath1–3. При каждом вызове создаёт собственные поля, а не Item или экземпляр профессии.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| fields | Alias3 | Конструкторы Foundry | Локально | При импорте |
| professionPath | Функция 5–12 | Объект четырёх полей | Default export | Без аргументов |
| pathName | StringField7 | Название пути | initial='' | Используется как подпись вкладки |
| skill1/skill2/skill3 | SchemaField8–10 | Три навыка | professionSkill() | Независимые определения |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| professionPath() | professionSkill/fields | {pathName,skill1,skill2,skill3} | Создаёт четыре DataField | Синхронно; не задаёт порядок открытия навыков, стоимость или ограничения уровня |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| professionSkill() | [module/data/item/templates/professionSkillData.js](../../../../../../../../module/data/item/templates/professionSkillData.js) | Import/call | 1/8–10 | Фабрика 8 полей |
| StringField/SchemaField | Foundry 14.367.0: /opt/foundryvtt/common/data/fields.mjs; common/abstract/data.mjs; common/abstract/type-data.mjs | Внешняя схема | 7–10 | Настоящие поля и независимость экземпляров |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/data/item/professionData.js](../../../../../../../../module/data/item/professionData.js) | professionPath() | 3 SchemaField | Импорт 2/16–18 |
| [module/item/sheets/configurations/WitcherProfessionConfigurationSheet.js](../../../../../../../../module/item/sheets/configurations/WitcherProfessionConfigurationSheet.js) | pathName/skill1–3 | Подписи вкладок и контекст | _prepareTabs/_preparePartContext |
| [templates/sheets/item/configuration/partials/profession/skillPathPart.hbs](../../../../../../../../templates/sheets/item/configuration/partials/profession/skillPathPart.hbs) | skill1–3 и их fields | Три включения фрагмента навыка | Пути из настоящей схемы |
| [templates/sheets/item/profession-sheet.hbs](../../../../../../../../templates/sheets/item/profession-sheet.hbs) | pathName/навыки | Редактирование трёх колонок | Полный HBS |
| [module/actor/mixins/professionMixin.js](../../../../../../../../module/actor/mixins/professionMixin.js) | skill1–3 | Сумма уровней/поиск | Конкретные потребители |

Область поиска: текущие module/ и templates/; регистрации сверены отдельно. Динамические обращения внешних модулей не исследовались.

## Данные и изменения состояния

Число путей задаёт ProfessionData; число навыков пути задаётся здесь. Имена пути/навыка не идентификаторы модели. Пустой pathName даёт пустую подпись вкладки конфигурации; дополнительных условий доступа фабрика не вводит.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Фабрика/состав | Полные 12 строк и настоящие модели | 4 поля; каждый путь/слот имеет собственную SchemaField | Не игровая проверка |
| Вкладки | Реальные _prepareTabs | Path A и две пустые подписи соответствуют данным | Application поверх фасада |

## Непроверенные участки и открытые вопросы

Исходник прочитан полностью. Изолированно использованы настоящие модели Foundry и системные методы; UI, TextEditor, Actor, Roll, запись и query частично заменены фасадами. Браузер, мир, БД и реальные броски не запускались. Связанные Actor-файлы прочитаны в пределах конкретных потребителей, не объявлены полностью разобранными.

## Связанные проблемы

Собственных новых проблем фабрики не обнаружено; потребители описаны отдельно.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.019 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.

## Дополнительная сверка TASK-0003.038

2026-09-11, `rusbar-main`, `b47ba02cdaebc6a66ad14a5638213b6eb24460b4`; исходники не менялись.

findSkillWithName проверяет definingSkill и skillPath1→2→3, внутри skill1→2→3, точные имена. Возвращает {skill,path}; после поиска пути вычисляет его повторно. Empty/duplicate names не являются устойчивой адресацией; группа 01 воспроизвела 110. Character HBS читает все 9 ячеек, Monster ни одной ветви.

[module/actor/mixins/professionMixin.js](../../../actor/mixins/professionMixin.js.md), [templates/partials/character/tab-profession.hbs](../../../../templates/partials/character/tab-profession.hbs.md), [templates/sheets/actor/partials/monster/tabs/tab-profession.hbs](../../../../templates/sheets/actor/partials/monster/tabs/tab-profession.hbs.md), [templates/dialog/combat/profession-attack.hbs](../../../../templates/dialog/combat/profession-attack.hbs.md).

[Сверка и ограничения](../../../../../review-log.md#task-0003038). Связанные файлы повторно в покрытии не учитывались; код и статусы issues не изменены.
