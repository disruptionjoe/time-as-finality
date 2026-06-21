# Fresh-Eyes Review Needed Updates v0.1

## Status

Fresh-eyes sub-agent review report for the next Candidate North Star version.

Reviewer:

```text
Sagan
```

Inputs reviewed:

- `Candidate North Star v0.2.md`;
- `Candidate North Star Next Version Update Queue v0.3.md`;
- `Prior-Art Audit of Capability Projection-deep-research-report.md`;
- `Database Absorption Test for Capability Projection-deep-research-report.md`;
- `Strongman for physics sections.md`.

## Concise Update Report

The current v0.3 queue is strong on database absorption and physics
steelmanning, but it under-integrates the broader prior-art audit. The next
Candidate North Star update should not only lower novelty around databases; it
should lower the global novelty posture around the core factorization slogan.

## Highest-Priority Additions

## 1. Add Global Absorption Warning, Not Just Database Absorption

The core sentence:

```text
observable equivalence is not necessarily capability equivalence
```

should be treated as broadly prefigured by mature traditions, especially:

- Blackwell / Le Cam / decision-theoretic sufficiency;
- concurrency/process semantics and observational equivalence;
- abstract interpretation and completeness of abstractions;
- POMDP belief-state sufficiency;
- resource-theoretic convertibility;
- causal/interventional equivalence;
- control observability/reachability.

Queue patch:

```text
The next version must say explicitly that the bare non-factorization schema is
not novel by itself. Its possible contribution is a cross-domain audit surface,
not the discovery that projections can lose future-relevant information.
```

## 2. Add Concurrency / Process Semantics As Major Missing Prior Art

The prior-art audit identifies van Glabbeek's linear-time/branching-time
spectrum and testing equivalences as the most damaging omission.

Queue patch:

```text
Add process semantics / concurrency theory to Prior Art First and
Same-Neighbor-Data. Treat distinguishing tests, bisimulation,
trace/failure/readiness semantics, and Hennessy-Milner-style logics as primary
absorbers for claims about observational equivalence versus
future-discriminating power.
```

## 3. Strengthen The Finite Pair Test With Interestingness / Canonicity

Current v0.2 pre-registration is necessary but not sufficient. A `Cap` can be
pre-registered and still be gerrymandered.

Queue patch:

```text
A finite same-pi pair is not interesting merely because Cap differs. The next
version must require a non-gerrymandered, domain-natural Cap and ask whether
the projection/capability relation is canonical, minimal, task-natural,
operationally motivated, or complete for a declared class.
```

Comparison targets:

```text
minimal sufficient statistic
coarsest adequate quotient
fully abstract semantics
Nerode congruence
minimal predictive state
belief-state reduction
complete abstract domain
```

## 4. Clarify What "Absorbed By Prior Art" Means

v0.2 sometimes implies absorption only when the neighbor distinguishes the
cases using legitimate state. Prior art can also absorb the failure itself by
already having a theory of insufficient projection.

Queue patch:

```text
Absorption can occur in two ways:
1. the neighbor's legitimate state distinguishes the cases and restores
   factorization;
2. the neighbor already has the native theorem/schema explaining the
   non-factorization.
```

This matters for Blackwell, abstract interpretation, process semantics,
databases, POMDPs, and resource theory.

## 5. Add Anti-Overclaim Language Around Enrichment

There is a tension in v0.2: enrichment is allowed, but many witnesses then
become "wrong projection" examples rather than evidence of residue.

Queue patch:

```text
When enrichment restores factorization using state variables already licensed
by the neighboring field, the result should usually be recorded as absorption,
translation residue, or heuristic residue, not as formal residue.
```

## 6. Promote Capability Type Discipline Above Examples

The next version should make `Cap` typing a central gate, not a later caveat.

Queue patch:

```text
Before any witness is considered, declare whether K is a set of answers,
preorder of admissible operations, decision-value object, provenance object,
behavioral equivalence class, resource convertibility structure, reachable set,
or approximate envelope.
```

Also add:

```text
Capability equivalence must be domain-native, task-natural, and fixed before
witness construction.
```

## Integration Priorities

1. First integrate the prior-art audit globally.
2. Then merge database updates as a special case of the broader absorption story.
3. Then upgrade physics sections into typed strongman instantiations.
4. Add a new named failure mode:

```text
gerrymandered_capability
```

Use it when `Cap` is technically predeclared but not operationally natural,
canonical, or native to the domain.

5. Add a new named target:

```text
canonical_residue
```

Use it only when a witness survives same-neighbor-data testing and uses a
domain-natural capability object not already explained by the neighboring
framework.

## Bottom Line

The next version should preserve the North Star, but with sharper humility:

```text
The bare factorization failure is old.
The possible value is a disciplined cross-domain audit language for asking
which projections preserve which future capabilities, when prior art absorbs
the answer, and when any nontrivial residue remains.
```

