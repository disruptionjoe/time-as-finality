# 2026-07-02 Physical-Latch Finality-Lock Screen Progress Run

## Governance Loaded

- `AGENTS.md`
- `steward/README.md`
- `Vision - North Star.md`
- `Method - Research Program Guidelines.md`
- `Lead Research Line - Time as Finality.md`
- `CONTRIBUTING.md`
- `ROADMAP.md`
- `TESTS.md`
- `COMPLEXITY-LEDGER.md`
- `open-problems/region-indexed-capability-discriminator.md`
- T400/T401/T402/T403 boundary/finality artifacts
- T145/T179 fixed-accounting absorber context

## Worktree State

Before edits, the worktree had one unexpected untracked file:

```text
models/resource_theory_absorber_audit.py
```

That file is a substantial T404 resource-theory absorber draft. It is treated
as pre-existing work outside this run. This run avoids the T404 slot, does not
modify that file, and does not include it in closeout.

At closeout, additional untracked T404 and basis-free capability draft
artifacts were visible in the worktree. They are also treated as unrelated
pre-existing or concurrent work and are left untouched.

No additional worktrees are registered for this repository.

## Objective

Advance the post-T403 Direction-A lane by replacing the stipulated
provisional/sealed flag with a finite physically typed latch substrate:

```text
match causal-domain data, joint payload, verdict payload, revision budget,
operation menu, resource accounting, provenance, control, and observer
boundary; vary only the typed latch topology that determines whether the final
record can still be rewritten.
```

The target is conservative:

- the lock state must be derived from substrate fields, not an accepted label;
- T403 causal-domain and joint-payload controls remain matched;
- T145-style fixed-accounting resource/provenance/control/boundary absorbers
  are granted;
- the capability split may survive that fixed-accounting projection;
- explicit latch-substrate completion should be checked as the next absorber;
- no claim-ledger movement, public posture change, North Star change, or
  cross-repo truth change is made.

## Planned Verification

- `python -m pytest tests/test_physical_latch_finality_lock_screen.py -q`
- focused regression with T403/T402/T145 tests
- `python -m models.physical_latch_finality_lock_screen`
- generated JSON parse
- `git diff --check`

## Receipt

Completed.

## Artifacts Created

- `tests/T405-physical-latch-finality-lock-screen.md`
- `models/physical_latch_finality_lock_screen.py`
- `tests/test_physical_latch_finality_lock_screen.py`
- `results/T405-physical-latch-finality-lock-screen-v0.1.json`
- `results/T405-physical-latch-finality-lock-screen-v0.1-results.md`

## Surfaces Updated

- `TESTS.md`
- `ROADMAP.md`
- `open-problems/region-indexed-capability-discriminator.md`
- `steward/memory-log.md`

## Result

T405 supplies the next post-T403 physical-substrate screen:

- the main pair imports the T403/T402 causal-domain signature;
- joint payload, verdict payload, revision budget, operation menu, resource
  accounting, provenance, reversible-control class, observer boundary, and
  latch support fields except topology are matched;
- the lock state is derived from finite latch topology rather than accepted as
  a stipulated finality label;
- only `can_revise_final_verdict` splits between the rewritable latch and the
  fused latch;
- the split survives the fixed-accounting projection;
- explicit latch-substrate completion restores factorization;
- resource, provenance, control, boundary, hidden-label, and stipulated-label
  controls classify correctly.

The result is conservative. It is not causal reachability, ordinary joint
input completion, T403-style stipulated finality-state completion, resource
accounting, provenance, control, boundary, or hidden-marker separation. It is
absorbed by explicit latch-substrate completion. No North Star, canon, claim
status, public posture, or cross-repo truth changed. No external action was
performed beyond the authorized GitHub versioning step planned for closeout.

## Verification

Passed:

```text
python -m pytest tests/test_physical_latch_finality_lock_screen.py tests/test_same_domain_finality_lock_screen.py tests/test_causal_domain_boundary_forcing_screen.py tests/test_physical_record_deletion_fixed_accounting.py -q
38 passed

python -m models.physical_latch_finality_lock_screen | python -m json.tool
model-json-ok

python -m json.tool results\T405-physical-latch-finality-lock-screen-v0.1.json
saved-json-ok

git diff --check
clean
```

## Next Safe Lane

Do not repeat explicit latch-topology separators. The next stronger
Direction-A target needs a substrate-native irreversibility or operation-
unavailability result that does not factor through explicit latch topology,
resource state, provenance state, control handle, or observer boundary.
