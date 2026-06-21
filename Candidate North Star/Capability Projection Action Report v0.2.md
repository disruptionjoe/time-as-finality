# Capability Projection Action Report v0.2

## Status

This report is a Candidate North Star working artifact.

It is not canon.
It is not a claim update.
It is not a roadmap commitment.
It is not paper-ready.
It does not promote the Candidate North Star.

This version revises `Capability Projection Action Report v0.1.md` after
hostile review. The main change is constraint: `Cap` must be typed, indexed,
equivalenced, and fixed before witness evaluation.

The governing posture remains:

```text
strongest version first
hostile audit second
demotion third
deletion only if necessary
```

## Headline Formulation

Use this as the compact formulation everywhere:

```text
For fixed observer, task, horizon, and resource boundary,
future capability need not factor through observer-visible state.
```

Formal version:

```text
pi_{O,Sigma,r,U} : Y -> X_{O,Sigma,r}(U)

Cap_{O,T,h,B} : Y -> K_{O,T,h,B}

Question:
Does Cap factor through pi up to the declared capability equivalence on K?
```

Prose name:

```text
capability-nondetermining projection
```

Do not use `nonfaithful` unless the document defines an actual functor and
hom-set injectivity question.

## Executive Judgment

The Candidate North Star remains worth preserving, but v0.1 was still too
permissive. Its danger is not obvious falsehood. Its danger is that `Cap`
could become:

```text
whatever future-useful thing the author later wishes had been preserved
```

The next phase must make the idea less inspiring and more constraining.

The project should proceed only under this rule:

```text
No capability distinction counts unless Cap was typed, indexed, and
equivalenced before the witness verdict.
```

## Non-Arbitrariness Conditions For `Cap`

A `Cap` object is admissible only if all of the following are fixed before
comparing candidate source states `y1` and `y2`.

1. The operation grammar is externally specified.
2. The task family `T` is fixed before witness evaluation.
3. The observer/access profile `O` is fixed before witness evaluation.
4. The horizon `h` is fixed before witness evaluation.
5. The budget, boundary, or resource condition `B` is explicit.
6. The capability structure `K` is typed.
7. The equivalence notion on `K` is declared before the verdict.
8. Positive controls where `Cap` does factor through `pi` are included.
9. Negative controls where `Cap` does not factor through `pi` are included.
10. Absorbing prior-art frameworks are given their full legitimate state.

Failure of any condition means the witness is under-typed, not a North Star
result.

## Default `Cap` Interface

Use indexed preorders as the default audit interface for v0.1, unless a domain
already supplies a better native structure.

Default interface:

```text
Cap_{O,T,h,B}(y) =
  indexed preorder of admissible future operations from source state y
```

Domain-native structures may be mapped into this interface for comparison:

| Domain | Native structure | Audit interface |
| --- | --- | --- |
| Git histories | graph/category of transformations | preorder of available operations |
| POMDPs | belief-state/update object | preorder over policies or values |
| resource theories | convertibility preorder/category | native preorder |
| quantum examples | operational/resource theory | preorder under allowed operations |
| sheaf examples | presheaf/sheaf with obstruction data | preorder of extend/reconstruct/glue operations |
| viability examples | reachable set / viability kernel | inclusion or dominance preorder |
| detector packets | admissibility and challenge rights | preorder of permitted audits/interventions |

The indexed preorder is not a final ontology. It is a common audit surface.

## Factorization Up To Equivalence

The strict equation:

```text
Cap = Cbar o pi
```

is too rigid for most mature settings. The audit should ask:

```text
Does there exist Cbar : X -> K
such that Cap(y) is equivalent to Cbar(pi(y))
under the declared equivalence relation on K?
```

Equivalently:

```text
Does Cap factor through pi up to chosen capability equivalence?
```

This prevents false non-factorization results that arise only because two
representations differ while their capability content is equivalent.

## Same-Neighbor-Data Condition

Before claiming residue, every absorbing framework must receive the information
that it would legitimately treat as state.

Same-neighbor-data condition:

```text
Each neighboring framework is given all information that framework normally
treats as state, history, access, resource, policy, belief, provenance,
environment, or admissibility data.
```

A witness survives as Candidate North Star residue only if:

```text
two cases remain equivalent under the relevant neighboring framework's
legitimate state representation
```

but:

```text
the typed Cap audit gives different capability verdicts
```

This blocks cheap wins where the North Star "beats" POMDPs by denying them
belief states, or "beats" provenance by hiding provenance.

## Witness Priority

Finite executable witnesses come first. Physics analogies come second.

Preferred witness order:

1. Git/provenance finite fixture:
   same endpoint tree, different revert/bisect/merge/recovery options.
2. Detector packet/access-rights finite fixture:
   same payload, different admissibility/challenge/future operation rights.
3. Quantum reduced-state/resource fixture:
   same reduced state, different global resource capability only when access
   profile includes the purifier, joint operations, side information, future
   environment access, or resource-conversion rights.
4. Viability/reachability toy model:
   same coarse state, different viable future sets.
