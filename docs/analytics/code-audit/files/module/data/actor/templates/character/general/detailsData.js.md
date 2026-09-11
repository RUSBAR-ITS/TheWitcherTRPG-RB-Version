# module/data/actor/templates/character/general/detailsData.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/data/actor/templates/character/general/detailsData.js](../../../../../../../../../../module/data/actor/templates/character/general/detailsData.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `17eeb6ae9efccf7474b9ca1845b9ab6370671a26` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.004](../../../../../../../../../tasks/task-0003.004.md), одна порция из восьми файлов |
| Запись перекрёстной сверки | [TASK-0003.004](../../../../../../../review-log.md#task-0003004) |

## Назначение файла

Собирает семь текстовых подробностей персонажа как пары value/label. После включения в CharacterData они находятся в system.general.details.

## Условия использования

При импорте локальная const fields получает foundry.data.fields. Файл экспортирует фабрику определения схемы; значениями экземпляра и валидацией занимается Foundry, а не сама фабрика. Импортирует valueLabel и семь раз вызывает её внутри details(); general() включает результат в SchemaField.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| fields | const, 3 | Классы полей Foundry | Локальная | Чтение в details |
| details | function, 5–16 | Определение семи подробностей | Default export | Создаёт отдельные SchemaField(valueLabel(...)) |
| clothing | SchemaField, 7 | Пара {value: StringField, label: StringField} | general.details.clothing | value=''; label='WITCHER.Clothing' |
| personality | SchemaField, 8 | Пара {value: StringField, label: StringField} | general.details.personality | value=''; label='WITCHER.Personality' |
| hairStyle | SchemaField, 9 | Пара {value: StringField, label: StringField} | general.details.hairStyle | value=''; label='WITCHER.Hair' |
| affectations | SchemaField, 10 | Пара {value: StringField, label: StringField} | general.details.affectations | value=''; label='WITCHER.Affectations' |
| valuedPerson | SchemaField, 11 | Пара {value: StringField, label: StringField} | general.details.valuedPerson | value=''; label='WITCHER.ValuedPerson' |
| value | SchemaField, 12 | Пара {value: StringField, label: StringField} | general.details.value | value=''; label='WITCHER.Value' |
| feelingsOnPeople | SchemaField, 13 | Пара {value: StringField, label: StringField} | general.details.feelingsOnPeople | value=''; label='WITCHER.FeelingsOnPeople' |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| details(); 5–16 | Доступен foundry.data.fields | Объект семи SchemaField | Создаёт новые определения полей при каждом вызове | Синхронно; без записи документов, обработчиков событий и собственного catch |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| valueLabel (default) | [module/data/actor/templates/valueLabelData.js](../../../../../../../../../../module/data/actor/templates/valueLabelData.js) | Прямой импорт и вызов | 1; 7–13: создаёт вложенные StringField value и label | Определение valueLabel:3–8; [проверенная карточка](../../valueLabelData.js.md) |
| SchemaField | Foundry 14.367.0, /opt/foundryvtt/common/data/fields.mjs | Глобальный API | 3,7–13: обёртки полей | Проверено в настоящем CharacterData |
| Семь ключей WITCHER.* | [lang/en.json](../../../../../../../../../../lang/en.json); [lang/ru.json](../../../../../../../../../../lang/ru.json) | Данные подписи → локализация в шаблоне | Передаются в valueLabel без вызова game.i18n | Все ключи найдены после expandObject, как при загрузке переводов Foundry |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/data/actor/templates/character/generalData.js](../../../../../../../../../../module/data/actor/templates/character/generalData.js) | details() | general.details = SchemaField(details()) | Импорт 3; вызов 12 |
| [module/data/actor/characterData.js](../../../../../../../../../../module/data/actor/characterData.js) | general.details | Сборка общей биографии | 16 |
| [templates/partials/character/tab-background.hbs](../../../../../../../../../../templates/partials/character/tab-background.hbs) | details.<ключ>.value/label | Перебор each, localize(details.label), input с динамическим name | 27–33 |
| [module/actor/sheets/WitcherCharacterSheet.js](../../../../../../../../../../module/actor/sheets/WitcherCharacterSheet.js) | Шаблон background | PARTS.background выбирает шаблон; контекст system от базового листа | 59–62,122–123 |

Поиск выполнен по именам файлов/экспортов, полным и относительным путям данных в module/, templates/ и packsJson/. В 226 JSON-компедиумах строковых путей, начинающихся с system.general или system.damageTypeModification, не найдено. Содержимое действующих БД packs и внешние макросы не проверялись.

## Данные и изменения состояния

general.details.value — имя одной из семи пар; её текст находится в general.details.value.value. label хранится как строковое поле данных и может отличаться от своего initial; это не метаданные StringField.label. Список подробностей фиксирован схемой, допустимые тексты фабрика не ограничивает choices. Форма пишет .value; программных расчётов этих текстов в проверенной области не найдено.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Поля ↔ defaults | CharacterData({}) с реальными полями Foundry | Ровно семь пар; все value пусты, label соответствуют таблице | Без сохранения формы |
| Импорт ↔ фабрика ↔ форма | detailsData:1,7–13; valueLabel:3–8; tab-background:27–33 | Все семь полей включены и доступны динамическому перебору | Внешние потребители не исследованы |
| Ключи перевода | Разбор en/ru через foundry.utils.expandObject | Все семь присутствуют | Другие языки и качество перевода не оценивались |

## Непроверенные участки и открытые вопросы

Полностью прочитан исходник и точечно проверены определения и потребители перечисленных связей. Мир, браузер, сохранение форм и применение реального ActiveEffect не запускались. Полный анализ соседних файлов остаётся их порциям; просмотр связи не повышает их статус в реестре.

## Связанные проблемы

Новых проблем в проверенном объёме не выявлено.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.004 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.

## Уточнение TASK-0003.033

2026-09-11, `12055fee62f01c6de49967044aedef9d7cfe0632`. Полный tab-background выводит все семь полей через each: clothing/personality/hairStyle/affectations/valuedPerson/value/feelingsOnPeople. Каждый путь заканчивается .value, label используется для перевода. Группа 09 проверила семь inputs; группа 15 — доступность подписей в en/ru.

Связи: [templates/partials/character/tab-background.hbs](../../../../../../templates/partials/character/tab-background.hbs.md). [Результаты и пределы проверки](../../../../../../../review-log.md#task-0003033).
