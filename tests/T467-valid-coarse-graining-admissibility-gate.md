# T467: Valid Coarse-Graining Admissibility Gate

## Target Claims

- [D1: Physical Finality Definition](../claims/D1-physical-finality-definition.md)
- [T10: Finality Superselection Rule](T10-finality-superselection-rule.md)
- [T29: Projection-Obstruction Schema](T29-projection-obstruction-schema.md)
- [valid-coarse-graining-as-finality-admissibility](../open-problems/valid-coarse-graining-as-finality-admissibility.md)

## Question

Can the repo's candidate answer to the valid-coarse-graining problem be made
finite and executable without claim promotion?

The target filter is:

```text
valid for this TaF purpose
= bounded-observer-certifiable as a finalized record
```

This is not a theorem identifying TaF with Observer Theory. It is an admission
gate for future packets.

## Setup

T467 enumerates named equivalence relations over a finite binary record-state
universe. Each candidate declares:

- the record fields needed to classify a state;
- a recognition cost;
- D1-style holder redundancy;
- D1-style reversal cost;
- whether the relation was declared before use;
- whether a certified record exists;
- whether a finality-native task is actually named.

The default observer budget grants access to record fields `0, 1, 2`, permits
two read fields, permits predicate cost at most three, requires two holders, and
permits reversal cost at most two.

## Positive Controls

- `two_holder_finality_band`: two accessible holders certify `00`, `11`, or
  mismatch.
- `bounded_local_count`: two accessible holders certify the local count of
  finalized support.

## Hostile Controls

- `microstate_identity`: too fine; no coarse-graining and over budget.
- `constant_all_states`: too coarse; no task separation.
- `hidden_fourth_field`: depends on a field outside the observer boundary.
- `ornate_table_lookup`: declared but computationally ornate.
- `posthoc_exception_partition`: selected after seeing the state set.
- `projection_only_shadow`: visible projection with no certified record.
- `single_holder_dashboard`: lacks D1-style redundancy.
- `observer_creates_truth_overread`: treats equivalencing as making truth.

## Success Criteria

T467 succeeds if it:

- admits only the bounded-observer-certifiable positive controls;
- rejects identity, trivial collapse, inaccessible, ornate, posthoc,
  projection-only, one-holder, and observer-creates-truth controls;
- keeps the distinction between a projection and a certified finality record;
- leaves claim status, public posture, and North Star untouched.

## Failure Criteria

T467 fails if it:

- admits full microstate identity as valid coarse-graining;
- admits trivial all-state collapse as useful finality;
- accepts inaccessible fields or ornate recognition as bounded-observer
  certification;
- treats projection alone as finality;
- allows observer equivalencing to create underlying truth;
- promotes D1, T10, T29, H7, Observer Theory, or a physics claim.

## Result

Implemented as T467 v0.1.

Verdict:

```text
VALID_COARSE_GRAINING_ADMISSIBILITY_GATE_BUILT_NO_PROMOTION
```

In the finite fixture, the bounded-observer certification filter matches the
predeclared valid set and rejects the hostile controls. This is an admission
gate, not an equivalence theorem, claim upgrade, or physics result.
