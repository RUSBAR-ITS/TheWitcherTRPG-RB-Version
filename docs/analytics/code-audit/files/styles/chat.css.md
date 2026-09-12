# styles/chat.css

| Поле | Значение |
| --- | --- |
| Исходный файл | [styles/chat.css](../../../../../styles/chat.css) |
| Тип файла | CSS |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-12 |
| Ветка и коммит | rusbar-main, ee24c2605f4db98fad1ff6db024d2b0c26883670 |
| Изменения относительно коммита | Нет; совпадает со срезом TASK-0001 15da5b225535e34af4e132c701b5353ef4eb667f |
| Задача и порция | [TASK-0003.048](../../../../tasks/task-0003.048.md), 16 файлов / 920 логических строк; данный файл — 74 |
| Запись перекрёстной сверки | [TASK-0003.048](../../review-log.md#task-0003048) |

## Назначение файла

Оформление описания Item, запроса ремонта и отдельных фрагментов боевых сообщений: цвет исхода процентного воздействия, кнопки статусов/урона/оглушения и заголовки.

## Условия использования

styles/witcher-styles.css импортирует файл в строке 19 после container-sheet.css и до item-header.css. Размеры item-tag и stored-item-img задаёт ранее загруженный tab-inventory.css, а не chat.css. .chat-message и .flavor-text приходят из шаблона сообщения ядра; отсутствие этих строк в системных HBS не означает отсутствия потребителя.

## Введённые сущности и действия с ними

Программных экспортов, классов JS и полей модели нет. Собственные сущности — 14 CSS-правил и 31 declarations. В таблице перечислены все selectors и свойства; знак → сохраняет реальную вложенность, а не обозначает дополнительный HTML-элемент.

| Селектор и внешние scopes | Строка | Полный набор declarations |
| --- | --- | --- |
| `.percentageFailed` | 1 | `background-color: firebrick`; `color: wheat` |
| `.percentageSuccess` | 6 | `background-color: greenyellow` |
| `.apply-status` | 10 | `display: flex`; `gap: 5px` |
| `.center-important` | 15 | `text-align: center`; `color: wheat`; `background-color: brown` |
| `.chat-item-description` | 21 | `display: flex`; `flex-direction: column`; `gap: 15px` |
| `.chat-item-header` | 27 | `display: flex`; `align-items: center`; `gap: 5px` |
| `.chat-item-header > img` | 33 | `border-radius: 5px`; `width: 40px`; `height: 40px`; `border: 1px solid rgba(25, 24, 19, 0.6)` |
| `.chat-item-header > h4` | 40 | `font-size: 1.3rem`; `margin: 0` |
| `.chat-description > .list-item-description > h4, .chat-components > h4` | 45 | `font-size: 1rem`; `margin: 0` |
| `.repair-message-section` | 51 | `display: flex`; `flex-direction: column`; `gap: 10px` |
| `.repair-section > table` | 57 | `margin: 0` |
| `.request-repair` | 61 | `width: 100%` |
| `.chat-message .flavor-text .attack-message .damage` | 65 | `width: 100%`; `margin-bottom: 5px` |
| `.chat-message .flavor-text .stun, .chat-message .flavor-text .crit-stun` | 70 | `width: 100%`; `margin-bottom: 5px` |

## Основные функции и методы

JavaScript-функций нет. Браузер сопоставляет selectors с DOM и применяет каскад; CSS не вызывает методы системы.

`.percentageFailed` задаёт firebrick/wheat, `.percentageSuccess` — greenyellow без собственного цвета текста. `.apply-status` — flex с gap 5px; успех/провал определяется damageUtilMixin, CSS его не рассчитывает. `.center-important` — центрированный wheat на brown. Карточка Item — колонка с gap 15px; шапка — строка с gap 5px и картинкой 40×40, h4 — 1.3rem/margin 0. Правило строки 45 с непосредственными дочерними элементами не достигает h4 описания/компонентов: каждый partial вставляет дополнительный section. Это issue-00308. Ремонтная секция — колонка/gap 10px, её непосредственная table без внешнего margin, кнопка запроса шириной 100%. Боевые кнопки damage/stun/crit-stun получают ширину 100% и нижний отступ 5px только внутри core .chat-message .flavor-text.

## Используемые сущности и зависимости

| Файл-источник | Сущность | Вид связи / место и цель | Основание |
| --- | --- | --- | --- |
| [styles/witcher-styles.css](../../../../../styles/witcher-styles.css) | @import | Единственное подключение этого файла в системных стилях. | Исходники, поиск module/templates/styles и AST; границы ниже |
| [system.json](../../../../../system.json) | styles | Загружает styles/witcher-styles.css. | Исходники, поиск module/templates/styles и AST; границы ниже |
| [templates/chat/item/item-description.hbs](../../../../../templates/chat/item/item-description.hbs) | chat-item-description/header, chat-description/components | Корень и его дочерние partial задают структуру сообщения; промежуточный section существенен для >. | Исходники, поиск module/templates/styles и AST; границы ниже |
| [templates/chat/item/repair.hbs](../../../../../templates/chat/item/repair.hbs) | repair-message-section/repair-section/request-repair | Шаблон запроса и отчёта ремонта. | Исходники, поиск module/templates/styles и AST; границы ниже |
| [module/item/mixins/damageUtilMixin.js](../../../../../module/item/mixins/damageUtilMixin.js) | damageRoll: percentageFailed/Success, apply-status | Процентное сравнение и сборка HTML; CSS лишь окрашивает результат. | Исходники, поиск module/templates/styles и AST; границы ниже |
| [templates/chat/combat/spellItem.hbs](../../../../../templates/chat/combat/spellItem.hbs) | a.apply-status | Статусные ссылки магии. | Исходники, поиск module/templates/styles и AST; границы ниже |
| [templates/chat/combat/defense/defenseCrit.hbs](../../../../../templates/chat/combat/defense/defenseCrit.hbs) | center-important, crit-stun | Предупреждение о критическом попадании и спасбросок. | Исходники, поиск module/templates/styles и AST; границы ниже |
| [templates/chat/combat/defense/defenseStun.hbs](../../../../../templates/chat/combat/defense/defenseStun.hbs) | stun | Кнопка оглушения. | Исходники, поиск module/templates/styles и AST; границы ниже |
| [module/actor/mixins/weaponAttackMixin.js](../../../../../module/actor/mixins/weaponAttackMixin.js) | attack-message, damage | Строка оружейной атаки с кнопкой урона. | Исходники, поиск module/templates/styles и AST; границы ниже |
| [module/actor/mixins/professionMixin.js](../../../../../module/actor/mixins/professionMixin.js) | attack-message, damage | Профессиональная атака создаёт тот же DOM-контракт. | Исходники, поиск module/templates/styles и AST; границы ниже |
| [module/scripts/chat.js](../../../../../module/scripts/chat.js) | onRepairRequest | Привязка button.request-repair; CSS не выполняет ремонт. | Исходники, поиск module/templates/styles и AST; границы ниже |
| [module/scripts/statusEffects/applyStatusEffect.js](../../../../../module/scripts/statusEffects/applyStatusEffect.js) | chatMessageListeners/onApplyStatus | Ссылки a.apply-status; собственные проблемы маршрута ранее зарегистрированы. | Исходники, поиск module/templates/styles и AST; границы ниже |
| [module/scripts/combat/combat.js](../../../../../module/scripts/combat/combat.js) | кнопки damage/stun/crit-stun | Обработчики боевого чата. | Исходники, поиск module/templates/styles и AST; границы ниже |

Внешние классы .chat-message/.flavor-text заданы Foundry 14.367.0 в /opt/foundryvtt/templates/sidebar/chat-message.hbs:1,24. Полный клиент не запускался.

## Известные потребители

| Файл-потребитель | Способ использования | Доказательство |
| --- | --- | --- |
| [styles/witcher-styles.css](../../../../../styles/witcher-styles.css) | Прямой @import | Путь найден один раз |
| [templates/chat/item/item-description.hbs](../../../../../templates/chat/item/item-description.hbs) | chat-item-description/header, chat-description/components | Корень и его дочерние partial задают структуру сообщения; промежуточный section существенен для >. |
| [templates/chat/item/repair.hbs](../../../../../templates/chat/item/repair.hbs) | repair-message-section/repair-section/request-repair | Шаблон запроса и отчёта ремонта. |
| [module/item/mixins/damageUtilMixin.js](../../../../../module/item/mixins/damageUtilMixin.js) | damageRoll: percentageFailed/Success, apply-status | Процентное сравнение и сборка HTML; CSS лишь окрашивает результат. |
| [templates/chat/combat/spellItem.hbs](../../../../../templates/chat/combat/spellItem.hbs) | a.apply-status | Статусные ссылки магии. |
| [templates/chat/combat/defense/defenseCrit.hbs](../../../../../templates/chat/combat/defense/defenseCrit.hbs) | center-important, crit-stun | Предупреждение о критическом попадании и спасбросок. |
| [templates/chat/combat/defense/defenseStun.hbs](../../../../../templates/chat/combat/defense/defenseStun.hbs) | stun | Кнопка оглушения. |
| [module/actor/mixins/weaponAttackMixin.js](../../../../../module/actor/mixins/weaponAttackMixin.js) | attack-message, damage | Строка оружейной атаки с кнопкой урона. |
| [module/actor/mixins/professionMixin.js](../../../../../module/actor/mixins/professionMixin.js) | attack-message, damage | Профессиональная атака создаёт тот же DOM-контракт. |

Поиск проведён в module/, templates/ и styles/ текущего checkout. Совпадение имени файла или поля не выдаётся за CSS-потребителя; старые и динамические элементы различены в описании. Внешние модули, переопределённые темы и мировые макросы не исследованы.

## Данные и изменения состояния

Стили не изменяют Item, Actor, ActiveEffect или настройки. Они оформляют DOM; игровые флаги, условия HBS и обработчики классов описаны выше. Файл не содержит расчёта характеристик, стоимости или количества.

## Проверки и доказательства

| Проверка | Источник / сценарий | Результат | Предел |
| --- | --- | --- | --- |
| Полный разбор | Исходный файл; PostCSS AST | 14 правил, 31 declarations, все вложенные scopes учтены | PostCSS не валидирует семантику значения CSS и не является браузером |
| Потребители/состояния | Чтение указанных HBS/JS и локальные сценарии | Группы 01–11: реальные HBS и модели, parse5 подтвердил структуру section и отсутствие совпадения обоих селекторов строки 45. Группа 12: repair-header, две repair-section и условная request-repair. 14 AST-правил, 31 declaration. | Без визуального рендера |
| Каскад | system.json и styles/witcher-styles.css | styles/witcher-styles.css импортирует файл в строке 19 после container-sheet.css и до item-header.css. Размеры item-tag и stored-item-img задаёт ранее загруженный tab-inventory.css, а не chat.css. .chat-message и .flavor-text приходят из шаблона сообщения ядра; отсутствие этих строк в системных HBS не означает отсутствия потребителя. | Сторонние стили/темы не охвачены |

## Непроверенные участки и открытые вопросы

Файл прочитан целиком. Проверки локальные: Foundry 14.367.0, Node 24.16.0, Handlebars 4.7.9, PostCSS 8.5.12. Модели, helpers, методы и HBS — реальные исходники; UUID resolver, Actor/DOM/ChatMessage и отдельные вспомогательные helpers представлены указанными в журнале фасадами. Не запускались мир, браузер, HTTP, БД, установка пакетов или сборка. Совпадение селектора и существование файла не доказывают конечный вид или доступ службы.

## Связанные проблемы

[docs/issues/potential/issue-00308.md](../../../../issues/potential/issue-00308.md), [docs/issues/potential/issue-00310.md](../../../../issues/potential/issue-00310.md). Наблюдения остаются potential; подтверждения и исправления не выполнялись.

## История актуализации

| Дата | Версия и область | Результат |
| --- | --- | --- |
| 2026-09-12 | ee24c2605f4db98fad1ff6db024d2b0c26883670; полный файл | Первичная карточка; [перекрёстная сверка](../../review-log.md#task-0003048) |
