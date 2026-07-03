# Capability-Boundary Mode Taxonomy — adopted internal reference

## Status

**Adopted internal organizing map (a frame, not a promoted claim).** Ratified as
the program's working classification of capability/finality boundaries (Joe, chat
2026-07-02). This is *not* a CLAIM-LEDGER entry, a theorem, or new physics — it is
the lens the program uses to classify any boundary attempt, and every mode has an
**established literature home** (see novelty note). Provenance:
`open-problems/finite-closed-capability-boundary-scope-theorem.md` (the derivation
and its withdrawn universal-theorem framing), the adversarial review
(`literature/Adversarial Referee Report ...`), and the prior-art verification
(`papers/drafts/prior-art-verification-and-divergent-direction-pass-2026-07-02.md`).

## The map

A **capability boundary** separates two configurations that are identical to a
bounded region `R` (agree on the observable algebra `⟨M_R⟩`) yet differ in an
enactable/recoverable transformation. By the algebraic Declarability Lemma the
separating datum is always present in the global algebra — so a boundary is either
**informationally declared** or **physically forced**, and forcing comes in three
modes. Four modes total, always stated relative to a declared class `A` of
admissible enlargements (A0 own-region ⊂ A1 ancilla/region ⊂ A2 resource/reference-
frame ⊂ A_all):

| Mode | What forces the boundary | Regime | Established home |
| --- | --- | --- | --- |
| **E0 — declared** | recoverable by some admissible enlargement (e.g. admit the co-present registers); a stipulated trace / fiat restriction. Collapses (joint-record completion). | both | access-restriction; Koashi–Imoto read-only/inaccessible split |
| **E1 — asymptotic / limit gap** | recovery cost or non-locality diverges only in a *family/limit*; a limit-invariant, not single-instance | both (family-level) | **Kadanoff extended-singularity theorem**; Butterfield; Landsman |
| **E2 — forcing assumption (hardness)** | no *feasible* admissible procedure recovers it across the family, conditional on a hardness hypothesis | both (family-level) | computational indistinguishability (Goldwasser–Micali; Yao) |
| **E3 — structural symmetry / conservation-law no-go** | an exact, single-instance impossibility on physical states under a symmetry/superselection rule, regardless of resources | (Q) quantum | **Wigner–Araki–Yanase**; resource theory of asymmetry (Marvian–Spekkens) |

- **Model-class split.** In the **classical finite-state** regime (C) the closure
  argument holds, E3 is empty, and E0/E1/E2 are exhaustive — no single-instance
  physical boundary. In the **finite-dimensional quantum** regime (Q) E3 is
  nonempty — exact single-instance physically-forced boundaries exist.
- **Overarching framing.** "Capabilities = which transformations are
  possible/impossible" is **constructor theory** (Deutsch–Marletto). This taxonomy
  is a classification of *why* a task is impossible (the four modes), read through
  the capability-measure program.

## Tri-repo alignment

- **E1** ≈ TaF game / Aumann–Shapley non-atomic limit (T413).
- **E2** ≈ TaF computational finality (T417); the computational-arrow swing is
  recorded as T419 REDESIGN, and T420 hardens the finite-cycle anti-relabel gate,
  so any remaining novelty is a family-level period-hardness redesign/abandon
  question (`open-problems/computational-finality-arrow.md`).
- **E3** ≈ **GU** structural-symmetry no-go (antilinear index-nullity / Krein
  grading) — one-way adjacency, never cited as support. T421 refutes the first
  GU-adjacent admissibility-adapter candidate as a functor and records it as a
  logged disanalogy, not a claim move.
- **E0** is the mode every absorbed TaF attempt used (stipulated gaps through
  co-present registers).

## Novelty note (honest, verified)

