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

## Internal support update (2026-07-04): quantum E3 exact no-go big swing

T447 (`results/T447-quantum-e3-exact-no-go-big-swing-v0.1-results.md`) attempts
the first finite exact-no-go packet after the T435/T436 A1/A2 discipline.

Verdict:
`QUANTUM_E3_FINITE_CATALYTIC_NO_GO_PACKET_BUILT_RECORDED_TIER_NOT_UNRESTRICTED_ABSOLUTE`.
In a finite two-sector charge toy, exact charge flip under a declared finite
non-wrapping exact-catalyst A2 policy would require a nonzero unit-modulus
eigenvector of a finite nilpotent shift; none exists. This survives only relative
to that declared finite catalytic policy. Cyclic references, consumed references,
ideal phase references, and the T435 phase-reference control route away from an
unrestricted absolute E3 claim.

This is a recorded-tier finite toy packet. It is not a WAY theorem, not a quantum
physics claim, not a GU/TaF adapter, not cross-repo evidence, and not claim-ledger
movement. Stronger E3 attempts must type the resource policy before the task and
handle cyclic, consumed, and ideal-reference absorbers.

## Internal support update (2026-07-05): E3-to-region adapter gate

T453 (`results/T453-e3-to-region-nonadmissibility-adapter-gate-v0.1-results.md`)
tests whether T447's finite exact E3 no-go can discharge T452's
region-indexed law-sector nonadmissibility burden.

Verdict: `T447_E3_NO_GO_DOES_NOT_DISCHARGE_REGION_T452_BURDEN`. T447 supplies
an exact no-go witness pattern, but T447 alone has no region-indexed pair.
Citation-only T445+T447 still leaves the T452 absorber firing because the exact
witness is not tied to T445's named law-sector completion. Reference-policy
splits factor through admitted completion and remain E0-declared. Generic
sector/gauge shortcuts route to the N14 absorber.

Only a synthetic integrated E3-region packet is admitted as a future review
target. Future Direction-A packets that cite E3 must integrate the exact no-go
with the same completion that would otherwise restore region-packet
factorization. T453 is not a region-indexed discriminator success, not a WAY
theorem, not a quantum physics theorem, not a GU/TaF adapter, not cross-repo
support, and not claim-ledger movement.

## Internal support update (2026-07-05): integrated E3-region packet swing

T454 (`results/T454-integrated-e3-region-packet-swing-v0.1-results.md`) realizes
the T453 synthetic target as a finite toy review packet.

Verdict: `INTEGRATED_E3_REGION_PACKET_ADMITTED_REVIEW_TARGET_NO_PROMOTION`. The
main packet matches all declared R-supported statistics and interventions,
splits revision capability only under the boundary menu, names the deficient-side
completion, and ties that completion to T447's finite non-wrapping
exact-catalyst no-go. It therefore passes the T452 check as a recorded-tier
review target.

The ceiling remains explicit. T454 is not a region-indexed discriminator
success: cyclic, consumed, and ideal reference controls route away from the
finite exact packet, and law-sector description still explains which side has
the boundary resource. It is not a real substrate law, not a quantum physics
theorem, not a WAY theorem, not a GU/TaF adapter, not cross-repo support, and
not claim-ledger movement.

## Internal support update (2026-07-05): T454 hostile-review gate

T455 (`results/T455-t454-hostile-review-gate-v0.1-results.md`) performs that
hostile review before any stronger Direction-A posture movement.

Verdict: `T454_SURVIVES_HOSTILE_REVIEW_AS_REVIEW_TARGET_PROMOTION_BLOCKED`. The
finite packet survives only at its claimed level: R-equality, boundary splitting,
exact-witness integration, and negative controls check out. Promotion remains
blocked because law-sector description still explains the boundary resource,
cyclic/consumed/ideal references route away from the finite exact packet, and no
policy-independent region theorem is supplied beyond the integration.

T455 preserves T454 as a recorded-tier review target only. It is not a
region-indexed discriminator success, real substrate law, quantum physics
theorem, WAY theorem, GU/TaF adapter, cross-repo support, claim-ledger movement,
public posture, or hard-policy movement.

## Internal support update (2026-07-05): policy-invariant region theorem gate

T456 (`results/T456-policy-invariant-region-theorem-gate-v0.1-results.md`)
turns T455's blocker set into the next admission gate for Direction-A packets.

