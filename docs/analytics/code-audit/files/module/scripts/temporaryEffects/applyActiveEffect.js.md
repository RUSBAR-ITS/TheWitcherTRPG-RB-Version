# module/scripts/temporaryEffects/applyActiveEffect.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/scripts/temporaryEffects/applyActiveEffect.js](../../../../../../../module/scripts/temporaryEffects/applyActiveEffect.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `a33bf33add228ae93f96a52046c8feb4ee992921` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.009](../../../../../../tasks/task-0003.009.md), одна порция из восьми файлов |
| Запись перекрёстной сверки | [TASK-0003.009](../../../../review-log.md#task-0003009) |

## Назначение файла

Маршрутизирует применение эффектов по целям или UUID Actor/Item: отделяет временные улучшения оружия, копирует обычные ActiveEffect в Actor и передаёт операции клиенту владельца через Queries.

## Условия использования

Доступны fromUuidSync, game.user.targets, game.users, ui.combat, ActiveEffect и зарегистрированные Queries. Входные activeEffects ожидаются массивом документов либо данных; соответствие этих форм длительности неодинаково в Foundry 14.367. Признаки applyWhen выбирают эффекты предмета, но не проверяют disabled. Код не изменяет численные характеристики напрямую.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| applyActiveEffectToTargets, applyActiveEffectToActorViaId, applyActiveEffectToActor | Три именованных async export; 3–68 | Общедоступные маршруты | Импортируются в mixin-файлах и queries | См. таблицу методов |
| applyTemporaryItemImprovements | Локальная async-функция; 70–80 | Разделение по владельцу | Не экспортируется | Вызывает метод Actor или отдельный query |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| applyActiveEffectToTargets; 3–12 | activeEffects, duration; game.user.targets | Promise<undefined> | При пустом наборе выходит, иначе для каждого target.actor.uuid вызывает основной маршрут | forEach без await; отсутствие actor у Token не проверяется; завершение не означает записи |
| applyActiveEffectToActorViaId; 14–30 | actorUuid, itemUuid, имя флага applyWhen, duration | Promise<undefined> | fromUuidSync Item; при наличии фильтрует effect.system[applyWhen]; при отсутствии отправляет тот же вызов activeGM | Не await вызов/query; нет условия прекращения повторной пересылки и проверки activeGM |
| applyActiveEffectToActor; 32–68 | actorUuid, activeEffects, duration; существующий Actor | Promise<undefined> | Пишет duration.rounds во входные эффекты, отдельно запускает улучшения; у владельца клонирует обычные эффекты в Actor | await только actor.createEmbeddedDocuments; временная ветка и remote query не ожидаются; catch нет |
| applyTemporaryItemImprovements; 70–80 | actor, все activeEffects | Promise<undefined> | У владельца actor.applyTemporaryItemImprovements; иначе отдельный query TheWitcherTRPG.applyTemporaryItemImprovements | Не фильтрует список и не ожидает конечное действие; фильтрация выполняется методом Actor |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| getActorOwner | [module/scripts/helper.js](../../../../../../../module/scripts/helper.js) | Прямой ES-import | Выбор получателя Queries при !actor.isOwner | 61–71: первый активный не-GM с OWNER при hasPlayerOwner, иначе activeGM; отсутствие получателя отдельно не обработано |
| fromUuidSync, ActiveEffect, clone, createEmbeddedDocuments | Внешнее ядро Foundry; /opt/foundryvtt/common/abstract/document.mjs и common/documents/active-effect.mjs | Разрешение UUID, создание и копирование | Сохранение обычных эффектов под Actor | clone читает toObject источника; фактические тела проверены |
| applyTemporaryItemImprovements | [module/actor/mixins/temporaryEffectMixin.js](../../../../../../../module/actor/mixins/temporaryEffectMixin.js); регистрация [module/actor/witcherActor.js](../../../../../../../module/actor/witcherActor.js) | Динамический метод Actor | Выбор оружия и создание его эффектов | Object.assign прототипа Actor |
| Маршруты query | [module/setup/queries.js](../../../../../../../module/setup/queries.js) | Строковое имя и payload | TheWitcherTRPG.query с function/data; отдельный TheWitcherTRPG.applyTemporaryItemImprovements | Обе принимающие ветви прочитаны; promise операции не возвращают |
| WitcherActiveEffect, две модели system | [module/activeEffect/witcherActiveEffect.js](../../../../../../../module/activeEffect/witcherActiveEffect.js); [module/data/activeEffects/witcherActiveEffectData.js](../../../../../../../module/data/activeEffects/witcherActiveEffectData.js); [module/data/activeEffects/witcherTemporaryItemImprovementData.js](../../../../../../../module/data/activeEffects/witcherTemporaryItemImprovementData.js) | Через регистрацию ядра | Флаги применения, выбор типа, hooks копии | Обычный эффект сохраняет changes; временные улучшения идут отдельным путём |
| game.user.targets, game.users.activeGM, ui.combat.combats | Внешние коллекции Foundry | Глобальные обращения | Цели, GM и первый isActive Combat | UI/сеть заменены наблюдаемыми объектами в проверке |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/TheWitcherTRPG.js](../../../../../../../module/TheWitcherTRPG.js) | applyActiveEffectToActorViaId | Публикация в game.api | Импорт и объект публичного API |
| [module/item/mixins/consumeMixin.js](../../../../../../../module/item/mixins/consumeMixin.js) | applyActiveEffectToActorViaId | Применение applySelf при использовании Item | Вызов с actor.uuid и item.uuid |
| [module/actor/mixins/castSpellMixin.js](../../../../../../../module/actor/mixins/castSpellMixin.js) | applyActiveEffectToActor / ToTargets | Эффекты applySelf и applyOnTarget после успешного пути заклинания; damage.duration | 253–267; параллельно применяются статусы |
| [module/actor/mixins/defenseMixin.js](../../../../../../../module/actor/mixins/defenseMixin.js); [module/actor/mixins/damageMixin.js](../../../../../../../module/actor/mixins/damageMixin.js) | applyActiveEffectToActorViaId | applyOnHit при попадании; applyOnDamage при уроне | Вызовы с UUID предмета и длительностью |
| [module/actor/mixins/professionMixin.js](../../../../../../../module/actor/mixins/professionMixin.js) | applyActiveEffectToActor | Динамически через общий query | function: applyActiveEffectToActor и созданный ActiveEffect |
| [module/setup/queries.js](../../../../../../../module/setup/queries.js) | applyActiveEffectToActor / ViaId | Белый список функций общего query | Импорт и вызов обработчика по function |

