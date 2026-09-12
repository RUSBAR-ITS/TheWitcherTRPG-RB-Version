# templates/chat/item/partials/item-description/description.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/chat/item/partials/item-description/description.hbs](../../../../../../../../../templates/chat/item/partials/item-description/description.hbs) |
| Тип файла | Handlebars |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-12 |
| Ветка и коммит | rusbar-main, ee24c2605f4db98fad1ff6db024d2b0c26883670 |
| Изменения относительно коммита | Нет; совпадает со срезом TASK-0001 15da5b225535e34af4e132c701b5353ef4eb667f |
| Задача и порция | [TASK-0003.048](../../../../../../../../tasks/task-0003.048.md), 16 файлов / 920 логических строк; данный файл — 10 |
| Запись перекрёстной сверки | [TASK-0003.048](../../../../../../review-log.md#task-0003048) |

## Назначение файла

Обычное текстовое описание оружия, брони, рецепта, транспорта и ценности в сообщении Item.

## Условия использования

Предзагружается preloadHandlebarsTemplates и включается корневым item-description.hbs без смены контекста. Самостоятельного вызова renderTemplate для этой части в module/ не найдено.

or из пяти строгих eq поддерживает armor, weapon, diagrams, mount, valuable. Внешний section создаётся всегда; list-item-description появляется для поддержанного типа даже при пустой description. Внутренний if выводит заголовок и span только при truthy item.system.description. CommonItemData.description — StringField; стандартный вывод экранирует HTML. Для container, enhancement, race, profession и остальных типов описание этой частью не выводится. Это проверенный перечень, обязательность добавления других типов пользователем не установлена.

## Введённые сущности и действия с ними

| Сущность | Определение / область | Действия |
| --- | --- | --- |
| HTML-фрагмент | Весь файл | Условия, текст, атрибуты и CSS-классы; нет сохранения документов |
| type | Внешний контекст Item.type | Выбор поддержанных типов |
| Пути чтения | Все буквальные обращения ниже | Готовые поля и справочники, без обновления |

Буквальные пути чтения: `item.system.description`.



## Основные функции и методы

Собственных функций нет; два уровня условий и экранированный вывод. Не вызывает редактор, TextEditor или игровые действия.

Внешние if/each/lookup — Handlebars 4.7.9; eq/or/gt/capitalize — registerHandelbarHelpers системы, localize/concat — Foundry client/applications/handlebars.mjs. Набор реально вызванных helpers определяется выражениями файла, а не всем доступным реестром. if без includeZero не показывает Number 0; стандартное {{}} экранирует текст и атрибуты.

## Используемые сущности и зависимости

| Источник | Используемая сущность | Связь и цель | Основание |
| --- | --- | --- | --- |
| [templates/chat/item/item-description.hbs](../../../../../../../../../templates/chat/item/item-description.hbs) | item/type/config | Единственное прямое включение partial, исходный контекст без hash. | Определение и место обращения сверены |
| [module/setup/handlebars.js](../../../../../../../../../module/setup/handlebars.js) | preloadHandlebarsTemplates/registerHandelbarHelpers | Предзагрузка пяти partial, системные eq/or/gt/capitalize; корень рендерится по запросу. | Определение и место обращения сверены |
| [styles/chat.css](../../../../../../../../../styles/chat.css) | chat-* и list-item-description | Общие размеры и несовпадение непосредственных потомков section. | Определение и место обращения сверены |
| [styles/tab-inventory.css](../../../../../../../../../styles/tab-inventory.css) | item-tags/item-tag, stored-item-* | Общие стили тегов и материалов. | Определение и место обращения сверены |
| [module/data/item/commonItemData.js](../../../../../../../../../module/data/item/commonItemData.js) | CommonItemData.description | Общая строка описания для всех пяти моделей. | Определение и место обращения сверены |
| [module/setup/registerDataModels.js](../../../../../../../../../module/setup/registerDataModels.js) | armor/weapon/diagrams/mount/valuable | Имена типов документов; diagrams во множественном числе. | Определение и место обращения сверены |
| [module/setup/handlebars.js](../../../../../../../../../module/setup/handlebars.js) | or/eq | Строгое сравнение и объединение условий. | Определение и место обращения сверены |

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
| Полнота | 10 строк исходного HBS | Все ветви, пути чтения и helpers описаны | Соседние файлы проверены только по связи |
| Рендер/модель | Настоящие Handlebars, модели и helpers | Группы 01–02, 05: поддержанные типы, пустая строка и <b>RichText</b>; последнее присутствует как &lt;b&gt; в строке сообщения, не как элемент b. Дальнейший Foundry enrichment отделён от HBS. | UUID/Document/чат — фасады, запись отсутствует |
| Локализация/ресурсы | en/ru expandObject, настоящий Localization; локальные файлы | 66 ключей комплекта: 65 ru, 1 отсутствует en/ru; девять PNG существуют | Другие локали/HTTP не проверены |

## Непроверенные участки и открытые вопросы

Файл прочитан целиком. Проверки локальные: Foundry 14.367.0, Node 24.16.0, Handlebars 4.7.9, PostCSS 8.5.12. Модели, helpers, методы и HBS — реальные исходники; UUID resolver, Actor/DOM/ChatMessage и отдельные вспомогательные helpers представлены указанными в журнале фасадами. Не запускались мир, браузер, HTTP, БД, установка пакетов или сборка. Совпадение селектора и существование файла не доказывают конечный вид или доступ службы. Скрытие нуля и печать сырого строкового enum описаны без самостоятельного вывода о нарушении игровых правил.

## Связанные проблемы

[docs/issues/potential/issue-00308.md](../../../../../../../../issues/potential/issue-00308.md). Наблюдения остаются potential; подтверждения и исправления не выполнялись.

## История актуализации

| Дата | Версия и область | Результат |
| --- | --- | --- |
| 2026-09-12 | ee24c2605f4db98fad1ff6db024d2b0c26883670; полный файл | Первичная карточка; [перекрёстная сверка](../../../../../../review-log.md#task-0003048) |
