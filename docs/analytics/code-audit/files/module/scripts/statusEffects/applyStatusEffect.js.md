# module/scripts/statusEffects/applyStatusEffect.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/scripts/statusEffects/applyStatusEffect.js](../../../../../../../module/scripts/statusEffects/applyStatusEffect.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `a33bf33add228ae93f96a52046c8feb4ee992921` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.009](../../../../../../tasks/task-0003.009.md), одна порция из восьми файлов |
| Запись перекрёстной сверки | [TASK-0003.009](../../../../review-log.md#task-0003009) |

## Назначение файла

Применяет статус по ID через Actor.toggleStatusEffect, передаёт запрос владельцу Actor, обрабатывает ссылки применения статуса в чате и вызывает необязательную интеграцию statuscounter.

## Условия использования

Ожидаются глобальные game, CONFIG, fromUuidSync и Actor API; для старого пакетного слушателя также $. Статусы определены в конфигурации системы и зарегистрированы в ядре. Этот маршрут отличается от WitcherActor.applyStatus: здесь используется toggleStatusEffect и собственная проверка иммунитета.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| Пять экспортируемых функций | 3–72; четыре function и одна const async | Пакетный и отдельный слушатели, действие клика, применение к целям/Actor | Именованные exports | Все описаны ниже |
| handleStatusCounterIntegration | Локальная функция; 74–84 | Настройка счётчика длительности | Не экспортируется | Вызывается после toggle до обработки иммунитета |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| addStatusEffectChatListeners; 3–13 | html, предполагающий одновременно DOM и jQuery API | undefined при успешном синхронном проходе | querySelector('.chat-message').each; оборачивает элемент в $, получает messageId, передаёт в chatMessageListeners | Несовместимые API; для DOM Element .each отсутствует. Внутренних вызовов export не найдено |
| chatMessageListeners; 15–21 | message (не используется), DOM html | Promise<undefined> | При наличии a.apply-status регистрирует click на каждом таком элементе | Нет снятия/защиты от повторной регистрации; callback не возвращает Promise onApplyStatus |
| onApplyStatus; 23–28 | event.currentTarget.dataset.status/duration | Promise<undefined> | Берёт getCurrentCharacter, вызывает применение по target.uuid | Не проверяет target и не ожидает применение |
| applyStatusEffectToTargets; 30–41 | Коллекция statusEffects с полем statusEffect у значений, duration | Promise<undefined> | Для каждого game.user.targets и Object.values(statusEffects) вызывает применение по Actor UUID | Пустые targets дают ранний выход; forEach без await; наличие target.actor не проверяется |
| applyStatusEffectToActor; 43–72 | actorUuid, statusEffectId, duration | Promise<undefined> | Нет Actor — выход; нет владения — query; иначе при непустом ID и отсутствии в appliedEffects переключает статус | await toggle; затем счётчик; затем при иммунитете setTimeout(toggle,1000). Нет catch; query и таймер не ожидаются |
| handleStatusCounterIntegration; 74–84 | target, statusId, duration | undefined | Пропускает выключенный модуль и falsy/нулевую duration; ищет статус/счётчик, setValue(parseInt(duration)), changeType(countdown_round) | querySelector вызван на массиве CONFIG.WITCHER.statusEffects; выполнение останавливается до EffectCounter |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| getActorOwner, getCurrentCharacter | [module/scripts/helper.js](../../../../../../../module/scripts/helper.js) | Два ES-import | Владелец для query; текущий персонаж для клика | getCurrentCharacter: первый controlled token.actor либо game.user.character; не набор targets и не диалог |
| Статусы системы и регистрация | [module/setup/config.js](../../../../../../../module/setup/config.js); [module/TheWitcherTRPG.js](../../../../../../../module/TheWitcherTRPG.js) | CONFIG.WITCHER.statusEffects / CONFIG.statusEffects | ID и определения для toggle, img для счётчика | Первый контейнер — массив; активное ядро использует зарегистрированные определения |
| Queries | [module/setup/queries.js](../../../../../../../module/setup/queries.js) | Динамический вызов по function | TheWitcherTRPG.query, data=[actorUuid,statusEffectId,duration] | Принимающий маршрут импортирует applyStatusEffectToActor |
| Actor.appliedEffects, toggleStatusEffect | Внешний /opt/foundryvtt/client/documents/actor.mjs | Чтение применимых эффектов и изменение embedded-документов | Проверка существования и переключение | toggle ищет существующий статус в this.effects, в том числе disabled; без active=true удаляет найденный |
| statusEffectImmunities | [module/data/actor/monsterData.js](../../../../../../../module/data/actor/monsterData.js) | Системное поле Actor | Если ID найден, планируется повторный toggle через 1000 ms | Поле объявлено у MonsterData; на остальных Actor код использует optional chaining |
| game.messages, DOM API, $, setTimeout | Внешние Foundry, браузер и jQuery | Слушатели, поиск сообщения, таймер | Пакетный export смешивает DOM/jQuery; актуальный hook передаёт DOM отдельного сообщения | Минимальные DOM/таймер doubles в проверке |
| EffectCounter, game.modules.get('statuscounter') | Внешний модуль /var/lib/foundryvtt/Data/modules/statuscounter | Необязательная интеграция | getAllCounters, поиск по path, setValue, changeType | Чтение каталога вернуло Permission denied; версия и реальный API модуля не установлены |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/TheWitcherTRPG.js](../../../../../../../module/TheWitcherTRPG.js) | chatMessageListeners | ApplyStatusEffects.chatMessageListeners при renderChatMessageHTML | Это фактический путь, без addStatusEffectChatListeners |
| [module/actor/mixins/castSpellMixin.js](../../../../../../../module/actor/mixins/castSpellMixin.js) | applyStatusEffectToActor / ToTargets | Эффекты заклинания на себя и цели, damage.duration | Соседний маршрут ActiveEffect вызывается отдельно |
| [module/actor/mixins/defenseMixin.js](../../../../../../../module/actor/mixins/defenseMixin.js); [module/actor/mixins/damageMixin.js](../../../../../../../module/actor/mixins/damageMixin.js) | applyStatusEffectToActor | staggered при защите и статусы полученного урона | Прямые импорты и вызовы |
| [module/setup/queries.js](../../../../../../../module/setup/queries.js) | applyStatusEffectToActor | Белый список общего query | Поиск владельца и выполнение на клиенте-получателе |
| [templates/chat/combat/spellItem.hbs](../../../../../../../templates/chat/combat/spellItem.hbs); [module/item/mixins/damageUtilMixin.js](../../../../../../../module/item/mixins/damageUtilMixin.js) | onApplyStatus через a.apply-status | Производители HTML-ссылок: dataset.status, у spellItem также duration | Делегирование через слушатель отдельного сообщения |
| Не найден в module/, templates/, packsJson/ | addStatusEffectChatListeners | Определение/export имеется, внутренних вызовов нет | Поиск точного имени; внешние модули/макросы не проверены |

