# Technical Report: Capability-Spread Transfer Lemma v0.1

## Status

Internal method-hardening artifact.

This report does not promote a claim, change the North Star, update the
roadmap, update the claim ledger, register a numbered test, create an
executable model, or assert new physics. It names the exact piece of the
shadow-protection program that currently transfers across domains:

```text
visible fiber -> capability spread -> native comparison -> absorber or repair
```

The purpose is to keep the dormant cross-domain theorem target honest. The
repo has a reusable audit spine. It does not yet have a nontrivial
cross-domain physics, geometry, or capability theorem.

## Inputs

This note consolidates the method boundary established by:

- `TECHNICAL-REPORT-native-comparison-regime-appendix-v0.1.md`
- `TECHNICAL-REPORT-two-domain-native-comparison-shadow-audit-v0.1.md`
- `TECHNICAL-REPORT-access-profile-alignment-lemma-v0.1.md`
- `TECHNICAL-REPORT-process-semantics-absorption-comparison-v0.1.md`
- `open-problems/cross-domain-shadow-protection-theorem.md`
- `workflows/templates/north-star-shadow-audit.template.md`

It also respects the causal-access absorber posture from T153/T402: changed
access data, changed causal diamonds, ordinary joint-state completion, and
domain-native semantic completion are not residue.

## Problem

The North Star theorem target asks whether a single observer-shadow theorem can
survive across mature domains.

The recent method artifacts show a weaker result:

```text
projection sufficiency can be audited in many domains by checking whether the
native capability spread over visible fibers collapses under the declared
native comparison
```

That is useful, but it risks being overstated. In its bare form it is a
transportable review rule, not a new theorem about physics or geometry.

This report states the transferable lemma and the stop line.

## Setup

For a domain `D`, declare:

```text
Y_D       source structure
A_D       admissible source states, A_D subset Y_D
O_D       observer or access profile
pi_D      visible projection, pi_D : A_D -> X_D
~=_X,D    visible equivalence on X_D
Cap_D     capability object, Cap_D : A_D -> K_D
R_K,D     native comparison on K_D
```

The access-profile alignment rule applies:

```text
pi_D and Cap_D must be indexed to the same access profile O_D
unless the run explicitly declares a cross-profile insufficiency question.
```

For a visible class `[x]`, define the raw capability spread:

```text
Spread_D([x]) =
  { Cap_D(y) | y in A_D and pi_D(y) ~=_X,D x }
```

The raw spread is not yet a verdict. It must be interpreted by `R_K,D`.

## Exact Equivalence-Valued Lemma

When `R_K,D` is an equivalence relation `~=_K,D`, define the quotient map:

```text
q_K,D : K_D -> K_D / ~=_K,D
```

Then the following are equivalent:

```text
1. q_K,D o Cap_D factors through the visible quotient A_D / ~=_X,D.

2. For all y1, y2 in A_D:
     pi_D(y1) ~=_X,D pi_D(y2)
       => Cap_D(y1) ~=_K,D Cap_D(y2)

3. For every visible class [x], q_K,D(Spread_D([x])) is a singleton.
```

This is the exact capability-spread lemma. It is domain-independent because
it is just quotient/fiber bookkeeping.

## Reflected-Regime Lemma

Many useful `K_D` objects are not equality-valued. They become comparable only
after the domain supplies a native reflection, summary, threshold, preorder
collapse, semantic quotient, or test-language quotient.

If a domain supplies a declared comparison map:

```text
r_D : K_D -> Kbar_D
```

where equality in `Kbar_D` represents the accepted native comparison for the
run, then the exact lemma applies to:

```text
r_D o Cap_D
```

The transferable statement becomes:

```text
r_D o Cap_D factors through pi_D
iff
r_D(Spread_D([x])) is singleton for every visible class [x].
```

Examples:

| Native regime | Possible `r_D` |
| --- | --- |
| Preorder/resource | quotient by mutual convertibility, complete monotone vector, or declared downset/upset reflection |
| Metric/tolerance | epsilon-cell, native error envelope, or certified bounded-spread verdict |
| Decision/risk | optimal-policy class, bounded regret class, or Blackwell/Le Cam comparison |
| Probabilistic/statistical | distributional equivalence, coupling class, or declared distance threshold |
| Process semantics | trace, failure, readiness, testing, bisimulation, or Nerode quotient |
| Causal access | matched causal past/access diamond/domain-of-dependence verdict under declared access data |

The map `r_D` must be declared before selecting the witness pair. Otherwise the
run is changing the capability comparison after seeing the evidence.

## Bounded-Spread Variant

Some regimes do not naturally collapse to exact equality. For a native
distance, divergence, loss gap, or error envelope, declare:

