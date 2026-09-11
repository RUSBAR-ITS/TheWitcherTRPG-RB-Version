# module/data/actor/lootData.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/data/actor/lootData.js](../../../../../../../module/data/actor/lootData.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `fe7ea7420cd4dfa6ee51baf7520f7b0ad8f8b13d` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.006](../../../../../../tasks/task-0003.006.md), одна порция из четырёх файлов |
| Запись перекрёстной сверки | [TASK-0003.006](../../../../review-log.md#task-0003006) |

## Назначение файла

Самостоятельная модель Actor.loot для хранилища добычи: максимальная отображаемая вместимость, описание и валюты. Предметы хранятся в Actor.items; модель считает только массу монет.

## Условия использования

LootData напрямую наследует foundry.abstract.TypeDataModel, CommonActorData не импортирует. [module/setup/registerDataModels.js](../../../../../../../module/setup/registerDataModels.js):3,40 регистрирует класс в CONFIG.Actor.dataModels.loot; [system.json](../../../../../../../system.json) объявляет loot, [module/setup/registerSheets.js](../../../../../../../module/setup/registerSheets.js):113–116 назначает WitcherLootSheet. Доступ к данным — Actor.system.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| fields | const:3 | Классы полей | Локальная | Чтение при defineSchema |
| LootData | class:5–25 | Модель хранилища | Default export; Actor.loot | Определение схемы; расчёт массы |

| Поле system | Тип / initial | Определение и источник | Назначение |
| --- | --- | --- | --- |
| maxWeight | NumberField / 0 | :8; локальное определение | Настройка полосы веса; своих min/max/integer нет. |
| description | StringField / '' | :9; локальное определение | Строка описания; в текущем loot-sheet.hbs её прямое отображение/редактирование не найдено. |
| currency | SchemaField(currency()) | :10; [module/data/actor/templates/common/currencyData.js](../../../../../../../module/data/actor/templates/common/currencyData.js) | bizant, ducat, lintar, floren, crown, oren, falsecoin; каждое число начинается с 0. |

stats, derivedStats, healthState, attackStats, notes, logs и другие поля CommonActorData/CharacterData не включаются. Собственных изображений/имени/массива предметов схема не вводит: name, img, items принадлежат Actor.

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| static defineSchema:6–12 | fields и currency | Объект трёх полей | Создаёт два поля и SchemaField(currency()) | Синхронно; super.defineSchema не вызывает; записи документов нет. |
| calcCurrencyWeight:14–24 | Семь значений this.currency | Number | Number каждого значения, сумма ×0.001, внешний Number | Без округления вверх, проверок диапазона, catch или побочных действий. |

Собственных prepareBaseData, prepareDerivedData, migrateData, enrichedText и вычисляемых getters нет. Пустые подготовительные методы и стандартная миграция наследуются от TypeDataModel/DataModel; миграции CommonActorData к LootData не относятся.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| currency | [module/data/actor/templates/common/currencyData.js](../../../../../../../module/data/actor/templates/common/currencyData.js); [карточка](templates/common/currencyData.js.md) | Импорт:1; вызов:10; чтение:16–22 | Одна и та же фабрика валют, что у CommonActorData | Семь имён совпали с телом calcCurrencyWeight. |
| TypeDataModel | Foundry 14.367.0: /opt/foundryvtt/common/abstract/type-data.mjs | Наследование:5 | Модель system | Настоящий класс в проверке. |
| NumberField, StringField, SchemaField | Foundry 14.367.0: /opt/foundryvtt/common/data/fields.mjs | Глобальный API fields:3 | defineSchema | Настоящие поля и экземпляр. |
| Number | ECMAScript | Преобразование:16–23 | Числовая сумма монет | Не перевод курсов валют; не масса Actor.items. |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/setup/registerDataModels.js](../../../../../../../module/setup/registerDataModels.js); [system.json](../../../../../../../system.json); [module/setup/registerSheets.js](../../../../../../../module/setup/registerSheets.js) | LootData / loot | Модель, манифест и лист одного типа | 3,40; Actor.loot;113–116 |
| [module/actor/witcherActor.js](../../../../../../../module/actor/witcherActor.js) | system.calcCurrencyWeight() | getTotalWeight суммирует массы items и монет, округляет Math.ceil | 245–247; prepareDerivedData:38 пропускает loot. |
| [module/actor/sheets/WitcherLootSheet.js](../../../../../../../module/actor/sheets/WitcherLootSheet.js) | system и getTotalWeight | _prepareContext передаёт модель и totalWeight | 48,61; PARTS:21–25 использует loot-sheet.hbs |
| [templates/sheets/actor/loot-sheet.hbs](../../../../../../../templates/sheets/actor/loot-sheet.hbs) | maxWeight и семь валют | Форма maxWeight; при >0 полоса/перегруз; поля currency | 3–25,43 и далее; name/img — поля Actor. |
| [module/data/actor/commonActorData.js](../../../../../../../module/data/actor/commonActorData.js) | Сопоставимый calcCurrencyWeight | Не вызов LootData: независимая реализация того же расчёта | 93–103; общий импорт currency не означает наследование. |

