# Сверка семи компедиумов с английской базовой книгой

**Итог 2026-09-17 / .00020:** B01–B17 исправлены, установлены и приняты после браузерной проверки; [К01 и девять исходных карточек закрыты](../issues/closed/issue-00331.md#acceptance) по поручению пользователя. A01–A09 остаются исключёнными авторскими вариантами. Датированные этапы подготовки ниже сохраняют прежние состояния.

Дата: 2026-09-16. Ветка `dev`, HEAD `433060047ca195773d582cac782a6a83a5c91ade`; исходные данные версии `14.3.1.00013`, оформление `14.3.1.00014`. Основание — поручение пользователя извлечь правила из предоставленной английской книги, сравнить компедиумы и дополнить [issue-00331](../issues/closed/issue-00331.md).

[Книжная выписка: источник, 40 страниц и указатель](compendium-core-rulebook-reference.md). Это сравнение с конкретным PDF 2018 года, не заключение о последней редакции правил.

## Исправление ошибок — 14.3.1.00016

Все согласованные B01–B17 выполнены в объёме [К01](../issues/closed/issue-00331.md#implementation): 48 JSON / шесть пакетов. A01–A09 сохранены. Текущий набор содержит 77 ActiveEffect / 358 changes вместо 79 / 360; число корневых документов, таблиц и результатов не изменилось. 254 documentUuid и 62 followUp разрешимы. Шесть временных баз собраны и проверены обратным извлечением в .00016; в .00018 [установлены в packs](../issues/closed/issue-00331.md#installation). Игровая приёмка ожидается.

Ниже сохранена **исходная сверка .00014**, включая найденные тогда ошибки, числа, цитаты и хеш. Она не является повторным списком нерешённых B. Реальное состояние каждого исправления, проверки и ограничения 00320/00328/00036 ведутся только в issue-00331.

## Охват и способ проверки

Прочитаны все **226 JSON** семи пакетов: **128 RollTable / 995 TableResult**, **94 criticalWound Item / 79 ActiveEffect / 360 changes** и **4 Folder**. Среди травм 32 исходных, 31 stabilized и 31 treated; у Separated Spine/Decapitated по книге нет двух последующих состояний. Поэтому 94 документа не означают 94 разных книжных травмы.

Для таблиц сопоставлены тексты, числа, диапазоны, вложенные ссылки и маршрут генерации. Для травм — три состояния книжной строки, записанные штрафы/множители, описания, названия, локации, состав и disabled эффектов, followUp. Действие изменений на Actor не исполнялось. Папки проверены как организация четырёх уровней, не как дополнительные правила.

Хеш исходного набора: `36de8fc2d2041aeed81052d84491c845c29f6ad577c876a0fbbe0e5d749fcc7b` (SHA256 последовательности `relative_path + NUL + bytes` всех 226 JSON, отсортированных по пути от корня репозитория). Книжный эталон извлечён независимо от JSON; таблицы компедиума не использовались для «восстановления» отсутствующего в PDF правила.

**17 групп наблюдений B01–B17** ниже включают и новые несоответствия, и книжное уточнение ранее зарегистрированных issues; это не 17 новых issue и не 17 выполненных исправлений. **9 групп A01–A09** относятся к адаптациям/редакциям либо неустановленным источникам. По последующему решению пользователя (.00015) они исключены из текущего плана исправлений и не блокируют работу над ошибками. Индивидуальные статусы старых карточек не изменены.

| Пакет | JSON | Результат |
| --- | --- | --- |
| character-generator | 13 | Главные дефекты — маршрут Life Event и ветка Family Fate; случайные расы/происхождение частично авторские |
| character-generator-sub-tables | 35 | Десять чужих текстов Elderland, пропуски переходов; большая часть чисел статуса/происхождения/siblings совпадает |
| lifepath | 21 | Основные тексты/диапазоны соответствуют с. 32–35; inline-формулы и вариации Gender/Who Was Wronged выделены отдельно |
| style | 7 | Все 70 результатов семи колонок соответствуют с. 36 по смыслу и диапазону; исправление опечатки Valuable не меняет правило |
| witcher-lifepath | 41 | Возрастные ссылки, пропущенные условия Hunt/смерти союзника, inline-формулы; несколько адаптаций |
| combat | 11 | Диапазоны монстра, знак штрафа, две неразрешимые ссылки, inline-формулы; Scatter пока без установленного числового источника |
| criticalWounds | 98 | 94 Item и 4 Folder; числовой штраф treated правой ноги, bleed treated рук, локации/имена/disabled и неполнота условий |

Семь пакетов не являются семью независимыми главами книги: контейнеры вызывают общие подтаблицы. Перекрытие диапазонов текст+ссылка или нескольких независимых колонок само по себе допустимо. Отсутствие ActiveEffect у описательного результата само по себе не ошибка: ручное применение правил в таблице не равно обещанию автоматизации.

## Установленные наблюдения и ожидаемое содержание

<a id="b01"></a>

### B01 — Life Event Generator обходит две промежуточные таблицы

Книга: [с. 31](compendium-core-rulebook-reference.md#page-31). Связь с прежними карточками: —.

Файлы: [Life Event Generator](../../packsJson/character-generator/Life_Event_Generator_4Y8IpS3ArbbP2gGc.json) (`4Y8IpS3ArbbP2gGc`).

**Сейчас:** `1–4 → Fortune (Z0eeWQI3R8v4YNLd)`, `5–7 → Misfortune (JNbvihde5EGIFPdB)`, `8–10 → Romance`. Ветка Allies and Enemies недостижима из этого генератора.

**Ожидаемое содержание / предложение:** `1–4 → Fortune or Misfortune (qKwYD3GHlGxCmiir)`, `5–7 → Allies and Enemies (Lp42vhkw20Ys973y)`, `8–10 → Romance` без изменения диапазонов. Книжные вероятности: Fortune 20%, Misfortune 20%, Ally 15%, Enemy 15%, Romance 30%; сейчас 40/30/0/0/30%.

<a id="b02"></a>

### B02 — В Parental Fate: Elderland скопирована нильфгаардская колонка

Книга: [с. 27](compendium-core-rulebook-reference.md#page-27). Связь с прежними карточками: —.

Файлы: [Parental Fate: Elderland](../../packsJson/character-generator-sub-tables/Parental_Fate__Elderland_jZVPaCIoQxFZiyRu.json) (`jZVPaCIoQxFZiyRu`).

**Сейчас:** Все десять текстов соответствуют колонке Nilfgaard (война, яд, тайная полиция, rogue mage и т. д.), хотя переходы ведут в Elderland Family Status.

**Ожидаемое содержание / предложение:** Заменить десять descriptions на Elderland: 1 обвинение в Scoia’tael; 2 предательство своего народа; 3 самоубийство; 4 погром; 5 одержимость былым величием; 6 изгнание; 7 проклятие; 8 передача другой семье; 9 вступление в Scoia’tael; 10 смерть в «несчастном случае». Полные тексты — в выписке. Не трогать Nilfgaard колонку этим исправлением.

<a id="b03"></a>

### B03 — После Family Fate пропускается Parental Fate

Книга: [с. 26](compendium-core-rulebook-reference.md#page-26). Связь с прежними карточками: —.

Файлы: [Family Fate: Northern](../../packsJson/character-generator-sub-tables/Family_Fate__Northern_CN0lwXPHxkV2vDeY.json) (`CN0lwXPHxkV2vDeY`); [Family Fate: Elderland](../../packsJson/character-generator-sub-tables/Family_Fate__Elderland_W6mgmCP3219eYdf0.json) (`W6mgmCP3219eYdf0`); [Family Fate: Nilfgaard](../../packsJson/character-generator-sub-tables/Family_Fate__Nilfgaard_VstrJuRw43OKcuGr.json) (`VstrJuRw43OKcuGr`); [Family and Parents: Elderland](../../packsJson/character-generator-sub-tables/Family_and_Parents__Elderland_d7NLtNEdvkagBLOP.json) (`d7NLtNEdvkagBLOP`); [Family and Parents: Nilfgaard](../../packsJson/character-generator-sub-tables/Family_and_Parents__Nilfgaard_5OcHT6WrJ8pL9cYp.json) (`5OcHT6WrJ8pL9cYp`); [Family and Parents: Northern](../../packsJson/character-generator-sub-tables/Family_and_Parents__Northern_xAVQucslVR12q2kc.json) (`xAVQucslVR12q2kc`); [Background Generator: Dwarves](../../packsJson/character-generator/Background_Generator__Dwarves_PCAssN2Ms7yLzuCv.json) (`PCAssN2Ms7yLzuCv`); [Background Generator: Elves](../../packsJson/character-generator/Background_Generator__Elves_L8o8Rz85um05VUW4.json) (`L8o8Rz85um05VUW4`).

**Сейчас:** Northern результаты 1–9 идут прямо в Family Status, а 10 вообще не имеет продолжения. Elderland/Nilfgaard Family Fate не имеют продолжения; вызывающие контейнеры при несчастье одновременно выдают Fate и сразу Status. Генераторы Elf/Dwarf повторяют такой обход.

**Ожидаемое содержание / предложение:** Обеспечить ровно один переход Family Fate → Parental Fate соответствующего региона → Family Status → Influential Friend, включая результат Northern 10. Способ размещения ссылок согласовать: добавление перехода без удаления прежнего параллельного Status вызовет двойное определение статуса. Не считать гибель семьи разрешением убрать явно напечатанный следующий этап.

<a id="b04"></a>

### B04 — Nilfgaard Parental Fate обрывается на 10

Книга: [с. 27](compendium-core-rulebook-reference.md#page-27). Связь с прежними карточками: —.

Файлы: [Parental Fate: Nilfgaard](../../packsJson/character-generator-sub-tables/Parental_Fate__Nilfgaard_wFuCDleU9PzP00mf.json) (`wFuCDleU9PzP00mf`).

**Сейчас:** Для результатов 1–9 есть ссылка на Family Status: Nilfgaard, для 10 остались текст и общий Which Parent, но нет Status.

**Ожидаемое содержание / предложение:** Для 10 также выполнить переход к `6WXA7KAOHjeqCCRn` ровно один раз.

<a id="b05"></a>

### B05 — Monster Damage Location: три неверных диапазона

Книга: [с. 154](compendium-core-rulebook-reference.md#page-154). Связь с прежними карточками: issue-00322.

Файлы: [Monster Damage Location](../../packsJson/combat/Monster_Damage_Location_KYyK6F8JHhA3hOu7.json) (`KYyK6F8JHhA3hOu7`).

**Сейчас:** В JSON Torso 2–5, R. Limb 6–7, Special/Tail or Wing 9–10; у L. Limb 8–9. На 9 выбираются две локации, а 5 ошибочно попадает в torso.

**Ожидаемое содержание / предложение:** Torso 2–4; R. Limb 5–7; L. Limb 8–9; Special 10. Имена «Tail or Wing» являются уточнением Special, числовой дефект от них не зависит.

<a id="b06"></a>

### B06 — Потерян минус у леченого Compound Leg Fracture в RollTable

Книга: [с. 160](compendium-core-rulebook-reference.md#page-160). Связь с прежними карточками: —.

Файлы: [Difficult Critical](../../packsJson/combat/Difficult_Critical_VIup1SZTMKCSGGbT.json) (`VIup1SZTMKCSGGbT`).

**Сейчас:** Результат 2–3, фрагмент Treated: `2 to SPD, Dodge/ Escape, and Athletics.`

**Ожидаемое содержание / предложение:** Восстановить `−2` в тексте результата. В обоих treated Items этой травмы уже стоят −2, их числа по этой причине менять не нужно.

<a id="b07"></a>

### B07 — Леченый Fractured Leg (Right) сохраняет исходный штраф −3

Книга: [с. 159](compendium-core-rulebook-reference.md#page-159). Связь с прежними карточками: issue-00326 (подпись, не числовое исправление).

Файлы: [Fractured Leg (Right - Treated)](../../packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Fractured_Leg__Right___Treated__Aa8wCz1OGM4gflmc.json) (`Aa8wCz1OGM4gflmc`).

**Сейчас:** Все три changes (`spd.totalModifiers`, `dodge.activeEffectModifiers`, `athletics.activeEffectModifiers`) равны −3. В левой treated-форме и тексте Combat указано −1.

**Ожидаемое содержание / предложение:** Для правой treated-формы все три штрафа должны быть −1. Это числовое расхождение отдельно от неверного имени эффекта.

<a id="b08"></a>

### B08 — После лечения открытого перелома руки возвращается bleed

Книга: [с. 160](compendium-core-rulebook-reference.md#page-160). Связь с прежними карточками: issue-00328 — отдельная проблема исполнения ADD, категория механик.

Файлы: [Compound Arm Fracture (Left - Treated)](../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Compound_Arm_Fracture__Left___Treated__zaKPfDQFGTR8FKju.json) (`zaKPfDQFGTR8FKju`); [Compound Arm Fracture (Right - Treated)](../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Compound_Arm_Fracture__Right___Treated__ujz1IMKCXoJF9w91.json) (`ujz1IMKCXoJF9w91`).

**Сейчас:** Оба treated Item хранят включённый эффект с `statuses=[bleed]` и `turnStartEffects.bleed`, amount=2. У stabilized-форм такого эффекта нет.

**Ожидаемое содержание / предложение:** В колонке Treated рука остаётся на перевязи, но может держать предметы; нового кровотечения там нет. Убрать bleed из этих двух treated-шаблонов после согласования. Это ошибка состава контента независимо от того, исполняет ли Foundry ошибочный ADD сейчас. Исходный bleed у нелеченых рук сохранить.

<a id="b09"></a>

### B09 — Hunt Generator не сообщает награду за охоту

Книга: [с. 244](compendium-core-rulebook-reference.md#page-244). Связь с прежними карточками: —.

Файлы: [Witcher Lifepath: Hunt Generator](../../packsJson/witcher-lifepath/Witcher_Lifepath__Hunt_Generator_vTIEP2TnU2n4hwY3.json) (`vTIEP2TnU2n4hwY3`); [Witcher Lifepath: Hunt - What Was the Prey?](../../packsJson/witcher-lifepath/Witcher_Lifepath__Hunt___What_Was_the_Prey__ZozZLNSgKpwEltsY.json) (`ZozZLNSgKpwEltsY`).

**Сейчас:** У генератора и таблицы добычи пустые descriptions; результаты выдают только категорию монстра, место, исход и поворот. Условие выбора конкретного монстра и +2 отсутствует.

**Ожидаемое содержание / предложение:** Добавить читаемое указание: выбрать конкретного монстра в выпавшей категории, получить +2 к связанным с ним Witcher Training checks. Это сначала полнота текста; автоматическое добавление условного навыкового бонуса — отдельное изменение механики.

<a id="b10"></a>

### B10 — У смерти союзника ведьмака потерян срок

Книга: [с. 243](compendium-core-rulebook-reference.md#page-243). Связь с прежними карточками: —.

Файлы: [Witcher Lifepath: Allies - Are They Alive?](../../packsJson/witcher-lifepath/Witcher_Lifepath__Allies___Are_They_Alive__2l9nl4ndvdgtn2SJ.json) (`2l9nl4ndvdgtn2SJ`); [Witcher Lifepath: Allies - How Did They Die](../../packsJson/witcher-lifepath/Witcher_Lifepath__Allies___How_Did_They_Die_AMYeAxAXD3DMX6St.json) (`AMYeAxAXD3DMX6St`).

**Сейчас:** Есть 30% смерти и четыре причины, но ни в родителе, ни в причинах не указано бросить 1d10 десятилетий до смерти. У врагов этот бросок сохранён.

**Ожидаемое содержание / предложение:** Вернуть один бросок/указание `1d10 decades later` при смерти союзника. Не вызывать его одновременно в двух местах; не путать с причиной смерти.

<a id="b11"></a>

### B11 — Теряется возрастной модификатор Trials

Книга: [с. 239](compendium-core-rulebook-reference.md#page-239). Связь с прежними карточками: issue-00321.

Файлы: [Witcher Background: How Did Early Training Go? +2](../../packsJson/witcher-lifepath/Witcher_Background__How_Did_Early_Training_Go___2_A7jt3mfuFTEQiXRv.json) (`A7jt3mfuFTEQiXRv`); [Witcher Background: How Did Early Training Go? -2](../../packsJson/witcher-lifepath/Witcher_Background__How_Did_Early_Training_Go___2_G9iWzbiGQloX7sls.json) (`G9iWzbiGQloX7sls`).

**Сейчас:** В обоих вариантах Early Training ±2 восемь обычных исходов (1,2,3,5,6,8,9,10) ссылаются на нулевое испытание `vaUFKIYBmEbJotfJ`.

**Ожидаемое содержание / предложение:** В варианте +2 эти восемь ссылок → Trials +2 (`zNG1R1HQoY6tpSLz`), в варианте −2 → Trials −2 (`CDX4hqsxcxxovYz3`). Исходы 4 и 7 уже учитывают сумму ±4/0; сверять матрицу в выписке и возраст на с. 238.

<a id="b12"></a>

### B12 — Книжное умножение переписано как x внутри Foundry inline rolls

Книга: [с. 169](compendium-core-rulebook-reference.md#page-169). Связь с прежними карточками: issue-00319.

Файлы: [Vehicle Control Loss](../../packsJson/combat/Vehicle_Control_Loss_zO7eKgtDOAH0qnow.json) (`zO7eKgtDOAH0qnow`); [Fortune](../../packsJson/lifepath/Fortune_Z0eeWQI3R8v4YNLd.json) (`Z0eeWQI3R8v4YNLd`); [Misfortune](../../packsJson/lifepath/Misfortune_JNbvihde5EGIFPdB.json) (`JNbvihde5EGIFPdB`); [Witcher Lifepath: Benefit Outcome](../../packsJson/witcher-lifepath/Witcher_Lifepath__Benefit_Outcome_snt4khwSoq2rdeZa.json) (`snt4khwSoq2rdeZa`); [Witcher Lifepath: Danger - Events](../../packsJson/witcher-lifepath/Witcher_Lifepath__Danger___Events_zVS3tsoiyTdjwU7i.json) (`zVS3tsoiyTdjwU7i`).

**Сейчас:** Семь вставок в пяти JSON используют `[[1d10x2]]`, `[[1d10x3]]`, `[[1d10x100]]`, `[[1d6x10]]`.

**Ожидаемое содержание / предложение:** Сохранить книжные величины, но для исполняемых формул использовать умножение Foundry `*`: транспорт ×2/×3 (с. 169), удача/долг ×100 (с. 32), украшение ×10 и Windfall ×100 (с. 242), долг ведьмака ×100 (с. 245). Печатное x вне формулы не требует механического поиска/замены.

<a id="b13"></a>

### B13 — Контейнер Mounted Control Loss ссылается на отсутствующие таблицы

Книга: [с. 169](compendium-core-rulebook-reference.md#page-169). Связь с прежними карточками: issue-00323.

Файлы: [Mounted Control Loss](../../packsJson/combat/Mounted_Control_Loss_VVb2zLR4NLdMLVQQ.json) (`VVb2zLR4NLdMLVQQ`).

**Сейчас:** `aLBBrVnSsL3wqQUx` и `6FrD4tQuyJOICu5m` отсутствуют среди источников. Контейнер не ссылается на фактически существующие две колонки с. 170.

**Ожидаемое содержание / предложение:** Сослаться на Personal (`KWLoKiOHKXXnq5E4`) и Mount (`XRdHZOmutZ3yzGRe`), каждая один раз, с независимыми бросками. Это UUID-исправление, а не объединение двух результатов в один бросок.

<a id="b14"></a>

### B14 — Анатомические локации расходятся с названием и книжной строкой

Книга: [с. 159](compendium-core-rulebook-reference.md#page-159). Связь с прежними карточками: issue-00324, issue-00325, issue-00327.

Файлы: [Minor Head Wound](../../packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Minor_Head_Wound_wPRuwd7RdLWnWmnb.json) (`wPRuwd7RdLWnWmnb`); [Minor Head Wound (Stabilized)](../../packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Minor_Head_Wound__Stabilized__EnwgL7ApZTdHgMbD.json) (`EnwgL7ApZTdHgMbD`); [Minor Head Wound (Treated)](../../packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Minor_Head_Wound__Treated__KsYEWWO5KlPHSdCy.json) (`KsYEWWO5KlPHSdCy`); [Sprained Leg (Left - Treated)](../../packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Sprained_Leg__Left___Treated__f7NaW1AMnrSLGkd3.json) (`f7NaW1AMnrSLGkd3`); [Compound Arm Fracture (Right - Stabilized)](../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Compound_Arm_Fracture__Right___Stabilized__NHNctAuhsapGZXiP.json) (`NHNctAuhsapGZXiP`); [Compound Leg Fracture (Right - Stabilized)](../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Compound_Leg_Fracture__Right___Stabilized__QCugb1JqpiFyBEN4.json) (`QCugb1JqpiFyBEN4`).

**Сейчас:** Minor Head Wound во всех трёх состояниях torso; Sprained Leg Left Treated — leftArm; Compound Arm Right Stabilized — rightLeg; Compound Leg Right Stabilized — rightArm.

**Ожидаемое содержание / предложение:** Ожидаемые `system.location`: head ×3; leftLeg; rightArm; rightLeg соответственно (с. 158–160). Проверить сохранение локации по всем followUp. Книга не вводит отдельного изменения стороны/части тела при лечении.

<a id="b15"></a>

### B15 — У исходной правой ампутации ноги отключены множители

Книга: [с. 160](compendium-core-rulebook-reference.md#page-160). Связь с прежними карточками: issue-00329; вычисление — issue-00036 / issue-00332.

Файлы: [Dismembered Leg (Right)](../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Dismembered_Leg__Right__Ssi9d4GQsAyYnt86.json) (`Ssi9d4GQsAyYnt86`).

**Сейчас:** Эффект с множителями 0.25 имеет `disabled=true`, в левой форме и правой stabilized — false.

**Ожидаемое содержание / предложение:** В составе шаблона должен быть активен одинаковый для сторон штраф четверти SPD/Dodge/Athletics. Исправление `.max` и порядка расчёта не включается сюда автоматически.

<a id="b16"></a>

### B16 — Названия сторон и Septic Shock

Книга: [с. 160](compendium-core-rulebook-reference.md#page-160). Связь с прежними карточками: issue-00326 содержит часть этих наблюдений; перечень расширен сверкой.

Файлы: [Fractured Leg (Right - Stabilized)](../../packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Fractured_Leg__Right___Stabilized__WNjcD3F3Hs5IdAaa.json) (`WNjcD3F3Hs5IdAaa`); [Fractured Leg (Right - Treated)](../../packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Fractured_Leg__Right___Treated__Aa8wCz1OGM4gflmc.json) (`Aa8wCz1OGM4gflmc`); [Fractured Leg (Right)](../../packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Fractured_Leg__Right__yI6kHQM8voHrBF2h.json) (`yI6kHQM8voHrBF2h`); [Dismembered Arm (Right)](../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Dismembered_Arm__Right__ZxvWPJPDD9fm34Pc.json) (`ZxvWPJPDD9fm34Pc`); [Dismembered Leg (Right)](../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Dismembered_Leg__Right__Ssi9d4GQsAyYnt86.json) (`Ssi9d4GQsAyYnt86`); [Compound Leg Fracture (Right)](../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Compound_Leg_Fracture__Right__Rf0m4mGjeHEl0PxP.json) (`Rf0m4mGjeHEl0PxP`); [Compound Leg Fracture (Right - Treated)](../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Compound_Leg_Fracture__Right___Treated__3SwpPbi2ddEJkebh.json) (`3SwpPbi2ddEJkebh`); [Sprained Arm (Right - Treated)](../../packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Sprained_Arm__Right___Treated__YiusbDXfFDhqwtQT.json) (`YiusbDXfFDhqwtQT`); [Sprained Leg (Left)](../../packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Sprained_Leg__Left__XPoH413WkKQUgrnw.json) (`XPoH413WkKQUgrnw`); [Sprained Leg (Left - Stabilized)](../../packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Sprained_Leg__Left___Stabilized__eblucqnyOS7lb5E5.json) (`eblucqnyOS7lb5E5`); [Sprained Leg (Left - Treated)](../../packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Sprained_Leg__Left___Treated__f7NaW1AMnrSLGkd3.json) (`f7NaW1AMnrSLGkd3`); [Spetic Shock](../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Spetic_Shock_tF3hsi4yZOMJ6xuW.json) (`tF3hsi4yZOMJ6xuW`); [Spetic Shock (Stabilized)](../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Spetic_Shock__Stabilized__LM6Kkh0ib6ux4WQp.json) (`LM6Kkh0ib6ux4WQp`); [Spetic Shock (Treated)](../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Spetic_Shock__Treated__vkr5MXhnalPp8yJJ.json) (`vkr5MXhnalPp8yJJ`).

**Сейчас:** 11 эффектов в 11 Items названы противоположной стороной. У трёх состояний и эффектов `Spetic Shock` вместо книжного `Septic Shock`.

**Ожидаемое содержание / предложение:** Согласовать имя эффекта с владельцем и состоянием; исправить Spetic → Septic в видимых именах, сохранив ID/UUID. Имена файлов с ID не обязаны меняться ради исправления видимого имени.

<a id="b17"></a>

### B17 — Книжные оговорки не полностью представлены в карточках травм

Книга: [с. 160](compendium-core-rulebook-reference.md#page-160). Связь с прежними карточками: —.

Файлы: [Cracked Ribs](../../packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Cracked_Ribs_7TzGQ2y4yZnG01im.json) (`7TzGQ2y4yZnG01im`); [Cracked Ribs (Stabilized)](../../packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Cracked_Ribs__Stabilized__2c4PbGjd0segbvmr.json) (`2c4PbGjd0segbvmr`); [Damaged Eye](../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Damaged_Eye_zHK1XmZ77V8c26Xv.json) (`zHK1XmZ77V8c26Xv`); [Damaged Eye (Stabilized)](../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Damaged_Eye__Stabilized__LNy3P3HUw2Ja9DNu.json) (`LNy3P3HUw2Ja9DNu`); [Damaged Eye (Treated)](../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Damaged_Eye__Treated__XQeXSAhvjrQZNpAE.json) (`XQeXSAhvjrQZNpAE`); [Heart Damage (Treated)](../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Heart_Damage__Treated__Me9fgalLrB0i9Z2O.json) (`Me9fgalLrB0i9Z2O`); [Spetic Shock (Treated)](../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Spetic_Shock__Treated__vkr5MXhnalPp8yJJ.json) (`vkr5MXhnalPp8yJJ`); [Dismembered Arm (Left)](../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Dismembered_Arm__Left__KQZRzczsSx1XY63m.json) (`KQZRzczsSx1XY63m`); [Dismembered Arm (Right)](../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Dismembered_Arm__Right__ZxvWPJPDD9fm34Pc.json) (`ZxvWPJPDD9fm34Pc`).

**Сейчас:** 42 из 94 Items имеют пустое `system.description`. Например, у Cracked Ribs не написано исключение HP (с. 158); у treated Eye/Heart/Septic не сохранено слово permanent; у исходной ампутации руки описание не включает прямой запрет пользоваться ею. Эффекты сами по себе не заменяют все условия книги.

**Ожидаемое содержание / предложение:** Дополнить описания релевантными условиями конкретного состояния, включая исключение HP, sight-based, постоянство и непригодность конечности. Не трактовать это как разрешение реализовать новые условные эффекты, протезы или изменение срока удаления. Полный автоматический перенос всех 42 описаний не обязателен без согласованного объёма; перечисленные утраты правил — обязательные точки проверки.

## Адаптации, различия редакций и неустановленные источники

Эти пункты сохранены как результаты исходной аналитики .00014. В .00015 пользователь поручил опустить авторские дополнения/отступления: A01–A09 исключены из текущего плана, остаются без изменений и не требуют решения перед исправлением B-пунктов. Вопросы в отдельных записях ниже относятся только к возможной будущей работе с ними.

<a id="a01"></a>

### A01 — Гендерные таблицы расширены относительно PDF

Источник для сравнения: [с. 30](compendium-core-rulebook-reference.md#page-30). Файлы: [Siblings: Gender](../../packsJson/character-generator-sub-tables/Siblings__Gender_QbkrG0W11fREICK8.json) (`QbkrG0W11fREICK8`); [Allies: Gender](../../packsJson/lifepath/Allies__Gender_QFHhoiXtIBYkL8Rd.json) (`QFHhoiXtIBYkL8Rd`); [Enemies: Gender](../../packsJson/lifepath/Enemies__Gender_FMondgMHlPLSy3cq.json) (`FMondgMHlPLSy3cq`); [Witcher Lifepath: Allies - Gender](../../packsJson/witcher-lifepath/Witcher_Lifepath__Allies___Gender_bw2dbovLaFTJJ8EP.json) (`bw2dbovLaFTJJ8EP`); [Witcher Lifepath: Danger - Enemies Generator](../../packsJson/witcher-lifepath/Witcher_Lifepath__Danger___Enemies_Generator_iwGZ1Sj0v9iBqvSk.json) (`iwGZ1Sj0v9iBqvSk`).

Четыре отдельные таблицы задают Male 1–4, Female 5–8, Gender Diverse 9–10; пятый документ — генератор врагов ведьмака — повторно использует обычную Enemies: Gender. В PDF siblings/обычные друзья/враги чередуют Male/Female (с. 30/33/34), союзники ведьмака — Male 1–5/Female 6–10 (с. 243), враги ведьмака — Male 1–2,5–6,9–10 и Female 3–4,7–8 (с. 245). Это установленная авторская вариация результатов и вероятностей, а не поломка ссылок. Сохранить расширение или обеспечить строгий книжный вариант — решение пользователя; молча удалять категории нельзя.

<a id="a02"></a>

### A02 — Генераторы эльфа/краснолюда выбирают только Elderlands

Источник для сравнения: [с. 25](compendium-core-rulebook-reference.md#page-25). Файлы: [Background Generator: Dwarves](../../packsJson/character-generator/Background_Generator__Dwarves_PCAssN2Ms7yLzuCv.json) (`PCAssN2Ms7yLzuCv`); [Background Generator: Elves](../../packsJson/character-generator/Background_Generator__Elves_L8o8Rz85um05VUW4.json) (`L8o8Rz85um05VUW4`); [Origin: Elderland](../../packsJson/character-generator-sub-tables/Origin__Elderland_f17QrlT4P5u8m65o.json) (`f17QrlT4P5u8m65o`).

Книжный выбор Human Lands остаётся допустимым для non-human; два генератора сразу назначают Dol Blathanna/Mahakam. Это ограниченный сценарий генератора, не неверный бонус этих земель. Отдельный Elderland 1d2 случайно выбирает одну из земель; в базовой книге выбор традиционной земли привязан к расе. Решить, нужны ли общие генераторы всех разрешённых происхождений или явная пометка ограниченного сценария.

<a id="a03"></a>

### A03 — RandomCharacter, Halfling/Gnome/Noble и случайные профессии

Источник для сравнения: [с. 20](compendium-core-rulebook-reference.md#page-20). Файлы: [Background Generator: RandomCharacter](../../packsJson/character-generator/Background_Generator__RandomCharacter_CIpykDUYYuJB0zLv.json) (`CIpykDUYYuJB0zLv`); [Background Generator: Halfling](../../packsJson/character-generator/Background_Generator__Halfling_ioZTpiW6W2eVwRiY.json) (`ioZTpiW6W2eVwRiY`); [Dwarf / Gnome Profession](../../packsJson/character-generator-sub-tables/Dwarf___Gnome_Profession_TjKh0NMxyyYxjSDt.json) (`TjKh0NMxyyYxjSDt`); [Elf Profession](../../packsJson/character-generator-sub-tables/Elf_Profession_zEykV0pe3YUlaDTd.json) (`zEykV0pe3YUlaDTd`); [Human Profession](../../packsJson/character-generator-sub-tables/Human_Profession_ZSSaEVLn53BVQ77b.json) (`ZSSaEVLn53BVQ77b`); [Siblings: Dwarves/Halflings](../../packsJson/character-generator-sub-tables/Siblings__Dwarves_Halflings_Ty1Hs3G4BXkkTu67.json) (`Ty1Hs3G4BXkkTu67`).

Базовая книга предлагает выбирать расу/профессию, четыре playable races на с. 21; таблицы вероятностей 1d15 и случайных профессий не найдены. Halfling, Gnome и Noble в этих генераторах нельзя подтвердить как варианты базовой книги; источники дополнений здесь не установлены. Halfling всегда вызывает Elderland Family and Parents даже после Human Lands — внутреннюю согласованность проверить после выбора источника. Не удалять дополнительный контент по одному отсутствию в core.

<a id="a04"></a>

### A04 — Школа Cat и написание имён отличаются от старого PDF

Источник для сравнения: [с. 238](compendium-core-rulebook-reference.md#page-238). Файлы: [Witcher Background: What School Did You Train In?](../../packsJson/witcher-lifepath/Witcher_Background__What_School_Did_You_Train_In__kEqyptPU1X7TvKc1.json) (`kEqyptPU1X7TvKc1`).

В JSON Cat: Immune to Non-Magical Charm Attempts, в PDF Immune to Charm Attempts. JSON Dyn Marv / Gorthwr Gvaed / Haern Cadvch; PDF Dyn Marw / Gorthwr Gwaed / Haern Cadwch. Различия реальны; более поздняя редакция/errata не проверена. До выбора источника не отменять ограничение Non-Magical как якобы доказанную ошибку.

<a id="a05"></a>

### A05 — Vehicle Control Loss: Swimming заменено Athletics

Источник для сравнения: [с. 169](compendium-core-rulebook-reference.md#page-169). Файлы: [Vehicle Control Loss](../../packsJson/combat/Vehicle_Control_Loss_zO7eKgtDOAH0qnow.json) (`zO7eKgtDOAH0qnow`).

В PDF результат 5–6 требует DC12 Swimming, в JSON DC12 Athletics. Это может быть адаптацией к перечню навыков/исправлением старой редакции. Числа 5d6/×3 совпадают с книгой; не возвращать несуществующий ключ навыка без отдельного решения. Окончание книжного текста swim out and up в JSON сокращено.

<a id="a06"></a>

### A06 — Первоисточник числовой таблицы Scatter не установлен

Источник для сравнения: [с. 163](compendium-core-rulebook-reference.md#page-163). Файлы: [Scatter: Direction and Distance](../../packsJson/combat/Scatter__Direction_and_Distance_qTOHZYKhe5GN3Ciw.json) (`qTOHZYKhe5GN3Ciw`).

В JSON десять направлений с дистанцией 1d6. В текстовом слое всего PDF найдены ссылки на Scatter на с. 157,163,165; сами десять строк не установлены. С. 165 визуально проверена: там ссылка, но нет таблицы. С. 163 отдельно задаёт 1d6/2 при безоружном и 1d6 при вооружённом обезоруживании: универсальная дистанция из compendium не должна подменять контекст. Источник направлений остаётся открытым; не объявлять их книжными или ошибочными без основания.

<a id="a07"></a>

### A07 — Trials расширяет крайние ячейки за пределы 1–10

Источник для сравнения: [с. 239](compendium-core-rulebook-reference.md#page-239). Файлы: [Witcher Background: How Did Your Trials Go? -2](../../packsJson/witcher-lifepath/Witcher_Background__How_Did_Your_Trials_Go___2_CDX4hqsxcxxovYz3.json) (`CDX4hqsxcxxovYz3`); [Witcher Background: How Did Your Trials Go? +2](../../packsJson/witcher-lifepath/Witcher_Background__How_Did_Your_Trials_Go___2_zNG1R1HQoY6tpSLz.json) (`zNG1R1HQoY6tpSLz`); [Witcher Background: How Did Your Trials Go? +4](../../packsJson/witcher-lifepath/Witcher_Background__How_Did_Your_Trials_Go___4_GknRX1nkVVcc9rCK.json) (`GknRX1nkVVcc9rCK`); [Witcher Background: How Did Your Trials Go? -4](../../packsJson/witcher-lifepath/Witcher_Background__How_Did_Your_Trials_Go___4_sY3qw9UfVyx1l9BF.json) (`sY3qw9UfVyx1l9BF`); [Witcher Background: How Did Your Trials Go?](../../packsJson/witcher-lifepath/Witcher_Background__How_Did_Your_Trials_Go__vaUFKIYBmEbJotfJ.json) (`vaUFKIYBmEbJotfJ`).

Все пять таблиц имеют крайние диапазоны −3..1 и 10..14; PDF печатает только 1, 2–3, 4–9, 10. Это осмысленная адаптация для суммы модификаторов −4..+4, не доказанная ошибка. Зафиксировать принятое правило крайних значений; не обрезать диапазоны и не создавать отсутствие результатов.

<a id="a08"></a>

### A08 — Двухисходные d2 переворачивают названия чётности

Источник для сравнения: [с. 25](compendium-core-rulebook-reference.md#page-25). Файлы: [Enemies: Who Was Wronged](../../packsJson/lifepath/Enemies__Who_Was_Wronged_cz5KlvgE7I7QV57H.json) (`cz5KlvgE7I7QV57H`); [Family and Parents: Elderland](../../packsJson/character-generator-sub-tables/Family_and_Parents__Elderland_d7NLtNEdvkagBLOP.json) (`d7NLtNEdvkagBLOP`); [Family and Parents: Nilfgaard](../../packsJson/character-generator-sub-tables/Family_and_Parents__Nilfgaard_5OcHT6WrJ8pL9cYp.json) (`5OcHT6WrJ8pL9cYp`); [Family and Parents: Northern](../../packsJson/character-generator-sub-tables/Family_and_Parents__Northern_xAVQucslVR12q2kc.json) (`xAVQucslVR12q2kc`); [Parents: Elderland](../../packsJson/character-generator-sub-tables/Parents__Elderland_zSTMrICDELIRaNyL.json) (`zSTMrICDELIRaNyL`); [Parents: Nilfgaard](../../packsJson/character-generator-sub-tables/Parents__Nilfgaard_Nnf1BMSJOnc5Mx3m.json) (`Nnf1BMSJOnc5Mx3m`); [Parents: Northern](../../packsJson/character-generator-sub-tables/Parents__Northern_SGuXziIZzzst1LVJ.json) (`SGuXziIZzzst1LVJ`); [Background Generator: Dwarves](../../packsJson/character-generator/Background_Generator__Dwarves_PCAssN2Ms7yLzuCv.json) (`PCAssN2Ms7yLzuCv`); [Background Generator: Elves](../../packsJson/character-generator/Background_Generator__Elves_L8o8Rz85um05VUW4.json) (`L8o8Rz85um05VUW4`).

В книге Family/Parents: even живы, odd несчастье; здесь 1 живы, 2 несчастье. В Who Was Wronged (с. 34) even означает обидели вас, в JSON это 1. Равные вероятности и независимые события сохраняются. Различать буквальное воспроизведение номера и сохранение распределения; не считать d2 вместо odd/even ошибкой само по себе.

<a id="a09"></a>

### A09 — Дополнительные колонки ведьмачьих NPC и родитель Nilfgaard №1

Источник для сравнения: [с. 243](compendium-core-rulebook-reference.md#page-243). Файлы: [Witcher Lifepath: Allies - Where Are They?](../../packsJson/witcher-lifepath/Witcher_Lifepath__Allies___Where_Are_They__LPwYvTqPg52QQ9IU.json) (`LPwYvTqPg52QQ9IU`); [Witcher Lifepath: Danger - Enemies: Power](../../packsJson/witcher-lifepath/Witcher_Lifepath__Danger___Enemies__Power_1QUG4e60Iqom24ac.json) (`1QUG4e60Iqom24ac`); [Parental Fate: Nilfgaard](../../packsJson/character-generator-sub-tables/Parental_Fate__Nilfgaard_wFuCDleU9PzP00mf.json) (`wFuCDleU9PzP00mf`).

Where Are They у ведьмачьего друга честно помечена Optional/not included; это перенос с. 33, не колонка с. 243. Числовой Power 1–10 у врагов ведьмака заимствован из обычного Lifepath с. 34, на с. 245 есть лишь тип силы. Nilfgaard Parental Fate №1 в PDF Father died, в JSON One or more of your parents, плюс общий Which Parent. Сохранить расширения или воспроизводить базовые формулировки дословно — согласовать; не исправлять по умолчанию.

## Условия книги на границе механик — issue-00332

Эти наблюдения не превращают контентную задачу в рефакторинг движка:

- **Условная Awareness.** Damaged Eye в описании ограничена зрением (с. 160), но changes адресуют общий `awareness.activeEffectModifiers`. Нельзя объявлять штраф слуха/обоняния книжным. Реализация условий требует анализа потребителя; в 00331 можно сохранить точное условие текстом.
- **Все действия.** Torn Stomach задаёт −2/−2/−1 ко всем действиям (с. 159), а JSON перечисляет навыки, включая неверный `commonspeech`. Исполнение и полнота профессиональных/характеристических бросков относятся к issue-00004 и механикам; эта сверка не утверждает, что перечень skills реализует все действия.
- **Вычисление характеристик и времени.** Cracked Ribs не влияет на HP; Foreign Object изменяет Recovery и Critical Healing; постоянные последствия Deadly и протезы не равны обычному сроку удаления травмы. Хранение `healingTime=0` в шаблоне само по себе не противоречит таблице сроков: срок определяется при использовании. Не менять числа по одному полю шаблона.
- **Максимумы и периодический урон.** Числа ¼, ½, bleed 2, poison 3, suffocation 3, acid 4 читаются в книге; они не подтверждают работоспособность `.max` и объектного ADD. Уже выделены issue-00036, issue-00021 и issue-00328. У treated рук сначала надо исправить ошибочный состав B08, а не заставлять все 16 текущих объектов безусловно исполняться.
- **Анатомические исключения, мгновенная смерть, периодические Stun saves и сохранение permanent** — правила с. 159–162/174, а не основание автоматически добавлять новый обработчик или новые типы Item в этой задаче.

[issue-00320 и issue-00328 остаются в механиках](../issues/open/issue-00332.md). Сборка, воспроизводимость и установка библиотек относятся к [issue-00333](../issues/open/issue-00333.md).

## Что совпало и не требует изменения по этой сверке

- Четыре уровня Combat имеют шесть книжных исходов с диапазонами 2–3, 4–5, 6–8, 9–10, 11, 12; исключение текста treated ноги вынесено в B06. Отличия описаний и автоматики травм рассматривались отдельно.
- Human Damage Location полностью совпадает по диапазонам, прицельным штрафам и множителям.
- Все 70 Style/Values результатов совпадают по содержанию и порядку.
- Northern/Vassal/Nilfgaard origin: диапазоны и навыковые +1 совпадают; Family Status: семь диапазонов и стартовые награды всех трёх регионов совпадают; Influential Friend: 30 пар влияния/предмета совпадают. Тексты Family Fate соответствуют региональным колонкам; дефект B03 именно в продолжении.
- Число siblings, Age, Feelings, Personality и Which Parent совпадают; Gender выделена в A01.
- Романтика, положение/знакомство/близость обычных союзников и содержание причин/силы/эскалации обычных врагов совпадают; преобразование odd/even отдельно в A08.
- Вероятности опасности 10/25/50/75% и все Outcome-диапазоны четырёх десятилетий совпадают. «Высокие» процентили вместо «низких» сохраняют вероятность. После Danger контейнеры также вызывают Outcome.
- Результаты Early Training, Trials в книжном диапазоне, Important Event, Where Are You Now, охотничьих колонок, Danger Events/Wounds соответствуют строкам книги по смыслу и числам. Пропущенные сопутствующие условия и ошибочные ссылки не отменяются этим совпадением.
- Проценты смертности и таблицы причин смерти ведьмачьих друзей/врагов совпадают; срок смерти друга пропущен (B10).
- Цепочки followUp всех 31 допускающих лечение исходных травм разрешаются и достигают treated без циклов. У всех 94 уровни/состояния соответствуют группе книжной строки; ошибочные локации и отдельные effects перечислены отдельно. Числовая симметрия правой/левой формы не выдержана для Fractured Leg treated (B07), остальное не означает гарантии исполнения.

## Порядок исправления и проверки

Актуальный [единый план ошибок К01](../issues/closed/issue-00331.md#k01), оформленный в .00015, объединяет старые issues и B01–B17 без дублирования. A01–A09 исключены и не блокируют реализацию. Точный перечень файлов и ограниченный состав B17 приведены в плане; текущий документ сохраняет исходную сверку .00014. Порядок: обычный Lifepath → Witcher Lifepath → Combat → criticalWounds → итоговая сверка. Ожидаемые значения брать из независимой выписки, а не из исправленного JSON.

Исходные рекомендации проверки (точный актуальный объём — в едином плане):

1. Пройти все 10 значений Life Event и обе ветки вложенного d2; проверить распределение 20/20/15/15/30 без случайного статистического теста.
2. Для трёх регионов пройти Family Fate 1–10, Parental Fate 1–10, обе семейные ветки; Status/Friend появляются ровно один раз. Заранее учесть известную глубину рекурсии issue-00320: исправленные ссылки не являются решением лимита Foundry.
3. Для Trials проверить матрицу 3 возрастов × 10 исходов обучения, а не только +4/−4; крайние диапазоны A07 сохраняются без изменения.
4. Для всех 10 значений Monster Damage Location получить ровно одну ожидаемую локацию; отдельно 5,9,10. Mounted вызывает ровно Personal и Mount, с независимыми бросками.
5. Проверить семь исправленных inline-формул настоящим Roll Foundry 14; ожидаемые границы ×100 — 100..1000, ×10 — 10..60, ×2 — 2..20, ×3 — 3..30.
6. Для изменённых травм сверить none/stabilized/treated, сторону, числовые значения, отсутствие bleed после лечения рук и постоянные/условные оговорки. Игровую применимость ждать от категории механик; простая проверка JSON её не доказывает.
7. После отдельного разрешения собрать затронутые packs во временное место, выполнить обратное извлечение и сравнение JSON/ID/UUID. Установка и права — отдельный этап, не побочный эффект анализа.
8. Обновить только карточки и записи справочника затронутых файлов, выполнить один `check --freshness`; полный повторный прогон справочника и всех игровых сценариев не нужен для этой Markdown-аналитики.

## Реестр покрытия всех 226 JSON

Здесь каждому документу назначен книжный раздел и предел вывода. «Сверены записанные значения» не означает исполнения в Foundry. ID B/A ведут к наблюдениям выше. Для Folder нет отдельной таблицы правил. Указаны **все** источники, а не только файлы с дефектами.

### character-generator

| Документ / путь к JSON | Тип / объём | Книга | Результат сопоставления |
| --- | --- | --- | --- |
| [Background Generator: Dwarves](../../packsJson/character-generator/Background_Generator__Dwarves_PCAssN2Ms7yLzuCv.json) (`PCAssN2Ms7yLzuCv`) | RollTable; 8 результатов | [с. 20](compendium-core-rulebook-reference.md#page-20), [с. 25](compendium-core-rulebook-reference.md#page-25), [с. 26](compendium-core-rulebook-reference.md#page-26), [с. 27](compendium-core-rulebook-reference.md#page-27), [с. 28](compendium-core-rulebook-reference.md#page-28), [с. 29](compendium-core-rulebook-reference.md#page-29), [с. 30](compendium-core-rulebook-reference.md#page-30), [с. 37](compendium-core-rulebook-reference.md#page-37) | [B03](#b03), [A02](#a02), [A08](#a08) |
| [Background Generator: Elves](../../packsJson/character-generator/Background_Generator__Elves_L8o8Rz85um05VUW4.json) (`L8o8Rz85um05VUW4`) | RollTable; 8 результатов | [с. 20](compendium-core-rulebook-reference.md#page-20), [с. 25](compendium-core-rulebook-reference.md#page-25), [с. 26](compendium-core-rulebook-reference.md#page-26), [с. 27](compendium-core-rulebook-reference.md#page-27), [с. 28](compendium-core-rulebook-reference.md#page-28), [с. 29](compendium-core-rulebook-reference.md#page-29), [с. 30](compendium-core-rulebook-reference.md#page-30), [с. 37](compendium-core-rulebook-reference.md#page-37) | [B03](#b03), [A02](#a02), [A08](#a08) |
| [Background Generator: Halfling](../../packsJson/character-generator/Background_Generator__Halfling_ioZTpiW6W2eVwRiY.json) (`ioZTpiW6W2eVwRiY`) | RollTable; 8 результатов | [с. 20](compendium-core-rulebook-reference.md#page-20), [с. 25](compendium-core-rulebook-reference.md#page-25), [с. 26](compendium-core-rulebook-reference.md#page-26), [с. 27](compendium-core-rulebook-reference.md#page-27), [с. 28](compendium-core-rulebook-reference.md#page-28), [с. 29](compendium-core-rulebook-reference.md#page-29), [с. 30](compendium-core-rulebook-reference.md#page-30), [с. 37](compendium-core-rulebook-reference.md#page-37) | [A03](#a03) |
| [Background Generator: Human](../../packsJson/character-generator/Background_Generator__Human_g9I3DpPOi5CfOFBz.json) (`g9I3DpPOi5CfOFBz`) | RollTable; 9 результатов | [с. 20](compendium-core-rulebook-reference.md#page-20), [с. 25](compendium-core-rulebook-reference.md#page-25), [с. 26](compendium-core-rulebook-reference.md#page-26), [с. 27](compendium-core-rulebook-reference.md#page-27), [с. 28](compendium-core-rulebook-reference.md#page-28), [с. 29](compendium-core-rulebook-reference.md#page-29), [с. 30](compendium-core-rulebook-reference.md#page-30), [с. 37](compendium-core-rulebook-reference.md#page-37) | Сверены тексты/диапазоны и ссылки; новых расхождений не выделено |
| [Background Generator: RandomCharacter](../../packsJson/character-generator/Background_Generator__RandomCharacter_CIpykDUYYuJB0zLv.json) (`CIpykDUYYuJB0zLv`) | RollTable; 10 результатов | [с. 20](compendium-core-rulebook-reference.md#page-20), [с. 25](compendium-core-rulebook-reference.md#page-25), [с. 26](compendium-core-rulebook-reference.md#page-26), [с. 27](compendium-core-rulebook-reference.md#page-27), [с. 28](compendium-core-rulebook-reference.md#page-28), [с. 29](compendium-core-rulebook-reference.md#page-29), [с. 30](compendium-core-rulebook-reference.md#page-30), [с. 37](compendium-core-rulebook-reference.md#page-37) | [A03](#a03) |
| [Life Event Generator](../../packsJson/character-generator/Life_Event_Generator_4Y8IpS3ArbbP2gGc.json) (`4Y8IpS3ArbbP2gGc`) | RollTable; 3 результата | [с. 31](compendium-core-rulebook-reference.md#page-31), [с. 32](compendium-core-rulebook-reference.md#page-32), [с. 33](compendium-core-rulebook-reference.md#page-33), [с. 35](compendium-core-rulebook-reference.md#page-35) | [B01](#b01) |
| [Siblings Generator](../../packsJson/character-generator/Siblings_Generator_Lem0B3XxmJeEVQms.json) (`Lem0B3XxmJeEVQms`) | RollTable; 4 результата | [с. 30](compendium-core-rulebook-reference.md#page-30) | Сверены тексты/диапазоны и ссылки; новых расхождений не выделено |
| [Style and Values](../../packsJson/character-generator/Style_and_Values_CjaIcLRWSlzwI6ly.json) (`CjaIcLRWSlzwI6ly`) | RollTable; 7 результатов | [с. 36](compendium-core-rulebook-reference.md#page-36) | Сверены тексты/диапазоны и ссылки; новых расхождений не выделено |
| [Witcher Background Generator](../../packsJson/character-generator/Witcher_Background_Generator_C5d6zkIMvS9gDWEN.json) (`C5d6zkIMvS9gDWEN`) | RollTable; 9 результатов | [с. 238](compendium-core-rulebook-reference.md#page-238), [с. 239](compendium-core-rulebook-reference.md#page-239), [с. 240](compendium-core-rulebook-reference.md#page-240) | Сверены тексты/диапазоны и ссылки; новых расхождений не выделено |
| [Witcher Lifepath: Cautious Decade](../../packsJson/character-generator/Witcher_Lifepath__Cautious_Decade_09MXduRik0BKuUqa.json) (`09MXduRik0BKuUqa`) | RollTable; 5 результатов | [с. 241](compendium-core-rulebook-reference.md#page-241) | Сверены тексты/диапазоны и ссылки; новых расхождений не выделено |
| [Witcher Lifepath: Non-Neutral Decade](../../packsJson/character-generator/Witcher_Lifepath__Non_Neutral_Decade_obLsbuoNixBUbeAy.json) (`obLsbuoNixBUbeAy`) | RollTable; 5 результатов | [с. 241](compendium-core-rulebook-reference.md#page-241) | Сверены тексты/диапазоны и ссылки; новых расхождений не выделено |
| [Witcher Lifepath: Normal Decade](../../packsJson/character-generator/Witcher_Lifepath__Normal_Decade_dsvsdl2GfKCWKsEO.json) (`dsvsdl2GfKCWKsEO`) | RollTable; 5 результатов | [с. 241](compendium-core-rulebook-reference.md#page-241) | Сверены тексты/диапазоны и ссылки; новых расхождений не выделено |
| [Witcher Lifepath: Risky Decade](../../packsJson/character-generator/Witcher_Lifepath__Risky_Decade_6zn78Gj7lZtJfS90.json) (`6zn78Gj7lZtJfS90`) | RollTable; 5 результатов | [с. 241](compendium-core-rulebook-reference.md#page-241) | Сверены тексты/диапазоны и ссылки; новых расхождений не выделено |

### character-generator-sub-tables

| Документ / путь к JSON | Тип / объём | Книга | Результат сопоставления |
| --- | --- | --- | --- |
| [Dwarf / Gnome Profession](../../packsJson/character-generator-sub-tables/Dwarf___Gnome_Profession_TjKh0NMxyyYxjSDt.json) (`TjKh0NMxyyYxjSDt`) | RollTable; 7 результатов | [с. 20](compendium-core-rulebook-reference.md#page-20), [с. 37](compendium-core-rulebook-reference.md#page-37) | [A03](#a03) |
| [Elf Profession](../../packsJson/character-generator-sub-tables/Elf_Profession_zEykV0pe3YUlaDTd.json) (`zEykV0pe3YUlaDTd`) | RollTable; 9 результатов | [с. 20](compendium-core-rulebook-reference.md#page-20), [с. 37](compendium-core-rulebook-reference.md#page-37) | [A03](#a03) |
| [Family Fate: Elderland](../../packsJson/character-generator-sub-tables/Family_Fate__Elderland_W6mgmCP3219eYdf0.json) (`W6mgmCP3219eYdf0`) | RollTable; 10 результатов | [с. 26](compendium-core-rulebook-reference.md#page-26) | [B03](#b03) |
| [Family Fate: Nilfgaard](../../packsJson/character-generator-sub-tables/Family_Fate__Nilfgaard_VstrJuRw43OKcuGr.json) (`VstrJuRw43OKcuGr`) | RollTable; 10 результатов | [с. 26](compendium-core-rulebook-reference.md#page-26) | [B03](#b03) |
| [Family Fate: Northern](../../packsJson/character-generator-sub-tables/Family_Fate__Northern_CN0lwXPHxkV2vDeY.json) (`CN0lwXPHxkV2vDeY`) | RollTable; 19 результатов | [с. 26](compendium-core-rulebook-reference.md#page-26) | [B03](#b03) |
| [Family Status: Elderland](../../packsJson/character-generator-sub-tables/Family_Status__Elderland_GOp8mGE4MiGaqjk2.json) (`GOp8mGE4MiGaqjk2`) | RollTable; 14 результатов | [с. 28](compendium-core-rulebook-reference.md#page-28) | Сверены тексты/диапазоны и ссылки; новых расхождений не выделено |
| [Family Status: Nilfgaard](../../packsJson/character-generator-sub-tables/Family_Status__Nilfgaard_6WXA7KAOHjeqCCRn.json) (`6WXA7KAOHjeqCCRn`) | RollTable; 14 результатов | [с. 28](compendium-core-rulebook-reference.md#page-28) | Сверены тексты/диапазоны и ссылки; новых расхождений не выделено |
| [Family Status: Northern](../../packsJson/character-generator-sub-tables/Family_Status__Northern_EeOlp8UMRiYS1AEt.json) (`EeOlp8UMRiYS1AEt`) | RollTable; 14 результатов | [с. 28](compendium-core-rulebook-reference.md#page-28) | Сверены тексты/диапазоны и ссылки; новых расхождений не выделено |
| [Family and Parents: Elderland](../../packsJson/character-generator-sub-tables/Family_and_Parents__Elderland_d7NLtNEdvkagBLOP.json) (`d7NLtNEdvkagBLOP`) | RollTable; 5 результатов | [с. 25](compendium-core-rulebook-reference.md#page-25) | [B03](#b03), [A08](#a08) |
| [Family and Parents: Nilfgaard](../../packsJson/character-generator-sub-tables/Family_and_Parents__Nilfgaard_5OcHT6WrJ8pL9cYp.json) (`5OcHT6WrJ8pL9cYp`) | RollTable; 5 результатов | [с. 25](compendium-core-rulebook-reference.md#page-25) | [B03](#b03), [A08](#a08) |
| [Family and Parents: Northern](../../packsJson/character-generator-sub-tables/Family_and_Parents__Northern_xAVQucslVR12q2kc.json) (`xAVQucslVR12q2kc`) | RollTable; 4 результата | [с. 25](compendium-core-rulebook-reference.md#page-25) | [B03](#b03), [A08](#a08) |
| [Human Profession](../../packsJson/character-generator-sub-tables/Human_Profession_ZSSaEVLn53BVQ77b.json) (`ZSSaEVLn53BVQ77b`) | RollTable; 9 результатов | [с. 20](compendium-core-rulebook-reference.md#page-20), [с. 37](compendium-core-rulebook-reference.md#page-37) | [A03](#a03) |
| [Most Influential Friend: Elderland](../../packsJson/character-generator-sub-tables/Most_Influential_Friend__Elderland_eATe1gk2PaKG1K9r.json) (`eATe1gk2PaKG1K9r`) | RollTable; 10 результатов | [с. 29](compendium-core-rulebook-reference.md#page-29) | Сверены тексты/диапазоны и ссылки; новых расхождений не выделено |
| [Most Influential Friend: Nilfgaard](../../packsJson/character-generator-sub-tables/Most_Influential_Friend__Nilfgaard_8R2zAqegJcbDr4xB.json) (`8R2zAqegJcbDr4xB`) | RollTable; 10 результатов | [с. 29](compendium-core-rulebook-reference.md#page-29) | Сверены тексты/диапазоны и ссылки; новых расхождений не выделено |
| [Most Influential Friend: Northern](../../packsJson/character-generator-sub-tables/Most_Influential_Friend__Northern_Xc9k6o8pE8Aaj1Kb.json) (`Xc9k6o8pE8Aaj1Kb`) | RollTable; 10 результатов | [с. 29](compendium-core-rulebook-reference.md#page-29) | Сверены тексты/диапазоны и ссылки; новых расхождений не выделено |
| [Nilfgaard Vassal Origin](../../packsJson/character-generator-sub-tables/Nilfgaard_Vassal_Origin_IEPMPHNGahrfyCWI.json) (`IEPMPHNGahrfyCWI`) | RollTable; 10 результатов | [с. 25](compendium-core-rulebook-reference.md#page-25) | Сверены тексты/диапазоны и ссылки; новых расхождений не выделено |
| [Origin: Elderland](../../packsJson/character-generator-sub-tables/Origin__Elderland_f17QrlT4P5u8m65o.json) (`f17QrlT4P5u8m65o`) | RollTable; 2 результата | [с. 25](compendium-core-rulebook-reference.md#page-25) | [A02](#a02) |
| [Origin: Human Lands](../../packsJson/character-generator-sub-tables/Origin__Human_Lands_de64KicDG5R7FFO9.json) (`de64KicDG5R7FFO9`) | RollTable; 2 результата | [с. 25](compendium-core-rulebook-reference.md#page-25) | Сверены тексты/диапазоны и ссылки; новых расхождений не выделено |
| [Origin: Nilfgaard](../../packsJson/character-generator-sub-tables/Origin__Nilfgaard_DAfZ8BGKmclyyFYc.json) (`DAfZ8BGKmclyyFYc`) | RollTable; 3 результата | [с. 25](compendium-core-rulebook-reference.md#page-25) | Сверены тексты/диапазоны и ссылки; новых расхождений не выделено |
| [Origin: Northern Kingdom](../../packsJson/character-generator-sub-tables/Origin__Northern_Kingdom_u0EwVGZtkHA4Knoa.json) (`u0EwVGZtkHA4Knoa`) | RollTable; 10 результатов | [с. 25](compendium-core-rulebook-reference.md#page-25) | Сверены тексты/диапазоны и ссылки; новых расхождений не выделено |
| [Parental Fate: Elderland](../../packsJson/character-generator-sub-tables/Parental_Fate__Elderland_jZVPaCIoQxFZiyRu.json) (`jZVPaCIoQxFZiyRu`) | RollTable; 21 результат | [с. 27](compendium-core-rulebook-reference.md#page-27) | [B02](#b02) |
| [Parental Fate: Nilfgaard](../../packsJson/character-generator-sub-tables/Parental_Fate__Nilfgaard_wFuCDleU9PzP00mf.json) (`wFuCDleU9PzP00mf`) | RollTable; 20 результатов | [с. 27](compendium-core-rulebook-reference.md#page-27) | [B04](#b04), [A09](#a09) |
| [Parental Fate: Northern](../../packsJson/character-generator-sub-tables/Parental_Fate__Northern_FQEyr6n57ae1ySLC.json) (`FQEyr6n57ae1ySLC`) | RollTable; 21 результат | [с. 27](compendium-core-rulebook-reference.md#page-27) | Сверены тексты/диапазоны и ссылки; новых расхождений не выделено |
| [Parents: Elderland](../../packsJson/character-generator-sub-tables/Parents__Elderland_zSTMrICDELIRaNyL.json) (`zSTMrICDELIRaNyL`) | RollTable; 4 результата | [с. 25](compendium-core-rulebook-reference.md#page-25) | [A08](#a08) |
| [Parents: Nilfgaard](../../packsJson/character-generator-sub-tables/Parents__Nilfgaard_Nnf1BMSJOnc5Mx3m.json) (`Nnf1BMSJOnc5Mx3m`) | RollTable; 4 результата | [с. 25](compendium-core-rulebook-reference.md#page-25) | [A08](#a08) |
| [Parents: Northern](../../packsJson/character-generator-sub-tables/Parents__Northern_SGuXziIZzzst1LVJ.json) (`SGuXziIZzzst1LVJ`) | RollTable; 4 результата | [с. 25](compendium-core-rulebook-reference.md#page-25) | [A08](#a08) |
| [Siblings: Age](../../packsJson/character-generator-sub-tables/Siblings__Age_0PcW1kFO5g40cELc.json) (`0PcW1kFO5g40cELc`) | RollTable; 3 результата | [с. 30](compendium-core-rulebook-reference.md#page-30) | Сверены тексты/диапазоны и ссылки; новых расхождений не выделено |
| [Siblings: Dwarves/Halflings](../../packsJson/character-generator-sub-tables/Siblings__Dwarves_Halflings_Ty1Hs3G4BXkkTu67.json) (`Ty1Hs3G4BXkkTu67`) | RollTable; 10 результатов | [с. 30](compendium-core-rulebook-reference.md#page-30) | [A03](#a03) |
| [Siblings: Elves](../../packsJson/character-generator-sub-tables/Siblings__Elves_6QuZTatyIKElcCKz.json) (`6QuZTatyIKElcCKz`) | RollTable; 3 результата | [с. 30](compendium-core-rulebook-reference.md#page-30) | Сверены тексты/диапазоны и ссылки; новых расхождений не выделено |
| [Siblings: Feelings About You](../../packsJson/character-generator-sub-tables/Siblings__Feelings_About_You_ACf1JfCfVtJWw5DG.json) (`ACf1JfCfVtJWw5DG`) | RollTable; 10 результатов | [с. 30](compendium-core-rulebook-reference.md#page-30) | Сверены тексты/диапазоны и ссылки; новых расхождений не выделено |
| [Siblings: Gender](../../packsJson/character-generator-sub-tables/Siblings__Gender_QbkrG0W11fREICK8.json) (`QbkrG0W11fREICK8`) | RollTable; 3 результата | [с. 30](compendium-core-rulebook-reference.md#page-30) | [A01](#a01) |
| [Siblings: Nilfgaard](../../packsJson/character-generator-sub-tables/Siblings__Nilfgaard_Vw40FuwmhTGp7Q4V.json) (`Vw40FuwmhTGp7Q4V`) | RollTable; 10 результатов | [с. 30](compendium-core-rulebook-reference.md#page-30) | Сверены тексты/диапазоны и ссылки; новых расхождений не выделено |
| [Siblings: Northern](../../packsJson/character-generator-sub-tables/Siblings__Northern_rLxCo0JWiGvTlapE.json) (`rLxCo0JWiGvTlapE`) | RollTable; 10 результатов | [с. 30](compendium-core-rulebook-reference.md#page-30) | Сверены тексты/диапазоны и ссылки; новых расхождений не выделено |
| [Siblings: Personality](../../packsJson/character-generator-sub-tables/Siblings__Personality_zNQCbwyK1biYFszn.json) (`zNQCbwyK1biYFszn`) | RollTable; 10 результатов | [с. 30](compendium-core-rulebook-reference.md#page-30) | Сверены тексты/диапазоны и ссылки; новых расхождений не выделено |
| [Which Parent](../../packsJson/character-generator-sub-tables/Which_Parent_7fAXpaJLFwlWxkWX.json) (`7fAXpaJLFwlWxkWX`) | RollTable; 3 результата | [с. 27](compendium-core-rulebook-reference.md#page-27) | Сверены тексты/диапазоны и ссылки; новых расхождений не выделено |

### combat

| Документ / путь к JSON | Тип / объём | Книга | Результат сопоставления |
| --- | --- | --- | --- |
| [Complex Critical](../../packsJson/combat/Complex_Critical_p3EAPCnu8RDawpWR.json) (`p3EAPCnu8RDawpWR`) | RollTable; 6 результатов | [с. 159](compendium-core-rulebook-reference.md#page-159) | Сверены тексты/диапазоны и ссылки; новых расхождений не выделено |
| [Deadly Critical](../../packsJson/combat/Deadly_Critical_GoXapMH54rEUWaZn.json) (`GoXapMH54rEUWaZn`) | RollTable; 6 результатов | [с. 160](compendium-core-rulebook-reference.md#page-160) | Сверены тексты/диапазоны и ссылки; новых расхождений не выделено |
| [Difficult Critical](../../packsJson/combat/Difficult_Critical_VIup1SZTMKCSGGbT.json) (`VIup1SZTMKCSGGbT`) | RollTable; 6 результатов | [с. 159](compendium-core-rulebook-reference.md#page-159), [с. 160](compendium-core-rulebook-reference.md#page-160) | [B06](#b06) |
| [Human Damage Location](../../packsJson/combat/Human_Damage_Location_jKFIdFvv4P49JXPU.json) (`jKFIdFvv4P49JXPU`) | RollTable; 6 результатов | [с. 154](compendium-core-rulebook-reference.md#page-154) | Сверены тексты/диапазоны и ссылки; новых расхождений не выделено |
| [Monster Damage Location](../../packsJson/combat/Monster_Damage_Location_KYyK6F8JHhA3hOu7.json) (`KYyK6F8JHhA3hOu7`) | RollTable; 5 результатов | [с. 154](compendium-core-rulebook-reference.md#page-154) | [B05](#b05) |
| [Mounted Control Loss](../../packsJson/combat/Mounted_Control_Loss_VVb2zLR4NLdMLVQQ.json) (`VVb2zLR4NLdMLVQQ`) | RollTable; 2 результата | [с. 169](compendium-core-rulebook-reference.md#page-169), [с. 170](compendium-core-rulebook-reference.md#page-170) | [B13](#b13) |
| [Mounted Control Loss: Mount](../../packsJson/combat/Mounted_Control_Loss__Mount_XRdHZOmutZ3yzGRe.json) (`XRdHZOmutZ3yzGRe`) | RollTable; 8 результатов | [с. 169](compendium-core-rulebook-reference.md#page-169), [с. 170](compendium-core-rulebook-reference.md#page-170) | Сверены тексты/диапазоны и ссылки; новых расхождений не выделено |
| [Mounted Control Loss: Personal](../../packsJson/combat/Mounted_Control_Loss__Personal_KWLoKiOHKXXnq5E4.json) (`KWLoKiOHKXXnq5E4`) | RollTable; 8 результатов | [с. 169](compendium-core-rulebook-reference.md#page-169), [с. 170](compendium-core-rulebook-reference.md#page-170) | Сверены тексты/диапазоны и ссылки; новых расхождений не выделено |
| [Scatter: Direction and Distance](../../packsJson/combat/Scatter__Direction_and_Distance_qTOHZYKhe5GN3Ciw.json) (`qTOHZYKhe5GN3Ciw`) | RollTable; 10 результатов | [с. 157](compendium-core-rulebook-reference.md#page-157), [с. 163](compendium-core-rulebook-reference.md#page-163), [с. 165](compendium-core-rulebook-reference.md#page-165) | [A06](#a06) |
| [Simple Critical](../../packsJson/combat/Simple_Critical_SkHR3GrB2e3Tz1v4.json) (`SkHR3GrB2e3Tz1v4`) | RollTable; 6 результатов | [с. 158](compendium-core-rulebook-reference.md#page-158) | Сверены тексты/диапазоны и ссылки; новых расхождений не выделено |
| [Vehicle Control Loss](../../packsJson/combat/Vehicle_Control_Loss_zO7eKgtDOAH0qnow.json) (`zO7eKgtDOAH0qnow`) | RollTable; 3 результата | [с. 169](compendium-core-rulebook-reference.md#page-169) | [B12](#b12), [A05](#a05) |

### criticalWounds

| Документ / путь к JSON | Тип / объём | Книга | Результат сопоставления |
| --- | --- | --- | --- |
| [Broken Ribs](../../packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Broken_Ribs_VfgJzcV75cGqsjuF.json) (`VfgJzcV75cGqsjuF`) | Item; none | [с. 159](compendium-core-rulebook-reference.md#page-159) | Сверены записанные значения; исполнение и полнота автоматизации не проверены |
| [Broken Ribs (Stabilized)](../../packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Broken_Ribs__Stabilized__4LmC6nGwRM0PpNl7.json) (`4LmC6nGwRM0PpNl7`) | Item; stabilized | [с. 159](compendium-core-rulebook-reference.md#page-159) | Сверены записанные значения; исполнение и полнота автоматизации не проверены |
| [Broken Ribs (Treated)](../../packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Broken_Ribs__Treated__77evBMjaJOlKTaRv.json) (`77evBMjaJOlKTaRv`) | Item; treated | [с. 159](compendium-core-rulebook-reference.md#page-159) | Сверены записанные значения; исполнение и полнота автоматизации не проверены |
| [Fractured Arm (Left)](../../packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Fractured_Arm__Left__Z2L7diKDSE9L7E9d.json) (`Z2L7diKDSE9L7E9d`) | Item; none | [с. 159](compendium-core-rulebook-reference.md#page-159) | Сверены записанные значения; исполнение и полнота автоматизации не проверены |
| [Fractured Arm (Left - Stabilized)](../../packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Fractured_Arm__Left___Stabilized__eCiJjDqfUyaXCW2z.json) (`eCiJjDqfUyaXCW2z`) | Item; stabilized | [с. 159](compendium-core-rulebook-reference.md#page-159) | Сверены записанные значения; исполнение и полнота автоматизации не проверены |
| [Fractured Arm (Left - Treated)](../../packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Fractured_Arm__Left___Treated__kPIkW1AXuybKZPEh.json) (`kPIkW1AXuybKZPEh`) | Item; treated | [с. 159](compendium-core-rulebook-reference.md#page-159) | Сверены записанные значения; исполнение и полнота автоматизации не проверены |
| [Fractured Arm (Right)](../../packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Fractured_Arm__Right__ZOyO6WlnMTDjzBj9.json) (`ZOyO6WlnMTDjzBj9`) | Item; none | [с. 159](compendium-core-rulebook-reference.md#page-159) | Сверены записанные значения; исполнение и полнота автоматизации не проверены |
| [Fractured Arm (Right - Stabilized)](../../packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Fractured_Arm__Right___Stabilized__t9bcLB3zDGUX9Uuq.json) (`t9bcLB3zDGUX9Uuq`) | Item; stabilized | [с. 159](compendium-core-rulebook-reference.md#page-159) | Сверены записанные значения; исполнение и полнота автоматизации не проверены |
| [Fractured Arm (Right - Treated)](../../packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Fractured_Arm__Right___Treated__djnBTcYyGVsykdoy.json) (`djnBTcYyGVsykdoy`) | Item; treated | [с. 159](compendium-core-rulebook-reference.md#page-159) | Сверены записанные значения; исполнение и полнота автоматизации не проверены |
| [Fractured Leg (Left - Stabilized)](../../packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Fractured_Leg__Left___Stabilized__LF0C1HVgY4hNZOFE.json) (`LF0C1HVgY4hNZOFE`) | Item; stabilized | [с. 159](compendium-core-rulebook-reference.md#page-159) | Сверены записанные значения; исполнение и полнота автоматизации не проверены |
| [Fractured Leg (Left - Treated)](../../packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Fractured_Leg__Left___Treated__nM9wqZXmrkFRRGTW.json) (`nM9wqZXmrkFRRGTW`) | Item; treated | [с. 159](compendium-core-rulebook-reference.md#page-159) | Сверены записанные значения; исполнение и полнота автоматизации не проверены |
| [Fractured Leg (Left)](../../packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Fractured_Leg__Left__r34NuXwHfPGZCpTu.json) (`r34NuXwHfPGZCpTu`) | Item; none | [с. 159](compendium-core-rulebook-reference.md#page-159) | Сверены записанные значения; исполнение и полнота автоматизации не проверены |
| [Fractured Leg (Right - Stabilized)](../../packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Fractured_Leg__Right___Stabilized__WNjcD3F3Hs5IdAaa.json) (`WNjcD3F3Hs5IdAaa`) | Item; stabilized | [с. 159](compendium-core-rulebook-reference.md#page-159) | [B16](#b16) |
| [Fractured Leg (Right - Treated)](../../packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Fractured_Leg__Right___Treated__Aa8wCz1OGM4gflmc.json) (`Aa8wCz1OGM4gflmc`) | Item; treated | [с. 159](compendium-core-rulebook-reference.md#page-159) | [B07](#b07), [B16](#b16) |
| [Fractured Leg (Right)](../../packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Fractured_Leg__Right__yI6kHQM8voHrBF2h.json) (`yI6kHQM8voHrBF2h`) | Item; none | [с. 159](compendium-core-rulebook-reference.md#page-159) | [B16](#b16) |
| [Lost Teeth](../../packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Lost_Teeth_IMLpjhiZ0yg6hjKI.json) (`IMLpjhiZ0yg6hjKI`) | Item; none | [с. 159](compendium-core-rulebook-reference.md#page-159) | Сверены записанные значения; исполнение и полнота автоматизации не проверены |
| [Lost Teeth (Stabilized)](../../packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Lost_Teeth__Stabilized__wccN560fe7WQgT0N.json) (`wccN560fe7WQgT0N`) | Item; stabilized | [с. 159](compendium-core-rulebook-reference.md#page-159) | Сверены записанные значения; исполнение и полнота автоматизации не проверены |
| [Lost Teeth (Treated)](../../packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Lost_Teeth__Treated__yHU7iYTocbAok2wH.json) (`yHU7iYTocbAok2wH`) | Item; treated | [с. 159](compendium-core-rulebook-reference.md#page-159) | Сверены записанные значения; исполнение и полнота автоматизации не проверены |
| [Minor Head Wound (Stabilized)](../../packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Minor_Head_Wound__Stabilized__EnwgL7ApZTdHgMbD.json) (`EnwgL7ApZTdHgMbD`) | Item; stabilized | [с. 159](compendium-core-rulebook-reference.md#page-159) | [B14](#b14) |
| [Minor Head Wound (Treated)](../../packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Minor_Head_Wound__Treated__KsYEWWO5KlPHSdCy.json) (`KsYEWWO5KlPHSdCy`) | Item; treated | [с. 159](compendium-core-rulebook-reference.md#page-159) | [B14](#b14) |
| [Minor Head Wound](../../packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Minor_Head_Wound_wPRuwd7RdLWnWmnb.json) (`wPRuwd7RdLWnWmnb`) | Item; none | [с. 159](compendium-core-rulebook-reference.md#page-159) | [B14](#b14) |
| [Ruptured Spleen (Stabilized)](../../packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Ruptured_Spleen__Stabilized__d8uhnIErEmsGtf94.json) (`d8uhnIErEmsGtf94`) | Item; stabilized | [с. 159](compendium-core-rulebook-reference.md#page-159) | Сверены записанные значения; исполнение и полнота автоматизации не проверены |
| [Ruptured Spleen (Treated)](../../packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Ruptured_Spleen__Treated__kFcie7Io28kKittg.json) (`kFcie7Io28kKittg`) | Item; treated | [с. 159](compendium-core-rulebook-reference.md#page-159) | Сверены записанные значения; исполнение и полнота автоматизации не проверены |
| [Ruptured Spleen](../../packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Ruptured_Spleen_rHrrGeB9A8bNCiC2.json) (`rHrrGeB9A8bNCiC2`) | Item; none | [с. 159](compendium-core-rulebook-reference.md#page-159) | Сверены записанные значения; исполнение и полнота автоматизации не проверены |
| [Complex](../../packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/_Folder.json) (`YcLLKtwU75uE8tdC`) | Folder | [с. 158](compendium-core-rulebook-reference.md#page-158), [с. 159](compendium-core-rulebook-reference.md#page-159), [с. 160](compendium-core-rulebook-reference.md#page-160) | Группа уровня травм; игрового результата нет |
| [Damaged Eye (Stabilized)](../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Damaged_Eye__Stabilized__LNy3P3HUw2Ja9DNu.json) (`LNy3P3HUw2Ja9DNu`) | Item; stabilized | [с. 160](compendium-core-rulebook-reference.md#page-160) | [B17](#b17) |
| [Damaged Eye (Treated)](../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Damaged_Eye__Treated__XQeXSAhvjrQZNpAE.json) (`XQeXSAhvjrQZNpAE`) | Item; treated | [с. 160](compendium-core-rulebook-reference.md#page-160) | [B17](#b17) |
| [Damaged Eye](../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Damaged_Eye_zHK1XmZ77V8c26Xv.json) (`zHK1XmZ77V8c26Xv`) | Item; none | [с. 160](compendium-core-rulebook-reference.md#page-160) | [B17](#b17) |
| [Dismembered Arm (Left)](../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Dismembered_Arm__Left__KQZRzczsSx1XY63m.json) (`KQZRzczsSx1XY63m`) | Item; none | [с. 160](compendium-core-rulebook-reference.md#page-160) | [B17](#b17) |
| [Dismembered Arm (Left - Stabilized)](../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Dismembered_Arm__Left___Stabilized__vmRDG8kxeCu3sYQC.json) (`vmRDG8kxeCu3sYQC`) | Item; stabilized | [с. 160](compendium-core-rulebook-reference.md#page-160) | Сверены записанные значения; исполнение и полнота автоматизации не проверены |
| [Dismembered Arm (Left - Treated)](../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Dismembered_Arm__Left___Treated__8Z1iHJLXrFm2i3Fb.json) (`8Z1iHJLXrFm2i3Fb`) | Item; treated | [с. 160](compendium-core-rulebook-reference.md#page-160) | Сверены записанные значения; исполнение и полнота автоматизации не проверены |
| [Dismembered Arm (Right)](../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Dismembered_Arm__Right__ZxvWPJPDD9fm34Pc.json) (`ZxvWPJPDD9fm34Pc`) | Item; none | [с. 160](compendium-core-rulebook-reference.md#page-160) | [B16](#b16), [B17](#b17) |
| [Dismembered Arm (Right - Stabilized)](../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Dismembered_Arm__Right___Stabilized__hKgvgj4lJ74wPt8N.json) (`hKgvgj4lJ74wPt8N`) | Item; stabilized | [с. 160](compendium-core-rulebook-reference.md#page-160) | Сверены записанные значения; исполнение и полнота автоматизации не проверены |
| [Dismembered Arm (Right - Treated)](../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Dismembered_Arm__Right___Treated__gPeOdwZ0OTVF9E3w.json) (`gPeOdwZ0OTVF9E3w`) | Item; treated | [с. 160](compendium-core-rulebook-reference.md#page-160) | Сверены записанные значения; исполнение и полнота автоматизации не проверены |
| [Dismembered Leg (Left)](../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Dismembered_Leg__Left__Us9OmoKhRydSqA8z.json) (`Us9OmoKhRydSqA8z`) | Item; none | [с. 160](compendium-core-rulebook-reference.md#page-160) | Сверены записанные значения; исполнение и полнота автоматизации не проверены |
| [Dismembered Leg (Left - Stabilized)](../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Dismembered_Leg__Left___Stabilized__lck0EEySmuLZXMrA.json) (`lck0EEySmuLZXMrA`) | Item; stabilized | [с. 160](compendium-core-rulebook-reference.md#page-160) | Сверены записанные значения; исполнение и полнота автоматизации не проверены |
| [Dismembered Leg (Left - Treated)](../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Dismembered_Leg__Left___Treated__eYEp1CPif98mDm2U.json) (`eYEp1CPif98mDm2U`) | Item; treated | [с. 160](compendium-core-rulebook-reference.md#page-160) | Сверены записанные значения; исполнение и полнота автоматизации не проверены |
| [Dismembered Leg (Right)](../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Dismembered_Leg__Right__Ssi9d4GQsAyYnt86.json) (`Ssi9d4GQsAyYnt86`) | Item; none | [с. 160](compendium-core-rulebook-reference.md#page-160) | [B15](#b15), [B16](#b16) |
| [Dismembered Leg (Right - Stabilized)](../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Dismembered_Leg__Right___Stabilized__vYza9bpK13G36YRV.json) (`vYza9bpK13G36YRV`) | Item; stabilized | [с. 160](compendium-core-rulebook-reference.md#page-160) | Сверены записанные значения; исполнение и полнота автоматизации не проверены |
| [Dismembered Leg (Right - Treated)](../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Dismembered_Leg__Right___Treated__KFbDbrS3OCs0C1h4.json) (`KFbDbrS3OCs0C1h4`) | Item; treated | [с. 160](compendium-core-rulebook-reference.md#page-160) | Сверены записанные значения; исполнение и полнота автоматизации не проверены |
| [Heart Damage](../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Heart_Damage_PVraD16y2VWkOH6J.json) (`PVraD16y2VWkOH6J`) | Item; none | [с. 160](compendium-core-rulebook-reference.md#page-160) | Сверены записанные значения; исполнение и полнота автоматизации не проверены |
| [Heart Damage (Stabilized)](../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Heart_Damage__Stabilized__O8EM4quPU4A5VOHH.json) (`O8EM4quPU4A5VOHH`) | Item; stabilized | [с. 160](compendium-core-rulebook-reference.md#page-160) | Сверены записанные значения; исполнение и полнота автоматизации не проверены |
| [Heart Damage (Treated)](../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Heart_Damage__Treated__Me9fgalLrB0i9Z2O.json) (`Me9fgalLrB0i9Z2O`) | Item; treated | [с. 160](compendium-core-rulebook-reference.md#page-160) | [B17](#b17) |
| [Separated Spine/Decapitated](../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Separated_Spine_Decapitated_MvrwnSrEqsTRdaeY.json) (`MvrwnSrEqsTRdaeY`) | Item; none | [с. 160](compendium-core-rulebook-reference.md#page-160) | Сверены записанные значения; исполнение и полнота автоматизации не проверены |
| [Spetic Shock (Stabilized)](../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Spetic_Shock__Stabilized__LM6Kkh0ib6ux4WQp.json) (`LM6Kkh0ib6ux4WQp`) | Item; stabilized | [с. 160](compendium-core-rulebook-reference.md#page-160) | [B16](#b16) |
| [Spetic Shock (Treated)](../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Spetic_Shock__Treated__vkr5MXhnalPp8yJJ.json) (`vkr5MXhnalPp8yJJ`) | Item; treated | [с. 160](compendium-core-rulebook-reference.md#page-160) | [B16](#b16), [B17](#b17) |
| [Spetic Shock](../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Spetic_Shock_tF3hsi4yZOMJ6xuW.json) (`tF3hsi4yZOMJ6xuW`) | Item; none | [с. 160](compendium-core-rulebook-reference.md#page-160) | [B16](#b16) |
| [Deadly](../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/_Folder.json) (`uofXQEP6HBtekOAO`) | Folder | [с. 158](compendium-core-rulebook-reference.md#page-158), [с. 159](compendium-core-rulebook-reference.md#page-159), [с. 160](compendium-core-rulebook-reference.md#page-160) | Группа уровня травм; игрового результата нет |
| [Compound Arm Fracture (Left - Stabilized)](../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Compound_Arm_Fracture__Left___Stabilized__tdcGSOZGCUhNArDc.json) (`tdcGSOZGCUhNArDc`) | Item; stabilized | [с. 159](compendium-core-rulebook-reference.md#page-159), [с. 160](compendium-core-rulebook-reference.md#page-160) | Сверены записанные значения; исполнение и полнота автоматизации не проверены |
| [Compound Arm Fracture (Left - Treated)](../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Compound_Arm_Fracture__Left___Treated__zaKPfDQFGTR8FKju.json) (`zaKPfDQFGTR8FKju`) | Item; treated | [с. 159](compendium-core-rulebook-reference.md#page-159), [с. 160](compendium-core-rulebook-reference.md#page-160) | [B08](#b08) |
| [Compound Arm Fracture (Left)](../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Compound_Arm_Fracture__Left__saPd4IMUCv5qZE60.json) (`saPd4IMUCv5qZE60`) | Item; none | [с. 159](compendium-core-rulebook-reference.md#page-159), [с. 160](compendium-core-rulebook-reference.md#page-160) | Сверены записанные значения; исполнение и полнота автоматизации не проверены |
| [Compound Arm Fracture (Right - Stabilized)](../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Compound_Arm_Fracture__Right___Stabilized__NHNctAuhsapGZXiP.json) (`NHNctAuhsapGZXiP`) | Item; stabilized | [с. 159](compendium-core-rulebook-reference.md#page-159), [с. 160](compendium-core-rulebook-reference.md#page-160) | [B14](#b14) |
| [Compound Arm Fracture (Right - Treated)](../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Compound_Arm_Fracture__Right___Treated__ujz1IMKCXoJF9w91.json) (`ujz1IMKCXoJF9w91`) | Item; treated | [с. 159](compendium-core-rulebook-reference.md#page-159), [с. 160](compendium-core-rulebook-reference.md#page-160) | [B08](#b08) |
| [Compound Arm Fracture (Right)](../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Compound_Arm_Fracture__Right__c3H8Xx7WYCcM37k6.json) (`c3H8Xx7WYCcM37k6`) | Item; none | [с. 159](compendium-core-rulebook-reference.md#page-159), [с. 160](compendium-core-rulebook-reference.md#page-160) | Сверены записанные значения; исполнение и полнота автоматизации не проверены |
| [Compound Leg Fracture (Left - Stabilized)](../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Compound_Leg_Fracture__Left___Stabilized__NiGtzaHs4dUj8Pmd.json) (`NiGtzaHs4dUj8Pmd`) | Item; stabilized | [с. 159](compendium-core-rulebook-reference.md#page-159), [с. 160](compendium-core-rulebook-reference.md#page-160) | Сверены записанные значения; исполнение и полнота автоматизации не проверены |
| [Compound Leg Fracture (Left - Treated)](../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Compound_Leg_Fracture__Left___Treated__kfyfxEVsMRUDDk1A.json) (`kfyfxEVsMRUDDk1A`) | Item; treated | [с. 159](compendium-core-rulebook-reference.md#page-159), [с. 160](compendium-core-rulebook-reference.md#page-160) | Сверены записанные значения; исполнение и полнота автоматизации не проверены |
| [Compound Leg Fracture (Left)](../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Compound_Leg_Fracture__Left__flpxY7FVPGevwfcg.json) (`flpxY7FVPGevwfcg`) | Item; none | [с. 159](compendium-core-rulebook-reference.md#page-159), [с. 160](compendium-core-rulebook-reference.md#page-160) | Сверены записанные значения; исполнение и полнота автоматизации не проверены |
| [Compound Leg Fracture (Right)](../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Compound_Leg_Fracture__Right__Rf0m4mGjeHEl0PxP.json) (`Rf0m4mGjeHEl0PxP`) | Item; none | [с. 159](compendium-core-rulebook-reference.md#page-159), [с. 160](compendium-core-rulebook-reference.md#page-160) | [B16](#b16) |
| [Compound Leg Fracture (Right - Stabilized)](../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Compound_Leg_Fracture__Right___Stabilized__QCugb1JqpiFyBEN4.json) (`QCugb1JqpiFyBEN4`) | Item; stabilized | [с. 159](compendium-core-rulebook-reference.md#page-159), [с. 160](compendium-core-rulebook-reference.md#page-160) | [B14](#b14) |
| [Compound Leg Fracture (Right - Treated)](../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Compound_Leg_Fracture__Right___Treated__3SwpPbi2ddEJkebh.json) (`3SwpPbi2ddEJkebh`) | Item; treated | [с. 159](compendium-core-rulebook-reference.md#page-159), [с. 160](compendium-core-rulebook-reference.md#page-160) | [B16](#b16) |
| [Concussion](../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Concussion_IK7pM8p3NcM4thcz.json) (`IK7pM8p3NcM4thcz`) | Item; none | [с. 159](compendium-core-rulebook-reference.md#page-159), [с. 160](compendium-core-rulebook-reference.md#page-160) | Сверены записанные значения; исполнение и полнота автоматизации не проверены |
| [Concussion (Stabilized)](../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Concussion__Stabilized__AFkm8KjxkwYxOCQo.json) (`AFkm8KjxkwYxOCQo`) | Item; stabilized | [с. 159](compendium-core-rulebook-reference.md#page-159), [с. 160](compendium-core-rulebook-reference.md#page-160) | Сверены записанные значения; исполнение и полнота автоматизации не проверены |
| [Concussion (Treated)](../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Concussion__Treated__ItXAMwWil2A7IqRv.json) (`ItXAMwWil2A7IqRv`) | Item; treated | [с. 159](compendium-core-rulebook-reference.md#page-159), [с. 160](compendium-core-rulebook-reference.md#page-160) | Сверены записанные значения; исполнение и полнота автоматизации не проверены |
| [Skull Fracture](../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Skull_Fracture_UImIh794nOy21jg2.json) (`UImIh794nOy21jg2`) | Item; none | [с. 159](compendium-core-rulebook-reference.md#page-159), [с. 160](compendium-core-rulebook-reference.md#page-160) | Сверены записанные значения; исполнение и полнота автоматизации не проверены |
| [Skull Fracture (Stabilized)](../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Skull_Fracture__Stabilized__ikv3qioEgGJG6Olw.json) (`ikv3qioEgGJG6Olw`) | Item; stabilized | [с. 159](compendium-core-rulebook-reference.md#page-159), [с. 160](compendium-core-rulebook-reference.md#page-160) | Сверены записанные значения; исполнение и полнота автоматизации не проверены |
| [Skull Fracture (Treated)](../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Skull_Fracture__Treated__v4RVIshohh1PPuAu.json) (`v4RVIshohh1PPuAu`) | Item; treated | [с. 159](compendium-core-rulebook-reference.md#page-159), [с. 160](compendium-core-rulebook-reference.md#page-160) | Сверены записанные значения; исполнение и полнота автоматизации не проверены |
| [Sucking Chest Wound (Stabilized)](../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Sucking_Chest_Wound__Stabilized__cfQ2OHPNVVKMDsDo.json) (`cfQ2OHPNVVKMDsDo`) | Item; stabilized | [с. 159](compendium-core-rulebook-reference.md#page-159), [с. 160](compendium-core-rulebook-reference.md#page-160) | Сверены записанные значения; исполнение и полнота автоматизации не проверены |
| [Sucking Chest Wound (Treated)](../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Sucking_Chest_Wound__Treated__wFul3Zr7mMaKjA5I.json) (`wFul3Zr7mMaKjA5I`) | Item; treated | [с. 159](compendium-core-rulebook-reference.md#page-159), [с. 160](compendium-core-rulebook-reference.md#page-160) | Сверены записанные значения; исполнение и полнота автоматизации не проверены |
| [Sucking Chest Wound](../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Sucking_Chest_Wound_tiVrEesPSzZ64HpZ.json) (`tiVrEesPSzZ64HpZ`) | Item; none | [с. 159](compendium-core-rulebook-reference.md#page-159), [с. 160](compendium-core-rulebook-reference.md#page-160) | Сверены записанные значения; исполнение и полнота автоматизации не проверены |
| [Torn Stomach](../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Torn_Stomach_5gnx9xNF52ap9PYi.json) (`5gnx9xNF52ap9PYi`) | Item; none | [с. 159](compendium-core-rulebook-reference.md#page-159), [с. 160](compendium-core-rulebook-reference.md#page-160) | Сверены записанные значения; исполнение и полнота автоматизации не проверены |
| [Torn Stomach (Stabilized)](../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Torn_Stomach__Stabilized__EpF0FD1nFXJTJ5Tj.json) (`EpF0FD1nFXJTJ5Tj`) | Item; stabilized | [с. 159](compendium-core-rulebook-reference.md#page-159), [с. 160](compendium-core-rulebook-reference.md#page-160) | Сверены записанные значения; исполнение и полнота автоматизации не проверены |
| [Torn Stomach (Treated)](../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Torn_Stomach__Treated__Mg1jn99OitVPdvje.json) (`Mg1jn99OitVPdvje`) | Item; treated | [с. 159](compendium-core-rulebook-reference.md#page-159), [с. 160](compendium-core-rulebook-reference.md#page-160) | Сверены записанные значения; исполнение и полнота автоматизации не проверены |
| [Difficult](../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/_Folder.json) (`ox3lLmV3zp0K67Ht`) | Folder | [с. 158](compendium-core-rulebook-reference.md#page-158), [с. 159](compendium-core-rulebook-reference.md#page-159), [с. 160](compendium-core-rulebook-reference.md#page-160) | Группа уровня травм; игрового результата нет |
| [Cracked Jaw](../../packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Cracked_Jaw_UnWBI9Sgu4AJv1z1.json) (`UnWBI9Sgu4AJv1z1`) | Item; none | [с. 158](compendium-core-rulebook-reference.md#page-158) | Сверены записанные значения; исполнение и полнота автоматизации не проверены |
| [Cracked Jaw (Stabilized)](../../packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Cracked_Jaw__Stabilized__h15wRehQQoIkxcf0.json) (`h15wRehQQoIkxcf0`) | Item; stabilized | [с. 158](compendium-core-rulebook-reference.md#page-158) | Сверены записанные значения; исполнение и полнота автоматизации не проверены |
| [Cracked Jaw (Treated)](../../packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Cracked_Jaw__Treated__AODuTRNu2RtJJhLD.json) (`AODuTRNu2RtJJhLD`) | Item; treated | [с. 158](compendium-core-rulebook-reference.md#page-158) | Сверены записанные значения; исполнение и полнота автоматизации не проверены |
| [Cracked Ribs](../../packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Cracked_Ribs_7TzGQ2y4yZnG01im.json) (`7TzGQ2y4yZnG01im`) | Item; none | [с. 158](compendium-core-rulebook-reference.md#page-158) | [B17](#b17) |
| [Cracked Ribs (Stabilized)](../../packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Cracked_Ribs__Stabilized__2c4PbGjd0segbvmr.json) (`2c4PbGjd0segbvmr`) | Item; stabilized | [с. 158](compendium-core-rulebook-reference.md#page-158) | [B17](#b17) |
| [Cracked Ribs (Treated)](../../packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Cracked_Ribs__Treated__oe4y6zxH2WUR9gSj.json) (`oe4y6zxH2WUR9gSj`) | Item; treated | [с. 158](compendium-core-rulebook-reference.md#page-158) | Сверены записанные значения; исполнение и полнота автоматизации не проверены |
| [Disfiguring Scar](../../packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Disfiguring_Scar_8tqapNHVCmSwijJw.json) (`8tqapNHVCmSwijJw`) | Item; none | [с. 158](compendium-core-rulebook-reference.md#page-158) | Сверены записанные значения; исполнение и полнота автоматизации не проверены |
| [Disfiguring Scar (Stabilized)](../../packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Disfiguring_Scar__Stabilized__AJeuZeFF29nEI5fc.json) (`AJeuZeFF29nEI5fc`) | Item; stabilized | [с. 158](compendium-core-rulebook-reference.md#page-158) | Сверены записанные значения; исполнение и полнота автоматизации не проверены |
| [Disfiguring Scar (Treated)](../../packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Disfiguring_Scar__Treated__kbeASc2PnnkYc5SR.json) (`kbeASc2PnnkYc5SR`) | Item; treated | [с. 158](compendium-core-rulebook-reference.md#page-158) | Сверены записанные значения; исполнение и полнота автоматизации не проверены |
| [Foreign Object (Stabilized)](../../packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Foreign_Object__Stabilized__fnYssldrMLVqbF22.json) (`fnYssldrMLVqbF22`) | Item; stabilized | [с. 158](compendium-core-rulebook-reference.md#page-158) | Сверены записанные значения; исполнение и полнота автоматизации не проверены |
| [Foreign Object (Treated)](../../packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Foreign_Object__Treated__rgRGVfLBlHMwUvGy.json) (`rgRGVfLBlHMwUvGy`) | Item; treated | [с. 158](compendium-core-rulebook-reference.md#page-158) | Сверены записанные значения; исполнение и полнота автоматизации не проверены |
| [Foreign Object](../../packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Foreign_Object_mylVzp10NMor44XR.json) (`mylVzp10NMor44XR`) | Item; none | [с. 158](compendium-core-rulebook-reference.md#page-158) | Сверены записанные значения; исполнение и полнота автоматизации не проверены |
| [Sprained Arm (Left - Stabilized)](../../packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Sprained_Arm__Left___Stabilized__01Seyu22NaDnctCi.json) (`01Seyu22NaDnctCi`) | Item; stabilized | [с. 158](compendium-core-rulebook-reference.md#page-158) | Сверены записанные значения; исполнение и полнота автоматизации не проверены |
| [Sprained Arm (Left - Treated)](../../packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Sprained_Arm__Left___Treated__q5vr9VLD2tEkL1ux.json) (`q5vr9VLD2tEkL1ux`) | Item; treated | [с. 158](compendium-core-rulebook-reference.md#page-158) | Сверены записанные значения; исполнение и полнота автоматизации не проверены |
| [Sprained Arm (Left)](../../packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Sprained_Arm__Left__quAixM7zp2bD9lXz.json) (`quAixM7zp2bD9lXz`) | Item; none | [с. 158](compendium-core-rulebook-reference.md#page-158) | Сверены записанные значения; исполнение и полнота автоматизации не проверены |
| [Sprained Arm (Right - Stabilized)](../../packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Sprained_Arm__Right___Stabilized__yGy3oWvmpX6WMm56.json) (`yGy3oWvmpX6WMm56`) | Item; stabilized | [с. 158](compendium-core-rulebook-reference.md#page-158) | Сверены записанные значения; исполнение и полнота автоматизации не проверены |
| [Sprained Arm (Right - Treated)](../../packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Sprained_Arm__Right___Treated__YiusbDXfFDhqwtQT.json) (`YiusbDXfFDhqwtQT`) | Item; treated | [с. 158](compendium-core-rulebook-reference.md#page-158) | [B16](#b16) |
| [Sprained Arm (Right)](../../packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Sprained_Arm__Right__umPVfrJeNU65S48O.json) (`umPVfrJeNU65S48O`) | Item; none | [с. 158](compendium-core-rulebook-reference.md#page-158) | Сверены записанные значения; исполнение и полнота автоматизации не проверены |
| [Sprained Leg (Left)](../../packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Sprained_Leg__Left__XPoH413WkKQUgrnw.json) (`XPoH413WkKQUgrnw`) | Item; none | [с. 158](compendium-core-rulebook-reference.md#page-158) | [B16](#b16) |
| [Sprained Leg (Left - Stabilized)](../../packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Sprained_Leg__Left___Stabilized__eblucqnyOS7lb5E5.json) (`eblucqnyOS7lb5E5`) | Item; stabilized | [с. 158](compendium-core-rulebook-reference.md#page-158) | [B16](#b16) |
| [Sprained Leg (Left - Treated)](../../packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Sprained_Leg__Left___Treated__f7NaW1AMnrSLGkd3.json) (`f7NaW1AMnrSLGkd3`) | Item; treated | [с. 158](compendium-core-rulebook-reference.md#page-158) | [B14](#b14), [B16](#b16) |
| [Sprained Leg (Right)](../../packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Sprained_Leg__Right__VhwzsUlv5csYSJTM.json) (`VhwzsUlv5csYSJTM`) | Item; none | [с. 158](compendium-core-rulebook-reference.md#page-158) | Сверены записанные значения; исполнение и полнота автоматизации не проверены |
| [Sprained Leg (Right - Stabilized)](../../packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Sprained_Leg__Right___Stabilized__fNiSVOJzpaxVvZTE.json) (`fNiSVOJzpaxVvZTE`) | Item; stabilized | [с. 158](compendium-core-rulebook-reference.md#page-158) | Сверены записанные значения; исполнение и полнота автоматизации не проверены |
| [Sprained Leg (Right - Treated)](../../packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Sprained_Leg__Right___Treated__8qatuNeEROueRDcZ.json) (`8qatuNeEROueRDcZ`) | Item; treated | [с. 158](compendium-core-rulebook-reference.md#page-158) | Сверены записанные значения; исполнение и полнота автоматизации не проверены |
| [Simple](../../packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/_Folder.json) (`kHSYUTn6UUJsIu4l`) | Folder | [с. 158](compendium-core-rulebook-reference.md#page-158), [с. 159](compendium-core-rulebook-reference.md#page-159), [с. 160](compendium-core-rulebook-reference.md#page-160) | Группа уровня травм; игрового результата нет |

### lifepath

| Документ / путь к JSON | Тип / объём | Книга | Результат сопоставления |
| --- | --- | --- | --- |
| [Allies: Closeness](../../packsJson/lifepath/Allies__Closeness_IswiqefPmaHECa5X.json) (`IswiqefPmaHECa5X`) | RollTable; 5 результатов | [с. 33](compendium-core-rulebook-reference.md#page-33) | Сверены тексты/диапазоны и ссылки; новых расхождений не выделено |
| [Allies: Gender](../../packsJson/lifepath/Allies__Gender_QFHhoiXtIBYkL8Rd.json) (`QFHhoiXtIBYkL8Rd`) | RollTable; 3 результата | [с. 33](compendium-core-rulebook-reference.md#page-33) | [A01](#a01) |
| [Allies: Generator](../../packsJson/lifepath/Allies__Generator_Va7NF10ETcMvndFo.json) (`Va7NF10ETcMvndFo`) | RollTable; 5 результатов | [с. 33](compendium-core-rulebook-reference.md#page-33) | Сверены тексты/диапазоны и ссылки; новых расхождений не выделено |
| [Allies: How You Met](../../packsJson/lifepath/Allies__How_You_Met_BqAizN8u9r6nMSyK.json) (`BqAizN8u9r6nMSyK`) | RollTable; 10 результатов | [с. 33](compendium-core-rulebook-reference.md#page-33) | Сверены тексты/диапазоны и ссылки; новых расхождений не выделено |
| [Allies: Position](../../packsJson/lifepath/Allies__Position_5sroduMneFqG9INx.json) (`5sroduMneFqG9INx`) | RollTable; 10 результатов | [с. 33](compendium-core-rulebook-reference.md#page-33) | Сверены тексты/диапазоны и ссылки; новых расхождений не выделено |
| [Allies: Where Are They?](../../packsJson/lifepath/Allies__Where_Are_They__W19e7rtl3ycrMhQU.json) (`W19e7rtl3ycrMhQU`) | RollTable; 4 результата | [с. 33](compendium-core-rulebook-reference.md#page-33) | Сверены тексты/диапазоны и ссылки; новых расхождений не выделено |
| [Allies and Enemies](../../packsJson/lifepath/Allies_and_Enemies_Lp42vhkw20Ys973y.json) (`Lp42vhkw20Ys973y`) | RollTable; 2 результата | [с. 33](compendium-core-rulebook-reference.md#page-33) | Сверены тексты/диапазоны и ссылки; новых расхождений не выделено |
| [Enemies: Gender](../../packsJson/lifepath/Enemies__Gender_FMondgMHlPLSy3cq.json) (`FMondgMHlPLSy3cq`) | RollTable; 3 результата | [с. 34](compendium-core-rulebook-reference.md#page-34) | [A01](#a01) |
| [Enemies: Generator](../../packsJson/lifepath/Enemies__Generator_7AXmeCSRkK3ktJ9Y.json) (`7AXmeCSRkK3ktJ9Y`) | RollTable; 7 результатов | [с. 34](compendium-core-rulebook-reference.md#page-34) | Сверены тексты/диапазоны и ссылки; новых расхождений не выделено |
| [Enemies: How Far Has It Escalated?](../../packsJson/lifepath/Enemies__How_Far_Has_It_Escalated__BLiqJBssahtqPqVf.json) (`BLiqJBssahtqPqVf`) | RollTable; 5 результатов | [с. 34](compendium-core-rulebook-reference.md#page-34) | Сверены тексты/диапазоны и ссылки; новых расхождений не выделено |
| [Enemies: Position](../../packsJson/lifepath/Enemies__Position_WeN4QhEHL468Ushx.json) (`WeN4QhEHL468Ushx`) | RollTable; 10 результатов | [с. 34](compendium-core-rulebook-reference.md#page-34) | Сверены тексты/диапазоны и ссылки; новых расхождений не выделено |
| [Enemies: Power](../../packsJson/lifepath/Enemies__Power_9mYMTKkCuU2ElJdx.json) (`9mYMTKkCuU2ElJdx`) | RollTable; 10 результатов | [с. 34](compendium-core-rulebook-reference.md#page-34) | Сверены тексты/диапазоны и ссылки; новых расхождений не выделено |
| [Enemies: The Cause](../../packsJson/lifepath/Enemies__The_Cause_U9R1ct2xP13y6R7j.json) (`U9R1ct2xP13y6R7j`) | RollTable; 10 результатов | [с. 34](compendium-core-rulebook-reference.md#page-34) | Сверены тексты/диапазоны и ссылки; новых расхождений не выделено |
| [Enemies: What Is Their Power?](../../packsJson/lifepath/Enemies__What_Is_Their_Power__sH1XIFHObBFdbjTI.json) (`sH1XIFHObBFdbjTI`) | RollTable; 5 результатов | [с. 34](compendium-core-rulebook-reference.md#page-34) | Сверены тексты/диапазоны и ссылки; новых расхождений не выделено |
| [Enemies: Who Was Wronged](../../packsJson/lifepath/Enemies__Who_Was_Wronged_cz5KlvgE7I7QV57H.json) (`cz5KlvgE7I7QV57H`) | RollTable; 2 результата | [с. 34](compendium-core-rulebook-reference.md#page-34) | [A08](#a08) |
| [Fortune](../../packsJson/lifepath/Fortune_Z0eeWQI3R8v4YNLd.json) (`Z0eeWQI3R8v4YNLd`) | RollTable; 10 результатов | [с. 32](compendium-core-rulebook-reference.md#page-32) | [B12](#b12) |
| [Fortune or Misfortune](../../packsJson/lifepath/Fortune_or_Misfortune_qKwYD3GHlGxCmiir.json) (`qKwYD3GHlGxCmiir`) | RollTable; 2 результата | [с. 32](compendium-core-rulebook-reference.md#page-32) | Сверены тексты/диапазоны и ссылки; новых расхождений не выделено |
| [Misfortune](../../packsJson/lifepath/Misfortune_JNbvihde5EGIFPdB.json) (`JNbvihde5EGIFPdB`) | RollTable; 10 результатов | [с. 32](compendium-core-rulebook-reference.md#page-32) | [B12](#b12) |
| [Romance](../../packsJson/lifepath/Romance_CDgdx129wZvINn16.json) (`CDgdx129wZvINn16`) | RollTable; 6 результатов | [с. 35](compendium-core-rulebook-reference.md#page-35) | Сверены тексты/диапазоны и ссылки; новых расхождений не выделено |
| [Romance: Problematic Love](../../packsJson/lifepath/Romance__Problematic_Love_l7k0hSL3iRzjJcYs.json) (`l7k0hSL3iRzjJcYs`) | RollTable; 10 результатов | [с. 35](compendium-core-rulebook-reference.md#page-35) | Сверены тексты/диапазоны и ссылки; новых расхождений не выделено |
| [Romance: Romantic Tragedy](../../packsJson/lifepath/Romance__Romantic_Tragedy_Jmvpwp9FRwRhDWZu.json) (`Jmvpwp9FRwRhDWZu`) | RollTable; 10 результатов | [с. 35](compendium-core-rulebook-reference.md#page-35) | Сверены тексты/диапазоны и ссылки; новых расхождений не выделено |

### style

| Документ / путь к JSON | Тип / объём | Книга | Результат сопоставления |
| --- | --- | --- | --- |
| [Style: Affectations](../../packsJson/style/Style__Affectations_4RWDMDzNdnz2kgwU.json) (`4RWDMDzNdnz2kgwU`) | RollTable; 10 результатов | [с. 36](compendium-core-rulebook-reference.md#page-36) | Сверены тексты/диапазоны и ссылки; новых расхождений не выделено |
| [Style: Clothing](../../packsJson/style/Style__Clothing_BuyEb4FcAyQL2hov.json) (`BuyEb4FcAyQL2hov`) | RollTable; 10 результатов | [с. 36](compendium-core-rulebook-reference.md#page-36) | Сверены тексты/диапазоны и ссылки; новых расхождений не выделено |
| [Style: Hair Style](../../packsJson/style/Style__Hair_Style_Ov9xIpAdWEPZCIoH.json) (`Ov9xIpAdWEPZCIoH`) | RollTable; 10 результатов | [с. 36](compendium-core-rulebook-reference.md#page-36) | Сверены тексты/диапазоны и ссылки; новых расхождений не выделено |
| [Style: Personality](../../packsJson/style/Style__Personality_TOQz3ETDronoeEDt.json) (`TOQz3ETDronoeEDt`) | RollTable; 10 результатов | [с. 36](compendium-core-rulebook-reference.md#page-36) | Сверены тексты/диапазоны и ссылки; новых расхождений не выделено |
| [Values: Feelings on People](../../packsJson/style/Values__Feelings_on_People_4eCXMVEfRx4PivWH.json) (`4eCXMVEfRx4PivWH`) | RollTable; 10 результатов | [с. 36](compendium-core-rulebook-reference.md#page-36) | Сверены тексты/диапазоны и ссылки; новых расхождений не выделено |
| [Values: Ideals](../../packsJson/style/Values__Ideals_s5EjP50ddIVoitHT.json) (`s5EjP50ddIVoitHT`) | RollTable; 10 результатов | [с. 36](compendium-core-rulebook-reference.md#page-36) | Сверены тексты/диапазоны и ссылки; новых расхождений не выделено |
| [Values: Valued Person](../../packsJson/style/Values__Valued_Person_y1WCi6n2Kpwqb27P.json) (`y1WCi6n2Kpwqb27P`) | RollTable; 10 результатов | [с. 36](compendium-core-rulebook-reference.md#page-36) | Сверены тексты/диапазоны и ссылки; новых расхождений не выделено |

### witcher-lifepath

| Документ / путь к JSON | Тип / объём | Книга | Результат сопоставления |
| --- | --- | --- | --- |
| [Witcher Background: How Did Early Training Go? +2](../../packsJson/witcher-lifepath/Witcher_Background__How_Did_Early_Training_Go___2_A7jt3mfuFTEQiXRv.json) (`A7jt3mfuFTEQiXRv`) | RollTable; 20 результатов | [с. 238](compendium-core-rulebook-reference.md#page-238), [с. 239](compendium-core-rulebook-reference.md#page-239) | [B11](#b11) |
| [Witcher Background: How Did Early Training Go? -2](../../packsJson/witcher-lifepath/Witcher_Background__How_Did_Early_Training_Go___2_G9iWzbiGQloX7sls.json) (`G9iWzbiGQloX7sls`) | RollTable; 20 результатов | [с. 238](compendium-core-rulebook-reference.md#page-238), [с. 239](compendium-core-rulebook-reference.md#page-239) | [B11](#b11) |
| [Witcher Background: How Did Early Training Go?](../../packsJson/witcher-lifepath/Witcher_Background__How_Did_Early_Training_Go__u2n9HR4RhSt1QV3l.json) (`u2n9HR4RhSt1QV3l`) | RollTable; 20 результатов | [с. 238](compendium-core-rulebook-reference.md#page-238), [с. 239](compendium-core-rulebook-reference.md#page-239) | Сверены тексты/диапазоны и ссылки; новых расхождений не выделено |
| [Witcher Background: How Did Your Trials Go? -2](../../packsJson/witcher-lifepath/Witcher_Background__How_Did_Your_Trials_Go___2_CDX4hqsxcxxovYz3.json) (`CDX4hqsxcxxovYz3`) | RollTable; 8 результатов | [с. 238](compendium-core-rulebook-reference.md#page-238), [с. 239](compendium-core-rulebook-reference.md#page-239) | [A07](#a07) |
| [Witcher Background: How Did Your Trials Go? +2](../../packsJson/witcher-lifepath/Witcher_Background__How_Did_Your_Trials_Go___2_zNG1R1HQoY6tpSLz.json) (`zNG1R1HQoY6tpSLz`) | RollTable; 8 результатов | [с. 238](compendium-core-rulebook-reference.md#page-238), [с. 239](compendium-core-rulebook-reference.md#page-239) | [A07](#a07) |
| [Witcher Background: How Did Your Trials Go? +4](../../packsJson/witcher-lifepath/Witcher_Background__How_Did_Your_Trials_Go___4_GknRX1nkVVcc9rCK.json) (`GknRX1nkVVcc9rCK`) | RollTable; 8 результатов | [с. 238](compendium-core-rulebook-reference.md#page-238), [с. 239](compendium-core-rulebook-reference.md#page-239) | [A07](#a07) |
| [Witcher Background: How Did Your Trials Go? -4](../../packsJson/witcher-lifepath/Witcher_Background__How_Did_Your_Trials_Go___4_sY3qw9UfVyx1l9BF.json) (`sY3qw9UfVyx1l9BF`) | RollTable; 8 результатов | [с. 238](compendium-core-rulebook-reference.md#page-238), [с. 239](compendium-core-rulebook-reference.md#page-239) | [A07](#a07) |
| [Witcher Background: How Did Your Trials Go?](../../packsJson/witcher-lifepath/Witcher_Background__How_Did_Your_Trials_Go__vaUFKIYBmEbJotfJ.json) (`vaUFKIYBmEbJotfJ`) | RollTable; 8 результатов | [с. 238](compendium-core-rulebook-reference.md#page-238), [с. 239](compendium-core-rulebook-reference.md#page-239) | [A07](#a07) |
| [Witcher Background: What School Did You Train In?](../../packsJson/witcher-lifepath/Witcher_Background__What_School_Did_You_Train_In__kEqyptPU1X7TvKc1.json) (`kEqyptPU1X7TvKc1`) | RollTable; 5 результатов | [с. 238](compendium-core-rulebook-reference.md#page-238) | [A04](#a04) |
| [Witcher Background: What Was Your Most Important Event](../../packsJson/witcher-lifepath/Witcher_Background__What_Was_Your_Most_Important_Event_34nU6OswdgAyMC6p.json) (`34nU6OswdgAyMC6p`) | RollTable; 20 результатов | [с. 240](compendium-core-rulebook-reference.md#page-240) | Сверены тексты/диапазоны и ссылки; новых расхождений не выделено |
| [Witcher Background: Where Are You Now?](../../packsJson/witcher-lifepath/Witcher_Background__Where_Are_You_Now__w8GcZsTyPF85V5Rr.json) (`w8GcZsTyPF85V5Rr`) | RollTable; 5 результатов | [с. 240](compendium-core-rulebook-reference.md#page-240) | Сверены тексты/диапазоны и ссылки; новых расхождений не выделено |
| [Witcher Lifepath: Allies - Are They Alive?](../../packsJson/witcher-lifepath/Witcher_Lifepath__Allies___Are_They_Alive__2l9nl4ndvdgtn2SJ.json) (`2l9nl4ndvdgtn2SJ`) | RollTable; 3 результата | [с. 243](compendium-core-rulebook-reference.md#page-243) | [B10](#b10) |
| [Witcher Lifepath: Allies - Closeness](../../packsJson/witcher-lifepath/Witcher_Lifepath__Allies___Closeness_TLO7kA1RyxfxP2D8.json) (`TLO7kA1RyxfxP2D8`) | RollTable; 3 результата | [с. 243](compendium-core-rulebook-reference.md#page-243) | Сверены тексты/диапазоны и ссылки; новых расхождений не выделено |
| [Witcher Lifepath: Allies - Gender](../../packsJson/witcher-lifepath/Witcher_Lifepath__Allies___Gender_bw2dbovLaFTJJ8EP.json) (`bw2dbovLaFTJJ8EP`) | RollTable; 3 результата | [с. 243](compendium-core-rulebook-reference.md#page-243) | [A01](#a01) |
| [Witcher Lifepath: Allies - Generator](../../packsJson/witcher-lifepath/Witcher_Lifepath__Allies___Generator_47kWQhpq3yeAG74c.json) (`47kWQhpq3yeAG74c`) | RollTable; 6 результатов | [с. 243](compendium-core-rulebook-reference.md#page-243) | Сверены тексты/диапазоны и ссылки; новых расхождений не выделено |
| [Witcher Lifepath: Allies - How Did They Die](../../packsJson/witcher-lifepath/Witcher_Lifepath__Allies___How_Did_They_Die_AMYeAxAXD3DMX6St.json) (`AMYeAxAXD3DMX6St`) | RollTable; 4 результата | [с. 243](compendium-core-rulebook-reference.md#page-243) | [B10](#b10) |
| [Witcher Lifepath: Allies - How You Met](../../packsJson/witcher-lifepath/Witcher_Lifepath__Allies___How_You_Met_pr3upjAFiZVHdOXp.json) (`pr3upjAFiZVHdOXp`) | RollTable; 10 результатов | [с. 243](compendium-core-rulebook-reference.md#page-243) | Сверены тексты/диапазоны и ссылки; новых расхождений не выделено |
| [Witcher Lifepath: Allies - Position](../../packsJson/witcher-lifepath/Witcher_Lifepath__Allies___Position_zG6aQ2srMV79PDHY.json) (`zG6aQ2srMV79PDHY`) | RollTable; 10 результатов | [с. 243](compendium-core-rulebook-reference.md#page-243) | Сверены тексты/диапазоны и ссылки; новых расхождений не выделено |
| [Witcher Lifepath: Allies - Where Are They?](../../packsJson/witcher-lifepath/Witcher_Lifepath__Allies___Where_Are_They__LPwYvTqPg52QQ9IU.json) (`LPwYvTqPg52QQ9IU`) | RollTable; 4 результата | [с. 33](compendium-core-rulebook-reference.md#page-33), [с. 243](compendium-core-rulebook-reference.md#page-243) | [A09](#a09) |
| [Witcher Lifepath: Benefit Outcome](../../packsJson/witcher-lifepath/Witcher_Lifepath__Benefit_Outcome_snt4khwSoq2rdeZa.json) (`snt4khwSoq2rdeZa`) | RollTable; 10 результатов | [с. 242](compendium-core-rulebook-reference.md#page-242) | [B12](#b12) |
| [Witcher Lifepath: Cautious Outcome](../../packsJson/witcher-lifepath/Witcher_Lifepath__Cautious_Outcome_jhPNDSApv5lQlUk3.json) (`jhPNDSApv5lQlUk3`) | RollTable; 7 результатов | [с. 241](compendium-core-rulebook-reference.md#page-241) | Сверены тексты/диапазоны и ссылки; новых расхождений не выделено |
| [Witcher Lifepath: Danger - Enemies Generator](../../packsJson/witcher-lifepath/Witcher_Lifepath__Danger___Enemies_Generator_iwGZ1Sj0v9iBqvSk.json) (`iwGZ1Sj0v9iBqvSk`) | RollTable; 7 результатов | [с. 245](compendium-core-rulebook-reference.md#page-245) | [A01](#a01) |
| [Witcher Lifepath: Danger - Enemies: Are They Alive?](../../packsJson/witcher-lifepath/Witcher_Lifepath__Danger___Enemies__Are_They_Alive__eywzppppagpC4HYO.json) (`eywzppppagpC4HYO`) | RollTable; 3 результата | [с. 245](compendium-core-rulebook-reference.md#page-245) | Сверены тексты/диапазоны и ссылки; новых расхождений не выделено |
| [Witcher Lifepath: Danger - Enemies: How Did They Die?](../../packsJson/witcher-lifepath/Witcher_Lifepath__Danger___Enemies__How_Did_They_Die__SwPXh5SRHrwfXyWP.json) (`SwPXh5SRHrwfXyWP`) | RollTable; 4 результата | [с. 245](compendium-core-rulebook-reference.md#page-245) | Сверены тексты/диапазоны и ссылки; новых расхождений не выделено |
| [Witcher Lifepath: Danger - Enemies: How Far Has It Escalated?](../../packsJson/witcher-lifepath/Witcher_Lifepath__Danger___Enemies__How_Far_Has_It_Escalated__8iZB8b98GEbOQfBQ.json) (`8iZB8b98GEbOQfBQ`) | RollTable; 5 результатов | [с. 245](compendium-core-rulebook-reference.md#page-245) | Сверены тексты/диапазоны и ссылки; новых расхождений не выделено |
| [Witcher Lifepath: Danger - Enemies: Position](../../packsJson/witcher-lifepath/Witcher_Lifepath__Danger___Enemies__Position_9m5zE1WyAI4xslyk.json) (`9m5zE1WyAI4xslyk`) | RollTable; 5 результатов | [с. 245](compendium-core-rulebook-reference.md#page-245) | Сверены тексты/диапазоны и ссылки; новых расхождений не выделено |
| [Witcher Lifepath: Danger - Enemies: Power](../../packsJson/witcher-lifepath/Witcher_Lifepath__Danger___Enemies__Power_1QUG4e60Iqom24ac.json) (`1QUG4e60Iqom24ac`) | RollTable; 10 результатов | [с. 245](compendium-core-rulebook-reference.md#page-245) | [A09](#a09) |
| [Witcher Lifepath: Danger - Enemies: The Cause](../../packsJson/witcher-lifepath/Witcher_Lifepath__Danger___Enemies__The_Cause_FR7XLvWHdkOwUtnC.json) (`FR7XLvWHdkOwUtnC`) | RollTable; 5 результатов | [с. 245](compendium-core-rulebook-reference.md#page-245) | Сверены тексты/диапазоны и ссылки; новых расхождений не выделено |
| [Witcher Lifepath: Danger - Enemies: What Is Their Power?](../../packsJson/witcher-lifepath/Witcher_Lifepath__Danger___Enemies__What_Is_Their_Power__xxaxFJfMA29gLFOm.json) (`xxaxFJfMA29gLFOm`) | RollTable; 5 результатов | [с. 245](compendium-core-rulebook-reference.md#page-245) | Сверены тексты/диапазоны и ссылки; новых расхождений не выделено |
| [Witcher Lifepath: Danger - Events](../../packsJson/witcher-lifepath/Witcher_Lifepath__Danger___Events_zVS3tsoiyTdjwU7i.json) (`zVS3tsoiyTdjwU7i`) | RollTable; 10 результатов | [с. 245](compendium-core-rulebook-reference.md#page-245) | [B12](#b12) |
| [Witcher Lifepath: Danger - Wounds](../../packsJson/witcher-lifepath/Witcher_Lifepath__Danger___Wounds_q2Cdg3rDUsu3xYLd.json) (`q2Cdg3rDUsu3xYLd`) | RollTable; 10 результатов | [с. 245](compendium-core-rulebook-reference.md#page-245) | Сверены тексты/диапазоны и ссылки; новых расхождений не выделено |
| [Witcher Lifepath: Dangers](../../packsJson/witcher-lifepath/Witcher_Lifepath__Dangers_QDAhRAIL7LNz9gME.json) (`QDAhRAIL7LNz9gME`) | RollTable; 4 результата | [с. 245](compendium-core-rulebook-reference.md#page-245) | Сверены тексты/диапазоны и ссылки; новых расхождений не выделено |
| [Witcher Lifepath: Hunt Generator](../../packsJson/witcher-lifepath/Witcher_Lifepath__Hunt_Generator_vTIEP2TnU2n4hwY3.json) (`vTIEP2TnU2n4hwY3`) | RollTable; 4 результата | [с. 244](compendium-core-rulebook-reference.md#page-244) | [B09](#b09) |
| [Witcher Lifepath: Hunt - How Did It End?](../../packsJson/witcher-lifepath/Witcher_Lifepath__Hunt___How_Did_It_End__n13vBwJk61euGPa1.json) (`n13vBwJk61euGPa1`) | RollTable; 5 результатов | [с. 244](compendium-core-rulebook-reference.md#page-244) | Сверены тексты/диапазоны и ссылки; новых расхождений не выделено |
| [Witcher Lifepath: Hunt - Was There a Twist?](../../packsJson/witcher-lifepath/Witcher_Lifepath__Hunt___Was_There_a_Twist__uLX85Bx2Jimqmx6o.json) (`uLX85Bx2Jimqmx6o`) | RollTable; 3 результата | [с. 244](compendium-core-rulebook-reference.md#page-244) | Сверены тексты/диапазоны и ссылки; новых расхождений не выделено |
| [Witcher Lifepath: Hunt - What Was the Prey?](../../packsJson/witcher-lifepath/Witcher_Lifepath__Hunt___What_Was_the_Prey__ZozZLNSgKpwEltsY.json) (`ZozZLNSgKpwEltsY`) | RollTable; 10 результатов | [с. 244](compendium-core-rulebook-reference.md#page-244) | [B09](#b09) |
| [Witcher Lifepath: Hunt - What Was the Twist?](../../packsJson/witcher-lifepath/Witcher_Lifepath__Hunt___What_Was_the_Twist__ZyRLAmxDu5SVt7rg.json) (`ZyRLAmxDu5SVt7rg`) | RollTable; 10 результатов | [с. 244](compendium-core-rulebook-reference.md#page-244) | Сверены тексты/диапазоны и ссылки; новых расхождений не выделено |
| [Witcher Lifepath: Hunt - Where Was the Prey?](../../packsJson/witcher-lifepath/Witcher_Lifepath__Hunt___Where_Was_the_Prey__PUVAGxwjXlFhXrhv.json) (`PUVAGxwjXlFhXrhv`) | RollTable; 10 результатов | [с. 244](compendium-core-rulebook-reference.md#page-244) | Сверены тексты/диапазоны и ссылки; новых расхождений не выделено |
| [Witcher Lifepath: Non-Neutral Outcome](../../packsJson/witcher-lifepath/Witcher_Lifepath__Non_Neutral_Outcome_sARR2vzegIiAh3uU.json) (`sARR2vzegIiAh3uU`) | RollTable; 7 результатов | [с. 241](compendium-core-rulebook-reference.md#page-241) | Сверены тексты/диапазоны и ссылки; новых расхождений не выделено |
| [Witcher Lifepath: Normal Outcome](../../packsJson/witcher-lifepath/Witcher_Lifepath__Normal_Outcome_Lu49KrUT3wDY1bJr.json) (`Lu49KrUT3wDY1bJr`) | RollTable; 7 результатов | [с. 241](compendium-core-rulebook-reference.md#page-241) | Сверены тексты/диапазоны и ссылки; новых расхождений не выделено |
| [Witcher Lifepath: Risky Outcome](../../packsJson/witcher-lifepath/Witcher_Lifepath__Risky_Outcome_R6BzlpXysvPx6O5c.json) (`R6BzlpXysvPx6O5c`) | RollTable; 7 результатов | [с. 241](compendium-core-rulebook-reference.md#page-241) | Сверены тексты/диапазоны и ссылки; новых расхождений не выделено |

## Фактические проверки этого исследования

- Все 226 JSON разобраны; подсчитаны 128 таблиц/995 результатов и 94 Item/79 эффектов/360 changes; каждой строке реестра назначена книжная область либо явно указан предел источника.
- Проверены внутренние `documentUuid`: найдены ровно две неразрешимые ссылки Mounted Control Loss; это уже известная issue-00323. Разрешимость ссылки не подтверждает правильность её назначения (B01–B04/B11).
- Проверены 31 цепочка followUp, 11 имён эффектов противоположной стороны, числовые значения B07 и состав treated-эффектов B08. Новые движковые сценарии не запускались.
- Выписка сверена с 40 выбранными страницами текстового слоя PDF; числа в основных матрицах перепроверены по страницам. Проверены ссылки новых документов, состав изменений и неизменность всех packsJson относительно начала работы.
- Проверка `python3 -B docs/analytics/system-index/query.py check --freshness --format json`: `valid=true`, `freshness=current`, differences пуст. Размер графа сохранён: 615 sources / 5386 entities / 15239 relations / 465 processes. Проверены 1241 локальная ссылка/якорь в затронутых материалах; `git diff --check` без замечаний. Существующие inode/mode/uid/gid сохранены.
- Работа с действующими БД не выполнялась. Попытка общего чтения дерева для исходного снимка натолкнулась на недоступный `packs/combat/LOG`; права не менялись, снимок ограничен документацией и доступными исходниками. Это не влияет на сверку packsJson и не является проверкой прав службы.

Это статическая сверка содержания и маршрутов по предоставленному изданию. Исправления, пересборка, игровая приёмка и подтверждение закрытия issues **не выполнены**.
