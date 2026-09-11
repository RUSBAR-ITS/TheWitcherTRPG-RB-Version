# module/data/actor/templates/character/logData.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/data/actor/templates/character/logData.js](../../../../../../../../../module/data/actor/templates/character/logData.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `c9eac1ffb28fdf69935d500fff26d4d0ad1d1609` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.005](../../../../../../../../tasks/task-0003.005.md), одна порция из семи файлов |
| Запись перекрёстной сверки | [TASK-0003.005](../../../../../../review-log.md#task-0003005) |

## Назначение файла

Модель двух журналов персонажа и операций добавления наград/расходов. Методы одновременно добавляют запись в историю и инициируют обновление соответствующего баланса Actor.

## Условия использования

Log наследует foundry.abstract.DataModel. CharacterData:4,30 импортирует класс и включает через EmbeddedDataField. В экземпляре Log.parent — CharacterData, Log.parent.parent — Actor. Самостоятельный Log без этой цепочки подходит для схемы/данных, но его методы награды требуют владельца с update.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| fields | const, 4 | Классы полей | Локальная | Используется defineSchema |
| Log | class, 6–38 | Вложенная модель журналов | Default export | Создание Foundry как EmbeddedDataField |
| ipLog | ArrayField(SchemaField), 9 | История IP | system.logs.ipLog | Начально []; записи создаёт ipLog() |
| currencyLog | ArrayField(SchemaField), 10 | История валют | system.logs.currencyLog | Начально []; записи создаёт currencyLog() |
| defineSchema | static method, 7–12 | Определение двух массивов | API модели Foundry | Вызывает обе фабрики |
| addIpReward | method, 14–29 | Запись и баланс обычных/магических IP | Метод экземпляра | push → Actor.update; собственный return отсутствует |
| addCurrencyReward | method, 31–37 | Запись и баланс выбранной валюты | Метод экземпляра | push → Actor.update; собственный return отсутствует |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| Log.defineSchema() | Классы полей Foundry и обе фабрики импортированы | Два ArrayField | Создаёт SchemaField записи каждого типа | Синхронно; без записей |
| Log.addIpReward(label,ip,isMagic) | Родитель CharacterData, grandparent с update; числовой ip необходим для сложения | undefined | Сначала push({label,ip,isMagic}); при !isMagic update ipLog и improvementPoints+ip; при isMagic — ipLog и magic.magicImprovementPoints+ip | Метод не async, не возвращает и не ожидает Promise update; нет catch/отката массива |
| Log.addCurrencyReward(label,amount,type) | Родитель с currency[type]; amount нужен числовой | undefined | push({label,amount,type}); update всего currencyLog и computed key system.currency.<type> | Нет проверки type, преобразования amount, ожидания/возврата update или отката |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| currencyLog (default) | [module/data/actor/templates/character/currencyLogData.js](../../../../../../../../../module/data/actor/templates/character/currencyLogData.js) | Прямой импорт/вызов | 1,10: схема записи валют | Фабрика прочитана полностью |
| ipLog (default) | [module/data/actor/templates/character/ipLogData.js](../../../../../../../../../module/data/actor/templates/character/ipLogData.js) | Прямой импорт/вызов | 2,9: схема записи IP | Фабрика прочитана полностью |
| DataModel, ArrayField, SchemaField | Foundry 14.367.0, /opt/foundryvtt/common/data/fields.mjs; /opt/foundryvtt/common/abstract/data.mjs | Наследование и API | 4,6,9–10; создание вложенной модели | Настоящий Log внутри CharacterData |
| parent: CharacterData | [module/data/actor/characterData.js](../../../../../../../../../module/data/actor/characterData.js) | Родитель EmbeddedDataField и чтение данных | 19–22,30: balances и Log; методы читают parent.improvementPoints/magic/currency | Связь родителей проверена реальными DataModel; currency унаследована |
| currency | [module/data/actor/templates/common/currencyData.js](../../../../../../../../../module/data/actor/templates/common/currencyData.js); [module/data/actor/commonActorData.js](../../../../../../../../../module/data/actor/commonActorData.js) | Наследованные данные | 35: доступ к балансу по type | Семь ключей валют общей модели |
| parent.parent.update | Foundry 14.367.0, /opt/foundryvtt/common/abstract/document.mjs:740–746 | Метод документа через владельца | 17,24,33: инициирует запись | В ядре async update ожидает updateDocuments и возвращает Promise; в сценарии заменён отложенной записью аргументов |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/data/actor/characterData.js](../../../../../../../../../module/data/actor/characterData.js) | Log | logs = EmbeddedDataField(Log) | 4,30 |
| [module/app/reward/reward.js](../../../../../../../../../module/app/reward/reward.js) | addIpReward/addCurrencyReward | handoutIpRewards/handoutCurrencyRewards после GM-проверки и диалога вызывают методы выбранных Actor | 57–88,145–177; forEach:69,157 |
| [module/actor/mixins/skillMixin.js](../../../../../../../../../module/actor/mixins/skillMixin.js) | addIpReward | levelUpSkill пишет расходы магических и обычных очков; затем сам вызывает Actor.update | 28,32,35–39 |
| [module/actor/sheets/WitcherCharacterSheet.js](../../../../../../../../../module/actor/sheets/WitcherCharacterSheet.js) | addIpReward | _saveIpSpending передаёт label и отрицательное значение из DOM | 452–458 |
| [module/actor/rewardsSheet.js](../../../../../../../../../module/actor/rewardsSheet.js) | logs для представления | Контекст system=document.system; PARTS.ip/currency | 29–36,48–53 |
| [templates/sheets/actor/rewards/ip.hbs](../../../../../../../../../templates/sheets/actor/rewards/ip.hbs); [templates/sheets/actor/rewards/currency.hbs](../../../../../../../../../templates/sheets/actor/rewards/currency.hbs) | Массивы журналов | each показывает записи в порядке массива | 3–9 / 3–11 |

