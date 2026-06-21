# Technical Report: Cyclic Reconciler Entropy Export v0.1

## Claim Under Test

H7 says finality structure can induce an observer-relative temporal direction
when admissible transformations are monotone in D1 finality. T18 proves that
as a conditional constructor theorem. T80 showed that raw observer-window
finality can decrease under reversible local dynamics. T82 then showed that
adding persistent memory helps only if the observer either uses irreversible
OR-style coarse-graining or consumes append-only blank ledger capacity.

T84 tests the next repair candidate: recycle the append-only ledger as a
fixed-size cyclic reconciler. If this worked, H7 would gain a stronger
physical-arrow foothold because persistent monotone records would not require
unbounded fresh memory.

## Artifact

The model uses the same T80 observation sequence:

```text
observed masks = (10, 11, 10, 00, 10, 11)
raw support = (1, 2, 1, 0, 1, 2)
```

It feeds those two-bit masks into a three-slot cyclic ring. At each step the
current observation overwrites the slot under the cursor.

Two accounting policies are compared:

```text
reversible export:
  write the new observation into the ring
  export the overwritten slot as external history

erasing heat bath:
  write the new observation into the ring
  discard the overwritten slot
```

The finite-map audit checks whether the one-step update is injective and how
many logical bits are lost in the generic recycle step.

## Current Strongest Claim

In the T80 observation witness, a fixed-size cyclic reconciler does not
produce monotone local retained records. Monotonicity returns only when
overwritten slots are exported as history or discarded through an erasing
heat-bath channel.

## Evidence

| Policy | Local support | Local monotone | Accounted support | Accounted monotone | Injective | Logical loss |
| --- | --- | --- | --- | --- | --- | ---: |
| Cyclic reversible export | (1, 3, 4, 3, 2, 3) | false | (1, 3, 4, 4, 5, 7) | true | true | 0 bits |
| Cyclic erasing heat bath | (1, 3, 4, 3, 2, 3) | false | (1, 3, 4, 4, 5, 7) | true | false | 2 bits per generic two-bit recycle |

The reversible export update is injective because the old slot is included in
the output. But then monotone support belongs to `ring + exported history`,
not to the fixed local observer ring.

The erasing update leaves the same local ring trajectory. Its generic finite
map has four preimages per image for a two-bit slot, hence 2 bits of logical
information loss per generic recycle update. Counting the erased support
recovers the same monotone curve, but this is not retained local record
memory; it is erasure bookkeeping.

## What This Improved

T84 closes the most obvious T82 loophole. "Make the ledger cyclic" does not
remove the resource boundary. It splits the repair into:

```text
local cyclic memory: nonmonotone
local memory plus exported history: monotone but no longer local
local memory plus erasure accounting: monotone only as entropy export
```

This makes H7 more evaluable because any proposed autonomous observer must
identify whether old records remain in the observer, leave as recoverable
history, or are erased into an environment.

## What This Weakened

H7 is further weakened as a physical-arrow claim. The toy cyclic observer
does not show a finality direction independent of thermodynamic accounting.
If exported history is counted, the arrow is carried by retained garbage. If
history is discarded, the update is non-injective and pays the ordinary
erasure cost. If only fixed local memory is counted, D1 support decreases.

## Falsification Condition

T84 fails if a fixed-capacity cyclic reconciler gives monotone local
retained-record support for the T80 sequence while remaining injective and
without exporting overwritten slots, erasing them, or hiding them in
inaccessible garbage.

## Claim Ledger Update

H7 should remain `partially_supported` only as a conditional constructor
theorem. T84 adds a cyclic-reconciler boundary: fixed local cyclic memory does
not supply monotone retained records in the T80 witness. Monotonicity is
recovered only by exported history/garbage or by erasure with positive
logical loss. The finality-induced direction has still not been separated
from entropy export in a physically autonomous observer.

## Open Blocker

No cyclic finite observer has yet produced D1-monotone local records under
reversible dynamics without an explicit export, garbage, or heat-bath
account.

## Next Work

Try a logically reversible compression/export model with a bounded entropy
sink and ask whether any nontrivial D1 monotone survives after the sink is
included in the state space.

## Reproduction

```bash
python -m unittest tests.test_cyclic_reconciler_entropy_export -v
python -m models.run_t84
```
