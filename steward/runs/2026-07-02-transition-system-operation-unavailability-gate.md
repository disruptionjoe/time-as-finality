# 2026-07-02 Transition-System Operation-Unavailability Gate Progress Run

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
- T403/T405 same-domain finality-lock artifacts
- T145/T179 fixed-accounting future-operation absorber context

## Worktree State

Before edits, the worktree had pre-existing local work outside this run:

```text
M TESTS.md
?? models/basis_free_capability_boundary.py
?? models/resource_theory_absorber_audit.py
?? results/T404-basis-free-capability-boundary-v0.1-results.md
?? results/T404-basis-free-capability-boundary-v0.1.json
?? results/T404-resource-theory-absorber-audit-v0.1-results.md
?? results/T404-resource-theory-absorber-audit-v0.1.json
?? tests/T404-basis-free-capability-boundary.md
?? tests/T404-resource-theory-absorber-audit.md
?? tests/test_basis_free_capability_boundary.py
?? tests/test_resource_theory_absorber_audit.py
```

Those files are treated as a separate T404/basis-free/resource-theory lane.
This run avoids the T404 slot, does not modify those files, and stages only
the T406 changes at closeout.

## Objective

Advance the post-T405 Direction-A lane by testing the next candidate word:
operation unavailability.

The target is a finite absorber gate:

```text
match causal-domain payload, final verdict payload, revision budget,
operation menu, resource accounting, provenance, control, boundary, and
non-dynamic substrate support; vary only the declared transition relation
that says whether revise_verdict is reachable.
```

If the revision capability splits only after the transition relation changes,
the split is absorbed by transition-system completion. If the transition
relation is also matched, no revision-capability split should remain in the
finite fixture.

## Planned Verification

- `python -m pytest tests/test_transition_system_operation_unavailability_gate.py -q`
- focused regression with T405/T403/T145 tests
- `python -m models.transition_system_operation_unavailability_gate`
- generated JSON parse
- `git diff --check`

## Receipt

Completed.

## Artifacts Created

- `tests/T406-transition-system-operation-unavailability-gate.md`
- `models/transition_system_operation_unavailability_gate.py`
- `tests/test_transition_system_operation_unavailability_gate.py`
- `results/T406-transition-system-operation-unavailability-gate-v0.1.json`
- `results/T406-transition-system-operation-unavailability-gate-v0.1-results.md`

## Surfaces Updated

- `TESTS.md`
- `ROADMAP.md`
- `open-problems/region-indexed-capability-discriminator.md`
- `steward/memory-log.md`

## Result

T406 supplies a conservative operation-unavailability absorber gate:

- the main pair imports the T405/T403 causal payload and final verdict payload;
- revision budget, operation menu, resource accounting, provenance,
  reversible-control class, observer boundary, and non-dynamic substrate
  support are matched;
- the only main-pair difference is the finite operation-labeled transition
  relation for `revise_verdict`;
- the only capability split is `can_revise_final_verdict`;
- transition-system completion restores factorization;
- every finite pair with the same transition-system completion has the same
  capability object in this fixture;
- operation-menu, resource, provenance, control, boundary, hidden-label, and
  latch-topology shortcut controls classify separately.

The result is an absorber/precheck, not a claim upgrade. No North Star, canon,
claim status, public posture, or cross-repo truth changed. No external action
was performed beyond the authorized GitHub versioning step planned for
closeout.

## Verification

Passed:

```text
python -m pytest tests/test_transition_system_operation_unavailability_gate.py tests/test_physical_latch_finality_lock_screen.py tests/test_same_domain_finality_lock_screen.py tests/test_physical_record_deletion_fixed_accounting.py -q
35 passed

python -m models.transition_system_operation_unavailability_gate | python -m json.tool
model-json-ok

python -m json.tool results\T406-transition-system-operation-unavailability-gate-v0.1.json
saved-json-ok

git diff --check
clean
```

## Next Safe Lane

Do not treat operation-unavailability language as progress unless the
transition-system completion relevant to the task is already matched. The next
positive route needs a domain-native law or measured substrate dynamics that
forces the transition relation rather than restating it.
