# T386 Results: Bidirectional Handshake Origin Screen

## Verdict

Raw compatibility still does not derive the handshake.

But the screen finds a stronger conditional result:

```text
If compatibility means local mutual attestability, and no global reconciler is
allowed, then the minimal witness is a two-leg bidirectional handshake.
```

Combined with T385:

```text
mutual local attestability
  -> minimal bidirectional handshake
  -> two primitive null compatibility-signal directions
```

## Protocol Results

| protocol | verdict | plain-English reason |
|---|---|---|
| `one_sided_readout` | rejected | One endpoint can read/receive, but the other endpoint cannot locally attest participation. |
| `broadcast_without_ack` | rejected | Broadcast is not pair-specific local compatibility and has no acknowledgment. |
| `shared_scalar_token` | rejected | A scalar token can be shared, but it supplies no directed signal geometry. |
| `global_reconciler_receipt` | rejected | Central reconciliation imports hidden global certification/order. |
| `minimal_bidirectional_handshake` | survivor | The minimal local mutual witness has one outgoing and one returning leg. |
| `three_phase_commit_handshake` | demoted | It is mutually attestable, but has extra primitive phases beyond the minimal witness. |
| `signed_anti_handshake` | rejected | It requires negative primitive source counts. |
| `asymmetric_receipt_handshake` | partial | Two directed legs exist, but only one endpoint keeps a local attestable receipt. |

## Strongest Claim

Raw compatibility still does not derive the handshake. But if compatibility
means local mutual attestability with no global reconciler, nonnegative source
counts, and minimality, then the minimal witness is a two-leg bidirectional
handshake. Combined with T385, that conditionally grounds the two-null basis.

## What This Clarifies

The live gap moved again.

It is no longer only:

```text
why two null channels?
```

or:

```text
why a round-trip handshake?
```

The sharper question is:

```text
why should compatibility mean mutual local attestability?
```

## Claim Ledger Update

Register T386 as:

```text
bidirectional_handshake_derived_from_mutual_attestability_not_raw_compatibility
```

## Next Open Object

```text
derive_or_falsify_mutual_attestability_semantics
```
