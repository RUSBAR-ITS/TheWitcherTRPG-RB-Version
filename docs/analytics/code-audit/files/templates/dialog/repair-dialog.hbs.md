# templates/dialog/repair-dialog.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/dialog/repair-dialog.hbs](../../../../../../templates/dialog/repair-dialog.hbs) |
| Тип файла | Handlebars, HTML-шаблон |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `c7cd9d71dcb1714cdccb175aee351a3f1df95c5b` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.017](../../../../../tasks/task-0003.017.md), одна порция из пяти файлов |
| Запись перекрёстной сверки | [TASK-0003.017](../../../review-log.md#task-0003017) |

## Назначение файла

Шаблон содержимого диалога ремонта: заголовок предмета, сложность, ожидаемый список повреждений и общий partial компонентов.

## Условия использования

Предзагружается setup/handlebars.js:66. RepairSystem.prepareDialogTemplate рендерит его с {components,data,isRequest,canEditCost}; DialogV2 добавляет кнопки извне. Сам HBS не вызывает ремонт и не обрабатывает отмену/submit.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| div.repair / header.item-header / h1.itemname / img.profile-img | HTML,1–8 | Заголовок действия, name/img/title предмета | Контекст data.item | Только вывод |
| table.information.repair-info / item-header-tablerow | HTML,9–28 | DC и строки повреждений | data.repairDC и each data.damagedLocations | label, reliabilityValue/maxReliabilityValue |
| general / itemimage | Элементы разметки,4–7/29 | Группировка блока изображения/информации | Не программные классы Foundry | Участвуют в CSS-селекторах |
| components-list include | Partial30–32 | Список ресурсов и цена | components=components, showCost=isRequest, canEditCost, totalPrice=data.repairPrice | Условные ценовые поля/итог создаёт partial |

## Основные функции и методы

Функций и классов нет. localize выводит подписи действия и DC; each выполняет тело для каждого damagedLocations. При undefined список не рисуется и шаблон сам не бросает ошибку. Ни этот файл, ни partial не вычисляют DC или повреждённые области.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| data.item, repairDC, damagedLocations, repairPrice; components/isRequest/canEditCost | [module/item/systems/repair.js](../../../../../../module/item/systems/repair.js) | Контекст renderTemplate | prepareDialogTemplate:118–165 | data.damagedLocations ожидается HBS, но не определён в RepairData; четыре сценария рендера дали только строку DC |
| components-list | [templates/partials/components-list.hbs](../../../../../../templates/partials/components-list.hbs) | Partial include | 30–32; передача строк и цены | Полная карточка TASK-0003.016; showCost здесь означает наличие artisan |
| Предзагрузка | [module/setup/handlebars.js](../../../../../../module/setup/handlebars.js) | loadTemplates | Список включает repair-dialog:66 | Путь совпадает с renderTemplate |
| WITCHER.Repair.action / params.repairDC | [lang/en.json](../../../../../../lang/en.json); [lang/ru.json](../../../../../../lang/ru.json) | localize | Заголовок и DC | Ключи проверены в двух локализациях |
| table.repair-info / .repair .components-list-container / .repair general | [styles/repair.css](../../../../../../styles/repair.css) | CSS | Выравнивание/шрифт таблицы, прокрутка и высота частей | Файл прочитан как зависимость; отдельный аудит CSS не заявлен |
| localize / each / partial / экранирование | Foundry 14.367.0, Handlebars 4.7.9 | Внешний шаблонизатор | Все подстановки | Реальный Handlebars/parse5; localize-фасад с настоящими словарями |
| data.item.img | Ресурс документа Item; встроенные icons Foundry или иное значение | Изображение | src/title | Загрузка изображений не проверялась; assets исключены из пофайлового анализа |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/item/systems/repair.js](../../../../../../module/item/systems/repair.js) | HTML диалога | prepareDialogTemplate→renderDialog→DialogV2.wait.content | Рендер и четыре конфигурации проверены |
| [module/setup/handlebars.js](../../../../../../module/setup/handlebars.js) | Путь HBS | Предзагрузка | 66 |

Область поиска: текущие module/ и templates/; регистрации сверены отдельно. Динамические обращения внешних модулей не исследовались.

## Данные и изменения состояния

Контекст data.item используется по ссылке, но HBS не меняет документ. Строки components уже содержат required1/quantity/missingQuantity/cost; шаблон получает готовый repairPrice. isRequest здесь вычисляется из artisan, а не означает кнопку «Запросить ремонт» в чате. Кнопки repair/sim-repair/request-repair/gm-repair задаются repair.js и не являются разметкой этого файла.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Полнота | 33 логические строки; полный контекст и partial | Все поля/селекторы перечислены | Браузер/CSS layout не проверен |
| Обычный и заказной ремонт | Реальные HBS, BaseItem/RepairData, GM=false/true | Заголовок/DC19; во всех случаях одна информационная строка, без повреждений | RepairData действительно не содержит damagedLocations |
| Требования | quantity0 owned, missing и unknown; quantities рецепта 8/5/4 | Все строки подготовлены с required1; owned0 помечен нехваткой | Расчёт находится в RepairSystem; соответствие количеств рулбуку не устанавливалось |
| Цена | isRequest/GM и components-list | При собственном ремонте cost-колонки скрыты; при artisan видимы, редактирование cost0 зависит от GM | Состав partial ранее проверен; денег HBS не меняет |

## Непроверенные участки и открытые вопросы

Полностью прочитан шаблон и сверены все данные. Foundry 14.367/Handlebars 4.7.9; рендер выполнен изолированно. Не проверены реальные модальные окна, серверный доступ к шаблону, загрузка картинки и отображение CSS. Дополнительные связи .item-header общего оформления здесь не считаются отдельным аудитом CSS.

## Связанные проблемы

[issue-00102](../../../../../issues/potential/issue-00102.md), [issue-00104](../../../../../issues/potential/issue-00104.md), [issue-00105](../../../../../issues/potential/issue-00105.md), [issue-00100](../../../../../issues/potential/issue-00100.md), [issue-00106](../../../../../issues/potential/issue-00106.md). 102 — отсутствующий список повреждений у источника;104 — отметка нехватки не превращается в проверку допуска;105 — null ломает подготовку. 100/106 относятся к включённому списку цены и его внешнему обработчику.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.017 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.
