# Obstruction Relocation Backlog Review

## Context Read

The current repo already has several nearby but non-identical mechanisms:

- T39: gluing obstruction is known CSP; PO1 adds typed projection and
  admissibility accounting.
- T63/T65: contextuality/global assignment failure is represented through
  holonomy and causal-boundary obstruction.
- T68/T72/T74: provenance failure moves from passive outcomes into protocol and
  raw-log obligations.
- T73: path-dependent admissibility is organized by composed LossKernel.
- T69: failure type is monotone only under declared finite hypotheses.
- Pati-Salam typed forgetting: the projection preserves some structure while
  losing load-bearing `T3R` information.

## Disposition Summary

| Version | New relative to repo? | Executable test? | Overclaim risk | Neutral math-paper connection | Disposition |
| --- | --- | --- | --- | --- | --- |
| 1: Obstruction Displacement | Yes as a cross-test taxonomy | Yes | Medium if phrased as universal | Strong as obstruction accounting | Add to persona backlog and open problem |
| 2: Reconstruction Debt | Yes if quantified | Yes | High if called information conservation | Strong if it gives uncertainty bounds | Add to persona backlog; require metric |
| 3: Obstruction-Degree Flow | Partly: T69 already covers H1/H0 narrow case | Eventually | High | Strong if generalized carefully | Block/defer until T69 hypotheses generalize |

## Goals Added

- P78: Obstruction Relocation Auditor.
- P79: Reconstruction Debt Quantifier.
- P80: Obstruction-Degree Flow Theorem Auditor, marked `blocked`.
- Open problem:
  `open-problems/obstruction-relocation-reconstruction-debt.md`.
- WC-31 in the explorations backlog.
- Additional LossKernel formalization questions about relocation and
  reconstruction debt.

## Conservation-Law Intuition

The user-facing intuition that should not be lost is:

```text
conservation law of obstruction
```

That phrase captures the pattern better than ordinary "bookkeeping": the
problem seems not to disappear, but to reappear as holonomy, inaccessible
witnesses, protocol assumptions, LossKernel data, or admissibility obligations.

The review keeps the phrase as motivation but rejects it as theorem language
until there is an invariant or balance law.

## Goals Rejected

Rejected as phrasing, not as intuition:

- "conservation of obstruction";
- "conservation of missing information";
- "projection cannot eliminate obstruction" as a universal claim.

These are too strong and invite false conservation-law readings.

## Goals Deferred

Version 3 is deferred. The only earned result is the narrow T69 finite
failure-type monotonicity statement. A broader H2/H1/H0 hierarchy needs explicit
coefficient systems, support semantics, cover hypotheses, and admissible
morphism classes.

## Candidate Main-Line Promotions

None yet.

Version 1 is the strongest candidate for the next executable LossKernel-family
test, but it should enter as a T102 audit target, not as a claim. Version 2 may
become paper-useful if it produces a non-circular ambiguity or uncertainty
measure. Version 3 is theorem-shaped but blocked.

## Recommended Next Concrete Test

Build T102: Obstruction Relocation Audit.

Minimum cases:

1. T39 CSP/PO1: known gluing obstruction plus typed admissibility accounting.
2. T63/T65: global assignment failure relocated to holonomy/causal-boundary
   language.
3. T68/T72/T74: outcome-level provenance obstruction relocated to protocol
   assumptions and raw-log obligations.
4. T73: path dependence relocated to composed LossKernel.
5. Pati-Salam typed forgetting: source representation structure lost under
   projection, with target ambiguity or failed table reconstruction.

The audit must include at least one negative control where the obstruction
genuinely vanishes because the source obstruction was not target-admissible.
