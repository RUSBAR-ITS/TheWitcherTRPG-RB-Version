# templates/sheets/actor/monster-sheet.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/sheets/actor/monster-sheet.hbs](../../../../../../../templates/sheets/actor/monster-sheet.hbs) |
| Тип файла | Handlebars |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `8b938d44a042749df027d8b58e28bb1d79638091` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.032](../../../../../../tasks/task-0003.032.md), 13 файлов, 973 логические строки |
| Запись перекрёстной сверки | [TASK-0003.032](../../../../review-log.md#task-0003032) |

## Назначение файла

Старый полный шаблон монстра: 334 строки с колонками характеристик, ресурсами, бронёй, классификацией, сведениями, действиями, старыми вкладками и знаниями. Файл прочитан и изолированно отрендерен целиком; активным шаблоном зарегистрированного V2-листа не является.

## Условия использования

Единственный найденный JS-потребитель пути — preloadHandlebarsTemplates. WitcherMonsterSheet использует PARTS других HBS; общий WitcherActorSheetV1 не выбирает этот template и сам не зарегистрирован. Предзагрузка не доказывает достижимость UI. Контекст старого файла исследован подачей текущей модели и явно загруженных partial.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| Имя и system.stats | 1–24 | Имя и базовые/итоговые характеристики | name; each stats кроме luck | value disabled/readonly, unmodifiedMax editable; stat-roll/data-stat |
| Производные показатели и ресурсы | 26–70 | derivedStats.value/max, отдельные Vigor/HP/STA/resolve | disabled без name и именованные editable ресурсы | resolve условен useVerbalCombat; temporary HP суффиксом |
| Четыре области брони | 71–92 | armorHead/armorUpper/armorLower/armorTailWing | number input | Не ограничены hasTailWing |
| Категория, угроза, сложность, награда | 94–119 | Сведения с редакторами | select category/threat/difficulty и input bounty | Эти редакторы отсутствуют в текущих формах |
| Иконки/общие сведения/портрет | 121–170 | 12 категорийных ветвей, 5 текстовых полей,Actor.img | if eq category; height/weight/environment/intelligence/organization | Старые имена картинок; img data-edit без современного data-action |
| Действия и изображения состояния | 172–222 | Init/death/crit/verbal; healthState.applied | Legacy class listeners | Readonly значения HP/STA/resolve/vigor; health отображается по applied, не сравнением с max |
| Девять значков спасбросков | 223–271 | Пороги deathSaves>0…8 | death-minus/plus | Начиная с 9 все девять одинаково активны; это предел изображения, не счётчика |
| Навигация и 5 partial | 275–307 | skills/profession/inventory/details/spells/effects | Legacy data-tab без data-action; profession только Humanoid | Профессиональная секция пуста; details partial содержит только whitespace |
| Три блока знаний | 310–331 | showCommonerSuperstition/commonSkillValue/common; showAcademicKnowledge/academicKnowledgeSkillValue/academicKnowledge; showMonsterLore/monsterLoreSkillValue/monsterLore | system.common/academicKnowledge/monsterLore | Редакторы raw HTML; visibility flags те же, что у текущего lore |

## Основные функции и методы

Программных функций нет. Ветви шаблона описаны выше; прямой записи Actor/Item, регистрации слушателей или экспорта добычи файл не выполняет.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| Источник старой предзагрузки | [module/setup/handlebars.js](../../../../../../../module/setup/handlebars.js) | загрузка | templatePath: 3 | Не регистрация листа |
| MonsterData/CommonActorData | [module/data/actor/monsterData.js](../../../../../../../module/data/actor/monsterData.js); [module/data/actor/commonActorData.js](../../../../../../../module/data/actor/commonActorData.js) | контекст/поля | Все system.* | Сверены типы и группы; для render использована настоящая модель с повторной миграцией label |
| Гипотетический общий контекст/события | [module/actor/sheets/WitcherActorSheetV1.js](../../../../../../../module/actor/sheets/WitcherActorSheetV1.js); [module/actor/sheets/WitcherActorSheet.js](../../../../../../../module/actor/sheets/WitcherActorSheet.js) | совместимость контракта | actor/system/config/effects и class listeners | Схожесть полей проверена; выбор старого шаблона этими классами не найден |
| MonsterTypes/monsterDifficulty/monsterComplexity | [module/setup/config.js](../../../../../../../module/setup/config.js) | словари | Три select | 12/4/3 значения; core selectOptions |
| Пять literal partial | [templates/partials/monster/monster-skill-tab.hbs](../../../../../../../templates/partials/monster/monster-skill-tab.hbs); [templates/partials/monster/monster-inventory-tab.hbs](../../../../../../../templates/partials/monster/monster-inventory-tab.hbs); [templates/partials/monster/monster-details-tab.hbs](../../../../../../../templates/partials/monster/monster-details-tab.hbs); [templates/partials/monster/monster-spell-tab.hbs](../../../../../../../templates/partials/monster/monster-spell-tab.hbs); [templates/partials/effect-part.hbs](../../../../../../../templates/partials/effect-part.hbs) | Handlebars partial | 289/296/299/302/305 | Все цели найдены/зарегистрированы в тесте; подробные старые skill/inventory/effect уже имеют карточки, spells — .039 |
| localize/eq/gte/gt/not/selectOptions/editor | [module/setup/handlebars.js](../../../../../../../module/setup/handlebars.js); [lang/en.json](../../../../../../../lang/en.json); [lang/ru.json](../../../../../../../lang/ru.json) | helpers/переводы | Поля,условия,редакторы | Системные сравнения, core not/editor/selectOptions, настоящий Localization; DOM-редактор заменён |
| CSS/ресурсы | [styles/monster-sheet.css](../../../../../../../styles/monster-sheet.css); [styles/monster-skill-tab.css](../../../../../../../styles/monster-skill-tab.css) | селекторы/пути | Старые колонки и resource img | CSS просмотрен по связям; assets исключены, наличие 11 категорийных файлов не подтвердилось |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/setup/handlebars.js](../../../../../../../module/setup/handlebars.js) | путь monster-sheet.hbs | preloadHandlebarsTemplates | Единственная найденная ссылка из JS на путь; поиск module/templates |

