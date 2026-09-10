# module/setup/settings.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/setup/settings.js](../../../../../../module/setup/settings.js) |
| Тип файла | JavaScript — настройки |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `3252300787c348e11f95098c345a6af7704b690c`; исходник совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f` |
| Изменения относительно коммита | Нет |
| Задача и порция | [TASK-0002](../../../../../tasks/task-0002-system-initialization.md); порция 3 |
| Запись перекрёстной сверки | [Журнал сверок](../../../review-log.md) — TASK-0002, порция 3 |

## Назначение файла

Регистрирует девять мировых настроек и формирует варианты выбора Item-компедиума травм.

## Условия использования

[module/TheWitcherTRPG.js](../../../../../../module/TheWitcherTRPG.js) — обработчик init, вызывает функцию после назначения классов документов. Нужны game.settings, game.packs и StringField Foundry; импорт не регистрирует настройки сам.

## Введённые сущности и действия с ними

| Ключ | Тип / default | Назначение | name / hint |
| --- | --- | --- | --- |
| criticalWoundsPack | StringField / `"TheWitcherTRPG.criticalWounds"` | Выбор pack для индекса/применения критических травм. | `WITCHER.Settings.criticalWoundsPack` / `WITCHER.Settings.criticalWoundsPackDetails` |
| useOptionalAdrenaline | Boolean / `false` | Опциональный адреналин в данных листа и addAdrenaline. | `WITCHER.Settings.Adrenaline` / `WITCHER.Settings.AdrenalineDetails` |
| useOptionalVerbalCombat | Boolean / `false` | Опциональный вербальный бой в контексте листа. | `WITCHER.Settings.useVerbalCombatRule` / `WITCHER.Settings.useVerbalCombatRuleHint` |
| silverTrait | Boolean / `false` | Вариант обработки серебра и отображения свойств урона. | `WITCHER.Settings.silverTrait` / `WITCHER.Settings.silverTraitHint` |
| displayRollsDetails | Boolean / `false` | Подробности формул бросков и контекст листа. | `WITCHER.Settings.displayRollDetails` / `WITCHER.Settings.displayRollDetailsHint` |
| useWitcherFont | Boolean / `false` | Класс оформления шрифтом при ready. | `WITCHER.Settings.specialFont` / нет |
| displayRep | Boolean / `false` | Отображение репутации в контексте листа. | `WITCHER.Settings.displayReputation` / `WITCHER.Settings.displayReputationHint` |
| clickableImageItemTypes | String / `"valuable"` | CSV типов Item для логики кликабельных картинок. | `WITCHER.Settings.clickableImageItemTypes` / `WITCHER.Settings.clickableImageItemTypesHint` |
| clickableImageCheckboxForGMOnly | Boolean / `true` | Ограничение интерфейса настройки кликабельной картинки мастером. | `WITCHER.Settings.clickableImageCheckboxForGMOnly` / нет |

Все девять: namespace TheWitcherTRPG, scope world, config true. criticalWoundsPack имеет StringField initial/default TheWitcherTRPG.criticalWounds, blank false, nullable false, choices getAllCompendia. Переключение настроек здесь не реализовано: регистрируется их описание.

## Основные функции и методы

| Функция | Вход / результат | Поведение |
| --- | --- | --- |
| registerSettings(), экспорт, стр. 1 | Без аргументов → undefined | Девять вызовов game.settings.register; onChange и requiresReload отсутствуют. |
| getAllCompendia(), локальная, стр. 86 | Без аргументов → объект collection: title | Читает текущую коллекцию packs при вызове choices; фильтрует только documentName === Item. Не проверяет наличие criticalWound внутри pack. |

## Используемые сущности и зависимости

| Сущность | Источник | Вид связи | Назначение / доказательство |
| --- | --- | --- | --- |
| game.settings.register | Foundry | API | Каждый блок registerSettings |
| StringField | foundry.data.fields | API / модель поля | Стр. 7–12: ограничения и callback выбора |
| game.packs | Foundry | Реестр документов | getAllCompendia: documentName, collection, title |
| Ключи WITCHER.Settings.* | [lang/en.json](../../../../../../lang/en.json); [lang/ru.json](../../../../../../lang/ru.json) | Локализация | name/hint перечислены выше; эти два файла содержат соответствующий раздел, полнота всех переводов не заявляется |
| getSetting | [module/setup/handlebars.js](../../../../../../module/setup/handlebars.js) | Косвенное чтение | Зарегистрированный helper читает TheWitcherTRPG + переданный ключ |

## Известные потребители

[module/TheWitcherTRPG.js](../../../../../../module/TheWitcherTRPG.js) — обработчик init, вызывает функцию после назначения классов документов.

| Настройка | Прямые чтения / helper в шаблоне |
| --- | --- |
| criticalWoundsPack | [module/TheWitcherTRPG.js](../../../../../../module/TheWitcherTRPG.js) (стр. 64); [module/actor/mixins/damageMixin.js](../../../../../../module/actor/mixins/damageMixin.js) (стр. 316) |
| useOptionalAdrenaline | [module/actor/mixins/adrenalineMixin.js](../../../../../../module/actor/mixins/adrenalineMixin.js) (стр. 3); [module/actor/sheets/WitcherActorSheet.js](../../../../../../module/actor/sheets/WitcherActorSheet.js) (стр. 61); [module/actor/sheets/WitcherActorSheetV1.js](../../../../../../module/actor/sheets/WitcherActorSheetV1.js) (стр. 27) |
| useOptionalVerbalCombat | [module/actor/sheets/WitcherActorSheet.js](../../../../../../module/actor/sheets/WitcherActorSheet.js) (стр. 63); [module/actor/sheets/WitcherActorSheetV1.js](../../../../../../module/actor/sheets/WitcherActorSheetV1.js) (стр. 29) |
| silverTrait | [module/actor/mixins/damageMixin.js](../../../../../../module/actor/mixins/damageMixin.js) (стр. 163); [module/item/sheets/configurations/WitcherPropertiesConfigurationSheet.js](../../../../../../module/item/sheets/configurations/WitcherPropertiesConfigurationSheet.js) (стр. 48) |
| displayRollsDetails | [module/actor/mixins/castSpellMixin.js](../../../../../../module/actor/mixins/castSpellMixin.js) (стр. 14); [module/actor/mixins/defenseMixin.js](../../../../../../module/actor/mixins/defenseMixin.js) (стр. 131); [module/actor/mixins/modifierMixin.js](../../../../../../module/actor/mixins/modifierMixin.js) (стр. 3); [module/actor/mixins/professionMixin.js](../../../../../../module/actor/mixins/professionMixin.js) (стр. 52); [module/actor/mixins/professionMixin.js](../../../../../../module/actor/mixins/professionMixin.js) (стр. 355); [module/actor/mixins/skillMixin.js](../../../../../../module/actor/mixins/skillMixin.js) (стр. 55); [module/actor/mixins/skillMixin.js](../../../../../../module/actor/mixins/skillMixin.js) (стр. 86); [module/actor/mixins/skillMixin.js](../../../../../../module/actor/mixins/skillMixin.js) (стр. 144); [module/actor/mixins/verbalCombatMixin.js](../../../../../../module/actor/mixins/verbalCombatMixin.js) (стр. 10); [module/actor/mixins/weaponAttackMixin.js](../../../../../../module/actor/mixins/weaponAttackMixin.js) (стр. 8); [module/actor/mixins/weaponAttackMixin.js](../../../../../../module/actor/mixins/weaponAttackMixin.js) (стр. 316); [module/actor/sheets/WitcherActorSheet.js](../../../../../../module/actor/sheets/WitcherActorSheet.js) (стр. 62); [module/actor/sheets/WitcherActorSheetV1.js](../../../../../../module/actor/sheets/WitcherActorSheetV1.js) (стр. 28); [module/actor/sheets/WitcherCharacterSheet.js](../../../../../../module/actor/sheets/WitcherCharacterSheet.js) (стр. 259); [module/actor/sheets/WitcherCharacterSheet.js](../../../../../../module/actor/sheets/WitcherCharacterSheet.js) (стр. 355); [module/item/systems/repair.js](../../../../../../module/item/systems/repair.js) (стр. 211); [module/scripts/helper.js](../../../../../../module/scripts/helper.js) (стр. 78); [module/scripts/verbalCombat/verbalCombatDefense.js](../../../../../../module/scripts/verbalCombat/verbalCombatDefense.js) (стр. 45) |
| useWitcherFont | [module/TheWitcherTRPG.js](../../../../../../module/TheWitcherTRPG.js) (стр. 77) |
| displayRep | [module/actor/sheets/WitcherActorSheet.js](../../../../../../module/actor/sheets/WitcherActorSheet.js) (стр. 64); [module/actor/sheets/WitcherActorSheetV1.js](../../../../../../module/actor/sheets/WitcherActorSheetV1.js) (стр. 30) |
| clickableImageItemTypes | [templates/partials/item-header.hbs](../../../../../../templates/partials/item-header.hbs) (стр. 10); [templates/partials/item-image.hbs](../../../../../../templates/partials/item-image.hbs) (стр. 1); [templates/partials/spell-header.hbs](../../../../../../templates/partials/spell-header.hbs) (стр. 10); [templates/sheets/item/hex-sheet.hbs](../../../../../../templates/sheets/item/hex-sheet.hbs) (стр. 11); [templates/sheets/item/ritual-sheet.hbs](../../../../../../templates/sheets/item/ritual-sheet.hbs) (стр. 7) |
| clickableImageCheckboxForGMOnly | [templates/partials/item-header.hbs](../../../../../../templates/partials/item-header.hbs) (стр. 10); [templates/partials/spell-header.hbs](../../../../../../templates/partials/spell-header.hbs) (стр. 10); [templates/sheets/item/hex-sheet.hbs](../../../../../../templates/sheets/item/hex-sheet.hbs) (стр. 11); [templates/sheets/item/ritual-sheet.hbs](../../../../../../templates/sheets/item/ritual-sheet.hbs) (стр. 7) |

Таблица построена по буквальным вызовам game.settings.get и getSetting. WitcherActorSheetV1 также содержит обращения; это не доказательство использования V1-листа в текущем интерфейсе. Подстановки имени настройки во время выполнения требуют отдельной проверки.

## Данные и изменения состояния

Регистрирует метаданные настроек клиента; функция не вызывает settings.set. getAllCompendia читает packs, возвращает новый объект, не меняет содержимое pack. Отсутствие onChange означает, что непосредственное обновление интерфейса данным файлом не задано.

## Проверки и доказательства

Полностью прочитаны 96 строк. Настоящая registerSettings выполнена в vm с подменой game.settings.register и StringField: получены 9 уникальных настроек. Callback choices вызван на двух фиктивных pack (Item/Actor), вернул только Item. Вызовы потребителей и их контекст сопоставлены поиском по module и templates.

## Непроверенные участки и открытые вопросы

Сохранение/валидация мировых настроек ядром и UI не воспроизводились. CSV не валидируется данным файлом. Названия опций не доказывают соответствие игровым правилам. При отсутствии pack дальнейшее ready поведение описано отдельно.

## Связанные проблемы

[issue-00002](../../../../../issues/potential/issue-00002.md) — ready не обрабатывает отсутствие выбранного pack.

## Дополнительная сверка — TASK-0003.003

2026-09-10, HEAD `c34b790379fd98cd7e33ccbeeca085e49297a40f`; исходники не изменены.

Настройка useOptionalAdrenaline управляет отображением счётчика и разрешает addAdrenaline; схема [adrenaline](../data/actor/templates/common/adrenalineData.js.md) сама настройки не читает и потолка не задаёт. displayRep управляет показом [числовой репутации](../data/actor/templates/common/reputationData.js.md) в листе; не меняет её модель и расчёт.

[Сценарии и результаты TASK-0003.003](../../../review-log.md#task-0003003).

## История актуализации

2026-09-10 — первичный разбор полного файла на указанном коммите; сверка порции 3 отражена в журнале. Файлы зависимостей проверены в пределах определений и обращений, без объявления их полного разбора.

2026-09-10 — TASK-0003.003: актуализированы связи с полностью разобранными структурами состояния Actor; ограничения полного клиента сохранены.

## Уточнение TASK-0003.007

2026-09-10, `b8b89a7e3392235f993c21f3c6d277a4a2e7a55f`. displayRollsDetails:46 считывается addActiveEffects. Он скрывает только имена источников персонального навыкового модификатора; подписи групповых модификаторов, атаки и защиты остаются. Проверены обе полученные строки; setter настройки и браузер не запускались.

Карточки: [WitcherActor](../actor/witcherActor.js.md), [modifierMixin](../actor/mixins/modifierMixin.js.md). [Сверка TASK-0003.007](../../../review-log.md#task-0003007).

## Уточнение TASK-0003.011

2026-09-10, `07237960627bf7debc2b4283aa55d1a8c5d1bb8b`; содержимое исходника совпадает с предыдущим срезом.

Матрица [шапки Item](../../templates/partials/item-header.hbs.md) подтвердила правила видимости checkbox: тип в CSV и (GM либо ограничение GM выключено). Матрица [item-image](../../templates/partials/item-image.hbs.md) требует ещё clickableImage=true. Настройка GM ограничивает видимость checkbox, не создаёт отдельного ограничения записи поля. Поле clickableImage не объявлено в моделях; проверенные настоящие Valuable/Armor/Weapon/Mutagen отбрасывают его при подготовке. Текущие списки инвентаря partial не используют: [issue-00063](../../../../../issues/potential/issue-00063.md). Сохранение мира не проверялось.

[TASK-0003.011 — сценарии и сверка](../../../review-log.md#task-0003011).
