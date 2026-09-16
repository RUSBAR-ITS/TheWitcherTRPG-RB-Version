# TASK-0006.017 — Бросок урона и контракты боевых сообщений

2026-09-15; rusbar-main, исходный HEAD 6fa707f90e678e046b58dfae390246a202515f4f; рабочее дерево в начале чистое. [Задача](../../tasks/task-0006.017.md).

## Область и остаток

Восемь основных исходников и выбранные смежные области. Схема v1 и CLI сохранены; полный индекс partial. Это чтение кода и сверка справочника; новый бой в Foundry не исполнялся.

| Основной источник | Область / остаток |
| --- | --- |
| [module/item/mixins/damageUtilMixin.js](../../../module/item/mixins/damageUtilMixin.js) (src-000159) | Три метода Item, callback формы и обработка записи эффекта; магический producer только выбранными адресами, остальной cast вне порции. |
| [module/scripts/damageInstance.js](../../../module/scripts/damageInstance.js) (src-000197) | Весь класс: девять публичных полей и десять методов; выбранные writers/тексты. Полные SP/HP и все локации остаются .018/.019. |
| [module/data/chatMessage/damageMessageData.js](../../../module/data/chatMessage/damageMessageData.js) (src-000096) | Вся локальная схема damage и effects; очистка ядра адресована, сохранение/доставка мира не проверены. |
| [module/data/chatMessage/templates/damageData.js](../../../module/data/chatMessage/templates/damageData.js) (src-000100) | Восемь общих полей damageData и оба включения; методы DamageProperties не принадлежат plain Damage.properties. |
| [module/data/chatMessage/baseMessageData.js](../../../module/data/chatMessage/baseMessageData.js) (src-000095) | Полная schema rollTotal и metadata; произвольные producers/consumers остаются partial. |
| [module/chatMessage/chatMessageData.js](../../../module/chatMessage/chatMessageData.js) (src-000050) | Конструктор и append, поля и выбранные вызовы; полный чат/доставка остаются .020. |
| [module/chatMessage/witcherChatMessage.js](../../../module/chatMessage/witcherChatMessage.js) (src-000051) | Пустой класс и существующая регистрация; поведение ядра не объявлено собственной реализацией. |
| [templates/dialog/combat/variableDamage.hbs](../../../templates/dialog/combat/variableDamage.hbs) (src-000509) | Вся форма: currentDamage/newDamage, ключ подписи и callback; реальный Dialog/DOM не исполнялся. |

## Контракты и существенные различия

