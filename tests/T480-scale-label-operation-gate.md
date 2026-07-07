# T480: Scale-Label Operation Gate

## Target Claims

- [RG Flow as a Multiscale-Transport Analogy](../open-problems/rg-flow-as-multiscale-transport-analogy.md)
- [T24: D1 Multiscale Observer Field](T24-d1-multiscale-observer-field.md)
- [T38: Minimal Multiscale Transport Formalization](T38-minimal-multiscale-transport.md)
- [T479: RG-Flow Multiscale Calibration Gate](T479-rg-flow-multiscale-calibration-gate.md)

## Setup

T479 allowed the RG/conformal fixed-point neighbor only as a no-intrinsic-scale
calibration endpoint, and required a declared scale-label or symmetry-breaking
operation before clocks, durations, or scale-genesis language is used.

T480 tests that burden directly. It asks whether a future packet has declared a
TaF-native scale-label operation over field-valued D1 / H1+ transport, while
blocking fixed-point clocks, RG-scale imports, label-only packets, hidden
calendar order, duration or arrow extraction, finality-by-relabeling,
conformal-phenomenology support, and promotion shortcuts.

## Success Criteria

- T479 confirms the scale-label burden exists and did not earn clocks or scale
  genesis.
- T24 confirms field-valued D1 is required for transport and gluing claims.
- T38 confirms H1+ is the best-supported finite transport object.
- One positive bookkeeping packet is admitted.
- All clock, duration, RG-scale, hidden-calendar, finality, phenomenology, and
  claim-promotion controls are blocked.
- The result remains bookkeeping only.

## Failure Criteria

- The gate admits an RG scale parameter as a record clock.
- The gate lets a fixed point generate intrinsic clocks or duration.
- A label word counts as an operation.
- Hidden calendar order or temporal ordering is smuggled through labels.
- A scale label changes record-finality status by relabeling alone.
- The result promotes a physics claim, scale-genesis theorem, claim-ledger move,
  roadmap move, North Star move, public-posture move, or cross-repo truth.

## Known Physics Constraints

RG scale and conformal symmetry remain external analogy material. T480 does not
evaluate RG beta functions, conformal-gravity phenomenology, unitarity, rotation
curves, asymptotic freedom, or quantum gravity.

## Result

Implemented as T480 v0.1.

Expected verdict:

```text
SCALE_LABEL_OPERATION_GATE_BUILT_BOOKKEEPING_ONLY_NO_CLOCK_PROMOTION
```

The gate admits a declared scale-label operation only as bookkeeping over T24
field-valued D1 and T38 H1+ transport. It earns no record clock, duration,
scale-genesis theorem, physics claim, claim-ledger movement, roadmap movement,
North Star movement, public-posture movement, or cross-repo movement.

## Reproduction

```bash
python -m pytest tests/test_scale_label_operation_gate.py -q
python -m models.scale_label_operation_gate --write-results
```

Artifacts:

- `models/scale_label_operation_gate.py`
- `tests/test_scale_label_operation_gate.py`
- `results/T480-scale-label-operation-gate-v0.1.json`
- `results/T480-scale-label-operation-gate-v0.1-results.md`

## Contribution Needed

Future packets should state whether their scale label is external bookkeeping
or earned internal structure, declare what observers and transport edges can
compare after labeling, and keep clocks, durations, arrows, finality changes,
RG mechanics, and physics posture blocked unless separately earned.
