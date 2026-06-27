# T300 Results: Selected T252 Singleton Probabilities

## Aggregate Checks

| Metric | Value |
| --- | --- |
| `uniform` | `{'fraction': '1/362880', 'float': 2.7557319223985893e-06}` |
| `lowcover` | `{'fraction': '1/185', 'float': 0.005405405405405406}` |
| `parentcap` | `{'fraction': '1/66', 'float': 0.015151515151515152}` |
| `deletion_soft` | `{'fraction': '32/790437', 'float': 4.048393483604639e-05}` |
| `shape_soft` | `{'fraction': '128/987721', 'float': 0.00012959125097066883}` |

- Verdict: `selected_singleton_remains_measure_sensitive`

## Strongest Claim

The selected T252 permutation remains a singleton inside every non-tautological measure; even parent-cap conditioning gives it probability only 1/66.

## What This Improved

T300 keeps the analysis from mistaking a tail measure for a selected-witness measure.

## What This Weakened Or Falsified

It weakens over-reading of the specific T252 permutation.

## Falsification Condition

T300 fails if selected probabilities are computed outside the same n=9 denominator.

## S1 Update

S1 is unchanged.

## Claim Ledger Update

Do not update the claim ledger from T300 alone.

## Open Blocker

No rule selects the specific T252 witness rather than the tail.

## Suggested Next

Audit tail symmetry and shape structure.

## Not Claimed

These finite selection audits do not define a physical measure, estimate dimension, prove faithful embedding, validate random sprinkling, derive metric structure, establish a continuum limit, or settle S1.
