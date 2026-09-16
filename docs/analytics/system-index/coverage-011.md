# Локализации en/ru — TASK-0006.011

Актуализация 2026-09-16, **issue-00330 / 14.3.1.00007**: выполнены подписи ru/en в 22 исходниках (включая версию system.json), сохранены все прежние ключи; механики и компедиумы исключены. Словари 1163 en / 1162 ru, общих 1160, en-only 3 / ru-only 2. Текущий граф: 5366 сущностей, 15129 отношения, 465 процессов. [Реализация, пофайловые уточнения и проверки](../../issues/open/issue-00330.md#реализация-и-проверки--143100007). Матрицы/протоколы ниже сохраняют исторические результаты; их сообщения об исправленных локализационных дефектах относятся к прежнему срезу.


Срез: 2026-09-15, rusbar-main, HEAD 41fe9cb905534016fc97e2fb06180c9aa5e991c3; Foundry 14.367.0. [Задача](../../tasks/task-0006.011.md), [примеры поиска](examples/expansion-011-queries.json), [манифест](manifest.json).

## Включённая область

1153 английских и 1135 русских строковых листьев: **2288 самостоятельных field**, принадлежащих двум исходникам. Для каждого сохранены runtime key в name, qualified_name с префиксом языка, точный raw JSON Pointer в location.symbol, строка исходника, текст и placeholders в summary. Поисковые aliases содержат подпись и адрес; ключ не помещается в нормализуемый alias, чтобы firstaid/firstAid оставались различимыми при точном поиске. Текст перевода не становится полем Actor.

У en/ru 1133 общих ключа: сопоставление задаётся 1133 отношениями refers из en в ru. Это сравнение словарей, не импорт/вызов fallback. Обратный обход использует то же отношение. В каждом исходнике 63 dotted-имени свойств; raw pointer сохраняет точку внутри имени, а name отражает путь после expandObject. Коллизий развёрнутых листьев и повторных JSON-имён не найдено. Четыре пустых hint в каждом языке остаются найденными строками.

Определения двух словарей — complete **только по строковым ключам**. Отношения и процессы остаются partial/not_indexed по своим аспектам. У JSON нет исполняемых методов: внешняя загрузка не выдана за локальный процесс словаря.

Внесены 496 буквальных мест из 41 файла: выбранные ранее области, строки config.js:1–756 и семь ключей handlebars.js. Файловый refers указывает точное место текста, без угадывания ближайшего метода по широкому диапазону класса/PARTS. Дополнительно прослежены конкретные настройки, metadata BooleanField, карты stats/skills/currency/damageTypes, formGroup, skill.label, tab prefixes, мастер эффектов и оба format-вызова. Отдельно связаны известные отсутствующие Weapon.Availability в tags:14/127. Этот охват не означает полного набора читателей всех 2288 строк и всех методов этих файлов.

Добавлено **2315 сущностей, 4724 отношений, 6 процессов**; накоплено **3323/7395/97**. Определения есть в 154/615 файлах: 2 complete и 152 partial; роли 60 основных/94 смежных, 461 без определений. Внешних/динамических границ 214. Старые ID сохранены; существующие шаги получили только отношения их фактического исполнителя в пределах собственных строк.

## Ключи, различающиеся между языками

20 ключей только en, два только ru. Это состав системных словарей: модули/мир могут дополнять и переопределять их.

| Ключ | Только | Текст |
| --- | --- | --- |
| WITCHER.Actor.deathState.ignore | en | DS |
| WITCHER.Actor.deathState.ignoreHint | en | Ignore Death State penalties when HP is 0 or below. |
| WITCHER.Actor.woundThreshold.ignore | en | WT |
| WITCHER.Actor.woundThreshold.ignoreHint | en | Ignore Wound Threshold penalties when HP is below WT. |
| WITCHER.Actor.woundThreshold.state | en | Wound State |
| WITCHER.Armor.locationLeftArm | en | Left Arm |
| WITCHER.Armor.locationLeftLeg | en | Left Leg |
| WITCHER.Armor.locationRightArm | en | Right Arm |
| WITCHER.Armor.locationRightLeg | en | Right Leg |
| WITCHER.DamageType.silver | en | Silver |
| WITCHER.Dialog.customModifier | en | Custom Modifiers |
| WITCHER.Dialog.savingThrow | en | Performing a saving throw |
| WITCHER.Effect.applyAfterCalculations | en | Apply this active effect after all derived stats were calculated |
| WITCHER.Spell.emanation | en | Emanation |
| WITCHER.deprecations.armorEnhancements.text | en | Armor Enhancements are being reworked. To prevent data loss you need to unattach your enhancements from armors and shields before updating to the next version. Some armors might already be broken, it is best to redo them in the next version. |
| WITCHER.deprecations.armorEnhancements.title | en | Armor Enhancements Rework |
| WITCHER.profession.skillPath.skill.thresholds.hasThresholds | en | Has thresholds |
| WITCHER.profession.skillPath.skill.thresholds.name | en | Name |
| WITCHER.profession.skillPath.skill.thresholds.thresholdValue | en | Threshold |
| WITCHER.skills.levelUp | en | Level up |
| WITCHER.Damage.silver | ru | Серебро |
| WITCHER.Dialog.attackCustom | ru | Модификатор атаки |

Сопоставлено с [R016-20](../code-audit/cross-check-0002.md#r016-20), [R016-21](../code-audit/cross-check-0002.md#r016-21), [R016-22](../code-audit/cross-check-0002.md#r016-22). [issue-00193](../../issues/potential/issue-00193.md) сохраняет позднее уточнение: семь Actor.Skill.* доступны после expandObject. [issue-00317](../../issues/potential/issue-00317.md) — различие DamageType.silver/Damage.silver; [issue-00318](../../issues/potential/issue-00318.md) — ru-label фазы эффекта; [issue-00178](../../issues/potential/issue-00178.md) — Weapon.Availability; [issue-00016](../../issues/potential/issue-00016.md) — регистр CRA labels. [issue-00053](../../issues/potential/issue-00053.md) касается отсутствующего DataField Temporary и отделена от перевода.

## Подстановки и внешний контракт

| Ключ (одинаковый набор en/ru) | Подстановки |
| --- | --- |
| WITCHER.currencyConverter.errors.insufficient | currency |
| WITCHER.Combat.healed | target, heal |

currencyConverter:69–70 передаёт локализованный CONFIG.WITCHER.currency[from] как currency. onHeal:41 передаёт уже вычисленный heal и target.name; actor.name добавляется вне перевода. ChatMessage.create:47 не ожидается.

В установленном ядре localize ищет строку в translations, затем _fallback, затем возвращает ключ. Пустая строка считается найденной. format — alias этого метода; при переданном data производится replace, отсутствующее значение может дать строку undefined. setLanguage загружает core → system → modules → world и отдельно en для языка != en; error загрузки/JSON даёт пустой словарь. Системный manifest только объявляет пути. Состав активных overrides и HTTP здесь не проверялся.

formGroup сначала проверяет field. toFormGroup выбирает label из config/поля/fieldPath; createFormGroup вызывает _loc при localize=true и записывает innerText. Поэтому missing-field и missing-translation — разные ветви. HBS localize передаёт hash в _loc и обычный HBS экранирует результат. Унаследованный EFFECT.TABS + systemSpecific разрешён как точный ключ; WITCHER.St + capitalize(skillKey) и WITCHER.Actor.settings + tab.id остаются динамическими выражениями.

Прочитаны локальные файлы ядра; строки ниже — внешнее доказательство, не шаги игрового JS.

| Файл ядра | Проверенный участок | SHA-256 полного файла |
| --- | --- | --- |
| /opt/foundryvtt/client/helpers/localization.mjs | 226–237; 283–374; 390–445; 481 | 0efd3b6434e772a12ea00bb9fd10d0186f031a0d8d6945a580dd8d809ce8080f |
| /opt/foundryvtt/common/utils/helpers.mjs | 541–556: expandObject | 8f309e7d8c4ace883990bac828aaa156f78b4f22ff4cc35007cfbfed38d8d0c0 |
| /opt/foundryvtt/client/applications/handlebars.mjs | 265–268; 531–546 | 0c5959e0ebdf5847277fba3284d76ee535084e022d087659fd0791e5ccd3545c |
| /opt/foundryvtt/common/data/fields.mjs | 662–668 | efa8e3ccdf553ca826580e60bfbfc97db57bdeadaa954a50f6a55e0ab52c3e01 |
| /opt/foundryvtt/client/applications/forms/fields.mjs | 28–73 | 92e1ac0b69f0c37beeb36d9171146790c4551978e29e4e2ee9f0d0190d316202 |
| /opt/foundryvtt/client/applications/api/application.mjs | 704–717 | b5aef80d3e042a4a856be9dd875c72a5224988d62046ba770f25376f4291faa0 |
| /opt/foundryvtt/client/applications/sheets/active-effect-config.mjs | 59–65 | 6384d0b979ce9daa46079450a4aab042afbff01463a4c7c86571d8cecaa605e2 |

Дополнительно проверен ключ ядра EFFECT.TABS.duration: Duration в /opt/foundryvtt/public/lang/en.json, SHA-256 04a78a37b3b79fb99978ca23de41304b5fe7c816ad858b0e65b92c17b646ef1f. Отсутствие этого ключа в системных JSON не означает отсутствия в общем словаре.

## Процессы

| ID | Область | Шагов |
| --- | --- | --- |
| proc-000092 | Локализация: декларация русского словаря | 1 |
| proc-000093 | Локализация: label фазы ActiveEffect | 1 |
| proc-000094 | Локализация: подпись встроенного навыка | 1 |
| proc-000095 | Локализация: предупреждение о недостатке валюты | 3 |
| proc-000096 | Локализация: сообщение о лечении | 3 |
| proc-000097 | Локализация: динамические названия сопротивлений | 1 |

Процессы имеют partial scope; завершение внешнего lookup/DOM/записи не обозначается локальным успехом. Использование схемной подписи и текущего Skill.label не объединяется.

## Перекрёстная сверка очереди .006–.011

Проверки выполняются по накопленному набору: сохранение старых ID/отношений; адреса новых строковых листьев; прямой и обратный доступ каждого отношения; все steps/exits и участие ключей/методов в процессах; refs, свежесть и покрытие 615 путей. Все восемь IQ представлены 24 новыми CLI-примерами. Исторические доказательные случаи сохраняют свои границы набора; текущие ответы проверяются отдельно.

Пройдены 87 тестов (197 CLI-случаев), check --freshness, проверка ссылок и сохранности; [протокол .011](review-log.md#task-0006011). Игровые сценарии, мир/БД и браузер не запускались; литературный перевод, правила, другие локали и все runtime overrides вне задачи.

## Следующий остаток

Текущая согласованная очередь .006–.011 закрывает свои области, но TASK-0006 остаётся in-progress. 461 файл без определений и оставшиеся области 152 частично представленных файлов сохранены в [перечне](expansion-inventory.json) и [плане](expansion-plan.md). Подписи из config не означают раскрытые боевые/экономические алгоритмы.

Следующую очередь можно формировать по самостоятельным процессам боя/урона, магии, жизненного цикла Item и форм, валюты/IP/наград, ремесла и генератора. Это остаток для обсуждения, без новых задач или выбранного приоритета. Другие языки и сверка контента с рулбуками остаются вне справочника.
