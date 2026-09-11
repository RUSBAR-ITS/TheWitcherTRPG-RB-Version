# module/data/actor/templates/character/pannelsData.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/data/actor/templates/character/pannelsData.js](../../../../../../../../../module/data/actor/templates/character/pannelsData.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `c9eac1ffb28fdf69935d500fff26d4d0ad1d1609` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.005](../../../../../../../../tasks/task-0003.005.md), одна порция из семи файлов |
| Запись перекрёстной сверки | [TASK-0003.005](../../../../../../review-log.md#task-0003005) |

## Назначение файла

Определяет 22 сохраняемых флага раскрытия разделов интерфейса на Actor. Имя pannels сохранено как в исходнике; это общее состояние документа, а не отдельные пользовательские настройки клиента.

## Условия использования

При импорте локальная const fields получает foundry.data.fields. Default export — фабрика определения схемы; каждый вызов создаёт новые поля. Очистку, начальные значения и валидацию применяет Foundry при создании/обновлении модели. CommonActorData:7,57 включает pannels() в SchemaField; поля наследуют CharacterData и MonsterData. Регистр и написание ключей используются шаблонами и динамическими обработчиками.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| fields | const, 2 | Классы полей | Локальная | Читается фабрикой |
| pannels | function, 4–31 | Схема состояния интерфейса | Default export | Возвращает 22 BooleanField |
| vitriolIsOpen, rebisIsOpen, aetherIsOpen, quebrithIsOpen, hydragenumIsOpen, vermilionIsOpen, solIsOpen, caelumIsOpen, fulgurIsOpen | BooleanField, 6–14 | Вещества | system.pannels.<ключ> | Все initial=false; обработчики переключают и сохраняют |
| noviceSpellIsOpen, journeymanSpellIsOpen, masterSpellIsOpen, ritualIsOpen, hexIsOpen, magicalgiftIsOpen | BooleanField, 16–21 | Магия | system.pannels.<ключ> | Все initial=false; обработчики переключают и сохраняют |
| intIsOpen, refIsOpen, dexIsOpen, bodyIsOpen, empIsOpen, craIsOpen, willIsOpen | BooleanField, 23–29 | Навыки | system.pannels.<ключ> | Все initial=false; обработчики переключают и сохраняют |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| pannels(); 4–31 | Доступен foundry.data.fields | Объект 22 BooleanField | Создаёт новые определения полей при каждом вызове | Синхронно; без записи документов, обработчиков событий и собственного catch |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| BooleanField | Foundry 14.367.0, /opt/foundryvtt/common/data/fields.mjs | Глобальный API | 2,6–29 | Начальные значения проверены настоящими моделями |
| Локальные импорты | Отсутствуют | — | Фабрика не регистрирует событий и не открывает UI | Все 31 строка |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/data/actor/commonActorData.js](../../../../../../../../../module/data/actor/commonActorData.js) | pannels() | SchemaField общих данных | Импорт 7; поле 57 |
| [module/actor/sheets/mixins/itemMixin.js](../../../../../../../../../module/actor/sheets/mixins/itemMixin.js) | Динамические subtype/spelltype + IsOpen | _onSubstanceDisplay/_onSpellDisplay читают флаг и вызывают Actor.update с !flag | 275–291; регистрация itemListener:334,338 |
| [module/actor/sheets/mixins/skillMixin.js](../../../../../../../../../module/actor/sheets/mixins/skillMixin.js) | Динамический skilltype + IsOpen | _onSkillDisplay формирует Actor.update | 17–24; регистрация skillListener:32 |
| [templates/partials/character/substances.hbs](../../../../../../../../../templates/partials/character/substances.hbs) | 9 флагов веществ | Класс sub-open и условное включение таблиц компонентов | 7–104; data-subtype на кликабельных элементах |
| [templates/sheets/actor/tabs/tab-inventory.hbs](../../../../../../../../../templates/sheets/actor/tabs/tab-inventory.hbs) | Шаблон веществ | Включает substances.hbs | 212; текущая PARTS.inventory персонажа |
| [templates/partials/monster/monster-spell-tab.hbs](../../../../../../../../../templates/partials/monster/monster-spell-tab.hbs) | 6 флагов магии | Стрелки и видимость таблиц; data-spelltype | 27–197; включение старым monster-sheet.hbs:302 |
| [templates/partials/monster/monster-skill-tab.hbs](../../../../../../../../../templates/partials/monster/monster-skill-tab.hbs) | 7 флагов навыков | Стрелки и таблицы; data-skilltype | 3–131; включение старым monster-sheet.hbs:289 |
| [module/actor/sheets/WitcherActorSheet.js](../../../../../../../../../module/actor/sheets/WitcherActorSheet.js) | Методы mixin | Подключение itemMixin/skillMixin и вызовы listeners | Object.assign:311,314; activateListeners |

