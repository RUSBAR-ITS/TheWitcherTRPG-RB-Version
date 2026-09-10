# module/data/activeEffects/witcherTemporaryItemImprovementData.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/data/activeEffects/witcherTemporaryItemImprovementData.js](../../../../../../../module/data/activeEffects/witcherTemporaryItemImprovementData.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `a33bf33add228ae93f96a52046c8feb4ee992921` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.009](../../../../../../tasks/task-0003.009.md), одна порция из восьми файлов |
| Запись перекрёстной сверки | [TASK-0003.009](../../../../review-log.md#task-0003009) |

## Назначение файла

Модель system эффекта типа temporaryItemImprovement: наследует список changes ядра и добавляет три флага маршрутизации/передачи. Не создаёт улучшение и не исполняет его изменения.

## Условия использования

При импорте определяется fields и экспортируемый класс. [module/setup/registerDataModels.js](../../../../../../../module/setup/registerDataModels.js) назначает модель CONFIG.ActiveEffect.dataModels.temporaryItemImprovement. Foundry создаёт её как effect.system. Статическая metadata заморожена и содержит type='temporaryItemImprovement'; системная модель объявлена отдельно от WitcherActiveEffectData и не наследует его дополнительные свойства.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| fields | Константа, 1 | Классы полей Foundry | Локальная | Читается defineSchema |
| WitcherTemporaryItemImprovementData | Класс, 3–22 | Системные данные эффекта | default export; реестр ActiveEffect | Создаётся ядром |
| metadata | Статическое Object.freeze, 4–6 | type: temporaryItemImprovement | Класс модели | Замороженный объект; не флаг экземпляра |
| changes | Унаследованное поле через ...super.defineSchema() | Массив изменений | effect.system.changes | Определение — в ядре, не повторно в этом файле |
| applySelf | BooleanField, 11 | initial=false, label=WITCHER.Effect.applySelf | effect.system.applySelf | Хранится в данных; само поле ничего не применяет |
| applyOnTarget | BooleanField, 15 | initial=false, label=WITCHER.Effect.applyOnTarget | effect.system.applyOnTarget | Хранится в данных; само поле ничего не применяет |
| isTransferred | BooleanField, 19 | initial=false | effect.system.isTransferred | Хранится в данных; само поле ничего не применяет |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| WitcherTemporaryItemImprovementData.defineSchema; 8–21 | Доступны foundry.data.fields и ActiveEffectTypeDataModel | Объект схемы: changes + 3 BooleanField | Расширяет ...super.defineSchema; собственных lifecycle-методов нет | Синхронно; не пишет документы |

Общая схема ядра Foundry 14.367.0 `/opt/foundryvtt/common/data/active-effect.mjs:15–26`: changes — ArrayField(SchemaField), ключи key:StringField(required), type:StringField(required, blank=false, initial='add'), value:AnyField(required, nullable, serializable, initial=''), phase:StringField(required, blank=false, initial='initial'), priority:NumberField без собственного initial. В изоляции у записи с key заданным и прочими полями по умолчанию priority был undefined и не попал в JSON. Тип проверяется на допустимый формат строки, а не на существование обработчика конкретной операции. DefaultPriority позже заполняет core ActiveEffect.prepareBaseData по change.type.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| ActiveEffectTypeDataModel / defineSchema | Foundry 14.367.0; common/data/active-effect.mjs | Наследование, super | changes и его схема/валидация | Исходное определение прочитано; использована настоящая модель |
| foundry.data.fields.BooleanField | Foundry common/data/fields.mjs | Конструирование | Собственные флаги | Оригинальная схема и начальные значения выполнены |
| Ключи WITCHER.Effect.* | [lang/en.json](../../../../../../../lang/en.json); [lang/ru.json](../../../../../../../lang/ru.json) | Локализация label | Все собственные поля кроме isTransferred имеют label | Ключи указаны в исходнике; наличие сверено |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/setup/registerDataModels.js](../../../../../../../module/setup/registerDataModels.js) | WitcherTemporaryItemImprovementData | Импорт/назначение реестра | Связь двусторонне уточнена |
| [module/activeEffect/witcherActiveEffect.js](../../../../../../../module/activeEffect/witcherActiveEffect.js) | applySelf, applyOnTarget, isTransferred | isSuppressed; isAppliedTemporaryItemImprovement/_preCreate | Полный разбор документа в этой порции |
| [module/scripts/temporaryEffects/applyActiveEffect.js](../../../../../../../module/scripts/temporaryEffects/applyActiveEffect.js) | applySelf/applyOnTarget | ViaId читает system[applyWhen]; этот тип направляется отдельному обработчику улучшений | 32–67; схема не выбирает получателя самостоятельно |
| [module/actor/mixins/temporaryEffectMixin.js](../../../../../../../module/actor/mixins/temporaryEffectMixin.js) | isTransferred; changes | Выбирает только temporaryItemImprovement; заменяет system тремя флагами | 4–46; issue-00042, отдельная модель не наследуется от base |
| [module/actor/mixins/castSpellMixin.js](../../../../../../../module/actor/mixins/castSpellMixin.js) | applySelf, applyOnTarget | Фильтрация эффектов при успешном заклинании | 253–267; дальнейший маршрут в applyActiveEffect.js |
| [module/item/witcherItem.js](../../../../../../../module/item/witcherItem.js) | isTransferred → isAppliedTemporaryItemImprovement; changes | Применение улучшений к Item одним проходом | 331–368; карточка Item дополнена |
| [module/actor/witcherActor.js](../../../../../../../module/actor/witcherActor.js) | isAppliedTemporaryItemImprovement | temporaryEffects добавляет эффекты Item с этим признаком | 26–33; это показ эффектов, не копирование changes |
| [module/activeEffect/WitcherActiveEffectSheet.js](../../../../../../../module/activeEffect/WitcherActiveEffectSheet.js) | system.schema.fields | Контекст systemFields для формы | _prepareContext:39–42; полный разбор — TASK-0003.010 |
| [templates/sheets/activeEffect/system-specific.hbs](../../../../../../../templates/sheets/activeEffect/system-specific.hbs) | Флаги модели | formGroup по системным полям | Интерфейс следующей порции; наличие поля не доказывает его работу |

