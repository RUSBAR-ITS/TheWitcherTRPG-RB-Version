# module/data/activeEffects/witcherActiveEffectData.js

## Текущее состояние — 14.3.1.00061

2026-09-18, TASK-0010.003. **Назначение:** Модель base AE и валидация новых настроек.

**Сущности, действия и зависимости:** ModifierChangeField добавляет defaults только числовым строкам; ModifierChangesField поднимает отказ элемента при частичном update. effectIdentityFields/validateEffectIdentity задают общие поля типа, validateModifierChange проверяет сочетания. defineSchema сохраняет пять полей native changes, клонируя их options, и добавляет flags. validateJoint проверяет ID. Зависимости: modifierContext.js и native ActiveEffectTypeDataModel/fields; экспорт identity используют временные улучшения.

[Исходник](../../../../../../../module/data/activeEffects/witcherActiveEffectData.js), [проверки и границы](../../../../../task-0010-003-checks.md). Статическая проверка; игровая приёмка не проводилась. Численный контракт следующих стадий ещё не внедрён.

## Предыдущие датированные проверки

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/data/activeEffects/witcherActiveEffectData.js](../../../../../../../module/data/activeEffects/witcherActiveEffectData.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `a33bf33add228ae93f96a52046c8feb4ee992921` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.009](../../../../../../tasks/task-0003.009.md), одна порция из восьми файлов |
| Запись перекрёстной сверки | [TASK-0003.009](../../../../review-log.md#task-0003009) |

## Назначение файла

Модель system обычного ActiveEffect типа base: наследует список changes ядра и добавляет пять флагов условий/фазы применения. Схема не заменяет документ эффекта и его обработчики.

## Условия использования

При импорте определяется fields и экспортируемый класс. [module/setup/registerDataModels.js](../../../../../../../module/setup/registerDataModels.js) назначает модель CONFIG.ActiveEffect.dataModels.base. Foundry создаёт её как effect.system. Собственная metadata не объявлена; класс прямо наследует ActiveEffectTypeDataModel.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| fields | Константа, 1 | Классы полей Foundry | Локальная | Читается defineSchema |
| WitcherActiveEffectData | Класс, 3–29 | Системные данные эффекта | default export; реестр ActiveEffect | Создаётся ядром |
| changes | Унаследованное поле через ...super.defineSchema() | Массив изменений | effect.system.changes | Определение — в ядре, не повторно в этом файле |
| applySelf | BooleanField, 7 | initial=false, label=WITCHER.Effect.applySelf | effect.system.applySelf | Хранится в данных; само поле ничего не применяет |
| applyOnTarget | BooleanField, 11 | initial=false, label=WITCHER.Effect.applyOnTarget | effect.system.applyOnTarget | Хранится в данных; само поле ничего не применяет |
| applyOnHit | BooleanField, 15 | initial=false, label=WITCHER.Effect.applyOnHit | effect.system.applyOnHit | Хранится в данных; само поле ничего не применяет |
| applyOnDamage | BooleanField, 19 | initial=false, label=WITCHER.Effect.applyOnDamage | effect.system.applyOnDamage | Хранится в данных; само поле ничего не применяет |
| applyAfterCalculations | BooleanField, 23 | initial=false, label=WITCHER.Effect.applyAfterCalculations | effect.system.applyAfterCalculations | Хранится в данных; само поле ничего не применяет |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| WitcherActiveEffectData.defineSchema; 4–28 | Доступны foundry.data.fields и ActiveEffectTypeDataModel | Объект схемы: changes + 5 BooleanField | Расширяет ...super.defineSchema; собственных lifecycle-методов нет | Синхронно; не пишет документы |

Общая схема ядра Foundry 14.367.0 `/opt/foundryvtt/common/data/active-effect.mjs:15–26`: changes — ArrayField(SchemaField), ключи key:StringField(required), type:StringField(required, blank=false, initial='add'), value:AnyField(required, nullable, serializable, initial=''), phase:StringField(required, blank=false, initial='initial'), priority:NumberField без собственного initial. В изоляции у записи с key заданным и прочими полями по умолчанию priority был undefined и не попал в JSON. Тип проверяется на допустимый формат строки, а не на существование обработчика конкретной операции. DefaultPriority позже заполняет core ActiveEffect.prepareBaseData по change.type.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| ActiveEffectTypeDataModel / defineSchema | Foundry 14.367.0; common/data/active-effect.mjs | Наследование, super | changes и его схема/валидация | Исходное определение прочитано; использована настоящая модель |
| foundry.data.fields.BooleanField | Foundry common/data/fields.mjs | Конструирование | Собственные флаги | Оригинальная схема и начальные значения выполнены |
| Ключи WITCHER.Effect.* | [lang/en.json](../../../../../../../lang/en.json); [lang/ru.json](../../../../../../../lang/ru.json) | Локализация label | Все пять собственных полей имеют label | Ключи заданы в исходнике; в en присутствуют все пять, в ru нет applyAfterCalculations — уточнение TASK-0003.051 ниже |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/setup/registerDataModels.js](../../../../../../../module/setup/registerDataModels.js) | WitcherActiveEffectData | Импорт/назначение реестра | Связь двусторонне уточнена |
| [module/activeEffect/witcherActiveEffect.js](../../../../../../../module/activeEffect/witcherActiveEffect.js) | applySelf, applyOnTarget, applyOnHit, applyOnDamage, applyAfterCalculations | isSuppressed; _preUpdate выбирает phase по applyAfterCalculations | Полный разбор документа в этой порции |
| [module/scripts/temporaryEffects/applyActiveEffect.js](../../../../../../../module/scripts/temporaryEffects/applyActiveEffect.js) | applySelf/applyOnTarget/applyOnHit/applyOnDamage | ViaId читает system[applyWhen]; обычная копия сбрасывает четыре apply-флага | 32–67; схема не выбирает получателя самостоятельно |
| [module/actor/mixins/castSpellMixin.js](../../../../../../../module/actor/mixins/castSpellMixin.js) | applySelf, applyOnTarget | Фильтрация эффектов при успешном заклинании | 253–267; дальнейший маршрут в applyActiveEffect.js |
| [module/actor/mixins/defenseMixin.js](../../../../../../../module/actor/mixins/defenseMixin.js) | applyOnHit | Передаёт имя флага в applyActiveEffectToActorViaId | 399–404 |
| [module/actor/mixins/damageMixin.js](../../../../../../../module/actor/mixins/damageMixin.js) | applyOnDamage | Передаёт имя флага после повреждения | 31–32 |
| [module/item/mixins/consumeMixin.js](../../../../../../../module/item/mixins/consumeMixin.js) | applySelf | Передаёт имя флага при потреблении | 15 |
| [module/activeEffect/WitcherActiveEffectSheet.js](../../../../../../../module/activeEffect/WitcherActiveEffectSheet.js) | system.schema.fields | Контекст systemFields для формы | _prepareContext:39–42; полный разбор — TASK-0003.010 |
| [templates/sheets/activeEffect/system-specific.hbs](../../../../../../../templates/sheets/activeEffect/system-specific.hbs) | Флаги модели | formGroup по системным полям | Интерфейс следующей порции; наличие поля не доказывает его работу |

