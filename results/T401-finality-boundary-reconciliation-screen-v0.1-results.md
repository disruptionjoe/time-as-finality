# T401 Results: Finality-Boundary Reconciliation Screen

- **Artifact:** `T401-finality-boundary-reconciliation-screen-v0.1`
- **Spec:** [tests/T401-finality-boundary-reconciliation-screen.md](../tests/T401-finality-boundary-reconciliation-screen.md)
- **Model:** [models/finality_boundary_reconciliation_screen.py](../models/finality_boundary_reconciliation_screen.py)
- **Numbers:** [T401-finality-boundary-reconciliation-screen-v0.1.json](T401-finality-boundary-reconciliation-screen-v0.1.json)

## Verdict

T401 supplies a finite finality-native forced-task candidate for the post-T400
lane.

The two source distributions are:

```text
aligned      = 00 / 11 with probability 1/2 each
anti_aligned = 01 / 10 with probability 1/2 each
```

Local statistics do not separate them:

- `R` total variation: `0.0`
- boundary-local total variation: `0.0`
- finite `R` intervention menu max difference: `0.0`
- region-only binary success: `0.5`
- boundary-local binary success: `0.5`

The predeclared record-reconciliation task asks whether the bounded-region
holder and boundary holder attest the same event value:

- aligned relation: `same = 1.0`, `different = 0.0`
- anti-aligned relation: `same = 0.0`, `different = 1.0`
- joint record binary success: `1.0`

## Interpretation

The finality record-reconciliation task passes the forced-task gate because
the declared output requires both record holders and the `R:B` relation is
native to the task.

The result is still absorbed by ordinary joint-record completion: once both
holder records are admitted, the same/different relation is an ordinary finite
joint-record fact. Optional joint state labels, hidden datum in `R`, closure-key
shortcuts, and class-marker shortcuts all fail the audit.

No claim-ledger movement. No North Star, canon, public posture, or external
resource-theory language changed.

## Verification

```text
python -m pytest tests/test_finality_boundary_reconciliation_screen.py -q
11 passed

python -m models.finality_boundary_reconciliation_screen
json-ok
```
