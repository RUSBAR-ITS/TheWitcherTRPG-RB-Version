# module/data/item/mixin/spellRegionMixin.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/data/item/mixin/spellRegionMixin.js](../../../../../../../../module/data/item/mixin/spellRegionMixin.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `ef8117ba6e5a184989e65761d47a068381056e4a` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.022](../../../../../../../tasks/task-0003.022.md), 5 файлов, 289 логических строк |
| Запись перекрёстной сверки | [TASK-0003.022](../../../../../review-log.md#task-0003022) |

## Назначение файла

Примесь жизненного цикла областей spell/ritual: построение Region-данных, интерактивное размещение либо привязанная к токену эманация, назначение макросов и планирование удаления через клиентский таймер.

## Условия использования

SpellData и RitualData присоединяют экспорт spellRegionMixin через Object.assign. Actor.castSpell вызывает createSpellRegion(roll, damage,{stamina: origStaCost}) после сообщения броска; ожидания результата и проверки fumble перед этим вызовом нет. Сам импорт не создаёт регион.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| spellRegionMixin | export let object; 1–176 | Четыре метода модели Item | Прототипы SpellData/RitualData | Динамический this — system-модель |
| regionData | Объект 29–52 | Данные для placeRegion/createTokenEmanation | Локальный payload | name, uuid, user, color, shapes, elevation, restriction, behaviors, visibility, displayMeasurements, locked, ownership, flags |
| flags.TheWitcherTRPG | 43–50 | Связь области с применением магии | roll, item, itemUuid, duration, actorUuid, options | Вход содержит сами roll/Item-объекты и UUID; факт сериализации БД не проверен |
| templateSize, gridBased, x, y, direction, shape | 54–60 | Геометрия в пикселях | Локальные значения | size × grid.size/grid.distance; gridBased=!isGridless; начальные x/y/direction=0 |
| circle / cone / rect / ray / emanation | switch61–113 | Пять поддерживаемых типов | circle, cone, rectangle, line; emanation отдельным API | Пустой/неизвестный тип возвращает null |
| regions; region.item/actorSheet | 117–139 | Результаты создания и дополнительные ссылки | Возвращаемый массив | Добавляются в память после создания; отсутствующий документ не отфильтрован |
| then/catch; timer callback | 8–15, 170–172 | Продолжение и отложенное удаление | Promise-цепочка и setTimeout | Цепочка не возвращается; ошибки поглощаются; таймер не хранится |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| async createSpellRegion(roll, damage, options) | templateProperties и parent Item | Promise<undefined> | Guard createTemplate/type/size → fromItem → await addBehaviorsToRegions → deleteSpellVisualEffect → пустой catch | Не возвращает/ожидает цепочку; options передаётся под именем, отличным от flagOptions; отрицательный size truthy |
| async fromItem(item,{roll, damage, flagOptions={}}) | Item с parent/actor; активный canvas.scene.grid; второй объект обязателен | Promise массива регионов / null либо отказ | Формирует flags/shapes; для emanation собирает зависимые токены, иначе вызывает drawPreview; затем добавляет item/actorSheet | Обычная ветвь передаёт Promise в Promise.all; неподдерживаемый тип сообщает undefined вместо ключа; нет guards для отсутствующего parent/grid |
| async drawPreview(regionData) | canvas.regions и приложения | Promise<RegionDocument\|null\|undefined> по core API | minimize всех приложений; await legend.close если доступна; await placeRegion({create: true}) | catch охватывает только placeRegion, возвращает null и при отмене, и при ошибке. Приложения не восстанавливает; minimize не ожидается |
| async deleteSpellVisualEffect(regions) | templateProperties.visualEffectDuration; game.user | Promise<undefined> после планирования | Не-GM пытается query; при положительном времени планирует setTimeout по каждому региону | В player-ветви item не определён; таймер использует будущую canvas.scene и region.id, не region.parent; Promise удаления не ожидает |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| TemplateProperties | [module/data/item/templates/regions/templatePropertiesData.js](../../../../../../../../module/data/item/templates/regions/templatePropertiesData.js) | Поля модели | Четыре поля в guard/геометрии/таймере | Схема разобрана целиком |
| RegionProperties.addBehaviorsToRegions | [module/data/item/templates/regions/regionPropertiesData.js](../../../../../../../../module/data/item/templates/regions/regionPropertiesData.js) | Вызов | Продолжение createSpellRegion | Сам метод завершается до update |
| query | [module/setup/queries.js](../../../../../../../../module/setup/queries.js) | RPC-контракт | deleteSpellVisualEffect | Имя отсутствует в allowlist; ошибка item возникает ещё до отправки |
| canvas.scene.grid/dimensions; game.user.id/color/viewedScene; CONST.REGION_VISIBILITY/DOCUMENT_OWNERSHIP_LEVELS | Foundry 14.367.0, client/documents/scene.mjs: 507; user.mjs: 47–51; common/constants.mjs | Глобальные данные | Построение Region и фильтр эманации | viewedScene — ID; distancePixels=grid.size/grid.distance |
| Actor.getDependentTokens; TokenDocument.scene | Foundry 14.367.0, client/documents/actor.mjs: 584–616; token.mjs: 105–107 | Внешние методы/геттер | Выбор токенов эманации | Реальный getDependentTokens возвращает TokenDocument[] всех зависимых сцен; scene — объект parent |
| RegionDocument.createTokenEmanation | Foundry 14.367.0, client/documents/region.mjs: 1306–1337 | Внешнее создание | range=size/2/grid.distance; regionData | Настоящее тело метода с façade create; API использует target-scene distancePixels, attachment и levels |
| RegionLayer.placeRegion; legend.close; ApplicationV2.minimize | Foundry 14.367.0, client/canvas/layers/regions.mjs: 598–781, 1162–1206; client/applications/api/application.mjs | Внешний preview/UI | drawPreview | placeRegion возвращает один Region/null, не Iterable; запрет прав доступа может бросить исключение; preview/DOM заменены |
| Region/Scene.deleteEmbeddedDocuments; setTimeout | Foundry 14.367.0 Region/Scene API; JavaScript Promise/timer | Запись/таймер | Создание/удаление | Создания, удаления и таймеры в опытах подменены; реальное ожидание времени не запускалось |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/data/item/spellData.js](../../../../../../../../module/data/item/spellData.js) | spellRegionMixin | Импорт и Object.assign | 3, 137 |
| [module/data/item/ritualData.js](../../../../../../../../module/data/item/ritualData.js) | spellRegionMixin | Импорт и Object.assign | 5, 91 |
| [module/actor/mixins/castSpellMixin.js](../../../../../../../../module/actor/mixins/castSpellMixin.js) | createSpellRegion | Передаёт roll/damage/options после toMessage | 250 |
| [module/scripts/regions/regionHooks.js](../../../../../../../../module/scripts/regions/regionHooks.js) | flags.duration/actorUuid | Второй механизм удаления на updateCombat | 4–17 |
| [module/setup/queries.js](../../../../../../../../module/setup/queries.js) | deleteSpellVisualEffect, предполагаемый маршрут | Запрос не разрешён | Сверка allowlist, issue9 |