## Данные и изменения состояния

В файле отсутствуют update/create/delete, броски, Hooks и доступ к Actor. Name, img, disabled, transfer, statuses, origin, start и duration находятся на документе ActiveEffect в ядре. `applyAfterCalculations` — системный флаг уровня эффекта; phase принадлежит каждой записи changes. Согласование этих уровней выполняет WitcherActiveEffect._preUpdate и оно имеет ограничения частичного обновления. Системные флаги по умолчанию false не фильтруют disabled самостоятельно.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Полнота | Полное чтение 29 строк, регистрация, все обращения к флагам | Одна схема; 5 собственных флагов; changes унаследован | Файл не исполняет воздействий |
| Модель Foundry | Оригинальный класс + реальные ActiveEffectTypeDataModel/fields в Node | changes=[]; все флаги false; запись changes получает add/initial/'' | Нет сохранения ActiveEffect в мире |
| Потребители | Класс, маршруты, Actor/Item, листы и шаблоны | Указаны реальные условия/фильтры, а не только наличие свойств | Полный UI следующей порции |

## Непроверенные участки и открытые вопросы

Defaults/схема не доказывают весь submit и доставку; [U005-01](../../../../cross-check-0002.md#u005-01)/[U005-02](../../../../cross-check-0002.md#u005-02). Произвольные поля/версии ядра — [U005-05](../../../../cross-check-0002.md#u005-05), ru/en интерфейс — [U005-07](../../../../cross-check-0002.md#u005-07).

## Связанные проблемы

[issue-00043](../../../../../../issues/closed/issue-00043.md) — обработчик частичного обновления/фаз; [issue-00044](../../../../../../issues/closed/issue-00044.md) — длительность копии задаётся на неверном уровне. Сама схема не исправлялась; статусы potential сохранены.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.009 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.

## Уточнение TASK-0003.010

2026-09-10, `247d3d86e344238a1445377c686eb6455146693c`; исходник прежнего среза не изменён.

Поля полностью сопоставлены с [templates/sheets/activeEffect/system-specific.hbs](../../../../../../../templates/sheets/activeEffect/system-specific.hbs): applyAfterCalculations выводится всегда, остальные четыре — у Item-эффекта. Это параметры целого эффекта; поля key/type/value/phase/priority отдельных строк рендерятся стандартными шаблонами ядра. [module/activeEffect/WitcherActiveEffectSheet.js](../../../../../../../module/activeEffect/WitcherActiveEffectSheet.js) не добавляет схеме ограничений характеристик; мастер лишь добавляет ключи.

[Общая сверка первой серии](../../../../review-log.md) — TASK-0003.010. Полный клиент и БД не запускались.

## Дополнительная сверка TASK-0003.038

2026-09-11, `rusbar-main`, `b47ba02cdaebc6a66ad14a5638213b6eb24460b4`; исходники не менялись.

Профессиональный HP использует ActiveEffect со старым changes/mode ADD. Настоящая core миграция положила change в system.changes и преобразовала mode→type и JSON value; поэтому старая форма changes сама по себе не зарегистрирована как ошибка. Конструктор/клон/сохранение полностью не исполнялись. icon вместо img — отдельная 243.

[module/actor/mixins/professionMixin.js](../../actor/mixins/professionMixin.js.md), [templates/partials/character/tab-profession.hbs](../../../templates/partials/character/tab-profession.hbs.md), [templates/sheets/actor/partials/monster/tabs/tab-profession.hbs](../../../templates/sheets/actor/partials/monster/tabs/tab-profession.hbs.md), [templates/dialog/combat/profession-attack.hbs](../../../templates/dialog/combat/profession-attack.hbs.md).

[Сверка и ограничения](../../../../review-log.md#task-0003038). Связанные файлы повторно в покрытии не учитывались; код и статусы issues не изменены.

## Дополнительная сверка TASK-0003.044

2026-09-12, rusbar-main, 965132d5d7972a0edd73aaa62484a1b6ba15991f; исходники не изменены.

Группа 31 снова исполнила унаследованную схему: system.changes корректен, value — AnyField. Группа 35 связала ранее известную миграцию с [updateDerivedStat](../../actor/mixins/damageMixin.js.md): BaseActiveEffect.migrateData разбирает корневую JSON-строку value в объект; потребитель затем повторно JSON.parse-ит объект и прерывает расход HP (новая 294). Группа 13 также показала запрос applyOnDamage после полного поглощения SP (290). Это поведение потребителей, не ошибка объявления самого флага/поля.

[Методика и пределы проверки](../../../../review-log.md#task-0003044). Уточнение связей не увеличивает покрытие; мир, браузер и БД не запускались.

## Дополнительная сверка TASK-0003.051

2026-09-12, rusbar-main, 4b9951094106e26d9274bbd5d5e8e7a709cfcf24. Исходник не менялся.

Уточнение прежней строки зависимостей: label заданы у пяти собственных полей, но все пять присутствуют только в en. Для applyAfterCalculations ключ WITCHER.Effect.applyAfterCalculations отсутствует в ru. Настоящий класс импортирован поверх ActiveEffectTypeDataModel ядра; label из schema.fields проверен настоящим Localization с fallback. [docs/issues/closed/issue-00318.md](../../../../../../issues/closed/issue-00318.md) описывает перевод, отдельно от issue-00043 о фазах/update. Полные словари: [en](../../../lang/en.json.md), [ru](../../../lang/ru.json.md).

[Результаты и ограничения сверки](../../../../review-log.md#task-0003051). Правки относятся к документации; мир, браузер, БД и исходники не менялись.

## Уточнение TASK-0003.058

2026-09-12; rusbar-main, 5283da15a49422fc339c44add4e7d7d02c174ce4; исходник не изменён.

Все 17 эффектов Simple используют тип base и эту модель. Штатная миграция переносит 55 старых changes в system.changes, mode=2 преобразуется в add, строки значений — в числа, phase получает initial. applyAfterCalculations отсутствует в JSON и становится false.

[Карточки Simple](../../../packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/_Folder.json.md), [протокол, методы и ограничения](../../../../review-log.md#task-0003058). Реальные записи в мир не выполнялись; состояния issues не менялись.

## Уточнение TASK-0003.059

2026-09-13; rusbar-main, d26e3381a7290807b8e76f9817d0f7a603c0e61a; исходник не изменён.

Для Complex подтверждена наследуемая схема system.changes и defaults пяти bool-флагов; все 61 legacy changes стали add/initial с числовыми значениями. Внешние statuscounter flags в фасаде без модуля очищаются ядром; это не проверка поведения установленного модуля.

[Карточки Complex](../../../packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/_Folder.json.md), [протокол и ограничения](../../../../review-log.md#task-0003059). Мир и БД не изменялись.

## Уточнение TASK-0003.060

2026-09-13; rusbar-main, aef03ca01b0db5887653d2b1301a4fe814372a3e; исходник не изменён.

201 Difficult changes штатно мигрируют: 12 multiply чисел, 180 add чисел и девять add объектов; initial, priority=10/20. applyAfterCalculations default=false. Схема не добавляет специальное сложение объекта turnStartEffects: core SchemaField ADD возвращает прежнее значение (issue-00328).

[Карточки Difficult](../../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/_Folder.json.md), [протокол и ограничения](../../../../review-log.md#task-0003060). Мир и БД не менялись.

## Дополнительная сверка TASK-0003.061

2026-09-14; rusbar-main, 1cae095ac2f0f009fb1358a888a7afcf5ea5ec2e. Исходник не изменён.

[Deadly](../../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/_Folder.json.md): четыре исходных системных apply-флага false, applyAfterCalculations отсутствует и получает false. Наследуемая схема сохраняет мигрированные 43 changes в system.changes/initial. Всего 360 изменений пакета: 341 адресует NumberField, 16 — SchemaField, три динамических commonspeech не объявлены. Типизированная схема не делает ADD объекта созданием записи — [issue-00328](../../../../../../issues/closed/issue-00328.md).

[Протокол и ограничения](../../../../review-log.md#task-0003061). Настоящие модели/методы исполнены с явными фасадами окружения и перехватом записи; полный клиентский lifecycle, мир, БД и серверный запуск не проверены.

## Сквозная сверка TASK-0004.005

2026-09-14; rusbar-main, 4686f913501b9c75082e79249364e40934f6a1da. Исходник совпадает со срезом TASK-0001; изменено только описание.

Модель base наследует changes ядра (key/type/value/phase/priority) и добавляет пять BooleanField. Флаги applySelf/Target/Hit/Damage читают suppression и вызывающие маршруты; applyAfterCalculations читается _preUpdate, а не автоматически вычислителем поля. На уровне changes здесь нет галочки потолка, лимита1–10 или общей операции «бонус характеристики». AnyField value допускает мигрированные объекты; их применение зависит от SchemaField/NumberField адресата. В ru отсутствует подпись applyAfterCalculations, core fallback en проверен отдельно (.051/00318).

Сопоставленные определения и потребители: [module/activeEffect/witcherActiveEffect.js](../../activeEffect/witcherActiveEffect.js.md), [module/activeEffect/WitcherActiveEffectSheet.js](../../activeEffect/WitcherActiveEffectSheet.js.md), [templates/sheets/activeEffect/system-specific.hbs](../../../templates/sheets/activeEffect/system-specific.hbs.md), [module/setup/registerDataModels.js](../../setup/registerDataModels.js.md), [lang/en.json](../../../lang/en.json.md), [lang/ru.json](../../../lang/ru.json.md).

[Протокол и границы](../../../../review-log.md#task-0004005) — TASK-0004.005; процессы [R005-01](../../../../cross-check-0002.md#r005-01), [R005-03](../../../../cross-check-0002.md#r005-03), [R005-06](../../../../cross-check-0002.md#r005-06), [R005-12](../../../../cross-check-0002.md#r005-12). В этой порции выполнена статическая сверка; поведенческие опыты принадлежат датированным прежним протоколам, а не новому прогону.