```text
Delta_D : K_D x K_D -> nonnegative values
epsilon_D
```

Then projection is sufficient only in the approximate sense:

```text
diameter_D(Spread_D([x])) <= epsilon_D
```

for every visible class `[x]`.

This variant is not the same theorem as exact factorization. It is a
predeclared bounded-spread audit. The tolerance must come from the domain's
normal criterion, not from the witness pair.

## What Transfers

The following spine transfers:

```text
1. declare access-aligned pi, Cap, X, K, and R_K;
2. compute or describe visible fibers;
3. inspect the native capability spread over each relevant fiber;
4. apply the native comparison, reflection, or tolerance;
5. grant the neighboring field its normal state, operations, equivalences,
   thresholds, and absorber theorems;
6. identify the smallest domain-natural enrichment that restores sufficiency,
   or record the surviving spread honestly.
```

This is enough to make reports reviewable across domains.

It is not enough to promote residue.

## What Does Not Transfer Yet

The following do not transfer from this lemma alone:

- a shared capability object across domains;
- a shared physical interpretation of `Cap`;
- a geometry theorem;
- a claim that observer shadows explain physics;
- novelty in ANN, QRT, process semantics, causal access, or resource theory;
- a canonical minimal enrichment theorem;
- a proof that two domain-specific reflections are instances of one larger
  mathematical structure.

The current cross-domain result is therefore:

```text
same audit form, not same theorem content
```

## Relationship To Native Absorbers

The lemma should be used to make absorbers stronger, not weaker.

If a native absorber supplies a standard enrichment:

```text
X_D -> X_D'
```

such that `Cap_D` collapses over the enriched visible fibers, then the correct
result is usually:

```text
projection underdescribed
translation residue
heuristic residue
redundant or demoted
```

not:

```text
canonical residue
new physics
geometry theorem
```

Examples already established by nearby artifacts:

- ANN retrieval: index/workload/resource state completes the projection.
- QRT: align the access profile and declare the free-operation frame.
- Process semantics: choose the native semantic quotient for the declared
  future-test task.
- Lorentzian causal access: match causal relation, world tube, access diamond,
  and domain-of-dependence inputs before scoring finality differences.
- Region-indexed boundary screens: avoid comparing `pi_R` to a capability that
  silently requires `R:B` access unless the cross-profile question is declared.

## Minimal Enrichment Discipline

The trivial repair:

```text
pi'(y) = (pi_D(y), Cap_D(y))
```

always restores sufficiency. It never establishes residue by itself.

The only useful repair is a domain-natural enrichment that is:

- smaller than appending `Cap_D` directly;
- legitimate in the neighboring field;
- declared before the witness pair is chosen;
- accessible to the declared observer or explicitly marked as a larger access
  profile;
- stable under the domain's normal equivalences, thresholds, and operations.

If the repair is exactly the neighboring field's standard state completion,
the result is absorption, not promotion.

## Reactivation Condition For The Dormant Theorem

`open-problems/cross-domain-shadow-protection-theorem.md` should stay dormant
until at least one stronger object appears.

Reactivation would require one of:

1. A canonical enrichment family that is not just `pi' = (pi, Cap)` and works
   in at least two mature domains under their native equivalences.
2. A cross-domain reflection theorem showing that two domain-specific
   `r_D` maps are instances of a shared structure, with nontrivial content.
3. An executable pair of domain artifacts where the same proof spine survives
   native state completion and native theorem absorption in both domains.
4. A formal minimality theorem for a native capability-kernel quotient that is
   useful outside a single domain.

Without one of those, the theorem target remains a method scaffold.

## Intake Rule For Future Witnesses

Before a future witness claims any residue, it should include this row:

```text
Capability-spread transfer check:
  visible fiber:
  raw spread:
  native comparison/reflection/tolerance:
  collapsed after native absorber? yes/no
  minimal enrichment:
  residue label:
```

Failure to fill the row is not fatal for exploratory notes, but it blocks
promotion.

## Verdict

Projection-sufficient?

```text
Exactly when the native reflected or compared capability spread collapses over
visible fibers.
```

Projection-insufficient?

```text
Only after pi, Cap, access profile, visible equivalence, native comparison,
and absorber state are all declared.
```

Minimal enrichment or repair:

```text
domain-natural state, semantic quotient, access-profile alignment, resource
frame, causal-access data, or native threshold completion
```

Residue label:

```text
method hardening / translation residue unless a stronger domain-natural
minimality or cross-domain reflection theorem is later earned
```

## Short Verdict

The capability-spread lemma is the transferable core currently earned by the
cross-domain shadow-protection work. It is useful because it forces future
witnesses to declare access, comparison, spread, absorber, and repair before
residue language. It is not yet a nontrivial cross-domain theorem.
