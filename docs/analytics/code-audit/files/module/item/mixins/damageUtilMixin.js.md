# module/item/mixins/damageUtilMixin.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/item/mixins/damageUtilMixin.js](../../../../../../../module/item/mixins/damageUtilMixin.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-12 |
| Ветка и коммит | rusbar-main, 965132d5d7972a0edd73aaa62484a1b6ba15991f |
| Изменения относительно коммита | Нет; совпадает со срезом TASK-0001 15da5b225535e34af4e132c701b5353ef4eb667f |
| Задача и порция | [TASK-0003.044](../../../../../../tasks/task-0003.044.md), 9 файлов / 603 логических строк; данный файл — 109 |
| Запись перекрёстной сверки | [TASK-0003.044](../../../../review-log.md#task-0003044) |

## Назначение файла

Формирование данных урона Item, диалог переменной формулы, бросок и сообщение с вероятностными воздействиями.

## Условия использования

damageUtilMixin импортируется и присоединяется к WitcherItem.prototype в [module/item/witcherItem.js](../../../../../../../module/item/witcherItem.js):375. При импорте сохраняется alias DialogV2. createBaseDamageObject вызывают weaponAttack и castSpell; rollDamage вызывается кнопкой damage сообщения атаки и веткой rollOnlyDmg оружейной атаки. Последняя передаёт properties после toObject(false), поэтому до Roll обнаруживается отсутствие getPreprocessedEffects (297). Обычная AttackMessageData восстанавливает эту модель; группа 38. Одноимённая функция словесного боя в scripts/verbalCombat — другой обработчик.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| damageUtilMixin / DialogV2 | Export объекта:7; alias:5 | Три метода Item / окно | Object.assign; alias локальный | При импорте урон не бросается |
| properties, item, itemUuid, crit, defenseOptions | Возвращаемый объект:9–18 | Начальный контекст атаки | createBaseDamageObject | properties/item/defenseOptions по ссылке; crit — новый объект из двух чисел |
| preprocessedEffects | Массив:47–77 | Сгруппированные воздействия с applied | system.damage.properties.effects и flags | Новые копии записей; процент проверяется до Roll/toMessage |
| flavor / damageFormula / messageData | Локальные данные:22–84 | HTML и формула броска | ChatMessageData(type:damage) | Не являются DamageInstance |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| createBaseDamageObject:8–19 | Item.system.damageProperties; parent.system.attackStats | Новый object | Ссылки properties/item/defenseOptions; uuid; копия critLocationModifier/critEffectModifier | Синхронно; без parent выбрасывает ошибку; formula/type/location ещё не задаёт |
| async rollDamage:21–88 | damage.formula/properties/location.name; Item/Actor | Promise<void> | Формула, optional диалог, strike множитель, location, эффекты, Roll.evaluate/toMessage, setFlag | Меняет damage.location; ждёт диалог/evaluate/toMessage, не setFlag; исключения не ловит |
| async createVariableDamageDialog:90–109 | Исходная строка | Promise<строка> | HBS currentDamage; DialogV2.prompt; ok читает button.form.elements.newDamage.value | rejectClose:true; отмена отклоняет Promise; не проверяет формулу |

### Формула и эффекты

formula приводится к строке; только пустая строка заменяется на '0' с уведомлением. Значения undefined/null не нормализуются в 0. При strike с dmgMulti всё выражение заключается в скобки, затем дописывается множитель из CONFIG. Это не тот же путь, что добавочное серебро в Actor. location заново разрешается через WitcherActor.getLocationObject и заменяется в исходном damage.

getPreprocessedEffects возвращает массив копий, объединяя совпадающие statusEffect. Для truthy percentage бросается getRandomInt(100); значение<=percentage даёт applied=true, больше — false. Для 0 applied не задаётся, модель сообщения затем получает false. Два эффекта 30+20 при контролируемом результате 50 проходят,51 — нет; исходные записи не получают applied. При неизвестном truthy statusEffect обращение к statusEffect.img выбрасывает TypeError до броска повреждения.

HTML flavor формируется строкой. Первое открытие div не закрыто символом '>' перед '<h1', поэтому HTML parser воспринимает '<h1' как атрибут div. Картинка/имя Item и имена воздействий вставлены без экранирования в этом методе; санитарная обработка готового ChatMessage в браузере не проверялась. Статусная ссылка .apply-status получает data-status, но не duration.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| WitcherActor.getLocationObject | [module/actor/witcherActor.js](../../../../../../../module/actor/witcherActor.js) | import/static call | rollDamage:40 | Фиксированная/случайная локация; экземпляр Actor не передаётся |
| ChatMessageData | [module/chatMessage/chatMessageData.js](../../../../../../../module/chatMessage/chatMessageData.js) | import/new | :79, actor/flavor/type/system | DTO, не Foundry document/model |
| getRandomInt | [module/scripts/helper.js](../../../../../../../module/scripts/helper.js) | import/call | :61, диапазон 1–100 | Реальное определение; контролируемые входы теста |
| DamageProperties.getPreprocessedEffects | [module/data/item/templates/combat/damagePropertiesData.js](../../../../../../../module/data/item/templates/combat/damagePropertiesData.js) | Вызов метода properties | :47, копирование и группировка | У DamageMessageData такого метода нет |
| DamageMessageData / damageData | [module/data/chatMessage/damageMessageData.js](../../../../../../../module/data/chatMessage/damageMessageData.js); [module/data/chatMessage/templates/damageData.js](../../../../../../../module/data/chatMessage/templates/damageData.js) | Схема type:damage | Массив effects/applied, очистка system.damage | duration исключается; properties становится plain object |
| weapon.attacks / statusEffects | [module/setup/config.js](../../../../../../../module/setup/config.js) | CONFIG lookup | strike.dmgMulti/label и поиск статуса | strong '*2'; отсутствующий статус не проверен |
| attackStats | [module/data/actor/templates/character/attackStatsData.js](../../../../../../../module/data/actor/templates/character/attackStatsData.js) | Чтение parent | Начальные критические поправки | Схема Actor и вызовы producer |
| variableDamage.hbs | [templates/dialog/combat/variableDamage.hbs](../../../../../../../templates/dialog/combat/variableDamage.hbs) | renderTemplate | currentDamage и callback newDamage | Контекст/поле совпадают |
| .apply-status listener | [module/scripts/statusEffects/applyStatusEffect.js](../../../../../../../module/scripts/statusEffects/applyStatusEffect.js) | HTML hook | Ссылка позволяет вручную применить статус | chatMessageListeners/onApplyStatus читают dataset.status |
| Roll/evaluate/toMessage; DialogV2/prompt; renderTemplate; ui.notifications; i18n | Foundry14.367.0 | Внешний API | Бросок, окно и сообщение | Настоящий Roll/Handlebars; запись/диалог перехвачены |
| Ключи WITCHER.table.Damage, Dialog.*, Damage.*, Item.Effect, Effect.* | [lang/en.json](../../../../../../../lang/en.json); [lang/ru.json](../../../../../../../lang/ru.json) | Локализация | flavor и окно | Заголовок окна uses Item.properties.variableDamage — ключ отсутствует, HBS использует существующий Item.DamageProperties.variableDamage |
| .item-img/.chat-icon/.flex/.gap/.percentageFailed/.percentageSuccess | [styles/system-styles.css](../../../../../../../styles/system-styles.css); [styles/chat.css](../../../../../../../styles/chat.css) | HTML/CSS | Классы flavor | Поиск селекторов; фактический CSS cascade не проверен |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/item/witcherItem.js](../../../../../../../module/item/witcherItem.js) | damageUtilMixin | import/Object.assign | Методы Item |
| [module/actor/mixins/weaponAttackMixin.js](../../../../../../../module/actor/mixins/weaponAttackMixin.js) | createBaseDamageObject / rollDamage | Подготовка атаки и rollOnlyDmg | :135,:301 |
| [module/actor/mixins/castSpellMixin.js](../../../../../../../module/actor/mixins/castSpellMixin.js) | createBaseDamageObject | Начальная структура damage | :16; меняет prepared процент при varEffect |
| [module/scripts/combat/combat.js](../../../../../../../module/scripts/combat/combat.js) | rollDamage | onDamage получает Item по message.system.attack.itemUuid | :19–23; damage=message.system.damage |
| [module/data/chatMessage/damageMessageData.js](../../../../../../../module/data/chatMessage/damageMessageData.js) | Payload effects/applied | Очистка результата toMessage | Явная схема ArrayField |

