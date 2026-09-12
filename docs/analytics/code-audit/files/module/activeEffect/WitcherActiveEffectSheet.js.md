# module/activeEffect/WitcherActiveEffectSheet.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/activeEffect/WitcherActiveEffectSheet.js](../../../../../../module/activeEffect/WitcherActiveEffectSheet.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `247d3d86e344238a1445377c686eb6455146693c` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.010](../../../../../tasks/task-0003.010.md), одна порция из восьми файлов |
| Запись перекрёстной сверки | [TASK-0003.010](../../../review-log.md#task-0003010) |

## Назначение файла

Расширяет ActiveEffectConfig ядра: системная вкладка, кнопка мастера выбора путей изменений и автодополнение ключей по схемам зарегистрированных моделей.

## Условия использования

[module/setup/registerSheets.js](../../../../../../module/setup/registerSheets.js) снимает регистрацию core ActiveEffectConfig и назначает WitcherActiveEffectConfig листом по умолчанию без фильтра types. Класс наследует ActiveEffectConfig Foundry 14.367; рендер использует существующего родителя Actor/Item. Модели и применение эффектов описаны в TASK-0003.009; здесь не вводится новый вычислитель бонусов.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| WitcherActiveEffectConfig | Именованный export class; 6–138 | Конфигурация документа | DocumentSheetConfig.registerSheet | Наследует ядро, расширен двумя Object.assign |
| DialogV2 | Константа; 4 | Ссылка на API диалога | Локальная | Используется wizardAction |
| DEFAULT_OPTIONS | Static; 7–11 | actions.wizard | Действие ApplicationV2 | Указывает на static wizardAction |
| PARTS | Static; 14–29 | Семь частей формы | header/tabs/details/duration/changes/systemSpecific/footer | Только systemSpecific — системный шаблон; у changes есть вложенный change.hbs |
| TABS | Static; 31–36 | Копия super.TABS.sheet + systemSpecific | Группа sheet | Сохраняет базовые вкладки и их настройки |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| _prepareContext; 39–43 | options; родительская подготовка | Контекст | Добавляет document.system.schema.fields как systemFields | await super; без записи |
| _onRender; 45–57 | context, options, this.element | undefined | super; autocomplete(); создаёт a[data-action=wizard] с иконкой и вставляет за кнопкой addChange | Не ждёт autocomplete; нет проверки addButton или удаления ранее вставленного элемента |
| static wizardAction; 59–97 | Контекст экземпляра; document.type | Promise<undefined> | base → getActiveEffectsBasePaths; temporaryItemImprovement → getActiveEffectsItemImprovementPaths; рендерит wizard и открывает prompt | Ждёт renderTemplate, не prompt/update. Callback делит выбранную строку по запятым, push({key}) в document.system.changes, update({changes:newChanges}) |
| autocomplete; 99–137 | Родитель Actor/Item; секция changes | Promise<undefined> | Обходит schema.apply всех dataModels выбранного реестра, исключает SchemaField, собирает fieldPath/label, сортирует и добавляет datalist | Не фильтрует фактический тип или transfer; единый id attribute-key-list; нет очистки предыдущего datalist и защиты parent=null |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| baseMixin | [module/activeEffect/mixins/baseMixin.js](../../../../../../module/activeEffect/mixins/baseMixin.js) | ES-import/Object.assign | Восемь методов подсказок Actor | Первое подключение, 140 |
| temporaryItemImprovementMixin | [module/activeEffect/mixins/temporaryItemImprovementMixin.js](../../../../../../module/activeEffect/mixins/temporaryItemImprovementMixin.js) | ES-import/Object.assign | Два метода подсказок Item | Второе подключение, 141; пересечений имён нет |
| ActiveEffectConfig, DEFAULT_OPTIONS/TABS, _prepareContext/_onRender | Внешнее ядро /opt/foundryvtt/client/applications/sheets/active-effect-config.mjs; DocumentSheetV2 | Наследование | Стандартные поля, действия addChange/deleteChange, обработка формы | Собственные методы не заменяют ядровой submit |
| Core PARTS templates | /opt/foundryvtt/templates/sheets/active-effect/{header,details,duration,changes,change}.hbs; templates/generic/{tab-navigation,form-footer}.hbs | Пути PARTS | Вся стандартная форма и строки key/type/value/phase/priority | Внешние файлы, не строки реестра системы |
| Системные шаблоны | [templates/dialog/activeEffects/wizard.hbs](../../../../../../templates/dialog/activeEffects/wizard.hbs); [templates/sheets/activeEffect/system-specific.hbs](../../../../../../templates/sheets/activeEffect/system-specific.hbs) | renderTemplate и PARTS | Выбор пути и поля apply* | Содержимое полностью разобрано в этой порции |
| CONFIG.Actor/Item.dataModels и SchemaField | [module/setup/registerDataModels.js](../../../../../../module/setup/registerDataModels.js); /opt/foundryvtt/common/data/fields.mjs | Обход schema.apply | fieldPath уже содержит system.; label локализуется | 4 модели Actor, 22 Item; проверены реальные схемы |
| DialogV2, DOM, game.i18n.localize | Внешний Foundry/браузер | Диалог и datalist | button.form.elements.path, querySelector, createElement | В изолированном запуске DOM и prompt подменены |
| Document.update / cleanData; _preUpdate | [module/activeEffect/witcherActiveEffect.js](../../../../../../module/activeEffect/witcherActiveEffect.js); /opt/foundryvtt/client/data/client-backend.mjs | Сохранение/миграция | Legacy changes очищается в system.changes до _preUpdate; системный hook назначает phase | Настоящий cleanData и исходный hook выполнены |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/setup/registerSheets.js](../../../../../../module/setup/registerSheets.js) | WitcherActiveEffectConfig | Регистрация листа по умолчанию для ActiveEffect | Импорт и registerSheet |
| ApplicationV2 ядра | PARTS/TABS/actions/hooks | Вызов подготовки, рендера, wizard по data-action | Стандартная диспетчеризация |
| [module/actor/sheets/mixins/activeEffectMixin.js](../../../../../../module/actor/sheets/mixins/activeEffectMixin.js); [module/item/sheets/configurations/WitcherConfigurationSheet.js](../../../../../../module/item/sheets/configurations/WitcherConfigurationSheet.js) | effect.sheet.render(true) | Косвенное открытие зарегистрированного листа | Ветвь edit; класс не импортируется этими обработчиками напрямую |

