# module/data/item/hexData.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/data/item/hexData.js](../../../../../../../module/data/item/hexData.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `a29234e7c42ef5f9d8095c2b5470e5e3c95824cc` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.021](../../../../../../tasks/task-0003.021.md), 13 файлов, 936 логических строк |
| Запись перекрёстной сверки | [TASK-0003.021](../../../../review-log.md#task-0003021) |

## Назначение файла

Модель system предмета hex: описательные параметры порчи, стоимость, требование снятия и допустимые способы защиты цели.

## Условия использования

CONFIG.Item.dataModels.hex регистрируется в registerDataModels; WitcherItem.migrateSpells переводит прежний class='Hexes' в type='hex'. Форма и Actor.castSpell читают модель.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| HexData | default class; 6–29 | Наследует CommonItemData | CONFIG.Item.dataModels.hex | Схема и выбор навыка |
| danger, stamina, effect, liftRequirement | String'' / Number0 / String'' / String''; 12–16 | Опасность, STA, описание и снятие | system.* | Ввод редактора; danger не ограничен choices |
| defenseOptions() | Spread фабрики; 18 | Множество способов защиты цели | system.defenseOptions | Не определяет собственную isApplicableDefense |
| fields; commonData | Локальные ссылки; 4, 8 | API и схема родителя | Локально | Чтение при defineSchema |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| static defineSchema() | CommonItemData и CONFIG.defenseOptions | Объект схемы | Дополняет общие 8 полей четырьмя и defenseOptions | Без записи |
| getUsedSkill() | parent.type; возможные spellAttackSkill/class | Объект навыка | skillMap → magic[parent.type]?.skill → magic[class].skill | При нормальном type hex выбирает hexweave; spellAttackSkill/class не объявлены в схеме; неверный parent может привести к TypeError |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| CommonItemData | [module/data/item/commonItemData.js](../../../../../../../module/data/item/commonItemData.js) | Импорт/наследование | defineSchema | Прочитана схема |
| defenseOptions | [module/data/item/templates/combat/defenseOptionsData.js](../../../../../../../module/data/item/templates/combat/defenseOptionsData.js) | Импорт/фабрика | defineSchema | Результат SetField; 6 начальных вариантов |
| CONFIG.WITCHER.magic/skillMap | [module/setup/config.js](../../../../../../../module/setup/config.js) | Глобальный реестр | getUsedSkill | magic.hex.skill=skillMap.hexweave |
| foundry.data.fields | Foundry14.367.0, common/data/fields.mjs | Внешний API | Схема и очистка | Настоящие поля в Node |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/setup/registerDataModels.js](../../../../../../../module/setup/registerDataModels.js) | HexData | Регистрация hex | 24, 62 |
| [module/item/sheets/WitcherHexSheet.js](../../../../../../../module/item/sheets/WitcherHexSheet.js) | system.danger/stamina/effect/liftRequirement | Контекст формы | _prepareContext |
| [templates/sheets/item/hex-sheet.hbs](../../../../../../../templates/sheets/item/hex-sheet.hbs) | Поля порчи | Форма | Полный разбор |
| [module/item/witcherItem.js](../../../../../../../module/item/witcherItem.js) | Тип hex; отсутствие attackOptions | migrateSpells/getItemAttack | type migration; getItemAttack возвращает none при отсутствии набора |
| [module/actor/mixins/castSpellMixin.js](../../../../../../../module/actor/mixins/castSpellMixin.js) | getUsedSkill/stamina/defenseOptions | Чтение в общем процессе магии | 27–32 и сообщение атаки |

Область поиска: module/ и templates/ текущего checkout; регистрация сверена с system.json. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Общая модель даёт описание/количество/вес/стоимость/книгу и флаги хранения. Собственных attackOptions, defenseProperties, областей, selfEffects/onCastEffects, миграций и методов изменения документов нет. getUsedSkill читает отсутствующие собственные поля, но нормальный type hex обеспечивает fallback. Встроенные ActiveEffect находятся на Item, вне этой схемы.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Нормальный экземпляр | Группы 01–02 | hexweave, defenseOptions6; isApplicableDefense отсутствует; canHaveTemporaryItemImprovement=false | Без документа Item и запуска порчи |
| Форма | Группы 10, 12, 15 | Поле Medium выбрано; требование снятия отображается; danger-подписи не разрешаются в en/ru | UI и локализация смоделированы через настоящий HBS |

## Непроверенные участки и открытые вопросы

Все 29 строк прочитаны. Полный castSpell, снятие порчи, игровые правила и влияние ActiveEffect не исследованы этой карточкой.

## Связанные проблемы

[issue-00063](../../../../../../issues/potential/issue-00063.md), [issue-00136](../../../../../../issues/potential/issue-00136.md), [issue-00137](../../../../../../issues/potential/issue-00137.md). 63 касается общего поля картинки; 136 — маршрут редактирования изображения в форме; 137 — ключи подписей опасности.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `a29234e7c42ef5f9d8095c2b5470e5e3c95824cc`; полный файл | Первая карточка; [сверка порции](../../../../review-log.md#task-0003021) |
