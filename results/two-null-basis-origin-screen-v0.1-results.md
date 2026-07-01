# T385 Results: Two-Null Basis Origin Screen

## Verdict

The screen does not derive the two-null basis from compatibility alone.

It does find a sharper minimal origin story:

```text
If compatibility must be expressed as a local round-trip handshake, then exactly
two primitive null compatibility-signal directions are the minimal clean basis.
```

So the open object moves from:

```text
basis_origin
```

to:

```text
handshake_origin
```

## Origin-Principle Results

| origin | verdict | plain-English reason |
|---|---|---|
| `absolute_clock_origin` | rejected | Imports the global time structure the substrate is supposed to render. |
| `scalar_source_action_origin` | rejected | Gives a local scalar, but no directional signal geometry. |
| `one_way_signal_origin` | rejected | One direction cannot close reciprocal observer calibration. |
| `minimal_handshake_origin` | survivor | A request/return or send/ack loop supplies two directions, local coupling, reciprocal calibration, and no global clock. |
| `overcomplete_broadcast_origin` | demoted | Extra primitive directions are not minimal and either overconstrain or factor through the two-direction basis. |
| `signed_cancellation_origin` | rejected | Requires negative primitive source counts. |
| `gauge_relabel_origin` | partial | Preserves local labels/identity, but does not originate calibrated signal rays. |

## Strongest Claim

A compatibility-only scalar, global clock, or one-way origin fails. A minimal
local round-trip handshake uniquely motivates exactly two primitive null
compatibility-signal directions within the declared screen, but the need for
bidirectional acknowledgment is still an imported premise.

## What This Clarifies

The two-null adapter is no longer just an arbitrary shape in the story. It is
the minimal form of a local reciprocal compatibility handshake.

But this is still not the full derivation. The next hard question is:

```text
Why must compatibility be bidirectional / round-trip in the first place?
```

## Claim Ledger Update

Register T385 as:

```text
two_null_basis_minimally_motivated_by_round_trip_handshake_not_derived_from_compatibility_alone
```

## Next Open Object

```text
derive_or_falsify_bidirectional_handshake_origin
```
