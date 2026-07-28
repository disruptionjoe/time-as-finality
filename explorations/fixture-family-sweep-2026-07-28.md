# Fixture-Family Sweep: Which Foliation-Overlay Findings Are Theorems, Which Are Regime Facts, and Which Are One-Fixture Artifacts

**Status:** exploration — formalism-internal robustness sweep; separates
typing-theorems from hand-built-fixture artifacts in the T586/T587/overlay
finding set; no new claim, no new T-number
**Date:** 2026-07-28
**Builds on:** [T586](../tests/T586-record-capability-order-gate.md)
([model](../models/t586_record_capability_order_gate.py)),
[T587](../tests/T587-t586-causal-collapse-boundary-attack.md)
([model](../models/t587_t586_causal_collapse_boundary_attack.py), verdict
`T586_DOWNGRADED_TO_TYPED_RECORD_PREREQUISITE_FILTER_REVIEW_ONLY`), and
[the foliation-overlay in-repo
reproduction](foliation-overlay-t586-reproduction-2026-07-27.md)
([model](../models/foliation_overlay_t586_reproduction.py))
**Model:**
[../models/fixture_family_sweep.py](../models/fixture_family_sweep.py)
(pure stdlib, deterministic — all randomness from fixed literal seeds declared
below; no clock or date calls; prints a JSON summary with an
expected/actual/match check table; exit 0 — all 32 gated checks match, and
repeat runs are byte-identical)

---

## Why this sweep exists

Every fixture-derived finding in the T586 → T587 → foliation-overlay chain
rests on **one** five-event fixture, `_landauer_record_events` in
`models/t586_record_capability_order_gate.py`. That fixture contains exactly
two causal edges that carry no record dependence — `seed_known_record ->
prepare_biased_reference` and `prepare_biased_reference ->
certify_erased_record` — and both are hand-declared. Three headline findings
lean on those two edges:

- **F1** — the record order is a **strict subrelation** of the causal order;
  "causal structure does strictly more constraining work than record
  structure" (T586's `causal_overread_control` audit; T587's absorption
  verdict; overlay finding 3).
- **F2** — a **foliation adds nothing** to the record order: recomputing the
  record closure with a genuine global-tick label present returns the
  identical closure (overlay finding 1), and everything the foliation adds is
  unlicensed — no record basis in either direction (overlay finding 2).
- **F3** — record and causal constraints **underdetermine the foliation**:
  of 120 candidate foliations, 5 respect the record order, only 3 the causal
  order, so the record-admissible set strictly contains the
  causally-admissible set, and a three-fold degeneracy survives both
  constraints (overlay findings 3–4).

A program-adversary pass asked the right question: are these facts about the
**formalism**, or facts about **that fixture** — artifacts of where two
record-free causal edges happen to have been drawn by hand? The adversary's
sharpest prediction: *in a fixture where every causal edge carries a record,
the strict-inclusion finding vanishes identically.*

This sweep answers by running the same derivations — T586's own
`build_order_report`, `causal_relation`, and `transitive_closure`, and the
overlay module's admissibility machinery, imported, not copied — across a
randomized fixture family of 600 fixtures spanning three regimes, and by
proving as theorems whatever turns out to be provable. It is
formalism-internal robustness work only.

## The three regimes

