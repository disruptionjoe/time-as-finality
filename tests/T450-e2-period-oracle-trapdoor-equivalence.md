# T450: E2 Period-Oracle Trapdoor Equivalence

## Route

D2 computational finality / E2 hardness lane, after T449 sharpened the remaining
closed public-permutation route to a hidden-order / cycle-length theorem target.

## Question

Is the T449 period-hardness route independent of the T417/Rabin trapdoor, or does
a useful period oracle collapse to predecessor recovery and hence to factoring?

## Candidate

For public squaring on `QR_N`:

```text
F_N(x) = x^2 mod N
```

If the cycle period `L` of a target `y` is known, the predecessor is:

```text
F_N^(L-1)(y)
```

That predecessor is the unique `QR_N` square root, i.e. the principal square
root. Rabin's square-root oracle reduction then factors `N`.

## Success Criteria

- For each T449 toy-family row, period-oracle predecessor recovery verifies
  `F(predecessor)=target`.
- An all-target period oracle gives a predecessor oracle.
- The predecessor oracle factors each toy modulus through Rabin reduction.
- Factorization / group-order completion computes the same period values as T449.
- Single-seed and single-challenge period values are classified as too weak to
  be family D2 evidence.
- All-target period oracles are classified as trapdoor-strength.
- No D2 redesign/abandon, claim promotion, crypto theorem, physics claim, or
  public posture is asserted.

## Failure Criteria

- Treat a single seed period as an arbitrary-target predecessor oracle.
- Treat a challenge-specific period value as a family oracle.
- Treat an all-target period oracle as weaker than trapdoor strength without
  explaining why Rabin reduction no longer applies.
- Treat trapdoor/group-order completion as new temporal residue.
- Edit `TESTS.md`, `CLAIM-LEDGER.md`, `ROADMAP.md`, North Star files, dirty
  governance files, public posture, hard policy, or T442 files.

## Claim Impact

No claim movement. T450 is a recorded-tier trapdoor-equivalence audit only. It
strongly recommends treating the current closed public-squaring period route as
absorbed by T417/Rabin unless a future theorem target changes the oracle scope or
assumption.

## Reproduction

```bash
python -m pytest tests/test_e2_period_oracle_trapdoor_equivalence.py -q
python -m models.e2_period_oracle_trapdoor_equivalence --write-results
```
