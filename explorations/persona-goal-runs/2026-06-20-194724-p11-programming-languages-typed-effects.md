# P11 Run - Programming Languages Theorist Typed Forgetting Effects

- timestamp: 2026-06-20T19:47:24-05:00
- goal_id: P11
- selected_persona: Programming Languages Theorist
- selected_goal: Translate typed forgetting into type-and-effect judgments, including introduction, elimination, composition, preservation, and declassification rules.
- bounded_question: Does the current LossKernel / TF1 evidence earn a small type-and-effect reading, and if so, what residual obligation remains after that translation?

## Repo Context Read

- [`/C:/Users/joe/JB/Github Repos/time-as-finality/claims/TF1-typed-forgetting-attribution.md`](</C:/Users/joe/JB/Github Repos/time-as-finality/claims/TF1-typed-forgetting-attribution.md>)
- [`/C:/Users/joe/JB/Github Repos/time-as-finality/open-problems/loss-kernel-formalization.md`](</C:/Users/joe/JB/Github Repos/time-as-finality/open-problems/loss-kernel-formalization.md>)
- [`/C:/Users/joe/JB/Github Repos/time-as-finality/tests/T37-typed-transport-network.md`](</C:/Users/joe/JB/Github Repos/time-as-finality/tests/T37-typed-transport-network.md>)
- [`/C:/Users/joe/JB/Github Repos/time-as-finality/tests/T73-losskernel-composition.md`](</C:/Users/joe/JB/Github Repos/time-as-finality/tests/T73-losskernel-composition.md>)
- [`/C:/Users/joe/JB/Github Repos/time-as-finality/tests/T99-losskernel-quotient-separation.md`](</C:/Users/joe/JB/Github Repos/time-as-finality/tests/T99-losskernel-quotient-separation.md>)
- [`/C:/Users/joe/JB/Github Repos/time-as-finality/tests/T107-loss-relocation.md`](</C:/Users/joe/JB/Github Repos/time-as-finality/tests/T107-loss-relocation.md>)
- [`/C:/Users/joe/JB/Github Repos/time-as-finality/tests/T108-loss-relocation-prior-art.md`](</C:/Users/joe/JB/Github Repos/time-as-finality/tests/T108-loss-relocation-prior-art.md>)
- [`/C:/Users/joe/JB/Github Repos/time-as-finality/tests/T127-same-neighbor-data-losskernel-audit.md`](</C:/Users/joe/JB/Github Repos/time-as-finality/tests/T127-same-neighbor-data-losskernel-audit.md>)
- [`/C:/Users/joe/JB/Github Repos/time-as-finality/models/losskernel_quotient_separation.py`](</C:/Users/joe/JB/Github Repos/time-as-finality/models/losskernel_quotient_separation.py>)
- [`/C:/Users/joe/JB/Github Repos/time-as-finality/models/loss_relocation_prior_art.py`](</C:/Users/joe/JB/Github Repos/time-as-finality/models/loss_relocation_prior_art.py>)
- [`/C:/Users/joe/JB/Github Repos/time-as-finality/explorations/research-constellation-orchestrator-2026-06-20.md`](</C:/Users/joe/JB/Github Repos/time-as-finality/explorations/research-constellation-orchestrator-2026-06-20.md>)

## Work Performed

1. Read the current LossKernel floor in T73: powerset-union accumulation on the tested finite family.
2. Read the T99 quotient witness and extracted the actual typed payload shape from `TypedLossWitness`.
3. Read T107/T108/T127 to identify what a PL reading must preserve: absorbed-loss controls, source-lift dependence, and the same-neighbor-data prior-art gate.
4. Recast the current branch into a minimal effect discipline rather than a new semantics-first calculus.

## Smallest Honest PL Translation

The current repo does support a type-and-effect reading, but only a modest one.

Use a judgment of the form:

```text
Gamma |- f : Source -> Target ! epsilon
```

where `epsilon` is a loss effect attached to the morphism.

At the current evidence level, there are two different effect strengths:

```text
epsilon_label  = finite lost-label set
epsilon_witness = finite set of source-anchored witness obligations
```

T73 justifies `epsilon_label` as a union-composed annotation.
T99 says `epsilon_label` is too weak for attribution.
The only serious PL candidate is therefore:

```text
epsilon = witness-carrying loss effect
```

where each effect entry has the same shape already visible in
`models/losskernel_quotient_separation.py`:

```text
(label, witness_id, witness_type, source_anchor, resolves_obstruction, obstruction_id)
```

That is enough to state introduction, elimination, composition, preservation,
and declassification rules without claiming new theorem language.

## Candidate Judgment Forms

### 1. Loss typing

```text
Gamma |- f : S -> T ! epsilon
```

`f` is a definable information-losing morphism with a typed loss effect.

### 2. Target obstruction judgment

```text
Gamma |- obstructed(T, o)
```