A fixture is a DAG on `n` events (n = 5–9), with events indexed so every edge
points forward in index order (acyclicity by construction; every event gets
one executable task, so record dependences always materialize as edges —
see §Task-typing wrinkle). Direct causal edges are drawn independently with a
per-fixture edge density; a record dependence on an edge means the source
event produces a fresh record that the target event's executable task
requires (unique producer per record, all required records produced
in-fixture, so T586's gate preconditions hold).

- **Regime (i) `RECORD=CAUSAL`** — every direct causal edge carries a record.
- **Regime (ii) `RECORD⊊CAUSAL`** — each causal edge carries a record with
  probability `p_rec` (the record density), with at least one record-free
  causal edge enforced. This is the T586 fixture's shape.
- **Regime (iii) `RECORD⊄CAUSAL`** — a regime-(ii) draw plus at least one
  planted record dependence between a pair of events with **no** declared
  causal path in either direction. The `CapabilityEvent` type and the T586
  gate permit this: nothing in `build_order_report` consults
  `causal_parents`, so such a fixture passes the strict-partial-order gate.
  This is exactly the alignment question T587's boundary typing left
  implicit.

## Pre-registered design (frozen before execution)

All parameters below were fixed before the sweep was first run, and the model
file hard-codes them as literals:

- 200 fixtures per regime (600 total), event count cycling through 5, 6, 7,
  8, 9 (40 fixtures per size per regime).
- Causal edge density drawn per fixture from `(0.2, 0.35, 0.5, 0.7)`; record
  density `p_rec` drawn per fixture from `(0.35, 0.6, 0.85)` (regimes ii and
  iii).
- Generator seeds: 58601 (regime i), 58602 (regime ii), 58603 (regime iii);
  overlay/extension sampling seeds derived as 58610 + a running fixture
  counter. `random.Random` with these literals is the only randomness source.
- Per fixture: record closure via `t586.build_order_report`; causal closure
  via `t586.causal_relation`; join closure via `t586.transitive_closure` on
  the union; linear-extension counts for all three via a downset bitmask
  dynamic program (n ≤ 9, so exact counting is exhaustive-equivalent — the
  DP counts exactly what brute-force permutation filtering counts, and the
  anchor check below verifies it against the overlay's brute-force 5/3
  values); six foliation overlays per fixture (identity, reversed,
  lexicographically-first record-admissible, three seeded random
  permutations) each applied as a clock-label + entropy-rank relabel followed
  by full recomputation of the record closure; two linear extensions per
  fixture (identity and one seeded random extension) tested for the
  added-comparabilities lemma.
- Anchor: the T586 fixture itself is pushed through the identical pipeline
  and must reproduce the overlay note's numbers exactly (6, 8, 4, 5, 3, 2,
  3, 10, 4, 4).
- Two hand demos, fixed in advance: a three-event shortcut fixture
  (record chain a→b→c with a record-free direct causal edge a→c) predicted
  to give **record closure = causal closure exactly** despite strict
  containment at the direct-edge level; and a two-event task-typing fixture
  (consumer with a required record but an empty task tuple) predicted to
  yield **no** record edge.

## Pre-registered predictions (written before the results section)

**P1 (F2 is structural — a typing theorem).** The foliation-invariance
finding holds universally: zero violations across all 600 fixtures × 6
overlays. Reason, claimed in advance as a proof: the record closure is
computed by `record_dependency_edges` + `transitive_closure` +
`_missing_required_records`, whose dataflow reads only `event_id`,
`produced_records`, `required_records`, and `executable_tasks`. The fields a
foliation overlay acts on (`clock_label`; also `entropy_rank`,
`causal_parents`, `irreversible_operation`) are dead inputs to that
computation. So the record closure factors through the record-typed
projection of the event structure, and **any** relabeling of the dead fields
— in particular any injective global time assignment — stabilizes it. The
sweep is confirmation, not the ground of the claim.

Also claimed in advance as a theorem (overlay finding 2 generalized): for any
strict partial order R and any linear extension L of R, the added
comparabilities L∖R are **exactly** the R-incomparable pairs oriented by L —
so their count equals the incomparable-pair count, and none has a record
basis in either direction. "Everything the foliation adds is unlicensed" is
pure order theory, not a fixture fact; the fixture-specific part is only the
number 4.

**P2 (F1 is regime-dependent — an alignment discipline, not typing).**
`record ⊆ causal` holds in regimes (i) and (ii) by construction and fails in
regime (iii) by construction, while the T586 gate passes in all three —
predicted 200/200 strict-partial-order passes in every regime. So the
subrelation fact is a property of causally-aligned fixtures, not of the
formalism. Within regime (ii), **strictness at the closure level is generic
but not universal**: closure equality occurs exactly when every record-free
causal edge already lies in the record closure (a transitive shortcut of
record paths). Predicted: the three-event shortcut demo exhibits equality
constructively; the sweep finds at least one closure-equal regime-(ii)
fixture; and the closure-equal fraction is higher at `p_rec = 0.85` than at
`p_rec = 0.35`.

