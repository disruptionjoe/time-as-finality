# RG Flow as a Multiscale-Transport Analogy

Open-problem stub, opened 2026-06-30 from an external-paper calibration pass (Avramidi & Barvinsky 1985,
*Asymptotic freedom in higher-derivative quantum gravity*, Phys. Lett. B 159, 269). Exploration-grade.
**Projection != finality** held: this is a calibration analogy for the multiscale program, not a finality
result. Coupling-flow is not record-flow.

## Problem

Avramidi-Barvinsky show curvature-squared gravity is **asymptotically free**: its couplings flow to a fixed
point in the UV, so the *effective structure of the theory transforms with scale* in a controlled, computable
way. The TaF north star names a **typed multiscale transport network** as the next mathematical target, and
T24 already builds a multiscale observer field. Question: **does renormalization-group flow give a worked
external template for what "typed transport of structure across scales" should look like** -- a fixed-point
target, a controlled flow, and scale-dependent effective content -- that TaF's multiscale program can
calibrate against?

## Working Claim (to attack)

RG flow is the most rigorous existing example of "the same system presents different effective structure at
different scales, with a computable transport law between scales and a fixed point organizing the flow." If
TaF's multiscale transport network is to be more than a metaphor, it should specify the analogues: what is
transported (effective record/finality structure), what the transport law is (the analogue of the beta
function), and whether there is a fixed point (a scale-invariant finality structure).

## Why It Might Help

- Forces the north-star "typed multiscale transport network" to name its transported quantity, its transport
  law, and its fixed-point object -- the three things an RG flow makes explicit -- instead of leaving
  "multiscale" as an unanalyzed adjective.
- Connects T24 (multiscale observer field) to a concrete external standard for scale-to-scale structure.

## How It Could Mislead

- RG flow transports *coupling constants*; TaF would transport *record/finality structure*. These are
  different objects; the analogy is at the level of "controlled scale-transport with a fixed point," not at
  the level of mechanism. Do not import beta-function machinery as if it acts on records.