## Данные и изменения состояния

Мастер выбирает только пути: он не спрашивает значение, операцию, приоритет или ограничение характеристики. Группа навыков сериализуется в строку с запятыми, после чего создаётся несколько строк changes. Существующий массив подготовленной модели меняется немедленно через push. Мастер не читает несохранённые поля основной формы; ядровая кнопка addChange, напротив, использует FormDataExtended и submit.

update получает старый корневой changes. В текущем ядре cleanData с migrate/partial переводит его в system.changes и достраивает type=add, value='', phase=initial. Нельзя считать этот путь заведомо неработающим только по устаревшему имени. Отсутствие applyAfterCalculations в payload приводит к уже известной issue-00043.

Автодополнение выбирает реестр по document.parent.documentName; даже base Item-эффект с transfer=true получает подсказки Item. Реальные fieldPath уже имеют префикс system.; предположение об отсутствии префикса опровергнуто проверкой. Разные типы внутри реестра объединяются, совпадающий ключ перезаписывает label. schema.apply без данных не раскрывает произвольные ключи TypedObjectField. Результат не является списком всех допустимых вычисляемых путей.

isItemEffect предоставляется ядром при подготовке details. HandlebarsApplicationMixin использует общий контекст частей, поэтому при обычном полном рендере этот флаг доступен systemSpecific. Частичный рендер требует отдельного учёта состава частей.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Полнота | 141 строка; 4 собственных метода, 3 static-конфигурации и 2 примеси/10 методов | Имена и пути сопоставлены с определениями и регистрацией | Соседние листы целиком не разбирались |
| Подсказки | Настоящие схемы всех зарегистрированных Actor/Item в Node | 718 ключей Actor и 701 Item; все с system.; Item не предлагает system.stats.ref.totalModifiers, но предлагает system.damage | DOM-список подменён; не браузер |
| Мастер/сохранение | Исходный wizardAction, настоящая модель, cleanData и _preUpdate; update перехвачен | При исходном value=1 и несохранённом 9 отправлено 1; добавлены два {key}; подготовленный массив 1→3, source остаётся длиной1 до записи; phase initial | БД, реальная форма и сетевой submit не выполнялись |
| Рендер | Два вызова исходного _onRender на сохранённом DOM | 2 кнопки wizard и 2 datalist | Модель частичного рендера; не утверждение о каждом полном рендере |
| Системная вкладка | Настоящий formGroup с отсутствующим полем Temporary-модели | Записана ошибка Non-existent data field; возвращена пустая строка | Остальные input отрисованы фасадом; полной формы браузера нет |

