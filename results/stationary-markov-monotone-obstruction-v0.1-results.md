# T122 Results: Stationary Markov Monotone Obstruction

## Strongest claim

In a finite Markov model at a stationary distribution, any scalar finality score with nonnegative one-step expected drift on every state in the stationary support has zero drift on that support. Strict H7-style monotonicity can appear only in transient or nonstationary sectors, or after naming a sink, boundary, capacity resource, postselection, or excluded reverse channel.

## Scenario table

| Scenario | Score | Stationary support | Drift | Weighted drift | Classification |
| --- | --- | --- | --- | ---: | --- |
| `detailed_balance_two_state_control` | `[0.0, 1.0]` | `[0, 1]` | `[0.2, -0.19999999999999996]` | 0.000000000000 | `not_a_monotone` |
| `biased_three_cycle_control` | `[0.0, 1.0, 2.0]` | `[0, 1, 2]` | `[1.1, 0.8, -1.9]` | 0.000000000000 | `not_a_monotone` |
| `absorbing_append_transient_control` | `[0.0, 1.0, 2.0, 3.0]` | `[3]` | `[1.0, 1.0, 1.0, 0.0]` | 0.000000000000 | `transient_only_monotonicity` |

## Deterministic finite-map sanity checks

| States | Transitions checked | Score assignments each | Recurrent strict monotones | All-state nondecreasing | Transient-only strict | Theorem holds |
| ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 2 | 4 | 9 | 0 | 24 | 6 | `True` |
| 3 | 27 | 27 | 0 | 306 | 147 | `True` |
| 4 | 256 | 81 | 0 | 5376 | 3528 | `True` |

## What this improved

T122 turns the T116 zero-resource stochastic record-arrow gate into a stationary finite-Markov obstruction. It separates true stationary support from positive-looking transient append paths.

## What this weakened

H7 is weakened as an independent thermodynamic-arrow proposal. Finite stationary stochastic dynamics cannot carry a strict scalar expected-finality arrow on their stationary support; any candidate arrow must be paid for by nonstationary resource drawdown, a boundary condition, or ordinary stochastic thermodynamic structure.

## Falsification condition

T122 is falsified by a finite Markov chain with a declared stationary distribution pi, piP=pi, and scalar D1-relevant score f such that E[f(X_{t+1})-f(X_t)|X_t=i] >= 0 for every state i with pi_i>0, with strict positivity for at least one such state, and with no time-dependent score, hidden state, omitted reverse channel, transient-only support, or nonstationary resource drawdown.

## H7 update

Add T122 to H7: the finite stationary Markov obstruction blocks the stationary version of a zero-resource record arrow. Strict expected finality cannot increase on stationary support without leaving the assumptions.

## Claim ledger update

H7 remains partially supported only as a conditional constructor/resource-accounting claim. T122 proves the finite stationary Markov obstruction: for piP=pi, the pi-weighted expected drift of any scalar finality score is zero, so nonnegative drift on every stationary-support state must be zero there. Strict stochastic record arrows require transient support, nonstationary resource drawdown, boundary/sink accounting, postselection, or excluded reverse channels.

## Open blocker

The remaining H7 route must be nonstationary, infinite-state, coarse-grained, or resource-explicit. It must quantify the free-energy, boundary, memory, or capacity drawdown rather than calling that drawdown finality.

## Recommended next

Demote H7's paper-facing label from thermodynamic-arrow claim to constructor/resource-accounting lemma, then decide whether a nonstationary free-energy model is still worth pursuing.
