# templates/partials/character-header.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/partials/character-header.hbs](../../../../../../templates/partials/character-header.hbs) |
| Тип файла | Handlebars |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `928ce4e537c6a3fdc34f8b6fa3fcfdb5a669f68d` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.031](../../../../../tasks/task-0003.031.md), 3 файла, 711 логических строк |
| Запись перекрёстной сверки | [TASK-0003.031](../../../review-log.md#task-0003031) |

## Назначение файла

Заголовок текущего листа персонажа: редактирование имени, краткие сведения о расе, профессии, поле, возрасте, родине и отношении общества; кнопки действий, IP/награды и счётчик спасбросков. Полностью прочитаны 69 строк. Раса и профессия показываются именами Item; описаний и бонусов здесь нет.

## Условия использования

Выбран через WitcherCharacterSheet.PARTS.header. Также включён в setup/handlebars templatePath, что само по себе не является выбором листа. Получает общий контекст полного CharacterSheet. В файле нет JS, импорта, подключения listener или собственной записи; name сохраняется общей формой, клики обслуживают примеси и базовый лист.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| .char-header-center; input.charname | 1–3 | Контейнер и имя Actor | PARTS.header | name='name', text; значение actor.name экранируется Handlebars |
| .char-general | 4–44 | Краткая биография | Контекст CharacterSheet/CharacterData | race.name/profession.name/system.gender/general.age; родина/отношение общества |
| Ветки homeland | 22–39 | Item родины имеет приоритет над старым полем | homeland.system либо system.general.homeland | value='other' → otherValue; иначе WITCHER.Homelands.<value> |
| .char-button-list | 46–55 | Инициатива, STA, смерть, крит/провал, лечение, словесный бой | CSS classes для listeners | Последняя кнопка условна по useVerbalCombat |
| .improvement-points; .open-rewards | 56–59 | Обычные IP и окно наград | system.improvementPoints; CharacterSheet listener | В строке 58 отсутствует закрывающий </a>; HTML5-парсер восстанавливает лишние anchors |
| .death-section | 60–67 | Текущий deathSaves и reset/add | deathsaveMixin | Подсказки Reset/Add заданы буквально, не через localize |

## Основные функции и методы

Программных функций нет. Разметка определяет условия отображения и DOM-контракт; вычисление бросков и запись выполняются в файлах-потребителях.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| Контекст actor/race/profession/homeland; _renderRewards | [module/actor/sheets/WitcherCharacterSheet.js](../../../../../../module/actor/sheets/WitcherCharacterSheet.js) | PARTS, данные, listener | Имя, сведения, награды | PARTS.header; _prepareCharacterData; activateListeners .open-rewards |
| _onInitRoll/_onRecoverSta/_onCritRoll/_onVerbalCombat; useVerbalCombat | [module/actor/sheets/WitcherActorSheet.js](../../../../../../module/actor/sheets/WitcherActorSheet.js) | контекст и click | Шесть основных кнопок с делегированием части примесям | Базовый activateListeners и методы 250–299 |
| deathSaveListener; _onDeathSaveRoll/_removeDeathSaves/_addDeathSaves; healListeners | [module/actor/sheets/mixins/deathSaveMixin.js](../../../../../../module/actor/sheets/mixins/deathSaveMixin.js); [module/actor/sheets/mixins/healMixin.js](../../../../../../module/actor/sheets/mixins/healMixin.js) | примеси, DOM | death-roll/death-minus/death-plus/heal-button | reset сбрасывает счётчик целиком; кнопки сами не бросают кубик |
| gender/general/improvementPoints; deathSaves | [module/data/actor/characterData.js](../../../../../../module/data/actor/characterData.js); [module/data/actor/templates/character/generalData.js](../../../../../../module/data/actor/templates/character/generalData.js); [module/data/actor/commonActorData.js](../../../../../../module/data/actor/commonActorData.js) | чтение полей | Краткие сведения и счётчики | Пол находится в system.gender; age — system.general.age; deathSaves — CommonActorData |
| HomelandData; старое homelandData | [module/data/item/homelandData.js](../../../../../../module/data/item/homelandData.js); [module/data/actor/templates/character/general/homelandData.js](../../../../../../module/data/actor/templates/character/general/homelandData.js) | чтение модели | Приоритет Item и otherValue | Обе ветви проверены рендером |
| WITCHER.homelands/socialStanding; переводимые ключи | [module/setup/config.js](../../../../../../module/setup/config.js); [lang/en.json](../../../../../../lang/en.json); [lang/ru.json](../../../../../../lang/ru.json) | локализация | Подписи и динамические ключи | Core Localization string fallback; пустой homeland возвращает технический префикс, не объект словаря |
| localize/concat/eq/unless; загрузка | [module/setup/handlebars.js](../../../../../../module/setup/handlebars.js) | предзагрузка и helpers | Ветки и подписи | eq из системы; localize/concat и базовые операторы Handlebars/Foundry |
| useOptionalVerbalCombat | [module/setup/settings.js](../../../../../../module/setup/settings.js) | настройка через родительский контекст | Показ verbal-button | Зарегистрированный флаг, читается базовым листом |
| .char-header-center/.char-actions/.action/.death-counter; раскладка | [styles/character-header.css](../../../../../../styles/character-header.css); [styles/character/sheet.css](../../../../../../styles/character/sheet.css) | CSS-селекторы | Размеры, flex/gap и области заголовка | Прочитаны соответствующие определения; полный CSS остаётся вне этой порции |
| Actor.name; общая форма; HTML5 tree construction | Foundry 14.367.0; Handlebars 4.7.9; parse5 | внешний API | Заполнение и DOM | Настоящий render/parse; browser layout не проверялся |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/actor/sheets/WitcherCharacterSheet.js](../../../../../../module/actor/sheets/WitcherCharacterSheet.js) | header HBS | PARTS.header | Путь в строке 33; фактическое использование |
| [module/setup/handlebars.js](../../../../../../module/setup/handlebars.js) | Путь header HBS | loadTemplates при предзагрузке | templatePath:6 |
| [module/actor/sheets/WitcherActorSheet.js](../../../../../../module/actor/sheets/WitcherActorSheet.js) | DOM кнопок | Собственные и подключённые listeners | init-roll/recover-sta/crit-roll/verbal-button и примеси |
| [module/actor/sheets/mixins/deathSaveMixin.js](../../../../../../module/actor/sheets/mixins/deathSaveMixin.js) | death-roll/death-minus/death-plus | click callbacks | Три события сверены |
| [module/actor/sheets/mixins/healMixin.js](../../../../../../module/actor/sheets/mixins/healMixin.js) | heal-button | healListeners | Подключается базовым листом |