## Непроверенные участки и открытые вопросы

Не выполнялись реальная навигация/submit, динамические модули и несколько открытых окон; общий id datalist требует отдельной проверки в браузере. Неподдерживаемый type и parent=null не защищены, но штатный сценарий таких документов не устанавливался. Кнопка мастера и autocomplete предполагают наличие части changes.

## Связанные проблемы

[issue-00051](../../../../../issues/potential/issue-00051.md), [issue-00052](../../../../../issues/potential/issue-00052.md), [issue-00053](../../../../../issues/potential/issue-00053.md), [issue-00055](../../../../../issues/potential/issue-00055.md) — схема получателя, несохранённая форма, отсутствующее поле, повторный рендер. [issue-00043](../../../../../issues/potential/issue-00043.md) дополнена реальным путём wizard → cleanData → _preUpdate.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.010 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.

## Уточнение TASK-0003.011

2026-09-10, `07237960627bf7debc2b4283aa55d1a8c5d1bb8b`; содержимое исходника совпадает с предыдущим срезом.

Подтверждён вход из [Item-конфигурации](../item/sheets/configurations/WitcherConfigurationSheet.js.md): action edit получает effect по ID текущего Item и вызывает effect.sheet.render(true), выбор класса обеспечен registerSheets. Создание FX в конфигурации и перенос FX в основной лист Item — разные маршруты: первое передаёт type/name/icon/origin/duration/disabled, второе использует core _onDropActiveEffect и object-копию при допустимом владельце. Сам мастер/автодополнение этим не менялись.

[TASK-0003.011 — сценарии и сверка](../../../review-log.md#task-0003011).

## Дополнительная сверка TASK-0003.047

2026-09-12, rusbar-main, 2f94c6c29e298ccf73d67ccc2e5fb8fc358dae2c; исходники не изменены.

[activeEffect.css](../../styles/activeEffect.css.md) оформляет общий список effect-part, который открывает этот редактор через edit; его название не означает, что он задаёт core таблицу changes. Три [фабрики modifier-полей](../data/item/templates/effectStatData.js.md) не используются мастером. Группа 05 исполнила getStatSuggestions/getSkillSuggestions: пути system.stats.int.totalModifiers и system.skills.emp.charisma.activeEffectModifiers формируются отдельно. Существующий путь wizard → legacy changes → core cleanData → system.changes, уточнённый ранее, не переоценивался как ошибка из-за имени поля.

[Сценарии, результаты и ограничения](../../../review-log.md#task-0003047). Связанные файлы повторно не засчитываются в покрытие.

## Дополнительная сверка TASK-0003.051

2026-09-12, rusbar-main, 4b9951094106e26d9274bbd5d5e8e7a709cfcf24. Исходник не менялся.

Системная вкладка добавляет id=systemSpecific к TABS.sheet и наследует ядровой labelPrefix=EFFECT.TABS; так возникает ключ EFFECT.TABS.systemSpecific, присутствующий в [en](../../lang/en.json.md) и [ru](../../lang/ru.json.md). _prepareContext передаёт systemFields, а system-specific.hbs запрашивает formGroup applyAfterCalculations с localize=true. У этой подписи нет ru-строки ([docs/issues/potential/issue-00318.md](../../../../../issues/potential/issue-00318.md)); настоящий localize возвращает английский fallback. Это не изменение мастера, фаз или сохранения.

[Результаты и ограничения сверки](../../../review-log.md#task-0003051). Правки относятся к документации; мир, браузер, БД и исходники не менялись.
