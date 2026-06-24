# Explorer: N, C, K Formal Definitions Over the Coherent Section Functor

**Date:** 2026-06-22
**Status:** Exploration — formal definitions attempted; blocking conditions named
**Origin:** Cross-repo coordination session; primary definitions live in TI E031
**Connects to:** CLAIM-LEDGER (PO1), open-problems/temporal-issuance-source-object-spec.md,
  explorer-optimal-issuance-rate-curve-2026-06-22.md, explorer-five-run-metabolic-issuance-2026-06-22.md
**Cross-repo primary:** temporal-issuance/explorations/E031 (full category structure and definitions)

---

## 0. What This Document Does

The five-run pass (explorer-five-run-metabolic-issuance-2026-06-22.md) established that
lambda*(S) = argmax_lambda [N - C - K] is absorbed by generic optimal control unless N,
C, K have substrate-native TaF definitions. The cross-repo session on 2026-06-22
produced the first category-morphism-level definitions via the TI formal object (E031).

This document is the TaF-native reading of those definitions, expressed through the
coherent section functor F: States(Ext_S) -> FinSets that Run 3 of the five-run pass
identified as the correct categorical object for TaF.

---

## 1. The Coherent Section Functor (TaF-Native Formal Object)

The five-run pass Run 3 (Category Theorist) identified the correct formal object:

```
F: States(Ext_S) -> FinSets
```

where:
- States(Ext_S) is the category of typed source constraint states S = (T_S, A_S)
  with morphisms = admissible extensions e: S -> S' (see E031 Part I for full spec)
- FinSets is the category of finite sets
- F(S) = the set of globally coherent sections at state S

**What is a globally coherent section?** In the D1RestrictionSystem setting, a globally
coherent section is an assignment of local data at each observer patch that satisfies
all gluing conditions simultaneously. In the Ext_S setting: a globally coherent section
at S is a maximal admissible subset X ⊆ T_S such that A_S(X) = 1 (admissible under
the state's predicate) and X satisfies the global-section condition across all observer
patches (no PO1 obstruction arises from the combination).

**F on morphisms:** For an admissible extension e: S -> S', F(e): F(S) -> F(S') maps
each globally coherent section at S to its extension in S' (if the new constraint c_e is
compatible with the section) or reports that no extension exists (if c_e creates a PO1
obstruction for that section).

**Functoriality:** F is functorial: F(id_S) = id_{F(S)} and F(e2 ∘ e1) = F(e2) ∘ F(e1)
if extensions compose coherently. This is a formal obligation (not verified in general):
functoriality requires that globally coherent sections compose, which needs the PO1
obstruction to be compositional. See TaF T34 (PO1 chain theorem) for partial support.

---

## 2. N, C, K as Natural Transformations Over F

### 2.1 N(lambda, S) — Rate of New Globally Coherent Sections

**TaF definition:**

```
N(lambda, S) = d|F(S)|/dt  evaluated at issuance rate lambda
```

where d|F(S)|/dt is the rate at which new objects appear in F(S) as S evolves under
the extension process at rate lambda.

In discrete-step terms:

```
N(lambda, S) = E_lambda[ |F(S')| - |F(S)| | S -> S' is one extension step ]
```

This is the expected growth in globally coherent sections per extension step.

**Why this is the TaF-native reading of N from E031:** E031 defines N as D4-morphism
density rate (proportion of type-novel extensions at rate lambda). In TaF, D4 morphisms
are exactly those extensions whose new constraint c_e does not create a PO1 obstruction
— because a PO1 obstruction means the new constraint is globally incoherent (no globally
coherent section extends to include it). So:

```
D4-Hom_lambda(S) in E031 ↔ {e: S -> S' | F(e) is nonempty} in TaF
```

An extension e is type-novel in TaF iff it adds a new type to the global coherent
section set rather than creating an obstruction. This makes N = d|F(S)|/dt the TaF
instantiation of the E031 morphism-density rate.

**Concavity in lambda (TaF version):** N is concave in lambda under the assumption
that the space of PO1-obstruction-free extensions available from S is finite. As lambda
increases, a growing fraction of newly generated extensions will create PO1 obstructions
rather than new coherent sections (because the restriction system becomes more constrained
as more extensions are added). This is the diminishing-returns mechanism for N in TaF.

