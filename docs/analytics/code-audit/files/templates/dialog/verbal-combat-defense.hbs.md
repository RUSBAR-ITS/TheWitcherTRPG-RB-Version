# templates/dialog/verbal-combat-defense.hbs

## Текущее состояние — 14.3.1.00103

2026-09-19, TASK-0011.003. Каждый input[name=verbalCombat] вложен в собственный label, общих id/for нет. data-group явно Defenses; value остаётся ключом defenses. Форма и имя customModifiers сохранены. Потребитель executeDefenseCallback читает только свой корень, валидирует ключ Defenses и передаёт выбор/manual в prepareCheck.

[Проверки и границы](../../../../task-0011-static-checks.md#task-0011003): 38 локальных сценариев прошли, игровая B03 ещё не запускалась. Ниже сохранены описания датированных прежних срезов; утверждения о глобальном выборе radio, DOM/jQuery меню и преждевременном завершении наших операций заменены этой секцией в пределах указанного изменения.

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/dialog/verbal-combat-defense.hbs](../../../../../../templates/dialog/verbal-combat-defense.hbs) |
| Тип файла | Handlebars |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-12 |
| Ветка и коммит | rusbar-main, a69f11d2e4c4318cfbf635dabad97b0062c63c20 |
| Изменения относительно коммита | Нет; совпадает со срезом TASK-0001 15da5b225535e34af4e132c701b5353ef4eb667f |
| Задача и порция | [TASK-0003.046](../../../../../tasks/task-0003.046.md), 5 файлов / 301 логических строк; данный файл — 13 |
| Запись перекрёстной сверки | [TASK-0003.046](../../../review-log.md#task-0003046) |

## Назначение файла

Выводит четыре способа словесной защиты и текстовое поле модификатора для callback legacy Dialog.

## Условия использования

[module/scripts/verbalCombat/verbalCombatDefense.js](../../../../../../module/scripts/verbalCombat/verbalCombatDefense.js):22–27 передаёт {defenses:CONFIG.WITCHER.verbalCombat.Defenses}; результат ставится content обычного Dialog V1. На входе нет cssClass и groupName.

## Введённые сущности и действия с ними

| Сущность | Вид / место | Действие |
| --- | --- | --- |
| form class=cssClass autocomplete=off | Корень:1–13 | Собственная форма контента; cssClass при данном producer пуст |
| h1 / div / each |1–10 | Заголовок и обход defenses |
| verbalData / verbalName | Алиасы each:4 | Конфигурация и ключ защиты |
| input[name=verbalCombat] | Radio:6–7 | id/value=verbalName; data-group=groupName без предоставленного значения; checked не задан |
| label[for=verbalName] |8 | Перевод verbalData.name |
| input[name=customModifiers] |11 | Текстовое поле, value0 |
| localize / concat | Helpers | Заголовок, имя и подпись модификатора |

## Основные функции и методы

Собственного JS нет; один each и core concat/localize. Все четыре защиты используют одно name. Внутри этого each groupName не определён; producer его тоже не передаёт. В сыром HTML получается data-group= />; parse5 разбирает значение data-group как '/', а не как название Defenses. Собственный defense callback читает только value, поэтому это поле ему не требуется. Ошибка данных другого глобального consumer зависит от выбранного элемента.

## Используемые сущности и зависимости

| Сущность | Источник | Связь / основание |
| --- | --- | --- |
| defenses | [module/setup/config.js](../../../../../../module/setup/config.js) | Ignore, Counterargue, ChangeSubject, Disengage |
| renderTemplate / executeDefenseCallback | [module/scripts/verbalCombat/verbalCombatDefense.js](../../../../../../module/scripts/verbalCombat/verbalCombatDefense.js) | Передаёт только defenses; читает глобальный radio и локальный html.find customModifiers |
| common radio name | [templates/dialog/verbal-combat.hbs](../../../../../../templates/dialog/verbal-combat.hbs); [module/actor/mixins/verbalCombatMixin.js](../../../../../../module/actor/mixins/verbalCombatMixin.js) | Совпадение имени/ID между окнами; обе функции document.querySelector не ограничивают контейнер |
| localize / concat / each | Foundry14.367.0 / Handlebars | Те же helpers, что общий диалог |
| WITCHER.verbalCombat.Title / verbalData.name / Dialog.customModifier | [lang/en.json](../../../../../../lang/en.json), [lang/ru.json](../../../../../../lang/ru.json) | Перевод подписей; customModifier в ru отсутствует |
| Dialog V1 | /opt/foundryvtt/client/appv1/api/dialog-v1.mjs | Внешняя оболочка окна; callback получает jQuery, поэтому локальный html.find допустим |

## Известные потребители

Единственный путь загрузки — [module/scripts/verbalCombat/verbalCombatDefense.js](../../../../../../module/scripts/verbalCombat/verbalCombatDefense.js). Общий action callback может увидеть эти radio через document, но не загружает сам HBS. Поиск module/templates; внешние расширения UI не проверены.

## Данные и изменения состояния

Выводит HTML формы; не меняет Resolve, не сравнивает атаку, не создаёт ChatMessage. Ни один radio не имеет начального checked. executeDefenseCallback при полном отсутствии выбранного radio возвращается; Cancel создаётся JS, не HBS. Текстовое значение customModifiers преобразуется сравнением<0/>0 в JS.

## Проверки и доказательства

Группа 17: реальный Handlebars/parse5 — четыре radio без checked, data-group='/', пустой cssClass; выбор отсутствует → callback ничего не бросает. Группы 18–20 исполнили все способы, нулевой/знаковые вводы и чужой radio Seduce → ошибка неизвестной защиты. Группа 25: извлечённый настоящий Dialog.submit передал jQuery. В 26 известный пропуск customModifier в ru отделён от наличия английского fallback.

## Непроверенные участки и открытые вопросы

Контекст CONFIG и callback сопоставлены. .013/.016/.018 сохраняют реальный form/radio lifecycle, label/фокус и несколько окон ([U011-03](../../../cross-check-0002.md#u011-03)). data-group не объявлен новым пользовательским сбоем; выбор начального действия и механика — [U011-07](../../../cross-check-0002.md#u011-07).

## Связанные проблемы

[303](../../../../../issues/closed/issue-00303.md) — глобальные radio между окнами; [186](../../../../../issues/closed/issue-00186.md) — русская подпись. [302](../../../../../issues/closed/issue-00302.md) — более ранний вход в диалог из контекстного меню.

## История актуализации

| Дата | Версия и область | Результат |
| --- | --- | --- |
| 2026-09-12 | a69f11d2e4c4318cfbf635dabad97b0062c63c20; полный файл | Первичная карточка; [перекрёстная сверка](../../../review-log.md#task-0003046) |

## Сквозная сверка TASK-0004.011

2026-09-14; rusbar-main, 55e56567f42ed2da8850d913f28d727113ebdbd3. Исходник совпадает со срезом TASK-0001; изменено только описание.

HBS рисует четыре защиты внутри form, без checked; context даёт Defenses, но не groupName, поэтому data-group не получает содержательного значения. Собственный callback это поле не читает. Radio name совпадает с общим окном словесного боя, а поиск checked находится в глобальном document; это связь issue303.

Сопоставленные определения и потребители: [module/scripts/verbalCombat/verbalCombatDefense.js](../../module/scripts/verbalCombat/verbalCombatDefense.js.md), [templates/dialog/verbal-combat.hbs](verbal-combat.hbs.md), [module/setup/config.js](../../module/setup/config.js.md).

[Протокол и границы](../../../review-log.md#task-0004011) — TASK-0004.011; процессы [R011-27](../../../cross-check-0002.md#r011-27). В этой порции выполнена статическая сверка; прежние опыты сохраняют свои даты и фасады. Новых поведенческих запусков нет; браузер, мир, сеть и запись в БД не запускались.
