# Technical Report: Stationary Markov Monotone Obstruction v0.1

## Claim Under Test

H7 says finality structure can induce an observer-relative temporal direction
when admissible transformations are monotone in D1 finality. T110 blocked a
strict scalar finality monotone in finite closed reversible permutation
dynamics. T116 then tested open stochastic fixtures and found no independent
arrow beyond path irreversibility, exported history, or fresh blank capacity.

T122 tests the remaining finite stationary Markov loophole: can a stationary
stochastic record process carry a strict scalar expected-finality arrow without
importing a sink, boundary, capacity resource, postselection, omitted reverse
channel, or nonstationary drawdown?

## Result

No. Let `P` be a finite Markov transition matrix, `pi` a stationary
distribution with `piP = pi`, and `f` a scalar finality score. Define the
one-step expected drift

```text
d_i = E[f(X_{t+1}) - f(X_t) | X_t = i].
```

Stationarity gives

```text
sum_i pi_i d_i = 0.
```

Therefore, if `d_i >= 0` for every state in the stationary support, then
`d_i = 0` on that support. A strict positive drift on any state with
`pi_i > 0` would make the stationary weighted drift positive, contradicting
`piP = pi`.

The executable fixtures check the boundary:

- a detailed-balance two-state control has zero weighted drift, but the score
  drifts up in one state and down in the other;
- a biased stationary three-cycle can have circulation, but the scalar score
  still cannot drift up everywhere on stationary support;
- an absorbing append control has strict positive drift only on transient
  states with zero stationary weight.

Small deterministic finite maps were also exhausted as a sanity check. They
allow nondecreasing scores to climb along transient trees into recurrent
classes, but no strict monotone lives on recurrent support.

## Current Strongest Claim

In a finite Markov model at a stationary distribution, any scalar finality
score with nonnegative one-step expected drift on every state in the stationary
support has zero drift on that support. Strict H7-style monotonicity can appear
only in transient or nonstationary sectors, or after naming a sink, boundary,
capacity resource, postselection, or excluded reverse channel.

## What This Improved

T122 turns the T116 zero-resource stochastic record-arrow gate into a
stationary finite-Markov obstruction. It separates true stationary support from
positive-looking transient append paths.

## What This Weakened Or Falsified

This does not falsify T18. T18 remains a conditional constructor theorem.

T122 weakens H7 as an independent thermodynamic-arrow proposal. Finite
stationary stochastic dynamics cannot carry a strict scalar expected-finality
arrow on their stationary support. Any candidate arrow must be paid for by
nonstationary resource drawdown, a boundary condition, or ordinary stochastic
thermodynamic structure.

## Falsification Condition

T122 is falsified by a finite Markov chain with a declared stationary
distribution `pi`, `piP=pi`, and scalar D1-relevant score `f` such that
`E[f(X_{t+1})-f(X_t)|X_t=i] >= 0` for every state `i` with `pi_i>0`, with
strict positivity for at least one such state, and with no time-dependent
score, hidden state, omitted reverse channel, transient-only support, or
nonstationary resource drawdown.

## Claim Ledger Update

Add T122 to H7:

```text
H7 remains partially supported only as a conditional constructor/resource-
accounting claim. T122 proves the finite stationary Markov obstruction: for
piP=pi, the pi-weighted expected drift of any scalar finality score is zero,
so nonnegative drift on every stationary-support state must be zero there.
Strict stochastic record arrows require transient support, nonstationary
resource drawdown, boundary/sink accounting, postselection, or excluded
reverse channels.
```

## Open Blocker

The remaining H7 route must be nonstationary, infinite-state, coarse-grained,
or resource-explicit. It must quantify the free-energy, boundary, memory, or
capacity drawdown rather than calling that drawdown finality.

## Next Work

Demote H7's paper-facing label from thermodynamic-arrow claim to
constructor/resource-accounting lemma, then decide whether a nonstationary
free-energy model is still worth pursuing.

## Reproduction

```bash
python -m unittest tests.test_stationary_markov_monotone_obstruction -v
python -m models.run_t122
```
