# templates/chat/combat/defense/defenseCrit.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/chat/combat/defense/defenseCrit.hbs](../../../../../../../../templates/chat/combat/defense/defenseCrit.hbs) |
| Тип файла | Handlebars / HTML |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-12 |
| Ветка и коммит | rusbar-main, 16695cbfc7fec3e0de56660c7cab21bc0304e94b |
| Изменения относительно коммита | Нет; совпадает со срезом TASK-0001 15da5b225535e34af4e132c701b5353ef4eb667f |
| Задача и порция | [TASK-0003.042](../../../../../../../tasks/task-0003.042.md), 5 файлов / 477 логических строк; данный файл — 6 |
| Запись перекрёстной сверки | [TASK-0003.042](../../../../../review-log.md#task-0003042) |

## Назначение файла

Условный фрагмент критической защиты: название тяжести, маркер меню критической травмы и кнопка спасброска.

## Условия использования

[module/actor/mixins/defenseMixin.js](../../../../../../../../module/actor/mixins/defenseMixin.js):220–227 рендерит фрагмент только при truthy crit, дополнительно сам шаблон содержит if crit. В контекст передаётся {crit:{criticalLevel:CONFIG.WITCHER.critLevel[crit.criticalLevel]}}. В system сообщения сохраняется другой, полный raw crit: HTML-контекст нельзя путать с данными для действий.

## Введённые сущности и действия с ними

| Сущность | Строки | Назначение |
| --- | --- | --- |
| if crit | 1–6 | При ложном/отсутствующем crit вывод пустой |
| h3.center-important.crit-taken | 2–4 | Локализованные заголовок и тяжесть; crit-taken — признак меню |
| button.crit-stun | 5 | Действие спасброска без дополнительного модификатора |

## Основные способы использования

Собственных JS-функций/обработчиков нет. Тяжесть не вычисляется: simple/complex/difficult/deadly установлены checkForCrit и превращены в ключ локализации через CONFIG. Кнопка не содержит defender UUID или critdamage; данные и выбор Actor находятся у обработчика чата.

## Используемые сущности и зависимости

| Сущность | Источник | Вид / основание |
| --- | --- | --- |
| crit.criticalLevel | [module/actor/mixins/defenseMixin.js](../../../../../../../../module/actor/mixins/defenseMixin.js), [module/setup/config.js](../../../../../../../../module/setup/config.js) | Контекст renderTemplate, строка ключа локализации |
| if / localize | Handlebars/Foundry, [lang/en.json](../../../../../../../../lang/en.json), [lang/ru.json](../../../../../../../../lang/ru.json) | WITCHER.Defense.Crit, WITCHER.Defense.critStun и ключ тяжести |
| center-important / crit-stun | [styles/chat.css](../../../../../../../../styles/chat.css):15,70–71 | Оформление заголовка/кнопки через styles/witcher-styles.css |
| crit-taken | [module/scripts/combat/combat.js](../../../../../../../../module/scripts/combat/combat.js):68–95 | wasCritted проверяет descendant .crit-taken, разрешая меню applyCritDamage/applyBonusCritDamage/applyCritWound |
| crit-stun | Тот же combat.js:33–37 | defenseChatMessageListeners: getInteractActor → stunSave() |
| system.crit | [module/data/chatMessage/defenseMessageData.js](../../../../../../../../module/data/chatMessage/defenseMessageData.js), [module/actor/mixins/damageMixin.js](../../../../../../../../module/actor/mixins/damageMixin.js) | Косвенный контракт меню; значения не берутся из текста h3 |

## Известные потребители

Производитель — [module/actor/mixins/defenseMixin.js](../../../../../../../../module/actor/mixins/defenseMixin.js). Селекторы — [module/scripts/combat/combat.js](../../../../../../../../module/scripts/combat/combat.js), CSS — [styles/chat.css](../../../../../../../../styles/chat.css). Контекстное меню ожидает элемент сообщения с вложенным h3; это не совпадение селектора с самим корнем h3. Полный DOM-проход контекстного меню от pointer не запускался.

## Данные и изменения состояния

HTML не изменяет критический объект. Состояние записи задаёт raw crit в ChatMessageData; реальная DefenseMessageData удаляет critEffectModifier до последующего меню. Наличие правильного заголовка не доказывает сохранность скрытого поля. Нажатие кнопки использует заново выбранного getInteractActor, а не автоматически message.system.defender.

## Проверки и доказательства

Прочитаны 6 логических строк. Группы 20–23 проверили пороги, контекст и полный маршрут формирования; 27 — пустой/непустой if и две кнопки объединённых фрагментов; 30 — native callback кнопки с пустыми target/currentTarget вызвал stunSave без аргумента. Группа 32 — raw/cleaned crit выбрали разные травмы в настоящем applyCritWound с фасадами каталога. [Методика](../../../../../review-log.md#task-0003042).

## Непроверенные участки и открытые вопросы

Файл прочитан полностью. Переводы, CSS-отрисовка, DOM событий клиента, menu anchoring, права и запись травмы не запускались. Тест обработчика не равен нажатию в браузере.

## Связанные проблемы

[docs/issues/potential/issue-00258.md](../../../../../../../issues/potential/issue-00258.md) — потеря critEffectModifier в модели сообщения; проблема не в отображении h3. [docs/issues/potential/issue-00185.md](../../../../../../../issues/potential/issue-00185.md) — отсутствующий получатель query может остановить производителя до рендера.

## История актуализации

| Дата | Версия и область | Результат |
| --- | --- | --- |
| 2026-09-12 | 16695cbfc7fec3e0de56660c7cab21bc0304e94b; полный файл | Первичная карточка; [перекрёстная сверка](../../../../../review-log.md#task-0003042) |
