# module/item/sheets/configurations/WitcherPropertiesConfigurationSheet.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/item/sheets/configurations/WitcherPropertiesConfigurationSheet.js](../../../../../../../../module/item/sheets/configurations/WitcherPropertiesConfigurationSheet.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `8cca18e14b75ec53028ee6bc49a837597de4d9af` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.013](../../../../../../../tasks/task-0003.013.md), одна порция из восьми файлов |
| Запись перекрёстной сверки | [TASK-0003.013](../../../../../review-log.md#task-0003013) |

## Назначение файла

Общий редактор боевых свойств Item: вкладки урона, защиты и регионов, контекст silverTrait и действия над записями предметных воздействий. Наследует управление документами ActiveEffect из базовой конфигурации.

## Условия использования

Default export WitcherPropertiesConfigurationSheet extends WitcherConfigurationSheet; экземпляр используется оружием, а подклассы WitcherSpellConfigurationSheet/WitcherArmorConfigurationSheet заменяют general-шаблон. Класс не наследует системный WitcherItemSheet: это отдельная ветка от HBM(ItemSheetV2).

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| WitcherPropertiesConfigurationSheet | Класс 3–116 | Редактор общих боевых свойств | Default export | Подготовка/рендер и изменение данных |
| DEFAULT_OPTIONS.actions | Static5–10 | addEffect/removeEffect | Собственные actions поверх inherited options | Указывают на _onAddEffect/_oRemoveEffect; editEffect обрабатывается change |
| PARTS | Static12–29 | Добавляет damageProperties/defenseProperties/regionProperties | Spread super.PARTS | Всего семь описателей до фильтрации |
| TABS.primary | Static31–43 | general,damageProperties,defenseProperties,regionProperties,activeEffects | Наследует initial/labelPrefix | Пять записей до фильтрации |
| context.settings.silverTrait | 45–51 | Режим серебряного свойства | Локальная добавка к context | Читает настройку системы |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| _prepareContext(options) | super context | Promise<context> | Добавляет settings.silverTrait | Читает game.settings; не сохраняет |
| _prepareTabs(group) | Результат super._prepareTabs | Объект вкладок | Только primary: удаляет вкладки без соответствующего system.*Properties | Наличие regionProperties достаточно, createTemplate здесь не проверяется |
| _configureRenderParts(options) | Результат HBM super; item.system | Объект частей | Удаляет damage, только если нет damageProperties и causeDamages; defense при отсутствии; region при !system.createTemplate | Критерии отличаются от _prepareTabs и текущей вложенности templateProperties |
| _onChangeForm(formConfig,event) | Change формы | undefined | Сначала super, затем для data-action editEffect вызов _onEditEffect | Не ждёт inherited submit и ручной update; разные пути записи |
| static _onAddEffect(event,element) | dataset.target | Promise<void> | randomID; update target.ID={percentage:0} | Не ждёт update; defaults остальных полей добавляет модель |
| _onEditEffect(event,element) | Ближайшая .list-item: id/target; dataset.field; value | Promise<void> | Если value=='on', подставляет checked; update target.id.field | Тип checkbox определяется текстом, issue-00060; update не awaited |
| static _oRemoveEffect(event,element) | Ближайшая .list-item id/target | Promise<void> | update target.-=id:null | Старый deletion-синтаксис; в Foundry 14 преобразуется в ForcedDeletion с compatibility warning; закомментированная _del ветвь не выполняется |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| WitcherConfigurationSheet | [module/item/sheets/configurations/WitcherConfigurationSheet.js](../../../../../../../../module/item/sheets/configurations/WitcherConfigurationSheet.js) | ES import/наследование/super | Все общие options/context/PARTS/TABS и управление ActiveEffect | Полный предыдущий разбор и текущая сверка |
| Шаблоны properties | [templates/sheets/item/configuration/tabs/damagePropertiesConfiguration.hbs](../../../../../../../../templates/sheets/item/configuration/tabs/damagePropertiesConfiguration.hbs); [templates/sheets/item/configuration/tabs/defensePropertiesConfiguration.hbs](../../../../../../../../templates/sheets/item/configuration/tabs/defensePropertiesConfiguration.hbs); [templates/sheets/item/configuration/tabs/regionPropertiesConfiguration.hbs](../../../../../../../../templates/sheets/item/configuration/tabs/regionPropertiesConfiguration.hbs) | Рендер PARTS | Три локальных описателя | Все HBS прочитаны |
| game.settings silverTrait | [module/setup/settings.js](../../../../../../../../module/setup/settings.js) | Чтение настройки | 48; вывод silverTrait либо silverDamage | Регистрация 37–43 и два режима шаблона |
| damageProperties, defenseProperties | [module/data/item/templates/combat/damagePropertiesData.js](../../../../../../../../module/data/item/templates/combat/damagePropertiesData.js); [module/data/item/templates/combat/defensePropertiesData.js](../../../../../../../../module/data/item/templates/combat/defensePropertiesData.js) | Чтение/редактирование models | Проверки вкладок, поля/effects | Настоящие схемы |
| regionProperties; templateProperties | [module/data/item/templates/regions/regionPropertiesData.js](../../../../../../../../module/data/item/templates/regions/regionPropertiesData.js); [module/data/item/templates/regions/templatePropertiesData.js](../../../../../../../../module/data/item/templates/regions/templatePropertiesData.js) | Чтение внешней схемы | Фильтрация частей и поля региона | Новый путь createTemplate отсутствует в проверке 75 |
| ApplicationV2._prepareTabs; HBM._configureRenderParts; formGroup; Item.update/randomID | Foundry 14.367.0, client/applications/api/application.mjs и handlebars-application.mjs; client/applications/handlebars.mjs | Внешний API | Сборка, рендер и запись | Оригинальные методы/поля исполнены, DocumentSheet/DOM/update представлены фасадами |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/item/sheets/WitcherWeaponSheet.js](../../../../../../../../module/item/sheets/WitcherWeaponSheet.js) | Экземпляр configuration | Оружие открывает общий редактор | Поле 6 |
| [module/item/sheets/configurations/WitcherSpellConfigurationSheet.js](../../../../../../../../module/item/sheets/configurations/WitcherSpellConfigurationSheet.js); [module/item/sheets/configurations/WitcherArmorConfigurationSheet.js](../../../../../../../../module/item/sheets/configurations/WitcherArmorConfigurationSheet.js) | Класс/PARTS | Наследование; замена general | Оба определения проверены |
| [templates/sheets/item/configuration/tabs/damagePropertiesConfiguration.hbs](../../../../../../../../templates/sheets/item/configuration/tabs/damagePropertiesConfiguration.hbs) | addEffect/removeEffect/editEffect | Список damageProperties.effects | data-target/id/field сверены |
| [templates/sheets/item/configuration/tabs/defensePropertiesConfiguration.hbs](../../../../../../../../templates/sheets/item/configuration/tabs/defensePropertiesConfiguration.hbs); [templates/sheets/item/configuration/tabs/regionPropertiesConfiguration.hbs](../../../../../../../../templates/sheets/item/configuration/tabs/regionPropertiesConfiguration.hbs) | Настройки через обычную форму | formGroup по schema | Проверка всех путей |

