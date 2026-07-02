# T400 Results: Boundary-Forced Task Gate

- **Artifact:** `T400-boundary-forced-task-gate-v0.1`
- **Spec:** [tests/T400-boundary-forced-task-gate.md](../tests/T400-boundary-forced-task-gate.md)
- **Model:** [models/boundary_forced_task_gate.py](../models/boundary_forced_task_gate.py)
- **Numbers:** [T400-boundary-forced-task-gate-v0.1.json](T400-boundary-forced-task-gate-v0.1.json)

## Verdict

T400 operationalizes the post-T399 burden as a finite task gate.

T399's measurement substrate is preserved:

- `R` trace distance: `0.0`
- boundary-local trace distance: `0.0`
- finite `R` intervention menu max difference: `0.0`
- region-only binary success: `0.5`
- boundary-crossing success: `1.0`

The task gate separates three cases:

- T399-style optional state-label readout fails with
  `optional_boundary_menu_only` and is labeled
  `absorbed_optional_enlarged_access`.
- The synthetic `R:B` parity task passes the formal gate because its declared
  output requires variables from both sides of the boundary, but it remains
  `formal_positive_control_only`.
- Hidden-datum, closure-key, and class-marker shortcuts all fail with explicit
  absorber labels.

## Interpretation

The artifact does not supply the desired domain-native Direction-A
discriminator. It only makes the gate executable:

```text
boundary crossing must be forced by the declared task/setup,
not merely admitted as ordinary enlarged-state access
```

The useful next move is therefore narrower: replace the synthetic parity
control with a physical or finality-native task declared before the witness
pair is selected.

No claim-ledger movement. No North Star, canon, public posture, or external
resource-theory language changed.

## Verification

```text
python -m pytest tests/test_boundary_forced_task_gate.py -q
8 passed in 0.18s

python -m models.boundary_forced_task_gate
json-ok
```

