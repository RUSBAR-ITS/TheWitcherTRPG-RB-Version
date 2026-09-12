# module/scripts/helper.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/scripts/helper.js](../../../../../../module/scripts/helper.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `9f16a7ae4bc942df85a105fd37d9a3cb3ef99f4b` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.028](../../../../../tasks/task-0003.028.md), 5 файлов, 372 логических строк |
| Запись перекрёстной сверки | [TASK-0003.028](../../../review-log.md#task-0003028) |

## Назначение файла

Общие функции выбора Actor/токена/владельца, получения случайного целого числа, сборки части формулы и ввода пользовательского модификатора. Не является обработчиком эффектов или правил: используется несколькими независимыми процессами.

## Условия использования

Восемь named export функций; при импорте сохраняется const DialogV2=foundry.applications.api.DialogV2. Источники текущего Actor — canvas.tokens.controlled и game.user.character; список кандидатов — game.actors; получатель query определяется по game.users. UI и запросы в соседних файлах запускаются только при соответствующих вызовах.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| DialogV2 | Локальная const, 1 | Ссылка на API окна | Сохраняется при импорте | input для Actor, prompt для модификатора. |
| getCurrentCharacter / getCurrentToken | export, 3–9 | Текущий Actor/токен | Синхронные функции | Первый controlled; fallback на character/character.token. |
| getInteractActor / chooseFromAvailableActors | async export, 11–58 | Выбор Actor для действия | Список и диалог | Текущий → доступные owned/hasPlayerOwner → уведомление. |
| getActorOwner | export, 61–71 | Доступный получатель query | Синхронная функция | Первый активный не-GM с OWNER либо activeGM. |
| getRandomInt | export, 73–75 | Случайное целое 1..max при положительном целом max | Синхронная функция | Math.random, отдельно от Foundry Roll. |
| addPart / getCustomModifier | export, 77–106 | Часть формулы и окно её ввода | Синхронная / async функции | Настройка детализации, локализация, пользовательская строка. |
| filters / input HTML / ok.callback | 32–57, 65–68, 99–101 | Выбор кандидатов/владельца и чтение формы | Локальные closures | Кандидаты фильтруются дважды; callback возвращает строковое value customModifiers. |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| getCurrentCharacter() | Доступны canvas.tokens.controlled и game.user | Первый token.actor либо game.user.character | Оператор ??, без проверки ownership | Пустой controlled и нет character → null/undefined; недоступный canvas.tokens даёт TypeError. |
| getCurrentToken() | Те же коллекции; для fallback нужен character | Первый controlled Token либо character.token | Не ищет токены по сцене | Без character обращение к .token бросает TypeError; world Actor.token может отсутствовать. Внешних вызовов в module/ не найдено. |
| getInteractActor() | Текущий Actor либо game.actors | Promise<Actor\|undefined> | Promise.resolve(getCurrentCharacter()) → при nullish chooseFromAvailableActors → при отсутствии UI error | При 0 кандидатов уведомляет, но возвращает undefined. TypeError от отмены input не переводится в обычный выход. |
| chooseFromAvailableActors() | game.actors optional; owned AND hasPlayerOwner | Promise<Actor\|undefined> | 0 → return; 1 → экземпляр; >1 → HTML select name actor → DialogV2.input → game.actors.get(values.actor) | Нет guard values: отмена input даёт null и TypeError. ID и имя кандидата вставляются в HTML напрямую. При удалённом ID возвращается undefined. |
| getActorOwner(actor) | Actor с hasPlayerOwner/testUserPermission; users | User либо activeGM, который может быть null | Фильтрует active, !isGM, OWNER при hasPlayerOwner; иначе activeGM | Не выбирает неактивного владельца, не проверяет текущего пользователя отдельно; actor отсутствует → TypeError. Не запускает query сам. |
| getRandomInt(max) | Положительный целый max для диапазона 1..max | Math.floor(Math.random()*max)+1 | Один вызов Math.random | Без валидации: max=0 даёт 1, undefined даёт NaN. Реальные потребители передают 2, 6, 10, 100. |
| addPart(value,details,hideZero=false) | Число или строка, ключ локализации, флаг скрытия | Строка | Всегда читает displayRollsDetails; если value==0 && hideZero → ''; иначе '+'+value, при детализации '[localized details]' | Приведение при ==0; не проверяет формулу/число. -2 даёт '+-2', что поддерживается парсером Foundry. |
| getCustomModifier(title) / ok.callback(event,button,dialog) | Заголовок; form.elements.customModifiers | Promise<string> | DialogV2.prompt с rejectClose=true; callback читает строковое .value; addPart(value,'WITCHER.Settings.Custom',true) | 0/'0' скрывается; отрицательный ввод сохраняет знак; отмена prompt отклоняет Promise. event/dialog не используются. |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| DialogV2.input / prompt / wait | Foundry 14.367.0: client/applications/api/dialog.mjs:369–427 | Глобальная ссылка | 1, 54, 92 | input по умолчанию rejectClose=false и закрытие возвращает null; getCustomModifier явно задаёт true. |
| canvas.tokens.controlled / game.user.character / game.actors / game.users | Foundry canvas, User, Actor/Users collections | Чтение документов и коллекций | 3–71 | Первый controlled/назначенный Actor; isOwner, hasPlayerOwner, testUserPermission('OWNER'), users.activeGM. |
| displayRollsDetails | [module/setup/settings.js](../../../../../../module/setup/settings.js) | Зарегистрированная настройка | addPart:78 | registerSettings:46–53: world Boolean, default=false; вызов до проверки hideZero. |
| WITCHER.Context.SelectActor / Dialog.customModifier / Button.Continue / Settings.Custom | [lang/en.json](../../../../../../lang/en.json); [lang/ru.json](../../../../../../lang/ru.json) | Локализация | Уведомление и диалог | В en все ключи присутствуют; в ru отсутствует WITCHER.Dialog.customModifier (issue-00186). title передаётся вызывающим кодом уже подготовленной строкой. |
| Math.random / Math.floor / Promise | JavaScript standard API | Случайное число и управление ожиданием | getRandomInt/getInteractActor | Не использует CONFIG.Dice или Foundry Roll; в проверке источник случайности заменён. |
| query — downstream получателя | [module/setup/queries.js](../../../../../../module/setup/queries.js); [module/scripts/statusEffects/applyStatusEffect.js](../../../../../../module/scripts/statusEffects/applyStatusEffect.js); [module/scripts/temporaryEffects/applyActiveEffect.js](../../../../../../module/scripts/temporaryEffects/applyActiveEffect.js) | Обратный процесс, без импорта в helper | getActorOwner → выбранный User.query | helper только возвращает User; выполнение/подтверждение операции реализовано отдельно. |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/actor/witcherActor.js](../../../../../../module/actor/witcherActor.js) | getRandomInt | getLocationObject: randomHuman/randomMonster, max=10 | import:1; вызовы:308/346 |
| [module/actor/mixins/defenseMixin.js](../../../../../../module/actor/mixins/defenseMixin.js) | getActorOwner / getRandomInt | Получатель запроса addAdrenaline; случайная сторона max=2 | 5, 213, 381/386 |
| [module/actor/mixins/damageMixin.js](../../../../../../module/actor/mixins/damageMixin.js) | getRandomInt | Выбор меньшего/большего последствия травмы: getRandomInt(6)+critEffectModifier при отсутствии crit.location.critEffect | 1, 326 |
| [module/item/mixins/damageUtilMixin.js](../../../../../../module/item/mixins/damageUtilMixin.js) | getRandomInt | Вероятность эффекта, max=100 | 3, 61 |
| [module/scripts/statusEffects/applyStatusEffect.js](../../../../../../module/scripts/statusEffects/applyStatusEffect.js) | getCurrentCharacter / getActorOwner | onApplyStatus берёт текущего Actor без диалога; не-owner перенаправляет query | 1; 25–27, 49–52 |
| [module/scripts/temporaryEffects/applyActiveEffect.js](../../../../../../module/scripts/temporaryEffects/applyActiveEffect.js) | getActorOwner | Делегирование ActiveEffect и temporary item improvements | 41, 72 |
| [module/actor/mixins/professionMixin.js](../../../../../../module/actor/mixins/professionMixin.js) | getActorOwner / getCustomModifier | Временные HP цели через query; пользовательский модификатор навыка | 4, 315, 367 |
| [module/actor/mixins/skillMixin.js](../../../../../../module/actor/mixins/skillMixin.js) | getCustomModifier | Обычный/пользовательский навык | 2, 76, 167 |
| [module/actor/sheets/mixins/statMixin.js](../../../../../../module/actor/sheets/mixins/statMixin.js) | getCustomModifier | Спасбросок характеристики; части объединяются через '+' | 4, 24–35; парсер принимает двойной '+' |
| [module/actor/mixins/verbalCombatMixin.js](../../../../../../module/actor/mixins/verbalCombatMixin.js) | addPart | База и произвольный модификатор словесной атаки | 61/62/67; truthy строка 'hide' используется как hideZero |
| [module/scripts/investigation/rollClue.js](../../../../../../module/scripts/investigation/rollClue.js) | getInteractActor | Actor для улики; guard отсутствует | 1, 6–8, 43; issue-00149 |
| [module/scripts/chat.js](../../../../../../module/scripts/chat.js) | getInteractActor | onRepairRequest; до processRequest проверяет actor | 51–61; другие owner/item guards — отдельный вопрос |
| [module/scripts/combat/combat.js](../../../../../../module/scripts/combat/combat.js) | getInteractActor | stunSave/критический урон/травма без guard; executeDefense с guard | 29/35, 47–55, 75/83/91 |
| [module/scripts/combat/applyDamage.js](../../../../../../module/scripts/combat/applyDamage.js) | getInteractActor | Меню обычного/несмертельного урона; зависимый диалог читает actor.type | 15/27, createApplyDamageDialog:64 |
| [module/scripts/verbalCombat/verbalCombat.js](../../../../../../module/scripts/verbalCombat/verbalCombat.js) | getInteractActor | Меню словесного урона; applyVerbalCombatDamage читает targetActor.system | 23, 52–55; DOM-путь разобран в дополнении .046 |
| [module/scripts/verbalCombat/verbalCombatDefense.js](../../../../../../module/scripts/verbalCombat/verbalCombatDefense.js) | getInteractActor | Меню словесной защиты; executeDefense имеет if(!actor)return | 13, 19–20; остальные ошибки DOM не переоцениваются в этой порции |

