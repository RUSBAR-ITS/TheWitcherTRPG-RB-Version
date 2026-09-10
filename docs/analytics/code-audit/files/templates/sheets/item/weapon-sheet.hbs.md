# templates/sheets/item/weapon-sheet.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/sheets/item/weapon-sheet.hbs](../../../../../../../templates/sheets/item/weapon-sheet.hbs) |
| Тип файла | Handlebars, HTML-шаблон |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `8cca18e14b75ec53028ee6bc49a837597de4d9af` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.013](../../../../../../tasks/task-0003.013.md), одна порция из восьми файлов |
| Запись перекрёстной сверки | [TASK-0003.013](../../../../review-log.md#task-0003013) |

## Назначение файла

Основное содержимое листа оружия: описание, основные настройки, виды урона, надёжность, характеристики оружия и привязка рецепта. Расширенные свойства урона/защиты редактируются отдельным окном.

## Условия использования

PARTS.main WitcherWeaponSheet. Требует item, config и inherited showConfig/настройки общей шапки. Корневой section.scrollable не является отдельной form: оболочку и submit предоставляет лист. Без JavaScript шаблон не меняет документы.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| section.scrollable | Корень 1–113 | Содержимое main | PARTS.main | Рендер HBM |
| item-header; associated-diagram | Partials2,112 | Общая шапка и связь рецепта | Имена systems/TheWitcherTRPG/templates/... | Контекст передаётся без отдельного hash |
| Описание и флаги | 5,11/15/21 | description, rollOnlyDmg, usingAmmo, isAmmo | textarea/checkbox с name | Обычная отправка формы |
| .damage-type | Четыре input48–59 | slashing/piercing/bludgeoning/elemental | id, checkbox, без name/data-action | Сохраняет специальный listener листа |
| Таблица оружия | 25–93 | accuracy/avail/reliable/maxReliability/hands/conceal/enhancements/rateOfFire | name system.* | Часть столбцов скрыта для ammo |
| Формула/дистанция | 94–111 | system.damage и system.range | Text inputs | Показываются при !isAmmo |

## Основные функции и методы

Функций/методов/экспортов нет. Директивы: localize, checked, selectOptions, unless; два вызова partial. Условие unless item.system.isAmmo повторяется для заголовков и полей accuracy, hands, enhancements, rateOfFire, damage, range. Ammo сохраняет описание, три основных checkbox, четыре вида урона, avail, reliable/maxReliability, conceal и рецепт.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| item.system | [module/data/item/weaponData.js](../../../../../../../module/data/item/weaponData.js) | Чтение данных/обычная форма | Все поля перечислены выше | Каждый name сопоставлен с 36 полями WeaponData; header имеет собственные поля |
| WitcherWeaponSheet/_onDamageTypeEdit | [module/item/sheets/WitcherWeaponSheet.js](../../../../../../../module/item/sheets/WitcherWeaponSheet.js) | Назначение обработчика | Четыре id checkbox без name | Listener .damage-type подключается при _onRender |
| item-header.hbs | [templates/partials/item-header.hbs](../../../../../../../templates/partials/item-header.hbs) | Partial | Имя/картинка/количество/вес/цена/источник/конфигурация | TASK-0003.011; прежние issues не исправлены |
| associated-diagram.hbs | [templates/partials/associated-diagram.hbs](../../../../../../../templates/partials/associated-diagram.hbs) | Partial | Ссылка/картинка/название рецепта и remove | Определение/маршрут примеси прочитаны |
| config.Availability/Concealment/weapon.hands | [module/setup/config.js](../../../../../../../module/setup/config.js) | Справочники selectOptions | 68/77/83 | Сопоставлены ключи выбора со строковыми полями |
| localize, checked, selectOptions, unless | Foundry 14.367.0 Handlebars и встроенный unless | Helpers | Локализация/checkbox/варианты/ветвление | Компиляция настоящим Handlebars; selectOptions в сценарии подменён |
| WITCHER.Item/Weapon/Dialog/Enhancement.* | [lang/ru.json](../../../../../../../lang/ru.json); [lang/en.json](../../../../../../../lang/en.json) | Локализация | Тексты label/title | Ключи проверены как связи, языки целиком не разобраны |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/item/sheets/WitcherWeaponSheet.js](../../../../../../../module/item/sheets/WitcherWeaponSheet.js) | Шаблон | PARTS.main.template | 10 |
| [module/item/sheets/WitcherItemSheet.js](../../../../../../../module/item/sheets/WitcherItemSheet.js) | Имена полей, configureItem и listeners наследника | Общий lifecycle/submit | _prepareContext/_onRender/_onChangeForm |

## Данные и изменения состояния

Обычная форма передаёт именованные значения в Item.update через ядро. Четыре checkbox вида урона отсутствуют в обычном form payload: отдельный обработчик составляет system.type вместе с локализованным text. Шаблон не выводит enhancementItems и не присоединяет улучшения; число enhancements означает ёмкость, а список связей обслуживается другими частями системы.

В проверенном контексте оружия с общей шапкой получено 19 именованных controls, для ammo —13; в обоих случаях четыре .damage-type без name. Числовые input применяют data-dtype=Number; формула/range остаются строками.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Обе ветви isAmmo | Настоящий Handlebars с WeaponData, parsed HTML через parse5 | 19/13 именованных controls; сохранены 4type-checkbox; рецепт в обеих ветвях | Без реального HTMLFormElement/отправки |
| Тип урона | HTML id→захваченный change-listener | Соответствует _onDamageTypeEdit; payload включает type.text | update перехвачен |
| Два partial | Регистрация исходных partial и рендер | Оба включены в результат | Настройки шапки заданы фасадом game.settings |

## Непроверенные участки и открытые вопросы

Полная отправка формы, доступность controls для разных владельцев и геометрия Drop не проверены. Из чтения шаблона не следует работа внешнего ремонта или броска. Поиск потребителей — module/ и templates/.

## Связанные проблемы

[issue-00080](../../../../../../issues/potential/issue-00080.md) относится к Drop области рецепта из partial. Настройки расширенных свойств и связанные проблемы разобраны в других карточках этой порции.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.013 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.
