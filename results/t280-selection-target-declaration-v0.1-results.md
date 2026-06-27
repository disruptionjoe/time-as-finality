# T280 Results: Selection Target Declaration

## Aggregate Checks

| Metric | Value |
| --- | --- |
| `total_cases` | `362880` |
| `target_tail_count` | `10` |
| `selected_t252_in_tail` | `True` |
| `target_definition` | `T126+T156, parent interval<=3, cover hub<=2/7, and every deletion satisfies the same gate` |

- Verdict: `t252_style_tail_declared_for_selection_audit`

## Strongest Claim

The selection target is the exact 10-case T252-style deletion-stable tail from T272.

## What This Improved

T280 turns the next route into an explicit target rather than a vague request for a better measure.

## What This Weakened Or Falsified

It weakens any hidden-target analysis: the target is declared before comparing measures.

## Falsification Condition

T280 fails if the target differs from the T272 tail definition.

## S1 Update

S1 is unchanged; declaring a finite target is not a physical measure.

## Claim Ledger Update

Do not update the claim ledger from T280 alone.

## Open Blocker

No natural weighting rule has been supplied yet.

## Suggested Next

Audit hard gates and soft weights against the declared tail.

## Not Claimed

These finite selection audits do not define a physical measure, estimate dimension, prove faithful embedding, validate random sprinkling, derive metric structure, establish a continuum limit, or settle S1.
