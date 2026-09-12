# lang/ru.json

| Поле | Значение |
| --- | --- |
| Исходный файл | [lang/ru.json](../../../../../lang/ru.json) |
| Тип файла | JSON, русский словарь локализации |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-12 |
| Ветка и коммит | rusbar-main, 4b9951094106e26d9274bbd5d5e8e7a709cfcf24 |
| Изменения относительно коммита | Нет; совпадает со срезом TASK-0001 15da5b225535e34af4e132c701b5353ef4eb667f |
| Задача и порция | [TASK-0003.051](../../../../tasks/task-0003.051.md), 2 файла / 3032 логические строки; данный файл — 1503 |
| Запись перекрёстной сверки | [TASK-0003.051](../../review-log.md#task-0003051) |

## Назначение файла

Русские подписи интерфейса системы: 1135 строковых листьев (26 TYPES, 1 EFFECT, 1108 WITCHER). При отсутствии собственного ключа Foundry обращается к en; локализация не меняет расчёты и не регистрирует новые типы документов.

## Условия использования

Манифест [system.json](../../../../../system.json) регистрирует восемь языков, включая lang=en → lang/en.json и lang=ru → lang/ru.json. В TASK-0003.051 исследуются только эти два словаря; изменение границ аудита не меняет список языков системы.

Установленный Foundry 14.367.0 загружает переводы в Localization.setLanguage: сначала ядро для поддерживаемого им языка, затем выбранный язык системы, активные модули и мир. #loadTranslationFile после JSON.parse/resp.json вызывает foundry.utils.expandObject; #getTranslations объединяет словари через mergeObject в порядке пакетов. Для ru отдельно загружается английский словарь fallback. Пути пакетов к этому моменту подготавливает Foundry; сам JSON не делает import или fetch.

Localization.localize/format сначала ищет строку в translations, затем в _fallback; если строки нет в обоих, возвращает исходный ключ. Проверка регистрозависима, пробелы не обрезаются, соседние пространства имён не являются псевдонимами. Пустая строка является найденным переводом. Внешний модуль/мир может переопределить результат; доступ реального сервера по HTTP здесь не проверялся.

## Введённые сущности и действия с ними

Это словарь данных, без классов, функций, обработчиков, формул и изменяемых игровых документов. Корни TYPES, EFFECT и WITCHER содержат только объекты и строковые листья. Структура и полный перечень ключей приведены ниже; обозначения после второго сегмента не образуют дополнительные корневые namespaces.

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| TYPES.Item.*, TYPES.Actor.*, TYPES.ActiveEffect.* | 26 строк: 21 / 4 / 1 | Человекочитаемые имена типов документов | Localization.initialize и системные/ядровые формы | Чтение по типу; наличие перевода не регистрирует сам тип |
| EFFECT.TABS.systemSpecific | Строка | Заголовок системной вкладки эффекта | [module/activeEffect/WitcherActiveEffectSheet.js](../../../../../module/activeEffect/WitcherActiveEffectSheet.js) | id=systemSpecific и наследуемый labelPrefix=EFFECT.TABS в ядре |
| WITCHER.* | Основной словарь | Подписи полей, кнопки, диалоги, чат, статусы, списки выбора | Прямые вызовы i18n, метаданные моделей, config, контекст шаблонов | Получение строк при подготовке контекста/формы/сообщения |
| WITCHER.currencyConverter.errors.insufficient | Строка с {currency} | Название валюты в предупреждении | [module/actor/mixins/currencyConverterMixin.js](../../../../../module/actor/mixins/currencyConverterMixin.js), openCurrencyConverter | Вложенная локализация валюты, затем format |
| WITCHER.Combat.healed | Строка с {target}, {heal} | Цель и количество лечения в сообщении | [module/scripts/chat.js](../../../../../module/scripts/chat.js), onHeal | Подстановка после вычисления фактического лечения |
| 63 dotted-ключа в каждом исходнике | Ключи вида Actor["Skill.Intelligence"], "Items.transferTitle" | Совместная запись с обычными вложенными объектами | expandObject при загрузке | Разворачивание в пути; все листья сохраняются |

В TYPES представлены также mystery/clue/obstacle/skill, которых нет в documentTypes манифеста, хотя модели регистрируются в [module/setup/registerDataModels.js](../../../../../module/setup/registerDataModels.js). Это прежнее рассогласование регистрации ([docs/issues/potential/issue-00005.md](../../../../issues/potential/issue-00005.md)), а не отсутствие переводов. В манифесте есть 22 соответствующих типа Actor/Item/ActiveEffect; все 22 имеют подписи en/ru. Три типа ChatMessage не имеют собственных TYPES.ChatMessage.*; при штатной инициализации ядро предусматривает общий label документа. Одного этого факта недостаточно для нового issue.

## Основные функции и методы

Собственных функций нет. Ниже перечислены операции потребителей, а не методы JSON.

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| Localization.setLanguage / #getTranslations / #loadTranslationFile | Язык, пакеты и пути | translations и английский _fallback | Загрузка, expandObject, mergeObject | Async; ошибка загрузки/парсинга даёт пустой словарь и сообщение ядра; работа сети не воспроизводилась |
| Localization.localize / format | Ключ; необязательные данные | Перевод или исходный ключ | Поиск строки и replace для {…} | Нет записи документов; отсутствующая подстановка при переданном объекте становится "undefined" |
| Handlebars localize | Ключ, options.hash | Строка для шаблона | SafeString-ключ превращается в string, непустой hash передаётся _loc | Обычный {{…}} экранирует HTML; сами переводы HTML-тегов не содержат |
| Метаданные DataField и formGroup / selectOptions | label/hint/choices + localize=true | Представление полей и вариантов | Локализация ключей, указанных моделями/config | Наличие label не означает отдельный вызов JSON; данные модели и перевод различаются |
| Localization.localizeDataModel / localizeSchema | LOCALIZATION_PREFIXES, FIELDS | Автоподписи схем | Ядровой механизм обхода схем | В module нет собственных LOCALIZATION_PREFIXES, в этих словарях нет FIELDS; системные поля задают явные label/hint |

## Используемые сущности и зависимости

JSON не вызывает код и не импортирует другой словарь. Здесь показаны зависимости механизма загрузки и интерпретации; направления вызова принадлежат Foundry и потребителям.

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| languages[].lang/path | [system.json](../../../../../system.json) | Регистрация ресурса | Выбор файла для языка | Манифест и настоящий setLanguage с подменой fetch |
| Localization, expandObject, mergeObject, getProperty | Foundry 14.367.0: client/helpers/localization.mjs, common/utils/helpers.mjs | Загрузка и интерпретация данных | Нормализация dotted-ключей, объединение и fallback | Исполнены реальные методы установленного ядра |
| Английский fallback / русский словарь | [lang/en.json](../../../../../lang/en.json), [lang/ru.json](../../../../../lang/ru.json) | Связь через ядро, без import | Второй поиск при отсутствии ru-строки | Все 20 расхождений проверены через настоящий localize/has |
| _loc, Handlebars localize | Foundry client/applications/handlebars.mjs; Handlebars 4.7.9 | Вызов внешнего helper | Отображение переводов, подстановка hash | Исполнен исходный helper, разобраны AST всех 132 HBS |
| formGroup, selectOptions, DataField.label/hint | Foundry и [module/data/item/templates/combat/attackOptionsData.js](../../../../../module/data/item/templates/combat/attackOptionsData.js), [module/data/activeEffects/witcherActiveEffectData.js](../../../../../module/data/activeEffects/witcherActiveEffectData.js) | Чтение метаданных | Настраиваемые формы | Реальные схемы полей и места localize=true; полный DOM формы не запускался |
| statMap, skillMap, damageTypes, currency, statusEffects | [module/setup/config.js](../../../../../module/setup/config.js) | Косвенные ссылки из справочника | Варианты выбора, имена бросков, валют и статусов | Точные ключи и исходный мастер эффектов |

## Известные потребители

Область поиска — все 214 JS module и 132 HBS templates, манифест и уже существующие карточки. В полном инвентаре ниже отражены точные строковые упоминания ключей с файлами и строками; это не счётчик выполненных вызовов. Литерал может быть label модели или записью config, которая локализуется позже.

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/setup/config.js](../../../../../module/setup/config.js) | statMap/skillMap, damageTypes, currency, statusEffects и другие ключи | Хранение ключей для будущего выбора и вызова i18n | Полный поиск точных литералов; первичная карточка config |
| [module/activeEffect/mixins/baseMixin.js](../../../../../module/activeEffect/mixins/baseMixin.js) | WITCHER.Stats.*, Actor.Lifepath.*, DamageType.*, skillMap.label | Составление подсказок мастера из полей Actor/config | Выполнен getActiveEffectsBasePaths на настоящем config и семи полях схемы damageTypeModification |
| [module/activeEffect/WitcherActiveEffectSheet.js](../../../../../module/activeEffect/WitcherActiveEffectSheet.js) | this.label, EFFECT.TABS.systemSpecific | Редактор локализует метаданные и заголовок вкладки | Исходный prepare-context и определение вкладки |
| [module/actor/mixins/skillMixin.js](../../../../../module/actor/mixins/skillMixin.js), [module/actor/sheets/mixins/statMixin.js](../../../../../module/actor/sheets/mixins/statMixin.js) | skillMap.label/rollLabel, stat.label, Dialog.savingThrow | Имена бросков и заголовок модификатора | Код и существующие карточки; несовпадения отражены в issues |
| [module/actor/mixins/currencyConverterMixin.js](../../../../../module/actor/mixins/currencyConverterMixin.js), [module/scripts/chat.js](../../../../../module/scripts/chat.js) | Две строки с подстановками | Предупреждение конвертера и onHeal | Исходные обработчики исполнены, диалог/запись/чат перехвачены |
| [module/item/mixins/damageUtilMixin.js](../../../../../module/item/mixins/damageUtilMixin.js), [module/actor/mixins/weaponAttackMixin.js](../../../../../module/actor/mixins/weaponAttackMixin.js), [module/actor/mixins/defenseMixin.js](../../../../../module/actor/mixins/defenseMixin.js) | DamageType.<type>, label атак/защит/навыков | Представление бросков и сообщений | Динамический ключ и ссылки на config; все ветви боя повторно не запускались |
| [module/actor/mixins/castSpellMixin.js](../../../../../module/actor/mixins/castSpellMixin.js), [templates/sheets/actor/partials/character/spell-type-list.hbs](../../../../../templates/sheets/actor/partials/character/spell-type-list.hbs) | WITCHER.Spell.<значение> | Тип/уровень/источник заклинания | Исходное построение ключей; Water ≠ water |
| [templates/partials/character/tab-skills.hbs](../../../../../templates/partials/character/tab-skills.hbs), [module/data/item/professionData.js](../../../../../module/data/item/professionData.js) | WITCHER.St<Stat>, Actor.Stat.<Stat> | Составление имени характеристики | concat и динамический регистр; префикс сам по себе не является пропущенным переводом |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-diagrams.hbs](../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-diagrams.hbs) | TYPES.Item.<system.type>, WITCHER.Inventory.<type> | Название подтипа рецепта | Не все значения данных являются типами Item; issue-00178 |
| [templates/partials/character-header.hbs](../../../../../templates/partials/character-header.hbs), [templates/sheets/actor/partials/monster/header.hbs](../../../../../templates/sheets/actor/partials/monster/header.hbs) | Homelands.*, socialStanding.*, Monster.Type.* | Вариант по данным Actor | Динамические concat, не отдельные JS-импорты |
| [templates/sheets/item/configuration/tabs/general.hbs](../../../../../templates/sheets/item/configuration/tabs/general.hbs), [templates/sheets/item/configuration/tabs/spellGeneral.hbs](../../../../../templates/sheets/item/configuration/tabs/spellGeneral.hbs) | WITCHER.DamageType.* через config.damageTypes | formGroup options и localize=true; context.config из WitcherConfigurationSheet | Код контекста, формы и значения справочника |
| [templates/partials/effect-part.hbs](../../../../../templates/partials/effect-part.hbs) | EFFECT.TABS.duration и DOCUMENT.* | Переводы ядра, четыре hash-подстановки type | Эти строки не обязаны определяться системой; duration найден в настоящем en ядра |

