[!note] this requires the deep research to come back and explicit joe approval to replace current north star

Observable equivalence is not necessarily capability equivalence.

````markdown
# Physics-Forward North Star: Observable Shadow And Capability Fiber

## Status

This is an intuitive North Star, not an earned theorem.

It is allowed to be bold, but it must remain mathematically typed.

Do not treat this as:
- a physics claim,
- a GU result,
- a TaF theorem,
- a replacement for relativity,
- a replacement for quantum theory,
- or a dark matter / dark energy explanation.

Treat it as the strongest guiding question currently visible from the repo:

> Is observable state sufficient to determine future admissible operations?

The recurring answer across recent audits appears to be:

> Not always.

---

# Core Mathematical Form

Let:

```text
π_{O,Σ,r,U} : Y -> X_{O,Σ,r}(U)
````

where:

- `Y` is a richer source state space;

- `X_{O,Σ,r}(U)` is the observer-visible shadow over domain `U`;

- `O` is the observer;

- `Σ` is the observational schema or interface;

- `r` is resolution / fidelity;

- `U` is a local domain or patch.


Let:

```text
Cap_{O,T,h,B}(y)
```

be the future capability structure available from source state `y`, indexed by:

- `O` = observer;

- `T` = task family;

- `h` = horizon;

- `B` = budget, boundary, or resource condition.


Examples of capabilities:

- transformations;

- measurements;

- reconstructions;

- interventions;

- certifications;

- challenges;

- repairs;

- transports;

- gluing operations;

- future decision rights.


The key relation is:

```text
π_{O,Σ,r,U}(y1) = π_{O,Σ,r,U}(y2)
```

does **not** necessarily imply:

```text
Cap_{O,T,h,B}(y1) = Cap_{O,T,h,B}(y2)
```

Equivalently:

```text
Cap_{O,T,h,B}
```

does not necessarily factor through:

```text
π_{O,Σ,r,U}
```

There may be no map:

```text
Cbar : X_{O,Σ,r}(U) -> Capability
```

such that:

```text
Cap = Cbar ∘ π
```

When no such factorization exists, the projection is:

```text
capability-nondetermining
```

or:

```text
capability-incomplete
```

This avoids category-theoretic confusion around the word "faithful."

---

# Central North Star

The observer-facing world may be a shadow of richer structure.

The visible state may tell us what is presently observable.

The capability fiber tells us what remains physically, causally, informationally, or operationally possible.

In shorthand:

```text
reality as experienced
=
observable state
+
capability fiber
```

The visible world is not denied.

The claim is only that the visible state may not be a complete invariant of future capability.

---

# Cap Structure Is The First Open Problem

The object:

```text
Cap(y)
```

must not remain vague.

Possible structures include:

1. a set of future operations;

2. a preorder of convertibility;

3. a category of admissible transformations;

4. a resource theory;

5. a Markov decision process;

6. a reachability relation;

7. a sheaf/subpresheaf of admissible sections;

8. an opportunity set;

9. an affordance landscape;

10. a policy space.


The central open problem is:

> Which Cap structure is appropriate for which domain?

Do not assume one universal Cap object.

---

# Known Prior Art To Compare Against

This North Star sits near several existing theories:

- POMDPs and partial observability;

- sufficient statistics;

- resource theories in quantum information;

- reachability and controllability;

- viability kernels;

- opportunity-set economics;

- affordance theory;

- active inference policy spaces;

- reinforcement-learning action/state spaces;

- sheaf theory and section compatibility;

- Koopman operator theory;

- provenance systems;

- access-control systems;

- mechanism design;

- abstract interpretation.


The research question is not:

> Is this completely new?

The research question is:

> Does this schema help unify the recurring same-visible-state / different-future-capability witnesses across domains?

---

# Physics-Forward Interpretations

The following are not claims.

They are disciplined physics-facing readings of the same mathematical pattern.

## 1. General Relativity

In general relativity, spacetime geometry determines causal structure.

The metric and matter-energy distribution affect:

- future-directed causal curves;

- horizons;

- accessible regions;

- proper-time structure;

- possible interactions.


Physics-facing reading:

> Gravity changes the geometry of future accessibility.

Mathematical form:

```text
same local visible description
does not necessarily imply
same future causal capability
```

The capability object may include reachable causal futures, admissible interactions, and possible observation domains.

## 2. Cosmological Expansion

In standard cosmology, the expansion history affects horizons and large-scale causal accessibility.

Physics-facing reading:

> Expansion changes the large-scale structure of future access.

The strong version is not:

```text
expansion creates time
```

but:

```text
cosmic expansion changes the future accessibility geometry available to embedded observers
```

This can be made mathematical through causal diamonds, event horizons, conformal time, and observer-dependent accessible regions.

## 3. Dark Matter

Dark matter should not be reinterpreted as "capability."

The disciplined reading is:

> visible luminous structure is not a sufficient invariant for gravitational dynamics.

Dark matter is already a case where:

```text
visible matter distribution
```

does not determine:

```text
dynamical gravitational consequences
```

Physics-facing reading:

> Hidden structure can survive projection through its dynamical effects.

This is an analogy for the schema, not an explanation of dark matter.

## 4. Dark Energy

Dark energy should not be called "possibility expansion."

The disciplined reading is:

> accelerated expansion modifies future causal accessibility.

In a universe with accelerated expansion, some regions become permanently inaccessible.

Physics-facing reading:

> Dark energy changes the asymptotic structure of future reachability.

Capability language may help describe the observer-relative loss of future causal access.

## 5. Black Holes

Black holes are natural capability-boundary objects.

They restrict:

- future communication;

- reconstruction;

- causal access;

- recoverable evidence;

- external intervention.


Physics-facing reading:

> A horizon is a boundary in future operation availability.

This does not solve the black hole information problem.

It only says black holes are a natural testbed for the distinction between visible exterior state and accessible future operations.

## 6. Standard Model Particles

Electrons, quarks, gauge bosons, and other particles should not be replaced by capability language.

But the Standard Model already uses structures that constrain future operations:

- charge constrains allowed interactions;

- spin constrains representation behavior under rotations/Lorentz transformations;

- mass affects propagation and inertial response;

- gauge structure determines coupling and redundancy;

- phase and holonomy affect interference and path-dependent observables.


Physics-facing reading:

> Particle properties are not merely labels; they constrain admissible transformations and interactions.

This fits the schema:

```text
same base spacetime location
+
different internal fiber data
->
different future interaction capability
```

## 7. Quantum Theory

Quantum theory provides especially strong analogues.

Examples:

- a reduced density matrix may hide different purifications;

- the same local state can have different entanglement structure;

- resource theories classify possible transformations under allowed operations;

- partial trace loses environment-side structure;

- measurement projections can preserve outcome while losing future reversibility.


Physics-facing reading:

> Local observable state may fail to determine future operational capability when hidden correlations, purification structure, or resource constraints differ.

This is one of the strongest known-neighbor domains.

## 8. Time

The North Star should not say observers create time.

The stronger version is:

> Time is the parameter along which capability structure evolves.

Or:

> Time tracks the changing relation between present visible state and future admissible operations.

This must respect recent H7 work:

- closed reversible systems do not generate strict scalar finality arrows;

- stationary finite Markov systems do not generate strict expected finality drift;

- any physical arrow requires openness, coarse-graining, resource accounting, erasure, boundary conditions, or nonstationarity.


Physics-facing reading:

> A serious capability theory of time must name the resource or boundary condition that makes capability evolution directional.

## 9. Emergence

Emergence becomes:

```text
structure
->
capability
->
further structure
```

A structure matters when it preserves or expands the future operations available to later structures.

Examples:

- atoms enable chemistry;

- chemistry enables life;

- life enables cognition;

- language enables institutions;

- science enables controlled reconstruction;

- observers enable mathematics and technology.


Physics-facing reading:

> Emergent structures are capability platforms.

This connects to maintenance, reconstruction debt, and public-goods funding of shared record systems.

---

# The Simplest Rule Set

## Rule 1 — Projection

Observers access shadows:

```text
π : Y -> X
```

## Rule 2 — Capability

Future operations live over source states:

```text
Cap : Y -> K
```

where `K` is some typed capability structure.

## Rule 3 — Factorization Test

Ask whether capability factors through the visible projection:

```text
Does there exist Cbar : X -> K
such that
Cap = Cbar ∘ π ?
```

## Rule 4 — If Yes

Then the visible state is sufficient for that capability question.

The hidden fiber structure adds nothing for that task.

## Rule 5 — If No

Then the projection is capability-incomplete:

```text
same visible state
different future capability
```

## Rule 6 — Physics Discipline

When applying this to physics, identify:

- the source structure `Y`;

- the observer-facing shadow `X`;

- the projection `π`;

- the capability structure `Cap`;

- the known physics framework;

- the nearest prior art;

- the falsification condition.


## Rule 7 — No Overclaiming

Never claim:

- capability explains dark matter;

- capability explains dark energy;

- capability replaces quantum theory;

- capability replaces general relativity;

- capability proves GU;

- observers create time.


The claim is only:

> Projection may lose operation-relevant structure.

---

# Falsification / Collapse Condition

This North Star loses force if, in all important repo domains:

```text
Cap
```

always factors through:

```text
π
```

after using standard enriched frameworks such as reachability, viability, opportunity sets, resource theories, provenance, access control, and mechanism design.

In that case, the North Star collapses into known theory.

That is an acceptable outcome.

---

# Current Strongest Formulation

The strongest version is:

> Physics may be read as the study of observable states together with the hidden structures that determine admissible future transformations.
>
> The repo's recurring pattern is that visible state often fails to determine future capability.
>
> This does not replace existing physics.
>
> It suggests a unifying mathematical question:
>
> When does observer-visible projection preserve or destroy capability-relevant structure?

Or, in one line:

```text
Observable equivalence is not necessarily capability equivalence.
```
