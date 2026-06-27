# T255: Nine-Event Ordinal Mutation Sensitivity

## Target Claims

- [S1: Spacetime As Consensus Envelope](../claims/S1-spacetime-consensus-envelope.md)
- [T252: Nine-Event Ordinal T54 Band Witness](T252-nine-event-ordinal-t54-band-witness.md)

## Central Question

Is the T252 selected permutation an isolated point, or do nearby one-swap
mutations also pass the finite T126/T156 screens?

## Setup

Audit all 36 one-transposition neighbors of the T252 permutation. For each
neighbor, run T126 and the same T156 ordering-fraction band.

## Success Criteria

- Exactly 36 one-transposition mutations are audited.
- The result separates T126-pass-and-band, T126-pass-outside-band, and
  T126-blocked-inside-band cases.
- The result is treated as local sensitivity only, not a global abundance
  theorem.

## Failure Criteria

T255 fails if mutations are not single transpositions, if the diagnostic target
changes from T252, or if local neighborhood abundance is promoted to S1.

## Implementation Result

Status: implemented.

T255 finds a mixed local neighborhood: 21 mutations pass both T126 and the
band, 13 remain inside the band but are blocked by T126, and 2 pass T126
outside the band.

## Run Command

```bash
python -m unittest tests.test_t252_t255_nine_event_ordinal_controls -v
python -m models.run_t252_t255
```