The target exhibits named obstruction `o`.

### 3. Attribution judgment

```text
Gamma |- attributable(f, o)
```

The obstruction is admissibly attributable to the loss carried by `f`.

### 4. Reconstruction / debt judgment

```text
Gamma |- reconstruct(T) <= debt(epsilon, o)
```

Reconstruction from the target is blocked, ambiguous, or debt-bearing relative
to the effect and the named target obstruction.

## Effect Rules The Repo Currently Earns

### Introduction

Primitive projections introduce loss effects:

```text
forgotten_structure(f) = F
--------------------------------
Gamma |- f : S -> T ! effect(F)
```

This is the T73 floor only. It earns label introduction, not attribution.

T99 suggests the stronger introduction shape:

```text
derive_witnesses(S, T, f) = W
--------------------------------
Gamma |- f : S -> T ! witness_effect(W)
```

but only as a candidate rule. Canonical derivation is still open.

### Composition

For the tested T34/T37 family:

```text
Gamma |- f : A -> B ! epsilon1
Gamma |- g : B -> C ! epsilon2
--------------------------------
Gamma |- g o f : A -> C ! (epsilon1 union epsilon2)
```

This is exactly the T73 result. In PL terms, the current branch behaves like a
commutative idempotent writer effect on the tested fixtures.

### Elimination / Witness Use

Loss effects matter only when they discharge a named target obstruction:

```text
Gamma |- f : S -> T ! epsilon
Gamma |- obstructed(T, o)
Gamma |- epsilon contains witness w resolving o
-----------------------------------------------
Gamma |- attributable(f, o)
```

This is the T99 upgrade over label-only loss. Decorative labels do not
eliminate obstruction debt.

### Preservation

The honest preservation statement is weak but useful:

```text
If Gamma |- f : S -> T ! epsilon
and f composes inside the tested finite family,
then loss information is preserved by composition as accumulated effect data.
```

This is not preservation of reconstructability. It is preservation of the loss
account carried by the derivation.

Equivalently:

```text
well-typed composition preserves effect accumulation
```

not:

```text
well-typed composition preserves attribution novelty
```

### Declassification

The repo earns only a very narrow declassification rule:

```text
Gamma |- f : S -> T ! epsilon
Gamma |- epsilon exposes a source-derived witness resolving o
-------------------------------------------------------------
Gamma |- use(epsilon) to justify attributable(f, o)
```

This is not free declassification. It is audited witness reveal.

T127 makes the restriction explicit: the same effect-account package must be
compared against provenance, abstract interpretation, lenses, CSP explanation,
and rich effects. If those neighboring accounts can read the same witness data,
then the PL formulation is useful notation but not separation.

## Deliberate Failure Modes

The PL reading must preserve two failures already enforced by the repo.

### 1. Label-only failure

T99 forces:

```text
same endpoints
same composite map
same endpoint behavior
same naive lost-label set
different attribution verdicts
```

Therefore:

```text
label effect alone is not an elimination principle
```

### 2. Absorbed-loss failure

T107/T108 require a negative control where source variation is lost but target
judgments are invariant across lifts.

Therefore:

```text
non-empty effect =/= automatic reconstruction debt
```

The effect may be observationally irrelevant for the target judgment under
audit. Any calculus that forces debt in all non-empty cases would contradict
the absorbed-loss control.

## Result

Bounded-run verdict:

```text
Yes, the current LossKernel/TF1 branch can be translated into a small
type-and-effect discipline.
```

But the translation does not currently rescue novelty. It mostly clarifies the
state of play:

- T73 = writer-style accumulation law.
- T99 = witness-sensitive elimination rule.
- T107 = reconstruction-debt reading over source lifts.
- T108 = rich neighboring effect/provenance frameworks can still absorb the
  finite behavior.
- T127 = prior-art gate must be passed against same-neighbor-data packages.

So the strongest honest PL summary is:

```text
LossKernel currently behaves like a witness-carrying effect account for
projection-created obstruction attribution.
```

The residual theorem target is not "invent a calculus." It is:

```text
derive the witness effect canonically and show one same-neighbor-data
separation that rich effect systems do not already absorb.
```

## Proposed Next Action

The next bounded PL-facing artifact should not be a paper abstract. It should
be one strict executable audit:

1. Treat T127's neighbor package as the effect account baseline.
2. Attempt one same-neighbor-data pair where a witness-carrying effect changes
   the attribution verdict.
3. If the neighboring rich effect account can express the same distinction,
   demote LossKernel to disciplined notation over existing effect machinery.

An especially good hostile fixture remains the Git semantic-merge case proposed
in the constellation note, because it pressures operation-right loss rather than
just missing data.

## Claim-Status Posture

- No claim status changes.
- No roadmap, TESTS index, or claim-ledger updates.
- `TF1` remains an open formal target.
- The PL translation clarifies the branch; it does not promote it.
