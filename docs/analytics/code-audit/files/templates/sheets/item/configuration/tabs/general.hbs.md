# templates/sheets/item/configuration/tabs/general.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/sheets/item/configuration/tabs/general.hbs](../../../../../../../../../templates/sheets/item/configuration/tabs/general.hbs) |
| Тип файла | Handlebars, HTML-шаблон |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `07237960627bf7debc2b4283aa55d1a8c5d1bb8b` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.011](../../../../../../../../tasks/task-0003.011.md), одна порция из семи файлов |
| Запись перекрёстной сверки | [TASK-0003.011](../../../../../../review-log.md#task-0003011) |

## Назначение файла

Выводит общие настройки вариантов атаки, навыков, бонусов, типа урона и защиты, если соответствующие поля существуют в схеме Item.

## Условия использования

PARTS.general в базовой конфигурации. Наследники могут заменить эту часть: Armor и Spell используют свои general-шаблоны; у WitcherPropertiesConfigurationSheet, применяемого к оружию, сохраняется этот файл. Контекст tabs приходит из ApplicationV2, systemFields/item/config — из WitcherConfigurationSheet. Проверка 22 схем — проверка совместимости путей, а не утверждение, что все 22 типа фактически показывают именно этот шаблон.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| section.tab[data-group=primary][data-tab=general] | 1/45 | Тело вкладки | tabs.general.cssClass | Визуальное состояние задаётся общим TABS |
| attackOptions + melee-ветвь | 2–15 | Виды атаки, meleeAttackSkill, applyMeleeBonus | При наличии поля и Set.has('melee') | formGroup по реальной схеме |
| ranged-ветвь | 16–26 | rangedAttackSkill, applyRangedMeleeBonus, isThrowable | Set.has('ranged') | Формы навыка, бонуса и метательного свойства |
| spell-ветвь | 27–35 | spellAttackSkill | Set.has('spell') | Заголовок использует ranged; ветви itemUse нет |
| damageType / defenseOptions | 37–44 | Тип урона и виды защиты | Каждое поле проверяется отдельно | formGroup с конфигурационными списками |

## Основные функции и методы

JavaScript-функций нет. Шаблон вычисляет условия Handlebars и создаёт разметку; обработчики и запись документов принадлежат указанным ниже файлам.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| systemFields/item/config/tabs | [module/item/sheets/configurations/WitcherConfigurationSheet.js](../../../../../../../../../module/item/sheets/configurations/WitcherConfigurationSheet.js); Foundry ApplicationV2 | Контекст | 1–42 | Сверено с _prepareContext и TABS |
| attackOptions, meleeAttackSkill, rangedAttackSkill, spellAttackSkill, applyMeleeBonus, applyRangedMeleeBonus, isThrowable | [module/data/item/templates/combat/attackOptionsData.js](../../../../../../../../../module/data/item/templates/combat/attackOptionsData.js) | Поля схемы | 2–35; фабрика входит в Weapon/Spell | Формы сверены с настоящими моделями; itemUseAttackSkill объявлен, но не выводится |
| damageType | [module/data/item/spellData.js](../../../../../../../../../module/data/item/spellData.js) | Поле | 37–38 | В Spell поле есть; на реальном Spell-листе general заменён другим шаблоном |
| defenseOptions | [module/data/item/templates/combat/defenseOptionsData.js](../../../../../../../../../module/data/item/templates/combat/defenseOptionsData.js) | Поле схемы | 40–43; включено в Weapon/Spell/Hex/Ritual | Настоящие схемы проверены |
| config.attackOptions/meleeAttackOptions/rangedAttackOptions/spellAttackOptions/damageTypes/defenseOptions | [module/setup/config.js](../../../../../../../../../module/setup/config.js) | Списки выбора | 4,11,21,32,38,42 | Имена и четыре attackOptions сверены |
| has(value,set) | [module/setup/handlebars.js](../../../../../../../../../module/setup/handlebars.js) | Helper | 6,16,27; вызывает set.has | Исполнен исходный helper с настоящим Set |
| formGroup | Foundry14.367 /opt/foundryvtt/client/applications/handlebars.mjs; /opt/foundryvtt/common/data/fields.mjs | Helper/схема | Рендерит пути fieldPath и значения | Настоящий helper, toFormGroup заменён фасадом регистрации полей |
| WITCHER.Attack.attackOptions.melee/ranged | [lang/en.json](../../../../../../../../../lang/en.json); [lang/ru.json](../../../../../../../../../lang/ru.json) | Локализация | 7,17,28 | У третьего раздела ranged вместо существующего spell |
| getItemAttack / проверка attack.skill | [module/item/witcherItem.js](../../../../../../../../../module/item/witcherItem.js); [module/actor/mixins/weaponAttackMixin.js](../../../../../../../../../module/actor/mixins/weaponAttackMixin.js) | Потребление настроек | Выбранный attackOption → <option>AttackSkill | Исходные методы: itemUse без навыка останавливается до броска |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/item/sheets/configurations/WitcherConfigurationSheet.js](../../../../../../../../../module/item/sheets/configurations/WitcherConfigurationSheet.js) | Шаблон general | PARTS.general:36 | Прямой путь |
| [module/item/sheets/configurations/WitcherPropertiesConfigurationSheet.js](../../../../../../../../../module/item/sheets/configurations/WitcherPropertiesConfigurationSheet.js) | Унаследованный PARTS.general | WitcherWeaponSheet открывает это окно | Точечная сверка наследования |
| [module/item/sheets/configurations/WitcherArmorConfigurationSheet.js](../../../../../../../../../module/item/sheets/configurations/WitcherArmorConfigurationSheet.js); [module/item/sheets/configurations/WitcherSpellConfigurationSheet.js](../../../../../../../../../module/item/sheets/configurations/WitcherSpellConfigurationSheet.js) | Имя general, но другой шаблон | Переопределение PARTS.general | Не считаются прямыми рендерами этого файла |