Вход в массовую выдачу зарегистрирован в [module/TheWitcherTRPG.js](../../../../../../../../../module/TheWitcherTRPG.js):39–42 как game.api.rewards.ip/currency; [module/actor/mixins/rewardsMixin.js](../../../../../../../../../module/actor/mixins/rewardsMixin.js):2–8 вызывает API для [this]. Эти обёртки и диалоги не являются методами Log.

Потребители искались по именам файлов/экспортов, точным и динамическим путям в module/, templates/ и packsJson/. В 226 JSON-компедиумах строковых ссылок с префиксами system.logs, system.skillTrainingN, system.pannels, system.attackStats не найдено. Бинарные packs, действующие БД и внешние макросы не проверялись.

## Данные и изменения состояния

push изменяет живой массив до любого успешного сохранения. Аргумент Actor.update содержит ссылку на весь массив и уже вычисленный абсолютный остаток; баланс parent в самом методе не присваивается. Запись массива и баланса инициируется одним update на вызов, но ошибка или незавершённость этого update вызывающему коду через результат Log не передаётся. Собственной сериализации конкурентных вызовов нет.

При ip/amount в виде строки оператор + может соединять строки. Проверки схемы не предшествуют push и вычислению суммы; они выполняются при последующей обработке документа. Методы не проверяют права GM, достаточность средств, допустимость знака или тип валюты. GM-проверка относится только к внешнему handout*-входу; утверждение о правах конкретного Actor вне реального клиента не делается.

