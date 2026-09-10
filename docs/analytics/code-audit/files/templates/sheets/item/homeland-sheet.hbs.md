# templates/sheets/item/homeland-sheet.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/sheets/item/homeland-sheet.hbs](../../../../../../../templates/sheets/item/homeland-sheet.hbs) |
| Тип файла | Handlebars, HTML-шаблон |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `29319a7a7e1dfc0663edbc15166f3b6a19682a2f` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.018](../../../../../../tasks/task-0003.018.md), одна порция из восьми файлов |
| Запись перекрёстной сверки | [TASK-0003.018](../../../../review-log.md#task-0003018) |

## Назначение файла

Основная форма родины: выбор ключа из справочника, свободное название для other и ссылка на общую конфигурацию Item.

## Условия использования

Подключается WitcherHomelandSheet.PARTS.main; item/config/showConfig поступают из WitcherItemSheet. enrichedText этому HBS не требуется. Форма работает с system самого Item, не Actor.general.homeland.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| section / header.sheet-header | HTML,1–16 | Оболочка формы | Один main PART | Не вводит вкладок |
| a.configure-item | 2–4 | Открыть настройки Item | if showConfig; data-action='configureItem' | Метод базового листа |
| select#homeland-select.details | 7–9 | Выбор родины | name='system.value' | config.homelands, selected=item.system.value, localize=true |
| input.details.hometailOther | 10–13 | Дополнительное имя | name='system.otherValue'; только value==='other' | Скрытие не удаляет сохранённую строку |

## Основные функции и методы

Функций/классов нет. if showConfig включает шестерёнку; eq(value,'other') включает текстовое поле; selectOptions выводит 26 вариантов WITCHER.homelands. Собственных действий смены названия/картинки Item, бонусов или выбора родины Actor файл не содержит.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| PARTS.main | [module/item/sheets/WitcherHomelandSheet.js](../../../../../../../module/item/sheets/WitcherHomelandSheet.js) | Подключение | 11 | Единственный источник пути этого HBS |
| value/otherValue | [module/data/item/homelandData.js](../../../../../../../module/data/item/homelandData.js) | Схема | system.value/system.otherValue | 2 строки, initial='', без choices/синхронизации |
| item/config/showConfig; configureItem | [module/item/sheets/WitcherItemSheet.js](../../../../../../../module/item/sheets/WitcherItemSheet.js) | Контекст/действие | _prepareContext/_renderConfigureDialog | Optional enrichedText у родины даёт undefined и не мешает форме |
| config.homelands | [module/setup/config.js](../../../../../../../module/setup/config.js) | Справочник | selectOptions:8 | 26 ключей; первый — other; сведения о ключах не равны ограничениям схемы |
| Переводы homelands | [lang/en.json](../../../../../../../lang/en.json); [lang/ru.json](../../../../../../../lang/ru.json) | localize опций | WITCHER.Homelands.* и WITCHER.background.other | Все 26 значений проверены после expandObject |
| eq | Foundry 14.367.0, /opt/foundryvtt/client/applications/handlebars.mjs:140 | Helper ядра | Условие 10 | Сравнение value с литералом other; в изоляции эквивалентная функция a===b |
| selectOptions/prepareSelectOptionGroups | Foundry 14.367.0, /opt/foundryvtt/client/applications/handlebars.mjs и client/applications/forms/fields.mjs | Helpers | Генерация вариантов и выбранного значения | Оба настоящие; HTML-обёртка — фасад |
| DocumentSheetV2.form | Foundry 14.367.0, /opt/foundryvtt/client/applications/api/document-sheet.mjs | Внешняя обработка полей | name system.value/otherValue | Стандартные expand/validate/submit; браузерный ввод не исполнялся |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/item/sheets/WitcherHomelandSheet.js](../../../../../../../module/item/sheets/WitcherHomelandSheet.js) | Основной шаблон | PARTS.main | Полная карточка и точный путь |

Область поиска: текущие module/ и templates/; регистрации сверены отдельно. Динамические обращения внешних модулей не исследовались.

## Данные и изменения состояния

Меняет только предлагаемые пользователю поля, записывает их DocumentSheet. otherValue остаётся в модели, когда value отличается от other и input отсутствует. HBS не содержит name/img/description/sourcebook/quantity или блоков ActiveEffect. Шестерёнка ведёт к конфигурации, где можно создавать эффекты отдельно.

Два других шаблона Actor имеют похожий выбор/вывод родины, но обращаются к другому контексту и не включают этот HBS. На Actor Item является альтернативой general.homeland; изменение этой формы не копирует значения в биографию.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Полный код | 16 строк и фактический контекст | Все данные из Item.system; нет необходимости enrichedText | Наследуемый submit не проверялся |
| Четыре входа | other, '', nilfgaard, customPlace в настоящей HomelandData | Именованных полей 2/1/1/1; 26 вариантов; явный selected other/nilfgaard, для пустого/unknown нет явного selected | Browser default selection не моделировался |
| Сохранённый текст | otherValue='Hidden' с value=customPlace | Модель хранит текст, HBS не выводит input | Не проверка пользовательского сохранения |
| Конфигурация | showConfig=true и handler предка | Шестерёнка есть; конфигурация привязана к тому же документу | Открытие проверено прямым вызовом обработчика, не DOM-кликом |

## Непроверенные участки и открытые вопросы

Весь HBS прочитан. Неподдерживаемый справочником ключ принимается моделью, а отсутствие его option показано как граница UI, не как согласованная ошибка. Реальные DOM события, поля формы, БД, права/HTTP и открытие окна Foundry не проверены.

## Связанные проблемы

Новых проблем этого шаблона в пределах проверки не обнаружено. Тип homeland согласован с регистрацией; отдельные вопросы общего листа перечислены в его карточке.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.018 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.
