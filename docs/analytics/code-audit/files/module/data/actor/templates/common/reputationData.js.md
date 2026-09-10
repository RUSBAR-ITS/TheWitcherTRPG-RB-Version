# module/data/actor/templates/common/reputationData.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/data/actor/templates/common/reputationData.js](../../../../../../../../../module/data/actor/templates/common/reputationData.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `c34b790379fd98cd7e33ccbeeca085e49297a40f` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.003](../../../../../../../../tasks/task-0003.003.md), одна порция из восьми файлов |
| Запись перекрёстной сверки | [TASK-0003.003](../../../../../../review-log.md#task-0003003) |

## Назначение файла

Определяет числовую репутацию Actor на основе общей фабрики stat, подготовку max и миграцию исходного максимума.

## Условия использования

Default export Reputation extends foundry.abstract.DataModel. [module/data/actor/commonActorData.js](../../../../../../../../../module/data/actor/commonActorData.js):13,36 включает модель через EmbeddedDataField. Это system.reputation; текстовая general.reputation из [module/data/actor/templates/character/generalData.js](../../../../../../../../../module/data/actor/templates/character/generalData.js):14 — отдельная запись valueLabel.

## Введённые сущности и действия с ними

| Сущность / поле | Определение и начальное значение | Действие |
| --- | --- | --- |
| Reputation | Класс :3; default export | Схема и миграция числовой репутации. |
| max | stat:5 — NumberField, initial=0, integer=true | Рабочий максимум, prepareBaseData присваивает unmodifiedMax. |
| unmodifiedMax | stat:6 — NumberField, initial=0, integer=true | База; получает старый max только при сравнении ==0. |
| value | stat:7 — NumberField, initial=0 | Значение для бросков; Actor.calculateStats присваивает max. |
| label | stat:8 — StringField, initial=WITCHER.Actor.DerStat.Rep | Ключ подписи; тот же ключ — metadata unmodifiedMax.label. |
| totalModifiers | stat:9 — NumberField, initial=0, integer=true | Объявлено фабрикой; собственные методы Reputation его не прибавляют. |

min/max диапазона фабрика stat не задаёт. Наличие totalModifiers не означает его включения в расчёт репутации.

## Основные функции и методы

| Метод | Вход → результат | Мутации, условия и асинхронность |
| --- | --- | --- |
| static defineSchema():4–6 | Без аргументов → stat('WITCHER.Actor.DerStat.Rep') | Создание пяти полей; синхронно. |
| prepareBaseData():8–10 | Экземпляр → undefined | this.max=this.unmodifiedMax, только память. |
| static migrateData(source):13–19 | Объект → super.migrateData(source) | Если source.unmodifiedMax == 0, записывает source.max в source.unmodifiedMax; меняет переданный объект синхронно. |

В репозитории не найден прямой вызов reputation.prepareBaseData(); CommonActorData.prepareBaseData:75 сам выполняет такое же присваивание. Наличие метода модели не выдаётся за доказательство его автоматического вызова на каждом вложенном экземпляре.

## Используемые сущности и зависимости

| Сущность | Определение | Связь и доказательство |
| --- | --- | --- |
| stat | [module/data/actor/templates/common/stats/statData.js](../../../../../../../../../module/data/actor/templates/common/stats/statData.js); [карточка](stats/statData.js.md) | Прямой импорт :1; вызов :5 с ключом подписи. Все поля делегированы фабрике. |
| DataModel | Foundry 14.367.0: /opt/foundryvtt/common/abstract/data.mjs | Наследование :3, super.migrateData:18. |
| WITCHER.Actor.DerStat.Rep | [lang/en.json](../../../../../../../../../lang/en.json); [lang/ru.json](../../../../../../../../../lang/ru.json) | Строковая ссылка на локализацию; отсутствует во всех восьми lang, см. issue-00014. |

## Известные потребители

| Файл | Обращение |
| --- | --- |
| [module/data/actor/commonActorData.js](../../../../../../../../../module/data/actor/commonActorData.js) | EmbeddedDataField:36; prepareBaseData:75 копирует unmodifiedMax→max. |
| [module/actor/witcherActor.js](../../../../../../../../../module/actor/witcherActor.js) | calculateStats:68 копирует reputation.max→value. В этой ветке нет прибавления totalModifiers. |
| [module/actor/sheets/mixins/statMixin.js](../../../../../../../../../module/actor/sheets/mixins/statMixin.js) | _onReputation:39–84: первый режим бросает 1d10 с порогом reputation.value и reversal=true; второй формирует 1d10 + репутация + WILL. |
| [templates/partials/character/tab-stats.hbs](../../../../../../../../../templates/partials/character/tab-stats.hbs) | :40–66 — отображение value/max и сравнение для оформления; доступность зависит от displayRep. |
| [templates/sheets/actor/configuration/app/partials/stats-block.hbs](../../../../../../../../../templates/sheets/actor/configuration/app/partials/stats-block.hbs); [templates/sheets/actor/configuration/app/edit-stats.hbs](../../../../../../../../../templates/sheets/actor/configuration/app/edit-stats.hbs) | Поле записи system.reputation.unmodifiedMax, отображаемое value берётся из reputation.max; edit-stats передаёт объект репутации. |
| [module/actor/sheets/WitcherActorSheet.js](../../../../../../../../../module/actor/sheets/WitcherActorSheet.js); [module/setup/settings.js](../../../../../../../../../module/setup/settings.js) | Контекст displayRep и одноимённая настройка:61. |
| [module/activeEffect/WitcherActiveEffectSheet.js](../../../../../../../../../module/activeEffect/WitcherActiveEffectSheet.js) | autocomplete:120–132 локализует metadata.label полей схемы; затрагивает отсутствующую подпись базы. |
| [module/setup/config.js](../../../../../../../../../module/setup/config.js) | statMap.reputation:130 имеет пустой origin; это не полный путь к этой модели. |

## Данные и изменения состояния

Миграция меняет source, подготовка — max в памяти; значения для отображения/броска назначает Actor. Отдельной записи документа и лимита репутации класс не выполняет. Входы {max:7}, {max:7,unmodifiedMax:0}, {max:7,unmodifiedMax:4} после подготовки дают max 0,7,4. Отсутствующий unmodifiedMax не удовлетворяет сравнению с 0 до подстановки default.

## Проверки и доказательства

Прочитаны 20 строк и stat целиком, сопоставлены подготовка CommonActorData, calculateStats и два режима броска. Три варианта миграции выполнены с настоящим Reputation и внутри CommonActorData; оба способа подготовки дали 0/7/4. Ключ подписи повторно проверен в восьми JSON локализаций — нигде не найден.

## Непроверенные участки и открытые вопросы

Импорт старых Actor, браузерные режимы броска, полная последовательность фаз эффектов и поддерживаемая история форматов не проверялись. Вопрос, какие поля репутации должны модифицироваться эффектами, требует отдельного согласования правил.

## Связанные проблемы

[issue-00011](../../../../../../../../issues/potential/issue-00011.md) дополнена случаем Reputation; [issue-00014](../../../../../../../../issues/potential/issue-00014.md) дополнена ссылкой на полный разбор модели. Дубликаты не создавались.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.003 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.

## Уточнение TASK-0003.006

2026-09-10, `fe7ea7420cd4dfa6ee51baf7520f7b0ad8f8b13d`. EmbeddedDataField(Reputation):36 и явное копирование reputation.max=unmodifiedMax:75 сверены с жизненным циклом ядра. Прямого рекурсивного вызова prepareBaseData вложенных DataModel нет; фактическое копирование выполняет CommonActorData. В проверке base3→max3, исходный снимок сохранился.

Карточки сборки: [commonActorData](../../commonActorData.js.md). [Сверка TASK-0003.006](../../../../../../review-log.md#task-0003006).

## Уточнение TASK-0003.007

2026-09-10, `b8b89a7e3392235f993c21f3c6d277a4a2e7a55f`. calculateStats:68 присваивает reputation.value=reputation.max при каждом из двух проходов; собственный модификатор reputation здесь не прибавляется. CommonActorData готовит max из unmodifiedMax; дальнейшее влияние эффекта зависит от его целевого поля/phase. Повторно описана граница вычислений без изменения правил.

Карточки: [WitcherActor](../../../../actor/witcherActor.js.md), [modifierMixin](../../../../actor/mixins/modifierMixin.js.md). [Сверка TASK-0003.007](../../../../../../review-log.md#task-0003007).