Область поиска: module/ и templates/ текущего checkout; регистрация сверена с system.json. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Обычные shapes: circle(radius=sizePx); cone(radius=sizePx, angle90, rotation0, curvature flat); rect→rectangle(width=height=sizePx, anchorX/Y0, rotation0); ray→line(length=sizePx, width=grid.size, rotation0). Все начинают с x=y=0; пользовательское размещение/поворот выполняет ядро. При неизвестном типе console.error выводит переменную shape (undefined).

regionData задаёт color пользователя либо #ff0000, elevation{bottom: 0, top: null}, restriction{enabled: false, type: move, priority: 0}, пустые behaviors, visibility ALWAYS, displayMeasurements=true, locked=false, default ownership NONE. uuid/user передаются в payload, но в просмотренной схеме BaseRegion самостоятельных полей uuid/user нет; их сохранение не утверждается. flags.duration берётся из damage?.duration, actorUuid — из item.parent.uuid, options — из flagOptions. createSpellRegion передаёт options, поэтому этот последний объект теряется.

Эманация строится по токенам item.actor: фильтр token.scene!==game.user.viewedScene сравнивает Scene с ID и не ограничивает результаты ожидаемой сценой. API createTokenEmanation получает size/2/grid.distance, сам заменяет shapes/elevation, задаёт attachment.token и levels, по умолчанию gridBased=false. Возвращённый undefined при запрете создания затем ломает region.item. Массивы/ссылки существуют в памяти; реальная сериализация flags и сохранение не подтверждены.

