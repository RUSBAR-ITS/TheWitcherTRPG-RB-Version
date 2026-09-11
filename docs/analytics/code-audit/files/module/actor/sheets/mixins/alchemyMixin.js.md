# module/actor/sheets/mixins/alchemyMixin.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/actor/sheets/mixins/alchemyMixin.js](../../../../../../../../module/actor/sheets/mixins/alchemyMixin.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `7dbb31bdbd094f58c77c9e58dd5a684df6bb942c` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.034](../../../../../../../tasks/task-0003.034.md), 5 файлов, 251 логическая строка |
| Запись перекрёстной сверки | [TASK-0003.034](../../../../../review-log.md#task-0003034) |

## Назначение файла

Примесь листа персонажа, формирующая массив описаний девяти алхимических веществ из уже вычисленных счётчиков контекста.

## Условия использования

alchemyMixin импортируется WitcherCharacterSheet и смешивается в его прототип. _prepareContext присваивает результат context.alchemyComponentsList после _prepareSubstances. Поиск alchemyComponentsList в module/templates дал только это присваивание и определение метода; шаблон substances.hbs читает отдельные *Count и не использует полученный массив.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| alchemyMixin | Экспорт объекта; 1–15 | Один метод подготовки | Object.assign в WitcherCharacterSheet | Не изменяет контекст при импорте |
| _prepareAlchemyComponentsList | Метод; 2–14 | Создать девять объектов key/label/image/count | Результат alchemyComponentsList | Массив и объекты создаются заново при вызове |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| _prepareAlchemyComponentsList(context) | Контекст со счётчиками vitriolCount…fulgurCount | Массив из девяти объектов | Фиксированный порядок и названия, count берётся из соответствующего поля | Не вычисляет суммы, не вызывает localize, не подставляет 0 при отсутствии счётчика. При {} все count undefined; при отсутствии самого context чтение поля некорректно. Записи документов нет. |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| *Count из _prepareSubstances | [module/actor/sheets/WitcherCharacterSheet.js](../../../../../../../../module/actor/sheets/WitcherCharacterSheet.js) | контекст | 4–12: vitriolCount/rebisCount/aetherCount/quebrithCount/hydragenumCount/vermilionCount/solCount/caelumCount/fulgurCount | Producer:220–237; caller:131 |
| Array.prototype.sum('quantity') | [module/actor/sheets/WitcherActorSheet.js](../../../../../../../../module/actor/sheets/WitcherActorSheet.js) | косвенная числовая зависимость | Вычисление счётчиков до вызова | 18–23: Number(item.system[prop] ?? 0) |
| getSubstance | [module/actor/mixins/craftingMixin.js](../../../../../../../../module/actor/mixins/craftingMixin.js) | косвенный поиск данных | Producer использует ключи девяти веществ | Stored исключён, нулевые записи могут оставаться |
| image basename | assets/images/{vitriol,rebis,aether,quebrith,hydragenum,vermilion,sol,caelum,fulgur}.png — вне пофайлового анализа | описательные данные | 4–12: только имя файла, без полного пути | Все девять файлов существуют; HTTP и изображение не проверялись |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/actor/sheets/WitcherCharacterSheet.js](../../../../../../../../module/actor/sheets/WitcherCharacterSheet.js) | alchemyMixin; _prepareAlchemyComponentsList | import:5, вызов:131, Object.assign:481 | Функция прототипа совпадает с экспортом, полный контекст проверен |

Область поиска: module/ и templates/ текущего checkout; прямые импорты и места вызова сверены отдельно от динамических обращений. Типы и листы сверены с system.json, module/setup/registerDataModels.js и module/setup/registerSheets.js. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Точный порядок/форма: {key:'vitriol',label:'Vitriol',image:'vitriol.png',count:context.vitriolCount}, затем rebis/Rebis/rebis.png, aether/Aether/aether.png, quebrith/Quebrith/quebrith.png, hydragenum/Hydragenum/hydragenum.png, vermilion/Vermilion/vermilion.png, sol/Sol/sol.png, caelum/Caelum/caelum.png, fulgur/Fulgur/fulgur.png. label — буквальное имя с заглавной первой буквой, не ключ локализации.

Не меняет context, Actor, Item и настройки. Текущая панель реализует сходный фиксированный перечень самостоятельно; по имени метода нельзя заключать, что массив управляет её рендером.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Маппинг | Группа 05 | Счётчики 0…8 сохранены в девяти записях, исходный context прежний; при {} count undefined | Нет UI-потребителя массива |
| Полный контекст | Группа 06 | vitriolCount=3 и alchemyComponentsList[0].count=3 | Панель проверена отдельно и читает исходный счётчик |
| Ресурсы/подключение | Группы 05,21 | 9 PNG существуют, Object.assign совпадает | Assets вне покрытия |

## Непроверенные участки и открытые вопросы

Файл прочитан полностью. Проверки выполнены в Node 24.16.0 с установленным кодом Foundry 14.367.0. Использованы реальные модели и методы системы; Application/Document-оболочки, DOM, UUID-резолвер, запись документов и чат заменены фасадами. Мир, браузер, HTTP и БД не запускались. Точные границы и сценарии приведены в журнале .034; чтение соседних определений не засчитывается как их новый полный разбор.

## Связанные проблемы

Новых проблем не зарегистрировано. Отсутствие потребителя массива не превращено в задачу удаления или замены интерфейса.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `7dbb31bdbd094f58c77c9e58dd5a684df6bb942c`; полный файл | Первая карточка; [сверка порции](../../../../../review-log.md#task-0003034) |
