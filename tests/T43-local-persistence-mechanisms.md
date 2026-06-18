# T43: Local Persistence Accumulation Mechanism Audit

## Target Claims

- [R1: Relativity And No Global Commit Order](../claims/R1-relativity-no-global-commit-order.md)
- [G2: Not A Replacement Theory](../guardrails/G2-not-a-replacement-theory.md)
- [D1: Physical Finality Definition](../claims/D1-physical-finality-definition.md)
- [T42: Local Persistence And Reconciliation Split Audit](T42-local-persistence-reconciliation-split.md)

## Setup

Build finite local accumulation generators around the T42
`LocalPersistenceReconciliationSystem`.

Each candidate mechanism generates node-local event deltas. The T42 comparison
machinery then measures:

```text
local accumulation difference
reconciliation lag
```

The propagation channel is held fixed for mechanism comparisons.

## Candidate Mechanisms

1. Intrinsic stabilization rate:
   - local deltas are set by a node-local rate parameter.

2. Finite local resource budget:
   - local deltas are capped by finite per-step stabilization budget.

3. Interaction density:
   - local deltas are generated from base rate plus local coupling terms.

4. Propagation shadow:
   - rejected candidate where local accumulation is reduced by propagation
     delay.

## Success Criteria

1. Compare H0-H5 explicitly.
2. Implement at least three candidate mechanisms.
3. Hold propagation fixed while varying candidate mechanisms.
4. Show propagation changes reconciliation lag without changing local
   accumulation under fixed intrinsic traces.
5. Include a combined case with both local accumulation difference and lag.
6. Eliminate at least one candidate as disguised propagation.
7. Identify whether distinct mechanisms can produce equivalent traces.
8. Recommend the smallest supported mathematical extension.

## Failure Criteria

1. No mechanism produces local accumulation differences with propagation fixed.
2. All local accumulation differences are caused by propagation delay.
3. The implementation modifies `D1RestrictionSystem` unnecessarily.
4. The report promotes a physical proper-time claim.
5. The equivalence search hides observational ambiguity.

## Known Physics Constraints

- This does not explain relativity.
- This does not introduce spacetime dynamics.
- This does not assume local accumulation corresponds to proper time.
- This does not promote a new physical claim.

## Contribution Needed

- Add richer observables capable of distinguishing resource budget from
  interaction density.
- Build a later recovery test only if a local accumulator can be mapped to a
  physical clock observable without inserting proper time as an input.
