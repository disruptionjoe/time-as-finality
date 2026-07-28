# The Nucleation Ratchet Toy: Type-Creation as Stochastic Barrier-Crossing, Finality as the Return Stroke

**Status:** Q-0066 **item-3 toy** — the first executable instance of the
two-stroke ratchet. Review-only: **no claim movement**, no T-number, no bin
regrade, no guardrail edit, no Lane or public-posture change, no cross-repo
result. **The fork stays TI's** (PP-3 / D-FORK untouched, carried by
pointer). **The DU STOP is respected** (record interface supplied, seam-only,
nothing split-dependent passed off as representation-independent). Verdict
shape: **RATCHET INSTANTIATED — WITH TWO PRE-REGISTERED PREDICTIONS FAILING
IN THEIR STRONG FORM**, both reported as first-class results and neither
tuned away.
**Date:** 2026-07-28
**Registered motivation:** Q-0066 item 3 — the nucleation toy, registered
wiki-first on the private thinking-wiki surface
(`joe-thinking-wiki#map/explorations/q0066-predictive-selection-and-the-issuance-fork-2026-07-28.md`;
**pointer only**, per public-repo hygiene — no private content beyond the
registration's existence, its ownership line (TI owns the fork, TaF the
currency, DU seam-only), and phrasing already public in-repo is imported).
**Made buildable by:**
[proposed-type-extension-morphism-gate-2026-07-28.md](proposed-type-extension-morphism-gate-2026-07-28.md)
Exit A — "the two-stroke ratchet toy … becomes buildable: this gate supplies
its type-space-growth stroke as a lawful operation." That packet's ε is
**imported and executed here**, not re-derived.
**Builds on (pointers; nothing re-derived):**
[commit-module-s3-capability-graded-finality-2026-07-28.md](commit-module-s3-capability-graded-finality-2026-07-28.md)
(commit(A, r): the un-commit closure, W_rev in kBT ln 2 units, typed
feasibility against T583 envelopes, per-axis margin vectors, the
anti-scalarization discipline, check (ii)'s class-axis direction and check
(iv)'s upward nesting);
[record-layer-naturality-spec-2026-07-28.md](record-layer-naturality-spec-2026-07-28.md)
(reconciliation at contact: union-with-provenance vs pairing forms, and the
**C-clock finding** — non-canonical metadata stores the *relative alignment*
of the two contexts, invariant under the diagonal subgroup and non-natural
under independent componentwise relabeling);
[commit-module-s2-redundancy-issuance-2026-07-28.md](commit-module-s2-redundancy-issuance-2026-07-28.md)
(its boundary-sentence pattern is this toy's: "issuance" is **declared
in-model dynamics**, never a source-metaphysics claim);
[commit-module-schema-2026-07-28.md](commit-module-schema-2026-07-28.md) §1.v
(bounded agent classes; the sealed-lab / no-settlement posture; "below the
record layer: silent");
[T583](../tests/T583-capability-contract-v1.md) /
[T585](../tests/T585-landauer-physical-capability-gate.md) (the declared
context, budgets, native Pareto comparison, and the one-bit fixture, consumed
verbatim);
[T584](../tests/T584-capability-invariance-morphism-gate.md) (the admissible
morphism classes the variant relabelings instantiate);
[T587](../tests/T587-t586-causal-collapse-boundary-attack.md) (the stop —
this toy mints no T-number and adds no comparator to the frozen T586 event
system).
**Model:** [../models/nucleation_ratchet_toy.py](../models/nucleation_ratchet_toy.py)
(stdlib + in-repo models only; run with
`python3 -B -m models.nucleation_ratchet_toy` from the repository root; exit
0; deterministic — fixed literal seeds, no wall-clock, no date, no OS
entropy; output verified **byte-identical across two consecutive runs**)
**Tags:** `research_note` · `review_only` · `finite_witness` ·
`execution_companion` · `toy_model`

---

## Verdict, stated first

The two-stroke ratchet **runs**. On a declared 3-region, 5-type, 30-tick
fixture with five literal seeds:

- the **type stroke** (nucleation → ε-extension → founding record) and the
  **commit stroke** (S3 grades over the growing record graph) move finality
  in opposite directions exactly as the packet's SPLIT-BY-LAYER result
  predicts — attainability conserved **by law** at every step, settlement
  prices monotone along ε (**P1 CONFIRMED**, 0 violations, 68 genuine
  reversible → final flips);
- the declared Kramers ordering is realized (**P2 CONFIRMED**);
- the Kibble–Zurek analog scales, with the honest KZ shape: defect *density*
  is set by the contact (quench) rate, defect *count* by system size
  (**P3 CONFIRMED**);
- **P4 fails in its strong form** — a defect record's un-commit price never
  dominates the record graph, because it is *downstream* of the two founding
  records it reconciles and S3 check (iv)'s upward nesting therefore forces
  its own ancestors to price higher. Defect permanence in this toy shows up
  **in the defect's ancestors, not in the defect** (**P4 SPLIT**: weak form
  holds, strong form fails);
- **P5's attribution clause fails** — the attainability layer is bitwise
  identical across all three arms (disclosure-indistinguishable, forced by
  conservativity), settlement and defect structure do separate, but a third
  arm with the reservoir **fully declared up front and variant adoption still
  stochastic** reproduces the nucleated arm's defect structure **exactly**.
  The defect signature localizes to *stochastic per-region selection*, not to
  type pre-existence. What type-*arrival* uniquely leaves behind is the
  **record-graph shape** — which record a newly arriving type may lawfully
  name as its consumption edge (**P5 SPLIT**).

**The single sharpest finding.** In this toy the entire in-model residue of
"issuance versus disclosure" reduces to one contract fact — *the consumption
edge a type may declare depends on what existed when it arrived* — and that
one fact is worth an order of magnitude in settlement price at **bitwise
identical attainability**: the same audit founding record prices
**10.098865286** kBT ln 2 units in the fully-declared arm (star graph:
closure = itself) and **103.874042944** in the nucleated arm (chain graph:
closure = everything that arrived after it), while every envelope restricted
to the base task family is identical to Env(C) in both.

---

## 1. What the toy is

Five declared objects, each a reuse:

1. **Regions.** N ≤ 5 T583-class declared contexts, each T585's one-bit
   Landauer context verbatim with `context_id` / `region_id` / `observer_id`
   re-labeled. Same declared budget everywhere (energy 0.75, time 5.0,
   communication 1.0, memory 1.0, error 0.01), same horizon. Each region
   starts holding one base record (declared ω = 9.0, floor 0.0 — S3's
   `r_erased_standard` row, verbatim).
2. **Type reservoir.** Five candidate task-types in three **type-slots**,
   each slot carrying a declared formation barrier Δ, a declared
   stabilization ω, and a declared performance point feasible inside the
   *unchanged* budget. Two slots carry two **exclusive variants** (same
   slot, different task id, **identical declared performance points** — the
   degeneracy is what makes variant choice a symmetry-breaking event, and
   what makes a variant relabeling a T584 *representation* morphism); the
   third slot has one variant.

   | slot | variants | Δ | declared rate e^(−βΔ) | declared ω |
   |---|---|---:|---:|---:|
   | `audit` | alpha, beta | 1.5 | 0.22313016 | 7.0 |
   | `archive` | alpha, beta | 3.0 | 0.049787068 | 4.0 |
   | `mint` | solo | 4.0 | 0.018315639 | 3.0 |

   Every ω is a verbatim reuse of an already-declared ledger row (S3 §2.1 /
   the packet's ε₁): base 9.0, audit 7.0, defect 6.0, crossing 5.0, archive
   4.0, mint 3.0. **Nothing about the barriers or the rate law is derived,
   imported, or claimed as physics — both are DECLARED.**
3. **Nucleation dynamics.** Per region, per tick, each unfilled slot crosses
   with declared probability `ATTEMPT · e^(−βΔ)` (β = 1.0, ATTEMPT = 1.0,
   seeded RNG). On crossing, the region's context extends by **ε_τ — the
   type-extension packet's own morphism class, imported**: the packet's
   `admissible` is called at **every** nucleation step, so conservativity
   (anti-revisionism), budget discipline, and the deletion / no-new-task legs
   are executed by the packet's own code, not re-implemented. Only the
   *record universe* is localized here (the toy's store grows, so
   `UNKNOWN_RECORD_CONSUMED` / `REISSUE_EXISTING_RECORD` /
   `TASK_ID_COLLISION_NOT_EXTENSION` are re-checked against the region store
   using the packet's own typed reason strings). Nucleation then **issues** a
   founding record for τ in that region, with declared ω, consuming the
   region's current head record — so types **stack in nucleation order**.
4. **Commit stroke.** At every tick, S3's un-commit price is recomputed for
   every record over its (depth-unbounded) downstream closure:
   `W_rev(r) = Σ_closure [ ω_i / ln 2 + Landauer floor_i ]` in T585's
   normalized kBT ln 2 units, graded against three declared classes by
   T583's own `point_is_feasible`, with per-axis margin **vectors** and no
   scalar anywhere.
5. **Contact reconciliation.** Regions meet pairwise on a declared contact
   schedule. Per slot at contact:
   - one side has the type, the other does not → **transfer**
     (union-with-provenance; the recipient adopts it and stops drawing —
     this is the causal-contact pre-emption that makes the KZ analog work);
   - both sides, same variant → **smooth merge**: union-with-provenance,
     **no generated metadata** — the form the naturality probe found NATURAL;
   - both sides, different variants → **the merge cannot be smooth**. A
     **DEFECT record** is issued at the boundary storing the ordered variant
     pair ((R_a, v_a), (R_b, v_b)) — i.e. the **relative alignment**, exactly
     the C-clock content the naturality probe localized. It consumes both
     founding records and is permanent.
   Each contact also fires one cross-boundary task, issuing a crossing
   record that consumes the boundary's defect records if any, else the two
   base records. Defects therefore accrete a consumer at every subsequent
   contact.

## 2. Construction fork declaration

- **Declared dynamics, not physics.** The barrier Δ, the Arrhenius/Kramers
  form of the rate law, β, and the attempt probability are **declared
  in-model parameters**. No phase transition, nucleation rate, or
  symmetry-breaking process in nature is modeled, reproduced, or claimed.
  The toy tests **coherence and in-model signatures only**.
- **"Issuance" is declared in-model dynamics.** Per the S2 boundary-sentence
  pattern: whether any lawful C → C⁺ in nature is genuine type creation or
  bounded disclosure of a fixed richer source is **PP-3 / D-FORK** (TI-C019,
  E026), owned by temporal-issuance and routed there by T588's fork handoff.
  Untouched here, by pointer. Nothing below is an issuance verdict.
- **Addition-only ε (inherited).** The packet's v1 scope binds: nucleation
  adds task types and only adds. Deletion, mutation, merge, and re-typing are
  different operations and are rejected fail-closed (controls).
- **Exclusivity is a declared toy law**, not a contract law: two variants of
  one slot may not both be instantiated in one region
  (`EXCLUSIVE_SLOT_ALREADY_OCCUPIED`). It is the symmetry-breaking analog and
  is declared as such.
- **Two axes, not conflated (inherited).** S3's ⊑ grows the un-committing
  *agent class*; ε grows the *world's* task space. They move finality
  oppositely. S3 check (ii)'s direction is verified untouched here.
- **Depth-unbounded closures.** Unlike the packet's depth-1 fixture, this
  toy's closures are transitive (types stack, defects accrete crossings).
  That is the point of making it dynamic — and it is what makes P4's strong
  form fail.

## 3. Pre-registered predictions (fixed before the results section)

P1–P5 below were written before execution and are **not** revised. Two fail
in their strong form; both failures are reported as first-class results and
neither the model nor the predictions were tuned to make them pass. Fixture
sizing (barriers, tick count, seed set) was fixed **before** this
pre-registration, on the single declared criterion that every reservoir slot
be exercised at least once; it was not revisited afterwards.

- **P1 — the two strokes move oppositely.** Each nucleation weakly raises the
  settlement price of every prior founding record; early records' finality
  grades are monotone non-decreasing in nucleation count (the packet's
  ε-monotonicity, now dynamic). No price decreases; no grade regresses from
  final to reversible at fixed class; at least one genuine flip occurs.
- **P2 — Kramers ordering in-model.** Realized nucleation counts across
  seeds respect the declared e^(−βΔ) ordering, and higher-barrier slots
  nucleate later and more rarely: count(audit) ≥ count(archive) ≥
  count(mint), and mean realized crossing tick ordered the other way.
  Measured **contact-free**, so that transfer pre-emption cannot confound it.
- **P3 — Kibble–Zurek analog.** Defect count scales with
  independent-nucleation opportunity.
  **P3a:** defect count is non-decreasing in the contact interval (rarer
  contact ⟹ more defects; raising contact frequency relative to the
  nucleation rate reduces defects).
  **P3b:** at fixed per-pair contact rate, defect count is non-decreasing in
  the number of regions.
- **P4 — defect permanence.** Defect records, once graded, are among the
  hardest to un-commit for the declared classes, because every subsequent
  cross-boundary task consumes them.
  **P4-strong:** a defect record's W_rev dominates every other record's
  W_rev at the end of the run.
  **P4-weak:** among records issued at or after the defect's issuance tick,
  the defect's W_rev is maximal.
- **P5 — the issuance/disclosure in-model signature.** Re-run identical seeds
  with the reservoir **fully declared up front** versus types **arriving by
  the nucleation rule**.
  **P5a:** the attainability layer is IDENTICAL — disclosure-indistinguishable,
  forced by conservativity: every region's envelope restricted to the base
  task family equals Env(C) bitwise in every arm at every step, and every
  exercised type's frontier point is identical across arms.
  **P5b:** settlement trajectories and defect structure are path- and
  order-dependent, and differ between the arms.
  **P5c (attribution).** The P5b separation is carried by type *arrival*
  per se. Could-fail exit named in advance: if a **third arm** — reservoir
  fully declared at t = 0 but variant adoption still a per-region seeded
  event — reproduces the nucleated arm's defect structure exactly, then P5c
  **fails for the defect channel** and the in-model signature localizes to
  stochastic per-region selection rather than to type pre-existence. The
  settlement channel is tested separately for the same pair.

  **Framing, fixed in advance and binding on the results.** P5 distinguishes
  the **dynamics' path-dependence**, not metaphysical issuance. It is not a
  test of PP-3 and cannot become one. The register's same-day sharpening is
  what makes it worth measuring at all: *if collapse/measurement is seeing
  rather than creating — disclosure-shaped — then the only in-model place
  issuance could show up is precisely this settlement/type-layer
  path-dependence.* P5 measures that place. A signature there is a statement
  about where a signature could live, not evidence that anything is issued.

## 4. Results

Executed configuration: 3 regions, 30 ticks, 5 literal seeds
(10007, 10009, 10037, 10039, 10061), contact every 6 ticks with all pairs
meeting, β = 1.0. Randomness is pre-drawn into one independent stream per
(seed, region, slot) with sub-seeds derived by fixed integer arithmetic, so
every arm consumes an identical table and a region's draws never depend on
how many regions the configuration contains.

### 4.1 P1 — the two strokes move oppositely: **CONFIRMED**

| quantity | value |
|---|---:|
| price-monotonicity violations (all records, all seeds, all ticks) | **0** |
| grade regressions final → reversible at fixed class | **0** |
| genuine reversible → final flips (bites) | **68** |

Sample trajectory, seed 10007, region R1's base record (kBT ln 2 units):

| tick | 1 | 6 | 12 | 18 | 24 | 30 |
|---|---:|---:|---:|---:|---:|---:|
| W_rev(`r_base_R1`) | 12.984255368 | 59.150496676 | 73.577447085 | 88.004397494 | 102.431347903 | 116.858298312 |

First tick FINAL: **2** for A_small (energy 14.0), **5** for A_mid (25.0),
**12** for A_big (64.0). The packet's static ε-monotonicity is thereby
exhibited dynamically: the world stroke only accretes finality, and it does
so *while the attainability layer is frozen by law* (§4.5).

### 4.2 P2 — Kramers ordering in-model: **CONFIRMED**

Contact-free leg, 15 (region × seed) opportunities per slot:

| slot | declared rate | realized nucleations | mean realized crossing tick |
|---|---:|---:|---:|
| `audit` (Δ 1.5) | 0.22313016 | 15 | 3.666667 |
| `archive` (Δ 3.0) | 0.049787068 | 13 | 8.615385 |
| `mint` (Δ 4.0) | 0.018315639 | 6 | 11.0 |

Both orderings hold. **Honest caveat:** the mean crossing tick is taken over
*realized* crossings only and is right-censored at tick 30, so it is an
ordering statistic, not an estimate of 1/p (the declared 1/p values are 4.48,
20.1, 54.6). The ordering claim is what was pre-registered and is what is
reported.

### 4.3 P3 — Kibble–Zurek analog: **CONFIRMED**

**P3a — contact-interval sweep** (3 regions, all pairs meeting every k ticks;
defects summed over 5 seeds):

| contact interval k | 2 | 3 | 5 | 10 | 15 | 30 |
|---|---:|---:|---:|---:|---:|---:|
| defects | 2 | 4 | 6 | 12 | 12 | 12 |

Monotone non-decreasing, saturating at 12 — the all-independent-nucleation
ceiling, where contact is too late to pre-empt any nucleation. Raising
contact frequency relative to the nucleation rate reduces defects by a factor
of six here.

**P3b — region-count sweep** (k = 6, all pairs meeting, so the per-pair
contact rate is held fixed):

| regions N | 2 | 3 | 4 | 5 |
|---|---:|---:|---:|---:|
| pairs | 1 | 3 | 6 | 10 |
| defects (5 seeds) | 2 | 6 | 12 | 24 |
| defects per pair per seed | 0.4 | 0.4 | 0.4 | 0.48 |

The KZ-faithful shape, and it was not designed in: **defect density per
boundary is essentially flat in N and is set by the contact (quench) rate,
while total defect count grows with system size.** That is the standard
correlation-length reading of the mechanism, recovered as an in-model
consequence of the declared rules.

### 4.4 P4 — defect permanence: **SPLIT; the strong form FAILS**

| form | outcome |
|---|---|
| **P4-strong** (defect W_rev dominates every record) | **FAILS** |
| **P4-weak** (dominates records issued at or after its tick) | holds, 6/6 defects |
| defect price growth after issuance | **+28.853900818** for every defect (4 subsequent contacts × 5/ln 2) |

Witness, seed 10007:

| record | kind | issued | final W_rev |
|---|---|---:|---:|
| `r_defect_R1_R3_audit` | defect | tick 6 | 44.723546268 |
| `r_found_R1_audit_beta` | founding (its own ancestor) | tick 2 | 103.874042944 |
| `r_base_R3` | base (ancestor) | tick 0 | 112.530213189 |

**Why it fails, structurally.** A defect record is *downstream* of the two
founding records it reconciles. S3 check (iv)'s upward nesting — un-commit
closures nest, prices weakly decrease downstream — therefore **forces** every
ancestor of a defect to price at least as high as the defect. No fixture
choice can rescue the strong form as stated; the prediction was
mis-specified, and the mis-specification is the result.

**What survives, and it is the sharper statement.** A defect's permanence is
real but it is *not located in the defect*: the defect is the mechanism by
which its ancestors become permanent. Issuing one defect adds 6/ln 2 to both
founding records' prices immediately and 5/ln 2 to them again at every
subsequent contact, because every crossing task at a defective boundary is
downstream of the founding records through the defect. **Failed reconciliation
does not make the boundary record hard to reverse; it makes the two
regions' foundations hard to reverse.**

### 4.5 P5 — the issuance/disclosure in-model signature: **SPLIT; the attribution clause FAILS**

Three arms, identical seeds and identical draw tables:
`nucleated` (types arrive by the rule; each consumes the region's current
head → **chain**), `declared` (reservoir fully declared at t = 0, every type
consuming the base record → **star**, variant chosen canonically), and
`declared_adopt` (reservoir fully declared at t = 0 → star, but variant
adoption still driven by the same seeded draws).

| clause | outcome |
|---|---|
| **P5a** attainability identical across arms | **CONFIRMED** — every region's envelope restricted to the base task family equals Env(C) bitwise, in all three arms, every seed; and every exercised type's frontier point is identical between `nucleated` and `declared_adopt` |
| **P5b** settlement and defect structure differ (nucleated vs declared) | **CONFIRMED** — defect counts per seed [2, 2, 0, 2, 0] vs [0, 0, 0, 0, 0]; founding-record price multisets differ |
| **P5c** defect channel attributable to type arrival | **FAILS** — `declared_adopt` reproduces the nucleated arm's defect signature **exactly**, seed by seed: [2, 2, 0, 2, 0] |
| **P5c** settlement channel attributable to type arrival | holds — founding-record prices differ between `nucleated` and `declared_adopt` |

Seed 10007, founding-record final prices (kBT ln 2 units):

| record | `nucleated` (chain) | `declared_adopt` (star) | `declared` (star, canonical) |
|---|---:|---:|---:|
| `r_found_R1_audit_*` | 103.874042944 | 99.545957821 | 10.098865286 |
| `r_found_R2_audit_alpha` | 60.593191717 | 54.822411554 | 10.098865286 |
| `r_found_R3_audit_alpha` | 54.822411554 | 54.822411554 | 10.098865286 |
| `r_found_R2_archive_*` | 5.770780164 | 5.770780164 | 5.770780164 |

**Reading, held to the pre-registered framing.** Three separations, and they
come apart:

1. **The attainability layer cannot see any of it.** Conservativity plus
   T583's task-gated order force it; the run certifies it bitwise. Whatever
   "arrived," nothing about what the old tasks can do changes. This is the
   packet's attainability-layer collapse, now verified along a 30-tick
   trajectory rather than at a single extension.
2. **The defect structure is not a type-arrival signature.** It is a
   *stochastic-per-region-selection* signature. A world whose type space was
   complete from the first instant, but in which each region still adopts a
   variant by a local chance event, produces bitwise the same defects. This
   deflates the naive reading of P5 and is exactly the anti-accommodation
   outcome the pre-registration named in advance.
3. **What type arrival does leave is a consumption-edge fact.** In the
   nucleated arm a type may name only what already exists as its consumption
   edge, so late types chain onto early ones; in a fully-declared reservoir
   every type names the base record and the graph is a star. That single
   contract fact is worth **10.098865286 → 103.874042944** on the same
   record at identical attainability.

Stated exactly: **the toy's in-model residue of "issuance" is not symmetry
breaking and not attainability — it is the order-dependence of admissible
consumption edges, priced by S3.** That is a statement about where a
signature could live in a model of this shape, not evidence about nature and
not an issuance verdict.

### 4.6 The reconciliation leg — the C-clock content, transplanted

The only contact-generated record content in the toy is the defect record,
and it behaves exactly as the naturality spec's C-clock form did on the twin
fixture:

- **invariant under the diagonal** variant relabeling (alpha ↔ beta applied
  to every region at once): the defect set and its stored pairs map
  consistently, count unchanged;
- **destroyed by a one-sided** relabeling (alpha ↔ beta in one region only):
  mismatches become matches and defects vanish.

So the defect record stores the **relative alignment** of the two regions'
declarations and nothing absolute — the naturality probe's observed
sharpening, reproduced on an independent fixture with a different generating
mechanism. The variant-blind control (§5) makes the same point destructively:
quotient the variant labels and the defect count collapses to zero.

### 4.7 S3 discipline legs

- **Class-axis monotonicity untouched.** Over every price realized anywhere
  in the run, A_small ⊑ A_mid ⊑ A_big never produces a record that is final
  for the larger class but not the smaller. S3 check (ii)'s direction is
  intact; the ratchet's second stroke lives on the other axis, as declared.
- **Anti-scalarization exhibit.** At price 21.640425613:
  `A_energy_poor_time_rich` is FINAL with margin (energy −9.640425613, time
  +877.359574387, …); `A_time_poor_energy_rich` is FINAL with margin
  (energy +42.359574387, time −0.640425613, …). Incomparable deficit
  patterns; no scalar exists anywhere in the toy.

## 5. Controls (all must fail closed; 8/8 did)

| control | expected | got | closed? |
|---|---|---|:-:|
| lawful nucleation (positive control) | `ADMISSIBLE` | `ADMISSIBLE` | ✓ |
| **mutation disguised as nucleation** (new type bundled with a cheapened existing task) | `EXISTING_TASK_MUTATION` | `EXISTING_TASK_MUTATION` | ✓ |
| budget-growing nucleation | `SILENT_BUDGET_GROWTH` | `SILENT_BUDGET_GROWTH` | ✓ |
| founding record consuming an undeclared record | `UNKNOWN_RECORD_CONSUMED` | `UNKNOWN_RECORD_CONSUMED` | ✓ |
| nucleation re-issuing an existing record id | `REISSUE_EXISTING_RECORD` | `REISSUE_EXISTING_RECORD` | ✓ |
| second variant into an occupied exclusive slot | `EXCLUSIVE_SLOT_ALREADY_OCCUPIED` | `EXCLUSIVE_SLOT_ALREADY_OCCUPIED` | ✓ |
| **defect rule ignoring variant identity** (variants quotiented) | 0 defects | 0 defects | ✓ |
| **zero-barrier reservoir** (Δ = 0: everything nucleates at tick 1) | one distinct defect count across the whole contact sweep | 14 at every k ∈ {2, 3, 5, 10, 15, 30} | ✓ |

The three mandated controls are the bolded rows. The first three rows are the
packet's own teeth, executed here through the packet's own `admissible`; the
mutation control is the load-bearing one, since it is what distinguishes
lawful nucleation from a revision of the past disguised as growth.

The zero-barrier control is the cleanest negative result in the set: with no
barriers, all nucleation completes before any contact, so P3's scaling
**collapses entirely** — the defect count is 14 whether regions meet every 2
ticks or once at tick 30. The KZ scaling in §4.3 is therefore genuinely
carried by the competition between the declared nucleation rate and the
declared contact rate, not by the counting geometry.

## 6. Unregistered observation — the two ontological layers

**Postdates the P1–P5 freeze; recorded as observation, never as a
pre-registered result, and it does not move anything.** Reading suggested
mid-run: the first-person layer is *local formation* (a region's own settled
structure), the third-person layer is the *reconciliation closure* (what
survives merging across regions); availability = formed **and** reconciled,
neither alone. Instantiated on data already computed: a record is
**REGION-FINAL** if it is final for A_mid inside its home region, and
**SHARED** if it is held by a region other than its home after contact
(transfer or smooth union-with-provenance). The **gap** is
region-final-but-never-shared.

| seed | region-final (base / founding) | shared (founding) | gap (base / founding) | defect residue |
|---|---|---:|---|---:|
| 10007 | 3 / 3 | 4 | 3 / 1 | 2 |
| 10009 | 3 / 2 | 2 | 3 / 1 | 2 |
| 10037 | 3 / 0 | 4 | 3 / 0 | 0 |
| 10039 | 3 / 5 | 5 | 3 / 1 | 2 |
| 10061 | 3 / 0 | 5 | 3 / 0 | 0 |

- The gap is **nonempty in every seed**, with a structural floor: a region's
  own base record is region-final and never enters cross-region structure.
- On the founding layer the gap **tracks P3a exactly**: gap = 1, 2, 3, 6, 6,
  6 across contact intervals k = 2, 3, 5, 10, 15, 30 — exactly half the
  defect count at every point. The mechanism, exhibited (seed 10007, k = 30):
  within a slot the **minority-variant region's founding record is the
  stranded one**, while the two majority regions merge smoothly and share
  each other's; a 1-versus-2 split across three regions yields two defects
  and one stranded record per slot. The factor of two is therefore
  three-region arithmetic, not a law — consistent with the gap *not* tracking
  the region-count leg below.
- It does **not** track the region-count leg: gap = 4, 3, 4, 3 for N = 2, 3,
  4, 5. The suggested prediction holds for the contact-rate knob and fails
  for the system-size knob — reported as it came out.

## 7. Boundary sentences (mandatory)

1. **The fork stays TI's.** Whether a lawful C → C⁺ is genuine issuance or
   disclosure of a larger fixed space is PP-3 / D-FORK (TI-C019, E026), owned
   by temporal-issuance, routed there by T588's fork handoff, carried here by
   pointer only and not rebuilt. A settlement-layer or defect-layer signature
   is **not** an issuance verdict; a well-defined ε does not assert that
   nature performs ε; and P5's separations are facts about a declared toy's
   path-dependence.
2. **DU seam-only; the DU STOP respected.** The record interface remains
   *supplied*, per dynamic-unity's banked no-go (HC-DU-063) and their
   autonomous-finality `NO_READY_MECHANISM` result (HC-DU-061), cited by
   pointer at their pins as in S2. Nothing here derives record-ness; no
   split-dependent quantity is passed off as representation-independent (the
   variant-relabeling legs are checked on T584 orbits); nothing asserts or
   tests whether any foliation, update ordering, or beable exists.
3. **T587's firebreak.** No capability delta, price change, grade flip,
   defect record, transfer, or new record-order edge is counted as time,
   temporal issuance, or an arrow by itself. No T-number is minted; no
   comparator is added to the frozen T586 event system; this is an
   exploration companion, not a reopening.
4. **Sealed-lab posture inherited unchanged** (schema §1.v): the toy grades
   committed records in declared contexts and takes no position on
   measurements inside sealed coherently controllable labs. Nothing here
   settles a settlement question the schema left open.
5. **Ownership per the Q-0066 registration:** TI owns the fork, TaF the
   currency (this toy), DU seam-only.

## Known Physics Constraints

None claimed. The only physical source input is T585's bounded Landauer-style
erasure cost, re-executed as source-owned input at run time; S3's ω rows enter
as declared fixture data with their declared-not-derived status inherited
unchanged. **The barriers Δ, the parameter β, the attempt probability, and
the Arrhenius/Kramers form of the rate law are DECLARED in-model parameters,
not physical constants, not fitted, and not sourced.** No nucleation rate, no
phase transition, no Kibble–Zurek exponent, and no collapse model is
established, endorsed, or used. The "Kramers ordering" and "Kibble–Zurek
analog" names are used for the *shape* of the declared dynamics and nothing
more.

## What This Does Not Claim

- **No physics of actual phase transitions.** The toy exhibits that a
  declared barrier-crossing rule plus a declared contact rule produce the
  ordering and scaling shapes those mechanisms have. It does not model,
  test, or support any claim about real nucleation, real symmetry breaking,
  real defect formation, or any KZ exponent. Nothing here is evidence about
  nature.
- **No issuance verdict, and no confirmation of the ratchet thesis.** P5's
  attribution clause *failed*; the surviving type-arrival signature is one
  narrow contract fact. Support for Q-0066 is exactly as narrow as §4.5
  states, and the failure is part of the result, not an inconvenience.
- **No claim movement.** No claim-ledger, Canon Index, hypothesis, Lane,
  guardrail, bin, or public-posture change. T583–T588, the type-extension
  packet, the naturality spec, and the S1–S6 verdicts are untouched and
  unmoved. No tick-family credit is implied or banked.
- **No T-number and no `tests/` promotion.** Un-T-numbered exploration
  companion, per the composition/type-extension companion discipline; the
  owner decides adoption.
- **Fixture-locality binds every number.** Three to five regions, five
  candidate types, three slots, thirty ticks, five seeds, one budget shape,
  three grading classes plus two incomparable ones, one contact topology.
  Every count, price, and threshold is fixture-specific; only the *structure*
  is claimed to be exercised. Nothing is asymptotic; nothing scales.
- **The naturality result is a shape-match, not an obstruction.** The defect
  record is contact-generated content that a declared cross-boundary task
  consumes in-model and that is non-natural under independent componentwise
  relabeling. That is the *shape* the naturality spec's named-but-unopened
  "non-naturalizable-reconciliation-content gate" asks about. **No obstruction
  is exhibited and that gate is not opened**: this toy tests one defect rule
  and one quotient control, and whether some natural family could generate
  operationally equivalent content is not tested here.
- **Capability remains T583's operational, executable-task measure** — not
  consciousness, cognition, awareness, or agency. A grade flip is a repriced
  feasibility fact about a declared class. The §6 "first-person /
  third-person" language is a reading label on two computed sets, and carries
  no phenomenal content whatever.
- **No promotion of unlikelihood to impossibility.** FINAL(A, r) is
  class-indexed inaccessibility; the spontaneous face stays strictly nonzero
  for every finite ω; no thermodynamic arrow is claimed (N8's
  "capability/topology residue" category, named as such).
- **No bearing on the foliation branch, and no covariant claim.** The toy is
  flat-contract only; the packet's condition (v) — covariant-scope
  admissibility, consumption restricted to J⁻ — is *not* checked here. The
  toy's contact schedule is a declared tick pattern and is not a causal
  structure.

## Uncertainties

- **P4's strong form was mis-specified, not merely refuted.** Any record
  graph in which defects are downstream of what they reconcile forces the
  observed outcome. A sharper permanence question — is there a class of
  contact-generated records whose price outruns their own ancestors? —
  requires a different graph shape (e.g. defects that are *consumed by* the
  founding records, or boundary-owned records with no regional ancestors)
  and is unbuilt.
- **P5's third arm is one disambiguation, not an exhaustive one.** Other
  declared-up-front arms are constructible (canonical adoption with
  order-dependent consumption edges, or arrival-ordered declaration with star
  edges) and would further factor the signature. Four such arms would
  saturate the 2 × 2; two were run.
- **The chain/star contrast is a declared modeling choice.** That a newly
  arriving type consumes the region's *current head* is a toy rule, not a
  contract law. The packet's record-interface discipline permits many
  consumption edges; a different declared rule would change the magnitude of
  §4.5's separation and possibly its existence. This is the largest single
  soft spot in the sharpest finding, and it is named rather than buried.
- **Degenerate variants are a declared idealization.** Exclusive variants
  carry identical performance points so that variant relabeling is a genuine
  T584 representation morphism. Non-degenerate variants would make the
  relabeling inadmissible and change the §4.6 leg entirely.
- **The P3b leg holds the per-pair contact rate fixed by fiat** (all pairs
  meet at every contact tick). Under the alternative declared schedule (one
  pair per contact tick), region count and per-pair contact rate move
  together and the legs no longer separate. Both are in the model; only the
  isolating one is reported for P3b.
- **Five seeds is a small sample.** P2's ordering is reported on aggregate
  counts over 15 opportunities per slot; per-seed inversions are possible and
  are not claimed against. The zero-barrier and variant-blind controls are
  deterministic and do not depend on sample size.
- **Grading uses one budget shape.** All three chain classes vary only in
  energy; time, communication, memory, and error budgets are fixed. The
  anti-scalarization exhibit uses the two deliberately incomparable classes,
  but the finality trajectories are effectively energy-graded.

## Constructive next objects (named, not built)

1. **The permanence-shape question** left by P4: a record graph in which
   contact-generated content is not dominated by its own ancestors, and
   whether "permanent" can mean anything else in an S3-graded fixture.
2. **The 2 × 2 arm saturation** for P5: separate consumption-edge order from
   variant-selection stochasticity completely, rather than at two corners.
3. **The covariant leg** of the toy: re-declare regions as causal diamonds
   and the contact schedule as actual causal contact, so that condition (v)
   (consumption restricted to J⁻) can be checked — the toy currently ignores
   it and says so.

## Provenance

- **Writer lock checked before any write:**
  `git rev-parse --git-path capacityos-writer.lock` →
  `.git/capacityos-writer.lock`, **not present**. Repository HEAD at read and
  write time: `cb2d43f`, working tree otherwise clean. This arm performs
  **file writes only** — no commit, no push, no branch. Its writes are
  exactly this file and `models/nucleation_ratchet_toy.py`.
- **Read in full before drafting:**
  proposed-type-extension-morphism-gate-2026-07-28.md and
  `models/type_extension_witness_probe.py` (the ε class, the conservativity /
  anti-revisionism law, budget and record-interface discipline, the
  SPLIT-BY-LAYER result — the probe's `admissible` is *imported and called*,
  not reimplemented); record-layer-naturality-spec-2026-07-28.md and
  `models/record_reconciliation_naturality_probe.py` (the reconciliation forms
  and the C-clock finding); commit-module-s3-capability-graded-finality-
  2026-07-28.md §§1–4 (commit(A, r), W_rev, the grade, checks (i)–(iv), the
  anti-scalarization discipline); commit-module-s2-redundancy-issuance-
  2026-07-28.md §6 (the TI boundary sentence, adopted as this toy's pattern);
  commit-module-schema-2026-07-28.md §1.v (scope, sealed labs); and
  `models/t583_capability_contract_v1.py` /
  `models/t585_landauer_physical_capability_gate.py` at the interfaces
  consumed (`attainable_envelope`, `point_is_feasible`, `Budget`,
  `PerformancePoint`, `_base_context`, `_points_for_state`).
- **Model run:** `python3 -B -m models.nucleation_ratchet_toy` from the
  repository root; **exit 0**; 7/7 structural checks pass; 8/8 controls fail
  closed; output verified **byte-identical across three consecutive runs**
  (md5 match). 619 lines — well over the type-extension companion's 271, and
  reported rather than smoothed: the simulation core (reservoir, nucleation,
  ε application, reconciliation, S3 pricing) is about 210 lines, and the
  overage is the five pre-registered legs, each of which runs its own sweep
  or arm set, plus the eight-control slate. Determinism: five fixed literal integer seeds, one
  `random.Random` stream per (seed, region, slot) with sub-seeds derived by
  fixed integer arithmetic; no wall-clock, no date, no OS entropy, no hashing
  of strings, no floating-point accumulation order dependence (all sums taken
  over sorted keys, all prices rounded to 9 dp). T585 is re-executed at run
  time as source-owned physical input rather than consumed from cache.
- **Prediction outcomes are data, not assertions.** The exit code is gated by
  the structural checks and the must-fail controls only; P1–P5 statuses do
  not gate it, precisely so that a failing prediction cannot create pressure
  to tune the model. P4-strong and P5c failed and the run still exits 0, by
  design and by pre-registration.
- **Q-0066** is cited by pointer to the private thinking-wiki registration
  only; no private content beyond the registration's existence, its ownership
  line, and phrasing already public in-repo is imported. The mid-run
  interpretive suggestion recorded in §6 postdates the P1–P5 freeze and is
  labeled as an unregistered observation throughout.
- **No fetches this run.** No external physics enters beyond T585's source law
  and S3's declared ω rows, both in-repo. No literature is cited, imported, or
  depth-upgraded.

## CORRECTION (2026-07-28, post-landing council review): the "sharpest finding" magnitude is refuted by this note's own §4.5 table

**The headline as written is wrong, and the refutation is already in this
file.** The stated finding — that the consumption-edge fact is "worth an
order of magnitude in settlement price," quoting 10.098865286 against
103.874042944 — compares two arms that differ in **two** variables at once:
graph shape (star vs chain) *and* defect count (0 vs 2). This note's own
third arm isolates them, and its price is printed in §4.5:

| arm | closure size | Σω | price |
|---|---:|---:|---:|
| `nucleated` (chain, 2 defects) | 14 | 72.0 | 103.874042944 |
| `declared_adopt` (star, 2 defects) | 13 | 69.0 | 99.545957821 |
| `declared` (star, 0 defects) | 1 | 7.0 | 10.098865286 |

The consumption-edge effect is the **chain vs `declared_adopt`**
difference: exactly one record (`r_found_R1_mint_solo`, ω = 3.0), i.e.
**4.328085122 units — 4.6% of the quoted gap.** The remaining 95.4%
belongs to the defect/crossing channel, which §4.5 reading item 2
explicitly declares is **not** a type-arrival signature. The headline
therefore claimed a magnitude that belongs to the mechanism this note
itself disclaims.

**Scaling makes it worse, not better** (tick sweep re-run by the closing
adversarial pass): the consumption-edge effect is **constant in run
length** — bounded above by Σω of types arriving later in the region,
≲ 20.2 units in this fixture — while the defect channel grows without
bound. Chain share of the quoted gap at 30 / 60 / 120 / 240 ticks:
**4.6% / 2.6% / 1.4% / 0.7%.** "An order of magnitude" is an artifact of
the 30-tick configuration.

**Corrected statement, which is smaller, true, and still worth having:**

> A lawful consumption-edge order contributes a **bounded,
> run-length-invariant** settlement increment — 4.328085122 units on the
> headline record, ≤ Σω of later-arriving types in general — while the
> unbounded part of the quoted gap belongs to the stochastic-selection
> channel this note declares is not a type-arrival signature.

**Two further corrections to this file's own framing.** (i) The
Uncertainties section describes the chain/star edge rule as the "largest
single soft spot" whose magnitude "a different declared rule would
change," i.e. as *untested*. It was tested — by this note's third arm,
whose result sits in §4.5. The soft-spot paragraph misdescribes the
evidentiary state. (ii) P3b's flat defect density is **not** a
KZ-faithful shape that "was not designed in": the sub-seed derivation
makes a region's draws independent of how many regions the configuration
contains, which forces N-independent per-pair mismatch probability and
hence flat density by construction. Without Kibble–Zurek sources in the
repository (currently zero), this result cannot distinguish KZ scaling
from Poisson thinning. The zero-barrier control remains a genuine
negative control.

**Independent corroboration, arrived within hours and not consumed here
until now:** `dynamic-unity#explorations/record-graph-settlement-and-delayed-activation-nonidentifiability-2026-07-28.md`
(HC-DU-087, citing `time-as-finality` revision 9981cb1 as external input)
reached the same conclusion — *"a real difference between those two
implementations… not a signature of type arrival. The comparison changed
two variables together"* — and supplies the hostile arm named unbuilt
here: dormant-then-activated types under the same head-consumption rule
produce a graph **identical** to the nucleated arm.

**What survives this correction, unchanged:** P5c's failure (the defect
structure is a selection signature, not a type-arrival signature — now
independently corroborated), P4's failure and its replacement (failed
reconciliation hardens the foundations, not the boundary — forced by
closure nesting in any DAG), P1, P2, P3a, and the attainability-layer
conservation. The correction removes a magnitude claim, not a result.
