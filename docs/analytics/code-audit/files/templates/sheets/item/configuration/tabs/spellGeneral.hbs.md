# templates/sheets/item/configuration/tabs/spellGeneral.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/sheets/item/configuration/tabs/spellGeneral.hbs](../../../../../../../../../templates/sheets/item/configuration/tabs/spellGeneral.hbs) |
| Тип файла | Handlebars |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-16: актуализация технических обращений по issue-00001 |
| Ветка и коммит | `dev`, база `d8e0e1ad1159cb71a8769b0353f812de6f1ed4d8` + незакоммиченное исправление issue-00001 |
| Изменения относительно коммита | issue-00001; текущие технические обращения актуализированы. Прежние опыты ниже относятся к своим датам. |
| Задача и порция | [TASK-0003.021](../../../../../../../../tasks/task-0003.021.md), 13 файлов, 936 логических строк |
| Запись перекрёстной сверки | [TASK-0003.021](../../../../../../review-log.md#task-0003021) |

Актуализация [issue-00001](../../../../../../../../issues/closed/issue-00001.md), 2026-09-16: Обращения к ресурсам и/или техническим namespaces переведены на TheWitcherTRPG-RB-Version. Формулы и порядок действий сохранены. Датированные проверки ниже выполнены до смены ID.

## Назначение файла

Общая вкладка конфигурации spell: выбор статусов для себя и цели, параметры атаки, тип урона и виды защиты цели.

## Условия использования

PARTS.general WitcherSpellConfigurationSheet; использует контекст WitcherConfigurationSheet (item/config/systemFields) и tabs.general.cssClass. События keyed CRUD предоставляет WitcherPropertiesConfigurationSheet.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| tab.general | div1 | Часть primary/general | CSS class из tabs.general | Рендер/навигация |
| selfEffects/onCastEffects tables | 2–45 | По одной строке на запись словаря | each effect, id | Не embedded ActiveEffect; названия selfProperties/targetProperties |
| addEffect/removeEffect/editEffect | data-action5, 13, 17, 27, 35, 39 | Создание/удаление/выбор статуса | data-target=system.selfEffects/system.onCastEffects; data-id; data-field=statusEffect | Без поля percentage и без имени обычного input |
| selectOptions statusEffects | 18, 40 | CONFIG.WITCHER.statusEffects массив | valueAttr=id, labelAttr=name, blank='', localize=true | nameAttr=id указан, но helper Foundry14 не использует этот параметр |
| attackOptionsPart; damageType/defenseOptions | 46–49 | Настройки атаки и два formGroup | systemFields и config.* | Поле defenseOptions — множество; damageType — String |

## Основные функции и методы

Функций JavaScript нет. each сохраняет ID словаря в dataset; selectOptions выбирает id статуса. editEffect вызывается inherited _onChangeForm, add/remove — actions родителя. Это отдельно от CRUD документов на вкладке activeEffects.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| WitcherSpellConfigurationSheet | [module/item/sheets/configurations/WitcherSpellConfigurationSheet.js](../../../../../../../../../module/item/sheets/configurations/WitcherSpellConfigurationSheet.js) | Загрузчик | PARTS.general | 7 |
| WitcherPropertiesConfigurationSheet | [module/item/sheets/configurations/WitcherPropertiesConfigurationSheet.js](../../../../../../../../../module/item/sheets/configurations/WitcherPropertiesConfigurationSheet.js) | Действия | _onAddEffect/_onEditEffect/_oRemoveEffect/_onChangeForm | Сверены data-target/field/id и update-пути |
| WitcherConfigurationSheet | [module/item/sheets/configurations/WitcherConfigurationSheet.js](../../../../../../../../../module/item/sheets/configurations/WitcherConfigurationSheet.js) | Контекст | item/config/systemFields/tabs | _prepareContext + inherited TABS |
| SpellData; itemEffect() | [module/data/item/spellData.js](../../../../../../../../../module/data/item/spellData.js); [module/data/item/templates/itemEffectData.js](../../../../../../../../../module/data/item/templates/itemEffectData.js) | Контракт схемы | TypedObjectField записи | name/statusEffect/percentage/varEffect; UI выбирает только statusEffect |
| attackOptionsPart.hbs | [templates/sheets/item/configuration/partials/attackOptionsPart.hbs](../../../../../../../../../templates/sheets/item/configuration/partials/attackOptionsPart.hbs) | Partial | 46 | Настоящее включение при изолированном рендере |
| CONFIG.WITCHER.statusEffects/damageTypes/defenseOptions | [module/setup/config.js](../../../../../../../../../module/setup/config.js) | Справочники | selectOptions/formGroup | Проверены id/name и value/label структур |
| Ключи WITCHER.* | [lang/en.json](../../../../../../../../../lang/en.json); [lang/ru.json](../../../../../../../../../lang/ru.json) | Локализация | Подписи | Literal-ключи разрешаются |
| localize/selectOptions/formGroup; each | Foundry14.367.0 client/applications/handlebars.mjs; Handlebars4.7.9 | Внешние helpers | Варианты/поля/циклы | Оригинальный helper прочитан; в рендере API-фасады; unknown nameAttr игнорируется |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/item/sheets/configurations/WitcherSpellConfigurationSheet.js](../../../../../../../../../module/item/sheets/configurations/WitcherSpellConfigurationSheet.js) | Этот HBS | PARTS.general | 7 |

