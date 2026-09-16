# templates/dialog/combat/profession-attack.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/dialog/combat/profession-attack.hbs](../../../../../../../templates/dialog/combat/profession-attack.hbs) |
| Тип файла | Handlebars |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `b47ba02cdaebc6a66ad14a5638213b6eb24460b4` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.038](../../../../../../tasks/task-0003.038.md), 4 файла, 965 логических строк |
| Запись перекрёстной сверки | [TASK-0003.038](../../../../review-log.md#task-0003038) |

## Назначение файла

Содержимое модального окна профессиональной атаки без оружия:14 полей поправок/локации/типа урона и справочная формула damage.

## Условия использования

Только doProfessionAttackRoll после usesWeapon=false. Получает attackSkill,displayDmgFormula,meleeBonus,config. Оконные кнопки/размер/отмена задаются JS, не HBS. В preload не найден.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| profession_roll_sheet | 1–163 | Контейнер | Прямой renderTemplate | Подпись attackSkill.alias через localize |
| 10checkbox | 10–133 | Обстоятельства атаки | names см. ниже | Начально unchecked, нет вычислений |
| 2select | 18–40 | damageType/location | callback .value строки | config.damageTypes;9 фиксированных локаций |
| 2input number | 81/147 | customAtt/customDmg | value0, class small | Без min/max/step/required |
| displayDmgFormula/meleeBonus | 138–159 | Предпросмотр | meleeBonus через truthy if | 0 скрыт, отрицательный показан |

## Основные функции и методы

Функций нет. localize и selectOptions готовят подписи, if(meleeBonus) управляет справочной ячейкой. Арифметика, случайная локация, расход STA, модификаторы эффекта и запись сообщения выполняются в JS/соседних файлах.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| doProfessionAttackRoll | [module/actor/mixins/professionMixin.js](../../../../../../../module/actor/mixins/professionMixin.js) | Производитель context/consumer form | render87–90; callback118–136 | checked Boolean, .value String; не FormDataExtended |
| config.damageTypes | [module/setup/config.js](../../../../../../../module/setup/config.js) | Select | Нет selected: первый штатный вариант | Справочник локализованных типов |
| Локализация | [lang/en.json](../../../../../../../lang/en.json); [lang/ru.json](../../../../../../../lang/ru.json) | Подписи | WITCHER.Dialog.* | EN/RU с core fallback проверены |
| Helpers | Foundry14.367.0 / Handlebars4.7.9 | localize/selectOptions/if | Рендер окна | Native inputs заменены при исполнении callback |
| getLocationObject | [module/actor/witcherActor.js](../../../../../../../module/actor/witcherActor.js) | Косвенное поведение вариантов | 9 значений select передаются JS | Random выбирается после ответа; named torso−1, head−6 |
| preloadHandlebarsTemplates | [module/setup/handlebars.js](../../../../../../../module/setup/handlebars.js) | Отрицательная сверка | Не входит в preload | Прямая загрузка в Actor |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/actor/mixins/professionMixin.js](../../../../../../../module/actor/mixins/professionMixin.js) | profession-attack.hbs | renderTemplate + DialogV2.prompt | 87–136 |

Область поиска: module/ и templates/ текущего checkout; прямые импорты и места вызова сверены отдельно от динамических обращений. Типы и листы сверены с system.json, module/setup/registerDataModels.js и module/setup/registerSheets.js. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Названия 14 полей: isExtraAttack, damageType, location, outsideLOS, isAmbush, isPinned, isSilhouetted, customAtt, targetOutsideLOS, isActivelyDodging, isMoving, isProne, isBlinded, customDmg. default location=randomHuman (первый option), ещё randomMonster/head/torso/leftArm/rightArm/leftLeg/rightLeg/tailWing. Checkbox подписи указывают+3/+5/+4/+2 и−3/−2/−3/−2/−3; JS дополнительно штрафует extra−3. customAtt/customDmg default "0". Связанный prompt modal=true, width600, rejectClose=true, contentClasses scrollable. Поля extra есть, поля цены STA нет.

