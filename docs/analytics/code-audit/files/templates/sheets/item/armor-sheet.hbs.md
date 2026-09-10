# templates/sheets/item/armor-sheet.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/sheets/item/armor-sheet.hbs](../../../../../../../templates/sheets/item/armor-sheet.hbs) |
| Тип файла | Handlebars, HTML-шаблон |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `0fa589bd300856ff309f362afcb66d6fa43401ab` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.014](../../../../../../tasks/task-0003.014.md), одна порция из девяти файлов |
| Запись перекрёстной сверки | [TASK-0003.014](../../../../review-log.md#task-0003014) |

## Назначение файла

Основная форма брони: описание, сопротивления, параметры ношения, SP или надёжность щита, предметные воздействия и рецепт.

## Условия использования

PARTS.main у WitcherArmorSheet. Требует item.system и config; включает item-header и associated-diagram. Корень section.scrollable. Именованные поля передаёт базовая форма, воздействия без name редактируются вручную через data-action.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| Описание и header | 1–6 | Имя/общие параметры через partial, description textarea | Всегда | Описание — обычный textarea, не enrichedText |
| resistance.slashing/piercing/bludgeoning | 31–36 | Checkbox физических сопротивлений | Всегда, checked из prepared system | Не из source, поэтому отражает улучшения |
| avail, enhancements, encumb, location, type | 38–52 | Доступность, ячейки, штраф, локация, тип | Select/number inputs | Options из config; enhancements не задаёт min/max/step |
| head.stoppingPower/maxStoppingPower | 74–82 | SP головы | Head или FullCover | Два поля базовых значений |
| torso, leftArm, rightArm: stoppingPower/maxStoppingPower | 83–105 | SP торса и обеих рук | Torso или FullCover | Шесть полей; стороны совпадают с подписью |
| leftLeg, rightLeg: stoppingPower/maxStoppingPower | 106–121 | SP ног | Leg или FullCover | Четыре поля; слева leftLeg, справа rightLeg |
| reliability/reliabilityMax | 122–129 | Надёжность щита | Только Shield | SP-заголовки скрыты у Shield, показаны подписи надёжности |
| effects | 133–154 | Собственные воздействия | each effect,id | Кнопки add/remove, edit name/statusEffect; data-target system.effects |
| enhancementsEffects | 155–171 | Воздействия улучшений | each | Имя и statusEffect disabled, без ID/action записи |
| Связанный рецепт | 174 | associated-diagram partial | Всегда | Удаление/Drop обслуживает примесь |

## Основные функции и методы

JS-функций нет. Условия eq/or/if/unless переключают пять вариантов location. each выводит два разных словаря воздействий. localize/checked/selectOptions формируют подписи, checkbox и choices. Собственные действия addEffect/removeEffect/editEffect адресуют базовый WitcherItemSheet; другие именованные поля сохраняются общей формой.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| WitcherArmorSheet | [module/item/sheets/WitcherArmorSheet.js](../../../../../../../module/item/sheets/WitcherArmorSheet.js) | PARTS/context | config.type/armorLocations/Availability, слушатель рецепта | Полный разбор |
| ArmorData | [module/data/item/armorData.js](../../../../../../../module/data/item/armorData.js) | Чтение system/запись путей | Все поля и getter enhancementsEffects | Настоящая модель и все шесть вариантов |
| SpData; ResistanceData | [module/data/item/templates/armor/spData.js](../../../../../../../module/data/item/templates/armor/spData.js); [module/data/item/templates/armor/resistanceData.js](../../../../../../../module/data/item/templates/armor/resistanceData.js) | Вложенные схемы | SP и resistance | Базовый SP отдельно от вычисленных сопротивлений |
| WitcherItemSheet | [module/item/sheets/WitcherItemSheet.js](../../../../../../../module/item/sheets/WitcherItemSheet.js) | Действия/submitOnChange | system.effects → _onEditEffect; общий submit остальных полей | DEFAULT_OPTIONS.actions и _onChangeForm сверены |
| itemEffect; CONFIG.armorEffects | [module/data/item/templates/itemEffectData.js](../../../../../../../module/data/item/templates/itemEffectData.js); [module/setup/config.js](../../../../../../../module/setup/config.js) | Схема/список options | Имя, statusEffect, id/name | Четыре armorEffects; percentage/varEffect не выведены |
| item-header; associated-diagram | [templates/partials/item-header.hbs](../../../../../../../templates/partials/item-header.hbs); [templates/partials/associated-diagram.hbs](../../../../../../../templates/partials/associated-diagram.hbs) | Partial | 2,174 | Точные пути включения; общие поля и рецепт |
| WITCHER.Item.*, Armor.*, Weapon.*, Enhancement.*, Location.* | [lang/ru.json](../../../../../../../lang/ru.json); [lang/en.json](../../../../../../../lang/en.json) | Локализация | Названия и подсказки | Ключи сопоставлены |
| Handlebars helpers; FormDataExtended/DocumentSheetV2 | Foundry 14.367.0, client/applications/handlebars.mjs и client/applications/api/document-sheet.mjs | Внешний API | Рендер и общий submit | Handlebars/parse5 настоящие; сериализация checkbox смоделирована, _processFormData исходный |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/item/sheets/WitcherArmorSheet.js](../../../../../../../module/item/sheets/WitcherArmorSheet.js) | Шаблон | PARTS.main | 10 |
| [module/item/sheets/WitcherItemSheet.js](../../../../../../../module/item/sheets/WitcherItemSheet.js) | data-action/именованные поля | CRUD effects и форма | Обработчики унаследованы |
| [module/actor/mixins/armorMixin.js](../../../../../../../module/actor/mixins/armorMixin.js) | Сохранённые SP/resistance/encumb/type | Расчёт экипированной брони | Связь через ArmorData, не прямой вызов HBS |

