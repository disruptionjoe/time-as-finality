# T388 Results: Mutual-Attestability Semantics Origin Screen

## Verdict

Raw compatibility still does not derive mutual local attestability.

But record-finalizable shared-state compatibility does:

```text
local finalizable shared state
  + durable receipts at both endpoints
  + source-owned authentic receipts
  + no global reconciler
  -> mutual local attestability
```

Combined with the previous ladder:

```text
record-finalizable shared-state compatibility
  -> mutual local attestability
  -> bidirectional handshake
  -> two primitive null compatibility-signal directions, conditionally
```

## Semantics Results

| semantics | verdict | plain-English reason |
|---|---|---|
| `raw_predicate_compatibility` | rejected / underdetermined | A bare compatible/incompatible predicate has no witness, receipt, persistence, or finality semantics. |
| `symmetric_label_compatibility` | partial | A mirrored label is not the same thing as endpoint-owned durable receipts. |
| `shared_scalar_token_compatibility` | rejected | A scalar token can be shared without finalizing a pairwise relation record. |
| `one_sided_readout_compatibility` | rejected | One endpoint cannot locally attest the relation. |
| `global_reconciled_compatibility` | rejected | Central reconciliation imports hidden certification/order. |
| `spoofed_receipt_compatibility` | rejected | Receipts do not count if spoofed, replayed, unowned, or equivocal. |
| `asymmetric_persistence_compatibility` | partial | Mutuality cannot be final if one side lacks durable persistence. |
| `finalizable_shared_state_compatibility` | survivor | Durable source-owned authentic receipts at both endpoints force mutual local attestability. |

## Strongest Claim

Raw compatibility still does not derive mutual local attestability. But if
compatibility means local record-finalizable shared state, with durable
source-owned authentic receipts at both endpoints and no global reconciler, then
mutual local attestability follows. Through T386 and T385 this gives a
conditional path to the bidirectional handshake and two-null basis motivation.

## What Changed

The T387 top gap is no longer just "why mutuality?" Under record-finality
semantics, mutuality is forced.

The remaining live gap is now:

```text
How do two protocol legs become null signal geometry?
```

That includes nullness, bilinearity, invariant signal units, and whether the
two-leg protocol is more than an analogy.

## Claim Ledger Update

Register T388 as:

```text
mutual_attestability_derived_from_record_finalizable_shared_state_not_raw_compatibility
```
