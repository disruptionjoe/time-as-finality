# 2026-07-02 Causal-Domain Boundary Forcing Screen Progress Run

## Governance Loaded

- `AGENTS.md`
- `steward/README.md`
- `Vision - North Star.md`
- `Method - Research Program Guidelines.md`
- `Lead Research Line - Time as Finality.md`
- `CONTRIBUTING.md`
- `ROADMAP.md`
- `HYPOTHESES.md`
- `CLAIM-LEDGER.md`
- `COMPLEXITY-LEDGER.md`
- `TESTS.md`
- `open-problems/region-indexed-capability-discriminator.md`
- T151/T153 causal-access artifacts
- T399/T400/T401 boundary-crossing artifacts

## Worktree State

Before edits, the only visible untracked file was `results/_rmtest.json`.
It was treated as pre-existing scratch / non-artifact material and left
untouched.

No additional worktrees are registered for this repository.

## Objective

Advance the post-T401 Direction-A lane by testing a physical-substrate version
of the forced-boundary task:

```text
finite 1+1 causal-domain record propagation where a common-future verdict
event is inside the domain of both boundary inputs but the bounded region R
alone cannot determine it.
```

The target is a conservative executable screen where:

- all `R`-supported statistics and finite `R` intervention/readout statistics
  agree between the pair;
- boundary-local statistics agree;
- the declared physical/finality task is predeclared as the value at a
  common-future verdict event;
- boundary crossing is forced by causal past / domain-of-dependence structure,
  not merely by optional enlarged-state access;
- the result is checked against T401's ordinary joint-record absorber and the
  stronger T151/T153 causal-access/domain-of-dependence absorber;
- no claim-ledger movement, public posture change, North Star change, or
  cross-repo truth change is made.

## Planned Verification

- `python -m pytest tests/test_causal_domain_boundary_forcing_screen.py -q`
- focused regression with T153/T401/T400 tests
- `python -m models.causal_domain_boundary_forcing_screen`
- generated JSON parse
- `git diff --check`

## Receipt

Completed.

## Artifacts Created

- `tests/T402-causal-domain-boundary-forcing-screen.md`
- `models/causal_domain_boundary_forcing_screen.py`
- `tests/test_causal_domain_boundary_forcing_screen.py`
- `results/T402-causal-domain-boundary-forcing-screen-v0.1.json`
- `results/T402-causal-domain-boundary-forcing-screen-v0.1-results.md`

## Surfaces Updated

- `TESTS.md`
- `ROADMAP.md`
- `open-problems/region-indexed-capability-discriminator.md`
- `steward/memory-log.md`

## Result

T402 supplies the physical-substrate screen requested after T401:

- `R` and `B` inputs are spacelike in a finite 1+1 causal-domain fixture;
- the common-future verdict event is in the joint `R:B` domain of dependence;
- the `R`-only and `B`-only domains do not determine the verdict;
- aligned and anti-aligned source distributions have identical `R` marginals,
  boundary-local marginals, and declared finite `R` intervention/readout
  statistics;
- the common-future same/different verdict separates with binary success `1.0`;
- optional joint labels, hidden datum in `R`, closure-key shortcuts, and
  class-marker shortcuts are blocked.

The result is conservative. The physical task-shape burden clears, but the
separator is absorbed by ordinary causal-domain completion plus joint input
access. No North Star, canon, claim status, public posture, or cross-repo truth
changed. No external action was performed beyond the authorized GitHub
versioning step planned for closeout.

## Verification

Passed:

```text
python -m pytest tests/test_causal_domain_boundary_forcing_screen.py -q
12 passed in 0.12s

python -m pytest tests/test_causal_domain_boundary_forcing_screen.py tests/test_lorentzian_causal_diamond_screen.py tests/test_finality_boundary_reconciliation_screen.py tests/test_boundary_forced_task_gate.py -q
40 passed in 0.30s

python -m models.causal_domain_boundary_forcing_screen | python -m json.tool
model-json-ok

python -m json.tool results\T402-causal-domain-boundary-forcing-screen-v0.1.json
saved-json-ok

git diff --check
clean
```

The first saved JSON attempt used PowerShell redirection and produced UTF-16;
the generated result artifact was rewritten as UTF-8 and then parsed cleanly.

## Next Safe Lane

Do not repeat causal-domain completion as if it were a surviving discriminator.
The next stronger Direction-A target needs a same-causal-domain-data capability
split not expressible as causal reachability, domain of dependence, or ordinary
joint input completion.
