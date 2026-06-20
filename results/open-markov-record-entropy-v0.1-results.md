# T116 Results: Open Markov Record-Entropy Comparison

## Strongest claim

In the tested finite open Markov record fixtures, strict accounted finality appears only with standard path irreversibility plus history export, or with fresh blank capacity. Detailed-balance controls do not yield a strict record arrow, and a biased entropy-producing local cycle is not by itself a scalar finality monotone.

## Scenario table

| Scenario | Accounted score | Irreversibility nats | Exported | Fresh capacity used | Classification |
| --- | --- | ---: | ---: | ---: | --- |
| detailed_balance_shuffle_control | `[0, 1, 0, 1, 0]` | 0.000000 | 0 | 0 | `no_strict_h7_arrow` |
| nonequilibrium_cycle_control | `[0, 1, 2, 0]` | 4.158883 | 0 | 0 | `no_strict_h7_arrow` |
| open_export_recorder | `[0, 1, 2, 2, 3, 4, 4]` | 13.183347 | 4 | 0 | `absorbed_by_entropy_export` |
| reversible_append_only_control | `[0, 1, 2, 3]` | 0.000000 | 0 | 3 | `absorbed_by_fresh_capacity` |

## detailed_balance_shuffle_control

- Local score sequence: `[0, 1, 0, 1, 0]`
- Accounted score sequence: `[0, 1, 0, 1, 0]`
- Local nondecreasing: `False`
- Accounted nondecreasing: `False`
- Strict accounted increases: `2`
- Total path irreversibility: `0.000000` nats
- Exported records added: `0`
- Fresh capacity consumed: `0`
- Candidate independent H7 arrow: `False`

No strict accounted finality arrow is present in this control.

## nonequilibrium_cycle_control

- Local score sequence: `[0, 1, 2, 0]`
- Accounted score sequence: `[0, 1, 2, 0]`
- Local nondecreasing: `False`
- Accounted nondecreasing: `False`
- Strict accounted increases: `2`
- Total path irreversibility: `4.158883` nats
- Exported records added: `0`
- Fresh capacity consumed: `0`
- Candidate independent H7 arrow: `False`

No strict accounted finality arrow is present in this control.

## open_export_recorder

- Local score sequence: `[0, 1, 2, 0, 1, 2, 0]`
- Accounted score sequence: `[0, 1, 2, 2, 3, 4, 4]`
- Local nondecreasing: `False`
- Accounted nondecreasing: `True`
- Strict accounted increases: `4`
- Total path irreversibility: `13.183347` nats
- Exported records added: `4`
- Fresh capacity consumed: `0`
- Candidate independent H7 arrow: `False`

The strict accounted arrow is explained by the open export channel and positive path irreversibility.

## reversible_append_only_control

- Local score sequence: `[0, 1, 2, 3]`
- Accounted score sequence: `[0, 1, 2, 3]`
- Local nondecreasing: `True`
- Accounted nondecreasing: `True`
- Strict accounted increases: `3`
- Total path irreversibility: `0.000000` nats
- Exported records added: `0`
- Fresh capacity consumed: `3`
- Candidate independent H7 arrow: `False`

The strict accounted arrow is paid for by consuming fresh blank record capacity.

## What this improved

T116 answers T110's open-system next step by comparing H7 record arrows directly with stochastic path irreversibility, exported history, and append-only blank capacity in one finite audit.

## What this weakened

H7 is weakened as an independent thermodynamic-arrow proposal. The open recorder's monotone accounted finality is fully explained by the declared export channel and positive path log-ratio; the zero-log-ratio monotone uses fresh capacity.

## Falsification condition

T116 is falsified by a finite stochastic record model with a strict accounted-D1 monotone, zero path irreversibility, no distributional free-energy drawdown, no exported history, no fresh capacity consumption, no postselection, and reverse dynamics included rather than excluded.

## H7 update

Add T116 to H7: the explicit open Markov witness gives no independent open Markov arrow separating finality direction from entropy/export/fresh-capacity accounting. H7 remains a constructor/resource-accounting claim unless a zero-resource stochastic record arrow is produced.

## Claim ledger update

H7 remains partially supported only as a conditional constructor or open-system resource-accounting claim. T116 finds no independent open Markov arrow: detailed-balance record shuffle has no strict finality direction, biased cyclic current is entropy-producing but not scalar-finality monotone, exported history gives monotone accounted records only with positive path irreversibility, and append-only monotonicity consumes fresh blank capacity.

## Open blocker

The repo still lacks a physically grounded H7 model whose record arrow is not absorbed by standard stochastic thermodynamics, history export, free-energy drawdown, or capacity accounting.

## Recommended next

Demote H7 in paper-facing prose to a constructor/resource accounting lemma, or search for a zero-resource stochastic record-arrow counterexample that clears the T116 gate.
