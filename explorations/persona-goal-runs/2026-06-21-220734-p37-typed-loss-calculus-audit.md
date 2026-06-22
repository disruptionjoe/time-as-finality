# P37 Run - Type-System Designer

- timestamp: 2026-06-21T22:07:34-05:00
- goal_id: P37
- selected_persona: Type-System Designer
- selected_goal: Write a typed-loss calculus with syntax, judgments, preservation, progress or deliberate failure, and composition rules.
- bounded_question: What is the smallest typed-loss calculus the repo can state honestly after T73, T99, T107, and T127?
- posture: bounded exploratory run only; no claim-status update, roadmap change, or ledger edit.

## Repo Context Read

- `explorations/persona-future-run-goals-2026-06-20.md`
- `Vision - North Star.md`
- `Method - Research Program Guidelines.md`
- `Lead Research Line - Time as Finality.md`
- `claims/TF1-typed-forgetting-attribution.md`
- `tests/T73-losskernel-composition.md`
- `models/losskernel_composition.py`
- `tests/T99-losskernel-quotient-separation.md`
- `models/losskernel_quotient_separation.py`
- `tests/T107-loss-relocation.md`
- `models/loss_relocation.py`
- `tests/T127-same-neighbor-data-losskernel-audit.md`
- `models/same_neighbor_data_losskernel_audit.py`
- `open-problems/loss-kernel-witness-obligation-normal-form.md`
- `models/transport_network.py`

## Work Performed

1. Selected the first queued persona goal, `P37 - Type-System Designer`.
2. Read the existing typed-loss line in the repo from the current union-style
   `LossKernel` law through the quotient, relocation, and same-neighbor-data
   audits.
3. Treated the request as a hostile typing exercise rather than a promotion
   opportunity: only keep rules already supported by finite witnesses.
4. Asked which parts of a true calculus are earned now:
   - syntax;
   - typing judgments;
   - preservation/composition;
   - progress;
   - explicit failure or abstention forms.

## Result

The repo does not yet support a fully semantic typed-loss calculus with a
strong progress theorem.

It does support a smaller and defensible object:

```text
a two-level typed-loss audit calculus
```

Level 1 types morphisms and accumulated named loss.
Level 2 types target-side witness obligations induced by source-fiber
dependence for a declared judgment family.

This is enough to make "typed loss" more disciplined than free labels, but not
enough to claim a new general semantics or prior-art-separated theorem.

## Smallest Honest Calculus

### 1. Syntax

Use the existing finite transport language:

```text
Layer A, B, C
primitive transport e : A -> B
identity id_A : A -> A
composite g o f : A -> C
judgment family J on target-visible states
```

Annotate each primitive transport with:

```text
forgotten_structure(e) : finite set of structure names
preserved_structure(e) : finite set of preserved dimensions
```

For a composite path `p`, define:

```text
LK_label(p) = union of forgotten_structure along p
```

For a declared judgment family `J`, define a derived obligation object:

```text
WO(p, J) = source-fiber witness obligation induced by lift dependence
```

with the current safe outcome classes:

```text
live_debt
stable_constraint
absorbed_freedom
```

### 2. Typing Judgments

The smallest useful judgments are:

```text
Gamma |- e : A => B [L]
Gamma |- p : A => B [L]
Gamma ; J |- p => debt
Gamma ; J |- p => constraint
Gamma ; J |- p => absorbed
Gamma ; J |- p => abstain
```

Read them as:

- `A => B [L]`: a typed transport from `A` to `B` carrying loss annotation `L`.
- `debt`: target judgment remains source-lift dependent.
- `constraint`: all source lifts uniformly forbid the judgment.
- `absorbed`: all source lifts give the same invariant verdict.
- `abstain`: the object is label-only, endpoint-invalid, or neighbor-absorbed.

### 3. Formation Rules

Safe formation rules are:

```text
id_A : A => A [empty]

e : A => B [forgotten_structure(e)]

if f : A => B [L1] and g : B => C [L2]
then g o f : A => C [L1 union L2]
```

This is exactly the T73 monoid-valued annotation law. No stronger categorical
reading is earned here.

### 4. Judgment Rules For Obligations

