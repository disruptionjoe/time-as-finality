# FUNCTOR-OBL-TaF-001: Functoriality of the Coherent Section Functor

## Status

RESOLVED (2026-06-24, T221) by directional split. This obligation is no longer
open. The verdict:

```text
F  : States(Ext_S)    -> FinSets   is NOT a functor   (counterexample, T221 Part I)
F_op : States(Ext_S)^op -> FinSets is     a functor   (proof,        T221 Part II)
```

The functorial direction (contravariant restriction-of-solutions) is the
opposite of the covariant direction PO1-NCK-001 and the NCK forward-issuance
dynamics required. So the blocker is settled by *refutation* of the assumed
covariant functor, not by satisfying it. Consequence: PO1-NCK-001 is re-scoped
(PO1 types K, not lambda*(S)); MTI is unchanged (its T184-T188 evidence never
depended on covariant functoriality). See
`tests/T221-coherent-section-functoriality-verdict.md` and
`results/T221-coherent-section-functoriality-verdict-v0.1-results.md`.

The original obligation text below is retained as the historical statement of
what was being asked, including the over-optimistic covariant "minimal
verification path" (lines reasoning toward F(e2 o e1) = F(e2) o F(e1)) that
T190 and T221 Part I refute: the covariant morphism map is not even total, so
composition preservation is never reached.

---

### Original obligation (historical, pre-T221)

Open formal obligation. This is not a claim promotion, not a test result,
and not an upgrade to any existing TaF claim. It is the blocking condition
for promoting PO1-NCK-001 from a candidate formal connection to a supported
formal connection.

## What This Obligation Requires

The NCK formal definitions (explorations/explorer-nck-formal-definitions-2026-06-22.md)
and the T188 PO1-NCK formal claim (tests/T188-po1-nck-formal-claim-and-cap-ti-step4.md)
both rely on:

```
F: States(Ext_S) -> FinSets
```

where:
- States(Ext_S) is the category of typed source constraint states S = (T_S, A_S)
  with morphisms = admissible extensions e: S -> S'
- FinSets is the category of finite sets
- F(S) = set of globally coherent sections at state S (assignments of local data
  satisfying all gluing conditions simultaneously with no PO1 obstruction)

**Functoriality claim:**
```
F(id_S) = id_{F(S)}           (identity preservation)
F(e2 ∘ e1) = F(e2) ∘ F(e1)   (composition preservation)
```

Until these two conditions are verified for the D1RestrictionSystem setting,
F is a well-motivated construction but not a proven functor. The NCK definitions
and PO1-NCK-001 connection carry an implicit functoriality assumption that must
be discharged before they can be formally promoted.

## Why This Is Nontrivial

**Identity preservation** is straightforward: the identity extension e = id_S
adds no new constraints, so every globally coherent section at S remains
coherent at S. F(id_S)(sigma) = sigma for all sigma in F(S). This follows
from the definition of F(S) as the set of sections satisfying the current
constraint set.

**Composition preservation** is nontrivial. For two admissible extensions
e1: S -> S' and e2: S' -> S'', we need:

```
F(e2 ∘ e1) = F(e2) ∘ F(e1)
```

This means: the set of globally coherent sections at S'' computed in one step
(via the composed extension e2 ∘ e1) must equal the set computed in two steps
(first extending from S to S' via e1, then from S' to S'' via e2).

**Where it can fail**: If PO1 obstructions are NOT compositional — meaning a
section that survives both e1 and e2 individually might not survive the composed
extension e2 ∘ e1 — then F is not functorial. This would happen if the composed
extension creates an obstruction that neither individual extension creates.

**Relationship to T34 (PO1 Chain Theorem):** T34 proves that PO1 admissibility
is an endpoint property of projection chains — AC1-AC7 are evaluated at the
(source, target) pair of a chain, not at individual links. This is evidence FOR
functoriality: if PO1 obstructions are endpoint-determined, then the section
set at the endpoint is determined by the composition, not by intermediate steps.
However, T34 does not prove F(e2 ∘ e1) = F(e2) ∘ F(e1) directly.

**The missing step**: T34 shows that the VERDICT (PO1 yes/no) is chain-
endpoint determined. What is needed is that the SECTION SET F(S) is also
determined by the same chain structure. These are equivalent only if:
- F(S) = empty iff S is PO1-obstructed (one direction: section existence iff PO1-free)
- F(S) != empty iff S has a globally coherent section (the other direction)

