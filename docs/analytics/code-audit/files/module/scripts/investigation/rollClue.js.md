# module/scripts/investigation/rollClue.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/scripts/investigation/rollClue.js](../../../../../../../module/scripts/investigation/rollClue.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `538dbac9bb9432c123fe4f3c00ab788b58517afb` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.023](../../../../../../tasks/task-0003.023.md), 14 файлов, 449 логических строк |
| Запись перекрёстной сверки | [TASK-0003.023](../../../../review-log.md#task-0003023) |

## Назначение файла

Выбирает взаимодействующего Actor и навык из clueItem.system.skillsUsed, затем запускает обычный Actor.rollSkill.

## Условия использования

Импортируется WitcherMysterySheet; вызывается действием rollClue строки улики. При импорте сохраняет ссылку на DialogV2; взаимодействие начинается только при вызове функции.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| getInteractActor | Named import, 1 | Получение Actor пользователя | Из helper.js | await перед проверкой навыков |
| DialogV2 | const, 3 | API выбора навыка | Локальная ссылка Foundry | wait при нескольких навыках |
| rollClue(clueItem) | async named export, 5–44 | Маршрут броска | WitcherMysterySheet._onRollClue | getInteractActor → выбор → rollSkill |
| availableSkills / choosenSkill / skills | 8–19 | Массив имён, выбранное имя и объекты skillMap | Локально; choosenSkill — написание исходника | 0 → return; 1 → прямое имя; >1 → reduce до массива описаний |
| selectedSkill callback / cancel | buttons, 28–38 | Действия диалога | DialogV2.wait | Читает button.form.elements.selectedSkill.value; cancel не имеет callback |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| async rollClue(clueItem) | Item с system.skillsUsed; доступный взаимодействующий Actor | Promise<undefined> | await getInteractActor; ранний выход при 0 навыков; 1 без диалога; несколько renderTemplate+DialogV2.wait; actor.rollSkill(choosenSkill) | Нет проверки actor/имени/отмены; rollSkill не ожидает; dc не передаёт |
| reduce callback | Каждое имя skillsUsed | acc.concat([CONFIG.WITCHER.skillMap[skill]]) | Строит массив описаний навыков | Неизвестное имя добавляет undefined |
| buttons.selectedSkill.callback(event,button,dialog) | Кнопка с form.elements.selectedSkill | Строка value | Читает конкретную форму кнопки | Пустой выбор не отвергается; event/dialog не используются |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| getInteractActor / getCurrentCharacter / chooseFromAvailableActors | [module/scripts/helper.js](../../../../../../../module/scripts/helper.js) | ES named import и цепочка helper | 6 | 11–58: выбранный токен → персонаж пользователя → список owned/hasPlayerOwner; отмена input может дать null |
| WITCHER.skillMap | [module/setup/config.js](../../../../../../../module/setup/config.js) | CONFIG lookup | 19 | name/label/attribute; неизвестное имя не проверено |
| WitcherActor.rollSkill / skillMixin.rollSkillCheck | [module/actor/witcherActor.js](../../../../../../../module/actor/witcherActor.js); [module/actor/mixins/skillMixin.js](../../../../../../../module/actor/mixins/skillMixin.js) | Метод Actor через примесь | 43 | rollSkill(name,threshold=-1) → skillMapEntry.attribute; dc этой функции доступен, но не передаётся |
| ClueData | [module/data/investigation/clueData.js](../../../../../../../module/data/investigation/clueData.js) | Входные поля | 8 | skillsUsed — ArrayField строк без choices |
| chooseEvidenceSkill.hbs | [templates/dialog/investigation/chooseEvidenceSkill.hbs](../../../../../../../templates/dialog/investigation/chooseEvidenceSkill.hbs) | renderTemplate | 20–23 | Контекст {skills}; select name selectedSkill |
| DialogV2.wait / _onSubmit | Foundry 14.367.0, client/applications/api/dialog.mjs:261–276, 405–428 | Внешний диалог | 26–40 | Настоящие методы ядра: cancel возвращает 'cancel', закрытие null |
| renderTemplate / i18n | Foundry 14.367.0 Handlebars; game.i18n | UI/локализация | Заголовок и кнопки | HBS выполнен с настоящими selectOptions/prepareSelectOptionGroups и фасадом HTML select |
| WITCHER.Investigation.evidence.chooseSkill / WITCHER.Dialog.ButtonRoll / WITCHER.Button.Cancel | [lang/en.json](../../../../../../../lang/en.json); [lang/ru.json](../../../../../../../lang/ru.json) | Ключи локализации | Заголовок/кнопки | Ключи найдены в обеих локализациях |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/actor/sheets/investigation/WitcherMysterySheet.js](../../../../../../../module/actor/sheets/investigation/WitcherMysterySheet.js) | rollClue | ES import и _onRollClue | 1, 113 |
| [templates/sheets/investigation/partials/clue-display.hbs](../../../../../../../templates/sheets/investigation/partials/clue-display.hbs) | data-action rollClue | Через обработчик листа | 35 |
| [templates/dialog/investigation/chooseEvidenceSkill.hbs](../../../../../../../templates/dialog/investigation/chooseEvidenceSkill.hbs) | skills и selectedSkill | Вход и обратное чтение формы | Отображение/выбор |

