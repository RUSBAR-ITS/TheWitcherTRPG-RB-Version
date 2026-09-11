# module/actor/sheets/mixins/skillMixin.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/actor/sheets/mixins/skillMixin.js](../../../../../../../../module/actor/sheets/mixins/skillMixin.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `273a6d7db0b7c866399db3ecd4f7191817ae6f10` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.029](../../../../../../../tasks/task-0003.029.md), 14 файлов, 763 логических строк |
| Запись перекрёстной сверки | [TASK-0003.029](../../../../../review-log.md#task-0003029) |

## Назначение файла

Общая примесь листа для суммы встроенных навыков, сворачивания старых групп и подключения броска/повышения навыка.

## Условия использования

Присоединена к V2 и V1 ActorSheet, а также к WitcherModifiersConfiguration. calc_total_skills вызывается CharacterSheet. Требует actor, skillMap, game.i18n и DOM/jQuery; методы формы используют data-атрибуты, а не определяют навык по подписи.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| skillMixin | export let, весь файл | Три метода листа | Object.assign прототипов листов и конфигурации | Сумма контекста; события клика |
| jQuery | Присваивание в skillListener | Контейнер результата $(html) | Глобальное имя без локального объявления | Заменяет глобальную функцию объектом; при отсутствующем глобальном binding бросает ReferenceError |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| calc_total_skills(context) | context.system.skills, label/value каждой модели | Число totalSkills | Два for..in; локализует label; удваивает value, если подпись содержит '(2)' | Не читает costMultiplier, Item-навыки, профессию, isVisible и флаги выбора. Зависит от наличия label и переводов |
| _onSkillDisplay(event) | closest('.skill').dataset.skilltype и actor.system.pannels | Нет возвращаемого результата | preventDefault; инвертирует system.pannels.<skilltype>IsOpen | actor.update не ожидается и не возвращается |
| skillListener(html) | DOM с querySelectorAll, actor и skillMap | Регистрация четырёх групп обработчиков | profession-roll → _onProfessionRoll; skill-display → _onSkillDisplay; rollSkill → rollSkillCheck; level-up → levelUpSkill | jQuery = $(html) меняет глобальную переменную; неизвестный data-skill передаёт undefined; проверки возможности повышения нет |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| rollSkillCheck / levelUpSkill | [module/actor/mixins/skillMixin.js](../../../../../../../../module/actor/mixins/skillMixin.js) | Методы Actor | Передача описания skillMap либо ключа кнопки | Два querySelectorAll в skillListener |
| _onProfessionRoll | [module/actor/mixins/professionMixin.js](../../../../../../../../module/actor/mixins/professionMixin.js) | Метод Actor | Обработчик .profession-roll | skillListener; метод ищет профессию и маршрут броска |
| Skill.label/value; Pannels | [module/data/actor/templates/common/skills/skillData.js](../../../../../../../../module/data/actor/templates/common/skills/skillData.js); [module/data/actor/templates/character/pannelsData.js](../../../../../../../../module/data/actor/templates/character/pannelsData.js) | Поля моделей | Суммирование и состояние старого списка | calc_total_skills / _onSkillDisplay |
| WITCHER.skillMap | [module/setup/config.js](../../../../../../../../module/setup/config.js) | Контекст this.skillMap листа | Преобразование ключа DOM в описание навыка | skillListener |
| Шаблоны строк и редактора | [templates/partials/character/skill-display.hbs](../../../../../../../../templates/partials/character/skill-display.hbs); [templates/partials/character/custom-skill-display.hbs](../../../../../../../../templates/partials/character/custom-skill-display.hbs); [templates/partials/monster/monster-skill-tab.hbs](../../../../../../../../templates/partials/monster/monster-skill-tab.hbs); [templates/partials/monster/monster-skill-display.hbs](../../../../../../../../templates/partials/monster/monster-skill-display.hbs); [templates/sheets/actor/configuration/app/edit-skills.hbs](../../../../../../../../templates/sheets/actor/configuration/app/edit-skills.hbs) | DOM-контракт | data-action=rollSkill/level-up, skill-display и skilltype | Буквальные селекторы и атрибуты |
| $, jQuery, HTMLElement; game.i18n | Foundry и браузер; переводы — lang/en.json, lang/ru.json | Внешний API | Обёртка DOM, регистрация событий и поиск '(2)' в переводе | Прямые вызовы; ES module выполняется в строгом режиме |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/actor/sheets/WitcherActorSheet.js](../../../../../../../../module/actor/sheets/WitcherActorSheet.js) | skillMixin | Импорт, Object.assign; activateListeners → skillListener | Прямой импорт и вызов |
| [module/actor/sheets/WitcherActorSheetV1.js](../../../../../../../../module/actor/sheets/WitcherActorSheetV1.js) | skillMixin | Аналогичное присоединение для старого базового листа | Прямой импорт и вызов |
| [module/actor/sheets/configurations/WitcherModifiersConfiguration.js](../../../../../../../../module/actor/sheets/configurations/WitcherModifiersConfiguration.js) | skillMixin | Импорт/Object.assign и подключение событий редактора | activateListeners |
| [module/actor/sheets/WitcherCharacterSheet.js](../../../../../../../../module/actor/sheets/WitcherCharacterSheet.js) | calc_total_skills | Заполняет context.totalSkills; отдельно считает профессию | _prepareCharacterData |