Потребители искались по именам файлов/экспортов, точным и динамическим путям в module/, templates/ и packsJson/. В 226 JSON-компедиумах строковых ссылок с префиксами system.logs, system.skillTrainingN, system.pannels, system.attackStats не найдено. Бинарные packs, действующие БД и внешние макросы не проверялись.

## Данные и изменения состояния

Обработчики ищут ближайшие .substance/.spell/.skill и берут соответственно dataset.subtype/spelltype/skilltype. Затем сохраняют system.pannels.<имя>IsOpen=!текущееЗначение. Во всех 22 случаях динамический ключ совпал со схемой; переключение false→true и true→false проверено. Запись инициируется через Actor.update, его Promise обработчики не возвращают; отдельная проблема по этим действиям без дополнительных наблюдений не регистрировалась.

Следует различать использование шаблона и наличие файла: текущие зарегистрированные WitcherCharacterSheet и WitcherMonsterSheet выбирают новые tab-skills.hbs и tab-magic.hbs, которые не читают pannels для групп навыков/магии. Старые monster-* шаблоны используют 13 соответствующих флагов, но их присутствие и предзагрузка старого monster-sheet не доказывают текущий рендер этой версии листа. Девять флагов веществ связаны с текущим inventory персонажа. Картинки веществ находятся в assets/ и исключены из пофайлового анализа.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Состав и defaults | Реальные Common/Character/MonsterData | 22 поля, все false; одинаковый набор в обеих специализациях | Без UI |
| Динамические ключи ↔ определения | data-subtype/spelltype/skilltype из трёх шаблонов, исходные обработчики | 22 существующих ключа; 44 перехваченных обновления для двух направлений | DOM.closest/update подменены |
| Текущие ↔ старые шаблоны | registerSheets:105–112; PARTS обоих листов; includes monster-sheet:289/302 | Текущие skills/magic используют новые общие шаблоны; старые зависимости отделены | HTTP/DOM и альтернативные внешние регистрации не проверены |

## Непроверенные участки и открытые вопросы

Исходник прочитан полностью; соседние файлы проверены только в пределах описанных связей. Мир, браузер, реальное сохранение и полный жизненный цикл Actor/листов не запускались. Подмены и исполнявшийся сценарий приведены в журнале; успешная проверка карточки не подтверждает исправность всей системы. Не установлено использование старого monster-sheet сторонними модулями/макросами. Само сохранение оставшихся флагов не объявлено проблемой или основанием для удаления.

## Связанные проблемы

Новых проблем этой фабрики и проверенных динамических путей не выявлено.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.005 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.

## Уточнение TASK-0003.006

2026-09-10, `fe7ea7420cd4dfa6ee51baf7520f7b0ad8f8b13d`. Все 22 флага входят в CommonActorData.pannels:57 и наследуются обеими моделями. Папка character не означает исключительное применение персонажем; различия старых и текущих потребителей, установленные TASK-0003.005, сохраняются.

Карточки сборки: [commonActorData](../../commonActorData.js.md). [Сверка TASK-0003.006](../../../../../../review-log.md#task-0003006).

## Уточнение TASK-0003.029

2026-09-11, `273a6d7db0b7c866399db3ecd4f7191817ae6f10`. Полностью прочитан старый monster-skill-tab: семь <stat>IsOpen читаются для шеврона и invisible таблиц; _onSkillDisplay пишет тот же динамический путь по skilltype. Текущая вкладка использует details и tabs, не этот переключатель.

Сверенные связи: [module/actor/sheets/mixins/skillMixin.js](../../../../../../../../../module/actor/sheets/mixins/skillMixin.js); [templates/partials/monster/monster-skill-tab.hbs](../../../../../../../../../templates/partials/monster/monster-skill-tab.hbs); [templates/partials/character/tab-skills.hbs](../../../../../../../../../templates/partials/character/tab-skills.hbs). Полные карточки новых файлов — в [указателе порции](../../../../../README.md#навыки-броски-развитие-и-пользовательские-навыки--task-0003029). [Проверки, ограничения и версия](../../../../../../review-log.md#task-0003029). Исходники и статус проблем не менялись.
