---
document_type: synthesis_status
batch_item: seventh_20_task_18
status: complete
authority: non_authoritative
write_scope: workflows/logs/synthesis
claim_effect: none
---

# T217 Two-Layer Transport / Record Capability Status

## Status

This note summarizes the two-layer capability object. It is an audit discipline
artifact, not a new physics result.

## Sources read

- `tests/T217-two-layer-transport-record-capability-object.md`
- `results/T217-two-layer-transport-record-capability-object-v0.1-results.md`
- `tests/T215-fixed-native-network-record-finality-split.md`
- `tests/T216-record-policy-native-absorber-audit.md`

## Plain-English finding

Transport timing and record finality should not be collapsed into one number.
They answer different tasks and have different native absorbers.

## Technical conclusion

T217 types the safe product object:

```text
Cap(Y) = (C_flow(D,q), record_reconstructable(policy))
```

The flow coordinate belongs to native transport/network theory. The record
coordinate belongs to provenance/ledger/audit theory. The product is useful
because it prevents two mistakes:

- inferring record finality from transport timing alone;
- treating transport absorption as record-finality absorption.

## Minimum next task

For any future witness, declare the task and coordinates before seeing the
split. Then test whether either coordinate survives after its native absorber
is granted.

## Stop condition

Stop if the product coordinates are chosen after the fact to preserve a split.

