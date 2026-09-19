# styles/configurations/modifier-configuration.css

## Текущее состояние — 14.3.1.00082

2026-09-19, TASK-0010.019. Добавлен modifier-stats: первая колонка max-content общая для строк через subgrid; зазор clamp(10px,1rem,20px), отдельный расчёт для каждого редактора. Сохранены узкий режим и прокрутка, сетка навыков прежняя.

[Реализация, синтетические проверки и границы](../../../../task-0010-019-visual-checks.md). Ниже сохранены описания датированных прежних срезов.

## Текущее состояние — 14.3.1.00077

2026-09-19, TASK-0010.014–.018. Ограниченный экраном редактор, flex window-content и прокручиваемая modifier-list; пятиколоночные Grid-строки, sticky шапка, равные числовые поля, подробности навыков. При контейнере<=40rem действия переходят на отдельную строку. Область только modifier-configuration; типографика из character/sheet.css.

[Исходник](../../../../../../styles/configurations/modifier-configuration.css), [реализация и проверки](../../../../task-0010-ui-fixes.md). Локальная проверка пройдена; реальная игровая/визуальная приёмка ожидается (HTTP502). Следующие датированные разделы описывают прежние срезы.


| Поле | Значение |
| --- | --- |
| Исходный файл | [styles/configurations/modifier-configuration.css](../../../../../../styles/configurations/modifier-configuration.css) |
| Тип файла | CSS |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-12 |
| Ветка и коммит | rusbar-main, 2f94c6c29e298ccf73d67ccc2e5fb8fc358dae2c |
| Изменения относительно коммита | Нет; совпадает со срезом TASK-0001 15da5b225535e34af4e132c701b5353ef4eb667f |
| Задача и порция | [TASK-0003.047](../../../../../tasks/task-0003.047.md), 10 файлов / 661 логических строк; данный файл — 5 |
| Запись перекрёстной сверки | [TASK-0003.047](../../../review-log.md#task-0003047) |

## Назначение файла

Переопределяет display содержимого окна конфигурации модификаторов, исключая для него общую сетку листа Actor.

## Условия использования

Прямой @import в [styles/witcher-styles.css](../../../../../../styles/witcher-styles.css):38, после character/sheet.css:29 и monster/sheet.css:34. Внешний селектор требует application sheet witcher actor modifier-configuration и отсутствие extended-sheet; вложенный — потомка .window-content.

## Введённые сущности и действия с ними

Файл не задаёт размеры окна, хотя в постановке они были ориентиром: единственная declaration — display:inherit. Значение наследуется от непосредственного родителя .window-content; это не самостоятельное display:flex и не наследование всех остальных свойств. Нет управления характеристиками, таблицами, min/max или вычислением модификаторов. :not(.extended-sheet) исключает специальные окна с этим классом.

Ниже перечислены все 2 rule-узла и 1 declarations. Внешняя вложенность читается слева направо; списки селекторов на каждом уровне сохраняются. Дочерний селектор без & означает потомка, а не новый глобальный селектор. Директив @import/@keyframes внутри файла нет.

| Строка | Внешняя вложенность | Селектор / шаг | Свойства |
| --- | --- | --- | --- |
| 1 | Корень | `.application.sheet.witcher.actor.modifier-configuration:not(.extended-sheet)` | Только вложенные правила |
| 2 | `.application.sheet.witcher.actor.modifier-configuration:not(.extended-sheet)` | `.window-content` | `display: inherit` |

## Основные функции и методы

JavaScript-функций и обработчиков нет. Файл объявляет CSS-правила, применяемые браузером к совпавшей разметке; вычисления свойств и псевдосостояний выполняет внешний CSS engine. 

## Используемые сущности и зависимости

| Сущность | Файл-источник | Вид / цель связи |
| --- | --- | --- |
| DEFAULT_OPTIONS.classes / position.width | [module/actor/sheets/configurations/WitcherModifiersConfiguration.js](../../../../../../module/actor/sheets/configurations/WitcherModifiersConfiguration.js) | classes witcher/sheet/actor/modifier-configuration и width520 в JS; extended-sheet не задаётся |
| Общая сетка .window-content | [styles/character/sheet.css](../../../../../../styles/character/sheet.css) | Широкий Actor-селектор display:grid и grid tracks; более специфичный selector этой карточки заменяет display |
| Порядок | [styles/witcher-styles.css](../../../../../../styles/witcher-styles.css) | Входной import после общей сетки |
| PARTS.stats | [templates/sheets/actor/configuration/app/edit-stats.hbs](../../../../../../templates/sheets/actor/configuration/app/edit-stats.hbs) | Содержимое окна характеристик; сам window-content создаёт ядро |
| PARTS.skills | [templates/sheets/actor/configuration/app/edit-skills.hbs](../../../../../../templates/sheets/actor/configuration/app/edit-skills.hbs) | Содержимое окна навыков, не источник родительского класса |

Входной ресурс [styles/witcher-styles.css](../../../../../../styles/witcher-styles.css) зарегистрирован в [system.json](../../../../../../system.json); эти соседи проверены в пределах подключения, их полные карточки здесь не создаются. Найденный локальный файл и строка @import не доказывают доступ по HTTP для службы Foundry.

## Известные потребители

[module/actor/sheets/configurations/WitcherModifiersConfiguration.js](../../../../../../module/actor/sheets/configurations/WitcherModifiersConfiguration.js) определяет соответствующие классы. Foundry ApplicationV2 создаёт application и window-content; HBS не обязан буквально содержать их. [module/actor/rewardsSheet.js](../../../../../../module/actor/rewardsSheet.js) и [module/actor/sheets/configurations/WitcherMonsterConfigurationSheet.js](../../../../../../module/actor/sheets/configurations/WitcherMonsterConfigurationSheet.js) используют extended-sheet, но не modifier-configuration и не являются адресатами этого CSS.

Область поиска: все templates/module/styles текущего среза, имена полей/классов в динамических producer и указанные методы ядра. Имена файлов и упоминания в комментариях отделены от создания HTML. Содержимое миров, внешние расширения и пользовательский enriched HTML не обследованы.

## Данные и изменения состояния

Раскрытый селектор: .application.sheet.witcher.actor.modifier-configuration:not(.extended-sheet) .window-content. Его специфичность 0,7,0 выше общего Actor-правила 0,6,0; import также позднее. Меняется только display: grid-template-columns/rows/gap из общей сетки не сбрасываются, хотя вне grid часть свойств не определяет размещение. Значение display родителя и окончательная геометрия в браузере не измерены.

CSS не создаёт документы, не меняет значения полей и не запускает сохранение/игровые действия. Размещение, hover и видимость отделены от JS управления. Файл прочитан целиком: 5 логических строк; переводы строк LF, нет завершающего newline.

## Проверки и доказательства

Группы 06–07: PostCSS разобрал два rule-узла (внешний контейнер и вложенное правило), одну declaration. Проверены порядок imports, значение inherit и классы DEFAULT_OPTIONS по исходнику. Окно не открывалось;520 — настройка JS, не результат измерения.

Методика — [журнал TASK-0003.047](../../../review-log.md#task-0003047). Использованы PostCSS8.5.12, Handlebars4.7.9 и parse5 из существующих зависимостей Foundry14.367.0. Разбор CSS AST подтверждает структуру, не принятие каждого значения браузером или итоговое computed style.

## Непроверенные участки и открытые вопросы

Полное чтение и прежний AST/HTML-разбор .047 подтверждают структуру, а не computed style, hover или геометрию реального окна. UI/темы/ru-en — [U005-07](../../../cross-check-0002.md#u005-07); внешние producers неиспользуемых классов — [U005-08](../../../cross-check-0002.md#u005-08).

## Связанные проблемы

Новых проблем не зарегистрировано. Наследование display не объявлено ошибкой по отсутствию размеров в CSS.

## История актуализации

| Дата | Версия и область | Результат |
| --- | --- | --- |
| 2026-09-12 | 2f94c6c29e298ccf73d67ccc2e5fb8fc358dae2c; полный файл | Первичная карточка; [перекрёстная сверка](../../../review-log.md#task-0003047) |

## Дополнительная сверка TASK-0003.049

2026-09-12, rusbar-main, 523c9b2616e19058b18f812ae0361c8a86366814. Исходный файл не изменён.

Полностью разобраны оба файла основной сетки Actor. Настоящий _initializeApplicationOptions/#mergeApplicationOptions ядра с извлечёнными classes подтвердил: Monster сохраняет actor и добавляет monster; конфигурация модификаторов не имеет extended-sheet и получает данный override. Изменяется только display, а tracks/gap остаются объявленными. Номера импортов общей сетки, монстра и override — 28/32/35; ранее указанные 29/34/38 — номера строк master, не номера импортов.

Карточки CSS: [styles/character/sheet.css](../character/sheet.css.md), [styles/monster/sheet.css](../monster/sheet.css.md).

[Методика и результаты](../../../review-log.md#task-0003049). Соседний файл повторно в покрытие не включён; браузер и БД не запускались.

## Сквозная сверка TASK-0004.005

2026-09-14; rusbar-main, 4686f913501b9c75082e79249364e40934f6a1da. Исходник совпадает со срезом TASK-0001; изменено только описание.

Единственная declaration display:inherit адресует .application.sheet.witcher.actor.modifier-configuration:not(.extended-sheet) .window-content. Эти классы приходят из DEFAULT_OPTIONS WitcherModifiersConfiguration и оболочки ApplicationV2. Это геометрия окна; значения totalModifiers/changes и ширина520 из JS этим CSS не рассчитываются.

Сопоставленные определения и потребители: [module/actor/sheets/configurations/WitcherModifiersConfiguration.js](../../module/actor/sheets/configurations/WitcherModifiersConfiguration.js.md), [styles/witcher-styles.css](../witcher-styles.css.md).

[Протокол и границы](../../../review-log.md#task-0004005) — TASK-0004.005; процессы [R005-13](../../../cross-check-0002.md#r005-13). В этой порции выполнена статическая сверка; поведенческие опыты принадлежат датированным прежним протоколам, а не новому прогону.