5. Sheaf/access-boundary toy model:
   same local visible section, different extend/reconstruct/glue capability.
6. Physics analogy appendix:
   gravity, cosmology, dark matter, dark energy, black holes, Standard Model
   structure, time, and emergence.

Do not lead with cosmology. It is evocative but too easy to make rhetorical.

## Quantum Access Caveat

Quantum theory is a strong neighbor, but it needs an access-profile caveat.

Safe wording:

> Same reduced state can correspond to different global states or
> purifications. Whether this changes capability depends on the
> observer/access profile `O` and allowed operation class. For a strictly local
> observer with no side access, the difference may be operationally
> unavailable; for an observer with access to the purifying system, joint
> operations, side information, future environment interaction, or
> entanglement-conversion protocols, the capability object may differ.

This prevents the local-state example from smuggling in inaccessible global
structure.

## Physics Quarantine

Physics sections are not evidential support for the Candidate North Star.

They are analogy and discipline sections. Their job is to prevent naive
language, import constraints, and identify stress tests. They do not promote
the thesis.

Every physics section must use:

```text
Known physics
Safe bridge
Not claimed
Test route
Falsifier / likely absorber
```

Allowed uses:

- analogy;
- stress test;
- borrowed formal constraint;
- example of projection insufficiency.

Disallowed uses:

- evidence for the North Star;
- proof of capability geometry;
- replacement language for physics;
- dark matter/dark energy/gravity/time explanation.

## Positive Controls

Positive controls must be added before any finite witness can be taken
seriously.

Examples where `Cap` should factor through `pi`:

1. fully observed deterministic finite state;
2. sufficient statistic for a fixed decision problem;
3. bisimulation-preserving abstraction;
4. complete resource monotone for a tiny fixture;
5. full detector packet including all admissibility fields;
6. full provenance graph for a Git operation-right fixture.

If the schema cannot recognize preservation cases, it is unfalsifiable.

## Decision Gate

After three finite witnesses and three positive controls, decide whether the
Candidate North Star is:

1. a distinct schema;
2. a translation layer across known theories;
3. absorbed vocabulary.

Decision should be based on:

- whether `Cap` was typed before verdicts;
- whether same-neighbor-data controls were respected;
- whether positive controls passed;
- whether any witness survived mature prior-art absorption.

## Updated Artifact Queue

### A. Capability Projection Schema v0.1

Label: `TYPE`

Purpose:

Define the audit interface:

```text
pi_{O,Sigma,r,U}
Cap_{O,T,h,B}
capability equivalence
factorization up to equivalence
non-arbitrariness conditions
same-neighbor-data condition
positive controls
```

This is now the highest priority artifact.

### B. Capability Factorization Audit Template v0.1

Label: `TEST`

Purpose:

Make every example answer the same fields:

```text
source structure Y
visible shadow X
projection pi
observer/access profile O
schema Sigma
resolution r
domain U
task T
horizon h
budget/resource boundary B
Cap type
Cap equivalence
factorization verdict up to equivalence
positive controls
negative controls
neighbor-state allowances
absorber
residue
```

### C. Prior-Art Absorption Matrix v0.1

Label: `COMPARE`

Purpose:

Hostile absorption matrix for:

- POMDPs;
- sufficient statistics / Blackwell order;
- control observability;
- bisimulation;
- resource theory;
- viability;
- causal inference;
- sheaf obstruction;
- Koopman;
- provenance/access control;
- abstract interpretation;
- opportunity sets;
- affordance theory.

### D. Candidate North Star v0.2

Label: `PRESERVE + TYPE`

Purpose:

Create a new North Star version, not a replacement, that:

- uses the headline formulation;
- starts with prior art;
- defines `Cap` as an audit interface;
- includes non-arbitrariness conditions;
- uses factorization up to equivalence;
- defines same-neighbor-data;
- moves physics into analogy/stress-test sections.

### E. Physics Grounding Appendix v0.1

Label: `PHYSICS-GROUND`

Purpose:

Preserve physics-facing material under quarantine.

## Immediate Do / Do Not

## Do

- Preserve the intuition.
- Use `capability-nondetermining projection`.
- Use `Cap does not factor through pi up to declared equivalence`.
- Fix `Cap` before witness verdicts.
- Use indexed preorder as default audit interface.
- Allow domain-native structures to map into the audit interface.
- Define same-neighbor-data before claiming residue.
- Add positive controls early.
- Treat prior-art absorption as information.
- Keep physics, but quarantine it.

## Do Not

- Do not call the projection `nonfaithful`.
- Do not leave `Cap` vague.
- Do not let `Cap` be discovered after seeing the witness.
- Do not deny neighbor frameworks their legitimate state.
- Do not use physics analogies as evidence.
- Do not lead with cosmology before finite witnesses.
- Do not edit the canonical North Star without explicit approval.

## Bottom Line

The next document should be less inspiring and more constraining.

The strongest governing principle is:

```text
No capability distinction counts unless Cap was typed, indexed, and
equivalenced before the witness verdict.
```
