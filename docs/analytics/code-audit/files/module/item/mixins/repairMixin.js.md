# module/item/mixins/repairMixin.js

## Текущее состояние — 14.3.1.00104

2026-09-19, TASK-0011.004. restoreReliability возвращает RepairSystem.restoreReliability(this). Завершение model.repair → parent.update передаётся Item и существующему query. Методы этой примеси остаются интерфейсом Item.

[Проверки и границы](../../../../../task-0011-static-checks.md#task-0011004): 38 локальных сценариев; B04 впереди. Ниже датированные предыдущие срезы, утверждения о разрывах этой цепочки заменены настоящим разделом.

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/item/mixins/repairMixin.js](../../../../../../../module/item/mixins/repairMixin.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `c7cd9d71dcb1714cdccb175aee351a3f1df95c5b` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.017](../../../../../../tasks/task-0003.017.md), одна порция из пяти файлов |
| Запись перекрёстной сверки | [TASK-0003.017](../../../../review-log.md#task-0003017) |

## Назначение файла

Присоединяет к документу Item два входа ремонта: открыть процесс с его владельцем или немедленно делегировать восстановление модели.

## Условия использования

Именованный export repairMixin добавляется к WitcherItem.prototype через Object.assign в witcherItem.js:373. При импорте загружается RepairSystem; операции не выполняются до вызова. this ожидается документом Item, а не Item.system. Методы существуют у всех WitcherItem, хотя canBeRepaired у общей модели false и UI показывает ремонт для соответствующих оружия/брони.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| repairMixin | Экспорт let,3–12 | Набор двух методов | Object.assign(WitcherItem.prototype,repairMixin) | Не создаёт экземпляров/данных |
| repair | Async method,4–6 | Начать пользовательский процесс | Item.repair() | Передаёт this.actor и this |
| restoreReliability | Method,8–10 | Вход восстановления по документу | Item.restoreReliability() | Делегирует RepairSystem без возвращения результата |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| repair() | this.actor/this, RepairSystem.process | Promise<void> | await process(this.actor,this) | Ждёт процесс до завершения диалога согласно вложенному контракту; ошибки распространяются. Не возвращает выбор кнопки и не добавляет проверок типа/владельца |
| restoreReliability() | this.system.repair должен существовать ниже по цепочке | undefined | RepairSystem.restoreReliability(this) | Не ждёт и не возвращает Promise записи; собственного контроля рецепта/ресурсов/прав нет |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| RepairSystem.process/restoreReliability | [module/item/systems/repair.js](../../../../../../../module/item/systems/repair.js) | Import/call | Импорт 1, вызовы 5/9 | Полный разбор; процесс ремонта отличается от прямого восстановления |
| WitcherItem.actor и system | [module/item/witcherItem.js](../../../../../../../module/item/witcherItem.js) | Контекст примеси | Ожидаемый this и установка прототипа 373 | Регистрация documentClass и Object.assign сверены |
| system.repair | [module/data/item/weaponData.js](../../../../../../../module/data/item/weaponData.js); [module/data/item/armorData.js](../../../../../../../module/data/item/armorData.js) | Косвенное делегирование | restoreReliability→RepairSystem→модель | Оружие reliable; броня reliability и 6 SP. Обе модели запускают parent.update без ожидания |
| Item.actor/update / Actor ownership | Foundry 14.367.0, общие и клиентские документы | Внешний контракт | Владелец/запись ниже по цепочке | Runtime — настоящие BaseItem/модели с update-фасадом; client WitcherItem не создавался |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/item/witcherItem.js](../../../../../../../module/item/witcherItem.js) | repairMixin | Импорт 6 и Object.assign373 | Прототип документа |
| [module/actor/sheets/WitcherCharacterSheet.js](../../../../../../../module/actor/sheets/WitcherCharacterSheet.js) | Item.repair | _repairItem442–446; обработчик .item-repair115 | Делегирование UI, сам лист не рассчитывает ремонт |
| [module/setup/socketHook.js](../../../../../../../module/setup/socketHook.js) | Item.restoreReliability | Активный GM разрешает UUID и вызывает разрешённый метод | Настоящий receiver проверен с документным фасадом |
| [module/setup/queries.js](../../../../../../../module/setup/queries.js) | Item.restoreReliability | Метод включён в callableEntityFunctions | Альтернативный generic query; штатный _doRepair использует сокет |

