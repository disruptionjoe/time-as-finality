# Candidate North Star v0.2: Capability Projection

## Status

This is a Candidate North Star working draft.

It is not canon.
It does not replace `NORTH-STAR.md`.
It is not a claim update.
It is not a roadmap commitment.
It is not paper-ready.
It is not evidence for a physics thesis.

It is a sharpened candidate statement built from:

- `Candidate North Star.md`;
- `Prior Art And Physics Grounding For Capability Projection - Deep Research.md`;
- `Capability Projection Action Report v0.2.md`;
- `Capability Projection Schema v0.1.md`;
- the follow-up review that recommends freezing the v0.2 action report and moving from defensive critique to operational schema.

## Governing Sentence

For fixed observer, task, horizon, and resource boundary:

```text
future capability need not factor through observer-visible state
```

Equivalent slogan:

```text
observable equivalence is not necessarily capability equivalence
```

Most important guardrail:

```text
a non-factorization verdict is a projection-sufficiency failure,
not a metaphysical claim
```

The Candidate North Star is therefore not:

```text
hidden things exist
```

It is the sharper audit question:

```text
which projections preserve which future capabilities,
for which observers, tasks, horizons, and resource boundaries?
```

## Core Question

Let:

```text
pi_{O,Sigma,r,U} : Y -> X_{O,Sigma,r}(U)
```

where:

- `Y` is a richer source structure;
- `X_{O,Sigma,r}(U)` is the observer-visible shadow over domain `U`;
- `O` is the observer or access profile;
- `Sigma` is the observational schema or interface;
- `r` is resolution, fidelity, or coarse-graining;
- `U` is the local domain, patch, or scope.

Let:

```text
Cap_{O,T,h,B} : Y -> K_{O,T,h,B}
```

where:

- `T` is the task family;
- `h` is the horizon;
- `B` is the budget, boundary, or resource condition;
- `K` is the typed capability structure.

The question is:

```text
Does Cap factor through pi up to the declared capability equivalence on K?
```

That is, does there exist:

```text
Cbar : X_{O,Sigma,r}(U) -> K_{O,T,h,B}
```

such that:

```text
Cap_{O,T,h,B}(y) ~=_K Cbar(pi_{O,Sigma,r,U}(y))
```

for every admissible source state `y`?

Finite pair test:

```text
pi(y1) = pi(y2)
```

but:

```text
Cap(y1) not ~=_K Cap(y2)
```

If such a pair survives the admissibility and prior-art controls, then `pi` is
capability-nondetermining for that indexed capability question.

## The Meaning Of `Cap`

`Cap` must not mean:

```text
whatever future-useful thing becomes convenient after seeing the example
```

The default early-stage interface is:

```text
Cap_{O,T,h,B}(y) =
  an indexed preorder of admissible future operations from source state y
```

The preorder is not a final ontology. It is a common audit surface.

Domain-native structures may map into it:

| Domain | Native structure | Audit reading |
| --- | --- | --- |
| Git/provenance | history graph or transformation category | available recovery, revert, bisect, merge, and audit operations |
| detector packets | admissibility, provenance, and challenge rights | permitted future audits and interventions |
| POMDPs | belief state and policy/value structure | future policies, values, or reachable beliefs |
| control theory | reachable and observable state structure | future controllability, estimability, and intervention options |
| resource theory | convertibility preorder or category | transformations under allowed operations |
| quantum examples | operational/resource structure | future operations under an access profile |
| sheaf examples | local sections and obstruction data | extend, reconstruct, or glue operations |
| viability examples | viability kernel or reachable set | constraint-respecting future paths |
| access control | permissions, roles, revocation, authority | future authorized actions |

The central open problem is not whether capability can be named.

The central open problem is:

```text
which Cap type makes capability equivalence,
projection loss, and prior-art absorption testable?
```

## Non-Arbitrariness Contract

No capability distinction counts unless `Cap` was typed, indexed, and
equivalenced before the witness verdict.

Every serious witness must fix:

1. operation grammar;
2. task family `T`;
3. observer/access profile `O`;
4. horizon `h`;
5. budget, boundary, or resource condition `B`;
6. source state space `Y`;
7. visible projection `pi`;
8. capability structure `K`;
9. capability equivalence `~=_K`;
10. preservation controls where `Cap` should factor through `pi`;
11. non-factorization witnesses where `Cap` should not factor through `pi`;
12. absorbing prior-art frameworks and their legitimate state.

Failure to satisfy this contract gives:

```text
under_typed
```

not:

```text
North Star evidence
```

## Projection Enrichment Is Allowed

An obvious objection is:

```text
then enrich the visible state until capability does factor
```

The answer is:

```text
yes
```

Enrichment is an allowed and often preferred outcome.

The audit does not assume that the original visible state was the right state
description. It asks which projection is sufficient for which capability
question.

