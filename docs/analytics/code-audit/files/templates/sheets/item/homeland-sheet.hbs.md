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

В TASK-0004.008 текущий файл и его связи сопоставлены с датированными протоколами TASK-0003.018/.019 (2026-09-10) и .038 (2026-09-11), в пределах относящихся к нему сценариев. Новых поведенческих запусков нет; прежние настоящие модели/методы и фасады различены в протоколе. Браузерный submit, мир, сеть и запись в БД не проверены. Установлены процессы R008-03, R008-20; оставшиеся границы: [U008-01](../../../../cross-check-0002.md#u008-01), [U008-07](../../../../cross-check-0002.md#u008-07). Полный пофайловый разбор соседей в TASK-0003 не равен проверке клиентского lifecycle.

## Связанные проблемы

Новых проблем этого шаблона в пределах проверки не обнаружено. Тип homeland согласован с регистрацией; отдельные вопросы общего листа перечислены в его карточке.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.018 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.

## Сквозная сверка TASK-0004.008

2026-09-14; rusbar-main, f96434101e0e827838c2e6a3e09da8933a9801ef. Исходник совпадает со срезом TASK-0001; изменено только описание.

Форма редактирует value и условный otherValue через унаследованный Item-submit. Наличие произвольного значения в модели не создаёт соответствующий option; собственных расчётов или записи Actor.general в HBS нет.

Сопоставленные определения и потребители: [module/item/sheets/WitcherHomelandSheet.js](../../../module/item/sheets/WitcherHomelandSheet.js.md), [module/data/item/homelandData.js](../../../module/data/item/homelandData.js.md), [module/item/sheets/WitcherItemSheet.js](../../../module/item/sheets/WitcherItemSheet.js.md), [module/setup/config.js](../../../module/setup/config.js.md), [lang/en.json](../../../lang/en.json.md), [lang/ru.json](../../../lang/ru.json.md).

[Протокол и границы](../../../../review-log.md#task-0004008) — TASK-0004.008; процессы [R008-03](../../../../cross-check-0002.md#r008-03), [R008-20](../../../../cross-check-0002.md#r008-20). В этой порции выполнена статическая сверка; прежние опыты сохраняют свои даты и фасады. Новых поведенческих запусков нет; браузер, мир, сеть и запись в БД не запускались.