Verdict:
`POLICY_INVARIANT_REGION_THEOREM_GATE_BUILT_CURRENT_T454_NOT_ADMITTED`. Current
T454/T455 remains a recorded-tier review target and is not admitted for stronger
posture because three requirements still fail: the boundary-resource completion
factors through law-sector description, cyclic/consumed/ideal reference policies
are not invariantly handled or independently precluded, and no
policy-independent region theorem is supplied beyond packet integration.

Only a synthetic future target clears the gate. Future Direction-A packets must
bring description nonfactorization, reference-policy invariance or preclusion,
and a policy-independent theorem before any stronger posture movement. T456 is
not a region-indexed discriminator success, real substrate law, quantum physics
theorem, WAY theorem, GU/TaF adapter, cross-repo support, claim-ledger movement,
public posture, or hard-policy movement.

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

## Internal support update (2026-07-04): E2 changed-transition regime gate

T444 (`results/T444-e2-changed-transition-regime-gate-v0.1-results.md`) implements
the separate-spec route that T438 required for changed-public-transition and
open/nonpermutation packets.

Verdict: `E2_CHANGED_TRANSITION_REGIME_GATE_BUILT_NO_D2_DECISION`. The gate
admits only predeclared changed-transition or open/nonpermutation packets for
separate-regime review. It rejects post-hoc/hidden transition policies,
thermodynamic/E1 packets, Brown-Susskind symmetric-complexity packets, pure
epistemic ignorance, unfrozen transition evidence, open packets with no dynamics
law, and resource/environment completion. Closed public-permutation packets route
back to T438.

This is routing support for the internal taxonomy, not D2 progress at claim
level. It does not redesign or abandon D2, prove a computational arrow, prove
cryptographic hardness, make a physics claim, update the claim ledger, or
authorize public posture.

## Internal support update (2026-07-04): E2 family/open-regime packet swing

T446 (`results/T446-e2-family-open-regime-big-swing-v0.1-results.md`) runs the
first recorded-tier positive packet swing after T438/T444.

Verdict:
`E2_OPEN_RABIN_LIFT_PACKET_SURVIVES_SCREEN_WITH_T417_CHAIN_RESIDUAL_NO_D2_DECISION`.
The open Rabin-lift chain clears T438/T444 routing and the main absorber screen:
public transition, injective open dynamics, information-theoretic reversal, named
Rabin/factoring hardness, no E1 cost basis, no symmetric complexity-growth basis,
and no hidden transition policy. The result remains recorded-tier because the
hard part may still be chained T417/Rabin static inversion, and the lift carries
growth debt.

This is D2/E2 routing support and candidate-packet pressure, not D2 redesign,
D2 success, claim support, cryptographic theorem, physics claim, or public
posture. The next useful E2 question is whether coupled open iteration adds any
theorem beyond per-step Rabin inversion.

## Internal support update (2026-07-04): E2 chain residual factorization

T448 (`results/T448-e2-chain-residual-factorization-v0.1-results.md`) resolves
the T446 residual for the current open Rabin-lift packet.

Verdict:
`T446_CHAIN_RESIDUAL_FACTORS_THROUGH_PER_STEP_RABIN_NO_NEW_D2_THEOREM`. Full-chain
recovery factors through public integer-square lift unwraps plus one independent
Rabin square-root inversion per current modulus. A length-one T446 chain already
embeds the ordinary T417/Rabin inversion problem, and changing the next lift
domain while preserving lift room does not change predecessor recovery.

This absorbs the current T446 chain as chained T417/Rabin inversion. It does not
redesign or abandon D2, prove a computational arrow, prove cryptographic
hardness, make a physics claim, update the claim ledger, or authorize public
posture. Future D2 work needs either T438-style true family-level period hardness
or a packet whose chain inversion is not product-decomposable into public unwraps
plus independent step inversions.

## Internal support update (2026-07-04): E2 period-hardness packet audit

T449 (`results/T449-e2-period-hardness-packet-audit-v0.1-results.md`) sharpens
T438's remaining closed public-permutation route after T448.

Verdict:
`E2_PERIOD_HARDNESS_PACKET_SHARPENED_TO_HIDDEN_ORDER_THEOREM_TARGET_NO_D2_DECISION`.
For BBS-style public squaring on `QR_N`, `F_N^t(x) = x^(2^t)`, and if
`d = ord_N(x)`, the orbit period is `L = ord_d(2)`. Once `L` is known,
predecessor recovery is public forward iteration. In the toy family, the formula
matches public cycle discovery and known period recovers predecessors. Granting
`|QR_N|` is recorded as trapdoor completion because `N` and `|QR_N|` recover
`p,q` in the semiprime setting.

