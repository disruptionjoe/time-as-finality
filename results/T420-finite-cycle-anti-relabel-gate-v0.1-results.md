# T420 - Finite-Cycle Anti-Relabel Gate - Results v0.1

- **Artifact:** `T420-finite-cycle-anti-relabel-gate-v0.1`
- **Problem:** `open-problems/computational-finality-arrow.md` (D2 after T419 REDESIGN)
- **Spec:** `tests/T420-finite-cycle-anti-relabel-gate.md`
- **Model:** `models/finite_cycle_anti_relabel_gate.py`
- **Test:** `tests/test_finite_cycle_anti_relabel_gate.py`
- **Tags:** D2_guardrail, finite_public_permutation, anti_relabel_gate,
  T419_K4_failure, period_hardness_required, no_claim_promotion

## Verdict

T420 holds as a guardrail. A closed finite public permutation supplies its own
predecessor recovery once the cycle is traversable:

```text
predecessor(y) = F^(L-1)(y)
```

where `L` is the cycle length containing `y`. If `L-1` is feasible or discoverable
inside the declared bound, a trapdoor-free agent recovers the predecessor by public
forward iteration. Therefore a finite toy cycle cannot support D2's proposed
computational arrow by itself.

This does **not** discharge D2, redesign it, abandon it, or promote a claim. It
only blocks one failure mode: asserting a temporal anti-relabel gap on an explicitly
finite public cycle.

## T419 Application

The T419 `QR_77` squaring permutation has state labels:

```text
[1, 4, 9, 15, 16, 23, 25, 36, 37, 53, 58, 60, 64, 67, 71]
```

With feasible step bound `3`, every cycle recovers its predecessor within bound.
The seed-4 orbit is:

```text
4 -> 16 -> 25 -> 9 -> 4
```

So the predecessor of `4` is recovered as `F^3(4) = 9`, using only the public
forward map. This is exactly the T419 K4 failure in reusable form.

## Long-Cycle Control

A length-17 public cycle with feasible bound `5` does **not** recover the
predecessor inside the bound. T420 classifies that outcome as inconclusive, not as
arrow evidence:

```text
bounded_search_inconclusive: non-recovery within this bound is not arrow evidence;
a family-level period-hardness assumption or a different regime must be declared
```

With feasible bound `16`, the same cycle recovers the predecessor publicly. The
control prevents the cheap move of treating bounded non-recovery as a D2 success.

## Relation To T110

T110 blocks strict scalar finality monotones on closed finite permutation orbits.
T420 blocks a sibling anti-relabel move: closed finite public permutation orbits
also provide their own public predecessor recovery once the cycle is traversable.

## Consequence For D2

A future D2 redesign cannot rely on a toy finite public cycle. It must do at least
one of the following:

- declare and defend family-level period hardness;
- change the agent's public transition knowledge;
- leave the closed public-permutation regime;
- demote the temporal story to T417's static E2 boundary.

No claim ledger, North Star, canon, public posture, or cross-repo truth movement.

## Reproduction

```bash
python -m pytest tests/test_finite_cycle_anti_relabel_gate.py -q
python -m models.finite_cycle_anti_relabel_gate
```
