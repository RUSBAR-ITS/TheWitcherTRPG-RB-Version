# module/data/item/templates/effectStatData.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/data/item/templates/effectStatData.js](../../../../../../../../module/data/item/templates/effectStatData.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-12 |
| Ветка и коммит | rusbar-main, 2f94c6c29e298ccf73d67ccc2e5fb8fc358dae2c |
| Изменения относительно коммита | Нет; совпадает со срезом TASK-0001 15da5b225535e34af4e132c701b5353ef4eb667f |
| Задача и порция | [TASK-0003.047](../../../../../../../tasks/task-0003.047.md), 10 файлов / 661 логических строк; данный файл — 9 |
| Запись перекрёстной сверки | [TASK-0003.047](../../../../../review-log.md#task-0003047) |

## Назначение файла

Не подключённая в исследуемом срезе фабрика трёх StringField: id, modifier и stat; сама значения не вычисляет и модель не регистрирует.

## Условия использования

При импорте const fields сохраняет foundry.data.fields; экспортируется default function modifierStat. Каждый явный вызов возвращает новый словарь и три новых StringField. id.initial содержит функцию, а не готовый ID: randomID вызывается ядром при подготовке отсутствующего значения, не при импорте или вызове фабрики.

Поиск по путям effectDerivedStatData/effectSkillData/effectStatData и именам effectDerivedStat/effectSkill/modifierStat в исходном репозитории (без docs/assets/.github/.git) нашёл только три определения. Прямых импортов, реэкспортов, строковых загрузчиков, регистраций и вызовов не найдено. Проверены [module/data/item/commonItemData.js](../../../../../../../../module/data/item/commonItemData.js), [module/setup/registerDataModels.js](../../../../../../../../module/setup/registerDataModels.js) и действующий маршрут ActiveEffect. Прямой импорт в проверке возможен; это не подтверждает штатное использование.

## Введённые сущности и действия с ними

| Сущность | Вид / строки | Доступность | Действие |
| --- | --- | --- | --- |
| fields | const:1 | Локальная ссылка | Доступ к конструктору StringField ядра |
| modifierStat | default function:3–9 | Единственный экспорт | Создаёт набор полей без аргументов |
| id | StringField:5 | Возвращённый словарь | initial: () => foundry.utils.randomID(); не специальный DocumentIdField |
| modifier | StringField:6 | Возвращённый словарь | initial: строка '0' |
| stat | StringField:7 | Возвращённый словарь | initial: пустая строка; choices не заданы |

## Основные функции и методы

| Функция | Входы | Результат | Ошибки / состояние |
| --- | --- | --- | --- |
| modifierStat() | Доступно foundry.data.fields при импорте | Обычный объект с тремя новыми полями | Без await, документов, регистрации и записи; без Foundry глобала импорт невозможен |
| id.initial() | В момент вызова нужен foundry.utils.randomID | Случайная строка ID | Вызывает внешний API; сама фабрика ID не кеширует и уникальность коллекции не проверяет |

### Поля и границы

Настоящие defaults StringField в установленном Foundry14.367.0: required=false, nullable=false, blank=true, trim=true, choices=undefined. Здесь задан только initial. Поэтому нет прикладной проверки имени stat, числового диапазона modifier, потолка 10 или минимума 1. Проверенные строки '-2', '12', '/2', '2+3', 'wrong' остаются строками; числа приводятся StringField к строке, пробелы обрезаются. Формула не исполняется.

В изолированной DataModel с этой схемой отсутствующий modifier получает  '0'; явная пустая строка сохраняется. null при штатной очистке заменён initial (nullable=false): modifier → '0', stat → ''. Явные id='own' и id='' сохраняются без randomID. Два новых экземпляра без id получили разные 16-символьные значения; это наблюдение двух генераций, не доказательство отсутствия любых коллизий.

В [effectSkill](../../../../../../../../module/data/item/templates/effectSkillData.js) modifier имеет initial='', здесь — '0'. Совпадение слова modifier не связывает эти поля с changes ActiveEffect.

## Используемые сущности и зависимости

| Сущность | Источник | Вид / место обращения | Основание |
| --- | --- | --- | --- |
| foundry.data.fields.StringField | Foundry14.367.0, /opt/foundryvtt/common/data/fields.mjs:1639 | Конструктор:5–7 | Настоящие поля и модель исполнены |
| foundry.utils.randomID | Foundry common/utils/helpers.mjs | Отложенный callback:5 | Настоящий генератор через счётчик вызовов |
| DataModel / SchemaField | Foundry common/abstract/data.mjs и fields.mjs | Только контрольный потребитель в памяти | Не импортируются этим файлом; в системе такой потребитель не найден |
| Две соседние фабрики | [module/data/item/templates/effectDerivedStatData.js](../../../../../../../../module/data/item/templates/effectDerivedStatData.js), [module/data/item/templates/effectSkillData.js](../../../../../../../../module/data/item/templates/effectSkillData.js) | Сопоставление структуры | Между файлами нет импортов или вызовов |

## Известные потребители

Производственные потребители не найдены в указанной области. [module/setup/registerDataModels.js](../../../../../../../../module/setup/registerDataModels.js) регистрирует классы Item/Actor/ActiveEffect, а не этот словарь полей. [module/data/item/commonItemData.js](../../../../../../../../module/data/item/commonItemData.js) его не включает. [module/data/activeEffects/witcherActiveEffectData.js](../../../../../../../../module/data/activeEffects/witcherActiveEffectData.js) наследует ActiveEffectTypeDataModel ядра, [module/activeEffect/WitcherActiveEffectSheet.js](../../../../../../../../module/activeEffect/WitcherActiveEffectSheet.js) работает с system.changes и мастером из [module/activeEffect/mixins/baseMixin.js](../../../../../../../../module/activeEffect/mixins/baseMixin.js). Мастер предлагает пути totalModifiers/activeEffectModifiers; эти поля id/modifier/stat он не создаёт.

## Данные и изменения состояния

Только объекты описаний схемы в памяти. Нет Actor/Item/ActiveEffect, changes, arithmetic, Hooks, миграции или сохранения. Преобразование и очистка строк принадлежат StringField, применение к игровым значениям должно было бы принадлежать отдельному consumer; такой consumer не установлен. Неиспользование само по себе не зарегистрировано проблемой.

## Проверки и доказательства

| Группы / действие | Результат | Ограничения |
| --- | --- | --- |
|01–02 | Свежие словари/поля; randomID не вызван фабрикой; реальные модели получают defaults и разные id | Контрольный subclass DataModel объявлен только в stdin |
|03–04 | Числа/строки/неизвестная цель/пустота/null; явные id; точные defaults StringField | Модель не зарегистрирована в CONFIG и не сохранена |
|05 и поиск rg | CommonItemData не содержит эти поля; настоящий мастер возвращает пути характеристик/навыков; подключений фабрик не найдено | Внешние модули, макросы и БД не обследованы |

## Непроверенные участки и открытые вопросы

Внешний динамический потребитель неизвестен — [U005-08](../../../../../cross-check-0002.md#u005-08). Отсутствие внутреннего вызова не разрешает удаление и не устанавливает замысел автора.

## Связанные проблемы

Новых проблем не зарегистрировано. Известные проблемы действующего ActiveEffect не приписываются этой неподключённой фабрике.

## История актуализации

| Дата | Версия и область | Результат |
| --- | --- | --- |
| 2026-09-12 | 2f94c6c29e298ccf73d67ccc2e5fb8fc358dae2c; полный файл | Первичная карточка; [перекрёстная сверка](../../../../../review-log.md#task-0003047) |

## Сквозная сверка TASK-0004.005

2026-09-14; rusbar-main, 4686f913501b9c75082e79249364e40934f6a1da. Исходник совпадает со срезом TASK-0001; изменено только описание.

Фабрика modifierStat возвращает id/modifier/stat как три StringField. modifier по умолчанию строка '0'; id вычисляется отложенным randomID. Повторный поиск по module/templates/packsJson не обнаружил подключения имени/пути. CommonItemData и регистрация моделей используют другую схему; мастер работает с ActiveEffect.system.changes. Контрольная DataModel в .047 была только потребителем в памяти и не доказывает наличие такого механизма в системе.

Сопоставленные определения и потребители: [module/data/item/commonItemData.js](../commonItemData.js.md), [module/setup/registerDataModels.js](../../../setup/registerDataModels.js.md), [module/activeEffect/WitcherActiveEffectSheet.js](../../../activeEffect/WitcherActiveEffectSheet.js.md), [module/data/activeEffects/witcherActiveEffectData.js](../../activeEffects/witcherActiveEffectData.js.md).

[Протокол и границы](../../../../../review-log.md#task-0004005) — TASK-0004.005; процессы [R005-14](../../../../../cross-check-0002.md#r005-14). В этой порции выполнена статическая сверка; поведенческие опыты принадлежат датированным прежним протоколам, а не новому прогону.
