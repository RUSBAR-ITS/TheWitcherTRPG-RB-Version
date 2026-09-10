# Проблемы

Здесь ведётся реестр проблем системы. Каждая проблема хранится в отдельном файле `issue-00001.md`; номер един для всех статусов и сохраняется при перемещении карточки.

| Каталог | Содержание |
| --- | --- |
| [potential](potential/README.md) | Найденные, но ещё не подтверждённые пользователем проблемы |
| [open](open/README.md) | Подтверждённые пользователем проблемы, которые необходимо исправить |
| [closed](closed/README.md) | Проблемы, закрытие которых подтверждено пользователем |

Агент согласовывает регистрацию до создания карточки. Подтверждение проблемы и разрешение на исправление — отдельные решения. Подробности — в [правилах](../rules/issues.md); для новой карточки используется [шаблон](templates/issue.md).

## Реестр

| ID | Описание | Статус |
| --- | --- | --- |
| [issue-00001](potential/issue-00001.md) | Возможное несоответствие регистрации системы в Foundry | `potential` |
| [issue-00002](potential/issue-00002.md) | Отсутствие выбранного компедиума прерывает обработчик ready | `potential` |
| [issue-00003](potential/issue-00003.md) | Интеграция statuscounter вызывает querySelector у массива статусов | `potential` |
| [issue-00004](potential/issue-00004.md) | Несогласованные commonspeech/commonsp нарушают обращения к общему языку | `potential` |
| [issue-00005](potential/issue-00005.md) | Модели и листы четырёх типов не согласованы с манифестом | `potential` |
| [issue-00006](potential/issue-00006.md) | Эффекты начала хода выполняются при любом обновлении Combat | `potential` |
| [issue-00007](potential/issue-00007.md) | В подсказках брони перепутаны левая и правая ноги | `potential` |
| [issue-00008](potential/issue-00008.md) | Ответ true от query не подтверждает выполнение операции | `potential` |
| [issue-00009](potential/issue-00009.md) | Запросы для регионов заклинания не согласованы с маршрутизатором | `potential` |
| [issue-00010](potential/issue-00010.md) | Неизвестный тип сообщения сокета вызывает TypeError | `potential` |
| [issue-00011](potential/issue-00011.md) | Миграция не восстанавливает отсутствующий unmodifiedMax из max | `potential` |
| [issue-00012](potential/issue-00012.md) | Модификаторы luck.max и toxicity.max прибавляются дважды | `potential` |
| [issue-00013](potential/issue-00013.md) | В знаниях монстра редактор получает исходный текст вместо enriched HTML | `potential` |
| [issue-00014](potential/issue-00014.md) | Ключ подписи числовой репутации отсутствует в локализациях | `potential` |
| [issue-00015](potential/issue-00015.md) | Подписи групп не передаются во вложенную модель Skill | `potential` |
| [issue-00016](potential/issue-00016.md) | Ключи подписей трёх навыков CRA расходятся с локализациями | `potential` |
| [issue-00017](potential/issue-00017.md) | Повышение магического навыка не списывает магические очки развития | `potential` |
| [issue-00018](potential/issue-00018.md) | Текущий шаблон навыков монстра не учитывает isVisible | `potential` |
| [issue-00019](potential/issue-00019.md) | Бонусы attacks имеют разную форму в схеме, подсказках и формуле | `potential` |
| [issue-00020](potential/issue-00020.md) | Обмен валюты на саму себя увеличивает остаток | `potential` |
| [issue-00021](potential/issue-00021.md) | Тип урона теряется при обработке turnStartEffects | `potential` |
| [issue-00022](potential/issue-00022.md) | Обработчик лечения начала хода не учитывает heal.modifier | `potential` |
| [issue-00023](potential/issue-00023.md) | Расход временных HP изменяет посторонние изменения того же эффекта | `potential` |
| [issue-00024](potential/issue-00024.md) | Подготовка листа заменяет объект событий жизни массивом в данных Actor | `potential` |
| [issue-00025](potential/issue-00025.md) | Флаг applyAP вызывает ошибку из-за несогласованного пути свойств урона | `potential` |
| [issue-00026](potential/issue-00026.md) | Множитель типа урона применяется только внутри веток сопротивления брони | `potential` |
| [issue-00027](potential/issue-00027.md) | Отрицательный flat изменения урона игнорируется | `potential` |
| [issue-00028](potential/issue-00028.md) | Методы журнала не возвращают завершение записи баланса | `potential` |
| [issue-00029](potential/issue-00029.md) | Отрицательное ручное списание IP передаётся строкой и не проходит валидацию | `potential` |
| [issue-00030](potential/issue-00030.md) | Вкладка IP монстра использует отсутствующие поля персонажа | `potential` |
| [issue-00031](potential/issue-00031.md) | Непустой список иммунитетов вызывает ReferenceError в WitcherActor.applyStatus | `potential` |
| [issue-00032](potential/issue-00032.md) | Получение списка локаций теряет контекст монстра с хвостом или крылом | `potential` |
| [issue-00033](potential/issue-00033.md) | Положительные модификаторы атаки и защиты создают формулу без оператора | `potential` |
| [issue-00034](potential/issue-00034.md) | Методы Actor завершаются раньше вложенных операций с предметами | `potential` |
| [issue-00035](potential/issue-00035.md) | Штраф от перегруза дважды вычитается из REF и DEX | `potential` |
| [issue-00036](potential/issue-00036.md) | Изменения максимумов эффектами теряются при подготовке характеристик | `potential` |
| [issue-00037](potential/issue-00037.md) | Интерфейс алхимии вызывает отсутствующий метод списка компонентов | `potential` |
| [issue-00038](potential/issue-00038.md) | Изготовление предмета завершается до записи инвентаря и сообщения | `potential` |
| [issue-00039](potential/issue-00039.md) | Генератор добычи предполагает единственный непустой результат таблицы | `potential` |
| [issue-00040](potential/issue-00040.md) | Повторная генерация добычи может терять увеличение количества | `potential` |
| [issue-00041](potential/issue-00041.md) | Сообщение об успешном изготовлении сохраняется при нехватке компонентов | `potential` |
| [issue-00042](potential/issue-00042.md) | Передача временного улучшения теряет список изменений эффекта | `potential` |
| [issue-00043](potential/issue-00043.md) | Частичные обновления ActiveEffect нарушают обработку фаз | `potential` |
| [issue-00044](potential/issue-00044.md) | Передаваемая длительность не попадает в копию ActiveEffect | `potential` |
| [issue-00045](potential/issue-00045.md) | Недоступный предмет повторно отправляется GM без условия остановки | `potential` |
| [issue-00046](potential/issue-00046.md) | Выбор временного улучшения не обрабатывает отсутствие оружия | `potential` |
| [issue-00047](potential/issue-00047.md) | Применение статуса из чата не проверяет наличие Actor | `potential` |
| [issue-00048](potential/issue-00048.md) | Пакетный обработчик статусов чата смешивает DOM и jQuery | `potential` |
| [issue-00049](potential/issue-00049.md) | Применение отключённого статуса удаляет его вместо включения | `potential` |
| [issue-00050](potential/issue-00050.md) | Временное улучшение не получает начало отсчёта длительности | `potential` |
| [issue-00051](potential/issue-00051.md) | Автодополнение переносимого эффекта предмета выбирает схему Item | `potential` |
| [issue-00052](potential/issue-00052.md) | Мастер изменений не учитывает несохранённые поля формы | `potential` |
| [issue-00053](potential/issue-00053.md) | Системная вкладка улучшения обращается к отсутствующему полю | `potential` |
| [issue-00054](potential/issue-00054.md) | Вкладка эффектов дважды выводит список критических травм | `potential` |
| [issue-00055](potential/issue-00055.md) | Повторный рендер частей добавляет дубликаты мастера и datalist | `potential` |
| [issue-00056](potential/issue-00056.md) | Описание эффекта не раскрывается в конфигурации Item | `potential` |
| [issue-00057](potential/issue-00057.md) | Для предмета note зарегистрирован лист без частей содержимого | `potential` |
| [issue-00058](potential/issue-00058.md) | Перенос некоторых документов в лист Item вызывает отсутствующие методы | `potential` |
| [issue-00059](potential/issue-00059.md) | Общий лист Item обходит hook dropItemSheetData ядра | `potential` |
| [issue-00060](potential/issue-00060.md) | Редактор предметных воздействий заменяет текст on булевым значением | `potential` |
| [issue-00061](potential/issue-00061.md) | Для варианта атаки itemUse в конфигурации нет выбора навыка | `potential` |
| [issue-00062](potential/issue-00062.md) | Раздел настройки заклинания подписан как дальний бой | `potential` |
| [issue-00063](potential/issue-00063.md) | Настройка кликабельной картинки не связана с моделью и текущим инвентарём | `potential` |
| [issue-00064](potential/issue-00064.md) | Начальный магический навык spellcasting отсутствует в справочнике навыков | `potential` |
| [issue-00065](potential/issue-00065.md) | Начальные настройки атаки теряют прежнее поле attackSkill при очистке модели | `potential` |
| [issue-00066](potential/issue-00066.md) | Настройка applyRangedMeleeBonus не участвует в расчёте атаки | `potential` |
| [issue-00067](potential/issue-00067.md) | Миграция свойств урона перезаписывает новые значения прежними полями | `potential` |
| [issue-00068](potential/issue-00068.md) | Миграция брони удаляет преобразованный массив предметных воздействий | `potential` |
| [issue-00069](potential/issue-00069.md) | Слияние свойств профессиональной атаки пропускает объект effects | `potential` |
| [issue-00070](potential/issue-00070.md) | Добавление эффектов атаки изменяет подготовленные свойства самого предмета | `potential` |
| [issue-00071](potential/issue-00071.md) | Отбор защит профессии игнорирует выключенный isDefense | `potential` |
| [issue-00072](potential/issue-00072.md) | Защита определяющего навыка профессии отсутствует в переборе доступных защит | `potential` |
| [issue-00073](potential/issue-00073.md) | Свойство silverTrait заменяет метод setType вместо изменения типа урона | `potential` |
| [issue-00074](potential/issue-00074.md) | Вкладка региональных свойств остаётся без содержимого из-за устаревшего пути createTemplate | `potential` |
| [issue-00075](potential/issue-00075.md) | Региональный шаблон запрашивает отсутствующее поле createRegionFromTemplate | `potential` |
| [issue-00076](potential/issue-00076.md) | Миграция региона перезаписывает актуальный макрос tokenMoveWithin | `potential` |
| [issue-00077](potential/issue-00077.md) | Подготовка улучшений оружия и брони требует Actor даже у отдельного Item | `potential` |
| [issue-00078](potential/issue-00078.md) | Миграция оружия и брони дублирует ID улучшения при смешанных представлениях | `potential` |
| [issue-00079](potential/issue-00079.md) | Выбор навыка защиты оружия останавливается на пустом meleeAttackSkill | `potential` |
| [issue-00080](potential/issue-00080.md) | Обработчик связанного рецепта обращается к dataset отсутствующего offsetParent | `potential` |
| [issue-00081](potential/issue-00081.md) | Promise ремонта оружия и брони завершается до обновления Item | `potential` |
| [issue-00082](potential/issue-00082.md) | Расчёт свободных ячеек брони выбрасывает RangeError при недопустимой длине массива | `potential` |
| [issue-00083](potential/issue-00083.md) | Повреждение брони пропускается, если урон SP превышает оставшийся modified SP | `potential` |
| [issue-00084](potential/issue-00084.md) | Подготовка Actor не разворачивает словарь предметных воздействий брони | `potential` |
| [issue-00085](potential/issue-00085.md) | Настройки дополнительной защиты брони не подключены к общему отбору защит | `potential` |
| [issue-00086](potential/issue-00086.md) | Миграция SP брони перезаписывает заполненные новые поля старыми значениями | `potential` |
| [issue-00087](potential/issue-00087.md) | Миграция сопротивлений брони заменяет актуальный false прежним true | `potential` |
| [issue-00088](potential/issue-00088.md) | Форма брони может сохранить сопротивление улучшения как базовое | `potential` |
| [issue-00089](potential/issue-00089.md) | Конфигурационные записи воздействий брони не соответствуют входу applyStatus | `potential` |
| [issue-00090](potential/issue-00090.md) | В русской локализации отсутствуют четыре подсказки локаций общей формы брони | `potential` |
| [issue-00091](potential/issue-00091.md) | Редактор эффектов расходования ищет ID, отсутствующий в схеме записей | `potential` |
| [issue-00092](potential/issue-00092.md) | Форма расходования обращается к отсутствующему полю addsTempHp | `potential` |
| [issue-00093](potential/issue-00093.md) | Лист мутагена не подключает настройки расходования из его модели | `potential` |

Статус соответствует каталогу карточки. При перемещении обновляются этот реестр и все ссылки на документ. Номер новой карточки определяется по реестру и файлам во всех трёх каталогах.

Регистрация проблемы не создаёт задачу и не определяет её приоритет. Согласованные задачи ведутся в [docs/tasks](../tasks/README.md).

[Начало документации](../README.md).
