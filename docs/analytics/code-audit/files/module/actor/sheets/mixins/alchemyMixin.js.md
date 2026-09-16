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

alchemyMixin импортируется WitcherCharacterSheet и смешивается в его прототип. _prepareContext присваивает результат context.alchemyComponentsList после _prepareSubstances. Текущий tab-inventory-diagrams.hbs:94–107 читает ../alchemyComponentsList внутри рецепта с isFormulae и показывает требуемые вещества и доступный запас. Отдельная панель substances.hbs читает *Count непосредственно. Различие этих потребителей уточнено в TASK-0004.007, N007-01.

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
| [templates/sheets/actor/partials/character/inventory/tab-inventory-diagrams.hbs](../../../../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-diagrams.hbs) | alchemyComponentsList: key/label/image/count | 94–107: isFormulae, ненулевое требование из alchemyComponents | Текущее чтение и N007-01, пять сценариев настоящего HBS |

Область поиска: module/ и templates/ текущего checkout; прямые импорты и места вызова сверены отдельно от динамических обращений. Типы и листы сверены с system.json, module/setup/registerDataModels.js и module/setup/registerSheets.js. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Точный порядок/форма: {key:'vitriol',label:'Vitriol',image:'vitriol.png',count:context.vitriolCount}, затем rebis/Rebis/rebis.png, aether/Aether/aether.png, quebrith/Quebrith/quebrith.png, hydragenum/Hydragenum/hydragenum.png, vermilion/Vermilion/vermilion.png, sol/Sol/sol.png, caelum/Caelum/caelum.png, fulgur/Fulgur/fulgur.png. label — буквальное имя с заглавной первой буквой, не ключ локализации.

Не меняет context, Actor, Item и настройки. Текущая панель реализует сходный фиксированный перечень самостоятельно; по имени метода нельзя заключать, что массив управляет её рендером.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Маппинг | Группа 05 | Счётчики 0…8 сохранены в девяти записях, исходный context прежний; при {} count undefined | Эта группа проверяла только producer; UI-потребитель подтверждён отдельно в TASK-0004.007, N007-01 |
| Полный контекст | Группа 06 | vitriolCount=3 и alchemyComponentsList[0].count=3 | Панель проверена отдельно и читает исходный счётчик |
| Ресурсы/подключение | Группы 05,21 | 9 PNG существуют, Object.assign совпадает | Assets вне покрытия |

## Непроверенные участки и открытые вопросы

В TASK-0004.007 текущие определения и потребители сопоставлены; прежние опыты TASK-0003.015/.016/.017 (2026-09-10) и .034 (2026-09-11) сохраняют собственные входы и фасады. Новая N007-01 проверяет producer/HBS на заданном контексте. Браузер, мир, сеть и запись в БД не запускались. Точные оставшиеся вопросы и ответственные блоки: [U007-01](../../../../../cross-check-0002.md#u007-01), [U007-07](../../../../../cross-check-0002.md#u007-07). Для этого файла установлены процессы R007-08, а не полный клиентский lifecycle.

## Связанные проблемы

Новых проблем не зарегистрировано. Ошибочное утверждение об отсутствии потребителя исправлено в TASK-0004.007. Таблица рецептов использует массив; это исправление документации, не дефект системы.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `7dbb31bdbd094f58c77c9e58dd5a684df6bb942c`; полный файл | Первая карточка; [сверка порции](../../../../../review-log.md#task-0003034) |

## Сквозная сверка TASK-0004.007

2026-09-14; rusbar-main, 6a26042f7881d9990c304483c7219e0698f6617e. Исходник совпадает со срезом TASK-0001; изменено только описание.

Примесь создаёт девять записей из *Count без изменения контекста. У массива есть consumer: tab-inventory-diagrams читает его при isFormulae, тогда как substances читает *Count напрямую. Ошибочное утверждение об отсутствии consumer исправлено; N007-01 подтвердила пять сочетаний требований/запаса/ветвления.

Сопоставленные определения и потребители: [module/actor/sheets/WitcherCharacterSheet.js](../WitcherCharacterSheet.js.md), [module/actor/sheets/WitcherActorSheet.js](../WitcherActorSheet.js.md), [module/actor/mixins/craftingMixin.js](../../mixins/craftingMixin.js.md), [templates/sheets/actor/partials/character/inventory/tab-inventory-diagrams.hbs](../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-diagrams.hbs.md).

[Протокол и границы](../../../../../review-log.md#task-0004007) — TASK-0004.007; процессы [R007-08](../../../../../cross-check-0002.md#r007-08). В этой порции выполнена статическая сверка; прежние опыты сохраняют свои даты и фасады. Единственный новый запуск N007-01 проверяет producer/HBS alchemyComponentsList на заданном контексте; его границы не распространяются на остальные процессы.
