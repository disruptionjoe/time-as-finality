# T251: T249 Deletion Stability Screen

## Target Claims

- [S1: Spacetime As Consensus Envelope](../claims/S1-spacetime-consensus-envelope.md)
- [T156: Myrheim-Meyer Ordering-Fraction Screen](T156-myrheim-meyer-ordering-fraction-screen.md)
- [T249: Larger T54/T126 Canonical Colimit](T249-larger-t54-t126-canonical-colimit.md)
- [T250: T249 Ordering-Fraction Screen](T250-t249-ordering-fraction-screen.md)

## Central Question

Is the T249 ordering-fraction failure caused by one special grid event, or is
it stable under single-event deletion?

## Setup

For each event in the T249 quotient-union relation:

1. remove that event;
2. restrict the strict relation to the remaining eight events;
3. rerun T126 with the scale floor set to the subdatum size;
4. compare the resulting ordering fraction to the same T156 target.

## Success Criteria

- All nine single-event deletions are audited.
- Every deletion remains a T126 `passes_filter_only` case.
- No deletion lands inside the declared `1/2 +/- 1/10` band.
- The result is reported as finite-witness demotion, not as a continuum theorem.

## Failure Criteria

T251 fails if:

- deletion suborders are not computed from the T249 quotient-union relation;
- T126 and T156 are run on different strict relations;
- any deletion enters the declared target band without being reported;
- the result is promoted into a general random-sprinkling or spacetime claim.

## Implementation Result

Status: implemented.

T251 finds that all nine single-event deletions still pass T126 and all nine
remain outside the flat 1+1 ordering-fraction band. The T249 over-ordering is
therefore stable under this finite deletion screen.

## Run Command

```bash
python -m unittest tests.test_t251_t249_deletion_stability -v
python -m models.run_t251
```

## Boundary

T251 says only that this specific T249 grid witness is stably over-ordered
under single deletions. It does not settle S1 or rule out other T54-native
families.
