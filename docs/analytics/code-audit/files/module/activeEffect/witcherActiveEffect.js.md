# module/activeEffect/witcherActiveEffect.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/activeEffect/witcherActiveEffect.js](../../../../../../module/activeEffect/witcherActiveEffect.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `a33bf33add228ae93f96a52046c8feb4ee992921` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.009](../../../../../tasks/task-0003.009.md), одна порция из восьми файлов |
| Запись перекрёстной сверки | [TASK-0003.009](../../../review-log.md#task-0003009) |

## Назначение файла

Определяет системный класс документа ActiveEffect: подавление эффекта, признаки временного улучшения, подготовку начала длительности и замену маркера навыка при создании, выбор фазы изменений при обновлении.

## Условия использования

Класс регистрируется как `CONFIG.ActiveEffect.documentClass` при init. Наследует клиентский `ActiveEffect` Foundry; собственный код не является общим вычислителем бонусов: применение `system.changes` выполняет ядро в процессе подготовки Actor/Item. Полный интерфейс настройки, включая wizard, относится к TASK-0003.010. Прямых ES-import нет; глобальные Foundry API необходимы уже при загрузке модуля.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| WitcherActiveEffect | default export, строка 3 | Документ эффекта | CONFIG.ActiveEffect.documentClass | Создание, подготовка, обновление через ядро |
| DialogV2 | Локальная константа, строка 1 | Ссылка на foundry.applications.api.DialogV2 | Не экспортируется | Ожидание выбора навыка |
| Четыре геттера и три async-метода | Строки 4–119 | Поведение экземпляра | Прототип класса | См. полную таблицу ниже |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| isSuppressed; 4–16 | Родитель с system; системные флаги | Boolean | true при parent.system.isActive=false, equipped=false или любом из applySelf/applyOnTarget/applyOnHit/applyOnDamage=true | Синхронно; parent без проверки. Не вызывает super.isSuppressed |
| isDisabled; 18–20 | disabled, необязательный parent.system.equipped | Boolean | disabled либо отсутствие equipped при значении по умолчанию true | Геттер для интерфейсной категоризации; не заменяет core active |
| isAppliedTemporaryItemImprovement; 26–28 | system.isTransferred | Значение поля | Возвращает признак уже переданного улучшения | Не проверяет type и корневой transfer |
| isTemporaryItemImprovement; 30–32 | type | Boolean | Сравнивает с temporaryItemImprovement | Не проверяет disabled, transfer или isTransferred |
| _preCreate; 39–71 | data, options, user; super._preCreate | false при запрете родителя, иначе undefined | При Actor-родителе или isTransferred и уже существующем start.combat.started уточняет combatant/длительность; затем последовательно выбирает навыки для ключей с @skill | await super и chooseSkill; updateSource меняет источник до сохранения; отмена выбора отклоняет Promise |
| chooseSkill; 73–107 | Изменяемая строка change; CONFIG.WITCHER.skillMap | undefined после выбора | Строит options по label, рендерит wizard, получает form.elements.path.value и присваивает change.key | await renderTemplate и DialogV2.prompt; rejectClose=true; остальные поля change не меняет |
| _preUpdate; 110–119 | Частичный data; options, user | false при запрете super, иначе undefined | phase=final только при истинном data.system.applyAfterCalculations, иначе initial; присваивает фазу всем data.system.changes | Не проверяет наличие changes внутри system; не читает прежнее значение флага; см. issue-00043 |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| ActiveEffect, active, isTemporary, isExpiryTrackable, _preCreate/_preUpdate | Внешнее ядро: /opt/foundryvtt/client/documents/active-effect.mjs; BaseActiveEffect: /opt/foundryvtt/common/documents/active-effect.mjs | Наследование | Подготовка документа, вычисление активности, схема и старт Actor-эффекта | Проверены соответствующие тела Foundry 14.367.0 |
| Поля system и changes | [module/data/activeEffects/witcherActiveEffectData.js](../../../../../../module/data/activeEffects/witcherActiveEffectData.js); [module/data/activeEffects/witcherTemporaryItemImprovementData.js](../../../../../../module/data/activeEffects/witcherTemporaryItemImprovementData.js) | Типовые модели | Чтение флагов и исходных изменений | Модели зарегистрированы отдельно; changes наследуется от ядра |
| Actor, Combat.getCombatantsByActor | Внешние foundry.documents.Actor и /opt/foundryvtt/client/documents/combat.mjs | instanceof, вызов метода | Поиск combatant по this.parent | Метод ожидает Actor или его ID; переданный Item не превращает в его Actor |
| skillMap | [module/setup/config.js](../../../../../../module/setup/config.js) | Глобально через CONFIG.WITCHER | label, attribute.name и ключ навыка превращаются в system.skills.<группа>.<ключ>.activeEffectModifiers | 52 варианта в изолированном вызове; reduce индексирует по label |
| DialogV2.prompt, renderTemplate, game.i18n.localize | Внешний Foundry API | UI и локализация | Выбор навыка; group локализуется как WITCHER.skills.name | Подменены в проверке, браузер не запускался |
| Шаблон выбора | [templates/dialog/activeEffects/wizard.hbs](../../../../../../templates/dialog/activeEffects/wizard.hbs) | Путь renderTemplate | Контекст selects и поле path | Исходный шаблон принимает selectOptions; полный разбор отложен |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/TheWitcherTRPG.js](../../../../../../module/TheWitcherTRPG.js) | WitcherActiveEffect | Импорт и регистрация documentClass при init | Прямое присваивание CONFIG.ActiveEffect.documentClass |
| [module/actor/sheets/mixins/activeEffectMixin.js](../../../../../../module/actor/sheets/mixins/activeEffectMixin.js) | isDisabled, isTemporaryItemImprovement, isAppliedTemporaryItemImprovement | Категоризация эффектов для листа | prepareActiveEffectCategories |
| [module/item/witcherItem.js](../../../../../../module/item/witcherItem.js) | isAppliedTemporaryItemImprovement | Выделение переданных улучшений из коллекции эффектов | Собственный маршрут Item, описанный в TASK-0003.008 |
| [module/scripts/temporaryEffects/applyActiveEffect.js](../../../../../../module/scripts/temporaryEffects/applyActiveEffect.js); [module/actor/mixins/temporaryEffectMixin.js](../../../../../../module/actor/mixins/temporaryEffectMixin.js) | Документы и hooks создания | Клонирование в Actor либо создание в выбранном оружии | Разные родители влияют на start и suppression |
| [module/actor/witcherActor.js](../../../../../../module/actor/witcherActor.js); [module/actor/sheets/WitcherActorSheet.js](../../../../../../module/actor/sheets/WitcherActorSheet.js); [module/actor/sheets/WitcherActorSheetV1.js](../../../../../../module/actor/sheets/WitcherActorSheetV1.js) | isAppliedTemporaryItemImprovement | Добавление эффектов Item в перечни для Actor/листа | temporaryEffects и подготовка данных листов |
| [module/item/sheets/configurations/WitcherConfigurationSheet.js](../../../../../../module/item/sheets/configurations/WitcherConfigurationSheet.js); [templates/sheets/activeEffect/system-specific.hbs](../../../../../../templates/sheets/activeEffect/system-specific.hbs) | isTemporaryItemImprovement, isAppliedTemporaryItemImprovement | Категория улучшений и доступность полей формы | Связанные ветви интерфейса, полный разбор в последующих порциях |
| [templates/partials/effect-part.hbs](../../../../../../templates/partials/effect-part.hbs) | isSuppressed | Условие отображения строки при наличии @root.actor | unless (and effect.isSuppressed @root.actor) |
| Ядро Actor/Item Foundry | active и hooks | Подготовка effects и фаз changes; сохранение документов | Клиентские документы Actor, Item, ActiveEffect |

