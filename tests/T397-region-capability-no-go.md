# T397: Region-Indexed Capability No-Go

## Route

Quantum foundations / bounded control regions / capability objects. First
executable instance of the **bounded-region capability assignment C(R)**
named in the tri-repo meta-synthesis
(`audits/2026-07-01-tri-repo-synthesis-hegelian-metasynthesis.md`,
Section 4), built as Hegelian survivor (a) of that document's persona-panel
pass: "a **region-indexed capability no-go** with a declared within-region
intervention menu." Direction A's next rung in its capability-phrased form
(the swing report's constraint: any record-order criterion must be stated at
the capability level, at k >= 3, not in marginal statistics).

## Claim

In a finite, exactly-simulable k = 3 order-superposition family (T395's
canonical switch subset) with a fixed bounded region, a declared finite
intervention menu, and a declared task set, three legs hold jointly:

1. **C(R) is real and region-indexed.** The achievable-task profile
   C(R) = (undo_within, undo_cross, order_postdiction, class_readout) is
   exactly computable per configuration; menu-achieved values equal
   closed-form optima; every failed undo leg is certified impossible for
   **all** channels supported on R (T393's certificate pattern), not merely
   for the menu.

2. **Anti-scalar at the capability level.** The realized "can-do" order on
   configurations (componentwise comparison of profiles) is a genuine
   partial order with incomparable pairs — the realized poset is the exact
   product of an undo chain and a readout chain (a 3 x 4 grid), with order
   dimension exactly 2 (computed with T394's imported checkers). By T394
   Theorem 2 (T49's Anti-Scalar Theorem as the d = 1 rung, tie-collapse
   closed), **no scalar capability monotone reproduces the enactability
   order**; two monotone axes do, and are exhibited.

3. **Statistics underdetermine capability (quantified no-go).** The declared
   non-capability probes — the computational-basis readout distribution over
   R (the house's ordinary event-level record convention, T392), with all
   marginals, at every swept preparation phase — are **exactly equal (max
   diff 0.0)** across a 16-configuration class that realizes **all 12**
   distinct capability profiles. Hence no functional of the declared
   R-statistics decides any capability-typed test that varies on the class
   (finite enumeration proof within the family). The featured
   statistics-identical pair is capability-INCOMPARABLE with gaps >= 0.5 in
   both directions; screening-off failure is certified with T392's imported
   Bayes-risk / CMI machinery. Conversely, a capability-identical pair
   differs in statistics: **neither typing refines the other.**

Failure of any leg would have been the reportable verdict (see Failure
Conditions); all three legs passed as stated.

## Class

**Exploratory, capability-object lineage.** First artifact of the C(R)
object named in the meta-synthesis (Section 4) and the Direction A
capability-phrased rung (its Section 5, OPEN lane 1). NOT registered in
CLAIM-LEDGER, deliberately: this is the definitional instance, not a claim
promotion. Lineage: T392/T393 (reversal capability at fixed data;
region-relative finality), T394 (order dimension; anti-scalar hierarchy),
T395 (k >= 3 partial records; capability-relative accessibility boundary),
T49 (Anti-Scalar), s6-g9 (same-final-record capability pair, formal side).
Promotion toward anything ledger-facing would require, at minimum: the
resource-theory absorber run (below), verified prior art, and a pause for
Joe per AGENTS.md.

## Status

Implemented; all three legs hold in this finite family. 34 tests green;
T392/T393/T394/T395 suites re-run alongside, still green (111 passed). No
claim promotion; no CLAIM-LEDGER entry; all decisions pause for Joe.

**Numbering collision, flagged for Joe:** while this artifact was being
built, another lane landed a complete quartet also numbered T397
(`tests/T397-multipath-class-marker-absorber.md` — the T395-recommended
multipath absorber run, timestamped before this spec registered). Distinct
slugs; both quartets intact; renumbering pauses for Joe per house precedent
(the session mount forbids renames). Substantively the two artifacts
compose: the absorber's verdict (T395's k >= 3 class-coarse signature is
generic multipath class-marker algebra) closes the statistics-side route,
which is exactly why this artifact's capability-side route is Direction A's
surviving rung.

## Target Claims

- Bounded-region capability assignment `C(R)` (meta-synthesis Section 4;
  exploratory working object — this artifact is its first instance)
- [T392: Fixed-SBS-Key Reversal Divergence Witness](T392-fixed-sbs-key-reversal-divergence-witness.md) (the "same data, different capability" pattern; machinery imported)
- [T393: Causal Forcing of the Access Asymmetry](T393-causal-forcing-of-access-asymmetry.md) (region + escape constructions; certificate pattern and grids imported)
- [T394: Axis-Count Reconstruction Hierarchy](T394-axis-count-reconstruction-hierarchy.md) (order-dimension checkers imported; Theorem 2 cited for the anti-scalar consequence)
- [T395: Record-Order Trade-off Probe](T395-record-order-tradeoff-probe.md) (k = 3 switch family imported; the capability-relative boundary this artifact builds on)
- [T49: Reconstruction Without Background Time](T49-reconstruction-without-background-time.md) (lineage; not upgraded)
- [Q1D: Contextuality And No-Signalling Guardrail](../claims/Q1D-contextuality-no-signalling-guardrail.md) (guardrail)
- [R1: Relativity And No Global Commit Order](../claims/R1-relativity-no-global-commit-order.md) (guardrail; untouched)

## Definitions (R, M, T, C(R))

**Region R** (declared once, uniformly for every configuration): the qubit
subset {c, r1, r2, t} — the 3-level order control, the two-qubit record
register, and the target. Outside R: the escape registers {e1, e2}. The
record sub-region {r1, r2} is the declared access for the readout tasks
(postdicting the order from the record, T395's D pattern; measuring c would
trivialize postdiction and is disclosed as such — c's readout still belongs
to the declared R statistics). Region membership is DECLARED here; T393 is
the artifact that showed such declarations can be causally forced (Tier 1,
conditional on emission), and re-deriving forcing is out of scope.

**Intervention menu M** (declared once, finite, config-independent):

- 16 unitary protocols: all ordered compositions of the four uncompute
  generators, each supported on R — c-controlled `Z^class` on r1,
  c-controlled `Z^class H` on r1, c-controlled `Z^fine` on r2, c-controlled
  inverse order unitary on t — including do-nothing.
- 4 measurement settings on the record sub-region ({Z, X} x {Z, X}) with
  optimal classical post-processing, computed exactly.

**Task set T** (declared, thresholds predeclared):

1. `undo_within`: phase-locked normalized visibility of the within-class
   control pair (0, 2), best over menu protocols; pass at `v* = 0.9`
   (`V_STAR` imported from T392/T393, unchanged).
2. `undo_cross`: same for the cross-class pair (0, 1); pass at `v*`.
3. `order_postdiction`: optimal k = 3 order discrimination from the record
   sub-region alone; pass at `p* = 0.9`.
4. `class_readout`: optimal binary class discrimination from the record
   sub-region (priors 2/3, 1/3, Helstrom); pass at `c* = 0.9`.

**C(R)**: the 4-vector of optimal task values, per configuration. The
enactability order: config X <= config Y iff Y's profile dominates X's
componentwise ("Y can do everything X can, at least as well, on the
declared task set").

**Configuration family** (declared exhaustively — no cherry-picking): all
24 = 3 x 2 x 4 combinations of r1-write in {none, class_phase,
class_zbasis}, r2-write in {none, fine_phase}, e-write in {none, class,
full, burn}. Records are written as c-controlled phase flips on |+>
registers (invisible to the declared Z readout) except the disclosed
z-basis control write (the statistics-visible control); escape writes copy
the class / the full order / an uncorrelated excitation ("burn", the T393
B'-analog) onto the escape registers.

**Declared non-capability probes (the "statistics" of Leg 3)**: the exact
joint computational-basis readout distribution over R — the house's
ordinary event-level record convention (T392's `R`, T162's pointer basis) —
including all its marginals, at the unphased preparation and at every
certificate phase for both phase placements. Probes from the intervention
menu (e.g., X-basis record readout) are capability-typed by definition;
the statistics/capability boundary is exactly the declared-readout /
declared-menu boundary, stated openly (see Honest Reviewer Attack Surface).

## Setup

Exact statevector, numpy, deterministic; nothing that carries a verdict is
sampled. `models/region_capability_no_go.py`. Subsystems INDEX-SORTED
(c, r1, r2, e1, e2, t), dims (3, 2, 2, 2, 2, 2), total Hilbert dimension 96
(inside the 10-qubit budget). Orders: T395's canonical 3-order subset
{ABC, BAC, CAB} with class partition "A before B" (class_of = [0, 1, 0]),
fine bit [0, 0, 1]; canonical operations A = Ry(pi/2), B = Rz(pi/2),
C = Rx(pi/2) imported from T395 (local builder asserted equal to T395's
`u_of_order`). Gate-built and branch-sum constructions asserted equal
(max diff 3.9e-17).

Imports, by name: T394's `minimal_axis_count`, `incomparable_pairs`,
`is_chain`, `verify_reconstruction`, `magnitudes_from_realizer`,
`weak_orders`; T393's `PHI_LOCK_GRID` (uniform 8-point locking grid) and
`PHI_CERT` (certificate sweep with incommensurate phases); T392's `V_STAR`,
`_bayes_risk`, `_conditional_mutual_information`; T395's k = 3 family and
statevector primitives. T393's region/escape machinery is adapted (its
helpers are hard-wired to a 9-qubit register layout; this model has
mixed-dimension subsystems), with the phi-independence certificate and the
channel-independent trace-norm bound re-implemented generically and cited.

## The Three Legs (what was verified, exactly)

### Leg 1 — capability profiles are real and region-indexed

- All 24 profiles computed exactly; **12 distinct profiles** realized.
- Menu-achieved readout values equal closed-form optima (orthogonal-group
  counting for order postdiction — guarded: the code raises if the family
  ever leaves the identical-or-orthogonal record regime; Helstrom trace-norm
  for class readout): max residual `8.9e-16`.
- **All 18 zero-valued undo legs certified against all R-channels**: the
  region-reduced state is exactly phi-independent across the T393 sweep
  (worst pairwise diff `4.2e-17` < 1e-12), and the T393-style
  channel-independent bound `3(||Re X||_1 + ||Im X||_1)`,
  `X = mean_phi e^{i phi} rho_R(phi)`, is numerically zero (worst
  `3.8e-16`), covering every CPTP map supported on R at once. Pass legs
  show genuine phi-dependence (floor `0.102` > 0.1 — teeth).
- Undo figure of merit is phase-locked (T392's gameability lemma): the
  manufactured-coherence cheat channel (discard c, re-prepare a coherent
  c state — a valid R-supported channel) achieves raw normalized coherence
  1.5 and locked visibility `3.9e-17`. Implemented as a null control.
- Haar spot check (20 seeded unitaries on R, illustrative only):
  max locked visibility `3.3e-17` < 0.05.
- Family-wide structural fact: `undo_within >= undo_cross` everywhere
  (escaping the class kills cross-class undo before within-class undo —
  T395's within-class-coherence-survives structure, here at the capability
  level).

### Leg 2 — anti-scalar at the capability level

- The realized capability poset: 12 profiles, 48 comparable pairs, **18
  incomparable pairs** (C(12,2) = 66 accounted exactly), not a chain.
- **The poset is the exact product order of an undo chain (3 levels:
  (0,0) < (1,0) < (1,1)) and a readout chain (4 levels: (1/3,2/3) <
  (2/3,2/3) < (2/3,1) < (1,1))** — a 3 x 4 grid, verified pairwise; Hasse
  edge count 17 = 3(4-1) + 4(3-1).
- **Order dimension exactly 2**, computed by T394's exhaustive realizer
  search; the 2-realizer's rank magnitudes verified to reconstruct the
  order on all pairs (T394 `verify_reconstruction`). Dimension >= 2 already
  follows from any incomparable pair (T394 Theorem 2 = T49's Anti-Scalar
  rung, with T394's tie-collapse closure covering scalar monotones with
  ties).
- **Scalar failure witnessed concretely, not just by citation**:
  (i) exhaustive scan of ALL 4,683 weak orders (total preorders — the order
  structure of any real-valued scalar, ties allowed) on the 6-profile
  spotlight subfamily: **0 reproduce** the enactability order;
  restriction-complete (a scalar reproducing the family order restricts to
  every subfamily). (ii) Per-pair trichotomy witnesses: for
  (pristine, publisher), `f(pristine) <= f(publisher)` denies pristine's
  strict undo advantages (gaps 1.0), `f(publisher) <= f(pristine)` denies
  publisher's strict readout advantages (gaps 2/3, 1/3), and a real-valued
  f must satisfy one of the two.
- Interpretive bonus, priced honestly: the two exhibited monotone axes
  (undo strength, readout strength) are an exact 2-axis capability
  coordinate system for THIS family; nothing is claimed beyond it (richer
  escape structures could realize higher dimension — T394's S_d ladder is
  the named continuation).

### Leg 3 — statistics underdetermine capability

- **Statistics partition of the 24 configurations: exactly 2 classes,
  sizes 16 and 8** (max intra-class diff exactly 0.0; min inter-class diff
  0.083 — teeth). The 16-class (all phase-basis writes, all escape modes)
  **realizes all 12 capability profiles**: any functional of the declared
  R-statistics is constant on a set spanning the entire realized C(R)
  range. The capability-typed test `undo_cross >= v*` takes both values
  (8 pass / 8 fail) on that class — no statistics-typed functional decides
  it (finite enumeration proof).
- **Featured pair** (pristine vs publisher): declared statistics exactly
  equal (max diff 0.0 over 13 phase/placement combinations), profiles
  (1, 1, 1/3, 2/3) vs (0, 0, 1, 1) — INCOMPARABLE, with max gap 1.0 in
  pristine's directions and 2/3 in publisher's (both >= the predeclared
  floor 0.5).
- **Screening-off failure, certified with T392's machinery**: decision
  problem = equal-prior config mixture, verdict = the capability verdict
  (fixed map from the certified undo_cross axis, T150 discipline). The full
  declared readout gives zero lift on all three losses (T155 discipline)
  and `I(V; S) = 1.3e-15` bits; one declared menu probe (record in X x X,
  (c, t) in Z) gives lift `1/3` on all three losses and
  `I(V; probe | probe's statistics part) = 2/3` bits exactly. T137-style
  downstream transform of the statistics: zero lift, zero CMI.
- **Null controls (non-vacuity)**: (i) the same statistics-typed functional
  family DOES distinguish (pristine, z_keeper): lift 0.25 — the equality
  certificates are not vacuous. (ii) The converse pair
  (class_keeper, z_keeper): capability profiles identical (diff 4.4e-16),
  statistics distinct (0.083) — capability does not determine statistics
  either; the two typings are mutually non-reducing. (iii) Burn null (T393
  B'-analog): a real, order-uncorrelated emission (excitation probability
  1.0 vs 0.0) moves neither the profile nor the statistics (both 0.0).

## Gates / Guardrails

- **Q1D (no-signalling), asserted numerically**: the declared R readout is
  exactly independent of the preparation phase (2.8e-17), of the
  escape-register writes (0.0 — outside-region couplings cannot steer the
  declared readout), and of the target-operation settings on the (c, r1,
  r2) marginal (4.2e-17), while the same settings move the target marginal
  by 0.130 (teeth). Disclosed: a single target traverses all operations;
  the asserted surface is non-steerability of the declared readout, not
  Bell-style spacelike independence (same disclosure as T395).
- **R1: untouched.** No claim about global temporal order, simultaneity, or
  spacetime. "Order" always means composition order of operations.
- **T137/T150/T155 discipline** inherited via the imported T392 machinery:
  verdict is a fixed map from an independently certified axis, both verdict
  classes carry 0.5 prior mass, lift is verified across a three-loss
  family, and the downstream-transform null is implemented.
- Verdict vocabulary predeclared as module constants, asserted verbatim.

## Neighbors / Prior Art

In-repo:

- **T392** — the "same data, different capability" pattern this artifact
  generalizes from one capability axis (reversal) to a profile; its
  Bayes-risk/CMI machinery is imported.
- **T393** — the region/escape construction and the two impossibility
  certificates (phi-independence; channel-independent trace-norm bound),
  adapted here to mixed-dimension subsystems; also the reason the declared
  region boundary is not a free parameter in principle (Tier-1 forcing,
  conditional on emission — cited, not re-derived).
- **T394** — supplies the dimension theory: Theorem 2 makes "no scalar"
  rigorous including tie-collapse; its checkers compute the realized
  dimension here. This artifact is the first PHYSICAL instantiation of a
  T394 capability poset (T394's magnitudes were abstract ranks).
- **T395** — the k = 3 switch family and the class-coarse record structure;
  its accessibility result (record read vs ignored moves no process
  marginal) is the capability-relative boundary this artifact turns into a
  three-leg object. The within-class/cross-class coherence split powers the
  undo-axis levels.
- **T49 / T50** — the anti-scalar lineage (d = 1 rung).
- **s6-g9** — same-final-record capability pair (formal presheaf side); no
  quantum dynamics, no menu, no statistics certificates.
- **T118 / T162** — the fixed-data collapse and SBS-key factorization this
  family deliberately does not re-litigate (records here are coherent
  phase-basis objects, not SBS-closed pointer records; no SBS key is
  claimed fixed — see Honest Reviewer Attack Surface).
- **T397 (multipath class-marker absorber; the number-collision twin)** —
  the other lane's absorber run of T395's k >= 3 residue: verdict absorbed
  (the class-coarse record signature is generic multipath class-marker
  algebra). Complementary, not competing: it closes the statistics-side
  scalarization route, leaving the capability-phrased route built here.
- **open-problems/region-indexed-capability-discriminator.md** — the same
  lane's card for this very object, seeded from the same meta-synthesis.
  This artifact instantiates its `C(R, M)` at the declared-readout level.
  The card's STRONGER fixture shape — exact equality also for statistics
  under all in-region interventions, with only a boundary-crossing menu
  separating — is NOT delivered here, and within this family it cannot be
  delivered by R-supported tasks at all: if all in-region interventional
  statistics agree, the region states agree, and every R-task value is a
  functional of the region-state family. That form needs boundary-crossing
  task support (T393's counterfactual-enlargement direction), named as open.

Candidate prior art (ALL from memory — flagged, unverified, none cited as
fact; per the no-fake-citations rule nothing enters `literature/` without
verification). **This is the absorber a reviewer will raise, priced now:**

- **Resource theories** — capability profiles resemble resource-monotone
  vectors; "no total order on resources / incomparable pairs under free
  operations" is STANDARD there (entanglement: Nielsen's majorization
  theorem and LOCC-incomparable states, ~1999; resource theories of
  coherence and asymmetry — from memory). The anti-scalar THEOREM-SHAPE of
  Leg 2 is therefore not new mathematics and is presumed absorbed. The
  residue claimed is the region-indexing (the same physical family, one
  declared boundary, tasks split by what escapes it), the record-access
  physicality (class-coarse vs full vs escaped records realizing the grid),
  and the exact statistics-flat family (Leg 3) — none of which the
  resource-theory frame supplies by itself.
- **Comparison of statistical experiments (Blackwell)** — Leg 3's
  "statistics equal, capability different" is adjacent to
  sufficiency/deficiency orderings; the repo's own T155 lineage already
  guards this side. The quantum version (equal declared readouts, different
  achievable-task sets under a declared menu) is the specific finite form
  built here.
- **Constructor theory** (possible/impossible transformations as the
  primitive) — the philosophical frame for capability-typing; persona 24's
  case in the meta-synthesis. No constructor-theoretic formalism is used or
  claimed.
- **Quantum Darwinism / SBS** — record-access structures; the repo's N10/
  T162 lineage. Here records are deliberately coherent (phase-basis), so
  SBS closure keys do not apply as-is.
- **Interventionist causality (Pearl-style)** — the meta-synthesis
  antithesis (persona 19): "capabilities are statistics-under-intervention."
  Leg 3 is scoped exactly as that antithesis's synthesis demands: the no-go
  is relative to the DECLARED readout (observational statistics); the menu
  IS interventional, and menu probes do distinguish the featured pair —
  stated openly, not hidden.

## Honest Reviewer Attack Surface

- **"The statistics/capability boundary is gerrymandered: X-basis readout
  is a 'capability probe' but Z-basis readout is 'statistics'."** Answer:
  the boundary is the house's own declared-record convention (T392's
  ordinary event-level record; T162's pointer basis), fixed before this
  artifact and used unchanged. The claim is exactly that THIS boundary —
  the one the repo's record vocabulary already commits to — is where
  capability and statistics diverge; the converse pair (capability-equal,
  statistics-distinct) shows neither typing refines the other, so the
  result is a two-directional independence, not a rigged one-way gap.
  Everything is relative to the declared readout and declared menu, stated
  in the Definitions.
- **"The incomparability is manufactured by task choice."** The tasks are
  the house's own named capability axes (undo = T392/T393's reversal axis;
  order postdiction = T395's D; class readout = T395's class Helstrom),
  with thresholds predeclared (v* imported unchanged), and the
  configuration family is the full declared write-product — swept
  exhaustively, no configuration selected post hoc.
- **"Resource theory already owns this."** Priced above; the theorem-shape
  is presumed absorbed, the residue is the region-indexed physical
  realization plus the exact statistical flatness. If verification of the
  prior art shows even the residue is standard, that finding would be
  recorded and the artifact re-scoped — the absorber run is the named next
  step and gates any promotion.
- **"The undo values are 0/1 — the profile grid is a knife-edge of perfect
  couplings."** True and disclosed: records and escape copies are perfect
  (CNOT-grade). T393's partial-amplitude machinery (thresholded forcing for
  alpha >= 0.75 pi) is the named tool for a graded v0.2; the grid would
  deform but the incomparability certificates are threshold-based
  (v* = 0.9) precisely so that partial-amplitude versions can inherit them.
- **"The region is declared, not physical."** As in T393's second attack
  line: declared once, uniformly, with T393's Tier-1 forcing (conditional
  on emission) cited as the mechanism that removes the declaration's
  freedom; the residual premise is that the apparatus has SOME bounded
  control region.
- **"c is in R, so 'order postdiction from the record' ignores available
  information."** Disclosed in Definitions: reading c trivializes order
  postdiction (c IS the order register); the task is the record-holder's
  capability (T395's D), and the declared statistics nevertheless include
  c's readout — the Leg-3 equality is asserted on the full R readout
  including c.

## Failure Conditions

- Any tuning of v*, p*, c*, CAP_GAP_MIN, the phase grids, or the
  configuration family to force a leg; all were fixed before profiles were
  inspected (v* imported unchanged from T392/T393; grids imported unchanged
  from T393; the family is the full write-product).
- Leg 1 fails if any menu value exceeds its closed-form optimum, any
  zero-leg certificate fails (phi-dependence found, or channel bound above
  v*), or the manufactured-coherence cheat scores on the locked metric.
  Reportable verdict: "C(R) not menu-robust / not certifiable in this
  family."
- Leg 2 fails if the realized profiles form a chain (no incomparable pair)
  or any weak order reproduces the enactability order. Reportable verdict:
  "capability order scalarizes — anti-scalar fails at the capability
  level."
- Leg 3 fails if no statistics-flat pair with capability gap >= 0.5 in both
  directions exists in the family. Reportable verdict: "capability-
  statistics rigidity at k = 3" — this would itself have been the headline
  result, written up as such (predeclared in the assignment; did not
  occur).
- Claiming any leg beyond the declared family, menu, readout convention, or
  thresholds; claiming novelty over the resource-theory absorber before it
  is run; any hidden-variable reading of the order superposition (Q1D); any
  spacetime claim (R1).

## Known Physics Constraints

- No-cloning respected: escape registers copy only class/fine values of the
  already-branched order degree of freedom (controlled-X in the c basis).
- All menu operations are genuine unitaries/channels supported on R; the
  impossibility side quantifies over all CPTP maps on R via the trace-norm
  bound (no channel enumeration).
- The 3-level control is embeddable in 2 qubits; total Hilbert dimension 96
  (< 2^7). Exact statevector throughout; the only randomness (Haar spot
  check) is seeded, illustrative, and carries no verdict.
- Perfect-coupling idealization disclosed (see attack surface); the
  partial-amplitude deformation is the named v0.2 card.

## What This Does Not Earn

- **No claim promotion, no CLAIM-LEDGER entry.** The C(R) object remains
  exploratory; every promotion decision pauses for Joe per AGENTS.md.
- **Not TI's source-side surplus.** Ext_S requires surplus over
  capability-typed readout; this artifact CONSTRUCTS capability-typed
  readout and shows statistics underdetermine it — it says nothing about
  what issuance adds beyond capability. Explicitly out of scope.
- **No new mathematics.** Leg 2's theorem-shape is T394's (itself presumed
  a re-derivation of classical dimension theory); the anti-scalar-in-
  resource-theories absorber is presumed to own the shape until the
  absorber run says otherwise.
- **No physical-agent claim.** "Capability" here is menu-relative and
  family-relative; that profiles are menu-robust in THIS family (readout
  optima are global optima; undo impossibility is all-channel) is a feature
  of the family, not a general fact.
- **No hardware, platform, or experimental claim**; no external-facing
  artifact. All flagged prior art is from memory and unverified.
- The interpretive reading (undo strength and readout strength as "the two
  capability axes") is scoped to this family; higher-dimensional capability
  posets are not exhibited (T394's S_d ladder names where they would come
  from).

## Reproduction

```bash
python -m pytest tests/test_region_capability_no_go.py -v
python -m models.region_capability_no_go
```

Deterministic; ~5 s each.

## Contribution Needed

- **The resource-theory absorber run** (gates any promotion): map the
  profile poset onto a declared resource-theoretic frame (LOCC/majorization
  or coherence monotones, once verified against the literature) and test
  whether the region-indexed residue survives — the exact analog of T395's
  own kill-test pattern, one level up.
- Partial-amplitude version (graded undo values via controlled-Ry escape,
  T393's alpha sweep): does the grid deform into a poset with MORE
  incomparability, or does thresholding restore the grid?
- Higher-dimensional capability posets: engineer escape structures
  realizing T394's S_3 (dimension 3) at the capability level — the first
  step toward "how much capability structure can a bounded region hide from
  its statistics."
- The TI-side twin (the meta-synthesis's survivor (a) second half): rewrite
  the Ext_S burden as a region-indexed task that capability-typed readout
  provably cannot perform, using this artifact's C(R) as the readout side.
  TI-owned; pauses for Joe.
- Verify the flagged prior art before anything external-facing.
