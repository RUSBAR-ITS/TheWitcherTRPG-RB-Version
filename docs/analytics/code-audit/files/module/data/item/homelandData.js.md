# module/data/item/homelandData.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/data/item/homelandData.js](../../../../../../../module/data/item/homelandData.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `29319a7a7e1dfc0663edbc15166f3b6a19682a2f` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.018](../../../../../../tasks/task-0003.018.md), одна порция из восьми файлов |
| Запись перекрёстной сверки | [TASK-0003.018](../../../../review-log.md#task-0003018) |

## Назначение файла

Модель system предмета homeland: ключ родины из интерфейса и дополнительное название для варианта other. Это самостоятельная TypeDataModel, не наследник CommonItemData и не фабрика биографии Actor.

## Условия использования

Default export HomelandData зарегистрирован как CONFIG.Item.dataModels.homeland; тип homeland присутствует в system.json. WitcherHomelandSheet получает system через общий Item-лист. Actor-лист при наличии homeland Item показывает его значения вместо редактирования general.homeland.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| fields | Alias,1 | Конструкторы полей | foundry.data.fields | Импорт API через global |
| HomelandData | Класс,3–14 | Типизированные данные родины | Default export / registry homeland | TypeDataModel |
| metadata | static Object.freeze,4–6 | Объект {type:'homeland'} | Свойство класса | Поверхностно заморожен; отдельно от регистрации типа |
| value | StringField,10 | Ключ выбранной родины | initial='' | choices и enum в схеме нет |
| otherValue | StringField,11 | Свободное дополнительное имя | initial='' | Сохраняется независимо от value; отображается при other |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| static defineSchema():8–13 | foundry.data.fields | Объект из value/otherValue | Создаёт два StringField | Нет super.defineSchema, enrichedText, prepare* или migrateData собственного определения |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| TypeDataModel, StringField | Foundry 14.367.0, /opt/foundryvtt/common/abstract/type-data.mjs и common/data/fields.mjs | Наследование/поля | 3,10–11 | Настоящие модель и поля; только 2 ключа |
| Object.freeze | JavaScript, Node 24.16 в проверке | Заморозка | 4–6 | metadata.type=homeland, isFrozen=true |
| homeland | [system.json](../../../../../../../system.json) | Декларация типа | documentTypes.Item.homeland171 | Тип согласован с map/листом; HTML-поля отсутствуют |
| WITCHER.homelands | [module/setup/config.js](../../../../../../../module/setup/config.js) | Варианты у потребителя, не импорт модели | Через HomelandSheet/HBS | 26 вариантов, other включён; схема принимает customPlace |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/setup/registerDataModels.js](../../../../../../../module/setup/registerDataModels.js) | HomelandData | Import29, map59 | Тип system |
| [module/item/sheets/WitcherHomelandSheet.js](../../../../../../../module/item/sheets/WitcherHomelandSheet.js) | Модель Item homeland | Наследует общий контекст | Не переопределяет enrichedText |
| [templates/sheets/item/homeland-sheet.hbs](../../../../../../../templates/sheets/item/homeland-sheet.hbs) | value/otherValue | select и условный текстовый input | 16 строк, имена system.value/system.otherValue |
| [module/actor/sheets/WitcherCharacterSheet.js](../../../../../../../module/actor/sheets/WitcherCharacterSheet.js) | Первый homeland Item | getList155 | Контекст меняет источник отображения, не значения Actor |
| [templates/partials/character/tab-background.hbs](../../../../../../../templates/partials/character/tab-background.hbs) | homeland.system.value/otherValue | Ветка if homeland19–25 | Вместо input Actor выводятся labels |
| [templates/partials/character-header.hbs](../../../../../../../templates/partials/character-header.hbs) | homeland.system.value/otherValue | Ветка if homeland31–39 | other выводит свободный текст, иначе ключ локализации |
| [module/actor/witcherActor.js](../../../../../../../module/actor/witcherActor.js) | Отсутствие общих Item-полей | getList/getTotalWeight/addItem | isStored отсутствует→не исключён из getList; calcWeight?.() даёт fallback0. Стековый addItem — отдельный общий контракт |

Область поиска: текущие module/ и templates/; регистрации сверены отдельно. Динамические обращения внешних модулей не исследовались.

## Данные и изменения состояния

value/otherValue являются данными этого Item. Одноимённая пара в Actor.general.homeland задана другой фабрикой; эта модель её не импортирует и не синхронизирует. При наличии Item сохранённая биография остаётся прежней и возвращается в отображение после отсутствия/удаления альтернативного Item.

В собственной схеме нет description, sourcebook, quantity, cost, weight, isStored, isCarried или enrichedText. Настоящая очистка входа с quantity3 не дала quantity ни в prepared, ни в toObject модели. Отсутствие этих полей — различие типов; оно не доказывает поломку каждого общего метода Item. name/img/effects принадлежат Document отдельно от system. ActiveEffect доступен через общую конфигурацию и не требует наследования CommonItemData.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Defaults/metadata | Настоящая HomelandData в WitcherItem/common BaseItem | 2 поля со значением'', frozen metadata.type=homeland | Мир/клиентские документы не создавались |
| Допустимые строки | customPlace/Hidden и посторонний quantity3 | value/otherValue сохранены, quantity отсутствует | Произвольный ключ разрешён схемой; не объявлен ошибкой |
| Форма | other, '', nilfgaard, customPlace | Количество named полей 2/1/1/1;26 вариантов; otherValue остаётся в данных при невидимом input | Реальный HBS/optionGroups, DOM-фасад; браузерный submit не проверен |
| Альтернативный источник | Item other='Audit Place', Actor aedirn | Подготовка не изменила Actor; header показал Item при наличии, Actor при отсутствии | Удаление реального Item не выполнялось |
| Регистрация/эффекты | Манифест/map/sheet; configuration create | Тип согласован; create передал base ActiveEffect с origin Item UUID | Создание в БД заменено перехватом |

## Непроверенные участки и открытые вопросы

Все 14 строк прочитаны. Серверная регистрация, реальный submit/удаление, компедиумы и автоматическое именование Item не проверены. Наличие arbitrary строки при отсутствии option — свойство схемы/формы, не согласованная ошибка или новое ограничение. Новых числовых/игровых действий нет.

## Связанные проблемы

[issue-00005](../../../../../../issues/potential/issue-00005.md), [issue-00034](../../../../../../issues/potential/issue-00034.md). 5 не относится к homeland: тип есть во всех трёх декларациях. 34 касается общей смены уникального Item, не этой схемы.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.018 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.
