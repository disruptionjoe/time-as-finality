# T503: Knuth-Bendix-Style Finality Admission Gate

## Target Claims

- [Valid Coarse-Graining as Finality Admissibility](../open-problems/valid-coarse-graining-as-finality-admissibility.md)
- [T61: MMO Reconciliation Finality](T61-mmo-reconciliation-finality.md)
- [T467: Valid Coarse-Graining Admissibility Gate](T467-valid-coarse-graining-admissibility-gate.md)
- [T489: Post-T478 Valid Coarse-Graining Closure Router](T489-post-t478-valid-coarse-graining-closure-router.md)

## Question

Does Knuth-Bendix-style rewrite completion supply a finite, domain-native
branch/cost check that is not merely a rename of the existing D1-style
bounded-observer certification filter?

This is a review-only intake gate. It does not import Wolfram-model physics,
prove a Knuth-Bendix theorem inside TaF, identify TaF with Observer Theory, or
move claim status.

## Setup

T503 reads the repo-local T61 reconciliation fixture and T467/T489 admission
logic, then evaluates finite abstract rewrite systems. For each case it records:

- rewrite termination;
- confluence to a single normal form;
- completion-rule cost against a finite observer budget;
- D1 bounded-observer certification status on the same candidate relation;
- the relationship between the two verdicts.

The expected relationship classes are:

- `coincident_admission`: completion and D1 both admit the case.
- `completion_refines_d1`: D1 admits the candidate, but rewrite completion
  rejects it because it is nonconfluent, cyclic, or over budget.
- `completion_not_sufficient`: rewrite completion admits the case, but D1
  rejects it because the record is inaccessible or too fine.

## Positive Controls

- `t61_positive_prediction_completion`: the T61 confirmed prediction and
  authority commit normalize to one reconciled history.
- `t61_conflict_rollback_completion`: the T61 stale-conflict case normalizes
  only after explicit rollback/conflict completion.

## Hostile Controls

- `accessible_two_normal_forms_no_join`: accessible certified branches
  terminate but have two normal forms.
- `accessible_cycle_no_final_normal_form`: accessible certified branch rewrite
  cycles without a final normal form.
- `accessible_over_budget_completion`: branches are joinable only with more
  completion rules than the declared observer budget permits.
- `hidden_authority_completion_shortcut`: rewrite completion converges through
  a hidden authority rule outside the observer budget.
- `microstate_identity_completion_shortcut`: a single microstate is trivially
  normal but full-state identity is not an admissible coarse-graining.

## Success Criteria

T503 succeeds if it:

- preserves the T61 positive and rollback fixtures as admitted by both D1 and
  completion;
- shows at least one D1-admitted case rejected by completion for branch/cost
  reasons;
- shows at least one completion-admitted case rejected by D1 for access or
  non-coarse-graining reasons;
- keeps the T489 route review-only;
- leaves claim status, public posture, North Star, roadmap, README, hard
  policy, protected license, external publication, and cross-repo truth
  untouched.

## Failure Criteria

T503 fails if it:

- treats confluence/termination as sufficient without D1-certified record
  access;
- treats D1 admission as sufficient despite nonconfluent, cyclic, or
  over-budget rewrite behavior;
- converts the finite gate into an Observer Theory/TaF equivalence theorem;
- imports Wolfram-model physics or claim movement;
- publishes externally or moves cross-repo truth.

## Known Physics Constraints

This is not a physics result. Gorard/Wolfram sources remain source-status
context for this gate; the executable verdict is based on repo-local finite
fixtures.

## Reproduction

```bash
python -m pytest tests/test_knuth_bendix_finality_admission_gate.py -q
python -m models.knuth_bendix_finality_admission_gate --write-results
```

Artifacts:

- `models/knuth_bendix_finality_admission_gate.py`
- `tests/test_knuth_bendix_finality_admission_gate.py`
- `results/T503-knuth-bendix-finality-admission-gate-v0.1.json`
- `results/T503-knuth-bendix-finality-admission-gate-v0.1-results.md`

## Contribution Needed

Future packets must verify primary sources before load-bearing use, declare a
finite abstract rewrite system, report termination/confluence/completion-cost,
compare against D1 on the same candidate relations, include both sides of the
hostile controls, and supply a domain-native cost/certifiability theorem before
claiming more than review-target status.