В файле нет удаления/редактирования записей, расчёта итогового остатка из истории или отметки времени. История — массив записей, а текущие balances хранятся отдельно. Поведение levelUpSkill с двумя записями и самостоятельным update необходимо оценивать вместе с этими побочными действиями Log.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Схема и цепочка родителей | Реальные CharacterData/Log; вместо Actor — минимальный DataModel с перехваченным update | logs instanceof Log; logs.parent=CharacterData; logs.parent.parent=двойник Actor; defaults [] | Двойник не реализует клиент/БД Actor |
| Обычные/магические IP и валюта | Исходные методы Log, исходные балансы 10/8/crown100 | Обычные +2→12; магические +3→11; обычные -2→8; crown+5→105, записи соответствуют аргументам | Подтверждены только payloads |
| Асинхронность | Отложенный update; await двух вызовов Log до разрешения Promise | Результат каждого метода undefined; два pending update. Балансы payloads IP12/13 или crown102/103 вместо последовательных итогов 15/105 | Реальный серверный порядок и потери записи не моделировались |
| Ручной расход | Исходный обработчик листа + Log + реальный updateSource dryRun | '3' → число 7, валидация успешна; '-3' → '10-3', ошибка improvementPoints must be a number | Объекты DOM и update подменены |
| Реальный побочный эффект для issue-00017 | Исходный levelUpSkill + настоящий Log, spellcast2, magic10 | Сначала update магических IP6 из Log, затем update IP10 из levelUpSkill; два pending запроса | Окончательный результат БД не проверялся |

## Непроверенные участки и открытые вопросы

Исходник прочитан полностью; соседние файлы проверены только в пределах описанных связей. Мир, браузер, реальное сохранение и полный жизненный цикл Actor/листов не запускались. Подмены и исполнявшийся сценарий приведены в журнале; успешная проверка карточки не подтверждает исправность всей системы. Полные диалоги выдачи, права и синхронизация клиентов относятся к последующим задачам. Неправильные аргументы (неизвестная валюта, строковый amount) отмечены как контракт метода; отдельные проблемы для непроверенных пользовательских путей не создавались.

## Связанные проблемы

[issue-00028](../../../../../../../../issues/potential/issue-00028.md) — отсутствие возвращаемого завершения записи и риск конфликтующих остатков. [issue-00029](../../../../../../../../issues/potential/issue-00029.md) — строковый расход в ручном интерфейсе. [issue-00017](../../../../../../../../issues/potential/issue-00017.md) дополнена вызовами настоящего Log: он действительно инициирует списание, которое следующий update levelUpSkill перекрывает в захваченных данных.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.005 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.

## Уточнение TASK-0003.006

2026-09-10, `fe7ea7420cd4dfa6ee51baf7520f7b0ad8f8b13d`. Подтверждено единственное включение Log в CharacterData.logs:30; CommonActorData и MonsterData такого блока не определяют. Методы записи балансов принадлежат Log и потребителям, CharacterData.enrichedText их не вызывает. Результаты TASK-0003.005 об асинхронности сохраняются.

Карточки сборки: [characterData](../../characterData.js.md), [monsterData](../../monsterData.js.md). [Сверка TASK-0003.006](../../../../../../review-log.md#task-0003006).

## Уточнение TASK-0003.029

2026-09-11, `273a6d7db0b7c866399db3ecd4f7191817ae6f10`. Повторно исполнен настоящий Log внутри CharacterData с полностью разобранным levelUpSkill. Магическая стоимость 4 при балансе 10 инициирует Log.update на 6, затем уровень инициирует update на прежние 10; обе записи не ожидаются. При удержанных Promise метод повышения завершился до записей. Итог серверной гонки этим опытом не установлен.

Сверенные связи: [module/actor/mixins/skillMixin.js](../../../../../../../../../module/actor/mixins/skillMixin.js); [templates/partials/character/tab-skills.hbs](../../../../../../../../../templates/partials/character/tab-skills.hbs). Полные карточки новых файлов — в [указателе порции](../../../../../README.md#навыки-броски-развитие-и-пользовательские-навыки--task-0003029). [Проверки, ограничения и версия](../../../../../../review-log.md#task-0003029). Исходники и статус проблем не менялись.
