# T192: `lambda*(S)` Derivation From PO1 Obstruction Dynamics

## Target Claims

- `PO1-NCK-001` (`tests/T188-po1-nck-formal-claim-and-cap-ti-step4.md`)
- `FUNCTOR-OBL-TaF-001` repair boundary (`tests/T190-coherent-section-functor-base-cases.md`, `tests/T191-restricted-functoriality-under-admissible-composition.md`)
- `lambda*(S)` dynamics claim (`tests/T185-lambda-star-msy-absorption-test.md`)

## Origin

T188 proposed the strong candidate claim:

```text
lambda*(S) is a consequence of PO1.
```

T190 and T191 then forced a semantic repair:

- the original covariant `FinSets` functor fails;
- the covariant `FinSets` rescue survives only on a section-preserving corner
  where `N = K = 0`.

T192 asks what survives after taking those two repairs seriously:

```text
Can lambda*(S) still be derived from PO1 obstruction dynamics, and if so, in
what exact sense?
```

## Formal Target Or Obligation

We test the strongest still-honest version of `PO1-NCK-001`.

### Candidate strong statement

```text
PO1 alone determines lambda*(S).
```

### Candidate narrowed statement

```text
PO1 naturally determines the obstruction-risk term K(lambda,S), but lambda*(S)
 requires additional non-PO1 structure specifying proposal/growth dynamics N
 and reconciliation cost C.
```

T192 must decide between these.

## Semantic Choice

T190/T191 leave two live repairs for the coherent-section object:

1. contravariant `FinSets`
2. covariant partial-map / relation-valued semantics

For `lambda*(S)` we choose the second, because the first immediately collapses
the intended growth reading:

```text
under contravariant FinSets, stricter states only lose or preserve sections;
they do not generate forward growth in |F(S)|.
```

So the only semantics that can support a forward issuance dynamics is:

```text
F_partial : States(Ext_S) -> ParSets
```

where an extension attempt may:

- preserve a coherent section,
- kill a coherent section,
- or introduce new compatible section structure through a proposal process.

## Setup / Formal Model

Let `S` be a current source-constraint state and let extension proposals arrive
at rate `lambda`.

### PO1-native term

For a proposed extension `e : S -> S'`, define:

```text
p_obs(S) = Pr[e creates a PO1 gluing obstruction for a currently coherent section]
```

Then the expected obstruction load is

```text
K(lambda,S) = lambda * |F(S)| * p_obs(S)
```

This is the cleanest survivor from T188: PO1 types what counts as an
obstruction event.

### Non-PO1 terms

To get an interior optimum, the dynamics also requires:

```text
N(lambda,S) = expected coherent gain rate from proposed extensions
C(lambda,S) = reconciliation / congestion cost
```

T185 already found that a quadratic `C` can produce the interior optimum, but
that this shape is partly absorber-owned unless grounded.

### Net objective

The candidate dynamics is

```text
J(lambda,S) = N(lambda,S) - C(lambda,S) - K(lambda,S)
lambda*(S) = argmax_lambda J(lambda,S)
```

T192 asks whether PO1 determines this full object or only its `K` term.

## Positive Control

Use a toy proposal process where:

```text
N(lambda,S) = a*lambda
C(lambda,S) = b*lambda^2
K(lambda,S) = k(S)*lambda
```

with

```text
k(S) = |F(S)| * p_obs(S).
```

Then

```text
J(lambda,S) = (a - k(S))*lambda - b*lambda^2
```

and the interior optimum is

```text
lambda*(S) = (a - k(S)) / (2b)
```

provided `a > k(S)` and `b > 0`.

This positive control shows:

- PO1 gives a meaningful typed contribution through `k(S)`;
- the optimum shifts with obstruction structure;
- but `a` and `b` are still needed.

## Negative Controls

### Negative Control A: Contravariant FinSets semantics

If the coherent-section object is interpreted contravariantly on the full
extension class, then adding constraints cannot increase the forward section
count. The growth reading

```text
N = d|F(S)|/dt
```

