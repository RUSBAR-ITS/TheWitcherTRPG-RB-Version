# module/item/sheets/WitcherWeaponSheet.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/item/sheets/WitcherWeaponSheet.js](../../../../../../../module/item/sheets/WitcherWeaponSheet.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `8cca18e14b75ec53028ee6bc49a837597de4d9af` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.013](../../../../../../tasks/task-0003.013.md), одна порция из восьми файлов |
| Запись перекрёстной сверки | [TASK-0003.013](../../../../review-log.md#task-0003013) |

## Назначение файла

Специализированный лист оружия. Подключает основную форму и общую конфигурацию боевых свойств, готовит список навыков, связывает checkbox видов урона с записью system.type и принимает подходящий рецепт.

## Условия использования

Default export WitcherWeaponSheet extends WitcherItemSheet; зарегистрирован как лист типа weapon. После конструктора общий configuration заменяется экземпляром WitcherPropertiesConfigurationSheet для того же Item. Один PARTS.main содержит weapon-sheet.hbs. Object.assign добавляет методы associatedDiagramMixin в prototype при загрузке модуля.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| WitcherWeaponSheet | Класс 5–55 | Лист оружия | Default export, Items.registerSheet weapon | Создание, подготовка, рендер, действия |
| configuration | Поле экземпляра 6 | Окно свойств того же Item | Новый WitcherPropertiesConfigurationSheet | Открывает inherited configureItem |
| PARTS.main | Static8–13 | Основная форма | template + scrollable:[''] | Обрабатывает HandlebarsApplicationMixin |
| context.config.attackSkills | Присваивание 19–25 | Массив восьми melee/ranged записей skillMap | config — ссылка CONFIG.WITCHER | Перезаписывается при подготовке; прямой читатель массива вне присваивания не найден |
| Методы associatedDiagramMixin | Object.assign57 | Подключение/снятие рецепта | Добавлены к prototype | Определены в отдельном файле |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| _prepareContext(options) | Контекст super и CONFIG.WITCHER | Promise<context> | Объединяет meleeSkills/rangedSkills; map в skillMap; Set устраняет одинаковые ссылки; пишет attackSkills | Мутирует общую config-ссылку в памяти; не Item |
| activateListeners(html) | DOM-root; jQuery $ | undefined | super; .damage-type change→_onDamageTypeEdit; _addAssociatedDiagramListeners | Вызывается реальным WitcherItemSheet._onRender; совместимость не выводится только из старого имени API |
| _onDamageTypeEdit(event) | currentTarget.id, текущее system.type | undefined | preventDefault; shallow-copy; инвертирует флаг по id; составляет локализованный text slashing/piercing/bludgeoning/elemental; update system.type | Ориентируется на модель, не element.checked; update не awaited |
| _onDropItem(event,item) | Документ с drop-router общего листа | Promise<void> | Делегирует _onDropDiagram с weapon и elderfolk-weapon | Не возвращает/не await-ит внутренний Promise; перенесённый документ в return не попадает |
| _addAssociatedDiagramListeners / _onRemoveAssociatedDiagram / _onDropDiagram | Примесь | См. внешний файл | Снятие связи, проверка области/типа и запись UUID | Не определения этого файла; проверены как вызванные сущности |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| WitcherPropertiesConfigurationSheet | [module/item/sheets/configurations/WitcherPropertiesConfigurationSheet.js](../../../../../../../module/item/sheets/configurations/WitcherPropertiesConfigurationSheet.js) | Import/создание | Строки 1,6; configuration | Класс/поля/рендер сверены |
| WitcherItemSheet | [module/item/sheets/WitcherItemSheet.js](../../../../../../../module/item/sheets/WitcherItemSheet.js) | Import/наследование | Базовые context, _onRender, формы/Drop | Прямой вызов activateListeners на 75; исполнялся _onRender |
| associatedDiagramMixin | [module/item/sheets/mixins/associatedDiagramMixin.js](../../../../../../../module/item/sheets/mixins/associatedDiagramMixin.js) | Import/Object.assign/вызов | 35,53,57 | Три метода прочитаны и вызваны отдельно |
| CONFIG.WITCHER.meleeSkills/rangedSkills/skillMap | [module/setup/config.js](../../../../../../../module/setup/config.js) | Глобальное чтение | 19–25 | Восемь записей массива |
| weapon-sheet.hbs | [templates/sheets/item/weapon-sheet.hbs](../../../../../../../templates/sheets/item/weapon-sheet.hbs) | PARTS template | 10 | Форма и listeners совпали |
| jQuery $, Item.update, core _onRender/DragDrop | Foundry 14.367.0 и jQuery клиента | Внешний API | Подписки/обновления; наследуемый рендер | CoreItem/DragDrop настоящие, jQuery/DOM/update в тесте заменены |
| WITCHER.DamageType.* | [lang/ru.json](../../../../../../../lang/ru.json); [lang/en.json](../../../../../../../lang/en.json) | Локализация | 44–47, формирование text | Ключи и русский результат проверены |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/setup/registerSheets.js](../../../../../../../module/setup/registerSheets.js) | WitcherWeaponSheet | Items.registerSheet, types:['weapon'] | 100–104 |
| [templates/sheets/item/weapon-sheet.hbs](../../../../../../../templates/sheets/item/weapon-sheet.hbs) | _onDamageTypeEdit через .damage-type | Четыре checkbox с id без name | Пути/подписка сверены |
| [templates/partials/associated-diagram.hbs](../../../../../../../templates/partials/associated-diagram.hbs) | Методы примеси | data-type=associatedDiagram и .remove-associated-diagram | Разметка и допустимые drop-тип/UUID |

