# module/data/item/commonItemData.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/data/item/commonItemData.js](../../../../../../../module/data/item/commonItemData.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `c5edcbadd05ff4038a174bd2e2a49785e40ea878` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.008](../../../../../../tasks/task-0003.008.md), одна порция из двух файлов |
| Запись перекрёстной сверки | [TASK-0003.008](../../../../review-log.md#task-0003008) |

## Назначение файла

Общая TypeDataModel для части типов Item: восемь полей описания, количества, массы, стоимости и видимости/хранения; расчёт массы и два признака возможностей. Это модель `item.system`, а не документ Item. Файл не задаёт эффекты, рецепты, атаки, ремонт и потребление.

## Условия использования

При импорте сохраняется ссылка `fields = foundry.data.fields` и определяется экспортируемый класс. [module/setup/registerDataModels.js](../../../../../../../module/setup/registerDataModels.js) регистрирует его непосредственно как `CONFIG.Item.dataModels.base`. Ещё 16 зарегистрированных моделей прямо наследуют CommonItemData и включают `...super.defineSchema()`; отложенная настройка полей относится к созданию/подготовке модели ядром, а не к записи в БД при импорте.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| fields | Локальная константа, 1 | Ссылка на классы полей Foundry | Не экспортируется | Используется defineSchema |
| CommonItemData | Класс, 3–29 | Общая модель Item | default export; регистрация base | Ядро создаёт как system документа; наследники расширяют схему |
| description | StringField; Описание; 6 | Начальное значение `''` | `item.system.description` | Определение поля; сам файл его не сохраняет |
| quantity | StringField; Количество, в том числе строковая формула добычи; 7 | Начальное значение `'1'` | `item.system.quantity` | Определение поля; сам файл его не сохраняет |
| weight | NumberField; Масса единицы; 8 | Начальное значение `0` | `item.system.weight` | Определение поля; сам файл его не сохраняет |
| cost | NumberField; Стоимость единицы; 9 | Начальное значение `0` | `item.system.cost` | Определение поля; сам файл его не сохраняет |
| sourcebook | StringField; Источник; 10 | Начальное значение `''` | `item.system.sourcebook` | Определение поля; сам файл его не сохраняет |
| isHidden | BooleanField; Признак скрытия; 12 | Начальное значение `false` | `item.system.isHidden` | Определение поля; сам файл его не сохраняет |
| isStored | BooleanField; Хранение в контейнере; 13 | Начальное значение `false` | `item.system.isStored` | Определение поля; сам файл его не сохраняет |
| isCarried | BooleanField; Предмет несут; 14 | Начальное значение `true` | `item.system.isCarried` | Определение поля; сам файл его не сохраняет |
| canHaveTemporaryItemImprovement / canBeRepaired | Геттеры, 22–28 | Базовые ответы false | Через item.system | Признаки для потребителей; не запреты на уровне БД |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| CommonItemData.defineSchema; 4–16 | Доступны fields | Новый объект из 8 полей | Не вызывает super.defineSchema; задаёт initial, собственных min/max/choices нет | Синхронно, без update |
| CommonItemData.calcWeight; 18–20 | Подготовленные quantity, weight, isCarried, isStored | isCarried && !isStored ? quantity × weight : 0 | Использует обычное числовое приведение JS при умножении | Без округления, вычисления Roll, проверки NaN и нижней границы; не изменяет поля |
| CommonItemData.canHaveTemporaryItemImprovement; 22–24 | Экземпляр | false | Базовый ответ для интерфейса создания улучшения | Синхронный getter |
| CommonItemData.canBeRepaired; 26–28 | Экземпляр | false | Базовый ответ для отображения ремонта | Синхронный getter |

`quantity` намеренно описано как строковое поле: [module/actor/sheets/WitcherMonsterSheet.js](../../../../../../../module/actor/sheets/WitcherMonsterSheet.js) при экспорте добычи (190–203) отдельно вычисляет строки с `d` через Roll. CommonItemData этого не делает: '1d6' × 2 даёт NaN; '-2' × 2 даёт -4. Эти результаты показывают границы расчёта, но не подтверждают, что такие значения допустимы по игровым правилам или должны одинаково обрабатываться у всех Actor. `isHidden` не участвует в calcWeight; `isStored` и `isCarried` участвуют независимо.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| TypeDataModel; StringField, NumberField, BooleanField | Foundry 14.367.0: /opt/foundryvtt/common/abstract/type-data.mjs; /opt/foundryvtt/common/data/fields.mjs | Наследование, конструирование | Схема system, приведение и начальные значения | Прямые обращения 1–14; изолированно использованы настоящие классы |
| Другие сущности системы | Прямых импортов нет | Отсутствие импортной зависимости | CommonItemData не вызывает Actor, Item, Roll или helpers системы | Полное чтение 29 строк |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/setup/registerDataModels.js](../../../../../../../module/setup/registerDataModels.js) | CommonItemData | Импорт и регистрация Item.base; 12, 47 | Сверено с определением и карточкой регистрации |
| [module/data/item/alchemicalData.js](../../../../../../../module/data/item/alchemicalData.js) | CommonItemData; super.defineSchema | Прямое наследование; зарегистрирован как alchemical; canHaveTemporaryItemImprovement → true | Проверены extends, состав общей схемы и указанные переопределения |
| [module/data/item/armorData.js](../../../../../../../module/data/item/armorData.js) | CommonItemData; super.defineSchema | Прямое наследование; зарегистрирован как armor; canBeRepaired → associatedDiagramUuid и повреждение хотя бы одного показателя брони/надёжности | Проверены extends, состав общей схемы и указанные переопределения |
| [module/data/item/componentData.js](../../../../../../../module/data/item/componentData.js) | CommonItemData; super.defineSchema | Прямое наследование; зарегистрирован как component; Общие методы наследуются | Проверены extends, состав общей схемы и указанные переопределения |
| [module/data/item/containerData.js](../../../../../../../module/data/item/containerData.js) | CommonItemData; super.defineSchema | Прямое наследование; зарегистрирован как container; calcWeight добавляет storedWeight | Проверены extends, состав общей схемы и указанные переопределения |
| [module/data/item/diagramData.js](../../../../../../../module/data/item/diagramData.js) | CommonItemData; super.defineSchema | Прямое наследование; зарегистрирован как diagrams; Общие методы наследуются; поля рецепта добавляет сама DiagramData | Проверены extends, состав общей схемы и указанные переопределения |
| [module/data/item/enhancementData.js](../../../../../../../module/data/item/enhancementData.js) | CommonItemData; super.defineSchema | Прямое наследование; зарегистрирован как enhancement; Общие методы наследуются | Проверены extends, состав общей схемы и указанные переопределения |
| [module/data/item/hexData.js](../../../../../../../module/data/item/hexData.js) | CommonItemData; super.defineSchema | Прямое наследование; зарегистрирован как hex; Общие методы наследуются | Проверены extends, состав общей схемы и указанные переопределения |
| [module/data/item/mountData.js](../../../../../../../module/data/item/mountData.js) | CommonItemData; super.defineSchema | Прямое наследование; зарегистрирован как mount; Общие методы наследуются | Проверены extends, состав общей схемы и указанные переопределения |
| [module/data/item/mutagenData.js](../../../../../../../module/data/item/mutagenData.js) | CommonItemData; super.defineSchema | Прямое наследование; зарегистрирован как mutagen; Общие методы наследуются | Проверены extends, состав общей схемы и указанные переопределения |
| [module/data/item/noteData.js](../../../../../../../module/data/item/noteData.js) | CommonItemData; super.defineSchema | Прямое наследование; зарегистрирован как note; Общие методы наследуются | Проверены extends, состав общей схемы и указанные переопределения |
| [module/data/item/professionData.js](../../../../../../../module/data/item/professionData.js) | CommonItemData; super.defineSchema | Прямое наследование; зарегистрирован как profession; Общие методы наследуются; добавляет enrichedText | Проверены extends, состав общей схемы и указанные переопределения |
| [module/data/item/raceData.js](../../../../../../../module/data/item/raceData.js) | CommonItemData; super.defineSchema | Прямое наследование; зарегистрирован как race; Общие методы наследуются; добавляет enrichedText | Проверены extends, состав общей схемы и указанные переопределения |
| [module/data/item/ritualData.js](../../../../../../../module/data/item/ritualData.js) | CommonItemData; super.defineSchema | Прямое наследование; зарегистрирован как ritual; Общие методы наследуются | Проверены extends, состав общей схемы и указанные переопределения |
| [module/data/item/spellData.js](../../../../../../../module/data/item/spellData.js) | CommonItemData; super.defineSchema | Прямое наследование; зарегистрирован как spell; canHaveTemporaryItemImprovement → true | Проверены extends, состав общей схемы и указанные переопределения |
| [module/data/item/valuableData.js](../../../../../../../module/data/item/valuableData.js) | CommonItemData; super.defineSchema | Прямое наследование; зарегистрирован как valuable; canHaveTemporaryItemImprovement → true | Проверены extends, состав общей схемы и указанные переопределения |
| [module/data/item/weaponData.js](../../../../../../../module/data/item/weaponData.js) | CommonItemData; super.defineSchema | Прямое наследование; зарегистрирован как weapon; canBeRepaired → associatedDiagramUuid и reliable < maxReliability | Проверены extends, состав общей схемы и указанные переопределения |
| [module/actor/witcherActor.js](../../../../../../../module/actor/witcherActor.js) | system.calcWeight; quantity | getTotalWeight:245–248 делегирует моделям; addItem/removeItem:259–283 преобразуют количество через Number | Карточка Actor дополнена обратной ссылкой |
| [module/item/witcherItem.js](../../../../../../../module/item/witcherItem.js) | system; возможности разных моделей | Сам документ не определяет общую схему; isConsumable читает отдельное поле, отсутствующее здесь | 72–77; карточка Item |
| [templates/partials/effect-part.hbs](../../../../../../../templates/partials/effect-part.hbs) | canHaveTemporaryItemImprovement | Строка 7 скрывает создание секции улучшения при false; это не запрет получить перенесённый эффект | Выражение unless и контекст document |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-weapons.hbs](../../../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-weapons.hbs) | canBeRepaired | Строка 36 показывает действие ремонта при truthy | Потребитель переопределения WeaponData |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-armors.hbs](../../../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-armors.hbs) | canBeRepaired | Строка 39 — аналогично для ArmorData | Потребитель переопределения ArmorData |
| [module/actor/sheets/mixins/itemMixin.js](../../../../../../../module/actor/sheets/mixins/itemMixin.js) | isCarried, поля item.system | _onItemCarried:112–118 переключает флаг через update; _onItemInlineEdit передаёт поле из dataset | Обработчики прочитаны точечно |
| [module/item/sheets/WitcherContainerSheet.js](../../../../../../../module/item/sheets/WitcherContainerSheet.js) | isStored | Помещение/извлечение:36/52 записывают true/false | Сверены обращения |
| [module/actor/sheets/WitcherActorSheet.js](../../../../../../../module/actor/sheets/WitcherActorSheet.js) | quantity; cost | Array.prototype.sum:18–24 читает Number(system[prop]); cost:26 и далее перемножает количество и цену | Это потребитель полей, не метод CommonItemData |
| [templates/sheets/item/race-sheet.hbs](../../../../../../../templates/sheets/item/race-sheet.hbs) | sourcebook | Поле формы system.sourcebook; 17 | Проверена строковая связь |
| [templates/sheets/item/weapon-sheet.hbs](../../../../../../../templates/sheets/item/weapon-sheet.hbs) | description | Textarea system.description; 5 | Проверена строковая связь |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-valuables.hbs](../../../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-valuables.hbs) | isCarried, weight, cost, description | Переключение и отображение полей; 24–56 | Проверен пример общего представления |

