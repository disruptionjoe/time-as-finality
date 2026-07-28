# The Decomposition Debt (S4): What the Declared Split Does on the T58x Fixtures, and What It Costs

**Status:** swing 4 of the commit-module series — the decomposition debt
(Debt L3); review-only — no claim movement, no T-number, no bin regrade, no
guardrail edit, no posture change, and no tick-family credit implied or
banked. Deliverable: D (the system/environment split + record-variable
coarse-graining) is made explicit as a split object over the T58x fixture
class, its load-bearing work is inventoried, an exhaustive re-decomposition
sweep separates split-invariant from split-fragile structure, and the
fixture-level route-A question is adjudicated with the price stated.
**Date:** 2026-07-28
**The fixed object:** [commit-module-schema-2026-07-28.md](commit-module-schema-2026-07-28.md)
(S1) — binding here: D's status (**IMPLICIT** — fixture-declared in
T585/T586, never stated in prose; presupposed by I's "produced record"
token); Debt L3 (§3); route A as stated there (derive D from causal locality
+ einselection-stability); and S1's dependency graph (I→D definitional, G→D
parametric, D→G route-A-parametric, D→I route-B-only).
**Registered kill / fallback (verbatim, from the schema's Debt L3):**

> "if both derivation routes for D are circular, D is a declared priced
> primitive."

Series-tasking gloss, carried unchanged: if both derivation routes are
circular, D is a **declared priced primitive — priced, not fatal**. CM dies
at this debt only via K-CM's terminal branch (a declared D failing to make I
and G well-defined at all), which is not in play below.
**Hard rail (cross-repo, their truth, read directly before citing):**
dynamic-unity holds the banked **general** result that records cannot be
intrinsic state scalars and that minimum **typed** structure — a declared
subsystem/algebra split — is necessary:
`dynamic-unity#explorations/state-only-record-functional-no-go-and-minimum-typed-record-structure-2026-07-27.md`
(claim `HC-DU-063`; pin commit `b190306`, file verified present at that
commit; verdict section read directly for this note). Nothing below
re-proves, restates, or tests any general minimum-typing or decomposition
theorem — that is DU's truth, cited by pointer. TaF's contribution here is
strictly **fixture-local**: the price tag of D on the T58x machinery.
**Builds on (cited by pointer; nothing re-derived):**
[T585](../tests/T585-landauer-physical-capability-gate.md)
([model](../models/t585_landauer_physical_capability_gate.py) — the declared
memory-cell/bath/work-store context and the T584 third-class fields);
[T586](../tests/T586-record-capability-order-gate.md) /
[results](../results/T586-record-capability-order-gate-v0.1-results.md)
([model](../models/t586_record_capability_order_gate.py) — the fixture class
this swing re-splits);
[T587 results](../results/T587-t586-causal-collapse-boundary-attack-v0.1-results.md)
(the boundary-input screen rows consumed below);
[T583](../tests/T583-capability-contract-v1.md) /
[T584](../tests/T584-capability-invariance-morphism-gate.md) (declared
contexts; the three admissible morphism classes);
[rival-symmetry-swings-2026-07-28](rival-symmetry-swings-2026-07-28.md) (R3
exit (iii), point 3 — the quiet D-need; the cost column this swing proposes
to update);
[fixture-family-sweep-2026-07-28](fixture-family-sweep-2026-07-28.md) (the
dead-input method this probe reuses; the causally-aligned regime);
[covariant-formulability-capability-rate-2026-07-28](covariant-formulability-capability-rate-2026-07-28.md)
(the alignment law J⁻ — the causal-locality ingredient's covariant form);
[N7](../literature/N7-q1a-measurement-neighbors.md) (Zurek's
decoherence/einselection RMP on the source list — the predictability-sieve
shelf, cited at shelf depth only).
**Model:**
[../models/decomposition_sweep_probe.py](../models/decomposition_sweep_probe.py)
(pure stdlib, deterministic — **no randomness at all**: the re-split family
is enumerated exhaustively, so the fixture-family sweep's seeded generators
are not needed; no clock or date calls; prints a JSON summary with an
expected/actual/match check table; exit 0 — all 27 gated checks match;
repeat runs byte-identical).
**Tags:** `research_note` · `review_only` · `commit_module_series_s4`

---

## 1. The load-bearing-work inventory: every place D works in the fixture class

D never appears as a named object in the T58x chain, yet the chain reads it
everywhere. The inventory, from direct source inspection:

| # | where | what D supplies there | which half of D | what re-drawing the boundary would change |
|---|---|---|---|---|
| 1 | T585 context declaration (`source_system = one_bit_memory_erasure_with_thermal_bath_and_work_store`; `region_id = R_memory_cell`; `access_profile` bath/work-store rows; `resource_provenance = fixed_thermal_bath_and_work_store`) | the factorization: memory cell vs thermal bath vs work store, declared in prose and context fields | split half | what "dissipated into the environment" refers to — R3 exit (iii), point 3, instantiated in source |
| 2 | T585 record variable (`MemoryState.p_one`, the memory marginal) + `irrelevant_coarse_graining_fields = (display_label, sensor_serial, coordinate_name)` (T584's third class) | the record-variable coarse-graining | grouping half | every G-value: `landauer_work_units` reads the grouped variable's entropy — G→D parametric, S1's edge |
| 3 | T586 `produced_records` / `required_records` tuples per event | the record/environment typing of tokens | typing half | the record order's **edges**: `record_dependency_edges` emits an edge only through a record-typed consumed token |
| 4 | T586 issuance typing ("which events issue" = nonempty `produced_records` under D) | I's "produced record" token | typing half | which of the five events count as record-issuing — I→D, S1's definitional edge |
| 5 | T587 boundary screen, admissible rows ("A **stable produced record** with a unique producer…") | the record variable inside I's admissibility predicate | both halves | the screen's verdicts presuppose a declared D per S1 §2; not re-adjudicated here |
| 6 | T586 source checks (`t585_erasure_capability_nontrivial` consumes T585's known/max-entropy separation) | the grade structure the grouping induces | grouping half | a regrouped T585 (§2, groupings g0/g2) fails `landauer_costs_ordered` / `physical_capability_nontrivial`, so the T586 **verdict** is grouping-sensitive through its source gate even though the order computation itself never reads a grade (dataflow observation; the probe's grouping rows mirror exactly the checks that fail) |
| 7 | S3's target grades (commit(A, r) over these fixtures) | ω evaluated relative to split + grouping | grouping half | grade **values** move only with the grouping, never with the typing (§2, tested) — the S1 coordination point |

Summary of the inventory: the **typing half** of D carries the order and the
issuance typing; the **grouping half** carries the grades and the capability
separations; the **split half** (bath/work-store factorization) is consumed
as declared context by both. This is S1's "Both other components consume it"
made local and mechanical.

## 2. The re-decomposition sweep

### Design (all declared; exhaustive; no generators needed)

The split-neutral substrate is the frozen fixture's own event/consumption
structure: five events with causal parents, tasks, and presentation fields
exactly as in `_landauer_record_events`, plus a 13-token universe read off
the T585/T586 declarations — 5 carrier tokens (the declared records), 3
environment-imprint tokens (bath heat and work-store debit of the erase
step; the certify step's readout trace — T585's declared bath/work-store
context; T587's `observer_readout` row), 5 bookkeeping tokens (one per
event, from T585's declared irrelevant fields). The physical consumption
relation (copy reads `r_known_zero`; erase reads `r_copied_zero`; certify
reads `r_erased_standard`; nothing else has an in-fixture reader) is
dynamics, not typing, and is held fixed: a re-split re-draws the
record/environment boundary, never the interactions.

- **Typing splits:** any subset S of the 13 tokens declared "record";
  `CapabilityEvent`s are rebuilt with produced/required filtered by S and
  pushed through T586's **live** `build_order_report` (imported, not
  copied — the fixture-family sweep's discipline). A consumed token outside
  S is consumed as untyped physical input (T587's `physical_intervention`
  row licenses exactly this: a causal parent that is not an issued-record
  prerequisite). All 2^13 = 8192 typings are enumerated.
- **Groupings:** five declared record-variable coarse-grainings, graded
  against the T585 states (known 0.0 / biased 0.10 / max-entropy 0.50):
  g0 trivial-constant; g1 baseline bit; g2 bit ⊗ one imported
  declared-irrelevant label bit; g3 bit-label swap and g4 joule
  representation round-trip (T584 second- and first-class morphisms of g1).
- **Hand demos:** carrier **merge** (identify the copy output with the seed
  record — a literal coarser carrier grouping at the token level) and
  carrier **refine** (split `r_erased_standard` into a consumed value part
  and an unread flag part).

### Results (all from the probe's single deterministic run; exit 0)

| measurement | result |
|---|---|
| T586 gate (`strict_partial_order`) across all retypings | **8192/8192 pass** — the gate is split-permissive: it checks coherence *of* a declared split and never selects one |
| distinct record closures | **8**, in classes of exactly **1024** each — the closure is a function of S ∩ {consumed carriers} = S ∩ {`r_known_zero`, `r_copied_zero`, `r_erased_standard`} alone |
| closure law | 0 violations of: closure(S) = transitive closure of the **surviving consumption edges** — the fixture-level analogue of the sweep's dead-input lemma L1, for the typing direction |
| baseline (T586) closure reproduced | in exactly the **1024** splits containing the consumed core — regardless of how the other 10 tokens are typed |
| `prepare_biased_reference` incomparability | **8192/8192** — survives every re-split |
| closure isomorphism classes | **5** (empty; one-edge; 3-chain+2 isolated; two 2-chains+1 isolated; the baseline 4-chain+1 isolated) — demoting consumed carriers degrades the order through these, never non-monotonically |
| issuance typing (which events issue) | **32 distinct issuing-event sets** across the family — every on/off pattern of the five events is realizable by retyping alone |
| record count | ranges **0–13** across the family |
| G-values under retyping | **1 distinct grade table across all 8192 splits** — the typing is a dead input to grade evaluation |
| G-values under regrouping | **fragile**: g0 flattens all costs to 0; g2 shifts known/biased/max to 1.0/1.469/2.0 — both destroy the fixture's graded capability separation; g1 = g3 = g4 exactly (0.0/0.468995594/1.0) |
| grouping selection by the fixture's own checks (`landauer_costs_ordered` + budget separation at 0.75) | admits **exactly {g1, g3, g4}** — the T584 orbit of the baseline grouping — and rejects g0 (coarser) and g2 (finer-with-imported-entropy) |
| merge demo | **gate-rejected**: `ValueError: record produced twice: r_known_zero` — unique produced-record ownership forbids literal carrier merges; coarser carrier groupings enter the typing only as demotions, which the 8192-sweep covers |
| refine demo | **order-inert**: closure identical to baseline, gate passes, record count 5 → 6 — refinement that preserves the reading relation moves only the count and the issuance surface |

### Split-stability summary

**Invariant** across every admissible re-split that keeps the three consumed
carriers typed (2^10 = 1024 splits), and a fortiori across the route-A class
of §3: the record closure (exactly, not merely up to isomorphism), the
biased-reference incomparability, the gate verdict, and every G-value.
**Covariant, not invariant**, under demotion of consumed carriers: the
closure degrades lawfully as the transitive closure of surviving consumption
edges (8 closure classes, 5 isomorphism classes). **Fragile everywhere**:
the record count (0–13) and the issuance typing (32 issuing-set patterns) —
D's fingerprints sit on *which events issue* and *how many records exist*,
not on the order those records generate once typed. **The grouping half is
the grades' whole exposure**: G-values are dead to the typing half
(8192/8192) and live to the grouping half, where the fixture's own
capability checks reject the coarser and entropy-importing candidates and
leave exactly the T584 orbit.

**S1 coordination, tested.** S1's claim that G is "independent as a
definition, parametric in use" is **confirmed as refined**: the parametric
dependence localizes entirely in the grouping half (tested: g0/g2 move
values and break the separation checks), while the typing half is dead
(tested: one grade table across 8192 retypings). S1's I→D definitional edge
is confirmed and quantified: issuance typing varies over 32 patterns under
re-splits that leave the order untouched. S1's D→G route-A edge is
instantiated and adjudicated benign in §3. S1's D→I route-B edge is **not
expressible on this fixture** (no redundancy/fragment structure exists in
the T586 data) and stays S2-coupled.

## 3. Route A at fixture level

### The criterion the fixture can express

The schema's route A derives D from causal locality + einselection
stability. The fixture cannot state a continuum sieve functional; what it
can state is the **task-functional shadow** of that selection — and stating
it exposes exactly what it consumes:

- **C2 (completeness):** every stable carrier token consumed by a
  downstream executable task is a record.
- **C3 (grade-stability):** records are drawn from the stable, certifiable
  carriers (T585's `stable_record` certification against the declared
  budget and horizon — grade content, consumed openly). *(Granularity
  note: C3's "certifiable" is carrier-class certifiability against the
  declared budget and horizon; S2's certified-(c) variant demands an
  in-fixture certification execution per record. Not interchangeable —
  S6 §6, seam 3.)*
- **C1 (strict consumption, reported as a variant):** every record is
  consumed by a downstream executable task.
- **Alignment (the causal-locality ingredient):** every consumption edge
  lies inside the supplied causal order — **checked, not assumed** (it
  holds: the fixture is causally aligned, the sweep's regime (ii); in the
  covariant form this is the J⁻ alignment law, and non-aligned fixtures are
  outside covariant scope per the schema §1.v).

This is explicitly the fixture-expressible, discrete analogue of
predictability-sieve-type selection — einselection's standard
operationalization, in which splits and pointer variables are selected by
whether they support predictively useful, stable records (Zurek's
decoherence/einselection RMP, on N7's source list; the mechanism the
schema's route A names). The criterion admits a split by downstream task
use plus certified stability; the continuum sieve functional itself (least
entropy production / most retained predictive information over dynamics) is
**not expressible here and not worked** — a scope limit, stated. One
forward bridge is named at recalled depth, flagged, and **not load-bearing
anywhere in this note**: Still–Sivak–Bell–Crooks 2012 ("thermodynamics of
prediction," PRL 109, 120604 — dissipation as non-predictive memory), which
would connect the criterion's grade ingredient to predictive value if a
future arm works the continuum sieve; any load-bearing use must fetch it
first.

### What the criterion selects (measured, not argued)

- **C2 ∧ C3 admits exactly 4 of the 8192 typings:** {consumed core},
  {core + `r_biased_reference`}, {core + `r_erasure_certificate`}, and
  {core + both} = **the T586 declaration itself**, which is the class's
  unique maximal element. Every promotion of environment-imprint or
  bookkeeping tokens is excluded (C3); every demotion of a consumed carrier
  is excluded (C2).
- **Across the admissible class:** one closure class (the baseline order,
  exactly), one grade table, one gate verdict — and **4 distinct issuance
  typings** (the certify and prepare events flip between issuing and
  non-issuing). The residue is precisely the typing of the two **terminal**
  carriers — stable tokens with no in-fixture consumer.
- **C1 ∧ C2 pins a unique split** — the consumed core {`r_known_zero`,
  `r_copied_zero`, `r_erased_standard`} — at the price of denying record
  status to all terminal tokens *within the fixture's horizon*. The gap
  between the C1 answer (records must already be consumed) and the C3
  answer (records may await consumers beyond the declared
  `single_reset_cycle` horizon) is a **horizon convention**: a genuine,
  bounded conventionality at the fixture boundary, two bits wide here.
- **Grouping half:** the grade-structure-reproduction checks select exactly
  the T584 orbit {g1, g3, g4} (§2) — the grouping is derived up to T584's
  admissible first/second-class morphisms, with the third class (declared
  irrelevant fields) already contracted as irrelevant.

### The G↔D loop, adjudicated

The criterion consumes grade content (C3; the grouping selection), so the
D→G parametric edge S1 flagged is live here. It is **benign, as S1
argued**, for three fixture-checkable reasons: (i) the candidate family
(8192 typings × 5 groupings) is declared from substrate data with no
reference to the selected element; (ii) G is evaluated **per candidate**
from substrate state data plus that candidate — the selection is a filter
over a finite declared family, not a fixed-point definition, and
terminates trivially; (iii) under the sieve reading, selection *by* a
stability/grade functional is the intended mechanism, not an accident — the
edge is parametric exactly as S1's dependency graph has it, and no
definition is circular. The **vicious** candidate cycle (I↔D under double
derivation) is untouched: nothing in C1–C3 consumes the issuance typing I —
the criterion reads task/consumption structure and grade content only —
and no redundancy-over-fragments vocabulary (route B / S2's territory)
appears anywhere in the derivation.

### Route-A verdict (fixture-level)

**Route A succeeds at fixture level, up to a declared equivalence class.**
On the T58x fixtures, the answer to this swing's question — derivable,
conventional-but-constrained, or bare declared primitive — splits along D's
own two halves:

- **grouping half: DERIVED up to the T584 orbit** (grade-structure
  reproduction rejects coarser and finer-with-imported-entropy candidates);
- **typing half: DERIVED on the interior** (consumed carriers forced in,
  non-carriers forced out) **and CONVENTIONAL-BUT-CONSTRAINED at the
  fixture boundary** (terminal carriers: a two-bit horizon convention whose
  members are closure- and grade-indistinguishable and differ only in
  issuance typing).

Nowhere on this fixture class is D a bare primitive. **The registered
kill's firing condition — both derivation routes circular — is therefore
not met at fixture level, and the fallback does not fire.** Route B was not
and could not be run here (no fragment structure in the fixture data); the
kill **remains registered** for the continuum framing, where route A proper
(QFT factorization + einselection) is named-not-worked (§6) and route B's
fixed point is S2-coupled.

## 4. The price tag

Stated in the tasked either-way form; the landed branch is the first.

**Route A narrowed, so D costs "a stability criterion + the residual
equivalence-class choice."** Itemized, with what each item already costs
elsewhere on the module's ledger:

| # | price item | currency | new to the ledger? |
|---|---|---|---|
| 1 | the fixture's consumption/dynamics structure (which operations read which tokens) | arena (inherited dynamics — the causal layer plus standard physics) | no — the module's dynamics are declared INHERITED (schema §1.ii) |
| 2 | the declared T583 task context (task family, operation menu, budget, horizon) consumed by C2/C3 | declaration — bounded-agent-class relativity | no — already priced module-wide by the schema's scope element (§1.v: every grading is capability-indexed) |
| 3 | a grade-stability ingredient (stability certification / threshold) | G-content — the benign parametric loop of §3 | shared, not new — the same ingredient S2's threshold route and S3's commit(A, r) already carry |
| 4 | the residual equivalence-class choice: a T584-orbit representative (grouping) | convention — already contracted (T584's admissible morphism classes) | no |
| 5 | the residual equivalence-class choice: the terminal-record horizon convention (typing) | convention — **new, bounded**: it moves the issuance typing of 2/5 events and the record count, never an order edge, never a grade | **yes — this is D's only genuinely new fixture-level cost** |

**Against the foliation package's beables entry** (the R3-registered shape
comparison): the beables entry is paid in **ontology** — new physical
structure (a preferred foliation; a privileged set of variables) asserted
real and doing distinctive work. D's priced form claims no new structure:
it is a **selection scheme over standard descriptions**, relative to an
already-declared context, with one contracted orbit choice and one bounded
horizon convention. Lighter in the ontology currency (nothing new is
asserted to exist); nonzero in the declaration currency (context-relative
selection + the two conventions). The R3 finding that the two entries are
**shape-symmetric** (both are added selection structure) stands; what this
swing establishes is that they are **currency-asymmetric** at fixture
level.

**What the derived-up-to-equivalence exit buys:** the R3 exit-(iii)
posture's quiet D-need stops being a free-floating privileged choice and
inherits the module's existing context-relativity; and because the order
and the grades are invariant across the derived class, S2's reproduction
target and S3's grade target may quantify over the class instead of fixing
a member. **What it forecloses:** context-free record facts at the fixture
boundary — whether a terminal token is a record is a horizon-convention
fact, not a split-free fact. That residue is adjacent to R3's
value-absoluteness pressure and is flagged for S5's settlement, not worked
here.

**The unlanded branch, for symmetry (not fired):** had both routes been
circular, the disposition was the registered one — D a declared priced
primitive, a cost-column entry symmetric to R3's beables-shaped debt, with
the declaration buying well-defined I and G evaluations and foreclosing any
claim that the module adds no selection structure. That branch remains the
registered disposition **for the continuum framing only**, where it is
untested.

## 5. Proposed cost-column updates (proposed, not enacted)

Enactment belongs to the series settlement or the steward; this arm changes
no text outside its own two files.

**(a) [rival-symmetry-swings-2026-07-28.md](rival-symmetry-swings-2026-07-28.md),
"The rival's cost column," row 3 — proposed one-line append to the cost
entry:**

> — decomposition half priced by S4: on the T58x fixtures D is derived up
> to equivalence (T584 orbit + a terminal-record horizon convention) from
> consumption structure + the declared task context + a grade-stability
> criterion, so "privileged decomposition" re-prices to
> "declared-context-relative selection"
> ([commit-module-s4-decomposition-debt-2026-07-28.md](commit-module-s4-decomposition-debt-2026-07-28.md);
> continuum case named-not-worked).

**(b) The rival-map row (the earned-form blockquote in "What the rival map
now says," mirrored in goal2 §3 / VERDICT.md) — proposed one-line insertion
after clause (c):**

> , and (d) fixes the system/environment split and record coarse-graining
> (D) — at fixture level derived up to a declared equivalence class from
> already-priced ingredients rather than standing as an independent
> privileged structure (S4).

**Debt L3 disposition offered to the series ledger (not a ledger edit):**
PARTIAL — discharged at fixture level with priced residues (rows 4–5 of the
price table); the continuum halves of the schema's discharge shape
(factorization funded by causal locality; pointer basis by einselection
proper) remain named-not-worked, and route B's fixed point remains
S2-coupled. Under S1's own rule — "a PARTIAL on any swing prices the
component rather than the whole" — this prices D without closing L3
generally.

## 6. The DU rail, and the continuum boundary

**The rail, honored.** The general question — whether *any* record ontology
requires declared typed structure — is dynamic-unity's, answered there:
`HC-DU-063` (pin `b190306`) proves the state-only record-functional no-go
and the minimum-typing necessity consequence ("a nontrivial physical record
cannot be an intrinsic scalar property of an instantaneous state while also
being invariant under every global representation change"; typed
correlation records become possible only "after a subsystem/algebra is
fixed" — DU's verdict section, read directly for this note). Nothing here
re-proves or restates that result, and nothing here treats it as TaF's.
What this swing adds is orthogonal and fixture-local: **given** that some
typed split must be declared (DU's floor), the T58x machinery's particular
split is recoverable up to a declared equivalence class from ingredients
the module already pays for — which is exactly the shape DU's own
consequence section demands of any record-first structure ("derive or
independently justify that structure"), executed here at fixture scale
only. The dynamic-unity STOP on foliation-existence testing is respected
throughout: nothing in this note asserts or tests any foliation, tick, or
beable.

**The continuum/QFT version is named, not worked.** Route A proper — region
algebras funding the factorization, einselection deriving the pointer
basis, the sieve functional replacing C2/C3 — is continuum machinery this
fixture cannot express. The schema's memory-cited QFT-factorization caveat
(region algebras do not literally tensor-factor; split-property-level
approximation only) is **not consumed by this note**: no conclusion above
touches continuum factorization, so the caveat stays exactly as S1 left it
— flagged, memory-cited, not load-bearing. Binding forward: any arm that
attempts route A's continuum framing must first source that caveat to
primary algebraic-QFT literature or drop the tensor-factorization framing;
it may not be cited at memory depth in load-bearing position.

**Boundary sentences (schema §4, applied):** temporal-issuance owns the
source question — nothing here touches what physically sources issuance;
dynamic-unity owns broader record-integration — no SBS/QD import is made
here (the sieve is cited at shelf depth as the named mechanism of a
criterion this note states task-functionally), and S2 remains bound by the
DU-holdings gate arm for any such import.

## What This Does Not Claim

- **No claim movement, no T-number.** T583–T588, every claim, bin, canon
  tier, guardrail, and test status stay exactly where their owners left
  them. The probe is an exploration model, not a gate.
- **No general derivation of D.** The route-A success is fixture-local: a
  five-event Landauer fixture with a declared 13-token substrate. The
  continuum route (factorization + einselection + sieve) is named, not
  worked; the general minimum-typing question is DU's, cited by pointer;
  no physics generality is claimed for the selection criterion.
- **No closure of Debt L3.** The offered disposition is PARTIAL; the
  registered kill remains live for the continuum framing, and route B's
  circularity adjudication remains S2-coupled and unresolved.
- **No substrate innocence claim.** The 13-token universe and the
  consumption relation are read off the fixture's declarations; a
  different substrate presentation could shift the boundary between
  "dynamics" and "typing." The probe's claim is conditional on that
  declared substrate, and the substrate is printed in its JSON summary.
- **No issuance derivation.** Selecting which *tokens* are records given
  the consumption structure is not deriving which *events* issue records
  from physics — that is S2's Debt L1, untouched. The criterion here
  presupposes the fixture's task structure; it does not manufacture I.
- **No rival advantage, no tick-family credit.** Pricing D cheaper than
  beables in the ontology currency is a Goal-3 cost-column fact proposal,
  not a verdict movement; the tick side's adverse artifacts stand
  regardless.
- **Depth limits are binding.** The predictability sieve enters at N7
  shelf depth (named mechanism, no fine-grained sieve mathematics used);
  Still–Sivak–Bell–Crooks 2012 is named at recalled depth, flagged, and
  load-bearing nowhere; the QFT caveat is not consumed.

## Uncertainties

- **Substrate sensitivity.** The terminal-token residue is two bits *on
  this fixture*; richer fixtures (more terminal records, longer horizons)
  would widen the horizon convention, and nothing here bounds its growth
  rate. Whether the residue stays "bounded convention" or grows into a
  genuine conventionality problem at scale is open.
- **The environment-imprint tokens are modeled as reader-less.** That is
  faithful to the fixture (no task consumes bath microstate), but a fixture
  family with feedback from bath imprints (T587's `autonomous_feedback`
  row, with an explicit issuance rule) would put C3's carrier restriction
  under pressure; not tested.
- **The grouping family is five members, not a space.** g0–g4 witness the
  selection's behavior (coarser rejected, finer-with-imported-entropy
  rejected, T584 orbit admitted) but do not survey all groupings; a
  grouping that mixes carrier and bath degrees of freedom nonlinearly is
  not expressible in the current T585 state type and was not tested.
- **C2's maximality clause is a convention with a task-functional warrant**
  (T587's feedback-row language), not a theorem; a rival completeness
  convention (e.g., record status only for tokens consumed within k steps)
  would re-partition the admissible class, though it provably cannot change
  the closure or the grades on this fixture (both are class-invariant).
- **The probe tests the live `build_order_report`.** As with the sweep's
  L1, a future change to the derivation (e.g., consulting `causal_parents`
  to filter record edges) would need the closure-law claim re-proved; the
  probe would catch it by importing the changed code.

## Provenance

- **Writer lock:** checked before writes —
  `git rev-parse --git-path capacityos-writer.lock` →
  `.git/capacityos-writer.lock`, not present. HEAD at read time: `1db0f6a`
  (matches the series' declared baseline). This arm performs file writes
  only — this note and `models/decomposition_sweep_probe.py`; no commit, no
  push, no edits to any other file (the §5 updates are proposed, not
  enacted).
- **In-repo texts read in full for this note:**
  commit-module-schema-2026-07-28.md (the fixed object, fully, per
  tasking); models/t586_record_capability_order_gate.py;
  models/t585_landauer_physical_capability_gate.py;
  rival-symmetry-swings-2026-07-28.md (fully);
  fixture-family-sweep-2026-07-28.md (fully); T586 results; T587 results;
  T584 (setup/criteria); goal2-charter-verdict §3;
  models/fixture_family_sweep.py (header, generators, check-table
  structure); covariant note (alignment-law and β^μ sections, targeted).
- **Cross-repo read (rail compliance):**
  `dynamic-unity/explorations/state-only-record-functional-no-go-and-minimum-typed-record-structure-2026-07-27.md`
  — executive-verdict and consequence sections read directly; file
  presence verified at pin commit `b190306` via
  `git cat-file -e`. Cited by pointer as DU's truth; nothing imported as
  TaF's.
- **No fetches this run.** The predictability sieve is cited at N7 shelf
  depth (Zurek RMP quant-ph/0105127 on N7's primary-source list; mechanism
  named by the schema's route A). Still–Sivak–Bell–Crooks 2012 (PRL 109,
  120604) is memory-cited at recalled depth, flagged inline, and
  load-bearing nowhere. The schema's QFT split-property caveat is carried
  unconsumed at its original memory-cited flag.
- **Determinism:** `python3 -m models.decomposition_sweep_probe` from the
  repository root; exhaustive enumeration (no randomness, no seeds); exit
  0 with all 27 gated checks matching; repeat runs verified byte-identical
  before this note was written.
- **Series coordination:** S1's dependency graph and D-status are
  consumed as the fixed object. No sibling swing output existed when this
  arm started; the S3 note and the S2/S3 probe models appeared in the
  working tree mid-run and are **not consumed** here (checked only for
  contradiction: S3 explicitly defers D's disposition to S4 — consistent).
  The mid-run series-gate enrichment (sieve anchoring) is folded into §3
  at the stated depths.