Область поиска: module/ и templates/ текущего checkout; регистрация сверена с system.json. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Функция сама не изменяет clueItem, тайну, время, complexity, ущерб или фокус. Даже выбор Actor предшествует проверке пустого skillsUsed. Передаётся единственный аргумент имени навыка; поле dc не попадает в threshold. Возврат функции не означает окончания броска. Отмена/неизвестное имя доходит до lookup в skillMixin, отсутствие Actor ломает вызов метода. Обычный бросок может открыть дальнейшие окна/создать сообщение уже в соседней цепочке; она здесь полностью не исполнена.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Actor и навыки | Группы 06–09 | 0 навыков без броска; 1 без диалога; несколько с выбором; нет Actor → TypeError; cancel/null/неизвестное имя переданы в rollSkill | getInteractActor настоящий; game/canvas/Dialog заменены |
| Контракт ядра диалога | Группа 05 | Настоящие wait/_onSubmit дали выбранное имя, 'cancel', null | Класс окна, DOM и события подменены |
| Порог и ожидание | Группы 06/10 | Передан только skillName; threshold по умолчанию -1; rollClue завершается до управляемого Promise броска | Запись сообщения и случайный бросок не выполнялись |

## Непроверенные участки и открытые вопросы

Все 44 строки прочитаны. На этапе .023 helper и skillMixin были проверены точечно; теперь helper описан полностью в .028, skillMixin остаётся в плане .029. Правила автоматического ущерба/времени и содержимое миров не проверялись.

## Связанные проблемы

[issue-00148](../../../../../../issues/potential/issue-00148.md), [issue-00149](../../../../../../issues/potential/issue-00149.md), [issue-00150](../../../../../../issues/potential/issue-00150.md), [issue-00151](../../../../../../issues/potential/issue-00151.md), [issue-00152](../../../../../../issues/potential/issue-00152.md). Отмена, отсутствие Actor, неизвестный навык, непереданная DC и преждевременное завершение задокументированы раздельно.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `538dbac9bb9432c123fe4f3c00ab788b58517afb`; полный файл | Первая карточка; [сверка порции](../../../../review-log.md#task-0003023) |

## Уточнение TASK-0003.028

2026-09-11, `9f16a7ae4bc942df85a105fd37d9a3cb3ef99f4b`: getInteractActor теперь полностью разобран: первый controlled Actor → character → 0/1/несколько owned && hasPlayerOwner. Ноль кандидатов возвращает undefined после уведомления; закрытый DialogV2.input возвращает null, values.actor вызывает TypeError. [issue-00149](../../../../../../issues/potential/issue-00149.md) дополнена связями с другими потребителями. Это не проверка полного skillMixin: его разбор остаётся TASK-0003.029.

Полные карточки зависимости: [module/scripts/helper.js](../helper.js.md). [Перекрёстная сверка](../../../../review-log.md#task-0003028). Это уточнение связи; исходный файл не изменён.