Область поиска: текущие module/ и templates/; регистрации сверены отдельно. Динамические обращения внешних модулей не исследовались.

## Данные и изменения состояния

Примесь собственных данных не хранит. repair открывает процесс на владельце Item; restoreReliability проходит непосредственно к записи модели. Ожидание repair не гарантирует завершение update/ChatMessage, потому что некоторые вложенные методы теряют Promise. Прямое restoreReliability не выполняет подбор компонентов, бросок или расчёт платы.

Кнопки инвентаря условно показываются через system.canBeRepaired в tab-inventory-weapons/armors; это отображение UI, а не проверка внутри примеси. Вызов на предметах с неподходящей моделью или без Actor не приобретает корректный контекст автоматически.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Подключение и UI | 12 строк, import и Object.assign; CharacterSheet/два inventory-HBS | Два разных входа принадлежат Item | Шаблоны инвентаря и лист целиком здесь не разбирались |
| Открытие | Настоящий repairMixin.repair на Item-фасаде | Создана ещё одна конфигурация DialogV2; отмена вернула управление | Диалог заменён; клики браузера не исполнялись |
| Восстановление | Настоящий restoreReliability и RepairSystem/WeaponData | Инициирован update reliable10; метод вернул undefined при pending update | Состояние/БД не изменялись |
| Удалённая связь | Настоящий socket sender/receiver и метод примеси | restoreReliability найден, вызван и передал восстановление модели | Объект передан в памяти; это не подтверждение доставки/записи |

## Непроверенные участки и открытые вопросы

В TASK-0004.007 текущие определения и потребители сопоставлены; прежние опыты TASK-0003.015/.016/.017 (2026-09-10) и .034 (2026-09-11) сохраняют собственные входы и фасады. Браузер, мир, сеть и запись в БД не запускались. Точные оставшиеся вопросы и ответственные блоки: [U007-02](../../../../cross-check-0002.md#u007-02), [U007-05](../../../../cross-check-0002.md#u007-05). Для этого файла установлены процессы R007-16, R007-19, а не полный клиентский lifecycle.

## Связанные проблемы

[issue-00081](../../../../../../issues/potential/issue-00081.md), [issue-00102](../../../../../../issues/potential/issue-00102.md), [issue-00103](../../../../../../issues/closed/issue-00103.md), [issue-00008](../../../../../../issues/potential/issue-00008.md), [issue-00010](../../../../../../issues/potential/issue-00010.md). 81 — раннее завершение нижних операций;102/103 блокируют обычный процесс. 8 — отдельный query,10 — общий receiver; это не дубликаты ошибок примеси.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.017 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.

## Сквозная сверка TASK-0004.007

2026-09-14; rusbar-main, 6a26042f7881d9990c304483c7219e0698f6617e. Исходник совпадает со срезом TASK-0001; изменено только описание.

repair() ожидает RepairSystem.process, restoreReliability() просто делегирует и не возвращает Promise. Это разные входы: основной ремонт имеет барьеры данных/настройки, прямое восстановление вызывает модель Item, включая получателя GM socket. Завершение wrapper не доказывает сохранение reliability/SP.

Сопоставленные определения и потребители: [module/item/systems/repair.js](../systems/repair.js.md), [module/item/witcherItem.js](../witcherItem.js.md), [module/data/item/weaponData.js](../../data/item/weaponData.js.md), [module/data/item/armorData.js](../../data/item/armorData.js.md), [module/actor/sheets/WitcherCharacterSheet.js](../../actor/sheets/WitcherCharacterSheet.js.md), [module/setup/socketHook.js](../../setup/socketHook.js.md), [module/setup/queries.js](../../setup/queries.js.md).

[Протокол и границы](../../../../review-log.md#task-0004007) — TASK-0004.007; процессы [R007-16](../../../../cross-check-0002.md#r007-16), [R007-19](../../../../cross-check-0002.md#r007-19). В этой порции выполнена статическая сверка; прежние опыты сохраняют свои даты и фасады. Единственный новый запуск N007-01 проверяет producer/HBS alchemyComponentsList на заданном контексте; его границы не распространяются на остальные процессы.