Поиск наследников охватывал все `module/data/item/*.js` и зарегистрированные модели расследований. [CriticalWoundData](../../../../../../../module/data/item/criticalWoundData.js), [HomelandData](../../../../../../../module/data/item/homelandData.js), [SkillItemData](../../../../../../../module/data/item/skillItemData.js), [ClueData](../../../../../../../module/data/investigation/clueData.js), [ObstacleData](../../../../../../../module/data/investigation/obstacleData.js) прямо наследуют TypeDataModel, а не CommonItemData. Среди 22 зарегистрированных типов Item — base, 16 наследников и эти пять отдельных моделей. Наличие одинаково названного поля/геттера у отдельных моделей не делает их наследниками.

У WeaponData/ArmorData canBeRepaired может вернуть пустую строку associatedDiagramUuid, а не строго false; UI использует truthiness. `canHaveTemporaryItemImprovement` не обозначает возможность оружия принять улучшение: оружие наследует false, но [module/actor/mixins/temporaryEffectMixin.js](../../../../../../../module/actor/mixins/temporaryEffectMixin.js) выбирает его как получателя. Флаг относится к созданию исходного эффекта в проверенном шаблоне. Другие ограничения этого процесса рассматриваются отдельно.

## Данные и изменения состояния

Файл создаёт определения полей и вычисляет значение массы в памяти. update/create/delete отсутствуют. Name, img, id/uuid, effects принадлежат документу Foundry; consumable, attackOptions, alchemyComponents, associatedItemUuid, equipped определяются специализированными моделями. CommonItemData не содержит enrichedText: [module/item/sheets/WitcherItemSheet.js](../../../../../../../module/item/sheets/WitcherItemSheet.js) обращается к нему условно через system; реализации находятся у расы, профессии и отдельной модели травмы.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Полнота | nl -ba; extends/super.defineSchema и регистрация | 29 строк; 8 полей, defineSchema, calcWeight, два getter; 16 прямых наследников | Наследники не получили собственных карточек в этой порции |
| Настоящая схема | node --input-type=module; оригинальная CommonItemData и поля Foundry | Все типы/initial совпали с таблицей; quantity остаётся строкой | Нет создания Item в БД |
| Масса | Шесть входов: 3×2; hidden; stored; !carried; 1d6; -2 | 6, 6, 0, 0, NaN, -4; Container 2×3+7=13 | Не запускалась подготовка содержимого контейнера |
| Возможности | Реальные CommonItemData/AlchemicalData/ValuableData; статические переопределения остальных | false/false у общей модели; true у двух проверенных наследников | Полный UI, ремонт и эффекты не проверены |

