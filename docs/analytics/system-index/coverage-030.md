# TASK-0006.030 — Развитие навыков, IP и журнал обучения

2026-09-16; rusbar-main, исходный HEAD `deee6c1dcec1b5419e8ac37bd8e69aececf0b2a5`, дерево в начале чистое. [Задача](../../tasks/task-0006.030.md), [запросы](examples/expansion-030-queries.json), [тесты](tests/test_expansion_030.py).

## Результат и пределы

Добавлены 63 сущности, 214 отношений и 9 процессов. Всего 4999 сущностей, 13817 отношений, 425 процессов (1391 шагов, 2596 переходов), 383 границы. Определения в 291/615 файлах: два словаря en/ru complete, 289 файлов partial. Роли: 206 основных/85 смежных/324 без определений. Отношения в 295 файлах, локальные шаги процессов в 145.

Все прежние ID, владельцы, 13603 отношения и 416 процессов сохранены. Уточнены шесть прежних сущностей (метод повышения, Log, фабрика training, Rewards, handout и граница IP controls). Новый уровень детализации не означает полного исполнения в Foundry. Данные мира, игровые исходники, аудит и issues не изменялись.

| Файл | Включённая область и остаток |
| --- | --- |
| [module/actor/mixins/skillMixin.js](../../../module/actor/mixins/skillMixin.js) (src-000022) | levelUp и его writers раскрыты; прежние roll/social/custom переиспользованы, полный runtime partial. |
| [module/actor/sheets/mixins/skillMixin.js](../../../module/actor/sheets/mixins/skillMixin.js) (src-000045) | Callback level-up и существующие listeners; глобальный jQuery и внешний lifecycle остаются границами. |
| [module/actor/sheets/WitcherCharacterSheet.js](../../../module/actor/sheets/WitcherCharacterSheet.js) (src-000029) | IP handlers/listeners/rewards instance; прочие методы и весь UI вне этой порции. |
| [module/data/actor/templates/character/ipLogData.js](../../../module/data/actor/templates/character/ipLogData.js) (src-000069) | Все три schema поля записи; внешняя очистка/хранение и все потребители не объявлены complete. |
| [module/data/actor/templates/character/logData.js](../../../module/data/actor/templates/character/logData.js) (src-000070) | Полная схема и addIpReward; addCurrencyReward/экономика вне .030. |
| [module/data/actor/templates/character/skillTrainingData.js](../../../module/data/actor/templates/character/skillTrainingData.js) (src-000072) | name/value factory, четыре source слота и ручной DOM маршрут; автоматическое обучение в module/templates не найдено. |
| [module/actor/rewardsSheet.js](../../../module/actor/rewardsSheet.js) (src-000026) | DEFAULT_OPTIONS/PARTS/TABS/context, header/IP; currency часть и общий core UI вне .030. |
| [module/app/reward/reward.js](../../../module/app/reward/reward.js) (src-000049) | getPlayerActors/ipRewardDialog/handoutIpRewards; currency методы не раскрыты, core DOM/DB внешние. |
| [module/actor/mixins/rewardsMixin.js](../../../module/actor/mixins/rewardsMixin.js) (src-000021) | addIpReward wrapper раскрыт; addCurrencyReward вне области. |
| [templates/partials/character/tab-skills.hbs](../../../templates/partials/character/tab-skills.hbs) (src-000527) | Встроенные/Item строки прежние; IP/training/rewards inputs и события раскрыты, общий browser lifecycle partial. |
| [templates/partials/character/tab-magic.hbs](../../../templates/partials/character/tab-magic.hbs) (src-000525) | Только magicImprovementPoints input/submit. Прочие магические/focus/vigor данные остаются следующими порциями. |
| [templates/sheets/actor/rewards/ip.hbs](../../../templates/sheets/actor/rewards/ip.hbs) (src-000575) | Весь IP HBS чтения; внешние render/локализация/стили partial. |
| [templates/sheets/actor/rewards/header.hbs](../../../templates/sheets/actor/rewards/header.hbs) (src-000574) | Заголовок окна и PARTS; внешний render/локализация partial. |
| [module/data/actor/characterData.js](../../../module/data/actor/characterData.js) (src-000054) | Два пула, logs и четыре training slots связаны; остальные поля/consumers прежние partial. |
| [module/app/htmlUtils.js](../../../module/app/htmlUtils.js) (src-000048) | createLabeledInput для IP формы; createLabeledSelect и прочие callers вне .030. |
| [templates/chat/rewards.hbs](../../../templates/chat/rewards.hbs) (src-000505) | IP report контекст/условие/список Actor; валютная ветвь отдельно. |
| [module/data/item/skillItemData.js](../../../module/data/item/skillItemData.js) (src-000124) | Схема value/потребители переиспользованы; граница отдельного Item уровня, не общий IP writer. |
| [module/setup/config.js](../../../module/setup/config.js) (src-000209) | magicSkills и optional costMultiplier; прежняя карта сохранена, остальной config вне порции. |

