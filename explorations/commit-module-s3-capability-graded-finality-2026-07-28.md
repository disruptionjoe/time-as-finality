# Capability-Graded Finality: commit(A, r) — Commit-Module Swing S3

**Status:** swing 3 of the commit-module series — the capability-graded
finality pass; owner of Debt L2 in the series schema
([commit-module-schema-2026-07-28.md](commit-module-schema-2026-07-28.md) §3);
review-only — no claim movement, no T-number, no bin regrade, no guardrail
edit, no posture change, and no tick-family credit implied or banked.
Deliverable: the rival's R2 debt ("commit is FAPP-grade") converted from an
unpriced apology into a theory — finality as a **capability-indexed grade**,
defined on the T585/T586 fixture class, executed, and run through the
pre-registered checks.
**Date:** 2026-07-28
**The fixed object:** the S1 schema binds throughout — G's independent
statement (reversal cost defined with zero record vocabulary — the cycle
breaker), the (I, G, D) decomposition, Debt L2's discharge clauses (a)–(c),
and the series end-states. Nothing in S1 is re-derived or moved.
**Model:**
[../models/capability_graded_finality_probe.py](../models/capability_graded_finality_probe.py)
(pure stdlib, deterministic — byte-identical output across repeat runs, no
randomness and no wall-clock values in the output; exit 0; all 16 checks
pass, with the must-fail control passing by failing closed; run with
`python3 -m models.capability_graded_finality_probe` from the repository
root; T585 and T586 are re-executed at run time as source-owned inputs, and
the record order is consumed from T586's own closure, never restated).
**Builds on (cited by pointer; nothing re-derived):**
[T583](../tests/T583-capability-contract-v1.md) /
[model](../models/t583_capability_contract_v1.py) (the envelope: budgets,
tasks, access, native Pareto comparison, completion vocabulary);
[T584](../tests/T584-capability-invariance-morphism-gate.md) (the admissible
morphism classes and the task-merge counterexample boundary);
[T585](../tests/T585-landauer-physical-capability-gate.md) /
[model](../models/t585_landauer_physical_capability_gate.py) (the one-bit
Landauer fixture; normalized kBT ln 2 units; the blind worst-case accounting);
[T586](../tests/T586-record-capability-order-gate.md) /
[model](../models/t586_record_capability_order_gate.py) (the record order and
its unique-producer dependency closure);
[rival-symmetry-swings-2026-07-28.md](rival-symmetry-swings-2026-07-28.md)
(R2: the Crooks chain, the e^{−ω} arithmetic, the anti-FAPP rail);
[N8](../literature/N8-h7-stochastic-thermodynamic-absorbers.md) (Landauer,
Bennett, Jarzynski, Crooks, Seifert primary listings, checked 2026-06-21; the
promotion gate and demotion rule that bind this note's vocabulary);
[covariant-formulability-capability-rate-2026-07-28.md](covariant-formulability-capability-rate-2026-07-28.md)
(horizons as invariant future distances — the covariant reading of the
declared divergent edge, via the S1 schema §1.vi borrow);
[composition-extensivity-execution-2026-07-28.md](composition-extensivity-execution-2026-07-28.md)
(composite classes compose by the executed ⊗ clause; pointer only — no
composite class is run here).
Cross-repo pointer (their truth, not imported): dynamic-unity
`HC-DU-064`, pin `b190306` — see the mandatory disambiguation, §7.
**Tags:** `research_note` · `review_only` · `finite_witness` ·
`execution_companion`

---

## The registered kill (verbatim, up front)

Registered in the series tasking before this note existed, S3 form:

> **K-S3:** "commit(A,r) must be T584-invariant, monotone under capability
> extension, with horizon kind-finality recovered as the uniform
> bounded-class limit."

S1's ledger short form (schema §3, Debt L2, quoted verbatim there):

> "commit(A, r) must be T584-invariant and monotone under capability
> extension, with absolute finality as the bounded-class limit."

S1 additionally fixed the discharge clauses this swing must meet: (a)
T584-invariance (representation, gauge, declared irrelevant
coarse-graining); (b) monotonicity under capability extension in the natural
contract order (region/access/menu/resources/budget dominance — more capable
classes see no more finality); (c) the two correct limits — everyday records
lose finality as capability extends unboundedly, horizon-crossed records
stay maximal **uniformly over all bounded classes**, recovering GR's
kind-level case as the bounded-class limit rather than as a separate
stipulation. The kill fires if invariance fails, monotonicity fails, or the
limit recovery cannot even be stated.

## Verdict

**K-S3 DOES NOT FIRE.** On the T585/T586 fixture class:

- **Invariance (check i): PASS.** Representation (joule round trip through
  T585's own converters, task-interface aliasing, protocol and context
  relabeling), bit-label gauge swap, and declared irrelevant coarse-graining
  all preserve FINAL, the typed status, and the full margin vector for every
  (class, record) pair; the T584-style task-vocabulary merge counterexample
  changes the native envelope and is caught (must-fail control fails
  closed).
- **Monotonicity (check ii): PASS.** On all 61 comparable pairs of the
  declared 15-class grid, extending capability never makes any record more
  final, and every margin axis weakly improves componentwise; the constraint
  bites — 148 genuine finality flips occur, all in the lawful direction.
- **Bounded-class limit (check iii): PASS, at exactly the pre-registered
  honest outcome.** Every finite-ω record leaves finality at a finite sweep
  scale (nothing in a finite fixture is absolutely final); the declared
  unbounded-cost edge is FINAL uniformly across every declared bounded
  class; the separation schema — FINAL for all bounded classes ⟺ W_rev
  diverges — holds constructively on the fixture class. The divergent edge
  is **declared, not derived**: what the fixture can and cannot witness is
  stated in §4, and kind-level finality stays credited to GR's causal layer
  (R2), not to the module.
- **Order-compatibility (check iv, additional): PASS.** Finality is
  compatible with the T586 record order — un-commit closures nest, prices
  weakly decrease downstream, finality propagates upstream for every class,
  and adding a downstream consumer only raises ancestors' grades (the
  redundancy connection, forward-cited to S2).

Debt L2's discharge shape is thereby **instantiated at fixture level**: a
commit functional with the demanded invariance, monotonicity, and limit
behavior exists and runs. What that does and does not earn is §5–§6.

---

## 1. The definition

### 1.1 Transition-level functionals first (zero record vocabulary)

The S1 circularity audit survives or dies here, so the order of definition
is load-bearing. The following are properties of **any** stabilizing
physical transition, record-issuing or not (S1 §2: T587's rejected classes
have well-defined values too):

- **ω** — the entropy production (nats) of the stabilizing transition,
  relative to a declared system/bath split and coarse-graining (G is
  D-conditional: independent as a definition, parametric in use).
- **Spontaneous reversal:** the entropy-consuming reverse trajectory has
  probability suppressed as P_R(−ω) = P_F(+ω)·e^{−ω} — Crooks Eq. (2),
  quoted in the swings from the fetched full text; strictly nonzero for all
  finite ω; integral form ⟨e^{−ω}⟩ = 1 (Crooks Eq. (4)).
- **Driven reversal:** un-doing the transition by protocol carries a work
  bill of ω·kBT — i.e., ω/ln 2 in T585's normalized kBT ln 2 units. Same ω,
  two faces: **log-improbability if you wait, work if you drive.** That
  identity is the Crooks content; the probe checks it as a construction
  identity (check `two_faces_tie`) and claims no re-derivation.
- **Logical reset floor:** erasing a carrier holding distribution p costs at
  least its binary entropy in kBT ln 2 units — T585's source law, verbatim
  ("minimum reset work ... as the binary entropy of the memory state");
  access-conditional exactly as T585 has it (a distribution-blind class owes
  the worst-case bit).

No record vocabulary, no issuance vocabulary, no finality vocabulary occurs
above. The cycle breaker survives intact.

### 1.2 The un-commit operation for a record r (D-parametric application)

Applying 1.1 to a *record* consumes declared D-data, and the declarations
are priced as declarations:

- **Carrier map (declared):** each fixture record has a declared carrier
  cell (`cell_seed`, `cell_copy`, `cell_erase`, `cell_cert`, `cell_bias`)
  with a current distribution p and a declared stabilization entropy
  production ω for its producing event. The T586 `entropy_rank` column is
  **not** reused for ω — it is a control column (the entropy-scalar control
  shows it fails to reproduce the record order), and reusing it would
  overread a control. ω is fresh declared data.
- **The operation:** un-commit(r) := erase r AND restore the pre-issuance
  state of its carriers and every copy/derivative — concretely, of every
  record in the **un-commit closure** of r: r itself plus all records whose
  producing event lies strictly downstream of r's producer in the T586
  record order. Record-layer only: the fixture's two hand-declared
  causal-only edges (the R2 caveat's edges) are deliberately **not**
  consumed; un-committing `r_known_zero` does not touch
  `prepare_biased_reference`.
- **Construction fork (declared after the fork audit):** this note uses the
  **closure-restoring** convention above.  A distinct, coherent
  **closure-free** convention erases only `r` and does not restore downstream
  records.  The conventions agree on the finite-price, representation/gauge,
  completion, and declared-horizon checks, but the closure-free rerun kills
  this note's order-compatibility and consumer-proliferation results.  It also
  removes the settlement effect later used by the type-extension and
  nucleation artifacts.  Neither convention is asserted to be physically
  correct; see
  [the un-commit fork audit](causal-past-theorem-attempt-2026-07-28.md#1-step-1--the-undeclared-construction-fork-un-commit-closure-vs-closure-free)
  for the executable partition.  Accordingly, every result here that depends
  on closure growth is conditional on this declared convention.
- **Declared idealizations (fixture-honesty):** the fixture has no
  microdynamics, so environment traces are summarized by the declared
  per-event ω plus the record-dependency cone (which, under T586's
  unique-producer discipline, is the fixture's complete copy bookkeeping).
  Microtrajectory bookkeeping is idealized away — declared, not smuggled.

### 1.3 The price W_rev(r), in T585 units

For the finite fixture records:

> W_rev(r) = Σ over the un-commit closure of
> [ ω_i / ln 2 (destabilization work) + Landauer reset floor of carrier i
> (access-conditional) ], in normalized kBT ln 2 units.

The energy component is law-derived (Landauer floors via T585's source law;
the destabilization term via the Crooks identification). The remaining axes
(time = 1.0 + units per event, mirroring T585's own reset-time law;
communication, memory, error per event) are fixture-declared prices, exactly
the declared shape T585's own point tables use. The **two regimes** attach
to the same record: paid reversal costs W_rev (work-priced, class-gradable);
spontaneous reversal has probability e^{−Σω_i} (probability-priced,
class-independent). Their relation is the Crooks tie of 1.1: the paid face's
destabilization component times ln 2 *is* the spontaneous face's
log-suppression.

### 1.4 The grade g(A, r)

An **agent class** A is a T583 declared context (region, observer/access
profile, task family, operation menu, resources, cost/error budget, horizon)
extended with a declared carrier-access set — nothing beyond the charter's
own capability machinery. The grade is the feasibility relation of the
un-commit task against A's envelope, kept native:

- the un-commit task is priced as a T583 `PerformancePoint` and tested with
  T583's own `point_is_feasible`;
- the outcome is **typed**: `IN_ENVELOPE`, `OUT_OF_ENVELOPE_BUDGET`,
  `OUT_OF_ENVELOPE_ACCESS` (a closure carrier outside A's declared access),
  `OUT_OF_ENVELOPE_MENU` (the reverse protocol not on A's menu);
- the **margin is a per-axis vector** (slack or deficit on energy, time,
  communication, memory, error). The anti-scalarization discipline applies
  to grades too: no scalar score exists anywhere in the definition, and the
  probe exhibits two classes FINAL for the same record with **incomparable**
  margin vectors (§3.5).

### 1.5 Finality

> **FINAL(A, r) ⟺ un-commit(r) ∉ Env(A).**

Record r is final *relative to agent class A* when un-committing r exceeds
A's capability envelope. This is the repo's name cashed out: time as
finality, finality as graded inaccessibility of reversal. FINAL is a
feasibility fact, not a score; the class-independent faces (W_rev, e^{−ω})
are the record's physics, and FINAL(A, ·) is where a declared WHOM meets
that physics. Per N8's rail: FINAL is class-indexed inaccessibility, **never
constructor impossibility** — the spontaneous face stays strictly nonzero
for every finite ω, and this note promotes nothing (promotion gate item 8
binds; the demotion rule's own taxonomy — "capability/topology residue ...
not thermodynamic-arrow evidence" — is exactly the category this grade
honestly lives in, and no arrow claim is made).

---

## 2. The fixture instantiation

### 2.1 Stabilization ledger (declared) and un-commit prices (computed)

| record | producer | ω (nats, declared) | closure (record-order cone) | Σω | W_rev (kBT ln 2 units) | P_spont = e^{−Σω} |
|---|---|---:|---|---:|---:|---:|
| `r_known_zero` | seed | 4.0 | known, copied, erased, certificate | 24.0 | 34.624680981 | 3.775e−11 |
| `r_copied_zero` | copy | 6.0 | copied, erased, certificate | 20.0 | 28.853900818 | 2.061e−09 |
| `r_erased_standard` | erase | 9.0 | erased, certificate | 14.0 | 20.197730572 | 8.315e−07 |
| `r_erasure_certificate` | certify | 5.0 | certificate | 5.0 | 7.213475204 | 6.738e−03 |
| `r_biased_reference` | prepare | 3.0 | itself only | 3.0 | 4.797080717 | 4.979e−02 |
| `r_horizon_departed` | declared edge | DECLARED_DIVERGENT | itself only | ∞ (declared) | DECLARED_DIVERGENT | 0.0 |

Two touches worth naming: the biased reference's W_rev carries the fixture's
own signature Landauer floor 0.468995594 (T585's biased-record cost)
on top of its 3/ln 2 destabilization term — floors and destabilization are
visibly different objects; and the floors of the known-zero chain are 0.0
for sighted classes (erasing a known bit is Landauer-free), which is exactly
why commitment is **not** located in the erasure floor: it is located in the
stabilization ω, as R2's mechanism section has it.

*Attribution note (recorded post-landing; S6 §6, seam 1):* this table
consumes T586's source-owned typing, under which `copy_known_record` is a
producer with its own record row (ω = 6.0) and the closure has 6 pairs.
S2's mechanism-honest provenance grouping types the same event as
broadcast — not an issuer — under which the copied row would not exist as
a separate record and 4 of the 6 closure pairs survive. Every per-record
number here is relative to that declared typing; neither attribution is
settled, and check (iv)'s verification on the 6-pair order does not
automatically transfer to the re-attributed 4-pair order (unrun).

### 2.2 The class grid (15 declared classes)

- **Budget sweep** (10 classes): T585's base context and budget
  (energy 0.75, time 5.0, communication 1.0, memory 1.0; error bound held
  fixed at 0.01 so the sweep is a ⊑-chain), scaled by
  s ∈ {1, 2, 4, 8, 16, 32, 40, 48, 64, 128}; menu extended with the declared
  `crooks_reverse_protocol`; task family extended with the per-record
  un-commit tasks.
- **A_blind_0048:** scale 48 without distribution access — Landauer floors
  go worst-case (1.0 per carrier), T585's own blind accounting.
- **A_no_copy_access_0128:** scale 128 without access to `cell_copy`.
- **A_no_reverse_0128:** scale 128 without the reverse protocol on the menu.
- **A_energy_poor_time_rich / A_time_poor_energy_rich:** deliberately
  ⊑-incomparable budget shapes (energy×32/time×128 vs energy×128/time×4)
  for the anti-scalarization exhibit.

The extension order A ⊑ A′ is componentwise dominance on every declared
capability field (budget axes, carrier access, access profile, menu, task
family) — Debt L2 (b)'s "natural contract order," implemented literally.
The grid has 61 comparable pairs.

---

## 3. Results

### 3.1 The grade table (FINAL profile; × = final, ∘ = in-envelope)

| class \ record | known | copied | erased | certificate | biased | horizon |
|---|:-:|:-:|:-:|:-:|:-:|:-:|
| A_scale_0001 | × | × | × | × | × | × |
| A_scale_0008 | × | × | × | × | ∘ | × |
| A_scale_0016 | × | × | × | ∘ | ∘ | × |
| A_scale_0032 | × | × | ∘ | ∘ | ∘ | × |
| A_scale_0040 | × | ∘ | ∘ | ∘ | ∘ | × |
| A_scale_0048 | ∘ | ∘ | ∘ | ∘ | ∘ | × |
| A_scale_0128 | ∘ | ∘ | ∘ | ∘ | ∘ | × |
| A_blind_0048 | × | ∘ | ∘ | ∘ | ∘ | × |
| A_no_copy_access_0128 | × | × | ∘ | ∘ | ∘ | × |
| A_no_reverse_0128 | × | × | × | × | × | × |

Sample margins (per-axis vectors; full precision in the probe output):
at A_scale_0048, `r_known_zero` is in-envelope with energy slack
+1.375319019 and time slack +201.375; the same record for A_blind_0048 is
OUT_OF_ENVELOPE_BUDGET with energy deficit −2.624680981 (the four worst-case
floors) — same budget, less access, more finality, absorbed as
ACCESS_COMPLETION. For A_no_reverse_0128 every finite record is
OUT_OF_ENVELOPE_MENU with every numeric margin positive: capability money
cannot buy an operation the menu lacks — the menu face and the budget face
are different completions, exactly T583's discipline.

### 3.2 Check (i) — T584 invariance: PASS

Applied to (A, r) jointly, per T584's admissible classes:

| morphism leg | class | outcome |
|---|---|---|
| joule round trip (T585's converters) + un-commit task aliasing + protocol/context relabel | representation | FINAL, status, and margin vector preserved for every (A, r); context `semantic_dict` unchanged |
| bit-label gauge swap, p → 1−p on every carrier | gauge | floors, prices, statuses, margins all invariant (binary entropy is gauge-invariant) |
| drop `display_label` / `sensor_serial` / `coordinate_name` | irrelevant coarse-graining | physical payload the grade consumes is unchanged |
| merge all per-record un-commit tasks into one task id | **inadmissible (must-fail)** | native envelope changes (record resolution lost: the merged frontier collapses to the cheapest record's point) — **caught**; the gate has teeth |

The grade reads no representation, gauge, or presentation label — Debt L2
(a) at fixture level.

### 3.3 Check (ii) — monotonicity under capability extension: PASS

Direction, stated exactly and tested: **for A ⊑ A′, FINAL(A′, r) ⟹
FINAL(A, r)** for every record — extending budgets, access, or menu never
makes any record MORE final; equivalently, finality can only evaporate as
capability extends. On all 61 comparable pairs × 6 records: no violation,
and 148 genuine flips occur — all from final (smaller class) to not-final
(larger class). Margins are monotone too: on budget-graded pairs every axis
weakly improves componentwise (slack grows, deficits shrink; the blind case
included, since worst-case floors weakly exceed sighted floors). Debt L2 (b)
at fixture level.

### 3.4 Check (iii) — the bounded-class limit: PASS, honest outcome

Un-finalization thresholds along the sweep (first scale in-envelope):

| record | W_rev | first sweep scale not final |
|---|---:|---:|
| `r_biased_reference` | 4.797080717 | 8 |
| `r_erasure_certificate` | 7.213475204 | 16 |
| `r_erased_standard` | 20.197730572 | 32 |
| `r_copied_zero` | 28.853900818 | 40 |
| `r_known_zero` | 34.624680981 | 48 |
| `r_horizon_departed` | DECLARED_DIVERGENT | **never — uniformly final across every declared bounded class** |

The expected honest outcome is the outcome: **no finite-ω record stays
final** as budgets grow — everything in a finite fixture is reversible at
some budget — and the thresholds are ordered exactly by un-commit closure
depth (deepest-upstream record last). The kind-level recovery is §4.
Constructive half, via T583's own feasibility predicate: for every finite
record, the class with budget = cost + 1 on each axis covers its un-commit;
for the declared divergent edge, no bounded budget can, and its carrier
(`cell_departed`) lies outside the declarable access universe besides.

### 3.5 Anti-scalarization exhibit

For `r_known_zero`: A_energy_poor_time_rich is FINAL with margin
(energy −10.625, time +601.375, …); A_time_poor_energy_rich is FINAL with
margin (energy +61.375, time −18.625, …). Incomparable deficit patterns —
neither class is "more unable" than the other, and no scalar could say
otherwise without a declared, T584-invariant scalarization that this note
does not construct (the covariant note's σ residue stays open; nothing here
consumes it). The grade is native-Pareto all the way down.

### 3.6 Check (iv) — order-compatibility with T586: PASS

On all 6 pairs of the T586 record-order closure (producers upstream ⇒
records upstream): un-commit closures nest (downstream's ⊆ upstream's);
W_rev and Σω are weakly (here strictly) decreasing downstream; and for every
class, FINAL(A, downstream) ⟹ FINAL(A, upstream) — **a record's finality
only grows as its consumers proliferate downstream.** The
consumer-proliferation probe makes that incremental: adding one declared
consumer (`archive_certificate`, ω = 4.0, consuming the certificate) weakly
increases every ancestor's price, changes no non-ancestor, and moves
finality only toward FINAL at fixed class. The T586-incomparable
`r_biased_reference` participates in no constraint (its closure is a
singleton, and it is the cheapest and first to un-finalize) — compatibility,
not collapse, with the partial order.

*(Post-landing note: S2 returned PARTIAL — neither branch above; the
order-compatibility fact stands on its own per the fallback clause, and
the "one mechanism, two faces" unification is not earned — S2 measured
redundancy doing no split-robust selective work on this fixture class;
S6 §6, seam 2.)*

This is the redundancy connection, and it is S2's territory approached from
the other side: S2 (issuance from redundancy —
[commit-module-s2-redundancy-issuance-2026-07-28.md](commit-module-s2-redundancy-issuance-2026-07-28.md),
a parallel arm; cited as a pointer only, its verdict not consumed here) asks
whether copies *constitute* record-hood; S3 finds that the same downstream
copies are what *price* the un-commit.
One mechanism, two faces — if S2 lands, issuance threshold and finality
grade become two readings of the same redundancy structure; if S2 fails,
this check stands on its own as an order-compatibility fact.

### 3.7 Finality deltas are named completions

Every finality flip across the grid's comparable class pairs is absorbed by
a named T583 completion class: 49 RESOURCE_BUDGET_COMPLETION,
4 ACCESS_COMPLETION, 1 MENU_COMPLETION, 0 unabsorbed. In T583's own audit vocabulary: **there is
no intrinsic finality delta anywhere on the grid** — every difference in
what is final for whom is a declared-context difference. That is the R2
repricing stated in the contract's native terms.

---

## 4. The limit-recovery statement (exact, with fixture boundaries)

The theorem-schema the fixture instantiates:

> **FINAL(A, r) for every bounded class A ⟺ W_rev(r) diverges** (equivalently:
> the un-commit closure's carriers exit every declarable access region, so
> the reversal work — covariantly, the invariant future distance to the
> carriers, per the covariant note's skeleton — is not finitely purchasable
> by any declared context).

with, for finite W_rev, the constructive converse: some bounded class covers
the un-commit (budget = cost + 1; §3.4). Horizon kind-finality is thereby
recovered **as the uniform bounded-class limit of the same grade** — the
W_rev → ∞ boundary of one definition — rather than as a separate
stipulation: no second finality concept is introduced for the horizon case.

**What the fixture CAN witness:** the separation itself — every finite-ω
record un-finalizes at a finite sweep scale while the divergent edge stays
final at every declared bounded class, uniformly, with both facts computed
by the same feasibility predicate; and the constructive covering for every
finite record.

**What the fixture CANNOT witness (declared, per fixture-honesty):** the
divergence is a **declared unbounded-cost edge** — a record whose carriers
are declared to have departed every accessible region — not a derived
geometric fact. The fixture proves nothing about GR: no causal structure is
modeled, no horizon is derived, and the sweep is finite (the "uniform over
all bounded classes" clause is witnessed over every *declared* class and
secured by the divergence declaration, not by quantification over an
infinite class family). Kind-level finality at actual horizons remains
credited to GR's causal layer (R2's grading table), and the module's
contribution remains the graded non-horizon leg. The schema above is the
honest bridge: it says *if* something makes W_rev diverge for every bounded
class — as causal disconnection would — *then* the grade goes kind-level
uniformly, with the antecedent supplied by GR, not by this fixture.

---

## 5. The payoff, exactly as earned

**The R2 debt, re-priced.** R2's finding was that "commit" is FAPP-graded:
un-commit probability e^{−ω}, "zero for all practical purposes ... and zero
as a matter of law at none." FAPP is an apology only while "practical
purposes" is an unanalyzed phrase. This swing replaces it: **"FAPP" becomes
"final-at-grade-g for declared class A"** — where g is the typed,
vector-margined feasibility relation of §1.4, and the two faces of the grade
are the un-commit probability (e^{−ω}, class-independent, what you get if
you wait) and the un-commit work (W_rev, what a class must pay to drive it —
in-envelope or not, per class). "For all practical purposes" now has a
formal referent: *for all tasks within the declared envelope of the class
whose practices they are.* The degree-not-kind structure R2 exposed is not
repaired — it is **owned**: degree is the content of the grade, and kind is
its declared-divergence boundary (§4).

**The epigraph, upgraded to a theorem-schema.** "The past is what has
become hard to undo" (README line 1) carried, per R2, an unanswered
question: hard *for whom*? The charter's own capability machinery supplies
the WHOM: a T583 declared context is precisely a formalized whom, and the
module's schema is

> **the past of class A = { records r : FINAL(A, r) } = { records whose
> un-commit lies outside A's envelope }**

— T584-invariant, monotone (a more capable class has a no-larger past —
extending capability can only soften finality, never harden it), compatible
with the record order (records with more downstream consumers are harder to
undo for everyone), and going kind-level exactly where W_rev diverges. The
epigraph's "hard" was degree-language already (R2's qualification); this
note makes the degree a functional and the "for whom" an argument.

**What remains NOT earned:**

- **No continuum claim.** One finite fixture family, causally-aligned
  regime (the sweep's scope entry binds); no field theory, no continuum
  limit, no claim about infinite record systems.
- **No quantum-measurement claim.** Nothing here touches sealed labs,
  proto-records, or the Wigner-friend exit — commit(A, r) is an input S5
  may consume, not a settlement of L4.
- **No claim that this grade is THE physical finality.** It is the
  module's candidate for it — CM's G-component in its capability-indexed
  form. Whether the identification (committedness := graded inaccessibility
  of reversal) is the right reading of physical finality is the series
  conclusion's question, and the charter's classification discipline
  (empirically-equivalent-but-explanatory) applies to it.
- **ω is declared, not derived.** Every evaluation is D-conditional (S1
  §2): the carrier map, the split, and the per-event ω are declared fixture
  data. S4 owns whether D can be derived or must stay a priced primitive;
  this swing neither anticipates nor discharges it.
- **No general theorems.** Invariance, monotonicity, and the limit schema
  are executed finite-witness facts on this fixture class plus definitional
  arguments; they are not proved for arbitrary record systems.

---

## 6. Pre-registered kill verdict

**K-S3 DOES NOT FIRE.**

- Invariance: did not fail (three admissible legs preserve FINAL and
  margins; the inadmissible merge is caught).
- Monotonicity: did not fail (61/61 pairs lawful; 148 flips, all in the
  extending-un-finalizes direction; margins componentwise monotone).
- The limit recovery: **statable and stated** (§4), with the honest rider
  that the horizon side enters the fixture as a declared divergent edge —
  the fixture witnesses the separation, GR supplies the geometry; S1's
  conviction clause for this leg (limit fails to separate horizon from
  everyday) is directly witnessed false at fixture level (§3.4).

Debt L2 therefore moves from "commit is FAPP-grade" (an unpriced apology on
the rival's ledger) to "commit(A, r) exists at fixture level with the
demanded properties" (a priced, executed component). Per S1's end-state
discipline, this prices the G-component; it does not close the series, and
a PARTIAL elsewhere (S2, S4, S5) still prices its own component.

---

## 7. Mandatory disambiguation (dynamic-unity's capability–record lattice)

The words "capability" and "record" occur load-bearingly in a dynamic-unity
result banked one day before this series:
`dynamic-unity#explorations/capability-record-galois-closure-and-non-chain-regional-finality-2026-07-27.md`
(`HC-DU-064`, pin `b190306`; its executive-verdict section was read before
this citation, per the series tasking). **Same words, different objects:**
their "capability–record" object is a *query-closure* polarity — an antitone
Galois connection between an observer's admitted response-query families and
record equivalences on histories, whose closed pairs form a complete (and in
their minimum specimen non-chain, M₃) lattice of *record requirements*;
commit(A, r) grades *reversal* capability — T583 envelopes pricing the
un-commit operation (Landauer floors, Crooks-side destabilization) — and
says nothing about query families or history quotients. Neither object
imports, implies, or adjudicates the other; `HC-DU-064` remains
dynamic-unity's truth, cited by pointer under Goal 3's routing measure. The
one shared moral, held at moral level only: **finality is graded and
non-global on both sides** — theirs a lattice of closed capability–record
pairs instead of one scalar progression, ours a class-indexed grade instead
of one absolute past. The convergence of two independent formalisms on
"graded, not global" is worth a pointer; it is not worth an identification,
and none is made.

---

## What This Does Not Claim

- **The dynamic-unity STOP on foliation-existence testing is respected.**
  Nothing here asserts or tests whether any foliation, update ordering,
  tick, or beable exists; `NI-DU-87` remains dynamic-unity's truth, cited
  by pointer.
- **No claim movement.** H2–H4, R1, T3, T583–T588, every claim, bin, canon
  tier, guardrail, and test status stay exactly where their owners left
  them. VERDICT.md and the Goal-2 NO are untouched.
- **No tick-family credit.** Pricing the rival's G-component does not
  revive T586's downgraded order claim, contract B, the confinement branch,
  or any closed route; the ten-plus adverse tick artifacts stand.
- **No T-number and no results/ artifact.** The probe is an un-T-numbered
  exploration companion (the composition companion's discipline); the owner
  mints numbers and decides adoption.
- **No promotion of unlikelihood to impossibility.** N8's gate binds:
  FINAL(A, r) is declared-class inaccessibility; e^{−ω} > 0 for every
  finite ω; nothing here is constructor impossibility, and no thermodynamic
  arrow is claimed (the grade is N8's "capability/topology residue"
  category, named as such).
- **No new physics and no priority.** Landauer's bound, Crooks' theorem,
  and the Jarzynski relation are their authors'; T583–T586 are the repo's;
  the assembly (un-commit closure pricing, capability-graded FINAL, the
  divergence-boundary reading of kind-finality) is application-level
  synthesis, likely known in parts to practitioners; priority is claimed
  for nothing.
- **No horizon geometry.** The divergent edge is declared; GR's causal
  structure is neither modeled nor tested; H4's territory is untouched.
- **No anticipation of parallel arms.** The S2 and S4 arms landed same-wave
  in parallel with this one; S2 is cited by filename pointer only (§3.6) and
  neither arm's verdict is read, consumed, or presumed here. The DU-holdings
  gate arm's report and S5 are awaited. The forward-cites in §3.6 are
  mechanism-level pointers only.
- **Depth limits are binding.** Crooks enters at the swings' full-text
  fetch (their extraction caveat carried); Landauer/Bennett/Jarzynski/
  Seifert at N8's primary-listing depth, checked 2026-06-21; no depth is
  upgraded here and nothing was fetched this run.

## Provenance

- **Writer lock:** checked before writes —
  `git rev-parse --git-path capacityos-writer.lock` →
  `.git/capacityos-writer.lock`, not present. HEAD at read time: `1db0f6a`
  (matches the series' declared baseline). This arm performs file writes
  only; no commit, no push; its writes are exactly this file and
  `models/capability_graded_finality_probe.py`.
- **In-repo texts read in full for this note:**
  commit-module-schema-2026-07-28.md (the fixed object, fully, per
  tasking); rival-symmetry-swings-2026-07-28.md (fully, per tasking — R2
  and its Crooks equations are consumed from there);
  tests/T583–T586 (all four specs) and models
  t583_capability_contract_v1.py, t584_capability_invariance_morphism_gate.py,
  t585_landauer_physical_capability_gate.py,
  t586_record_capability_order_gate.py (all four, fully — the probe consumes
  their public machinery and re-executes T585/T586 at run time); N8 (full);
  README.md line 1 and GLOSSARY.md (Commit Order, Finality Domain) verified
  verbatim; composition-extensivity-execution-2026-07-28.md (head and
  verdict sections, for the companion discipline and the ⊗ pointer).
- **Cross-repo read:** dynamic-unity's HC-DU-064 note — front matter and
  executive-verdict section read in the local clone; file presence verified
  at pin `b190306` (`git ls-tree`); cited by pointer only.
- **Consulted at section level (not read in full):**
  covariant-formulability-capability-rate-2026-07-28.md — the
  corner-distance/horizon lines only, carried primarily through the S1
  schema's §1.vi summary.
- **No fetches this run.** All external physics enters via the swings'
  labeled fetches (Crooks full text) and N8's primary listings; depth
  labels carried, not upgraded.
- **Model run:** `python3 -m models.capability_graded_finality_probe` from
  the repository root; exit 0; 16/16 checks pass; output byte-identical
  across repeat runs (verified); deterministic by construction — no
  randomness anywhere (so no seeds are needed), no wall-clock values.
- **Registered-kill provenance:** K-S3 was registered in the series tasking
  before this note existed and is quoted verbatim up front alongside S1 §3's
  ledger form; the adjudication protocol executed here (invariance /
  monotonicity / limit clauses) is S1's, sharpened without weakening by the
  uniform-bounded-class wording.

## CONVENTION FORK — declared retroactively (2026-07-28)

§1.2's un-commit definition — *erase r AND restore the pre-issuance state
of every record in the un-commit closure* — was declared in one sentence
with **no construction-fork declaration**, in a repository whose own
discipline requires forks be named rather than defaulted. The alternative
reading, *un-commit(r) := erase r only*, has now been executed:
`models/uncommit_convention_fork_probe.py` (rebinds the pricing function;
this file's own probe is unmodified and still exits 0) and
`explorations/causal-past-theorem-attempt-2026-07-28.md` Step 1.

**Results fall on opposite sides of the fork, and the program had bundled
them.**

*Convention-CARRIED — these die under the closure-free reading:* check
(iv)'s order-compatibility (3 of 4 legs **invert** — it does not go
vacuous, it goes false); the closure-depth ordering of un-finalization
thresholds (`r_known_zero` moves from last to first-tied — an artifact);
the type-extension settlement separation (collapses into the deflationary
exit that packet had itself registered as evidence *against* the ratchet
thesis); the nucleation toy's P1 (68 genuine flips → **0**; its structural
check fails and it exits 1 with `STRUCTURAL_FAILURE`, with the underlying
dynamics verified bit-identical across the fork).

*Convention-INDEPENDENT — these pass under both:* the limit-separation
schema, the horizon edge's uniform finality (the divergent row is
identical across the fork), both monotonicity checks, all three T584
invariance legs, the merge control, and the completion classification.

**Anything citing this file's closure-dependent results must carry the
fork.** A third convention (r plus its carriers but not downstream
derivatives) sits between the two and was not run, so the bracket may not
be tight. One further honest note: the anti-scalarization exhibit also
fails under the fork — diagnosed post-hoc as specimen loss (both
incomparable classes fall in-envelope at the lower price), not structural,
but it exposes real fragility in that exhibit's design.
