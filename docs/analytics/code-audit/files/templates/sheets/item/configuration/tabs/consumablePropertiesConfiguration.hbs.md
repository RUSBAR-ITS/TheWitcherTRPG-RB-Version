# templates/sheets/item/configuration/tabs/consumablePropertiesConfiguration.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/sheets/item/configuration/tabs/consumablePropertiesConfiguration.hbs](../../../../../../../../../templates/sheets/item/configuration/tabs/consumablePropertiesConfiguration.hbs) |
| Тип файла | Handlebars, HTML-шаблон |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `7edb814aa870da75c7ad7633536e899a8d07e205` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.015](../../../../../../../../tasks/task-0003.015.md), одна порция из пятнадцати файлов |
| Запись перекрёстной сверки | [TASK-0003.015](../../../../../../review-log.md#task-0003015) |

## Назначение файла

Вкладка расходования: признак isConsumable, лечение и редакторы списков добавляемых/снимаемых статусов.

## Условия использования

Подключается PARTS.consumableProperties класса WitcherConsumableConfigurationSheet. Контекст: tabs, systemFields, item.system, config.statusEffects. В родительской configuration есть общий form handler; ручные строки слушает специализированный _onRender.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| Корневой tab | div с data-group=primary/data-tab=consumableProperties | CSS-класс активности из tabs | Configuration PARTS | Показ вкладки |
| isConsumable / doesHeal / heal / addsTempHp | Четыре обращения formGroup | Условная настройка применения и лечения | systemFields, item.system | Форма; addsTempHp в модели отсутствует |
| effects / removesEffects | Две таблицы each as effect name | Записи статусов | consumeProperties | add/remove/edit |
| data-id / data-target / data-field | Контракт DOM | effect.id; название массива; поле записи | Обработчики configuration | Поиск и изменение записи |

## Основные функции и методы

JavaScript-методов нет. formGroup isConsumable отображается всегда. Если isConsumable: doesHeal, условный heal при doesHeal, попытка addsTempHp и обе таблицы. effects выводит name и statusEffect, removesEffects — только statusEffect. selectOptions берёт config.statusEffects, blank='', selected, valueAttr='id', labelAttr='name', localize=true; также передаёт nameAttr='id'. each получает индекс под именем name, но он не используется. Добавление/удаление — data-action; input[name] у ручных строк нет.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| WitcherConsumableConfigurationSheet | [module/item/sheets/configurations/WitcherConsumableConfigurationSheet.js](../../../../../../../../../module/item/sheets/configurations/WitcherConsumableConfigurationSheet.js) | Контекст / обработчики | PARTS, actions и слушатели focusout/input | Определение и обращение сверены |
| ConsumablePropertiesData / consumable() | [module/data/item/templates/consumePropertiesData.js](../../../../../../../../../module/data/item/templates/consumePropertiesData.js); [module/data/item/templates/consumableData.js](../../../../../../../../../module/data/item/templates/consumableData.js) | Схема формы | isConsumable / doesHeal / heal; отсутствующее addsTempHp | Определение и обращение сверены |
| itemEffect() | [module/data/item/templates/itemEffectData.js](../../../../../../../../../module/data/item/templates/itemEffectData.js) | Схема строки | name/statusEffect, без id | Определение и обращение сверены |
| CONFIG.WITCHER.statusEffects | [module/setup/config.js](../../../../../../../../../module/setup/config.js) | Словарь вариантов | Выбор статуса | Определение и обращение сверены |
| WITCHER.Item.* / WITCHER.table.Name | [lang/ru.json](../../../../../../../../../lang/ru.json) | Локализация | Подписи/placeholder | Определение и обращение сверены |
| formGroup / selectOptions / if / each | Foundry Handlebars API | Внешний API | Генерация полей и списков | Определение и обращение сверены |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/item/sheets/configurations/WitcherConsumableConfigurationSheet.js](../../../../../../../../../module/item/sheets/configurations/WitcherConsumableConfigurationSheet.js) | Вкладка/DOM-атрибуты | PARTS.template; действия и слушатели | Двусторонняя связь |

Область поиска: текущие module/ и templates/; регистрации сверены отдельно. Динамические обращения внешних модулей не исследовались.

## Данные и изменения состояния

При выключенном isConsumable остальные свойства сохраняются в данных, но не выводятся. Форма не отображает percentage/varEffect. data-id у очищенных моделью записей равен пустой строке, потому что effect.id отсутствует. Core formGroup V14.367 при несуществующем addsTempHp пишет console.error и возвращает пустую SafeString; остальные поля/таблицы продолжают рендериться. Это не исключение всей формы и не работающая опция временного здоровья.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Условия полей | 3 состояния (false,false), (true,false), (true,true) | 1/2/3 корректных formGroup; 0/1/1 сообщений об отсутствующем addsTempHp | Настоящий helper, toFormGroup фасад |
| Таблицы/действия | Настоящая модель + HBS + parse5 + методы редактора | Оба data-id=''; edit TypeError; remove без удаления; add присоединяет запись | DOM события и update подменены |
| Схема статусов | Полное чтение itemEffectData/config и места вызова | Обычные записи, не ActiveEffect documents; активные эффекты редактируются другой вкладкой | Не проверены сторонние конфигурации |

## Непроверенные участки и открытые вопросы

Не запускались браузерный DOM/FormDataExtended и реальные сохранения. Выбор пользовательского исправления для ID или отсутствующего поля не сделан. Нельзя считать добавленный массив работоспособным редактором только по наличию кнопок.

## Связанные проблемы

[issue-00091](../../../../../../../../issues/potential/issue-00091.md), [issue-00092](../../../../../../../../issues/potential/issue-00092.md), [issue-00060](../../../../../../../../issues/potential/issue-00060.md). 60 относится к условной ветви обработчика текста после поиска записи; раньше неё срабатывает 91.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.015 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.
