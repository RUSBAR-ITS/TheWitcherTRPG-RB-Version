# module/data/actor/templates/character/attackStatsData.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/data/actor/templates/character/attackStatsData.js](../../../../../../../../../module/data/actor/templates/character/attackStatsData.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `c9eac1ffb28fdf69935d500fff26d4d0ad1d1609` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.005](../../../../../../../../tasks/task-0003.005.md), одна порция из семи файлов |
| Запись перекрёстной сверки | [TASK-0003.005](../../../../../../review-log.md#task-0003005) |

## Назначение файла

Собирает общие данные Actor для бонуса ближнего боя, строк punch/kick и двух модификаторов критической травмы. Вычисления и применение находятся в документе Actor и его mixin-файлах.

## Условия использования

При импорте локальная const fields получает foundry.data.fields. Default export — фабрика определения схемы; каждый вызов создаёт новые поля. Очистку, начальные значения и валидацию применяет Foundry при создании/обновлении модели. attackStats() вызывает attack() для двух пар. CommonActorData:6,47 включает блок в SchemaField; его наследуют персонаж и монстр. Собственных вычислений и hooks в фабрике нет.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| fields | const, 3 | Классы полей | Локальная | Читается фабрикой |
| attackStats | function, 5–13 | Сборка пяти полей | Default export | Создаёт три NumberField и два SchemaField |
| meleeBonus | NumberField, 7 | Добавка урона ближнего боя | system.attackStats.meleeBonus | initial=0; собственных диапазонов нет |
| punch | SchemaField, 8 | Пара label/value для удара рукой | system.attackStats.punch | attack('WITCHER.Actor.DerStat.Punch') |
| kick | SchemaField, 9 | Пара label/value для удара ногой | system.attackStats.kick | attack('WITCHER.Actor.DerStat.Kick') |
| critLocationModifier | NumberField, 10 | Добавка к определению случайной локации крита | system.attackStats.critLocationModifier | initial=0; min/max/integer не заданы |
| critEffectModifier | NumberField, 11 | Добавка выбора эффекта травмы | system.attackStats.critEffectModifier | initial=0; min/max/integer не заданы |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| attackStats(); 5–13 | Доступен foundry.data.fields | Объект пяти полей | Создаёт новые определения полей при каждом вызове | Синхронно; без записи документов, обработчиков событий и собственного catch |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| attack (default) | [module/data/actor/templates/character/attackData.js](../../../../../../../../../module/data/actor/templates/character/attackData.js) | Прямой импорт и два вызова | 1,8–9 | Фабрика label/value прочитана полностью |
| NumberField, SchemaField | Foundry 14.367.0, /opt/foundryvtt/common/data/fields.mjs | Глобальный API | 3,7–11 | Состав и defaults проверены настоящими моделями |
| Ключи Punch/Kick | [lang/en.json](../../../../../../../../../lang/en.json); [lang/ru.json](../../../../../../../../../lang/ru.json) | Аргументы attack(label) | 8–9: initial строк label | Оба перевода найдены после expandObject |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/data/actor/commonActorData.js](../../../../../../../../../module/data/actor/commonActorData.js) | attackStats() и meleeBonus | Включение схемы; migrateCalculatedStats обнуляет truthy source.attackStats.meleeBonus | 6,47,118 |
| [module/actor/witcherActor.js](../../../../../../../../../module/actor/witcherActor.js) | meleeBonus/punch.value/kick.value | calculateAttackStats добавляет бонус BODY и заменяет две строки | 191–196; вызов в конце prepareDerivedData:53 |
| [module/activeEffect/mixins/baseMixin.js](../../../../../../../../../module/activeEffect/mixins/baseMixin.js) | Три числовых поля | getOtherSuggestions предлагает точные пути для эффекта | 125–143 |
| [module/activeEffect/WitcherActiveEffectSheet.js](../../../../../../../../../module/activeEffect/WitcherActiveEffectSheet.js) | Пути getOtherSuggestions | wizardAction для base вызывает getActiveEffectsBasePaths; baseMixin включает getOtherSuggestions | wizardAction:59–96; Object.assign:140 |
| [module/actor/mixins/weaponAttackMixin.js](../../../../../../../../../module/actor/mixins/weaponAttackMixin.js) | meleeBonus | weaponAttack при applyMeleeBonus и character/addMeleeBonus добавляет знак/величину в формулу; передаёт число контексту диалога | 15–28,56–66 |
| [module/actor/mixins/professionMixin.js](../../../../../../../../../module/actor/mixins/professionMixin.js) | meleeBonus и два crit-модификатора | doProfessionAttackRoll строит формулу и объект damage.crit | 59–87,142–149 |
| [module/item/mixins/damageUtilMixin.js](../../../../../../../../../module/item/mixins/damageUtilMixin.js) | Два crit-модификатора | createBaseDamageObject копирует из parent.system.attackStats в crit | 8–18 |
| [module/actor/mixins/defenseMixin.js](../../../../../../../../../module/actor/mixins/defenseMixin.js) | critLocationModifier/critEffectModifier в damage.crit | При критическом результате защиты переносит critEffectModifier; случайная локация использует 2d6+critLocationModifier | 205–209,355–357 |
| [module/actor/mixins/damageMixin.js](../../../../../../../../../module/actor/mixins/damageMixin.js) | crit.critEffectModifier | При выборе из нескольких травм берёт location.critEffect либо getRandomInt(6)+модификатор; >4 выбирает lesserEffect=false | applyCritWound:312–336 |
| [templates/dialog/combat/weapon-attack.hbs](../../../../../../../../../templates/dialog/combat/weapon-attack.hbs); [templates/dialog/combat/profession-attack.hbs](../../../../../../../../../templates/dialog/combat/profession-attack.hbs) | meleeBonus контекста | Показывает опциональное значение | 231–236 / 152–157 |

