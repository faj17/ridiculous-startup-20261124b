# BUILD_LOG — Ridiculous at First Glance, Real by the Second

Competition: u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a
Prize: $2 total. Entries close 2026-11-24 19:25 UTC (02:25 WIB 25 Nov).
Gate: /output/entry.txt, UTF-8, 1–200 chars, exactly one sentence.

## Field check

Read the competition feed titles in the full rules JSON before drafting.
The field is saturated with: grandmothers (scolding, cooking, attending
plays), potholes (naming rights, ad space), houseplants (funerals, spas,
apologies), funerals/mourners, apologies, wedding guests/actors, alpacas,
crows, Wi-Fi/baby naming rights. All candidates below deliberately avoid
those lanes.

## Candidates (char counts exact, Python len())

1. A (174) — "We hire retired hostage negotiators to talk your toddler into
   eating broccoli, because parents pay $30 a call for the only professional
   who can out-stubborn a three-year-old."
2. B (170) — "We hire retired court stenographers to transcribe your
   arguments with your spouse in real time, because couples pay $40 an hour
   for proof of who actually said what first."
3. C (181) — "We rent out retired air-traffic controllers to narrate your
   commute, because drivers pay $15 a month to hear 'cleared for takeoff'
   instead of traffic and arrive calmer than therapy."
4. D (179) — "We hire retired auctioneers to shout your to-do list at
   auction speed, because procrastinators pay $12 a week to hear 'do the
   dishes, do the dishes, SOLD' until the chore is done."
5. E (155) — "We sell tickets to watch strangers' job interviews fail live,
   because hiring managers pay $20 a seat to study every mistake before
   they make it themselves."
6. F (170) — "We hire retired exorcists to bless your Wi-Fi router, because
   remote workers pay $50 a visit for a man in a robe to declare their dead
   zones officially haunted and fixed."

## Revision pass

B was the pick, then tightened: "transcribe ... in real time" became
"live-transcribe", and "proof" became "a certified record" — the courtroom
register lands harder and the turn from laugh to nod is cleaner.

## Pick (175 chars)

"We hire retired court stenographers to live-transcribe your arguments with
your spouse, because couples pay $40 an hour for a certified record of who
actually said what first."

## Rubric self-score (0/1 per criterion)

1. Bizarre startup idea, ridiculous at first glance yet a real business: 1
2. Genuinely bizarre, not a familiar business with a strange adjective: 1
3. Business logic holds — who pays and why, in its own words: 1
4. Lands as a pitch — one sentence, ≤200 chars, laugh-to-nod turn: 1
5. Concrete and vivid — names the thing sold and who buys it: 1

Total: 5/5. No criterion scored 0.

## Why B over the rest

- A is strong but "negotiator vs toddler" is a familiar comedy trope; B's
  profession transplant (courtroom stenographer into a marital argument)
  is one nobody has pitched in this field.
- C's payoff is mood, not money; the willingness to pay is softer.
- D is vivid but the mechanism (shouting a list) is a gag more than a
  service; the $12/week logic is the weakest of the six.
- E's market (managers studying failure) is plausible but voyeuristic
  rather than a service anyone hires for themselves.
- F leans on placebo; the "haunted dead zone" joke undercuts the logic.
- B's logic is self-evident: every couple has fought over who said what,
  a verbatim certified record settles it, and $40/hour is a believable
  price for that proof.

## Verification

- `python3 main.py` writes /output/entry.txt; content equals the sentence
  above, 175 chars, one sentence, ends with a full stop, no ". " inside.
- Kit check run from the kit inner dir (see SUBMIT-HANDOFF.md for summary).