<a id="level"></a>
## Повышение встроенного навыка

Кнопка находится в edit-skills.hbs:9–10, открываемом конфигуратором характеристик/навыков. Основной tab-skills.hbs содержит вывод навыков, переход к редактору и отдельную вкладку IP; собственного level-up в нём нет. sheet.skillMixin.skillListener передаёт dataset.skill в actor.levelUpSkill без ожидания результата события. Ключ формы берётся из модели, тогда как commonspeech в skillMap расходится с commonsp модели (issue4).

| Шаг | Фактический контракт |
| --- | --- |
| Чтение | skillMap[skillName], entry.attribute.name, system.skills[attribute][skillName].value; базовый уровень, не modifiedValue |
| Цена | Math.max(skillValue,1) × (entry.costMultiplier ?? 1). В текущей карте 12 записей с costMultiplier=2 |
| Магический навык | magicSkills содержит spellcast, ritcraft, hexweave; внутренний magicalCost равен цене, а при magicalIp<цены заменяется всем magicalIp |
| Журнал магии | Обычная стоимость уменьшается на внутренний magicalCost; вызов Log с отрицательной магической дельтой выполняется даже при нуле |
| Журнал обычных IP | Отрицательная оставшаяся стоимость записывается только при truthy levelUpCost |
| Итоговый запрос | ++skillValue, обычный пул минус остаток, магический пул минус внешняя magicalCost=0; update не ожидается |

Внешняя и внутренняя let magicalCost — разные переменные. Журнал инициирует собственный update магического пула, а последний запрос посылает исходный магический баланс (issue17). В коде нет guard достаточности обычных IP, максимального уровня, типа Actor или неизвестного ключа. Для отрицательного магического пула также нет нижнего ограничения (issues191/192). Это описание текущих вычислений, не правила развития и не исправление.

<a id="log"></a>
## Журнал и границы сохранения

CharacterData.logs содержит EmbeddedDataField(Log); ipLog — ArrayField записей label/String, ip/Number, isMagic/Boolean. Числовой ip имеет initial=0 без min/max/integer; запись не содержит времени, ID навыка или UUID награды. Log.addIpReward сначала делает push в подготовленный массив, затем запускает parent.parent.update полного массива и абсолютного баланса одного пула. isMagic выбирает пул по истинности аргумента до очистки схемой. parent — CharacterData, parent.parent — Actor.

Метод синхронный: Promise update не возвращён и не ожидается. Баланс в подготовленном объекте непосредственно не присваивается. Вызовы при повышении, несколько наград и ручные списания не являются атомарной операцией. Пример обычного повышения при достаточных IP: Log и финальный update могут послать одинаковый абсолютный остаток; это не обязательно двойное списание. При magic payload конфликтуют из-за затенения переменной. Порядок завершения БД здесь не проверялся (issue28).

<a id="manual"></a>
## Ручные поля и списание из строки

Ручные inputs system.improvementPoints, system.magic.magicImprovementPoints и восемь полей system.skillTraining1–4.name/value идут через унаследованную Actor форму. DocumentSheetV2 читает типизированную форму, разворачивает пути, валидирует и ожидает document.update. Это самостоятельные writers без Log.addIpReward и без повышения Skill. Number input обрабатывается ядром и без data-dtype. Форма может не отправиться при отсутствии изменения/редактирования; HTML не доказывает запись в БД.

Соседняя кнопка .saveIpSpending вызывает _saveIpSpending: label берётся из первого DOM input, value из второго. Если строка value<0, она остаётся строкой; иначе умножение на −1 даёт Number. Log получает два аргумента, значит выбран обычный пул. При балансе 10 и вводе '-3' выражение Number+string даёт payload '10-3' до валидации; это исторически проверенная проблема29/200, новое исполнение не заявлено. Обработчик не читает сохранённый skillTrainingN напрямую, не очищает input и не повышает навык; повторный клик снова инициирует списание.

<a id="training"></a>
## Отдельные хранилища уровня