## Непроверенные участки и открытые вопросы

Специализированные модели, контейнеры, листы и их обработчики не разобраны целиком. Сборка всех документов Foundry, HTTP/UI, валидация обновлений и игровые данные не запускались. Политика строковых/отрицательных количеств и правила массы не утверждались. Область поиска прямых потребителей — module и templates; динамические макросы миров и модули вне системы не исследованы.

## Связанные проблемы

Отдельная проблема в CommonItemData не зарегистрирована. Проблемы действий Item и передачи улучшений описаны в [карточке WitcherItem](../../item/witcherItem.js.md); базовые признаки не следует трактовать как их причину.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.008 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.

## Уточнение TASK-0003.011

2026-09-10, `07237960627bf7debc2b4283aa55d1a8c5d1bb8b`; содержимое исходника совпадает с предыдущим срезом.

Поля общей модели сверены с [шапкой десяти форм](../../../templates/partials/item-header.hbs.md). quantity остаётся StringField несмотря на data-dtype=Number в input, а weight/cost — NumberField. В отличие от них, system.clickableImage отсутствует в схеме: настоящие ValuableData/ArmorData/WeaponData/MutagenData при входном true не содержат его в подготовленных данных и toObject. Весь путь настройки разобран в [issue-00063](../../../../../../issues/potential/issue-00063.md). Это проверка моделей в Node, не запись мировых Item.