## Данные и изменения состояния

Маршрут Actor сначала выполняет `effect.duration.rounds = duration ?? effect.duration.rounds` для всего входа. В Foundry 14.367 современная схема — `duration.value/units/expiry/expired`; запись rounds у живой модели не попадает в _source. У данных из toObject legacy rounds — getter без setter, у JSON-копии это уже обычное добавленное свойство. Формы входа дают разные результаты; см. issue-00044.

При отсутствии владельческих прав уходят два запроса: улучшения получают весь список; общий query — только типы, отличные от temporaryItemImprovement. В data общего query входят actorUuid и список, отдельный duration отсутствует.

У владельца вход без метода clone превращается в new ActiveEffect. Затем clone задаёт parent=actor, false для четырёх apply-флагов и старый путь duration.combat. Остальные данные копируются по правилам ядра, в том числе changes, disabled, origin и start; собственный код не задаёт новый origin и не включает отключённый эффект. Корневой transfer определяется также hooks ядра при создании. Вызов createEmbeddedDocuments выполняется даже для пустого списка обычных эффектов.

Копирование не объединяет записи по имени/источнику и не содержит собственной политики повторного получения. Применимость и последующие расчёты выполняются документами ядра; отдельного хранения вычисленных бонусов здесь нет.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Полнота маршрутов | Полное чтение 80 строк, поиск всех трёх export в module/templates/packsJson | 3 экспортируемых и 1 локальная async-функция; перечислены прямые и query-потребители | Тела соседних mixin-файлов прочитаны по местам вызова |
| Длительность | Исходный ES-модуль, настоящие BaseActiveEffect/модели/clone/toObject 14.367, подмена Actor и записи | При исходных 5 rounds запрошенные 0/2 оставляют копию с value=5; прямой toObject вызывает ошибку setter; JSON-данные с value=5 тоже сохраняют 5 | Не выполнялись клиентские hooks сохранения и запись БД |
| Асинхронность | Отложенный createEmbeddedDocuments и журнал query-вызовов | Прямой owned-маршрут ждёт обычную запись; ToTargets/ViaId и temp-ветка возвращаются раньше; remote даёт два запроса | Нет проверки реального обмена между клиентами |
| Нет Item | Три ручных исполнения входящего ViaId с всегда отсутствующим UUID | Каждый снова отправляет тот же запрос GM | Реальный бесконечный цикл не запускался |

