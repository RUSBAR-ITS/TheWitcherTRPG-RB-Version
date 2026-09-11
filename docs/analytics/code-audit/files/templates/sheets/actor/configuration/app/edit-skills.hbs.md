# templates/sheets/actor/configuration/app/edit-skills.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/sheets/actor/configuration/app/edit-skills.hbs](../../../../../../../../../templates/sheets/actor/configuration/app/edit-skills.hbs) |
| Тип файла | Handlebars |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `273a6d7db0b7c866399db3ecd4f7191817ae6f10` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.029](../../../../../../../../tasks/task-0003.029.md), 14 файлов, 763 логических строк |
| Запись перекрёстной сверки | [TASK-0003.029](../../../../../../review-log.md#task-0003029) |

## Назначение файла

Редактор группы встроенных навыков: базовый уровень, повышение через IP, три флага происхождения и read-only активная добавка.

## Условия использования

PARTS.skills WitcherModifiersConfiguration получает system и skillKey. Конфигурацию открывают текущие CharacterSheet и MonsterSheet через openModifiers; skillListener подключает data-action=level-up.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| with lookup system.skills skillKey / each skillGroup | Строки 1–45 | Выбор одной группы и перебор моделей Skill | @root.skillKey сохраняет атрибут внутри each | Неверный skillKey даёт пустое содержимое edit-stats |
| value / isProfession / isPickup / isLearned | Строки 6–27 | Четыре редактируемых поля каждого навыка | Пути system.skills.{{@root.skillKey}}.{{skillName}}.* | value number, флаги checkbox |
| button level-up | Строки 9–10 | Повышение навыка | data-skill={{skillName}} | Доступность не зависит от типа Actor и наличия IP |
| activeEffectModifiers | Строки 29–42 | Просмотр активной добавки | Два disabled input с подписью эффекта | Ноль скрывается, отрицательные значения показываются |

## Основные функции и методы

JS-функций нет. checked отражает три булевых поля; localize выводит skill.label, подписи флагов, levelUp и activeEffect.tab. @root устраняет смену контекста вложенных with/each. Кнопка вызывает levelUpSkill через листовую примесь; собственного submit/action обработчика HBS не содержит.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| WitcherModifiersConfiguration | [module/actor/sheets/configurations/WitcherModifiersConfiguration.js](../../../../../../../../../module/actor/sheets/configurations/WitcherModifiersConfiguration.js) | PARTS, контекст и жизненный цикл | system/skillKey; submitOnChange=true; _onRender → activateListeners | Определения в классе; полный аудит запланирован в .030 |
| Skill | [module/data/actor/templates/common/skills/skillData.js](../../../../../../../../../module/data/actor/templates/common/skills/skillData.js) | Модель группы | value/label, isProfession/isPickup/isLearned, activeEffectModifiers | Пути HBS и поля модели |
| skillListener / levelUpSkill | [module/actor/sheets/mixins/skillMixin.js](../../../../../../../../../module/actor/sheets/mixins/skillMixin.js); [module/actor/mixins/skillMixin.js](../../../../../../../../../module/actor/mixins/skillMixin.js) | Событие → Actor | Ключ button → стоимость, журнал, повышение | data-action=level-up |
| openModifiers | [module/actor/sheets/WitcherCharacterSheet.js](../../../../../../../../../module/actor/sheets/WitcherCharacterSheet.js); [module/actor/sheets/WitcherMonsterSheet.js](../../../../../../../../../module/actor/sheets/WitcherMonsterSheet.js); [templates/partials/character/tab-skills.hbs](../../../../../../../../../templates/partials/character/tab-skills.hbs) | Действие открытия | Общая вкладка передаёт type=skill и skillKey; оба листа создают конфигурацию | Определения actions и вызов конструктора |
| CharacterData / MonsterData | [module/data/actor/characterData.js](../../../../../../../../../module/data/actor/characterData.js); [module/data/actor/monsterData.js](../../../../../../../../../module/data/actor/monsterData.js) | Схемы владельца | Только персонаж имеет logs, IP и magic, требуемые повышением | Сопоставление доступности кнопки и предусловий |
| with / lookup / each / checked / localize | Handlebars и Foundry VTT; lang/en.json, lang/ru.json | Внешние helper и локализация | Выбор группы, поля формы, подписи | WITCHER.skills.levelUp есть в en, отсутствует в ru |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/actor/sheets/configurations/WitcherModifiersConfiguration.js](../../../../../../../../../module/actor/sheets/configurations/WitcherModifiersConfiguration.js) | Весь HBS | PARTS.skills | Буквальная ссылка; собственного preload в setup/handlebars нет |

