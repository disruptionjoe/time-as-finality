# T196: Exact WBE-Continuum Bridge Audit

## Correction Notice

Updated after the T187 review/T200-T209 follow-up. This audit's negative
continuum verdict is strengthened: the source object is now explicitly a finite
harmonic proxy, not an exact finite Moses optimization. T205 kills the
unweighted path-harmonic proxy as a continuum-stable bridge object.

## Target Claims

- MTI (`claims/MTI-metabolic-temporal-irreducibility.md`)
- T187 finite harmonic-proxy audit
- T195 metric-causal separation beyond tree fixtures
- T197 absorber audit against scheduling / queueing / flow theory
- `open-problems/finite-to-smooth-shadow-bridge.md`
- `open-problems/temporal-issuance-source-object-spec.md`

## Origin

The current finite MTI / Cap_TI stack now says something fairly specific:

```text
finite weighted path families can exhibit metric-causal separation,
but the earned predictive object has narrowed to a harmonic-mean timing summary
T* (or T*_DAG in the finite non-tree generalization).
```

That is already much weaker than a continuum West-Brown-Enquist story. T196
asks whether the repo has actually earned a bridge from the finite objects to a
continuum WBE-style scaling reading, or whether that larger bridge remains
aspirational / imported from neighboring theory.

## Formal Target Or Obligation

Audit whether the finite MTI / Moses objects supply a typed bridge to a
continuum WBE-style target.

The bridge would need to connect:

```text
finite weighted path-time objects
  ->
continuum hierarchical transport / scaling-law objects
```

without handwaving away the following burdens:

1. the bridge type;
2. the preserved capability or residue;
3. the scaling family or limit object;
4. the role of geometry vs. imported neighboring theory;
5. positive and hostile controls.

## Candidate Source And Target

### Finite source actually earned in the repo

The source object currently earned is not "the full WBE law." It is:

```text
finite weighted path families with
T* = harmonic_mean(path delivery times),
beta = 1 - log(T*) / log(n),
R = T*
```

and its non-tree extension:

```text
finite weighted DAG families with
T*_DAG = harmonic_mean(admissible path times).
```

### Continuum target being invoked

The invoked target is a WBE-style continuum reading:

```text
hierarchical transport in a physical substrate
with a scale law such as mu ~ n^beta
and a continuum / asymptotic interpretation of beta.
```

## Required Bridge Assumptions

To honestly bridge the finite source to the continuum target, the repo would
need all of the following typed assumptions:

### Assumption A1: Bridge type

One of the accepted bridge types from
`open-problems/finite-to-smooth-shadow-bridge.md` must be declared, e.g.:

```text
continuum scaling limit
finite-cover approximation
coarse-graining functor
category of models with comparison functor
```

**Current status:** not declared.

### Assumption A2: Independent target typing

The continuum WBE target must be typed independently of the finite witness:

```text
what is the continuum object?
what is the scaling family?
what parameter tends to a limit?
what equivalence relation is preserved?
```

**Current status:** only gestured at through neighboring WBE / Moses language.

### Assumption A3: Preserved capability or residue

The bridge must say what is preserved:

```text
is it the beta split?
the capability value R?
the metric-causal separation?
some obstruction or witness obligation?
```

**Current status:** not formally declared beyond the finite summary statistic.

### Assumption A4: Control family across scale

The bridge must supply:

- a positive control where the finite distinction survives refinement or scaling;
- a hostile control where refinement destroys it or reduces it to neighbor-owned
  continuum structure.

**Current status:** absent.

### Assumption A5: Non-imported geometry burden

The bridge must separate:

```text
what is earned from finite repo mathematics
vs
what is simply inherited from the external WBE theory.
```

**Current status:** unresolved.

## Positive Control

The strongest finite positive control currently available is only this:

```text
T186/T187/T195 show that at fixed finite n,
metric timing differences can change beta while causal order is held fixed.
```

This is a positive control for finite metric-causal separation.

It is **not yet** a positive control for a continuum bridge, because it does not
show preservation under refinement, scaling, or any declared bridge map.

## Negative / Hostile Controls

### Hostile Control H1: No declared bridge map

If no bridge type is declared, the continuum reading defaults to metaphor or
neighbor import, not a tested bridge.

This hostile control currently fires.

### Hostile Control H2: Absorbed finite value

T197 already showed that the current exact-family capability collapses to a
standard timing summary:

```text
R = T*
```

If the finite source object is already absorbed as a scheduling / flow summary,
then a continuum move that simply redescribes the same object in WBE language
does not create new repo-owned residue.

This hostile control currently fires.

### Hostile Control H3: No scaling-family evidence

The finite tests use isolated small fixtures and analytic formulas, not a
declared sequence of models approaching a continuum limit.

No evidence currently shows:

```text
n -> infinity behavior,
scale-family stability,
renormalized parameter control,
or preservation under refinement.
```

This hostile control currently fires.

## Absorber Pass

### Step 1: What the repo truly owns

The repo currently owns:

- finite metric-causal split witnesses;
- finite harmonic-mean timing summaries;
- narrowing and absorption discipline around those summaries.

### Step 2: What the external WBE theory owns

The external neighbor theory owns:

- the continuum metabolic-scaling program;
- the biological / physical interpretation of the 3/4 law;
- the asymptotic scaling-law context;
- the continuum transport reading.

### Step 3: Bridge audit

The current finite witness stack does not provide:

- a bridge map;
- a limit theorem;
- a refinement family;
- a proof that the finite residue survives scaling;
- a proof that the continuum interpretation is not just imported from the
  neighboring WBE theory.

So the current move from finite witness to continuum WBE reading is not yet a
typed bridge. It is still a suggestive analogy plus neighbor import.

## Results

### 1. The finite result does not yet bridge itself to continuum WBE

No accepted bridge type is currently declared.

No scaling-family control is currently supplied.

No preserved capability across a bridge is currently typed.

So the continuum move is not earned by the present finite artifacts.

### 2. The bridge is not merely narrow; it is presently unsupported

This is stronger than saying "the bridge works only on a limited class."

The issue is more basic:

```text
the bridge has not yet been constructed as a bridge.
```

### 3. What remains true

T196 does not kill the finite MTI / T186 / T195 content.

It kills the stronger inference:

```text
finite harmonic-mean witnesses already support a continuum WBE reading.
```

That inference is not currently justified.

## Verdict: killed

T196 returns `killed` for the current bridge attempt.

Repo-safe statement:

```text
The current finite MTI / Moses witness stack does not yet support a legitimate
continuum WBE bridge. No accepted bridge map, scaling family, preserved
capability statement, or refinement control has been supplied, and the finite
predictive object is already heavily absorbed as a standard timing summary.
```

## Falsification Conditions

This killed verdict should be revisited only if a future artifact supplies:

1. a declared bridge type from the finite-to-smooth bridge menu;
2. an independently typed continuum target;
3. a preserved capability or residue named before the example;
4. at least one positive refinement / scaling control and one hostile control;
5. a proof that the bridge preserves or weakens the finite residue rather than
   importing the continuum story from neighboring theory.

## Next Step

T196 narrows T199 sharply:

```text
the reviewer-facing packet should present a finite, narrowed metric-causal
separation result with explicit non-claims about continuum WBE support.
```
