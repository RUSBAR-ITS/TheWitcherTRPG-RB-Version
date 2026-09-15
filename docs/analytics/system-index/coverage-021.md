# TASK-0006.021 — Критические травмы и переходы между Item

2026-09-15; rusbar-main, исходный HEAD `33b48126984ca2420f8d027ab0a49475710d23ac`; рабочее дерево в начале чистое. [Задача](../../tasks/task-0006.021.md).

## Область и остаток

Семь основных исходников и выбранные смежные участки. Схема v1 и CLI сохранены; покрытие справочника partial. Здесь описана текущая реализация, без изменения правил или исполнения игрового сценария.

| Источник | Включено и границы |
| --- | --- |
| [module/actor/mixins/damageMixin.js](../../../module/actor/mixins/damageMixin.js) (src-000014) | Добавлены полные критические входы и независимый Actor.calculateHealingTime; .019 damage сохранён. Произвольные сторонние callers, данные pack и запись мира не проверены. |
| [module/data/item/criticalWoundData.js](../../../module/data/item/criticalWoundData.js) (src-000112) | Весь класс, девять полей, prepared срок, enrichedText, heal/treat и getter. Core lifecycle/фактическое сохранение и произвольные UUID остаются внешними. |
| [module/item/sheets/WitcherCriticalWoundSheet.js](../../../module/item/sheets/WitcherCriticalWoundSheet.js) (src-000167) | Весь специализированный класс: options/PARTS/Drop. Общие контекст/форма/configuration переиспользуют .012; живой UI не исполнялся. |
| [module/actor/sheets/mixins/criticalWoundMixin.js](../../../module/actor/sheets/mixins/criticalWoundMixin.js) (src-000038) | Весь mixin: add/treat/listener/три callback; отсутствующий remove-метод отмечен без выдуманного пользовательского пути. |
| [templates/partials/crit-wounds-table.hbs](../../../templates/partials/crit-wounds-table.hbs) (src-000530) | Весь partial: список, идентификаторы, подписи/дни и treat; общий editor .013, второй список соседней вкладки отделён. |
| [templates/sheets/item/criticalWound-sheet.hbs](../../../templates/sheets/item/criticalWound-sheet.hbs) (src-000599) | Весь main HBS и поля; inherited submit — явная граница, стерилизация не выведена. |
| [styles/crit-wounds-table.css](../../../styles/crit-wounds-table.css) (src-000455) | Статическое соответствие selectors трём выбранным HBS и размеры полей. Браузерный cascade/все внешние использующие классы не проверены. |

## Контракты и маршруты

