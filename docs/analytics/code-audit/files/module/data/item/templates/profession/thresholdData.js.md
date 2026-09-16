# module/data/item/templates/profession/thresholdData.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/data/item/templates/profession/thresholdData.js](../../../../../../../../../module/data/item/templates/profession/thresholdData.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `c26eb64dd54cc434087f54c3c6b678b6092b15a2` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.019](../../../../../../../../tasks/task-0003.019.md), одна порция из двенадцати файлов |
| Запись перекрёстной сверки | [TASK-0003.019](../../../../../../review-log.md#task-0003019) |

## Назначение файла

Модель включения порогов профессионального навыка и словаря именованных значений проверки.

## Условия использования

Threshold extends DataModel; professionSkill включает экземпляр через EmbeddedDataField thresholds. Вложенный thresholds.thresholds — намеренные два уровня пути.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| Threshold/fields | Класс 3/alias1 | Два верхних поля | Default export | defineSchema |
| hasThresholds | BooleanField6–9 | Включение ветви/таблицы | initial=false | Не требует непустого словаря |
| thresholds | TypedObjectField10–15 | ID→SchemaField{name,value} | name StringField без своего initial; value Number initial0 | ID создаёт конфигурация через randomID; число без собственного min/max/integer |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| static defineSchema():4–17 | fields | BooleanField и TypedObjectField | Задаёт поля name/value записей | Синхронно; не сортирует и не выбирает порог, не выполняет бросок |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| DataModel/BooleanField/TypedObjectField/SchemaField/StringField/NumberField | Foundry 14.367.0: /opt/foundryvtt/common/data/fields.mjs; common/abstract/data.mjs; common/abstract/type-data.mjs | Наследование/схема | 3–14 | Реальные поля и пустой словарь |
| hasThresholds label | [lang/en.json](../../../../../../../../../lang/en.json); [lang/ru.json](../../../../../../../../../lang/ru.json) | Локализация | 8 | В en есть, в ru нет |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/data/item/templates/professionSkillData.js](../../../../../../../../../module/data/item/templates/professionSkillData.js) | Threshold | EmbeddedDataField19 | Импорт 4 |
| [module/item/sheets/configurations/WitcherProfessionConfigurationSheet.js](../../../../../../../../../module/item/sheets/configurations/WitcherProfessionConfigurationSheet.js) | thresholds.thresholds.<id> | 6 методов поиска/CRUD | randomID/add/edit/-=; payload проверены |
| [templates/sheets/item/configuration/partials/profession/skillPathSkillPart.hbs](../../../../../../../../../templates/sheets/item/configuration/partials/profession/skillPathSkillPart.hbs) | hasThresholds/name/value | Форма/таблица | 91–119; rows data-id |
| [module/actor/mixins/professionMixin.js](../../../../../../../../../module/actor/mixins/professionMixin.js) | Словарь порогов | doProfessionThreshold:323–348 | Один без выбора, несколько через prompt; пустой не защищён |

Область поиска: текущие module/ и templates/; регистрации сверены отдельно. Динамические обращения внешних модулей не исследовались.

## Данные и изменения состояния

Ветка порогов выбирается после attack и custom usage. Один порог выбирается по Object.entries[0], для нескольких открывается select; значение/name передаются doProfessionSkillRoll как threshold/thresholdDesc. Сортировки/автоматического выбора по результату нет. Пустой словарь допустим даже с hasThresholds=true; await обновления обработчиками не обеспечен.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Пустой/один/два | Настоящий doProfessionThreshold | Пустой select→TypeError после пустого выбора; Easy5 без окна; b→B8 | Dialog-фасад |
| CRUD | Настоящие методы конфигурации | add{value:0}, edit.value='9', delete -=th; Pending update не ожидается | Запись перехвачена |
| Локализация | 157 ключей en/ru | Три подписи thresholds отсутствуют в ru, есть в en | I18n fallback клиента не запускался |

## Непроверенные участки и открытые вопросы

