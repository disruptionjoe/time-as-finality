# T116: Open Markov Record-Entropy Comparison

## Route

Thermodynamic arrow of time.

## Question

After T110 blocks strict scalar finality monotones in finite closed reversible
systems, can an explicitly open stochastic record process give H7 an arrow
that is not merely standard path irreversibility, history export, or fresh
blank capacity?

## Motivation

H7 should not survive by moving from a closed reversible toy model to an open
Markov toy model unless the open model adds something not already captured by
ordinary stochastic thermodynamics or resource accounting. The useful test is
therefore hostile: accept an H7 arrow only if strict accounted finality appears
without positive path log-ratio, exported history, fresh capacity, hidden
postselection, or omitted reverse dynamics.

## Success Criteria

- Include a detailed-balance record-shuffle control with zero path
  irreversibility.
- Include a biased local cycle showing that entropy-producing current alone is
  not a scalar finality monotone.
- Include an open export recorder where local records cycle but accounted
  exported records are nondecreasing.
- Include a reversible append-only control where monotonicity uses fresh blank
  capacity rather than entropy export.
- State a falsification condition for an independent open-system H7 arrow.

## Failure Criteria

- Count exported history without naming it.
- Treat fresh blank capacity as free.
- Claim entropy production alone is finality.
- Ignore reverse probabilities while calling the process stochastic.
- Upgrade H7 if the monotone is fully explained by standard path
  irreversibility, exported history, or capacity consumption.

## Claim Impact

If T116 holds, H7 remains only a conditional constructor or open-system
resource-accounting claim. It does not yet give an independent thermodynamic
arrow.

## Reproduction

```bash
python -m unittest tests.test_open_markov_record_entropy -v
python -m models.run_t116
```