## Данные и изменения состояния

Список appliedEffects используется для запрета повторного применения уже активного статуса. В этом случае длительность не продлевается, счётчик не обновляется. Корневое duration нового ActiveEffect этим кодом не задаётся: параметр duration используется интеграцией statuscounter. Выключенный статус в this.effects может отсутствовать в appliedEffects; core toggle при этом удаляет его. Это не эквивалент команды «включить».

Иммунитет обрабатывается после первичного toggle: через секунду код пытается переключить статус обратно. Ошибка счётчика прерывает путь раньше постановки таймера. При выключенном statuscounter воспроизведены один начальный toggle и таймер 1000 ms; при включённом с duration=2 — один toggle и ошибка querySelector, без таймера.

Клик берёт Actor выделенного управляемого токена либо назначенного персонажа пользователя, а не автора сообщения и не targets. data.duration приходит строкой из HTML; явное преобразование в число есть только внутри счётчика.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Полнота | Полное чтение 84 строк, поиск импортов, имён экспортов и a.apply-status | 6 функций; пакетный export не является текущим hook чата | Соседние файлы просмотрены по связанным определениям |
| Основные ветви | Исходные функции; fromUuidSync, Actor API, таймер, query подменены | Нет Actor/ID — нет toggle; активный статус — нет toggle; новый — один; иммунитет — таймер повторного | Не реальный клиент |
| Отключённый статус | Исходный core toggleStatusEffect 14.367 с наблюдаемым deleteEmbeddedDocuments | Удаляет disabled-fire при попытке applyStatusEffectToActor | Список appliedEffects задан явно; БД не используется |
| Чат | Минимальный DOM с регистрацией click; getCurrentCharacter без выбранного/назначенного Actor | Отдельный слушатель регистрируется; действие клика читает uuid у undefined; пакетный слушатель падает на .each | Браузер, повторный рендер и внешние макросы не запускались |
| statuscounter | CONFIG системы, active=true, duration='2', статус с иммунитетом | querySelector is not a function; таймеров иммунитета 0 | Сам модуль недоступен для чтения; его EffectCounter не вызывался |