The *packaging* (four modes for capability boundaries + the crypto crosswalk + the
tri-repo alignment) was not found verbatim, but **every component and the framing
have established homes** (verified by arXiv fetch, 2026-07-02). So this taxonomy is
a **useful internal map and at most a synthesis/perspective**, not a novel result.
Its value is organizing the program: it explains the kill history, tells any new
boundary attempt which mode it lives in, and localizes where genuine novelty could
still be (E2 computational finality; any future E3 adapter must start from the
T421 disanalogy rather than restating the refused functor).

## How to use it

For any capability/finality boundary attempt, ask: is the separating datum
recoverable by an admissible enlargement (**E0**, declared — stop)? If not, is the
forcing a limit/family effect (**E1**), a hardness assumption (**E2**), or an exact
symmetry no-go (**E3**)? Name the admissible class `A`; state the regime (C)/(Q).
A single-instance non-declared classical boundary is impossible (use E1/E2); a
single-instance quantum one must be E3.

No North Star, canon, public-posture, cross-repo, or ledger movement. GU/TI remain
stress-test input only. Promotion of any mode to a claim pauses for Joe.

## Internal support update (2026-07-03): classical C-fragment executable gate

T432 (`results/T432-classical-finite-boundary-declarability-gate-v0.1-results.md`)
turns the classical finite-state fragment into a recorded-tier executable check.
With `A0` as declared region observables and `A1` as the full co-present finite
classical code, every tested single-instance separator outside `A0` is recovered
by `A1`. The full-support parity guard has no proper coordinate support and is
still `A1`-declared. The exhaustive `n in {1,2,3}` Boolean sweep found zero
single-instance physical candidates.

T433 (`results/T433-classical-declarability-proof-certificate-v0.1-results.md`)
adds the constructive proof certificate for that same classical C-fragment:
for a finite classical product code `Omega`, region projection `pi_R`, and total
datum `d : Omega -> V`, `A1` contains `id_Omega`, so `d = L o id_Omega` by finite
lookup. A0 insufficiency is therefore E0-declared relative to A1, not a
single-instance physical boundary.

This is support for using the taxonomy internally, not a promoted theorem. It
does not touch the quantum E3 route or the T421 logged disanalogy.

## Internal support update (2026-07-03): quantum E3 A-class gate

T435 (`results/T435-quantum-e3-admissible-menu-gate-v0.1-results.md`) supplies a
recorded-tier finite A-class control for the taxonomy's quantum E3 hinge. In a
two-sector parity/superselection toy with `P=diag(1,-1)`, the states `|+><+|` and
`|-><-|` share the same A1 symmetry-respecting sector-population shadow, while
the relative-phase observable `X` separates them and does not commute with `P`.

Verdict: `QUANTUM_E3_A_CLASS_GATE_BUILT_NO_CLAIM_PROMOTION`. Relative to A1
without a reference/asymmetry resource, the phase datum is recorded as
`E3_STRUCTURAL_SYMMETRY_RELATIVE_TO_A1_NO_REFERENCE`. The same pair becomes
`E0_DECLARED_RELATIVE_TO_A2_REFERENCE_RESOURCE` once A2 admits the reference
resource. Visible A1 controls, classical finite-code controls, post-hoc symmetry
selectors, missing-symmetry packets, and hidden-label oracles do not pass.

This is a taxonomy/admission gate only. It is not a WAY theorem, not a quantum
physics claim, not a GU/TaF adapter, not cross-repo evidence, and not a claim
promotion. T421's logged disanalogy remains closed as stated.

## Internal support update (2026-07-03): quantum E3 resource-lift classifier

T436 (`results/T436-quantum-e3-resource-lift-classifier-v0.1-results.md`) adds the
resource-lift guardrail that T435 makes necessary. A candidate that clears the A1
symmetry-respecting menu is not automatically an absolute E3/no-go result. It must
also audit A2 reference/asymmetry resources.