For a declared target judgment family `J`, inspect the source preimage fiber of
the target-visible case.

Let `Verd(p, J)` be the set of source-lift verdicts.

Then the current finite rule is:

```text
Verd(p, J) = {True, False}  =>  Gamma ; J |- p => debt
Verd(p, J) = {False}        =>  Gamma ; J |- p => constraint
Verd(p, J) = {True}         =>  Gamma ; J |- p => absorbed
```

This is the T107 rule. It is source-anchored and derived from finite fibers,
not attached as prose metadata.

### 5. Deliberate Failure / Abstention Rules

The repo now forces explicit non-progress cases.

```text
label-only kernel            => abstain
same-neighbor-data collapse  => abstain
endpoint-difference control  => abstain
path-metadata-only split     => abstain
absorbed-loss control        => absorbed, not debt
```

This is the main lesson from T99 and T127: not every non-empty loss annotation
earns a live typed-loss verdict.

## Preservation And Progress

### What is preserved

The following are currently supported:

- Well-formed transport typing is preserved by identity and composition.
- Label accumulation is associative up to finite-set union on the tested
  family.
- Non-empty label loss can remain stable under further composition.
- Source-fiber derivation can preserve the distinction between debt,
  constraint, and absorbed cases for a fixed declared judgment family.

### What is not preserved

The following stronger statements are not earned:

- a canonical semantic `WO(g o f, J)` composition theorem;
- prior-art-separated preservation of typed-loss verdicts under quotienting;
- a theorem that non-empty `LK_label` implies a live witness obligation;
- a theorem that every typed-loss judgment survives same-neighbor-data audit.

### Progress status

An ordinary progress theorem would be false in the current finite family.

The honest replacement is:

```text
well-typed loss annotations do not guarantee live debt;
they may terminate in debt, constraint, absorbed, or abstain
```

So the calculus is better read as a typed audit calculus with explicit
deliberate failure modes, not as an always-progressing reduction system.

## Main Decision

If P37 were promoted later, the right object to promote is not:

```text
LossKernel as a new semantic effect system
```

It is the weaker object:

```text
typed-loss audit calculus =
  compositional label accumulation
  + source-derived witness-obligation verdicts
  + explicit abstention / absorbed forms
```

This earns the word `typed` in a modest sense:

- transports are typed;
- loss annotations are typed by source/target morphisms;
- target judgments are typed by declared judgment families;
- failure modes are typed rather than hidden.

It does not yet earn:

- a strong semantics for composition of witness obligations;
- a general preservation/progress theorem;
- a novelty claim beyond disciplined integration vocabulary.

## Minimal Calculus Skeleton

```text
Types:
  A, B, C                     layers / restriction systems
  L                           finite loss-label object
  J                           target judgment family
  K                           obligation verdict in {debt,constraint,absorbed,abstain}

Terms:
  id_A
  e
  g o f

Typing:
  Gamma |- f : A => B [L]
  Gamma ; J |- f => K

Composition:
  LK_label(id_A) = empty
  LK_label(g o f) = LK_label(f) union LK_label(g)

Judgment derivation:
  mixed source lifts      => debt
  all forbidden lifts     => constraint
  all allowed lifts       => absorbed
  quotient-invalid/label-only/neighbor-absorbed => abstain
```

## Blockers

1. `WO(f, J)` does not yet have a proved composition law comparable to the T73
   union rule.
2. T127 blocks any default assumption that the calculus yields a
   prior-art-separated theorem target.
3. The strongest surviving object may still collapse into a canonical normal
   form for source-derived witness obligations rather than an independent
   calculus family.

## Proposed Next Action

If this branch is continued later, the most honest next bounded step is:

1. choose one T107 finite family;
2. define `WO(f, J)` canonically from its source-fiber lift table;
3. test whether `WO(g o f, J)` has any nontrivial composition law at all; and
4. demote the calculus to integration vocabulary immediately if the only law
   left is label union plus neighbor-visible abstention.

## Claim-Status Posture

- No claim status changes recommended.
- No ROADMAP or TESTS changes recommended.
- No CLAIM-LEDGER update recommended.
- Best current posture: typed-loss audit calculus, not promoted theorem
  calculus.
