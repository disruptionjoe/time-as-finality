# T375 Results: Sixty-Four Task Measure Stress Synthesis

## Aggregate Checks

| Metric | Value |
| --- | --- |
| `completed_task_count` | `64` |
| `best_simple_hard_tail_probability` | `{'fraction': '5/8', 'float': 0.625}` |
| `best_soft_tail_probability` | `{'fraction': '1342177280/1705336003', 'float': 0.7870456482704071}` |
| `round_verdict` | `finite_candidate_measures_concentrate_tail_but_remain_underived` |

- Verdict: `finite_candidate_measures_concentrate_tail_but_remain_underived`

## Strongest Claim

T312-T375 complete a 64-task finite measure stress round: candidate measures can concentrate the T252-style tail, but the successful weights remain underived.

## What This Improved

The round upgrades the blocker from 'find any concentrating finite score' to 'derive the candidate action from finality-domain dynamics.'

## What This Weakened Or Falsified

It weakens both pessimism about finite concentration and optimism about S1; concentration exists, but derivation is missing.

## Falsification Condition

T375 fails if the candidate scores are later shown to use the tail label or if a physical derivation is supplied and ignored.

## S1 Update

S1 remains requires_added_assumption for the finite ordinal route.

## Claim Ledger Update

Do not update the claim ledger from T375 alone.

## Open Blocker

No finality-domain dynamics derive the successful finite weighting rule yet.

## Suggested Next

Derive or reject the candidate action from finality-domain data rather than from post-hoc tail labels.

## Not Claimed

These finite measure stress tests do not define a physical measure, estimate dimension, prove faithful embedding, validate random sprinkling, derive metric structure, establish a continuum limit, or settle S1.
