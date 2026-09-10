# module/data/actor/monsterData.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/data/actor/monsterData.js](../../../../../../../module/data/actor/monsterData.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `fe7ea7420cd4dfa6ee51baf7520f7b0ad8f8b13d` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.006](../../../../../../tasks/task-0003.006.md), одна порция из четырёх файлов |
| Запись перекрёстной сверки | [TASK-0003.006](../../../../review-log.md#task-0003006) |

## Назначение файла

Модель Actor.monster: к 19 общим полям добавляет 34 поля сведений, природной брони, сопротивлений, иммунитетов и настроек монстра. Подготавливает три блока знаний для листа. Боевые действия выполняют внешние потребители этих полей.

## Условия использования

MonsterData extends CommonActorData, default export. [module/setup/registerDataModels.js](../../../../../../../module/setup/registerDataModels.js):1,39 связывает класс с CONFIG.Actor.dataModels.monster; [system.json](../../../../../../../system.json) объявляет monster и htmlFields common/academicKnowledge/monsterLore; [module/setup/registerSheets.js](../../../../../../../module/setup/registerSheets.js):109–112 назначает WitcherMonsterSheet. Всего 53 поля system: 19 общих и 34 собственных. CharacterData не является родителем, его general, logs, magic, improvementPoints и skillTraining1–4 здесь не определены.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| fields | const:4 | Поля Foundry | Локальная | Чтение при defineSchema |
| MonsterData | class:6–75 | Специализация монстра | Default export; Actor.monster | Создание схемы; enrichedText; методы CommonActorData по наследованию |

| Поле system | Тип / initial | Строки | Смысл и проверенный потребитель |
| --- | --- | --- | --- |
| 19 общих полей | ...commonData | 8 | super.defineSchema:8, spread:11; [полный перечень общей схемы](commonActorData.js.md) без переопределений. |
| category | StringField / 'Humanoid' | 12 | Категория; header/sidebar, совпадение с damageObject.properties.oilEffect в damageMixin:16. |
| threat | StringField / '' | 13 | Ключ monsterDifficulty при отображении header:14. |
| difficulty | StringField / '' | 14 | Ключ monsterComplexity при отображении header:18. |
| bounty | NumberField / 0 | 15 | Награда; явное редактирование найдено в старом monster-sheet.hbs:116–118. |
| resistantNonSilver | BooleanField / false | 16–19 | Настройка; applyDamage:65 предлагает соответствующую галочку. |
| resistantNonMeteorite | BooleanField / false | 20–23 | Настройка; applyDamage:66 предлагает соответствующую галочку. |
| armorHead | NumberField / 0 | 25 | Природная броня головы; armorMixin:30–31. |
| armorUpper | NumberField / 0 | 26 | Природная броня торса/рук; armorMixin:35–46. |
| armorLower | NumberField / 0 | 27 | Природная броня ног; armorMixin:50–56. |
| armorTailWing | NumberField / 0 | 28 | Природная броня хвоста/крыла; armorMixin:60–61. |
| regeneration | NumberField / 0 | 29 | Начало хода: applyMonsterRegeneration в generalCombatHook:11–38. |
| resistances | StringField / '' | 31 | Текст, monster-status:3; не словарь числовых damageTypeModification. |
| immunities | StringField / '' | 32 | Текст, monster-status:5; отдельный от списка статусных иммунитетов. |
| statusEffectImmunities | ArrayField(StringField(initial='')) | 33 | По умолчанию []; строки ID статусов; multi-select monster-status:7–8 и обработчики статусов. |
| susceptibilities | StringField / '' | 34 | Текст уязвимостей, monster-status:11. |
| senses | StringField / '' | 35 | Текст чувств, monster-status:13. |
| height | StringField / '' | 37 | Текст роста, monster-info:4. |
| weight | StringField / '' | 38 | Описание массы, monster-info:8; не масса инвентаря getTotalWeight. |
| environment | StringField / '' | 39 | Среда, monster-info:12. |
| intelligence | StringField / '' | 40 | Описание интеллекта, monster-info:16; не stats.int. |
| organization | StringField / '' | 41 | Организация, monster-info:20. |
| common | HTMLField / '' | 43 | Первый блок знаний, enrichedText:69. |
| commonSkillValue | StringField / '' | 44 | Значение проверки блока; форма type=number в monster-knowledge:4–5. |
| showCommonerSuperstition | BooleanField / true | 45–48 | Видимость блока common; monster-knowledge:2. |
| academicKnowledge | HTMLField / '' | 49 | Академические знания, enrichedText:70. |
| academicKnowledgeSkillValue | StringField / '' | 50 | Значение проверки блока; форма type=number в monster-knowledge:11–12. |
| showAcademicKnowledge | BooleanField / true | 51–54 | Видимость второго блока; monster-knowledge:9. |
| monsterLore | HTMLField / '' | 55 | Ведьмачьи знания, enrichedText:71. |
| monsterLoreSkillValue | StringField / '' | 56 | Значение проверки блока; форма type=number в monster-knowledge:18–19. |
| showMonsterLore | BooleanField / true | 57 | Видимость третьего блока; monster-knowledge:16. |
| customStat | BooleanField / false | 59 | Отключает автоматические ветки calculateDerivedStat для hp/sta и расчёт resolve/focus по текущим статам; это шире подписи CustomHP/STA. |
| addMeleeBonus | BooleanField / false | 60 | Разрешает включение бонуса BODY в атаки монстра с applyMeleeBonus; weaponAttackMixin:15, professionMixin:59. |
| dontAddAttr | BooleanField / false | 61 | Убирает характеристику из формул rollSkillCheck/rollCustomSkillCheck; skillMixin:60,149. |
| hasTailWing | BooleanField / false | 62 | Условие добавления tailWing в WitcherActor.getAllLocations:295; текущая передача контекста нарушена, issue-00032. |

Собственные определения не задают choices для строк и min/max/integer для чисел. HTML input type=number у трёх SkillValue не меняет StringField модели. Модель не содержит вычисляемого getter для награды, сопротивлений или регенерации.

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| static defineSchema:7–64 | CommonActorData, поля Foundry | Объект 53 полей | super.defineSchema и 34 дополнения | Синхронно; не сохраняет Actor и не регистрирует обработчики. |
| async enrichedText:66–74 | common, academicKnowledge, monsterLore; this.schema | Promise<{lore:{common,academicKnowledge,monsterLore}}> | Три последовательных await createEnrichedText с путями одноимённых полей | Каждый результат имеет enriched/value/systemField; без catch/сохранения. Ошибка раннего await прервёт следующие вызовы. |

prepareBaseData, calcCurrencyWeight и три метода миграции наследуются от CommonActorData. Собственного prepareDerivedData нет. Даже скрытые флагом show* знания проходят enrichedText: флаги проверяет шаблон, метод их не читает.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| CommonActorData; super.defineSchema | [module/data/actor/commonActorData.js](../../../../../../../module/data/actor/commonActorData.js); [карточка](commonActorData.js.md) | Импорт:1 / наследование:6 / вызов:8 | 19 общих полей и методы | Сверены реальные классы; общие fields не заменены. |
| createEnrichedText | [module/data/dataUtils.js](../../../../../../../module/data/dataUtils.js); [карточка](../dataUtils.js.md) | Импорт:2 / вызовы:69–71 | Обогащение трёх HTML-полей | Транзитивно вызывает TextEditor.implementation.enrichHTML и schema.getField. |
| StringField, NumberField, BooleanField, ArrayField, HTMLField | Foundry 14.367.0: /opt/foundryvtt/common/data/fields.mjs | Глобальный API fields:4 | Определения собственных полей | Настоящая схема/экземпляры проверены. |
| WITCHER.Monster.* — 10 label-ключей | [lang/en.json](../../../../../../../lang/en.json); [lang/ru.json](../../../../../../../lang/ru.json) | Строковые метаданные схемы | Поля resistance, regeneration, show*, customStat, addMeleeBonus, dontAddAttr, hasTailWing | В обеих локализациях найдены все 10 ключей; это не импорт функций перевода. |

Точные label: WITCHER.Monster.resistantNonSilver, WITCHER.Monster.resistantNonMeteorite, WITCHER.Monster.regeneration, WITCHER.Monster.CommonerSuperstition, WITCHER.Monster.AcademicKnowledge, WITCHER.Monster.WitcherKnowledge, WITCHER.Monster.CustomHP/STA, WITCHER.Monster.addMeleeBonus, WITCHER.Monster.dontAddAttr, WITCHER.Monster.hasTailWing.

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/setup/registerDataModels.js](../../../../../../../module/setup/registerDataModels.js); [system.json](../../../../../../../system.json); [module/setup/registerSheets.js](../../../../../../../module/setup/registerSheets.js) | MonsterData; monster; три htmlFields | Регистрация модели, типа и листа | Тип согласован; issue-00005 касается mystery и трёх Item, не monster. |
| [module/actor/sheets/WitcherMonsterSheet.js](../../../../../../../module/actor/sheets/WitcherMonsterSheet.js) | system.schema.fields; enrichedText() | _prepareContext:123–125 ожидает модель и добавляет результат в контекст | Используется текущий зарегистрированный лист. |
| [templates/sheets/actor/partials/monster/tabs/partials/monster-knowledge.hbs](../../../../../../../templates/sheets/actor/partials/monster/tabs/partials/monster-knowledge.hbs) | Три HTML, три show*, три SkillValue | Формы и условный вывод; в enriched передаётся .value | 2–21; issue-00013, не ошибка возвращаемой структуры модели. |
| [templates/sheets/actor/partials/monster/tabs/partials/monster-info.hbs](../../../../../../../templates/sheets/actor/partials/monster/tabs/partials/monster-info.hbs); [templates/sheets/actor/partials/monster/tabs/partials/monster-status.hbs](../../../../../../../templates/sheets/actor/partials/monster/tabs/partials/monster-status.hbs) | Описательные поля и statusEffectImmunities | Поля формы / multi-select | info:4–20; status:3–13 |
| [templates/sheets/actor/partials/monster/header.hbs](../../../../../../../templates/sheets/actor/partials/monster/header.hbs); [templates/sheets/actor/partials/monster/sidebar.hbs](../../../../../../../templates/sheets/actor/partials/monster/sidebar.hbs) | category, threat, difficulty | Подписи через CONFIG.WITCHER и путь картинки | header:10–18; sidebar:3; assets вне пофайлового анализа. |
| [module/actor/sheets/configurations/WitcherMonsterConfigurationSheet.js](../../../../../../../module/actor/sheets/configurations/WitcherMonsterConfigurationSheet.js); [templates/sheets/actor/configuration/monster/general.hbs](../../../../../../../templates/sheets/actor/configuration/monster/general.hbs) | system, schema.fields; флаги и regeneration | Контекст:56–58; formGroup; при customStat поля hp/sta/resolve.unmodifiedMax | general:2–21; сохранение формы не запускалось. |
| [module/actor/witcherActor.js](../../../../../../../module/actor/witcherActor.js) | customStat, statusEffectImmunities, hasTailWing | calculateDerivedStat:163–184; applyStatus:206; static getAllLocations:295 | Контекст последних двух вызовов проверен отдельно; issues31/32. |
| [module/actor/mixins/armorMixin.js](../../../../../../../module/actor/mixins/armorMixin.js) | armorHead/Upper/Lower/TailWing | Суммирование природной брони и уменьшение SP | 30–61,269–281; по коду, не полный бой. |
| [module/actor/mixins/damageMixin.js](../../../../../../../module/actor/mixins/damageMixin.js) | category; список локаций через getAllLocations | Совпадение с oilEffect; applyDamageToAllLocations | 16,85–96; второй путь зависит от locationMixin. |
| [module/actor/mixins/weaponAttackMixin.js](../../../../../../../module/actor/mixins/weaponAttackMixin.js); [module/actor/mixins/professionMixin.js](../../../../../../../module/actor/mixins/professionMixin.js); [module/actor/mixins/skillMixin.js](../../../../../../../module/actor/mixins/skillMixin.js) | addMeleeBonus, dontAddAttr | Ветви построения урона и броска | 15;59;60,149 соответственно. |
| [module/actor/mixins/locationMixin.js](../../../../../../../module/actor/mixins/locationMixin.js) | Доступ к hasTailWing через static getAllLocations | Обёртка экземпляра вызывает метод класса без передачи Actor | 4–5; issue-00032. |
| [module/scripts/combat/generalCombatHook.js](../../../../../../../module/scripts/combat/generalCombatHook.js) | regeneration; hp.value/max | Для monster, ненулевой regeneration и без dead: min(value+regeneration,max), Actor.update | 11–38; общий hook требует активного GM. |
| [module/scripts/combat/applyDamage.js](../../../../../../../module/scripts/combat/applyDamage.js) | resistantNonSilver/resistantNonMeteorite | Исходное состояние галочек диалога урона | 65–66; не непосредственное сопротивление в defineSchema. |
| [module/scripts/statusEffects/applyStatusEffect.js](../../../../../../../module/scripts/statusEffects/applyStatusEffect.js) | statusEffectImmunities | applyStatusEffectToActor:65; сверяет переданный statusEffectId и планирует toggle | Здесь statusEffectId — параметр; отличается от ошибочного WitcherActor.applyStatus. |
| [templates/sheets/actor/monster-sheet.hbs](../../../../../../../templates/sheets/actor/monster-sheet.hbs) | bounty и другие поля | Старая монолитная форма | 116–118; текущий PARTS WitcherMonsterSheet использует раздельные шаблоны, достижимость старого листа не утверждается. |

