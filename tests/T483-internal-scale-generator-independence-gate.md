# T483: Internal Scale Generator Independence Gate

## Target Claims

- [RG Flow as a Multiscale-Transport Analogy](../open-problems/rg-flow-as-multiscale-transport-analogy.md)
- [T24: D1 Multiscale Observer Field](T24-d1-multiscale-observer-field.md)
- [T38: Minimal Multiscale Transport Formalization](T38-minimal-multiscale-transport.md)
- [T480: Scale-Label Operation Gate](T480-scale-label-operation-gate.md)
- [T481: Internal Scale Structure Admission Gate](T481-internal-scale-structure-admission-gate.md)
- [T482: Internal Scale Generator Invariance Probe](T482-internal-scale-generator-invariance-probe.md)

## Setup

T482 made the first concrete post-T481 internal-scale review target: a
D1-support-gradient generator. The packet passed review mechanics but factored
through the existing D1 profile tuple, so it earned only D1 bookkeeping.

T483 makes the next burden executable. A generator must not be recoverable from
the existing D1 profile tuple before it can even be admitted as a future review
target.

The positive review control uses the T24/T38 connected and partitioned
transport fixtures:

```text
connected_transport_scenario
partitioned_transport_scenario
```

These fixtures hold observer IDs and D1 profile vectors fixed while changing
trust-preserving transport topology. The generator classifies observer sites
by transport component relative to the declared source and target.

## Success Criteria

- T482 remains passed and bookkeeping-only.
- The T482 support-gradient generator is rejected as D1-profile completion.
- The connected and partitioned T24/T38 fixtures have identical D1 profile
  vectors but different transport-topology signatures.
- The transport-topology generator survives observer-label relabeling.
- The transport-topology packet is admitted only as a synthetic future review
  target and transport-topology bookkeeping.
- Label-only, posthoc, observer-order, hidden-time, duration/arrow, finality,
  RG/conformal, physics, and promotion shortcuts are blocked.
- The result earns no independent internal scale structure, record clock,
  duration, temporal arrow, record-finality change, scale-genesis theorem,
  physics claim, D1 promotion, RG/TaF equivalence theorem, claim-ledger
  movement, roadmap movement, North Star movement, public-posture movement, or
  cross-repo movement.

## Failure Criteria

- A D1-completion generator is admitted as independent.
- Fixed-D1 counterfactual controls are omitted or chosen post hoc.
- Observer ID order survives as a generator.
- Hidden time/order metadata creates scale, duration, or arrow evidence.
- A transport component changes record-finality status.
- RG or conformal fixed-point machinery becomes a TaF internal generator.
- The result promotes D1, scale genesis, physics posture, public posture,
  claim status, or cross-repo truth.

## Known Physics Constraints

RG scale and conformal symmetry remain external analogy material. T483 does not
evaluate RG beta functions, conformal-gravity phenomenology, unitarity,
rotation curves, asymptotic freedom, or quantum gravity.

## Result

Implemented as T483 v0.1.

Expected verdict:

```text
INTERNAL_SCALE_INDEPENDENCE_GATE_BUILT_REVIEW_TARGET_ONLY_NO_PROMOTION
```

The gate rejects T482's support-gradient generator as D1 completion. It admits
a fixed-D1 transport-topology separator only as a future review target and
transport-topology bookkeeping, not independent internal scale structure.

## Reproduction

```bash
python -m pytest tests/test_internal_scale_generator_independence_gate.py -q
python -m models.internal_scale_generator_independence_gate --write-results
```

Artifacts:

- `models/internal_scale_generator_independence_gate.py`
- `tests/test_internal_scale_generator_independence_gate.py`
- `results/T483-internal-scale-generator-independence-gate-v0.1.json`
- `results/T483-internal-scale-generator-independence-gate-v0.1-results.md`

## Contribution Needed

Future internal-scale packets must include a fixed-D1 counterfactual
independence control before claiming an internal generator. Fixed-D1
transport-topology separation is review metadata only unless a later theorem
connects it to internal scale without importing clocks, duration, finality,
RG/conformal mechanisms, physics posture, or claim promotion.
