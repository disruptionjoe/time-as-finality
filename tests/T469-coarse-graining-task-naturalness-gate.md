# T469: Coarse-Graining Task-Naturalness Gate

## Target Claims

- [D1: Physical Finality Definition](../claims/D1-physical-finality-definition.md)
- [T10: Finality Superselection Rule](T10-finality-superselection-rule.md)
- [T29: Projection-Obstruction Schema](T29-projection-obstruction-schema.md)
- [valid-coarse-graining-as-finality-admissibility](../open-problems/valid-coarse-graining-as-finality-admissibility.md)
- [T467: Valid Coarse-Graining Admissibility Gate](T467-valid-coarse-graining-admissibility-gate.md)
- [T468: Coarse-Graining Positive-Control Independence](T468-coarse-graining-positive-control-independence.md)

## Question

Can the T467/T468 valid-coarse-graining lane be repaired into a stricter
finite packet gate that requires independent positive controls and a real
task-naturalness account rather than a bare `finality_native_task` flag?

## Setup

T469 evaluates finite coarse-graining packets over a four-bit record-state
universe with the first three fields inside the observer access boundary. The
repaired packet uses three accessible holders, preserving T468's minimum
holder width for independent positive controls while retaining a hidden fourth
field as an access-boundary hostile control.

Each candidate must pass:

- the T467-style bounded-certification gate;
- a predeclared certified record object;
- preservation of record value, support, or finality status;
- task semantics that do not merely restate the chosen labeler;
- an explicit demotion condition;
- no observer-creates-truth overread.

The packet also must show that its positive controls are independent and that
cheap accessible non-finality hostile controls are blocked.

## Positive Controls

- `three_holder_finality_band`: three accessible holders certify
  stable-zero, stable-one, or unsettled finality status.
- `three_holder_support_count`: three accessible holders certify local
  finalized-support multiplicity.

## Hostile Controls

- `cheap_accessible_xor_with_task_label`: cheap, accessible, and admitted by
  the older mechanical gate if a task label is asserted, but blocked by T469
  because no certified record object or natural finality task is supplied.
- `label_restatement_lookup`: bounded relation whose task account merely
  restates selected labels.
- `hidden_fourth_field_task`: depends on a field outside the observer boundary.
- `observer_creates_truth_overread`: treats observer equivalencing as making
  underlying truth.

## Legacy Packet Control

The inherited two-holder T467 positive controls are evaluated as a packet. They
remain individually well-formed but fail packet admission because the finality
band and support count induce the same partition in the two-holder fixture.

## Success Criteria

T469 succeeds if it:

- admits the repaired three-holder packet for review;
- rejects the inherited two-holder packet for non-independent positive controls;
- blocks cheap xor even when it passes the old mechanical admission gate;
- blocks label-restatement, hidden-field, and observer-creates-truth controls;
- leaves claim status, public posture, and North Star untouched.

## Failure Criteria

T469 fails if it:

- treats the two-holder T467 positives as independent support;
- admits a cheap accessible xor because a task label was asserted;
- accepts label restatement as task-naturalness evidence;
- accepts inaccessible fields or observer-creates-truth overreads;
- promotes D1, T10, T29, Observer Theory, valid coarse-graining, or any
  physics/consciousness claim.

## Result

Implemented as T469 v0.1.

Verdict:

```text
TASK_NATURALNESS_GATE_BUILT_FIXTURE_REPAIRED_NO_PROMOTION
```

The repaired three-holder packet is admitted for future review, while the
legacy two-holder packet is not. This is a fixture repair and admission gate,
not an Observer Theory equivalence theorem, D1/T10/T29 promotion, claim
upgrade, or physics/consciousness result.
