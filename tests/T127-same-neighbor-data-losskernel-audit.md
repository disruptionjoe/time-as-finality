# T127: Same-Neighbor-Data LossKernel Audit

## Route

Mathematical machinery / prior-art separation audit.

## Status

Specification only. No model, result artifact, or theorem claim exists yet.

## Anchors

- `explorations/recurring-structure-map-v0.1.md`
- `open-problems/loss-kernel-formalization.md`
- `claims/TF1-typed-forgetting-attribution.md`
- `tests/T34-po1-chained-projection.md`
- `tests/T37-typed-transport-network.md`
- `tests/T39-csp-satisfiability-reframing.md`
- `tests/T40-holarchy-lab.md`
- `tests/T69-losskernel-failure-type.md`
- `tests/T73-losskernel-composition.md`
- `tests/T99-losskernel-quotient-separation.md`
- `tests/T107-loss-relocation.md`
- `tests/T108-loss-relocation-prior-art.md`
- `papers/typed-loss-kernels-obstruction-attribution-v0.1.md`

## Question

Can LossKernel produce a different admissible-attribution verdict in two finite
cases while every mature neighboring account receives the same data?

Equivalently: is there a same-neighbor-data quotient witness where LossKernel
does more than restate gluing obstruction, CSP diagnosis, category bookkeeping,
path-sensitive labels, provenance, abstract-interpretation fibers, lens
complements, or rich effect annotations?

## Motivation

The current LossKernel program is audit-blocked. T73 supports only a finite
powerset-union annotation law. T99 shows label-only LossKernel fails the
quotient-survival gate. T107 gives a sharper source-fiber relocation semantics,
but T108 says that semantics is absorbed by why-not provenance, abstract
interpretation, lenses, CSP explanation, and rich effects unless a stricter
same-neighbor-data witness is found.

T127 is the next gate. It does not try to promote LossKernel. It asks for the
minimum fixture that would justify keeping TF1 as more than disciplined
annotation vocabulary.

## Same-Neighbor-Data Quotient

Two candidate cases `A` and `B` must be quotient-equal for all neighbor-visible
summaries listed below. The finite source/target fixtures may differ only in
data that is used to derive the proposed source-anchored witness obligation and
is not already present in any neighbor's allowed data package.

- same source and target satisfiability status;
- same ordinary source/target summaries and same composite map behavior visible
  to endpoint and categorical bookkeeping accounts;
- same endpoint behavior under the admissibility checklist except for the
  proposed LossKernel witness obligation;
- same signed-graph or CSP conflict structure, including frustrated cycles,
  minimal unsat cores, diagnoses, and repair sets available to the CSP account;
- same provenance and why-not provenance graph available to the provenance
  account;
- same abstraction and concretization fibers available to the abstract
  interpretation account;
- same lens get/put behavior and same complement data available to the lens
  account;
- same graded, writer, or rich effect annotation available to the effect account;
- same naive lost-label set and same path-sensitive accumulated label set;
- same categorical bookkeeping facts: endpoints, composability, identity,
  associativity, and union-style accumulation.

The audit may not hide distinguishing data inside a renamed LossKernel label. Any
distinction must be a source-anchored witness obligation that can be inspected
against the finite source and target structures.

## Candidate Extra Object

The only allowed extra LossKernel content is:

```text
source_anchored_witness_obligation =
  source structure reference
  target obstruction reference
  lost source witness or constraint family
  resolution role
  checkable relation between the lost witness and the target obstruction
```

The obligation must be derived from the finite source, target, and morphism data.
It is not allowed to be a free-text attribution note, a relabeled CSP diagnosis,
or a path label that differs only because the path metadata differs.

## Required Witness Attempts

### 1. Positive Separation Attempt

Construct two quotient-equal finite cases with different LossKernel attribution
verdicts:

- Case `A`: the loss object carries a source-anchored witness obligation that
  names structure whose presence resolves the target obstruction in the source.
- Case `B`: all neighbor data remain the same, but the corresponding
  source-anchored obligation fails or is absent.

This is the only route to a positive T127 result.

### 2. Absorption Control

If the proposed witness obligation is recoverable by any neighbor from its
allowed data package for the fixture, record absorption rather than separation.

### 3. Label-Only Control

Build paired cases with different naive labels but identical source-anchored
obligations. The verdict must collapse. If it does not, the test is only checking
label bookkeeping.

### 4. Endpoint-Difference Control

Build paired cases with different source or target satisfiability behavior. These
must be rejected as invalid quotient witnesses, because endpoint differences do
not count as LossKernel separation.

### 5. Path-Metadata Control

Build paired paths like the T37 diamond where path labels differ. These do not
count unless the distinction survives the same-neighbor-data quotient and is
grounded in source-anchored witness obligations rather than accumulated labels.

### 6. Absorbed-Loss Control

Include a T34/T107-style absorbed case where non-empty loss exists but target
judgments are invariant across source lifts. The verdict must demote the loss as
non-attribution-relevant, preserving the guardrail against false conservation.

## Success Criteria

T127 succeeds only if all of the following hold:

- A same-neighbor-data pair is constructed without changing neighbor-visible
  CSP, provenance, abstract-interpretation, lens, effect, path-label, or category
  bookkeeping data.
- The two cases receive different attribution verdicts solely because a
  source-anchored witness obligation passes in one case and fails in the other.
- The witness obligation is derived from finite source/target/morphism data, not
  assigned as metadata after the verdict is known.
- Label-only, endpoint-difference, path-metadata, and absorbed-loss controls all
  behave as specified.
- The result is stated as a narrow source-anchored witness obligation result, not
  as novelty for gluing obstruction, CSP mechanics, category structure, or path
  labels.

## Failure Criteria

T127 fails or demotes TF1 if any of the following occur:

- The distinction is visible to CSP, provenance, abstract interpretation, lenses,
  rich effects, or ordinary categorical bookkeeping from their allowed data
  packages.
- The distinction depends on different endpoints, different composite maps,
  different path labels, different naive lost-label sets, or different neighbor
  inputs.
- The LossKernel object merely attaches a verdict-carrying label to the morphism.
- The proposed obligation cannot be derived from source and target structures.
- Absorbed loss is forced into an attribution verdict.
- The audit claims novelty for known gluing obstruction, signed-graph parity CSP,
  category closure, monoid-valued accumulation, or path-sensitive bookkeeping.

## Expected Disposition

Default expectation is demotion. If the same-neighbor-data quotient cannot be
made strict, LossKernel remains useful as integration vocabulary:

```text
typed, composable annotation for source-derived witness obligations
```

but not as an independent formal invariant or prior-art-separated theorem.

If a strict witness is found, TF1 may remain an open formal target with a narrowed
candidate semantics:

```text
admissible attribution requires a source-derived witness obligation that survives
the same-neighbor-data quotient
```

This still would not promote the obstruction mechanism itself.

## Claim Impact

No claim promotion from this specification alone.

- `TF1` remains an open formal target.
- T34/T37/T73 remain evidence for path and composition bookkeeping only.
- T39 remains the guardrail that the obstruction layer is known CSP machinery.
- T40 remains evidence that cross-level attribution needs declared loss, not that
  declared loss is novel.
- T69 remains finite-fixture and review-blocked for general failure-type claims.
- T99/T107/T108 define the current demotion pressure.

## Implementation Notes

An eventual implementation should emit a structured verdict:

```text
separation_witness | absorbed_by_neighbor | invalid_quotient | label_only | demote
```

and should report which neighbor first absorbs the proposed distinction. No
`results/` artifact should be created until the fixture is implemented and the
controls are executable.
