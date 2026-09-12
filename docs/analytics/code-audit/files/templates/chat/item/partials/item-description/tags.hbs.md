# templates/chat/item/partials/item-description/tags.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/chat/item/partials/item-description/tags.hbs](../../../../../../../../../templates/chat/item/partials/item-description/tags.hbs) |
| Тип файла | Handlebars |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-12 |
| Ветка и коммит | rusbar-main, ee24c2605f4db98fad1ff6db024d2b0c26883670 |
| Изменения относительно коммита | Нет; совпадает со срезом TASK-0001 15da5b225535e34af4e132c701b5353ef4eb667f |
| Задача и порция | [TASK-0003.048](../../../../../../../../tasks/task-0003.048.md), 16 файлов / 920 логических строк; данный файл — 332 |
| Запись перекрёстной сверки | [TASK-0003.048](../../../../../../review-log.md#task-0003048) |

## Назначение файла

Все группы тегов кратких свойств Item: от доступности и массы до сопротивлений, сложности рецепта и точности оружия.

## Условия использования

Предзагружается preloadHandlebarsTemplates и включается корневым item-description.hbs без смены контекста. Самостоятельного вызова renderTemplate для этой части в module/ не найдено.

Девять независимых блоков if покрывают 13 типов. Корневой контекст остаётся {item,type,config}; each effects вводит собственный block-param effects. Теги преимущественно проверяют truthiness: Number 0/false/пустая строка скрываются, отрицательное число truthy; StringField превращает числовой 0 в строку '0', которая видима. Исключения — gt для weapon.accuracy и effect.percentage, а также безусловные теги контейнера/ценности/рецепта. Это не фильтрация данных модели. Внутри item-tags нет JS, кнопок броска или автоматического применения статуса. Значения type/source/level/statusEffect преимущественно печатаются как сохранённые строки; lookup+localize используется только для перечисленных справочников.

## Введённые сущности и действия с ними

| Сущность | Определение / область | Действия |
| --- | --- | --- |
| HTML-фрагмент | Весь файл | Условия, текст, атрибуты и CSS-классы; нет сохранения документов |
| type | Внешний контекст Item.type | Выбор поддержанных типов |
| Пути чтения | Все буквальные обращения ниже | Готовые поля и справочники, без обновления |

Буквальные пути чтения: `config.Availability`, `config.Concealment`, `config.craftingLevels`, `config.weapon.hands`, `effects.percentage`, `effects.statusEffect`, `item.system.accuracy`, `item.system.alchemyDC`, `item.system.avail`, `item.system.bludgeoning`, `item.system.conceal`, `item.system.control`, `item.system.cost`, `item.system.craftingDC`, `item.system.craftingTime`, `item.system.danger`, `item.system.defence`, `item.system.dex`, `item.system.difficultyCheck`, `item.system.duration`, `item.system.effects`, `item.system.encumb`, `item.system.forage`, `item.system.hands`, `item.system.hp`, `item.system.investment`, `item.system.isAmmo`, `item.system.isFormulae`, `item.system.level`, `item.system.piercing`, `item.system.preparationTime`, `item.system.quantityObtainable`, `item.system.range`, `item.system.rarity`, `item.system.slashing`, `item.system.source`, `item.system.speed`, `item.system.time`, `item.system.toxicity`, `item.system.type`, `item.system.type.text`, `item.system.weight`.

| Строки | Типы | Полный набор условий/значений | Контракт |
| --- | --- | --- | --- |
| 1–44 | alchemical / mutagen | type безусловно; alchemyDC, avail, time, weight, cost, toxicity по if | avail → config.Availability/localize; прочие значения обычным текстом. Поля группы существуют не в обеих моделях. |
| 45–84 | armor | type; slashing/piercing/bludgeoning; encumb; weight — if | Три старых плоских сопротивления не читают system.resistance.*. Тип брони печатается без перевода. |
| 85–124 | component | type, rarity, quantityObtainable, forage, weight, cost — if | Строки '0' проходят условие; числовой weight/cost=0 нет. |
| 125–144 | container / valuable | avail/conceal/weight/cost безусловно | Первые два через config.Availability/Concealment; в ContainerData их нет, содержимое тега пустое. |
| 145–179 | diagrams | isFormulae выбирает alchemyDC или craftingDC; type/level/craftingTime/cost/investment безусловно | level → config.craftingLevels/localize; type — сырая строка. 0 DC/cost/investment отображаются. |
| 180–209 | enhancement | type/weight/cost по if; each effects при percentage>0 | statusEffect сырой ID, затем percentage%; name и varEffect не выводятся. |
| 210–237 | mount | dex/control/speed/hp — if | Первые три StringField, HP NumberField. |
| 238–289 | spell / hex / ritual | source, level, danger, range, preparationTime, difficultyCheck, duration, defence — if | Общая ветвь для разного состава схем. difficultyCheck строковый '0' видим. |
| 290–332 | weapon | type.text/range/conceal/weight по if; accuracy>0; isAmmo либо hands | hands → config.weapon.hands/localize; conceal → config.Concealment. Отрицательная accuracy не выводится. |

## Основные функции и методы

Собственных функций нет. Полная таблица ветвей выше описывает условия каждой группы. Три сопротивления брони читаются по item.system.slashing/piercing/bludgeoning, хотя современная модель хранит resistance.*: issue-00306. Точность показывается только при >0 с литералом '+', поэтому штраф исчезает из описания, хотя участвует в weaponAttack: issue-00307. Безусловные availability/conceal контейнера дают пустое значение lookup, не новый справочник. Tooltip WITCHER.Weapon.Availability отсутствует в en/ru — дополнение прежней issue-00178.

Внешние if/each/lookup — Handlebars 4.7.9; eq/or/gt/capitalize — registerHandelbarHelpers системы, localize/concat — Foundry client/applications/handlebars.mjs. Набор реально вызванных helpers определяется выражениями файла, а не всем доступным реестром. if без includeZero не показывает Number 0; стандартное {{}} экранирует текст и атрибуты.

## Используемые сущности и зависимости

| Источник | Используемая сущность | Связь и цель | Основание |
| --- | --- | --- | --- |
| [templates/chat/item/item-description.hbs](../../../../../../../../../templates/chat/item/item-description.hbs) | item/type/config | Единственное прямое включение partial, исходный контекст без hash. | Определение и место обращения сверены |
| [module/setup/handlebars.js](../../../../../../../../../module/setup/handlebars.js) | preloadHandlebarsTemplates/registerHandelbarHelpers | Предзагрузка пяти partial, системные eq/or/gt/capitalize; корень рендерится по запросу. | Определение и место обращения сверены |
| [styles/chat.css](../../../../../../../../../styles/chat.css) | chat-* и list-item-description | Общие размеры и несовпадение непосредственных потомков section. | Определение и место обращения сверены |
| [styles/tab-inventory.css](../../../../../../../../../styles/tab-inventory.css) | item-tags/item-tag, stored-item-* | Общие стили тегов и материалов. | Определение и место обращения сверены |
| [module/data/item/alchemicalData.js](../../../../../../../../../module/data/item/alchemicalData.js) | AlchemicalData | type/avail/time/toxicity; alchemyDC отсутствует. | Определение и место обращения сверены |
| [module/data/item/mutagenData.js](../../../../../../../../../module/data/item/mutagenData.js) | MutagenData | type/alchemyDC; avail/time/toxicity отсутствуют. | Определение и место обращения сверены |
| [module/data/item/armorData.js](../../../../../../../../../module/data/item/armorData.js) | ArmorData | type/encumb и nested resistance; плоские сопротивления устарели. | Определение и место обращения сверены |
| [module/data/item/componentData.js](../../../../../../../../../module/data/item/componentData.js) | ComponentData | type/rarity/quantityObtainable/forage. | Определение и место обращения сверены |
| [module/data/item/containerData.js](../../../../../../../../../module/data/item/containerData.js) | ContainerData | Общие weight/cost есть, avail/conceal не объявлены. | Определение и место обращения сверены |
| [module/data/item/valuableData.js](../../../../../../../../../module/data/item/valuableData.js) | ValuableData | avail/conceal и общие числовые поля. | Определение и место обращения сверены |
| [module/data/item/diagramData.js](../../../../../../../../../module/data/item/diagramData.js) | DiagramData | isFormulae, DC, type/level/craftingTime/investment. | Определение и место обращения сверены |
| [module/data/item/enhancementData.js](../../../../../../../../../module/data/item/enhancementData.js) | EnhancementData.effects | TypedObjectField записей itemEffect, не ActiveEffect.changes. | Определение и место обращения сверены |
| [module/data/item/templates/itemEffectData.js](../../../../../../../../../module/data/item/templates/itemEffectData.js) | itemEffect | statusEffect/percentage/name/varEffect; последние два не выводятся этим each. | Определение и место обращения сверены |
| [module/data/item/mountData.js](../../../../../../../../../module/data/item/mountData.js) | MountData | dex/control/speed — строки, hp — число. | Определение и место обращения сверены |
| [module/data/item/spellData.js](../../../../../../../../../module/data/item/spellData.js) | SpellData | source/level/range/duration/defence. | Определение и место обращения сверены |
| [module/data/item/hexData.js](../../../../../../../../../module/data/item/hexData.js) | HexData | danger. | Определение и место обращения сверены |
| [module/data/item/ritualData.js](../../../../../../../../../module/data/item/ritualData.js) | RitualData | level/range/preparationTime/difficultyCheck/duration/defence. | Определение и место обращения сверены |
| [module/data/item/weaponData.js](../../../../../../../../../module/data/item/weaponData.js) | WeaponData | type.text/range/accuracy/isAmmo/hands/conceal. | Определение и место обращения сверены |
| [module/data/item/templates/weaponTypeData.js](../../../../../../../../../module/data/item/templates/weaponTypeData.js) | weaponType | Вложенное text; флаги урона в этой ветви не выводятся. | Определение и место обращения сверены |
| [module/data/item/commonItemData.js](../../../../../../../../../module/data/item/commonItemData.js) | weight/cost | Общие NumberField, значения 0. | Определение и место обращения сверены |
| [module/setup/config.js](../../../../../../../../../module/setup/config.js) | WITCHER.Availability/Concealment/craftingLevels/weapon.hands | Динамические ключи localize после lookup. | Определение и место обращения сверены |
| [module/setup/handlebars.js](../../../../../../../../../module/setup/handlebars.js) | eq/or/gt | Строгий выбор типов и фильтры >0. | Определение и место обращения сверены |

Локализация: [lang/ru.json](../../../../../../../../../lang/ru.json) и [lang/en.json](../../../../../../../../../lang/en.json); настоящий Localization 14.367.0 с expandObject и en fallback. Иконки Font Awesome и обрамление сообщения предоставляет клиент Foundry. Ресурсы assets и внешний клиент не получают карточек этого аудита.

## Известные потребители

| Потребитель | Использование | Условия / основание |
| --- | --- | --- |
| [templates/chat/item/item-description.hbs](../../../../../../../../../templates/chat/item/item-description.hbs) | partial-включение | Без hash/with, полный контекст item/type/config |
| [module/setup/handlebars.js](../../../../../../../../../module/setup/handlebars.js) | preloadHandlebarsTemplates | Загрузка и регистрация partial отдельно от фактического показа |

Область поиска — module/ и templates/ текущего checkout. Макросы миров, внешние модули и подменённые шаблоны не проверялись.

## Данные и изменения состояния

Шаблон создаёт HTML-строку, не модифицирует предмет или Actor. Producer передаёт подготовленную модель Item, а не результат сериализации. Имя и img принадлежат Document, system-поля — моделям системы. Сам HBS не обогащает HTML: markup экранируется. После создания стандартного сообщения ядро ChatMessage.renderHTML вызывает TextEditor.enrichHTML (client/documents/chat-message.mjs:414), поэтому сохранённый @UUID/inline roll нельзя объявлять навсегда простым текстом только по первому рендеру. Полный последующий enrichment в браузере здесь не исполнялся.

## Проверки и доказательства

| Что | Метод / источник | Результат | Предел |
| --- | --- | --- | --- |
| Полнота | 332 строк исходного HBS | Все ветви, пути чтения и helpers описаны | Соседние файлы проверены только по связи |
| Рендер/модель | Настоящие Handlebars, модели и helpers | Группы 01, 04, 06–09, 16: defaults всех моделей и заполненные допустимые значения. Положительный TypedObject effects даёт bleeding/35%, имя DescriptiveName не выводится; нулевой процент пропущен. Weapon accuracy -2/0/+2 → 0/0/1 тег точности. Настоящий Localization с expandObject и en fallback: 66 статических/динамических ключей всего комплекта, 65 доступны в ru, WITCHER.Weapon.Availability отсутствует и в en. Проверка не охватывает сторонние модули перевода. | UUID/Document/чат — фасады, запись отсутствует |
| Локализация/ресурсы | en/ru expandObject, настоящий Localization; локальные файлы | 66 ключей комплекта: 65 ru, 1 отсутствует en/ru; девять PNG существуют | Другие локали/HTTP не проверены |

## Непроверенные участки и открытые вопросы

Файл прочитан целиком. Проверки локальные: Foundry 14.367.0, Node 24.16.0, Handlebars 4.7.9, PostCSS 8.5.12. Модели, helpers, методы и HBS — реальные исходники; UUID resolver, Actor/DOM/ChatMessage и отдельные вспомогательные helpers представлены указанными в журнале фасадами. Не запускались мир, браузер, HTTP, БД, установка пакетов или сборка. Совпадение селектора и существование файла не доказывают конечный вид или доступ службы. Скрытие нуля и печать сырого строкового enum описаны без самостоятельного вывода о нарушении игровых правил.

## Связанные проблемы

[docs/issues/potential/issue-00178.md](../../../../../../../../issues/potential/issue-00178.md), [docs/issues/potential/issue-00306.md](../../../../../../../../issues/potential/issue-00306.md), [docs/issues/potential/issue-00307.md](../../../../../../../../issues/potential/issue-00307.md), [docs/issues/potential/issue-00310.md](../../../../../../../../issues/potential/issue-00310.md). Наблюдения остаются potential; подтверждения и исправления не выполнялись.

## История актуализации

| Дата | Версия и область | Результат |
| --- | --- | --- |
| 2026-09-12 | ee24c2605f4db98fad1ff6db024d2b0c26883670; полный файл | Первичная карточка; [перекрёстная сверка](../../../../../../review-log.md#task-0003048) |