Область поиска: module/ и templates/ текущего checkout; прямые импорты и места вызова сверены отдельно от динамических обращений. Типы и листы сверены с system.json, module/setup/registerDataModels.js и module/setup/registerSheets.js. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Форма меняет встроенные навыки Actor, не Item-навыки. Сохранение value и трёх checkbox — стандартный submitOnChange владельца; повышение отдельно вызывает Actor.levelUpSkill. Disabled поля показывают activeEffectModifiers, не сохраняют его. HTML содержит tr/td внутри div skill-modifiers: parse5 удаляет эти табличные оболочки, сохраняя input; видимый дефект этим опытом не установлен.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Полный шаблон и контекст | 47 строк; класс конфигурации и оба openModifiers | @root.skillKey корректно задаёт пути; кнопка есть у персонажа и монстра | Полный разбор класса завершён в .030 |
| Настоящий Handlebars | Группы с нулевым/отрицательным уровнем/добавкой, флаги, неверный skillKey | Корректные пути и кнопки; неверная группа пустая; 0 добавки скрыт | Submit формы не воспроизводился |
| Повышение Monster | Настоящие MonsterData, конфигурация и levelUpSkill для обычного/магического навыка | Кнопка отрендерена; вызов бросает TypeError из-за отсутствующих logs/magic | Action вызван изолированно; не сеанс браузера |
| Локализация и структура HTML | Lookup en/ru и parse5 результата | RU levelUp отсутствует; непригодные tr/td оболочки отброшены, input сохранены | Нет вывода о полном CSS/визуальном поведении |

## Непроверенные участки и открытые вопросы

На этапе .029 класс WitcherModifiersConfiguration проверялся точечно; в .030 его полная карточка завершена. Наличие отсутствующего русского ключа не означает отсутствие английского fallback. Отдельный дефект HTML по одному восстановлению дерева не регистрировался.

## Связанные проблемы

[issue-00004](../../../../../../../../issues/potential/issue-00004.md), [issue-00015](../../../../../../../../issues/potential/issue-00015.md), [issue-00016](../../../../../../../../issues/potential/issue-00016.md), [issue-00017](../../../../../../../../issues/potential/issue-00017.md), [issue-00191](../../../../../../../../issues/potential/issue-00191.md), [issue-00192](../../../../../../../../issues/potential/issue-00192.md), [issue-00193](../../../../../../../../issues/potential/issue-00193.md). Повышение, ключи и подписи отражены в соответствующих issues, без автоматического подтверждения или исправления.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `273a6d7db0b7c866399db3ecd4f7191817ae6f10`; полный файл | Первая карточка; [сверка порции](../../../../../../review-log.md#task-0003029) |

## Уточнение TASK-0003.030

2026-09-11, `aa6af106e86a9c75fe050d599f961c8fadb74f1b`. Полный разбор владельца формы завершён: класс хранит type/skillKey независимо, оба PARTS по умолчанию рендерятся. Содержимое skills зависит от skillKey, а не type; обычный openModifiers передаёт соответствующую пару. Штатная форма отправляет все enabled поля, в том числе checkbox/value; ошибка повышения Monster остаётся.

Сверенные источники: [module/actor/sheets/configurations/WitcherModifiersConfiguration.js](../../../../../../../../../module/actor/sheets/configurations/WitcherModifiersConfiguration.js); [templates/sheets/actor/configuration/app/edit-stats.hbs](../../../../../../../../../templates/sheets/actor/configuration/app/edit-stats.hbs). [Итоговая сверка третьей серии, сценарии и ограничения](../../../../../../review-log.md#task-0003030). Код и статусы проблем не менялись.
