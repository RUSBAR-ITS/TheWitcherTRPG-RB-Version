# templates/chat/combat/statusEffect.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/chat/combat/statusEffect.hbs](../../../../../../../templates/chat/combat/statusEffect.hbs) |
| Тип файла | Handlebars, HTML-шаблон |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `a33bf33add228ae93f96a52046c8feb4ee992921` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.009](../../../../../../tasks/task-0003.009.md), одна порция из восьми файлов |
| Запись перекрёстной сверки | [TASK-0003.009](../../../../review-log.md#task-0003009) |

## Назначение файла

Отображает название и иконку воздействия, которое обрабатывается боевым циклом через combatEffects.turnStartEffects. Это короткое уведомление в чате, без команды применения статуса.

## Условия использования

Единственный найденный renderer — applyCombatEffect(actor,status) в generalCombatHook.js. В шаблон передаётся сам status из Object.values(actor.system.combatEffects.turnStartEffects), если у него truthy heal.amount либо damage.amount. Этот контекст не является автоматически документом ActiveEffect: он хранит описание действия боя.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| div.witcherTRPG | Строки 1–3 | Обёртка уведомления | Включается в ChatMessage.content | Нет собственных событий |
| img.chat-icon-small и текст | Строка 2 | Иконка img, локализованное name, подпись WITCHER.statusEffects.applyCombat | Поля объекта status | Нет ссылок, form, data-атрибутов или partial |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| Рендер Handlebars; 1–3 | img, name и helper localize | Строка HTML | Вывод локализованной подписи, иконки и локализованного имени | Собственных JS-функций нет; изменения Actor и сообщения выполняются вызывающим кодом |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| status.img и status.name | [module/scripts/combat/generalCombatHook.js](../../../../../../../module/scripts/combat/generalCombatHook.js) | Прямой контекст renderTemplate | applyCombatEffect передаёт status без обёртки | Строки 46–60 |
| combatEffects.turnStartEffects | [module/data/actor/templates/common/combatEffectsData.js](../../../../../../../module/data/actor/templates/common/combatEffectsData.js) | Исходные данные Actor | Object.values даёт элементы обработки | Цепочка от модели через Actor до renderer проверена |
| Значения статусов с img/name и изменениями turnStartEffects | [module/setup/config.js](../../../../../../../module/setup/config.js) | Данные CONFIG.WITCHER.statusEffects через эффекты | Например, healing/fire задают данные воздействия | Отдельные определения и ключи изменений сопоставлены |
| localize, escaped interpolation | Внешние Foundry Handlebars helper и Handlebars | Рендер | Локализация фиксированного ключа и status.name; src из img | В runtime helper локализации подменён |
| WITCHER.statusEffects.applyCombat и ключи name | [lang/en.json](../../../../../../../lang/en.json); [lang/ru.json](../../../../../../../lang/ru.json) | Строки локализации | Подпись применения в бою и имена статусов | Фиксированный ключ сверён, динамический зависит от status |
| chat-icon-small | [styles/system-styles.css](../../../../../../../styles/system-styles.css) | CSS selector | Ширина иконки 1em | Строки 17–19 |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/scripts/combat/generalCombatHook.js](../../../../../../../module/scripts/combat/generalCombatHook.js) | Полный шаблон | applyCombatEffect рендерит content; getSpeaker(actor), style OTHER, core messageMode, ChatMessage.create | Единственный найденный renderer в module/templates/packsJson |
| [module/setup/hooks.js](../../../../../../../module/setup/hooks.js) | Косвенно через applyGeneralCombatHooks | updateCombat запускает обработку; выбор текущего combatant.actor у activeGM | Шаблон напрямую в hooks не упоминается |
| Foundry ChatMessage UI | HTML уведомления | Отображение; лечение/урон выполняются отдельно в generalCombatHook | В шаблоне нет обработчиков применения |

## Данные и изменения состояния

Сам шаблон только читает img и name. heal/damage служат условиями и данными вызывающего обработчика, в HTML не выводятся. Сообщение строится до соответствующих ветвей фактического урона/лечения; корректность вычисления этих ветвей не обеспечивается разметкой.

Несмотря на имя statusEffect.hbs, здесь нет a.apply-status, data-status или data-duration. Ссылки применения для applyStatusEffect.js производятся другими файлами — spellItem.hbs и damageUtilMixin.js. Их полный разбор не входит в эту порцию.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Полнота | Все 3 логические строки и поиск имени шаблона | Один renderer, два localize, одна img; событий/partials нет | Без завершающего перевода строки; wc -l даёт 2 |
| Цепочка данных | hooks → applyGeneralCombatHooks → applyCombatEffects → applyCombatEffect → renderTemplate(status) | Контекст получен из turnStartEffects; не из коллекции Item.effects | Прочитаны только связанные участки соседних файлов |
| Рендер | Настоящий Handlebars с name=WITCHER.statusEffects.fire и img=fire.svg; localize-подмена | Получены ожидаемые имя/путь иконки; ссылок применения нет | Без браузера, записи чата и реальной локализации |

## Непроверенные участки и открытые вопросы

Полный боевой цикл, время срабатывания updateCombat и отображение сообщения в мире не запускались. Соседний generalCombatHook.js не получает карточку целиком от этой проверки. Допустимость всех произвольных status.name/img и внешних производителей данных не установлена.

## Связанные проблемы

Собственная проблема разметки не выявлена. Соседний процесс связан с [issue-00006](../../../../../../issues/potential/issue-00006.md) (условия updateCombat), [issue-00021](../../../../../../issues/potential/issue-00021.md) (тип урона) и [issue-00022](../../../../../../issues/potential/issue-00022.md) (модификатор лечения).

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.009 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.
