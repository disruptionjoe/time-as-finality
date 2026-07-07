# T487: Reachability Quotient Capability Spread Gate

## Target Claims

- [RG Flow as a Multiscale-Transport Analogy](../open-problems/rg-flow-as-multiscale-transport-analogy.md)
- [T24: D1 Multiscale Observer Field](T24-d1-multiscale-observer-field.md)
- [T38: Minimal Multiscale Transport Formalization](T38-minimal-multiscale-transport.md)
- [T480: Scale-Label Operation Gate](T480-scale-label-operation-gate.md)
- [T481: Internal Scale Structure Admission Gate](T481-internal-scale-structure-admission-gate.md)
- [T482: Internal Scale Generator Invariance Probe](T482-internal-scale-generator-invariance-probe.md)
- [T483: Internal Scale Generator Independence Gate](T483-internal-scale-generator-independence-gate.md)
- [T484: Transport Topology Refinement Naturalness Gate](T484-transport-topology-refinement-naturalness-gate.md)
- [T485: Transport Topology Invariant Quotient Gate](T485-transport-topology-invariant-quotient-gate.md)

## Setup

T485 admits the finite source/target trust-reachability quotient over original
observer sites as review-grade bookkeeping only. It also blocks component size,
path length, hop bands, and relay count as refinement artifacts, and blocks
clock, duration, finality, scale, physics, and promotion overreads.

T487 asks the next downstream question without rerunning T485:

```text
Given the T485 quotient signature as the visible projection, which declared
transport-task capability objects are determined over quotient-visible fibers?
```

The positive controls are narrow:

- source-target reachability for the declared transport task;
- quotient role profile over original observer sites.

Hostile packets try to read the same quotient as path latency, relay budget,
component-size capacity, record finality, internal scale, physics support, or
claim/public-posture promotion.

## Success Criteria

- The committed T485 artifact remains the anchor and is consumed rather than
  rerun.
- Source-target reachability has singleton spread over each T485 quotient
  visible class.
- Quotient role profile has singleton spread over each T485 quotient visible
  class.
- Path-latency band, relay count, and component-size capability readings have
  non-singleton spreads over the connected quotient visible class.
- Finality, clock, duration, scale, physics, and promotion readings are blocked.
- The result earns no independent internal scale structure, record clock,
  duration, temporal arrow, record-finality change, scale-genesis theorem,
  physics claim, D1 promotion, RG/TaF equivalence theorem, claim-ledger
  movement, roadmap movement, North Star movement, public-posture movement, or
  cross-repo movement.

## Failure Criteria

- The gate reopens or re-runs T485 rather than consuming its committed artifact.
- Non-singleton path, relay, or component-size spread is admitted as determined
  by the reachability quotient.
- Reachability sufficiency is converted into internal scale, clock, duration,
  finality, RG/conformal, physics, or claim-promotion evidence.
- The result changes claim status, public posture, North Star, roadmap, hard
  policy, or cross-repo truth.

## Known Physics Constraints

RG scale and conformal symmetry remain external analogy material. T487 does
not evaluate RG beta functions, conformal-gravity phenomenology, unitarity,
rotation curves, asymptotic freedom, quantum gravity, or physical clocks.

## Result

Implemented as T487 v0.1.

Expected verdict:

```text
REACHABILITY_QUOTIENT_CAPABILITY_SPREAD_BUILT_TASK_ONLY
```

The T485 quotient signature is sufficient for the declared reachability task
and quotient role-profile task only. It is not sufficient for path-latency,
relay-budget, or component-size capability readings, whose spreads are
non-singleton over the same visible quotient class.

## Reproduction

```bash
python -m pytest tests/test_reachability_quotient_capability_spread_gate.py -q
python -m models.reachability_quotient_capability_spread_gate --write-results
```

Artifacts:

- `models/reachability_quotient_capability_spread_gate.py`
- `tests/test_reachability_quotient_capability_spread_gate.py`
- `results/T487-reachability-quotient-capability-spread-gate-v0.1.json`
- `results/T487-reachability-quotient-capability-spread-gate-v0.1-results.md`

## Contribution Needed

Future packets that use the T485 quotient must declare the capability object
before treating the quotient as sufficient, compute capability spread over
quotient-visible fibers, and keep reachability sufficiency separate from
scale, clock, duration, finality, RG/conformal mechanisms, physics posture, or
claim promotion unless a separate theorem earns more.
