# LossKernel Witness-Obligation Normal Form

## Status

Open formal target after T108 and T127.

## Why This Exists

T99, T108, and T127 jointly narrow the honest surviving LossKernel target.

- T99 shows label-only `LossKernel` is too weak.
- T108 shows the current relocation semantics is absorbed by mature neighbor
  frameworks once they receive the same source fiber and target judgment.
- T127 shows no strict same-neighbor-data separation survives in the current
  finite fixture family.

So the next target should not be:

```text
find one more clever finite witness and call LossKernel novel
```

The next target should be:

```text
define the strongest canonical normal form for source-derived witness
obligations, then test whether that normal form does any work that nearby
frameworks do not already do
```

## Recast Target

For a typed projection or morphism

```text
f : Source -> Target
```

and a declared target-side judgment family

```text
J
```

define a source-derived obligation object

```text
WO(f, J)
```

that names which source-lift distinctions must still be witnessed, certified,
or ruled out before `J` can be treated as settled from target-side data alone.

The important shift is:

```text
LossKernel as a list of lost labels
```

becomes

```text
LossKernel as a canonical normal form for witness obligations induced by
source-fiber dependence
```

## Minimal Data Shape

The current smallest serious candidate is:

```text
WO(f, J) =
  target_judgment
  source_fiber_class
  lift-sensitive distinctions
  obligation_generators
  absorbed_vs_live tag
  neighbor-visible realization map
```

Where:

- `target_judgment` fixes what verdict is under discussion.
- `source_fiber_class` fixes the relevant source lifts over the same target
  data.
- `lift-sensitive distinctions` names which source differences still change
  `J`.
- `obligation_generators` names the smallest source-derived certificates still
  needed to settle `J`.
- `absorbed_vs_live` records whether those obligations are already standard in
  a mature neighbor account.
- `neighbor-visible realization map` states how the same obligations appear in
  provenance, why-not provenance, abstract interpretation, lenses, CSP
  explanation, effect annotations, or other legitimate neighbor data.

## Canonicality Requirement

This recast only matters if `WO(f, J)` is derived rather than attached.

Minimum acceptable standard:

```text
same morphism + same source/target structures + same judgment family J
=> same witness-obligation normal form
```

If the object changes only because the author renamed labels or chose a
different prose explanation, it fails.

## What Would Count As Progress

1. Derive `WO(f, J)` canonically from source fibers and judgment dependence in
   at least one finite family.
2. Show how T107-style "loss relocation" is exactly a witness-obligation
   statement rather than a metaphor.
3. Prove a collapse theorem when the neighbor-visible realization map is
   surjective onto a mature absorber's own obligation object.
4. Produce one finite family where the normal form is useful even if it is not
   prior-art separated, for example by giving a cleaner admissibility checklist
   or a minimal source-derived audit object.

## What Would Kill This Recast

The recast should be demoted if any of the following happens.

1. `WO(f, J)` cannot be derived without hand-built annotations.
2. Every tested `WO(f, J)` is definitionally identical to a standard neighbor
   object once the same data are granted.
3. The normal form does not simplify admissibility, comparison, or hostile
   review relative to existing provenance/effect/audit machinery.
4. The best surviving statement is still only:

```text
some hidden source distinction matters
```

with no canonical witness object.

## Current Strongest Safe Claim

After T127, the strongest safe claim is:

```text
LossKernel has not earned a prior-art-separated theorem target in the current
finite family. At best it may survive as a canonical normal form for
source-derived witness obligations under projection.
```

## Recommended Next Move

Do one of these, and do not mix them:

1. Build a finite canonicality test for `WO(f, J)` on one existing T107/T127
   family.
2. Prove collapse into a named neighbor object under explicit same-data
   hypotheses.
3. If neither survives, demote LossKernel from open theorem target to
   integration vocabulary and stop advertising TF1 as a likely novelty route.
