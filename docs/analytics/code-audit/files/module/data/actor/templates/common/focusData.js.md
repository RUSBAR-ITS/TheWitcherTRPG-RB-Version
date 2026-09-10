# module/data/actor/templates/common/focusData.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/data/actor/templates/common/focusData.js](../../../../../../../../../module/data/actor/templates/common/focusData.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `c34b790379fd98cd7e33ccbeeca085e49297a40f` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.003](../../../../../../../../tasks/task-0003.003.md), одна порция из восьми файлов |
| Запись перекрёстной сверки | [TASK-0003.003](../../../../../../review-log.md#task-0003003) |

## Назначение файла

Фабрика пары name/value для одного из четырёх слотов фокусировки Actor; описывает данные, используемые выбором снижения стоимости заклинания.

## Условия использования

[module/data/actor/commonActorData.js](../../../../../../../../../module/data/actor/commonActorData.js):4,51–54 вызывает focus() четыре раза в отдельных SchemaField focus1/focus2/focus3/focus4.

## Введённые сущности и действия с ними

| Поле / сущность | Тип, начальное значение и ограничения | Назначение и действия |
| --- | --- | --- |
| focus() | default export, :4–9 | Фабрика полей одного слота. |
| name | StringField, initial='' | Произвольное имя. |
| value | NumberField, initial=0; min/max/integer не заданы | Числовое значение для выбора фокусировки. |

## Основные функции и методы

focus():4–9 без аргументов возвращает поля name/value. Не расходует ресурс и не рассчитывает стоимость магии.

## Используемые сущности и зависимости

| Сущность | Файл определения / API | Связь, место и цель |
| --- | --- | --- |
| NumberField, StringField | Внешний API Foundry 14.367.0: /opt/foundryvtt/common/data/fields.mjs | fields:2; поля :6–7. |
| Четыре слота focus1–focus4 | [module/data/actor/commonActorData.js](../../../../../../../../../module/data/actor/commonActorData.js) | Внешний владелец и отдельные вызовы фабрики:51–54. |

## Известные потребители

| Файл-потребитель | Обращение и условия |
| --- | --- |
| [module/actor/mixins/castSpellMixin.js](../../../../../../../../../module/actor/mixins/castSpellMixin.js) | castSpell:50–86 выбирает только слоты value>0, делает focusOptions с числом и подписью name(value). :101–115 считывает focus/secondFocus из диалога и вычитает сумму из стоимости STA; :116–132 добавляет цену дополнительной атаки и ограничивает итог снизу единицей. |
| [templates/dialog/combat/spell-attack.hbs](../../../../../../../../../templates/dialog/combat/spell-attack.hbs) | Получает useFocus/focusOptions; выбор focus и secondFocus возвращает значения обработчику. |
| [templates/partials/character/tab-magic.hbs](../../../../../../../../../templates/partials/character/tab-magic.hbs) | Вкладка focus:55–77 даёт ввод name/value четырёх слотов. Используется PARTS.magic персонажа и монстра. |
| [templates/partials/monster/monster-spell-tab.hbs](../../../../../../../../../templates/partials/monster/monster-spell-tab.hbs) | Имеющийся другой шаблон также содержит четыре поля; не объявляется текущим PARTS.magic. |
| [module/actor/sheets/WitcherCharacterSheet.js](../../../../../../../../../module/actor/sheets/WitcherCharacterSheet.js); [module/actor/sheets/WitcherMonsterSheet.js](../../../../../../../../../module/actor/sheets/WitcherMonsterSheet.js) | Текущие magic PARTS указывают на character/tab-magic; есть magicTabs.focus. |

Область поиска: прямые импорты в module, обращения к полям в module/templates и строковые пути в 226 packsJson. Соседние файлы проверялись в пределах указанных обращений. Их полный разбор не объявляется выполненным.

## Данные и изменения состояния

Каждый слот отдельный объект: изменение focus1.value не меняет focus2. castSpell читает слоты, а пишет остаток system.derivedStats.sta.value, не уменьшает focusN.value. Одноимённый derivedStats.focus — отдельная модель производного параметра; эти поля с ней не объединяются.

## Проверки и доказательства

Прочитаны 9 строк. Реальная CommonActorData создаёт четыре независимые пары {'name':'','value':0}; изменение первого слота до 3 оставляет второй нулевым. Связка выбора в шаблоне и вычитания двух выбранных чисел прочитана до записи STA.

Файл прочитан полностью; определения и потребители сопоставлены в обе стороны. Изолированные проверки использовали реальные DataModel/TypeDataModel и поля установленного Foundry, а внешние действия — явно указанные подмены. Полный сценарий и результаты находятся в журнале TASK-0003.003.

## Непроверенные участки и открытые вопросы

Полный castSpell, DOM выбора двух фокусов, допустимость сочетаний, предметы-фокусы и игровые правила не проверялись. Изолированная проверка этой карточки подтверждает схему и независимость слотов.

## Связанные проблемы

Новых проблем в пределах выполненной проверки не зарегистрировано.


## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.003 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.

## Уточнение TASK-0003.006

2026-09-10, `fe7ea7420cd4dfa6ee51baf7520f7b0ad8f8b13d`. Четыре отдельных SchemaField(focus()) включены в focus1–4:51–54 у персонажа и монстра. Одноимённый derivedStats.focus имеет другой источник; CommonActorData.prepareBaseData:88 вычисляет его unmodifiedMax из текущих WILL.value/INT.value.

Карточки сборки: [commonActorData](../../commonActorData.js.md). [Сверка TASK-0003.006](../../../../../../review-log.md#task-0003006).
