# templates/sheets/actor/partials/character/sidebar.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/sheets/actor/partials/character/sidebar.hbs](../../../../../../../../../templates/sheets/actor/partials/character/sidebar.hbs) |
| Тип файла | Handlebars |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `928ce4e537c6a3fdc34f8b6fa3fcfdb5a669f68d` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.031](../../../../../../../../tasks/task-0003.031.md), 3 файла, 711 логических строк |
| Запись перекрёстной сверки | [TASK-0003.031](../../../../../../review-log.md#task-0003031) |

## Назначение файла

Боковая панель character: изображение Actor, индикатор здоровья, полосы и ввод ресурсов, щит, флаги игнорирования состояний, удача и условный адреналин. Полностью прочитана 161 строка. Биография, имена расы/профессии и окно наград принадлежат заголовку/другим вкладкам, не этой панели.

## Условия использования

WitcherCharacterSheet.PARTS.sidebar выбирает этот HBS. Прямой записи или регистрации событий нет: именованные input обслуживает общая форма ActorSheetV2, luck/adrenaline — statMixin, editImage — действие Foundry. Точный путь отсутствует в массиве предзагрузки setup/handlebars; наличие PARTS достаточно для отдельной загрузки через HandlebarsApplication.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| img.witcher-actor-img | 3–4 | Изображение Actor | src actor.img; title actor.name; data-action=editImage/data-edit=img | Изменение инициируется унаследованным action; alt='actor image' — литерал |
| .wound-state | 5–12 | Иконка состояния | Читает HP.unmodifiedMax и woundTreshold.value | HP>=unmodifiedMax: целое зелёное сердце; иначе >=threshold: зелёное треснувшее; иначе оранжевое |
| .status-section | 15–79 | HP/STA/toxicity/focus; условный resolve | progress и input | progress max читает текущий max; HP/STA input max=99, остальные max из модели |
| temporaryHpSum | 23–25 | Дополнительная подпись HP | combatEffects.temporaryEffects | Показывает '+ сумма' только при >=1; не прибавляет её к input/progress |
| vigor-display; shield-display | 81–103 | Vigor.max и editable shield.value | Условие truthiness vigor; числовой input щита | Нулевой Vigor скрыт, отрицательный показан; у щита нет min/max |
| wound-threshold-toggle; death-state-toggle | 104–129 | Игнорирование двух состояний | Checkbox system.healthState.*.ignored | checked читает flags; applied не изменяется этим шаблоном |
| luck-display | 130–143 | Удача и ручное редактирование | system.stats.luck.value, luck-minus/luck-reset | Input без min/max; кнопки обслуживает statMixin |
| adrenaline-display | 144–159 | Адреналин при useAdrenaline | system.adrenaline.value, adrenaline-minus/plus | Input без min/max; UI-флаг и серверная логика разделены |

## Основные функции и методы

Программных функций нет. Две ветви индикатора, conditional resolve/vigor/adrenaline, progress и именованные input задают представление и payload общей формы; действия определены вне HBS.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| PARTS.sidebar; контекст | [module/actor/sheets/WitcherCharacterSheet.js](../../../../../../../../../module/actor/sheets/WitcherCharacterSheet.js) | шаблон и данные | Текущий character | Определение пути и _prepareContext |
| useAdrenaline/useVerbalCombat; temporaryHpSum; общая форма | [module/actor/sheets/WitcherActorSheet.js](../../../../../../../../../module/actor/sheets/WitcherActorSheet.js) | контекст, наследование | Опции, сумма временного HP и автосохранение | 61–76; submitOnChange в DEFAULT_OPTIONS |
| healthState; stats/derivedStats; combatEffects | [module/data/actor/commonActorData.js](../../../../../../../../../module/data/actor/commonActorData.js); [module/data/actor/templates/common/stats/statData.js](../../../../../../../../../module/data/actor/templates/common/stats/statData.js); [module/data/actor/templates/common/stats/statsData.js](../../../../../../../../../module/data/actor/templates/common/stats/statsData.js); [module/data/actor/templates/common/stats/derivedStatsData.js](../../../../../../../../../module/data/actor/templates/common/stats/derivedStatsData.js); [module/data/actor/templates/common/combatEffectsData.js](../../../../../../../../../module/data/actor/templates/common/combatEffectsData.js) | поля модели | Значения/max/unmodifiedMax, threshold, флаги | Модели не задают общего лимита HP/STA=99 |
| calculateStats/calculateDerivedStats и применение состояний | [module/actor/witcherActor.js](../../../../../../../../../module/actor/witcherActor.js) | соседний расчёт/потребитель flags | Пределы отображения и последующая подготовка | Чтение healthState в calculateStat:88, вызываемом из prepareDerivedData; полный жизненный цикл не воспроизводился |
| statListener; _onLuckMinus/_onLuckReset/_onAdrenalineMinus/_onAdrenalinePlus | [module/actor/sheets/mixins/statMixin.js](../../../../../../../../../module/actor/sheets/mixins/statMixin.js) | DOM-события | Четыре кнопки | Селекторы совпадают; plus делегирует Actor.addAdrenaline |
| useOptionalAdrenaline/useOptionalVerbalCombat | [module/setup/settings.js](../../../../../../../../../module/setup/settings.js) | настройки через контекст | Условные панели | Flags проверены true/false |
| gte/checked/localize и переводы | [module/setup/handlebars.js](../../../../../../../../../module/setup/handlebars.js); [lang/en.json](../../../../../../../../../lang/en.json); [lang/ru.json](../../../../../../../../../lang/ru.json) | helpers/локализация | Пороги, checkbox, подписи | Фактический Localization + expandObject; четыре ключа flags отсутствуют в ru, fallback en |
| .char-sidebar/.char-image/.wound-state/.status-section | [styles/character-header.css](../../../../../../../../../styles/character-header.css); [styles/character/sheet.css](../../../../../../../../../styles/character/sheet.css) | CSS | Размещение и размер панели | Точечное чтение; полный CSS вне порции |
| editImage; FormDataExtended; DocumentSheet._processFormData | Foundry 14.367.0 | форма/действие | Изображение и ввод | application.mjs:2134–2161; document-sheet.mjs:507; настоящий разбор формы, DOM подменён |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/actor/sheets/WitcherCharacterSheet.js](../../../../../../../../../module/actor/sheets/WitcherCharacterSheet.js) | sidebar HBS | PARTS.sidebar | Путь 30; контекст передаётся листом |
| [module/actor/sheets/mixins/statMixin.js](../../../../../../../../../module/actor/sheets/mixins/statMixin.js) | luck/adrenaline classes | statListener | Кнопки и named поля — разные способы изменения |
| [module/actor/sheets/WitcherActorSheet.js](../../../../../../../../../module/actor/sheets/WitcherActorSheet.js) | input и контекст | activateListeners и форма ActorSheetV2 | Общее выделение input; настройка submitOnChange |

