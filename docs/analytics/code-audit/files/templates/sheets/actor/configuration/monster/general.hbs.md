# templates/sheets/actor/configuration/monster/general.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/sheets/actor/configuration/monster/general.hbs](../../../../../../../../../templates/sheets/actor/configuration/monster/general.hbs) |
| Тип файла | Handlebars |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `8b938d44a042749df027d8b58e28bb1d79638091` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.032](../../../../../../../../tasks/task-0003.032.md), 13 файлов, 973 логические строки |
| Запись перекрёстной сверки | [TASK-0003.032](../../../../../../review-log.md#task-0003032) |

## Назначение файла

Общая вкладка конфигурации монстра: пользовательские максимумы, регенерация, видимость знаний и боевые флаги. Все 22 строки прочитаны.

## Условия использования

PARTS.general конфигурации, tabs.general из единственной группы TABS.primary, подготовленной базовым Application.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| customStat и три max | 2–7 | Режим пользовательских ресурсов | customStat; derivedStats.hp/sta/resolve.unmodifiedMax | Три NumberField появляются только при true |
| regeneration | 8 | Регенерация | system.regeneration | Числовое поле из схемы |
| Три флага знаний | 10–12 | Показ lore | showCommonerSuperstition/showAcademicKnowledge/showMonsterLore | BooleanField |
| Боевые флаги | 15–21 | Состав броска/локации/сопротивления | dontAddAttr/addMeleeBonus/hasTailWing/resistantNonSilver/resistantNonMeteorite | BooleanField; конкретное применение живёт в соседних обработчиках |

## Основные функции и методы

Программных функций и экспортов нет. Ниже описаны поля/условия разметки и их контракт с моделями и обработчиками; собственной записи документа файл не выполняет.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| system/systemFields/tabs | [module/actor/sheets/configurations/WitcherMonsterConfigurationSheet.js](../../../../../../../../../module/actor/sheets/configurations/WitcherMonsterConfigurationSheet.js) | контекст | Все formGroup | Точная модель Actor и _getSkills отдельно |
| MonsterData/derivedStats | [module/data/actor/monsterData.js](../../../../../../../../../module/data/actor/monsterData.js); [module/data/actor/templates/common/stats/derivedStatsData.js](../../../../../../../../../module/data/actor/templates/common/stats/derivedStatsData.js) | схема | Флаги/числа/подписи | 10 полей без custom, 13 с ним |
| calculateDerivedStat; getAllLocations | [module/actor/witcherActor.js](../../../../../../../../../module/actor/witcherActor.js); [module/actor/mixins/locationMixin.js](../../../../../../../../../module/actor/mixins/locationMixin.js) | потребители | Пределы HP/STA/resolve и hasTailWing | Группы 05/24; Wrapper теряет this для монстра |
| dontAddAttr; addMeleeBonus | [module/actor/mixins/skillMixin.js](../../../../../../../../../module/actor/mixins/skillMixin.js); [module/actor/mixins/weaponAttackMixin.js](../../../../../../../../../module/actor/mixins/weaponAttackMixin.js); [module/actor/mixins/professionMixin.js](../../../../../../../../../module/actor/mixins/professionMixin.js) | соседний расчёт | Броски навыка и бонус ближнего боя | Проверены места чтения, полный бой не запускался |
| regeneration; resistantNon* | [module/scripts/combat/generalCombatHook.js](../../../../../../../../../module/scripts/combat/generalCombatHook.js); [module/scripts/combat/applyDamage.js](../../../../../../../../../module/scripts/combat/applyDamage.js) | соседние обработчики | Ход и диалог урона | Точечное чтение источников; без выполнения боя |
| formGroup | [module/setup/handlebars.js](../../../../../../../../../module/setup/handlebars.js) | core helper через Handlebars | Схема поля → input | Настоящие DataField.toFormGroup; createInput/createFormGroup фасады |
| Локализованные labels | [lang/en.json](../../../../../../../../../lang/en.json); [lang/ru.json](../../../../../../../../../lang/ru.json) | схема | localize=true | Назначены моделью, не объявляются новыми сущностями HBS |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/actor/sheets/configurations/WitcherMonsterConfigurationSheet.js](../../../../../../../../../module/actor/sheets/configurations/WitcherMonsterConfigurationSheet.js) | HBS general | PARTS.general | Путь/обращение сверены в исходнике |
| [templates/sheets/actor/partials/monster/tabs/partials/monster-knowledge.hbs](../../../../../../../../../templates/sheets/actor/partials/monster/tabs/partials/monster-knowledge.hbs) | show* flags | Видимость трёх lore блоков | Путь/обращение сверены в исходнике |
| [templates/sheets/actor/partials/monster/sidebar.hbs](../../../../../../../../../templates/sheets/actor/partials/monster/sidebar.hbs) | hp/sta/resolve и броня | Показ ресурсов; hasTailWing не скрывает armorTailWing | Путь/обращение сверены в исходнике |

Область поиска: module/ и templates/ текущего checkout; прямые импорты и места вызова сверены отдельно от динамических обращений. Типы и листы сверены с system.json, module/setup/registerDataModels.js и module/setup/registerSheets.js. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Все поля сохраняются общей формой; прямого обработчика в HBS нет. Включение customStat показывает три исходных максимума и не означает отмены прочих расчётов Actor. Положительность/целочисленность поля задаёт схема, не дополнительный код этого файла. Редакторов category/threat/difficulty/bounty нет.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Форма/сохранение модели | 04 | 10/13 input, bool и числа переданы через FormDataExtended/core _processFormData в MonsterData.updateSource | Без Document.update |
| Режимы/локации | 05/24 | Обычный HP40; custom HP90/STA70/resolve80; hasTailWing=true не добавил локацию через текущий wrapper | Проверены настоящие числовые методы, не бой |

## Непроверенные участки и открытые вопросы

Файл прочитан целиком. Мир, браузер, HTTP-доступ, Document.update и работа нескольких клиентов не запускались. Настоящие модели, Handlebars, core helpers и вычисления использовались с фасадами Application/DOM и перехватом записи; подробные границы — в журнале .032. CSS и ресурсы проверены только как зависимости, соседние файлы вне порции не засчитываются в покрытие.

## Связанные проблемы

[issue-00032](../../../../../../../../issues/potential/issue-00032.md), [issue-00209](../../../../../../../../issues/potential/issue-00209.md). Исправления не выполнялись; вывод ограничен указанными проверками.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `8b938d44a042749df027d8b58e28bb1d79638091`; полный файл | Первая карточка; [сверка порции](../../../../../../review-log.md#task-0003032) |