Область поиска: текущие module/ и templates/; регистрации сверены отдельно. Динамические обращения внешних модулей не исследовались.

## Данные и изменения состояния

Смена location скрывает неподходящие поля, но не очищает данные других частей. Конфигурация armorGeneral может редактировать все шесть частей независимо от location. Щит хранит reliability, оружие — reliable: эти пути не взаимозаменяемы.

Собственные строки effects дают имя и statusEffect из config.armorEffects; percentage/varEffect остаются в модели, но здесь не редактируются. Воздействия улучшений доступны только для чтения. Форма не выводит список самих enhancementItems/freeEnhancements: его показывает инвентарь Actor.

Checkbox сопротивления читает вычисленное значение. В изолированном сценарии base.slashing=false, улучшение даёт true, checkbox отмечен; передача такого значения через исходный _processFormData и updateSource сохраняет true даже после удаления ID улучшения. Это моделирование сохранения значений формы, не выполненный браузерный submit.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Шесть вариантов | location '',Head,Torso,Leg,FullCover,Shield | 15/17/21/19/27/17 именованных controls с общим header; специфических SP-полей 0/2/6/4/12/0, у Shield 2 надёжности | Включён checkbox clickableImage из настройки, связанный с прежней issue-00063 |
| Воздействия | Одна своя запись и две от улучшения | Два editable поля и четыре disabled controls | Обработчики/ключи сверены, DOM-события — фасад |
| Стороны и торс | Пары name/value и localize во всех строках | leftLeg/rightLeg и torso.maxStoppingPower адресуют свои значения | Tooltip инвентаря — другой файл |
| Сопротивление | Настоящие модели, HBS, исходный _processFormData, updateSource | Вычисленное true попало в submit и сохранилось без улучшения | FormData.object собран из отрендеренных checkbox; не реальный браузер |

## Непроверенные участки и открытые вопросы

Не проверено сохранение через полный DocumentSheetV2/FormDataExtended в браузере, динамическая геометрия recipe-drop, HTTP-доступ и внешний CSS. Все 175 строк прочитаны и сопоставлены с моделями/обработчиками.

## Связанные проблемы

[issue-00007](../../../../../../issues/potential/issue-00007.md), [issue-00060](../../../../../../issues/potential/issue-00060.md), [issue-00063](../../../../../../issues/potential/issue-00063.md), [issue-00080](../../../../../../issues/potential/issue-00080.md), [issue-00082](../../../../../../issues/potential/issue-00082.md), [issue-00084](../../../../../../issues/potential/issue-00084.md), [issue-00088](../../../../../../issues/potential/issue-00088.md). Подписи текущей формы не дублируют ошибку helper из issue-00007. Остальные наблюдения относятся к унаследованным элементам и потреблению данных.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.014 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.
