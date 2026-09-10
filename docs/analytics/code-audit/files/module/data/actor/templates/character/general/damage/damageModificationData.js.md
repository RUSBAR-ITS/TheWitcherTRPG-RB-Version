# module/data/actor/templates/character/general/damage/damageModificationData.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/data/actor/templates/character/general/damage/damageModificationData.js](../../../../../../../../../../../module/data/actor/templates/character/general/damage/damageModificationData.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `17eeb6ae9efccf7474b9ca1845b9ab6370671a26` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.004](../../../../../../../../../../tasks/task-0003.004.md), одна порция из восьми файлов |
| Запись перекрёстной сверки | [TASK-0003.004](../../../../../../../../review-log.md#task-0003004) |

## Назначение файла

Определяет тройку параметров изменения входящего урона одного типа: flat, multiplication, applyAP. Реальную семантику задают обработчики Actor; фабрика создаёт только поля.

## Условия использования

При импорте локальная const fields получает foundry.data.fields. Файл экспортирует фабрику определения схемы; значениями экземпляра и валидацией занимается Foundry, а не сама фабрика. damageTypeModification() вызывает damageModification() семь раз и вкладывает каждый результат в SchemaField. Несмотря на каталог character/general/damage, конечный путь — system.damageTypeModification.<тип>.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| fields | const, 1 | Классы полей | Локальная | Читается фабрикой |
| damageModification | function, 3–9 | Определение одного набора | Default export | Три новых поля при вызове |
| flat | NumberField, 5 | Числовой параметр добавки | Вложенное поле типа | initial=0; min/max/integer не заданы |
| multiplication | NumberField, 6 | Числовой коэффициент | Вложенное поле типа | initial=1; min/max/integer не заданы |
| applyAP | BooleanField, 7 | Флаг обработки бронебойности | Вложенное поле типа | initial=false; код применения вне фабрики |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| damageModification(); 3–9 | Доступен foundry.data.fields | {flat:NumberField,multiplication:NumberField,applyAP:BooleanField} | Создаёт новые определения полей при каждом вызове | Синхронно; без записи документов, обработчиков событий и собственного catch |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| NumberField, BooleanField | Foundry 14.367.0, /opt/foundryvtt/common/data/fields.mjs | Глобальный API | 1,5–7 | Настоящая модель; NumberField defaults:1489–1498 |
| Локальные импорты | Отсутствуют | — | Не выполняет расчёт урона и не подключает обработчики | Все 9 строк |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/data/actor/templates/character/general/damage/damageTypeModificationData.js](../../../../../../../../../../../module/data/actor/templates/character/general/damage/damageTypeModificationData.js) | damageModification() | Семь SchemaField | Импорт 1, вызовы 7–13 |

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/data/actor/commonActorData.js](../../../../../../../../../../../module/data/actor/commonActorData.js) | damageTypeModification() | SchemaField на system.damageTypeModification | Импорт 9; вызов 49 |
| [module/data/actor/characterData.js](../../../../../../../../../../../module/data/actor/characterData.js); [module/data/actor/monsterData.js](../../../../../../../../../../../module/data/actor/monsterData.js) | Общий блок семи типов | Наследование CommonActorData, spread super.defineSchema() | Обе defineSchema:10–14 / 8–11 |
| [module/activeEffect/mixins/baseMixin.js](../../../../../../../../../../../module/activeEffect/mixins/baseMixin.js) | Ключи типов и flat/multiplication/applyAP | getDamageModifcators строит три пути на ключ; getActiveEffectsBasePaths включает их | 10,145–171 |
| [module/activeEffect/WitcherActiveEffectSheet.js](../../../../../../../../../../../module/activeEffect/WitcherActiveEffectSheet.js) | Пути мастера | wizardAction вызывает getActiveEffectsBasePaths для base; добавляет key в changes | 59–96; приложение mixin:140 |
| [module/actor/mixins/damageUtilMixin.js](../../../../../../../../../../../module/actor/mixins/damageUtilMixin.js) | flat/multiplication/applyAP | getFlatDamageMod и getMultiDamageMod читают выбранный damage.type | 3–16 |
| [module/actor/mixins/damageMixin.js](../../../../../../../../../../../module/actor/mixins/damageMixin.js) | flat и коэффициент через calculateArmorResistances | calculateDamageWithLocation вызывает getter flat и обработку сопротивлений | 200–214 |
| [module/actor/mixins/armorMixin.js](../../../../../../../../../../../module/actor/mixins/armorMixin.js) | multiplication/applyAP через getMultiDamageMod | calculateArmorResistances вызывает getter; множитель применяется внутри двух веток брони | 206–227 |
| [module/actor/witcherActor.js](../../../../../../../../../../../module/actor/witcherActor.js) | Методы mixin на Actor | Object.assign связывает damageMixin/damageUtilMixin/armorMixin | 440–441,449 |

