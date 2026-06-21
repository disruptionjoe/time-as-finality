# Candidate North Star Low-Hanging Formal Patch Report v0.1

## Status

This is a patch report for the next Candidate North Star version.

It is not the next Candidate North Star draft.
It is not canon.
It does not promote Capability Projection as novel.
It does not draft new examples.

Purpose:

```text
Resolve low-hanging formal items that can strengthen the next version without
changing the settled posture.
```

Settled posture to preserve:

- global absorption comes first;
- `Cap` discipline comes before examples;
- finite pair tests are necessary but weak;
- canonical residue is the hard target;
- known physics induces capability objects, not the reverse;
- database examples are finite fixtures and absorbers, not novelty proof.

## Executive Recommendation

The next Candidate North Star version should add a compact formal patch near
the start of the Formal Core:

```text
For declared observer O, schema Sigma, resolution r, domain U, visible-state
equivalence ~=_X, task family T, horizon h, boundary B, capability object K,
and capability equivalence ~=_K, a projection pi : Y -> X is
capability-sufficient for Cap : Y -> K exactly when Cap factors through pi up
to ~=_K.

Equivalently, Cap is ~=_K-constant on every pi-fiber.
```

This patch should then introduce:

- exact capability-sufficiency / insufficiency definitions;
- the factorization iff fiber-constancy lemma;
- the minimal capability-preserving quotient;
- the trivial enrichment theorem;
- capability spread over projection fibers;
- `projection_underdescribed` as a demotion label;
- a sharper distinction between `canonical_residue` and `formal_residue`.

Do not expand the example inventory until these are in place.

## Patch 1: Exact Capability-Sufficiency Definition

Add a definition after the first `pi` and `Cap` declarations.

Suggested wording:

```text
Fix visible-state equivalence ~=_X on X and capability equivalence ~=_K on K.

A projection pi : Y -> X is capability-sufficient for Cap : Y -> K when there
exists Cbar : X -> K such that, for every admissible y in Y,

  Cap(y) ~=_K Cbar(pi(y)).

Equivalently, the observer-visible state determines the declared capability
object up to the declared capability equivalence.
```

Add the negative definition:

```text
pi is capability-insufficient for Cap when there exist admissible y1,y2 in Y
such that:

  pi(y1) ~=_X pi(y2)

but:

  Cap(y1) not ~=_K Cap(y2).
```

Implementation note:

Use `capability-sufficient`, `capability-insufficient`, and
`projection-sufficiency failure` as the default terms. Avoid
`capability-nonfaithful` unless a true functorial faithfulness condition is
being used.

## Patch 2: Factorization Iff Fiber-Constancy Lemma

Add the lemma immediately after the definition above.

Suggested wording:

```text
Lemma: Cap factors through pi up to ~=_K iff Cap is ~=_K-constant on every
pi-fiber.

Proof sketch:
If Cap(y) ~=_K Cbar(pi(y)), then any y1,y2 with pi(y1) ~=_X pi(y2) have
equivalent Cap-values through the same visible state. Conversely, if Cap is
constant on each pi-fiber, define Cbar(x) to be the common ~=_K-class of
Cap(y) for any y with pi(y)=x. Fiber-constancy makes this well-defined.
```

Guardrail:

This lemma is not novelty evidence. It is quotient/descent bookkeeping. Its
value is that it forces every witness to say exactly which projection,
capability object, and equivalence relation are being tested.

## Patch 3: Minimal Capability-Preserving Quotient

Add this after the lemma as the positive target for formal cleanup.

Suggested wording:

```text
Define the capability equivalence on source states:

  y1 ~_Cap y2 iff Cap(y1) ~=_K Cap(y2).

Then Y / ~_Cap is the coarsest quotient of Y that preserves the declared
capability object. A projection pi is capability-sufficient exactly when it
does not identify source states from distinct ~_Cap classes:

  ker(pi) subset ker(Cap).
```

Interpretation:

```text
The honest mathematical target is not another same-pi / different-Cap pair.
The target is the minimal capability-preserving quotient, or a domain-native
approximation to it.
```

Use in review:

- If the native field already has this quotient, record absorption.
- If the quotient is merely restated in new language, record translation
  residue at most.
- If a cross-domain family of such quotients or enrichments appears, that is a
  stronger candidate for formal or canonical residue.

## Patch 4: Trivial Enrichment Theorem

Add this in the absorption section, preferably under State-Enrichment
Absorption.

Suggested wording:

```text
Trivial enrichment theorem:

For any pi : Y -> X and Cap : Y -> K, define:

  pi'(y) = (pi(y), Cap(y)) : Y -> X x K.

Then Cap factors through pi'.
```

Consequence:

```text
Every projection-sufficiency failure can be repaired by enriching the visible
state with the capability object itself. Therefore the research question is
not whether enrichment can restore factorization. It is whether the enrichment
is domain-natural, minimal, canonical, operationally available, or already
standard in the neighboring theory.
```

Residue effect:

