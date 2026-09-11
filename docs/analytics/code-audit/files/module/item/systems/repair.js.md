# module/item/systems/repair.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/item/systems/repair.js](../../../../../../../module/item/systems/repair.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `c7cd9d71dcb1714cdccb175aee351a3f1df95c5b` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.017](../../../../../../tasks/task-0003.017.md), одна порция из пяти файлов |
| Запись перекрёстной сверки | [TASK-0003.017](../../../../review-log.md#task-0003017) |

## Назначение файла

Процесс ремонта Item: разрешение рецепта и компонентов, выбор исполнителя, диалог, формула проверки, сообщения и вызов восстановления. Хранит краткоживущий RepairData и экспортирует общий экземпляр RepairSystem.

## Условия использования

Модуль импортируют repairMixin и обработчик чата. При импорте определяются Repair/RepairData, costEditMixin добавляется к прототипу, создаётся Object.freeze(new Repair()). Документ WitcherItem получает методы примеси; кнопка инвентаря вызывает item.repair(), кнопка запроса в чате — processRequest(owner,item,artisan). Импорт сам не бросает кубы и не изменяет документы. Это обычные классы JavaScript, не DataModel/Document Foundry.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| Repair | Локальный класс,11–292 | Координация ремонта | Доступен через default instance | 15 собственных методов плюс 2 из costEditMixin |
| RepairData | Локальный класс,294–341 | Контекст одного обращения | Возвращается prepareData | Конструктор и 7 getters; нет сериализации/регистрации |
| DialogV2 | Локальный alias,6 | Окно и ожидание выбора | foundry.applications.api.DialogV2 | Захватывается при импорте |
| repairModifier / perEnchantModifier | Константы,8–9 | Поправка сложности -5 / +2 за непустой ID улучшения | Локальные | Только расчёт/подпись; соответствие рулбуку здесь не устанавливается |
| RepairSystem | Экземпляр,343–347 | Единый получатель вызовов | Default export | Object.assign прототипа, затем поверхностный freeze экземпляра |
| actor, item, diagram, ownedComponents, missingComponents, unknownComponents, artisan, additionalCost | Собственные поля RepairData,295–303 | Ссылки на документы, три списка, исполнитель и ручная цена | additionalCost=0, artisan=null по умолчанию | Не копии документов; callback диалога меняет additionalCost |
| enchantsCount, executor, repairDC, repairDCFormula, enchantsDC, skillName, repairPrice | Getters RepairData,306–340 | Вычисляемые значения | Читаются методами/Handlebars | Пересчитываются при чтении; не сохраняются |
| repair / sim-repair / request-repair / gm-repair; render callback | Объекты кнопок и стрелочные функции,67–114 | Выбор обычного ремонта, симуляции, публикации запроса, GM-восстановления; ввод цены | DialogV2.wait | Callbacks замыкают один data; render подписывает DOM через примесь |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| process(actor,item):12–17 | Владелец и Item | Promise<void> | Ждёт prepareData; при data ждёт renderDialog | Без catch, результат диалога наружу не возвращает |
| prepareData(actor,item,artisan=null):19–55 | item.system.associatedDiagramUuid; executor.findNeededComponent | Promise<RepairData> либо undefined | await fromUuid рецепта; для каждой craftingComponents берёт первый найденный по имени; иначе await UUID или unknown | Нет рецепта → error и выход. Нет проверки типа/quantity/успешности UUID материала; quantity строки рецепта не используется |
| processRequest(owner,item,artisan):57–63 | Выбранный исполнитель | Promise<void> | prepareData(owner,item,artisan); повторно data.artisan=artisan; renderDialog | Инвентарь/навык берутся у artisan, предмет остаётся у owner |
| renderDialog(data):65–116 | Полный контекст | Promise<void> | Готовит HTML; repair(false,false), sim-repair(true,false); без artisan request-repair, с artisan и user.isGM gm-repair(true,true) | modal:true; await DialogV2.wait. Render callback присваивает data.additionalCost. Отмена без callback не начинает ремонт |
| prepareDialogTemplate(data):118–165 | Три массива, game.user.isGM | Promise<string> | unknown→missing→owned; img/name/quantity/missingQuantity/required=1/cost; isRequest=(artisan!==null), canEditCost=isGM | Owned quantity<1 показывается как нехватка; это не проверка допуска. null в missing вызывает TypeError на oc.img |
| repairItem(data,options):167–182 | simulate, gmRepair; для обычного пути ожидается damagedLocations | Promise результата уведомления либо void | При !simulate отклоняет missing/unknown, затем отсутствие повреждений; далее gmRepair или commonRepair | В штатном RepairData нет damagedLocations: при наличии всех компонентов чтение .length бросает TypeError. simulate обходит оба условия |
| commonRepair(data,simulate):184–198 | Формула/контекст; extendedRoll | Promise<void> | prepareRollFormula→prepareRollConfig→await initMessageData→await extendedRoll; success=total>threshold; при !simulate _doRepair; roll.toMessage | showResult=false отключает публикацию внутри extendedRoll; завершающий toMessage не ожидается. Ошибки подготовки/синхронного _doRepair прерывают следующий шаг |
| gmRepair(data):200–203 | item.system.repair | Promise<void> | Ждёт sendRepairInfoToChat(false), вызывает system.repair | Нет броска, removeItem, изменения денег или проверки разрешения Item; вложенные create/update не ожидаются |
| prepareRollFormula(data):205–224 | executor.stats.cra.value, skills.cra.crafting.value, addActiveEffects | Строка при успешном чтении настроек | 1d10+CRA+crafting; подписи по displayRollsDetails; затем addActiveEffects('crafting') | woundsAffectSkillBase не зарегистрирована системой → core get бросает. При внешнем true добавляет только открывающую скобку; modifierMixin её не закрывает |
| prepareRollConfig(data,reliabilityToRestore):226–238 | repairDC/skillName | RollConfig | showCrit=true, showSuccess=true, showResult=false, threshold=DC, подписи успеха/провала | reliabilityToRestore нигде не читается; defense/reversal остаются false |
| initMessageData(data):240–248 | executor и renderChatTemplate | Promise<{speaker,flavor,system:{}}> | Рендерит обычную карточку результата, speaker по исполнителю | Только подготовка; сам ChatMessage не создаёт |
| renderChatTemplate(data,isRequest):250–260 | RepairData | Promise<string> | Передаёт data,isRequest,isOrder=(artisan!==null),showComponents=owned.length или missing.length | unknownComponents не участвует в showComponents; значения могут быть числами, используемыми HBS по truthiness |
| _doRepair(data,success):262–275 | Список owned, executor.removeItem, item.canUserModify | undefined | Для каждой записи запускает removeItem(_id,1) при успехе и провале; success и право update → getRestoreReliabilityData→item.update; иначе emitForGM('restoreReliability',[uuid]) | getRestoreReliabilityData не определён. В изолированном вызове remove уже начат перед этой ошибкой. remove/update/emit не ожидаются |
| sendRepairInfoToChat(data,isRequest):277–287 | renderChatTemplate, executor | Promise<void> | Ждёт HTML, собирает content/speaker/style OTHER, вызывает ChatMessage.create | Не ждёт создания сообщения |
| restoreReliability(item):289–291 | system.repair | undefined | Прямое делегирование модели | Без проверок рецепта, материалов, прав и ожидания repair |
| RepairData.constructor(...):295–304 | actor,item,diagram,три массива,artisan | Новый data | Сохраняет 7 аргументов; additionalCost=0 | damagedLocations здесь и в прототипе отсутствует |
| get enchantsCount():306–308 / enchantsDC():328–330 | item.system.enhancementItemIds | Число truthy ID / число×2 | filter(e=>e).length, затем множитель | Не разрешает ID, не проверяет applied/equipped, не устраняет повторы; отсутствие массива вызывает ошибку |
| get executor():310–312 / skillName():332–334 | artisan,actor; CONFIG.WITCHER.skillMap.crafting.rollLabel | Исполнитель / локализованное имя навыка | artisan??actor; localize | Ссылки и подпись, без записи |
| get repairDC():314–316 / repairDCFormula():318–326 | craftingDC и enchantsCount | DC / поясняющая строка | craftingDC-5+2×count; строка условно добавляет слагаемое улучшений | Не числовой бросок; пределы DC не задаются |
| get repairPrice():336–340 | Цены owned/missing, additionalCost | Сумма | Начинает с additionalCost, прибавляет по одной cost каждого owned и missing | Нет умножения на quantity, отдельной цены труда или платежа; unknown учитывается только ручным additionalCost; null/нечисловые значения могут нарушить расчёт |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| extendedRoll | [module/scripts/rolls/extendedRoll.js](../../../../../../../module/scripts/rolls/extendedRoll.js) | Import/call | commonRepair:192; evaluate/crit/fumble и разметка результата | Функция прочитана; настоящий код выполнен с Roll-фасадом, без критического броска |
| RollConfig | [module/scripts/rollConfig.js](../../../../../../../module/scripts/rollConfig.js) | Import/new | prepareRollConfig:227 | Конструктор с defense=false/reversal=false; определения и изолированный вызов |
| emitForGM | [module/scripts/socket/socketMessage.js](../../../../../../../module/scripts/socket/socketMessage.js) | Import/call | _doRepair:272; удалённое восстановление при отсутствии update | Настоящий sender/receiver исполнены через перехваченный объект сообщения; сеть не использована |
| costEditMixin.attachHtmlListeners/_calculateAdditionalCost | [module/item/mixins/costEditMixin.js](../../../../../../../module/item/mixins/costEditMixin.js) | Import/Object.assign | Прототип 343, render114; присвоение additionalCost | Полный разбор этой порции |
| findNeededComponent | [module/actor/mixins/craftingMixin.js](../../../../../../../module/actor/mixins/craftingMixin.js) | Метод executor | prepareData:35; первый компонент по имени/локализованной субстанции | Определение 15–40, вызов с настоящими BaseItem; фильтра isStored здесь нет |
| removeItem | [module/actor/witcherActor.js](../../../../../../../module/actor/witcherActor.js) | Метод executor | _doRepair:264; списание единицы каждой записи | Определение 275–283 ждёт delete/update, но Repair его Promise не использует |
| addActiveEffects | [module/actor/mixins/modifierMixin.js](../../../../../../../module/actor/mixins/modifierMixin.js) | Метод executor | prepareRollFormula:222; фрагмент навыка crafting | Полный ранее проверенный метод; настоящий вызов дал +2[bonus] и не закрыл скобку |
| CRA value (Stats.cra → stat.value) | [module/data/actor/templates/common/stats/statsData.js](../../../../../../../module/data/actor/templates/common/stats/statsData.js); [module/data/actor/templates/common/stats/statData.js](../../../../../../../module/data/actor/templates/common/stats/statData.js) | Чтение prepared Actor | prepareRollFormula:206–209; statMap.cra/skillMap.crafting задают подписи | Пути stats.cra.value и skills.cra.crafting.value сверены с Actor и конфигурацией |
| crafting / value, activeEffectModifiers | [module/data/actor/templates/common/skills/craData.js](../../../../../../../module/data/actor/templates/common/skills/craData.js); [module/data/actor/templates/common/skills/skillData.js](../../../../../../../module/data/actor/templates/common/skills/skillData.js) | Схема навыка | Craft.crafting → Skill.value; addActiveEffects читает подготовленный activeEffectModifiers | Фабрика навыков и ранее проверенные карточки |
| associatedDiagramUuid, enhancementItemIds, system.repair | [module/data/item/weaponData.js](../../../../../../../module/data/item/weaponData.js) | Чтение модели и вызов | prepareData/getters/gmRepair/restoreReliability | WeaponData.repair→parent.update(system.reliable=maxReliability); реальный BaseItem, update-фасад |
| associatedDiagramUuid, enhancementItemIds, system.repair | [module/data/item/armorData.js](../../../../../../../module/data/item/armorData.js) | Чтение модели и вызов | Те же общие ветви | ArmorData.repair→reliability и 6 stoppingPower максимумов; payload проверен |
| craftingComponents/craftingDC | [module/data/item/diagramData.js](../../../../../../../module/data/item/diagramData.js) | Чтение модели рецепта | prepareData/RepairData | Настоящая DiagramData; quantities требования не используются ремонтом |
| quantity/cost/name/uuid | [module/data/item/componentData.js](../../../../../../../module/data/item/componentData.js); [module/data/item/commonItemData.js](../../../../../../../module/data/item/commonItemData.js) | Чтение Item/system | Подбор и отображение owned/missing | name/uuid принадлежат Document, quantity/cost наследуются CommonItemData; реальный BaseItem |
| statMap.cra.label / skillMap.crafting.rollLabel | [module/setup/config.js](../../../../../../../module/setup/config.js) | CONFIG.WITCHER | Локализованные подписи формулы и DC | Реальные значения WITCHER.Actor.Stat.Cra / WITCHER.skills.crafting.rollLabel |
| displayRollsDetails; отсутствие woundsAffectSkillBase | [module/setup/settings.js](../../../../../../../module/setup/settings.js) | game.settings.get | prepareRollFormula:211–216 | registerSettings реально зарегистрировал 9 ключей; старого ключа нет |
| Ремонтный диалог | [templates/dialog/repair-dialog.hbs](../../../../../../../templates/dialog/repair-dialog.hbs) | renderTemplate | prepareDialogTemplate:161–164 | Полный HBS и контекст; фактический Handlebars |
| Запрос/результат ремонта | [templates/chat/item/repair.hbs](../../../../../../../templates/chat/item/repair.hbs) | renderTemplate | renderChatTemplate:251–259 | Полный HBS и обработчик request-repair |
| Ключи WITCHER.Repair.*, ComponentsList.totalPrice и динамические подписи | [lang/en.json](../../../../../../../lang/en.json); [lang/ru.json](../../../../../../../lang/ru.json) | localize/шаблоны | Кнопки, предупреждения, сообщения и формула | 20 итоговых ключей этой порции существуют в en/ru; остальные языки не проверены |
| DialogV2.wait | Foundry 14.367.0, /opt/foundryvtt/client/applications/api/dialog.mjs:405–425 | Внешний API | renderDialog ожидает выбор/закрытие | Core close по умолчанию разрешает null; runtime wait был фасадом отмены |
| fromUuid / canUserModify / Item.update / ChatMessage / CONST.CHAT_MESSAGE_STYLES.OTHER | Foundry 14.367.0; UUID: /opt/foundryvtt/client/utils/helpers.mjs; common Document/модели | Внешний API | Разрешение документов, права, запись предмета, публикация | UUID/update/права/chat в сценариях подменены; модельные данные и константа настоящие |
| ClientSettings.get / #assertSetting | Foundry 14.367.0, /opt/foundryvtt/client/helpers/client-settings.mjs:212–229,264–271 | Внешний API | Настройки формулы | Реальный класс/регистрация; storage и Setting заменены; неизвестный ключ действительно бросил Error |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/item/mixins/repairMixin.js](../../../../../../../module/item/mixins/repairMixin.js) | RepairSystem.process/restoreReliability | Методы Item через примесь | Импорт 1, вызовы 5/9; полный разбор |
| [module/scripts/chat.js](../../../../../../../module/scripts/chat.js) | RepairSystem.processRequest | onRepairRequest выбирает artisan и ищет owner/item по ID | Импорт 2, callback50–62; настоящий listener исполнен с Actor/DOM-фасадами |
| [templates/dialog/repair-dialog.hbs](../../../../../../../templates/dialog/repair-dialog.hbs) | RepairData и подготовленный components | Отображение сложности/ожидаемых повреждений/цены | Полный шаблон |
| [templates/chat/item/repair.hbs](../../../../../../../templates/chat/item/repair.hbs) | RepairData и isRequest/isOrder/showComponents | Запрос/информационная часть результата | Полный шаблон |

Область поиска: текущие module/ и templates/; регистрации сверены отдельно. Динамические обращения внешних модулей не исследовались.

## Данные и изменения состояния

prepareData и getters читают документы, формируют массивы ссылок и временный data. Единственное присвоение цены — additionalCost в render callback; списания кошелька или передачи денег в этом файле нет. _doRepair инициирует removeItem по одной единице на запись независимо от success; восстановление запускается только при success. GM-путь не расходует материалы. Цена в сообщении не доказывает платёж.

Два независимых разрыва нельзя скрывать описанием предполагаемого успешного процесса: у RepairData отсутствует damagedLocations, у Repair — getRestoreReliabilityData; настройка woundsAffectSkillBase отсутствует в регистрации. Поэтому изолированные проверки нижних ветвей не доказывают достижимость обычного успешного ремонта в текущем клиенте.

При успехе без прав используется socket system.TheWitcherTRPG: [uuid] → активный GM → документ.restoreReliability → примесь → system.repair. Это отдельный протокол от CONFIG.queries и без прикладного ответа об окончании обновления. _doRepair запускает списание до отправки. Обновления/сообщения не объединены в транзакцию.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Подготовка/контекст | Настоящие RepairSystem/RepairData, Component/Diagram/Weapon BaseItem; UUID-карта | Без рецепта 2 уведомления; owned Leather quantity0/isStoredtrue, missing Steel, unknown Unknown; artisan использует свой инвентарь | Документы не из мира, UUID API заменён |
| Getters и диалог | DC20, ID[a,'',a], cost3/5, additional4; реальные HBS | enchants2/DC19/price12; 4 комбинации GM/artisan дали ожидаемые наборы кнопок; повреждения отсутствуют | DialogV2.wait только регистрирует конфигурацию и возвращает null |
| Обычный путь | Реальный repairItem на RepairData с пустыми missing/unknown | TypeError чтения length; с вручную добавленным [] — предупреждение; missing/unknown отклоняется раньше | damagedLocations=[]/[{}] добавлялся только для отдельной проверки условий, не исправлялся код |
| Успешный _doRepair | Прямой вызов, update разрешён | removeItem вызван, затем getRestoreReliabilityData is not a function | Не доказательство списания в обычном UI: штатный путь имеет более ранние ошибки |
| Настройки/парсер | Настоящие registerSettings/ClientSettings; затем отдельный get-фасад; Foundry RollParser/grammar.pegjs и Peggy в памяти | 9 ключей, неизвестный throws; с false обе формулы разбираются, с true обе дают SyntaxError | Подмена get исследует условную ветвь, не регистрирует новую настройку |
| Симуляция и порог | Настоящие commonRepair/extendedRoll, Roll-фасад totals18/19/20, DC19 | Успех false/false/true; только Roll.toMessage, без восстановления/списания; метод вернулся при pending сообщении | Нет реальных кубов/crit/fumble/БД; неизвестная настройка для этого опыта подменена |
| GM/модели/сокет | Настоящие gmRepair, repairMixin, методы моделей, sender/receiver; управляемые Promise | GM: create→weapon.update reliable10 без remove; Armor payload 7 полей; socket получен активным GM и инициировал update | Сеть и запись заменены, завершение методов не равно завершению pending операций |
| Ошибочные ссылки/чат | Реальные prepareData/prepareDialogTemplate/renderChatTemplate и chat listener | missing=[null]→TypeError img; только unknown скрыты; удалённый owner→TypeError items | Состояние мира и удаление Actor не воспроизводились |
| Локализация/полный охват | 347 строк,15 методов Repair, конструктор/7 getters,4 импорта; 20 ключей всей порции | Чтение и связи сверены; все 20 ключей en/ru найдены | Код не исправлялся; проверка текста не подтверждает игровые правила |

## Непроверенные участки и открытые вопросы

Foundry 14.367/Node 24.16, Linux. Полностью прочитан этот файл; соседние чат, сокет, Roll и Actor-операции просмотрены на границах и не получают карточек от этой проверки. Не запускались мир, браузер, настоящие броски, сеть, запись в БД, платёж, конкурирующие действия или клиент с внешними модулями. Наличие старой настройки у внешнего модуля не проверено. Для нижних ветвей явно использованы подменённые settings/Roll и, в проверке допуска, вручную добавленный damagedLocations. Статус «Проверено» относится к описанию кода.

## Связанные проблемы

[issue-00102](../../../../../../issues/potential/issue-00102.md), [issue-00103](../../../../../../issues/potential/issue-00103.md), [issue-00104](../../../../../../issues/potential/issue-00104.md), [issue-00105](../../../../../../issues/potential/issue-00105.md), [issue-00106](../../../../../../issues/potential/issue-00106.md), [issue-00107](../../../../../../issues/potential/issue-00107.md), [issue-00108](../../../../../../issues/potential/issue-00108.md), [issue-00081](../../../../../../issues/potential/issue-00081.md), [issue-00100](../../../../../../issues/potential/issue-00100.md), [issue-00008](../../../../../../issues/potential/issue-00008.md), [issue-00010](../../../../../../issues/potential/issue-00010.md), [issue-00034](../../../../../../issues/potential/issue-00034.md). 102/103 — независимые блокировки;104 — нулевой owned;105 — null UUID;106 — глобальный DOM цены;107/108 — границы чата. 81 дополнена ожиданием операций ремонта,100 — прежний NaN. 8/10 описывают маршрутизацию;34 относится к другим методам Actor, сам removeItem ожидает запись.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.017 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.

## Уточнение TASK-0003.028

2026-09-11, `9f16a7ae4bc942df85a105fd37d9a3cb3ef99f4b`: commonRepair:190 вызывает extendedRoll с prepareRollConfig, где showResult=false. Общий бросок не исправляет формулу: реальный parser отклоняет незакрытую скобку и фрагмент с пропущенным оператором. В штатном ремонте [issue-00103](../../../../../../issues/potential/issue-00103.md) прерывает подготовку раньше, на незарегистрированной настройке; повторного исполнения ремонта в этой порции не было. RollConfig.showSuccess не читается extendedRoll, успех определяется threshold>=0.

Полные карточки зависимости: [module/scripts/rollConfig.js](../../scripts/rollConfig.js.md), [module/scripts/rolls/extendedRoll.js](../../scripts/rolls/extendedRoll.js.md). [Перекрёстная сверка](../../../../review-log.md#task-0003028). Это уточнение связи; исходный файл не изменён.

## Уточнение TASK-0003.034

2026-09-11, `7dbb31bdbd094f58c77c9e58dd5a684df6bb942c`. Полная craftingMixin подтвердила контракт findNeededComponent: включает stored и quantity0, сохраняет порядок коллекции. prepareData:35 берёт лишь [0], затем при отсутствии имени отдельно пробует UUID. В .034 заново проверен сам поиск, полный ремонт не запускался; прежняя issue-00104 и другие результаты ремонта не подменяются новым сценарием.

Связи: [module/actor/mixins/craftingMixin.js](../../actor/mixins/craftingMixin.js.md). [Результаты и пределы проверки](../../../../review-log.md#task-0003034).

### Дополнительная сверка TASK-0003.040

2026-09-11, `rusbar-main`, `74322e91edac106c82668f4a47eef53ce1889dc1`; исходники прежние. Default singleton RepairSystem импортирован chat.js. Его callback передаёт processRequest(owner,item,artisan) в правильном порядке и ожидает Promise. Группа20 исполнила реальный processRequest с заменёнными prototype prepareData/renderDialog, группа23 — настоящий prepareData до раннего отсутствия диаграммы. Успешный полный ремонт не выполнялся; missing-owner падает до RepairSystem (issue-00108), а missing Item при существующем owner даёт выход.

Сопоставленные исходники: [module/scripts/chat.js](../../../../../../../module/scripts/chat.js). Полные новые описания: [chat.js](../../scripts/chat.js.md).

[Сверка порции и всей серии .031–.040](../../../../review-log.md#task-0003040). Уточнение связи не означает повторной проверки всех сценариев соседнего файла; мир/БД и браузер не запускались.