## Данные и изменения состояния

В шаблоне 9 различных вызовов formGroup. Имена контролов берутся из schema.fieldPath; данные идут через стандартную форму ItemSheetV2. На модели Weapon с включёнными всеми вариантами найдено 8 полей, на Spell — 9 с damageType, на Hex/Ritual — по 1 defenseOptions, на остальных 18 зарегистрированных схемах — 0. Отсутствующая секция для itemUse не мешает выбрать сам вариант в attackOptions; это оставляет разрыв перед чтением itemUseAttackSkill. Собственных ограничений чисел или записи здесь нет.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Пути/условия | Настоящие схемы 22 Item и Set всех четырёх видов атаки; исходный has/formGroup | Полей Weapon8, Spell9, Hex1, Ritual1, остальные0; itemUseAttackSkill не создан | toFormGroup — фасад; тест каждой схемы не равен реальному выбору шаблона её листом |
| Подписи | Handlebars с ru.json | melee=Ближний бой; ranged и spell-разделы оба Дальний бой | Полный браузер не запускался |
| Потребитель itemUse | getItemAttack + начало weaponAttack на WeaponData | attackOption=itemUse, skill отсутствует, уведомление Атакующий навык не настроен | Броски/данные мира не выполнялись |

## Непроверенные участки и открытые вопросы

Все 45 строк прочитаны. Полноценные select/multi-select контролы и сохранение Set через браузер не исполнялись; исходник formGroup и поля использованы, DOM построения поля заменён. Расширенные свойства конкретных Item и профессиональные атаки остаются будущим порциям.

## Связанные проблемы

[issue-00061](../../../../../../../../issues/potential/issue-00061.md) — отсутствует выбор навыка itemUse; [issue-00062](../../../../../../../../issues/potential/issue-00062.md) — заголовок spell подписан ranged.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.011 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.

## Уточнение TASK-0003.012

2026-09-10, `d20d821e3a8a0a989ec503b0e97413a5a1431ad9`; исходник не изменён. Полный разбор схем [attackOptions](../../../../../../../../../module/data/item/templates/combat/attackOptionsData.js) и [defenseOptions](../../../../../../../../../module/data/item/templates/combat/defenseOptionsData.js) подтвердил пути formGroup. UI options не являются schema choices. Отдельный applyRangedMeleeBonus сохраняется полем, но расчёт его не читает ([issue-00066](../../../../../../../../issues/potential/issue-00066.md)). Для spell default задан spellcasting, отсутствующий в skillMap; это отдельная [issue-00064](../../../../../../../../issues/potential/issue-00064.md), помимо ранее описанных подписи spell и отсутствия itemUse.

Результат и границы — [сверка TASK-0003.012](../../../../../../review-log.md#task-0003012).