Область поиска: module/ и templates/ текущего checkout; прямые импорты и места вызова сверены отдельно от динамических обращений. Типы сообщений проверены по system.json и module/setup/registerDataModels.js. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Функции выбора сами не записывают Actor/User и не применяют эффектов. getInteractActor может показать уведомление, выбор из нескольких — окно. Кандидаты требуют одновременно isOwner и hasPlayerOwner, поэтому доступный GM NPC без владельца-игрока не входит в список; текущий controlled Actor при этом выбирается до фильтра. getActorOwner не гарантирует существование результата, если нет активного GM/игрока-владельца.

getRandomInt не создаёт Roll/ChatMessage; влияет на downstream выбор локации, последствия травмы, стороны и вероятности эффекта. addPart лишь строит строку: нулевой ввод с hideZero скрывает, отрицательный сохраняет; итоговая формула парсится далее. getCustomModifier возвращает строку с ведущим '+', а не числовое значение.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Текущий Actor/Token и выбор | Группа 15 | Приоритет первого controlled, fallback character, 0/1/>1 кандидатов, исключение NPC без player owner, выбранный/удалённый ID; null input → TypeError | Настоящий helper; UI и коллекции/Actor заменены. Контракт null отдельно прочитан в ядре. |
| Владелец и делегирование | Группа 16 | Активный OWNER приоритетнее GM; иначе GM; без обоих null. Настоящий applyStatusEffectToActor при !isOwner и таком результате отвергается с TypeError до query | Реальный метод потребителя, fromUuidSync и Actor представлены фасадами; удалённый клиент не запускался. |
| Границы случайного диапазона | Группа 17 | Для max=2/6/10/100 при Math.random=0 → 1, при 1−EPSILON → max; 0/undefined не валидируются | Подтверждён расчёт границ, не распределение случайности. |
| Модификаторы и парсер | Группы 11, 18 | 0/'0' → ''; -2 → '+-2'; детализация добавляет ключ; реальный parser принимает +-2, ++-2, ++2; prompt cancel отклоняет Promise | prompt/input — фасады, callback из настоящего helper; окна не рендерились. |