- Три действия критического сообщения независимы: applyCritDamage, applyBonusCritDamage, applyCritWound получают message.system.crit из прежнего proc-000210. Первые два вызывают applyDamage без await: DamageInstance без type, torso/hp, bypass двух броней, но не щита. Обработка урона и эффектов остаётся маршрутом .019.
- applyCritWound использует Item pack из criticalWoundsPack. Ready.getIndex заранее запросил criticalLevel/location/lesserEffect/treatment (.006); настройка допускает любой Item pack, не проверяет subtype. Два filter выбирают location.name/criticalLevel, ещё один — treatment none. Единственный кандидат берётся без lesserEffect. Иначе явный location.critEffect либо getRandomInt(6)+critEffectModifier определяет first find: >4 → lesserEffect false, иначе true. Guard pack/кандидата/UUID нет; пустой/множественный набор не превращён в надёжную таблицу.
- raw critEffectModifier производителя не объявлен DefenseMessageData.crit; location.modifier является другим полем. Если critEffect отсутствует и modifier undefined, сумма NaN идёт в else. Head/torso могут иметь явный critEffect; руки/ноги — отдельная ветвь .016. Чтение схемы не выдаётся за новое выполнение Foundry cleaning.
- После await fromUuid вызывается addItem без await, затем создаётся сообщение с сырыми name/description. addItem .013 ищет первое совпадение name/type. Без force и если Item не stored запросит quantity=Number(old)+Number(1); у травмы quantity не объявлен. Это не политика сброса состояния при повторе. Разные имена стадий не совпадают. Успех сообщения не доказывает завершение создания Item.
- CriticalWoundData определяет девять полей: description, criticalLevel, treatment, location, lesserEffect, daysHealed, healingTime, sterilized, followUp. ID/name/img/effects находятся в документе Item. NumberField дней не имеет min/integer; строки степени/состояния/локации не являются enum схемы. DocumentUUIDField ограничивает документ Item, а не подтип/существование/цикл переходов. Старое export htmlFields не добавлено к схеме.
- Два calculateHealingTime принадлежат разным владельцам. Actor helper возвращает max(8/12/15−BODY.max,1); прямой caller в module не найден. Модель записывает то же в prepared healingTime при prepareDerivedData и наличии parent.parent. Это не запись healingTime в источник. Deadly/unknown у Actor возвращают undefined, у модели оставляют прежнее значение. Используется BODY.max, не value; весь порядок финальных эффектов этим не утверждается.
- Ручное добавление создаёт Item с локализованным именем и type criticalWound без await, без выбора компедиума. Listener регистрирует add/treat/remove callbacks. Метод _onCriticalWoundRemove в module не найден, но выбранные HBS не выводят .delete-crit; доступный ошибочный клик не выдуман. Кнопка лечения передаёт UUID через event.target.dataset.id; fromUuidSync и crit.system.treat не защищены от отсутствия документа/метода.
- WitcherCriticalWoundSheet наследует ItemSheetV2-контекст/форму и общий Drop. isEditable и тип документа проверяются до override; _onDropItem сохраняет item.uuid в system.followUp без await/return, не проверяя criticalWound subtype. PARTS.main и DEFAULT_OPTIONS выделены отдельно; поля формы сохраняет inherited submitOnChange. В форме нет управления sterilized; healingTime disabled, дни редактируемы.
- Partial выводит documentsByType.criticalWound: локальный Item ID для общего inline editor .013, UUID для treat, config labels, daysHealed и disabled healingTime. Inline writer использует строковое input.value (кроме Boolean); преобразование схемы остаётся границей. tab-effects включает partial и второй собственный список тех же Items. Повтор строки UI не означает второй Item. Обогащение description идёт через createEnrichedText → enriched/value/systemField и прежний Actor context.
- heal сначала только при treatment treated увеличивает prepared daysHealed на1. Если вход sterilized truthy и this.sterilized false — ещё +2 и updates.system.sterilized=true; prepared флаг не меняется напрямую. Порог daysHealed>=healingTime проверяется вне treated. Deadly запрещает только автоматический treat. При пороге вызывается treat без await, накопленные updates не отправляются; иначе Object.keys(updates) truthy даже для {}, и parent.update запущен без await.
- treat при непустой followUp ожидает только fromUuid. Затем actor.createEmbeddedDocuments(Item,[followUpItem]) запускается без await и без проверки результата, после него — parent.delete без await. При пустой ссылке сразу удаляется исходный Item. Reject разрешения UUID останавливает до удаления; null не имеет собственного guard. Это не атомарная замена и не перенос days/sterilized/location/effects: новый документ приносит свои данные. Ручной treat не проверяет treatment/степень, в том числе deadly.
- Удаляется Item вместе с его embedded effects. Отдельно скопированные Actor.effects этот метод не ищет. Обычные переносимые эффекты используют прежнюю Actor/ActiveEffect цепочку .008; location/treatment сами по себе не выбирают change keys. Getter canHaveTemporaryItemImprovement=false скрывает только создание temporaryItemImprovement в effect-part, не отменяет обычные эффекты.
- В recoverActor выбран только callback forEach: после await ресурсной записи Actor вызывается crit.system.heal({sterilized:isSterilized}) без ожидания Promise. Полная логика отдыха/регенерации и сообщения — .022. Граница callback сохранена, завершение всех травм до сообщения не утверждается.
- CSS сопоставлен с текущими div/ol/li и обоими представлениями. Старые .crit-wounds-table/tbody/tr и часть имён не совпадают с выбранными шаблонами. Ширина40px для days/healing не ограничивает значения. Cascade браузера не исполнялся; классы/орфография существующего кода сохранены.

## Техническая цепочка экспорта

Прочитаны только три файла одной цепочки Sprained Leg (Left): none → stabilized → treated → пустая followUp. Это технические свидетельства UUID/Item/embedded ActiveEffect; fromUuid читает действующий документ, не JSON в packsJson. Совпадение pack с экспортом не доказано. Определения всех экспортов в справочник не добавлены.