Поиск потребителей выполнен в module/, templates/, packsJson/; отдельно прочитаны регистрация и текущая форма loot. Поиск system.description выдаёт другие типы Actor/Item; они не считаются доказательством использования LootData.description.

## Данные и изменения состояния

Собственные методы не делают update/create/delete. calcCurrencyWeight возвращает сырую массу семи валют с одинаковым коэффициентом; номинальная стоимость монеты не влияет на массу. Округляет общий вес Actor.getTotalWeight, а не эта модель. maxWeight используется проверенной формой для индикации; модель не запрещает превышение вместимости. Операции переноса/покупки предметов и изменения кошелька относятся к листу и mixins и здесь целиком не проверялись.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Схема | 25 строк; один импорт; настоящий LootData | Ровно maxWeight, description, currency; нет полей CommonActorData | Не игровой Actor. |
| Масса | По одной монете каждого вида, реальный calcCurrencyWeight | 0.007, как у Common/Character/Monster | Изолированный вызов, без предметов. |
| Регистрация и форма | registerDataModels, manifest, registerSheets, WitcherLootSheet.PARTS | loot присутствует во всех трёх декларациях; текущая форма найдена | Не запуск рендера/сохранения. |
| Перекрёстная сверка | Общая фабрика currency и карточка TASK-0003.003 | Состав валют и различие массы модели/округления Actor согласованы | Экономика и обмен не пересматривались. |

## Непроверенные участки и открытые вопросы

Файл прочитан полностью. Не проверены покупки, перенос предметов, сохранение формы и содержимое миров. Отсутствие прямого потребителя description в текущей форме не объявлено ошибкой. Динамические обращения внешних модулей не исследованы.

## Связанные проблемы

Новых проблем непосредственно в LootData при этом разборе не зарегистрировано. [issue-00020](../../../../../../issues/potential/issue-00020.md) относится к обмену валют в общем потребителе, а [issue-00005](../../../../../../issues/potential/issue-00005.md) — к другим типам: loot в манифесте присутствует. Это не вывод об исправности всех операций с добычей.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.006 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.

## Уточнение TASK-0003.007

2026-09-10, `b8b89a7e3392235f993c21f3c6d277a4a2e7a55f`. WitcherActor.prepareDerivedData возвращается после super для type=loot, не обращаясь к stats/derivedStats. getTotalWeight суммирует calcWeight всех items и calcCurrencyWeight модели с Math.ceil; getList фильтрует stored для обычных типов, но не в специальной ветке shield.

Карточки: [WitcherActor](../../actor/witcherActor.js.md), [modifierMixin](../../actor/mixins/modifierMixin.js.md). [Сверка TASK-0003.007](../../../../review-log.md#task-0003007).

## Уточнение TASK-0003.032

2026-09-11, `8b938d44a042749df027d8b58e28bb1d79638091`. Экспорт Monster создаёт Actor type loot из полной actor.toObject с новым name/folder, затем пересчитывает все embedded Items. Payload сохраняет исходные system/items/effects/ownership/flags/prototypeToken; реально нормализованный документ ядра в тесте не создавался. Экспорт не фильтруется context.loots. Работа самого Loot-листа остаётся .035.

Связи: [module/actor/sheets/WitcherMonsterSheet.js](../../actor/sheets/WitcherMonsterSheet.js.md). [Результаты и пределы проверки](../../../../review-log.md#task-0003032).

## Дополнительная сверка TASK-0003.035

2026-09-11, `rusbar-main`, `1d29f681ffed1c46b9c05b0eff09935300c3bf7d`; исходники не менялись.

Полный consumer WitcherLootSheet читает maxWeight и currency, считает totalWeight через Actor.getTotalWeight→calcCurrencyWeight; HBS даёт семь валют. Модель не содержит skills, поэтому profession Drop через общий itemMixin вызывает TypeError (issue225). totalCost не поле схемы и не вычисленный контекст LootSheet (issue219). Наличие mount с HP0 не меняет модель loot.

Полные карточки порции: [module/actor/sheets/WitcherLootSheet.js](../../actor/sheets/WitcherLootSheet.js.md), [templates/sheets/actor/loot-sheet.hbs](../../../templates/sheets/actor/loot-sheet.hbs.md), [templates/sheets/actor/partials/loot/loot-item-display.hbs](../../../templates/sheets/actor/partials/loot/loot-item-display.hbs.md), [module/data/item/mountData.js](../item/mountData.js.md), [module/item/sheets/WitcherMountSheet.js](../../item/sheets/WitcherMountSheet.js.md), [templates/sheets/item/mount-sheet.hbs](../../../templates/sheets/item/mount-sheet.hbs.md).

[Проверки, общая сверка 31 файла с прежними 247 и ограничения](../../../../review-log.md#task-0003035). Связанный файл повторно в покрытии не учитывается; исправления не выполнялись.