Поиск выполнен по именам файлов/экспортов, полным и относительным путям данных в module/, templates/ и packsJson/. В 226 JSON-компедиумах строковых путей, начинающихся с system.general или system.damageTypeModification, не найдено. Содержимое действующих БД packs и внешние макросы не проверялись.

## Данные и изменения состояния

Фабрики хранят параметры без собственных вычислений. Применение установлено по конкретной цепочке:

| Поле | Чтение | Фактическое применение |
| --- | --- | --- |
| flat | getFlatDamageMod(damage) по damage.type; нет типа → 0 | После вычитания SP и проверки полного блокирования calculateDamageWithLocation добавляет отдельный DamageInstance только при flat>0. Затем применяется коэффициент локации. Отрицательное значение не уменьшает урон; созданный экземпляр имеет type=null. |
| multiplication | getMultiDamageMod(damage) по damage.type; нет типа → 1 | calculateArmorResistances умножает только в успешных ветках сопротивления надетой/естественной брони: floor(0.5 × damage × multiplication). Без сопротивлений брони не применяется; при обеих ветках применяется дважды. |
| applyAP | getMultiDamageMod проверяет флаг выбранного типа | При true пытается читать damage.damageProperties.armorPiercing/improvedArmorPiercing, хотя вызывающий код передаёт damage.properties. На обычном входе без AP воспроизведён TypeError. При AP calculateArmorResistances возвращает экземпляр до вызова getter, независимо от флага. |

Getter flat вызывается для общего damage.type, а не каждого damageInstance.type. Аналогично множитель выбирается по damage.type; у сопротивлений надетой брони проверяется тип экземпляра, у естественной — тип общего damage. Это зафиксированные обращения, а не предложенная архитектура. Сами getters ничего не сохраняют; calculateArmorResistances меняет переданный instance.damage в памяти. Сохранение HP находится дальше в damageMixin и здесь не воспроизводилось.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Defaults и диапазоны | Реальные Common/Character/MonsterData | У семи типов {flat:0,multiplication:1,applyAP:false}; отрицательные и дробные числа принимаются | Не проверяет игровой смысл |
| Мастер ↔ схема | Исходный getDamageModifcators с подменой i18n и родителей | 21 путь Actor и Item внутри Actor; все найдены в схеме. Для самостоятельного Item — 0 | Окно, выбор и запись ActiveEffect не выполнялись |
| applyAP ↔ реальный контракт damage | Исходные calculateArmorResistances/getMultiDamageMod | true и properties без AP → TypeError; AP-вход → возврат damage=10 | Без полного боя |
| multiplication ↔ сопротивления | Урон 10, multiplication=0.5, applyAP=false | Без брони 10; только надетая 2; только естественная 2; обе 0 | Модель брони подменена объектами; её правила отдельно не оценивались |
| flat ↔ calculateDamageWithLocation | Исходный метод, SP=0, torso×1, брони нет; запись SP подменена | flat=-3/0/+3 → массивы урона [10]/[10]/[10,3] | Нет реального урона, чата, износа, серебра и прочих веток |

## Непроверенные участки и открытые вопросы

Полностью прочитан исходник и точечно проверены определения и потребители перечисленных связей. Мир, браузер, сохранение форм и применение реального ActiveEffect не запускались. Полный анализ соседних файлов остаётся их порциям; просмотр связи не повышает их статус в реестре. Для flat<0 и самостоятельного множителя ожидаемую механику нужно подтвердить до выбора исправления; schema/подпись мастера не заменяют правила.

## Связанные проблемы

[issue-00025](../../../../../../../../../../issues/potential/issue-00025.md) — неверный путь при applyAP. [issue-00026](../../../../../../../../../../issues/potential/issue-00026.md) — множитель зависит от двух веток сопротивления брони. [issue-00027](../../../../../../../../../../issues/potential/issue-00027.md) — отрицательный flat игнорируется. Все остаются potential; не являются исправлениями или согласованными изменениями правил.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.004 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.