Секундный таймер и countdownDurationOfRegions независимы. У таймера нет сохранённого ID/повторной регистрации после перезагрузки страницы; код не отменяет его при досрочном удалении. Это описание реализации, не решение о требуемой политике длительности.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Guard/асинхронность/геометрия | Группы 06–10 | Отключение, пустой тип и 0 не запускают fromItem. Все 4 обычные формы построены верно по входной формуле, затем Promise.all от Promise даёт TypeError. Запущенный preview может завершиться позже; продолжения behaviors/таймера не происходят | Настоящие методы, façade canvas; никакого размещения в мире |
| Эманация | Группы 11–13; исходные методы ядра | Два токена двух сцен проходят фильтр. При size10/активной distance5 радиус 20px; смена лишь активной distance на 10 уменьшает радиус того же токена до 10px. core API задаёт attachment/levels; options через внешний вызов потерян; undefined создания даёт TypeError | Региональные create заменены, геометрия вычисляется настоящим телом ядра |
| Удаление | Группы 05, 14 | Не-GM получает ReferenceError item; GM планирует 2000 мс, смена canvas.scene адресует другую сцену; отсутствие сцены вызывает TypeError | Таймер вызван вручную, delete — журнал аргументов |

## Непроверенные участки и открытые вопросы

Все 176 строк прочитаны. Не выполнялись реальное рисование, поворот мышью, сохранение Region/flags, сериализация Item/Roll, политика уровней сцены, перезагрузка таймеров, несколько клиентов и исполнение макросов. Сравнение геометрии устанавливает зависимость от сцены; игровой выбор радиуса/диаметра остаётся несогласованным.

## Связанные проблемы

[issue-00009](../../../../../../../issues/potential/issue-00009.md), [issue-00128](../../../../../../../issues/potential/issue-00128.md), [issue-00129](../../../../../../../issues/potential/issue-00129.md), [issue-00138](../../../../../../../issues/potential/issue-00138.md), [issue-00139](../../../../../../../issues/potential/issue-00139.md), [issue-00140](../../../../../../../issues/potential/issue-00140.md), [issue-00141](../../../../../../../issues/potential/issue-00141.md), [issue-00142](../../../../../../../issues/potential/issue-00142.md), [issue-00143](../../../../../../../issues/potential/issue-00143.md), [issue-00144](../../../../../../../issues/potential/issue-00144.md), [issue-00146](../../../../../../../issues/potential/issue-00146.md). 9 — обмен с GM; 128/129 — входные данные/форма.138 — Promise.all; 139 — потеря options; 140/141 — сцены и размер эманации; 142 — завершение/ошибки; 143 — отменённое создание; 144 — сцена срока жизни; 146 — пустая duration у потребителя.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `ef8117ba6e5a184989e65761d47a068381056e4a`; полный файл | Первая карточка; [сверка порции](../../../../../review-log.md#task-0003022) |

## Дополнительная сверка TASK-0003.039

2026-09-11, `c598d74e34f4be51535de78b38f0601c286c5407`; исходники не менялись.

В полном castSpell createSpellRegion вызван после await сообщения, до проверки fumble, без await и с {stamina:origStaCost}. Группы 28/32 подтвердили цену до фокуса и сохранение пустого flags.options из-за options/flagOptions. Настоящий fromItem circle попал в прежнюю ошибку Promise.all(Promise), поглощённую createSpellRegion; placeRegion был фасадом.

[module/actor/mixins/castSpellMixin.js](../../../../../../../../module/actor/mixins/castSpellMixin.js) — [карточка](../../../actor/mixins/castSpellMixin.js.md).

[Сценарии, методика и пределы проверки](../../../../../review-log.md#task-0003039). Соседние определения проверены в пределах связи; это не расширяет состав шести полностью разобранных файлов.
