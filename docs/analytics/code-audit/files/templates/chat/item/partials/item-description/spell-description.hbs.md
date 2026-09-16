# templates/chat/item/partials/item-description/spell-description.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/chat/item/partials/item-description/spell-description.hbs](../../../../../../../../../templates/chat/item/partials/item-description/spell-description.hbs) |
| Тип файла | Handlebars |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-12 |
| Ветка и коммит | rusbar-main, ee24c2605f4db98fad1ff6db024d2b0c26883670 |
| Изменения относительно коммита | Нет; совпадает со срезом TASK-0001 15da5b225535e34af4e132c701b5353ef4eb667f |
| Задача и порция | [TASK-0003.048](../../../../../../../../tasks/task-0003.048.md), 16 файлов / 920 логических строк; данный файл — 22 |
| Запись перекрёстной сверки | [TASK-0003.048](../../../../../../review-log.md#task-0003048) |

## Назначение файла

Текст эффекта, побочного эффекта и условия снятия для spell, hex и ritual в общем сообщении Item.

## Условия использования

Предзагружается preloadHandlebarsTemplates и включается корневым item-description.hbs без смены контекста. Самостоятельного вызова renderTemplate для этой части в module/ не найдено.

Внешнее условие принимает spell/hex/ritual. Для каждого создаются три div.list-item-description, даже если все поля пусты. Внутри независимые if: effect → WITCHER.Item.Effect; sideEffect → WITCHER.Spell.SideEffect; liftRequirement → WITCHER.Spell.Requirements. effect есть во всех трёх моделях, sideEffect — в SpellData, liftRequirement — в HexData. RitualData не создаёт два последних поля, что нормально для общей разметки. Строки проходят HTML escaping. Эта часть не выводит selfEffects/onCastEffects/ritualComponents и не является боевым spellItem.hbs.

## Введённые сущности и действия с ними

| Сущность | Определение / область | Действия |
| --- | --- | --- |
| HTML-фрагмент | Весь файл | Условия, текст, атрибуты и CSS-классы; нет сохранения документов |
| type | Внешний контекст Item.type | Выбор поддержанных типов |
| Пути чтения | Все буквальные обращения ниже | Готовые поля и справочники, без обновления |

Буквальные пути чтения: `item.system.effect`, `item.system.liftRequirement`, `item.system.sideEffect`.



## Основные функции и методы

JS-функций нет. Условия только отбирают текст; расход STA, проверка DC, применение эффекта и броски находятся вне общего сообщения описания.

Внешние if/each/lookup — Handlebars 4.7.9; eq/or/gt/capitalize — registerHandelbarHelpers системы, localize/concat — Foundry client/applications/handlebars.mjs. Набор реально вызванных helpers определяется выражениями файла, а не всем доступным реестром. if без includeZero не показывает Number 0; стандартное {{}} экранирует текст и атрибуты.

## Используемые сущности и зависимости

| Источник | Используемая сущность | Связь и цель | Основание |
| --- | --- | --- | --- |
| [templates/chat/item/item-description.hbs](../../../../../../../../../templates/chat/item/item-description.hbs) | item/type/config | Единственное прямое включение partial, исходный контекст без hash. | Определение и место обращения сверены |
| [module/setup/handlebars.js](../../../../../../../../../module/setup/handlebars.js) | preloadHandlebarsTemplates/registerHandelbarHelpers | Предзагрузка пяти partial, системные eq/or/gt/capitalize; корень рендерится по запросу. | Определение и место обращения сверены |
| [styles/chat.css](../../../../../../../../../styles/chat.css) | chat-* и list-item-description | Общие размеры и несовпадение непосредственных потомков section. | Определение и место обращения сверены |
| [styles/tab-inventory.css](../../../../../../../../../styles/tab-inventory.css) | item-tags/item-tag, stored-item-* | Общие стили тегов и материалов. | Определение и место обращения сверены |
| [module/data/item/spellData.js](../../../../../../../../../module/data/item/spellData.js) | SpellData.effect/sideEffect | Основной и побочный тексты. | Определение и место обращения сверены |
| [module/data/item/hexData.js](../../../../../../../../../module/data/item/hexData.js) | HexData.effect/liftRequirement | Эффект порчи и снятие. | Определение и место обращения сверены |
| [module/data/item/ritualData.js](../../../../../../../../../module/data/item/ritualData.js) | RitualData.effect | Текст ритуала; компоненты здесь не читаются. | Определение и место обращения сверены |
| [module/setup/handlebars.js](../../../../../../../../../module/setup/handlebars.js) | or/eq | Три строгих проверки типа. | Определение и место обращения сверены |

Локализация: [lang/ru.json](../../../../../../../../../lang/ru.json) и [lang/en.json](../../../../../../../../../lang/en.json); настоящий Localization 14.367.0 с expandObject и en fallback. Иконки Font Awesome и обрамление сообщения предоставляет клиент Foundry. Ресурсы assets и внешний клиент не получают карточек этого аудита.

## Известные потребители

| Потребитель | Использование | Условия / основание |
| --- | --- | --- |
| [templates/chat/item/item-description.hbs](../../../../../../../../../templates/chat/item/item-description.hbs) | partial-включение | Без hash/with, полный контекст item/type/config |
| [module/setup/handlebars.js](../../../../../../../../../module/setup/handlebars.js) | preloadHandlebarsTemplates | Загрузка и регистрация partial отдельно от фактического показа |

Область поиска — module/ и templates/ текущего checkout. Макросы миров, внешние модули и подменённые шаблоны не проверялись.

## Данные и изменения состояния

Шаблон создаёт HTML-строку, не модифицирует предмет или Actor. Producer передаёт подготовленную модель Item, а не результат сериализации. Имя и img принадлежат Document, system-поля — моделям системы. Сам HBS не обогащает HTML: markup экранируется. После создания стандартного сообщения ядро ChatMessage.renderHTML вызывает TextEditor.enrichHTML (client/documents/chat-message.mjs:414), поэтому сохранённый @UUID/inline roll нельзя объявлять навсегда простым текстом только по первому рендеру. Полный последующий enrichment в браузере здесь не исполнялся.

## Проверки и доказательства

| Что | Метод / источник | Результат | Предел |
| --- | --- | --- | --- |
| Полнота | 22 строк исходного HBS | Все ветви, пути чтения и helpers описаны | Соседние файлы проверены только по связи |
| Рендер/модель | Настоящие Handlebars, модели и helpers | Группы 01, 05, 16: настоящие Spell/Hex/Ritual дают по три контейнера, тексты и условия отобраны по схемам. HTML в effect/sideEffect/liftRequirement экранирован; отдельный чат сотворения не переисполнялся. | UUID/Document/чат — фасады, запись отсутствует |
| Локализация/ресурсы | en/ru expandObject, настоящий Localization; локальные файлы | 66 ключей комплекта: 65 ru, 1 отсутствует en/ru; девять PNG существуют | Другие локали/HTTP не проверены |

## Непроверенные участки и открытые вопросы

Текущая статическая сверка завершена; прежние пофайловые опыты сохраняют свои даты и фасады. spell/hex/ritual печатают поля своих описаний через обычные {{}}; sideEffect относится к spell, liftRequirement к hex. Рендер текста не выполняет cast, не расходует компоненты и не создаёт ActiveEffect. Непроверенные границы и следующий критерий: [U016-06](../../../../../../cross-check-0002.md#u016-06), [U016-02](../../../../../../cross-check-0002.md#u016-02), [U016-08](../../../../../../cross-check-0002.md#u016-08). Полный браузерный цикл, мир, HTTP и запись в БД не выполнялись; смысл перевода/игровых правил не оценивался.

## Связанные проблемы

[docs/issues/potential/issue-00308.md](../../../../../../../../issues/potential/issue-00308.md). Наблюдения остаются potential; подтверждения и исправления не выполнялись.

## История актуализации

| Дата | Версия и область | Результат |
| --- | --- | --- |
| 2026-09-12 | ee24c2605f4db98fad1ff6db024d2b0c26883670; полный файл | Первичная карточка; [перекрёстная сверка](../../../../../../review-log.md#task-0003048) |

## Сквозная сверка TASK-0004.016

2026-09-14; rusbar-main, 0588289c84d955201457f44ec2f8152a9258135e. Исходник совпадает со срезом TASK-0001; изменено только описание.

spell/hex/ritual печатают поля своих описаний через обычные {{}}; sideEffect относится к spell, liftRequirement к hex. Рендер текста не выполняет cast, не расходует компоненты и не создаёт ActiveEffect.

Сопоставленные определения и потребители: [module/actor/sheets/mixins/itemMixin.js](../../../../../module/actor/sheets/mixins/itemMixin.js.md), [module/setup/handlebars.js](../../../../../module/setup/handlebars.js.md), [module/data/item/commonItemData.js](../../../../../module/data/item/commonItemData.js.md), [module/actor/sheets/WitcherCharacterSheet.js](../../../../../module/actor/sheets/WitcherCharacterSheet.js.md), [templates/partials/character/tab-background.hbs](../../../../partials/character/tab-background.hbs.md), [module/setup/config.js](../../../../../module/setup/config.js.md).

[Протокол и границы](../../../../../../review-log.md#task-0004016) — TASK-0004.016; процессы [R016-02](../../../../../../cross-check-0002.md#r016-02), [R016-03](../../../../../../cross-check-0002.md#r016-03), [R016-06](../../../../../../cross-check-0002.md#r016-06). В этой порции выполнена статическая сверка; прежние опыты сохраняют свои даты и фасады. Новых поведенческих запусков нет; браузер, мир, сеть и запись в БД не запускались.
