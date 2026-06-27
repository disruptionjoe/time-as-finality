# T253: Nine-Event Ordinal Deletion Stability

## Target Claims

- [S1: Spacetime As Consensus Envelope](../claims/S1-spacetime-consensus-envelope.md)
- [T156: Myrheim-Meyer Ordering-Fraction Screen](T156-myrheim-meyer-ordering-fraction-screen.md)
- [T252: Nine-Event Ordinal T54 Band Witness](T252-nine-event-ordinal-t54-band-witness.md)

## Central Question

Does the T252 selected ordinal witness remain inside the declared
ordering-fraction band after every single-event deletion?

## Setup

For each of the nine events, restrict the T252 strict relation after deleting
that event. Run T126 and T156 on the restricted relation.

## Success Criteria

- All nine deletion cases are audited.
- Every deletion passes T126.
- Every deletion remains inside the declared `1/2 +/- 1/10` band.
- The result is reported as finite control-only.

## Failure Criteria

T253 fails if deletion suborders are not restrictions of the T252 relation, if
any failed deletion is hidden, or if deletion stability is promoted into a
continuum claim.

## Implementation Result

Status: implemented.

T253 finds that all nine T252 single-event deletions pass T126 and remain
inside the declared ordering-fraction band.

## Run Command

```bash
python -m unittest tests.test_t252_t255_nine_event_ordinal_controls -v
python -m models.run_t252_t255
```
