# templates/sheets/item/configuration/partials/profession/skillPathPart.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/sheets/item/configuration/partials/profession/skillPathPart.hbs](../../../../../../../../../../templates/sheets/item/configuration/partials/profession/skillPathPart.hbs) |
| Тип файла | Handlebars, HTML-шаблон |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `c26eb64dd54cc434087f54c3c6b678b6092b15a2` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.019](../../../../../../../../../tasks/task-0003.019.md), одна порция из двенадцати файлов |
| Запись перекрёстной сверки | [TASK-0003.019](../../../../../../../review-log.md#task-0003019) |

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

Исходник прочитан полностью. Системные классы листов настоящие, ItemSheetV2/HandlebarsApplicationMixin работают поверх DocumentSheet-фасада. Рендер проверяет контекст/поля и маршруты; реальный браузер, права, сохранение Item и работа нескольких клиентов не проверены.

## Связанные проблемы

[issue-00110](../../../../../../../../../issues/potential/issue-00110.md), [issue-00112](../../../../../../../../../issues/potential/issue-00112.md). Связанные проблемы находятся в адресации нижнего редактора и отсутствии definingSkill в наборе частей.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.019 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.
