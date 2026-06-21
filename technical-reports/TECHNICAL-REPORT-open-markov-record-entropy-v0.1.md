# Technical Report: Open Markov Record-Entropy Comparison v0.1

## Claim Under Test

H7 says finality structure can induce an observer-relative temporal direction
when admissible transformations are monotone in D1 finality. T110 showed that
a strict scalar finality monotone cannot live inside a finite closed
reversible system: any nondecreasing scalar score on a finite permutation
orbit is constant.

T116 tests the next loophole. If the system is explicitly open and stochastic,
can record-finality direction add anything beyond standard path
irreversibility, exported history, or fresh blank capacity?

## Result

The finite audit finds no independent open Markov arrow.

The detailed-balance record-shuffle control has zero path irreversibility and
no strict accounted finality direction:

```text
0 -> 1 -> 0 -> 1 -> 0
```

The biased local cycle has positive path irreversibility, but it is not a
scalar finality monotone:

```text
0 -> 1 -> 2 -> 0
```

The open export recorder gives nondecreasing accounted records only by naming
an export channel. Local records cycle:

```text
0 -> 1 -> 2 -> 0 -> 1 -> 2 -> 0
```

while local plus exported history is nondecreasing:

```text
0 -> 1 -> 2 -> 2 -> 3 -> 4 -> 4
```

This positive case is absorbed by the declared export channel and positive
path log-ratio.

The reversible append-only control is monotone with zero path log-ratio, but
only while consuming fresh blank capacity:

```text
fresh capacity: 3 -> 2 -> 1 -> 0
records:        0 -> 1 -> 2 -> 3
```

## Current Strongest Claim

In the tested finite open Markov record fixtures, strict accounted finality
appears only with standard path irreversibility plus history export, or with
fresh blank capacity. Detailed-balance controls do not yield a strict record
arrow, and a biased entropy-producing local cycle is not by itself a scalar
finality monotone.

## What This Improved

T116 answers T110's open-system next step by comparing H7 record arrows
directly with stochastic path irreversibility, exported history, and
append-only blank capacity in one finite audit.

## What This Weakened Or Falsified

This does not falsify T18. T18 remains a conditional constructor theorem.

T116 weakens H7 as an independent thermodynamic-arrow proposal. The open
recorder's monotone accounted finality is fully explained by the declared
export channel and positive path log-ratio. The zero-log-ratio monotone uses
fresh capacity. Neither is an independent finality-derived physical arrow.

## Falsification Condition

T116 is falsified by a finite stochastic record model with a strict
accounted-D1 monotone, zero path irreversibility, no distributional
free-energy drawdown, no exported history, no fresh capacity consumption, no
postselection, and reverse dynamics included rather than excluded.

## Claim Ledger Update

Add T116 to H7:

```text
H7 remains partially supported only as a conditional constructor or
open-system resource-accounting claim. T116 finds no independent open Markov
arrow: detailed-balance record shuffle has no strict finality direction,
biased cyclic current is entropy-producing but not scalar-finality monotone,
exported history gives monotone accounted records only with positive path
irreversibility, and append-only monotonicity consumes fresh blank capacity.
```

## Open Blocker

The repo still lacks a physically grounded H7 model whose record arrow is not
absorbed by standard stochastic thermodynamics, history export, free-energy
drawdown, or capacity accounting.

## Next Work

Demote H7 in paper-facing prose to a constructor/resource-accounting lemma, or
search for a zero-resource stochastic record-arrow counterexample that clears
the T116 gate.

## Reproduction

```bash
python -m unittest tests.test_open_markov_record_entropy -v
python -m models.run_t116
```
