# T122: Stationary Markov Monotone Obstruction

## Route

Thermodynamic arrow of time.

## Question

After T116, can a finite stationary stochastic record process support a strict
H7 finality arrow without path irreversibility, exported history, fresh blank
capacity, postselection, omitted reverse dynamics, or nonstationary resource
drawdown?

## Motivation

T110 blocks strict scalar finality monotones inside finite closed reversible
permutation dynamics. T116 shows that the tested open Markov arrows are
absorbed by entropy/export/capacity accounting. The remaining clean loophole is
a finite stationary Markov chain with a scalar score whose expected finality
drift is nonnegative everywhere on stationary support and strict somewhere.

## Success Criteria

- State and test the finite stationary Markov obstruction.
- Include a detailed-balance control.
- Include a biased stationary cycle control where circulation does not rescue
  a scalar finality arrow.
- Include an absorbing append control showing that positive-looking monotonicity
  can live only off stationary support.
- Exhaust small deterministic finite maps as a sanity check for recurrent
  versus transient monotonicity.
- Give a falsification condition that a future H7 model would have to clear.

## Failure Criteria

- Treat transient append paths as stationary arrows.
- Ignore the stationary distribution while claiming a stochastic monotone.
- Count strict increase on zero-probability states as an H7 success.
- Hide nonstationary free-energy or capacity drawdown.
- Upgrade H7 as a thermodynamic-arrow claim.

## Claim Impact

If T122 holds, finite stationary Markov dynamics cannot supply the missing
zero-resource stochastic record arrow. H7 should be demoted in paper-facing
language to a constructor/resource-accounting lemma unless a nonstationary,
infinite-state, or resource-explicit model is produced and compared with
standard thermodynamics.

## Reproduction

```bash
python -m unittest tests.test_stationary_markov_monotone_obstruction -v
python -m models.run_t122
```
