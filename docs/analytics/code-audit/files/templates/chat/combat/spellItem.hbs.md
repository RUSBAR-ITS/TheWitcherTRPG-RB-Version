# templates/chat/combat/spellItem.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/chat/combat/spellItem.hbs](../../../../../../../templates/chat/combat/spellItem.hbs) |
| Тип файла | Handlebars |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `c598d74e34f4be51535de78b38f0601c286c5407` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.039](../../../../../../tasks/task-0003.039.md), 6 файлов, 870 логических строк |
| Запись перекрёстной сверки | [TASK-0003.039](../../../../review-log.md#task-0003039) |

## Назначение файла

HTML flavor результата сотворения: описание магического Item, показ стоимости/источника/длительности/компонентов и кнопки урона, щита, лечения, ссылки статусов.

## Условия использования

castSpell:227–234 передаёт spellItem, templateInfo, damage. HBS рендерится до extendedRoll, поэтому ни успех, ни fumble ему ещё не известны. Готовый HTML включается в ChatMessageData(type=attack).

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| Заголовок и свойства Item | 1–41 | Картинка, имя, STA и магическое описание | Поля spellItem.system/templateInfo | if по truthy, обычное экранирование |
| button.damage / button.shield / button.heal | 43–55 | Последующие действия пользователя | Условие только causeDamages/createsShield/doesHeal | data-img/name; для shield/heal также значение и Actor UUID |
| templateInfo.selfEffects / a.apply-status | 57–71 | Описание и ручное применение статуса | each по подготовленному массиву | data-status и ../damage.duration; имя/иконка из CONFIG |

## Основные функции и методы

Собственных JS-функций нет. if/each/unless/eq управляют разметкой, localize — подписями. durationText вставляется тройными скобками, чтобы показать anchor броска; остальные поля экранируются.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| castSpellMixin.castSpell | [module/actor/mixins/castSpellMixin.js](../../../../../../../module/actor/mixins/castSpellMixin.js) | Единственный прямой producer | spellItem/templateInfo/damage; renderTemplate227 | Шаблон не получает roll.options и не блокирует кнопки на fumble |
| SpellData/HexData/RitualData | [module/data/item/spellData.js](../../../../../../../module/data/item/spellData.js); [module/data/item/hexData.js](../../../../../../../module/data/item/hexData.js); [module/data/item/ritualData.js](../../../../../../../module/data/item/ritualData.js) | Содержимое Item | effect,range,duration,defence,preparationTime,difficultyCheck,ritualComponents,alternateRitualComponents,liftRequirement и флаги | RitualData готовит объекты item/quantity/img из UUID |
| onShield / onHeal / chatMessageListeners | [module/scripts/chat.js](../../../../../../../module/scripts/chat.js) | Селекторы кнопок | shield→data-shield в Actor.update; heal→parseInt/data-heal и выбор цели | Нет вычисления формулы и проверки результата исходного броска |
| onDamage / attackChatMessageListeners | [module/scripts/combat/combat.js](../../../../../../../module/scripts/combat/combat.js) | button.damage | Item по message.system.attack.itemUuid → rollDamage | UUID даёт getItemAttack; data-img/name не заменяют UUID |
| chatMessageListeners / onApplyStatus | [module/scripts/statusEffects/applyStatusEffect.js](../../../../../../../module/scripts/statusEffects/applyStatusEffect.js) | a.apply-status | Берёт status,duration, getCurrentCharacter; вызывает общий helper | Ручная цель определяется при клике, не жёстко spell Actor |
| getInteractActor / getCurrentCharacter | [module/scripts/helper.js](../../../../../../../module/scripts/helper.js) | Внешние действия чата | Боевой контекст/ручной статус | Автоматическое применение не зависит от ссылки |
| ChatMessageData / AttackMessageData / damageData | [module/chatMessage/chatMessageData.js](../../../../../../../module/chatMessage/chatMessageData.js); [module/data/chatMessage/attackMessageData.js](../../../../../../../module/data/chatMessage/attackMessageData.js); [module/data/chatMessage/templates/damageData.js](../../../../../../../module/data/chatMessage/templates/damageData.js) | Сообщение/схема | HTML хранится flavor; shield/heal/duration нет в damageData | Формулы этих кнопок остаются в data-атрибутах |
| CONFIG.WITCHER.statusEffects / eq | [module/setup/config.js](../../../../../../../module/setup/config.js); [module/setup/handlebars.js](../../../../../../../module/setup/handlebars.js) | Данные статуса и helper | selfEffect.effect.name/statusEffect и statusEffect.img/name | Неизвестный ID не гарантирует картинку/перевод |
| Локализация | [lang/en.json](../../../../../../../lang/en.json); [lang/ru.json](../../../../../../../lang/ru.json) | localize | WITCHER.Spell.*, WITCHER.DC, WITCHER.Item.Effect/table.Damage | Динамический source Water не найден; literal ключи этого HBS доступны |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/actor/mixins/castSpellMixin.js](../../../../../../../module/actor/mixins/castSpellMixin.js) | spellItem.hbs | renderTemplate227→ChatMessageData238 | Подготовка flavor |
| [module/scripts/chat.js](../../../../../../../module/scripts/chat.js) | shield/heal buttons | chatMessageListeners | Клик читает data-атрибуты |
| [module/scripts/combat/combat.js](../../../../../../../module/scripts/combat/combat.js) | damage button | attackChatMessageListeners | Берёт typed attack.itemUuid из сообщения |
| [module/scripts/statusEffects/applyStatusEffect.js](../../../../../../../module/scripts/statusEffects/applyStatusEffect.js) | apply-status link | chatMessageListeners | Ручное действие |