**P3 (F3's strict inclusion is F1 in disguise; it vanishes in regime (i) and
breaks in regime (iii)).** Claimed in advance as a theorem: for strict
partial orders R ⊆ C on the same finite ground set, the linear-extension
counts satisfy e(R) ≥ e(C), with **equality if and only if R = C**. Hence
"record-admissible ⊋ causally-admissible" is mathematically equivalent to
"record closure ⊊ causal closure": overlay finding 3 is a counting shadow of
F1, not an independent finding. Predictions: regime (i) — the adversary's
prediction confirmed identically, 200/200 fixtures with e(record) =
e(causal) and zero record-admissible-but-causally-inadmissible foliations;
regime (ii) — strict inclusion in exactly the closure-strict fixtures
(predicted equivalence violations: 0); regime (iii) — the containment itself
fails: 200/200 fixtures have a causally-admissible foliation that violates
the record order (via the planted causally-unrelated record pair plus
Szpilrajn), and a minority in which every causal edge happened to draw a
record shows full inversion (record closure ⊋ causal closure — record
structure doing strictly more constraining work than causal).

**P4 (degeneracy > 1 is a counting fact; the value 3 is an artifact).**
e(P) = 1 iff P is a total order; any incomparable pair yields e(P) ≥ 2 (both
orientations extend). Predicted: zero violations of "e(record) = 1 iff the
record order has no incomparable pair" across all 600 fixtures; the joint
(record+causal) extension count is ≥ 2 whenever the join leaves an
incomparable pair; the specific value 3 appears as nothing but one point in
a broad distribution.

**Falsifiers, stated in advance.** Any overlay-invariance violation kills P1
and is the headline. Any regime-(ii) fixture with e(record) > e(causal) but
record closure = causal closure (or vice versa) kills the P3 equivalence.
Zero closure-equal fixtures in regime (ii) would weaken P2's "generic but
not universal" to "not observed at these densities" (the shortcut demo would
still establish existence). A density trend opposite to prediction is a
recorded miss.

---

## Results — outcomes against pre-registration

All numbers below are from a single deterministic run of
`python3 -m models.fixture_family_sweep` (exit 0, all 32 checks match; the
JSON summary is byte-identical across repeat runs), except the regime-(iii)
inversion-mechanism split (25/38, 13/38) and the 162/200 mutual-non-containment
count, which are an in-note reanalysis of the same seeded fixture family
(recomputable by regenerating regime (iii) with the model's own generators;
independently re-verified before commit). No prediction was edited after
execution.

| Prediction | Outcome |
|---|---|
| P1: overlay invariance universal, 0 violations | **Confirmed.** 600/600 fixtures, 3,600 overlay recomputations (plus six on the anchor), 0 closure changes, 0 strictness changes |
| P1 (finding-2 lemma): added comparabilities = incomparable pairs, none record-based | **Confirmed.** 1,200 record-extension checks (identity + seeded-random per fixture) and 600 causal-extension checks, 0 violations |
| P2: gate passes in all three regimes | **Confirmed.** 600/600 `strict_partial_order`, including all 200 regime-(iii) fixtures with a record edge outside the causal order |
| P2: record ⊆ causal in (i)+(ii), fails in (iii) | **Confirmed.** 400/400 and 200/200 respectively (by construction, verified) |
| P2: regime-(ii) closure equality exists, rises with record density | **Confirmed.** 7/200 closure-equal fixtures; fraction by `p_rec`: 0.35 → 0/64 (0.000), 0.60 → 2/66 (0.030), 0.85 → 5/70 (0.071). The predicted 0.85 > 0.35 ordering holds; at the lowest density the sweep found none (the shortcut demo still gives constructive existence at any density) |
| P3: e(R) ≥ e(C) with equality iff R = C, in (i)+(ii) | **Confirmed.** 400/400, 0 equivalence violations, 0 monotonicity violations |
| P3: regime (i) — strict inclusion vanishes identically | **Confirmed.** 200/200 with e(record) = e(causal) = e(joint) exactly (ratio min = median = max = 1); 0 record-admissible-but-causally-inadmissible foliations |
| P3: regime (iii) — causal admissibility no longer implies record admissibility | **Confirmed.** 200/200 fixtures with a causally-admissible foliation violating the record order (e(joint) < e(causal)) |
| P3: regime (iii) minority with full inversion (record ⊋ causal) | **Confirmed on existence and minority (38/200); the predicted mechanism was only partially right.** In 25/38 every causal direct edge drew a record, as predicted; in 13/38 the inversion arises by a route the prediction missed — record-free causal edges whose pairs are nonetheless implied by the record closure. Recorded as a partial miss, not smoothed |
| P4: e = 1 iff no incomparable pair | **Confirmed.** 600/600, 0 violations |
| P4: the value 3 is one point in a broad distribution | **Confirmed.** Joint-order extension counts range 1 to 35,280 (median 22) across the family; the value 3 occurs in 24/600 fixtures, and the degeneracy vanishes outright (count 1) in 34/600 |

