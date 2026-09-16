# Процессы пилота TASK-0006.004

2026-09-14; rusbar-main, `3b22cf11595611a18b17fac091acae1249549b03`. [Задача](../../tasks/task-0006.004.md), [протокол](review-log.md#task-0006004), [поиск](README.md).

В [данные процессов](data/processes/pilot.jsonl) добавлены 12 записей: 96 шагов и 144 перехода. Вместе с неизменными начальными примерами — **14 процессов, 101 шаг и 151 переход**. Сущностей по-прежнему 400, отношений 977. Состав пилота тот же: выбранные области 23 основных и 13 смежных файлов, без нового пофайлового счётчика.

## Адреса процессов

Запрос `process ID` раскрывает шаги, отношения, условия и выходы. `--offset/--limit` ограничивает страницу, но выходы и отметки перехода за страницу сохраняются. Все новые процессы partial: внешние API, соседние тела и полные цепочки интерфейса раскрыты только в объявленных границах. Complete у proc-000001 относится только к нормальному пути getter.

| Процесс | Назначение | Шагов | Вход | Покрытие |
| --- | --- | --- | --- | --- |
| <a id="proc-000001"></a>proc-000001 | Чтение Skill.modifiedValue | 2 | ent-000016 — [Skill.modifiedValue](../../../module/data/actor/templates/common/skills/skillData.js) | complete |
| <a id="proc-000002"></a>proc-000002 | Общий цикл подписей Intelligence.migrateData | 3 | ent-000032 — [Intelligence.migrateData](../../../module/data/actor/templates/common/skills/intData.js) | partial |
| <a id="proc-000003"></a>proc-000003 | Подготовка баз CommonActorData | 4 | ent-000141 — [CommonActorData.prepareBaseData](../../../module/data/actor/commonActorData.js) | partial |
| <a id="proc-000004"></a>proc-000004 | Порядок производных расчётов Actor | 8 | ent-000280 — [WitcherActor.prepareDerivedData](../../../module/actor/witcherActor.js) | partial |
| <a id="proc-000005"></a>proc-000005 | Расчёт одного значения характеристики | 11 | ent-000282 — [WitcherActor.calculateStat](../../../module/actor/witcherActor.js) | partial |
| <a id="proc-000006"></a>proc-000006 | Применение эффекта: системное подавление и граница ядра | 3 | ent-000313 — [WitcherActiveEffect.isSuppressed](../../../module/activeEffect/witcherActiveEffect.js) | partial |
| <a id="proc-000007"></a>proc-000007 | Назначение фазы изменения при обновлении ActiveEffect | 6 | ent-000319 — [WitcherActiveEffect._preUpdate](../../../module/activeEffect/witcherActiveEffect.js) | partial |
| <a id="proc-000008"></a>proc-000008 | Навыковые и групповые добавки к формуле | 10 | ent-000296 — [actor.modifierMixin.addActiveEffects](../../../module/actor/mixins/modifierMixin.js) | partial |
| <a id="proc-000009"></a>proc-000009 | Вход броска из обработчика навыка | 1 | ent-000382 — [sheet.skillMixin.skillListener/rollSkill click](../../../module/actor/sheets/mixins/skillMixin.js) | partial |
| <a id="proc-000010"></a>proc-000010 | Прямой вход rollSkill по ключу | 1 | ent-000301 — [actor.skillMixin.rollSkill](../../../module/actor/mixins/skillMixin.js) | partial |
| <a id="proc-000011"></a>proc-000011 | Бросок встроенного навыка: сбор формулы | 12 | ent-000302 — [actor.skillMixin.rollSkillCheck](../../../module/actor/mixins/skillMixin.js) | partial |
| <a id="proc-000012"></a>proc-000012 | Общий бросок: Roll, критические исходы, порог и сообщение | 23 | ent-000369 — [extendedRoll](../../../module/scripts/rolls/extendedRoll.js) | partial |
| <a id="proc-000013"></a>proc-000013 | Бросок собственного Item-навыка | 11 | ent-000304 — [actor.skillMixin.rollCustomSkillCheck](../../../module/actor/mixins/skillMixin.js) | partial |
| <a id="proc-000014"></a>proc-000014 | Ввод пользовательского модификатора и строка addPart | 6 | ent-000360 — [getCustomModifier](../../../module/scripts/helper.js) | partial |

## Четыре направления задачи

| Направление | Записи | Границы и связь частей |
| --- | --- | --- |
| Подготовка Actor и характеристик | proc-000003/000004/000005 | Базы, два прохода системных расчётов, отдельный calculateStat. Начальные/финальные фазы выполняет ядро вне тел этих методов |
| Применение ActiveEffect | proc-000006/000007 | Собственный getter подавления и назначение phase в update-payload. Отбор effects/changes, сортировка и операция поля — внешний контракт ниже |
| Значение навыка и модификаторы | proc-000001/000008/000014 | Getter суммы, отдельная сборка числовых/групповых добавок и пользовательская строка. Getter не вставлен в цепочку обычного броска |
| Вход броска и результат | proc-000009–000013 | Callback и прямой вызов имеют отдельные входы; общее тело rollSkillCheck описано один раз. Item-навык имеет свой путь; extendedRoll общий |

Ссылка на другой процесс в scope/summary означает место раскрытия вызываемого метода. Она не является дополнительным ребром next: переходы next остаются внутри одного процесса. Например, proc-000011 делегирует Roll через scope_boundary в proc-000012. Так вызов helper не превращается в копирование всех его шагов.

## Жизненный цикл и применение effects

Порядок установлен чтением текущего ядра и [R003-02](../code-audit/cross-check-0002.md#r003-02), [R005-04](../code-audit/cross-check-0002.md#r005-04), [R005-05](../code-audit/cross-check-0002.md#r005-05), [R018-02](../code-audit/cross-check-0002.md#r018-02):

| Положение | Исполнитель | Что происходит |
| --- | --- | --- |
| До initial | ClientDocument → system.prepareBaseData | Для Character/Monster — CommonActorData, proc-000003; меняются prepared-базы |
| Подготовка документа | Core Actor.prepareBaseData / prepareEmbeddedDocuments | Сбрасываются служебные коллекции, готовятся вложенные документы |
| initial | Core Actor.applyActiveEffects | Эффекты применяются перед системными derived-расчётами |
| Системные derived | system.prepareDerivedData → WitcherActor.prepareDerivedData | proc-000004: stats → fixed → stats → derived → attacks; calculateStat отдельно в proc-000005 |
| final | Core Actor.prepareData после super.prepareData | Повторный проход эффектов для final; затем специальные статусы токенов |

Даже ранний return для loot/mystery останавливает только системный override, а не дальнейшую final-фазу ядра. В prepareDerivedData async applyStatus вызывается без await, включая пустой armorEffects; его Promise не удерживает переход к расчётам.

Применение изменений в ядре различает несколько условий:

1. Уже завершённая в этом цикле фаза не выполняется повторно. Для нестрокового аргумента ядро выбирает initial/final с предупреждением; неизвестная строковая фаза регистрирует ошибку через Hooks.onError. Нормальный lifecycle передаёт зарегистрированные строки.
2. allApplicableEffects включает собственные Actor.effects и Item.effects с transfer. active проверяет !disabled && !isSuppressed; proc-000006 раскрывает только собственный getter. Предшествующие барьеры могут вообще не допустить входа в него.
3. В system.changes пропускаются пустой key и несовпавшая phase. token.* отделяется от обычных изменений Actor. В initial отдельно обрабатываются statuses.
4. Prepared priority получает default через ??= по change.type; явный 0 сохраняется. Отобранные строки сортируются по priority. Общего нового правила «все ADD раньше MULTIPLY» здесь не вводится.
5. ActiveEffect.applyChange разрешает key и выбирает configured handler, обработчик известного поля либо неизвестного пути. applyChangeField передаёт текущее значение в field.applyChange и пишет результат при modifyTarget и update !== undefined. Тип поля и операция существенны; произвольный key не обещает числового изменения.
6. Изменённое prepared-поле читает соответствующий потребитель. Stat.value, stat.max, totalModifiers, Skill.value и activeEffectModifiers имеют разные адреса и роли.

Эта часть остаётся **внешним контрактом**, а не фиктивными локальными шагами со строками системного класса. Proc-000006 начинается с isSuppressed, не с полного Actor.applyActiveEffects. Для внешнего API, указанного только в границе выхода, поиск processes не придумывает участие в локальном шаге. Полный индекс ядра Foundry этим этапом не создан.

Дополнительно перечитаны /opt/foundryvtt/client/documents/actor.mjs:212–275,305–313,428–474; client/documents/active-effect.mjs:265–273,500–502,527–578; common/data/active-effect.mjs:15–26 и ClientDocument.prepareData:313–320. Версия 14.367.0 и отпечатки четырёх файлов совпадают с [проверкой .003](pilot-coverage.md#внешние-контракты-и-динамические-цели). Автоматический check сверяет package.json; содержимое файлов ядра дополнительно сверено отдельно, игровой lifecycle не исполнялся.

## Ожидание, ранние выходы и данные

- В calculateStat смерть и ранение — разные ветви: смерть добавляет 2 к divider и пропускает сброс/проверку woundThreshold. REF/DEX учитывают перегруз дважды; второй calculateStats после fixed повторяет чтение порога.
- _preUpdate ожидает super и останавливается при строго false. Затем читает только data.system?.applyAfterCalculations. Отсутствующий system пропускает обход; существующий system без подходящего changes может вызвать ошибку. Phase записывается в payload, сохранение выполняет Foundry.
- Неизвестный skillMap-ключ возвращает пустую строку addActiveEffects ещё до групп. Имена effects служат подписью уже подготовленного числа; отсутствие имени не меняет арифметическую операцию поля.
- rollSkillCheck читает stat.value до проверки dontAddAttr. Getter modifiedValue здесь не вызывается; собственный Item.activeEffectModifiers в rollCustomSkillCheck тоже не читается.
- getCustomModifier ожидает prompt с rejectClose=true; отмена передаёт rejection caller. addPart принимает строку и не валидирует формулу как Roll.
- extendedRoll ожидает evaluate и toMessage. Критический провал сохраняет полную fumbleAmount до ограничения вычитаемого. Порог зависит от threshold/defense/reversal; showSuccess не читается.
- После toMessage вызовы setFlag не ожидаются. При showResult=false возвращается Roll с messageData, без создания сообщения здесь и без применения отдельного flags. Callback DOM возвращает Promise броска, но EventTarget его не ожидает.
- Неперехваченные ошибки и внешние продолжения отмечены выходами. Partial не обещает исчерпывающей схемы всех исключений внешних конструкторов, библиотек и неверных произвольных данных.

## Поиск участия сущности

IQ-07 теперь учитывает **исполнителя шага и оба конца отношений, явно прикреплённых к этому шагу**. Структура ответа сохранена: process ID, step_ids, entry_matches. Само наличие связи где-то в общем графе не означает участие во всех вызывающих процессах; транзитивное включение и поиск через owner автоматически не выполняются.

Для source-запроса отбираются шаги по месту выполнения, не по файлу определения участвующего поля. --scope также ограничивает место шага. Поэтому processes ent-000012 находит getter и сборку модификаторов; тот же запрос с --scope src-000022 не включает поле по косвенному вызову helper.

```bash
python3 docs/analytics/system-index/query.py processes ent-000012
python3 docs/analytics/system-index/query.py processes ent-000281
python3 docs/analytics/system-index/query.py processes ent-000344
python3 docs/analytics/system-index/query.py processes ent-000176
python3 docs/analytics/system-index/query.py process proc-000012 --offset 16 --limit 1
python3 docs/analytics/system-index/query.py details proc-000006
```

Ожидаемые ориентиры из [12 новых CLI-случаев](examples/process-queries.json):

| Вопрос | Ответ |
| --- | --- |
| Где участвует Skill.activeEffectModifiers? | proc-000001/read; proc-000008/numeric и append |
| Как увидеть повторный calculateStats? | proc-000004/stats-first и stats-second — разные шаги и строки вызова |
| Где участвует threshold? | Конфигурация proc-000011 и сравнения/подпись proc-000012 |
| Где участвует applyAfterCalculations? | proc-000007/phase; чтение update-payload |
| Как раскрывается showResult? | Страница proc-000012/output сохраняет ссылки publish/defer с outside_page=true |
| Есть ли явные шаги в config.js? | Нет: processes src-000209 возвращает not_indexed; чтение карты из другого файла не меняет место шага |

Случаи IQ-01–IQ-06/IQ-08 продолжают проверяться [примерами пилота](examples/pilot-queries.json). P13 обновлён под появившиеся proc-000004/000005; его прежний пустой ответ зафиксирован протоколом .003. EX-01–EX-16 по-прежнему проверяются на отдельном начальном наборе. Детальные доказательства и статусы issues остаются в существующем аудите.

## Следующий этап

[TASK-0006.005](../../tasks/task-0006.005.md) проверит пилот в целом и подготовит дальнейшую очередь. Этот этап не объявляет завершённым справочник всех 615 файлов и не расширяет пофайловый анализ.
