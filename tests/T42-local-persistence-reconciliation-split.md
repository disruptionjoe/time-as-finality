# T42: Local Persistence And Reconciliation Split Audit

## Target Claims

- [R1: Relativity And No Global Commit Order](../claims/R1-relativity-no-global-commit-order.md)
- [G2: Not A Replacement Theory](../guardrails/G2-not-a-replacement-theory.md)
- [D1: Physical Finality Definition](../claims/D1-physical-finality-definition.md)
- [T3: Spacelike Events And No Global Commit Order](T3-spacelike-events-no-global-commit-order.md)
- [Exploration: Proper Time, Persistence, and Reconciliation Fork](../explorations/proper-time-persistence-reconciliation-fork.md)

## Setup

Define a finite `LocalPersistenceReconciliationSystem`:

- nodes are persistent record-holding systems;
- each node has an ordered local history of irreversible constraint events;
- a local accumulator sums irreversible constraint deltas along that history;
- record channels carry source records to target nodes with finite delay;
- comparison events compute what the target can see about the source.

The model separates two observables:

```text
local persistence accumulation
record propagation / reconciliation delay
```

The simulator event index is bookkeeping only. It is not physical time.

## Witness Cases

1. Delay without dilation:
   - both nodes accumulate the same local persistence;
   - one record channel has delay;
   - expected: reconciliation lag appears, local accumulation difference does not.

2. Dilation-like accumulation without extra delay:
   - nodes accumulate different local persistence totals;
   - record channel delay is zero;
   - expected: local accumulation difference appears, reconciliation lag does not.

3. Both effects together:
   - local accumulation differs;
   - record channel is delayed;
   - expected: both observables appear.

4. Null case:
   - local accumulation is identical;
   - record channel delay is zero;
   - expected: neither observable appears.

## Success Criteria

1. Define the finite object and all four witnesses.
2. Correctly classify delay without dilation.
3. Correctly classify dilation-like accumulation without extra delay.
4. Correctly classify both effects together.
5. Correctly classify the null case.
6. Demonstrate that local accumulation difference and reconciliation lag are
   independent finite observables.
7. Retain the R1/T3 guardrail: do not equate signal delay with time dilation.

## Failure Criteria

1. Delay alone creates a local accumulation difference.
2. Accumulation difference requires channel delay.
3. The null case manufactures a rate difference.
4. The model inserts metric proper time as an input and then claims recovery.
5. The result cannot distinguish local-history accumulation from record access lag.

## Known Physics Constraints

- This does not replace special relativity or general relativity.
- This does not derive physical proper time.
- This does not deny proper time or invariant interval structure.
- This does not treat a communication delay as time dilation.
- Any future physics-facing recovery test must map the finite accumulator to a
  known proper-time pattern without inserting that pattern as an input.

## Contribution Needed

- Compare the local accumulator to known clock models without using proper time
  as an input.
- Build a recovery test for a simple relativistic pattern only after the finite
  split has been validated.
- Decide whether local persistence remains a toy diagnostic or becomes a
  candidate physical observable.