The anchor reproduced the overlay note's numbers exactly (record closure 6,
causal closure 8, incomparable pairs 4, extensions 5 vs 3 vs 3, record-
admissible-but-causally-inadmissible 2, added comparabilities 4 =
incomparable count, chosen extension causally inadmissible), which also
validates the bitmask DP against the overlay's brute-force permutation
filter (5 and 3 both ways). The three-event shortcut demo returned **record
closure = causal closure** with distinct direct-edge sets, as predicted. The
task-typing demo returned zero record edges for a consumer with a required
record but no executable task.

### Regime map (the load-bearing table)

| Quantity | (i) RECORD=CAUSAL | (ii) RECORD⊊CAUSAL | (iii) RECORD⊄CAUSAL |
|---|---|---|---|
| T586 gate (`strict_partial_order`) | 200/200 pass | 200/200 pass | 200/200 pass |
| record ⊆ causal | 200/200 (equality) | 200/200 | 0/200 |
| record closure = causal closure | 200/200 | 7/200 | 0/200 |
| record closure ⊊ causal closure | 0/200 | 193/200 | 0/200 |
| A_record ⊋ A_causal (strict foliation inclusion) | 0/200 | 193/200 | not a containment: 162/200 mutual non-containment, 38/200 inverted (A_record ⊊ A_causal) |
| causally-admissible foliation violating record order exists | 0/200 | 0/200 | 200/200 |
| record closure ⊋ causal closure (full inversion) | 0/200 | 0/200 | 38/200 |
| degeneracy ratio e(R)/e(C): min / median / max | 1 / 1 / 1 | 1 / 3.67 / 756 | no longer ≥ 1: 0.119 / 1.71 / 1,176 |
| e(record) min / median / max | 1 / 24 / 35,280 | 1 / 120 / 120,960 | 1 / 60 / 40,320 |
| e(causal) min / median / max | 1 / 24 / 35,280 | 1 / 24.5 / 33,264 | 2 / 29 / 18,648 |
| e(record) = 1 iff no incomparable record pair | 200/200 | 200/200 | 200/200 |
| overlay invariance (P1) violations | 0 | 0 | 0 |

Record-incomparability density spanned 0–1 across the family (per-regime
medians 0.40 / 0.72 / 0.60), so the sweep exercised near-total through
near-empty record orders; 12 regime-(ii) fixtures drew an **empty** record
closure — the boundary case where the record order does no constraining work
at all and the degeneracy ratio peaks (max 756). Regime (iii) needed 10
deterministic resamples (draws whose causal closure was total, leaving no
causally-unrelated pair to plant).

Regime-(ii) closure equality by record density `p_rec` (the F1-strictness
boundary): 0.35 → 0/64; 0.60 → 2/66; 0.85 → 5/70, with median degeneracy
ratio falling 13.96 → 4.72 → 2.00 across the same bins. Strictness of
"causal does more work" is density-dependent exactly as the shortcut
criterion says: equality iff every record-free causal edge is a transitive
shortcut of record paths, which becomes likelier as records saturate the
causal graph — and the *amount* of extra work (the ratio) shrinks toward 1
as saturation approaches.

## The four lemmas (proof sketches)

