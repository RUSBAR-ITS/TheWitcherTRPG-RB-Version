# module/data/actor/templates/character/general/backgroundData.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/data/actor/templates/character/general/backgroundData.js](../../../../../../../../../../module/data/actor/templates/character/general/backgroundData.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `17eeb6ae9efccf7474b9ca1845b9ab6370671a26` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.004](../../../../../../../../../tasks/task-0003.004.md), одна порция из восьми файлов |
| Запись перекрёстной сверки | [TASK-0003.004](../../../../../../../review-log.md#task-0003004) |

## Назначение файла

Определяет поле HTML биографии персонажа. Итоговый путь — system.general.background.value; фабрика не задаёт происхождение, родину или расовые бонусы.

## Условия использования

При импорте локальная const fields получает foundry.data.fields. Файл экспортирует фабрику определения схемы; значениями экземпляра и валидацией занимается Foundry, а не сама фабрика. Единственный прямой потребитель — generalData.js:2,11; CharacterData затем включает general() в свою схему.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| fields | const, 1 | Ссылка на классы полей | Локальная | Читается фабрикой |
| background | function, 3–7 | Создать определение биографии | Default export | Возвращает объект с одним полем |
| value | HTMLField, 5 | Текст биографии | В возвращённой схеме | initial = пустая строка; редактор и отображение находятся вне файла |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| background(); 3–7 | Доступен foundry.data.fields | {value: HTMLField} | Создаёт новые определения полей при каждом вызове | Синхронно; без записи документов, обработчиков событий и собственного catch |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| HTMLField | Foundry 14.367.0, /opt/foundryvtt/common/data/fields.mjs:3950–3966 | Глобальный API | 1,5; HTML-поле для formGroup | Реальный класс; defaults required/blank=true, стандартный ввод prose-mirror |
| Локальные импорты | Отсутствуют | — | Фабрика не вызывает другие файлы системы | Прочитаны все 7 строк |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/data/actor/templates/character/generalData.js](../../../../../../../../../../module/data/actor/templates/character/generalData.js) | background() | Вложение в SchemaField general.background | Импорт 2, вызов 11 |
| [module/data/actor/characterData.js](../../../../../../../../../../module/data/actor/characterData.js) | general.background.value | enrichedText() передаёт значение и путь в createEnrichedText | 16,34–40 |
| [module/data/dataUtils.js](../../../../../../../../../../module/data/dataUtils.js) | Строка и schema.getField | Возвращает {enriched,value,systemField}; TextEditor.enrichHTML вызывается здесь | createEnrichedText:1–7 |
| [module/actor/sheets/WitcherCharacterSheet.js](../../../../../../../../../../module/actor/sheets/WitcherCharacterSheet.js) | enrichedText.general.background | _prepareContext дополняет контекст результатом document.system.enrichedText() | 139–142; PARTS.background:59–62 |
| [templates/partials/character/tab-background.hbs](../../../../../../../../../../templates/partials/character/tab-background.hbs) | systemField/value/enriched | formGroup с toggled=true формирует редактор | 52 |

Поиск выполнен по именам файлов/экспортов, полным и относительным путям данных в module/, templates/ и packsJson/. В 226 JSON-компедиумах строковых путей, начинающихся с system.general или system.damageTypeModification, не найдено. Содержимое действующих БД packs и внешние макросы не проверялись.

## Данные и изменения состояния

Фабрика создаёт определение HTMLField, Foundry создаёт пустое значение. Подготовка enrichedText строит отдельные данные представления: исходная строка, результат обогащения и объект поля с fieldPath system.general.background.value. Сохранение ввода поручено форме листа с submitOnChange; background() ничего не сохраняет.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Начальное значение и тип | Настоящий CharacterData и Character.schema.getField | value='', класс HTMLField | Без клиента |
| Цепочка обогащения | Исходные CharacterData.enrichedText и createEnrichedText; TextEditor подменён сборщиком аргумента | Строка <p>History</p> передана без замены; fieldPath равен system.general.background.value; value/enriched разделены | HTML-обогащение и редактор не проверялись |
| Шаблон ↔ контекст | tab-background:52 и _prepareContext:139–142 | Используются соответствующие три значения | Статическая сверка |

## Непроверенные участки и открытые вопросы

Полностью прочитан исходник и точечно проверены определения и потребители перечисленных связей. Мир, браузер, сохранение форм и применение реального ActiveEffect не запускались. Полный анализ соседних файлов остаётся их порциям; просмотр связи не повышает их статус в реестре.

## Связанные проблемы

Новых проблем этой фабрики и проверенной цепочки background не выявлено.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.004 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.
