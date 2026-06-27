# T250: T249 Ordering-Fraction Screen

## Target Claims

- [S1: Spacetime As Consensus Envelope](../claims/S1-spacetime-consensus-envelope.md)
- [T126: Finality-Colimit Causal-Set Embeddability Audit](T126-finality-colimit-causal-set-embeddability.md)
- [T156: Myrheim-Meyer Ordering-Fraction Screen](T156-myrheim-meyer-ordering-fraction-screen.md)
- [T249: Larger T54/T126 Canonical Colimit](T249-larger-t54-t126-canonical-colimit.md)

## Central Question

Does the T249 nine-event T54-native grid colimit merely pass T126, or does it
also match the declared flat 1+1 Myrheim-Meyer ordering-fraction band?

## Setup

T250 reuses the exact T249 quotient-union relation and sends it through the
existing T156 target:

```text
target = 1/2 +/- 1/10
```

## Success Criteria

- T249 remains canonical under T54.
- T249 still passes the T126 finite filter.
- T250 computes the ordering fraction from the same strict relation.
- The T249 ordering fraction is recorded as `3/4`.
- The verdict is a demotion, not a spacetime-facing upgrade.

## Failure Criteria

T250 fails if:

- it sends a synthetic grid rather than the T249 quotient-union relation;
- it changes the target band after seeing the result;
- it treats a failed ordering-fraction screen as dimension evidence;
- it edits the claim ledger or roadmap.

## Implementation Result

Status: implemented.

T250 finds that T249 passes T126 but fails the declared flat 1+1 ordering
fraction target. The T249 ordering fraction is `3/4`, outside `1/2 +/- 1/10`.

## Run Command

```bash
python -m unittest tests.test_t250_t249_ordering_fraction_screen -v
python -m models.run_t250
```

## Boundary

T250 is a named-diagnostic demotion of one finite witness. It does not prove a
continuum no-go, estimate dimension, or settle S1.