This follows from the definition of F, so T34 does imply F is defined on
endpoints. What T34 does NOT prove is that F on morphisms (the map F(e):
F(S) -> F(S')) commutes with composition.

## Minimal Verification Path

**Step 1**: State the composition law formally for the two-patch fixture
(from T28/T39 CAP theorem witness):

```
S_0: two patches with admissibility predicates P_A = {+1}, P_B = {+1}
e1: S_0 -> S_1 by adding constraint x_A = x_B
e2: S_1 -> S_2 by adding constraint x_A = +1

F(S_0) = {(+1, +1), (-1, -1), (+1, -1), (-1, +1)}  [before P_A, P_B constraints]
F(S_1) = {(+1, +1), (-1, -1)}  [x_A = x_B constrains to same sign]
F(S_2) = {(+1, +1)}  [x_A = +1 forces the positive case]

Composition e2 ∘ e1: S_0 -> S_2 by adding {x_A = x_B, x_A = +1}
F(e2 ∘ e1)(F(S_0)) = {(+1, +1)}  (only section surviving both constraints)
F(e2)(F(e1)(F(S_0))) = F(e2)({(+1,+1), (-1,-1)}) = {(+1,+1)}

EQUAL. F(e2 ∘ e1) = F(e2) ∘ F(e1) for this fixture.
```

**Step 2**: Verify in the PO1-creating case (one extension creates PO1):

```
e3: S_0 -> S_3 by adding constraint x_A = -x_B (incompatible with P_A, P_B)

F(S_3) = {} [PO1 obstruction — no section satisfies P_A and P_B and x_A=-x_B]
F(e3)(sigma) = undefined for sigma in F(S_0) with P_A,P_B [sigma has x_A,x_B both in {+1,-1}]

If F(S_3) = {} for ALL sigma, then F(e3) is the map F(S_0) -> {} (empty)
F(e2 ∘ e3): We cannot extend from S_3 (no sections exist), so composition
produces the empty section set.
```

This confirms F is well-defined on PO1-obstructed states (empty section set)
and that composition through an obstructed intermediate gives empty sets.

**Step 3**: Verify the general principle — PO1 obstruction is preserved under
composition (if e1 creates a PO1 obstruction, then e2 ∘ e1 also has empty
F, regardless of e2). This follows from:
- F(S') = {} implies F(S'') = {} for any extension e2: S' -> S''
  (cannot extend from empty section set)

**The composition law F(e2 ∘ e1) = F(e2) ∘ F(e1) then holds as:**
- If F(S') = {}, then F(e2 ∘ e1) maps to {} and F(e2) ∘ F(e1) also maps to {}
- If F(S') != {}, then F(e2) ∘ F(e1) applies F(e1) to get F(S') and F(e2) to get F(S'')

The question is whether going from S to S'' in one step gives the same result
as going through S'. This holds iff the constraint accumulation in e2 ∘ e1 is
the same as the sequential accumulation of e1 then e2. Since D1RestrictionSystem
extensions add constraints one at a time, and the constraint set of e2 ∘ e1 is
the union of constraints from e1 and e2, this should hold.

## Formal Obligation Statement

**FUNCTOR-OBL-TaF-001** is satisfied when all three of the following are verified:

1. **Identity**: F(id_S) = id_{F(S)} for all states S. (Follows from definition.)

2. **Composition on non-obstructed chains**: F(e2 ∘ e1) = F(e2) ∘ F(e1) when
   both F(S') and F(S'') are non-empty. Requires checking that sequential
   constraint accumulation gives the same section set as simultaneous
   constraint accumulation.

3. **Composition through obstruction**: F(e2 ∘ e1) = {} whenever F(S') = {},
   because no sections survive. (Follows from the definition of F(S').)

## Recommended Test

Register as T189 (or incorporate into T188 as a verification step):

**T189: Coherent Section Functor Composition Law**

Target: FUNCTOR-OBL-TaF-001
Setup: Two-patch D1RestrictionSystem with sequential extensions
Test: Verify F(e2 ∘ e1) = F(e2) ∘ F(e1) for the non-obstructed and
  obstructed cases from the T28/T39 fixture.
Expected result: VERIFIED for finite two-patch cases; argue extension to
  general finite D1RestrictionSystems by constraint-accumulation argument.

## What Verification Unblocks

Verifying FUNCTOR-OBL-TaF-001 allows:
1. PO1-NCK-001 to be formally promoted from `candidate` to `supported` in CLAIM-LEDGER.md
2. The N, C, K definitions in explorer-nck-formal-definitions-2026-06-22.md to become
   formal TaF objects rather than candidates
3. lambda*(S) to be stated as a formal TaF theorem (not just a formal-candidate claim)
4. Cap_TI Candidate C to advance from OPERATIVE CAPABILITY to SUPPORTED FORMAL CAPABILITY

Until FUNCTOR-OBL-TaF-001 is verified, the PO1-NCK connection is informally
supported but cannot be cited as a formal theorem.
