# Iterated Loss Dynamics

## Status

Open formal target. This is not a main research line yet.

## Question

Given a finite typed morphism, projection, transport loop, or restriction
operator `T`, study the sequence:

```text
LossKernel(T)
LossKernel(T^2)
LossKernel(T^3)
...
LossKernel(T^n)
```

Does repeated traversal expose stable, periodic, saturating, or degrading loss
patterns that are invisible from the one-step kernel?

## Why This Is Plausible But Not Earned

Current support is one-step:

- T69 connects typed loss to failure-type monotonicity and cycle destruction.
- T73 verifies finite union-style LossKernel composition and path-dependent
  admissibility on T34/T37 families.
- T63/T65 show a holonomy branch of reconstruction failure, including a loop
  where parity matters.
- The Pati-Salam typed-forgetting witness shows that a projection can preserve
  some structure while losing load-bearing structure.

None of these yet proves that iteration adds new information. Iterated loss
may collapse to ordinary finite powerset saturation:

```text
LossKernel(T^n) = LossKernel(T)
```

or to monotone label accumulation with no new mathematics.

## Guardrail On GU-Adjacent Sources

Geometric Unity is not treated as validated physics. GU-adjacent structures may
only serve as geometry-generating test harnesses for finite loops, projections,
or transports. Valid phrasing:

```text
GU suggests a candidate finite loop to probe.
```

Invalid phrasing:

```text
GU predicts this loss dynamic.
```

The Pati-Salam witness is the precedent: it is useful as a finite
typed-forgetting example, not as validation of GU physics.

## Candidate Behaviors

An iterated LossKernel trajectory may show:

- fixed point;
- period-2 Mobius-like recurrence;
- longer recurrence;
- monotone saturation;
- attractor;
- no recurrence within bounded horizon;
- failure-type degradation;
- hidden periodicity in preserved or forgotten structure.

## Feature Schema For A First Executable Test

For each finite trajectory `T, T^2, ..., T^n`, extract:

- loss size;
- loss type vector;
- newly lost dimensions;
- preserved invariant count;
- failure type: `none`, `H0`, or `H1`;
- `cycle_destroying` flag;
- `topology_preserved` flag;
- holonomy value when defined;
- recurrence period if detected;
- stabilization time;
- projection target class.

The purpose of latent/signature analysis is example discovery only. It must not
replace the symbolic LossKernel definitions.

## Success Criteria

- Produce at least one bounded finite operator where `LossKernel(T^n)` has a
  behavior not visible from `LossKernel(T)` alone.
- Show that the behavior is not merely label-union saturation already explained
  by T73.
- Connect the behavior to at least one existing earned result: T69, T73,
  T63/T65, Pati-Salam typed forgetting, or the reconstruction-failure hierarchy.
- State a falsification condition for every proposed recurrence category.

## Failure Criteria

- Every finite witness reduces to one-step LossKernel plus ordinary finite
  union saturation.
- The examples require GU physics claims rather than finite mathematical
  structures.
- The feature extractor clusters fixtures only by hand-chosen labels.
- Recurrence taxonomy appears before a nontrivial witness family exists.

## First Concrete Test

Build a bounded executable audit, tentatively:

```text
T101: Iterated Loss Dynamics
```

Minimum model:

1. Define a finite `IteratedLossOperator` carrying source state, target state,
   preserved structure, forgotten structure, and optional cover/holonomy data.
2. Include at least four controls: fixed loss, monotone saturation, period-2
   recurrence, and cycle-destroying degradation.
3. Compute `LossKernel(T^n)` up to a fixed horizon.
4. Detect period, stabilization time, failure-type change, and whether the
   trajectory is already explained by T73 union accumulation.
5. Explicitly classify the result as example-generator, algebra extension, or
   null visualization.

## Promotion Gate

Do not promote iterated loss to a main research line until it explains at least
two existing earned branches better than the one-step LossKernel:

- path-dependent admissibility in T73;
- failure-type monotonicity in T69;
- holonomy/loop behavior in T63/T65;
- representation/projection loss in the Pati-Salam witness;
- reconstruction-failure hierarchy cases.

If it only generates examples, keep it in persona backlog and explorations.
If it defines a finite orbit object with nontrivial invariants, promote only to
the LossKernel formalization program, not to independent physics.
