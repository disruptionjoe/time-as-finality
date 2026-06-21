# T154 Results: T54/T58-to-T126 Bridge

## Aggregate Checks

- Canonical completions audited: True
- T58 gate required and passed: True
- Actual canonical colimits blocked before manifold claims: True
- No named dimension estimator applied: True

## Bridge Table

| Source completion | T54 | T58 gate | T126 | Causet candidate | Manifold filter | Events | Strict pairs | Ordering fraction | Verdict |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- |
| `T51_phantom_repair` | `canonical` | `True` | `insufficient_scale` | `True` | `False` | 3 | 2 | 2/3 (0.667) | `causet_candidate_only` |
| `T52_symmetric_reconstruction` | `canonical` | `True` | `insufficient_scale` | `True` | `False` | 4 | 3 | 1/2 (0.500) | `causet_candidate_only` |
| `T53_ambiguous_identity` | `underdetermined` | `False` | `not_descent_datum` | `False` | `False` | 0 | - | - | `blocked_before_spacetime_claim` |

## T51_phantom_repair

- T126 classification: `insufficient_scale`
- Dimension diagnostic: `myrheim_meyer_ordering_fraction_not_applied_below_minimum_scale`
- Reason: The relation is a finite causal-set candidate, but the witness is too small for the selected manifoldlikeness diagnostics.

## T52_symmetric_reconstruction

- T126 classification: `insufficient_scale`
- Dimension diagnostic: `myrheim_meyer_ordering_fraction_not_applied_below_minimum_scale`
- Reason: The relation is a finite causal-set candidate, but the witness is too small for the selected manifoldlikeness diagnostics.

## T53_ambiguous_identity

- T126 classification: `not_descent_datum`
- Dimension diagnostic: `not_reached`
- Reason: The T54-style descent gate failed or is missing, so no causal-set embeddability claim is meaningful.

## Strongest Claim

The actual T54 canonical T51/T52 quotient-union completions can be adapted into finite causal-set candidates only after the T58 phantom-gap gate passes, but both are too small for T126 manifoldlikeness or named dimension-estimator use.

## What This Improved

T154 removes a placeholder in the S1/T126 chain: T126 now has a direct executable bridge from T54 completions and T58 gap checks, rather than only synthetic controls and prose dependencies.

## What This Weakened

T51 and T52 are not current spacetime-reconstruction witnesses. They are three- and four-event finite causal-set candidates whose positive content stops at the causal-set gate.

## Falsification Condition

T154 fails if the adapter changes the T54 event-finality order, if T58 exact-match extension is not required before phantom-gap resolution, or if a sub-scale finite colimit is legitimately promoted to manifoldlike evidence without a declared dimension, sprinkling, locality, or continuum-limit diagnostic.

## S1 Update

S1 remains open_formal_target. Actual T54/T58 colimits now enter the T126 screen, but the current canonical examples are only small causal-set candidates and are blocked before manifold claims.

## Claim Ledger Update

Add T154 to S1: T54 canonical T51/T52 completions pass through a T58 well-formed phantom-gap gate into T126, where both are classified insufficient_scale. This makes the finite-to-spacetime bridge more executable while weakening any T51/T52 spacetime read.

## Open Blocker

No actual finality colimit in the current T54/T58 family is large enough to apply a named causal-set dimension estimator, sprinkling diagnostic, locality test, faithful embedding theorem, or continuum-limit argument.

## Suggested Next

Construct a larger T54-style canonical colimit with at least the T126 minimum scale, then compare it to a declared Myrheim-Meyer ordering-fraction target or a named sprinkling/locality diagnostic.