## Данные и изменения состояния

Вкладки и части — отдельные структуры. Для Weapon видимы general/damage/defense/activeEffects, регион отсутствует. Для Armor — general/defense/activeEffects. Для Spell regionProperties входит в tabs, но исключается из parts и при false, и при true настоящего templateProperties.createTemplate. Наличие кнопки вкладки не доказывает рендер её тела.

Ручные effects — TypedObjectField записей name/statusEffect/percentage/varEffect. Это не Item.effects с документами ActiveEffect; последними управляет inherited onManageActiveEffect. Изменения ручной строки не имеют name HTML-поля, поэтому их динамический target/field обслуживается _onEditEffect.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Матрица parts/tabs | Настоящие классы, Core HBM/Application методы, Weapon/Armor/Spell | Weapon6 parts, Armor5, Spell6; регион есть только в tabs Spell; true вложенного createTemplate результат не меняет | Не полноценный браузерный Application |
| Операции effects | Реальные методы; update перехвачен; WeaponData.updateSource | Добавление со случайным ID; on→false→строка false; percentage25; удаление -=fx прошло | Запись в БД отсутствует |
| Контекст и шаблон | Восемь сочетаний silverTrait/staminaIsVar/defenseDifferenceMultiplier | Две серебряные ветви; cap по флагу; disabled улучшения, varEffect только при переменной stamina | formGroup настоящий; field.toFormGroup и selectOptions — фасады |
| Отсутствующее поле региона | Прямой рендер шаблона с настоящей схемой Spell | Core formGroup пишет сообщение и возвращает пустую строку; четыре Macro-поля остаются | Штатный региональный PART скрыт отдельной ошибкой |

## Непроверенные участки и открытые вопросы

UI сохранения, цикл частичного рендера при смене активной вкладки, сетевые ошибки update и сторонние подмены моделей не проверялись. Область поиска — module/, templates/, текущие определения ядра. Регионы создающими методами не запускались.

## Связанные проблемы

[issue-00060](../../../../../../../issues/potential/issue-00060.md), [issue-00074](../../../../../../../issues/potential/issue-00074.md), [issue-00075](../../../../../../../issues/potential/issue-00075.md) — текст on, фильтрация региона по старому пути и отсутствующее поле его шаблона.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.013 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.

## Уточнение TASK-0003.014

2026-09-10, `0fa589bd300856ff309f362afcb66d6fa43401ab`; исходник неизменен. [Перекрёстная сверка](../../../../../review-log.md#task-0003014).

Полностью разобрана [module/item/sheets/configurations/WitcherArmorConfigurationSheet.js](../../../../../../../../module/item/sheets/configurations/WitcherArmorConfigurationSheet.js): она заменяет только PARTS.general, остальные настройки наследует. Для FullCover/Shield сохранены general/defenseProperties/activeEffects и пять частей; general всегда выводит 12 исходных SP-полей. Наличие defenseProperties в форме не компенсирует отсутствующие методы делегирования ArmorData ([issue-00085](../../../../../../../issues/potential/issue-00085.md)).