В TASK-0004.008 текущий файл и его связи сопоставлены с датированными протоколами TASK-0003.018/.019 (2026-09-10) и .038 (2026-09-11), в пределах относящихся к нему сценариев. Новых поведенческих запусков нет; прежние настоящие модели/методы и фасады различены в протоколе. Браузерный submit, мир, сеть и запись в БД не проверены. Установлены процессы R008-06, R008-11, R008-20; оставшиеся границы: [U008-01](../../../../../../cross-check-0002.md#u008-01), [U008-06](../../../../../../cross-check-0002.md#u008-06). Полный пофайловый разбор соседей в TASK-0003 не равен проверке клиентского lifecycle.

## Связанные проблемы

[issue-00110](../../../../../../../../issues/potential/issue-00110.md), [issue-00115](../../../../../../../../issues/potential/issue-00115.md), [issue-00119](../../../../../../../../issues/closed/issue-00119.md), [issue-00120](../../../../../../../../issues/potential/issue-00120.md). Проблемы находятся у потребителей и в локализации, не означают необходимость изменения структуры словаря.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.019 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.

## Дополнительная сверка TASK-0003.038

2026-09-11, `rusbar-main`, `b47ba02cdaebc6a66ad14a5638213b6eb24460b4`; исходники не менялись.

Одна запись выбирается безокна; несколько через select id=threshold и form.elements.threshold; пустой словарь открывает пустой select и падает(115). Значение 0 передаётся корректно. doProfessionThreshold не возвращает Promise броска(241); strict threshold semantics задаёт extendedRoll. EN fallback для трёх отсутствующих RU ключей проверен(119).

[module/actor/mixins/professionMixin.js](../../../../actor/mixins/professionMixin.js.md), [templates/partials/character/tab-profession.hbs](../../../../../templates/partials/character/tab-profession.hbs.md), [templates/sheets/actor/partials/monster/tabs/tab-profession.hbs](../../../../../templates/sheets/actor/partials/monster/tabs/tab-profession.hbs.md), [templates/dialog/combat/profession-attack.hbs](../../../../../templates/dialog/combat/profession-attack.hbs.md).

[Сверка и ограничения](../../../../../../review-log.md#task-0003038). Связанные файлы повторно в покрытии не учитывались; код и статусы issues не изменены.

## Сквозная сверка TASK-0004.008

2026-09-14; rusbar-main, f96434101e0e827838c2e6a3e09da8933a9801ef. Исходник совпадает со срезом TASK-0001; изменено только описание.

hasThresholds и словарь порогов описывают данные, которые UI заполняет по ID. Runtime автоматически выбирает единственный элемент, открывает выбор при нуле/нескольких; пустой результат не проверяет. Label hasThresholds модели и два заголовка name/thresholdValue шаблона отсутствуют в ru; это отделено от ошибки пустого выбора.

Сопоставленные определения и потребители: [lang/en.json](../../../../../lang/en.json.md), [lang/ru.json](../../../../../lang/ru.json.md), [module/data/item/templates/professionSkillData.js](../professionSkillData.js.md), [module/item/sheets/configurations/WitcherProfessionConfigurationSheet.js](../../../../item/sheets/configurations/WitcherProfessionConfigurationSheet.js.md), [templates/sheets/item/configuration/partials/profession/skillPathSkillPart.hbs](../../../../../templates/sheets/item/configuration/partials/profession/skillPathSkillPart.hbs.md), [module/actor/mixins/professionMixin.js](../../../../actor/mixins/professionMixin.js.md).

[Протокол и границы](../../../../../../review-log.md#task-0004008) — TASK-0004.008; процессы [R008-06](../../../../../../cross-check-0002.md#r008-06), [R008-11](../../../../../../cross-check-0002.md#r008-11), [R008-20](../../../../../../cross-check-0002.md#r008-20). В этой порции выполнена статическая сверка; прежние опыты сохраняют свои даты и фасады. Новых поведенческих запусков нет; браузер, мир, сеть и запись в БД не запускались.
