# module/data/actor/templates/common/adrenalineData.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/data/actor/templates/common/adrenalineData.js](../../../../../../../../../module/data/actor/templates/common/adrenalineData.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `c34b790379fd98cd7e33ccbeeca085e49297a40f` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.003](../../../../../../../../tasks/task-0003.003.md), одна порция из восьми файлов |
| Запись перекрёстной сверки | [TASK-0003.003](../../../../../../review-log.md#task-0003003) |

## Назначение файла

Фабрика двух полей счётчика адреналина Actor. Возможность использования адреналина определяется потребителями и настройкой системы.

## Условия использования

[module/data/actor/commonActorData.js](../../../../../../../../../module/data/actor/commonActorData.js):2,37 импортирует adrenaline и вызывает внутри SchemaField. По наследованию поле есть у CharacterData и MonsterData. При импорте читается foundry.data.fields.

## Введённые сущности и действия с ними

| Поле / сущность | Тип, начальное значение и ограничения | Назначение и действия |
| --- | --- | --- |
| adrenaline() | default export, :3–8 | Создаёт новый объект полей. |
| value | NumberField, initial=0; min/max/integer не заданы | Текущее количество. |
| label | StringField, initial=WITCHER.Actor.Adrenaline | Ключ подписи счётчика. |

## Основные функции и методы

adrenaline():3–8 без аргументов возвращает value/label. Собственных расчётов, миграции, сброса и записи документов в файле нет.

## Используемые сущности и зависимости

| Сущность | Файл определения / API | Связь, место и цель |
| --- | --- | --- |
| NumberField, StringField | Внешний API Foundry 14.367.0: /opt/foundryvtt/common/data/fields.mjs | Локальная ссылка fields:1; создание полей:5–6. |
| WITCHER.Actor.Adrenaline | [lang/en.json](../../../../../../../../../lang/en.json); [lang/ru.json](../../../../../../../../../lang/ru.json) | Строковый ключ initial label; перевод присутствует в en/ru. |

## Известные потребители

| Файл-потребитель | Обращение и условия |
| --- | --- |
| [module/data/actor/commonActorData.js](../../../../../../../../../module/data/actor/commonActorData.js) | defineSchema:37 — system.adrenaline; migrateAdrenaline:131–133 переносит current в value, если существующий value ложен. |
| [module/actor/mixins/adrenalineMixin.js](../../../../../../../../../module/actor/mixins/adrenalineMixin.js) | addAdrenaline:2–5 увеличивает value через update только при useOptionalAdrenaline=true; собственного потолка здесь нет. |
| [module/actor/sheets/mixins/statMixin.js](../../../../../../../../../module/actor/sheets/mixins/statMixin.js) | _onAdrenalineMinus:110–115 уменьшает при value>0; _onAdrenalinePlus:117–120 вызывает addAdrenaline; statListener:129–130 связывает кнопки. |
| [module/actor/sheets/WitcherActorSheet.js](../../../../../../../../../module/actor/sheets/WitcherActorSheet.js); [module/setup/settings.js](../../../../../../../../../module/setup/settings.js) | Лист читает useOptionalAdrenaline в context.useAdrenaline; настройка зарегистрирована в settings:17. |
| [templates/sheets/actor/partials/character/sidebar.hbs](../../../../../../../../../templates/sheets/actor/partials/character/sidebar.hbs) | Блок useAdrenaline, :145–156 — ввод system.adrenaline.value, кнопки плюс/минус. |
| [module/actor/mixins/defenseMixin.js](../../../../../../../../../module/actor/mixins/defenseMixin.js); [module/setup/queries.js](../../../../../../../../../module/setup/queries.js) | defense:209–218 отправляет addAdrenaline владельцу атакующего при truthy результате checkForCrit(roll.total, totalAttack); queries:26 включает метод в список обработки. |
| [module/actor/witcherActor.js](../../../../../../../../../module/actor/witcherActor.js) | Импорт adrenalineMixin:18 и Object.assign:453 предоставляют Actor.addAdrenaline. |

Область поиска: прямые импорты в module, обращения к полям в module/templates и строковые пути в 226 packsJson. Соседние файлы проверялись в пределах указанных обращений. Их полный разбор не объявляется выполненным.

## Данные и изменения состояния

Фабрика только создаёт схему. Начальный счётчик — 0. Изменение количества через Actor.update выполняют указанные методы и форма. CommonActorData.migrateAdrenaline меняет входной source: {current:3}→value=3, {value:2,current:3} сохраняет 2, {value:0,current:3} даёт 3. Это буквальное условие !value, а не особое ограничение фабрики.

## Проверки и доказательства

Проверены все 8 строк, начальные значения реальной CommonActorData и три входа миграции. Исходный addAdrenaline при включённой настройке сформировал единственный update value=1; при выключенной записи не было. Локализация label найдена в 7 из 8 файлов (нет it.json, en содержит ключ); работа fallback в браузере не запускалась.

Файл прочитан полностью; определения и потребители сопоставлены в обе стороны. Изолированные проверки использовали реальные DataModel/TypeDataModel и поля установленного Foundry, а внешние действия — явно указанные подмены. Полный сценарий и результаты находятся в журнале TASK-0003.003.

## Непроверенные участки и открытые вопросы

Полные условия получения/расходования адреналина в бою, сетевой query, повторные обновления и соответствие рулбуку не проверялись. Отсутствие min/max в схеме само по себе не объявляется ошибкой.

## Связанные проблемы

Новых проблем, требующих отдельной карточки для этого файла, в пределах проверки не выявлено.


## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.003 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.

## Уточнение TASK-0003.006

2026-09-10, `fe7ea7420cd4dfa6ee51baf7520f7b0ad8f8b13d`. Сверено включение:37 и полностью разобрана migrateAdrenaline:131–133. Прямой вызов для {current:3}/{value:0,current:3}/{value:2,current:3} дал value3/3/2. Для {value:0} без current метод оставляет собственное свойство value=undefined до очистки полей; это дополнительная граница проверки, не результат миграции мира.

Карточки сборки: [commonActorData](../../commonActorData.js.md). [Сверка TASK-0003.006](../../../../../../review-log.md#task-0003006).