| Данные | Writer / потребитель | Граница |
| --- | --- | --- |
| Actor.system.skills.*.*.value | levelUpSkill; прежний редактор builtin значений; rollSkillCheck/Skill.modifiedValue | IP-повышение привязано к ключам карты |
| Character.skillTraining1–4.name/value | Именованные поля формы; DOM кнопка вызывает Log | Произвольные подпись/сумма, не ссылка на Skill; автоматическое обучение не найдено в module/templates |
| Item типа skill: system.value | Отдельная SkillItemData, чтение rollCustomSkillCheck | Общего автоматического IP writer в проверенной области нет; generic Item inline handler не является системой развития |
| Item профессии: definingSkill/девять слотов .level | Прежние редактор/inline маршруты .028; roll/threshold/attack/usage .029 | Поле level не смешивается с builtin Skill.value и IP |

Legacy customSkills.hbs:17 имеет inline поле Item.system.value и общий обработчик itemMixin:128–146; это условный legacy маршрут, не доказательство подключения этой формы к текущему листу. Текущий skill-item-sheet.hbs редактирует имя и attribute, не value; текущий custom-skill-display имеет ранее описанную границу контекста. Здесь не вводится новый процесс повышения Item.

Character и Monster могут разделять HBS, но CharacterData определяет IP/logs/training, а MonsterData этих полей не добавляет. Видимая вкладка не обеспечивает модели/метода logs (issues30/192). Сам по себе partial-граф не доказывает отсутствие внешнего макроса или иной автоматизации.

<a id="rewards"></a>
## Выдача IP через API

.manualIpReward → WitcherCharacterSheet._addIpReward → actor.rewardsMixin.addIpReward → game.api.rewards.ip([this]) → Rewards.handoutIpRewards. Первые два wrappers не возвращают и не ожидают дочерние операции. API зарегистрирован main.init; handout явно обращается к Rewards.ipRewardDialog, поэтому не зависит от this=Rewards.

| Этап | Фактическое поведение |
| --- | --- |
| Права | handout сразу возвращается для !game.user.isGM. Прямой ipRewardDialog сам GM не проверяет и награду не выдаёт |
| Получатели | Если actors falsy, getPlayerActors фильтрует game.actors по hasPlayerOwner; явный [] остаётся пустым. helper.getInteractActor/getActorOwner здесь не вызываются |
| Форма | Все предложенные UUID выбраны; multi-checkbox возвращает уникальный массив строк. label текст, ip Number/null, isMagic Boolean. createLabeledInput не задаёт min/max/required |
| Закрытие | await DialogV2.input; default rejectClose=false возвращает null. Guard handout также останавливает отсутствие actors и пустой выбор |
| Разрешение | fromUuidSync каждого UUID после окна без проверки существования, типа или logs |
| Выдача | Только truthy ip: forEach Log.addIpReward без ожидания updates. Отрицательные значения этим условием не запрещены |
| Отчёт | После guard выбора await renderTemplate выполняется даже при 0/null ip; контекст actors,label,ip не содержит isMagic |
| Сообщение | Только truthy ip: ChatMessage.create без await/return. Успешное сообщение не подтверждает успех записи Actor |

hasPlayerOwner означает non-GM OWNER, без проверки активности игрока или типа Actor. Синхронная ошибка получателя прерывает forEach после уже начатых записей; отклонение независимого update не усваивается этим циклом (issues28/233). Числовая типизация DialogV2.input отличается от прямого чтения DOM в _saveIpSpending; строковую проблему200 на форму выдачи не переносим.

## Просмотр истории

CharacterSheet создаёт rewards=new RewardsSheet({document:this.actor}); .open-rewards вызывает rewards?.render(true). RewardsSheet наследует ActorSheetV2 через HandlebarsApplicationMixin; PARTS header/tabs/ip/currency и default вкладка ip. _prepareContext ожидает базовый контекст и передаёт document.system. IP HBS только выводит label/ip/isMagic в порядке массива; form.submitOnChange=true не создаёт отсутствующие поля редактирования. Валютные методы/шаблон и полный lifecycle окна остаются вне .030.

## Источники доказательств

Исходники сопоставлены с относящимися к этой области разделами карточек и позднего аудита R003-07, R004-09/10/11, R008-04, R013-11, а также R014-17/18/19. Прочитаны полные связанные issue4/17/28/29/30/116/149/167/185/191/192/193/200, дополнительно202/232/233/234 для разграничения UI/API/валюты. Их исторические даты, статусы и пределы доказательств сохраняются; новое игровое воспроизведение не заявлено. Эти документы не изменялись.

Установленное ядро Foundry 14.367.0 проверено чтением перечисленных участков. SHA256 фиксирует файл, не запуск клиента или БД.

