# templates/sheets/item/configuration/tabs/spellGeneral.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/sheets/item/configuration/tabs/spellGeneral.hbs](../../../../../../../../../templates/sheets/item/configuration/tabs/spellGeneral.hbs) |
| Тип файла | Handlebars |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `a29234e7c42ef5f9d8095c2b5470e5e3c95824cc` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.021](../../../../../../../../tasks/task-0003.021.md), 13 файлов, 936 логических строк |
| Запись перекрёстной сверки | [TASK-0003.021](../../../../../../review-log.md#task-0003021) |

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

Все 49 строк прочитаны. Полный UI и работа целевых статусов/ActiveEffect в игровом процессе не проверены; действие inherited text='on' касается общего обработчика.

## Связанные проблемы

[issue-00060](../../../../../../../../issues/potential/issue-00060.md), [issue-00062](../../../../../../../../issues/potential/issue-00062.md), [issue-00133](../../../../../../../../issues/potential/issue-00133.md). 60 — ограничение общего обработчика; 133 — подготовка сообщения потребителем selfEffects. issue-00062 проверена как контроль: используемый attackOptionsPart подписывает spell правильно, в отличие от прежней общей general.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `a29234e7c42ef5f9d8095c2b5470e5e3c95824cc`; полный файл | Первая карточка; [сверка порции](../../../../../../review-log.md#task-0003021) |