**L1 (dead-input factorization — upgrades F2 to a typing theorem).** The
record closure returned by `build_order_report` is a function of the tuple
(`event_id`, `produced_records`, `required_records`, `executable_tasks`)
alone. Proof by dataflow inspection of
`models/t586_record_capability_order_gate.py`: `record_dependency_edges`
reads only those four fields (producer map from `produced_records`, edges
from `required_records` × `executable_tasks`); `transitive_closure` reads
only event ids and the edge set; `_missing_required_records` reads only
`produced_records`/`required_records`; nothing else feeds `closure` or
`strict_partial_order`. `clock_label`, `entropy_rank`, `causal_parents`, and
`irreversible_operation` are dead inputs to the closure. A foliation overlay
in the overlay module's sense is a relabeling of `clock_label`; therefore
**every** foliation overlay — admissible or not — leaves the record closure
fixed, for every event set, not just the T586 fixture. Confirmed 3,600/3,600.

**L2 (unlicensed additions — upgrades overlay finding 2 to order theory).**
For a strict partial order R and any linear extension L (as a set of ordered
pairs, the total order's comparabilities): L ⊇ R, and for (a,b) ∈ L∖R we
have (a,b) ∉ R by membership and (b,a) ∉ R because L extends R and contains
(a,b). So L∖R is exactly the set of R-incomparable pairs, oriented by L:
|L∖R| = incomparable-pair count, and no added pair has a basis in R in
either direction. Confirmed 1,200/1,200 for the record order and 600/600 for
the causal order.

**L3 (extension-count strictness ⟺ closure strictness).** For strict partial
orders R ⊆ C on the same finite set: every linear extension of C extends R,
so e(R) ≥ e(C). If R = C, equality. If R ⊊ C, pick (a,b) ∈ C∖R; since C is
antisymmetric and R ⊆ C, (b,a) ∉ R, so a,b are R-incomparable; the
transitive closure of R ∪ {(b,a)} is then a strict partial order (a cycle
would need an R-path from a to b, i.e. (a,b) ∈ R, excluded), and by
Szpilrajn (finite case: greedy topological completion) it has a linear
extension — which extends R and violates C. So e(R) > e(C), and
**A_record ⊋ A_causal ⟺ record closure ⊊ causal closure**. Overlay finding
3's strict inclusion is not an independent observation: it is F1's
strictness, counted. Confirmed 400/400 with 0 equivalence violations.

**L4 (degeneracy > 1 ⟺ an incomparable pair).** e(P) = 1 iff P is total:
if some pair is incomparable, the L3 construction run in both orientations
gives two distinct extensions, so e ≥ 2; if P is total its unique extension
is itself. The *existence* of residual foliation underdetermination is
therefore a counting fact about any non-total order — what the fixture
supplies is only the particular multiplicity (3), which the sweep shows to
be one point in a distribution running from 1 to 35,280 (median 22; the
value 3 occurs in 24/600 fixtures; the degeneracy vanishes outright in
34/600 whose joint order is total). Confirmed 600/600.

## Per-finding verdicts

**F1 — "the record order is a strict subrelation of the causal order /
causal does strictly more constraining work": REGIME-DEPENDENT.**
The containment is not typing-enforced: `build_order_report` never consults
`causal_parents`, and regime-(iii) fixtures — record dependences between
causally-unrelated events — are type-legal and pass the T586 gate 200/200.
The containment is an **alignment discipline** the T586 fixture obeys by
hand: every required record's producer is also a declared causal ancestor of
its consumer. Given that discipline (regimes i–ii), containment is
guaranteed; **strictness** is then a second, independent condition — some
record-free causal edge escapes the record closure — which is generic
(193/200 regime-(ii) draws) but not universal: closure equality occurred in
7/200, rising with record density (0/64 at `p_rec` = 0.35, 2/66 at 0.60,
5/70 at 0.85), and holds identically in regime (i), confirming the
adversary's prediction as a construction-level fact. The three-event
shortcut demo shows equality is achievable with as few as three events and
one record-free edge.

**F2 — "a foliation adds nothing to the record order": TYPING-THEOREM
(upgraded).** L1 is a dataflow fact about the derivation, not a fixture
fact: the record closure factors through the record-typed projection of the
event structure, so any clock relabeling — hence any foliation overlay —
stabilizes it, for every fixture expressible in the type. The companion
claim "everything the foliation adds is unlicensed" is likewise a theorem
(L2) for any strict partial order and any linear extension; only the count 4
is fixture-specific (it equals the fixture's incomparable-pair count).
Overlay finding 1 and finding 2's structure are hereby upgraded from
fixture-facts to theorems; nothing about them depended on the five-event
fixture.

**F3 — "record+causal constraints underdetermine the foliation" and
"record-admissible ⊋ causally-admissible": SPLIT VERDICT.**
(a) The strict inclusion is REGIME-DEPENDENT and, by L3, **equivalent** to
F1's closure strictness — it is the same fact counted, not corroboration.
It vanishes identically in regime (i) (200/200, ratio exactly 1), holds in
exactly the closure-strict 193/200 of regime (ii), and in regime (iii) stops
being a containment at all: 200/200 fixtures have causally-admissible
foliations that violate the record order, and in 38/200 the inversion is
total (record closure ⊋ causal closure, so the record-admissible set is
strictly inside the causally-admissible set — record structure doing
strictly more constraining work, the mirror image of the T586 sentence; the
degeneracy ratio drops to 0.119 at its extreme).
(b) The *existence* of residual degeneracy after imposing both orders is a
THEOREM (L4) whenever the joint order leaves an incomparable pair — generic
across the family (566/600 fixtures).
(c) The *three-fold* value is an ARTIFACT of the five-event fixture: joint
extension counts across the family run from 1 (joint order total — the
degeneracy can vanish entirely, 34/600) to 35,280, median 22, with the
value 3 occurring in 24/600. "Derived by the fixture, not posited" survives
for the existence claim, with the multiplicity demoted to fixture data.

## Consequences for citability of the three headline findings

| Where it is stated | Current wording | Status after sweep | Earned wording |
|---|---|---|---|
| T586 audit `causal_overread_control`; T587 `causal_order_absorbs_record_order`; overlay finding 3 | "The supplied causal relation contains extra ordinary-causal edges not licensed by executable record dependence" / "Every T586 record-order edge is already causally ordered" / "Causal structure does strictly more constraining work than record structure in this fixture" | REGIME-DEPENDENT | "In causally-aligned fixtures (every required record's producer a causal ancestor of its consumer), the record closure is contained in the causal closure; the containment is strict exactly when some record-free causal edge escapes the record closure — generic in the sweep (193/200 regime-(ii) draws), failing in a density-dependent fraction (7/200 overall, rising to 5/70 at p_rec = 0.85) and identically in the record-saturated regime. The typing itself does not force alignment: record dependences without causal paths are type-legal, pass the T586 gate, and reverse the verdict — including 38/200 sweep fixtures where the record closure strictly contains the causal closure." |
| Overlay finding 1 (and its strengthening of T586's clock-label control) | "The foliation changes nothing… returns a closure identical to baseline" | TYPING-THEOREM (upgraded) | "Theorem (dead-input factorization): the record closure is a function of the record-typed projection (event id, produced records, required records, executable tasks) alone; every clock relabeling — hence every foliation overlay — leaves it invariant, for every fixture expressible in the type. The five-event computation is one instance of a structural fact." |
| Overlay finding 2 | "Everything the foliation adds is unlicensed… exactly the 4 pairs the record order leaves incomparable, all with no record basis" | TYPING-THEOREM (structure); ARTIFACT (the count 4) | "Theorem: for any strict partial order and any linear extension, the added comparabilities are exactly the incomparable pairs oriented by the extension — none has a basis in the underlying order. The count equals the fixture's incomparable-pair count (4 here)." |
| Overlay findings 3–4 (strict inclusion; three-fold degeneracy) | "5 respect the record order but only 3 the causal order… a three-fold degeneracy survives everything… derived by the fixture, not posited" | REGIME-DEPENDENT (inclusion, ⟺ F1 by L3); THEOREM (existence of degeneracy > 1 given an incomparable pair); ARTIFACT (the values 5, 3, 2, 3) | "The strict inclusion of record-admissible in causally-admissible foliations is equivalent to strictness of the closure containment (a counting shadow of F1, with the same regime map — it vanishes identically when every causal edge carries a record). Residual degeneracy > 1 is a theorem for any fixture whose joint order leaves an incomparable pair, and can vanish (joint order total). The specific multiplicities are fixture data." |
| T587 adjudication ("absorbed by… causal comparators") | "T586 has no relation-level residual beyond ordinary task-prerequisite dependency and is absorbed by the strongest standard dependency and causal comparators **on the frozen event system**" | REGIME-QUALIFIED (already scoped; the scope is now load-bearing) | Keep, with the qualifier made explicit when cited: "absorption is a property of causally-aligned fixtures; the typing admits fixtures where the causal comparator does not absorb the record order, so absorption should be cited as conditional on the alignment discipline, not as a property of the record-order construction itself." |

Two of the three headline findings therefore change citation class: F2
upgrades (fixture-fact → theorem), F1 and F3(a) get regime qualifiers and
lose independence from each other (one fact, stated twice). The overlay
note's own hedges ("in this fixture", "counts are fixture-specific") were
correctly placed; this sweep converts those hedges into a regime map with
the boundary located.

### Task-typing wrinkle (recorded for precision)

`record_dependency_edges` emits an edge only through the consumer's
`executable_tasks` loop: an event that requires a record but declares no
executable task contributes **no** record-order edge (demonstrated by the
two-event demo; the record still counts as produced, so nothing is flagged
missing). T586's phrase "executable task dependence on produced records" is
thus doubly typed — record issuance **and** task executability are both
load-bearing. Downstream wordings should say "task-dependence order," not
"record-consumption order."

## What This Does Not Claim

- **No physics generality.** This is formalism-internal robustness of a
  finite combinatorial construction. Nothing here is evidence about actual
  spacetime, causal sets, a substrate tick, preferred frames, or Lorentz
  structure; "regime (iii)" is a statement about what the typing permits,
  not about what physics realizes.
- **No new T-number, no claim movement.** T587's stop stands; no
  claim-ledger or Canon Index update is earned or proposed; the T586/T587
  verdicts are unchanged — this note only re-scopes how their findings may
  be cited.
- **No revival of T586's downgraded order claim.** If anything, L3 tightens
  the downgrade's logic: the foliation-counting corroboration was the
  subrelation fact restated, not independent support.
- **No adjudication of regime (iii)'s physical legitimacy.** Whether the
  source contract should outlaw record dependences without causal transport
  (an alignment axiom — "records travel causally") is a modeling decision
  for the record-issuance contract, flagged as open; this sweep only shows
  the current typing does not impose it.
- **No measure claim.** Sweep fractions (7/200, 193/200, 38/200, and the
  density-bin fractions) are relative to the pre-registered generator grid,
  not universal measures over fixture space. The theorem parts (L1–L4) do
  not depend on the grid; the fraction parts do.

## Uncertainties

- The generator draws forward-oriented DAGs with independent edges at fixed
  density grids; correlated or adversarially structured fixtures could sit
  differently in the fraction tables (not in the theorems).
- The regime taxonomy is defined at the direct-edge level; regime (ii)
  direct-strictness does not imply closure-strictness (that gap is exactly
  the 7/200), and a finer taxonomy could split regime (iii) by how much of
  the record order escapes the causal order (the sweep's coarse split:
  162/200 mutual non-containment, 38/200 full inversion).
- L1 is a dataflow theorem about the current `build_order_report`
  implementation; a future change to the derivation (e.g., consulting
  causal parents to filter record edges) would need the proof redone. The
  sweep would catch it: the model imports and executes the live derivation.

## Provenance

- Repo baseline at write time: `main` = `74e18ce`; writer lock
  `.git/capacityos-writer.lock` checked absent before writes. File writes
  only; no commits or pushes from this arm.
- This note and `models/fixture_family_sweep.py` were produced by execution
  arm E5 of the 2026-07-28 strategy-wave slate (fixture-family sweep
  mission), downstream of the program-adversary arm's finding that the
  fixture-derived results rest on one five-event fixture with two
  hand-declared causal-only edges.
- Predictions in §Pre-registered predictions were written before the model
  was first executed and were not edited afterward; the model's check table
  gates exit status on the theorem confirmations and the anchor/demo
  reproductions, not on the empirical fractions, so a failed prediction
  would have surfaced as a reported miss, not a crash.
- Run from the repository root:

```sh
python3 -m models.fixture_family_sweep
```

Deterministic: repeat runs produce byte-identical JSON (fixed literal seeds
58601/58602/58603/58610+counter; no clock, date, or filesystem-order
dependence).
