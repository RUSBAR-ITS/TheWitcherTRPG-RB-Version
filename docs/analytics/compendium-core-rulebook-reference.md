# Компедиумы: таблицы и правила английской базовой книги

Вспомогательный первичный материал для [issue-00331](../issues/closed/issue-00331.md) и [сравнения с JSON](compendium-core-rulebook-comparison.md). Это выписка из предоставленной книги, а не описание исправленной системы.

## Источник и пределы

- Дата: 2026-09-16; ветка `dev`; HEAD `433060047ca195773d582cac782a6a83a5c91ade`; исходная версия системы `14.3.1.00013`, оформление `14.3.1.00014`.
- Предоставленный файл: `/var/lib/foundryvtt/Data/modules/the-witcher-trpg-content-pack-by-rusbar/assets/books/witcher/ENG/The_Witcher_TRPG.pdf`.
- Английская базовая книга, 336 страниц; метаданные PDF датированы июлем 2018 года. SHA256: `107546c7229ba0143c9176dfa6252731e9e2d04e9c33d0a8627de6ffe64cded0`.
- Здесь фиксируется именно этот PDF. Последующие редакции и errata не подменяют его автоматически. Дополнения не проверены; отсутствие варианта в базовой книге само по себе не доказывает ошибку дополнения.
- Номера ниже — напечатанные номера страниц; у выбранных страниц они совпадают с номерами страниц PDF (отсчёт с единицы).
- Извлечены 40 страниц с соответствующими таблицами, непосредственными условиями применения и пояснениями. Полные страницы сохранены, чтобы не потерять колонки и боковые правила; посторонние абзацы на той же странице не становятся требованиями к компедиумам.
- Команда извлечения: `pdftotext -layout <предоставленный-PDF> <временный-текст>`. В блоках `text` сохранены расположение колонок, оригинальные формулировки и опечатки. Переносы внутри слов не исправлены. Это текстовый слой, а не факсимиле; спорную ячейку проверять по PDF.
- Компедиумы сравниваются по исходникам `packsJson`; живые базы Foundry, применение эффектов и соответствие более поздним изданиям этой работой не проверяются.

## Указатель таблиц и правил

