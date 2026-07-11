# T527: Observerse Protocol-Stack Ablation

## Target Claims

- Observerse protocol-stack exploration
- T526 follow-on context only: S1 remains guarded; no S1 movement is targeted

## Central Question

Does the recent deterministic Observerse protocol-stack ablation remain
mechanically checkable as an illustration-grade model, with each advertised
collapse mode and the governance conditional preserved?

## Setup

T527 wraps `models/observerse_stack_ablation.py` without changing its model
logic. The source model computes sustained coherent structure (SCS) for the
full stack and for removals of issuance, admissibility, sybil/finality,
consensus, and governance under two rule-horizon assumptions.

The harness freezes the review-only interpretation:

- core-layer removals must reduce SCS to at most 20% of the full stack;
- governance with near-term fixed rules must collapse;
- governance with rules that anticipate the full horizon must not collapse;
- the result remains illustration/compositionality grade, not validation.

## Success Criteria

- Full stack SCS is positive and stable.
- Each core-layer removal is at or below 20% of the full-stack SCS.
- The governance near-term/full-horizon contrast is visible.
- The generated result packet preserves no-claim, no-canon, and no-public-
  posture boundary flags.

## Failure Criteria

T527 fails if:

- any core-layer removal remains above 20% of the full-stack SCS;
- the governance conditional disappears;
- the result is framed as validating Observerse, proving S1, or proving the
  Bitcoin analogy;
- any claim status, canon verdict, or public posture is moved.

## Implementation Result

Status: implemented.

The deterministic ablation harness passes. Issuance, admissibility,
sybil/finality, and consensus removals each collapse sustained coherent
structure to at most 20% of the full-stack baseline. Governance is conditional:
near-term fixed rules collapse, while full-horizon rules do not.

## Run Command

```bash
python -m unittest tests.test_observerse_stack_ablation -v
python -m models.run_t527
```

## Boundary

T527 is a regression harness for an illustration-grade deterministic model. It
does not validate Observerse, derive S1, prove the Bitcoin analogy, promote any
claim, change canon, or change public posture.
