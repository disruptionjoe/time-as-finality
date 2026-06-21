# Candidate North Star v0.3 Synthesis Plan

## Status

Synthesis artifact for drafting:

```text
Candidate North Star v0.3.md
```

Inputs synthesized:

- `Candidate North Star v0.2.md`;
- `Candidate North Star Next Version Update Queue v0.3.md`;
- `Prior-Art Audit of Capability Projection-deep-research-report.md`;
- `Database Absorption Test for Capability Projection-deep-research-report.md`;
- `Strongman for physics sections.md`;
- `Fresh-Eyes Review Needed Updates v0.1.md`.

## Main Verdict

The next version should preserve the Candidate North Star, but with sharper
humility and stronger typing.

The bare slogan:

```text
observable equivalence is not necessarily capability equivalence
```

is not novel as a mathematical idea.

The possible value is:

```text
a disciplined cross-domain audit language for asking which projections
preserve which future capabilities, when prior art absorbs the answer, and
when any canonical residue remains.
```

## Draft Spine

## 1. Status And Posture

State clearly:

- not canon;
- not a theorem;
- not a physics claim;
- not a novelty claim about projection loss;
- a candidate cross-domain audit surface.

## 2. Governing Sentence

Keep:

```text
For fixed observer, task, horizon, and resource boundary,
future capability need not factor through observer-visible state.
```

But immediately add:

```text
This is old in many mature theories. The live question is not whether
projection can lose future-relevant information, but whether one indexed audit
surface usefully compares such losses across domains.
```

## 3. Formal Core

Keep:

```text
pi_{O,Sigma,r,U} : Y -> X_{O,Sigma,r}(U)
Cap_{O,T,h,B} : Y -> K_{O,T,h,B}
```

Add the fiber-constancy formulation:

```text
Cap factors through pi up to equivalence iff Cap is equivalent-constant on
each pi-fiber.
```

## 4. Capability Type Gate

Before examples, require `K` to be declared:

- set of answers;
- preorder of operations;
- decision/risk object;
- provenance object;
- behavioral equivalence class;
- resource convertibility structure;
- reachable/viable set;
- causal intervention query class;
- database workload;
- approximate retrieval envelope.

Add:

```text
gerrymandered_capability
```

for technically predeclared but non-natural `Cap`.

## 5. Prior-Art First

Add top-tier absorbers:

- Blackwell / Le Cam / decision sufficiency;
- concurrency/process semantics and testing equivalences;
- abstract interpretation and complete abstractions;
- POMDP belief-state sufficiency;
- resource convertibility;
- causal inference;
- control observability/reachability;
- database determinacy and provenance.

## 6. Absorption Has Two Forms

Add:

```text
state-enrichment absorption
native-theory absorption
```

Formal residue requires surviving both.

## 7. Finite Pair Test Is Necessary But Weak

State:

```text
A same-pi/different-Cap pair proves only non-factorization for the chosen
projection and capability. It is interesting only when the projection and Cap
are domain-natural, canonical, or operationally forced.
```

## 8. Residue Ladder

Use:

1. canonical residue;
2. formal residue;
3. translation residue;
4. heuristic residue;
5. redundant/demoted.

Define `canonical_residue` as the strong target.

## 9. Database Section

Treat database theory as the cleanest finite executable absorber:

- view/query determinacy;
- provenance;
- MVCC;
- access control;
- materialization/index state;
- distributed consistency;
- vector/ANN approximate retrieval.

Make database examples finite witnesses and controls, not novelty evidence.

## 10. Physics Strongman

Keep physics, but upgrade it.

Each section should instantiate:

```text
Y / X / pi / Cap / K / equivalence / non-factorization question / support /
kill condition / absorber / not claimed
```

Physics should be bold but not incorrect.

## 11. Collapse Condition

Make collapse stronger:

```text
If mature prior art absorbs the distinction by enrichment or by native theory,
record translation or heuristic residue. Do not defend formal novelty.
```

## Drafting Rule

The new version should be less defensive than v0.2 in the physics sections, but
more hostile than v0.2 in the prior-art sections.

In short:

```text
humble about novelty
strict about Cap
strong about physics instantiation
honest about absorption
```

