# module/actor/sheets/configurations/WitcherModifiersConfiguration.js

## Текущее состояние — 14.3.1.00082

2026-09-19, TASK-0010.019. statRows.label выбирает statMap.labelFull → statMap.label → value.label. Полные имена производных отделены от model labels; пути сохранения/покупки уровня и PARTS прежние.

[Реализация, синтетические проверки и границы](../../../../../../task-0010-019-visual-checks.md). Ниже сохранены описания датированных прежних срезов.

## Текущее состояние — 14.3.1.00077

2026-09-19, TASK-0010.014–.018. DEFAULT_OPTIONS.position 820×620; PARTS со scrollable. Новый getter title локализует назначение редактора, _configureRenderOptions выбирает одну часть stats/skills. _prepareContext использует полное имя из CONFIG.WITCHER.statMap, сохраняет разделение source-базы и currentValue. _processFormData/покупка прежние: isManualDerivedStat, statMixin, skillMixin. Зависит от ключей WITCHER.Editor ru/en и шаблонов app/edit-*.

[Исходник](../../../../../../../../module/actor/sheets/configurations/WitcherModifiersConfiguration.js), [реализация и проверки](../../../../../../task-0010-ui-fixes.md). Локальная проверка пройдена; реальная игровая/визуальная приёмка ожидается (HTTP502). Следующие датированные разделы описывают прежние срезы.


## Текущее состояние — 14.3.1.00064

2026-09-18, TASK-0010.006. **Назначение:** Редактор сохранённых баз и действий прокачки.

**Методы, сущности, действия и зависимости:** _prepareContext выставляет canPurchase только character; базы/currentValue остаются раздельными. _processFormData расширяет native данные, разрешает только существующие primary базы/baseCap, builtin value/baseCap/флаги, ручные derived базы через общий isManualDerivedStat и reputation.unmodifiedMax. Автоматические max/value/базы не попадают в payload. Зависимости — derivedStatData, Foundry utils/form lifecycle; подписи/ручной режим .003/.005 сохранены.

[Исходник](../../../../../../../../module/actor/sheets/configurations/WitcherModifiersConfiguration.js), [проверки/границы](../../../../../../task-0010-006-checks.md). Ниже, если есть, сохранены датированные предыдущие срезы; изменённые операции описаны здесь.