## Данные и изменения состояния

`disabled`, `transfer`, `type`, `start`, `duration`, `statuses` — корневые поля ядра; `apply*` и `isTransferred` — поля типовых моделей. `isTransferred` не является копией `transfer`: первое отмечает результат передачи улучшения, второе участвует в перечислении применимых эффектов Item ядром.

При создании в начатом бою выбирается первый combatant. Для `units=rounds` и expiry turnStart/turnEnd значение уменьшается на один, если ход цели впереди текущего, либо это текущий ход и expiry=turnEnd. Для уже прошедшего хода уменьшения нет; прочие units/expiry не обрабатываются. Условия не создают `start` из null. Временное улучшение на Item передаёт сам Item в getCombatantsByActor; этот поиск не находит combatant его владельца.

Изменение с `@skill` получает целиком новый ключ; замены подстроки нет. Источник `_source.system.changes` изменяется до сохранения. При обновлении фаза берётся из переданного payload, а не из текущей модели; это существенно для частичных update.

Переопределённый isSuppressed не учитывает core `duration.expired` и `system.isSuppressed`. Это не доказывает, что все эффекты бессрочны: effect-registry ядра отдельно обрабатывает отслеживаемые эффекты, а система задаёт expiryAction=delete. Для Item-улучшения со start=null проверка isExpiryTrackable даёт false; см. issue-00050.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Полнота | Полное чтение 120 логических строк; поиск регистраций и геттеров в module/templates | 4 геттера, 3 async-метода; импортов нет | Зависимости за пределами порции прочитаны по связанным участкам |
| Активность | Исходные геттеры + core active, подменённые parent/system | Обычный активен; disabled/неэкипированный/неактивный родитель и apply-флаги дают разные active/isDisabled; expired сам по себе не подавляет | Не запускался общий scheduler мира |
| Фаза update | Исходный _preUpdate с разрешающим super | name-only проходит; system без changes вызывает TypeError; changes-only при прежнем true получает initial; changes+true — final | Полная форма UI не проверялась |
| Начало боя | Матрица turnNumber=0/1/2, текущий ход=1, value=2, обе expiry | Итоговые длительности 2/2/2/1/1/1; Item не получает combatant; start=null остаётся null | Actor/Combat-контекст подменён; тело getCombatantsByActor взято из ядра |
| Выбор навыка | Исходный chooseSkill и карта системы, подмены renderTemplate/prompt | 52 варианта; @skill заменён выбранным путём swordsmanship; отмена отклоняет Promise | Нет проверки реального диалога |

