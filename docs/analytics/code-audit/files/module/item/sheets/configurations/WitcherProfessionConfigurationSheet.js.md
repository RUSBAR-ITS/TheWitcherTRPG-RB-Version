# module/item/sheets/configurations/WitcherProfessionConfigurationSheet.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/item/sheets/configurations/WitcherProfessionConfigurationSheet.js](../../../../../../../../module/item/sheets/configurations/WitcherProfessionConfigurationSheet.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `c26eb64dd54cc434087f54c3c6b678b6092b15a2` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.019](../../../../../../../tasks/task-0003.019.md), одна порция из двенадцати файлов |
| Запись перекрёстной сверки | [TASK-0003.019](../../../../../review-log.md#task-0003019) |

## Назначение файла

Конфигурация профессии: три вкладки путей, поля навыков, CRUD предметных воздействий и порогов с поиском по имени.

## Условия использования

Default class WitcherProfessionConfigurationSheet extends WitcherConfigurationSheet. Создаётся специализированным основным листом для того же Item. Наследует контекст item/systemFields/config/effects и CRUD ActiveEffect; это отдельный механизм от редактирования skillAttack.damageProperties.effects.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| Класс | 3–212 | Специализированный редактор | Default export | 11 собственных методов |
| DEFAULT_OPTIONS.actions | 5–12 | 4 регистрации | addEffectDamageProperties/removeEffect/addThreshold/removeThreshold | Фактическое removeEffect не совпадает с HBS |
| PARTS | 14–31 | 4 общих части и 3 пути | Spread super.PARTS + skillPath1–3 | Один skillPathPart.hbs для каждого пути |
| TABS.primary | 33–44 | 5 вкладок | general,3 пути,activeEffects; initial general | labelPrefix WITCHER.Item.Settings; названия путей заменяются данными |
| partContext | 61–65 | config/tab/partId | Локально | Ветки добавляют skillPathFields/skillPath |
| SkillObject | Возврат find* | {skill,path} | Внутренний результат | Путь используется в update; ID навыка отсутствует |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| _prepareTabs(group):48–58 | Конфигурация tabs/Item | Объект вкладок super | Для primary заменяет 3 label на pathName | Синхронно; пустые названия остаются пустыми; локальный system не используется |
| async _preparePartContext(partId,context,options):60–90 | context.tabs/item/systemFields | Для пути 5 ключей; иначе исходный context | Сопоставляет partId с данными/SchemaField skillPath1–3 | Не зовёт super; definingSkill ветви нет |
| _onChangeForm(formConfig,event):92–100 | event.target.dataset.action | Не возвращает результат записи | super; editEffectDamageProperties→метод; editThreshold→метод | Общий submit и спецupdate не ожидаются этим методом |
| static async _onAddEffectDamageProperties(event,element):102–111 | data-target=skillName | Promise<void> | preventDefault;find;randomID;update effects.<id>={percentage:0} | Не ожидает update; неизвестное имя→TypeError path |
| async _onEditEffectDamageProperties(event,element):114–130 | closest.list-item id/target;field/value | Promise<void> | value=='on'→checked;update effects.<id>.<field> | Проверяется содержимое, не type. update не ожидается |
| static async _oRemoveEffectDamageProperties(event):133–142 | event.currentTarget.closest.list-item | Promise<void> | Находит имя/ID; update effects.-=<id>:null | Не использует element из ApplicationV2; update не ожидается |
| static async _onAddThreshold(event,element):144–153 | data-target имя | Promise<void> | randomID; update thresholds.thresholds.<id>={value:0} | Update без await |
| async _onEditThreshold(event,element):155–168 | row id/target;field/value | Promise<void> | update thresholds.thresholds.<id>.<field>=value | value остаётся строкой до очистки схемой; без await |
| static async _oRemoveThreshold(event,element):170–179 | row id/target через element | Promise<void> | update thresholds.thresholds.-=<id>:null | Второй аргумент используется; без await. Закомментированный v14-вариант не исполняется |
| findSkillWithName(skillName):182–197 | document.system | {skill,path} либо undefined | Порядок путей 1→2→3; успешный findInPath повторяется | definingSkill не проверяется; выбирается первое совпадение, включая пустую строку |
| findSkillWithNameInSkillPath(skillPath,skillName):199–211 | Путь/имя | {skill,path:'skillN'} либо null | Сравнение === для skill1→2→3 | Никакой уникальности/ID; отсутствующий skillPath не защищён |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| WitcherConfigurationSheet | [module/item/sheets/configurations/WitcherConfigurationSheet.js](../../../../../../../../module/item/sheets/configurations/WitcherConfigurationSheet.js) | Import/extends/super | 1/3/15/48/93 | Общие tabs/контекст/ActiveEffect |
| skillPathPart | [templates/sheets/item/configuration/partials/profession/skillPathPart.hbs](../../../../../../../../templates/sheets/item/configuration/partials/profession/skillPathPart.hbs) | PARTS.main путей | 18/23/28 | Три применения одного HBS |
| ProfessionData / professionPath / professionSkill | [module/data/item/professionData.js](../../../../../../../../module/data/item/professionData.js); [module/data/item/templates/professionPathData.js](../../../../../../../../module/data/item/templates/professionPathData.js); [module/data/item/templates/professionSkillData.js](../../../../../../../../module/data/item/templates/professionSkillData.js) | Поля Item/schema | 51–86/поиск | Реальные схемы и контекст |
| DamageProperties.effects/itemEffect | [module/data/item/templates/combat/damagePropertiesData.js](../../../../../../../../module/data/item/templates/combat/damagePropertiesData.js); [module/data/item/templates/itemEffectData.js](../../../../../../../../module/data/item/templates/itemEffectData.js) | Пути update | 102–142 | TypedObjectField, percentage/имя/статус; не ActiveEffect |
| Threshold | [module/data/item/templates/profession/thresholdData.js](../../../../../../../../module/data/item/templates/profession/thresholdData.js) | Пути update | 144–179 | TypedObjectField с name/value |
| CONFIG.WITCHER | [module/setup/config.js](../../../../../../../../module/setup/config.js) | Global | 62 и HBS-варианты | statOptions готовит основной лист; statusEffects/attackOptions |
| randomID/Item.update/ApplicationV2 | Foundry 14.367.0, /opt/foundryvtt/client/applications/api/application.mjs; common/utils/helpers.mjs; client/applications/api/document-sheet.mjs | ID/запись/события | CRUD/делегированный click | Core #onClickAction передаёт(event,target); исполнено извлечённое тело |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/item/sheets/WitcherProfessionSheet.js](../../../../../../../../module/item/sheets/WitcherProfessionSheet.js) | Класс | new configuration | Импорт 2/поле 11 |
| [templates/sheets/item/configuration/partials/profession/skillPathPart.hbs](../../../../../../../../templates/sheets/item/configuration/partials/profession/skillPathPart.hbs) | skillPathFields/skillPath/tab/partId | Контекст трёх путей | Полный HBS |
| [templates/sheets/item/configuration/partials/profession/skillPathSkillPart.hbs](../../../../../../../../templates/sheets/item/configuration/partials/profession/skillPathSkillPart.hbs) | 6 data-action и data-id/target/field | Кнопки/изменения | removeEffectDamageProperties не зарегистрирован |
| [templates/sheets/item/configuration/tabs/activeEffectConfiguration.hbs](../../../../../../../../templates/sheets/item/configuration/tabs/activeEffectConfiguration.hbs) | Унаследованные create/toggle/edit/delete | Отдельный редактор ActiveEffect | 4 категории контекста |
| [templates/sheets/item/configuration/tabs/general.hbs](../../../../../../../../templates/sheets/item/configuration/tabs/general.hbs) | Унаследованные общие поля | General пуст для ProfessionData | В модели нет корневых attack/damage/defense |

Область поиска: текущие module/ и templates/; регистрации сверены отдельно. Динамические обращения внешних модулей не исследовались.

## Данные и изменения состояния

Добавляет/правит/удаляет вложенные записи system, не создаёт отдельный ActiveEffect этими шестью CRUD-методами. ActiveEffect обслуживают унаследованные actions. Именованные formGroup формируют полный путь из DataField; ручные строки effects/thresholds не имеют name и сохраняются специальным change-handler.

Маршрутизация по skillName делает одноимённые/пустые навыки неоднозначными. Отключение признаков скрывает поля, но не удаляет данные. Пустое имя пути не заменяется порядковым названием. Схема definingSkill поддерживает те же настройки, но конфигурация его не содержит.

Все 6 async CRUD вернулись до разрешения update. Кнопка removeEffectDamageProperties ушла в fallback core без записи; метод под именем removeEffect дополнительно ожидает неверный currentTarget. Это два препятствия одной цепочки удаления.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Контекст/части | Реальные _prepareTabs/_preparePartContext и HBS | General0 полей;3 пути;5 вкладок;4 категории AE; definingSkill отсутствует | UI-фасад |
| CRUD/pending | 6 настоящих методов | Верные пути выбранного первого навыка; add/delete ID; edit value строка;все returned while pending | Promise записи перехвачен и затем разрешён |
| Удаление/click | Реальный core dispatcher | Штатное действие без handler→0 update; прямой remove с currentTarget приложения→TypeError | DOM события смоделированы |
| Имя/строка on | find+edit | Dup→первый путь; текст on→false; unknown→TypeError | Прямые методы/модели, не сохранение в мире |

## Непроверенные участки и открытые вопросы

Исходник прочитан полностью. Системные классы листов настоящие, ItemSheetV2/HandlebarsApplicationMixin работают поверх DocumentSheet-фасада. Рендер проверяет контекст/поля и маршруты; реальный браузер, права, сохранение Item и работа нескольких клиентов не проверены.

## Связанные проблемы

[issue-00060](../../../../../../../issues/potential/issue-00060.md), [issue-00110](../../../../../../../issues/potential/issue-00110.md), [issue-00111](../../../../../../../issues/potential/issue-00111.md), [issue-00112](../../../../../../../issues/potential/issue-00112.md), [issue-00120](../../../../../../../issues/potential/issue-00120.md). Наблюдения не подтверждены пользователем, код не исправлялся.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.019 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.