## Данные и изменения состояния

Выбор checkbox записывает весь shallow-copy system.type с текстовым описанием, сохраняя остальные флаги. При slashing:true и событии piercing результат — «Режущий, Колющий». Настройки урона/защиты находятся в configuration и отдельном шаблоне, а не в основном листе.

Drop рецепта меняет associatedDiagramUuid; соответствующий предмет не создаётся в инвентаре. _onDropDiagram проверяет event.target.offsetParent.dataset.type. Если offsetParent отсутствует, возникает исключение; если он относится к другой области, связь не устанавливается. Фактическая геометрия offsetParent в браузере не проверялась.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Регистрация/рендер | Исходники регистратора/родителя; изолированный _onRender | Подключены .damage-type change и .remove-associated-diagram click | Реальные классы, DOM/jQuery — фасад |
| Изменение вида | Вызван захваченный change-listener на настоящем листе/модели | system.type записан с piercing:true и русским text | update перехвачен |
| Рецепт | weapon recipe, armor recipe, remove; offsetParent=null | Правильный UUID передан; неверный тип дал предупреждение без update; снятие→''; null→ошибка dataset | Полный пользовательский DragEvent не создавался |
| Контекст | Настоящий _prepareContext | Восемь skills; context.config===CONFIG.WITCHER | Не утверждается использование attackSkills формой: читатель не найден |

## Непроверенные участки и открытые вопросы

Исходник и текущие связи сопоставлены в TASK-0004.006. Прежние ссылки на будущий пофайловый разбор TASK-0003 больше не являются очередью: он завершён. Остались конкретные границы сквозной проверки: [U006-01](../../../../cross-check-0002.md#u006-01); [U006-05](../../../../cross-check-0002.md#u006-05). Shared CONFIG.attackSkills и отдельные recipe listeners не добавляют автоматического сохранения prepared данных.

## Связанные проблемы

[issue-00080](../../../../../../issues/potential/issue-00080.md) — зависимость привязки рецепта от offsetParent. Разрешён вопрос TASK-0003.012 о вызове activateListeners: он действительно вызывается родителем; нового наблюдения об отсутствии listener нет.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.013 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.

## Уточнение TASK-0003.016

2026-09-10, `53f74994011383cb544cabac96285430f00cb38a`; исходник неизменен. [Перекрёстная сверка](../../../../review-log.md#task-0003016).

Полный разбор [module/item/sheets/mixins/associatedDiagramMixin.js](../../../../../../../module/item/sheets/mixins/associatedDiagramMixin.js) подтвердил контракт _onDropDiagram(event,item,'weapon','elderfolk-weapon') и удаления пустой строкой. Части [templates/partials/associated-diagram.hbs](../../../../../../../templates/partials/associated-diagram.hbs) не имеют собственного picker: добавление происходит через drop. Новый [module/item/sheets/WitcherDiagramSheet.js](../../../../../../../module/item/sheets/WitcherDiagramSheet.js) на стороне рецепта отдельно пишет UUID результата; это не создание двусторонней связи. Геометрия offsetParent в браузере по-прежнему не проверена.

## Сквозная сверка TASK-0004.006

2026-09-14; rusbar-main, a176c4f18879f2e5a63b93bc15345fc26d9f535a. Исходник совпадает со срезом TASK-0001; изменено только описание.

Weapon sheet подключает основной HBS, properties configuration и associatedDiagramMixin. Четыре checkbox без name обрабатываются change.damage-type: переключается сохранённый Bool и обновляется type целиком. Shared CONFIG.attackSkills и отдельные recipe listeners не добавляют автоматического сохранения prepared данных.

Сопоставленные определения и потребители: [module/data/item/templates/weaponTypeData.js](../../data/item/templates/weaponTypeData.js.md), [module/data/item/weaponData.js](../../data/item/weaponData.js.md), [templates/sheets/item/weapon-sheet.hbs](../../../templates/sheets/item/weapon-sheet.hbs.md), [module/data/item/templates/associatedDiagramData.js](../../data/item/templates/associatedDiagramData.js.md).

[Протокол и границы](../../../../review-log.md#task-0004006) — TASK-0004.006; процессы [R006-08](../../../../cross-check-0002.md#r006-08). В этой порции выполнена статическая сверка; поведенческие опыты принадлежат датированным прежним протоколам, а не новому прогону.