| Файл | Строки | Контракт | SHA256 |
| --- | --- | --- | --- |
| `/opt/foundryvtt/client/applications/api/dialog.mjs` | 380–426 | DialogV2.input: default callback FormDataExtended.object; default rejectClose=false, close возвращает null. | `4e2d299eaa931d96df1839e64a2defc60b6b95ee89a3e1d32d60b99040899343` |
| `/opt/foundryvtt/client/applications/ux/form-data-extended.mjs` | 168–222 | Number input → Number/null, checkbox без value → Boolean; чтение multi-select. | `0585d07f0ca067969b4dfdde6d187e7d8315abd1cb2dbf9dd55325c003175a01` |
| `/opt/foundryvtt/client/applications/api/document-sheet.mjs` | 431–434,465–469,486–531 | Общий submit: editable, expand/validate, await document.update. | `7925d81900eeea0d5e79606e12ce43539ae00714f50d8452c7305fe81394aa01` |
| `/opt/foundryvtt/client/documents/abstract/client-document.mjs` | 155–173 | hasPlayerOwner: non-GM OWNER без active guard. | `a007180e3cf8d465dffe43b11272f289b4cf77a9e301c7d431f48267dfad8e9e` |
| `/opt/foundryvtt/client/applications/forms/fields.mjs` | 128–156 | createMultiSelectInput type checkboxes → multi-checkbox. | `92e1ac0b69f0c37beeb36d9171146790c4551978e29e4e2ee9f0d0190d316202` |
| `/opt/foundryvtt/client/applications/elements/multi-select.mjs` | 35–65,100–123,324–410 | Set выбранных строковых UUID, value массив; checkbox select/unselect. | `37f6b19705a81f27744dcd1732cdfac1041abc5631ab86e7cfca4e5e94d92c41` |

## Процессы

<a id="proc-000417"></a>
### proc-000417 — Повышение builtin навыка: цена, журнал и отдельный update

Ключ из edit-skills, не имя Item и не строка training.

Шаги: click → lookup → magic → partial → magic-log → ordinary → update. Условия ветвления, await/scheduled и выходы — в JSONL.

<a id="proc-000418"></a>
### proc-000418 — Запись IP в Log и выбранный пул Actor

Sync helper изменяет prepared массив раньше внешней записи.

Шаги: push → pool → ordinary → magic. Условия ветвления, await/scheduled и выходы — в JSONL.

<a id="proc-000419"></a>
### proc-000419 — Ручные обычные IP и четыре строки обучения

Изменение именованной Actor формы; Log и levelUp не вызываются.

Шаги: input → submit. Условия ветвления, await/scheduled и выходы — в JSONL.

<a id="proc-000420"></a>
### proc-000420 — Ручной магический пул IP

Изменение именованной Actor формы; Log и levelUp не вызываются.

Шаги: input → submit. Условия ветвления, await/scheduled и выходы — в JSONL.

<a id="proc-000421"></a>
### proc-000421 — Строка обучения: ручное списание обычных IP

Клик читает DOM соседей независимо от текущего source training.

Шаги: siblings → log. Условия ветвления, await/scheduled и выходы — в JSONL.

<a id="proc-000422"></a>
### proc-000422 — Ручная IP-награда: лист → Actor → API

GM guard расположен ниже в handout; оба wrappers не ожидают результат.

Шаги: sheet → actor. Условия ветвления, await/scheduled и выходы — в JSONL.

<a id="proc-000423"></a>
### proc-000423 — Форма IP-награды: получатели и типы ввода

Общий сбор формы не проверяет GM; handout делает это до вызова.

Шаги: actors → form → input → result. Условия ветвления, await/scheduled и выходы — в JSONL.

<a id="proc-000424"></a>
### proc-000424 — IP-награда: GM, выбор, журналы и чат

Разделены ожидание окна/render и не ожидаемые update/create.

Шаги: gm → selection → grant → render → chat. Условия ветвления, await/scheduled и выходы — в JSONL.

<a id="proc-000425"></a>
### proc-000425 — Просмотр истории IP в RewardsSheet

render окна не начисляет награды и не редактирует записи IP.

Шаги: open → context → list. Условия ветвления, await/scheduled и выходы — в JSONL.

## Проверки

Проверены все 255 тестовых методов в 29 модулях и 769 примеров CLI, включая 36 новых по IQ-01–IQ-08; ошибок в итоговых результатах нет. Исторические проверки выполняются на предусмотренных прежними тестами срезах. Это проверки справочника по исходникам, без запуска игрового сценария. Перекрёстно сверены исходные адреса/владельцы, оба конца отношений, readers/writers, ветви и выходы, refs/facets/роли. [Протокол](review-log.md#task-0006030). Следующая — [TASK-0006.031](../../tasks/task-0006.031.md); родитель in-progress.