## Непроверенные участки и открытые вопросы

API и версия statuscounter, реальные таймеры нескольких клиентов и сохранение статуса в мире не проверены. Не утверждается, что ошибка пакетного export ломает штатный renderChatMessageHTML. Шаблон statusEffect.hbs из этой порции не содержит a.apply-status и не является источником команды применения.

## Связанные проблемы

[issue-00003](../../../../../../issues/potential/issue-00003.md) — массив и счётчик; [issue-00008](../../../../../../issues/potential/issue-00008.md) — ожидание Queries; [issue-00047](../../../../../../issues/potential/issue-00047.md) — Actor для клика; [issue-00048](../../../../../../issues/potential/issue-00048.md) — пакетный слушатель; [issue-00049](../../../../../../issues/potential/issue-00049.md) — отключённый статус. [issue-00031](../../../../../../issues/potential/issue-00031.md) относится к другому методу WitcherActor.applyStatus, не к этой функции.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.009 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.

## Уточнение TASK-0003.028

2026-09-11, `9f16a7ae4bc942df85a105fd37d9a3cb3ef99f4b`: onApplyStatus использует getCurrentCharacter без диалога выбора; applyStatusEffectToActor при !actor.isOwner вызывает getActorOwner(actor).query. Полный helper и настоящий метод потребителя с фасадами показали TypeError при отсутствии активного OWNER и activeGM. Это [issue-00185](../../../../../../issues/potential/issue-00185.md), отдельная от [issue-00008](../../../../../../issues/potential/issue-00008.md) о результате уже отправленного query. Источники текущего Actor и получатель запроса — разные операции.

Полные карточки зависимости: [module/scripts/helper.js](../helper.js.md). [Перекрёстная сверка](../../../../review-log.md#task-0003028). Это уточнение связи; исходный файл не изменён.

## Дополнительная сверка TASK-0003.039

2026-09-11, `c598d74e34f4be51535de78b38f0601c286c5407`; исходники не менялись.

Собственные эффекты castSpell обходятся Object.values, onCastEffects передаётся целиком. Группы 20–24: dictionary self применяется без вывода ссылки; нет целей→ранний выход; цель+undefined у ritual/hex→TypeError. Ручная a.apply-status использует getCurrentCharacter при клике. Statuscounter не включался; прежняя issue-00003 остаётся отдельным ограничением.

[module/actor/mixins/castSpellMixin.js](../../../../../../../module/actor/mixins/castSpellMixin.js) — [карточка](../../actor/mixins/castSpellMixin.js.md); [templates/chat/combat/spellItem.hbs](../../../../../../../templates/chat/combat/spellItem.hbs) — [карточка](../../../templates/chat/combat/spellItem.hbs.md).

[Сценарии, методика и пределы проверки](../../../../review-log.md#task-0003039). Соседние определения проверены в пределах связи; это не расширяет состав шести полностью разобранных файлов.
