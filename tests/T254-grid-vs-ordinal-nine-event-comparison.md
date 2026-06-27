# T254: Grid Vs Ordinal Nine-Event Comparison

## Target Claims

- [S1: Spacetime As Consensus Envelope](../claims/S1-spacetime-consensus-envelope.md)
- [T249: Larger T54/T126 Canonical Colimit](T249-larger-t54-t126-canonical-colimit.md)
- [T250: T249 Ordering-Fraction Screen](T250-t249-ordering-fraction-screen.md)
- [T251: T249 Deletion Stability Screen](T251-t249-deletion-stability-screen.md)
- [T252: Nine-Event Ordinal T54 Band Witness](T252-nine-event-ordinal-t54-band-witness.md)
- [T253: Nine-Event Ordinal Deletion Stability](T253-nine-event-ordinal-deletion-stability.md)

## Central Question

At the same nine-event scale, how different are the T249 product-grid witness
and the T252 selected ordinal witness under the T156 band and deletion screen?

## Success Criteria

- T249 is reported as over-ordered: parent band fail, 0/9 deletion band passes.
- T252 is reported as inside-band: parent band pass, 9/9 deletion band passes.
- The result is a comparison control, not an S1 upgrade.

## Failure Criteria

T254 fails if the witnesses use different diagnostic targets, if deletion pass
counts are misreported, or if the contrast is treated as a generative law.

## Implementation Result

Status: implemented.

T254 turns T249 and T252 into an explicit same-scale contrast: product-grid
shape is stably over-ordered, while the selected ordinal shape is stably inside
the declared band.

## Run Command

```bash
python -m unittest tests.test_t252_t255_nine_event_ordinal_controls -v
python -m models.run_t252_t255
```