| Экспорт | Свидетельство |
| --- | --- |
| [Sprained_Leg__Left__XPoH413WkKQUgrnw.json](../../../packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Sprained_Leg__Left__XPoH413WkKQUgrnw.json) | none; followUp → stabilized, SPD/dodge/athletics −2 |
| [Sprained_Leg__Left___Stabilized__eblucqnyOS7lb5E5.json](../../../packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Sprained_Leg__Left___Stabilized__eblucqnyOS7lb5E5.json) | stabilized; followUp → treated, SPD/dodge/athletics −1 |
| [Sprained_Leg__Left___Treated__f7NaW1AMnrSLGkd3.json](../../../packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Sprained_Leg__Left___Treated__f7NaW1AMnrSLGkd3.json) | treated; followUp null, только SPD −1; location leftArm (issue-00325) |

У каждой формы собственный Item и один embedded base effect, transfer=true/disabled=false. Одинаковый embedded ID допустим в разных Item. Raw changes старого экспорта не смешаны с текущим system.changes без миграционной границы .007/.008; совпадение имён эффектов не определяет механическое действие. Проверка соответствия контента рулбуку не проводилась.

## Доказательства и ограничения

Семь первичных областей прочитаны в указанных пределах: damageMixin:288–356; остальные шесть файлов целиком. Прочитаны поздние карточки этих файлов, R011-18 и R012-01…09. У соседей проверены settings:1–14/86–96, entry:61–73, manifest:51–57, Actor.addItem:259–273, crit/location producer и DefenseMessageData, helper getRandomInt, healMixin:52–102 (индексируется только handoff), stat/stats модели, tab-effects целиком, config critLevel/critTreatment, Item sheet/context/Drop, Actor context/listeners, inline writer и effect-part:1–27. Остальная общая логика эффектов/урона/меню переиспользована из прежних проверок.
Полностью прочитаны связанные issues: 00002,00054,00121,00122,00127,00258,00288,00289,00324,00325,00327. Прежние даты, воспроизведения и ограничения остаются историческими; нового запуска игрового сценария нет. Issues/аудит не изменены, новые проблемы не зарегистрированы.
Внешний fromUuid проверен по /opt/foundryvtt/client/utils/helpers.mjs:149–211 (включая соседний fromUuidSync): загрузка Compendium через await getDocument, возврат Document/null. SHA256 целого файла: `21d7b80e8f7ac7b8e4c53aef622f36ec1867ca6be75ae7bb21c959df733d314c`. Это выбранное внешнее чтение, не новый system source. Допустимость Document в createEmbeddedDocuments опирается также на прежнюю проверку ядра .013; фактическое сохранение/права/UUID/live DOM и многоклиентность не исполнялись.

## Процессы

<a id="proc-000314"></a>

### proc-000314 — Критический урон: critdamage

Callback меню .020 передаёт prepared crit; два самостоятельных действия, не автоматическая пара.

<a id="proc-000315"></a>

### proc-000315 — Критический урон: bonusdamage

Callback меню .020 передаёт prepared crit; два самостоятельных действия, не автоматическая пара.

<a id="proc-000316"></a>

### proc-000316 — Травма: выбор Item из индекса

applyCritWound(crit); индексный Item pack, не RollTable и не JSON экспорт.

<a id="proc-000317"></a>

### proc-000317 — Срок травмы: самостоятельный Actor helper

Прямой caller в module не найден; это не метод модели Item.

<a id="proc-000318"></a>

### proc-000318 — Травма: схема девяти полей

Foundry вызывает статическую фабрику модели; Item ID/name/img/effects находятся вне system schema.

<a id="proc-000319"></a>

### proc-000319 — Травма: подготовка срока

Подготовка Item.system; наблюдается текущее BODY.max владельца, не обещание итогового порядка всех эффектов.

<a id="proc-000320"></a>

### proc-000320 — Срок травмы: prepared поле модели

CriticalWoundData.calculateHealingTime(actor); не Actor.calculateHealingTime.

<a id="proc-000321"></a>

### proc-000321 — Травма: описание для формы и Actor sheet

Вызов из WitcherItemSheet контекста либо Actor._prepareItems; не сохранение.

<a id="proc-000322"></a>

### proc-000322 — Травма: день заживления и завершение

system.heal({sterilized}); вызывает отдых .022, ручная кнопка идёт прямо в treat.

<a id="proc-000323"></a>

### proc-000323 — Травма: переход по followUp или удаление

