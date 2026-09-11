# templates/sheets/actor/partials/monster/tabs/partials/monster-knowledge.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/sheets/actor/partials/monster/tabs/partials/monster-knowledge.hbs](../../../../../../../../../../../templates/sheets/actor/partials/monster/tabs/partials/monster-knowledge.hbs) |
| Тип файла | Handlebars |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `8b938d44a042749df027d8b58e28bb1d79638091` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.032](../../../../../../../../../../tasks/task-0003.032.md), 13 файлов, 973 логические строки |
| Запись перекрёстной сверки | [TASK-0003.032](../../../../../../../../review-log.md#task-0003032) |

## Назначение файла

Три блока знаний монстра: суеверия, академические сведения и ведьмачьи знания. У каждого отдельная видимость, сложность и HTML-поле; все 23 строки прочитаны.

## Условия использования

Подключается как partial в detailTabs.lore и предзагружается. Требует systemFields, document.system и enrichedText.lore из полного контекста.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| CommonerSuperstition | 2–8 | Суеверия | showCommonerSuperstition/commonSkillValue/common | Числовой input + formGroup HTMLField |
| AcademicKnowledge | 9–15 | Академические сведения | showAcademicKnowledge/academicKnowledgeSkillValue/academicKnowledge | Свой флаг и порог |
| MonsterLore | 16–22 | Ведьмачьи знания | showMonsterLore/monsterLoreSkillValue/monsterLore | Свой флаг и порог |

## Основные функции и методы

Программных функций и экспортов нет. Ниже описаны поля/условия разметки и их контракт с моделями и обработчиками; собственной записи документа файл не выполняет.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| MonsterData и CommonActorData | [module/data/actor/monsterData.js](../../../../../../../../../../../module/data/actor/monsterData.js); [module/data/actor/commonActorData.js](../../../../../../../../../../../module/data/actor/commonActorData.js) | модель/поля | system и systemFields | Пути сверены с определениями, использованы настоящие модели |
| Контекст листа | [module/actor/sheets/WitcherMonsterSheet.js](../../../../../../../../../../../module/actor/sheets/WitcherMonsterSheet.js); [module/actor/sheets/WitcherActorSheet.js](../../../../../../../../../../../module/actor/sheets/WitcherActorSheet.js) | PARTS/подготовка | actor/document/system, опции, записи enrichedText | Полный _prepareContext выполнен с Application-фасадом |
| helpers и переводы | [module/setup/handlebars.js](../../../../../../../../../../../module/setup/handlebars.js); [lang/en.json](../../../../../../../../../../../lang/en.json); [lang/ru.json](../../../../../../../../../../../lang/ru.json) | Handlebars/локализация | localize, concat, eq/gte, checked, selectOptions, formGroup/editor по месту | Системные helpers и core helpers сверены; DOM-элементы формы заменены |
| createEnrichedText | [module/data/dataUtils.js](../../../../../../../../../../../module/data/dataUtils.js) | подготовка HTML | enrichedText.lore.* | value — исходник, enriched — результат enrichHTML; HBS передаёт enriched=*.value |
| Настройки видимости | [templates/sheets/actor/configuration/monster/general.hbs](../../../../../../../../../../../templates/sheets/actor/configuration/monster/general.hbs) | связанные input | Три checkbox | Флаги сохраняются в той же модели |
| CSS-селекторы | [styles/monster/details.css](../../../../../../../../../../../styles/monster/details.css) | оформление | .monster-knowledge | Прочитаны нужные селекторы; полный CSS вне порции |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [templates/sheets/actor/partials/monster/tabs/tab-details.hbs](../../../../../../../../../../../templates/sheets/actor/partials/monster/tabs/tab-details.hbs) | partial | detailTabs.lore | Путь/обращение сверены в исходнике |
| [module/setup/handlebars.js](../../../../../../../../../../../module/setup/handlebars.js) | путь | preloadHandlebarsTemplates | Путь/обращение сверены в исходнике |

Область поиска: module/ и templates/ текущего checkout; прямые импорты и места вызова сверены отдельно от динамических обращений. Типы и листы сверены с system.json, module/setup/registerDataModels.js и module/setup/registerSheets.js. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Три *SkillValue в MonsterData являются StringField, хотя input number/data-dtype Number; запись может приводиться моделью к строке, границы/проверка броска здесь не задаются. formGroup передаёт raw значение из document.system и в enriched снова raw *.value, toggled=true. Наличие подготовленного *.enriched не означает его использование.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Видимость и обогащение | 10 | Три редактора и 3 числовых input; при всех flags=false блоки исчезают. В renderer передано @UUID..., хотя producer дал <p>@UUID...</p> | Настоящие модель/formGroup/HTMLField; HTMLProseMirrorElement.create заменён и записывает аргументы |

## Непроверенные участки и открытые вопросы

Файл прочитан целиком. Мир, браузер, HTTP-доступ, Document.update и работа нескольких клиентов не запускались. Настоящие модели, Handlebars, core helpers и вычисления использовались с фасадами Application/DOM и перехватом записи; подробные границы — в журнале .032. CSS и ресурсы проверены только как зависимости, соседние файлы вне порции не засчитываются в покрытие.

## Связанные проблемы

[issue-00013](../../../../../../../../../../issues/potential/issue-00013.md). Исправления не выполнялись; вывод ограничен указанными проверками.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `8b938d44a042749df027d8b58e28bb1d79638091`; полный файл | Первая карточка; [сверка порции](../../../../../../../../review-log.md#task-0003032) |
