# templates/sheets/item/configuration/tabs/defensePropertiesConfiguration.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/sheets/item/configuration/tabs/defensePropertiesConfiguration.hbs](../../../../../../../../../templates/sheets/item/configuration/tabs/defensePropertiesConfiguration.hbs) |
| Тип файла | Handlebars, HTML-шаблон |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `8cca18e14b75ec53028ee6bc49a837597de4d9af` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.013](../../../../../../../../tasks/task-0003.013.md), одна порция из восьми файлов |
| Запись перекрёстной сверки | [TASK-0003.013](../../../../../../review-log.md#task-0003013) |

## Назначение файла

Вкладка редактирования трёх свойств собственной защиты предмета: parrying, defendsAgainst и modifier. Формулу защиты выполняет Actor, а эта разметка лишь выводит поля модели.

## Условия использования

PARTS.defenseProperties общей конфигурации; присутствует у Weapon/Spell/Armor, если item.system.defenseProperties существует. Корневой div использует tabs.defenseProperties.cssClass и data-group='primary', data-tab='defenseProperties'.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| Корень вкладки | 1–2 | Связь с навигацией | PARTS.defenseProperties | Применяет cssClass вкладки |
| parrying | formGroup3–7 | Признак парирующего свойства | Schema/value: defenseProperties.parrying | BooleanField |
| defendsAgainst | formGroup8–13 | Виды атак, против которых работает защита | options=config.attackOptions | SetField, выбор берётся из справочника |
| modifier | formGroup14–18 | Числовая поправка защиты | Schema/value: defenseProperties.modifier | NumberField |

## Основные функции и методы

JS-функций нет. Три formGroup с localize=true, без условий/циклов/ручных actions. Существование полей предполагается; скрытие вкладки выполняет класс конфигурации.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| DefenseProperties | [module/data/item/templates/combat/defensePropertiesData.js](../../../../../../../../../module/data/item/templates/combat/defensePropertiesData.js) | Схема и значения | Все три formGroup | Настоящие поля сверены |
| Контекст и фильтрация | [module/item/sheets/configurations/WitcherPropertiesConfigurationSheet.js](../../../../../../../../../module/item/sheets/configurations/WitcherPropertiesConfigurationSheet.js) | PARTS/TABS/context | Проверки существования модели | Матрица Weapon/Armor/Spell |
| config.attackOptions | [module/setup/config.js](../../../../../../../../../module/setup/config.js) | Options | defendsAgainst выбирает melee/ranged/spell/itemUse | Это виды атаки, не defenseOptions dodge/parry |
| formGroup | Foundry 14.367.0, client/applications/handlebars.mjs | Helper | Имена/подписи/controls по DataField | Исходный helper исполнен, toFormGroup — фасад |
| Схемные label/hint | [lang/ru.json](../../../../../../../../../lang/ru.json); [lang/en.json](../../../../../../../../../lang/en.json) | Локализация | WITCHER.Item.DefenseProperties.* | Проверены в TASK-0003.012 |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/item/sheets/configurations/WitcherPropertiesConfigurationSheet.js](../../../../../../../../../module/item/sheets/configurations/WitcherPropertiesConfigurationSheet.js) | Шаблон | PARTS.defenseProperties | 19–23 |
| [module/actor/mixins/defenseMixin.js](../../../../../../../../../module/actor/mixins/defenseMixin.js); [module/data/item/weaponData.js](../../../../../../../../../module/data/item/weaponData.js) | Значения, редактируемые формой | Применимость/выбор навыка/парирование | Downstream, не вызов непосредственно из HBS |

## Данные и изменения состояния

Обычные именованные controls формируются ядром по полным путям system.defenseProperties.*. Ручного item.update в шаблоне нет. UI не проверяет навык защиты: его выбирает WeaponData.createDefenseOption. Наличие schema у ArmorData не означает наличие делегирующих методов собственной защиты; это остаётся предметом TASK-0003.014.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Три пути | Рендер с WeaponData и исходным formGroup | Получены system.defenseProperties.parrying/defendsAgainst/modifier | Без реальной отправки формы |
| Фильтрация | Матрица трёх реальных моделей | У всех вкладка и часть сохранены | Полное применение защиты не запускалось |

## Непроверенные участки и открытые вопросы

Исходник и текущие связи сопоставлены в TASK-0004.006. Прежние ссылки на будущий пофайловый разбор TASK-0003 больше не являются очередью: он завершён. Остались конкретные границы сквозной проверки: [U006-01](../../../../../../cross-check-0002.md#u006-01); [U006-03](../../../../../../cross-check-0002.md#u006-03). Сохранённые значения ещё должны пройти методы владельца; Armor их не делегирует, Weapon выбирает skill nullish-цепочкой, Profession отдельно обрабатывает пути.

## Связанные проблемы

[issue-00079](../../../../../../../../issues/potential/issue-00079.md) — выбор пустого/неподходящего навыка внешней WeaponData. Разметка сама навыка не выбирает.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.013 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.

## Сквозная сверка TASK-0004.006

2026-09-14; rusbar-main, a176c4f18879f2e5a63b93bc15345fc26d9f535a. Исходник совпадает со срезом TASK-0001; изменено только описание.

Три formGroup соответствуют parrying/defendsAgainst/modifier вложенной модели. Сохранённые значения ещё должны пройти методы владельца; Armor их не делегирует, Weapon выбирает skill nullish-цепочкой, Profession отдельно обрабатывает пути.

Сопоставленные определения и потребители: [module/data/item/templates/combat/defenseOptionsData.js](../../../../../module/data/item/templates/combat/defenseOptionsData.js.md), [module/data/item/templates/combat/defensePropertiesData.js](../../../../../module/data/item/templates/combat/defensePropertiesData.js.md), [module/data/item/templates/combat/skillDefenseData.js](../../../../../module/data/item/templates/combat/skillDefenseData.js.md), [module/data/item/professionData.js](../../../../../module/data/item/professionData.js.md).

[Протокол и границы](../../../../../../review-log.md#task-0004006) — TASK-0004.006; процессы [R006-07](../../../../../../cross-check-0002.md#r006-07). В этой порции выполнена статическая сверка; поведенческие опыты принадлежат датированным прежним протоколам, а не новому прогону.
