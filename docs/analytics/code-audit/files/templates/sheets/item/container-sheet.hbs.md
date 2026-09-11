# templates/sheets/item/container-sheet.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/sheets/item/container-sheet.hbs](../../../../../../../templates/sheets/item/container-sheet.hbs) |
| Тип файла | Handlebars |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `66cd03705dbc398eba0026284a298b5fbe337035` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.024](../../../../../../tasks/task-0003.024.md), 3 файла, 136 логических строк |
| Запись перекрёстной сверки | [TASK-0003.024](../../../../review-log.md#task-0003024) |

## Назначение файла

Форма контейнера: общая шапка предмета, описание, отношение storedWeight/carry и список подготовленного содержимого с кнопками извлечения.

## Условия использования

WitcherContainerSheet.PARTS.main загружает шаблон. Базовый WitcherItemSheet передаёт item, data=item.system, systemFields, config и showConfig. Шапка включается общим partial; контейнерный шаблон сам не читает UUID и не считает вес.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| section.scrollable | 1–39 | Контейнер разметки | PARTS.main | Без собственного form; форма унаследована от DocumentSheetV2 |
| item-header.hbs | partial, 2 | Имя/картинка/общие поля | Без отдельного hash-контекста | Читает item/config/showConfig |
| system.description | textarea, 4 | Редактируемое описание контейнера | {{data.description}} | Обычный текст; enrichedText не используется |
| storedWeight / system.carry | 6–12 | Текущий вес и вместимость | storedWeight disabled; carry number/data-dtype Number | storedWeight не имеет name и не отправляется этим полем |
| each data.itemContent as \|storedItem\| | 13–38 | Подготовленные строки | name,quantity,weight,description,uuid | Имеет .container-item, .header и item-content |
| remove-item / data-uuid | 17–18 | Кнопка извлечения | storedItem.uuid | Click listener листа; собственного data-action нет |
| quantity/weight/description | 21–35 | Сведения о содержимом | disabled inputs/textarea | Description выводится только при truthy значении; img в этой форме не используется |

## Основные функции и методы

JavaScript-функций нет. Partial добавляет общие поля. each/if показывают подготовленные данные; текст интерполируется с HTML-экранированием. Клик .remove-item делегируется установленному листом listener. Вычисление, разрешение UUID и изменение Item выполняют другие файлы.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| WitcherContainerSheet | [module/item/sheets/WitcherContainerSheet.js](../../../../../../../module/item/sheets/WitcherContainerSheet.js) | Потребитель/обработчик | PARTS.main и .remove-item | Ожидает dataset.uuid |
| WitcherItemSheet | [module/item/sheets/WitcherItemSheet.js](../../../../../../../module/item/sheets/WitcherItemSheet.js) | Контекст | item/data/systemFields/config/showConfig | Группа 14 исполнила настоящий _prepareContext на базе-фасаде |
| ContainerData | [module/data/item/containerData.js](../../../../../../../module/data/item/containerData.js) | Prepared-структура | storedWeight/carry/itemContent | itemContent не поле схемы; 7 ключей строки |
| item-header.hbs | [templates/partials/item-header.hbs](../../../../../../../templates/partials/item-header.hbs) | Буквальный partial | 2 | Шапка проверена с обычным контейнером; общий configureItem |
| localize WITCHER.Item.Quantity / WITCHER.Item.Weight | [lang/en.json](../../../../../../../lang/en.json); [lang/ru.json](../../../../../../../lang/ru.json) | Локализация | 23/27 | Оба ключа существуют в en/ru |
| Handlebars / форма V2 | Foundry 14.367.0 client/applications/handlebars.mjs; api/document-sheet.mjs | Внешний рендер/форма | each/if/интерполяция; именованные поля | Рендер Handlebars 4.7.9 и разбор parse5 |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/item/sheets/WitcherContainerSheet.js](../../../../../../../module/item/sheets/WitcherContainerSheet.js) | container-sheet.hbs | PARTS.main | 19 |

Область поиска: module/ и templates/ текущего checkout; регистрация сверена с system.json. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

В форме нельзя менять количество/вес содержимого: поля disabled и без name. Извлечение оперирует полным UUID из prepared-строки. Нет проверок GM/owner в шаблоне; доступ формы и запись должны обеспечиваться базовым листом/API. Прямая форма контейнера не показывает img storedItem, но модель готовит его для инвентарного потребителя. Описание выводится как исходная строка в textarea; HTML не интерпретируется.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Контекст/поля/HTML | Группа 14 | data === item.system; одна ссылка удаления с нужным UUID; пустой список не даёт кнопок; <b>Bag</b> экранирован; system-пути формы входят в схему | База листа, helpers настроек и браузерный DOM подменены |
| Реакция UI | Группы 11/14 | Кнопка соответствует _onRemoveItem; listener click установлен | Фактическая отправка формы/клик браузера не выполнялись |

## Непроверенные участки и открытые вопросы

Все 39 строк прочитаны. Браузерный рендер, доступ наблюдателя, сохранение carry/description, загрузка изображений и доступность HTTP не проверялись. Собственной ошибки пути data/system или потерянного UUID в корректно подготовленной строке не обнаружено.

## Связанные проблемы

[issue-00156](../../../../../../issues/potential/issue-00156.md), [issue-00157](../../../../../../issues/potential/issue-00157.md), [issue-00158](../../../../../../issues/potential/issue-00158.md), [issue-00163](../../../../../../issues/potential/issue-00163.md). Проблемы относятся к подготовке строк/извлечению и применению вместимости, а не к совпадению полей HBS.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `66cd03705dbc398eba0026284a298b5fbe337035`; полный файл | Первая карточка; [сверка порции](../../../../review-log.md#task-0003024) |