When a richer projection preserves capability, record:

```text
projection pi was insufficient
enriched projection pi' was sufficient
```

This is a useful result, not a defeat.

## Same-Neighbor-Data Condition

Before claiming residue beyond prior art, each neighboring framework must
receive all information that it legitimately treats as state.

Examples:

| Neighbor | Legitimate state/data |
| --- | --- |
| POMDPs | belief state, history, transition model, observation model |
| sufficient statistics / Blackwell order | decision problem, experiment, risk/value structure |
| control theory | latent state, output map, dynamics, controls |
| bisimulation | transition and reward/future behavior structure |
| resource theory | allowed operations, free states, monotones, catalysts if admitted |
| causal inference | graph class, latent assumptions, intervention targets |
| provenance | history, dependency graph, signatures, authority |
| access control | permissions, roles, policies, revocation/challenge state |
| sheaf theory | cover, sections, restrictions, coefficient system |
| viability theory | constraints, dynamics, horizon, viability kernel |
| abstract interpretation | abstraction/concretization maps, fibers, invariants |

A witness survives as Candidate North Star residue only if:

```text
two cases remain equivalent under the neighbor's legitimate representation
```

but:

```text
the typed Cap audit still gives inequivalent capability
```

If the neighbor distinguishes the cases using its legitimate state, the result
is:

```text
absorbed by neighbor
```

Absorption is information. It is not embarrassment.

## Residue Ladder

The Candidate North Star should no longer use a binary split between
"distinct schema" and "absorbed vocabulary."

Use four outcomes.

### 1. Formal Residue

A capability distinction survives after mature neighboring frameworks receive
their legitimate state.

This is the only outcome that supports a distinct mathematical program.

### 2. Translation Residue

No new formal phenomenon survives, but the schema aligns multiple neighboring
theories under one audit surface.

This may still be valuable.

### 3. Heuristic Residue Only

The language helps discover missing state, access, provenance, or resource
data, even though the final explanation belongs to known theory.

This should be preserved as workflow vocabulary, not promoted as theory.

### 4. Delete Or Demote As Redundant

The language adds confusion, duplicates an existing framework, or fails to make
new distinctions.

Demotion can preserve a note as historical or comparative context.

## Prior Art First

This Candidate North Star is surrounded by strong prior art.

That is a strength if handled honestly.

The first comparison surfaces are:

- POMDPs and belief-state sufficiency;
- sufficient statistics and Blackwell informativeness;
- control observability and controllability;
- bisimulation-preserving abstraction;
- resource-theory convertibility;
- viability kernels;
- causal inference and interventional equivalence;
- sheaf local-to-global obstruction;
- Koopman/operator-theoretic observables;
- provenance and access-control systems;
- abstract interpretation;
- opportunity-set and affordance theories.

The North Star should not claim:

```text
these traditions missed hidden capability
```

It should ask:

```text
can a single indexed factorization audit make their shared projection-loss
pattern easier to compare, test, and demote when absorbed?
```

## Witness Priority

Finite, executable, same-visible-state witnesses come before physics analogies.

Preferred order:

1. Git/provenance fixture:
   same endpoint tree, different revert, bisect, merge, recovery, or audit
   operations.
2. Detector packet/access-rights fixture:
   same payload, different admissibility, challenge, or future intervention
   rights.
3. Quantum local-state/resource fixture:
   same reduced state, different global resource capability only under an
   access profile that includes purifier access, joint operations, side
   information, future environment access, or resource-conversion rights.
4. Viability/reachability fixture:
   same coarse state, different viable future sets.
5. Sheaf/access-boundary fixture:
   same local visible section, different extend/reconstruct/glue capability.
6. Physics analogy appendix:
   gravity, cosmology, dark matter, dark energy, black holes, Standard Model
   structure, time, and emergence.

## Preservation Controls

A serious schema must know when projection is sufficient.

Examples where `Cap` should factor through `pi`:

- fully observed deterministic finite state;
- sufficient statistic for a fixed decision problem;
- bisimulation-preserving abstraction;
- complete resource monotone for a tiny fixture;
- full detector packet including all admissibility fields;
- full provenance graph for a Git operation-right fixture.

If the schema cannot recognize preservation, it is unfalsifiable.

## Non-Factorization Witnesses

Examples where `Cap` may fail to factor through `pi`:

- same endpoint Git tree with different history-dependent recovery rights;
- same detector payload with different admissibility wrapper;
- same reduced quantum state with different resource capability under a
  qualified access profile;
- same coarse reachable state with different viability kernel;
- same local section with different global reconstruction or gluing capability.

These are not conclusions. They are audit targets.

## Physics Analogy Discipline

Physics stays in the Candidate North Star, but it is not evidential support.

Physics sections are:

- analogy;
- stress test;
- borrowed formal constraint;
- source of disciplined examples.

