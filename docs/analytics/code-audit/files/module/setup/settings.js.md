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

## Уточнение TASK-0003.012

2026-09-10, `d20d821e3a8a0a989ec503b0e97413a5a1431ad9`; исходник не изменён. Настройка silverTrait переключает потребление [DamageProperties.silverTrait/silverDamage](../../../../../../module/data/item/templates/combat/damagePropertiesData.js). Точечно проверенная ветвь calculateDamageWithLocation присваивает строку instance.setType вместо вызова метода: [issue-00073](../../../../../issues/potential/issue-00073.md). Проверена связь настройки с обработчиком, не вся механика серебряного урона.

Результат и границы — [сверка TASK-0003.012](../../../review-log.md#task-0003012).

## Уточнение TASK-0003.017

2026-09-10, `c7cd9d71dcb1714cdccb175aee351a3f1df95c5b`; исходники неизменны. [Сверка](../../../review-log.md#task-0003017).

Повторно исполнен настоящий registerSettings с настоящим ClientSettings Foundry 14.367 и storage/Setting-фасадами: зарегистрированы 9 прежних ключей, displayRollsDetails по умолчанию false. [RepairSystem](../../../../../../module/item/systems/repair.js) обращается к отсутствующей woundsAffectSkillBase; реальный get выбросил ошибку неизвестной настройки. Это [issue-00103](../../../../../issues/potential/issue-00103.md), а не молчаливое значение false. Проверка дополнительной регистрации внешними модулями не выполнялась.

## Уточнение TASK-0003.020

2026-09-11, `rusbar-main`, `b09f992960a76d1c75946f402e42d93fa0785008`; проверены связи с критическими травмами, лечением и отдыхом. Полный первоначальный разбор и его ограничения сохранены.

| Связь | Файл | Результат проверки |
| --- | --- | --- |
| criticalWoundsPack | [module/actor/mixins/damageMixin.js](../../../../../../module/actor/mixins/damageMixin.js) | applyCritWound:314–339 читает выбранный pack, фильтрует treatment=none/location/criticalLevel и выбирает lesserEffect. Это внешний потребитель модели травмы, не функция лечения. |
| CriticalWoundData.followUp | [module/data/item/criticalWoundData.js](../../../../../../module/data/item/criticalWoundData.js) | Ссылка следующего Item разрешается напрямую через fromUuid; настройка pack не переназначает её. |

[Сверка порции и итоговая сверка 96 файлов второй серии](../../../review-log.md#task-0003020); браузер, мир и записи в БД не запускались.

## Уточнение TASK-0003.021

Проверено 2026-09-11 на `a29234e7c42ef5f9d8095c2b5470e5e3c95824cc`; исходник не менялся.

clickableImageItemTypes (CSV, defaultvaluable) и clickableImageCheckboxForGMOnly(defaulttrue) прочитаны всеми тремя магическими заголовками. Checkbox может выводиться, но соответствующее поле отсутствует в трёх моделях (issue63). Отдельный editImage action присутствует у spell и отсутствует у hex/ritual (issue136).

Сверенные карточки: [templates/sheets/item/spell-sheet.hbs](../../templates/sheets/item/spell-sheet.hbs.md), [templates/sheets/item/hex-sheet.hbs](../../templates/sheets/item/hex-sheet.hbs.md), [templates/sheets/item/ritual-sheet.hbs](../../templates/sheets/item/ritual-sheet.hbs.md), [templates/partials/spell-header.hbs](../../templates/partials/spell-header.hbs.md).

[Результаты и пределы сверки](../../../review-log.md#task-0003021).

## Уточнение TASK-0003.028

2026-09-11, `9f16a7ae4bc942df85a105fd37d9a3cb3ef99f4b`: displayRollsDetails:46–53 — world Boolean с default=false. Полный helper.addPart читает настройку до проверки hideZero; при true добавляет локализованную подпись в квадратных скобках. getCustomModifier с нулём возвращает пустую строку, с -2 — '+-2' с опциональной подписью. Реальный parser Foundry принимает такие последовательности знаков; [issue-00033](../../../../../issues/potential/issue-00033.md) относится к отсутствующему оператору в другом сборщике.

Полные карточки зависимости: [module/scripts/helper.js](../scripts/helper.js.md). [Перекрёстная сверка](../../../review-log.md#task-0003028). Это уточнение связи; исходный файл не изменён.

## Уточнение TASK-0003.030

2026-09-11, `aa6af106e86a9c75fe050d599f961c8fadb74f1b`. useOptionalAdrenaline (world Boolean false) проверяется внутри addAdrenaline и определяет видимость блока sidebar через useAdrenaline. displayRep (world Boolean false) вместе с isGM управляет показом репутации, не правами вызова _onReputation. displayRollsDetails не меняет описанный пороговый смысл stat-save.

Сверенные источники: [module/actor/mixins/adrenalineMixin.js](../../../../../../module/actor/mixins/adrenalineMixin.js); [module/actor/sheets/mixins/statMixin.js](../../../../../../module/actor/sheets/mixins/statMixin.js); [templates/partials/character/tab-stats.hbs](../../../../../../templates/partials/character/tab-stats.hbs). [Итоговая сверка третьей серии, сценарии и ограничения](../../../review-log.md#task-0003030). Код и статусы проблем не менялись.

## Уточнение TASK-0003.031

2026-09-11, `928ce4e537c6a3fdc34f8b6fa3fcfdb5a669f68d`. Character callbacks непосредственно читают displayRollsDetails; base context передаёт useVerbalCombat и useAdrenaline в новые шаблоны. При отключении словесного боя скрываются header-action и resolve, при отключении адреналина — его управление. Подробнее проверены формулы с displayRollsDetails в обоих режимах.

Связи: [module/actor/sheets/WitcherCharacterSheet.js](../actor/sheets/WitcherCharacterSheet.js.md); [templates/partials/character-header.hbs](../../templates/partials/character-header.hbs.md); [templates/sheets/actor/partials/character/sidebar.hbs](../../templates/sheets/actor/partials/character/sidebar.hbs.md). [Методика и ограничения сверки](../../../review-log.md#task-0003031).

## Уточнение TASK-0003.032

2026-09-11, `8b938d44a042749df027d8b58e28bb1d79638091`. useOptionalVerbalCombat проходит через базовый контекст в Monster header/sidebar и старый полный HBS. Флаг управляет кнопкой словесного боя и блоком resolve; конфигурация general предлагает custom resolve max независимо от его видимости. Другие настройки не объявляются переисследованными.

Связи: [module/actor/sheets/WitcherMonsterSheet.js](../actor/sheets/WitcherMonsterSheet.js.md); [templates/sheets/actor/partials/monster/header.hbs](../../templates/sheets/actor/partials/monster/header.hbs.md); [templates/sheets/actor/partials/monster/sidebar.hbs](../../templates/sheets/actor/partials/monster/sidebar.hbs.md); [templates/sheets/actor/configuration/monster/general.hbs](../../templates/sheets/actor/configuration/monster/general.hbs.md); [templates/sheets/actor/monster-sheet.hbs](../../templates/sheets/actor/monster-sheet.hbs.md). [Результаты и пределы проверки](../../../review-log.md#task-0003032).

## Дополнительная сверка TASK-0003.038

2026-09-11, `rusbar-main`, `b47ba02cdaebc6a66ad14a5638213b6eb24460b4`; исходники не менялись.

displayRollsDetails прочитан обоими профессиональными бросками. Группа 10/22 с реальным Roll дала одинаковые числовые итоги при переключении, различается аннотация формул. Настройки resource/применения не добавлялись.

[module/actor/mixins/professionMixin.js](../actor/mixins/professionMixin.js.md), [templates/partials/character/tab-profession.hbs](../../templates/partials/character/tab-profession.hbs.md), [templates/sheets/actor/partials/monster/tabs/tab-profession.hbs](../../templates/sheets/actor/partials/monster/tabs/tab-profession.hbs.md), [templates/dialog/combat/profession-attack.hbs](../../templates/dialog/combat/profession-attack.hbs.md).

[Сверка и ограничения](../../../review-log.md#task-0003038). Связанные файлы повторно в покрытии не учитывались; код и статусы issues не изменены.

## Дополнительная сверка TASK-0003.039

2026-09-11, `c598d74e34f4be51535de78b38f0601c286c5407`; исходники не менялись.

displayRollsDetails читается castSpell при формировании характеристик, навыка, EV, customMod и локации; группа 10 показала неизменный итог при включённых подписях. Собственного setting порога или списка магии метод не читает.

[module/actor/mixins/castSpellMixin.js](../../../../../../module/actor/mixins/castSpellMixin.js) — [карточка](../actor/mixins/castSpellMixin.js.md).

[Сценарии, методика и пределы проверки](../../../review-log.md#task-0003039). Соседние определения проверены в пределах связи; это не расширяет состав шести полностью разобранных файлов.

## Дополнительная сверка TASK-0003.041

2026-09-12, rusbar-main, d5c7a4b871dce3aa55f4b8b589e62c3c9450f2d3; исходник не изменён.

displayRollsDetails прочитан в [weaponAttack/constructBaseAttackFormula](../actor/mixins/weaponAttackMixin.js.md): включает подписи основы, модификаторов, места/удара/урона. Формулы с подписями разобраны настоящим Roll в группе 08; локализатор возвращал ключи, интерфейс выбора настройки не запускался.

[Сверка и ограничения](../../../review-log.md#task-0003041). Уточнение связи не увеличивает пофайловое покрытие; исправления не выполнялись.

## Уточнение TASK-0003.057 — боевые таблицы

2026-09-12, rusbar-main 8573642b0136f80b8ae3456de51e1b7f637ec7f3; исходник не изменён.

criticalWoundsPack:2–14 по умолчанию TheWitcherTRPG.criticalWounds; choices=getAllCompendia:86–95 фильтрует documentName='Item'. Combat зарегистрирован как RollTable и этим списком не предлагается. Настройка не переключает автоматические броски на одноимённые таблицы Combat.

[Карточки Combat](../../README.md#боевые-таблицы--task-0003057), [перекрёстная сверка](../../../review-log.md#task-0003057). Для issue-00322/00323/00324 см. [реестр проблем](../../../../../issues/potential/../README.md). Пределы изолированных сценариев сохранены отдельно от запуска мира.
