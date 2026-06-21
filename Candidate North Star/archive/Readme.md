````markdown
# Candidate North Star — Research Posture

## Status

This folder exists to eventually promote one candidate North Star to replace the current North Star. Anytime any updates are made, create a new version rather than deleting the previous version.

This folder preserves bold, speculative, physics-facing North Star material.

The contents are not canon.

They are not claim updates.

They are not roadmap commitments.

They are not paper-ready statements.

They are not evidence unless separately supported by executable models, proofs, technical reports, or external sources.

This folder exists to protect and develop the deepest intuition of the project while keeping it mathematically disciplined.

---

## Core Posture

The posture of this folder is:

> Push the strongest possible mathematical version forward.
>
> Do not remove an idea merely because it is bold, speculative, unfamiliar, or not yet earned.
>
> Remove or demote an idea only when it is clearly wrong, internally incoherent, contradicted by known results, or collapses completely into better-existing theory.

The goal is not safety through vagueness.

The goal is rigor through sharpening.

---

## Working North Star

The current candidate North Star is:

> Observable state is not necessarily a complete invariant of future capability.

In mathematical shorthand:

```text
π(y1) = π(y2)
does not imply
C(y1) = C(y2)
````

where:

- `π : Y -> X` is a projection from richer source structure to observer-visible state;

- `X` is the observer-facing shadow;

- `Y` is the richer underlying structure;

- `C(y)` is the future capability structure available from source state `y`.


The visible state may remain the same while future admissible operations differ.

This pattern has appeared across:

- detector packets;

- Git/version-control histories;

- provenance;

- witness access;

- reconstruction debt;

- operation rights;

- ASP / accessible structured possibility;

- FOA / future operation availability;

- maintenance-cost investigations;

- LossKernel / loss relocation.


The current intuition is that these may be manifestations of a deeper projection/fiber/capability structure.

---

## Physics-Forward Policy

This folder should lean into physics-facing interpretations.

Do not strip out physics merely because it is speculative.

Instead, make every physics-facing idea as mathematically precise as possible.

Allowed:

- connect to known physics;

- use general relativity, quantum theory, Standard Model structure, gauge theory, fiber bundles, resource theories, causal structure, thermodynamics, and cosmology as serious comparison surfaces;

- propose bold analogies when clearly labeled;

- develop speculative bridges if they are typed, falsifiable, and not already contradicted.


Not allowed:

- claiming support that has not been earned;

- saying TaF proves GU;

- saying GU proves TaF;

- claiming a replacement for relativity, quantum theory, or the Standard Model;

- treating dark matter, dark energy, black holes, consciousness, or time as solved;

- using physics language only decoratively.


The instruction is:

> Do not remove physics.
>
> Formalize it.

---

## Default Treatment Of Bold Ideas

A bold idea should be preserved if it is:

- mathematically expressible;

- not obviously false;

- not already ruled out by known results;

- connected to a recurring pattern in the repo;

- capable of being pressure-tested;

- useful for generating finite models, audits, or proofs.


A bold idea should be demoted if it is:

- internally incoherent;

- impossible to type;

- contradicted by known physics or mathematics;

- dependent on equivocation;

- pure metaphor with no route to test;

- fully absorbed by existing theory with no useful residue.


Demotion does not mean deletion.

If an idea fails as a primitive but survives as vocabulary, analogy, audit discipline, or organizing question, preserve that outcome.

---

## Review Standard

The correct review posture is:

```text
strongest version first
hostile audit second
demotion third
deletion only if necessary
```

Do not begin by making the idea smaller.

Begin by making it sharper.

Then test it.

---

## Prior-Art Standard

Every major idea in this folder must eventually be compared against nearby known frameworks.

Relevant neighbors include:

- partial observability / POMDPs;

- sufficient statistics;

- resource theories;

- quantum information;

- reachability analysis;

- controllability;

- viability kernels;

- active inference;

- reinforcement learning;

- opportunity-set economics;

- affordance theory;

- capability theory;

- sheaf theory;

- fiber bundles;

- gauge theory;

- Koopman operators;

- provenance systems;

- access-control systems;

- mechanism design;

- abstract interpretation;

- thermodynamics;

- general relativity;

- quantum theory;

- Standard Model representation structure.


Prior-art absorption is not failure.

It is information.

If a concept collapses into known theory, record the collapse clearly and preserve any useful translation layer.

---

## Physics Interpretation Guardrail

Physics-facing sections should follow this structure:

1. State the known physics.

2. State the candidate mathematical analogy or bridge.

3. State what is not being claimed.

4. State what would make the bridge testable.

5. State what would falsify or dissolve the bridge.


Example posture:

```text
Safe:
General relativity already ties causal accessibility to spacetime geometry.
This makes gravity a natural comparison surface for future-capability geometry.