- createBaseDamageObject и getPreprocessedEffects переиспользуют процессы .014. Первый отдаёт properties/Item/defenseOptions по ссылке; crit — отдельный объект. Formula/type/location не задаются. Preprocessing копирует записи и объединяет совпадающие непустые statusEffect, суммируя percentage; это не отменяет прежних мутаций prepared Item в weaponAttack/castSpell.
- rollDamage переводит formula в строку. Только пустая строка заменяется на 0 с уведомлением; undefined/null не становятся нулём. Переменный ввод может полностью заменить формулу; strike.dmgMulti оборачивает всё выражение в скобки. Локация вновь вычисляется статическим resolver и заменяет damage.location по ссылке.
- Вход rollDamage требует DamageProperties.getPreprocessedEffects. Attack.damage.properties — EmbeddedDataField с модельными методами; прямой rollOnlyDmg из .015 передаёт обычный объект после toObject(false). Исходное наблюдение issue297 сохраняется. На выходе DamageMessageData.properties — обычный SchemaField без этого метода; найденный штатный вызов повторного rollDamage с готовым Damage здесь не утверждается.
- У каждой копии эффекта сначала строится имя и ручная ссылка статуса, затем проверяется truthy percentage. getRandomInt(100) даёт 1–100; roll>percentage ставит false, иначе true. Для 0 applied не назначается и схема сообщения даёт false. Неизвестный truthy statusEffect вызывает чтение img/name у отсутствующей записи до Roll. Ручная ссылка не проверяет applied и не содержит duration.
- DamageMessageData расширяет общую damageData, заменяет Embedded properties на SchemaField и effects на ArrayField с applied. Percentage ограничивается диапазоном 0–100 уже при очистке сообщения. ArrayField ядра преобразует plain object по неотрицательным целочисленным ключам: словарь с обычными ID теряет записи, числовой словарь не обязан очищаться целиком.
- Восемь полей damageData: itemUuid/formula/crit/strike/type/originalLocation/location/properties. Duration, raw Item и вложенный defenseOptions не объявлены; схема с prune удаляет их. Дополнительный flag.damage не восстанавливает поле system.damage.duration для onHit/onDamage. Defense.crit остаётся отдельной схемой .016 без critEffectModifier; общий damage.crit этот модификатор содержит.
- ChatMessageData — контейнер параметров, сохраняющий ссылки system/flags. append объединяет верхний уровень, добавляет flavor, сохраняет speaker/type; документа не создаёт. WitcherChatMessage — пустой subclass, а отдельные CONFIG.ChatMessage.dataModels определяют модель system.
- rollDamage использует обычный Roll и ждёт evaluate/toMessage, затем запускает setFlag без await и возвращает undefined. В прочитанном ядре Roll.toMessage задаёт content/rolls и создаёт выбранный класс документа, но не пишет system.rollTotal. Его заполняет extendedRoll; BaseMessageData только объявляет поле.
- Физическое меню берёт parseInt первого DOM .dice-total и dataset.messageId; normal выбирает HP/STA по isNonLethal. applyDamageFromMessage читает prepared system.damage, а не flag. Он меняет location/oilEffect по ссылке и передаёт тот же объект дальше. Полные применение, диалог/сеть и HP остаются .019/.020.
- DamageInstance — изменяемый обычный объект: initialDamage и damage получают вход без проверки, ещё семь полей null. Setters меняют только своё поле и возвращают this. Пять методов текста лишь соединяют текущее значение и optional [source], без локализации/расчёта; null виден как текст.
- Адресованы producers DamageInstance в chat/status/oil/silver/flat/crit, прямые writers shielded/damage/afterSp/afterLocation/afterResistance и читатели текста. setShielded не имеет найденных calls вне определения; blocked не записывается найденными consumers. Присваивание setType="silver" не обозначено вызовом setter. Полные алгоритмы сопротивлений и shared allLocations остаются .018/.019.
- variableDamage.hbs получает только currentDamage, cssClass отсутствует. Callback читает newDamage.value как строку; rejectClose отклоняет Promise. Точный ключ HBS — WITCHER.Item.DamageProperties.variableDamage, JS title запрашивает отсутствующий Item.properties.variableDamage. Сокращённое написание в поздней карточке не перенесено в индекс.
- Начальный flavor содержит незакрытый div перед h1; прежний parse5 сохранял marker damage-message, но не создавал отдельный h1. CSS процентных исходов и статуса адресован по реальным selectors; browser sanitization и computed style не проверялись.

## Доказательства и границы

Прочитаны восемь основных исходников, выбранные смежные участки, поздние карточки TASK-0004.004/.011 и R011-01–05/12. Сопоставлены полные issues 00070/00073/00184/00247/00257/00285/00286/00291/00293/00295/00296/00297/00300. Прежние опыты .040/.041/.044/.045/.046 сохраняют даты и фасады. Новых issues и запусков игрового сценария нет; potential статусы не менялись. Словесный type=damage остаётся установленным соседом по R011-01/02 и поздним карточкам; его полный процесс B12 не раскрыт.

Прочитаны локальные участки Roll.toMessage и очистки SchemaField/ArrayField/NumberField. Это внешние контракты, без нового исполнения ядра, записи в БД, браузера, проверки сети или соответствия рулбукам.

| Внешний файл | Область | SHA-256 |
| --- | --- | --- |
| /opt/foundryvtt/client/dice/roll.mjs | toMessage:926–953; только чтение | a27f498f7b3864a1baa7cebbb1ccb611f9796720b4a4d153df779803b995c7ff |
| /opt/foundryvtt/common/data/fields.mjs | SchemaField:1066–1147; NumberField:1504–1537; ArrayField:2369–2408; только чтение | efa8e3ccdf553ca826580e60bfbfc97db57bdeadaa954a50f6a55e0ab52c3e01 |

## Процессы

<a id="proc-000212"></a>

### proc-000212 — Контейнер сообщения: создание

actor/flavor/type/system/flags → обычный DTO; не запись документа.

<a id="proc-000213"></a>

### proc-000213 — Контейнер сообщения: добавление

append не меняет speaker/type и не сохраняет ChatMessage.

<a id="proc-000214"></a>

### proc-000214 — Общее сообщение: поле итога

Объявление единственного rollTotal; число записывается отдельно отправителем.

<a id="proc-000215"></a>

### proc-000215 — Сообщение урона: замена свойств

damageData предоставляет общий контракт; properties/effects заменяются локальной схемой.