If a standard native enrichment restores factorization, demote the witness to
absorption, translation residue, or heuristic residue. Do not call it formal
residue.

## Patch 5: Capability Spread Over Projection Fibers

Add this after the finite pair test.

Suggested wording:

```text
For a visible state x, define the capability spread over its source fiber:

  Spread_Cap(x) = { Cap(y) | y in pi^{-1}(x) } / ~=_K.

Then Cap factors through pi iff Spread_Cap(x) is a singleton for every
visible state x.
```

Clarification:

```text
The projection fiber pi^{-1}(x) is not itself the capability. The audit object
is the spread of capability values across that fiber.
```

Optional finite-audit summaries:

```text
ambiguity_Cap(x) = |Spread_Cap(x)|
diameter_Cap(x) = diameter(Spread_Cap(x)) when K has metric/order structure
```

Use:

- finite pair witnesses show non-singleton spread;
- preservation controls show singleton spread;
- probabilistic or approximate domains may measure spread rather than demand
  exact equality.

## Patch 6: Add `projection_underdescribed`

Recommendation:

Add the label.

Definition:

```text
projection_underdescribed
```

Use it when the chosen projection omits native state data that the domain
standardly treats as part of the relevant state, interface, or access profile.

Distinguish from:

```text
same_visible_state_underspecified
```

Use `same_visible_state_underspecified` when equality of visible state has not
been indexed well enough.

Use `projection_underdescribed` when equality is indexed, but the projection
itself has intentionally left out obvious domain-native data.

Examples:

- repo tree without commit DAG when history is task-relevant;
- database snapshot without transaction log for audit or rollback capability;
- top-k result without embedding model, index state, filters, and search
  budget;
- local physical patch without access profile, boundary conditions, or allowed
  operation class;
- reduced quantum state without the operation/access regime that determines
  which resources are available.

Disposition:

Most `projection_underdescribed` witnesses should be demoted unless the report
can show why the impoverished projection is nevertheless the domain-natural
observer interface.

## Patch 7: Sharpen `canonical_residue` Versus `formal_residue`

Current issue:

The ladder is right, but `canonical_residue` and `formal_residue` are too easy
to blur.

Recommended split:

```text
formal_residue
```

Use when a typed distinction survives immediate prior-art absorption as a
clean formal object, lemma, theorem, quotient, metric, or audit criterion, but
its canonicity across domains is not established.

Required:

- `K` is typed;
- `~=_K` is declared;
- the projection is operationally meaningful;
- the witness survives trivial same-field enrichment;
- the native theory does not already contain the same result in equivalent
  form.

Not required:

- cross-domain inevitability;
- uniqueness;
- canonical enrichment family;
- physics-bearing consequence.

```text
canonical_residue
```

Use only when the surviving object appears forced rather than chosen.

Required:

- all `formal_residue` requirements;
- `Cap` is domain-natural, operationally forced, or uniquely selected by the
  task/interface;
- the relevant quotient or enrichment is minimal or otherwise canonical in
  the native field;
- the result survives both state-enrichment absorption and native-theory
  absorption;
- the same structure or enrichment pattern recurs across mature domains, or
  reveals an unavoidable tradeoff across observer, task, horizon, and resource
  boundary.

Short rule:

```text
formal_residue = a surviving typed formal distinction.
canonical_residue = a surviving typed formal distinction whose capability
object, quotient, or enrichment is forced rather than gerrymandered.
```

Default:

Assume translation or heuristic residue unless the report explicitly satisfies
the stricter requirements.

## Suggested Placement In Next Version

Recommended order:

1. Executive posture: keep global absorption first.
2. Formal core: add exact capability-sufficiency definition.
3. Lemma: factorization iff fiber-constancy.
4. Minimal quotient and capability spread.
5. Capability type gate.
6. Finite pair test: necessary but weak.
7. Absorption: add trivial enrichment theorem.
8. Failure labels: add `projection_underdescribed`.
9. Residue ladder: sharpen `formal_residue` and `canonical_residue`.
10. Examples and physics only after the formal and `Cap` gates.

## Compact Reviewer Checklist

Use this before accepting any future witness:

```text
Y declared?
X declared?
pi declared?
visible equivalence ~=_X declared?
K typed?
Cap declared before the witness?
capability equivalence ~=_K declared?
projection operationally meaningful?
same-visible-state context fixed?
projection underdescribed?
Cap domain-natural or gerrymandered?
fiber spread singleton or non-singleton?
minimal capability-preserving quotient identified?
trivial/native enrichment tested?
native-theory absorption tested?
residue label justified?
```

Physics addendum:

```text
known physics -> induced Cap -> projection sufficiency audit
```

Reject or demote any physics-facing section that reverses this direction.

## Bottom Line

The next Candidate North Star version should make the hard formal spine
unmissable:

```text
Capability Projection is projection sufficiency for typed capability objects.
Non-factorization is old. The useful work is declaring Cap, checking
fiber-constancy, identifying the minimal capability-preserving quotient,
testing natural enrichments and native absorbers, and recording whether any
formal or canonical residue remains.
```

