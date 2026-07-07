# T479: RG-Flow Multiscale Calibration Gate

## Target Claims

- [RG Flow as a Multiscale-Transport Analogy](../open-problems/rg-flow-as-multiscale-transport-analogy.md)
- [T24: D1 Multiscale Observer Field](T24-d1-multiscale-observer-field.md)
- [T38: Minimal Multiscale Transport Formalization](T38-minimal-multiscale-transport.md)
- [N15: Conformal Gravity as a Scale-Genesis Calibration Neighbor](../literature/N15-conformal-gravity-scale-genesis-calibration.md)

## Setup

T479 tests whether the RG-flow analogy can name the three minimum analogues
requested by the open problem without importing RG mechanics into TaF:

1. transported structure;
2. transport law;
3. fixed-point / scale-genesis endpoint.

The local TaF anchors are T24 field-valued D1 and T38 H1+ typed transport.
The external RG/conformal-gravity material remains pointer-grade analogy
context only.

## Success Criteria

- T24 confirms vector/field-valued D1 is required for multiscale transport and
  gluing claims.
- T38 confirms H1+ is the best-supported finite multiscale transport object.
- A positive calibration packet names all three analogues using T24/T38 objects.
- Coupling-flow import, action-functional import, clocked fixed-point overread,
  record-finality-from-RG overread, incomplete fixed-point-only packets, and
  conformal-phenomenology support are blocked.
- The result remains analogy-ledger only.

## Failure Criteria

- The gate admits RG beta functions as TaF record transport.
- The gate imports an action/Lagrangian onto records.
- The fixed-point analogue carries intrinsic scale, clocks, or duration before a
  declared scale-label operation.
- The result promotes a physics claim, RG/TaF equivalence theorem, scale-genesis
  theorem, claim-ledger move, North Star move, roadmap move, or public-posture
  move.

## Known Physics Constraints

RG flow transports coupling/effective-theory data, not record/finality data.
Conformal symmetry and scale genesis remain external analogy material. T479
does not evaluate conformal-gravity phenomenology, unitarity, rotation curves,
asymptotic freedom, or quantum gravity.

## Result

Implemented as T479 v0.1.

Expected verdict:

```text
RG_FLOW_CALIBRATION_GATE_BUILT_ANALOGY_ONLY_NO_PROMOTION
```

The gate admits one local calibration packet and blocks all mechanism-import
and posture-overread controls. It earns no D1, field-valued D1, RG/TaF,
scale-genesis, physics, claim-ledger, roadmap, North Star, public-posture, or
cross-repo movement.

## Reproduction

```bash
python -m pytest tests/test_rg_flow_multiscale_calibration_gate.py -q
python -m models.rg_flow_multiscale_calibration_gate --write-results
```

Artifacts:

- `models/rg_flow_multiscale_calibration_gate.py`
- `tests/test_rg_flow_multiscale_calibration_gate.py`
- `results/T479-rg-flow-multiscale-calibration-gate-v0.1.json`
- `results/T479-rg-flow-multiscale-calibration-gate-v0.1-results.md`

## Contribution Needed

Future packets should primary-source-check the RG/conformal-gravity neighbor
before any stronger use, and should define a TaF-native scale-label or
symmetry-breaking operation before talking about clocks, durations, or scale
genesis inside the record/finality system.
