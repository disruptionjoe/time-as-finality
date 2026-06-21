# Technical Report: Lorentzian Causal-Diamond Screen v0.1

## Claim Under Test

T151 weakened B1/S1/R1 by showing that direct classical record-access claims
factor through a declared causal-access graph. B1's next requested test was a
Lorentzian causal-diamond or domain-of-dependence version.

T153 asks whether any TaF-specific residue remains once the absorber is
ordinary 1+1 Minkowski causal structure rather than a graph proxy.

## Result

No independent TaF spacetime or black-hole mechanism is found in the tested
fixtures.

The tested access and reconstructability verdicts factor through:

- causal pasts;
- causal diamonds;
- spacelike separation plus common future reconciliation;
- changed observer access diamonds;
- and future domains of dependence.

## Audit Summary

| Fixture | Verdict | Meaning |
| --- | --- | --- |
| `remote_signal_causal_past` | `remote_signal_is_causal_record_access` | Remote observation through received light is causal record access, not direct participation. |
| `spacelike_pair_later_reconciliation` | `spacelike_no_invariant_order_later_reconciles` | No invariant order is assigned, but both records can reconcile in a common future. |
| `domain_of_dependence_interval` | `domain_of_dependence_absorbs_reconstructability` | The reconstructability split is ordinary domain-of-dependence membership. |
| `same_source_changed_access_diamond` | `verdict_split_absorbed_by_changed_access_diamond` | The split is caused by changing the observer access diamond. |
| `fixed_lorentzian_data_control` | `fixed_lorentzian_data_no_finality_split` | Matched causal data produce no verdict split in the control. |

## Current Strongest Claim

R1/S1/B1 can safely use finality language only when it is indexed by explicit
Lorentzian causal data. In this screen, every access or reconstructability
split is absorbed by standard causal structure. The strongest surviving R1
content is no-global-commit-order discipline: spacelike events lack invariant
causal order but can later be compared inside a common future.

## What This Improved

T153 makes the causal-access absorber harder to evade than T151. It replaces a
generic record-channel graph with explicit causal pasts, diamonds, spacelike
separation, and a finite domain-of-dependence interval.

## What This Weakened

S1 and B1 are weaker wherever they rely on ordinary access or reconstructability
splits. A verdict change caused by changed causal past, access diamond, or
domain-of-dependence data is not TaF evidence.

## Falsification Condition

T153 fails in TaF's favor only if a future fixture matches the Lorentzian
causal relation, observer world tube, access diamond, domain-of-dependence
inputs, record channels, and boundary data, yet still produces a task-natural
finality capability split not expressible as standard causal access or
reconstructability.

## Claim Ledger Update

Add T153 to R1/S1/B1:

```text
T153 gives R1/S1/B1 a Lorentzian causal-diamond screen. The tested verdicts
factor through causal pasts, common futures, changed access diamonds, and
domains of dependence. No same-Lorentzian-data TaF residue is found.
```

## Open Blocker

The screen is 1+1 Minkowski only. It has no curvature, global hyperbolicity
theorem, black-hole metric, QFT algebra, holographic encoding, semiclassical
gravity, or continuum finality-colimit construction.

## Recommended Next Move

Use T153 as the absorber gate for S1/B1. The next non-null move is either a
causal-set/manifoldlikeness implementation for T126 or a named
Schwarzschild/de Sitter causal-access witness with native absorber variables
declared up front.

## Reproduction

```bash
python -m unittest tests.test_lorentzian_causal_diamond_screen -v
python -m models.run_t153
```