## Непроверенные участки и открытые вопросы

Сериализация реальных сетевых сообщений, права нескольких клиентов и отключение получателя не проверялись. Ошибка прямого toObject установлена для этой формы аргумента, а не для всех данных из query. Настоящее сохранение/истечение эффекта в мире и весь UI остаются непроверенными.

## Связанные проблемы

[issue-00044](../../../../../../issues/potential/issue-00044.md) — длительность копии; [issue-00045](../../../../../../issues/potential/issue-00045.md) — повторная пересылка отсутствующего Item; [issue-00008](../../../../../../issues/potential/issue-00008.md) — завершение Queries и вложенных операций. Ветвь оружия: [issue-00042](../../../../../../issues/potential/issue-00042.md), [issue-00046](../../../../../../issues/potential/issue-00046.md), [issue-00050](../../../../../../issues/potential/issue-00050.md).

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.009 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.

## Уточнение TASK-0003.015

2026-09-10, `7edb814aa870da75c7ad7633536e899a8d07e205`; исходник неизменен. [Перекрёстная сверка](../../../../review-log.md#task-0003015).

Полностью проверен [module/item/mixins/consumeMixin.js](../../../../../../../module/item/mixins/consumeMixin.js), прямой caller applyActiveEffectToActorViaId(actor.uuid,item.uuid,'applySelf') без duration. Из двух настоящих BaseActiveEffect helper отобрал applySelf=true и сформировал копию со сброшенными флагами применения; duration.value=3 сохранилась. Текстовые time/toxicity Item не участвуют в этом вызове. При quantity1 и задержанном лечении Actor.removeItem удалил UUID источника из фасада до helper; перехвачен один запрос GM, локального createEmbeddedDocuments не было. Удалённый обработчик и повторная доставка не запускались; связь с issue-00045 уточнена без имитации сети.

## Уточнение TASK-0003.028

2026-09-11, `9f16a7ae4bc942df85a105fd37d9a3cb3ef99f4b`: getActorOwner выбирает первого активного не-GM с OWNER при hasPlayerOwner, иначе activeGM; результат может отсутствовать. Вызовы query:41/72 не имеют guard получателя — смежные места [issue-00185](../../../../../../issues/potential/issue-00185.md). В .028 непосредственно исполнен аналогичный маршрут applyStatusEffectToActor; создание/клонирование ActiveEffect и удалённые запросы здесь повторно не исполнялись.

Полные карточки зависимости: [module/scripts/helper.js](../helper.js.md). [Перекрёстная сверка](../../../../review-log.md#task-0003028). Это уточнение связи; исходный файл не изменён.
