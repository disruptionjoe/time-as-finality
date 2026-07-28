# CM Swing 2 — Issuance from Redundancy: The SBS-Class Reproduction Test on the Frozen Fixture Family

**Status:** swing 2 of the commit-module series — issuance-from-redundancy
(Debt L1, repair route 2); review-only — no claim movement, no T-number, no
bin regrade, no guardrail edit, no posture change, and no tick-family credit
implied or banked. Deliverable: the redundancy repair route for CM's I is
executed against its registered kill on the frozen fixtures, and the kill's
adjudication is returned.
**Date:** 2026-07-28
**Fixed object:** [commit-module-schema-2026-07-28](commit-module-schema-2026-07-28.md)
was read in full and binds this note: the module's (I, G, D) statement (its
§1), the I↔D cycle analysis (its §2 — this swing is the I-end of the two
cycle-breaking routes; S4 owns the D-end), Debt L1 with its discharge and
conviction shapes (its §3), and the S2 adjudication protocol fixed there.
That protocol is confirmed as read and is applied verbatim below: **PASS** —
reproduction with no privileged-D input (the criterion's
decomposition-inputs quantified over the admissible class, order invariant
across it); **PARTIAL** — the kill fires scoped: reproduction succeeds only
given a declared D, so I becomes derived-conditional-on-D and the primitive
count transfers to S4 rather than dropping; **FAIL** — the kill fires
terminally for the redundancy route: no reproduction even D-conditionally,
and I stays a declared primitive.
**Model:**
[../models/redundancy_issuance_probe.py](../models/redundancy_issuance_probe.py)
(pure stdlib, deterministic — fixed literal seeds 61001/61002/61003 plus the
sweep's own 58601/58602 reused verbatim; JSON summary with an
expected/actual/match check table; all 26 gated checks match, exit 0, repeat
runs byte-identical; `python3 -m models.fixture_family_sweep` re-run after
this probe was added and still exits 0).
**Builds on (cited by pointer; nothing re-derived):**
[T587](../tests/T587-t586-causal-collapse-boundary-attack.md) /
[results](../results/T587-t586-causal-collapse-boundary-attack-v0.1-results.md)
(the supplied issuance typing — the reproduction target's right-hand side);
[T586](../tests/T586-record-capability-order-gate.md) /
[results](../results/T586-record-capability-order-gate-v0.1-results.md) and
[models/t586_record_capability_order_gate.py](../models/t586_record_capability_order_gate.py)
(the frozen fixture and the record order to reproduce);
[T585](../tests/T585-landauer-physical-capability-gate.md) (stability as a
certified task — the (c) flag);
[fixture-family-sweep-2026-07-28](fixture-family-sweep-2026-07-28.md) and
[models/fixture_family_sweep.py](../models/fixture_family_sweep.py) (the
causally-aligned regimes and generators, reused verbatim);
[rival-symmetry-swings-2026-07-28](rival-symmetry-swings-2026-07-28.md) §R1
(steelman route 2 — the redundancy route this swing executes);
[N10](../literature/N10-q1a-spectrum-broadcast-structure-absorber.md) (the
SBS / strong-quantum-Darwinism primary set: Korbicz–Horodecki–Horodecki
2014; Horodecki–Korbicz–Horodecki 2015; Brandão–Piani–Horodecki 2015;
Le & Olaya-Castro 2019; Korbicz 2021 review — sources verified there
2026-06-21; no new fetches needed, no formal condition missing for this
fixture class). Cross-repo pointers (their truth, not imported): HC-DU-063
and HC-DU-061, verified by reading — §6.
**Tags:** `research_note` · `review_only` · `swing_2` · `negative_result_scoped`

---

## The registered kill (verbatim, up front)

> **S2 kill:** "redundancy-issuance must reproduce the T586 record order on
> causally-aligned fixtures without consuming D."

Reproduction target, from L1's discharge shape: the seed → copy → erase →
certify chain (via `r_known_zero`, `r_copied_zero`, `r_erased_standard`)
with the biased-reference event incomparable, on causally-aligned fixtures,
from redundancy/grade structure alone. The sweep's regime qualification
binds: regimes (i) `RECORD=CAUSAL` and (ii) `RECORD⊊CAUSAL` are in scope;
the non-aligned regime (iii) sector is outside the series' carried scope
entry and is not run.

**Verdict, stated first: PARTIAL.** The kill fires scoped, on the
protocol's exact wording: reproduction succeeds only given a declared D —
specifically, only at decomposition choices that make the redundancy
condition degenerate (every issued variable a single-carrier variable), and
the induced order is **not** invariant across the admissible decomposition
class (the provenance-level coarse-graining breaks reproduction on the
frozen fixture itself, at every threshold). PASS's invariance clause fails
measurably; FAIL's no-reproduction clause fails measurably. I becomes
derived-conditional-on-D at best, and the primitive count transfers to S4.
Sections 1–5 are the evidence; §5 gives the exact scope.

## 1. The question and the coextension target

S2 asks whether an SBS / strong-quantum-Darwinism redundancy condition
(N10's primary set) supplies the physical condition that **coextends** with
T587's supplied issuance typing on TaF's frozen fixtures — reproduction,
not grounding. Coextension is tested at three levels:

1. **class level** — the eleven T587 boundary-input classes: the condition
   must admit exactly `physical_record_production` and
   `native_record_issuance_rule`;
2. **event level** — the frozen fixture's five events: the condition's
   issued-event set against the typing's admitted producers;
3. **order level** — the induced record order (edges from issued variables
   consumed by executable tasks, transitively closed) against the T586
   closure (6 pairs; `prepare_biased_reference` incomparable), then across
   the causally-aligned fixture family.

## 2. The operationalization, with its honesty flags

The SBS target (N10's absorber shape):
ρ_{S E₁…E_n} = Σ_i p_i |i⟩⟨i|_S ⊗ ρ_{E₁|i} ⊗ … ⊗ ρ_{E_n|i}, with
conditional fragment states mutually distinguishable
(ρ_{E_k|i} ρ_{E_k|j} = 0 for i ≠ j). The mechanism, not the vibe: a
**pointer variable** on the system whose value is **redundantly imprinted**
in multiple **environment fragments**, each **independently accessible**
by distinct observers **without mutual disturbance**, with **strong
independence** (no hidden inter-fragment correlation doing objectivity
work). Le & Olaya-Castro 2019: strong quantum Darwinism + strong
independence ⟺ SBS.

Fixture translation (T586's world: events, produced/required record tokens,
executable tasks, budgets):

> An event **issues** a record iff a declared discrete outcome variable of
> the event is (a) imprinted in ≥ R stable carrier tokens outside the
> source (fragment redundancy), (b) independently consumable by distinct
> downstream tasks without disturbing each other or the source
> (objectivity), and optionally (c) stable under the fixture's admissible
> operations over the declared horizon.

The decomposition inputs this consumes are declared, not hidden — they are
exactly D's two halves plus one provenance datum:

- **coarse-graining** (which tokens are carriers of one variable), varied
  over an admissible class of three: `token_level` (finest — each token its
  own variable), `event_level` (one variable per producing event), and
  `provenance_level` (event-level plus copy attribution: a token produced
  by a copy-type task is a carrier of the *source* token's variable,
  transitively — the SBS-honest reading, under which a copy proliferates an
  existing pointer variable rather than originating one);
- **fragment partition** (which carriers count as independently accessible
  fragments — N10's fragment-partition and observer-accessible-subset
  data), varied over finest / single-block / seeded random partitions, with
  R counting nonempty blocks;
- the copy-type attribution rule itself (task-label semantics), a supplied
  provenance datum.

**Honesty flags, declared before the results:**

- **F1 — (c) is grade content.** "Stable" has exactly two fixture
  expressions: *declared* (the token type's own word — the supplied
  typing's "stable," no independent content) or *certified* (T585's
  `certify_record_stability` task against a declared budget and horizon — a
  capability-contract test, i.e., G-vocabulary). The operationalization
  cannot state (c) without one of them. This is the I→G edge S1 found,
  reproduced here, not hidden; both variants are computed (§3.2).
- **F2 — the condition is split-relative by construction.** Pointer
  variable, carrier grouping, and fragment partition are D-inputs. This is
  carried openly under the supplied-split clause (§6, sentence 2) and is
  precisely what the split-stability probe (§4) adjudicates.
- **F3 — the fixture class cannot express actual redundancy non-trivially.**
  Every T586-class record is a single token with at most one consumer; the
  only native multi-carrier structure anywhere in the frozen fixture is the
  copy chain `r_known_zero` → `r_copied_zero`. So R ≥ 2 (the thing that
  makes SBS *SBS* rather than mere correlation) is expressible only through
  the coarse-graining declaration. Declared in advance as the trivialization
  horn: if reproduction holds only where redundancy is degenerate, that is
  a finding, not a success.
- **F4 — (b) does per-fixture work nowhere in the family.** The fixture
  semantics of `required_records` is non-destructive shared read, so
  independent non-disturbing consumability is a property of the token
  *type*, exhibited per-fixture only in the class screen (observer-private
  readout vs. shared-readable token). Strong independence (no hidden
  inter-fragment correlation) has no fixture expression at all: carrier
  tokens have no conditional-state structure to correlate. Recorded as an
  expressiveness bound, not silently dropped.
- **F5 — the class screen is a coextension-by-construction audit.** The
  eleven class profiles (discrete outcome? native carriers? non-disturbing
  multi-access?) are declared from T587's own reason lines, quoted in the
  probe's source. The screen checks that the redundancy condition on those
  profiles recovers the typing's verdicts — a consistency check against the
  typing's stated physical rationale, weaker than the fixture computations,
  which consume nothing from T587 but the target closure.

## 3. Results

All numbers from the single deterministic run of
`python3 -m models.redundancy_issuance_probe` (exit 0; all 26 gated checks
match; byte-identical on repeat).

### 3.1 Class screen (typing coextension)

At R = 1 the condition admits exactly
`{physical_record_production, native_record_issuance_rule}` — equal to
T587's live admitted set (imported from the running model, not re-typed):
the nine rejected classes fail on carrier existence (access change,
capability change, section choice, readout, intervention, bare feedback,
edge/defect variables, stochastic input: no stable consumable carrier of
the outcome is natively imprinted) or on discreteness (continuous flux: no
frozen packet). **At R = 2 the condition admits nothing** — even the two
admissible classes' exemplars natively imprint one carrier. Class-level
coextension holds exactly at the degenerate threshold and fails totally at
every actual-redundancy threshold.

### 3.2 The frozen T586 fixture (thirteen cells)

Target: the 6-pair T586 closure, `prepare_biased_reference` incomparable
(both confirmed in-probe from the live T586 model).

| cell (grouping · R · partition) | issued events | closure pairs | reproduces? |
|---|---|---:|:---:|
| token · R1 · finest | all five | 6 | **yes** |
| token · R1 · single-block | all five | 6 | **yes** |
| event · R1 · finest | all five | 6 | **yes** |
| event · R1 · single-block | all five | 6 | **yes** |
| token · R2 · any | none | 0 | no |
| event · R2 · any | none | 0 | no |
| provenance · R1 · finest or single-block | seed, erase, certify, biased — **copy is not an issuer** | 4 | no |
| provenance · R2 · finest | seed only | 2 | no |
| provenance · R2 · single-block | none | 0 | no |
| token · R1 · certified-stability variant of (c) | erase only | 1 | no |

Three structural facts, each gated:

1. **Reproduction occurs only in the four degenerate cells** (token/event
   grouping at R = 1), where every issued variable has exactly one carrier
   (`max_issued_carrier_count` = 1) — the redundancy scalar does no work,
   and the issued-event set is extensionally the producing-event set: the
   criterion has collapsed into "emits a stable consumable token," which is
   T587's own admissibility predicate restated in carrier vocabulary.
2. **The one non-degenerate coarse-graining breaks reproduction at every
   threshold — at the copy step.** Under the provenance-level grouping the
   fixture's only genuine redundancy appears (the seed's variable, carriers
   `{r_known_zero, r_copied_zero}`, R = 2) — and precisely there the
   SBS-honest attribution reclassifies `copy_known_record` as proliferation
   of the seed's variable rather than issuance of its own, deleting the
   `copy → erase` edge basis (the erase edge re-attaches to the seed) and
   losing 2 of the 6 closure pairs even at R = 1. The mechanism and the
   typing disagree exactly on the event that *creates* redundancy: T587
   types the copy as `physical_record_production` in its own right; SBS
   mechanics types it as broadcast. *(Post-landing cross-reference: S3's
   grade tables consume the other side of this disagreement — T586's
   typing as source-owned input, copy as producer with ω = 6.0 and its own
   closure row. Neither attribution is settled; S6 §6 seam 1 is the
   record.)*
3. **The certified form of (c) fails; the declared form is the typing.**
   Requiring in-fixture certification (T585's stability-as-task) issues
   only the erase output (closure 1 pair); requiring declared stability
   adds nothing the typing did not already supply. The (c) fork is
   grade-supplied either way — the I→G edge, exhibited.

### 3.3 The causally-aligned family (sweep generators, seeds verbatim)

200 fixtures per regime; regime-(ii) empty-record-closure count reproduced
the sweep's own 12/200, confirming the regenerated family is the sweep's
family. Per-regime rates:

| quantity | (i) RECORD=CAUSAL | (ii) RECORD⊊CAUSAL |
|---|---|---|
| R=1 reproduction, all three groupings | 200/200 each | 200/200 each |
| R=1 issued set = producing-event set (degeneracy identity) | 200/200 | 200/200 |
| R=1 issued set invariant under all partitions | 200/200 | 200/200 |
| provenance ≡ event grouping (plain family is copy-blind) | 200/200 | 200/200 |
| R=2 reproduction (event/provenance grouping) | 20/200 (all non-vacuous) | 31/200 (19 non-vacuous + 12 vacuous empty-closure) |
| R=2 reproduction (token grouping), non-vacuous | 0/200 | 0/200 |
| R=2 coverage of the record closure, min/median/max | 0 / 0.714 / 1 | 0 / 0.5 / 1 |
| fixtures with any multi-carrier variable (R≥2 expressible at all) | 172/200 | 128/200 |
| R=2 issued set flips: finest vs single-block partition | 172/200 | 128/200 |
| R=2 issued set flips: finest vs seeded partition | 123/200 | 90/200 |
| non-vacuous R=2 reproduction surviving the single-block partition | **0/200** | **0/200** |

Readings: at R = 1 reproduction is universal — and universally degenerate
(the issuance criterion is provably carrier-nonemptiness; the identity is
gated per fixture, not asserted). At R = 2 a minority reproduces
non-vacuously (exactly the fixtures where every record source happens to
have out-degree ≥ 2 under the event grouping) — and **every one of those
successes is split-borne**: under the single-block fragment partition, all
of them fail (0/400 survive). The R=2 fragility counts equal the
multi-carrier availability counts exactly: wherever redundancy is
expressible at all, the declared partition decides whether it fires.

One caveat the probe surfaces about the family itself: the plain sweep
generators emit no copy tasks, so provenance-level and event-level
groupings coincide 400/400 — the plain family cannot even express the
coarse-graining fragility the frozen fixture exhibits. Hence:

### 3.4 The copy-augmented subfamily (the frozen fixture's structure, at family scale)

60 regime-(ii) fixtures, one seeded copy event inserted into one record
edge each (causal alignment preserved; the T586 gate passes 60/60; the
reproduction target is each augmented fixture's own recomputed closure).
Results, all gated: token-level R1 reproduces 60/60; the copy event is an
issuer under the token grouping 60/60 and under the provenance grouping
0/60; provenance-level R1 reproduction **0/60** (the copy edge basis is
re-attributed in every fixture); issued-set difference between admissible
groupings 60/60; the origin variable is genuinely multi-carrier 60/60, and
its R=2 issuance flips under the fragment partition 60/60. A three-event
hand demo pins the minimal witness: same events, same records, same
consumption — the R=2 verdict and the reproduction flip on the declared
partition alone.

## 4. The "without consuming D" adjudication

Protocol: vicious — the split does the selecting and redundancy is
decoration; benign — redundancy does real selective work *given any*
declared split (split-stable selected set). Executed on both D axes:

- **Fragment-partition axis.** At R = 1 the issued set is
  partition-invariant everywhere (460/460 fixtures incl. augmented; also a
  two-line theorem: a nonempty carrier set has ≥ 1 nonempty block under
  every partition). At R ≥ 2 the issued set is partition-fragile on every
  fixture where redundancy is expressible at all (finest vs single-block
  flips 172+128/400 + 60/60 — exactly the multi-carrier counts), and no
  non-vacuous R=2 reproduction survives the single-block partition
  (0/400).
- **Coarse-graining axis.** At R = 1 the issued set is grouping-stable on
  the copy-free family (an artifact of the family's copy-blindness) and
  grouping-fragile wherever copy structure exists: the frozen fixture and
  60/60 augmented fixtures flip the copy event's issuer status and lose
  reproduction under the provenance grouping — at the *degenerate*
  threshold, before redundancy proper is even engaged.

Adjudication: **the consumption of D is vicious at every non-degenerate
configuration.** The redundancy scalar R adds selection only where the
declared split has already created carrier multiplicity, and the selection
it adds flips under admissible split changes; where the selected set is
split-stable (R = 1, token/event grouping) the redundancy condition is
extensionally the supplied typing and selects nothing the typing did not.
At no point does redundancy do split-robust selective work. The I↔D cycle
is therefore **not broken from this end**: per the fixed protocol sentence,
split-fragility = PARTIAL at best.

Two closing observations for the ledger, neither softening the verdict:

1. **The routes collapse toward each other.** The only way to make
   "broadcastability" non-vacuous on this fixture class is to price it —
   copyability within a declared budget/horizon (T585 prices erase and
   certify, not copy; a priced copy is a capability-contract quantity).
   That is G-vocabulary: pushed for content, repair route 2 (redundancy)
   degenerates into repair route 1 (threshold on G given D), carrying the
   same D-conditionality. The two S2 repair routes are not independent
   here.
2. **What the degenerate coextension still buys.** The R=1 identity is not
   nothing: it verifies mechanically that T587's typing is coextensive with
   *stable-consumable-carrier existence* — the qualitative precondition of
   the SBS mechanism (a carrier the environment can hold and distinct
   consumers can read without disturbance) — across the whole aligned
   family and the class screen. What it is not is a derivation: the
   quantitative content that makes redundancy a *condition* (R ≫ 1,
   independence, distinguishability) is exactly the part the fixture class
   cannot express non-trivially (F3, F4) and the part that, where
   expressible, contradicts the typing at the copy step.

## 5. Verdict: PARTIAL, per the registered protocol

- **Not PASS.** The PASS clause requires the criterion's
  decomposition-inputs quantified over the admissible class with the order
  invariant across it. Measured false: the provenance-level grouping — an
  admissible member, and the only mechanism-honest treatment of copies —
  breaks reproduction on the frozen fixture (4/6 pairs at R=1) and on
  60/60 augmented fixtures. A lawyered PASS on the R=1 token/event cells
  would relabel: the reproducing criterion there contains no redundancy
  (gated degeneracy identity), so what reproduces is the typing restated,
  and K-CM's discipline (a reduction must not be a relabeling) bars
  counting a restatement as a derivation.
- **Not FAIL.** The FAIL clause requires no reproduction even
  D-conditionally. Measured false: given the declared D (token- or
  event-level coarse-graining, any partition, R=1), reproduction is exact —
  frozen fixture 6/6 with the biased reference incomparable, and 200/200 in
  both causally-aligned regimes, all three groupings.
- **PARTIAL, exact scope.** Reproduction succeeds only given a declared D,
  so I becomes derived-conditional-on-D and the primitive count transfers
  to S4 — the protocol's own wording, landed literally: the reproducing
  D-choices are precisely the ones on which the redundancy condition
  degenerates to the supplied predicate. **L1 is discharged to this grade
  and no further:** the redundancy route yields a physical-condition
  *candidate* for the typing — stable-consumable-carrier existence,
  coextensive with T587's admitted classes and order-reproducing across
  the aligned family, conditional on a declared coarse-graining and
  partition — not a derivation of I from redundancy structure doing
  independent selective work. The typing's supplied status stands; what
  changed is that its physical content is now stated, tested, and priced
  (the price: D, transferred to S4).
- **Terminal branch: not fired, and not near.** K-CM's terminal branch
  needs S2 to fail both repair routes *and* S4's fallback to fail.
  This swing returns PARTIAL on route 2 with an explicit D-conditional
  reproducing form; route 1 (threshold on G given D) is untested by this
  swing and §4's observation 1 suggests it is where route 2's content was
  heading anyway.
- **Fixture-expressiveness qualifier, carried honestly.** The R≥2 failures
  are failures *on this fixture class*, whose records are single tokens
  with single consumers — the class cannot host SBS's discriminating
  structure (conditional fragment states, strong independence,
  distinguishability). This PARTIAL is "not established here, and the
  degenerate/fragile dichotomy is established here," not "SBS-issuance
  refuted." A genuine physical test of the redundancy route needs a richer
  frozen fixture family (multi-consumer, conditional-state, priced-copy) —
  a target for the series conclusion to weigh, not for this swing to
  build.

## 6. Boundary sentences (mandatory)

1. **The source question is not touched.** S2 tests a record-local
   reproduction claim on frozen TaF fixtures: whether an
   SBS/strong-Darwinism redundancy condition (N10's primary set), evaluated
   relative to the fixture's declared system/environment split, reproduces
   T587's supplied issuance typing — which boundary events are admitted as
   `physical_record_production` / `native_record_issuance_rule`. It does
   not adjudicate whether typed issuance is genuine source-side type
   creation versus bounded disclosure of a fixed richer source — that is
   PP-3/D-FORK (TI-C019, E026), owned by temporal-issuance and routed there
   by T588's fork handoff; a positive reproduction here would leave PP-3
   exactly as open as before — and this swing's PARTIAL leaves it more so.
2. **The supplied-split clause.** The redundancy criterion is evaluated
   **relative to** the fixture's declared split — consistent with
   dynamic-unity's banked no-go that a record cannot be an intrinsic state
   scalar (their HC-DU-063,
   `dynamic-unity#explorations/state-only-record-functional-no-go-and-minimum-typed-record-structure-2026-07-27.md`,
   pin `b190306`, **verified by reading the verdict and theorem sections at
   the pin**: the orbit-separation criterion and the two-bit
   same-spectrum witness make record-ness underivable from a bare invariant
   state scalar; a split-relative correlation functional becomes possible
   only once the algebra/factorization is part of the physical contract —
   "the extra algebra/factorization is doing essential physical work" —
   and their Stop binds this note's usage: a basis/split-dependent
   redundancy measure must not be passed off as representation-independent).
   Convergent support, same pin, likewise verified by reading: DU's
   autonomous-finality three-mechanism gate independently returned
   `NO_READY_MECHANISM` — the record interface remains *supplied* (their
   HC-DU-061,
   `dynamic-unity#explorations/autonomous-finality-three-mechanism-selection-gate-result-2026-07-27.md`;
   its passport rows mark threshold/partition and access ports as supplied
   across all three mechanism classes). This swing's split-fragility result
   is the same lesson landed on TaF's own fixtures: the split does
   selection work the redundancy scalar cannot replace.
3. **Dynamic-unity's STOP on foliation-existence testing is respected.**
   CM is the rival's component, priced under TaF's charter comparison;
   nothing here asserts or tests any foliation, update ordering, tick, or
   beable, and `NI-DU-87` remains dynamic-unity's truth, cited by pointer.

## What This Does Not Claim

- **No claim movement.** T583–T588, every claim, bin, canon tier,
  guardrail, and test status stay where their owners left them. The T586/
  T587 verdicts are unchanged; this note reproduces their fixtures, never
  regrades them.
- **No derivation of I.** The reproducing form is D-conditional and
  degenerate; nothing here converts T587's typing from supplied to
  derived. L1's discharge is partial exactly as stated in §5, and the
  transfer of the primitive count to S4 is a *debt movement on the rival's
  ledger*, not a resolution.
- **No refutation of the redundancy route as physics.** SBS and strong
  quantum Darwinism are untouched as physics; what failed here is their
  non-trivial expressibility on this finite classical-abstract fixture
  class plus the split-robustness of their fixture translation. The
  richer-fixture reopener is named in §5 and not prejudged.
- **No new physics, no priority.** The SBS conditions are their authors'
  (N10's primary set). The groupings, partitions, thresholds, and the
  probe are bookkeeping over the existing fixtures.
- **No tick-family credit.** A PARTIAL on the rival's module prices the
  rival's component; it revives nothing on the tick side and implies no
  symmetric credit anywhere.
- **No cross-repo movement.** HC-DU-063 and HC-DU-061 are cited as DU's
  truth at a pinned commit after direct verification; nothing is imported
  as TaF truth, and no DU surface is asked to change.
- **Scope is binding.** Causally-aligned regimes only; the non-aligned
  sector, horizon physics, sealed coherently controllable labs, and the
  unbounded agent class are all outside this swing per the schema's scope
  declarations.

## Provenance

- **Writer lock:** checked before each write —
  `git rev-parse --git-path capacityos-writer.lock` →
  `.git/capacityos-writer.lock`, not present (re-checked between the model
  write and this note). HEAD at read and write time: `1db0f6a` (the
  series' declared baseline). This arm performs file writes only — this
  note and `models/redundancy_issuance_probe.py`; no commit, no push.
- **Fixed object:** `explorations/commit-module-schema-2026-07-28.md` read
  in full before any design work; the S2 kill, its adjudication protocol,
  the I↔D cycle table, and boundary-sentence obligations bind this note as
  written there.
- **In-repo texts read for this note:** T586 test + results + model
  (fixture verbatim); T587 test + results + model (typing and boundary
  classes, imported live into the probe); T585 model (context, budget,
  certify task); fixture-family-sweep note + model (regime definitions,
  generators, seeds — reused verbatim, and the probe's regeneration
  cross-checks the sweep's own 12/200 empty-closure count);
  rival-symmetry-swings §R1 (steelman route 2); N10 in full (the SBS
  formal conditions used in §2 are all present there; no fetch needed).
- **Cross-repo verification:** both DU pointers read directly at pin
  `b190306` via `git show` in the dynamic-unity repo (current DU HEAD
  `f9a8568`; `git diff b190306..f9a8568` on both files is empty, so pin
  and head texts coincide). Read: HC-DU-063 head, §§2–5, stop/reopen;
  HC-DU-061 head, executive verdict, passport rows, admission decision.
- **Parallel-arm dependency (boundary sentence 2 of the schema), carried
  open:** the series' DU-holdings gate arm's report was **not present in
  this repository at write time** (searched explorations and run surfaces).
  Per the schema, S2 may not close ahead of it. Handling: this note's SBS
  usage is mechanism-template-only and its verdict is
  degenerate-or-fragile — no SBS/QD physics claim is treated as landed
  support for anything — and the two specific DU pointers used were
  verified by direct reading rather than via the gate arm. The series
  conclusion must still consult that arm's report before treating S2 as
  closed; this dependency is flagged, not discharged.
  *Resolution note (series close): the gate arm ran report-only; no report
  file will land in this repository — its GO/SEAM verdicts are recorded in
  the series' closeout mailbox note on the system-runtime surface, which
  is the consultable record this dependency names. S2 closes when that
  note is consulted; the mitigations above stand on their own.*
- **Determinism:** all probe randomness from literal seeds (sweep's
  58601/58602 reused for family regeneration; probe-local 61001/61002/61003
  for partitions and augmentation); repeat runs byte-identical; 26/26
  gated checks match, exit 0; empirical rates (R=2 reproduction, coverage,
  fragility fractions) are reported as measurements relative to the
  pre-registered generator grid, not gated and not universal measures.
