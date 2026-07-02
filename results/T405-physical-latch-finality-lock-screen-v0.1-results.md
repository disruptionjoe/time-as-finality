# T405 Physical-Latch Finality-Lock Screen v0.1 Results

## Status

Implemented finite screen. No claim promotion.

## Artifact

- Model: `models/physical_latch_finality_lock_screen.py`
- Test spec: `tests/T405-physical-latch-finality-lock-screen.md`
- JSON: `results/T405-physical-latch-finality-lock-screen-v0.1.json`
- Focused tests: `tests/test_physical_latch_finality_lock_screen.py`

## Result

T405 replaces T403's stipulated provisional/sealed finality flag with a finite
physical latch substrate.

The main pair:

- imports the same T403/T402 causal-domain signature;
- has the same joint payload and verdict payload;
- has the same revision budget and operation menu;
- has the same resource accounting, provenance, reversible-control class, and
  observer boundary;
- has the same latch support fields except topology;
- differs only in derived lock state:
  `physically_rewritable` versus `physically_sealed`.

The capability split is exactly:

```text
can_revise_final_verdict
```

The split survives the fixed-accounting projection but is absorbed by explicit
latch-substrate completion.

## Controls

Controls classify as expected:

- matched latch: `no_capability_split`
- two-bit resource burden: `absorbed_by_resource_accounting`
- invalid provenance: `absorbed_by_provenance_completion`
- disabled rewrite control: `absorbed_by_control_completion`
- closed observer boundary: `absorbed_by_boundary_completion`
- hidden source label: `blocked_hidden_label_shortcut`
- stipulated finality label: `blocked_stipulated_finality_label`

## Interpretation

This is useful progress, but it is absorptive. T405 shows that the post-T403
lane can be made less stipulative: the lock state is derived from finite latch
topology rather than accepted as a label. It also shows that this stronger
screen still factors through ordinary substrate completion.

No North Star, canon, claim-ledger, public-posture, or cross-repo truth change
is earned.

## Next Burden

A future upgrade needs a substrate-native irreversibility or operation-
unavailability result that does not factor through explicit latch topology,
resource state, provenance state, control handle, or observer boundary.
