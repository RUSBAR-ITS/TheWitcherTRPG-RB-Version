# module/data/actor/templates/valueLabelData.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/data/actor/templates/valueLabelData.js](../../../../../../../../module/data/actor/templates/valueLabelData.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `7b7788bc614e5b7a57f8c596fb64ca75ecabd8b7` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.001](../../../../../../../tasks/task-0003.001.md), одна порция из пяти файлов |
| Запись перекрёстной сверки | [TASK-0003.001](../../../../../review-log.md#task-0003001) |

## Назначение файла

Фабрика двух строковых полей: пользовательское значение и ключ его подписи. Применяется к подробностям персонажа и текстовому полю general.reputation; числовая reputation создаётся другой схемой.

## Условия использования

При импорте `fields` получает ссылку на `foundry.data.fields`. Default export `valueLabel(label)` вызывается фабриками схем; возвращаемый объект затем передаётся в `SchemaField`. Это не класс модели и не обработчик жизненного цикла.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| fields | const, 1 | Доступ к классам полей Foundry | Локальная ссылка | Читается при вызове фабрики. |
| valueLabel | function, 3–8 | Создать набор полей | Default export | Каждый вызов создаёт новые StringField. |
| value | StringField, 5 | Строковое значение | В возвращаемом объекте | initial = пустая строка. |
| label | StringField, 6 | Начальный ключ подписи | В возвращаемом объекте | initial = аргумент label; локализация при отображении. |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| valueLabel(label) | Значение initial для StringField; Foundry.fields доступен при импорте | Объект {value: StringField, label: StringField} | Создание двух определений поля | Синхронная; без сохранения, валидации аргумента и catch. |

`label` — отдельное поле данных, а не метаданные `value.label`. Код не делает подпись неизменяемой и не вызывает `game.i18n`. Преобразование строк, trim и допустимость пустого значения регулирует `StringField`; своих переопределений фабрика не задаёт.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| foundry.data.fields.StringField | Foundry 14.367.0, /opt/foundryvtt/common/data/fields.mjs:1639 и далее | Глобальный API | 1, 5–6: создать строковые поля | Прочитаны defaults, проверено создание настоящих полей. |
| Ключи label | Аргументы из generalData.js и detailsData.js; [lang/en.json](../../../../../../../../lang/en.json) и [lang/ru.json](../../../../../../../../lang/ru.json) | Переданные данные и локализация потребителя | Значение initial поля label | Все восемь используемых ключей присутствуют в en/ru. |
| Локальные импорты | Отсутствуют | — | Фабрика не зависит от других файлов системы напрямую | Полный файл, 8 строк. |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/data/actor/templates/character/generalData.js](../../../../../../../../module/data/actor/templates/character/generalData.js) | valueLabel | general.reputation = SchemaField(valueLabel('WITCHER.Reputation')) | Импорт 1; вызов 14. |
| [module/data/actor/templates/character/general/detailsData.js](../../../../../../../../module/data/actor/templates/character/general/detailsData.js) | valueLabel | Семь полей details | Импорт 1; вызовы 7–13. |
| [module/data/actor/characterData.js](../../../../../../../../module/data/actor/characterData.js) | Вложенные general.reputation и general.details | Включает general() в SchemaField | Импорт generalData; defineSchema:16. |
| [templates/partials/character/tab-background.hbs](../../../../../../../../templates/partials/character/tab-background.hbs) | details.label, details.value | Перебирает семь записей; localize(label); input пишет .value | 27–32; name строится динамически. |
| [module/actor/sheets/WitcherCharacterSheet.js](../../../../../../../../module/actor/sheets/WitcherCharacterSheet.js) | Данные и шаблон background | PARTS подключает tab-background.hbs | 60; сохранение формы не воспроизводилось. |

| Путь после включения в CharacterData | Начальный label |
| --- | --- |
| general.reputation | WITCHER.Reputation |
| general.details.clothing | WITCHER.Clothing |
| general.details.personality | WITCHER.Personality |
| general.details.hairStyle | WITCHER.Hair |
| general.details.affectations | WITCHER.Affectations |
| general.details.valuedPerson | WITCHER.ValuedPerson |
| general.details.value | WITCHER.Value |
| general.details.feelingsOnPeople | WITCHER.FeelingsOnPeople |

Поиск по `valueLabelData`, `valueLabel(`, `general.details` и `general.reputation` выполнен в коде и шаблонах. Для `general.reputation.value` явного чтения/записи вне определения схемы в этой области не найдено. Это не доказывает отсутствия внешних макросов; числовые `system.reputation` и её броски не относятся к этой фабрике.

## Данные и изменения состояния

Создаёт определения полей, не значения конкретного документа. Начальные значения применяет Foundry при очистке данных. Фабрика не меняет Actor, не выполняет бросок и не ограничивает длину или набор допустимых строк своими настройками.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Форма результата | Вызов исходной фабрики с настоящими StringField | Ровно value и label; указанные initial | Без клиента Foundry. |
| Определения и включение | Два импорта, восемь вызовов; CharacterData и шаблон | Установлены полные пути и перевод подписи в интерфейсе | Сохранение формы не запускалось. |
| Локализация | Разбор JSON en/ru по точным ключам | Восемь ключей найдены | Семантика переводов и остальные языки для этих ключей не оценивались. |

## Непроверенные участки и открытые вопросы

Непрочитанных частей файла нет. Отсутствие найденного потребителя general.reputation не классифицировано как ошибка: поле может быть оставлено для данных или внешних средств. На момент TASK-0003.001 полный разбор generalData и листа персонажа оставался следующим порциям; generalData затем разобрана в TASK-0003.004, см. дополнение ниже.

## Связанные проблемы

Новых проблем самой фабрики в пределах выполненной проверки не выявлено.


## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.001 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.

## Уточнение TASK-0003.004

2026-09-10, `17eeb6ae9efccf7474b9ca1845b9ab6370671a26`. Полностью разобраны оба прямых потребителя: [detailsData.js](character/general/detailsData.js.md) и [generalData.js](character/generalData.js.md). Реальный CharacterData подтвердил семь пар details и текстовую general.reputation; label хранится в данных. Потребитель details — динамические inputs tab-background:27–33. Явное чтение general.reputation по-прежнему не найдено в module/templates/packsJson. Полный разбор листа остаётся следующей порции.

[Перекрёстная сверка TASK-0003.004](../../../../../review-log.md#task-0003004).
