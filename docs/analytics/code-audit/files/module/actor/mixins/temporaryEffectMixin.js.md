# module/actor/mixins/temporaryEffectMixin.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/actor/mixins/temporaryEffectMixin.js](../../../../../../../module/actor/mixins/temporaryEffectMixin.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `a33bf33add228ae93f96a52046c8feb4ee992921` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.009](../../../../../../tasks/task-0003.009.md), одна порция из восьми файлов |
| Запись перекрёстной сверки | [TASK-0003.009](../../../../review-log.md#task-0003009) |

## Назначение файла

Добавляет Actor метод применения временных улучшений: выбирает одно оружие, формирует данные его ActiveEffect и отправляет в чат сообщение со списком улучшений.

## Условия использования

Mixin присоединяется к прототипу WitcherActor. `this` — Actor с items и uuid; вход effects содержит документы либо данные эффектов. При отсутствии типа temporaryItemImprovement метод сразу выходит. Наличие доступного оружия предполагается, но не проверяется перед показом выбора.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| temporaryEffectMixin | Именованный export let; строка 3 | Набор методов Actor | Object.assign(WitcherActor.prototype, temporaryEffectMixin) | Содержит один async-метод |
| DialogV2 | Локальная константа; строка 1 | Диалог выбора | foundry.applications.api.DialogV2 | Не экспортируется |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| applyTemporaryItemImprovements; 4–61 | effects; this.items и uuid | Promise<undefined> | Фильтрует temporaryItemImprovement, выбирает weapon через prompt, формирует копии, запускает createEmbeddedDocuments и рендер сообщения | await prompt и renderTemplate; запись Item и ChatMessage.create не ожидаются; rejectClose=true; catch отсутствует |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| WitcherActor | [module/actor/witcherActor.js](../../../../../../../module/actor/witcherActor.js) | Получатель mixin | this.items, this.uuid; вызов с Actor-контекстом | Прямой импорт и Object.assign в документе Actor |
| WitcherItem и createEmbeddedDocuments | [module/item/witcherItem.js](../../../../../../../module/item/witcherItem.js); внешний Foundry Item | Коллекция Actor.items, embedded-запись | Выбор всех item.type=weapon и создание их ActiveEffect | Дополнительных фильтров equipped/isStored/quantity нет |
| TemporaryItemImprovement model и WitcherActiveEffect | [module/data/activeEffects/witcherTemporaryItemImprovementData.js](../../../../../../../module/data/activeEffects/witcherTemporaryItemImprovementData.js); [module/activeEffect/witcherActiveEffect.js](../../../../../../../module/activeEffect/witcherActiveEffect.js) | Через type и регистрацию | system.isTransferred, applySelf, applyOnTarget; поведение эффекта на Item | Наследуемые changes теряются при замене system |
| DialogV2.prompt | Внешний foundry.applications.api | Выбор одного weapon.id | HTML select name=choosen; callback читает form.elements.choosen.value | Реальный диалог не запускался |
| Шаблон сообщения | [templates/chat/item/appliedTemporaryItemImprovements.hbs](../../../../../../../templates/chat/item/appliedTemporaryItemImprovements.hbs) | renderTemplate | Контекст item и temporaryItemImprovements | 48–53; данные переданы до завершения создания документов |
| renderTemplate, ChatMessage, CONST, ui.combat | Внешние API Foundry | Рендер, getSpeaker, create и поиск боя | style OTHER; duration.combat из первого isActive Combat | Запись чата/оружия подменена в изолированном сценарии |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/scripts/temporaryEffects/applyActiveEffect.js](../../../../../../../module/scripts/temporaryEffects/applyActiveEffect.js) | actor.applyTemporaryItemImprovements | Owned-ветвь локальной функции; получает весь входной список | Фильтрация типов выполняется здесь |
| [module/setup/queries.js](../../../../../../../module/setup/queries.js) | actor.applyTemporaryItemImprovements | Отдельный query TheWitcherTRPG.applyTemporaryItemImprovements | Actor разрешается по UUID; вызов не ожидается |
| [module/actor/witcherActor.js](../../../../../../../module/actor/witcherActor.js) | temporaryEffectMixin | Добавляет метод экземплярам Actor | Object.assign |

## Данные и изменения состояния

HTML option строится строкой: value=weapon.id, data-itemId=weapon.itemId, текст=weapon.name. Экранирования при сборке строки нет; data-itemId далее не используется. Из weapons.find по выбранному ID берётся один Item.

Для каждой копии сначала разворачивается `temp.toObject?.() ?? temp`, затем name становится `<оружие> - <эффект>`, origin заменяется UUID Actor. Объект system полностью заменяется тремя флагами: isTransferred=true, applySelf=false, applyOnTarget=false. В частности, system.changes исходного эффекта не переносится. В duration разворачивается temp.duration и добавляется legacy combat; современный start не задаётся, start=null из исходника сохраняется.

`weapon.createEmbeddedDocuments('ActiveEffect', temps)` запускается без await. Шаблон получает массив подготовленных данных, а не созданные документы. Speaker строится как `ChatMessage.getSpeaker({actor:this.actor})`, хотя в штатном вызове this — Actor; этот маршрут сам не передаёт this как speaker.actor. Сообщение запускается без ожидания результата, собственный метод не возвращает созданные эффекты.

Потеря changes и отсутствие start — разные наблюдения: даже улучшение с пустыми changes может иметь конечную длительность, но start=null не допускает его к isExpiryTrackable ядра. Применение transferred-эффектов в Item и их включение в Actor описаны в карточках обоих документов.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Полнота | Все 62 строки; вызовы в Actor, applyActiveEffect, queries; шаблон | Один метод; нет собственной модели или слушателя чата | Соседние файлы не получают статус полного разбора от этой проверки |
| Данные копии | Исходный метод + реальный BaseActiveEffect/Temporary-модель, подмена выбора оружия и записи | Исходное changes из одной строки стало []; origin=Actor.UUID, имя Sword - Oil, flags перенесены по коду | Нормализация настоящей моделью, БД не задействована |
| Ожидание | createEmbeddedDocuments возвращает управляемый незавершённый Promise | Метод завершился и ChatMessage.create вызван при ещё ожидающей записи оружия | Доказательство порядка вызовов, не сеть |
| Нет оружия/отмена | items без weapon, принят пустой выбор; отдельно reject prompt | Пустой выбор вызывает чтение name у undefined; отмена распространяет rejection | UI подменён |
| Начало длительности | Копия start=null; исходные core/system preCreate и core isExpiryTrackable | start=null, active=true, isTemporary=true, isExpiryTrackable=false | Малый контекст hooks; полный scheduler не запускался |

## Непроверенные участки и открытые вопросы

Настоящая форма выбора, оформление чата, влияние модулей и запись документа в мире не проверялись. Назначение weapon.itemId и speaker.actor требует сверки при полном разборе UI/чат-механизма; здесь зафиксированы фактические аргументы. Не делается вывод о сбое всех Item-эффектов: проблема начала отсчёта воспроизведена для конкретного start=null.

## Связанные проблемы

[issue-00042](../../../../../../issues/potential/issue-00042.md) — потеря changes; [issue-00046](../../../../../../issues/potential/issue-00046.md) — пустой список оружия; [issue-00050](../../../../../../issues/potential/issue-00050.md) — начало длительности; [issue-00008](../../../../../../issues/potential/issue-00008.md) — асинхронные маршруты Queries.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.009 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.
