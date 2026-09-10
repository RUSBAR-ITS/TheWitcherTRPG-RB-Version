# templates/chat/item/consume.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/chat/item/consume.hbs](../../../../../../../templates/chat/item/consume.hbs) |
| Тип файла | Handlebars, HTML-шаблон |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `7edb814aa870da75c7ad7633536e899a8d07e205` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.015](../../../../../../tasks/task-0003.015.md), одна порция из пятнадцати файлов |
| Запись перекрёстной сверки | [TASK-0003.015](../../../../review-log.md#task-0003015) |

## Назначение файла

HTML сообщения о применении Item: название, величина лечения и представление списка добавляемых статусов.

## Условия использования

consumeMixin.createConsumeMessage вызывает renderTemplate с item, messageInfos и statusEffects, после чего создаёт ChatMessage. Сам HBS документов не создаёт.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| Название | h3 item.name | Имя предмета | Параметр renderTemplate | Вывод с обычным escaping |
| Лечение | Условный div | doesHeal и messageInfos.heal | Item.consume | Показывается по флагу, не по ненулевому числу |
| Статусы | if effects; each statusEffects | name, statusEffect.img, localize statusEffect.name | Преобразованный список createConsumeMessage | span/img.chat-icon; alt='status effect icon' |

## Основные функции и методы

JavaScript-функций, кнопок и действий нет. if item.system.consumeProperties.doesHeal выводит WITCHER.Item.ConsumeProperties.Chat.healedFor и messageInfos.heal. if item.system.consumeProperties.effects выводит WITCHER.Item.ConsumeProperties.Chat.consumeEffects, затем каждый элемент statusEffects. Пустой массив ложен для Handlebars if; именованный элемент без выбранного/известного статуса остаётся в списке.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| createConsumeMessage | [module/item/mixins/consumeMixin.js](../../../../../../../module/item/mixins/consumeMixin.js) | Поставщик контекста / renderTemplate | item/messageInfos/statusEffects | Определение и обращение сверены |
| CONFIG.WITCHER.statusEffects | [module/setup/config.js](../../../../../../../module/setup/config.js) | Косвенный источник metadata | find по id выполняется до HBS | Определение и обращение сверены |
| WITCHER.Item.ConsumeProperties.Chat.healedFor / WITCHER.Item.ConsumeProperties.Chat.consumeEffects / ключи статусов | [lang/ru.json](../../../../../../../lang/ru.json) | Локализация | Подписи | Определение и обращение сверены |
| Handlebars if/each/localize | Foundry Handlebars API | Внешний API | Условный вывод и локализация | Определение и обращение сверены |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/item/mixins/consumeMixin.js](../../../../../../../module/item/mixins/consumeMixin.js) | Шаблон consume.hbs | Путь messageTemplate / renderTemplate | Прямое обращение |

Область поиска: текущие module/ и templates/; регистрации сверены отдельно. Динамические обращения внешних модулей не исследовались.

## Данные и изменения состояния

Нет записи в документы. Не показывает removesEffects, количество, токсичность, time и список перенесённых applySelf ActiveEffect. Пустой/неизвестный statusEffect даёт undefined metadata: img остаётся с src='', подпись пуста, name выводится. Текст сообщения не является подтверждением завершения лечения/статусов/эффектов, поскольку consume не ожидает соответствующие Promise.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Контекст/поля | Полный HBS и настоящий createConsumeMessage | Сообщение HP8/10+5 показывает 2; style/speaker задаются вне HBS | Создание ChatMessage перехвачено |
| Границы списка | Рендер [], name-only, fire и missing-status | 0/1/1/1 картинок; у fire icons/svg/fire.svg; у name-only/unknown src='' | Локализация/DOM представлены ограниченными фасадами; не браузер |

## Непроверенные участки и открытые вопросы

Не проверялись доставка чата, CSS, мультиязычный клиент и отсутствие ресурса иконки. Пустая иконка здесь записана как граница текущего представления; новая issue по ней не создавалась.

## Связанные проблемы

[issue-00034](../../../../../../issues/potential/issue-00034.md). Сообщение может появиться до завершения операций применения.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.015 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.
