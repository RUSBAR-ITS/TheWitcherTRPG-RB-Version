# module/data/item/raceData.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/data/item/raceData.js](../../../../../../../module/data/item/raceData.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `29319a7a7e1dfc0663edbc15166f3b6a19682a2f` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.018](../../../../../../tasks/task-0003.018.md), одна порция из восьми файлов |
| Запись перекрёстной сверки | [TASK-0003.018](../../../../review-log.md#task-0003018) |

## Назначение файла

Модель system предмета race: общие сведения Item, четыре именованные текстовые особенности и таблица социального положения по пяти регионам. Готовит HTML особенностей для листов; числовых бонусов в этих полях нет.

## Условия использования

Default export RaceData extends CommonItemData. registerDataModels назначает CONFIG.Item.dataModels.race; system.json объявляет race и htmlFields description/*.description. Foundry создаёт system по типу Item, а RaceSheet или CharacterSheet явно вызывает enrichedText. При импорте только определяются класс и alias fields; бонусы, документы и эффекты от импорта не создаются.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| RaceData | Класс,8–31 | Данные race Item | Default export, CONFIG.Item.dataModels.race | Схема и async enrichedText |
| fields | Alias,6 | Доступ к конструкторам | foundry.data.fields | Захватывается при импорте |
| Общие поля | Spread commonData,10–13 | quantity,weight,cost,sourcebook,isHidden,isStored,isCarried и description | super.defineSchema из CommonItemData | quantity='1'; weight/cost=0; sourcebook=''; hidden/stored=false,carried=true |
| description | HTMLField,14 | Общее HTML-описание расы | Заменяет StringField общей схемы, initial='' | Ниже не входит в enrichedText; рассмотренные формы его не выводят |
| perk1, perk2, perk3, perk4 | Четыре SchemaField,15–18 | Фиксированные слоты особенностей | Каждый вызов perk() создаёт name/description | Пустые строки по умолчанию; не ArrayField, нет списка changes/механики бонусов |
| socialStanding | SchemaField,19 | Пять строк: north,nilfgaard,skellige,dolBlathanna,mahakam | socialStanding() | Справочная таблица расы, отдельная от Actor.general.socialStanding |
| Результат enrichedText | Новый объект,24–29 | perk1–perk4 → enriched/value/systemField | Возвращается вызывающему листу | Не новый документ и не сохранённое поле модели |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| static defineSchema():9–21 | CommonItemData и две фабрики | 13 полей верхнего уровня | Копирует 8 общих ключей; заменяет description на HTMLField; добавляет 4 perk и socialStanding | Синхронно; каждого поля свой экземпляр; choices/числовых правил особенностей нет |
| async enrichedText():23–30 | this.perk1–perk4.description и schema | Promise<{perk1,perk2,perk3,perk4}> | Четыре последовательных await createEnrichedText(this,text,'perkN.description') | Пустые строки также обрабатываются. Нет catch; отказ одного helper прерывает последующие. Не изменяет source и не обогащает общее description |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| CommonItemData | [module/data/item/commonItemData.js](../../../../../../../module/data/item/commonItemData.js) | Import/extends/super | 1,8,10; общие 8 полей и методы calcWeight/canHaveTemporaryItemImprovement/canBeRepaired | Схема проверена; description тут переопределён |
| perk() | [module/data/item/templates/perkData.js](../../../../../../../module/data/item/templates/perkData.js) | Import/SchemaField | 2,15–18; четыре независимые пары полей | Полный разбор фабрики и различие экземпляров |
| socialStanding() | [module/data/item/templates/socialStandingData.js](../../../../../../../module/data/item/templates/socialStandingData.js) | Import/SchemaField | 3,19; таблица регионов | Полная фабрика |
| createEnrichedText | [module/data/dataUtils.js](../../../../../../../module/data/dataUtils.js) | Import/await call | 4,25–28 | Настоящий helper берёт enrichHTML и schema.getField; TextEditor в опыте заменён маркером |
| fields.SchemaField/HTMLField; TypeDataModel/Document lifecycle | Foundry 14.367.0, /opt/foundryvtt/common/data/fields.mjs и common/abstract/type-data.mjs | Внешняя схема/очистка | Определение и создание настоящих моделей | Системный WitcherItem исполнялся поверх common BaseItem, без client Document/БД |
| Item.type=race; htmlFields | [system.json](../../../../../../../system.json) | Декларация типа/HTML | documentTypes.Item.race:178–180 | description/*.description соответствуют HTMLField. Серверная санация не запускалась |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/setup/registerDataModels.js](../../../../../../../module/setup/registerDataModels.js) | RaceData | Import14, map60 | CONFIG.Item.dataModels.race |
| [module/item/sheets/WitcherItemSheet.js](../../../../../../../module/item/sheets/WitcherItemSheet.js) | schema, enrichedText | _prepareContext:48–54 для RaceSheet | Готовит item/config/systemFields/enrichedText/showConfig |
| [module/item/sheets/WitcherRaceSheet.js](../../../../../../../module/item/sheets/WitcherRaceSheet.js) | RaceData через общий контекст | Собственный PARTS.main | Модель напрямую не импортирует |
| [templates/sheets/item/race-sheet.hbs](../../../../../../../templates/sheets/item/race-sheet.hbs) | perk1–4, sourcebook, socialStanding | 15 именованных элементов формы, включая 4 HTML-редактора | Настоящие HBS/formGroup/HTMLField передали верные value/enriched/path |
| [module/actor/sheets/WitcherCharacterSheet.js](../../../../../../../module/actor/sheets/WitcherCharacterSheet.js) | race Item и enrichedText | getList('race')[0], затем system.enrichedText:156,163–165 | Отдельный context.enrichedText.race |
| [templates/partials/character/tab-profession.hbs](../../../../../../../templates/partials/character/tab-profession.hbs) | race.name/perk/socialStanding | Показ и inline-редактирование Item | 263–335; исходный текст передаётся editor, подготовленный enriched не используется |
| [templates/partials/character-header.hbs](../../../../../../../templates/partials/character-header.hbs) | race.name | Заголовок персонажа 6 | Имя Document, а не general.race |

Область поиска: текущие module/ и templates/; регистрации сверены отдельно. Динамические обращения внешних модулей не исследовались.

## Данные и изменения состояния

Модель не создаёт ActiveEffect и не превращает текст особенности в модификатор. Настроенные Item.effects обрабатываются отдельно общими механизмами Actor/ActiveEffect. Схема не содержит операций, условий, ID бонусов или привязки эффекта к конкретному perk.

Общее description существует в модели и манифесте, но не входит в четыре возвращаемые записи и не имеет поля в race-sheet либо общей конфигурации; отсутствие потребителя зафиксировано без вывода о ненужности данных. Семь прочих общих полей наследуются, хотя собственная форма редактирует из них sourcebook.

Race.socialStanding не копируется в Actor.system.general.socialStanding. Последнее выбирается в биографии и читается addSocialStanding при бросках. Изменение региональной строки через Actor-лист адресует race Item, а не значение Actor. Имя расы для показа берётся из Item.name; general.race остаётся отдельной строкой.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Схема/наследование | Настоящие RaceData/WitcherItem с common BaseItem Foundry | 13 полей; description HTMLField против StringField базы; 4 независимых perk; defaults проверены | Клиентский Item и серверная валидация не запускались |
| Обогащение | 4 настоящих await helper, один UUID-текст и 3 пустых | 4 результата с system.perkN.description; source побайтно в JSON не изменён; description не включён | TextEditor возвращает отличимый HTML-маркер, реальные ссылки не разрешались |
| Форма расы | Настоящие HBS/formGroup/HTMLField.toFormGroup/toInput | 15 именованных элементов;4 HTML-входа передали свои value/enriched; север hated и Nilfgaard equal сохранены как selected | HTMLProseMirrorElement и оболочка DOM — фасады |
| Потребитель Actor | Настоящий _prepareCharacterData и фрагмент tab-profession | enrichedText.race приготовлен, но все 4 editor получили raw; исходная @UUID осталась в HTML | Отдельное наблюдение 109; работа/сохранение редактора не проверены |
| Автоматика | Поиск по module/templates; настоящий addSocialStanding и inline-handler | Пять регионов только отображаются/редактируются; формулы читают general.socialStanding | Соответствие чисел рулбуку здесь не проверяется |

## Непроверенные участки и открытые вопросы

Все 31 строки и 4 импорта прочитаны; схема, helper и связи установлены. Foundry 14.367/Node 24.16. UI, TextEditor, запись, инвентарь и операции Actor частично представлены фасадами; реальный мир, ссылки UUID и серверный HTML-фильтр не запускались. Класс WitcherItem в опыте наследует common BaseItem, не клиентский Item. Полный аудит листа Actor/бросков/packsJson остаётся другим порциям.

## Связанные проблемы

[issue-00109](../../../../../../issues/potential/issue-00109.md), [issue-00005](../../../../../../issues/potential/issue-00005.md), [issue-00034](../../../../../../issues/potential/issue-00034.md), [issue-00013](../../../../../../issues/potential/issue-00013.md). 109 — неиспользование enriched у потребителя Actor. 5 сопоставлена: race объявлена корректно и не входит в перечень четырёх пропущенных типов. 34 — прежняя граница смены уникального Item;13 — аналогичный принцип передачи HTML в другом шаблоне, отдельная причина/карточка.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.018 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.

## Уточнение TASK-0003.029

2026-09-11, `273a6d7db0b7c866399db3ecd4f7191817ae6f10`. Полный addSocialStanding подтверждает различие источников: пять региональных полей Race.socialStanding и одно Actor.general.socialStanding. Наличие у Race северного hated не меняет автоматически итог броска Actor с другим общим статусом. Не установлен механизм автоматического выбора региона; никакое правило переноса не вводилось.

Сверенные связи: [module/actor/mixins/skillMixin.js](../../../../../../../module/actor/mixins/skillMixin.js); [module/data/actor/templates/character/generalData.js](../../../../../../../module/data/actor/templates/character/generalData.js). Полные карточки новых файлов — в [указателе порции](../../../README.md#навыки-броски-развитие-и-пользовательские-навыки--task-0003029). [Проверки, ограничения и версия](../../../../review-log.md#task-0003029). Исходники и статус проблем не менялись.

## Уточнение TASK-0003.031

2026-09-11, `928ce4e537c6a3fdc34f8b6fa3fcfdb5a669f68d`. Полный Character._prepareCharacterData выбирает первый нестored race и вызывает настоящий enrichedText для perk1–4. Header выводит имя race, sidebar расы не показывает. Передача обогащённых описаний в tab-profession — отдельный контракт прежней issue-00109; весь этот HBS остаётся TASK-0003.038.

Связи: [module/actor/sheets/WitcherCharacterSheet.js](../../actor/sheets/WitcherCharacterSheet.js.md); [templates/partials/character-header.hbs](../../../templates/partials/character-header.hbs.md). [Методика и ограничения сверки](../../../../review-log.md#task-0003031).

## Дополнительная сверка TASK-0003.038

2026-09-11, `rusbar-main`, `b47ba02cdaebc6a66ad14a5638213b6eb24460b4`; исходники не менялись.

Полный Character tab-profession включает perk1–4 и 5socialStanding select;35 путей с профессией проверены на схемах. Raw editor description остаётся отдельным reader и не использует context.enrichedText.race(109). Actor inline callback пишет в raceItem через.closest.item. Browser-rich-text сохранение не проверено.

[module/actor/mixins/professionMixin.js](../../actor/mixins/professionMixin.js.md), [templates/partials/character/tab-profession.hbs](../../../templates/partials/character/tab-profession.hbs.md), [templates/sheets/actor/partials/monster/tabs/tab-profession.hbs](../../../templates/sheets/actor/partials/monster/tabs/tab-profession.hbs.md), [templates/dialog/combat/profession-attack.hbs](../../../templates/dialog/combat/profession-attack.hbs.md).

[Сверка и ограничения](../../../../review-log.md#task-0003038). Связанные файлы повторно в покрытии не учитывались; код и статусы issues не изменены.
