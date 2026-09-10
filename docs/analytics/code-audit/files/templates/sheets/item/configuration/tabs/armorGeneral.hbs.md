# templates/sheets/item/configuration/tabs/armorGeneral.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/sheets/item/configuration/tabs/armorGeneral.hbs](../../../../../../../../../templates/sheets/item/configuration/tabs/armorGeneral.hbs) |
| Тип файла | Handlebars, HTML-шаблон |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `0fa589bd300856ff309f362afcb66d6fa43401ab` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.014](../../../../../../../../tasks/task-0003.014.md), одна порция из девяти файлов |
| Запись перекрёстной сверки | [TASK-0003.014](../../../../../../review-log.md#task-0003014) |

## Назначение файла

Вкладка конфигурации, выводящая исходные текущие и максимальные SP всех шести частей тела.

## Условия использования

PARTS.general WitcherArmorConfigurationSheet. Нужны tabs.general.cssClass, systemFields и document.system. Форма всегда выводит все части, независимо от location и типа щита.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| Корень general | 1 | Контейнер вкладки | data-group primary/data-tab general | CSS-класс из контекста |
| head.stoppingPower/maxStoppingPower | 3–4 | Голова | Два formGroup | Подсказка WITCHER.Armor.LocationHead |
| torso.stoppingPower/maxStoppingPower | 6–7 | Торс | Два formGroup | Подсказка WITCHER.Armor.LocationTorso |
| leftArm.stoppingPower/maxStoppingPower | 9–10 | Левая рука | Два formGroup | Подсказка WITCHER.Armor.locationLeftArm |
| rightArm.stoppingPower/maxStoppingPower | 12–13 | Правая рука | Два formGroup | Подсказка WITCHER.Armor.locationRightArm |
| leftLeg.stoppingPower/maxStoppingPower | 15–16 | Левая нога | Два formGroup | Подсказка WITCHER.Armor.locationLeftLeg |
| rightLeg.stoppingPower/maxStoppingPower | 18–19 | Правая нога | Два formGroup | Подсказка WITCHER.Armor.locationRightLeg |

## Основные функции и методы

Функций, условий, циклов и data-action нет. Двенадцать formGroup получают настоящее определение поля, соответствующее document.system значение, localize=true и отдельную подсказку локации. Генерацию контролов и запись выполняет внешний framework.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| WitcherArmorConfigurationSheet | [module/item/sheets/configurations/WitcherArmorConfigurationSheet.js](../../../../../../../../../module/item/sheets/configurations/WitcherArmorConfigurationSheet.js) | PARTS/context | Подключение и tabs.general | Полный файл проверен |
| ArmorData; SpData | [module/data/item/armorData.js](../../../../../../../../../module/data/item/armorData.js); [module/data/item/templates/armor/spData.js](../../../../../../../../../module/data/item/templates/armor/spData.js) | Schema/value | Шесть пар исходного SP/max | modified-поля не редактируются |
| WitcherConfigurationSheet | [module/item/sheets/configurations/WitcherConfigurationSheet.js](../../../../../../../../../module/item/sheets/configurations/WitcherConfigurationSheet.js) | Наследуемый контекст | document и systemFields | Базовая подготовка |
| Подсказки WITCHER.Armor.* | [lang/ru.json](../../../../../../../../../lang/ru.json); [lang/en.json](../../../../../../../../../lang/en.json) | Локализация | Все шесть локаций | Ключи правильные для en; четыре отсутствуют в ru (issue-00090) |
| formGroup | Foundry 14.367.0, client/applications/handlebars.mjs | Внешний helper | Все 12 вызовов | Настоящий helper, toFormGroup — учёт путей |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/item/sheets/configurations/WitcherArmorConfigurationSheet.js](../../../../../../../../../module/item/sheets/configurations/WitcherArmorConfigurationSheet.js) | Шаблон general | PARTS.general | 7 |

Область поиска: текущие module/ и templates/; регистрации сверены отдельно. Динамические обращения внешних модулей не исследовались.

## Данные и изменения состояния

Сохраняются system.<часть>.stoppingPower и maxStoppingPower. Нет reliability/reliabilityMax и нет условного скрытия частей при Shield: эти поля находятся в основном листе. Значения рук и ног направлены в одноимённые модели, в отличие от отдельной ошибки tooltip armorPartsInfo.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Пути и условия | Рендер FullCover и Shield с настоящими схемами | Ровно 12 действительных путей в обоих случаях, без ошибки helper | Контролы представлены фасадом |
| Локализация | Исходные строки и en/ru | В en найдены все; в ru отсутствуют четыре для рук/ног. Привязки сторон совпадают | Tooltip инвентаря не рендерился заново |

## Непроверенные участки и открытые вопросы

Все 20 строк проверены. Полная сериализация формы и обновление Item через браузер не выполнялись; наличие скрытых SP у щита не объявлено ошибкой.

## Связанные проблемы

[issue-00007](../../../../../../../../issues/potential/issue-00007.md), [issue-00086](../../../../../../../../issues/potential/issue-00086.md). Локальные подписи правильные; миграция старых SP может перезаписывать редактируемые здесь значения.

Отсутствующие русские подсказки рук/ног — [issue-00090](../../../../../../../../issues/potential/issue-00090.md). При штатном английском fallback ожидается английский текст, без изменения адреса поля.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.014 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.
