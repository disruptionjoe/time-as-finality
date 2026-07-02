# 2026-07-02 Same-Domain Finality-Lock Screen Progress Run

## Governance Loaded

- `AGENTS.md`
- `steward/README.md`
- `Vision - North Star.md`
- `Method - Research Program Guidelines.md`
- `Lead Research Line - Time as Finality.md`
- `CONTRIBUTING.md`
- `ROADMAP.md`
- `TESTS.md`
- `open-problems/region-indexed-capability-discriminator.md`
- T400/T401/T402 boundary-crossing artifacts
- H7, T119, and T145 future-operation / fixed-accounting context

## Worktree State

Before edits, the only visible untracked file was `results/_rmtest.json`.
It was treated as pre-existing scratch / non-artifact material and left
untouched.

No additional worktrees are registered for this repository.

## Objective

Advance the post-T402 Direction-A lane by testing the first finite
same-causal-domain-data split:

```text
match causal-domain data, joint payload, verdict payload, revision budget, and
operation menu; vary only provisional versus sealed record-finality state.
```

The target is a conservative executable screen where:

- causal reachability and domain-of-dependence data are matched;
- ordinary joint input completion is matched;
- operation-menu variation is isolated as a separate absorber control;
- hidden source-label shortcuts are blocked;
- the only main-pair capability split is future operation availability for
  revising the final verdict;
- explicit finality-state completion is checked as the absorber;
- no claim-ledger movement, public posture change, North Star change, or
  cross-repo truth change is made.

## Planned Verification

- `python -m pytest tests/test_same_domain_finality_lock_screen.py -q`
- focused regression with T402/T401/T400 tests
- `python -m models.same_domain_finality_lock_screen`
- generated JSON parse
- `git diff --check`

## Receipt

Completed.

## Artifacts Created

- `tests/T403-same-domain-finality-lock-screen.md`
- `models/same_domain_finality_lock_screen.py`
- `tests/test_same_domain_finality_lock_screen.py`
- `results/T403-same-domain-finality-lock-screen-v0.1.json`
- `results/T403-same-domain-finality-lock-screen-v0.1-results.md`

## Surfaces Updated

- `TESTS.md`
- `ROADMAP.md`
- `open-problems/region-indexed-capability-discriminator.md`
- `steward/memory-log.md`

## Result

T403 supplies the first same-domain screen requested after T402:

- the T402 causal-domain signature is imported unchanged;
- the main pair has identical causal-domain data, joint payload, verdict
  payload, revision budget, and operation menu;
- the only capability split is `can_revise_final_verdict`;
- the provisional record can revise the final verdict;
- the sealed record cannot revise the final verdict;
- a matched-finality control has no split;
- a joint-input control is absorbed by ordinary joint input completion;
- an operation-menu control is absorbed by operation-menu completion;
- hidden source-label separation is blocked.

The result is conservative. The split is not causal reachability,
domain-of-dependence, or ordinary joint input completion, but it is absorbed by
explicit finality-state completion. No North Star, canon, claim status, public
posture, or cross-repo truth changed. No external action was performed beyond
the authorized GitHub versioning step planned for closeout.

## Verification

Passed:

```text
python -m pytest tests/test_same_domain_finality_lock_screen.py -q
9 passed

python -m pytest tests/test_same_domain_finality_lock_screen.py tests/test_causal_domain_boundary_forcing_screen.py tests/test_finality_boundary_reconciliation_screen.py tests/test_boundary_forced_task_gate.py -q
40 passed

python -m models.same_domain_finality_lock_screen | python -m json.tool
model-json-ok

python -m json.tool results\T403-same-domain-finality-lock-screen-v0.1.json
saved-json-ok

git diff --check
clean
```

## Next Safe Lane

Do not count provisional/sealed finality state as a hidden causal-domain
discriminator. The next stronger Direction-A target needs a physically typed
finality-lock substrate whose state is not merely stipulated and whose
operation availability survives fixed-accounting resource, provenance,
control, and boundary absorbers.