Область поиска: module/ и templates/ текущего checkout; прямые импорты и места вызова сверены отдельно от динамических обращений. Типы и листы сверены с system.json, module/setup/registerDataModels.js и module/setup/registerSheets.js. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

При двух включённых опциях форма имеет 10 input: восемь числовых (HP, STA, toxicity, focus, resolve, shield, luck, adrenaline) и два checkbox. Без resolve/adrenaline остаются восемь input. Все значения — текущие value; потолки progress читаются из max. Никакого универсального ограничения 1/10 этот HBS не вводит.

HTML max=99 у HP/STA не является верхней границей данных: в проверке FormDataExtended передал HP=120, настоящий CharacterData.updateSource его принял; штатный _onChangeForm вызывает _onSubmitForm без checkValidity. Реакция браузерных спиннеров и submit-событий отдельно не проверялась. Indicator сравнивает с unmodifiedMax: HP=40 при max=60/base=40 показывает целое сердце, HP=35 при max=35/base=40 — треснувшее. Временное HP и ignored/applied flags в эти сравнения не входят.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Условия/значения/флаги | 21,25; настоящий HBS, FormDataExtended, core _processFormData и CharacterData.updateSource | HP120, STA−2, luck−1 переданы; checked сохраняет bool; Vigor0 скрыт, −1 показан | DOM-фасад; сервер и native constraint validation не запускались |
| Индикатор | 22 | Текущий max и база дают разные признаки полного здоровья; ниже threshold — оранжевый | Синтетические подготовленные значения; частота таких Actor не изучалась |
| Переводы | 26 | Четыре ключа ignore/ignoreHint отсутствуют в ru, en fallback есть | 49 буквальных ключей всей порции; полные словари остальных языков не проверялись |

## Непроверенные участки и открытые вопросы

Файл прочитан полностью. Браузер/CSS/реальная запись Actor и работа editImage не запускались. Иконка показывает только указанные сравнения, а не доказанное состояние всей игровой механики. Все статусы и ресурсные методы не повторно тестировались: их definitions и прежние карточки сопоставлены с этой разметкой.

## Связанные проблемы

[issue-00203](../../../../../../../../issues/potential/issue-00203.md), [issue-00205](../../../../../../../../issues/potential/issue-00205.md). Индикатор и отсутствующие русские подписи зарегистрированы как potential; ограничения ввода 99 описаны без утверждения о серверном запрете значений выше 99.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `928ce4e537c6a3fdc34f8b6fa3fcfdb5a669f68d`; полный файл | Первая карточка; [сверка порции](../../../../../../review-log.md#task-0003031) |
