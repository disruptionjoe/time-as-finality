# T190: Coherent Section Functor Base Cases

## Target Claims

- `FUNCTOR-OBL-TaF-001` (`open-problems/functor-obl-taf-001-coherent-section-functor.md`)
- `PO1-NCK-001` (`tests/T188-po1-nck-formal-claim-and-cap-ti-step4.md`)
- NCK formal definitions (`explorations/explorer-nck-formal-definitions-2026-06-22.md`)

## Origin

The MTI / Cap_TI packet introduced the coherent-section object

```text
F : States(Ext_S) -> FinSets
```

and treated it as the formal base for `N`, `C`, and `K`. That move is blocked
until the morphism action of `F` is verified on finite base cases. T190 is the
first Wave 1 test in the ten-test fanout and asks the smallest possible
question:

```text
Does the currently stated covariant coherent-section construction define a
genuine FinSets functor on finite extension chains?
```

## Formal Target Or Obligation

The open problem states:

```text
F(S) = set of globally coherent sections at state S
F(e): F(S) -> F(S')
```

for an admissible extension `e : S -> S'` that adds new constraints. T190
tests the finite base cases needed for functoriality:

1. Identity: `F(id_S) = id_{F(S)}`
2. Composition on non-obstructed chains:
   `F(e2 o e1) = F(e2) o F(e1)`
3. Composition through obstruction

The test also checks a stricter precondition that the open problem leaves
implicit:

```text
For F to land in FinSets, F(e) must be a total function on every source section.
```

## Setup / Fixtures

Use finite binary same/different restriction systems in the style of T28/T39.
Write `F(S)` as the set of globally coherent sections satisfying all current
constraints.

### Fixture A: Redundant-Constraint Singleton Chain

Let

```text
S0: P_A = {+1}, P_B = {+1}
```

Then

```text
F(S0) = {(+1,+1)}
```

Define:

```text
e1: add x_A = x_B          (redundant)
e2: add x_A = +1           (redundant)
```

Then

```text
F(S1) = {(+1,+1)}
F(S2) = {(+1,+1)}
```

and the candidate morphism action is total and unique at every step.

### Fixture B: Selective-Survival Chain

Let

```text
S0: no unary predicates, no pair constraints
```

Then

```text
F(S0) = {
  (+1,+1), (+1,-1), (-1,+1), (-1,-1)
}
```

Define:

```text
e1: add x_A = x_B
e2: add x_A = +1
```

Then

```text
F(S1) = {(+1,+1), (-1,-1)}
F(S2) = {(+1,+1)}
```

The problem is immediate:

- `(+1,-1)` and `(-1,+1)` do not extend through `e1`
- `(-1,-1)` extends through `e1` but not through `e2`

So the stated covariant map `F(e): F(S) -> F(S')` is not total.

### Fixture C: Total Obstruction Extension

Let

```text
S0: P_A = {+1}, P_B = {+1}
F(S0) = {(+1,+1)}
```

Define:

```text
e_bad: add x_A = -x_B
```

Then

```text
F(S_bad) = empty
```

There is no total function from a singleton set to the empty set in `FinSets`.
So the stated covariant action fails before composition is even asked.

## Positive Control

Fixture A is the positive control. The current covariant statement works when
every extension is redundant relative to the unique existing coherent section.

Explicitly:

```text
F(id_S0) = id_{ {(+1,+1)} }
F(e1) and F(e2) are both the identity on the singleton
F(e2 o e1) = F(e2) o F(e1)
```

This confirms that no contradiction appears in the trivial total case.

## Negative Control

Fixture C is the negative control. A single new incompatible constraint sends a
nonempty coherent-section set to the empty set. The currently stated covariant
`FinSets` morphism cannot exist in that case.

This is stronger than a mere composition failure: it is a typing failure of the
codomain.

## Absorber Pass

The strongest native absorber is ordinary category-theoretic treatment of
solution sets under constraint addition.

Under that absorber:

1. **Canonical contravariant version:** if `e : S -> S'` means "`S'` has all
   the constraints of `S`, plus more", then there is always a total inclusion

   ```text
   F_op(e): F(S') -> F(S)
   ```

   because every solution of the stricter state is automatically a solution of
   the looser state.

2. **Canonical covariant salvage:** if one insists on the direction
   `S -> S'`, the natural codomain is not `FinSets` but a category of partial
   maps, relations, or subset-valued transitions.

3. **What T41 already rules out:** T41 shows PO1 itself is not a functor on the
   D1 morphism category. T190 is a different question. It shows that the
   currently stated coherent-section action also fails as a covariant `FinSets`
   functor unless the morphism class is severely restricted.

So the absorber verdict is:

```text
The repo does not have a novel new categorical obstruction here.
The base issue is standard: feasible-section sets under added constraints are
canonically contravariant, not covariant, unless one changes codomain or
restricts morphisms.
```

## Results

### 1. Identity passes in the trivial total case

For every finite state `S`, `F(id_S) = id_{F(S)}` is valid.

### 2. The current covariant `FinSets` statement fails as soon as extensions can kill sections

Fixture B shows partiality:

```text
F(e1) is undefined on two source sections
F(e2) is undefined on one section of F(S1)
```

Therefore the currently stated map is not a total function `F(S) -> F(S')`.

### 3. Total obstruction makes the codomain failure explicit

Fixture C shows:

```text
F(S0) = singleton
F(S_bad) = empty
```

No function exists from `1` to `0` in `FinSets`. The statement fails before
composition is considered.

### 4. What survives

Two narrower statements survive the finite base-case pass:

1. **Contravariant strict-solution functor**

   ```text
   F_op : States(Ext_S)^op -> FinSets
   ```

   with `F_op(e)` the inclusion of stricter coherent sections into looser ones.

2. **Covariant partial-map version**

   ```text
   F_partial : States(Ext_S) -> ParSets
   ```

   where each section is mapped only when the new constraint admits an
   extension.

T190 does not prove either version in general, but it identifies them as the
correct finite repairs and shows the original covariant `FinSets` typing is too
strong.

## Verdict: narrowed

The finite base cases do **not** verify the current statement

```text
F : States(Ext_S) -> FinSets
```

as a covariant functor on admissible extensions.

What survives is narrower:

- identity is fine;
- the covariant action works only on a restricted class where every extension
  preserves all source sections;
- the canonical unrestricted reading is contravariant or partial-map valued.

## Falsification Conditions

T190 should be reconsidered only if one of the following is supplied:

1. A revised definition of morphisms in `States(Ext_S)` under which every
   admissible extension preserves all source coherent sections.
2. A codomain change from `FinSets` to partial maps / relations / pointed sets.
3. A proof that the intended state transition is actually the opposite
   direction, making the coherent-section action contravariant.

Without one of those repairs, the current covariant statement should not be
used as if verified.

## Next Step

Run `T191` as the repair test:

```text
Identify the largest useful subcategory on which the coherent-section action is
actually functorial, or rewrite the formalism contravariantly.
```