Область поиска: module/ и templates/ текущего checkout; прямые импорты и места вызова сверены отдельно от динамических обращений. Типы и листы сверены с system.json, module/setup/registerDataModels.js и module/setup/registerSheets.js. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Disabled input не должны участвовать в обычной форме; в тесте поле system.stats.int.value имело disabled, а unmodifiedMax — нет. У старого Vigor редактируется value, текущий sidebar показывает max. bounty — text input при NumberField модели. Category изображения прописаны вручную; 11 прежних множественных имён не существуют. Статусы healthState.applied только читаются. Редакторы знаний получают raw текст и стандартный editor без дополнительного обогащения в файле. Значения и подписи внутри динамических each/partial проверены по контексту.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Полный файл/достижимость | 13/23, поиск пути через rg | Handlebars.precompile и render проходят с core helper not; текущие PARTS не содержат путь; предзагрузка найдена | Контекст подан вручную; ни браузерный старый лист, ни V1 не запускались |
| Поля/ресурсы | 23 | Найдены category/threat/difficulty/bounty, readonly value; 12 category src, 11 отсутствуют | Проверка наличия assets, не анализ картинок или HTTP |
| Локализация | 25 | Буквальные ключи есть в en; остальные пределы описаны в общем журнале | Встроенные label модели не отождествляются с литералами файла |

## Непроверенные участки и открытые вопросы

Файл прочитан целиком. Мир, браузер, HTTP-доступ, Document.update и работа нескольких клиентов не запускались. Настоящие модели, Handlebars, core helpers и вычисления использовались с фасадами Application/DOM и перехватом записи; подробные границы — в журнале .032. CSS и ресурсы проверены только как зависимости, соседние файлы вне порции не засчитываются в покрытие. Поведение старых вложенных вкладок проверено только в пределах совместимости с данным шаблоном. Пустая profession/details не означает пустую текущую вкладку.

## Связанные проблемы

[issue-00013](../../../../../../issues/potential/issue-00013.md), [issue-00180](../../../../../../issues/potential/issue-00180.md), [issue-00209](../../../../../../issues/potential/issue-00209.md), [issue-00210](../../../../../../issues/potential/issue-00210.md). Старые ошибки не названы активными на текущем V2-листе. Новая issue-00210 явно ограничена старым ресурсным маршрутом.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `8b938d44a042749df027d8b58e28bb1d79638091`; полный файл | Первая карточка; [сверка порции](../../../../review-log.md#task-0003032) |
