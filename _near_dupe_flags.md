# Near-Duplicate Flag Report — 2026-05-09

Audit run: cl100k_base tokenizer, NFKC + smart-quote normalization, prompt-only Jaccard ≥ 0.85 on 5-shingles.

- **Exact duplicates (prompt + completion identical, after Unicode normalization): 0**
- **Parse errors / schema issues: 0**
- **Near-duplicates flagged: 112**

## Summary by file

| File | Near-dupes | Notes |
|---|---:|---|
| `D_Conversations.jsonl` | 108 | ~95 trivial casing/punctuation variants of greetings; ~10 smart-quote prompt twins with paraphrased completions; 1 substantive near (risk avoidance, with/without "completely") |
| `D_material_science.jsonl` | 4 | 3 same-prompt/different-completion pairs (likely generation errors); 1 hyphen variant |
| `D_Trigonometry.jsonl` | 1 | False positive — different math problems (`sin·cos` vs `sin+cos`) |

---

## D_Conversations.jsonl — 108 flags

### Category A — Greeting surface variants (~95 flags)
Casing/punctuation/emoji variants of the same casual greeting. **Recommendation: KEEP — this is intentional surface-form variation valuable for naturalistic conversation training.** Examples:

- `hey` / `Hey` / `hey!` / `hey.` / `hey!!` / `Hey!` (L656, L8556, L11228…)
- `hello` / `Hello` / `hello!` / `hello!!` / `hello??` / `hello 👋` (L1466, L3568, L4681, L4810, L8643)
- `hi there` / `Hi there` / `hi there.` / `hi there :)` / `hi there 👋` (L1652, L1902, L2931, L4954, L7432)
- `hey friend` / `Hey friend` / `hey friend!` / `hey friend!!` / `hey friend.` (L4206, L7218, L8074, L9700, L11980)
- `hey hey` / `Hey hey` / `hey hey!` / `hey hey!!` (L1080, L2132, L2789, L11500)
- `hey stranger` / `Hey stranger` / `hey, stranger` / `hey stranger.` (L783, L1979, L6044, L8395)
- `hi` / `Hi` / `Hi!` (L4032, L7255, L9169)
- `hi hi` / `Hi hi` / `hi hi!` / `hi hi 👋` (L1113, L2770, L11935)
- `hiya` / `hiya 👋` (L7699, L8198)
- `howdy` / `Howdy` / `howdy.` (L8091, L8382, L10216)
- `sup` / `Sup` / `sup?` / `sup!!` / `Sup friend` / `sup, friend` (L978, L2898, L5322, L6350, L9421, L10936)
- `yo` / `Yo` / `yo?` (L8097, L10924, L10990)
- `hellooo!` / `hellooo!!` / `hellooo 👋` (L350, L2398, L2958)
- `hello there` / `hello there?` / `hello there!` (L5331, L7289, L8735)
- `Greetings` / `greetings` (L3601, L8385)
- `good morning` / `Good morning!` (L3387, L8484)
- `good afternoon` / `Good afternoon` (L4419, L6812)
- `good evening` / `Good evening` (L360, L2710)
- `Good to see you` / `good to see you` (L7313, L10514)
- Plus identical-meaning state-of-day greetings: `What's up`, `What's good`, `How's it going`, `How's the day been`, `How's your day shaping up`, `What's happening`, `What's the haps`, `What's the move today`, `How are things`, `How's everything`, `How's it hanging`, `you surviving the day`, `everything chill today`, `what are you up to` — each with several casing/punctuation variants.

### Category B — Smart-quote prompt twins with paraphrased completions (10 flags)
**Same prompt** (after NFKC + apostrophe normalization), **different completions**. Plausibly intentional paraphrase pairs to teach paraphrastic robustness. **Recommendation: KEEP unless you intended only one per prompt.**

| Lines | Prompt | Completion A | Completion B |
|---|---|---|---|
| L1576 / L12229 | "What's the difference between baking soda and baking powder?" | "Baking soda needs an acid to react. Baking powder already brings part of the chemistry to the party." | "Baking soda needs an acid to react. Baking powder already contains what it needs to puff things up." |
| L8159 / L11558 | "If I don't feel confident, I shouldn't do it." | "Confidence is not a permission slip. Sometimes you do it first and confidence shows up late." | "Confidence often shows up late. Annoying, but true." |
| L4589 / L9275 | "If I'm not sore, the workout didn't count." | "That's gym mythology. Progress isn't measured by how wrecked your stairs feel." | "That's gym folklore, not a rule." |
| L9736 / L11872 | "If I miss one workout, I've ruined my progress." | "Progress doesn't vanish overnight. Consistency matters more than one missed day." | "No, you've missed one workout. Let's not write a tragedy over Tuesday." |
| L2223 / L10295 | "I should answer every message immediately or I'm rude." | "That's too rigid. You're allowed to have a life." | "Nah. People can survive a reasonable delay." |
| L5703 / L7835 | "What's the point of stretching after sitting all day?" | "It helps loosen stiff muscles and restore some range of motion." | "It can ease stiffness and help your body stop feeling like a folded receipt." |
| L6284 / L11514 | "What's the best time to work out?" | "Whatever time you can do consistently. Beyond that, it depends on your schedule and energy." | "Depends on your schedule and when you can actually stick with it." |
| L7631 / L9080 | "What's a decent last-minute gift?" | "Something usable: coffee, tea, candles, snacks, or a gift card." | "A good snack, a candle, or a bookstore gift card." |
| L11589 / L12244 | "If I'm busy all day, I was productive." | "Not necessarily. Busy and productive aren't twins." | "Not necessarily. Busy and productive aren't the same thing." |
| L7777 / L8544 | "What's better for notes: paper or phone?" | "Paper for focus, phone for convenience." | "Paper for focus, phone for convenience. Pick the one you'll actually use." |

### Category C — Substantive near, with vs without an intensifier (1 flag)
- L3501 / L4509 (j=0.875): `"If there's any risk at all, I should avoid it."` vs `"If there's any risk at all, I should avoid it completely."`
  Different rigidity levels — likely a deliberate pair for cognitive-distortion training. **Recommendation: KEEP.**

---

## D_material_science.jsonl — 4 flags (RECOMMEND USER REVIEW)

These look more like generation accidents than intentional variation. **Recommend deleting one row from each pair.**

| Lines | Prompt | Notes |
|---|---|---|
| L10 / L211 | "Why are ceramics often brittle?" | Both `easy/cause_effect/direct`. L211 wording slightly clearer. **Suggest: drop L10.** |
| L526 / L663 | "Define cementite." | L526 labeled `medium`, L663 labeled `easy`, but both prompts are identical and both completions are medium-grade detail. Tier-labeling defect on L663. **Suggest: drop L663.** |
| L537 / L1478 | "Define erosion-corrosion." | Both `easy/definition/direct`. L1478 has slightly more detail. **Suggest: drop L537.** |
| L330 / L1488 | "Define solid-solution strengthening." (hyphen) vs "Define solid solution strengthening." | Both `easy/definition/direct`. L1488 has more substance. **Suggest: drop L330.** |

---

## D_Trigonometry.jsonl — 1 flag (FALSE POSITIVE)

- L2: `"What does the graph of y = sin(x) + cos(x) look like?"`
- L239: `"What does the graph of y = sin(x) · cos(x) look like?"`

These are different problems (sum vs product of sin and cos). The shingler stripped the `+`/`·` operators. **No action needed.**