Область поиска: module/ и templates/ текущего checkout; регистрация сверена с system.json. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

При добавлении создаётся запись {percentage: 0}, модель дополняет остальные поля. Выбор сохраняет только statusEffect по ID; remove удаляет ключ словаря. Отсутствие поля percentage не означает 100%-ное прохождение всей магии: потребитель отдельно проверяет fumble, после чего отправляет статусы без проверки percentage. Документные эффекты Item.effects живут в другой вкладке.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Рендер двух словарей | Группа 13; SELF/fire и TARGET/poison | ID/target сохранены; выбран правильный option; percentage73 остаётся в данных, но поля ввода нет | Настоящие HBS/модель; select/formGroup фасады |
| CRUD | Группа 14; исходные методы родителя | add→percentage0; edit→system.selfEffects.SELF.statusEffect; remove→system.selfEffects.-=SELF | update только записан в журнал вызовов, БД не менялась |

## Непроверенные участки и открытые вопросы

Исходник и указанные связи сопоставлены в TASK-0004.009. Фактический submit, inherited обработчики в браузере и доставка статусов/AE не исполнялись; data-target не доказывает сохранение всех полей модели. Остаток: [U009-01](../../../../../../cross-check-0002.md#u009-01), [U009-03](../../../../../../cross-check-0002.md#u009-03), [U009-07](../../../../../../cross-check-0002.md#u009-07). Новых поведенческих запусков нет; прежние протоколы сохраняют даты и фасады.

## Связанные проблемы

[issue-00060](../../../../../../../../issues/potential/issue-00060.md), [issue-00062](../../../../../../../../issues/closed/issue-00062.md), [issue-00133](../../../../../../../../issues/potential/issue-00133.md). 60 — ограничение общего обработчика; 133 — подготовка сообщения потребителем selfEffects. issue-00062 проверена как контроль: используемый attackOptionsPart подписывает spell правильно, в отличие от прежней общей general.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `a29234e7c42ef5f9d8095c2b5470e5e3c95824cc`; полный файл | Первая карточка; [сверка порции](../../../../../../review-log.md#task-0003021) |

## Сквозная сверка TASK-0004.009

2026-09-14; rusbar-main, 7adc2362937779de0c03957aacf73ff2cf13e211. Исходник совпадает со срезом TASK-0001; изменено только описание.

spellGeneral связывает два keyed списка self/onCast со встроенными add/remove/edit обработчиками и statusEffect choices. UI редактирует не весь itemEffect, а документы ActiveEffect представлены другой вкладкой. attackOptions partial, damageType и defenseOptions описывают отдельные способности Spell.

Сопоставленные определения и потребители: [module/item/sheets/configurations/WitcherSpellConfigurationSheet.js](../../../../../module/item/sheets/configurations/WitcherSpellConfigurationSheet.js.md), [module/item/sheets/configurations/WitcherPropertiesConfigurationSheet.js](../../../../../module/item/sheets/configurations/WitcherPropertiesConfigurationSheet.js.md), [module/item/sheets/configurations/WitcherConfigurationSheet.js](../../../../../module/item/sheets/configurations/WitcherConfigurationSheet.js.md), [module/data/item/spellData.js](../../../../../module/data/item/spellData.js.md), [module/data/item/templates/itemEffectData.js](../../../../../module/data/item/templates/itemEffectData.js.md), [templates/sheets/item/configuration/partials/attackOptionsPart.hbs](../partials/attackOptionsPart.hbs.md), [module/setup/config.js](../../../../../module/setup/config.js.md), [lang/en.json](../../../../../lang/en.json.md), [lang/ru.json](../../../../../lang/ru.json.md).

[Протокол и границы](../../../../../../review-log.md#task-0004009) — TASK-0004.009; процессы [R009-06](../../../../../../cross-check-0002.md#r009-06). В этой порции выполнена статическая сверка; прежние опыты сохраняют свои даты и фасады. Новых поведенческих запусков нет; браузер, мир, сеть и запись в БД не запускались.
