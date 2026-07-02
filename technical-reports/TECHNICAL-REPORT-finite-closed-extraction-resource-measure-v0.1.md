# Finite-Closed Extraction-Resource Measure v0.1

## Status

Support artifact for
`open-problems/finite-closed-capability-boundary-scope-theorem.md`.

No claim promotion. No `CLAIM-LEDGER.md` edit. No `TESTS.md` registration. No
North Star, canon, public-posture, physics, or cross-repo movement.

## Purpose

The scope theorem candidate left one honest softness: what exactly is the
extraction resource in the Part-2 closure argument?

This note gives the v0.1 answer. It does not establish the theorem; it makes the
single-instance ceiling precise enough to test and attack.

## Finite Closed Boundary Instance

A finite closed boundary instance is:

```text
I = (C, V, F, d)
```

where:

- `C` is a finite set of configurations.
- `V : C -> X` is the visible signature produced by the declared region and
  region-supported menu.
- `F : C -> Z` is the co-present closed code retained by the closed model.
- `d : C -> K` is the boundary-crossing datum or capability readout.

Closedness for this support artifact means:

```text
F(c1) = F(c2) => d(c1) = d(c2)
```

So the closed code determines the datum. The visible region has a boundary when:

```text
V(c1) = V(c2)
d(c1) != d(c2)
```

Equivalently, `d` does not factor through `V`.

## Extraction Measure

For a single finite instance, define the lookup extractor:

```text
E_I : im(F) -> K
E_I(F(c)) = d(c)
```

This is well-defined by closedness.

Define the single-instance lookup cost:

```text
L(I) = |im(F)|
```

Then:

```text
L(I) <= |C| < infinity
```

Therefore every single finite closed instance has a finite extraction upper
bound. The extractor may be enormous, useless, or physically unavailable under a
declared budget; the point is exactly that finite single-instance
"prohibitiveness" is not absolute. It is relative to a budget or to a family.

## Consequence For The Scope Theorem

The Part-2 closure argument can now be stated without the soft phrase
"extraction resource":

1. If `d` separates a visible fiber but is determined by the finite closed code
   `F`, then a finite lookup extractor exists for that instance.
2. A stipulated finite budget that forbids using that extractor is an `E0`
   declared gap.
3. A non-declared physical boundary needs a family-level resource statement:
   either an unconditional asymptotic lower-bound theorem (`E1`) or a forcing
   assumption / hardness hypothesis (`E2`).

This does not prove any lower bound. It blocks only the single-instance shortcut.

## Witness Normal Forms

The executable support model checks three existing witness shadows:

| Witness | Visible signature `V` | Closed code `F` | Datum `d` | Gap mode |
| --- | --- | --- | --- | --- |
| T411 departed-record shadow | all `R`-supported statistics equal | retained tier-1 witness | boundary readout | `E0` declared/crackable |
| T413 grand-coalition shadow | all proper coalitions equal | grand-coalition value | certificate present/absent | `E0` single instance; `E1` only in the non-atomic limit |
| T417 QR shadow | Jacobi `+1` signature | `(x, N)` | quadratic residue class | `E2` hardness plus `E1` family growth |

All three have finite single-instance lookup upper bound `2` in the compressed
support fixture. T417 is not an exception to the finite ceiling: it becomes
interesting only because the family-level recovery cost grows and the hardness
assumption denies a feasible shortcut.

## Limits

This support artifact does not claim:

- that the scope theorem is promoted;
- that the Part-2 taxonomy is externally established;
- that T417 proves cryptographic hardness;
- that any physics-facing boundary has been built;
- that lookup cost is a natural physical cost.

It only formalizes the internal bookkeeping needed for the closure argument.
The next internal-rigor steps are a model-class statement of finite closed
systems and hostile review against the `E0/E1/E2` exhaustiveness taxonomy.

## Reproduction

```bash
python -m pytest tests/test_finite_closed_extraction_resource_measure.py -q
python -m models.finite_closed_extraction_resource_measure
```