Ручное лечение и автоматический порог используют один метод; type/treatment/criticalLevel не проверяются.

<a id="proc-000324"></a>

### proc-000324 — Лист Actor: регистрация действий травм

V2 _onRender→activateListeners или V1 activateListeners; передан HTMLElement.

<a id="proc-000325"></a>

### proc-000325 — Травма: click add

Callback DOM; return вызываемого метода не заставляет DOM ждать Promise.

<a id="proc-000326"></a>

### proc-000326 — Травма: click remove

Callback DOM; return вызываемого метода не заставляет DOM ждать Promise.

<a id="proc-000327"></a>

### proc-000327 — Травма: click treat

Callback DOM; return вызываемого метода не заставляет DOM ждать Promise.

<a id="proc-000328"></a>

### proc-000328 — Травма: ручное создание Item

Нажатие .add-crit; это не выбор из компедиума.

<a id="proc-000329"></a>

### proc-000329 — Травма: ручная кнопка лечения

Нажатие data-action=treatCriticalWound; от лечения днями не зависит.

<a id="proc-000330"></a>

### proc-000330 — Редактор травмы: сохранить followUp

Унаследованный Drop проверяет isEditable и documentName Item; этот override subtype не проверяет.

<a id="proc-000331"></a>

### proc-000331 — Отдых: передача стерилизации травме

Selected forEach callback recoverActor: после await ресурсы Actor, до сообщения .022.

<a id="proc-000332"></a>

### proc-000332 — Список травм: значения и действия

Включение partial; вывод списка не создаёт Items.

<a id="proc-000333"></a>

### proc-000333 — Редактор травмы: поля и inherited submit

PARTS.main WitcherCriticalWoundSheet; metadata/context/configuration унаследованы.

<a id="proc-000334"></a>

### proc-000334 — Травмы: соответствие CSS разметке

Статическое применение stylesheet; не игровой переход.

## Проверки

Пройдены все 170 тестовых методов (unittest, 1340.706 с), включая 485 CLI-примеров, из них 32 новых. Это проверки справочника по исходникам, без исполнения игрового сценария.

~~~bash
python3 -B -m unittest discover -s docs/analytics/system-index/tests -v
python3 -B docs/analytics/system-index/query.py check --freshness --format json
git diff --check
~~~

До публикации проверены 32 новых ожидания CLI и семь проверок .021 на временном наборе. Сверка с исходниками исправила неточные имена переменных в новых строковых проверках. Дополнительно проведены 124 проверки расширений без CLI: выявлена повторная связь renders к тому же partial. Новая дублирующая запись удалена, прежняя связь к src-000530 переиспользована; затронутый тест .008 повторно прошёл без изменения теста. После этого опубликован набор и успешно выполнен полный прогон выше.

У 451 из 453 прежних CLI-примеров сохранены проверяемые списки ID/концов отношений. Два накопленных ответа .006 расширены: X006-07 дополнен прямым чтением criticalWoundsPack в applyCritWound:316, X006-12 — proc-000316. Прежние читатель/процессы и их адреса сохранены, основание расширения записано в примерах. Начальные 16 примеров по-прежнему проверяются на seed-наборе. Исторические численные итоги .020 закреплены диапазонами ID; все её содержательные проверки сохранены.

Проверены оба направления 11605 отношений, локализация определений, принадлежность отношений шагам, достижимость выходов и три аспекта покрытия 615 sources. Все 313 прежних процессов сохранены побайтно как записи. У двух прежних отношений rel-010882/010883 обновлена только текстовая пометка payload о раскрытом критическом входе; остальные 11391 прежнее отношение неизменны. Десять прежних сущностей уточнены с сохранением ID/owner/kind. Ссылки/актуальность и сохранность после обновления навигации — в итоговом протоколе.


## Итог и следующая порция

Добавлены 55 сущностей, 212 отношений, 21 процесс и 11 динамических/внешних границ. Накоплено 4528 сущностей, 11605 связей и 334 процесса (1091 шаг, 1993 перехода); 329 границ. Определения есть в 246/615 файлах: два словаря complete по строковым ключам, 244 файла partial; роли 142 основных/104 смежных, 369 без определений.

TASK-0006.021 done; следующая — [TASK-0006.022](../../tasks/task-0006.022.md), лечение, отдых, регенерация и спасброски смерти. Родитель остаётся in-progress. [Итоговая сверка](review-log.md#task-0006021).