Область поиска: module/ и templates/ текущего checkout; прямые импорты и места вызова сверены отдельно от динамических обращений. Типы и листы сверены с system.json, module/setup/registerDataModels.js и module/setup/registerSheets.js. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Поля: spellItem.img/name; templateInfo.staCostDisplay/spellSource/durationText/actor.uuid/selfEffects; spellItem.system.effect/range/duration/defence/preparationTime/difficultyCheck/ritualComponents/alternateRitualComponents/liftRequirement/causeDamages/createsShield/doesHeal. Для компонентов главный массив даёт quantity×item.name, альтернативный вставляется целиком и строкифицируется как [object Object].

Щит/лечение используют damage.shield/heal; onShield получает строку и обновляет щит исходного Actor, без Roll. onHeal parseInt, затем первая цель → первый контролируемый token → game.user.character; при отсутствии цели ничего не делает. Положительное лечение ограничивает HP.max, повторное нажатие не запрещено; исходный caster нужен для speaker/текста. Если формула '1d6', лечение становится 1; формула щита '2d6' не проходит числовую модель. Для numeric '7' щит обновляется строковым значением с последующим coercion поля.

selfEffects здесь ожидает массив {effect,statusEffect}; в актуальном castSpell словарь не проходит length и блок не получает контекст. Legacy-массив показывает только записи со statusEffect. Применение автоматически после броска идёт независимо от наличия этих ссылок. damage.duration используется ссылкой на статус, но не типизированным damageData. Кнопки урона/щита/лечения не проверяют fumble, так как создаются до броска.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Данные и кнопки | Группы 13/15–21/24 | attack UUID сохраняется; фиксированные/переменные значения щита, отказ variable heal; реальные обработчики кнопок | DOM/addEventListener и запись заменены |
| Эффекты и компоненты | Группы 20–23/29 | Словарь отсутствует в HTML, legacy-массив выводится; альтернативы object Object | Активные эффекты не создавались в Foundry |
| Локализация/типизированная граница | Группы 17/30 | shield/heal отсутствуют в damageData; source Water остаётся ключом | Реальная модель, без ChatMessage persistence |

## Непроверенные участки и открытые вопросы

Файлы порции прочитаны целиком. Проверка: Foundry 14.367.0, Node 24.16.0, реальные модели/методы, Roll/extendedRoll, Handlebars 4.7.9, expandObject и core Localization с fallback. Диалог, Application/DOM, вывод Roll.toAnchor, запись Actor/Item/ChatMessage, UUID resolver, создание/clone ActiveEffect, canvas и query заменены фасадами. Реальные браузер, HTTP, БД, компедиумы, сетевые клиенты и жизненный цикл эффекта не запускались. Текстовые формулы проверены как поведение кода, без выбора правил книг.

## Связанные проблемы

[issue-00133](../../../../../../issues/potential/issue-00133.md), [issue-00134](../../../../../../issues/potential/issue-00134.md), [issue-00135](../../../../../../issues/potential/issue-00135.md), [issue-00137](../../../../../../issues/potential/issue-00137.md), [issue-00249](../../../../../../issues/potential/issue-00249.md), [issue-00253](../../../../../../issues/potential/issue-00253.md). Полная карточка scripts/chat.js остаётся .040; здесь разобраны только потребители трёх типов элементов результата.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `c598d74e34f4be51535de78b38f0601c286c5407`; полный файл | Первая карточка; [сверка порции](../../../../review-log.md#task-0003039) |
