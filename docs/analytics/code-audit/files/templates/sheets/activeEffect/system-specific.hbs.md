# templates/sheets/activeEffect/system-specific.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/sheets/activeEffect/system-specific.hbs](../../../../../../../templates/sheets/activeEffect/system-specific.hbs) |
| Тип файла | Handlebars, HTML-шаблон |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `247d3d86e344238a1445377c686eb6455146693c` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.010](../../../../../../tasks/task-0003.010.md), одна порция из восьми файлов |
| Запись перекрёстной сверки | [TASK-0003.010](../../../../review-log.md#task-0003010) |

## Назначение файла

Отображает системные флаги ActiveEffect: фазу вычислений и условия переноса воздействия при использовании предмета.

## Условия использования

PARTS.systemSpecific зарегистрирован WitcherActiveEffectConfig. Контекст содержит tab, document и systemFields; isItemEffect берётся из core _preparePartContext('details') при полном рендере с общим контекстом. Шаблон не создаёт собственную форму сохранения.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| section.tab.scrollable | 1–11 | Часть systemSpecific | data-group=tab.group, data-tab=tab.id, класс active | Tab-navigation ядра |
| Пять formGroup | 2–8 | Поля системной модели | applyAfterCalculations всегда; applySelf/applyOnTarget при isItemEffect; applyOnHit/applyOnDamage дополнительно при !isTemporaryItemImprovement | isTransferred не выводится |
| if/unless | 3–10 | Условия отображения | Handlebars | Не включают/выключают сами эффекты |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| Рендер Handlebars; 1–11 | systemFields, document.system, isItemEffect, tab | HTML системной вкладки | formGroup с value и localize=true | Собственных функций/записи нет |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| systemFields и PARTS | [module/activeEffect/WitcherActiveEffectSheet.js](../../../../../../../module/activeEffect/WitcherActiveEffectSheet.js) | Контекст и регистрация | document.system.schema.fields | _prepareContext и PARTS.systemSpecific |
| Пять флагов base | [module/data/activeEffects/witcherActiveEffectData.js](../../../../../../../module/data/activeEffects/witcherActiveEffectData.js) | BooleanField | Отображение и имя поля через formGroup | applyAfterCalculations, applySelf, applyOnTarget, applyOnHit, applyOnDamage |
| Поля temporary | [module/data/activeEffects/witcherTemporaryItemImprovementData.js](../../../../../../../module/data/activeEffects/witcherTemporaryItemImprovementData.js) | Другая схема | Есть applySelf/applyOnTarget/isTransferred, нет applyAfterCalculations | Безусловная первая formGroup получает undefined |
| isTemporaryItemImprovement; _preUpdate | [module/activeEffect/witcherActiveEffect.js](../../../../../../../module/activeEffect/witcherActiveEffect.js) | Геттер и обработчик | Условие видимости; преобразование флага в phase | Сам шаблон не меняет change.phase |
| formGroup; наследуемое сохранение | /opt/foundryvtt/client/applications/handlebars.mjs; sheets/active-effect-config.mjs; api/document-sheet.mjs | Внешний API | Поле формирует input; submit обрабатывает форму | При field=undefined helper пишет console.error и возвращает пустую строку |
| Локализация labels модели | [lang/en.json](../../../../../../../lang/en.json); [lang/ru.json](../../../../../../../lang/ru.json) | Через formGroup localize | Подписи WITCHER.Effect.* | Определения label находятся в схемах |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/activeEffect/WitcherActiveEffectSheet.js](../../../../../../../module/activeEffect/WitcherActiveEffectSheet.js) | Полный шаблон | PARTS.systemSpecific | Единственная системная точка включения |
| ActiveEffectConfig/DocumentSheetV2 ядра | Поля сформированной формы | Обработка submit и document.update | Не обработчик данного HBS |

## Данные и изменения состояния

Обычный Item-эффект показывает пять флагов; Actor-эффект — только applyAfterCalculations. Временное улучшение Item показывает два условия использования, но первая безусловная formGroup обращается к отсутствующему applyAfterCalculations. В текущем ядре это сообщение об ошибке и пустой фрагмент, а не доказанный срыв всей формы.

Переключатели относятся к эффекту целиком. Они не являются свойствами отдельного бонуса и не задают минимум/максимум характеристики. Корневой transfer находится в стандартной вкладке details ядра, не здесь.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Поля ↔ модели | 11 строк и настоящие system.schema двух типов | Base содержит пять ожидаемых полей; temporary — только два видимых и служебный isTransferred | Без записи |
| Рендер | Настоящие Handlebars и formGroup; фасад для toFormGroup существующих полей | Base: пять input, без ошибок; temporary Item: два input и одна ошибка отсутствующего поля | Полные DOM-input и браузер не воспроизводились |
| Контекст | Прочитаны core _preparePartContext и общий контекст HandlebarsApplicationMixin | isItemEffect из details доступен следующим частям обычного полного рендера | Частичный рендер отдельно не запускался |

## Непроверенные участки и открытые вопросы

Проверка полного сохранения формы, частичных рендеров только systemSpecific и реальной локализации остаётся вне изолированного сценария.

## Связанные проблемы

[issue-00053](../../../../../../issues/potential/issue-00053.md) — отсутствующее поле временного улучшения; [issue-00043](../../../../../../issues/potential/issue-00043.md) — согласование флага с changes при частичном обновлении.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.010 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.
