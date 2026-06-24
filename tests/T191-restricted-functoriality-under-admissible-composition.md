# T191: Restricted Functoriality Under Admissible Composition

## Target Claims

- `FUNCTOR-OBL-TaF-001` (`open-problems/functor-obl-taf-001-coherent-section-functor.md`)
- `PO1-NCK-001` (`tests/T188-po1-nck-formal-claim-and-cap-ti-step4.md`)
- NCK formal definitions (`explorations/explorer-nck-formal-definitions-2026-06-22.md`)

## Origin

T190 showed that the currently stated covariant object

```text
F : States(Ext_S) -> FinSets
```

fails on finite base cases because extensions can kill coherent sections,
making `F(e)` partial or impossible in `FinSets`.

T191 asks the repair question that T190 left open:

```text
Is there a largest useful subcategory of admissible extensions on which the
covariant coherent-section action really is functorial?
```

If yes, name it and test closure. If no, say so cleanly and route the formalism
to the better repair.

## Formal Target Or Obligation

We test three candidate repairs:

1. **Covariant section-preserving subcategory**

   ```text
   F_cov : SectPres(Ext_S) -> FinSets
   ```

   where an arrow `e : S -> S'` is allowed only if every `sigma in F(S)`
   remains coherent in `S'`.

2. **Full contravariant repair**

   ```text
   F_op : States(Ext_S)^op -> FinSets
   ```

   sending stricter-state sections into looser-state sections by inclusion.

3. **Full covariant partial-map repair**

   ```text
   F_partial : States(Ext_S) -> ParSets
   ```

T191 is specifically about candidate (1): does the covariant `FinSets` version
become functorial on a well-defined restricted subcategory, and is that
subcategory useful enough for the NCK program?

## Setup / Fixtures

Use the same finite binary restriction systems as T190.

### Definition: Section-Preserving Extension

Call an extension `e : S -> S'` **section-preserving** iff

```text
for every sigma in F(S), sigma also lies in F(S').
```

Because `S'` is obtained by adding constraints to `S`, this condition is
equivalent to

```text
F(S') = F(S).
```

No new section can appear when constraints are added; the only way every old
section survives is that the coherent-section set stays unchanged.

### Fixture A: Redundant-Constraint Chain

From T190:

```text
S0: P_A = {+1}, P_B = {+1}
F(S0) = {(+1,+1)}
e1: add x_A = x_B
e2: add x_A = +1
```

Then:

```text
F(S0) = F(S1) = F(S2) = {(+1,+1)}
```

So `e1`, `e2`, and `e2 o e1` are all section-preserving.

### Fixture B: Selective-Survival Chain

From T190:

```text
S0: no constraints
F(S0) = {
  (+1,+1), (+1,-1), (-1,+1), (-1,-1)
}
e1: add x_A = x_B
e2: add x_A = +1
```

Then:

```text
F(S1) = {(+1,+1), (-1,-1)}
F(S2) = {(+1,+1)}
```

Neither `e1` nor `e2` is section-preserving.

### Fixture C: Total Obstruction Chain

From T190:

```text
S0: P_A = {+1}, P_B = {+1}
F(S0) = {(+1,+1)}
e_bad: add x_A = -x_B
F(S_bad) = empty
```

`e_bad` is not section-preserving.

## Positive Control

Fixture A is the positive control.

On section-preserving arrows:

```text
F_cov(id_S0) = id_{F(S0)}
F_cov(e1) = id_{ {(+1,+1)} }
F_cov(e2) = id_{ {(+1,+1)} }
F_cov(e2 o e1) = F_cov(e2) o F_cov(e1)
```

This verifies identity and composition on the redundant finite chain.

## Negative Control

Fixture B is the negative control for usefulness, and Fixture C is the negative
control for closure beyond the section-preserving class.

- Fixture B shows that once an extension removes even one coherent section,
  covariant `FinSets` functoriality disappears.
- Fixture C shows total obstruction is even further outside the class.

## Absorber Pass

The native absorber is standard solution-set semantics under monotone
constraint strengthening.

That absorber says:

1. The canonical unrestricted statement is contravariant:

   ```text
   F_op(e): F(S') -> F(S)
   ```

2. A covariant `FinSets` reading can survive only on a subcategory where
   constraint strengthening does not change the solution set.

3. Such a subcategory is mathematically legitimate but generically weak:
   solution-preserving arrows behave like identities on solution sets.

This absorber is decisive here. T191 is not discovering a new category law; it
is identifying which standard repair is honest and which one is too weak for
the repo's intended dynamics.

## Results

### 1. The section-preserving subcategory is closed under identity

For any state `S`,

```text
F(S) = F(S)
```

so `id_S` is section-preserving.

### 2. The section-preserving subcategory is closed under composition

Suppose

```text
e1 : S -> S'
e2 : S' -> S''
```

are both section-preserving. Then

```text
F(S) = F(S')
F(S') = F(S'')
```

hence

```text
F(S) = F(S'')
```

so `e2 o e1` is section-preserving.

Therefore `SectPres(Ext_S)` is a well-defined subcategory of the extension
category.

### 3. On this subcategory, the covariant `FinSets` action is functorial

If `e : S -> S'` is section-preserving, then each source section survives
unchanged, so the only honest action is

```text
F_cov(e)(sigma) = sigma.
```

Thus every arrow acts as the identity on the unchanged finite set `F(S)=F(S')`,
and identity/composition follow immediately.

### 4. This subcategory is too weak for NCK dynamics

On every arrow in `SectPres(Ext_S)`:

```text
|F(S')| = |F(S)|
```

So the key NCK quantities collapse:

```text
N = 0
K = 0
```

for pure extension steps inside the subcategory. No new coherent sections are
generated, and no sections are lost to obstruction. The only remaining dynamic
quantity would be an external cost annotation unrelated to section-count
change.

That makes the covariant `FinSets` repair formally valid but strategically
useless for the MTI / PO1-NCK program.

### 5. What survives as the useful repair

Two live repairs remain after the finite check:

1. **Useful full repair:** contravariant `FinSets` on the full extension class.
2. **Useful covariant repair:** partial-map or relation-valued semantics on the
   full extension class.

The section-preserving covariant subcategory is only a degenerate corner where
the functor law is true because nothing interesting happens to coherent
sections.

## Verdict: narrowed

T191 finds a genuine covariant `FinSets` subcategory:

```text
SectPres(Ext_S)
```

closed under identity and composition.

But the result is still **narrowed**, not promoted, because that subcategory is
too weak to support the intended NCK dynamics. It preserves functoriality only
by banning precisely the section-changing behavior that `N`, `K`, and
`lambda*(S)` are supposed to track.

## Falsification Conditions

This verdict should be revisited only if one of the following occurs:

1. A richer object-level notion of "extension" is defined where source
   sections can change while still giving a total covariant `FinSets` map.
2. The NCK program is reformulated so that section-preserving arrows are enough
   for the relevant dynamics.
3. A pointed-set or option-valued codomain is shown to preserve the needed
   covariant semantics without collapsing into partial-map language.

Without one of those repairs, the section-preserving subcategory should be
treated as a formal boundary result, not the final coherent-section semantics.

## Next Step

Use this result to route the next work:

```text
T192 should not assume the original covariant FinSets statement.
It should derive lambda*(S) only after choosing between:
  (a) contravariant coherent-section semantics, or
  (b) covariant partial-map semantics.
```