Область поиска: module/ и templates/ текущего checkout; прямые импорты и места вызова сверены отдельно от динамических обращений. Типы и листы сверены с system.json, module/setup/registerDataModels.js и module/setup/registerSheets.js. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Единственное именованное поле формы — name. Бонусов, минимумов/потолков или изменения IP этот HBS не задаёт. Локализация homeland использует item при наличии; пустой/неизвестный value может вывести ключ. Отдельные тире остаются даже при пустых сведениях.

Незакрытый .open-rewards создаёт после HTML5-разбора три ссылки: одну с иконкой в improvement-points, пустую в char-actions и пустую в death-section. Это проверено parse5; дополнительные клики по счётчику смерти или конкретное смещение в браузере не утверждаются.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Сведения/родина/видимость | Группа 19; настоящий Handlebars | Имя с HTML экранировано; родина Item заменяет старую; verbal-button появляется при true | Контекст с настоящей CharacterData и выбранными Item; без браузера |
| Незакрытая ссылка | 20; parse5.parseFragment и дерево родителей | 3 open-rewards вместо одной; две пустые | HTML5-разбор, не оценка реального layout |
| Сохранение имени | 25; FormDataExtended + DocumentSheet._processFormData | Payload содержит name Actor и поля панели | DOM-фасад и перехват записи |
| Ключи | 26; core Localization после expandObject | Ключи header есть в en/ru; динамические префиксы отделены | Reset/Add литералы, не полнота всех переводов системы |

## Непроверенные участки и открытые вопросы

Файл прочитан целиком. Не запускались полный браузерный лист, раскладка CSS, сетевые игровые действия, сохранение Actor.name в БД и пользовательские модули. Работа кнопок описана по сопоставлению с definitions/listeners; броски/лечение уже изучены в соседних порциях, полностью здесь не повторялись.

## Связанные проблемы

[issue-00202](../../../../../issues/potential/issue-00202.md). Незакрытая ссылка зарегистрирована как potential с доказанным результатом HTML5-разбора; визуальные последствия требуют браузерной проверки.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `928ce4e537c6a3fdc34f8b6fa3fcfdb5a669f68d`; полный файл | Первая карточка; [сверка порции](../../../review-log.md#task-0003031) |

## Дополнительная сверка TASK-0003.037

2026-09-11, `rusbar-main`, `639fde4bad4a7ba4c538d3b08ddc5cfd846ca75e`; исходники не менялись.

Ссылка .open-rewards ведёт через CharacterSheet._renderRewards к отдельному RewardsSheet с журналами IP/currency. Она не запускает начисление. Полный разбор назначения окна не исправляет незакрытую ссылку (issue202), зафиксированную в .031.

[module/actor/mixins/rewardsMixin.js](../../module/actor/mixins/rewardsMixin.js.md), [module/actor/rewardsSheet.js](../../module/actor/rewardsSheet.js.md), [module/app/reward/reward.js](../../module/app/reward/reward.js.md), [templates/chat/rewards.hbs](../chat/rewards.hbs.md).

[Перекрёстная сверка и ограничения](../../../review-log.md#task-0003037). Связанные файлы повторно в покрытие не добавлялись; исходники и статусы issues не менялись.

## Дополнительная сверка TASK-0003.049

2026-09-12, rusbar-main, 523c9b2616e19058b18f812ae0361c8a86366814. Исходный файл не изменён.

Полностью описаны character-header.css и общая сетка. Контейнер char-header-center получает позицию 2/1, а вложенные actions/button-list/death-counter — flex-правила. При useVerbalCombat=true настоящий HBS даёт шесть button-roll. HTML5-парсер по-прежнему восстанавливает дополнительные open-rewards из незакрытой ссылки (issue-00202); видимое смещение не измерялось.

Карточки CSS: [styles/character-header.css](../../styles/character-header.css.md), [styles/character/sheet.css](../../styles/character/sheet.css.md).

[Методика и результаты](../../../review-log.md#task-0003049). Соседний файл повторно в покрытие не включён; браузер и БД не запускались.
