# module/data/actor/templates/common/currencyData.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/data/actor/templates/common/currencyData.js](../../../../../../../../../module/data/actor/templates/common/currencyData.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `c34b790379fd98cd7e33ccbeeca085e49297a40f` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.003](../../../../../../../../tasks/task-0003.003.md), одна порция из восьми файлов |
| Запись перекрёстной сверки | [TASK-0003.003](../../../../../../review-log.md#task-0003003) |

## Назначение файла

Фабрика семи числовых остатков валют; используется общей моделью Actor и моделью добычи.

## Условия использования

[module/data/actor/commonActorData.js](../../../../../../../../../module/data/actor/commonActorData.js):1,20 и [module/data/actor/lootData.js](../../../../../../../../../module/data/actor/lootData.js):1,10 напрямую импортируют фабрику и оборачивают её в SchemaField currency. Это два непосредственных потребителя.

## Введённые сущности и действия с ними

| Поле / сущность | Тип, начальное значение и ограничения | Назначение и действия |
| --- | --- | --- |
| currency() | default export, :3–13 | Создаёт объект полей. |
| bizant | NumberField, initial=0 | Количество монет; min/max/integer не заданы. |
| ducat | NumberField, initial=0 | Количество монет; min/max/integer не заданы. |
| lintar | NumberField, initial=0 | Количество монет; min/max/integer не заданы. |
| floren | NumberField, initial=0 | Количество монет; min/max/integer не заданы. |
| crown | NumberField, initial=0 | Количество монет; min/max/integer не заданы. |
| oren | NumberField, initial=0 | Количество монет; min/max/integer не заданы. |
| falsecoin | NumberField, initial=0 | Количество монет; min/max/integer не заданы. |

## Основные функции и методы

currency():3–13 возвращает семь NumberField. Курсы, комиссии, перевод валют, вес и журнал поступлений здесь не вычисляются.

## Используемые сущности и зависимости

| Сущность | Файл определения / API | Связь, место и цель |
| --- | --- | --- |
| fields.NumberField | Внешний API Foundry 14.367.0: /opt/foundryvtt/common/data/fields.mjs | Глобальная ссылка :1; конструирование :5–11. |
| Ключи валют | [module/setup/config.js](../../../../../../../../../module/setup/config.js) | Сопоставление с WITCHER.currency:624–632, rates:634–641 и excluded:643–645; фабрика справочник не импортирует. |

## Известные потребители

| Файл-потребитель | Обращение и условия |
| --- | --- |
| [module/data/actor/commonActorData.js](../../../../../../../../../module/data/actor/commonActorData.js); [module/data/actor/lootData.js](../../../../../../../../../module/data/actor/lootData.js) | Обе calcCurrencyWeight суммируют Number семи полей, включая falsecoin, и умножают число монет на 0.001. |
| [module/actor/witcherActor.js](../../../../../../../../../module/actor/witcherActor.js) | getTotalWeight:245–247 добавляет system.calcCurrencyWeight() к весу предметов, округляет итог вверх. |
| [module/actor/mixins/currencyConverterMixin.js](../../../../../../../../../module/actor/mixins/currencyConverterMixin.js) | openCurrencyConverter:17–103 читает остатки, исключает falsecoin, рассчитывает amount×fromRate/toRate×(1-fee/100), округляет вниз и пишет два пути currency; getCurrencyRates:9–15 читает config. |
| [module/actor/sheets/mixins/currencyConverterMixin.js](../../../../../../../../../module/actor/sheets/mixins/currencyConverterMixin.js); [module/actor/sheets/WitcherActorSheet.js](../../../../../../../../../module/actor/sheets/WitcherActorSheet.js) | Обработчик .open-currency-converter вызывает actor.handleCurrencyConverter, затем openCurrencyConverter; подключён currencyConverterListeners:244. |
| [templates/sheets/actor/currencyConverter/currencyConverter.hbs](../../../../../../../../../templates/sheets/actor/currencyConverter/currencyConverter.hbs); [templates/chat/currency-conversion.hbs](../../../../../../../../../templates/chat/currency-conversion.hbs) | Диалог получает список currencies/options; две независимые валюты from/to и комиссия. Сообщение отображает результат. |
| [module/data/actor/templates/character/logData.js](../../../../../../../../../module/data/actor/templates/character/logData.js); [module/app/reward/reward.js](../../../../../../../../../module/app/reward/reward.js) | Log.addCurrencyReward:31–36 добавляет currencyLog и обновляет system.currency[type]; Rewards.handoutCurrencyRewards:148–157 вызывает метод выбранных Actor. |
| [module/actor/sheets/WitcherLootSheet.js](../../../../../../../../../module/actor/sheets/WitcherLootSheet.js) | Обработчик покупки:149–162 сравнивает остаток покупателя со стоимостью, затем формирует списание и зачисление currency[coinType]. |
| [templates/sheets/actor/tabs/tab-inventory.hbs](../../../../../../../../../templates/sheets/actor/tabs/tab-inventory.hbs); [templates/sheets/actor/loot-sheet.hbs](../../../../../../../../../templates/sheets/actor/loot-sheet.hbs) | Семь полей ввода system.currency.<ключ>; настройки HTML не являются ограничениями фабрики. |
| [templates/sheets/actor/rewards/currency.hbs](../../../../../../../../../templates/sheets/actor/rewards/currency.hbs) | Отображает журнал валюты и находит подпись типа в config.currency. |

Область поиска: прямые импорты в module, обращения к полям в module/templates и строковые пути в 226 packsJson. Соседние файлы проверялись в пределах указанных обращений. Их полный разбор не объявляется выполненным.

## Данные и изменения состояния

Исходные остатки хранятся в system.currency; фабрика не записывает Actor и не хранит курсы. WITCHER.currency содержит те же семь ключей; currencyRates — шесть, falsecoin исключён из конвертера. В нормальном примере crown=100, обмен 10 crown→oren без комиссии даёт update crown=90/oren=10. Одинаковые from/to дают повторный вычисляемый ключ в объекте update — [issue-00020](../../../../../../../../issues/potential/issue-00020.md).

## Проверки и доказательства

Прочитаны 13 строк. Ключи фабрики сверены со справочником и курсами. 1+2+3+4+5+6+7 монет дают 0.028 в обеих настоящих моделях. Исходный openCurrencyConverter выполнен с подменёнными DialogV2, renderTemplate, ChatMessage и update: нормальный и одинаковый from/to проверены отдельно.

Файл прочитан полностью; определения и потребители сопоставлены в обе стороны. Изолированные проверки использовали реальные DataModel/TypeDataModel и поля установленного Foundry, а внешние действия — явно указанные подмены. Полный сценарий и результаты находятся в журнале TASK-0003.003.

## Непроверенные участки и открытые вопросы

Браузерная валидация, конкурирующие покупки, фактическая запись и журнал, полная экономика и корректность курсов по правилам не проверялись.

## Связанные проблемы

[issue-00020](../../../../../../../../issues/potential/issue-00020.md) — при обмене на ту же валюту в аргументах update увеличивается остаток.


## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.003 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.

## Уточнение TASK-0003.005

2026-09-10, `c9eac1ffb28fdf69935d500fff26d4d0ad1d1609`. Подробно описаны [currencyLogData](../character/currencyLogData.js.md) и [Log](../character/logData.js.md). Log.addCurrencyReward пишет историю и абсолютный остаток одной валюты в одном update, но не возвращает Promise. Настоящая модель с crown100 и amount5 сформировала 105; два вызова с ожиданием лишь результата Log до завершения update дали 102/103 для +2/+3. Это [issue-00028](../../../../../../../../issues/potential/issue-00028.md); серверный итог не проверялся.

[Сверка TASK-0003.005](../../../../../../review-log.md#task-0003005).

## Уточнение TASK-0003.006

2026-09-10, `fe7ea7420cd4dfa6ee51baf7520f7b0ad8f8b13d`. Повторно сопоставлены оба прямых включения currency: CommonActorData:20 и LootData:10. Персонаж/монстр получают первое по наследованию; LootData общую модель не наследует. По одной монете семи видов дали 0.007 в каждой из четырёх настоящих моделей; округление общего веса остаётся в Actor.getTotalWeight.

Карточки сборки: [commonActorData](../../commonActorData.js.md), [lootData](../../lootData.js.md). [Сверка TASK-0003.006](../../../../../../review-log.md#task-0003006).

## Уточнение TASK-0003.027

2026-09-11, `rusbar-main`, `ce0c7eb7069b215b641d725913b3aae21502e811`. Семь полей точно соответствуют input.name современной вкладки инвентаря: bizant/ducat/lintar/floren/crown/oren/falsecoin. Все input type=number/data-dtype=Number; min/max в HBS отсутствуют. Это Actor form submit, а не Item inline-edit.

Связанные шаблоны: [templates/sheets/actor/tabs/tab-inventory.hbs](../../../../../../../../../templates/sheets/actor/tabs/tab-inventory.hbs). [Проверки и ограничения](../../../../../../review-log.md#task-0003027). Полный разбор соседей вне этой порции не засчитывается.
