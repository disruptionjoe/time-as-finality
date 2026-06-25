# T220 Results: LossKernel Witness-Obligation Factorization

## Aggregate checks

- Canonical factorization holds (obligation = psi . nu): True
- Neighbor reconstruction matches obligation: True
- Same-neighbor-data separation impossible in canonical regime: True
- Strict same-neighbor-data separation found: False
- Hidden-source escape separates (non-factoring): True
- Hidden-source escape factors through neighbor: False
- Hidden-source escape is prior-art separation: False
- Verdict: narrowed

## Fiber-constancy certificate (fibers of nu)

| Fiber | Cases | Obligation constant | Verdict constant | Verdict |
| --- | --- | --- | --- | --- |
| 0 | mixed_a, mixed_b_relabelled | True | True | candidate_witness_obligation |
| 1 | uniform_false_constraint | True | True | demote_non_attribution_relevant_loss |
| 2 | uniform_true_absorbed | True | True | demote_non_attribution_relevant_loss |
| 3 | resolved_endpoint | True | True | inadmissible_no_target_obstruction |

## Pair probes

| Pair | Same neighbor data | Obligation diverges | Factors through nu | Classification |
| --- | --- | --- | --- | --- |
| `canonical_0` | True | False | True | `collapse` |
| `canonical_1` | False | True | True | `different_neighbor_data` |
| `canonical_2` | False | True | True | `different_neighbor_data` |
| `canonical_3` | False | True | True | `different_neighbor_data` |
| `canonical_4` | False | True | True | `different_neighbor_data` |
| `canonical_5` | False | True | True | `different_neighbor_data` |
| `canonical_6` | False | True | True | `different_neighbor_data` |
| `canonical_7` | False | False | True | `different_neighbor_data` |
| `canonical_8` | False | False | True | `different_neighbor_data` |
| `canonical_9` | False | False | True | `different_neighbor_data` |
| `hidden_source_escape` | True | True | False | `non_factoring_escape` |

## Strongest claim

The canonical LossKernel witness obligation factors through the neighbor-visible data map: obligation = psi . nu. Because a map that factors through nu is constant on each fiber of nu, and the fibers of nu are exactly the same-neighbor-data classes, two cases with identical neighbor-visible data necessarily receive the same obligation and the same attribution verdict. The T127 negative is therefore not an accident of the fixture family; it is forced. The only way to separate same-neighbor-data cases is to read a source datum no neighbor package exposes, which is a non-factoring obligation and not a prior-art separation: admitting that datum as legitimate audit data enlarges the neighbor package and restores absorption one level up. LossKernel is hereby certified as a canonical witness-obligation normal form that collapses into neighbor data, not a prior-art-separated obstruction object.

## What this improved

T220 upgrades the T127 search-negative to a structural certificate. The repo no longer has to leave same-neighbor-data separation open as a thing that might appear with more cleverness in the current derivation; the factorization rules it out by construction and names the single remaining loophole.

## What this weakened

This closes the default TF1 rescue path for the canonical derivation. A prior-art-separated obstruction theorem cannot come from any obligation that is a function of neighbor-visible data, which the canonical LossKernel obligation is.

## Falsification condition

T220 is overturned in TF1's favor only by exhibiting an obligation map that (a) separates two cases sharing the full neighbor-visible signature nu, and (b) is itself a function of nu (factors through it). The factorization theorem shows these two requirements are contradictory, so the falsifier must instead argue that some source field used by the obligation is legitimately OUTSIDE every mature neighbor package -- a claim that has repeatedly failed (T108, T127) because mature provenance/effect/abstraction systems absorb any declared source field once it is named.

## TF1 update

TF1 remains open_formal_target, but its LossKernel sub-target is downgraded from 'prior-art-separated obstruction theorem' to 'certified witness-obligation normal form (collapse-into-neighbor)'. The same-neighbor-data quotient route is closed structurally, not just empirically.

## Claim ledger update

Add T220 to TF1: the canonical witness obligation factors through the neighbor-visible data map (obligation = psi . nu), so same-neighbor-data separation is impossible in the canonical regime by fiber-constancy, certifying LossKernel as a collapse-into-neighbor witness-obligation normal form. The lone escape (non-factoring obligation reading a hidden source datum) is not a prior-art separation because admitting the datum enlarges the neighbor package. TF1 stays open_formal_target with the LossKernel sub-target downgraded to the normal-form reading.

## Open blocker

The certified normal form is weaker than a publishable separation. Its remaining value is audit/integration: a canonical, neighbor-reconstructible checklist of source-derived obligations. No new-mathematical-object language is earned.

## Recommended next

Retire same-neighbor-data separation as a live TF1 rescue. Either develop the certified normal form as an integration/audit vocabulary (cleaner admissibility checklist, neighbor-reconstructible), or redirect novelty effort to live internal movement (T125/T126 geometry gates) per the ROADMAP attention queue.
