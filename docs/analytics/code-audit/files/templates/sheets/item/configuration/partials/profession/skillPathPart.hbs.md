# templates/sheets/item/configuration/partials/profession/skillPathPart.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/sheets/item/configuration/partials/profession/skillPathPart.hbs](../../../../../../../../../../templates/sheets/item/configuration/partials/profession/skillPathPart.hbs) |
| Тип файла | Handlebars, HTML-шаблон |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-16: актуализация технических обращений по issue-00001 |
| Ветка и коммит | `dev`, база `d8e0e1ad1159cb71a8769b0353f812de6f1ed4d8` + незакоммиченное исправление issue-00001 |
| Изменения относительно коммита | issue-00001; текущие технические обращения актуализированы. Прежние опыты ниже относятся к своим датам. |
| Задача и порция | [TASK-0003.019](../../../../../../../../../tasks/task-0003.019.md), одна порция из двенадцати файлов |
| Запись перекрёстной сверки | [TASK-0003.019](../../../../../../../review-log.md#task-0003019) |

Актуализация [issue-00001](../../../../../../../../../issues/open/issue-00001.md), 2026-09-16: Обращения к ресурсам и/или техническим namespaces переведены на TheWitcherTRPG-RB-Version. Формулы и порядок действий сохранены. Датированные проверки ниже выполнены до смены ID.

## Назначение файла

Фрагмент вкладки одного пути конфигурации: три включения редактора навыка с соответствующими данными и SchemaField.

## Условия использования

Один HBS используется PARTS.skillPath1/2/3. В _preparePartContext передаются skillPathFields,skillPath,config,tab,partId.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| div.tab | 1–5 | Вкладка/прокрутка | tab.cssClass,data-group=primary,data-tab=partId | Оболочка;не записывает Item |
| Три include skillPathSkillPart | 2–4 | Редакторы skill1/2/3 | skillFields=skillPathFields.fields.skillN;skill=skillPath.skillN | Контекст config наследуется partial |

## Основные функции и методы

Собственных функций нет. Три явных включения частичного шаблона; не each по произвольному списку, не отдельный редактор definingSkill.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| WitcherProfessionConfigurationSheet | [module/item/sheets/configurations/WitcherProfessionConfigurationSheet.js](../../../../../../../../../../module/item/sheets/configurations/WitcherProfessionConfigurationSheet.js) | PARTS/контекст | 18/23/28 и _preparePartContext | Один шаблон для трёх путей |
| professionPath | [module/data/item/templates/professionPathData.js](../../../../../../../../../../module/data/item/templates/professionPathData.js) | Поля/схема | skill1–3 | SchemaField.fields |
| skillPathSkillPart | [templates/sheets/item/configuration/partials/profession/skillPathSkillPart.hbs](../../../../../../../../../../templates/sheets/item/configuration/partials/profession/skillPathSkillPart.hbs) | Handlebars partial | 2–4 | Передача DataField и значения одного слота |
| registerHelpers/loadHandlebarTemplates | [module/setup/handlebars.js](../../../../../../../../../../module/setup/handlebars.js) | Предзагрузка partial | 58 | Фрагмент skillPathSkillPart зарегистрирован |
| HandlebarsApplicationMixin/Handlebars | Foundry 14.367.0, /opt/foundryvtt/client/applications/api/handlebars-application.mjs; Handlebars 4.7.9 | Внешний рендер | Контекст partial/частей | Исходный HBS отрендерен |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/item/sheets/configurations/WitcherProfessionConfigurationSheet.js](../../../../../../../../../../module/item/sheets/configurations/WitcherProfessionConfigurationSheet.js) | Шаблон пути | PARTS.skillPath1–3 | Три ссылки на одинаковый путь |

Область поиска: текущие module/ и templates/; регистрации сверены отдельно. Динамические обращения внешних модулей не исследовались.

## Данные и изменения состояния

Фрагмент передаёт явный объект каждого слота, но внутренние кнопки нижнего HBS используют skillName. Таким образом правильный контекст рендера не гарантирует правильную адресацию CRUD. Пути с пустыми настройками выводят по 4 флага на каждый из 3 навыков.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Все 3 пути | Реальные part-context и HBS | skillPath2/3 дали по 12 флагов; путь 1 с 2 заполненными навыками —74 formGroup | Это записи полей, не полноценные DOM-элементы Foundry |
| Соответствие данных | Переданные schema/skill | Полные system.skillPathN.skillM пути | Не запись модели |

## Непроверенные участки и открытые вопросы

В TASK-0004.008 текущий файл и его связи сопоставлены с датированными протоколами TASK-0003.018/.019 (2026-09-10) и .038 (2026-09-11), в пределах относящихся к нему сценариев. Новых поведенческих запусков нет; прежние настоящие модели/методы и фасады различены в протоколе. Браузерный submit, мир, сеть и запись в БД не проверены. Установлены процессы R008-06, R008-07, R008-20; оставшиеся границы: [U008-01](../../../../../../../cross-check-0002.md#u008-01). Полный пофайловый разбор соседей в TASK-0003 не равен проверке клиентского lifecycle.

## Связанные проблемы

[issue-00110](../../../../../../../../../issues/potential/issue-00110.md), [issue-00112](../../../../../../../../../issues/potential/issue-00112.md). Связанные проблемы находятся в адресации нижнего редактора и отсутствии definingSkill в наборе частей.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.019 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.

## Сквозная сверка TASK-0004.008

2026-09-14; rusbar-main, f96434101e0e827838c2e6a3e09da8933a9801ef. Исходник совпадает со срезом TASK-0001; изменено только описание.

Один PARTS-шаблон переиспользуется для трёх путей и каждый раз включает три skillPathSkillPart с их полями/данными. definingSkill не проходит через эту схему вкладок.

Сопоставленные определения и потребители: [module/item/sheets/configurations/WitcherProfessionConfigurationSheet.js](../../../../../../module/item/sheets/configurations/WitcherProfessionConfigurationSheet.js.md), [module/data/item/templates/professionPathData.js](../../../../../../module/data/item/templates/professionPathData.js.md), [templates/sheets/item/configuration/partials/profession/skillPathSkillPart.hbs](skillPathSkillPart.hbs.md), [module/setup/handlebars.js](../../../../../../module/setup/handlebars.js.md).

[Протокол и границы](../../../../../../../review-log.md#task-0004008) — TASK-0004.008; процессы [R008-06](../../../../../../../cross-check-0002.md#r008-06), [R008-07](../../../../../../../cross-check-0002.md#r008-07), [R008-20](../../../../../../../cross-check-0002.md#r008-20). В этой порции выполнена статическая сверка; прежние опыты сохраняют свои даты и фасады. Новых поведенческих запусков нет; браузер, мир, сеть и запись в БД не запускались.