## Данные и изменения состояния

В файле отсутствуют update/create/delete, броски, Hooks и доступ к Actor. Name, img, disabled, transfer, statuses, origin, start и duration находятся на документе ActiveEffect в ядре. `isTransferred` — признак уже перенесённого улучшения; он не равнозначен корневому transfer, который участвует в переносе эффекта Item на Actor. applyAfterCalculations/applyOnHit/applyOnDamage здесь не определены. Системные флаги по умолчанию false не фильтруют disabled самостоятельно.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Полнота | Полное чтение 22 строк, регистрация, все обращения к флагам | Одна схема; 3 собственных флага; changes унаследован | Файл не исполняет воздействий |
| Модель Foundry | Оригинальный класс + реальные ActiveEffectTypeDataModel/fields в Node | changes=[]; все флаги false; запись changes получает add/initial/'' | Нет сохранения ActiveEffect в мире |
| Потребители | Класс, маршруты, Actor/Item, листы и шаблоны | Указаны реальные условия/фильтры, а не только наличие свойств | Полный UI следующей порции |

## Непроверенные участки и открытые вопросы

Модель и зависимости прочитаны в указанном объёме; реальный клиент, пользовательские обновления и серверное хранение не запускались. Полные маршруты сетевой передачи, интерфейс и конкретные игровые эффекты не подтверждаются проверкой default-значений. Источник унаследованных полей зафиксирован для 14.367.0; другие версии не исследованы.

## Связанные проблемы

[issue-00042](../../../../../../issues/potential/issue-00042.md) — потеря changes в передатчике; [issue-00050](../../../../../../issues/potential/issue-00050.md) — начало длительности при применении улучшения. Сама схема не исправлялась; статусы potential сохранены.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.009 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.
