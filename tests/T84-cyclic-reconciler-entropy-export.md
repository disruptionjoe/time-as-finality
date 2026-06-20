# T84: Cyclic Reconciler Entropy Export

## Route

Thermodynamic arrow of time.

## Question

Can the T82 append-only ledger repair be made cyclic with fixed local memory,
so that H7 gets monotone retained records without ordinary entropy export,
garbage retention, or erasure?

## Result

The finite witness is a weakening result.

Using the T80 reversible Rule 30 observation sequence:

```text
observed masks = (10, 11, 10, 00, 10, 11)
raw support = (1, 2, 1, 0, 1, 2)
```

a three-slot cyclic reconciler has local ring support:

```text
local ring support = (1, 3, 4, 3, 2, 3)
```

This is not monotone. Monotonicity returns only after adding an external
accounting channel:

```text
exported-slot support = (0, 0, 0, 1, 3, 4)
ring + export support = (1, 3, 4, 4, 5, 7)
```

The reversible export update is injective because every overwritten slot is
preserved as external history. The erasing cyclic update is non-injective:
for a generic two-bit slot recycle it loses 2 bits, with 4 preimages per
image.

## Claim Impact

H7 remains only conditionally supported. A cyclic reconciler does not supply
an autonomous local arrow in this witness. It either exports overwritten
records, hides them as garbage/history, or erases them with positive logical
loss.

## Falsification Condition

T84 fails if a fixed-capacity cyclic reconciler gives monotone local
retained-record support for the T80 sequence while remaining injective and
without exporting overwritten slots, erasing them, or hiding them in
inaccessible garbage.

## Reproduction

```bash
python -m unittest tests.test_cyclic_reconciler_entropy_export -v
python -m models.run_t84
```
