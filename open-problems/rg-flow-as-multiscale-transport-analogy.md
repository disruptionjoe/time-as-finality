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