[TASK-0003.011 — сценарии и сверка](../../../../review-log.md#task-0003011).

## Уточнение TASK-0003.012

2026-09-10, `d20d821e3a8a0a989ec503b0e97413a5a1431ad9`; исходник не изменён. У общих боевых моделей нет наследования от CommonItemData. WeaponData/SpellData/ArmorData наследуют CommonItemData и включают [DamageProperties](../../../../../../../module/data/item/templates/combat/damagePropertiesData.js), [DefenseProperties](../../../../../../../module/data/item/templates/combat/defensePropertiesData.js), [ResistanceData](../../../../../../../module/data/item/templates/armor/resistanceData.js), [SpData](../../../../../../../module/data/item/templates/armor/spData.js) через EmbeddedDataField. ArmorData явно вызывает две фазы Resistance/SP; CommonItemData их сам не обходит. Реальные parent этих вложенных полей указывают на system-модель владельца.

Результат и границы — [сверка TASK-0003.012](../../../../review-log.md#task-0003012).

## Уточнение TASK-0003.015

2026-09-10, `7edb814aa870da75c7ad7633536e899a8d07e205`; исходник неизменен. [Перекрёстная сверка](../../../../review-log.md#task-0003015).

Полностью разобраны три наследника: [module/data/item/alchemicalData.js](../../../../../../../module/data/item/alchemicalData.js), [module/data/item/mutagenData.js](../../../../../../../module/data/item/mutagenData.js), [module/data/item/valuableData.js](../../../../../../../module/data/item/valuableData.js). Все получают восемь общих полей и включают ещё два из [module/data/item/templates/consumableData.js](../../../../../../../module/data/item/templates/consumableData.js). AlchemicalData и ValuableData переопределяют canHaveTemporaryItemImprovement=true; MutagenData сохраняет false. quantity остаётся StringField: consume не изменяет его, а Actor.removeItem вычитает количество и вызывает update либо delete.

## Уточнение TASK-0003.016

2026-09-10, `53f74994011383cb544cabac96285430f00cb38a`; исходник неизменен. [Перекрёстная сверка](../../../../review-log.md#task-0003016).

Полностью разобраны [module/data/item/componentData.js](../../../../../../../module/data/item/componentData.js) и [module/data/item/diagramData.js](../../../../../../../module/data/item/diagramData.js). Первая добавляет 6 строк к 8 общим полям (14 всего), вторая — 12 полей (20 всего). description в обоих случаях расположен в system, что сопоставлено с неверными верхними путями [templates/partials/associated-diagram.hbs](../../../../../../../templates/partials/associated-diagram.hbs) и [templates/partials/associated-item.hbs](../../../../../../../templates/partials/associated-item.hbs). Оба типа наследуют canBeRepaired=false и canHaveTemporaryItemImprovement=false.

## Уточнение TASK-0003.018

2026-09-10, `rusbar-main`, `29319a7a7e1dfc0663edbc15166f3b6a19682a2f`. [RaceData](../../../../../../../module/data/item/raceData.js) расширяет 8 общих полей четырьмя SchemaField особенностей и одной SchemaField социального положения, переопределяя description в HTMLField (13 полей). calcWeight и общие getters наследуются. [HomelandData](../../../../../../../module/data/item/homelandData.js) не наследует этот класс: в настоящей модели quantity, переданное во входе, отсутствует и в подготовленных данных, и в toObject(). name/img/effects принадлежат документу Item, а не этой общей схеме.

[Перекрёстная сверка](../../../../review-log.md#task-0003018). Исходники не изменены; это уточнение проверенных связей, а не повторный полный разбор файла.

## Уточнение TASK-0003.019

2026-09-10, `rusbar-main`, `c26eb64dd54cc434087f54c3c6b678b6092b15a2`. [ProfessionData](../../../../../../../module/data/item/professionData.js) сохраняет 8 общих полей без переопределения description, добавляя notes/definingSkill/3 пути/professionSkills: всего 14. В форме редактируется sourcebook; навыки и заметки используют свои HTMLField. Общие getters/calcWeight наследуются, числовые бонусы от общего описания не создаются.

[Перекрёстная сверка](../../../../review-log.md#task-0003019). Исходники не изменены; уточнение касается проверенных связей, не повторного полного разбора файла.

## Уточнение TASK-0003.021

Проверено 2026-09-11 на `a29234e7c42ef5f9d8095c2b5470e5e3c95824cc`; исходник не менялся.

SpellData, HexData и RitualData наследуют общие 8 полей. Только SpellData переопределяет canHaveTemporaryItemImprovement=true; собственных полей clickableImage и механики ActiveEffect общая модель по-прежнему не даёт.

Сверенные карточки: [module/data/item/spellData.js](spellData.js.md), [module/data/item/hexData.js](hexData.js.md), [module/data/item/ritualData.js](ritualData.js.md), [templates/partials/spell-header.hbs](../../../templates/partials/spell-header.hbs.md).

[Результаты и пределы сверки](../../../../review-log.md#task-0003021).