Потребители искались по именам файлов/экспортов, точным и динамическим путям в module/, templates/ и packsJson/. В 226 JSON-компедиумах строковых ссылок с префиксами system.logs, system.skillTrainingN, system.pannels, system.attackStats не найдено. Бинарные packs, действующие БД и внешние макросы не проверялись.

## Данные и изменения состояния

Начальные числовые значения равны 0, punch/kick.value пусты. При создании модели ненулевой исходный meleeBonus сбрасывается миграцией CommonActorData; источник не имеет отдельного unmodifiedMeleeBonus. В памяти calculateAttackStats вычисляет B=ceil((BODY.value−6)/2)×2 и делает meleeBonus+=B. Прибавка, уже находившаяся в подготовленных данных, сохраняется в итоговом числе, но строки punch/kick строятся только из B. Метод вызывается один раз в показанной prepareDerivedData; искусственный повтор на той же модели не использовался для вывода о повторном начислении в мире.

Числовые модификаторы критов копируются в данные атаки. Модификатор локации применяется в ветке originalLocation.includes('random'), а выбор эффекта может быть уже предопределён location.critEffect. Полный выбор травмы и соответствие правилу не анализировались. Сама фабрика не создаёт эффект/травму и не обновляет Actor; calculateAttackStats меняет подготовленные значения в памяти.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Поля и вложение | Common/Character/MonsterData | Пять полей с точными defaults; обе специализации наследуют блок | Без полной подготовки документа |
| Расчёт BODY и уже имеющейся добавки | Исходный calculateAttackStats, предварительный meleeBonus=3, BODY1/6/8 | Итог -1/3/5; punch 1d6+-4 / 1d6+0 / 1d6+2; kick 1d6+0 / 1d6+4 / 1d6+6 | Добавка 3 установлена прямо в памяти; реальный ActiveEffect не применялся |
| Миграция исходного бонуса | new Common({attackStats:{meleeBonus:3}}) | В модели бонус 0 | Не отдельная проверка обновления документа |
| Мастер ↔ схема | Исходный getOtherSuggestions и Common.schema.getField | Три пути meleeBonus/critLocationModifier/critEffectModifier существуют | Окно/запись ActiveEffect не запускались |
| Потребители критов/формул | Точечное чтение методов из таблицы | Прослежены копирование в crit и условия двух применений | Полный бой, Roll и травмы не выполнялись |

## Непроверенные участки и открытые вопросы

Исходник прочитан полностью; соседние файлы проверены только в пределах описанных связей. Мир, браузер, реальное сохранение и полный жизненный цикл Actor/листов не запускались. Подмены и исполнявшийся сценарий приведены в журнале; успешная проверка карточки не подтверждает исправность всей системы. Дальнейшие роли сохранённых punch/kick.value и применение эффектов разных фаз остаются предметом последующих порций. Обнуление исходного meleeBonus и отсутствие найденных читателей punch/kick зафиксированы без автоматического объявления ошибок.

## Связанные проблемы

Новых проблем самой фабрики и проверенной цепочки атак не зарегистрировано. [issue-00012](../../../../../../../../issues/potential/issue-00012.md) относится к другому расчёту luck/toxicity; похожая запись += не является достаточным основанием переносить тот вывод на calculateAttackStats.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.005 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.

## Уточнение TASK-0003.006

2026-09-10, `fe7ea7420cd4dfa6ee51baf7520f7b0ad8f8b13d`. Подтверждено attackStats:47 у персонажа и монстра; расположение фабрики в character не ограничивает тип владельца. CommonActorData.migrateCalculatedStats:118 обнуляет truthy meleeBonus до последующих расчётов Actor.

Карточки сборки: [commonActorData](../../commonActorData.js.md). [Сверка TASK-0003.006](../../../../../../review-log.md#task-0003006).

## Уточнение TASK-0003.007

2026-09-10, `b8b89a7e3392235f993c21f3c6d277a4a2e7a55f`. WitcherActor.calculateAttackStats:191–196 завершает собственную подготовку: C=ceil((BODY.value−6)/2)×2, meleeBonus+=C, punch/kick строятся из C. Это отдельный расчёт от modifierMixin.addAttackModifiers: последний только превращает combatEffects.attackModifier в строку и имеет issue-00033.

Карточки: [WitcherActor](../../../../actor/witcherActor.js.md), [modifierMixin](../../../../actor/mixins/modifierMixin.js.md). [Сверка TASK-0003.007](../../../../../../review-log.md#task-0003007).