## Непроверенные участки и открытые вопросы

Не выполнялись создание/обновление в мире, полный клиентский жизненный цикл и истечение реальных длительностей. Родитель без system и неembedded-документы требуют отдельной проверки; допустимость таких документов в ядре не означает их корректную поддержку этим геттером. Поля wizard и возможность задания произвольной строки changes подробно проверяются в следующей порции.

## Связанные проблемы

[issue-00043](../../../../../issues/potential/issue-00043.md) — частичные обновления и фазы. [issue-00050](../../../../../issues/potential/issue-00050.md) — start и контекст владельца временного улучшения. Связанный маршрут копирования: [issue-00044](../../../../../issues/potential/issue-00044.md). Все карточки остаются potential; код не исправлялся.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.009 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.

## Уточнение TASK-0003.010

2026-09-10, `247d3d86e344238a1445377c686eb6455146693c`; исходник прежнего среза не изменён.

[templates/dialog/activeEffects/wizard.hbs](../../../../../../templates/dialog/activeEffects/wizard.hbs) имеет два потребителя: chooseSkill при создании заменяет key одной записи, [module/activeEffect/WitcherActiveEffectSheet.js](../../../../../../module/activeEffect/WitcherActiveEffectSheet.js) при редактировании добавляет выбранные пути как новые changes. Шаблон содержит только select, без величины/режима/ограничения характеристики. Корневой update({changes}) мастера мигрируется ядром в system.changes до _preUpdate; исходный hook затем даёт initial при отсутствии applyAfterCalculations в payload (расширение issue-00043).

[Общая сверка первой серии](../../../review-log.md) — TASK-0003.010. Полный клиент и БД не запускались.

## Уточнение TASK-0003.011

2026-09-10, `07237960627bf7debc2b4283aa55d1a8c5d1bb8b`; содержимое исходника совпадает с предыдущим срезом.

Дополнительно сверены вызывающие участки [основного листа Item](../item/sheets/WitcherItemSheet.js.md) и [конфигурации](../item/sheets/configurations/WitcherConfigurationSheet.js.md). В конфигурации create явно задаёт base/temporaryItemImprovement, не задаёт changes/transfer/units и возвращает Promise создания. При Drop настоящий ItemSheetV2 передаёт effect.toObject() в ActiveEffect.create с parent=item, отказывает при том же родителе или isOwner=false. Эти проверки выполнены с перехватом записи, а не реальным созданием/переносом документов.

[TASK-0003.011 — сценарии и сверка](../../../review-log.md#task-0003011).

## Уточнение TASK-0003.018

2026-09-10, `rusbar-main`, `29319a7a7e1dfc0663edbc15166f3b6a19682a2f`. isSuppressed не содержит отдельной ветви для [race](../../../../../../module/data/item/raceData.js) или [homeland](../../../../../../module/data/item/homelandData.js). Настоящий getter на фасадах родителей обоих типов вернул false без запрещающих полей/флагов и true при applySelf=true. Внешний core Actor.allApplicableEffects собирает Actor.effects и Item.effects с transfer без ограничения по этим типам; actual generator проверен в памяти. active/shouldApplyChange/фазы и числовое применение отдельно прочитаны, но весь pipeline здесь не запускался. Текст особенности расы сам эффектов не порождает.

[Перекрёстная сверка](../../../review-log.md#task-0003018). Исходники не изменены; это уточнение проверенных связей, а не повторный полный разбор файла.