## Непроверенные участки и открытые вопросы

Полностью прочитаны 106 строк, все восемь экспортов и 16 импортирующих файлов сверены. getCurrentToken не имеет найденных внешних вызовов; некорректные max текущими потребителями не передаются, поэтому их крайние случаи не оформлены самостоятельными issues. Для расширения issue-00149 проверены реальные guards соседей, но полный UI боевых/словесных действий и многоклиентские запросы не исполнялись.

## Связанные проблемы

[issue-00008](../../../../../issues/potential/issue-00008.md), [issue-00149](../../../../../issues/potential/issue-00149.md), [issue-00185](../../../../../issues/potential/issue-00185.md). issue-00149 дополнена общим выбором Actor и потребителями. issue-00185 — отсутствие доступного получателя query; issue-00008 касается уже другого этапа, подтверждения выполнения обработчиком.

Дополнительно [issue-00186](../../../../../issues/potential/issue-00186.md): отсутствует русская подпись пользовательского модификатора. Ключи проверены структурным чтением en/ru; стандартный английский fallback сверён по коду Localization ядра. Сторонние переводы и браузер не проверялись.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `9f16a7ae4bc942df85a105fd37d9a3cb3ef99f4b`; полный файл | Первая карточка; [сверка порции](../../../review-log.md#task-0003028) |

## Уточнение TASK-0003.029

2026-09-11, `273a6d7db0b7c866399db3ecd4f7191817ae6f10`. Полный разбор actor/skillMixin подтверждает два ожидаемых getCustomModifier перед extendedRoll. Отмена прерывает навык без сообщения; положительные/отрицательные добавки входят в настоящую формулу. Неизвестный Item.attribute/ID может завершить метод ещё до запроса. Политика игнорирования собственных бонусов принадлежит другому helper — modifierMixin.addActiveEffects.

Сверенные связи: [module/actor/mixins/skillMixin.js](../../../../../../module/actor/mixins/skillMixin.js). Полные карточки новых файлов — в [указателе порции](../../README.md#навыки-броски-развитие-и-пользовательские-навыки--task-0003029). [Проверки, ограничения и версия](../../../review-log.md#task-0003029). Исходники и статус проблем не менялись.

## Уточнение TASK-0003.030

2026-09-11, `aa6af106e86a9c75fe050d599f961c8fadb74f1b`. getCustomModifier вызван stat-save перед броском; положительный модификатор увеличивает кубик при reversal и тем самым затрудняет успех. Отмена отклоняет Promise. Проверка переводов теперь включает expandObject, как в core; русские customModifier и savingThrow отсутствуют, en fallback есть.

Сверенные источники: [module/actor/sheets/mixins/statMixin.js](../../../../../../module/actor/sheets/mixins/statMixin.js). [Итоговая сверка третьей серии, сценарии и ограничения](../../../review-log.md#task-0003030). Код и статусы проблем не менялись.

## Дополнительная сверка TASK-0003.038

2026-09-11, `rusbar-main`, `b47ba02cdaebc6a66ad14a5638213b6eb24460b4`; исходники не менялись.

getCustomModifier используется обычным профессиональным skillRoll: строка 0 не добавляется, custom 2 даёт +2; rejectClose возвращает отклонённый Promise. getActorOwner(target) выбирает получателя temporaryHp query. applyOnTarget выбирает первую цель либо this. При отсутствии владельца/activeGM query не защищён; полный сетевой сценарий не выполнен.

[module/actor/mixins/professionMixin.js](../actor/mixins/professionMixin.js.md), [templates/partials/character/tab-profession.hbs](../../templates/partials/character/tab-profession.hbs.md), [templates/sheets/actor/partials/monster/tabs/tab-profession.hbs](../../templates/sheets/actor/partials/monster/tabs/tab-profession.hbs.md), [templates/dialog/combat/profession-attack.hbs](../../templates/dialog/combat/profession-attack.hbs.md).

[Сверка и ограничения](../../../review-log.md#task-0003038). Связанные файлы повторно в покрытии не учитывались; код и статусы issues не изменены.

## Дополнительная сверка TASK-0003.039

2026-09-11, `c598d74e34f4be51535de78b38f0601c286c5407`; исходники не менялись.

getActorOwner вызывается из effect/status helpers после castSpell при actor.isOwner=false; группа 33 захватила запросы, не исполняя сеть. getCurrentCharacter обслуживает ручную ссылку статуса; castSpell автоматические эффекты направляет по Actor UUID/targets.

[templates/chat/combat/spellItem.hbs](../../../../../../templates/chat/combat/spellItem.hbs) — [карточка](../../templates/chat/combat/spellItem.hbs.md).

[Сценарии, методика и пределы проверки](../../../review-log.md#task-0003039). Соседние определения проверены в пределах связи; это не расширяет состав шести полностью разобранных файлов.

### Дополнительная сверка TASK-0003.040

2026-09-11, `rusbar-main`, `74322e91edac106c82668f4a47eef53ce1889dc1`; исходники прежние. Прямой named-import getInteractActor используется только запросом ремонта chat.js. Сначала выбирается controlled/user.character либо доступный Actor, и только потом проверяются owner/item. При отсутствии исполнителя callback всё ещё может упасть на отсутствующем owner. Отмена выбора из нескольких персонажей в тестовом DialogV2.input=null приводит к TypeError внутри chooseFromAvailableActors(values.actor). Кнопка лечения использует собственный targets→controlled→character алгоритм и не вызывает этот helper.

Сопоставленные исходники: [module/scripts/chat.js](../../../../../../module/scripts/chat.js). Полные новые описания: [chat.js](chat.js.md).

[Сверка порции и всей серии .031–.040](../../../review-log.md#task-0003040). Уточнение связи не означает повторной проверки всех сценариев соседнего файла; мир/БД и браузер не запускались.

## Дополнительная сверка TASK-0003.042

2026-09-12, rusbar-main, 16695cbfc7fec3e0de56660c7cab21bc0304e94b; исходники не изменены.

В [критическом пути](../actor/mixins/defenseMixin.js.md) getActorOwner исполнен: активный OWNER предпочтён GM, отсутствие GM/владельца ведёт к TypeError до toMessage (185). Отдельно отсутствующий attacker Actor ломает чтение hasPlayerOwner. getRandomInt для сторон конечностей заменён фиксированным 1/2; распределение случайности не проверено.

[Сверка и ограничения](../../../review-log.md#task-0003042). Уточнение связей не увеличивает покрытие. Код и статусы issues не исправлялись; подтверждение пользователя не получено.

## Дополнительная сверка TASK-0003.045

2026-09-12, rusbar-main, 20ce99a1218a82bf46c84570e55587253d0cfbc3; исходники не изменены.

Полностью описаны [боевые listeners](../../../../../../module/scripts/combat/combat.js) и [меню урона](../../../../../../module/scripts/combat/applyDamage.js). Группа 04 получила отсутствующий Actor через фасад getInteractActor: executeDefense вышел, stun и три critical callbacks дали TypeError. Группа 11 проверила чтение actor.type в диалоге. Это повторная проверка уже перечисленных потребителей issue149; новый дубль не создан. Сам алгоритм выбора/helper input заново не исполнялся. Вложенный event.target не ломает эти closure/listeners; прежняя проблема onRepairRequest относится к другому пути.

[Проверки, результаты и ограничения](../../../review-log.md#task-0003045). Связанные файлы не засчитываются повторно в покрытии.

## Дополнительная сверка TASK-0003.046

2026-09-12, rusbar-main, a69f11d2e4c4318cfbf635dabad97b0062c63c20; исходники не изменены.

Полностью разобраны [общий словесный бросок](../actor/mixins/verbalCombatMixin.js.md) и [применение урона](verbalCombat/verbalCombat.js.md). Настоящий addPart принимает 0/−2/+2/2+3 и truthy строку 'hide'; формулы распарсены настоящим Roll (группа 02). Defense самостоятельно сравнивает текстовый customModifiers с 0 и пропускает 2+3, не вызывает addPart для него. applyVerbalCombatDamage:52–55 без Actor выбрасывает TypeError, executeDefense:19–20 имеет guard (группы 15/17); меню блокируется раньше по [302](../../../../../issues/potential/issue-00302.md). Это уточнение [149](../../../../../issues/potential/issue-00149.md), сам выбор getInteractActor/input повторно не запускался.

[Сценарии, результаты и ограничения](../../../review-log.md#task-0003046). Связанные файлы повторно не засчитываются в покрытие.

## Уточнение TASK-0003.057 — боевые таблицы

2026-09-12, rusbar-main 8573642b0136f80b8ae3456de51e1b7f637ec7f3; исходник не изменён.

getRandomInt:73–75 реально использован в 20 проверках Actor.randomHuman/randomMonster с контролируемым Math.random. Основные RollTable используют собственный Roll/Die RNG. Совпадение названия локаций не связывает эти генераторы.

[Карточки Combat](../../README.md#боевые-таблицы--task-0003057), [перекрёстная сверка](../../../review-log.md#task-0003057). Для issue-00322/00323/00324 см. [реестр проблем](../../../../../issues/potential/../README.md). Пределы изолированных сценариев сохранены отдельно от запуска мира.
