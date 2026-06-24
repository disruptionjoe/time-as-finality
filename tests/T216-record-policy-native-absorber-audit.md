# T216: Record-Policy Native Absorber Audit

## Target Claims

- T215 fixed native network record-finality split
- Capability Projection absorption protocol

## Origin

T215 finds a split at fixed network state. T216 asks whether that split survives
after record/provenance/ledger theory is granted its normal variables.

## Formal Target

Grant native record state:

```text
append-only flag
history retention
challenge window
provenance/audit policy
```

and test whether the split remains surprising.

## Setup / Fixtures

Use the T215 append-only and overwrite policies.

## Positive Control

If visible state omits record policy, reconstructability fails to factor
through the visible network state.

## Negative Control

If visible state includes record policy, reconstructability factors normally.

## Absorber Pass

Provenance, logging, ledger, and audit theory absorb the split. They already
treat history retention and append-only semantics as native state.

## Results

T215 survives as a useful TaF-shaped task, but not as canonical residue. It is
translation/formal-audit residue: the projection was underdescribed for a
record-reconstruction task.

## Verdict: absorbed

Absorbed by native record/provenance state completion.

## Falsification Conditions

Revisit if two systems with the same native record/provenance state still split
on reconstruction capability.

## Next Step

T217 types the two-layer capability so future runs do not conflate transport
and record-finality coordinates.
