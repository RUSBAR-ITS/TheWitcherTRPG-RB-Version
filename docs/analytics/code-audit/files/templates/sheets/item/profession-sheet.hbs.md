# templates/sheets/item/profession-sheet.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/sheets/item/profession-sheet.hbs](../../../../../../../templates/sheets/item/profession-sheet.hbs) |
| Тип файла | Handlebars, HTML-шаблон |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `c26eb64dd54cc434087f54c3c6b678b6092b15a2` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.019](../../../../../../tasks/task-0003.019.md), одна порция из двенадцати файлов |
| Запись перекрёстной сверки | [TASK-0003.019](../../../../review-log.md#task-0003019) |

## Актуализация N01–N08 — 14.3.1.00010

2026-09-16, dev, база aeb527c6e6402e8a5f940a2c3ad0020d7e5b35e4. Отображаемые placeholder/tooltip используют `WITCHER.Name`. Привязки name/data-field, классы действий, условия шаблона и введённые имена сохранены.

[Реализация и адресные проверки](../../../../../../issues/closed/issue-00330.md#реализация-n01n08--143100010). Датированные разборы ниже сохраняют результаты прежних срезов.


## Назначение файла

Основная форма профессии: имя/источник, десять навыков и их описания, названия путей, заметки и набор обычных профессиональных навыков.

## Условия использования

PARTS.main класса WitcheProfessionSheet. Получает item,systemFields,enrichedText,config,professionSkills,showConfig из общего и специализированного контекста. Шаблон не включает skillPathPart и не является конфигурацией механик.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| section.scrollable/header | 1–23 | Оболочка/заголовок | Один main PART | name;configureItem при showConfig;editImage/img;sourcebook |
| defining-skill | 25–37 | 4 поля основного навыка | skillName/stat/level/definition | definition через formInput |
| profession-notes | 38–42 | notes | formInput enrichedText.notes | Отдельно от CommonItemData.description |
| profession-path | 43–164 | 3 колонки по 3 навыка | 3 pathName +9 наборов 4 полей | Фиксированная разметка |
| professionSkills | 166–168 | Выбор обычных навыков | formGroup SetField;options из контекста | 52 варианта;не 10 навыков профессии |

## Основные функции и методы

Собственных функций/классов нет. Десять selectOptions для statTypes, 11 formInput для HTML, один formGroup для professionSkills. if showConfig управляет шестерёнкой. Имя и уровень каждого слота адресуются полным name=system.<path>.<field>, независимо от отображаемого skillName.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| WitcheProfessionSheet | [module/item/sheets/WitcherProfessionSheet.js](../../../../../../../module/item/sheets/WitcherProfessionSheet.js) | PARTS/контекст | Включение/списки | 52 choices и 9 statOptions (здесь statTypes с none) |
| WitcherItemSheet | [module/item/sheets/WitcherItemSheet.js](../../../../../../../module/item/sheets/WitcherItemSheet.js) | Общий контекст/actions | configureItem/systemFields/enrichedText | Полный путь |
| ProfessionData | [module/data/item/professionData.js](../../../../../../../module/data/item/professionData.js) | Поля/HTML | 10 навыков+notes+professionSkills | 11 реальных enriched результатов |
| professionPath/professionSkill | [module/data/item/templates/professionPathData.js](../../../../../../../module/data/item/templates/professionPathData.js); [module/data/item/templates/professionSkillData.js](../../../../../../../module/data/item/templates/professionSkillData.js) | Вложенные определения | 3 имени пути/10 наборов | Пути form names сверены |
| statTypes/skillMap | [module/setup/config.js](../../../../../../../module/setup/config.js) | Справочник | selectOptions/formGroup | 10 statTypes включая none;52 навыка |
| localize | [lang/en.json](../../../../../../../lang/en.json); [lang/ru.json](../../../../../../../lang/ru.json) | Переводы | SourceBook/Notes и варианты | 157 общих ключей проверены, два прежних пробела skillMap |
| formInput/formGroup/selectOptions/HTMLField | Foundry 14.367.0, /opt/foundryvtt/client/applications/handlebars.mjs; common/data/fields.mjs | Helpers/поля | Рендер формы | HTMLField/11 ProseMirror inputs настоящие до DOM-фасада |
| editImage/именованные поля | Foundry 14.367.0, /opt/foundryvtt/client/applications/api/document-sheet.mjs | Внешние действия/submit | data-action/name | Декларации, без реального submit |
| CSS/image | [styles/profession-sheet.css](../../../../../../../styles/profession-sheet.css); [styles/character/tab-profession.css](../../../../../../../styles/character/tab-profession.css) | Селекторы/контекст | profession-layout/card/level/input/editor | Внешний вид не проверен; assets вне аудита |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/item/sheets/WitcherProfessionSheet.js](../../../../../../../module/item/sheets/WitcherProfessionSheet.js) | Основной HBS | PARTS.main | 15–17 |

Область поиска: текущие module/ и templates/; регистрации сверены отдельно. Динамические обращения внешних модулей не исследовались.

## Данные и изменения состояния

47 именованных элементов: name/sourcebook (2), 10×4 полей навыков (40), 3 pathName, notes, professionSkills. Все 11 HTML-полей передают field/value/enriched отдельно. В отличие от Actor-вкладки, готовый HTML используется. Никакие атаки/HP/эффекты не исполняются рендером. Механические признаки definingSkill здесь не редактируются; number-поля уровня не задают min/max.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Рендер | Настоящий HBS/formInput/HTMLField | 47 имён;11 HTML-входов с правильным value/enriched/path | SetField финальный DOM заменён регистратором |
| Пути/модель | Поля 47 элементов и schema | Все соответствуют модели/Document.name | Сохранение не запускалось |
| Конфигурация | showConfig/action | Открытие передано специальной конфигурации, defining-механик здесь нет | Без click UI |

## Непроверенные участки и открытые вопросы

В TASK-0004.008 текущий файл и его связи сопоставлены с датированными протоколами TASK-0003.018/.019 (2026-09-10) и .038 (2026-09-11), в пределах относящихся к нему сценариев. Новых поведенческих запусков нет; прежние настоящие модели/методы и фасады различены в протоколе. Браузерный submit, мир, сеть и запись в БД не проверены. Установлены процессы R008-04, R008-05, R008-06, R008-20; оставшиеся границы: [U008-01](../../../../cross-check-0002.md#u008-01), [U008-06](../../../../cross-check-0002.md#u008-06). Полный пофайловый разбор соседей в TASK-0003 не равен проверке клиентского lifecycle.

## Связанные проблемы

[issue-00016](../../../../../../issues/closed/issue-00016.md), [issue-00112](../../../../../../issues/potential/issue-00112.md), [issue-00118](../../../../../../issues/potential/issue-00118.md). Пустой stat — граница модели/Actor-кнопки; сама форма его не преобразует в коде HBS.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.019 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.

## Сквозная сверка TASK-0004.008

2026-09-14; rusbar-main, f96434101e0e827838c2e6a3e09da8933a9801ef. Исходник совпадает со срезом TASK-0001; изменено только описание.

Основная форма редактирует десять слотов, три имени пути, notes и Set базовых навыков. Статистика берётся из statTypes с none, одиннадцать HTMLField получают value/enriched. Дополнительные механики находятся в отдельной configuration и доступны лишь девяти навыкам путей.

Сопоставленные определения и потребители: [module/item/sheets/WitcherProfessionSheet.js](../../../module/item/sheets/WitcherProfessionSheet.js.md), [module/item/sheets/WitcherItemSheet.js](../../../module/item/sheets/WitcherItemSheet.js.md), [module/data/item/professionData.js](../../../module/data/item/professionData.js.md), [module/data/item/templates/professionPathData.js](../../../module/data/item/templates/professionPathData.js.md), [module/data/item/templates/professionSkillData.js](../../../module/data/item/templates/professionSkillData.js.md), [module/setup/config.js](../../../module/setup/config.js.md), [lang/en.json](../../../lang/en.json.md), [lang/ru.json](../../../lang/ru.json.md), [styles/profession-sheet.css](../../../styles/profession-sheet.css.md), [styles/character/tab-profession.css](../../../styles/character/tab-profession.css.md).

[Протокол и границы](../../../../review-log.md#task-0004008) — TASK-0004.008; процессы [R008-04](../../../../cross-check-0002.md#r008-04), [R008-05](../../../../cross-check-0002.md#r008-05), [R008-06](../../../../cross-check-0002.md#r008-06), [R008-20](../../../../cross-check-0002.md#r008-20). В этой порции выполнена статическая сверка; прежние опыты сохраняют свои даты и фасады. Новых поведенческих запусков нет; браузер, мир, сеть и запись в БД не запускались.