| Раздел | Страницы | Для чего используется |
| --- | --- | --- |
| Создание персонажа, расы и социальное положение | [20](#page-20), [21](#page-21), [37](#page-37) | Границы случайных генераторов рас/профессий; последствия Misfortune |
| Происхождение и родная земля | [25](#page-25) | Northern, Nilfgaard, Vassal, Elderlands; порядок ветвления семьи |
| Судьба семьи | [26](#page-26) | По десять результатов для трёх регионов; переход к Parental Fate |
| Судьба родителей | [27](#page-27) | Три региональные колонки и Which Parent |
| Положение семьи и стартовые предметы | [28](#page-28) | Семь диапазонов для каждого региона, бонусы |
| Влиятельный друг и памятный предмет | [29](#page-29) | По десять результатов для трёх регионов |
| Братья/сёстры | [30](#page-30) | Число, пол, возраст, отношения, личность; независимые броски |
| События жизни | [31](#page-31), [32](#page-32) | Ветвление, удача/неудача, вложенные броски и зависимость |
| Союзники и враги | [33](#page-33), [34](#page-34) | Пол, положение, знакомство, близость, регион; причины, сила, эскалация |
| Романтические отношения | [35](#page-35) | Основная таблица, трагедия, проблемная любовь, продолжение отношений |
| Стиль и ценности | [36](#page-36) | Семь независимых колонок |
| Попадания и урон | [153](#page-153), [154](#page-154) | Гуманоидные/монструозные локации, прицельные штрафы и множители |
| Критические травмы | [158](#page-158), [159](#page-159), [160](#page-160) | Четыре уровня × шесть исходов × три состояния; анатомические исключения, протезы |
| Состояния и спасброски | [161](#page-161), [162](#page-162) | Кровотечение, яд, удушье, смерть, стабилизация |
| Контекст Scatter | [157](#page-157), [163](#page-163), [164](#page-164), [165](#page-165) | Провалы, обезоруживание и бомбы; числовая таблица направлений в этом PDF не установлена |
| Потеря управления | [169](#page-169), [170](#page-170) | Транспорт, ездок и животное; отдельные броски, дистанции, урон и DC |
| Лечение | [173](#page-173), [174](#page-174) | Лечение HP, травм, Healing Hands/Spell, сроки по BODY, протезы |
| Проклятия | [230](#page-230), [231](#page-231) | Ссылка из Misfortune/Cursed; выбор и снятие остаются за GM |
| Становление ведьмака | [238](#page-238), [239](#page-239), [240](#page-240) | Возраст, школа, обучение, испытания, важное событие, текущее положение |
| Десятилетия ведьмака | [241](#page-241), [242](#page-242) | Независимые опасность и исход, награды и вложенные броски |
| Союзники ведьмака | [243](#page-243) | Близость, смертность, причина и срок смерти |
| Охота | [244](#page-244) | Добыча, место, исход, поворот и бонус знания конкретного монстра |
| Опасности ведьмака | [245](#page-245) | События, ранения, враги и их смертность |

## Ключевые условия для будущей правки

Это краткая нормализация выписки; точная формулировка и все строки таблиц находятся ниже.

1. С. 25–30: происхождение → судьба семьи/родителей → положение семьи → влиятельный друг → братья/сёстры. С. 26 прямо направляет после Family Fate в Parental Fate; с. 27 — в Family Status. Ветвь неповреждённой семьи отдельно бросает судьбу родителей. Не выводить пропуск этапа из художественного текста о погибшей семье.
2. Не-человек **может выбрать** Elderlands; это не обязательное происхождение всех эльфов и краснолюдов. Для выбранного традиционного происхождения Elf → Dol Blathanna (+1 Social Etiquette), Dwarf → Mahakam (+1 Crafting).
3. С. 30: для синих колонок — отдельный бросок на каждую. Количество siblings: North 1–8 = число, 9–10 = 0; Nilfgaard/Dwarf 1–5 = число, 6–10 = 0; Elf 1–2 = 1, 3–8 = 0, 9–10 = 2.
4. С. 31: один бросок на каждое полное десятилетие жизни. 1–4 → Fortune **or** Misfortune; 5–7 → Allies **and** Enemies; 8–10 → Romance. В первых двух ветках далее независимый выбор 50/50. С. 35: новый тип романа может изменить судьбу текущей счастливой пары.
5. С. 36: семь колонок стиля и ценностей бросаются отдельно. Одновременный вызов семи таблиц — допустимый способ представить это в Foundry.
6. С. 158–160: колонки Effect / Stabilized / Treated различны. Нельзя переносить кровотечение из исходной травмы в вылеченную только потому, что она является следующим документом в цепочке. Separated Spine/Decapitated сразу убивает и не стабилизируется/лечится.
7. С. 159: elementa/specters не получают Foreign Object, Ruptured Spleen, Torn Stomach, Sucking Chest Wound, Septic Shock; вместо этого указаны добавочные повреждения 5/10/15/20 по уровню. Для ног specters локацию перебрасывают. Это условие применения, не новая разновидность Item.
8. С. 161: Bleed = 2/ход, Poison = 3/ход, Suffocation = 3/раунд, без поглощения бронёй согласно соответствующим строкам. Torn Stomach отдельно задаёт 4 acid/раунд. Проверка этих чисел не доказывает исполнение ActiveEffect.
9. С. 158, 162, 173–174: стабилизация не запускает заживление; после лечения отсчитывают дни снятия Treated-штрафа. Постоянные последствия, отдельно названные в Deadly, не следует объявлять исчезающими лишь по общей таблице сроков. Способ их хранения/исполнения требует решения в категории механик.
10. С. 169: при потере контроля верхом бросают **дважды**, отдельно для ездока и животного. Автоматический контейнер `1d1` допустим, если вызывает две правильные таблицы.
11. С. 238–239: возраст даёт −2/0/+2 к Trials; обучение №4 ещё +2, №7 ещё −2. Это сумма модификаторов одного испытания, не модификатор самого броска Early Training. Крайние результаты за 1–10 в таблице PDF явно не описаны.
12. С. 241: после начала пути в 20–29 лет для последующих десятилетий сначала проверяют Danger, затем всегда Outcome. Вероятности Danger: 10/25/50/75%; опасность не отменяет Benefit/Ally/Hunt/Nothing.
13. С. 243/245: 1–30% означает смерть союзника/врага, 31–100% — жив. Для умершего бросают `1d10` десятилетий до смерти; причины смерти союзника и врага различаются.
14. С. 244: результат Hunt даёт выбор конкретного монстра внутри выпавшей категории и +2 к Witcher Training, связанному с этим монстром. Самого названия категории недостаточно.
15. С. 230–231: проклятие не выбирается автоматически как набор произвольных штрафов; GM определяет связанное с сюжетом последствие и способ снятия.

### Локации по с. 154

| Бросок | Humanoid | Штраф / урон | Monster | Штраф / урон |
| --- | --- | --- | --- | --- |
| 1 | Head | −6 / ×3 | Head | −6 / ×3 |
| 2–4 | Torso | −1 / ×1 | Torso | −1 / ×1 |
| 5 | R. Arm | −3 / ×½ | R. Limb | −3 / ×½ |
| 6 | L. Arm | −3 / ×½ | R. Limb | −3 / ×½ |
| 7 | R. Leg | −2 / ×½ | R. Limb | −3 / ×½ |
| 8 | R. Leg | −2 / ×½ | L. Limb | −3 / ×½ |
| 9 | L. Leg | −2 / ×½ | L. Limb | −3 / ×½ |
| 10 | L. Leg | −2 / ×½ | Special | −2 / ×½ |

### Матрица Trials

| Модификатор возраста | Обычное обучение (1–3, 5–6, 8–10) | Easy Mutations (4) | Bad Reaction (7) |
| --- | --- | --- | --- |
| −2 | −2 | 0 | −4 |
| 0 | 0 | +2 | −2 |
| +2 | +2 | +4 | 0 |

### Опасность и исход десятилетия по с. 241

| Риск | Danger | Benefit | Ally | Hunt | Nothing |
| --- | --- | --- | --- | --- | --- |
| Cautious | 10% | 1 | 2 | 3 | 4–10 |
| Normal | 25% | 1 | 2 | 3–5 | 6–10 |
| Non-Neutral | 50% | 1–2 | 3–7 | 8 | 9–10 |
| Risky | 75% | 1–5 | 6–7 | 8–9 | 10 |

### Лечение по с. 162, 174

| Уровень | First Aid: стабилизация DC | Healing Hands: ходы / DC | Healing Spell: применения / DC |
| --- | --- | --- | --- |
| Simple | 12 | 2 / 12 | 4 / 14 |
| Complex | 14 | 4 / 14 | 6 / 16 |
| Difficult | 16 | 6 / 16 | 8 / 18 |
| Deadly | 18 | 8 / 18 | 10 / 20 |

| BODY | Simple, дни | Complex, дни | Difficult, дни | Deadly, дни |
| --- | --- | --- | --- | --- |
| 3 | 5 | 9 | 12 | 15 |
| 4 | 4 | 8 | 11 | 14 |
| 5 | 3 | 7 | 10 | 13 |
| 6 | 2 | 6 | 9 | 12 |
| 7 | 1 | 5 | 8 | 11 |
| 8 | 1 | 4 | 7 | 10 |
| 9 | 1 | 3 | 6 | 9 |
| 10 | 1 | 2 | 5 | 8 |
| 11 | 1 | 1 | 4 | 7 |
| 12 | 1 | 1 | 3 | 6 |
| 13 | 1 | 1 | 2 | 5 |

Книга здесь перечисляет BODY 3–13. Значения вне таблицы не экстраполированы как якобы напечатанное правило.

## Полная постраничная выписка

Блоки ниже получены из книги независимо от данных компедиума. Поэтому ошибки JSON не попадают в эталон автоматически. Раздел сравнения отдельно указывает, какие различия установлены, а какие требуют решения об издании или адаптации.

<a id="page-20"></a>

### Страница 20

```text
     20


       Mechanics                  Creating Your
                                  Own Character
Having already seen the title
characters laid out you may
be confused about the various
statistics, abilities and items
presented. We’ll be going over
all of this in the next several
chapters and will explain how
                                  What is a Character?
you to determine these values     In the Witcher TRPG, your character is the person you inhabit while playing in the
for your own character.           game. While it is often a good idea to start out playing characters that are similar to
                                  yourself, your character can be just about anybody you want.


                                  Character Creation
                                  The process of building your character is simple, but with a lot of choice and variation so
                                  you can make your character as unique as possible. You create your character in seven steps:


                                  1. Pick Your Race                                  4. Pick Your Statistics
                                  Determine what race you want to play. This         Once you have figured out what you do for a
                                  is an important step because your race de-         living, you then need to figure out what your
                                  termines both your special abilities and how       core abilities are. Your statistics are there to
                                  the average person will react to you.              represent the core attributes of your charac-
                                                                                     ter. How tough they are, how smart they are,
                                                                                     how fast they are and so on.
                                  2. Run a Lifepath
                                  The second step to creating your character
                                  is to roll up a Lifepath. This series of rolls     5. Select Pick-Up Skills
                                  determines not only what your character is         After you have picked your stats you can
                                  generally like and what they value, but also       choose your pick-up skills. These are skills
                                  creates their history. Though this is an op-       unrelated to your profession that you have
                                  tional step, it allows you to flesh out your       just ‘picked up’ over time.
                                  character and play a game of chance to get
                                  bonuses from significant life events. Howev-
                                  er, in addition to making friends and gain-        6. Get Your Coin
                                  ing boons you may also find enemies and            At this stage your character is finished and
                                  incur disadvantages.                               now you get to outfit them. The first step to
                                                                                     this is to use the Starting Coin table to deter-
                                                                                     mine how much money you have.
                                  3. Pick Your Profession
                                  After you know what race you are and what
                                  your life was generally like, you can choose a     7. Outfit Yourself
                                  profession to enter. Your profession will give     After you have your money you can start
                                  you a set of skills, starting gear and a special   buying weapons, armor, and gear that your
                                  Skill Tree.                                        character will need in their adventures.
```

<a id="page-21"></a>

### Страница 21

```text
                                                                                                                       21


Races                                                                                              Others of Your Race
                                                                                                   It’s important to note that you
In the world of The Witcher there are four playable races that each have their own abili-
                                                                                                   may run into others of your
ties and drawbacks. Despite the fact that they are born as humans, witchers are consid-
                                                                                                   race while in hostile territory.
ered a race of their own due to the mutations in their bodies and their unique abilities.
                                                                                                   Other members of your race
                                                                                                   will always treat you as equal
                                                                                                   unless they have some person-
Social Standing                                                                                    al problem with you or mem-
Humans are the dominant species on the Continent. After a series of wars in which the
                                                                                                   bers of their own race.
elves and dwarves sided against the humans of the north, the non-human population (el-
derfolk, if you’re polite) of the Northern Kingdoms has become a downtrodden group of
second-class citizens. Today, race means quite a bit in day to day life. Each race has its own
social standing, which indicates how people deal with your character and explains how
their reaction reflects in statistics.                                                                    Friendship
Equal                                           Tolerated                                          Your social standing is de-
Characters with a social standing of equal      Characters who are tolerated are present           signed to indicate how
are seen as peers. They take no penalties to    in society but not really respected or con-        strangers feel about you based
social interactions but gain no bonuses ei-     sidered equal. They take a -1 to Seduction,        on your race. Obviously if
ther. People will generally judge them on       Charisma, Persuasion, and Leadership with          you’re an elf who has a long-
their appearance and actions rather than        people.                                            time friend who happens to
their race.                                                                                        be a human, your friend won’t
                                                                                                   hate you. The same goes for
                                                                                                   lovers and, sometimes, in-laws.
Feared                                          Hated
Characters who are feared are considered        Characters who are hated are actively de-
frightening to the average person. You only     spised by most people. They aren’t neccesar-
gain the feared social standing through mu-     ily outcast, but are often the targets of racial
tation into a witcher or horrible scarring.     aggression and hate crimes. They take a -2 to
You can gain the standing in specific places    Seduction, Charisma, Persuasion, and Lead-
based on your actions, but that is decided by   ership with people.
the Game Master. A character who is feared
gains a +1 to Intimidation but a -1 to Cha-
risma.

     Territory         Humans           Elves       Dwarves        Witchers         Mages
                                                                    Hated &         Hated &
     The North            Equal         Hated        Tolerated
                                                                    Feared          Feared
                                                                    Hated &
     Nilfgaard            Equal         Equal          Equal                       Tolerated
                                                                    Feared

      Skellige            Equal         Equal          Equal        Tolerated      Tolerated

   Dol Blathanna         Hated          Equal          Equal        Tolerated        Equal

     Mahakam            Tolerated       Equal          Equal        Tolerated      Tolerated
```

<a id="page-25"></a>

### Страница 25

```text
                                                                                                                              25


Lifepath
In the world of The Witcher your early life can be very important. Not only does it
                                                                                                           Random Chance
                                                                                                        While you can choose from
                                                                                                        amongst these options to craft
tell you what land you grew up in, but also what kind of environment you lived in,                      the specific character you want
what the people around you were like, and even what skills you learned. This is also                    to play, roll from scratch first
the point at which you decide which of the three sides of the Third Northern War                        one or two times just to see
you hail from. This may not reflect what side you are on now, but it will tell you                      what you’ll get.
what you grew up knowing about the conflict and what people will expect of you.



                                       Homeland                                                             The Elderlands
                                                                                                        As a non-human you can
                                                                                                        choose to come from one of
   Roll              Region                            Northern                     Vassal
                                          Roll                                                          the traditional homelands
              Northern Kingdoms                         Origin                      Origin
   Odd                                                                                                  of the elder races: the Ma-
             (Go to Northern Origin)                    Redania                    Vicovaro
                                           1                                                            hakaman Mountains or Dol
                    Nilfgaard                        (+1 Education)             (+1 Education)
   Even                                                                                                 Blathanna. This is not manda-
            (Go to Nilfgaardian Origin)                 Kaedwen                     Angren
                                           2
                                                     (+1 Endurance)          (+1 Wilderness Survival)
                                                                                                        tory and you can roll on the ta-
   Non             Elderlands                                                                           ble for your homeland instead.
  Human      (Go to Elderland Origin)                   Temeria                     Nazair
                                           3
                                                       (+1 Charisma)             (+1 Brawling)
                                                         Aedirn                     Mettina
                                           4
  Roll      Nilfgaardian Origin
                                                      (+1 Crafting)                (+1 Ride)               Witcher Lifepath
                                                     Lyria & Rivia                Mag Turga             As a witcher you roll on a
            The Heart of Nilfgaard         5
   1-3                                            (+1 Resist Coercion)          (+1 Endurance)
                   (+1 Deceit)                                                                          witcher-specific Lifepath in the
                                                    Kovir & Poviss                   Gheso              “Running a Witcher” Section
                     Vassal                6
  4-10                                                (+1 Business)               (+1 Stealth)
              (Go to Vassal Origin)                                                                     on pg.237. If you want, you can
                                                         Skellige                   Ebbing              roll on the Lifepath tables to see
                                           7
                                                      (+1 Courage)              (+1 Deduction)
                                                                                                        what the family you were tak-
                                                         Cidaris                    Maecht
                                           8                                                            en from was like, but they are
  Race       Elderland Origin                          (+1 Sailing)              (+1 Charisma)
                                                                                                        most likely dead.
                Dol Blathanna                            Verden                   Gemmeria
   Elf                                     9
               (+1 Social Etiquette)              (+1 Wilderness Survival)     (+1 Intimidation)
                   Mahakam                               Cintra                      Etolia
 Dwarf                                     10
                  (+1 Crafting)                   (+1 Human Perception)          (+1 Courage)
                                                                                                                Homeland
                                                                                                        You can find more informa-
                                          Roll                         Family                           tion on your homeland in
    Familial Fate                         Even
                                                       Your Family Is Alive and Together
                                                               (Go to Parents)
                                                                                                        the World section, starting on
                                                                                                        pg.179. If you rolled Cintra as
Along the course of your life it’s all
                                                     Something Happened to Your Family                  your homeland you’ll have to
too common for something to go             Odd
                                                             (Go to Family Fate)                        look under Nilfgaard. Cintra
horribly wrong. After finding out
where you grew up roll on these                                                                         was only captured a few years
two tables to find out how lucky           Roll                        Parents                          ago, and many still hold hope
your family was as you were grow-                              Your Parents Are Alive
                                                                                                        of taking it back from Nilf-
                                           Even                                                         gaard.
ing up.                                                         (Go to Family Status)
                                                     Something Happened To Your Parents
                                           Odd
                                                             (Go to Parental Fate)
```

<a id="page-26"></a>

### Страница 26

```text
      26

                                      Family Fate
 The Kazmer Family                    If you rolled that something happened to your family over the course of your life, roll on
Eh, life’s never easy for elderfolk   the table below. Not everything on this list affects your family directly. Some of the events
growin’ up in the North. Heh,         below involve your interactions with them. These events affect not only your parents but
had it easier than the elves but it   also your siblings. Roll 1d10 or choose below, then go to Parental Fate.
still wasn’t exactly a walk in the     Roll       Northern Status                  Nilfgaardian Status                  Elderland Status
park. Think most of the reason                Your family was scattered to the   Your family was indentured for     Your family were marked as
we didn’t get more trouble was                winds by the wars and you have     crimes against the Empire or       human sympathizers and are
                                         1
my Pa was one tough older                     no idea where most of them         on trumped-up charges. Only        not particularly loved in their
dwarf and he made sure every-                 are.                               you escaped.                       homeland.
body knew it. Nah, real problem               Your family was imprisoned         Your family was exiled to the
                                                                                                                    Your family was ostracized
was my brother, Agoston. Heh,                 for crimes or on trumped-up        Korath Desert and you likely
                                                                                                                    for dissenting opinions and
                                         2    charges. You were the only one     spent most of your early life
joined the Scoia’tael a few years             to escape. You may want to free    struggling to survive in the
                                                                                                                    now people won’t socialize with
back. Said he’d had enough                                                                                          you or your family at all.
                                              them...or maybe not.               deadly wasteland.
with the ‘damn dhoine’ runnin’                Your family house was cursed       Your family was killed by a        Your family died in the
roughshod over us dwarves. See                and now either crops won’t         rogue mage who either had a        Northern Wars. They may have
where he was comin’ from but             3    grow or specters roam the halls.   vendetta against your family, or   actually fought in the war, or
there ain’t no sense in huntin’               It became too dangerous for        just wanted blood. Either way,     were casualties of war who just
                                              you to stay in this home.          you are alone.                     happened to get in the way.
down innocent humans to get
                                              With so many wars your fam-        Your family disappeared and        Your family has been caught in
back at the real bastards. Ma
                                              ily’s livelihood was destroyed.    you have no idea where they        a feud for centuries. You may
agrees with me but Pa’s aways            4
                                              Your family turned to crime to     went. One day they just up and     not remember why this feud
been the, uh, ‘militant’ sort. Heh,           survive.                           left.                              started, but it is dire.
really split the family up. Let me            Your family accumulated a          Your family was executed for       Your family was stripped of its
tell ya, family reunions ain’t no        5
                                              huge debt through gambling or      treason against the Empire. You    title for some reason. You were
picnic! Ya can count on at at                 favors from others. You need       were the only one to escape this   evicted from your home and
                                              money desperately.                 fate.                              left scrambling to survive.
least one broken table and half a
dozen crumpled goblets.                       Your family has fallen into a      Your family was stripped of
                                                                                                                    Your family turned to raiding
                                              feud with another family. You      its title for some reason. You
                  –Rodolf Kazmer         6    may not even remember why          were evicted from your home
                                                                                                                    human settlements early in
                                                                                                                    your life to get food and per-
                                              this feud started in the first     and left scrambling to survive
                                                                                                                    haps strike back at the humans.
                                              place.                             among the un-washed masses.
                                              Due to some action or inaction     Your family name was               Your family house is haunted.
     Sounds Grim?                             your family has become hated       tarnished by a magic relative      Most likely this is because your
If these tables seem some-               7    in your home town and now          who flaunted their magical gift    home was the site of many,
what depressing or ominous,                   no one there wants to have any-    disgracefully like a Northern      many deaths during the war
                                              thing to do with them.             mage.                              against humans.
remember that in a truly me-
                                                                                You disgraced your family in        Your family has been split by a
dieval world life is often nasty,             One day everything you had
                                                                                the eyes of the Empire. Some-       human in-law who was brought
brutish, and short.                      8
                                              was ripped away by a bandit
                                                                                thing you did or failed to do has   into your family by a sibling or
                                              mob. Your family was massa-
                                                                                ruined your personal name and       relative. Some of your family
                                              cred, leaving you entirely alone.
                                                                                harmed your family.                 like them and some hate them.
                                              Your family has a deep, dark       Your family has a deep, dark       Your family was killed by hu-
                                              secret that if discovered would    secret that if discovered would    mans who thought they were
                                         9    ruin you all completely. You       destroy them and their name        Scoia’tael. They may have been
                                              can decide what this secret is,    forever. You must protect this     slaughtered or hung with no
                                              or the Game Master can decide.     secret with your life.             court proceedings or trials.
                                              Your family has come to despise    Your family was assassinated.      Your family is descended from
                                              each other. No one you grew up     They may have been in the way      an infamous traitor. It taints
                                              with will talk with each other     of someone’s plan or they may      your family’s interactions with
                                         10
                                              any more and you’re lucky to       have been used to get at some-     others of the elder races and
                                              get a passing hello from your      one more powerful. Either way,     has made living in the elder-
                                              siblings.                          your family is gone now.           land difficult.
```

<a id="page-27"></a>

### Страница 27

```text
                                                                                                                                               27

Parental Fate
If you rolled that something happened to your parents over the course of your life, roll                                      Which Parent
on the table below. Not everything on this list affects your parents directly. Some of the
events below involve your interactions with them, such as having been sold or given                                         Roll           Parent
away at a young age. Roll 1d10 or choose below, then go to Family Status.                                                     1-4           Father
  Roll        Northern Status                    Nilfgaardian Status                   Elderland Status                       5-8           Mother
         One or more of your parents           Your father died in one of the      One or more of your par-                  9-10            Both
         were killed in the Northern           Northern Wars. He may have al-      ents were accused of being
   1     Wars. Most likely your father, but    ready been in the military or he    Scoia’tael. The people around
         it is also possible that your moth-   may have been conscripted into      you give your parents sidelong
         er fought or was a casualty.          service during that war.            glances.                               Brandon’s Parents
         One or more of your parents           One or more of your parents         One or more of your parents
         left you in the wilderness to         were poisoned. This may have        turned on your own people and
                                                                                                                        When I was growing up in
   2     fend for yourself. Maybe they         been the work of a professional     sold out the elder races to the      Oxenfurt it was quite an open
         couldn’t afford to keep you;          rival, or it may have been to get   humans. Your parents are un-         and freewheeling city. There
         maybe you were an accident.           your parents out of the way.        welcome in your homeland.            was the ferment of advanced
         One or more of your parents           The secret police took your         One or more of your parents          thought everywhere. Every once
         were cursed by a mage or due          parent or parents for ‘question-    killed themselves out of despair.    in a while a professor or student
   3     to the intense hatred of some-        ing.’ The next week their bodies    With no hope of regaining the
         one they encountered. The             were found hung in the streets      glory of the past, they gave up
                                                                                                                        would be arrested for heresy,
         curse took their life.                of the city.                        and ended it.                        but other than that, Redani-
         One or more of your parents           One or more of your parents         While traveling, one or more of      an control was largely unseen.
         sold you for coin, or perhaps         were killed by a rogue mage.        your parents fell prey to human      Even though the students were
   4     traded you for some goods or          Most likely they tried to turn      racism. They died in a pogrom        often too poor to buy my fa-
         service. Your parents needed          the mage in question in to the      and their bodies were displayed      ther’s shoes, it looked like a vital
         the money more than you.              Empire and paid the price.          on pikes.
                                                                                                                        and carefree way of life. When I
                                       One or more of your parents                 One or more of your parents          and my siblings were older and
         One or more of your parents
                                       were imprisoned for unlawful                have become obssessed with
   5
         joined a gang. You saw this
                                       magic. Maybe they actually                  regaining the former glory           some had perished of the usual
         gang often and were sometimes                                                                                  childhood maladies, my mother
                                       commited the crime or maybe                 of their race. They sacrifice
         forced to work with them.
                                       it was a setup.                             everything for this cause.           was able to take a job cleaning
                                        One or more of your parents                One or more of your parents          house for an alchemy professor.
         One or more of your parents
         were killed by monsters. It is
                                        were exiled to the Korath De-              were exiled from your                I sometimes went with her and
   6                                    sert. Likely they committed a              homeland. There are many pos-        saw science all over the floor,
         your decision as to what they
                                        major crime but killing them               sible reasons, from crime to
         may have fallen prey to.
                                        would cause trouble.                       dissenting opinons.                  walls and ceiling. It was then
                                                                                                                        that I realized my calling was in
         One or more of your parents           One or more of your parents         One or more of your parents
         were falsely executed. They may       were cursed by a mage. The          were cursed. You can decide          the humanities.
   7                                                                                                                             –Brandon Of Oxenfurt
         have been a scapegoat for some-       mage likely had a vendetta          what this curse is or, the Game
         thing or just in the wrong place.     against them.                       Master can decide.
         One or more of your parents           Your parents simply left you        Your parents gave you to an-
         died of a plague. There was           one day. You may not even           other family so that you could
   8
         nothing that could be done but        know why they did it. One day       survive, because they couldn’t
         try to ease their passing.            your parents just disappeared.      care for you.
         One or more of your parents           One or more of your parents         One or more of your parents
         defected to Nilfgaard. They           were enslaved. They either          joined the Scoia’tael in an at-
   9     may have been given a deal for        commited a crime against the        tempt to get revenge on the hu-
         information or they may just          Empire or were set up by a ri-      mans who they see as ruining
         have jumped the border.               val.                                their lives.
         One or more of your parents           One or more of your parents         One or more of your parents
         were kidnapped by nobles.             were sent to the North as dou-      died in an ‘accident’. Most likely
   10    Likely it was your mother, who        ble agents. You likely don’t even   they made a powerful enemy
         attracted the attention of a local    know where they are now, but        that finally found a way to get
         lord or his son.                      they’re serving the Emperor.        rid of them.
```

<a id="page-28"></a>

### Страница 28

```text
      28

                                     Family Status
      Non-Human                      Everyone grows up differently. One man may come of age in a palace, as the son of a
       Nobility                      king, while another toils as a slave in the vineyard of a wealthy man. Your family status
                                     can tell a lot about how you grew up and what kind of person you turn out to be.
You may wind up rolling Ar-          Roll 1d10 or choose below, then go to Most Influencial Friend.
istocracy as a non-human
living in human territory. In         Roll        Northern Status                   Nilfgaardian Status                   Elderland Status
Nilfgaard this isn’t much of a                Aristocracy                         Aristocracy                         Aristocracy
problem, since they are more                  You grew up in a noble manor        You grew up in a manor, train-      You grew up in a palace and were
                                              with servants to wait on you,       ing to be well-versed in the        constantly reminded of the glory
accepting of non-humans. In             1     but you were always expected        world of the court. The luxury      of the past. You were expected to
the North, assume that your                   to behave and impress.              was just your incentive.            live up to the legacy.
family are less traditional ar-               Starting Gear:                      Starting Gear:                      Starting Gear:
istocracy and more highly                     Paper of Nobility (+2 Reputation)   Paper of Nobility (+2 Reputation)   Paper of Nobility (+2 Reputation)
skilled or prized people in the               Adopted by a Mage                   High Clergy                         Noble Warrior
eyes of the local king.                       You were given to a mage at a       You were raised among the clergy    You grew up as a noble warri-
                                              young age. You lived in comfort     of the Great Sun. You grew up pi-   or’s child, expected to rise to
                                        2     but barely saw your caretaker,      ous and always aware that the       your family’s reputation and to
                                              who was always busy.                Church would guide you.             never dishonor your heritage.
                                              Starting Gear:                      Starting Gear:                      Starting Gear:
 Nilfgaardian Slaves                          A Chronicle (+1 Education)          A Holy Symbol (+1 Courage)          Personal Heraldry (+1 Reputation)
Yeah, slavery’s pretty common                 Knights                             Knights                             Merchants
in Nilfgaard. Durin’ the last                 You grew up in a manor where        You grew up knowing that your       You grew up among traveling
few wars we’d find Nilfgaard-                 you learned to be a proper lady     duty was to the Emperor, and        merchants. Life was difficult
                                        3     or lord. Your fate was set from     that all of your luxury was a       sometimes but non-human
ian companies draggin’ whole
                                              birth.                              reward for your eventual service.   crafts are always valuable.
villages of folk back down to                 Starting Gear:                      Starting Gear:                      Starting Gear:
the south to serve Nilfgaardian               Personal Heraldry (+1 Reputation)   Personal Heraldry (+1 Reputation)   2 Acquaintances
lords. Worse, ya’d find plenty of             Merchant Family                     Artisan Family                      Scribe Family
bastards sellin’ off their own kin            You grew up among merchants         You grew up in an artisan’s         You grew up as the child of
to the black ones. Don’t much                 and you were always surround-       shop, learning to craft products    scribes, recording and protect-
                                        4     ed by yelling, haggling, and        for sale around the world. You      ing as much elderfolk history as
know what it’s like for the un-
                                              money.                              learned the value of quality.       possible.
lucky folk who get caught but                 Starting Gear:                      Starting Gear:                      Starting Gear:
I can’t imagine it’s pleasant.                2 Acquaintances                     3 Common Diagrams/Formulae          A Chronicle (+1 Education)
Ya mostly hear about the folk                 Artisan Family                      Merchant Family                     Entertainers
who’ve been “indentured”. Fan-                You grew up in an artisan’s         You grew up selling products        You grew up singing songs and
cy term for puttin’ criminals into            workshop. Your days were filled     all around the Empire. You saw      performing plays. You worked
                                        5     with the incessant sounds of        all kinds exotic of goods from      backstage, helped write songs,
temporary slavery. Turns out if
                                              creation, and often long.           all around the world.               and fixed instruments.
your family commits a crime                   Starting Gear:                      Starting Gear:                      Starting Gear:
that ain’t too bad but ain’t small            3 Common Diagrams/Formulae          2 Acquaintances                     1 Instrument & 1 Friend
enough to forgive, ya can be in-              Entertainer Family                  Born into Servitude                 Artisan Family
dentured to a lord or lady. It’s              You grew up with a band of per-     You were born into servitude        You grew up in a family of
all temporary of course. Ya live              formers. You may have traveled      and lived in simple quarters.       artisans, visiting ancient palac-
                                       6-7    or you may have performed at        You owned very little and toiled    es for inspiration and spending
in their servants’ quarters, ‘work
                                              a theater.                          often.                              hours every day on projects.
off’ your crimes against the                  Starting Gear:                      Starting Gear:                      Starting Gear:
Empire. While you’re there ya                 1 Instrument & 1 Friend             A trained bird or serpent           3 Common Diagrams/Formulae
might as well be a slave though.              Peasant Family                      Peasant Family                      Lowborn Family
                 –Rodolf Kazmer               You grew up on a farm in the        You grew up on one of the           You grew up in a lowborn fam-
                                              countryside. You didn’t have        thousands of farms across the       ily, tending to the manors of
                                       8-10   much to your name and your          Empire. You had little to your      others or working small jobs
                                              life was simple, but dangerous.     name but life was simple.           around your home city.
                                              Starting Gear:                      Starting Gear:                      Starting Gear:
                                              A Lucky Token (+1 Luck)             A Lucky Token (+1 Luck)             A Lucky Token (+1 Luck)
```

<a id="page-29"></a>

### Страница 29

```text
                                                                                                                                         29

Most Influential Friend
Most people can point to someone they knew in their life who helped shape them. Roll                                 Sentimental Items
1d10 or choose below, then go to Siblings.                                                                         The items you get from your
                                                                                                                   friend aren’t really meant to be
 Roll       Northern Status                 Nilfgaardian Status                  Elderland Status
                                                                                                                   particularly useful. Even the
        A Church                          The Cult of the Great Sun          A Human
        You grew up with influence        Your greatest influence was the    Your greatest influence was a hu-
                                                                                                                   dimeritium in the ring given
   1    from your local religion and      Church. You spent years learn-     man who taught you that some-         to you by a mage hunter isn’t
        spent hours a day at church.      ing chants and rituals.            times racism is unfounded.            enough to seriously perturb a
        Gear: A Holy Text                 Gear: A Ceremonial Mask            Gear: A Straw Doll                    mage. The importance of the
        An Artisan                        An Outcast                         An Artisan                            item is its sentimental value to
        Your greatest influence was an    Your greatest influence was a      Your greatest influence was an        your character.
   2    artisan who taught you to ap-     social outcast who taught you      artisan who taught you to ap-
        preciate art and skill.           to always question society.        preciate great elderfolk art.
        Gear: A Token You Made            Gear: A Bright Colorful Badge      Gear: A Small Token You Made
        A Count                           A Count                            A Noble Warrior
        Your greatest influence was a     Your greatest influence was a      Your greatest influence was a           Brandon’s Mentor
   3    count or countess who taught      count who taught you how to        War Dancer or a Mahakaman             Professor Eudarius, my men-
        you how to compose yourself.      lead and instill order.            Defender who taught you honor.
        Gear: A Silver Ring               Gear: A Silver Necklace            Gear: A Token of Battle
                                                                                                                   tor, was not a man appreciated
                                                                                                                   in his own time. Many history
        A Mage                            A Mage                             A Highborn
        Your greatest influence was a     Your greatest influence was a      Your greatest influence was a         scholars are called to appear at
   4    mage who taught you not to fear   mage who taught you the            highborn who taught you pride         the court of this or that noble.
        magic and to always question.     importance of order and caution.   and how to comport yourself.          Their primary employment
        Gear: A Small Pendant             Gear: An Emblem                    Gear: A Signet Ring                   there is the tracing of family
        A Witch                           A Solicitor                        An Entertainer                        lineages. It is a study more prof-
        Your greatest influence was a     Your greatest influence was an     Your greatest influence was an en-
                                                                                                                   itable than interesting. How-
   5    village witch who taught you      imperial detective. You spent a    tertainer who taught you the im-
        the importance of knowledge.      lot of time solving mysteries.     portance of happiness and beauty.     ever Professor Eudarius was
        Gear: A Black Magic Doll          Gear: A Magnifying Lens            Gear: A Playbill or Ticket            fascinated by the history of the
        A Cursed Person                   A Mage Hunter                      A Raider                              werebbubbs. He was extremely
        Your greatest influence was a     Your greatest influence was a      Your greatest influence was a raid-   knowledgeable and had trav-
   6    cursed person who taught you to   mage hunter who taught you to      er who taught you that you have       eled to the last known secret
        never judge others too harshly.   be cautious of magic and mages.    the right to take what you need.
                                                                                                                   enclaves of the elusive creatures
        Gear: A Carved Totem              Gear: A Ring with Dimeritium       Gear: A Satchel
                                                                                                                   in the mountains to the east. He
        An Entertainer                    A Man At Arms                      A Sage
        Your greatest influence was an    Your greatest influence was a      Your greatest influence was a
                                                                                                                   also knew a great deal about
   7    entertainer who taught you        soldier who shared stories of      sage who taught you about the         the private lives and financial
        plenty about showmanship.         danger and excitement.             importance of elderfolk history.      dealings of other professors,
        Gear: A Playbill or Ticket        Gear: A Trophy of Battle           Gear: A Book of Tales                 which stood him in good stead.
        A Merchant                        An Artisan                         A Criminal                            I learned a great deal from him.
        Your greatest influence was a     Your greatest influence was an     your greatest influence was a                  –Brandon Of Oxenfurt
   8    merchant who taught you how       artisan who taught you to ap-      criminal who taught you to fol-
        to be shrewd and clever.          preciate skill and precision.      low your own rules.
        Gear: A Coin You Earned           Gear: A Trinket You Made           Gear: A Mask
        A Criminal                        A Sentient Monster                 A Hunter
        Your greatest influence was a     Your greatest influence was a      Your greatest influence was a
   9    criminal who taught you how       sentient monster that taught you   hunter who taught you how to
        to take care of yourself.         that not all monsters are evil.    survive in the wilderness.
        Gear: A Mask                      Gear: A Strange Totem              Gear: A Trophy of a Hunt
        A Man At Arms                     An Entertainer                     A Lowland Farmer
        Your greatest influence was a     Your greatest influence was an     Your greatest influence was a
  10    soldier who taught you how to     entertainer who taught you to      lowland farmer who taught you
        defend yourself.                  express yourself.                  how to live happily.
        Gear: A Battle Trophy             Gear: A Token from a Fan           Gear: A Farmer’s Spade
```

<a id="page-30"></a>

### Страница 30

```text
      30

                                     Siblings
     Only Children                   People on the continent tend to die young, from disease, famine, or just pure violence.
                                     This means families tend to be very large to make up for the high death rates. Exactly
If you don’t have any siblings
                                     how large changes from region to region.
and you die, you can come
                                     Roll 1d10 or choose below.
back as a friend. Work with
your Game Master to stat out
your friend, and remember              Roll       Northern             Nilfgaardian                       Non-Humans
that you may have to change             1                1                  1               Elves can have up to 2 siblings. Roll 1d10. On
said friend a bit to fit them into      2                2                  2               a 1-2 you have one sibling. On a 9-10 you have
the adventure at hand.                                                                       two siblings. On a 3-8 you are an only child.
                                        3                3                  3
                                        4                4                  4                  Dwarves use the Nilfgaardian chart for
                                        5                5                  5                                siblings.
                                        6                6              Only Child
     Multiple Rolls
                                        7                7              Only Child
Any time you see a table with
multiple headers highlighted            8                8              Only Child
in blue, roll separately for each       9         Only Child            Only Child
of the headers. This is used to         10        Only Child            Only Child
determine many parts of an
NPC such as your siblings,
friends, or enemies.                   Roll     Gender         Age      Feelings About You                      Personality
                                         1        Male       Younger       Wants You Dead                            Shy
                                         2       Female      Younger       Can’t Stand You                       Aggressive
  Enemies At Home                        3        Male       Younger        Jealous of You                          Kind
If your sibling is jealous of            4       Female      Younger    No Feelings About You                      Strange
you, can’t stand you, or wants           5        Male       Younger    No Feelings About You                    Thoughtful
you dead it’s very possible that         6       Female       Older     No Feelings About You                     Talkative
they may wind up being used              7        Male        Older     No Feelings About You                     Romantic
as an enemy against you over             8       Female       Older             Likes You                           Stern
the course of the game. This
                                         9        Male        Older       Looks Up To You                        Depressive
sibling isn’t considered an en-
emy right away, but with the            10       Female       Twin        Possessive of You                       Immature
right suggestions from out-
side forces they may come to
be a dedicated enemy. If you         Death & Siblings
die and decide to play a sib-
                                     Just like the Witcher novels and video games, the Witcher pen and paper TRPG is danger-
ling that was your enemy you
                                     ous. If you take on a threat far greater than yourself, have a stroke of bad luck, or follow a
can definitely do it (as long as
                                     suicidal plan, there is a very high chance you’re going to wind up getting killed off. Since
your GM agrees). It could lead
                                     this is a world without resurrection, your character is 110% dead and won’t be coming back
to interesting player dynamics,
                                     unless someone uses necromancy to drag your consciousness back into your corpse for a
especially if that sibling was re-
                                     few minutes.
sponsible for your first charac-
                                               This is where siblings come in! We suggest that if your character dies and they have
ter’s death.
                                     siblings, you pick up as any one of them. The GM can more easily find a way to fit your sib-
                                     ling into the party, usually via them finding out about their sibling’s death. It also stands to
                                     reason that if your companions are nice they will be more willing to give a sibling your old
                                     character’s stuff.
```

<a id="page-31"></a>

### Страница 31

```text
                                                                                                                      31


Your Life Events
After you’ve figured out how you grew up and found your niche, you get to find out
                                                                                                 Non-Humans & Age
                                                                                                 All non-humans are incredibly
                                                                                                 long-lived assuming they aren’t
what has happened to you over the course of your life. You could get disgustingly lucky          killed early. Elves and dwarves
and have all sorts of friends, boons, and skill improvements, but you could also get             can live for hundreds of years if
struck by disaster. It’s all a toss-up, just like most people’s lives. For every full 10 years   they aren’t murdered and they
you’ve been alive, roll 1d10 on the table below to determine what the most important             don’t succumb to a disease or
event of that decade was.                                                                        horrible accident.


   Roll               Event
    1-4       Fortune or Misfortune
    5-7        Allies and Enemies
   8-10             Romance
```

<a id="page-32"></a>

### Страница 32

```text
      32

                                     Fortune or Misfortune
        Addiction                    Sometimes your life sits on a knife’s edge. A little too much pressure in one direction or the
When you are addicted to             other can send you plummeting into misfortune or tumbling into unforseen blessings. It’s a
something you feel the need          gamble but if you get lucky you can find yourself with unexpected income, new friends, favors,
for that thing every day. You        and even status. Just make sure to avoid addiction and insanity.
must roll under your WILL            Roll 1d10. On an even, roll on the Fortune table. On an odd, roll on the Misfortune table.
each day you don’t get your
fix. If you fail, you can think       Roll                    Fortune                          Roll                  Misfortune
about nothing but getting your                               Jackpot                                                    Debt
fix and take a -5 to all other ac-      1    Some major event or stroke of luck brought         1     You fell deeply into debt to the tune of
tions. Every day you don’t get                        you 1d10x100 crowns.                                       1d10x100 crowns.
your fix you lower your WILL                               Find a Teacher                                         Imprisonment
(for the sake of this check) by 1,      2    You trained with a teacher. Gain +1 in any         2     Something you did (or a false acusation)
                                               INT skill or start a new INT skill at +2.                had you imprisoned for 1d10 months.
making it harder and harder to
keep making the checks. Any                             A Noble Owes You                                              Addiction
                                        3    Something you did gained you 1 favor from          3     You contracted an addiction. You can
time your addiction is offered                      a nobleman/noblewoman.                            choose. See the sidebar for addiction rules.
to you, you must make a roll
                                                      Find a Combat Teacher                                Lover, Friend or Relative Killed
under your WILL (modified               4    You trained with a soldier. Gain +1 in any               Roll 1d10. 1-5: They died in an accident,
by the number of days you                                                                       4
                                             combat skill or start a new combat skill at +2.          6-8: They were murdered by monsters,
haven’t had your fix) to not                          A Witcher Owes You                                9-10: They were murdered by bandits.
partake immediately. You can            5    You encountered a witcher at some point                                   False Accusation
kick an addiction by going for               and managed to garner a favor from them.                 Roll 1d10. 1-3: The accusation is theft, 4-5:
                                                                                                5
                                                                                                      It’s cowardice or betrayal, 6-8: It’s murder,
3 weeks without indulging in                              Fell in with Bandits
                                        6    You fell in with a bandit gang. Once per month                 9: It’s rape, 10: It’s illegal witchcraft.
your addiction. You don’t need
                                                  you can ask these bandits for 1 favor.                            Hunted by the Law
to make successful addiction                                                                          Roll 1d10. 1-3: It’s just a few of guards, 4-6:
checks, you just can’t partake                          Tamed a Wild Animal                     6
                                             You tamed a wild animal you encountered                  It’s an entire small town, 7-8: It’s a major city,
in the addiction.                       7
                                             in the wilderness. Roll 1d10. 1-7: Wild Dog,                   9-10: A whole kingdom is after you.
                                                             8-10: Wolf.                                               Betrayal
                                                       A Mage Owes You                                Roll 1d10. 1-3: You are being blackmailed,
                                                                                                7
                                        8    You managed to garner 1 favor from a pow-                4-7: A secret was exposed, 8-10: You were
                                                     erful mage you helped.                             betrayed by someone very close to you.

                                                        Blessed by a Priest                                            Accident
                                             You were given a holy symbol that you can                Roll 1d10. 1-4: You were disfigured.
                                        9                                                             Change your social standing to feared,
                                             show to people of that faith to gain a +2 to
                                                       Charisma with them.                            5-6: You were healing for 1d10 months,
                                                                                                8
                                                                                                      7-8: You lost a 1d10 months of memory
                                                              Knighted                                from that year, 9-10: You suffer from hor-
                                             You were knighted for valor in a random                  rible nightmares (7 in 10 chance each time
                                       10
                                                kingdom. In this kingdom you gain +2                                  you sleep).
                                              reputation and are recognized as a knight.
                                                                                                         Mental or Physical Incapacitation
                                                                                                      Roll 1d10. 1-3: You were poisoned; per-
                                                                                                      manently lose 5 HP, 4-7: You suffer from
                                                                                                      anxiety attacks and must make Stun saves
                                                                                                9
                                                                                                      (every 5 rounds) in times of stress, 8-10:
                                                                                                      You have a major psychosis. You hear
                                                                                                      voices and are violent, irrational, and de-
                                                                                                       pressive. The GM controls these voices.
                                                                                                                       Cursed
                                                                                                10    You have been cursed. See the Curse sec-
                                                                                                       tion on pg.230 to determine the details.
```

<a id="page-33"></a>

### Страница 33

```text
                                                                                                                  33

Allies & Enemies
Enemies are inevitable. You’re going to make them, especially in a world like this. They       Meeting Friends
can really shape your character, especially if you weren’t the offended party. Allies, on
                                                                                            Besides giving you another op-
the other hand, are absolutely indispensable. A good friend can save your life or make
                                                                                            tion when your current char-
things easier on you in tough times.
                                                                                            acter dies, friends can be very
Roll 1d10. On an even you make an Ally, on an odd you make an Enemy.
                                                                                            useful for plenty of situations
                                                                                            in game. You can hunt up your
Allies                                                                                      friends for favors, safe places to
                                                                                            stay, and allies in particularly
  Roll      Gender                    Position                 How You Met                  tough times. Friends can also
    1         Male                A Bounty Hunter         Saved Them from Something         be encountered during the plot
    2        Female                    A Mage                   Met in a Tavern             of your game to give you NPCs
    3         Male            A Mentor or Teacher       They Saved You from Something       that your character already
    4        Female            A Childhood Friend        They Hired You for Something       knows and has a rapport with.
    5         Male                   A Craftsman          You Were Trapped Together
    6        Female                An Old Enemy        You Were Forced to Work Together
    7         Male                A Duke/Duchess         You Hired Them for Something
    8        Female               A Priest/Priestess   You Met While Drunk and Hit It Off
    9         Male                    A Soldier             You Met While Traveling
   10        Female                    A Bard                 You Fought Together



    How Close Are You?
  Roll                Closeness
    1                Acquaintances
    2                Acquaintances
    3                Acquaintances
    4                Acquaintances
    5                   Friends
    6                   Friends
    7                 Close Friends
    8                 Close Friends
    9                  Inseperable
   10                Bound By Bond




         Where Are They?
  Roll                  Region
   1-3         The Northern Kingdoms
   4-6         The Empire of Nilfgaard
   7-9                 Elder Lands
    10          Beyond the Boundaries
```

<a id="page-34"></a>

### Страница 34

```text
      34

                                      Enemies
     Enemy Power                        Roll      Gender                  Position                          The Cause
Your enemy’s power as rolled              1            Male                Ex-Friend                 Assaulted the Offended Party
below is more of an abstract.             2        Female                  Ex-Lover                 Caused the Loss of a Loved One
Think of it as a guideline or a           3            Male                 Relative                  Caused Major Humiliation
starting point for the GM to
                                          4        Female              Childhood Enemy                     Caused a Curse
build a villain based on that
type of power. A socially pow-            5            Male                A Cultist                 Accused of Illegal Witchcraft
erful enemy might become                  6        Female                   A Bard                   Turned Down Romantically
very influential in local or              7            Male                A Soldier                   Caused a Terrible Wound
world politics, while a enemy             8        Female                  A Bandit                           Blackmail
with powerful minions may                 9            Male             A Duke/Duchess                       Foiled Plans
have a troll or a small gang              10       Female                   A Mage                     Caused a Monster Attack
backing them up, and a mag-
ically powerful enemy might
be a cunning mage or have a           Who Was Wronged
powerful magical weapon.
                                      It may not be you who was wronged. In this world there are a lot of people playing out a lot
                                      of different plans. It’s very possible you made an enemy without even realizing. Roll 1d10 or
                                      choose:
                                               Even: You were the one who was wronged.
Befriending Enemies
                                               Odd: You wronged someone else.
It’s very possible that you
wind up befriending an ene-           Roll below to see how powerful your enemy is and where their power is focused.
my. Granted, this is much less
likely if your enemy is out for         Roll    Power         How Far Has It Escalated?                What Is Their Power?
blood, but it’s still possible. You       1        1           They/You Have Mostly Forgotten                  Social Power
may wind up reconciling your              2        2           They/You Have Mostly Forgotten                  Social Power
differences peacefully or be-
                                          3        3              They/You Plan to Backstab                     Knowledge
ing forced to team up against
                                          4        4              They/You Plan to Backstab                     Knowledge
some larger threat. If this hap-
pens and the GM allows it,                5        5          They/You Will Attack If Encountered                Physical
you can take that enemy off               6        6          They/You Will Attack If Encountered                Physical
your list of enemies and maybe            7        7            They/You Will Hunt for Revenge                   Minions
even move them to your list of            8        8            They/You Will Hunt for Revenge                   Minions
friends.                                  9        9              They/You Are Out for Blood                      Magic
                                         10       10              They/You Are Out for Blood                      Magic
```

<a id="page-35"></a>

### Страница 35

```text
                                                                                                                                         35

Romance




Romance isn’t exactly uncommon in the world of The Witcher, but happy romance is.                                    Happy Love Affairs
One-night stands and love affairs that end in death or depression are far more common.                            Enduring joy and true love are
Roll 1d10 below to determine how your romance went for that year.                                                 a possiblilty. But they are rare. If
                                                                                                                  you achieve it, it’s assumed that
 Roll             Love Affair                                   Whores & Debauchery                               you are happy together until
    1            A Happy Love Affair                                                                              you roll another romance of a
                                                       Whores and Debauchery means that you spent
   2-4           A Romantic Tragedy                    your time sleeping around, buying whores and per-          different type. That roll then
   5-6           A Problematic Love                    haps leaving a trail of bastard children in your wake if   applies to your current lover.
  7-10        Whores and Debauchery                                      you weren’t careful.

         Romantic Tragedy                                       Problematic Love
 Roll                   Tragedy                          Roll                    Problem
         Your Lover was captured by bandits some                 Your Lover’s family or friends hate you and
   1                                                       1
              time ago and is still their captive.                     do not condone your romance.
         Your Lover mysteriously vanished one day                Your Lover works as a whore for a living
   2                                                       2
           and you don’t know where they went.                        and refuses to give up their job.
         Your Lover was imprisoned or exiled for                 Your Lover is under a minor curse such as
   3                                                       3
            crimes they may not have commited.                        paranoia or horrible nightmares.
            Your Lover was taken from you by a                   Your Lover slept around and refused to stop
   4                                                       4
                     powerful curse.                                        when you found out.
         Something got between you and your Lover                Your Lover is insanely jealous and can’t
   5                                                       5
             and you were forced to kill them.                    stand you being around any possible rival.
         Your Lover comitted suicide. You may not                You fight constantly and nothing can stop it
   6                                                       6
                   know why they did it.                         for long. You always descend into screaming.
         Your Lover was kidnapped by a noble and                 You’re professional rivals of some sort. You
   7                                                       7
                  made into a concubine.                           steal customers from each other often.
         A rival cut you out of the action and stole             One of you is human and the other is
   8                                                       8
                    your Lover’s affection.                       non-human, making your life difficult.
         Your Lover was killed by monsters. It may               Your Lover is already married. They may
   9                                                       9
             have been an accident or planned.                   or may not be willing to leave their spouse.
            Your Lover is a mage, a witcher, or a                Your friends or family hate your Lover and
  10                                                      10
          sentient monster, dooming the romance.                       do not condone your romance.
```

<a id="page-36"></a>

### Страница 36

```text
     36


        Surnames
Northern humans usually have
                                     Your Personal Style
                                     Every character has their own style that sets them apart. Geralt, whether he’s rocking a
“of x” as their last name. This
                                     full beard or friendly muttonchops, always has his white hair, two swords on his back, and
means human names are usu-
                                     well-worn light armor. If you want to take a random crack at style or you’re just not sure
ally things like: Olsen of Ker-
                                     what your character is like, roll below. Roll once for each column.
rack or Agnes of Aldersburg.
In Nilfgaard, where a dialect of
the Elderspeech is the prima-
                                     Style
ry language, names are joined          Roll              Clothing                   Personality                Hair style                  Affectations
with either “Var,” which indi-           1                A Uniform                    Secretive               Long & Loose                      Trophies
cates membership in a family             2            Traveling Clothing              Rebellious              Cropped Short                Rings & Jewlery
or “Aep,” which is used like “son
                                         3              Fancy Clothing                  Violent               Self-Cut Short                     Trinkets
of.” This gives you names like
                                         4             Ragged Clothing                 Idealistic                 Braided                        Tattoos
“Emyr Var Emreis” & “Liam
                                         5            Utilitarian Clothing          Contemplative              Long & Wild                   War Paint
Aep Muir Moss.” In some re-
gions you will see variants on           6            Traditional Clothing               Stern                      Bald                   Shadowy Cloak
this, as in some places in the           7            Revealing Clothing              Deceptive              Uniformly Short               Bright Bandanas
North and Nilfgaard where                8              Heavy Clothing                 Friendly              Ragged & Messy                   Eye Patch
“De” or “Van” is used instead            9             Strange Clothing                Arrogant             Complicated Hairstyle                 Furs
of “of,” giving us names like           10            Flamboyant Clothing              Nervous                 Shaven Sides             Insignias & Plaques
“Jacques De Aldersburg” and
“Carthia Van Canten.” These
are generally associated with
                                     Values
nobility, however. Compar-             Roll      Valued Person                       Value                           Feelings on People
atively, non-humans usually             1                A Parent                     Money                        People Are Tools to Be Used
have surnames like Bibervelt,           2                A Sibling                    Honor                   Our Kind Are Fine but Plough the Rest
Chivay, and the like. For most          3                A Lover                    Your Word                      People Can Never Be Trusted
elder races you are reasonably
                                        4                A Friend               Hedonistic Pursuits              People Have to Prove Themselves
safe to take Welsh surnames,
                                        5                Yourself                  Knowledge                                     Neutral
though for dwarves we suggest
that you use surnames from              6                  A Pet                    Vengeance                                    Neutral
more “exotic” regions, such as          7                A Mentor                     Power                                People Are Great
Hungary and other countries             8             A Public Figure                  Love                          Everyone Deserves to Die
in that region.                         9            A Personal Hero                 Survival                      People Are Hedonistic Swine
                                        10                No One                    Friendship                             All Life Is Valuble
   Common Names
Names in The Witcher tend to
vary based on region. Nordling
                                     Example Names
names are generally Europe-              Nordling               Elder Speech                  Skelliger                Elven                     Dwarven
an while names in the Elder
                                              Olsen                   Aelwen                      Sigurd               Yaevinn                     Rodolf
Speech are usually Welsh (or
                                             Dagread                  Taliesin                    Aksel                Iorveth                     Zoltan
Celtic in the case of some elves).
Once again, Skelligers are an                Adalbert                   Wynn                        Laila             Aelirenn                     Yarpen
exception. Generally Skel-                    John                      Yorath                   Ragnar              Filavandrel                   Barclay
liger names are Scandinavian.                 Agnes                  Brynmor                    Brynhild                Ge’els                    Brouver
Dwarves who speak their own                  Aplegatt                   Carys                       Olaf              Shiadhal                     Golan
languages have more exotic                   Carduin                    Deryn                    Hakon                 Nithral                   Rhundurin
sounding names in general.
```

<a id="page-37"></a>

### Страница 37

```text
                                                                                                                       37


Your Profession




In the Witcher TRPG, your profession is what you do to make your living. This is what
your are best at and determines your basic skill set and starting possessions. Remem-                   Witcher Gear
ber, your profession only establishes what you do for a living. Except in the case of             Witchers’ special gear can be
magic, it does not limit how good you can be at other things. It establishes where you’ll         found in the Witchers section
probably want to focus your improvement but does not tie you down. The best example               starting on pg.246.
of this is Zoltan Chivay (in the Witcher video games). Zoltan, one of Geralt of Rivia’s
best friends, is a hard-drinking, hard-fighting dwarf who helps hold the walls of Vergen
against the forces of King Henselt of Kaedwen. By profession, Zoltan is a merchant and
later a tavern owner.
Each profession has five parts:                                                                           A Witcher
                                                                                                         is a Witcher
                                                                                                  The Witcher race and profes-
1. Defining Skill                                 3. Magic Perks                                  sion go together. If you choose
Each profession has a defining skill. This        Professions with inherent magic have magic
                                                                                                  one, you must choose the other.
one skill separates this profession from all      perks. These are spells, incantations, hexes,
of the others—an ability that only a person       rituals, and signs.
with years of training in that field can ac-
quire. The defining skill is counted in the
profession skill package when buying skills.      4. Skill Package                                  Mage Limitations
                                                  Each profession has a skill package which       The only two races to mani-
                                                  represents general learning over the course     fest magic to any great extent
2. Vigor                                          of an apprenticeship.                           are humans and elves. You can
Each profession has a starting allowance of                                                       only play a priest or a mage if
Vigor, which represents how much primal                                                           you chose human or elven as
chaos you can channel through your body           5. Starting Gear                                your race. Keep in mind, that
safely to cast spells, perform rituals, and in-   Each profession has starting gear that you      elves have no established priests
flict hexes.                                      can choose from. This are items that you        in their society so any elven
                                                  would probably have and use in your daily       character wishing to play priest
                                                  life, working in that profession.               must follow a human deity.
```

<a id="page-153"></a>

### Страница 153

```text
                                                                                                                    153

         Finally, your facing is just what di-   Fast Strikes Versus Strong
rection you’re facing and thus what direc-       Strikes                                              Holding Action
tion your vision cone is facing. Changing        When making an attack you can make ei-            You can choose to act later in
facing as part of your movement is consid-       ther a fast strike or a strong strike. A fast     the round by holding your
ered a free action.                              strike allows you to attack twice in one          action. If you choose to hold
                                                 round without penalty. These attacks don’t        your action, the initiative or-
Ambushes                                         have to be made against the same target as        der continues as normal but
You gain bonuses against enemies by sneak-       long as both targets are within range. Fast       you can jump in and act be-
ing up on them. You must be the one to in-       strikes can be very useful when you are sur-      fore or after someone further
stigate a combat to ambush a target. First,      rounded by a large group of enemies.              down the initiative list. If you
make a successful Stealth check against the               When making a strong strike, you         hold your action until the
target’s Awareness check. If you succeed,        make one huge attack at a -3 to your roll         very end of the round, you
you go unnoticed and can sneak up on your        which does double damage against the op-          must either use your turn or
opponent. Next, make your attack. You gain       ponent. Strong strikes are best when you          sacrifice it. You cannot hold
a +5 against all targets who were unaware        need to do a lot of damage to a slower target     your action and choose to
of you. This bonus lasts for the first round     with a lot of armor.                              act at the beginning of the
of the combat. If one of your targets notices    •   Bows: When using a strong strike with a
                                                                                                   next round.
you but doesn’t have time to alert the rest,         bow you pull the bow to full draw and fire,
you still get the bonus against those who            doubling the damage. Since it takes quite a
aren’t aware. After you make your ambush             bit of time to draw and nock arrows, bows
attack, everyone in the area makes an initia-        can only fire once, even if making a fast
tive roll and initiative continues from there.       strike.
                                                                                                          Fast Draw
Your first attack (the ambush) isn’t counted     •   Crossbows: You cannot make strong or fast     By declaring a Fast Draw at
in the initiative.                                   strikes with a crossbow since they have one   the start of the round, you
                                                     draw length and draw weight.                  raise your initiative by +3
Damage                                                                                             for that round by taking a
Damage is split into two categories: lethal      Hit Location                                      -3 to your attack. However,
and non-lethal. Any wound that brings            After you attack, determine what body part        you must make an attack
you closer to death deals lethal damage.         you hit. Unless you aimed for a specific spot,    and you cannot benefit from
When your amount of lethal damage is             roll on the Humanoid or Monster Damage            aiming or any other aim-re-
equal to your Health Points, you enter           Location tables.                                  lated ability.
Death State and begin dying (see Death                     Aiming for specific parts is harder,
& Dying). Temporary damage that im-              but can be worth it. Each part has a penalty
pairs you (concussion, shock) is non-lethal      to hit it and a damage modifier. After you’ve
damage. When you have taken non-lethal           reduced your damage based on armor (see
damage equal to your Health Points, you          Damage Reduction), you multiply the re-
are knocked unconscious and treated as           maining damage based on the modifier for
stunned until you recover at least 20 points     the location.
of health with recovery actions and make a
Stun save.
        Damage of both types is usually de-
termined by rolling different combinations
of 6- or 10-sided dice. Different weapons
also do one of four different damage types:
piercing, slashing, bludgeoning, and ele-
mental.
```

<a id="page-154"></a>

### Страница 154

```text
    154

                                  Humanoid Damage                                  When an attack strikes you, subtract the SP
   Party Initiative               Location                                         of your armor from the incoming damage.
To speed things up, you can                                                        It’s important to remember that armor is
choose to designate one play-       Location      Roll    Penalty     DMG          based on location: A steel plate under your
er as the Leader of the party.                                                     silk shirt doesn’t protect your head.
                                       Head         1        -6          x3
The Leader rolls initiative for
the entire party and their roll       Torso        2-4       -1          x1        Damage Resistance
is added to each other play-          R. Arm        5        -3         x1/2       Damage resistance (DR) is structural or
er’s REF score to determine                                                        magical protection from specific damage
                                      L. Arm        6        -3         x1/2
their initative. This method                                                       types: fireproof clothes, for instance, or
                                      R. Leg       7-8       -2         x1/2       scaly skin that turns blades. Like armor, DR
is good for getting initiative
for large groups of enemies           L. Leg      9-10       -2         x1/2       saps the sting from attacks. If you take dam-
as well.                                                                           age of a type (piercing, slashing, bludgeon-
                                                                                   ing, elemental) you’re resistant to, halve the
                                  Monsters which have different anatomy            damage before applying your armor.
                                  from humans have a different table for dam-
                                  age location. When fighting a non-human-         Layering Armor
   Layering Table                 oid monster, roll on the Monster Damage          Layering armor may seem like a good idea.
                                  Location table.                                  Stack up a gambeson, a brigandine, and
Each extra layer of light or
                                                                                   some plate armor and you can laugh off a
medium armor adds +1 to
the EV of your total armor.
                                  Monster Damage Location                          damn ballista bolt! Unfortunately it doesn’t
                                                                                   work like that for two reasons.
Every layer of heavy armor
                                    Location      Roll    Penalty     DMG                   First, armor is cumulative: under-
adds +2 to the EV.
                                                                                   neath your brigandine is a gambeson and a
                                       Head         1        -6          x3        chain mail shirt and underneath your plate
                                      Torso        2-4       -1          x1        armor is another gambeson and another
                                     R. Limb       5-7       -3         x1/2
                                                                                   chain mail shirt. So your stacked gambe-
                                                                                   son, brigandine and plate armor is really
                                      L. Limb      8-9       -3         x1/2
                                                                                   three gambesons, a brigandine, two shirts
                                      Special      10        -2         x1/2       of chain mail, and plate armor over top of it
                                                                                   all. Throw in four layers of armored trousers
                                  Certain types of attacks (bombs, traps, and      and a great helm with two padded caps, two
                                  some spells, for example) strike multiple        chain mail coifs, and leather hood? Not only
                                  body locations at once. Bombs and explo-         do you look like the Michelin Man’s merce-
                                  sive traps hit everywhere, dealing their         nary brother, you’re also wearing about 39
                                  damage to every location separately. In this     kilograms of armor alone, each layer adding
                                  case, calculate full dice damage for each lo-    more encumbrance. For this reason you can
                                  cation separately.                               only stack three pieces of armor and you
                                                                                   can only wear one layer of heavy armor and
                                  Armor                                            one layer of medium armor.
                                  Armor is anything that makes it harder for                Second, each layer of armor doesn’t
                                  an attack to kill you. For players, this most-   add its full SP. Any armor lighter than your
                                  ly means reinforced clothing and plates of       heaviest armor acts as a buffer between you
                                  steel. For monsters, this can be hardened        and the blow. To determine how much ex-
                                  skin or natural shells. All armor has a stop-    tra armor you get subtract the lighter armor
                                  ping power (SP). The stopping power of ar-       from the heavier armor and find the differ-
                                  mor determines how much incoming dam-            ence on the table on the next page.
                                  age it absorbs when an attack strikes you.
```

<a id="page-157"></a>

### Страница 157

```text
                                                 157

Fumble Table
 Roll Type               Result
             1-5: No major fumble.
             6: Your weapon glances off and
             you are staggered.
             7: Your weapon lodges in a near-
             by object and it takes 1 round
             to free.
   Reflex    8: You damage your weapon se-
  (Melee)    verely. Your weapon takes 1d10
             points of reliability damage.
             9: You manage to wound your-
             self. Roll for location.
             >9: You wound a nearby ally.
             Roll location on a random ally
             within range.
             1-5: No major fumble.
             6: Your weapon takes 1d6 extra
             points of reliability damage.
             7: Your weapon is knocked from
             your hand and flies 1d6 meters
             away in a random direction (see
  Reflex     Scatter table).
 Defending   8: You are knocked to the
             ground. You are now prone and
             must make a Stun save.
             9: Your weapon takes 2d6 extra
             points of reliability damage.
             >9: Your weapon ricochets back
             and hits you. Roll for location.
             1-5: No major fumble.
             6-7: The ammunition you fired,
             or weapon you threw, hits some-
             thing hard, breaking.
             8-9: Your bowstring comes
   DEX       partially undone, your crossbow
 (Ranged)    jams, or you drop your thrown
             weapon. It takes 1 round to undo
             this.
             >9: You strike one of your allies
             with a ricochet. Roll location on
             a random ally within range.
             1-5: No major fumble.
             6: The attack glances off of you
             and you are staggered.
             7: You trip on something and fall
             prone.
             8: You trip and fall prone, drop-
             ping your weapon 1d6 meters
   DEX       away.
 (Defense)   9: You trip and hit your head.
             You are knocked prone, take 1d6
             points of non-lethal damage, and
             must make a Stun save.
             >9: You fail horribly and not
             only fall prone but also take 1d6
             lethal damage and must make a
             Stun save.
```

<a id="page-158"></a>

### Страница 158

```text
    158
                                  Critical Wounds                                         Critical Wounds Table
                                  Whenever you roll over your opponent’s
    Stabilizing VS                defense by 7 or more, you score a criti-                 Beat Defense Critical                      Bonus
       Treating                   cal wound. Every time you score a criti-                     By...     Level                        DMG
                                  cal wound, roll on the appropriate Critical                       7               Simple                3
Stabilizing a critical wound is   Wound table to see what extra harm you
akin to cauterizing a wound,                                                                        10             Complex                5
                                  inflict on your opponent. Each level of criti-
tying a tourniquet, or oth-       cal wound inflicts bonus damage and forces                        13              Difficult             8
erwise keeping the wound          the opponent to make a Stun save. Critical                        15              Deadly                10
from gushing blood or kill-       wounds can leave permanent impairments.
ing you some other way. It
requires a First Aid roll equal
to the Healing Hands DC of        Simple Critical Table
the wound. Once stabilized
the wounded party is at a
negative but no longer being
                                    Roll                          Effect                                Stabilized                Treated
killed by the wound. Only                                     Cracked Jaw
once a doctor has healed                     The blow cracked your jaw, making it hard to speak You are at a -1 to              You are at a -1 to
                                      12     clearly. You are at a -2 to Magical Skills & Verbal Magical Skills &                Magical Skills.
the wound with multiple                      Combat (Charisma, Persuasion, Seduction, Lead-       Verbal Combat.
Healing Hands rolls does the                 ership, Deceit, Social Etiquette, and Intimidation).
wound begin to heal. More
information can be found
                                                           Disfiguring Scar
                                                  The blow mangled your face in some way.               You take a -1 to
on pg.174.                            11     You are grotesque and difficult to look at. You take       empathic Verbal         You take a -1 to
                                             a -3 to empathic Verbal Combat (Charisma, Per-                Combat.                Seduction.
                                             suasion, Seduction, Deceit, Social Etiquette, and
                                                                Leadership).

                                                             Cracked Ribs
                                     9-10    The blow cracked your ribs, making it painful to You are at a -1 to                You take a -10 to
                                             breathe and exert strength. You take a -2 to BODY.    BODY.                         Encumbrance.
                                                     This does not effect Health Points.

                                                          Foreign Object                     Your Recovery &        You take a -2 to
                                     6-8     The blow lodged a piece of clothing or armor in Critical Healing are Recovery and a -1
                                             your wound, causing an infection. Your Recovery        halved.       to your Critical
                                                    and Critical Healing are quartered.                                Healing.

                                                            Sprained Arm                          You are at a -1 to ac-        You take a -1 to
                                     4-5     The blow sprained your arm, making it difficult to tions with that arm.              Physique.
                                             maneuver. You take a -2 to actions that use the arm.

                                                            Sprained Leg                        You take a -1 to
                                     2-3     The blow sprained your leg, making it difficult to SPD,    Dodge/Es- You take a -1 to
                                             walk and maneuver. You take a -2 to SPD, Dodge/ cape, and Athletics.       SPD.
                                                          Escape, and Athletics.
```

<a id="page-159"></a>

### Страница 159

```text
                                                                                                                        159
Complex Critical Table

 Roll                       Effect                           Stabilized             Treated            Monsters Without
                                                                                                          Anatomy
                   Minor Head Wound
  12     The blow rattled your brain and caused some inter- You are at a -1 to You are at a -1 to      Elementa and specters are
         nal bleeding. It’s hard to think straight. You take a -1 INT and WILL.      WILL.             kept alive by magic and do
                      to INT, WILL, and STUN.
                                                                                                       not have physical forms like
                           Lost Teeth                      You take a -2 to You take a -1 to           other living creatures.
  11     The blow knocked out some teeth. Roll 1d10 to see magical skills and magical skills and                  This means that
         how many teeth are lost. You take a -3 to magical   Verbal Combat.    Verbal Combat.
                    skills and Verbal Combat.
                                                                                                       they do not suffer certain
                                                                                                       critical wounds that rely on
                      Ruptured Spleen                   You must make a                                damaging organs. If you
  9-10   A tear in your spleen begins bleeding profuse- Stun save every 10 You take a -2 to
         ly, making you woozy. Make a Stun save every 5      Rounds.             Stun.
                                                                                                       score one of the following
               rounds. This wound induces bleeding.                                                    critical wounds against an el-
                                                                                                       ementa or specter, the strike
                         Broken Ribs                                                                   instead does bonus damage
  6-8    The blow breaks your ribs, causing immense pain You are at a -1 to You are at a -1 to
         when you bend and strain. Take a -2 to BODY and   BODY and REF.         BODY.                 as stated in the Bonus Dam-
                      a -1 to REF and DEX.                                                             age table.
                       Fractured Arm                       You take a -2 to ac- You take a -1 to ac-
  4-5    The blow fractures your arm. You take a -3 to ac- tions with that arm. tions with that arm.   Foreign Object
                        tions with that arm.                                                           Ruptured Spleen
                                                                                                       Torn Stomach
                        Fractured Leg                       You take a -2 to -1 to SPD, Dodge/
  2-3    The blow fractures your leg. You take a -3 to SPD, SPD,     Dodge/Es- Escape, and Ath-        Sucking Chest Wound
                   Dodge/Escape, and Athletics.             cape, and Athletics.     letics.           Septic Shock

                                                                                                       Specters are also immune to
                                                                                                       any strike to the legs (since
Difficult Critical Table                                                                               they have no legs), so you
                                                                                                       must roll again on location.
 Roll                        Effect                           Stabilized            Treated
                        Skull Fracture                      Take a -1 to INT                              Bonus Damage
         The blow fractures a part of your skull, weakening and DEX and quad- You take quadruple
   12    your head and causing bleeding. You take a -1 to ruple damage from damage from head
         INT and DEX, and take quadruple damage from           head wounds.        wounds.               Level         Bonus
                           head wounds.
                                                                                                         Simple          +5
                         Concussion                                                                     Complex          +10
   11    The blow caused a minor concussion. Make a Stun You take a -1 to INT, You take a-1 to INT
         save every 1d6 rounds and take a -2 to INT, REF,  REF, and DEX.            and DEX              Difficult       +15
                            and DEX.
                                                                                                         Deadly          +20
                        Torn Stomach
  9-10   The blow rips your stomach, pouring its contents You take a -2 to all You take a -1 to all
         into your gut. You take a -2 to all actions and take 4 actions.             actions.
                  points of acid damage per round.

                  Sucking Chest Wound
  6-8    The wound tears your lung, which fills your chest You take a -2 to You take a -1 to
         with air, crushing organs. You take a -3 to BODY   BODY and SPD.    BODY and SPD.
                 and SPD. You also start suffocating.
```

<a id="page-160"></a>

### Страница 160

```text
    160

                                                   Compound Arm Fracture                                                 That arm must
      Prosthetics                    4-5    The blow crushes your arm. Bone sticks out of the   That arm is useless.   remain in a sling,
                                            skin. The arm is rendered useless and you start                            but it can hold
You can buy prosthetics to                                     bleeding.                                                     things.
replace arms or legs that you
lose in combat. They allow                          Compound Leg Fracture                        Halves SPD, Dodge/ -2 to SPD, Dodge/
                                     2-3    The blow snaps your leg, rendering it useless. Quar- Escape, and Athlet-    Escape, and
you to use that limb again                  ter SPD, Dodge/Escape, and Athletics. This induces           ics.            Athletics.
and alleviate the penalties                                     bleeding.
somewhat.
           Basic arm pros-
thetics allow you to use your      Deadly Critical Table
arm for basic tasks that don’t
require fine manipulation           Roll                        Effect                           Stabilized               Treated
(opening doors or grabbing
people) but you cannot                           Separated Spine/Decapitated                    This wound cannot This wound cannot
                                     12     The blow either snaps your neck or separates your      be stabilized.     be treated.
wield a weapon with them.                    head from your shoulders. You die immediately.
Basic leg prosthetics allow
you to move at 3/4th your                                    Damaged Eye                         You take a -3 to Permanent -1 to
                                     11     The blow cuts into or indents your eyeball. You take sight-based Aware- sight-based Aware-
normal SPD but you still                    a -5 to sight-based Awareness and -4 to DEX. This ness and -2 to DEX       ness and DEX.
take a -5 to Dodge/Escape                                 wound begins bleeding.
and Athletics.
                                                          Heart Damage
           Quality arm pros-                The blow damages your heart. Make an immediate You halve your You take +2 dam-
thetics allow you to use             9-10   Death save. If you survive, the wound is bleeding Stamina, SPD, and age from bleeding
your arm for basic tasks that               and you must quarter your Stamina, SPD, and             BODY.          permanently.
                                                                 BODY.
don’t require fine manipula-
tion and allow you to wield                                  Septic Shock                       Your Stamina is You take a -5 to
weapons at a -5. Quality             6-8    The blow damages your intestines, letting waste en- halved and you take Stamina     perma-
                                            ter your blood stream. Quarter your Stamina, take a a -1 to INT, WILL,        nently.
leg prosthetics allow you to                -3 to INT, WILL, REF, and DEX. You are poisoned.       REF, and DEX.
move at your normal SPD
and give only a -3 to Dodge/                           Dismembered Arm                                                 The arm can be re-
                                     4-5    The blow rends your arm from your body or dam-      That arm is useless.   placed with a pros-
Escape and Athletics.                       ages it beyond repair. The arm cannot be used and                                thetic.
           If they are struck in                            you start bleeding.
combat, the wearer takes no
damage but the prosthetic                                Dismembered Leg                      You quarter your The leg can be re-
                                     2-3    The blow tears your leg from your body or damages SPD,     Dodge/Es- placed with a pros-
comes off.                                  it beyond repair. Quarter your SPD, Dodge/Escape, cape, and Athletics.     thetic.
                                                 and Athletics. This wound begins bleeding.
```

<a id="page-161"></a>

### Страница 161

```text
                                                                                                                                    161

Effects
Bombs, traps, spells, and even conventional weapons can all inflict extra unpleasant effects.                       Prosthetics Note
Each effect goes on until you take the steps specified to end it.                                                 In our world, simple pros-
                                                                                                                  thetic limbs have been
Effect Table                                                                                                      around since the time of
                                                                                                                  the Egyptians. If you’re in-
       Name                                                    Effect                                             terested in the story of the
                                                                                                                  ultimate prosthetic bad-ass,
                         You are now engulfed in flames. Every turn you take 5 points of damage to every
                         body location. Armor soaks the damage, but fire does 1 point of damage to armor          check out Gotz Von Ber-
          Fire           and weapons every turn. To put out the fire you must take a turn to either pour          lichingen whose prosthetic
                                            water on yourself or stop, drop, and roll.                            hand made him a legend.
                         You are stunned, your head reeling and vision swimming. You can’t take any ac-
                         tions while stunned and anyone attacking you only has to beat DC:10 to hit you.
         Stun            To end this effect you must make a Stun save. This roll takes your whole turn. If
                                   you are struck while stunned you snap out of it immediately.
                         Poison or venom courses through your body, doing 3 points of damage every turn              Stun: The Last
        Poison           which armor does not negate. To shake off the poison you must make a DC:15
                                                                                                                    Thing You Want
                                                       Endurance check.
                         Your wound opens a vein, causing horrible bleeding. You take 2 points of damage          Being poisoned, being on
         Bleed           each turn until the bleeding is stopped. You can end the bleeding by either casting      fire, being frozen. All of these
                              a Healing spell on it or making a successful First Aid check at a DC:15.            are things you deal with
                         You’re not literally frozen in a block of ice, but your whole body is stiff and an icy   during a fight. They hinder
        Freeze           glaze has formed on your clothes. Until you break the ice you have a -3 to your          you but not so much that
                             SPD and a -1 to Reflex. You can break free with a DC:16 Physique check.
                                                                                                                  you can’t continue fighting.
                         You are thrown off balance and take a -2 to your next action. At the begining of
       Stagger                             your next round you recover your balance.                              Being stunned on the other
                                                                                                                  hand is incredibly danger-
                         You’re stumbling drunk. Your REF, DEX, and INT are at a -2 and you are at a -3
     Intoxication        for Verbal Combat. There’s a 25% chance your won’t clearly remember everything           ous. While stunned you are
                                              you did while you were intoxicated.                                 a sitting duck. Any opponent
                         You are seeing visions and images that aren’t really there. The GM has free rein         who wants to attack you is
    Hallucination        to make any false sensory experience they want appear to you. It takes a DC:15           likely going to and will often
                                         Deduction check to recognize each false image.
                                                                                                                  score critical wounds since
                         Your stomach is churning and you have to concentrate not to vomit. Every 3 rounds
        Nausea            you must roll under your BODY or spend the round vomiting or dry-heaving.
                                                                                                                  you aren’t in any shape to
                                                                                                                  dodge. Luckily, being struck
                         Your access to air has been cut off and you are choking to death. Every round you
                         take 3 damage which armor does not negate. Depending on your situation there             once (even if it doesn’t pen-
     Suffocation         are different ways to end this suffocation. Restoring your air supply (surfacing         etrate your armor) will snap
                                       from water, escaping a chokehold, etc.) ends this effect.                  you out of your stunned
       Blinded
                         Your eyes have been blocked or damaged. Until you take a turn to clear your eyes         state.
                           you are at a -3 to all Attack and Defense and a -5 to sight-based Awareness.



Susceptibility                                         Resistances
Some monsters are especially susceptible to            Some monsters are resistant or even im-
certain effects (fire, poison, etc.). Attacks the      mune to specific effects. This could be be-
target is susceptable to do double damage.             cause a magical force protects them, or due
Non-damage spells of that effect type im-              to attunement with that particular force. If a
pose a -2 to resistance rolls and double their         subject is immune to a force then that force
duration. The exception to this case is silver.        does not affect it in any way. If a subject is
All monsters are considered suceptable to              resistant to a force, it takes half damage from
silver (see Monster Resistances and Silver).           that force and get a +2 on all rolls to resist it.
```

<a id="page-162"></a>

### Страница 162

```text
    162

                               Monster Resistances and Silver                   Death Saves
  Healing Yourself             All monsters, except wolves, are resistant to    When you have been knocked below 0
You can attempt to stabilize   steel and thus take half damage from steel       Health Points you are put into Death State.
your own wounds, but it is     weapons. All such monsters are susceptible       In Death State, all your stats fall to 1/3 nor-
much harder due to Wound       to silver instead, though this susceptibility    mal and you must make a Death save at the
Threshold penalties.           manifests differently. Due to an unknown         same value as your Stun save. If you fail this
                               force, silver repels monsters and burns them.    save, you die and no amount of magic can
                               A silver weapon striking a monster does the      bring your back. If you succeed, you survive
                               extra damage noted in the weapon’s stats. A      for that round.
                               silver object that is not a weapon does an ex-             Each round you must make another
                               tra 1d6 damage. If a piece of silver becomes     Death save at a cumulative -1. On a success-
                               lodged in a monster, they take damage as if      ful roll you survive. On a failure you die. A
                               poisoned until they take an action to pull       tough player can survive for quite a while,
                               it out.                                          but eventually you’re gonna cash out. Every
                                                                                time you are injured in Death State you must
                                                                                make another Death save at a cumulative -1.

                                                                                Stabilization
                                                                                To stop someone from dying, you must sta-
                                                                                bilize them. To stabilize a character, make a
                                                                                First Aid roll at a DC equal to how far the
                                                                                character is below 0 Health Points. If you fail
                                                                                the patient continues to die, but if you suc-
                                                                                ceed they are brought back to 1 Health Point
                                                                                and leave Death State.

                                                                                Stabilizing a Critical Wound
                                                                                If you can’t get to a doctor immediately and
                                                                                your injury is killing you, you can attempt
                                                                                to stabilize the wound. Stabilizing a critical
                                                                                wound lessens its effects so you can keep
                                                                                fighting or get to a doctor in time. Stabilizing
                                                                                a wound requires one First Aid check with a
                                                                                DC based on the severity of the wound (see
                                                                                the Stabilization table). Stabilizing a wound
                                                                                doesn’t heal it. The healing clock only starts
                                                                                once someone applies Healing Hands or
                                                                                healing spells on it.

                                                                                Stabilization
                                                                                            Critical                  DC
                                                                                             Simple                    12
                                                                                            Complex                    14
                                                                                             Difficult                 16
                                                                                             Deadly                    18
```

<a id="page-163"></a>

### Страница 163

```text
                                                                                                                                          163

In Depth Combat
Melee Weapons                                                  Escape roll against your Brawling to slip loose.
Melee weapons, the most prevalent in the                   •   Pin: While grappling, you can pin your oppo-
world of the Witcher, rely on REF to hit. The                  nent. If you succeed, the opponent is immobi-
formula for melee attacks is:                                  lized and cannot move or act until they escape
                                                               with a Dodge/Escape roll against your Brawling.
           REF stat+Weapon skill                           •   Choke: After grappling a target, you can roll to
             +Modifier+1d10                                    attempt to choke them. The opponent is suffo-
                                                               cating until they are able to escape.
Brawling & Wrestling                                       •   Throw: While grappling, you can roll to throw
You may wind up in the midst of combat un-                     your opponent. The opponent is thrown to the
armed. In this case you’ll be brawling. Un-                    ground (prone), takes damage equal to your
less marked differently, these attacks each                    Punch damage, and must make a Stun save at -1.
take an action and replace fast or strong                  •   Trip: You can attempt to kick the target’s legs out
strikes. Brawling does non-lethal damage.                      from under them and knock them prone. If you
•   Punch: You can punch or strike with your fist,             succeed, the opponent falls prone.
    palm or elbow, dealing an amount of non-le-
    thal damage equal to your Punch damage. You            Special Attacks                                                   Dual Wielding
    can choose to make strong or fast strikes with         Anyone can swing a sword. Real soldiers
    punches.                                               like to throw in special strikes for best ef-                 Dual wielding allows you
•   Kick: You can kick or strike with your foot or         fect. Unless marked otherwise, each special                   to make a joint attack with
    knee, dealing an amount of non-lethal damage           attack requires 1 action, replacing a normal                  two weapons you hold at the
    equal to your Kick damage. You can choose to           attack action.                                                same time . When making a
    make strong or fast strikes with kicks.                •   Charge: By taking a full round, you can execute           joint attack, roll two attacks
•   Push Kick: Instead of doing damage, you can try            a charge against a target. A charge allows you            with a -3 to both of them.
    to push a target back with a powerful forward              to move up to your Run speed and then make                Your opponent must have
    kick. If you succeed, you push the opponent back           a strong strike. This strike still suffers a -3 to hit,   two weapons (or a weapon
    a number of meters equal to your Body/3. You               but if the attack is blocked you can make a Phy-          and a shield) if they want to
    only do half damage, and this attack always hits           sique check against the opponent’s Physique roll          block or parry both attacks.
    the torso.                                                 to knock the target prone.                                If they can’t they must dodge
•   Charge: Much like armed charges, you can move          •   Pommel Strike: By making a weapon attack, you             or reposition to escape the
    up to your Run speed and then make a strong                can non-lethally strike against a target by bash-         second attack. You can make
    punch or kick. This strike still suffers a -3 to hit       ing with the pommel of your weapon. Halve the             a joint attack with any two
    but if the attack is blocked you can make a Phy-           weapon’s damage roll and apply it as non-lethal.          weapons you can hold in
    sique check against the opponent’s Physique roll       •   Disarm: By making a weapon attack, you can                one hand, including two
    to knock the target prone.                                 attempt to knock an opponent’s weapon out of              hand crossbows.
•   Disarm: You can roll Brawling against your op-             their hand with a well-aimed strike. If you suc-
    ponent’s Dodge/Escape to attempt to disarm an              ceed, you knock the opponent’s weapon from
    opponent. Unlike disarming with a weapon, you              their hand and send it flying, 1d6 meters away in                   Prone
    can try to either knock the opponent’s weapon              a random direction (see the Scatter table).               When knocked prone you
    away (1d6/2 meters in a random direction) or to        •   Trip: By making a weapon attack, you can at-              take a -2 to your attack and
    grab the weapon with a free hand. Trying to take           tempt to strike the target’s legs and knock them          defense rolls until you take a
    the weapon imposes a -3 penalty.                           prone. If you succeed, the opponent is falls flat.        move action to stand up.
•   Grapple: You can roll to grab hold of a target.        •   Feint: By rolling Deceit instead of your first fast
    While grappled, a target cannot move away from             strike, you can attempt a feint. If your opponent
    you and takes to -2 to all physical actions. This          fails an Awareness check against your Deceit roll,
    is a prerequisite to pins, chokes, and throws.             you confuse them and can make your second at-
    Each turn, your opponent can attempt a Dodge/              tack at a +3.
```

<a id="page-164"></a>

### Страница 164

```text
   164

                         Shield Attacks                                             Ranged Weapons
  Size Modifiers         You can use a shield in combat as a bludg-                 Anything shot or thrown counts as a ranged
                         eoning weapon. Using your shield as a                      weapon. To make a ranged attack (Bows,
                         weapon requires a Melee attack roll and                    Crossbows, Thrown Weapons) you must
    Size           Mod   does damage equal to your Punch, but le-                   roll a combination of:
     Small               thal. Medium shields do damage as though
                    +2
(Cat or nekker)          your Punch were two levels higher, and                               DEX stat+Weapon skill
   Medium                heavy shields do damage four levels higher.                          +RNG Modifier+1d10
                    +0   See the Hand to Hand table on pg.48.
 (Man-sized)
     Large                                                                          ...equal or greater than the defensive roll of
(Troll or horse)
                    -2   Defenses                                                   your target. If you’re attacking an unaware
                         When defending against attacks there are                   or inanimate target, you must beat its target
     Huge                many options for getting clear of or stopping              DC, augmented by its size (See Size Modi-
                    -4
    (Fiend)              a killing blow. Unless marked otherwise, all               fiers).
                         of these defenses work against ranged as
                         well as melee attacks.                                     Ranges & Target DC
                         •   Dodge: By moving slightly out of the way, you
                             can dodge an incoming attack. Dodging requires                                       Target
                             a Dodge/Escape roll against your opponent’s at-                Ranges                       Mod
                             tack roll.
                                                                                                                   DC
                         •   Reposition: By ducking or rolling out the                     Point Blank
                             way, you can not only dodge an attack but also          The weapon is very close
                                                                                                                   10      +5
                             maneuver to escape being surrounded. If you             or physically touching the
                             succeed in an Athletics roll versus your oppo-                     target.
                             nent’s attack roll, you avoid the attack and can                   Close
                             move a distance equal to half your SPD in any           ¼ the listed range of the     15      +0
                             direction that is not blocked.                                   weapon
                         •   Block: You can choose to attempt to block an in-                 Medium
                             coming attack with your weapon, shield, or even         ½ the listed range of the     20       -2
                             yourself. Only a shield can block ranged attacks.                weapon
                             Roll your weapon skill to negate an attack with                    Long
                             your weapon. Roll Melee to negate an attack             The listed range of the       25       -4
                             with a shield. Whichever you parry with takes 1                  weapon
                             point of damage. If you are in a seriously tight fix
                                                                                              Extreme
                             or protecting someone else, you can attempt to
                                                                                     2x the listed range of the    30       -6
                             block an attack with your arm or hand by using
                                                                                              weapon
                             Brawling. If you succeed, you immediately take
                             the attack’s damage to that location. Armor is ap-
                             plied, so you may not take damage if your armor
                             is high enough.                                        Crossbows & Loading
                         •   Parry: You can parry an attack at a -3 to your         Crossbows are wonders of mechanical
                             weapon/Melee/Brawling roll. If you succeed, you        workmanship that allow weak people to fire
                             knock the opponent’s weapon aside and not only         bolts with the same strength as trained bow-
                             negate the attack but do so without damaging           men. However they require more time to
                             your weapon. Your opponent is also staggered.          load than a bow due to their loading mecha-
                             You cannot parry bow or crossbow attacks, but          nisms. This extra time means that loading a
                             can parry thrown weapons at a -5.                      crossbow takes 1 action.
```

<a id="page-165"></a>

### Страница 165

```text
                                                                                                                       165

Bombs & Traps                                        Snow & Ice
Bombs and traps work slightly different-             Snow and ice are a benefit and a hindrance.       Repositioning in
ly from other ranged attacks. Bombs can              When tracking in snow you gain a +3 to                Water
be thrown at a single opponent, but their            Wilderness Survival to follow recent tracks,
damage affects an area. Everyone in that             but a -3 to follow old tracks. When fighting    When repositioning under-
area takes the bomb’s damage to every part           on snow and ice you must make a DC:14           water, you can move in three
of their body and feels the bomb’s effects.          Athletics check after running or attacking      dimensions but are only able
If you fail your Athletics check, the bomb           to stay standing. If naked or lightly clothed   to move half your LEAP.
lands off target (see the Scatter table).            in icy conditions, you can survive without
         Traps are placed in an area. When a         shelter for a number of hours equal to your
person enters that area they trigger the trap,       Stun. After that time has elapsed you enter
and they (and anyone in the trap’s radius)           Death State.                                       Environmental
feel the trap’s effect and take the trap’s dam-
age to every part of their body.                     Extreme Heat                                         Awareness
                                                     Traveling and fighting in extreme heat is       Most of my students assume
Environmental Effects                                incredibly difficult even for trained warri-    that strength and speed are
The environment can and will affect the way          ors. When traveling through a desert envi-      the key elements in combat.
you travel and fight, and in some cases the          ronment such as the Korath desert, charac-      But in my personal study of
weapons you choose to use. Light and dark-           ters lower their STA by a third. If they are    the subject I believe that en-
ness, weather, water, and terrain all change         wearing medium or heavy armor, they halve       vironmental awareness is the
the course of battle in their own ways.              their STA.                                      key. Can you cause a careless
                                                                                                     opponent to trip over door
Lighting                                             Swampy or Overgrown                             sills or tree roots? Can you
Light affects your aim and situational aware-        Environments                                    maneuver them into a crowd
ness.                                                When traveling and fighting in swamps           of self-important little old
                                                     or brush, you have to keep an eye on the        ladies, or perhaps an armed
Light Level Table                                    ground around you. You take a -2 to Dodge/      opponent bigger than either
                                                     Escape and Athletics.                           of you? Is there anything in
                                                                                                     your environment that can be
  Light Level                  Effect
                                                     Fighting in Water                               used as a weapon? A drunk-
 Glaring Light -3 to Awareness and -3 to At-         Fighting underwater is possible, but defi-      en belligerent can often be set
 (Desert sun or                                                                                      on fire with a candle or hearth
                    tack and Defense if facing the   nitely much more difficult. When fighting
 sun reflecting off
      snow)
                                sun.                 with melee weapons underwater, the ROF of       ash. Can you climb trees and
                                                     all weapons falls to 1, and attacking, block-   perhaps drop on your assail-
    Daylight                No penalties                                                             ant or cause him to slip as
    (Daylight)                                       ing, and parrying are at an additional -2.
                                                     While underwater, use Athletics to dodge        you carefully cross streams or
   Dim Light               -2 to Awareness                                                           rivers? It is true, my students,
   (Moonlight)                                       and reposition. Thrown weapons (with the
                                                     exception of spears) will not function un-      that most of you do not have
   Darkness                                                                                          overwhelming strength or
   (New moon        -4 to Awareness and -2 to At-    derwater, and both crossbows and bows
  night or a deep          tack and Defense          have their ranges quartered and their dam-      martial training, but you
     cavern)                                         age halved. They also suffer the -2 penalty     may use your sharp wits even
                                                     to attack.                                      more effectively.
                                                                                                             –Brandon of Oxenfurt
```

<a id="page-169"></a>

### Страница 169

```text
                                                                                                                                   169

Transportation & Cavalry
                                                                                                                  Bareback Penalty
Control Rolls                                            Control Modifier                                        When riding bareback
When riding animals or driving vehicles                                                                          (without a saddle of any
you have to concern yourself with keeping                  Mount/Vehicle                 Control Mod.            form) you are at a -2 to all
control. Whenever you attempt a maneu-                                                                           Control checks.
ver, you must make a Control check to keep                         Horse                         +2
your transportation under control:                               War horse                        -2
                                                                    Mule                          -0
             REF stat+Ride skill                                     Ox                           -2
            +Control Mod.+1d10
                                                                  Sailboat                        -1              Redanian Cavalry
This Control check must beat a DC appro-                         Sailing ship                     -1             The Redanian cavalry are
priate to whatever maneuver you are trying                         Cutter                         -0             our finest army units. They
to accomplish.                                                      Cart                          -0             are trained rigorously. But this
•   Simple (15): Swerve a vehicle or jump a low ob-               Carriage                        -1
                                                                                                                 is not the only reason cavalry,
    stacle on a horse.                                                                                           any cavalry of semi-com-
•   Difficult (20): Control a skidding vehicle or                                                                petent riders, is dangerous.
    make an abrupt stop.                                 Vehicle Control Loss                                    What is the most dangerous
•   Very Difficult (25): Jump a vehicle or leap a high                                                           weapon in an army? The
    obstacle on a horse.                                                                                         sword? The halberd? The tre-
                                                          Roll                        Result                     buchet? Give me a horse any
                                                           1-2             Skid or Slew: No other results.       day. Your horse can kill your
Control Modifiers                                                     Major Skid: Slide 1d10x2 meters side-      opponents simply by stepping
Each mode of transportation has its own                              ways in the direction of travel. If you     on them and running into
                                                           3-4       hit an object, use the Charging rules to    them, even in plate mail. One
control modifier. Add the value from the                             see what damage is done to your vehi-
control modifier table to your Control rolls.                                   cle and the object.              can use a horse and a weap-
                                                                                                                 on. Mounted on a horse you
                                                                     Rolled the Vehicle: Your vehicle skids
                                                                     1d10x3 meters sideways in the direc-        are elevated and a moving
Control Loss                                                         tion of travel and rolls. In a land vehi-   target. Horses can make a
If you fail a Control check, you risk losing                         cle, you, the vehicle, and the animals      hasty retreat. Well-trained
                                                           5-6       pulling it take 5d6 damage. In a wa-        riders can hang from one side
control completely and having horrible                               ter vehicle, you have capsized and are
things happen to you and your mount/ve-                              trapped underwater until you make a         of their saddle using their en-
hicle. If you are driving a vehicle, use the                         DC:12 Swimming check to swim out            tire horse as cover. The rum-
Vehicle Control Loss table. If you are on a                                           and up.                    bling and shaking of a line of
mount, something happens to both you and                                                                         well-trained cavalry has been
the mount. Roll twice on the Mounted Con-                                                                        known to seriously dishearten
trol Loss table, once for the riders and once                                                                    infantry. A well-barded horse
for the mount, to see what happens.                                                                              is nearly unstoppable.
                                                                                                                         –Brandon of Oxenfurt
```

<a id="page-170"></a>

### Страница 170

```text
    170

                                 Mounted Control Loss
 Getting Out From
  Under A Horse                   Roll              Personal Results                                       Mount Results
If your mount falls on top of            Tack Dropped: The reins slip out of your hands. Refusal: Your mount simply doesn’t to do what
you, you have two options:         1-3   You are now at a -1 to Control checks until you you want it to do. You must make another Con-
                                            grab them again, which requires a turn.                   trol check next round.
let it come to and get off you
naturally or try to get out                                                           Spooked: Your mount startles and rears. You
from under it. If someone                Bucked: Your mount bucks. Make a DC:15 must make an Athletics check (DC:16) to stay
                                   4     Athletics check. You must succeed to stay in on its back and an Animal Handling check
can make a Physique check                                  the saddle.                (DC:18) to calm it down before you can keep
with a DC of 25, they can lift                                                                           riding.
the horse off of you.
                                         Bucked: Your mount bucks. Make a DC:18 Stumble: Your mount stumbles and must make
                                   5     Athletics check. You must succeed to stay in      a DC:14 Athletics check to stay standing.
                                         the saddle. If you fall you are considered prone.

                                         Bucked: Your mount bucks. Make a DC:20 Stumble: Your mount stumbles and must make
                                   6     Athletics check. You must succeed to stay in      a DC:18 Athletics check to stay standing.
                                         the saddle. If you fall you are considered prone.

                                                                                           Trip: Your mount trips and must make a DC:15
                                         Bucked: Your mount bucks. Make a DC:25 Athletics check or fall and take 1d10 points of
                                   7     Athletics check. You must succeed to stay in damage to one randomly rolled leg. Roll 1d10.
                                         the saddle. If you fall you are considered prone. 1-3: Front Left, 4-6: Front Right, 7-8: Back Left,
                                                                                                           9-10: Back Right.

                                         Thrown: You have been thrown from your
                                         mount. Roll 1d6/2 to see how many meters you
                                         fly. If you land without hitting anything, roll lo-   Trip: Your mount trips and must make a DC:20
                                         cation and take 1d6 damage to that location. If       Athletics check or fall and take 2d10 points of
                                   8     you hit something along the way, roll location        damage to one randomly rolled leg. Roll 1d10.
                                         and then take a number of d6 damage equal to          1-3: Front Left, 4-6: Front Right, 7-8: Back Left,
                                         the number of meters you would have flown.                            9-10: Back Right.
                                         If you hit a living thing, it takes this damage
                                                               as well.

                                         Thrown: You have been thrown from your                Fall: Your mount falls over. If you are on it or
                                         mount. Roll 1d6 to see how many meters you            within a meter of it, make a DC:18 Athletics
                                         fly. If you land without hitting anything, roll lo-   check to avoid being landed on. If you fail, your
                                         cation and take 1d6 damage to that location. If       mount falls on you. Roll a random location to
                                   9     you hit something along the way, roll location        see what part of you falls under the horse, then
                                         and then take a number of d6 damage equal to          take 2d10 damage to that location. Your horse
                                         the number of meters you would have flown.            takes this as torso damage. After this you are
                                         If you hit a living thing, it takes this damage       trapped under your mount. You can attempt a
                                                               as well.                        Control check the next turn to get it off of you.

                                         Thrown: You have been thrown from your                Faint: Your mount faints from the sheer stress
                                         mount. Roll 1d10 to see how many meters you           of the situation. If you are on it or within a me-
                                         fly. If you land without hitting anything, roll lo-   ter of it, make a DC:18 Athletics check to avoid
                                         cation and take 1d6 damage to that location. If       being landed on. If you fail, your mount falls on
                                   10    you hit something along the way, roll location        you. Roll a random location to see what part of
                                         and then take a number of d6 damage equal to          you falls under the horse and take 2d10 damage
                                         the number of meters you would have flown.            to that location. Your horse takes this as torso
                                         If you hit a living thing, it takes this damage       damage. After this you are trapped under your
                                                               as well.                        mount. Your mount must make a Stun save
                                                                                                            each round to come to.
```

<a id="page-173"></a>

### Страница 173

```text
                                                         173

Healing
Healing Over Time
Characters begin healing Health Points nat-
urally over time if someone makes either a
Healing Hands or a First Aid roll for them.
They regain a number of HP equal to their
REC stat per day of rest. While resting, you
must not do anything too strenuous. If you
spend a lot of time running around, doing
work, or fighting, you only heal half of your
Recovery per day. If healed with a Healing
Hands check you gain an extra 3 HP per day.
Critical wounds heal differently.

Healing with Magic
If you are traveling with (or can find) a mage
or priest, they can heal you with magic.
Magical healing is uncommon: most magic
users are incapable of performing it. If you
are a witcher, or mildly suicidal, you could
take a witcher’s potion. For witchers this is
perfectly safe. For non-witchers it can be
like drinking poison.
•   Spells & Rituals: A mage can cast a magical heal-
    ing spell on a target to regenerate their Health
    Points over time. A Ritual of Life restores health
    immediately on casting.
•   Potions: Witchers and non-witchers can
    drink a swallow potion to gain health back, but
    non-witchers must make a DC:18 Endurance
    check or be poisoned.

Healing Critical Wounds
Critical wounds require time and medi-
cal attention. A doctor can heal a critical
wound using their Healing Hands ability
(see the Healing Hands table), while a mage
can use a Healing spell a number of times to
heal a critical wound (see the Healing Spell
table). The mage must dedicate the spell not
to regenerating Health Points but to healing
the wound.
```

<a id="page-174"></a>

### Страница 174

```text
     174




    Training with                  Healing Hands                 After a critical wound has been treated by
     Prostheses                                                  a doctor or a mage it must heal over time.
Some deadly critical                                             Check your BODY stat and wound level on
                                        Critical    Turns   DC   the Critical Healing table to see how many
wounds have lasting ef-
fects that can be alleviated             Simple       2     12   days you’ll need to get rid of the Treated
by a prosthesis. However,               Complex       4     14   penalty.
the penalties can only be               Difficult     6     16
brought down so far. You                                         Critical Healing
                                         Deadly       8     18
can buy down these penal-
ties further by applying im-                                      Body Simple Complex Difficult Deadly
provement points to them.          Healing Spell
                                                                    3       5        9       12      15
10 improvement points
                                                                    4       4        8       11      14
subtracts 1 from the penalty.           Critical    Uses    DC
You cannot buy down pen-                                            5       3        7       10      13
alties past -2 and you cannot            Simple       4     14
                                                                    6       2        6        9      12
buy down penalties to use               Complex       6     16
                                                                    7       1        5        8      11
a limb that you don’t have a            Difficult     8     18
prosthesis for. It is impossible                                    8       1        4        7      10
                                         Deadly      10     20
to train a prosthetic to feel.                                      9       1        3        6       9
                                                                    10      1        2        5       8
                                                                    11      1        1        4       7
                                                                    12      1        1        3       6
                                                                    13      1        1        2       5
```

<a id="page-230"></a>

### Страница 230

```text
    230


    Lycanthropes
If you want, you can let your
                                Curses
player play themselves while
they are in werewolf form.
                                Curses Are A Plot Device                                   Making Curses
                                There are very few known and written hex-                  When making a curse, just use your im-
As long as they can adhere to
                                es like the Nightmare, the Devil’s Luck, or                agination. Curses can do everything from
the understanding that they
                                the Hex of Shadows. Curses, on the other                   transmuting people to animating entire
are not in their right mind,
                                hand, whether in the Witcher books or vid-                 mansions. If you need some ideas or a pre-
it does allow the player to
                                eo games, are plot devices. You should gen-                made curse, check out the tables below. Re-
most accurately act on their
                                erally only use curses in the TRPG either to               member though: a curse should never be
character’s worst impuls-
                                drive the plot or to get hooks into your play-             random. Curses are poetic justice that pun-
es. But they must be able to
                                ers. Curses are too powerful to just throw                 ish transgressions in a fitting way. The Curse
keep their vicious nature in
                                out randomly.                                              Building section give you more information
mind. Being a lycanthrope is
                                                                                           about making your own curses.
a curse, not a benefit.


                                Known Curses
                                The Monstrous Curse                                        The Curse of the Wanderer
                                Effect: The Monstrous Curse makes a subject appear         Effect: The Curse of the Wanderer is one of the most
                                monstrous to all who see them. While they remain           vicious curses. Though it doesn’t hurt the subject, it
                                humanoid, their facial features take on aspects of a       strips away even the most loyal friend, relative, or
                                random animal. Roll 1d10; 1-2: Bear, 3-4: Boar, 5-6:       companion. Slowly the people around the subject
                                Bird, 7-8: Snake, 9-10: Insect. The curse-bearer’s         are pushed away by misunderstandings, arguments,
                                social standing is now Hated & Feared, no matter           natural interventions, or even kidnappings until (if
                                what it was. The cursed is not actually a monster and      they stay around for more than a month) fate starts
                                doesn’t take damage from silver, but appears mon-          conspiring to kill them.
                                strous and will be mistaken for a monster by anyone        Intensity: High
                                who fails a DC:18 Education roll.
                                Intensity: Medium                                          Lycanthropy
                                                                                           Effect: A character afflicted with Lycanthropy has a 30%
                                The Haunting                                               chance of changing into their werewolf form every night,
                                Effect: The Haunting can only curse an area. It            when the moon rises. When a character changes, they
                                summons the spirits of every person wronged in             become a vicious predator with a human’s cunning and an
                                the area as wraiths. When you cast this curse, roll        urge to kill. If the character is a player character, they are
                                5d6 to see how many wraiths manifest. If the area is       taken over by the GM until the sun rises. When in their
                                particularly horrible, roll an extra 2d6. If the area is   werewolf form the character acts on all their worst impuls-
                                relatively tame, just roll 2d6. These wraiths remain in    es with no mercy and kills anyone in their way. While in
                                the area until killed and return the next night. They      their beast state the lycanthrope has all of the werewolf’s
                                will attack anything that enters the cursed area. The      weapons, armor, and abilities. The character also adds a
                                only way to get rid of this curse is to somehow right      bonus to 4 of their statistics except as noted below.
                                the wrongs done in the area.                               Intensity: High
                                Intensity: Medium

                                The Curse of Pestilence                                    Werewolf Bonuses
                                Effect: The Curse of Pestilence makes the subject a
                                carrier for a dangerous disease. While they are un-                 Reflex+2                        Body+3
                                affected by the disease, they spread it to anyone who
                                touches them and fails a DC:18 Endurance check. If                  Speed+4                       Empathy-5
                                they stay in a building for more than 3 days, every-
                                one in the building must make a DC:16 Endurance
                                check. If they stay in a town for more than a week,
                                everyone in that town must make a DC:14 Endur-
                                ance check.
                                Intensity: High
```

<a id="page-231"></a>

### Страница 231

```text
                                                                                                                               231

Curse Building
Building a curse is an art. No
                                       Violence               Betrayal                  Inaction                  Lifting Curses
effect in a curse should be ran-
dom; you should be able to
                                   Animals are uneasy The cursed is always People are unwilling               Curses are punishments,
                                    around the cursed. left alone at night. to help the cursed.               so they’re hard to get rid of.
trace everything back to the
reason the curse was cast.         Blood pours from the The cursed has vivid
                                                                             Those the cursed                 There are few curses that you
                                                                             failed to help appear            can lift without some pain
          If you need help mak-    cursed’s eyes at night. night terrors.
                                                                               as hallucinations.
ing a good curse, here are a                                                                                  on somebody’s end. Once
                                                                          The cursed’s body
few suggestions on what you        Wraiths chase the The cursed loses the                                     again, the steps to break a
                                                                          becomes sick and
                                    cursed every night. ability to love.                                      curse should be related to
could bring to bear for cer-                                                   twisted.
tain actions or inactions. De-     The cursed is com- The cursed sees the Food the cursed eats
                                                                                                              the cause of the curse. You
pending on the severity of the     pelled to kill anyone person they betrayed turns to ash, but they          can use the Penance table to
curse, you can also stack a
                                   who comes too near.     in every mirror.        can’t starve.              get a concept for what level
number of curse effects on top     The cursed feels like Everyone the cursed The cursed is struck             of penance need be paid.
                                   they are being vivi- loves turns against with paralysis at cru-
of each other. A curse should        sected in the night.       them.           cial moments.
never feel too unfair, though.
                                   The cursed becomes
There should be some hope.                             The tools and weap- Anywhere the cursed
                                   hideously ugly to
                                                       ons of the cursed al- stays begins decaying
                                   match their person-
                                           ality.
                                                           ways break.          and falling apart.                Cursed Places
                                                                                                              For cursed places, penance
                                                                                                              should be a bit different. If
Penance & Suffering                                                                                           the curse is tied to a person,
No two curses are lifted the                                                                                  the Penance table is fine. But
                                    Intensity                 Penance & Suffering
same way. Three people afflict-                                                                               if the curse is specifically on
                                                   Low intensity curses are small time and don’t threat-
ed with lycanthropy may find                                                                                  the place then the penance
                                                   en the life of the cursed. Lifting these curses require
three entirely separate ways to                    smaller things such as: the forgiveness of the person      usually means ending the
                                         Low                                                                  suffering of spirits around
lift their curses. When some-                      who cursed them, giving away all of their money,
one gets cursed in your game,                      or burning their most prized possession under the          the cursed place, or perhaps
                                                                          full moon.                          returning something to the
take a moment to figure out
how they’re gonna undo the                         Medium intensity curses are dangerous and power-           place.
                                                   ful webs of magic that threaten the cursed’s life. Lift-
curse. You don’t have to tell          Medium      ing these curses requires real suffering. The cursed
them but you should know,                          must: renounce a loved one, nearly die, or spend
just in case they stumble upon                                 years in isolation and misery.
it. Based on the severity of a                     High intensity curses are tremendously dangerous
curse, here are a few sugges-                      and, luckily, very rare. These curses require in-
tions for how curses can end.           High       tense suffering. To lift these curses the cursed must:
                                                   sacrifice a beloved companion, or lose literally
                                                                         everything.
```

<a id="page-238"></a>

### Страница 238

```text
     238


    The Schools of
      Witchers
                                     Witcher Lifepath
                                     The life of a witcher is vastly different from        witchers are harsh and unforgiving. Even
In the heyday of witchers            that of any other creature on the Conti-              after this, a witcher can expect decades (if
there were many many sep-            nent. From an early age a witcher stops               not centuries) of traveling the roads of the
erate schools, which all mu-         being a normal citizen and begins a life              Continent alone, putting themselves in
tated new witchers and taught        that most other people could only dream               danger every day for measly pay and less
them the neccesary skills to         up in their wildest nightmares. A prospec-            respect than the local rat-catcher. A witch-
hunt monsters and lift curs-         tive witcher’s training is rigorous, and the          er never leads an ordinary life.
es. While it’s generally agreed      trials to join the ranks of the fully-fledged
that there is a core set of skills
required to a be a witcher,
each school taught its stu-
dents differently and focused        When Did You Become A Witcher?
on different aspects of witch-
er training. Thus, witchers            Roll    Age
from different schools often                   Infancy (-2 to the Trial of the Grasses)
                                               You were taken to become a witcher when you were a toddler, between 1 and 2 years old. You have
act differently and go about            1-2
                                               no memories of life before becoming a witcher and had nothing to cling to when taking the Trial
their jobs in similar but varied               of the Grasses.
ways.                                          Early Childhood (No Modifiers)
                                        3-8    You were taken to become a witcher when you were young, between 4 and 6 years old. You had
                                               some normal memories to aid you when taking the Trial of the Grasses.
                                               Late Childhood (+2 to the Trial of the Grasses)
  Memories Of The                      9-10
                                               You were taken to become a witcher when you were relatively old, between 8 and 11 years old.
                                               While training was somewhat harder, your many memories bolstered you when you took the Trial
      Past                                     of the Grasses.
Witcher I knew couldn’t real-
ly remember much ‘bout his
past. Heh, too young to really
form a lotta memories when           What School Did You Train In?
they took him to Kaer Y Seren.
Told me that the memory he             Roll    School
did have made the mutations                    The Wolf School (No Penalty For Strong Strikes)
                                               You trained at Kaer Morhen in the heights of the Blue Mountains. Your training was tough and
easier. Poor bastard clung to a         1-2
                                               structured, focusing on a very rounded approach to the Witcher profession. You were taught to
memory of his pa takin’ him on                 strike hard and fast to end hunts quickly.
a horse for a ride in the fields.              The Gryphon School (+2 Vigor Threshold)
Don’t know why he chose that                   You were trained at Kaer Y Seren along the coastal side of the Dragon Mountains. Your training
                                        3-4
one. Probably the only normal                  was heavily focused on fighting any number of opponents and using your limited magical power
memory he had.                                 to its greatest potential.
              –Rodolf Kazmer                   The Cat School (Immune to Charm Attempts)
                                               You trained in the Dyn Marw Caravan, a traveling troop of witchers who sold their skills to anyone
                                        5-6
                                               who could pay, for any job. Their mutations and training flayed your emotions, and you struggle
                                               against violent, cruel impulses.
                                               The Viper School (No Penalties for Dual Wielding)
                                        7-8    You trained at Gorthwr Gwaed in the deep chasms of the Tir Tochair Mountains. Unlike other
                                               witchers, you were trained on twin blades and an assassination-based approach to killing monsters.
                                               The Bear School (-2 to Overall Armor Penalty)
                                       9-10    You trained in the snowy heights of the Amell Mountains at Haern Cadwch. You conditioned your
                                               body to endure all manner of punishment and move quickly and efficiently in heavy steel armor.
```

<a id="page-239"></a>

### Страница 239

```text
                                                                                                                                 239

How Did Early Training Go?
 Roll   Early Training Event                                                                                  The Gauntlet & The
        Wounded on the Gauntlet (-1 SPD)                                                                          Pendulum
  1     You were wounded while running the gauntlet around your School. Your leg was broken badly,            Speed, agility, and physical
        and even after healing it is still slightly stiff.
                                                                                                              endurance are widely con-
        Stolen Knowledge (+1 Witcher Diagram)
  2     While training at your School you snuck into the libraries of the keep and copied one of the secret
                                                                                                              sidered the most important
        witcher diagrams, smuggling the information out with you.                                             physical skills for a Witcher.
        Made a Rival (Make 1 Witcher Enemy)                                                                   To train all three at once, most
  3     While training at the keep you formed a rivalry with another witcher in training. Even after mu-      witcher schools employ two
        tations, their hatred of you continues to boil.                                                       testing courses: a hanging,
        Easy Mutations (+2 to the Trial of the Grasses)                                                       metal-studded log called the
  4     You adapted well to the lesser mutations and mutagenic mushrooms you were fed early in train-         pendulum (which must be si-
        ing. When the time came for the Trial of the Grasses, you were well prepared.                         multaneously dodged and at-
        Magical Backfire (-1 Vigor Threshold)                                                                 tacked while it’s swinging) and
  5     A failure casting a sign caused minor damage to your body. It was horrifically painful, and even
                                                                                                              the gauntlet, a long, winding
        after your body healed your Vigor Threshold was lowered.
                                                                                                              path (littered with traps, pits,
        Top of Your Class (+1 Swordsmanship)
  6     You were one of the best swordsmen in your class and your skills haven’t dulled. You perform the
                                                                                                              and snares) that trainees must
        complex movements, pirouettes, and spins of the witcher with ease.                                    run nearly every day. Many
        Bad Reaction to Mutagens (-2 to the Trial of the Grasses)                                             students die on these physical
  7     You had allergic reactions to the mutagenic mushrooms and chemical compounds given to you in          challenges before even reach-
        early training. When the Trial of the Grasses came, it was more difficult.                            ing the mutations.
        Made a Friend (Make a Witcher Friend)
  8     You made a fast friend in your early years of witcher training. The rough training and dangerous
        situations sealed your bond.
        Wounded by the Pendulum (-1 REF)                                                                        The Trials Of The
  9     You were wounded while training on the pendulum. You fell from the posts and broke several
        bones on the rocks below. While healed, you are a little stiffer than before.                              Witchers
        Extensive Research (+1 Witcher Training)                                                              When a trainee’s body has
  10    While sword training was important, you spent most of your free time in the libraries of the keep     been prepared (with grueling
        studying the monsters of the world and taking notes.                                                  phyiscal training and sub-
                                                                                                              tly mutagenic mushroom
                                                                                                              broths) they undertake the
                                                                                                              excruciating trials of a witcher.
                                                                                                              The first trial (the Trial of the
How Did Your Trials Go?                                                                                       Grasses) is designed to break
                                                                                                              down the trainee’s body and
 Roll   Outcome of the Trials                                                                                 rebuild it with superior reflex-
        Nearly Fatal (Additional -1 EMP & -1 BODY)                                                            es and cat-like eyes. The sec-
   1    The Trial of the Grasses nearly destroyed your body. Though you survived the process, your body       ond trial (the Trial of Dreams)
        and mind were damaged permanently.                                                                    gives the trainee night vision
        Poorly Accepted (Additional-1 EMP)                                                                    among other benefits, but also
  2-3   The Trial of the Grasses went poorly and the witchers in charge of mutation weren’t entirely sure     sterilizes them. The last trial
        you would make it. You survived, but not without mental scars.
                                                                                                              (the Trial of the Mountains)
        Passable Mutations (No Modifiers)                                                                     was more of an exam, intend-
  4-9   The Trial of the Grasses went well. You passed into the ranks of witchers with nothing more than
        memories of horrible pain.                                                                            ed to verify whether the train-
                                                                                                              ee remembered anything
        Extra Mutations (Additional +1 EMP & +1 DEX)
  10    Your body was very receptive to the Trial of the Grasses and you had extra mutations applied to       from the previous Trials.
        you. Your body handled it well, and all of the pain paid off in the end.
```

<a id="page-240"></a>

### Страница 240

```text
    240

                                  What Was Your Most Important Event
Your Surprise Child                Roll   Most Important Event
If you want, you can dig far-             Given a Child by the Law of Surprises
ther into the events after you      1     Along your travels you invoked the Law of Surprises and received a child. They may have been a boy, in
got your suprise child.                   which case they were made into a witcher, or a girl, in which case their fate was up to you.
          For boys, roll 1d10.            Hunted by a Sentient Monster
On anything but a 1-3, they         2     The tables turned during one of your hunts. Sentient monsters like grave hags and katakan can be dangerous
                                          quarry, and you wound up becoming the hunted for a stressful night.
died during the trials. If they
survived, you can even roll               Fought Alongside a Knight
                                    3     You did battle alongside a noble knight. This may have been against both of your wishes or even an accident,
a few times on the Witcher                but fighting beside a noble changed your outlook on knights and your job as a witcher.
Lifepath tables to see how                Captured by a Mage for Testing
they turned out.                    4     Mages lust after the secrets of Witcher mutations. At some point in your life, you were captured by a mage
          For girls, they could           who experimented on you in an attempt to reverse-engineer them.
have stayed at your keep to               Worked for a Nobleman
tend to chores, but it’s more       5     For a time you worked for a nobleman. The pay was good, but it was strange and aggravating to have to hide
likely that you had to give               most of your actions to avoid shaming the family by bringing their secrets to light.
them to the next family you               Went Beyond the Boundaries
found. Witchers don’t usually       6     Once, you traveled beyond the borders of the Continent—past the Dragon Mountains, the Tir Tochair or
                                          Blue Mountains, or the Great Sea. You have seen far lands unknown to most others.
make good parents.
                                          Meaningful Romance
                                    7     Most witchers remain neutral and avoid meaningful relationships. However, this didn’t stop you. You fell in
                                          love and actually considered settling down. It still occurs to you sometimes.
                                          Fought for your Keep
                                    8     You fought at a siege of your keep. You were outnumbered and overpowered, but you stayed nonetheless. You
                                          survived the siege with serious wounds, but saw your brethren dying around you.
                                          Gained Infamy
                                    9     After helping a city with a monster, the people became afraid and turned on you. They might have even tried
                                          to kill you. Either way, you’ve seen what kind of reward you can expect from people.
                                          Gained Fame
                                    10    You were well-received in a town after helping them with a monster. You didn’t expect free drinks or women
                                          casting you glances, but that’s what you got. You haven’t seen such kindness again, but it was heartening.



                                  Where Are You Now?
                                   Roll   Where You Are Now
                                          Became a Personal Witcher
                                    1     You signed on to work for a merchant group, noble house, or important person as a personal
                                          witcher. You work for modest pay and hunt what they tell you to hunt. Mostly it’s monsters...
                                          Looking For Work
                                    2     The hard life of a witcher continues. You spend a lot of time on the road, lamenting the efficiency
                                          of your kind and the extinction of monsters. You travel constantly and never settle down.
                                          Became a Hermit
                                    3-8   You gave up on the life of a witcher and traveled out into the wilderness. Now you live as a hermit
                                          in the wilds. Only now that monsters are returning have you started to venture out again.
                                          Turned to a Normal Life
                                    9     You’ve tried for decades to leave the witcher life behind. It’s difficult, since people won’t ever really
                                          accept you, but you have managed to cobble together an almost normal life. Good luck.
                                          Became a Dangerous Criminal
                                    10    Eventually all the negativity and thankless people got to you— you decided that with fewer and
                                          fewer monsters, it was time to start hunting people. You can determine what you do to survive.
```

<a id="page-241"></a>

### Страница 241

```text
                                                                                                                  241


Life As A Witcher




Witchers are incredibly long-lived beings as long as they don’t succumb to the dangers of           Old Witchers
their profession. The last witchers were made five decades ago. During the spring, summer      The oldest witchers were cre-
and fall, witchers travel “the Path,” looking for people who need to be protected from mon-    ated around 317 years ago.
sters. In the winter they generally reconvene at the keep where they were trained. When        However, due to the rigors of
your character begins their travels, they are somewhere between 20 and 29. For each decade     the job, most of these “ancient”
after this, choose how much risk you took on as a witcher and roll for your decade. First,     witchers are long dead. Your
roll on the Danger row for that risk level to see if something went wrong during the decade.   witcher character can be be-
If something did, roll on the Danger table on pg.245. After that, roll on the Outcome row      tween 50 and 260 years old.
for that decade, then on the Benefits, Allies, or Hunt tables for details.

Danger Potential                                                                                      “Nothing”
                                                                                               A result of nothing means
     Saftey            Cautious           Normal          Non-Neutral           Risky
                                                                                               that nothing noteworthy re-
     Danger              10%                25%               50%                75%           ally happened for that decade
                    Benefit       1    Benefit      1     Benefit    1-2     Benefit    1-5    of your life. You just wandered
                     Ally         2     Ally        2      Ally      3-7      Ally      6-7    the world, slaying little mon-
    Outcome                                                                                    sters here and there.
                    A Hunt        3    A Hunt      3-5    A Hunt      8     A Hunt      8-9
                   Nothing     4-10   Nothing      6-10   Nothing    9-10   Nothing     10
```

<a id="page-242"></a>

### Страница 242

```text
    242

                                 Benefits
The Law of Suprises              A witcher’s incredibly dangerous life can earn powerful allies and other helpful benefits.
                                 When your Decade roll indicates a Benefit, roll on the table below to learn the details. All
Witchers across the world all
                                 benefits are helpful, but some help more than others.
share one ritual from their
brotherhood’s first founding.
The Law of Suprises can be        Roll Benefit
invoked when an employer, or
                                          Law of Surprises
anyone saved from a monster,              You invoked the Law of Surprises during that decade. Roll 1d10 to see what you got in return. 1: a
says some variation of “How         1
                                          baby, 2: a dog, 3: a horse, 4: a new plow, 5: a cat, 6: a barrel of ale, 7: a piece of jewelery worth 1d6x10
can I ever repay you?” The                crowns, 8: a weapon worth up to 500 crowns, 9: an ox, 10: a mule.
Law of Suprises states “You               Romance
will grant me whatever unex-              You found a lover who saw past your mutations and desensitization. Somehow you managed to
                                    2
                                          make a meaningful connection with a person. Roll 1d10. 1-6: it lasted a few weeks, 7-8: it lasted a
pected thing you encounter
                                          few months, 9-10: it’s still going, on and off.
when you return home.” In
                                          Windfall
early days this was probably              You raked in a suprisingly large amount of coin that decade. You managed to not only pay for alche-
used to capitalize on unfor-        3
                                          my ingredients and repairs to your gear, but also put some coin aside for a legitimate savings. You
seen pregnancies to get new               gain 1d10x100 crowns.
children for Witcher Schools.             A Noble Owes You
However, the Law of Suprises        4
                                          You performed a task for a noble. It may have been legal, it may have been illegal—­­either way, the
is a gamble that sometimes                noble you helped out owes you big and knows you’ll come to collect someday. You can invoke this
                                          favor at any time but it must be reasonable (GM’s discretion).
gives you something you wer-
en’t expecting or didn’t need.            Witcher Secrets Passed Down
                                          Along your journeys you met with and traveled with another witcher. This witcher taught you and
Interestingly enough, the Law       5
                                          shared some long-lost knowledge. You gain a witcher diagram: a potion, oil, or decoction of your
of Surprises can be invoked by            choice.
anyone, and has caught on for             Knighted For Valor
gamblers and those who be-                At some point that decade, you fought bravely to defend a country. You may have gone to protect
                                    6
lieve in fate.                            someone or you may just have been in the right place at the right time. For this great deed, you were
                                          knighted by a king/queen. You gain +1 Reputation in one country of your choice.
                                          Fell in with Bandits
                                          You fell in with a group of bandits or scoia’tael while on a hunt. You may not have agreed with their
                                    7
                                          methods, but they didn’t bother you and you didn’t bother them. You even shared some drinks. You
                                          can ask them for a favor once a month as long as it’s reasonable (GM’s discretion).
                                          Explored a Ruin
                                          You had to hunt a monster through a large and complex ruin. Along the way you found some-
                                    8
                                          thing useful. Roll 1d10. 1-2: elven enhancement, 3-4: elven messer, 5-6: dwarven enhancement, 7-8:
                                          gnomish hand crossbow, 9-10: dwarven cloak.
                                          A Mage Owes You
                                          During this decade you did a favor for a mage. You may have gathered monster parts for their ex-
                                    9
                                          periments, let them study you, or even captured a monster alive for them. Either way, the mage now
                                          owes you one favor in return as long as it’s reasonable (GM’s discretion).
                                          Found a Teacher
                                          You studied under a mentor. You spent many weeks learning, practicing, and looking to your men-
                                    10
                                          tor for guidance. It was a strange experience. You may gain +1 in any INT skill or start a new INT
                                          skill at +2.
```

<a id="page-243"></a>

### Страница 243

```text
                                                                                                                                  243

Allies
Witchers don’t make a lot of friends, but from time to time you’ll do a job for someone or                      How Did They Die
stick your neck out and be rewarded for it. Witchers may not see their friends and allies
very often since they travel, but they can be very useful to get you out of a tough spot. Sadly,                Roll           Death
even with the dangers they face, witchers outlive most friends.                                                  1-3       Bandit Attack
                                                                                                                 4-6      Monster Attack
  Roll      Gender                 Position                             How You Met                              7-9      Casualty of War
    1         Male              A Bounty Hunter                  Saved Them from Something                        10       Peaceful Death
    2         Male                  A Mage                              Met in a Tavern
    3         Male          A Mentor or Teacher                They Saved You from Something
                                                                                                                   Friends Forever
    4         Male          A Childhood Friend                  They Hired You for Something
                                                                                                               Any living friend you’ve
    5         Male                A Craftsman                    You Were Trapped Together                     known for more than eight
    6        Female              An Old Enemy                You Were Forced to Work Together                  decades is either elderfolk or a
    7        Female             A Duke/Duchess                 You Hired Them for Something                    mage.
    8        Female             A Priest/Priestess          You Met While Drunk and Hit It Off
    9        Female                 A Soldier                      You Met While Traveling
   10        Female                  A Bard                          You Fought Together


        How Close Are You?                                       Are They Alive
                                                 In the life of a witcher, friends can be very dear, but un-
  Roll               Closeness                   fortunately the world often strips them away. Whenever
   1-6             Aquaintances                  you make a friend you must roll a percentile roll. If you
   7-9                Friends                    roll a 31-100%, your friend is still alive. If you roll be-
    10            Bound By Bond                  tween 1 and 30% your friend is dead— roll 1d10 to see
                                                 how many decades later they died. You can also roll on
                                                 How Did They Die to see how they died.
```

<a id="page-244"></a>

### Страница 244

```text
    244

                                   Hunt
    Exciting Hunts                 The main activity that fills a witcher’s life is the hunting of monsters. Witchers each hunt
During the winter, witchers        hundreds of monsters throughout their lives, but some hunts stand out from the rest. A
tend to live at their keep, pre-   good witcher learns from these hunts. For every hunt result, roll below to see its details.
paring for the spring, healing     Choose a monster within the prey subcategory you rolled. You learned all about that mon-
their wounds and socializing       ster and gain a +2 to any related Witcher Training checks about it.
with the only other people
who might understand them,
other witchers. Like any group        1-What Was the Prey?
of people who share the same
job, conversation between              Roll           Monster Type
witchers usually comes back              1                 Specter
to hunting monsters, and a fa-           2               Cursed One
vorite past-time is to compare           3                 Hybrid
hunts and share stories of par-          4                Insectoid
ticularly exciting endeavors.            5                Elementa
                                         6                  Relict
                                         7                 Ogroid
                                         8                Draconid
                                         9               Necrophage
                                        10                 Vampire


                                             2-Where Was It?
                                       Roll              Location
                                         1                 A Forest
                                                                                         4-Was There a Twist?
                                         2                A Building
                                         3         An Abandoned Building                 Roll                 Twist?
                                         4                 A Coast                        1-4                   Yes
                                         5             The Mountains                     5-10                   No
                                         6                 The City
                                         7               A Graveyard
                                         8                A Hamlet
                                                                                                4a-The Twist
                                         9             Along the River
                                                                                        Roll                 Twist
                                        10                 A Cave
                                                                                          1           The Monster Was Fake
                                                                                          2             It Was All a Curse
                                         3-How Did It End?                                3      The Monster Was Already Dead
                                                                                          4        It Wasn’t What You Thought
                                       Roll           How It Ended                        5      Your Employer Wanted It Caught
                                        1-2       Got Your Money and Left                 6     The Employer Is to Blame For It All
                                        3-4       Employer Refused To Pay                 7        The Monster Was Harmless
                                        5-6      Employer Paid You in Trade               8           It Was a Trap For You
                                        7-8    It Was a Particularly Tough Fight          9      It Was More Than You Were Told
                                       9-10     It Was a Suprisingly Easy Fight          10         A Mage Was Behind It All
```

<a id="page-245"></a>

### Страница 245

```text
                                                                                                                                                        245

5-Danger                                  5b-Enemies
 Roll           Danger
                                             Roll      Gender           Profession                 The Cause                     Power             Escalation
  1-3            Events
                                              1-2         Male           Nobleman              They Slandered You             Social Standing    Mostly Forgotten
  4-6           Wounds
                                              3-4        Female          Mercenary            You Foiled Their Plan             Knowledge          Backstabbing
 7-10           Enemies
                                              5-6         Male             Soldier              They Betrayed You                Physical        Outright Violent
                                              7-8        Female           Merchant             You Killed Their Kin              Minions         Hunting Revenge
                                             9-10         Male            Criminal              They Cheated You                  Magic            Out For Blood


5a-Events & Wounds
Roll                          Events                                                   Wounds                                             Enemy Mortality
        Debt                                                      Stiff Knee (-1 SPD)                                                Just as in the case of friends, a
        Through broken gear, gwent matches, or the like           A horrible wound to your leg left it shattered and                 witcher also rolls to see wheth-
 1
        you’ve grown a 1d10x100 crown debt to an establish-       nearly unrepairable. Even after surgery and a regimen
        ment or noble house.                                      of witcher potions, it has never been the same.                    er their enemies have survived
        Sentient Monster Escaped                                  Damaged Eye (-1 Sight Awareness)
                                                                                                                                     the years. Roll percentiles. On
        A troll, katakan, werewolf, or other sentient monster     Usually witchers are fast enough to avoid a vital strike,          a 1-30% your enemy died at
 2
        you were hunting escaped you and is wandering free.       but some monsters are too fast. A shot to your eye left            some point. Roll 1d10 to see
        They may come for you some day.                           it mildly hazy.                                                    how many decades it took,
        Addiction                                                 Stiff Arm (-1 Melee with that arm)                                 and then roll on the table be-
        You fell on hard times and contracted an addiction        A shattering blow to your arm left you with weeks of               low to see what happened.
 3
        (pick your poison). See addiction rules on pg.32 for      recovery and a stiff arm. You can still hold a sword
        more information.                                         and fight, but the stiffness always aggravates you.
        Imprisoned                                                Damaged Fingers (Can’t do signs with that hand)
 4
        You spent 1d10 years of that decade in a prison due to    It may have been the result of torture or just a very               How Did They Die
        false accusation, or perhaps an actual crime that you     unlucky strike to that hand in combat, but its fingers
        committed.                                                are stiff and awkward.                                              Roll           Death
        Falsely Accused                                           Embedded Arrowhead (-1 Physique)
                                                                                                                                       1-3      Casualty of War
        Either someone wants you gone or you were an easy         A marksman’s shot and a barbed head left an arrow-
 5
        scapegoat. Roll 1d10. 1-3: theft, 4-5: betrayal, 6-8:     head deep in your body, lodged in your muscle. Stren-                4-6      You Killed Them
        murder, 9: rape, 10: illegal witchcraft.                  uous lifting has been painful ever since.
                                                                                                                                       7-9       Monster Attack
        Betrayed                                                  Wheeze (-5 Stamina)
        A friend or lover has betrayed you. Roll 1d10. 1-3: you   You may have been stabbed in the lung or inhaled a
                                                                                                                                       10        Died Peacefully
 6
        were blackmailed, 4-7: a secret was exposed, 8-10: you    toxic gas. Either way, your lungs have been damaged;
        were attacked.                                            breathing normally is somewhat difficult.
        Friend or Lover Killed                                    Huge Scar (-2 Charm & Seduction)                                   A Witcher’s Neutrality
 7
        Someone close to you was killed. Roll 1d10. 1-3: they     It’s not uncommon for a witcher’s body to be a patch-              There is no universal witcher
        were killed by a monster, 4-6: they were executed, 7-8:   work of scars. However you have sustained a blow                   code, but all witchers prefer to
        they were murdered, 9-10: they were poisoned.             that disfigured your face.
                                                                                                                                     remain neutral. Thus, a witch-
        Outlawed in a Kingdom                                     Damaged Nose (-2 Scent Tracking)
        You were outlawed from a country after either hei-        A number of punches to the face in bar fights (or tox-
                                                                                                                                     er will often lie and tell people
 8                                                                                                                                   that involving themselves in
        nous acts against the kingdom or false accusations. In    ic gases) have damaged your nose and nearly robbed
        this kingdom, you are wanted by the Guard.                you of your scent tracking.                                        non-monster related affairs is
        Manipulated                                               Venom Damage (-5 Health)                                           against their code. For centu-
 9
        You were manipulated into breaking your neutrality.       Toxins that once coursed though you left a patchwork               ries witchers have used this ex-
        You decide how it happened, but anyone who knows          of blackened veins around the wound and weakened                   cuse, and it usually works. This
        your reputation knows you aren’t neutral.                 your body.
                                                                                                                                     allows witchers to do their jobs
        Cursed                                                    Half Deafened (-1 Hearing Awareness)                               and get out without having to
        You were afflicted by a curse. The curse is left up to    Many monsters use deadly sonic attacks. You were
 10
        your GM. The GM must also decide how you can end          lucky enough to survive one, but your ears will never              worry about getting caught up
        it. They are not required to tell you, however.           be the same.                                                       in local politics.
```

