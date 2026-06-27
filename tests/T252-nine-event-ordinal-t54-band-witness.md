# T252: Nine-Event Ordinal T54 Band Witness

## Target Claims

- [S1: Spacetime As Consensus Envelope](../claims/S1-spacetime-consensus-envelope.md)
- [T126: Finality-Colimit Causal-Set Embeddability Audit](T126-finality-colimit-causal-set-embeddability.md)
- [T156: Myrheim-Meyer Ordering-Fraction Screen](T156-myrheim-meyer-ordering-fraction-screen.md)
- [T249: Larger T54/T126 Canonical Colimit](T249-larger-t54-t126-canonical-colimit.md)

## Central Question

Can a same-scale nine-event T54-native witness avoid the T249 grid's
over-ordering and land inside the declared flat 1+1 ordering-fraction band?

## Setup

Use the fixed ordinal permutation:

```text
(0, 5, 6, 7, 8, 1, 2, 3, 4)
```

Build a two-observer T54 datum whose record order is the permutation order,
then run T54, T126, and T156 on the same strict relation.

## Success Criteria

- T54 completion is canonical.
- T126 verdict is `passes_filter_only`.
- Ordering fraction is `5/9`.
- T156 verdict is `passes_ordering_fraction_control_only`.
- S1 is not upgraded.

## Failure Criteria

T252 fails if the witness is synthetic rather than T54-completed, if T126 and
T156 use different strict relations, or if a selected finite control is treated
as typical or continuum-facing.

## Implementation Result

Status: implemented.

T252 finds one selected nine-event T54-native ordinal control that passes T126
and the declared ordering-fraction band. This is a control, not a generative
spacetime result.

## Run Command

```bash
python -m unittest tests.test_t252_t255_nine_event_ordinal_controls -v
python -m models.run_t252_t255
```