Область поиска: module/ и templates/ текущего checkout; прямые импорты и места вызова сверены отдельно от динамических обращений. Типы и листы сверены с system.json, module/setup/registerDataModels.js и module/setup/registerSheets.js. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Суммирование не изменяет Actor. В нём коэффициент определяется переводом label, а не skillMap.costMultiplier. Старый переключатель пишет system.pannels; клики делегируют мутации и броски Actor. Присваивание jQuery — отдельное глобальное изменение, не поле контекста.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Функции и подключения | 42 строки полностью; поиск импортов и четырёх селекторов | 3 метода; два базовых листа и конфигурация; CharacterSheet использует сумму | Класс конфигурации полностью описан в TASK-0003.030 |
| Сумма настоящих моделей | 52 навыка уровня 1; свежие модели и модели с мигрированными label; en/ru | Без label: 52. После заполнения label: 64 в обоих языках; флаги не меняют итог | Это зависимость от существующих данных; не новая проверка всех языков |
| События | Настоящие методы, контролируемая DOM-обёртка и записывающий Actor | Бросок/повышение получили ключи; pannels инвертирован; jQuery заменён объектом; без binding получен ReferenceError | Полный браузерный цикл рендера не воспроизводился |
| Ключ Item против встроенного | Реальный Handlebars текущей custom-строки + обработчик | Item.name попадает в skillMap lookup; неизвестное имя приводит к ошибке Actor | Событие вызвано изолированно по данным отрендеренной строки |

## Непроверенные участки и открытые вопросы

Повторная регистрация событий в живом браузере, все языки, профессиональные броски и их формулы в этой порции не исследовались. Итог calc_total_skills — сумма встроенных навыков с весом из подписи; его смысл для правил создания персонажа отдельно не устанавливался.

## Связанные проблемы

[issue-00004](../../../../../../../issues/potential/issue-00004.md), [issue-00015](../../../../../../../issues/potential/issue-00015.md), [issue-00167](../../../../../../../issues/potential/issue-00167.md), [issue-00187](../../../../../../../issues/potential/issue-00187.md), [issue-00192](../../../../../../../issues/potential/issue-00192.md). Глобальный jQuery, незаполненные label и ключи соотнесены с прежними issues; проблемы текущих строк и повышения у монстра описаны отдельно.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `273a6d7db0b7c866399db3ecd4f7191817ae6f10`; полный файл | Первая карточка; [сверка порции](../../../../../review-log.md#task-0003029) |

## Уточнение TASK-0003.030

2026-09-11, `aa6af106e86a9c75fe050d599f961c8fadb74f1b`. Класс WitcherModifiersConfiguration теперь полностью описан: две части, context.config ссылка, замена statLabels и последовательное подключение stat/skillListener. Полный разбор подтвердил сохранение проблемы глобального jQuery; соседний statListener использует только локальный html.

Сверенные источники: [module/actor/sheets/configurations/WitcherModifiersConfiguration.js](../../../../../../../../module/actor/sheets/configurations/WitcherModifiersConfiguration.js); [module/actor/sheets/mixins/statMixin.js](../../../../../../../../module/actor/sheets/mixins/statMixin.js). [Итоговая сверка третьей серии, сценарии и ограничения](../../../../../review-log.md#task-0003030). Код и статусы проблем не менялись.
