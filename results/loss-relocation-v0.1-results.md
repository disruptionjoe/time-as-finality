# T107 Results: Loss Relocation

## Aggregate Checks

- Derived debt count: 4
- Stable constraint count: 1
- Absorbed freedom count: 1
- False conservation rejected: True
- Source-anchored derivation: True

## Scenario Verdicts

| Scenario | Lost axis | Displaced form | Relocation class |
| --- | --- | --- | --- |
| charge_neutrality_debt | charge | admissibility_condition | reconstruction_debt |
| spin_orientation_debt | spin | orientation_debt | reconstruction_debt |
| mass_persistence_debt | mass | persistence_debt | reconstruction_debt |
| phase_history_debt | phase | path_memory | reconstruction_debt |
| gauge_representative_absorbed | gauge | absorbed_freedom | absorbed_freedom |
| lorentz_access_constraint | lorentz_frame | frame_constraint | stable_constraint_surface |

## Six-Axis Bridge

| GU axis | Lost structure shape | TaF relocation target |
| --- | --- | --- |
| L1 substrate | lost internal coordinate | target constraint or debt |
| L2 observer | lost resolving access | admissibility obligation |
| L3 pairing | lost coupling channel | provenance requirement |
| L4 causal order | lost frame/order witness | access constraint |
| L5 emergence | lost microstate distinction | stable equivalence class |
| L6 coordination loop | lost feedback state | reconstruction debt |

## Strongest Claim

A finite projection can relocate lost structure into target-side debt or constraint when target judgments vary across source lifts. The relocation is derived from preimage fibers, not from free-text loss labels. But there is no conservation law: gauge-like lost structure can be absorbed when every lift gives the same invariant judgment.

## What This Improved

T107 turns the intuition 'track where lost structure goes' into a finite audit rule: inspect source lifts of a target judgment. Mixed lift verdicts derive reconstruction debt; uniform forbidden lifts derive a constraint surface; uniform invariant lifts absorb the loss.

## What This Weakened

This weakens any strong conservation slogan. Lost structure need not reappear as a new object. It reappears only when a target-side judgment remains lift-dependent or uniformly constrained after projection.

## Falsification Condition

Reject the relocation program as independent content if every derived debt is recoverable from ordinary target CSP data without source-fiber inspection, or if source-fiber inspection never separates debt, stable constraint, and absorbed freedom beyond standard provenance bookkeeping.

## TF1 Update

TF1 gains a sharper candidate semantics: a LossKernel witness obligation is derivable when a target judgment has mixed verdicts over the source preimage fiber. Non-empty loss is not enough, and some loss is absorbed.

## Claim Ledger Update

Add T107 to TF1: loss relocation is modeled by source-fiber lift analysis. Mixed lift verdicts produce reconstruction debt, uniform forbidden lifts produce a stable constraint surface, and uniform invariant lifts show absorbed freedom. This supports a source-anchored derivation path while rejecting conservation-style language.

## Open Blocker

The finite rule must be compared against why-not provenance, abstract interpretation, lenses, and CSP explanation machinery. T107 supplies semantics, not prior-art separation.

## Recommended Next

Re-express T99's typed witness obligations with this source-fiber rule and test whether the quotient separation still survives.