Предпросмотр не включает введённый позднее customDmg. meleeBonus показывает переданное значение, которое у монстра может не входить в actual damageFormula (issue244). Текст skill alias/displayDmgFormula экранирует Handlebars, арифметика не исполняется самим шаблоном. Проверка full browser validity/особых input values не выполнялась.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Форма/callback | Группы 07–10 | 14 полей; строки custom/type/location, bool checked; модификаторы проверены на Roll | Браузер не запускался |
| Локализация | Группа 20 | Все literal keys HBS доступны EN/RU после expandObject/fallback | Не полный аудит языков |

## Непроверенные участки и открытые вопросы

В TASK-0004.008 текущий файл и его связи сопоставлены с датированными протоколами TASK-0003.018/.019 (2026-09-10) и .038 (2026-09-11), в пределах относящихся к нему сценариев. Новых поведенческих запусков нет; прежние настоящие модели/методы и фасады различены в протоколе. Браузерный submit, мир, сеть и запись в БД не проверены. Установлены процессы R008-15, R008-17, R008-19, R008-20; оставшиеся границы: [U008-03](../../../../cross-check-0002.md#u008-03), [U008-04](../../../../cross-check-0002.md#u008-04), [U008-06](../../../../cross-check-0002.md#u008-06). Полный пофайловый разбор соседей в TASK-0003 не равен проверке клиентского lifecycle.

## Связанные проблемы

[issue-00238](../../../../../../issues/potential/issue-00238.md), [issue-00244](../../../../../../issues/potential/issue-00244.md). 238 — поле extra запускает ветку без собственного расхода STA;244 — справочный meleeBonus расходится с actual formula у монстра. Остальные ошибки producer описаны в карточке примеси.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `b47ba02cdaebc6a66ad14a5638213b6eb24460b4`; полный файл | Первая карточка; [сверка порции](../../../../review-log.md#task-0003038) |

## Дополнительная сверка TASK-0003.041

2026-09-12, rusbar-main, d5c7a4b871dce3aa55f4b8b589e62c3c9450f2d3; исходник не изменён.

Теперь полностью описан соседний [attack-sheet.css](../../../styles/attack-sheet.css.md): div.attack-sheet — общий с оружейным диалогом класс; word-wrap:break-all невалиден по W3C (267). [weapon-roll.css](../../../styles/weapon-roll.css.md) ограничен другим корневым классом, этот профессиональный шаблон ему не соответствует. issue-00244 расширена на отдельный оружейный preview монстра, исходный профессиональный путь сохранён.

[Сверка и ограничения](../../../../review-log.md#task-0003041). Уточнение связи не увеличивает пофайловое покрытие; исправления не выполнялись.

## Сквозная сверка TASK-0004.008

2026-09-14; rusbar-main, f96434101e0e827838c2e6a3e09da8933a9801ef. Исходник совпадает со срезом TASK-0001; изменено только описание.

Четырнадцать именованных контролов формируют callback прямой атаки: десять checkbox, две строки select, два custom number. Арифметика/STA/UUID принадлежат producer, а показ meleeBonus — переданному context; монстр может увидеть бонус вне фактической формулы.

Сопоставленные определения и потребители: [module/actor/mixins/professionMixin.js](../../../module/actor/mixins/professionMixin.js.md), [module/setup/config.js](../../../module/setup/config.js.md), [lang/en.json](../../../lang/en.json.md), [lang/ru.json](../../../lang/ru.json.md), [module/actor/witcherActor.js](../../../module/actor/witcherActor.js.md), [module/setup/handlebars.js](../../../module/setup/handlebars.js.md).

[Протокол и границы](../../../../review-log.md#task-0004008) — TASK-0004.008; процессы [R008-15](../../../../cross-check-0002.md#r008-15), [R008-17](../../../../cross-check-0002.md#r008-17), [R008-19](../../../../cross-check-0002.md#r008-19), [R008-20](../../../../cross-check-0002.md#r008-20). В этой порции выполнена статическая сверка; прежние опыты сохраняют свои даты и фасады. Новых поведенческих запусков нет; браузер, мир, сеть и запись в БД не запускались.