Verdict: `QUANTUM_E3_RESOURCE_LIFT_CLASSIFIER_BUILT_T435_RELATIVE_NOT_ABSOLUTE`.
The T435 phase pair and dephased-mixture control are both classified as
`A1_RELATIVE_LIFTED_TO_E0_BY_A2_REFERENCE`, not absolute E3. A synthetic exact
no-go control proves the classifier can report the absolute-after-resource shape,
but it is calibration only. Large resource cost, missing A2 audit, post-hoc
resource policy, hidden-resource oracle, A1-visible controls, and classical
full-code controls do not pass.

Future quantum E3 attempts should report both A1 status and A2 resource-lift
status. A real absolute E3 artifact must bring an independently typed exact no-go
witness that survives the resource-lift audit. T436 is not a WAY theorem, not a
quantum physics claim, not a GU/TaF adapter, not cross-repo evidence, and not a
claim promotion.

## Internal support update (2026-07-03): repaired-taxonomy hostile-review gate

T437 (`results/T437-repaired-taxonomy-hostile-review-gate-v0.1-results.md`) audits
the repaired taxonomy packet against the adversarial-review checklist after T433,
T435, and T436.

Verdict: `REPAIRED_TAXONOMY_INTERNAL_MAP_SURVIVES_HOSTILE_REVIEW_NO_PROMOTION`.
The repair packet passes as an internal mode classifier: the universal no-go stays
withdrawn; prior art is recorded as low-novelty context; the classical C-fragment
has a constructive proof certificate; and the quantum E3 side is guarded by A-class
and A2 resource-lift reporting.

The gate keeps promotion blocked. It does not authorize a public hard-theorem
paper, claim-ledger movement, real absolute E3, D2 redesign/abandon, T421 revival,
GU/TaF adapter movement, or cross-repo support. Use the taxonomy internally for
classification and routing only unless Joe authorizes a separate promotion or
external posture decision.

## Internal support update (2026-07-03): E2 period-hardness admission gate

T438 (`results/T438-e2-period-hardness-admission-gate-v0.1-results.md`) applies
the taxonomy internally to the D2/E2 computational-finality lane after T419/T420.

Verdict: `E2_PERIOD_HARDNESS_ADMISSION_GATE_BUILT_NO_D2_DECISION`. The gate admits
only a predeclared family-level period-hardness packet as a future E2 redesign
target. It rejects finite public cycles, bounded non-recovery, point-inversion-only
static relabels, thermodynamic/E1 packets, Brown-Susskind complexity-growth
packets, single-instance claims, and post-hoc selectors. Packets that change public
transition knowledge or leave the closed public-permutation regime require a
separate spec.

This is routing support for the internal taxonomy, not D2 progress at claim level.
It does not redesign or abandon D2, prove a computational arrow, prove
cryptographic hardness, make a physics claim, update the claim ledger, or authorize
public posture.

## Internal support update (2026-07-03): finite-time/catalytic thermodynamic gate

T439 (`results/T439-finite-time-catalytic-thermo-witness-gate-v0.1-results.md`)
applies the taxonomy's E1 thermodynamic-resource discipline to H7-style
finite-time and catalytic record-deletion packets.

Verdict: `FINITE_TIME_CATALYTIC_THERMO_GATE_BUILT_NO_H7_PROMOTION`. The gate
rejects reversible uncopy, blind Landauer-style erasure, finite kinetic
barriers, nonequilibrium current-only packets, omitted feedback-memory ledgers,
hidden sinks/export, untyped resource units, undeclared or consumed catalysts,
and task splits that disappear once thermodynamic and information ledgers are
matched. Exact ideal-limit or sector-lock packets are routed to a separate
E1/E3/idealization spec rather than admitted as finite-time thermodynamic
witnesses.

Only a full-accounting synthetic packet is admitted as a future review target.
T439 does not promote H7, derive a thermodynamic arrow, prove a stochastic-
thermodynamic or catalytic resource theorem, update the claim ledger, or
authorize public posture.
