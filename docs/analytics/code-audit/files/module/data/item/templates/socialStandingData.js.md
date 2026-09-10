# module/data/item/templates/socialStandingData.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/data/item/templates/socialStandingData.js](../../../../../../../../module/data/item/templates/socialStandingData.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `29319a7a7e1dfc0663edbc15166f3b6a19682a2f` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.018](../../../../../../../tasks/task-0003.018.md), одна порция из восьми файлов |
| Запись перекрёстной сверки | [TASK-0003.018](../../../../../review-log.md#task-0003018) |

## Назначение файла

Фабрика пяти строк регионального социального положения расы. Определяет структуру таблицы, которую формы отображают и редактируют.

## Условия использования

Default function socialStanding вызывается только RaceData.defineSchema для SchemaField socialStanding. Это функция схемы, не класс Actor и не обработчик социального броска.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| fields | Alias,1 | Конструкторы | foundry.data.fields | Локально |
| socialStanding | Default function,3–11 | Создать пять StringField | Импорт RaceData | Новые Field при каждом вызове |
| north, nilfgaard, skellige, dolBlathanna, mahakam | StringField,5–9 | Пять региональных значений | initial='' у всех | Ключ dolBlathanna с заглавной B; не homeland ключ dolblathanna |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| socialStanding() | foundry.data.fields | {north,nilfgaard,skellige,dolBlathanna,mahakam} | Создаёт 5 полей без choices | Без вычисления штрафа, определения текущего региона, чтения Actor или записи |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| StringField | Foundry 14.367.0, /opt/foundryvtt/common/data/fields.mjs | Внешняя схема | 5–9 | Пустые строки/произвольное customStanding приняты |
| WITCHER.socialStanding | [module/setup/config.js](../../../../../../../../module/setup/config.js) | Словарь у потребителей | selectOptions в формах | 6 значений: equal,tolerated,hated,feared,toleratedFeared,hatedFeared; это UI-опции, не choices фабрики |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/data/item/raceData.js](../../../../../../../../module/data/item/raceData.js) | socialStanding() | Import3, SchemaField19 | Единственный прямой caller |
| [templates/sheets/item/race-sheet.hbs](../../../../../../../../templates/sheets/item/race-sheet.hbs) | system.socialStanding.<регион> | 5 именованных select | Те же ключи/регистр |
| [templates/partials/character/tab-profession.hbs](../../../../../../../../templates/partials/character/tab-profession.hbs) | race.system.socialStanding.<регион> | 5 inline-edit с data-field Item | 302–323, обработчик itemMixin |
| [module/actor/sheets/mixins/itemMixin.js](../../../../../../../../module/actor/sheets/mixins/itemMixin.js) | data-field system.socialStanding.<регион> | _onItemInlineEdit пишет выбранный Item по ID | Контроль: payload system.socialStanding.north='feared' |

Область поиска: текущие module/ и templates/; регистрации сверены отдельно. Динамические обращения внешних модулей не исследовались.

## Данные и изменения состояния

Содержит региональные строки Item. Actor.general.socialStanding — отдельная единственная строка, заданная generalData и используемая skillMixin.addSocialStanding. Прямой связи копирования/выбора региона между ними в module/templates не найдено. Общий словарь 6 значений используется в обеих формах, но совместное использование options не синхронизирует данные.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Полнота/поля | 11 логических строк,2 вызова фабрики | 5 ключей, все initial='', разные экземпляры полей | Количество строк учитывает последнюю строку без перевода |
| Форма/строки | Настоящие RaceData, optionGroups, inline-handler | hated/equal верно выбраны; запись north адресует Item; general.socialStanding остаётся equal | Перехват update, без БД |
| Потребитель формулы | Настоящий addSocialStanding,7 значений Actor | equal/'' не дали штрафа даже при Race.north=hated; hated дал -2 харизме | Математика зафиксирована по коду, соответствие рулбуку не проверялось |

## Непроверенные участки и открытые вопросы

Фабрика прочитана целиком. Нет автоматического выбора региона или числовых полей. Незаполненные/неизвестные строки допускаются схемой; необходимость ограничения требует отдельного решения. Полный аудит социальных бросков — за пределами этой порции.

## Связанные проблемы

Новых проблем самой фабрики не обнаружено в пределах проверки. Различие таблицы расы и активного положения Actor описано как фактическое разделение данных.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.018 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.