Physics sections are not:

- proof of the Candidate North Star;
- replacements for known physics;
- explanations of gravity, dark matter, dark energy, black holes, quantum
  theory, or time.

Every physics use must state:

```text
Known physics
Safe bridge
Not claimed
Test route
Falsifier / likely absorber
```

### Gravity

Known physics: general relativity ties causal accessibility to spacetime
geometry through light cones, causal futures, horizons, and global structure.

Safe bridge:

```text
geometry constrains future accessibility
```

Not claimed:

```text
gravity is capability
capability explains gravity
```

Likely absorber: standard causal structure in general relativity.

### Cosmology And Dark Energy

Known physics: expansion history and accelerated expansion affect large-scale
causal accessibility and event horizons.

Safe bridge:

```text
cosmic expansion changes future accessibility geometry
```

Not claimed:

```text
dark energy is capability
capability explains accelerated expansion
```

Likely absorber: cosmological horizon and causal-access theory.

### Dark Matter

Known physics: electromagnetically visible structure does not determine all
gravitationally relevant structure.

Safe bridge:

```text
visible structure can underdetermine dynamically relevant structure
```

Not claimed:

```text
dark matter is hidden capability
capability explains dark matter
```

Likely disposition: analogy only.

### Black Holes

Known physics: horizons are causal boundaries that make observer location and
access profile unavoidable.

Safe bridge:

```text
horizon = boundary in future operation availability
```

Not claimed:

```text
capability solves the information problem
black holes prove TaF
```

Likely absorber: standard horizon, causal-access, and reconstruction language.

### Quantum Theory

Known physics: local reduced states can hide purification, entanglement, and
resource structure, but only some observers can operationally access those
differences.

Safe bridge:

```text
same local readout may coexist with different global operational possibilities
under a qualified access profile
```

Not claimed:

```text
same reduced density matrix always implies different local capability
```

Mandatory caveat:

```text
for a strictly local observer with no side access, different purifications may
be operationally unavailable
```

Likely absorber: quantum information and quantum resource theory.

### Standard Model Structure

Known physics: charge, spin, mass, gauge representation, phase, and selection
rules constrain possible interactions.

Safe bridge:

```text
internal physical structure constrains admissible transformations
```

Not claimed:

```text
charge, spin, or mass are capability
```

Likely disposition: useful analogy and formal discipline, not evidence.

### Time

Known physics: relativity and thermodynamics already govern temporal order and
physical arrows.

Safe bridge:

```text
capability can be tracked along physical time
```

or:

```text
projected visible state may remain fixed while future-operation structure
changes inside the projection fiber
```

Not claimed:

```text
observers create time
capability replaces time
closed reversible systems generate a strict finality arrow
```

Directional claims must name openness, resource accounting, erasure,
coarse-graining, boundary conditions, or nonstationarity.

### Emergence

Known neighbors: viability theory, affordance theory, niche construction, major
transitions, constructor theory, and resource theory.

Safe bridge:

```text
emergent structures can become platforms for future capability
```

Not claimed:

```text
all emergence is capability expansion
```

Likely disposition: highly generative translation layer; novelty uncertain.

## Relationship To The Existing TaF North Star

The current repo North Star protects an intuition about records, stabilization,
observer-accessible sections, finality, and the possible relation between time
and recursively nested record structures.

This Candidate North Star does not replace that intuition.

It offers a possible adjacent audit lens:

```text
record-facing projection
->
observer-visible state
```

may be insufficient to determine:

```text
future admissible operations
```

When the candidate is useful, it can sharpen questions about:

- reconstruction debt;
- observer access;
- witness availability;
- provenance and authority;
- future operation availability;
- maintenance viability;
- typed forgetting and LossKernel attribution.

When it is absorbed, it should be routed back into the absorbing framework.

## Collapse Condition

The Candidate North Star weakens or dissolves if:

```text
Cap always factors through an appropriately enriched projection
after mature neighboring theories receive their legitimate state
```

In that case, the candidate should not be defended as a new theory.

It should be recorded as one of:

- translation residue;
- heuristic residue;
- redundant vocabulary;
- deleted/demoted material.

This is an acceptable outcome.

The purpose is discovery, not defense.

## Current Best Formulation

The strongest current version is:

> For fixed observer, task, horizon, and resource boundary, future capability
> need not factor through observer-visible state.
>
> When factorization fails, the result is a projection-sufficiency failure for
> that indexed capability question, not a metaphysical discovery.
>
> When enrichment restores factorization, the enrichment should be recorded as
> the right state description.
>
> When mature prior art absorbs the distinction, the candidate survives only as
> translation or heuristic residue.

Compact form:

```text
observable equivalence is not necessarily capability equivalence
```

Operational form:

```text
type Cap
declare equivalence
test factorization
grant prior art its legitimate state
record the residue honestly
```
