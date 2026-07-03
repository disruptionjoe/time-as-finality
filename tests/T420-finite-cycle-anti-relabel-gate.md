# T420: Finite-Cycle Anti-Relabel Gate

## Route

D2 computational finality / computational arrow of time.

## Question

Can the T419 K4 failure be made into a reusable gate for any alleged temporal
arrow exhibited on a closed finite public permutation?

## Motivation

T419 failed because the exhibited Rabin/BBS toy orbit was a short finite cycle.
Once the transition map is public, the recorded predecessor is recovered by
iterating the public forward map around the cycle. The result was not a distinct
computational arrow; it was T417's static square-root boundary relabelled along a
time index.

T420 isolates that failure condition so future D2 redesign work cannot pass by
asserting a trapdoor-free backward gap on an explicitly finite public cycle.

## Success Criteria

- State the finite-cycle predecessor lemma for public permutations.
- Apply it to T419's `QR_77` squaring permutation and seed-4 orbit.
- Show every T419 `QR_77` cycle has a public predecessor recovery cost of at most
  three forward steps.
- Include a long-cycle control where a small search bound fails, but the result is
  classified as "requires a period-hardness assumption," not as an earned arrow.
- Cross-link the gate to T110's finite closed permutation obstruction without
  changing H7 or claim status.

## Failure Criteria

- Treat bounded non-recovery as evidence for a computational arrow.
- Confuse point square-root hardness with predecessor hardness on a known finite
  cycle.
- Hide the cycle length, transition map, observed state, or feasible bound.
- Claim D2 is discharged, redesigned, abandoned, or promoted.
- Treat cryptographic or number-theoretic material as physics evidence.

## Claim Impact

No claim movement. If T420 holds, it only hardens the D2 anti-relabel guard:
finite public-cycle exhibitions are absorbed unless a future run declares and
defends family-level period hardness or leaves the closed public-permutation toy
regime.

## Reproduction

```bash
python -m pytest tests/test_finite_cycle_anti_relabel_gate.py -q
python -m models.finite_cycle_anti_relabel_gate
```
