# module/item/sheets/configurations/WitcherConsumableConfigurationSheet.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/item/sheets/configurations/WitcherConsumableConfigurationSheet.js](../../../../../../../../module/item/sheets/configurations/WitcherConsumableConfigurationSheet.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `7edb814aa870da75c7ad7633536e899a8d07e205` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.015](../../../../../../../tasks/task-0003.015.md), одна порция из пятнадцати файлов |
| Запись перекрёстной сверки | [TASK-0003.015](../../../../../review-log.md#task-0003015) |

## Назначение файла

Расширяет общую configuration вкладкой расходования и обработчиками двух массивов предметных статусов.

## Условия использования

Создаётся листами WitcherAlchemicalSheet/WitcherValuableSheet как configuration. WitcherMutagenSheet его не подключает. Наследуется контекст и сохранение обычных полей WitcherConfigurationSheet; ручные массивы используют собственные actions/listeners.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| WitcherConsumableConfigurationSheet | default class | Специализированный редактор | Прямые импорты двух листов | Окно того же Item |
| DEFAULT_OPTIONS.actions | static object | addEffect→_onAddEffect; removeEffect→_oRemoveEffect | Диспетчер ApplicationV2 | Обработчики клика |
| PARTS | static object + super.PARTS | consumableProperties.template; scrollable=[''] | HBM | Всего header/tabs/general/activeEffects/consumableProperties |
| TABS.primary | static object + super.TABS.primary | general, consumableProperties, activeEffects | Подготовка вкладок | Сохраняет начальную general и labelPrefix родителя |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| _onRender(context, options) | Результат рендера / this.element | undefined | Вызывает super; input[editEffect]→focusout; select[editEffect]→input | Не await super; создаёт bind(this) для каждого слушателя |
| static async _onAddEffect(event, element) | dataset.target: effects или removesEffects | Promise без результата update | preventDefault; берёт массив ?? []; push({percentage:100}); update всего массива | Мутирует подготовленный массив; id не создаётся; update не await/return |
| async _onEditEffect(event) | currentTarget.closest('.list-item'); dataset.id/target/field, value | Promise; ошибка при отсутствии записи | value=='on'→checked; findIndex(obj.id==itemId); присваивает поле; update массива | Обычный пустой data-id даёт index=-1 и TypeError до update; записи/ожидания нет |
| static async _oRemoveEffect(event, element) | Ближайшая строка с id/target | Promise без результата update | filter(item.id!==itemId); update массива | При id=undefined и data-id='' ничего не удаляет; update не await/return |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| WitcherConfigurationSheet | [module/item/sheets/configurations/WitcherConfigurationSheet.js](../../../../../../../../module/item/sheets/configurations/WitcherConfigurationSheet.js) | Прямой импорт / наследование | Базовые части, tabs, контекст, формы/эффекты | Определение и место использования сверены |
| Вкладка расходования | [templates/sheets/item/configuration/tabs/consumablePropertiesConfiguration.hbs](../../../../../../../../templates/sheets/item/configuration/tabs/consumablePropertiesConfiguration.hbs) | PARTS.template | data-action / data-target / data-field / data-id | Определение и место использования сверены |
| ConsumablePropertiesData | [module/data/item/templates/consumePropertiesData.js](../../../../../../../../module/data/item/templates/consumePropertiesData.js) | Контракт данных | Массивы effects/removesEffects | Определение и место использования сверены |
| itemEffect() | [module/data/item/templates/itemEffectData.js](../../../../../../../../module/data/item/templates/itemEffectData.js) | Вложенная схема | В записи отсутствует id | Определение и место использования сверены |
| Item.update / ApplicationV2 actions / DOM events | Foundry и браузерные API | Внешний API | Сохранение и события | Определение и место использования сверены |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/item/sheets/WitcherAlchemicalSheet.js](../../../../../../../../module/item/sheets/WitcherAlchemicalSheet.js) | Класс configuration | Создание экземпляра | Прямой импорт |
| [module/item/sheets/WitcherValuableSheet.js](../../../../../../../../module/item/sheets/WitcherValuableSheet.js) | Класс configuration | Создание экземпляра | Прямой импорт |
| [templates/sheets/item/configuration/tabs/consumablePropertiesConfiguration.hbs](../../../../../../../../templates/sheets/item/configuration/tabs/consumablePropertiesConfiguration.hbs) | actions и _onEditEffect | Клики, focusout/input | Разметка и ручная привязка |

Область поиска: текущие module/ и templates/; регистрации сверены отдельно. Динамические обращения внешних модулей не исследовались.

## Данные и изменения состояния

Обычные поля формы именованные; ручные поля строк не имеют name и обновляются отдельным Item.update. Для effects редактируются name/statusEffect, для removesEffects только statusEffect. В обоих массивах элемент не имеет id, а HBS не использует доступный индекс each. Ошибка поиска не связана с отсутствием имени или конкретным выбранным статусом. Значения не нормализуются по типу поля, кроме эвристики value=='on'. Этот последний дефект совпадает с issue-00060, но здесь закрыт более ранней ошибкой идентификации.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Схема→DOM→метод | Настоящая модель и HBS; исходные add/edit/remove | Два списка: пустой data-id; edit TypeError; remove передаёт прежний массив; add добавляет {percentage:100} | Запись update перехвачена; не DB |
| Связь событий | Исходный _onRender с DOM-фасадом | focusout для input, input для select; базовый рендер вызван | Полный цикл браузера не проверен |
| Текст on | В подготовленную запись вручную добавлен временный id, совпадающий с DOM | _onEditEffect сформировал name=false | Изолирует только эвристику; такой id модель не сохраняет |
| Вкладки | Исходные методы HBM/Core + _prepareContext | 3 вкладки, 5 частей | Внешний DocumentSheet — фасад |

## Непроверенные участки и открытые вопросы

Не проверялись server-side update, конкурентное редактирование массивов и полный FormDataExtended. Тесты не доказывают сохранение ручного id и не устраняют issue-00091. Имена actions не означают создание документов ActiveEffect: здесь меняются только обычные записи статусов.

## Связанные проблемы

[issue-00091](../../../../../../../issues/potential/issue-00091.md), [issue-00092](../../../../../../../issues/potential/issue-00092.md), [issue-00060](../../../../../../../issues/potential/issue-00060.md), [issue-00093](../../../../../../../issues/potential/issue-00093.md). 91/92 относятся к этой configuration; 60 — условная ветвь после успешного поиска записи; 93 — отсутствие подключения у мутагена.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.015 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.