- Asymptotic freedom is a statement about a Lagrangian field theory with an action. TaF has no action (see
  the free-boundary persona sprint's variational counter-signal). The analogy is to the *shape* of
  scale-transport, not to its derivation from an action.

## Connection to Existing Claims and Tests

- [T24: D1 Multiscale Observer Field](../tests/T24-d1-multiscale-observer-field.md)
- North-star direction: typed multiscale transport network (program memory).
- [free-boundary-paper-persona-sprint-2026-06-30](../explorations/free-boundary-paper-persona-sprint-2026-06-30.md)
- [N15: Conformal Gravity as a Scale-Genesis Calibration Neighbor](../literature/N15-conformal-gravity-scale-genesis-calibration.md)
  (added 2026-07-06): the maximally symmetric member of the same higher-derivative family; exact
  conformal symmetry as the "no intrinsic scale" endpoint of the fixed-point picture. Same guards.

## Contribution Needed

On the T24 multiscale model, attempt to name the three RG analogues explicitly (transported structure,
transport law, fixed point). If even one cannot be named, that is a useful negative bounding what "multiscale
transport" can mean in TaF. Keep it as an analogy ledger; do not promote to a claim.

## T479 addendum: RG-flow multiscale calibration gate

T479 makes the contribution request executable:
`results/T479-rg-flow-multiscale-calibration-gate-v0.1-results.md`; spec
`tests/T479-rg-flow-multiscale-calibration-gate.md`; model
`models/rg_flow_multiscale_calibration_gate.py`.

Verdict:

```text
RG_FLOW_CALIBRATION_GATE_BUILT_ANALOGY_ONLY_NO_PROMOTION
```

The gate admits one local calibration packet only. T24 supplies field-valued
D1 as the transported structure, T38 supplies finite H1+ transport as the
transport-law analogue, and the conformal/fixed-point neighbor is usable only
as a no-intrinsic-scale endpoint that requires a declared scale-label operation
before record-clock structure appears. Coupling-flow import, Lagrangian/action
import, fixed-point clocks, record-finality-from-RG, conformal-phenomenology
support, and fixed-point-only packets are blocked.

This keeps the lane at analogy-ledger grade. Future packets must primary-source
check the RG/conformal-gravity neighbor before stronger use, declare the TaF
transported structure and transport law separately from RG beta functions, and
state the scale-label or symmetry-breaking operation before using clocks,
durations, or scale-genesis language. No D1 promotion, field-valued D1 canon
update, RG/TaF equivalence theorem, scale-genesis theorem, physics claim,
claim-ledger movement, roadmap movement, North Star movement, public-posture
movement, or cross-repo truth movement is earned.

## T480 addendum: scale-label operation gate

T480 makes the post-T479 scale-label burden executable:
`results/T480-scale-label-operation-gate-v0.1-results.md`; spec
`tests/T480-scale-label-operation-gate.md`; model
`models/scale_label_operation_gate.py`.

Verdict:

```text
SCALE_LABEL_OPERATION_GATE_BUILT_BOOKKEEPING_ONLY_NO_CLOCK_PROMOTION
```

The gate admits a single declared scale-label operation only as bookkeeping
over T24 field-valued D1 and T38 H1+ transport. It may label observer/scale
sites for future review and state which transport edges can be compared, but
it does not create record clocks, durations, record finality, scale genesis,
or physics support. Fixed-point clock language, RG-scale imports, label-only
packets, hidden calendar order, duration or arrow extraction,
finality-by-relabeling, conformal-phenomenology support, and promotion
shortcuts are blocked.

Future packets must declare the scale-label operation as an operation, not a
label word; keep transported structure and transport law separate from the
scale label; state whether the label is external bookkeeping or earned
internal structure; and keep clocks, durations, arrows, finality changes, RG
mechanics, and physics posture blocked unless separately earned. No D1
promotion, RG/TaF equivalence theorem, scale-genesis theorem, physics claim,
claim-ledger movement, roadmap movement, North Star movement, public-posture
movement, or cross-repo truth movement is earned.

## T481 addendum: internal scale-structure admission gate

T481 makes T480's external-bookkeeping/internal-structure split executable:
`results/T481-internal-scale-structure-admission-gate-v0.1-results.md`; spec
`tests/T481-internal-scale-structure-admission-gate.md`; model
`models/internal_scale_structure_admission_gate.py`.

Verdict:

```text
INTERNAL_SCALE_STRUCTURE_GATE_BUILT_REVIEW_ONLY_NO_CLOCK_PROMOTION
```

The gate admits external scale labels only as comparison-domain bookkeeping
over T24/T38/T480. It also admits one synthetic future internal-scale packet
only as a review target when the packet predeclares a TaF-native internal
generating rule, comparison domain, positive and negative controls, and
relabel-invariance checks. Assertion-only internal structure, label-only
structure, posthoc comparison domains, hidden calendar order, duration or
arrow extraction, finality-by-scale-labeling, RG/conformal mechanism import,
physics support, and promotion shortcuts are blocked.

This earns no internal scale structure. Future packets must state whether the
scale label is external bookkeeping or claimed internal structure before
witness construction, predeclare the comparison domain, and keep clocks,
durations, temporal arrows, finality changes, RG/conformal mechanics, physics
posture, and claim movement blocked unless separately earned. No D1 promotion,
RG/TaF equivalence theorem, scale-genesis theorem, physics claim,
claim-ledger movement, roadmap movement, North Star movement, public-posture
movement, or cross-repo truth movement is earned.

## T482 addendum: internal scale-generator invariance probe

T482 makes T481's synthetic review target concrete:
`results/T482-internal-scale-generator-invariance-probe-v0.1-results.md`;
spec `tests/T482-internal-scale-generator-invariance-probe.md`; model
`models/internal_scale_generator_invariance_probe.py`.

Verdict:

```text
D1_SUPPORT_GRADIENT_PROBE_BUILT_BOOKKEEPING_ONLY_NO_SCALE_STRUCTURE
```

The probe predeclares a finite D1-support-gradient generator:
`support_depth = accessible_support + holder_redundancy + branch_support +
reversal_cost`, with fixed low/middle/high bands. The stratified T24 packet
produces nontrivial support bands, the uniform T24 null control collapses to
one band, and the generated band multiset is invariant under observer-label
relabeling.

This admits the packet only as review-grade D1 bookkeeping. The scale bands
factor entirely through the existing D1 profile tuple, so T482 earns no
independent internal scale structure. Label-only, posthoc-threshold,
observer-label-order, hidden-time, duration/arrow, finality, RG/conformal,
physics, and promotion shortcuts remain blocked. Future packets must either
keep support-gradient bands labeled as D1 bookkeeping or supply an independent
TaF-native generator that does not merely factor through the D1 tuple. No D1
promotion, internal scale-structure theorem, RG/TaF equivalence theorem,
scale-genesis theorem, physics claim, claim-ledger movement, roadmap movement,
North Star movement, public-posture movement, or cross-repo truth movement is
earned.

## T483 addendum: internal scale-generator independence gate

T483 makes T482's independence burden executable:
`results/T483-internal-scale-generator-independence-gate-v0.1-results.md`;
spec `tests/T483-internal-scale-generator-independence-gate.md`; model
`models/internal_scale_generator_independence_gate.py`.

Verdict:

```text
INTERNAL_SCALE_INDEPENDENCE_GATE_BUILT_REVIEW_TARGET_ONLY_NO_PROMOTION
```

The gate rejects T482's support-gradient generator as D1-profile completion. A
synthetic transport-topology generator separates T24/T38 connected vs
partitioned fixtures while their D1 vectors are fixed and survives
observer-label relabeling. This is admitted only as a future review target and
transport-topology bookkeeping.

Future packets must prove the generator is not recoverable from the existing
D1 profile tuple, include a fixed-D1 counterfactual pair, preserve
relabel-invariance, and keep transport topology separate from scale, clock,
duration, finality, RG/conformal, physics, and promotion language unless a
separate theorem earns more. No independent internal scale structure, record
clock, duration, temporal arrow, record-finality change, scale-genesis theorem,
physics claim, D1 promotion, RG/TaF equivalence theorem, claim-ledger movement,
roadmap movement, North Star movement, public-posture movement, or cross-repo
truth is earned.

## T484 addendum: transport-topology refinement naturalness gate

T484 makes the T483 topology review-target burden stricter:
`results/T484-transport-topology-refinement-naturalness-gate-v0.1-results.md`;
spec `tests/T484-transport-topology-refinement-naturalness-gate.md`; model
`models/transport_topology_refinement_naturalness_gate.py`.

Verdict:

```text
TRANSPORT_TOPOLOGY_REFINEMENT_GATE_BUILT_REACHABILITY_BOOKKEEPING_ONLY
```

The gate subdivides trust-preserving transport edges in the T24/T38 connected
and partitioned fixtures while preserving the D1 profile tuples for original
observer sites. Source/target reachability roles remain stable under
subdivision and observer-label relabeling, so the T483 topology packet remains
admitted only as review-grade reachability bookkeeping.

Component size and shortest-path length change under the same benign
refinement, so they are blocked as internal-scale, clock, duration, finality,
or scale-genesis evidence. Future packets must include transport-refinement
controls before using topology as a generator, reject component-size and
path-length scale readings unless an invariant morphism class is declared, and
keep reachability topology separate from scale, clock, duration, finality,
RG/conformal, physics, and promotion language unless a separate theorem earns
more. No independent internal scale structure, record clock, duration,
temporal arrow, record-finality change, scale-genesis theorem, physics claim,
D1 promotion, RG/TaF equivalence theorem, claim-ledger movement, roadmap
movement, North Star movement, public-posture movement, or cross-repo truth is
earned.

## T485 addendum: transport-topology invariant quotient gate

T485 makes T484's invariant-morphism caveat executable:
`results/T485-transport-topology-invariant-quotient-gate-v0.1-results.md`;
spec `tests/T485-transport-topology-invariant-quotient-gate.md`; model
`models/transport_topology_invariant_quotient_gate.py`.

Verdict:

```text
TRANSPORT_TOPOLOGY_INVARIANT_QUOTIENT_BUILT_REACHABILITY_ONLY
```

The gate declares the finite morphism class of observer-label relabeling plus
trust-edge subdivision, with relay sites forgotten back to original observer
reachability. Under that class, the source/target trust-reachability quotient
over original observer sites is stable and still separates the connected and
partitioned fixed-D1 pair, so it remains admitted as review-grade bookkeeping
only.

Component count is absorbed as a derived quotient summary. Component size,
shortest-path length, hop bands, and relay count vary under benign iterated
subdivision, so they remain blocked as internal-scale, clock, duration,
finality, or scale-genesis evidence. Future topology packets must declare
their morphism/refinement class before using topology as a generator, quotient
refinement artifacts away, and keep reachability separate from scale, clocks,
duration, finality, RG/conformal mechanisms, physics posture, and claim
promotion unless a separate theorem earns more. No independent internal scale
structure, record clock, duration, temporal arrow, record-finality change,
scale-genesis theorem, physics claim, D1 promotion, RG/TaF equivalence theorem,
claim-ledger movement, roadmap movement, North Star movement, public-posture
movement, or cross-repo truth is earned.

## T487 addendum: reachability quotient capability-spread gate

T487 consumes T485's committed quotient result without rerunning the T485
topology gate:
`results/T487-reachability-quotient-capability-spread-gate-v0.1-results.md`;
spec `tests/T487-reachability-quotient-capability-spread-gate.md`; model
`models/reachability_quotient_capability_spread_gate.py`.

Verdict:

```text
REACHABILITY_QUOTIENT_CAPABILITY_SPREAD_BUILT_TASK_ONLY
```

The T485 quotient signature is sufficient for two declared transport-task
capabilities: source-target reachability and the quotient role profile over
original observer sites. It is not sufficient for path-latency, relay-budget,
or component-size capability readings, because those spreads are non-singleton
over the connected quotient-visible fiber. Finality, clock, duration, scale,
physics, and promotion readings remain blocked overreads.

Future packets that use the T485 quotient must declare the capability object
before treating the quotient as sufficient, compute capability spread over
quotient-visible fibers, and keep reachability sufficiency separate from
scale, clock, duration, finality, RG/conformal mechanisms, physics posture, or
claim promotion unless a separate theorem earns more. No independent internal
scale structure, record clock, duration, temporal arrow, record-finality
change, scale-genesis theorem, physics claim, D1 promotion, RG/TaF equivalence
theorem, claim-ledger movement, roadmap movement, North Star movement,
public-posture movement, or cross-repo truth is earned.

## T488 addendum: post-T487 reachability quotient closure router

T488 closes the current T479-T487 RG/multiscale reachability-quotient thread
against minor restarts:
`results/T488-post-t487-reachability-quotient-closure-router-v0.1-results.md`;
spec `tests/T488-post-t487-reachability-quotient-closure-router.md`; model
`models/post_t487_reachability_quotient_closure_router.py`.

Verdict:

```text
POST_T487_REACHABILITY_QUOTIENT_THREAD_CLOSED_NEW_EVIDENCE_ONLY
```

The router treats T487 as reachability-task sufficiency only. It rejects
reachability-quotient upgrades, role-profile scale restarts, path-latency,
relay-budget, component-size, record-finality, RG/conformal import, and
claim/public-posture shortcuts. An undercontrolled independent-capability
packet is also rejected for missing hostile controls.

Future work can reopen the surface only by bringing a newly declared
independent capability object with capability-spread controls, a domain-native
morphism class that changes the invariance burden, or a direct record-finality
bridge theorem with hostile controls. Admitted future targets are review
targets only; they are not evidence. No independent internal scale structure,
record clock, duration, temporal arrow, record-finality change,
scale-genesis theorem, physics claim, D1 promotion, RG/TaF equivalence
theorem, claim-ledger movement, roadmap movement, README movement, North Star
movement, public-posture movement, or cross-repo truth is earned.
