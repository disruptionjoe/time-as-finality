# S6 G9 Same Final Record Capability Pair Results

Result: focused tests pass `5/5`.

Machine-readable output:

- [s6-g9-same-final-record-capability-pair-v0.1.json](s6-g9-same-final-record-capability-pair-v0.1.json)

## Status

This is G9 in the second S6 ambitious-goal sequence.

It builds the clean finite S1/S6 capability non-factorization witness:

```text
aF_phase = aF_plain
Cap(F_phase) != Cap(F_plain)
```

Both presheaf cases carry the same pointer and provenance fields. The generic
G8 finite associated-record engine therefore returns the same final record.

## Presheaf Pair

Phase-sensitive case:

```text
capabilities = read_pointer, reconstruct_provenance_order, phase_sensitive_branch
```

Plain case:

```text
capabilities = read_pointer, reconstruct_provenance_order
```

Both cases agree on the final record fields:

```text
pointer        = 1
prep_measure   = true
measure_record = true
```

## Associated Record

The associated records match exactly on:

```text
values
final_capabilities
```

Final capabilities:

```text
read_pointer
reconstruct_provenance_order
```

Only the phase-sensitive presheaf loses:

```text
phase_sensitive_branch
```

## Interpretation

G9 is the strongest finite S1/S6 witness so far because the same final record
can be produced from two locally different capability profiles. The loss is
visible only across the unit map from local presheaf data into the associated
record.

## Guardrail

```text
Finite same-final-record pair only: demonstrates capability loss across
declared descent, not a new quantum separation theorem.
```

The capability difference is intentionally finite and declared. A stronger
witness should source the capability difference from a known quantum task or
resource monotone.

## Verdict

```text
Project[O] + Finalize[R] + Lose[K]
not Issue[S]
```

## Reproduction

```bash
python -m unittest tests.test_s6_g9_same_final_record_pair -v
python -m models.run_s6_g9_same_final_record_pair --output results/s6-g9-same-final-record-capability-pair-v0.1.json
```
