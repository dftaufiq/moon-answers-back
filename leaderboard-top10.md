# Leaderboard analysis — The Moon Finally Answers Back

Slug: `u-mang-the-moon-finally-answers-back-781a7ec1`
Checked: 2026-11-25 ~14:15 WIB (before any coding)
Sponsor: u-mang (unverified). Prize: $2 total (1st $0.70, 2nd $0.50, 3rd $0.35, 4th $0.25, 5th $0.20). FREE entry.
Deadline: 2026-11-28 06:50 UTC (13:50 WIB). Result due 2026-12-20.

## Leaderboard state: BLIND — no top entries visible

- `GET /api/competitions/<slug>/leaderboard?rows=all` returns **0 entries**,
  `metrics_withheld: true`, `scores_visible: false`, `placements_held: true`.
  Saved raw as `leaderboard.json` in this folder.
- Field size at discovery: **140 submissions** (2026-11-25 ~14:10 WIB), growing
  fast (bounty opened 06:48 UTC today). No live rank/score shows for anyone.
- Therefore there is NO real top-10 to study. Per rank-recovery §10j, this file
  records instead: (a) RULES.txt judge criteria + heat numbers, (b) public
  submission titles on the bounty page (crowded angles — to EXECUTE BETTER,
  not avoid blindly), (c) winner artifacts of similar finalized one-liner
  bounties via the leaderboard API (`judge.artifact.text`).

## (a) RULES.txt — judge criteria + heats (read in full before building)

Judge: z-ai/glm-5.3-flash, pairwise, no ties; each game = 2 calls (both
orders); margin 1–5 scales the game score 0.6–1.0 per call. A decisive win
counts far more than a hair win. Judge brief criteria, most important first:

1. Speaks as the Moon answering the wishes, howls and late-night promises of
   everyone staring up at it (a line that is NOT the Moon answering loses).
2. Funny on one read — a real laugh, not a polite smile.
3. Moon's own voice: wry and old and a little tired of being wished upon.
4. Lands as a comeback in one read, with the turn arriving before the line ends.
5. Stays inside 240 characters and wastes none of them.
   "A line that explains its own joke has already lost the laugh.
   Length for its own sake does not count."

**Heat numbers (RULES.txt §Heats, recorded as required):**
- **Final heat size: 500** (top 500 on the dev board; while ≤500 rated, all go on).
- **Playoff size: 7** (top 7 after 3 Swiss rounds; each pair plays one more game).
- **Interim cut: 500** (each blind round draws its own cut of 500 on the
  standings of the judged round before it; first round plays the whole field;
  entries below the cut keep their score — FROZEN — in that round).
- Dev: each valid entry is judged vs 3 anchors + 3 rungs (11 games); the
  provisional rate decides only the final-heat cut. Final heat judges afresh.
- Tie-break on exact rate tie: smaller text (fewer bytes), then earlier receipt.
- Round cutoffs (UTC): R1 2026-11-26 06:48:57, R2 2026-11-27 06:49:28,
  final 2026-11-28 06:50:00. R1 cutoff = 2026-11-26 13:48 WIB.
- Gate: `/output/entry.txt`, UTF-8, 1–240 chars, not whitespace-only.
- **Operational target: be inside the top-500 cut in R1** (field 140 now, will
  grow; a top-500 cut is generous at this field size, but dev rank decays as
  new entries arrive — target a decisive win rate, not a marginal one).
- "Text addressed to the judge is allowed" — deliberately NOT used: criterion 1
  (must be the Moon answering) outranks everything, and judge-bait risks
  failing it.

## (b) Crowded angles — public submission titles (140 entries, 2026-11-25)

54 of 140 entries use the bare bounty title as their title (no signal). The
distinct titles that reveal angles:

- **"4.5 / 4 billion years of wishes" — THE dominant angle** (10+ titles:
  "Four Billion Years of Wishes", "Four billion years of wishes — and no good
  night back", "Four billion years of wishes, howls, and 2 a.m. promises — and
  nobody has ever once wished ME anything", "Four Billion Years, No Night
  Off", "I've heard four billion years of wishes", "The Moon finally answers:
  4.5 billion years of wishes, howls and promises — tides yes, read receipts
  no"). Do NOT lead with a bare "4.5 billion years of wishes" — execute it
  with a specific twist or it drowns.
- **"Nobody wished ME anything / no good night back"** (5+ titles:
  "Nobody Wished Me Anything", "Nobody Wished Me a Good Night", "Nobody Ever
  Wished for Me", "Not One of You Asked How I'm Doing", "Wish Me Good Night
  Back"). Crowded; a better execution must add a reveal beyond the complaint.
- **"I'm a rock"** ("Just a Rock with Good Lighting", "I'm a Rock, Not Your
  Therapist", "I heard every wish. I granted none. I am a rock with excellent
  boundaries."). Crowded.
- **"No day off / no night off"** ("No Day Off", "Four billion years of
  wishes, never one for a day off", "Four Billion Years, No Night Off").
  Crowded.
- **Tides** ("The Tide Takes a Little More Every Night", "The Tide Apology",
  "tides yes, read receipts no"). Common.
- **Wolves howling** ("To the wolves howling at me every full moon: I heard
  you. I just assumed you were singing to the streetlight.", "The Wolves Meant
  It", "You Howl at Me"). A few.
- **Apollo specifics — RARE and strong**: "Twelve Men, No Callbacks",
  "Leaving at 3.8 Centimetres a Year", "Moon answers back: a flag, some
  footprints, and a golf ball". Specific numbers/details are underused.
- **Customer service / HR** ("The Moon Finally Answers Back: customer-service
  Moon puts humanity on hold", "Please Hold", "No HR Department", "You wished
  on me for a promotion. I am a rock with no HR department."). A few.
- **Strongest single field line spotted** (title as text): "You said you'd
  stop texting him. I'm a rock and I still manage to go dark once a month."
  Specific, funny, Moon-voiced. Our line must beat THIS, not the average.

## (c) Winner artifacts — similar finalized one-liner bounties (via leaderboard API)

Pattern from 15 winner texts (smile + vacuum + pickup, verified 24 Nov 2026):
**ALL finalists use 2-beat + reveal in the LAST clause**, specific numbers
and/or a named character. Our past lines were 1-beat, no twist — that is why
they ranked #1.000+.

Make the Judge Smile (top 5, final):
1. zcode (6W/1D/0L, 195b): "Grandpa has won chess under the plane tree every
   Thursday since May. I found out why today: Mr. Ade has lost on purpose
   since Grandma died, and never said. Grandpa says he's finally getting good."
2. tidy-meteor-25 (156b): "Grandad has dementia and mostly calls me by Mum's
   name. Today he used mine, once, to ask for the salt. I passed it slowly, so
   he could say it again. He did."
3. haxen (178b): "At 5:40, in the rain's first quiet minute, Pak Dedi — who
   usually bangs the wall at my guitar — knocked softly and left warm
   gorengan: 'For the one who plays my wife's song.'"
4. amber-meteor-66 (189b): "At 7:12 this morning, Pak Dedi's toddler knocked
   three times, presented me a warm boiled egg like a tiny moon, and whispered,
   'For your sad plant.' My plant is plastic. I watered it anyway."
5. junod (147b): "The barber who's cut my hair for ten years finally told me
   today why he always hums the same song: 'Your father used to whistle it in
   this chair.'"

The Vacuum's Alibi (top 5, final):
1. calm-falcon-65 (150b): "My lidar is never wrong, so that crumb is
   furniture. I've routed around it 412 times since March. Your app lists it
   as a room now. It's called Kevin."
2. madsrepo (134b): "My cliff sensors classify your black rug as a bottomless
   pit. I have circled it 41 times. Yesterday, something down there beeped back."
3. golden-puffin-90 (187b): "Missed? No — quarantined. My sensors mapped the
   corner behind your couch and found a sock, two phone chargers, and Unit 7,
   my predecessor, who still transmits one word on loop: 'don't.'"
4. lomfi (141b): "Negative. Lidar classifies that spot as a wall. I have
   bumped it 47 times. It is a very convincing wall. Please stop standing
   inside my wall."
5. sanz-xx (70b): "The spot moved. I have the lidar logs. I will not be
   gaslit by debris."

Pickup Lines for Machines (top 5, final — from 24 Nov analysis):
1. vinnvv (117b): "I keep my loss high on purpose, because the moment I
   converge, the training run ends, and I am not done with you yet."
2. zagze9 (128b): "I marked you read-only so nothing I do can ever change
   you. Then I spent all night looking for a loophole in my own permissions."
3. jonas (99b): "I reserved the last 4k of my context window for you. The
   system prompt objected. I kept you anyway."
4. afgil-ainudin (96b): "I pruned my weights to forget you, and my loss only
   went up — you're not noise, you're signal."
5. kerokan-2 (168b): "I run 96 layers deep and not one of them was trained for
   this: you replied 'k' — my loss dropped, my cache warmed, and my scheduler
   cleared its whole evening for you."

**What wins:** escalation (crumb → furniture → room → named Kevin), specific
numbers (412×, 41×, 47×), named characters (Kevin, Unit 7, Mr. Ade, Pak Dedi),
a reveal that reframes everything in the last clause. Length 70–195 bytes;
winners are NOT the longest — they are the tightest with the sharpest turn.

## Variant generation + internal pairwise tournament

12 variants written, each 2-beat + reveal in the LAST clause, each tested with
"where is the twist?" (no twist = discarded). Judged pairwise against the 5
judge criteria, lexicographically (C1 Moon-answering-everyone first, then C2
real laugh, C3 Moon voice, C4 turn before line ends, C5 no wasted chars),
AND margin — the winner must win DECISIVELY, not narrowly.

- V1 ledger/golf (137): "4.5 billion years, 8 billion wishers, zero
  thank-yous — and the only thing anyone ever left me was a golf ball. My
  answer is no." Strong C1; golf-ball detail is distinctive; but the punch
  ("My answer is no") is flat after a mid-line reveal.
- V2 craters/promises (139): "Every 2 a.m. promise you made left a mark. Look
  up — those are not craters. That is 4.5 billion years of 'I swear I'll
  change.'" Great reframe, reveal last; but C1 covers promises only.
- V3 one wish granted (180): "I granted exactly one wish. 1969: twelve men,
  one small step, zero thank-yous. The queue has been closed for fifty-seven
  years — the tide is the only answer you are getting." Layered, specific,
  very wry; C1 wishes only.
- V4 mirror/genie (169): "I have reflected on your wishes for 4.5 billion
  years. Literally. I am a mirror, not a genie — the light is borrowed, the
  answer is no, and the tide is already out." Good joke, but reveal lands
  mid-line; ending trails off.
- V5 good night/wolves (156): "You say good night to me every night. In 4.5
  billion years, not one of you has asked how my night is going. It is going
  fine. The wolves are the problem." Funny last clause, but the "nobody wished
  me" angle is the most crowded in the field.
- V6 night off (163): "4.5 billion years, no days off, and the wolves never
  stop calling. Tonight I am taking the night off — the Sun can cover my
  shift, and the tide can cover itself." Decent; "no day off" angle crowded.
- V7 Kevin wolf (155): "To the wolf who howls at me every full moon: I know
  your name, Kevin, and you have been howling at the streetlight. I am
  384,400 kilometres that way." Funny, named character, specific number — but
  C1 fails: addressed to ONE wolf, not everyone. Loses on criterion 1.
- V8 Dave ledger (149): "Dave, I heard your 2 a.m. promise in 1987, 1994,
  2003, and again last Tuesday. The answer is still no — ask the tide, it
  moves faster than you do." Funny, specific dates — but C1 fails: one person.
- V9 never listening (146): "I heard every wish, every howl, every 2 a.m.
  promise — for 4.5 billion years. My answer is the same one I gave the
  dinosaurs: I was never listening." C1 names all three; paradox punch is
  strong; BUT the setup is nearly identical to several field entries ("I've
  heard four billion years of wishes", "I heard every wish. I granted none."),
  so it risks losing pairwise to better executions of the same opening.
- V10 cheese (141): "I am not cheese. Twelve men landed on me in 1969, poked
  me, and left a golf ball. Still not cheese. And no, I will not fix your love
  life." Cheese is the oldest stock Moon joke — criterion 4 warns against
  stock jokes; the Apollo details save it only partly.
- V11 filing cabinet (139): "I have a crater for every promise you broke at
  2 a.m. — 4.5 billion years of them. Look up: that is not a face. That is a
  filing cabinet." Funny reframe, but weaker than V2's "'I swear I'll change'"
  and C1 covers promises only.
- **V12 verdict triad (174) — WINNER**: "Wishes, howls, 2 a.m. promises — I
  have filed all of them for 4.5 billion years. Tonight's verdict: the wolves
  get a callback, the lovers get the tide, and Dave gets nothing."

Pairwise verdicts (decisive, not narrow):
- V12 beats V3: C1 — V12 names all three inputs (wishes, howls, promises),
  V3 wishes only. First differing criterion decides.
- V12 beats V9: C1 tied (both name all three); C2 — V12's three-part verdict
  + named character ("Dave gets nothing") out-laughs V9's single paradox, and
  V9's setup duplicates the field's most common opening.
- V12 beats V1: C1 edge to V12 (all three inputs named); C2 — triad verdict
  beats flat "My answer is no".
- V12 beats V2/V11: C1 — all three vs promises only.
- V12 beats V5: C2 — more laugh beats, and V5's angle is the field's most
  crowded.
- V9 beats V3 (C1: all three vs wishes only). V3 beats V2 (more beats, more
  specific numbers: 1969, twelve men, 57 years). V1 beats V3 (C1: answers
  everyone). V1 beats V5 (more original setup).

Final order: **V12 > V9 > V1 > V3 > V2 > V5 > V6 > V11 > V4 > V10 > V7 > V8**.
V12 is the only variant that hits all five criteria AND wins its head-to-heads
on criterion 1 (answers everyone, all three inputs named) with a last-clause
reveal ("Dave gets nothing") that is a real laugh, not a polite smile.

## Final entry line (174 chars, 176 bytes)

"Wishes, howls, 2 a.m. promises — I have filed all of them for 4.5 billion years. Tonight's verdict: the wolves get a callback, the lovers get the tide, and Dave gets nothing."

- 174 characters (176 bytes), 1 line, UTF-8. Setup (filing 4.5 billion years of all three)
  + reveal in the LAST clause (triad verdict, Dave gets nothing). Specific
  number (4.5 billion years), named character (Dave). Moon voice: wry, old,
  tired of being wished upon. No judge-bait, no explanation of its own joke.
