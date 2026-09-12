# templates/chat/item/item-description.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/chat/item/item-description.hbs](../../../../../../../templates/chat/item/item-description.hbs) |
| Тип файла | Handlebars |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-12 |
| Ветка и коммит | rusbar-main, ee24c2605f4db98fad1ff6db024d2b0c26883670 |
| Изменения относительно коммита | Нет; совпадает со срезом TASK-0001 15da5b225535e34af4e132c701b5353ef4eb667f |
| Задача и порция | [TASK-0003.048](../../../../../../tasks/task-0003.048.md), 16 файлов / 920 логических строк; данный файл — 17 |
| Запись перекрёстной сверки | [TASK-0003.048](../../../../review-log.md#task-0003048) |

## Назначение файла

Корневой шаблон сообщения «показать предмет в чате»: изображение и имя Item, описание по типу, материалы рецепта и теги свойств.

## Условия использования

Вызывается itemMixin._onItemMessage при .item-chat; не включён в предзагрузку корней. Пять partial предзагружаются setup/handlebars.

Корень всегда создаёт section.chat-item-description, header с img/h4, div.chat-description, div.chat-components и footer.chat-item-tags.item-tags. Нет условия на весь Item: неподдержанный тип сохраняет шапку и пустые контейнеры. Первые три partial (description, spell-description, alchemicals) включаются в chat-description, crafting-items — в chat-components, tags — в footer. Включения не передают hash и не меняют контекст, каждый partial сам проверяет type. Следовательно, Item.type='diagrams' корректно проходит три ветви рецепта; имя класса DiagramData и имя файла diagramData.js не определяют тип документа.

## Введённые сущности и действия с ними

| Сущность | Определение / область | Действия |
| --- | --- | --- |
| HTML-фрагмент | Весь файл | Условия, текст, атрибуты и CSS-классы; нет сохранения документов |
| type | Внешний контекст Item.type | Выбор поддержанных типов |
| Пути чтения | Все буквальные обращения ниже | Готовые поля и справочники, без обновления |

Буквальные пути чтения: `item.img`, `item.name`.



## Основные функции и методы

JS-методов, inline scripts, data-action и игровых кнопок нет. Браузерный details появляется во вложенном crafting-items и содержит только summary; действия ремонта/урона не принадлежат этому шаблону.

Внешние if/each/lookup — Handlebars 4.7.9; eq/or/gt/capitalize — registerHandelbarHelpers системы, localize/concat — Foundry client/applications/handlebars.mjs. Набор реально вызванных helpers определяется выражениями файла, а не всем доступным реестром. if без includeZero не показывает Number 0; стандартное {{}} экранирует текст и атрибуты.

## Используемые сущности и зависимости

| Источник | Используемая сущность | Связь и цель | Основание |
| --- | --- | --- | --- |
| [module/setup/handlebars.js](../../../../../../../module/setup/handlebars.js) | preloadHandlebarsTemplates/registerHandelbarHelpers | Предзагрузка пяти partial, системные eq/or/gt/capitalize; корень рендерится по запросу. | Определение и место обращения сверены |
| [styles/chat.css](../../../../../../../styles/chat.css) | chat-* и list-item-description | Общие размеры и несовпадение непосредственных потомков section. | Определение и место обращения сверены |
| [styles/tab-inventory.css](../../../../../../../styles/tab-inventory.css) | item-tags/item-tag, stored-item-* | Общие стили тегов и материалов. | Определение и место обращения сверены |
| [module/actor/sheets/mixins/itemMixin.js](../../../../../../../module/actor/sheets/mixins/itemMixin.js) | itemMixin._onItemMessage | Читает closest('.list-item').dataset.itemId; actor.items.get; передаёт исходный Item, type=item.type, config=WITCHER. | Определение и место обращения сверены |
| [module/setup/config.js](../../../../../../../module/setup/config.js) | WITCHER | Общий справочник для вложенных тегов. | Определение и место обращения сверены |
| [module/setup/registerDataModels.js](../../../../../../../module/setup/registerDataModels.js) | registerDataModels; Item.diagrams | Фактическая регистрация типов, проверенная вместе с system.json. | Определение и место обращения сверены |
| [templates/chat/item/partials/item-description/description.hbs](../../../../../../../templates/chat/item/partials/item-description/description.hbs) | description | Текст обычных предметов | Определение и место обращения сверены |
| [templates/chat/item/partials/item-description/spell-description.hbs](../../../../../../../templates/chat/item/partials/item-description/spell-description.hbs) | spell-description | Эффекты магии | Определение и место обращения сверены |
| [templates/chat/item/partials/item-description/alchemicals.hbs](../../../../../../../templates/chat/item/partials/item-description/alchemicals.hbs) | alchemicals | Алхимия/мутагены/компоненты | Определение и место обращения сверены |
| [templates/chat/item/partials/item-description/crafting-items.hbs](../../../../../../../templates/chat/item/partials/item-description/crafting-items.hbs) | crafting-items | Материалы | Определение и место обращения сверены |
| [templates/chat/item/partials/item-description/tags.hbs](../../../../../../../templates/chat/item/partials/item-description/tags.hbs) | tags | Признаки | Определение и место обращения сверены |

Локализация: [lang/ru.json](../../../../../../../lang/ru.json) и [lang/en.json](../../../../../../../lang/en.json); настоящий Localization 14.367.0 с expandObject и en fallback. Иконки Font Awesome и обрамление сообщения предоставляет клиент Foundry. Ресурсы assets и внешний клиент не получают карточек этого аудита.

## Известные потребители

| Потребитель | Использование | Условия / основание |
| --- | --- | --- |
| [module/actor/sheets/mixins/itemMixin.js](../../../../../../../module/actor/sheets/mixins/itemMixin.js) | _onItemMessage: renderTemplate | item-chat в текущих списках Actor; prepared Item по ссылке |

Область поиска — module/ и templates/ текущего checkout. Макросы миров, внешние модули и подменённые шаблоны не проверялись.

## Данные и изменения состояния

Шаблон создаёт HTML-строку, не модифицирует предмет или Actor. Producer передаёт подготовленную модель Item, а не результат сериализации. Имя и img принадлежат Document, system-поля — моделям системы. Сам HBS не обогащает HTML: markup экранируется. После создания стандартного сообщения ядро ChatMessage.renderHTML вызывает TextEditor.enrichHTML (client/documents/chat-message.mjs:414), поэтому сохранённый @UUID/inline roll нельзя объявлять навсегда простым текстом только по первому рендеру. Полный последующий enrichment в браузере здесь не исполнялся.

## Проверки и доказательства

| Что | Метод / источник | Результат | Предел |
| --- | --- | --- | --- |
| Полнота | 17 строк исходного HBS | Все ветви, пути чтения и helpers описаны | Соседние файлы проверены только по связи |
| Рендер/модель | Настоящие Handlebars, модели и helpers | Группы 01–03, 11, 16: 13 зарегистрированных типов и unknown, prepared DiagramData передана настоящим _onItemMessage без промежуточного toObject. Компонент с доступным UUID выводит актуальное имя/картинку; с недоступным — сохранённое имя. Полные сообщения создавались как строки, ChatMessage.create перехвачен. | UUID/Document/чат — фасады, запись отсутствует |
| Локализация/ресурсы | en/ru expandObject, настоящий Localization; локальные файлы | 66 ключей комплекта: 65 ru, 1 отсутствует en/ru; девять PNG существуют | Другие локали/HTTP не проверены |

## Непроверенные участки и открытые вопросы

Файл прочитан целиком. Проверки локальные: Foundry 14.367.0, Node 24.16.0, Handlebars 4.7.9, PostCSS 8.5.12. Модели, helpers, методы и HBS — реальные исходники; UUID resolver, Actor/DOM/ChatMessage и отдельные вспомогательные helpers представлены указанными в журнале фасадами. Не запускались мир, браузер, HTTP, БД, установка пакетов или сборка. Совпадение селектора и существование файла не доказывают конечный вид или доступ службы. Скрытие нуля и печать сырого строкового enum описаны без самостоятельного вывода о нарушении игровых правил.

## Связанные проблемы

[docs/issues/potential/issue-00175.md](../../../../../../issues/potential/issue-00175.md), [docs/issues/potential/issue-00178.md](../../../../../../issues/potential/issue-00178.md), [docs/issues/potential/issue-00306.md](../../../../../../issues/potential/issue-00306.md), [docs/issues/potential/issue-00307.md](../../../../../../issues/potential/issue-00307.md), [docs/issues/potential/issue-00308.md](../../../../../../issues/potential/issue-00308.md), [docs/issues/potential/issue-00310.md](../../../../../../issues/potential/issue-00310.md). Наблюдения остаются potential; подтверждения и исправления не выполнялись.

## История актуализации

| Дата | Версия и область | Результат |
| --- | --- | --- |
| 2026-09-12 | ee24c2605f4db98fad1ff6db024d2b0c26883670; полный файл | Первичная карточка; [перекрёстная сверка](../../../../review-log.md#task-0003048) |