fails as a forward covariant issuance law.

So PO1 alone does not recover a forward `lambda*(S)` from contravariant
`FinSets`.

### Negative Control B: Section-preserving covariant subcategory

By T191, on `SectPres(Ext_S)`:

```text
|F(S')| = |F(S)|
N = 0
K = 0
```

Hence there is no nontrivial `lambda*(S)` to derive there either.

### Negative Control C: PO1-only model with no independent N or C

If one keeps only the PO1-native term

```text
J_PO1(lambda,S) = -K(lambda,S) = -lambda * |F(S)| * p_obs(S),
```

then the optimizer is the boundary solution

```text
lambda*(S) = 0.
```

So PO1 by itself does not produce a nonzero interior optimum.

## Absorber Pass

The strongest absorber is the generic optimal-control / queueing / MSY family
already examined in T185.

That absorber owns the following structure:

```text
linear gain
minus convex cost
minus state-weighted risk
=> interior optimum under ordinary first-order conditions
```

What PO1 adds, if anything, is not the existence of such an optimum in
general. It adds a domain-native typing of the obstruction-risk term:

```text
K(lambda,S) = lambda * |F(S)| * p_obs(S)
```

where `p_obs(S)` is defined by PO1 gluing obstruction rather than by an
arbitrary collapse penalty.

So the absorber verdict is:

```text
PO1 does not uniquely generate the entire lambda*(S) formalism.
PO1 does give a native meaning to one load-bearing term inside that formalism.
```

## Results

### 1. The strong statement fails

The strong claim

```text
PO1 alone determines lambda*(S)
```

fails on all three semantic checks:

- full covariant `FinSets` is unavailable (T190);
- section-preserving covariance is dynamically sterile (T191);
- PO1 risk without independent gain/cost gives the trivial optimum `lambda*=0`.

### 2. The narrowed statement survives

What survives is:

```text
PO1 determines the obstruction term K, not the whole optimum.
```

More precisely:

- `PO1` types which extension events count as obstruction;
- `|F(S)|` weights how many coherent sections are exposed;
- `lambda` scales the frequency of extension attempts.

That yields a natural obstruction-load term

```text
K(lambda,S) = lambda * |F(S)| * p_obs(S).
```

### 3. Interior optimum requires extra structure beyond PO1

A nonzero interior optimum exists only after adding:

1. a proposal/gain law `N(lambda,S)`;
2. a reconciliation/congestion law `C(lambda,S)`.

Those may be TaF-typed or absorber-owned, but they are not supplied by PO1
alone.

### 4. Repo-level consequence for PO1-NCK

`PO1-NCK-001` should be read more narrowly:

```text
lambda*(S) is not a pure consequence of PO1.
Rather, PO1 provides the native obstruction-risk component of a broader
issuance dynamics once gain and cost are separately typed.
```

This is still useful, but it is weaker than the original formulation in T188.

## Verdict: narrowed

T192 narrows the formal connection.

Supported:

```text
PO1 => native obstruction term K(lambda,S)
```

Not supported:

```text
PO1 => full derivation of lambda*(S)
```

The interior optimum is a mixed object requiring PO1 plus additional dynamics
for gain and reconciliation cost.

## Falsification Conditions

This verdict should be revisited only if one of the following appears:

1. A TaF-internal derivation of `N(lambda,S)` from the repaired coherent-section
   semantics.
2. A TaF-internal derivation of `C(lambda,S)` from reconciliation / queue
   structure that does not simply restate a generic quadratic penalty.
3. A different semantic repair of the coherent-section object that makes the
   full `lambda*(S)` follow without importing extra growth/cost structure.

Without one of those, `PO1-NCK-001` should remain a narrowed mixed-dynamics
claim.

## Next Step

The honest next moves are now split:

```text
T193/T194: continue the Cap_TI hostile line.
T197: run the absorber audit directly on the MTI / lambda* dynamics package.
```

For the PO1-NCK side specifically:

```text
do not promote lambda*(S) as a PO1 theorem until N and C are independently
typed under the repaired semantics.
```