Область поиска — module/, templates/, packsJson/; потребители общих полей — в CommonActorData и вложенных карточках. Строки resistances/immunities/susceptibilities не превращаются данной моделью в боевые эффекты. Зафиксированная текстовая форма не доказывает отсутствие внешних модулей, читающих эти строки.

## Данные и изменения состояния

Собственные методы собирают схему и отдельный контекст lore. enrichedText не заменяет исходные HTML; проверенный снимок модели сохранился. Изменения HP при регенерации, брони при повреждении, применение статусов и записи из форм выполняются в перечисленных потребителях. Общая подготовка баз описана в CommonActorData, а конечные расчёты — в WitcherActor.

Значение customStat влияет и на resolve/focus: в calculateDerivedStat ветка !customStat использует текущие WILL/INT, а при true остаётся unmodifiedMax+totalModifiers. Подпись настройки и вычисление описаны раздельно; соответствие игровым правилам не оценивалось.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Полнота | 75 строк; два импорта; настоящая MonsterData.schema | 53 поля =19+34; отсутствуют поля CharacterData | Самостоятельного игрового Actor не создано. |
| Enrichment | Три исходных вызова с подменой TextEditor | systemField.fieldPath: system.common, system.academicKnowledge, system.monsterLore; value/enriched раздельны | Без браузерного редактора. |
| Подписи | expandObject en/ru JSON + 10 label из реальной схемы | 10/10 найдено в каждой локализации | Не проверка качества перевода. |
| Иммунитеты | Исходный applyStatus; настоящая MonsterData, Set; toggleStatusEffect подменён записью вызовов | [] проходит; любой из ['bleeding']/['unrelated'] даёт ReferenceError statusEffectId после вызова toggle | Не запись статуса/БД; issue-00031. |
| Контекст локаций | Оригинальные static getAllLocations и locationMixin.getAllLocations, actor.type=monster/hasTailWing=true | Через текущую обёртку 6 локаций без tailWing; при явном this=actor тот же static возвращает 7 | Контроль причины потери контекста; полный расчёт урона не запускался. |

## Непроверенные участки и открытые вопросы

Файл полностью прочитан. UI/БД, регенерация в настоящем бою, все варианты сопротивлений и влияние внешних модулей не запускались. Старый monster-sheet не приравнен к текущему PARTS. Разбор mystery и всего Actor остаётся вне четырёх файлов этой порции; соседние методы просмотрены только для установления связей.

## Связанные проблемы

- [issue-00013](../../../../../../issues/potential/issue-00013.md) — редактор знаний получает исходный value вместо enriched.
- [issue-00018](../../../../../../issues/potential/issue-00018.md) — потребитель навыков игнорирует настройку видимости монстра.
- [issue-00030](../../../../../../issues/potential/issue-00030.md) — вкладка IP использует отсутствующие поля персонажа.
- [issue-00031](../../../../../../issues/potential/issue-00031.md) — неопределённый statusEffectId в обработчике иммунитетов Actor.
- [issue-00032](../../../../../../issues/potential/issue-00032.md) — потеря контекста монстра при перечислении локаций с хвостом/крылом.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.006 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.