This keeps D2 alive only as a hidden-order / cycle-length theorem target with
seed-distribution controls. It does not redesign or abandon D2, prove period
hardness, prove a computational arrow, prove cryptographic hardness, make a
physics claim, update the claim ledger, or authorize public posture.

## Internal support update (2026-07-04): E2 period-oracle trapdoor equivalence

T450 (`results/T450-e2-period-oracle-trapdoor-equivalence-v0.1-results.md`)
stress-tests whether T449's hidden-order period route is independent of the
T417/Rabin trapdoor.

Verdict:
`PERIOD_ORACLE_COLLAPSES_TO_RABIN_TRAPDOOR_NO_INDEPENDENT_D2_ROUTE`. For the
current closed public-squaring route, an all-target period oracle gives unique
predecessors; Rabin's square-root oracle reduction factors `N` from that
predecessor oracle. Conversely, group-order/factorization completion computes
periods.

This absorbs the current closed public-squaring period route as Rabin/factoring
trapdoor equivalence. It does not redesign or abandon D2, prove period hardness,
prove a computational arrow, prove cryptographic hardness, make a physics claim,
update the claim ledger, or authorize public posture. Continuing D2 now requires
a nonstandard period assumption with a declared scope that avoids both
single-seed weakness and all-target trapdoor equivalence; otherwise the temporal
route should be demoted to T417's static E2 boundary in a separate governed
decision packet.

## Internal support update (2026-07-05): D2 temporal route demotion packet

T451 (`results/T451-d2-temporal-route-demotion-packet-v0.1-results.md`) executes
the separate governed decision packet recommended by T450.

Verdict:
`CURRENT_D2_TEMPORAL_ROUTE_DEMOTED_TO_T417_STATIC_E2_BOUNDARY`. The current
D2 temporal computational-arrow route has exhausted its tested continuations:
finite public cycles are absorbed by public period traversal, the tested open
Rabin-lift chain factors through per-step T417/Rabin inversion, and the closed
public-squaring period route collapses to Rabin/factoring trapdoor equivalence.

This closes the current temporal D2 route back to T417's static E2 boundary as
an internal route-level decision. It does not demote the D2 definition, promote
a claim, prove a computational arrow, prove cryptographic hardness, make a
physics claim, update the claim ledger, or authorize public posture. Future D2
work remains admissible only if it supplies a changed assumption or scope that
clears the T438/T444 gates and avoids the T448/T450 absorbers.

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

## Internal support update (2026-07-03): ideal-limit / sector-lock routing gate

T440 (`results/T440-ideal-limit-sector-lock-routing-gate-v0.1-results.md`)
implements the separate E1/E3/idealization spec that T439 required for exact
ideal-limit and sector-lock packets.

Verdict: `IDEAL_LIMIT_SECTOR_LOCK_ROUTING_GATE_BUILT_NO_PROMOTION`. Infinite
barriers and exact sector bans without finite operational substrate route to
H7-null idealization; gauge representative changes are not physical deletion;
finite barriers, finite enforcement, leakage paths, compensating reservoirs,
and reference resources route to absorber or E0/resource completion. E1 review
requires a family-level limit packet with finite approximants, a predeclared
limit invariant, and diverging recovery cost or nonlocality. E3 review requires
an exact no-go on physical states that survives conserved-quantity, reservoir,
boundary, reference, allowed-control, and A2 resource-lift audit.

Only synthetic E1/E3 controls are admitted as future review targets. T440 does
not promote H7, prove an E1 theorem, prove an E3 theorem, prove WAY, move the
claim ledger, or authorize public posture.

## Internal support update (2026-07-03): E1 family-limit packet gate

T441 (`results/T441-e1-family-limit-packet-gate-v0.1-results.md`) implements
the E1 family-limit packet gate required by T440.

Verdict: `E1_FAMILY_LIMIT_PACKET_GATE_BUILT_NO_PROMOTION`. The gate admits only
a predeclared family-level E1 packet with finite approximants, an
approximant-to-limit map, stable task and operation class, fixed observer and
resource accounting, a finite-auditable limit invariant, convergence/error
controls, a negative control, and a diverging recovery cost or nonlocality
quantity.

Single-instance idealizations, finite barriers, finite gaps, post-hoc
selectors, family drift, hidden resources, missing controls, bounded cost
families, and E2/E3 packets are rejected, absorbed, or routed to the proper
mode gate. Only a synthetic E1 control is admitted for future review. T441 does
not promote H7, prove an E1 theorem, prove a thermodynamic arrow, move the
claim ledger, or authorize public posture.
