# T481: Internal Scale Structure Admission Gate

## Target Claims

- [RG Flow as a Multiscale-Transport Analogy](../open-problems/rg-flow-as-multiscale-transport-analogy.md)
- [T24: D1 Multiscale Observer Field](T24-d1-multiscale-observer-field.md)
- [T38: Minimal Multiscale Transport Formalization](T38-minimal-multiscale-transport.md)
- [T479: RG-Flow Multiscale Calibration Gate](T479-rg-flow-multiscale-calibration-gate.md)
- [T480: Scale-Label Operation Gate](T480-scale-label-operation-gate.md)

## Setup

T480 admits a declared scale-label operation only as external bookkeeping over
T24 field-valued D1 and T38 H1+ transport. It also requires future packets to
state whether the label is external bookkeeping or earned internal structure,
and to state what observers and transport edges can compare after labeling.

T481 makes that next burden executable. It distinguishes:

- external scale-label bookkeeping;
- a synthetic future internal-scale-structure review target;
- hostile shortcuts that turn labels into internal structure, clocks,
  durations, finality changes, RG/conformal mechanisms, physics posture, or
  claim movement.

## Success Criteria

- T480 remains passed and bookkeeping-only.
- An external scale-label packet is admitted only as comparison-domain
  bookkeeping.
- A synthetic internal-scale review packet is admitted only as a future review
  target when it predeclares an internal generating rule, comparison domain,
  controls, and relabel-invariance checks.
- Assertion-only, label-only, posthoc-domain, hidden-calendar, duration/arrow,
  finality, RG/conformal, physics, and promotion shortcuts are blocked.
- The result earns no internal scale structure, clock, duration, temporal
  arrow, finality change, scale-genesis theorem, physics claim, claim-ledger
  movement, roadmap movement, North Star movement, public-posture movement, or
  cross-repo movement.

## Failure Criteria

- A label word counts as internal structure.
- A posthoc comparison domain is admitted.
- Hidden calendar order or temporal ordering is smuggled through labels.
- Ordered labels create duration or a temporal arrow.
- Scale labels change record-finality status.
- RG or conformal fixed-point machinery becomes a TaF internal generator.
- The result promotes D1, scale genesis, physics posture, public posture,
  claim status, or cross-repo truth.

## Known Physics Constraints

RG scale and conformal symmetry remain external analogy material. T481 does not
evaluate RG beta functions, conformal-gravity phenomenology, unitarity,
rotation curves, asymptotic freedom, or quantum gravity.

## Result

Implemented as T481 v0.1.

Expected verdict:

```text
INTERNAL_SCALE_STRUCTURE_GATE_BUILT_REVIEW_ONLY_NO_CLOCK_PROMOTION
```

The gate admits external scale labels only as bookkeeping and admits one
synthetic internal-scale packet only as a future review target. It earns no
internal scale structure, record clock, duration, temporal arrow, record
finality change, scale-genesis theorem, physics claim, claim-ledger movement,
roadmap movement, North Star movement, public-posture movement, or cross-repo
movement.

## Reproduction

```bash
python -m pytest tests/test_internal_scale_structure_admission_gate.py -q
python -m models.internal_scale_structure_admission_gate --write-results
```

Artifacts:

- `models/internal_scale_structure_admission_gate.py`
- `tests/test_internal_scale_structure_admission_gate.py`
- `results/T481-internal-scale-structure-admission-gate-v0.1.json`
- `results/T481-internal-scale-structure-admission-gate-v0.1-results.md`

## Contribution Needed

Future packets should decide whether they are external-bookkeeping packets or
internal-structure review packets before witness construction. Internal review
requires a TaF-native generating rule, predeclared comparison domain, positive
and negative controls, and relabel-invariance checks before any clock,
duration, finality, scale-genesis, RG, or physics language is considered.
