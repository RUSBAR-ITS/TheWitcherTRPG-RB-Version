# templates/sheets/item/configuration/tabs/regionPropertiesConfiguration.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/sheets/item/configuration/tabs/regionPropertiesConfiguration.hbs](../../../../../../../../../templates/sheets/item/configuration/tabs/regionPropertiesConfiguration.hbs) |
| Тип файла | Handlebars, HTML-шаблон |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `8cca18e14b75ec53028ee6bc49a837597de4d9af` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.013](../../../../../../../../tasks/task-0003.013.md), одна порция из восьми файлов |
| Запись перекрёстной сверки | [TASK-0003.013](../../../../../../review-log.md#task-0003013) |

## Назначение файла

Общая вкладка настройки региона: запрошенный флаг создания региона и четыре ссылки на макросы событий. При сверке обнаружено, что первый флаг отсутствует в текущей модели, а штатный рендер вкладки блокируется отдельным условием конфигурации.

## Условия использования

PARTS.regionProperties WitcherPropertiesConfigurationSheet; наследуется конфигурацией Spell. Требует tabs.regionProperties, item.system.regionProperties и schema. Для текущей SpellData присутствует кнопка вкладки, но part исключается по отсутствующему system.createTemplate. Прямой рендер при проверке — диагностический сценарий, а не обычный путь открытия окна.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| Корень | 1–2 | Вкладка regionProperties | data-group primary/data-tab regionProperties | Класс из tabs |
| createRegionFromTemplate | formGroup3–7 | Запрошенный шаблоном флаг | Отсутствует в RegionProperties.defineSchema | Helper получает undefined |
| behaviours.tokenEnter | formGroup8–12 | Macro для входа | DocumentUUIDField type Macro | Схемный label |
| behaviours.tokenTurnStart | formGroup13–17 | Macro начала хода | DocumentUUIDField type Macro | Схемный label |
| behaviours.tokenMoveWithin | formGroup18–22 | Macro движения внутри | DocumentUUIDField type Macro | label модели использует имя tokenPreMove |
| behaviours.tokenExit | formGroup23–27 | Macro выхода | DocumentUUIDField type Macro | Схемный label |

## Основные функции и методы

JS-функций нет. Пять безусловных formGroup(localize=true), без своих options/conditions/actions. Schema/value пути совпадают по четырём behaviours-полям, но createRegionFromTemplate не определён ни в одной схеме текущей системы.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| RegionProperties | [module/data/item/templates/regions/regionPropertiesData.js](../../../../../../../../../module/data/item/templates/regions/regionPropertiesData.js) | Schema/value | Только поле behaviours на корне | defineSchema и миграция прочитаны |
| regionBehaviours() | [module/data/item/templates/regions/regionBehavioursData.js](../../../../../../../../../module/data/item/templates/regions/regionBehavioursData.js) | Вложенные поля | Четыре DocumentUUIDField Macro, required:false | Полное определение фабрики |
| TemplateProperties.createTemplate | [module/data/item/templates/regions/templatePropertiesData.js](../../../../../../../../../module/data/item/templates/regions/templatePropertiesData.js) | Смежная схема | Фактическая настройка создания шаблона, не createRegionFromTemplate | Определение и spell-sheet путь |
| WitcherPropertiesConfigurationSheet | [module/item/sheets/configurations/WitcherPropertiesConfigurationSheet.js](../../../../../../../../../module/item/sheets/configurations/WitcherPropertiesConfigurationSheet.js) | PARTS/TABS/context | Проверка system.createTemplate вместо вложенного поля | _configureRenderParts:75 |
| formGroup/DocumentUUIDField | Foundry 14.367.0; client/applications/handlebars.mjs, common/data/fields.mjs | Helpers/модель | Генерация полей, реакция на отсутствующее определение | Исходный formGroup логирует ошибку и возвращает пустой SafeString |
| WITCHER.Item.RegionProperties.* | [lang/ru.json](../../../../../../../../../lang/ru.json); [lang/en.json](../../../../../../../../../lang/en.json) | Локализация | Названия четырёх событий | Сопоставлены через схему |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/item/sheets/configurations/WitcherPropertiesConfigurationSheet.js](../../../../../../../../../module/item/sheets/configurations/WitcherPropertiesConfigurationSheet.js) | Шаблон | PARTS.regionProperties,24–28 | Рендер фильтруется отдельно |
| [module/data/item/templates/regions/regionPropertiesData.js](../../../../../../../../../module/data/item/templates/regions/regionPropertiesData.js) | behaviours.* | createRegionBehaviour и addBehaviorsToRegions создают executeMacro по ключам | Точечное чтение; регионы не создавались |
| [module/data/item/mixin/spellRegionMixin.js](../../../../../../../../../module/data/item/mixin/spellRegionMixin.js) | regionProperties | createSpellRegion вызывает добавление behaviours | Проверена связь, не весь процесс |

## Данные и изменения состояния

При наличии шаблона обычная форма записывает UUID макросов в system.regionProperties.behaviours.*. В диагностическом рендере первый formGroup не создаёт control и пишет «Non-existent data field…»; исключения, прерывающего весь рендер, нет. Остальные четыре поля формируются.

Модель RegionProperties.migrateData безусловно присваивает tokenMoveWithin=tokenPreMove. Настоящая модель с новым UUID и без старого поля получила tokenMoveWithin:null; со старым полем перенос работает, а при двух значениях побеждает старое. Эта потеря относится к очистке данных, отдельно от скрытия UI.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Пять путей | Реальная схема Spell/RegionProperties плюс исходный formGroup | Четыре Macro-поля найдены; createRegionFromTemplate отсутствует и пропущен с одним сообщением | toFormGroup представлен фасадом учёта путей |
| Видимость | Нормальная Spell с templateProperties.createTemplate true/false | Вкладка есть в tabs, тела нет в parts при обоих значениях | Браузер не запускался |
| Новый/старый макрос | Настоящие RegionProperties с tokenMoveWithin, tokenPreMove и обоими | Новый→null; старый→новый; оба→старое значение | Не сохранение реального Macro/Region |

## Непроверенные участки и открытые вопросы

Не создавались зоны и behaviours, не запускались executeMacro или взаимодействие нескольких клиентов. Модели регионов прочитаны в пределах используемых полей/миграции, не получают статуса полного разбора в этой порции. Не предполагается, что устранение одного UI-разрыва исправляет весь процесс регионов.

## Связанные проблемы

[issue-00074](../../../../../../../../issues/potential/issue-00074.md), [issue-00075](../../../../../../../../issues/potential/issue-00075.md), [issue-00076](../../../../../../../../issues/potential/issue-00076.md) — условия PARTS, отсутствующий флаг и перезапись нового поля макроса.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.013 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.