Область поиска module/, templates/, styles/. Внешние макросы не исследованы.

## Данные и изменения состояния

createBaseDamageObject не делает копию properties: последующие addEffects/varEffect могут изменить prepared Item, не _source (70/247). Сам rollDamage получает копии эффектов и меняет им applied, не исходный словарь. В сообщении одновременно готовятся system.damage и дополнительный flags.TheWitcherTRPG.damage; setFlag выполняется отдельной записью. Нормальный получатель читает system.damage. duration присутствует в сыром payload/flag, но очищается схемой system; critEffectModifier внутри damage.crit сохраняется.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Три метода, ссылка/формулы | Группы 01,03–04 | Parent обязателен; 4,2+3,2d6+1,strong, пустая; submit/cancel/ошибка | Настоящий Roll, minimize кубов; prompt фасад |
| Вероятность/память | 05 |30+20→50;50 проходит/51 нет;0→false; source не меняется | Контролируемый random вместо статистического теста |
| Граница сообщения | 06 | toMessage ожидается, setFlag остаётся pending; DMD удаляет duration | Реальная модель после сериализации JSON; не DB |
| HTML/переводы | 07,32 | '<h1' стал атрибутом; неверный title key отсутствует в en/ru | parse5 и expandObject; не клиентский рендер |

Группа 38 отдельно проверила форму прямого rollOnlyDmg после toObject(false) и контроль через настоящую AttackMessageData: прямой вызов отклоняется, сообщение восстанавливает метод и даёт Roll4.

## Непроверенные участки и открытые вопросы

Все строки прочитаны. Диалог и браузерный lifecycle сообщений, реальная запись флага, разрешение UUID и очистка HTML не запускались. Повторный rollDamage на уже готовом damage-сообщении со SchemaField properties не является найденным штатным путём: он не имеет getPreprocessedEffects. Отрицательная/невалидная формула и неизвестная локация не нормализуются этим методом.

## Связанные проблемы

[00070](../../../../../../issues/potential/issue-00070.md), [00184](../../../../../../issues/potential/issue-00184.md), [00247](../../../../../../issues/potential/issue-00247.md), [00257](../../../../../../issues/potential/issue-00257.md), [00293](../../../../../../issues/potential/issue-00293.md) HTML, [00295](../../../../../../issues/potential/issue-00295.md) неизвестный статус, [00296](../../../../../../issues/potential/issue-00296.md) ключ заголовка.

[issue-00297](../../../../../../issues/potential/issue-00297.md) — разрыв формы properties в прямом rollOnlyDmg.

## История актуализации

| Дата | Версия и область | Результат |
| --- | --- | --- |
| 2026-09-12 | 965132d5d7972a0edd73aaa62484a1b6ba15991f; полный файл | Первичная карточка; [перекрёстная сверка](../../../../review-log.md#task-0003044) |