Найдено 1094 AST-обращения к helper localize: 1013 с буквальным первым аргументом и 81 с выражением/переменной. Четыре обращения с hash относятся к DOCUMENT.* ядра. Это не включает локализацию внутри formGroup/selectOptions и не доказывает, что каждый шаблон достижим в текущем UI.

Пользовательские name/label, сохранённые строки документов, lookup/concat, формируемые пути и метаданные полей могут обращаться к ключам без буквального упоминания полного пути. Поэтому отсутствие строки в индексе потребителей не означает, что перевод не нужен. 120 отсутствующих ключей старого справочника WITCHER.Crit принадлежат 24 записям config; прямого читателя config.Crit в module/templates не найдено. Текущее применение травм читает выбранный компедиум; нового issue только по этим 120 ключам не создано.

## Данные и изменения состояния

При загрузке изменяются словари локализатора в памяти; вычисления характеристик, эффектов и правил не происходят в JSON. Переведённая строка может попасть в заголовок, HTML или формулу-аннотацию у потребителя и затем сохраниться в сообщении/журнале; перезагрузка языка не переписывает уже сохранённый текст. Точные последствия задаёт вызывающий код.

В каждом словаре четыре пустые строки hint относятся к вариантам attackSkill. Это допустимые пустые подсказки, не отсутствие ключа. Только две строки содержат фигурные подстановки; наборы имён совпадают между en/ru. HTML-тегов, массивов, чисел, bool, null, повторяющихся JSON-ключей и потерь листьев при нормализации не обнаружено. Символы сравнения, пунктуация и игровой текст не превращают строку в программную операцию.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Полная структура | Python json.loads(object_pairs_hook), обход всех листьев; настоящий expandObject/mergeObject | 1153 en / 1135 ru; 1133 общих, 20 только en, 2 только ru; ключи не потеряны | Лингвистическая редактура и сверка с книгами не выполнялись |
| Загрузка и fallback | Настоящий Localization.setLanguage, fetch возвращает локальные данные в памяти | ru выбран, en загружен; модуль/мир переопределяют систему в штатном порядке | Настройки реального мира, HTTP и внешние пакеты не исследовались |
| Все строковые листья | localize/has на настоящих словарях | Каждая собственная строка и все 20 fallback совпали с ожидаемым значением | Проверено в изоляции от дополнительных переводов |
| Подстановки | Реальные onHeal/openCurrencyConverter и ядровой HBS helper | heal/target/currency переданы; в этих сценариях "undefined" не появляется; HBS экранирует тестовый текст | Запись документов, UI и ChatMessage подменены |
| Ключи потребителей | Точные литералы 346 JS/HBS; AST 132 HBS; выборочная трассировка динамики | Индекс, прежние issues и два новых пропуска ru | Это не AST JavaScript и не полный запуск всех динамических путей |
| Повторная сверка | [docs/analytics/code-audit/review-log.md](../../review-log.md#task-0003051) | 17 групп изолированных проверок, сопоставление с прежними карточками | TASK-0004/TASK-0005 этим не выполнены |

## Непроверенные участки и открытые вопросы

Не проверялись смысловая точность перевода игровых правил, терминологическое единообразие, другие шесть языков, контент компедиумов, реальный браузер/мир, сетевой доступ к ресурсам, активные модули переводов и все возможные сохранённые/пользовательские ключи. Три en-only ключа без найденного потребителя и два ru-only ключа сохранены как наблюдение состава; удалять их на основании поиска нельзя.

## Связанные проблемы

Повторно сопоставлены с текущими en/ru: [docs/issues/potential/issue-00014.md](../../../../issues/potential/issue-00014.md), [docs/issues/potential/issue-00016.md](../../../../issues/potential/issue-00016.md), [docs/issues/potential/issue-00090.md](../../../../issues/potential/issue-00090.md), [docs/issues/potential/issue-00098.md](../../../../issues/potential/issue-00098.md), [docs/issues/potential/issue-00119.md](../../../../issues/potential/issue-00119.md), [docs/issues/potential/issue-00137.md](../../../../issues/potential/issue-00137.md), [docs/issues/potential/issue-00178.md](../../../../issues/potential/issue-00178.md), [docs/issues/potential/issue-00186.md](../../../../issues/potential/issue-00186.md), [docs/issues/potential/issue-00193.md](../../../../issues/potential/issue-00193.md), [docs/issues/potential/issue-00205.md](../../../../issues/potential/issue-00205.md), [docs/issues/potential/issue-00234.md](../../../../issues/potential/issue-00234.md), [docs/issues/potential/issue-00296.md](../../../../issues/potential/issue-00296.md). Ошибки ключа и отсутствие русского перевода различаются.

Новые наблюдения: [docs/issues/potential/issue-00317.md](../../../../issues/potential/issue-00317.md) — русское название silver записано по другому пути; [docs/issues/potential/issue-00318.md](../../../../issues/potential/issue-00318.md) — нет русского перевода applyAfterCalculations. Статусы potential; переводы, код и решения по исправлению не менялись.

## Состав русского словаря

Полный набор ru — 1133 общих ключа из [инвентаря en](en.json.md#полный-инвентарь-строковых-ключей), без перечисленных ниже 20 en-only ключей, плюс два ru-only ключа. Это точное описание всего набора, без предположения, что словари совпадают. Индекс en содержит места употребления общих ключей и русских пропусков; для 981 из 1135 собственных ru-ключей найдено точное строковое упоминание в module/templates.

| Группа / ключ второго уровня | Строк en | Строк ru |
| --- | --- | --- |
| TYPES.Item | 21 | 21 |
| TYPES.Actor | 4 | 4 |
| TYPES.ActiveEffect | 1 | 1 |
| EFFECT.TABS | 1 | 1 |
| WITCHER.Name | 1 | 1 |
| WITCHER.Type | 1 | 1 |
| WITCHER.Percentage | 1 | 1 |
| WITCHER.NoEffects | 1 | 1 |
| WITCHER.DC | 1 | 1 |
| WITCHER.Attack | 15 | 15 |
| WITCHER.Defense | 11 | 11 |
| WITCHER.Actor | 91 | 86 |
| WITCHER.Alchemy | 6 | 6 |
| WITCHER.Armor | 31 | 27 |
| WITCHER.Item | 89 | 89 |
| WITCHER.Damage | 24 | 25 |
| WITCHER.Dialog | 76 | 75 |
| WITCHER.DamageType | 9 | 8 |
| WITCHER.profession | 17 | 14 |
| WITCHER.Weapon | 42 | 42 |
| WITCHER.Location | 10 | 10 |
| WITCHER.Component | 4 | 4 |
| WITCHER.criticalWound | 17 | 17 |
| WITCHER.Enhancement | 10 | 10 |
| WITCHER.Diagram | 24 | 24 |
| WITCHER.Valuable | 12 | 12 |
| WITCHER.StInt | 1 | 1 |
| WITCHER.StRef | 1 | 1 |
| WITCHER.StDex | 1 | 1 |
| WITCHER.StBody | 1 | 1 |
| WITCHER.StEmp | 1 | 1 |
| WITCHER.StCra | 1 | 1 |
| WITCHER.StWill | 1 | 1 |
| WITCHER.StLuck | 1 | 1 |
| WITCHER.StSpd | 1 | 1 |
| WITCHER.StVigor | 1 | 1 |
| WITCHER.StReputation | 1 | 1 |
| WITCHER.CritWound | 9 | 9 |
| WITCHER.Homeland | 1 | 1 |
| WITCHER.Homelands | 25 | 25 |
| WITCHER.MinValue | 1 | 1 |
| WITCHER.MaxValue | 1 | 1 |
| WITCHER.Value | 1 | 1 |
| WITCHER.ValuedPerson | 1 | 1 |
| WITCHER.Affectations | 1 | 1 |
| WITCHER.Hair | 1 | 1 |
| WITCHER.Personality | 1 | 1 |
| WITCHER.Clothing | 1 | 1 |
| WITCHER.FeelingsOnPeople | 1 | 1 |
| WITCHER.LifeEvents | 1 | 1 |
| WITCHER.Decade | 1 | 1 |
| WITCHER.Event | 1 | 1 |
| WITCHER.DeathSave | 1 | 1 |
| WITCHER.BeforeCrit | 1 | 1 |
| WITCHER.Crit | 1 | 1 |
| WITCHER.Fumble | 1 | 1 |
| WITCHER.CritTotal | 1 | 1 |
| WITCHER.table | 10 | 10 |
| WITCHER.Monster | 56 | 56 |
| WITCHER.Mount | 6 | 6 |
| WITCHER.Mutagen | 8 | 8 |
| WITCHER.Loot | 18 | 18 |
| WITCHER.Inventory | 44 | 44 |
| WITCHER.Button | 4 | 4 |
| WITCHER.Spell | 65 | 64 |
| WITCHER.Chat | 8 | 8 |
| WITCHER.Currency | 7 | 7 |
| WITCHER.currencyConverter | 9 | 9 |
| WITCHER.Settings | 17 | 17 |
| WITCHER.background | 1 | 1 |
| WITCHER.Resources | 1 | 1 |
| WITCHER.Notes | 1 | 1 |
| WITCHER.skills | 76 | 75 |
| WITCHER.Stats | 2 | 2 |
| WITCHER.SocialStanding | 1 | 1 |
| WITCHER.Profession | 1 | 1 |
| WITCHER.Reputation | 1 | 1 |
| WITCHER.NoDamageSpecified | 1 | 1 |
| WITCHER.Shield | 1 | 1 |
| WITCHER.Items | 2 | 2 |
| WITCHER.Combat | 3 | 3 |
| WITCHER.Context | 11 | 11 |
| WITCHER.Heal | 14 | 14 |
| WITCHER.Apply | 1 | 1 |
| WITCHER.ReputationTitle | 1 | 1 |
| WITCHER.ReputationButton | 2 | 2 |
| WITCHER.ReputationSave | 1 | 1 |
| WITCHER.ReputationFaceDown | 1 | 1 |
| WITCHER.verbalCombat | 38 | 38 |
| WITCHER.Effect | 16 | 15 |
| WITCHER.activeEffect | 7 | 7 |
| WITCHER.character | 1 | 1 |
| WITCHER.socialStanding | 11 | 11 |
| WITCHER.craft | 7 | 7 |
| WITCHER.err | 3 | 3 |
| WITCHER.Investigation | 12 | 12 |
| WITCHER.statusEffects | 27 | 27 |
| WITCHER.armorEffects | 3 | 3 |
| WITCHER.fumbleResults | 23 | 23 |
| WITCHER.deprecations | 8 | 6 |
| WITCHER.AssociatedDiagram | 4 | 4 |
| WITCHER.Repair | 20 | 20 |
| WITCHER.ComponentsList | 5 | 5 |
| WITCHER.rewards | 10 | 10 |
| WITCHER.magic | 1 | 1 |

### Ключи, для которых используется английский fallback

| Ключ только en | Английская строка | Потребитель / наблюдение |
| --- | --- | --- |
| WITCHER.Actor.deathState.ignore | DS | [issue-00205](../../../../issues/potential/issue-00205.md); [templates/sheets/actor/partials/character/sidebar.hbs:120](../../../../../templates/sheets/actor/partials/character/sidebar.hbs); [templates/sheets/actor/partials/monster/sidebar.hbs:143](../../../../../templates/sheets/actor/partials/monster/sidebar.hbs) |
| WITCHER.Actor.deathState.ignoreHint | Ignore Death State penalties when HP is 0 or below. | [issue-00205](../../../../issues/potential/issue-00205.md); [templates/sheets/actor/partials/character/sidebar.hbs:123](../../../../../templates/sheets/actor/partials/character/sidebar.hbs); [templates/sheets/actor/partials/monster/sidebar.hbs:146](../../../../../templates/sheets/actor/partials/monster/sidebar.hbs) |
| WITCHER.Actor.woundThreshold.ignore | WT | [issue-00205](../../../../issues/potential/issue-00205.md); [templates/sheets/actor/partials/character/sidebar.hbs:107](../../../../../templates/sheets/actor/partials/character/sidebar.hbs); [templates/sheets/actor/partials/monster/sidebar.hbs:130](../../../../../templates/sheets/actor/partials/monster/sidebar.hbs) |
| WITCHER.Actor.woundThreshold.ignoreHint | Ignore Wound Threshold penalties when HP is below WT. | [issue-00205](../../../../issues/potential/issue-00205.md); [templates/sheets/actor/partials/character/sidebar.hbs:110](../../../../../templates/sheets/actor/partials/character/sidebar.hbs); [templates/sheets/actor/partials/monster/sidebar.hbs:133](../../../../../templates/sheets/actor/partials/monster/sidebar.hbs) |
| WITCHER.Actor.woundThreshold.state | Wound State | Потребитель не найден; новый issue не создан |
| WITCHER.Armor.locationLeftArm | Left Arm | [issue-00090](../../../../issues/potential/issue-00090.md); [templates/sheets/item/configuration/tabs/armorGeneral.hbs:9](../../../../../templates/sheets/item/configuration/tabs/armorGeneral.hbs); [templates/sheets/item/configuration/tabs/armorGeneral.hbs:10](../../../../../templates/sheets/item/configuration/tabs/armorGeneral.hbs) |
| WITCHER.Armor.locationLeftLeg | Left Leg | [issue-00090](../../../../issues/potential/issue-00090.md); [templates/sheets/item/configuration/tabs/armorGeneral.hbs:15](../../../../../templates/sheets/item/configuration/tabs/armorGeneral.hbs); [templates/sheets/item/configuration/tabs/armorGeneral.hbs:16](../../../../../templates/sheets/item/configuration/tabs/armorGeneral.hbs) |
| WITCHER.Armor.locationRightArm | Right Arm | [issue-00090](../../../../issues/potential/issue-00090.md); [templates/sheets/item/configuration/tabs/armorGeneral.hbs:12](../../../../../templates/sheets/item/configuration/tabs/armorGeneral.hbs); [templates/sheets/item/configuration/tabs/armorGeneral.hbs:13](../../../../../templates/sheets/item/configuration/tabs/armorGeneral.hbs) |
| WITCHER.Armor.locationRightLeg | Right Leg | [issue-00090](../../../../issues/potential/issue-00090.md); [templates/sheets/item/configuration/tabs/armorGeneral.hbs:18](../../../../../templates/sheets/item/configuration/tabs/armorGeneral.hbs); [templates/sheets/item/configuration/tabs/armorGeneral.hbs:19](../../../../../templates/sheets/item/configuration/tabs/armorGeneral.hbs) |
| WITCHER.DamageType.silver | Silver | [issue-00317](../../../../issues/potential/issue-00317.md); [module/actor/mixins/damageMixin.js:172](../../../../../module/actor/mixins/damageMixin.js); [module/setup/config.js:752](../../../../../module/setup/config.js) |
| WITCHER.Dialog.customModifier | Custom Modifiers | [issue-00186](../../../../issues/potential/issue-00186.md); [module/actor/mixins/weaponAttackMixin.js:253](../../../../../module/actor/mixins/weaponAttackMixin.js); [module/scripts/helper.js:94](../../../../../module/scripts/helper.js); [templates/dialog/combat/profession-attack.hbs:83](../../../../../templates/dialog/combat/profession-attack.hbs); [templates/dialog/combat/spell-attack.hbs:34](../../../../../templates/dialog/combat/spell-attack.hbs); [templates/dialog/combat/weapon-attack.hbs:209](../../../../../templates/dialog/combat/weapon-attack.hbs); [templates/dialog/verbal-combat-defense.hbs:11](../../../../../templates/dialog/verbal-combat-defense.hbs); [templates/dialog/verbal-combat.hbs:13](../../../../../templates/dialog/verbal-combat.hbs) |
| WITCHER.Dialog.savingThrow | Performing a saving throw | [issue-00193](../../../../issues/potential/issue-00193.md); [module/actor/sheets/mixins/statMixin.js:25](../../../../../module/actor/sheets/mixins/statMixin.js) |
| WITCHER.Effect.applyAfterCalculations | Apply this active effect after all derived stats were calculated | [issue-00318](../../../../issues/potential/issue-00318.md); [module/data/activeEffects/witcherActiveEffectData.js:25](../../../../../module/data/activeEffects/witcherActiveEffectData.js) |
| WITCHER.Spell.emanation | Emanation | [issue-00137](../../../../issues/potential/issue-00137.md); [module/item/sheets/WitcherRitualSheet.js:32](../../../../../module/item/sheets/WitcherRitualSheet.js); [module/item/sheets/WitcherSpellSheet.js:61](../../../../../module/item/sheets/WitcherSpellSheet.js) |
| WITCHER.deprecations.armorEnhancements.text | Armor Enhancements are being reworked. To prevent data loss you need to unattach your enhancements from armors and shields before updating to the next version. Some armors might already be broken, it is best to redo them in the next version. | Потребитель не найден; новый issue не создан |
| WITCHER.deprecations.armorEnhancements.title | Armor Enhancements Rework | Потребитель не найден; новый issue не создан |
| WITCHER.profession.skillPath.skill.thresholds.hasThresholds | Has thresholds | [issue-00119](../../../../issues/potential/issue-00119.md); [module/data/item/templates/profession/thresholdData.js:8](../../../../../module/data/item/templates/profession/thresholdData.js) |
| WITCHER.profession.skillPath.skill.thresholds.name | Name | [issue-00119](../../../../issues/potential/issue-00119.md); [templates/sheets/item/configuration/partials/profession/skillPathSkillPart.hbs:98](../../../../../templates/sheets/item/configuration/partials/profession/skillPathSkillPart.hbs) |
| WITCHER.profession.skillPath.skill.thresholds.thresholdValue | Threshold | [issue-00119](../../../../issues/potential/issue-00119.md); [templates/sheets/item/configuration/partials/profession/skillPathSkillPart.hbs:99](../../../../../templates/sheets/item/configuration/partials/profession/skillPathSkillPart.hbs) |
| WITCHER.skills.levelUp | Level up | [issue-00193](../../../../issues/potential/issue-00193.md); [templates/sheets/actor/configuration/app/edit-skills.hbs:10](../../../../../templates/sheets/actor/configuration/app/edit-skills.hbs) |

### Ключи только русского словаря

| Ключ | Значение | Найденный потребитель |
| --- | --- | --- |
| WITCHER.Damage.silver | Серебро | Точного употребления в module/templates нет. Это не alias для используемого WITCHER.DamageType.silver; issue-00317 |
| WITCHER.Dialog.attackCustom | Модификатор атаки | Точного употребления в module/templates нет; используемый customModifier отличается, issue-00186 |

Отсутствие найденного потребителя не является основанием удалять ключ или объявлять его ошибочным: возможны внешние/сохранённые данные. Никакие значения словаря в ходе аудита не исправлены.

## История актуализации

| Дата | Версия и область | Результат |
| --- | --- | --- |
| 2026-09-12 | 4b9951094106e26d9274bbd5d5e8e7a709cfcf24; полный файл | Первичная карточка; [перекрёстная сверка](../../review-log.md#task-0003051) |