## Предыдущие датированные проверки

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/actor/sheets/configurations/WitcherModifiersConfiguration.js](../../../../../../../../module/actor/sheets/configurations/WitcherModifiersConfiguration.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-16: актуализация технических обращений по issue-00001 |
| Ветка и коммит | `dev`, база `d8e0e1ad1159cb71a8769b0353f812de6f1ed4d8` + незакоммиченное исправление issue-00001 |
| Изменения относительно коммита | issue-00001; текущие технические обращения актуализированы. Прежние опыты ниже относятся к своим датам. |
| Задача и порция | [TASK-0003.030](../../../../../../../tasks/task-0003.030.md), 9 файлов, 424 логических строк |
| Запись перекрёстной сверки | [TASK-0003.030](../../../../../review-log.md#task-0003030) |

Актуализация [issue-00001](../../../../../../../issues/closed/issue-00001.md), 2026-09-16: Обращения к ресурсам и/или техническим namespaces переведены на TheWitcherTRPG-RB-Version. Формулы и порядок действий сохранены. Датированные проверки ниже выполнены до смены ID.

## Назначение файла

Общее окно редактора исходных характеристик, производных параметров и группы встроенных навыков.

## Условия использования

Default export extends HandlebarsApplicationMixin(ActorSheetV2). CharacterSheet и MonsterSheet создают его напрямую через openModifiers с document/type/skillKey; отдельной регистрации листом по умолчанию нет.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| WitcherModifiersConfiguration | Класс,6–68 | Окно конфигурации | Default export | Конструктор, контекст и слушатели |
| statMap / skillMap | Поля экземпляра,7–8 | Ссылки на CONFIG.WITCHER | Доступны обеим примесям | Снимок ссылки при создании, не копии карт |
| DEFAULT_OPTIONS | 18–31 | resizable, width520, классы witcher/sheet/actor/modifier-configuration | Статический объект | submitOnChange=true; closeOnSubmit=false; actions={} |
| PARTS.stats / skills | 33–40 | Два HBS редактора | Статический объект | Обе части поддерживаются; type фильтрует содержимое HBS, не список PARTS |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| constructor(options={}) | ActorSheetV2 options | Экземпляр | super(options); сохраняет type/skillKey | Не валидирует значения и не выбирает parts |
| _onRender(context,options) | Созданный element | Promise<void> | await super; activateListeners(this.element) | Регистрация двух примесей после каждого рендера; частичное повторное связывание в браузере не исследовано |
| activateListeners(html) | DOM, statListener/skillListener | Нет результата | Вызывает statListener, затем skillListener | Наследованные методы привязаны через Object.assign; skillListener перезаписывает глобальную jQuery |
| _prepareContext(options) | document.system, CONFIG.WITCHER | Promise<context> | await super; config — общая ссылка; заново создаёт config.statLabels из label??labelShort; system/type/skillKey | Изменяет глобальный CONFIG.WITCHER.statLabels; не копирует модели/карты и не обновляет Actor |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| skillMixin | [module/actor/sheets/mixins/skillMixin.js](../../../../../../../../module/actor/sheets/mixins/skillMixin.js) | Прямой named import / Object.assign | Сумма и слушатели навыков; level-up | 3,51,71 |
| statMixin | [module/actor/sheets/mixins/statMixin.js](../../../../../../../../module/actor/sheets/mixins/statMixin.js) | Прямой named import / Object.assign | Слушатели характеристик/ресурсов | 4,50,70 |
| edit-stats.hbs | [templates/sheets/actor/configuration/app/edit-stats.hbs](../../../../../../../../templates/sheets/actor/configuration/app/edit-stats.hbs) | Буквальный PARTS.stats | type stats/derivedStats определяет набор полей | 35 |
| edit-skills.hbs | [templates/sheets/actor/configuration/app/edit-skills.hbs](../../../../../../../../templates/sheets/actor/configuration/app/edit-skills.hbs) | Буквальный PARTS.skills | lookup system.skills skillKey, независимо от type | 38 |
| WITCHER.statMap / skillMap | [module/setup/config.js](../../../../../../../../module/setup/config.js) | Глобальная конфигурация | Ссылки экземпляра и производная statLabels | 7–8,56–60 |
| CharacterData / MonsterData | [module/data/actor/characterData.js](../../../../../../../../module/data/actor/characterData.js); [module/data/actor/monsterData.js](../../../../../../../../module/data/actor/monsterData.js) | document.system | Общий редактор не ограничен типом Actor | Создатели передают свой document |
| HandlebarsApplicationMixin / ActorSheetV2 / DocumentSheetV2 | Foundry 14.367; client/applications/api/{handlebars-application,document-sheet,application}.mjs | Наследование, рендер и форма | По умолчанию обе части; FormDataExtended всей формы; _processFormData → expanded submit → document.update | Core _configureRenderOptions:72–78, Application._onSubmitForm:2134–2144, DocumentSheet._processFormData:507–509 |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/actor/sheets/WitcherCharacterSheet.js](../../../../../../../../module/actor/sheets/WitcherCharacterSheet.js) | Класс | Импорт и new из #openModifiers | 7,468–478 |
| [module/actor/sheets/WitcherMonsterSheet.js](../../../../../../../../module/actor/sheets/WitcherMonsterSheet.js) | Класс | Импорт и new из #openModifiers | 3,213–223 |
| [templates/sheets/actor/configuration/app/edit-stats.hbs](../../../../../../../../templates/sheets/actor/configuration/app/edit-stats.hbs) | context.type/system | Выбирает stats/derivedStats | Весь wrapper |
| [templates/sheets/actor/configuration/app/edit-skills.hbs](../../../../../../../../templates/sheets/actor/configuration/app/edit-skills.hbs) | context.skillKey/system | Группа и @root.skillKey для input | Весь HBS |

Область поиска: module/ и templates/ текущего checkout; прямые импорты и места вызова сверены отдельно от динамических обращений. Типы и листы сверены с system.json, module/setup/registerDataModels.js и module/setup/registerSheets.js. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Настройки экземпляра type и skillKey существуют независимо. При обычном вызове stats/derivedStats skillKey не задан, поэтому часть skills пустая; type='skill' с int оставляет stats-wrapper пустым и показывает 13 навыков. Если одновременно задать type='stats' и skillKey='int', оба набора будут иметь содержимое — в классе нет взаимоисключающей проверки. Форму сохраняет Foundry; общая отправка включает все enabled именованные поля.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Класс, options и композиция | Полные 71 строки; imports, оба openModifiers, core render/form | 2 импорта/примеси,2 PARTS,4 собственных метода | Проверка core по определениям, не полное Application |
| Настоящий контекст/HBS | Группа 11: stats/derivedStats/skill/неизвестный/undefined | 10/12/52/0/0 полей соответственно; CONFIG.statLabels заменяется новым объектом; 8 jQuery-селекторов обеих примесей | Базовый Sheet и DOM-фасады |
| Отправка формы | Группы 14–15: настоящий FormDataExtended и DocumentSheet._processFormData | Соседнее поле с максимумом попадает в отправляемую исходную базу; производные пересчитываются | Валидация system настоящая, серверный Document.update не выполнялся |

## Непроверенные участки и открытые вопросы

Сверены producer контекста, HBS и именованные поля. Реальная обработка FormDataExtended из .030 — изолированное историческое доказательство; браузер, права и серверный submit не запускались. Точный остаток — [U003-04](../../../../../cross-check-0002.md#u003-04).

## Связанные проблемы

[issue-00167](../../../../../../../issues/potential/issue-00167.md), [issue-00192](../../../../../../../issues/closed/issue-00192.md), [issue-00194](../../../../../../../issues/closed/issue-00194.md), [issue-00195](../../../../../../../issues/closed/issue-00195.md). Полный разбор закрывает прежнюю границу .029 по этому классу, но не подтверждает и не исправляет issues.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `aa6af106e86a9c75fe050d599f961c8fadb74f1b`; полный файл | Первая карточка; [сверка порции](../../../../../review-log.md#task-0003030) |

## Уточнение TASK-0003.032

2026-09-11, `8b938d44a042749df027d8b58e28bb1d79638091`. Полный MonsterSheet action #openModifiers передаёт document/type/skillKey, preventDefault и render без ожидания. Это другое окно, чем WitcherMonsterConfigurationSheet; наличие обоих путей объясняет, почему настройка isVisible и повышение навыка относятся к разным обработчикам.

Связи: [module/actor/sheets/WitcherMonsterSheet.js](../WitcherMonsterSheet.js.md); [module/actor/sheets/configurations/WitcherMonsterConfigurationSheet.js](WitcherMonsterConfigurationSheet.js.md). [Результаты и пределы проверки](../../../../../review-log.md#task-0003032).

## Дополнительная сверка TASK-0003.047

2026-09-12, rusbar-main, 2f94c6c29e298ccf73d67ccc2e5fb8fc358dae2c; исходники не изменены.

Полностью разобран [CSS этого окна](../../../../styles/configurations/modifier-configuration.css.md). Его единственное свойство display:inherit у .window-content перекрывает более общую сетку Actor; width520 задаётся здесь в DEFAULT_OPTIONS, не в CSS. Классы witcher/sheet/actor/modifier-configuration сопоставлены с selector и :not(.extended-sheet). Порядок @import и специфичность установлены статически; реальное значение display родителя и геометрия окна не измерены.

[Сценарии, результаты и ограничения](../../../../../review-log.md#task-0003047). Связанные файлы повторно не засчитываются в покрытие.

## Сквозная сверка TASK-0004.003

2026-09-14; rusbar-main, b4aeecb967caf97700cc565a670d6347b933619f. Исходник совпадает со срезом TASK-0001; изменено только описание.

Конструктор хранит type/skillKey, оба PARTS существуют одновременно; type выбирает содержимое edit-stats, skillKey — edit-skills. _prepareContext передаёт живой document.system и изменяет CONFIG.statLabels. submitOnChange запускает общий сбор формы в core; stats-block показывает max в именованном поле unmodifiedMax. .030 проверяла реальную сериализацию формы/модели: соседний изменённый максимум попадает в базу (00194), отдельные производные перезаписываются расчётом (00195).

Сопоставленные определения и потребители: [module/actor/sheets/WitcherActorSheet.js](../WitcherActorSheet.js.md), [module/actor/sheets/WitcherCharacterSheet.js](../WitcherCharacterSheet.js.md), [module/actor/sheets/mixins/skillMixin.js](../mixins/skillMixin.js.md), [templates/sheets/actor/configuration/app/edit-stats.hbs](../../../../templates/sheets/actor/configuration/app/edit-stats.hbs.md), [templates/sheets/actor/configuration/app/partials/stats-block.hbs](../../../../templates/sheets/actor/configuration/app/partials/stats-block.hbs.md).

[Протокол и границы](../../../../../review-log.md#task-0004003) — TASK-0004.003; процессы [R003-10](../../../../../cross-check-0002.md#r003-10). Новое исполнение N01 протокола ограничено моделями и собственными расчётами Actor; остальные перечисленные опыты относятся к прежним порциям.
