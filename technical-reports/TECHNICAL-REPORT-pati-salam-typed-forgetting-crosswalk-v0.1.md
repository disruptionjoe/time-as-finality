# Technical Report: Pati-Salam Typed Forgetting Crosswalk v0.1

## Claim Under Test

The GU Pati-Salam verification is useful to TaF only if it provides a precise
mathematical witness for typed structure preservation. The candidate witness is
the hypercharge map:

```text
Y = T3R + (B-L)/2
```

The test is whether forgetting `T3R` while retaining `B-L` preserves the
16-state carrier but fails to reconstruct the Standard-Model one-generation
`n = 6Y` table.

## Artifact

T88 implements the crosswalk inside TaF:

- builds the Spin(10) chiral 16 from weights `(+-1/2)^5` with even minus
  parity;
- computes `B-L`, `T3L`, `T3R`, hypercharge, charge, and `n = 6Y`;
- compares the full Pati-Salam map with the `B-L`-only projection;
- records the lost structure as a `LossKernel`;
- explicitly refuses a PO1 or physics-upgrade reading.

## Result

The full map exactly reconstructs the six-row table:

```text
(3,    2, +1, 6)
(3bar, 1, +2, 3)
(3bar, 1, -4, 3)
(1,    2, -3, 2)
(1,    1, +6, 1)
(1,    1,  0, 1)
```

The `B-L`-only projection preserves total dimension `16` but merges the
right-singlet rows:

```text
(3,    2, +1, 6)
(3bar, 1, -1, 6)
(1,    2, -3, 2)
(1,    1, +3, 2)
```

So the projected `n` set is `{-3, -1, +1, +3}` rather than
`{-4, -3, 0, +1, +2, +6}`.

## Current Strongest Claim

The GU Pati-Salam verification supplies a clean external typed-forgetting
witness for TaF: the 16-state carrier and `B-L` data survive the naive
projection, but the forgotten `T3R` term is load-bearing for the
Standard-Model hypercharge invariant.

## What This Improved

T88 gives TF1 a non-TaF, non-software-example witness where named forgotten
structure is demonstrably necessary for a downstream invariant. It also
clarifies that some useful GU material belongs in TaF as mathematical
machinery, not as shared physics.

## What This Weakened Or Falsified

T88 weakens any broad GU/TaF bridge language. This is not a PO1 instance under
the current TaF definition because no `D1RestrictionSystem` gluing obstruction
has been built. It is a typed invariant-reconstruction failure under a lossy
projection.

It also does not validate GU physics. The source GU finding is group-theoretic:
it checks the standard `SO(10) -> Pati-Salam -> SM` representation arithmetic,
not whether nature realizes the breaking chain.

## Falsification Condition

Reject this crosswalk if `B-L` alone reproduces the paper `n=1` multiplet
table, if the full Pati-Salam map fails to reproduce the table, or if the
failure can be repaired without restoring a right-isospin-equivalent term.

## Claim Ledger Update

TF1 can be updated, without status upgrade, as follows:

```text
T88 adds an external finite representation-theory witness for typed forgetting:
the Pati-Salam hypercharge table is preserved by the full map
Y = T3R + (B-L)/2 but not by the B-L-only projection. The lost structure is
named as SU2R_cartan_T3R/right_isospin_splitting. This supports LossKernel as
an attribution vocabulary, not TaF or GU physics.
```

## Open Blocker

The witness is not yet embedded in `D1RestrictionSystem`, PO1, or a categorical
typed-transport object. It is an invariant-preservation/loss example, not a
local-to-global obstruction theorem.

## Next Work

If continued, recast this case as an explicit typed transport object with
source, target, preserved invariants, and LossKernel fields. Only after that
should it be tested against PO1-style gluing machinery.

## Reproduction

```bash
python -m unittest tests.test_pati_salam_typed_forgetting_crosswalk -v
python -m models.run_t88
```