**Kill condition for N:** N fails to be concave in lambda if new globally coherent
sections catalyze further globally coherent sections (positive feedback via the
D1RestrictionSystem's gluing structure). This would require the gluing conditions to
become easier to satisfy as the schema grows — which can happen if new constraints
reduce the degrees of freedom available to form incoherent assignments (a compactification
effect on the section space). If this occurs, N could be convex in lambda at some states,
eliminating the interior optimum guarantee for those states.

### 2.2 K(lambda, S) — PO1 Obstruction Rate (TaF-Native K)

**TaF definition:**

```
K(lambda, S) = Pr[ F(S') = empty | S -> S' is one extension step at rate lambda ]
             * lambda * |F(S)|
```

Decomposed:
- Pr[F(S') = empty | ...] is the probability that a randomly chosen extension at rate
  lambda creates a total PO1 obstruction (no globally coherent section survives)
- lambda * |F(S)| weights by the rate and current coherent-section count
  (more sections means more at risk from each new extension)

**Why this is superlinear in lambda:** Each new extension creates an independent PO1
obstruction risk for each existing globally coherent section. If p is the probability
that any single extension obstructs any single existing section:

```
K(lambda, S) ≈ p * lambda * |F(S)|
```

This grows superlinearly in lambda when |F(S)| itself is growing (which it is, at rate
N(lambda, S)), creating a coupled system:

```
d|F|/dt = N(lambda, S) - K(lambda, S)  (net coherent section growth rate)
K = p * lambda * |F|
```

When lambda is small, N > K and |F| grows. As lambda increases, K grows faster than N
(superlinear growth of K vs. concave growth of N). The interior optimum lambda*(S) is
where N(lambda, S) = K(lambda, S) + C(lambda, S).

**Connection to PO1 in the CLAIM-LEDGER:** PO1 states that a projection from a globally
satisfiable richer restriction system to a more restricted system can exhibit a
gluing obstruction. K is the rate at which PO1 events occur under the extension process.
lambda*(S) is therefore the rate that maximizes the balance between generating new PO1-free
sections (N) and triggering PO1 obstructions (K). This makes the issuance rate curve a
formal consequence of PO1 rather than an independent claim.

**Independence assumption in TaF:** The p-factor independence assumption (each extension
creates independent obstruction risk) holds when PO1 obstructions are isolated to the
new constraint c_e and do not propagate to previously coherent sections through the
gluing structure. When the gluing structure has long-range dependencies (a constraint
at one patch creates incompatibilities at distant patches), obstructions are correlated
and p is not independent across sections. This must be checked for specific restriction
system instances.

**Falsifiability condition:** K fails to be superlinear in lambda if PO1 obstructions
are positively correlated across sections — i.e., if the addition of c_e tends to make
all sections either obstructed or all coherent (co-movement). This would occur in
a restriction system where constraints are globally coupled rather than locally compatible.
T28 (CAP theorem bridge) and T34 (PO1 chain theorem) give partial evidence for both cases.

### 2.3 C(lambda, S) — Section Integration Cost (TaF-Native C)

**TaF definition:**

```
C(lambda, S) = lambda * E_lambda[ SectionCost(e, F(S)) ]
```

where SectionCost(e, F(S)) is the cost of integrating the new constraint c_e introduced
by e into all existing globally coherent sections in F(S):

```
SectionCost(e, F(S)) = |{sigma in F(S) : sigma must be updated to include c_e}| / |F(S)|
```

This is the fraction of existing globally coherent sections that must be tested for
compatibility with the new constraint and updated if compatible.

**Connection to TypedTransportNetwork:** In the TaF typed transport network (T37), each
new constraint that enters through an extension e must be transported through the network
layers with explicit preservation and forgetting. SectionCost(e, F(S)) is the transport
cost of c_e through the D1RestrictionSystem's observer patches — how many patches must
receive and integrate the new constraint.

**Convexity in lambda (TaF version):** C is linear in lambda when SectionCost is
independent of lambda (each new extension costs the same to integrate regardless of
how many are being processed concurrently). C becomes strictly convex in lambda under
the congestion model: higher lambda means more extensions in the reconciliation queue,
each taking longer because the queue is backed up. The congestion coefficient beta
(from E031's C definition) represents the per-extension overhead from queue contention.

---

## 3. Interior Optimum Existence (TaF-Native Statement)

**Theorem candidate (TaF version):**

lambda*(S) is a well-defined interior optimum (0 < lambda*(S) < infinity) iff:
1. N is concave in lambda (finite PO1-free extension space with diminishing returns)
2. K is superlinear in lambda (independent per-section obstruction risk with p > 0)
3. C is strictly convex in lambda (reconciliation queue congestion with beta > 0)
4. At lambda = 0: dN/d(lambda) > dC/d(lambda) + dK/d(lambda) (issuance is worthwhile
   at very low rates — this holds when some PO1-free extensions are available)
5. At lambda -> infinity: dN/d(lambda) < dC/d(lambda) + dK/d(lambda) (issuance becomes
   too costly at high rates — this holds when K grows faster than N)

Under conditions 1-5, the net functional N - C - K is strictly concave in lambda at S,
with a unique interior maximum lambda*(S) satisfying the first-order condition.

**Why this is TaF-native (not just generic optimal control):** The standard MSY
absorption test (five-run pass Run 4) asks whether N - C - K maps onto the MSY
functional. In TaF, it does not map cleanly onto MSY because:
- N is not a logistic growth rate; it is a cardinality-of-coherent-sections growth rate
  determined by the D1RestrictionSystem's gluing structure
- K is not a harvesting rate; it is a PO1 obstruction probability determined by the
  restriction system's compatibility structure
- The interior optimum condition (K superlinear because of independent per-section
  obstruction risk) is a structural property of the restriction system, not a generic
  resource management result

The MSY formula lambda* = r*K/4 (for logistic growth) will give a different value than
the first-order condition above unless the restriction system's gluing structure
happens to satisfy the logistic growth assumption. Testing whether they agree for a
specific restriction system is the MSY comparison required by the five-run pass.

---

## 4. MSY Absorption Test Result (Partial)

**What is absorbed:** The qualitative shape of lambda*(S) — rising at low lambda, peaking
at an interior optimum, declining at high lambda — is predicted by any MSY-type analysis
and is not TaF-native.

**What is not absorbed:** The specific functional forms of N, C, K in terms of:
- The cardinality of globally coherent sections |F(S)|
- The PO1 obstruction probability p
- The D1RestrictionSystem gluing structure (which determines p)
- The per-section integration cost SectionCost(e, F(S))

These are TaF-native because they reference the restriction system and PO1 obstruction
concepts that are not available in generic resource management theory.

**The discriminating test:** Compute lambda*(S) for a specific D1RestrictionSystem
instance using both the TaF definitions above and the logistic-MSY formula. If they agree,
the TaF structure is adding no discriminating content (the restriction system happens to be
logistic). If they disagree, the gap is TaF-specific structural content.

**Recommended test case:** Two-patch restriction system from E029's C1 sheaf/holonomy
intake: two observer patches with incompatible admissibility predicates. Compute |F(S)|
as the number of jointly admissible sections, p as the PO1 obstruction probability,
and lambda*(S) from both formulas. The incompatible admissibility predicates should
produce a p that is higher than the logistic growth rate would imply, giving a
lower lambda*(S) in the TaF formula than in the MSY formula.

---

## 5. Outstanding Blocking Tasks for TaF

1. **Functoriality of F (FUNCTOR-OBL-TaF-001):** Verify that F: States(Ext_S) -> FinSets
   is genuinely functorial (F(e2 ∘ e1) = F(e2) ∘ F(e1)) using T34's PO1 chain theorem.

2. **Independence assumption verification (IA-TaF-001):** For a specific D1RestrictionSystem
   instance, verify that PO1 obstructions are independent across globally coherent sections
   (required for K superlinearity). T29 (projection-obstruction schema) and T31/T32
   (admissibility conditions) give candidate verification tools.

3. **MSY discrimination test (MSY-TaF-001):** Execute the two-patch comparison described
   in §4. This is the cheapest test for whether the TaF definitions are providing
   discriminating content beyond generic MSY theory.

4. **PO1 formal connection (PO1-NCK-001):** Formally state the claim that lambda*(S) is
   a consequence of PO1 (i.e., K is the PO1 event rate), and add this as a candidate
   claim in the CLAIM-LEDGER. The connection is informal until K's superlinearity is
   verified for a specific restriction system.

5. **PP-3 layer declaration (TaF-PP3-001):** All definitions above are layer-neutral.
   For TaF, S is claimed to be a source-layer state. This claim inherits PP-3 ambiguity:
   a static TaF restriction system with widening observer apertures could produce the
   same F(S) trajectory as a genuinely expanding source. The PP-3 source witness
   requirement from E029 applies to the TaF definitions here.

---

## 6. Placement Summary

| Object | TaF location | Status |
|---|---|---|
| F: States(Ext_S) -> FinSets | New formal object; should be added to FORMALISM.md | candidate |
| N = d|F(S)|/dt | Connects to CLAIM-LEDGER via PO1 | candidate |
| K = p * lambda * |F(S)| | PO1 obstruction rate; connects to PO1 claim | candidate |
| C = reconciliation cost per section | TypedTransportNetwork cost; connects to T37 | candidate |
| lambda*(S) interior optimum | open-problems/ until blocking tasks complete | candidate |
| MSY discrimination test | models/ (Python implementation candidate) | action item |