<a id="proc-000216"></a>

### proc-000216 — Общие поля урона сообщения

Восемь полей; properties здесь Embedded, Defense.crit отдельная схема.

<a id="proc-000217"></a>

### proc-000217 — Урон: ввод переменной формулы

Исходная строка, без валидации формулы; отказ окна отклоняет Promise.

<a id="proc-000218"></a>

### proc-000218 — Урон: подтверждение новой строки

Внешний Dialog вызывает ok.callback; это отдельный ввод, не Roll.

<a id="proc-000219"></a>

### proc-000219 — Урон Item: формула, эффекты и сообщение

damage по ссылке с моделью properties; метод не возвращает Roll/ChatMessage.

<a id="proc-000220"></a>

### proc-000220 — Урон: процент одной записи

Синхронный forEach; ручная ссылка статуса строится до процентной проверки.

<a id="proc-000221"></a>

### proc-000221 — Порция урона: создание

Обычный объект, без проверки входа и без Foundry Document.

<a id="proc-000222"></a>

### proc-000222 — Порция урона: setType

Fluent setter меняет только type и возвращает тот же объект.

<a id="proc-000223"></a>

### proc-000223 — Порция урона: setShielded

Fluent setter меняет только shielded и возвращает тот же объект.

<a id="proc-000224"></a>

### proc-000224 — Порция урона: setSource

Fluent setter меняет только source и возвращает тот же объект.

<a id="proc-000225"></a>

### proc-000225 — Порция урона: initialDamageText

Текст текущего поля и optional [source]; нет локализации или расчёта.

<a id="proc-000226"></a>

### proc-000226 — Порция урона: afterSpText

Текст текущего поля и optional [source]; нет локализации или расчёта.

<a id="proc-000227"></a>

### proc-000227 — Порция урона: afterLocationText

Текст текущего поля и optional [source]; нет локализации или расчёта.

<a id="proc-000228"></a>

### proc-000228 — Порция урона: afterResistanceText

Текст текущего поля и optional [source]; нет локализации или расчёта.

<a id="proc-000229"></a>

### proc-000229 — Порция урона: damageText

Текст текущего поля и optional [source]; нет локализации или расчёта.

<a id="proc-000230"></a>

### proc-000230 — Сообщение урона: источники входа

Выбранные callbacks физического урона; полное меню и применение остаются .019/.020.

## Проверки

Пройдены все 134 тестовых метода (unittest, 832.147 с), включая 28 новых CLI-случаев; накоплено 357 CLI-примеров. Это проверки справочника по исходникам, без исполнения игрового сценария.

~~~bash
python3 -B -m unittest discover -s docs/analytics/system-index/tests -v
python3 -B docs/analytics/system-index/query.py check --freshness --format json
git diff --check
~~~

До общего прогона все 28 новых ожиданий сопоставлены с временным набором, семь отдельных проверок новой порции прошли. Проверены владельцы моделей/DTO, формула и порядок вероятности/сообщения/флага, ввод newDamage и локализация, DamageInstance/setters/writers/тексты, конкретные sources DOM/system и внешняя очистка. На предварительном этапе исправлен многострочный режим регулярного выражения в тесте перечисления полей; исходные определения и ожидания не менялись.

Прежние 329 поисковых примеров сравнены с предыдущим набором: проверяемые списки ID и концов связей не изменились. Численные итоги .016 сохранены как исторический диапазон ID; прежние содержательные проверки сохранены. Полный прогон после этих подготовительных действий успешен.

Все 10013 отношений проверены в обоих направлениях. Для новых процессов проверены достижимость шагов/выходов и принадлежность отношений сущности/диапазону шага; три аспекта покрытия сверены для 615 sources. Окончательная актуальность, ссылки и сохранность после навигационных правок приведены в журнале. JavaScript боя, браузер, мир/БД и межклиентская доставка этими тестами не исполняются.


## Итог и следующая порция

Добавлены 71 сущность, 247 отношений и 19 процессов; шесть новых внешних/динамических границ. Накоплено 4191 сущность, 10013 связей и 230 процессов (821 шаг, 1443 перехода); 284 границы. Определения есть в 227/615 файлах: два словаря complete по строковым ключам, 225 файлов partial; роли 111 основных/116 смежных, 388 без определений.

TASK-0006.017 done; следующая — [TASK-0006.018](../../tasks/task-0006.018.md), броня, сопротивления и износ SP. Родитель остаётся in-progress. Окончательная сверка — в [журнале](review-log.md#task-0006017).
