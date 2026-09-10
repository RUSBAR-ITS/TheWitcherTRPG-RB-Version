# module/activeEffect/mixins/temporaryItemImprovementMixin.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/activeEffect/mixins/temporaryItemImprovementMixin.js](../../../../../../../module/activeEffect/mixins/temporaryItemImprovementMixin.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `247d3d86e344238a1445377c686eb6455146693c` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.010](../../../../../../tasks/task-0003.010.md), одна порция из восьми файлов |
| Запись перекрёстной сверки | [TASK-0003.010](../../../../review-log.md#task-0003010) |

## Назначение файла

Предоставляет мастеру три пути изменения урона временного улучшения Item.

## Условия использования

Объект подключён к WitcherActiveEffectConfig.prototype после baseMixin. Его сборщик вызывается wizardAction только для document.type=temporaryItemImprovement. Сам mixin не фильтрует тип получателя, не вычисляет урон и не задаёт операцию изменения.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| temporaryItemImprovementMixin | export let, 1–27 | Объект двух методов | Object.assign листа | Формирует новые объекты подсказок |
| baseDamage / oilEffect / silverDamage | Ключи результата getItemDamageSuggestions | Три варианта мастера | value — путь, label/group — локализованные подписи | Не поля новой модели |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| getActiveEffectsItemImprovementPaths; 2–6 | Контекст с getItemDamageSuggestions | Объект подсказок | Spread результата единственной группы | Синхронно; без сохранения |
| getItemDamageSuggestions; 8–26 | game.i18n.localize | Три записи label/value/group | Создаёт пути system.damage, system.damageProperties.oilEffect, system.damageProperties.silverDamage | Значение, тип операции и приоритет не задаются |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| game.i18n.localize; WITCHER.Weapon.Damage, WITCHER.Damage.oil, WITCHER.Damage.silverDmg, WITCHER.Effect.wizard.Item.damage | [lang/en.json](../../../../../../../lang/en.json); [lang/ru.json](../../../../../../../lang/ru.json); внешний i18n | Локализация | Три подписи и общая группа | Ключи сверены |
| damage | [module/data/item/weaponData.js](../../../../../../../module/data/item/weaponData.js) | Путь схемы | StringField формулы урона | Подсказка system.damage |
| oilEffect, silverDamage | [module/data/item/templates/combat/damagePropertiesData.js](../../../../../../../module/data/item/templates/combat/damagePropertiesData.js) | Пути вложенной модели | Два StringField | EmbeddedDataField в WeaponData |
| WitcherActiveEffectConfig | [module/activeEffect/WitcherActiveEffectSheet.js](../../../../../../../module/activeEffect/WitcherActiveEffectSheet.js) | Получатель mixin | Присоединяет методы и читает результат | Прямой импорт и Object.assign |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/activeEffect/WitcherActiveEffectSheet.js](../../../../../../../module/activeEffect/WitcherActiveEffectSheet.js) | getActiveEffectsItemImprovementPaths | Ветка temporaryItemImprovement в wizardAction | Передача selects шаблону |
| [templates/dialog/activeEffects/wizard.hbs](../../../../../../../templates/dialog/activeEffects/wizard.hbs) | Результирующие записи | selectOptions использует value/label/group | Косвенно через renderTemplate |

## Данные и изменения состояния

Возвращаемые строки не содержат формулы или величины бонуса. Превращение выбранного пути в changes выполняется листом; применение — документом эффекта/Item. Наличие трёх подсказок не ограничивает ручной ввод произвольного ключа. В других типах Item эти пути могут отсутствовать; целевой Weapon проверен отдельно.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Состав и пути | 27 строк; исходные методы и настоящая WeaponData | 3 записи; каждый путь разрешился в StringField | Не проверка арифметики урона |
| Потребитель | wizardAction + wizard.hbs | Тип temporaryItemImprovement выбирает именно этот сборщик | UI подменён |

## Непроверенные участки и открытые вопросы

Не проверялись все типы Item и конкретные игровые формулы/операции для строковых полей. Передача улучшения, его длительность и потеря changes разобраны в TASK-0003.009.

## Связанные проблемы

Собственная ошибка трёх путей не выявлена. Применение связано с [issue-00042](../../../../../../issues/potential/issue-00042.md) и [issue-00050](../../../../../../issues/potential/issue-00050.md); мастер — с [issue-00052](../../../../../../issues/potential/issue-00052.md).

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.010 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.
