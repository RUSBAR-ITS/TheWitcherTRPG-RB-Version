# module/item/sheets/WitcherSpellSheet.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/item/sheets/WitcherSpellSheet.js](../../../../../../../module/item/sheets/WitcherSpellSheet.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `a29234e7c42ef5f9d8095c2b5470e5e3c95824cc` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.021](../../../../../../tasks/task-0003.021.md), 13 файлов, 936 логических строк |
| Запись перекрёстной сверки | [TASK-0003.021](../../../../review-log.md#task-0003021) |

## Назначение файла

Специализированный редактор spell. Добавляет словари вариантов и использует конфигурацию боевых/региональных свойств заклинания.

## Условия использования

registerSheets регистрирует лист по умолчанию для Item spell. Создание экземпляра заменяет базовую configuration экземпляром WitcherSpellConfigurationSheet. PARTS.main загружает основной HBS; контекст формируется асинхронно.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| WitcherSpellSheet | default class; 5–65 | Наследник WitcherItemSheet | Items.registerSheet, type spell | Открытие/рендер формы |
| configuration | Поле экземпляра; 6 | WitcherSpellConfigurationSheet({document: this.item}) | this.configuration | configureItem родителя открывает это окно |
| static PARTS.main | template/scrollable; 8–13 | spell-sheet.hbs | ApplicationV2 PARTS | Рендер основной секции |
| selects.class | createSelects; 25–30 | Spells, Invocations, Witcher, MagicalGift | context.selects | Ключи сохранённых классов |
| selects.levelSpell/levelMagicalGift | 31–39 | novice/journeyman/master; minor gift/major gift | context.selects | Выбор условно по классу |
| selects.sourceElements/sourceClass/domain/templateType | 40–62 | mixedElements/earth/air/fire/Water; druid/preacher/arch priest; basic/alternate; rect/circle/cone/ray/emanation | context.selects | Подписи — ключи локализации; Water — с заглавной буквы |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| async _prepareContext(options) | Базовый sheet context | Promise контекста | await super; context.selects=createSelects; return | Записи Item нет |
| createSelects() | Нет | Новый объект 7 словарей | Возвращает статические значения вариантов | Не проверяет текущие значения и не задаёт значения по умолчанию модели |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| WitcherItemSheet | [module/item/sheets/WitcherItemSheet.js](../../../../../../../module/item/sheets/WitcherItemSheet.js) | Импорт/наследование | Базовый контекст, submitOnChange, configureItem, DragDrop и _onRender | Родитель прочитан; собственный createSelects дополняет контекст |
| CONFIG.WITCHER; ключи WITCHER.* | [module/setup/config.js](../../../../../../../module/setup/config.js) | Контекст через родителя | config для полей/вариантов | _prepareContext в базовом листе |
| localize/selectOptions | Foundry14.367.0 /opt/foundryvtt/client/applications/handlebars.mjs; Handlebars4.7.9 | Внешний UI | Варианты передаются HBS | Настоящий HBS; фасады helpers/ItemSheetV2, полный браузер не запускался |
| Ключи подписей | [lang/en.json](../../../../../../../lang/en.json); [lang/ru.json](../../../../../../../lang/ru.json) | Локализация | Значения createSelects | JSON en/ru проверены с раскрытием dotted ключей |
| WitcherSpellConfigurationSheet | [module/item/sheets/configurations/WitcherSpellConfigurationSheet.js](../../../../../../../module/item/sheets/configurations/WitcherSpellConfigurationSheet.js) | Импорт/создание | configuration | Сверены наследование и PARTS |
| spell-sheet.hbs | [templates/sheets/item/spell-sheet.hbs](../../../../../../../templates/sheets/item/spell-sheet.hbs) | PARTS.main | Основная форма | Путь и поля сверены |
| SpellData | [module/data/item/spellData.js](../../../../../../../module/data/item/spellData.js) | Косвенная модель | context.item.system | Все используемые обычные поля найдены; исключение clickableImage — общий issue |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/setup/registerSheets.js](../../../../../../../module/setup/registerSheets.js) | WitcherSpellSheet | Импорт и регистрация | 12, 76–78 |
| [templates/sheets/item/spell-sheet.hbs](../../../../../../../templates/sheets/item/spell-sheet.hbs) | context/selects | Основная форма | Полный разбор |
| [templates/partials/spell-header.hbs](../../../../../../../templates/partials/spell-header.hbs) | class/level/source selects | Partial в основной форме | Полный разбор |

Область поиска: module/ и templates/ текущего checkout; регистрация сверена с system.json. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Создаёт UI-контекст и конфигурацию; собственных обработчиков сохранения, броска и эффектов нет. DEFAULT_OPTIONS, действия и форма наследуются. Значения sourceElements и поля модели — самостоятельные контракты: ключ Water отображается как water, а castSpell формирует ключ WITCHER.Spell.Water.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Наследование/контекст | Группа 10; настоящие классы системы, фасад ItemSheetV2 | selects и showConfig доступны; configuration специализирована | Нет реального оконного DOM |
| Условная форма | Группы 11, 13, 15 | Проверены 4 класса ×2 режима STA и все признаки; русской emanation нет; сгенерированный Water-ключ не разрешается | Обычные helpers локализации/select/formGroup подменены по контракту |

## Непроверенные участки и открытые вопросы

Все 65 строк прочитаны. Живой submit, FilePicker и регионы не запускались; дополнительные данные миров/модулей вне области поиска.

## Связанные проблемы

[issue-00062](../../../../../../issues/potential/issue-00062.md), [issue-00063](../../../../../../issues/potential/issue-00063.md), [issue-00074](../../../../../../issues/potential/issue-00074.md), [issue-00075](../../../../../../issues/potential/issue-00075.md), [issue-00133](../../../../../../issues/potential/issue-00133.md), [issue-00134](../../../../../../issues/potential/issue-00134.md), [issue-00137](../../../../../../issues/potential/issue-00137.md). 137 относится к словарям; 63/74/75/133/134 — связанные маршруты. issue-00062 сопоставлена: специальная spellGeneral включает attackOptionsPart с правильной подписью, поэтому ошибка общей general сюда не переносится.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `a29234e7c42ef5f9d8095c2b5470e5e3c95824cc`; полный файл | Первая карточка; [сверка порции](../../../../review-log.md#task-0003021) |
