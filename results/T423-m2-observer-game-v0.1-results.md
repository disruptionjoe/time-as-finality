# T423 - M2 Observer-Game / Judgment-Aggregation Finality Probe (Route B) - v0.1 results

> Recorded-tier exploratory big-swing. `TESTS.md` and `CLAIM-LEDGER.md` are
> UNTOUCHED; the T-number lives only in this header / the spec header. NO claim
> promotion; ledger actions pause for Joe. Cross-domain material (social choice,
> judgment aggregation, cooperative game theory) is the OBJECT OF STUDY, never
> evidence for physics or a sibling repo. ONE-WAY RULE holds: GU / TI /
> ai-epistemology are vocabulary and template only; the only code import is
> TaF-native T413. Committed as recorded-tier in `68f814b`; no claim promotion,
> `TESTS.md`, or `CLAIM-LEDGER.md` movement is earned.

- Spec (frozen first): `tests/T423-m2-observer-game.md`
- Model: `models/m2_observer_game.py`
- Tests: `tests/test_m2_observer_game.py` (18 asserts, all pass, ~0.2 s)
- Run: `python -m pytest tests/test_m2_observer_game.py -q`

## Verdict: REDESIGN (on the canonicity axis) -- the M2 load-bearing move did NOT beat T422

**The honest bottom line.** M2's whole reason for existing was the **canonicity
lift**: show a single finite finality datum computed -- to the same value -- by
**two independent descriptions**, so that "two categories agree" clears the
category-relativity ceiling that capped T422. That specific move **did not land.**
The same-number agreement `d(N) = omega = 1` is **shared-primitive and
category-relative**: the coalition-lattice gap game `v_gap(S)` is literally equal
to the proposition-lattice `dilemma_indicator(S)` as a set function over all 8
coalitions, so the "two descriptions" are **one majority object read twice**, not
two independent measurement channels. The predeclared kill for this exact case
(from the M2 prep note: *"the object is only computable in one hand-picked
category (category-relative, as T422) -> REDESIGN"*) **FIRES.** So on the axis M2
was built to move, the verdict is **REDESIGN**, not GO.

**What this is NOT: it is not ABANDON.** The dilemma is a genuine List-Pettit
obstruction (not engineered / not a tie artifact); the Aumann-Shapley value
genuinely IS the T413 SURVIVES-R1 separator (not a relabeled Shapley routine, not
two hand-set numbers); the one-way rule holds (only TaF-native T413 imported); and
the **finality-specific** cross-application (the no-local-witness / non-atomic /
discursive-dilemma framing) is **not pre-empted** in the literature. So a real,
falsifiable, synthesis-tier object survives -- the finite witness that TaF's
SURVIVES-R1 grand-dividend is realized as a concrete doctrinal paradox, with a
definite magnitude-decoupling disanalogy and a working consistency-relaxation
falsifier. That earns; the **canonical two-category coincidence does not.**

Net: **REDESIGN** -- keep the finite witness and the cross-application; rebuild the
canonicity leg around a description that does **not** reduce to the shared majority
primitive (a genuinely different measurement channel), or record honestly that the
finality datum is finite-witnessed but **not** yet computed canonically.

| leg | result |
| --- | --- |
| S1 genuine discursive dilemma (K2 guard) | PASS |
| S2 global-no-local (v_gap = u_N, SURVIVES-R1) | PASS (atomic k=1 only) |
| S3 Aumann-Shapley IS the separator (= T413 datum) | PASS |
| S4 canonicity (the M2 load-bearing move) | **FAILS -> REDESIGN** (category-relative, shared-primitive) |
| S5 falsifiers stated and behave | PASS |
| K1 T422 recurrence | **FIRES** (category-relativity recurs; canonicity not cleared) |
| K2 / K3 / K4 / K5 kills | none fired |

## S1 - the dilemma is genuine (with numbers)

Frozen profile `p=(1,1,0)`, `q=(1,0,1)`, `r_i = p_i&q_i = (1,0,0)`. Every
individual judgment obeys the doctrine (`judges_consistent = True`). The
collective majorities: `maj-p = 1` (judges 1,2), `maj-q = 1` (judges 1,3),
`maj-r = 0` (only judge 1). Premise-based verdict `P(N) = 1&1 = 1` (ACCEPT r);
conclusion-based verdict `C(N) = maj-r = 0` (REJECT r). The collective set
`{p:1, q:1, r:0}` violates `r = p&q`. Not a tie artifact: p and q each carry a
strict 2/3 majority. **This is a real List-Pettit discursive dilemma.**

## S2 - global-no-local (the collective verdict lives in NO proper subset)

The gap game over the 8 coalitions:

| coalition | P | C | v_gap |
| --- | --- | --- | --- |
| {} , {2}, {3}, {1,2}, {1,3}, {2,3} | 0 | 0 | 0 |
| {1} | 1 | 1 | 0 |
| **{1,2,3}** | **1** | **0** | **1** |

`v_gap` is **exactly the unanimity game u_N**: Mobius dividends = `{ {1,2,3}: 1 }`
(0 on every proper coalition). Exhaustive scan: `dilemma_indicator = 0` on all 7
proper subsets, `= 1` only on N. `joint_record_completion_verdict(v_gap, 0)`:
`min_sep_coalition = {1,2,3}`, `datum_in_proper_subset = False`, **verdict =
SURVIVES-R1**. The collective verdict is reconstructible from **no proper subset**
of individual judgments -- the genuine "global datum present in the whole and in
no proper subset."

## S3 - the Aumann-Shapley value IS the finality separator

`shapley_by_dividends == shapley_by_permutations = (1/3, 1/3, 1/3)` (Leg-1
cross-check), symmetric and efficient. `d(N) = 1` **IS T413 Pair-2's
grand-coalition SURVIVES-R1 datum** -- the same grand-dividend object, not a fresh
number (the gap game realizes T413's efficiency-axiom R1 object as a concrete
discursive dilemma). K3 does not fire: the value is grand-concentrated and
survives R1.

**Aumann-Shapley trend (k copies of each judge-type).** Delta = `v_gap(N) = 1` is
preserved on the grand coalition at every k; individual pivotality dilutes:

| k | n | v_gap(N)=Delta | phi(type-1) | phi(type-2,3) | naive 1/(kn) | global-no-local? |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 3 | 1 | 1/3 | 1/3 | 1/3 | **yes** |
| 2 | 6 | 1 | 7/30 | 2/15 | 1/6 | no |
| 3 | 9 | 1 | 53/315 | 26/315 | 1/9 | no |

**Honest finding (recorded, inside the ceiling):** the strict "no proper subset
reconstructs" property is an **atomic (k=1) knife-edge**, not a property of the
non-atomic limit. For k>=2 a one-of-each-type size-3 sub-coalition reproduces the
original dilemma exactly, so `min_dilemma_coalition_size = 3 < n` and
global-no-local FAILS. What the replication limit preserves is Delta = 1 (total)
with vanishing individual atoms -- the Aumann-Shapley dilution -- **not** the
no-local-witness property. The shares also do not hit the naive `1/(kn)`
(because the game is no longer u_N once proper subsets carry the datum). This is
a genuine caveat on the "value carries the global datum in the non-atomic limit"
story and is reported rather than buried.

## S4 - canonicity: TESTED, and DEMOTED (the T422-relevant leg)

**(a) Localization agreement -- holds, but is shared-primitive (K1-partial).**
The gap-dividend support is `{ {1,2,3} }`. An **independent** obstruction measure
`omega`, computed on the PROPOSITION lattice (not the coalition lattice) as the
number of minimally-inconsistent subsets of the collective's endorsed literals
`{p, q, ~r}`, equals **1** -- the single minimal inconsistent set is the whole
`{p, q, ~r}`. So `omega = 1 = d(N)`. BUT on consistent judges `v_gap ==
dilemma_indicator` as set functions (verified over all 8 coalitions): the two
descriptions share the same majority primitive. Per T413 Leg 8 (Shapley is linear
in v => exact Shapley agreement <=> same induced game), this agreement is
**shared-primitive, and does NOT by itself escape T422's category-relativity**.
K1 fires as PARTIAL. This is logged, not spun.

**(b) Doctrine-family co-variation -- adds independent signal.** Varying the
doctrine on the SAME frozen p,q columns, comparing the SURVIVES-R1 separator
verdict against the proposition-lattice `omega`:

| doctrine | r column | raw d(N) | JRC verdict | separator | omega | agree? |
| --- | --- | --- | --- | --- | --- | --- |
| AND | (1,0,0) | 1 | SURVIVES-R1 | 1 | 1 | yes |
| OR | (1,1,1) | 1 | **ABSORBED** | 0 | 0 | yes |
| DICT (r=p) | (1,1,0) | 0 | no-separation | 0 | 0 | yes |
| NOCONN | (0,0,0) | 0 | no-separation | 0 | 0 | yes |

The separator and `omega` **co-vary and agree across the whole family** (vector
`[1,0,0,0]`, genuinely varying), without any re-tuning; a guard-the-guard test
confirms a fabricated disagreement would be caught. **Note the OR row is the
honest subtlety:** OR's raw grand Mobius dividend is 1, but the gap game is
`-u_{2,3} + u_N` -- ABSORBED at the proper coalition {2,3} (a tie-rule artifact),
NOT a global-no-local separator. This is exactly why the family is compared via
the SURVIVES-R1 absorption test, not raw d(N); using the correct separator test,
OR gives 0 and matches omega = 0. Only AND yields a genuine global-no-local
separator.

**(c) Magnitude decoupling -- the falsifiable teeth.** The premise game
`v_prem(S) = P(S)` gives dividends `{ {1}:1, {1,2}:-1, {1,3}:-1, {1,2,3}:2 }`, so
`d(N)_prem = 2 != 1` and `phi_prem = (2/3, 1/6, 1/6) != (1/3,1/3,1/3)`. A third
natural reading of the SAME situation computes a DIFFERENT datum. This proves the
gap<->omega agreement at 1 is **not** "everything computes the same number by
construction" -- it is a nontrivial coincidence of two specific readings, with a
third reading demonstrably disagreeing. The two readings are **not identical by
construction** (this is the K4-avoidance leg: where equality is claimed the
numbers match; where they are different objects they differ).

**Honest canonicity verdict.** Two independent descriptions (coalition-lattice
Shapley d(N); proposition-lattice MI-set omega) DO compute the same datum `1` on
the AND model, and co-vary across the doctrine family. But the equality is
**shared-primitive** (both read the same majority verdicts), so it does **not**
clear the canonical/category-free bar T422 set. The genuine, falsifiable content
is the **magnitude-decoupling disanalogy** (premise reading = 2 with asymmetric
shares). Because the same-datum equality is **category-relative** (one primitive
read twice, not two channels), the predeclared **REDESIGN** kill fires on this
leg: canonicity is **not achieved**. The finite witness and the cross-application
survive at synthesis tier; the canonical two-category coincidence does not.

## S5 - falsifiers (stated; behavior verified)

- **Consistency relaxation decouples the routes.** Set `r = (0,0,0)` (judges
  individually INCONSISTENT: `judges_consistent = False`). The collective set is
  still inconsistent and `omega = 1`, yet the gap game is now **ABSORBED**
  (`jrc_verdict != SURVIVES-R1`): there is no genuine global-no-local separator.
  So the omega<->separator agreement is a **regime fact** (holds only for
  consistent judges), not an identity. Falsifier behaves.
- **A proper subset reconstructing the dilemma** would kill global-no-local:
  scanned exhaustively at k=1, does not trigger (`dilemma_only_on_grand = True`).
  It DOES trigger under replication (k>=2), reported above as the atomic
  knife-edge caveat.
- **Doctrine-family disagreement** would kill co-variation: does not trigger.

## Kill-leg audit

- **K1 (T422 recurrence)** -- **fires as PARTIAL**, exactly as pre-flagged: the
  localization agreement is shared-primitive, so canonicity DEMOTES rather than
  clears. Not an ABANDON; the magnitude teeth + co-variation keep it a genuine
  synthesis-tier cross-application.
- **K2 (engineered dilemma)** -- does not fire: judges verified consistent; p,q
  carry strict majorities (no tie artifact).
- **K3 (value not the separator)** -- does not fire: d(N)=1 is grand-concentrated
  and SURVIVES-R1. (Contrast the OR control, which correctly ABSORBS.)
- **K4 (different data under same identification)** -- does not fire as an
  ABANDON: where equality is claimed (gap d(N) vs omega) the numbers match; the
  premise reading is a DIFFERENT object and is honestly reported as differing.
- **K5 (sibling load-bearing)** -- does not fire: the only import is TaF-native
  T413; ai-epistemology / TI / GU are vocabulary only.
- **K6 (prior art)** -- pre-conceded. The individual ingredients are established:
  List-Pettit discursive dilemma / doctrinal paradox (List & Pettit 2002); Shapley
  value of a simple/voting game as pivotality (Shapley-Shubik); Harsanyi
  dividends and interaction/Mobius indices (Grabisch-Owen-Roubens). The novelty is
  confined to the **finality cross-application** -- realizing T413's SURVIVES-R1
  grand-dividend as a concrete discursive dilemma, with the magnitude-decoupling
  disanalogy -- which is synthesis-tier, not a new general theorem.

## Steering-risk self-audit

The claim was framed by the orchestrating persona, so "engineer the two
descriptions to coincide" was the live risk. The structural guard that is NOT
under the toy's control: T413 Leg 8 (Shapley linear in v) forces exact Shapley
agreement to mean "same induced game" -- so any clean same-number canonicity is
claiming what the linearity lemma forbids. The build predicts and discloses this
(the demotion is the honest output), rather than hiding it. The one genuinely
independent, non-shared-primitive signal (the magnitude decoupling: premise
reading = 2, asymmetric shares) is the falsifiable residue that survives the
audit. The doctrine-family co-variation is real but still majority-primitive
driven; it strengthens, it does not escape.

## Adversarial audit -- six independent probes (did the kill FIRE?)

Six independent adversarial passes were run against the artifact. Their verdicts,
and whether each maps to a kill that FIRED:

| # | attack | verdict | kill fired? |
| --- | --- | --- | --- |
| 1 | **category-relative**: is `d(N) = omega` two independent computations or a shared-primitive identification true only in a chosen category (the T422 ceiling)? | **BREAKS** (conf 0.85) | **YES -- the decisive kill.** `v_gap(S) == dilemma_indicator(S)` on all 8 coalitions; both `omega` and the SURVIVES-R1 separator are functions of the SAME grand-majority triple; off the frozen fixture (collective triple (0,0,1)) the functions diverge (omega=2, indicator=1). One majority object read two ways -> **category-relative -> REDESIGN.** |
| 2 | **dilemma-genuine**: reconstruct the collective verdict from a proper subset; is the discursive dilemma real or engineered? | **SURVIVES** (conf 0.86) | no. Canonical doctrinal paradox, judges individually consistent, p and q carry strict 2/3 majorities; no proper subset forces the collective triple (1,1,0); over all 64 AND-consistent profiles "localized" is coextensive with "genuine grand-dilemma" (6/6). Discloses the atomic k=1 knife-edge. |
| 3 | **shapley-is-separator**: does the Aumann-Shapley value actually equal the T413 finality separator, or is it forced? | **SURVIVES** (conf 0.87) | no. Two independent Shapley routines agree; the separator routine contains no Shapley reference (not a relabel); `sum(phi)=v(N)=d(N)=1` is the efficiency axiom on a structurally-forced `u_N`, not two tuned numbers; a rigged `u_12` decouples location (Shapley still sums to 1 but separator flips to ABSORBED). |
| 4 | **one-way-violation**: is any GU / TI / ai-epistemology / architecture-of-legitimacy sibling RESULT load-bearing as evidence? | **SURVIVES** (conf 0.90) | no. Static + runtime import audits clean: only stdlib + TaF-native `models.legitimacy_shapley_finality_probe` (T413) loaded; siblings appear only in ONE-WAY-RULE disclaimer headers. K5 correctly does not fire. |
| 5 | **prior-art**: is "(Aumann-)Shapley value = judgment-aggregation obstruction" already in the literature? | **PARTIAL** (conf 0.70) | partial. The **generic** "Shapley value of an MI-set/inconsistency measure" connection is **pre-empted** (Livshits & Kimelfeld, arXiv:2009.13819, Shapley value of inconsistency measures for functional dependencies). The **finality-specific** cross-application -- discursive-dilemma + gap-game value + no-local-witness / non-atomic-legitimacy framing -- is **NOT** pre-empted (~7 targeted searches, ingredients appear separately, never joined). |
| 6 | **correctness**: fresh independent recomputation (not importing their code) of every number. | **SURVIVES** (conf 0.90) | no. 18/18 pass; independent recompute matches exactly (R=(1,0,0), v_gap=u_N, phi=(1/3,1/3,1/3), omega=1=d(N), premise d(N)=2 phi=(2/3,1/6,1/6), doctrine family AND/OR/DICT/NOCONN, AS trend). The decisive honesty check `v_gap(S)==dilemma_indicator(S)` reproduces -- substantiating the demotion. Minor: NOCONN omega hardcoded 0 (disclosed). |

**Reading of the audit.** Five of six probes leave the surviving object intact --
the dilemma is genuine, the value IS the separator, no sibling result is
load-bearing, the arithmetic is correct, and the finality-specific cross-application
is un-pre-empted. **The one that BREAKS is the one M2 was built to win**: canonicity
/ category-independence. That is dispositive for the GO/REDESIGN/ABANDON call.

## Recommendation: REDESIGN

- **NOT GO.** GO required the finality datum to be computed **canonically by two
  independent descriptions**, beating T422. Attack 1 breaks exactly there: the two
  descriptions collapse to one shared majority primitive, so the agreement is
  category-relative -- the T422 ceiling **recurs**. The load-bearing move did not
  land.
- **NOT ABANDON.** The descriptions do not compute *different* data on the fixture
  (they agree at 1), the dilemma is not fake (attack 2 survives), and the
  finality-specific cross-application is not pre-empted (attack 5 partial). So this
  is not a coincidence-collapse or a prior-art kill.
- **REDESIGN is the honest call.** What survives and should be kept: the finite
  (n=3), exact-arithmetic witness that TaF's SURVIVES-R1 grand-dividend finality
  datum is realized as a genuine List-Pettit discursive dilemma, with Aumann-Shapley
  value `(1/3,1/3,1/3)`, `d(N)=1` IS the separator, a falsifiable
  magnitude-decoupling disanalogy, and a working consistency-relaxation falsifier.
  What must be rebuilt to ever reach GO: a **second description that does not reduce
  to the coalition-majority primitive** -- a genuinely independent measurement
  channel (e.g. a topological/`H^1` index that is not a set-function relabel of the
  majority verdict, the Route-A bonus that was optional here). Absent that, the
  canonical claim cannot clear category-relativity, and the finality datum stands as
  **finite-witnessed but not canonically computed.**

Recorded-tier; no claim promotion; ledger actions and any REDESIGN swing pause for
Joe.

## What this earns / does not earn

**Earns (recorded, synthesis tier, method not evidence):** a finite (n=3),
fully-enumerated, exact-arithmetic witness that TaF's SURVIVES-R1 grand-dividend
finality datum is realized as a genuine List-Pettit discursive dilemma; its
Aumann-Shapley value `(1/3,1/3,1/3)` with `d(N)=1` IS that separator; an
independent proposition-lattice obstruction computes the same `1` and co-varies
across a doctrine family; and a falsifiable magnitude-decoupling disanalogy with
a definite consistency-relaxation falsifier.

**Does not earn:** clean category-free canonicity (**REDESIGN** -- the localization
agreement is shared-primitive / category-relative, K1 fires; the T422 ceiling
recurs on the one axis M2 was built to move); any universal theorem; any claim
promotion; any cross-repo evidential use; any physics or governance claim. The
strict global-no-local property is an atomic knife-edge that the non-atomic limit
does not preserve (honest caveat). Pauses for Joe.