Unsafe:
Capability geometry explains gravity.
```

---

## Core Schema To Preserve

The strongest formal schema currently is:

```text
π_{O,Σ,r,U} : Y -> X_{O,Σ,r}(U)
```

where:

- `O` = observer;

- `Σ` = observational schema/interface;

- `r` = resolution or fidelity;

- `U` = local domain or patch;

- `Y` = richer source structure;

- `X` = observer-visible shadow.


Capability structure:

```text
Cap_{O,T,h,B}(y)
```

where:

- `T` = task family;

- `h` = horizon;

- `B` = budget, boundary, or resource condition.


Core question:

```text
Does Cap factor through π?
```

That is:

```text
Does there exist Cbar : X -> Capability
such that
Cap = Cbar ∘ π ?
```

If yes, the visible state is sufficient for the capability question.

If no, then the projection is capability-incomplete:

```text
same visible state
different future capability
```

---

## Candidate Physical Story

The speculative physics-facing North Star may be stated as:

> The observer-facing world is a projection of richer structure.
>
> The visible state tells us what is presently observable.
>
> The capability fiber tells us what remains physically, causally, informationally, or operationally possible.

This should be explored through known physics, not around it.

Possible physics-facing interpretations:

- **Big Bang:** initial condition as expansion of accessible structure and future possibility.

- **Cosmological expansion:** changing large-scale future accessibility geometry.

- **Gravity:** curvature shaping causal reachability and future admissible trajectories.

- **Dark matter:** visible matter distribution not being a complete invariant of gravitational dynamics.

- **Dark energy:** accelerated expansion changing asymptotic causal accessibility.

- **Black holes:** horizons as boundaries in future operation availability and reconstruction.

- **Quantum theory:** local states not determining hidden entanglement, purification, resource, or future transformation capability.

- **Standard Model particles:** charge, spin, mass, phase, and gauge structure as constraints on admissible interactions and transformations.

- **Time:** not observer-created, but possibly related to the evolution of capability structure under resource, boundary, and irreversibility conditions.

- **Emergence:** structures becoming platforms that preserve or expand future capability for further structure.


These are not claims.

They are candidate interpretations to be made rigorous or discarded.

---

## Relationship To Recent Repo Work

Recent audits repeatedly found:

```text
same visible state
≠
same future capability
```

Examples:

- same Git endpoint, different merge/revert/bisect capability;

- same detector payload, different admissibility and challenge rights;

- same coarse metrics, different witness access;

- same record, different reconstruction paths;

- same visible support, different future operation availability.


This folder should preserve the possibility that these are not isolated coincidences but instances of a shared projection/fiber/capability pattern.

---

## Falsification / Dissolution Condition

The North Star weakens or dissolves if:

```text
Cap always factors through π
```

for the important domains of the repo once standard enriched theories are properly used.

In plain English:

> If visible state plus known enriched frameworks always determine future capability, then the North Star collapses into existing reachability, viability, provenance, resource theory, or opportunity-set language.

That outcome is acceptable.

The purpose is discovery, not defense.

---

## Folder Contents

This folder may contain:

- North Star statements;

- steelman essays;

- hostile critiques;

- persona assessments;

- physics-facing speculative notes;

- prior-art comparisons;

- finite-test proposals;

- failed formulations;

- demotions and absorption results;

- candidate mathematical schemas.


It should not contain:

- claim-ledger updates;

- roadmap changes;

- paper-facing assertions;

- unsupported promotions;

- canon language.


---

## Guiding Rule

When in doubt:

```text
do not delete the intuition
type it
test it
compare it
demote it if needed
```

The purpose of this folder is to keep the boldest version alive long enough to be made precise.

The standard is not:

```text
Is this already proven?
```

The standard is:

```text
Is this mathematically expressible,
not obviously wrong,
and potentially generative under hostile review?
```

If yes, preserve it here.
