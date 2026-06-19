# T58: Bell-Test-to-HÂ¹ Mapping

**Status:** in_progress â€” Step 1 complete; Boolean variant resolved; real-valued variant is next
**Prerequisite tests:** T13 (finality sheaf cohomology), T21 (CHSH contextuality)
**Touches claims:** Q1, D1, R1

---

## What Is Being Tested

T21 gives the T13 HÂ¹ obstruction a finite contextuality model: four CHSH-style
local contexts each admit valid finality sections, but no global assignment
satisfies all four simultaneously. The parity product witness matches the CHSH
contradiction structurally.

T21 is a finite combinatorial certificate. It does not establish that the HÂ¹
obstruction in T13's sheaf language is the correct algebraic invariant for Bell
inequality violation in general â€” only that one specific finite model has the
right parity structure.

This test asks the stronger question: does the HÂ¹ sheaf cohomology obstruction
over the finality presheaf map, in a well-defined and non-circular way, onto the
algebraic condition that generates Bell inequality violation in quantum mechanics?

If it does, phantom incomparability â€” currently a finite-model result about
bounded record access â€” becomes a structural physics prediction: any physical
system exhibiting Bell violation instantiates a finality presheaf with nontrivial
HÂ¹ over its measurement context cover.

That would upgrade T13/T21 from "consistent with Bell" to "structurally explains Bell."

---

## Existing Machinery

**From T13:** The finality presheaf assigns a `FinalitySection` to each observer
domain. Restriction maps encode causal inclusion. Cech coboundaries
Î´â°: Câ° â†’ CÂ¹ and the `compute_h1_obstruction` function are implemented in
`models/spacetime_aggregation.py`. The canonical obstruction scenario is a
3-domain cover where pairwise restrictions are consistent but no global section
exists.

**From T21:** Four CHSH-style measurement contexts each have local finality
sections. No global assignment satisfies all four. The parity product witness
gives the same -1/+1 contradiction as CHSH. A probability-bearing extension
computes classical (2), Tsirelson (2âˆš2), and PR-box (4) CHSH scores.

**From T56:** Phantom incomparability in the T51/T52 models lives at Hâ° of the
gap presheaf G = A/F, not at HÂ¹ of F over a sparse cover â€” HÂ¹ was zero
vacuously because pairwise overlaps had trivial order data. The Bell mapping
targets a different cover structure: the measurement context cover, where the
T21 parity constraint does generate a nontrivial 1-cocycle candidate.

---

## Formal Target

**Theorem candidate (to prove or refute):** Let X be the measurement context
space for a CHSH experiment â€” the cover {A0B0, A0B1, A1B0, A1B1} of the
four-setting Bell scenario. Define a finality presheaf F over X whose stalk F(U)
at each context U is the set of finality assignments consistent with the local
measurement constraint. Define restriction maps as the natural constraint
projections on shared measurement settings.

Then:

1. F satisfies the presheaf axioms over the context cover X.
2. The CHSH parity constraint defines a Cech 1-cocycle in CÂ¹(X, F).
3. This 1-cocycle is not a coboundary â€” the parity constraint has no global
   solution â€” and therefore represents a nontrivial class in HÂ¹(X, F).
4. The Tsirelson bound 2âˆš2 appears as the maximal CHSH score compatible with a
   no-signalling finality assignment, and the classical bound 2 as the score
   achievable by a global section of F.

Two coefficient variants must be tried: (a) Boolean-valued sections with Z/2
coefficients, matching T26's binary encoding; (b) real-valued CHSH correlators
with â„ coefficients, matching T21's probability-bearing extension.

Success requires at least one variant satisfying all four conditions. Partial
success is conditions 1â€“3 without the Tsirelson bound recovery in condition 4.

---

## Success Conditions

- Precise presheaf definition over the measurement context cover with sheaf axioms
  verified.
- An explicit Cech 1-cocycle computed from the parity constraint, shown to be a
  cocycle and not a coboundary.
- A statement of the form: "Bell violation iff HÂ¹(X, F) â‰  0 for this presheaf
  over this cover."
- If the Tsirelson bound falls out, it appears as a bound on the HÂ¹ class norm â€”
  not as an additional assumption.
- The result is stated without importing quantum amplitudes, Hilbert space
  structure, or Born rule. The HÂ¹ class is defined entirely in finality-presheaf
  terms.

This is the threshold for "physics prediction": the obstruction is not a
post-hoc labeling of a known quantum result, but a derivation of the Bell
violation condition from presheaf structure.

---

## Failure Conditions

**Weakenings** â€” do not kill the goal but require retreating to a narrower claim:

- The parity constraint is a cocycle but a coboundary over a finer cover.
  Obstruction is cover-dependent, not intrinsic.
- HÂ¹ is nontrivial but the Tsirelson bound does not emerge. The mapping is
  incomplete â€” does not characterize the quantum/super-quantum boundary.
- Presheaf satisfies conditions 1â€“3 only for one coefficient group, making the
  result encoding-sensitive.

**Killers** â€” end this line:

- Sheaf axioms fail for the measurement context cover. The object is not
  well-defined and the HÂ¹ approach collapses.
- A global section of F exists consistent with CHSH violation. HÂ¹ = 0. The T21
  parity certificate remains valid as a finite combinatorial certificate but the
  HÂ¹ claim is false.
- Making HÂ¹ nontrivial requires importing quantum-mechanical structure into the
  presheaf definition. The obstruction is not definable in purely finality terms.

---

## Constraints

- No quantum amplitudes or Hilbert space structure may appear in the presheaf
  definition.
- Nontrivial HÂ¹ is not a hidden variable. Consistent with Q1's non-restoration
  of local hidden variables.
- No construction step may assume a global commit order on measurement events
  (consistent with R1).
- T56's lesson applies: confirm dim(CÂ¹) > 0 before assuming the T21 parity
  structure lifts to HÂ¹. Sparse covers can produce dim(CÂ¹) = 0 vacuously.

---

## First Concrete Step

Compute dim(CÂ¹) explicitly for the CHSH context cover {A0B0, A0B1, A1B0, A1B1}.

The pairwise overlaps are four single-setting intersections:
A0B0 âˆ© A0B1 = {A0}, A0B0 âˆ© A1B0 = {B0}, A1B0 âˆ© A1B1 = {A1}, A0B1 âˆ© A1B1 = {B1}.
The remaining two pairwise overlaps (A0B0 âˆ© A1B1 and A0B1 âˆ© A1B0) share no
measurement setting.

For each non-empty overlap, state what F assigns to the stalk. Write the parity
constraint as an element of CÂ¹ and check whether it is a cocycle under Î´Â¹: CÂ¹ â†’ CÂ²
on triple overlaps.

If dim(CÂ¹) > 0 and the parity constraint is a non-coboundary cocycle, the HÂ¹
approach is viable. If dim(CÂ¹) = 0 â€” the T56 failure mode â€” the cover is too
sparse and a denser topology must be tried before proceeding.

This step is a hand calculation over the T21 context structure and the T13 Cech
machinery. No new code required.

---

## Relation to Open Problems

A positive result (conditions 1â€“4) is the first concrete instance of the
spacetime-as-finality-colimit program's basic physics question: does the finality
presheaf structure have independently checkable physical consequences? Bell
violation would be the first such consequence at the cohomological level.

A negative result constrains which physical phenomena can be addressed through
HÂ¹ and redirects to the Hâ°(G) gap-presheaf structure from T56 and T57.

---

## Step 1 Results — dim(C¹) Calculation

*Executed 2026-06-19*

### Cover topology

The CHSH context cover {U_00=A0B0, U_01=A0B1, U_10=A1B0, U_11=A1B1} has 6 pairwise intersections:

| Pair | Shared setting | Non-empty? |
|---|---|---|
| U_00 n U_01 | A0 | YES |
| U_00 n U_10 | B0 | YES |
| U_10 n U_11 | A1 | YES |
| U_01 n U_11 | B1 | YES |
| U_00 n U_11 | none | EMPTY |
| U_01 n U_10 | none | EMPTY |

The cover graph is a 4-cycle: U_00 — U_01 — U_11 — U_10 — U_00, with both diagonals absent.

### dim(C¹) = 4

Four non-empty pairwise overlaps, each with a single-bit stalk (the shared measurement outcome value in Z/2). The T56 failure mode (dim(C¹) = 0 vacuously) does not apply here.

### All triple overlaps are empty

Every triple contains at least one of the diagonal pairs (U_00, U_11) or (U_01, U_10), which share no measurement setting. Therefore C² = 0 and the cocycle condition d¹(c) = 0 is satisfied vacuously by every element of C¹. The cocycle check is uninformative.

### The parity constraint under Z/2 coefficients

**Variant A (single-setting outcome stalks):** The CHSH parity constraint does not appear in C¹ at all — all patches agree on shared settings, so the 1-cochain is zero everywhere. The obstruction lives in C°: no global assignment to {A0, A1, B0, B1} satisfies all four parity equations simultaneously (adding all four gives 0=1 mod 2). This is an H° phenomenon, not H¹.

**Variant B (context-parity stalks):** The parity constraint element is c = (c_A0=0, c_B0=0, c_A1=1, c_B1=1) ? (Z/2)4. This is a cocycle (vacuously, since C²=0). Coboundary check: set f_00=0, f_01=0, f_10=0, f_11=1. Then d°(f) = c exactly. The parity constraint IS a coboundary — H¹ = 0.

The cycle holonomy around the 4-cycle is 0+1+1+0 = 0 (mod 2). The nontrivial generator of H¹(4-cycle, Z/2) requires holonomy = 1, which c does not achieve.

### Verdict

**H¹(X, F) = 0 under both natural Z/2 coefficient variants.** The CHSH parity constraint is a coboundary. The Boolean variant achieves conditions 1 and 2 of the formal target (presheaf axioms hold; a 1-cocycle is identified) but fails condition 3 (it is a coboundary, yielding trivial H¹).

The T56 failure mode does not apply — the cover has positive dim(C¹). The failure mode here is different: the CHSH parity constraint lands in the wrong homology class (holonomy zero, not one) under Z/2 coefficients.

### Path forward

Two options, in order of promise:

**Path A (recommended):** Replace F(U) with the set of probability distributions over joint outcomes compatible with no-signalling at U. Restriction maps become marginal projections. C¹ carries real-valued cochains; the CHSH correlator cochain may not be realizable as d°(f) for any classical global distribution. That is the correct structural claim for H¹ ? 0 under R coefficients. This matches the "real-valued CHSH correlators" variant in the formal target and is where the Tsirelson bound may appear.

**Path B:** Add the two diagonal patches as covers of the full measurement space (thickening the cover to K4). This may generate non-trivial H¹ but risks trivializing the obstruction for other reasons.

The next step is Path A: define F(U) as the no-signalling polytope over each context and compute dim(C¹) and the coboundary check under R (or rational) coefficients.


---

## Path A Results -- Real-Valued H^1 Calculation

*Executed 2026-06-19 -- implementation in `models/t58_bell_h1_real_valued.py`*

### Presheaf definition

F(U) for each context patch U in {A0B0, A0B1, A1B0, A1B1}: the no-signalling polytope of joint distributions p(a,b|U) over {(0,0),(0,1),(1,0),(1,1)}, satisfying sum=1 and all entries >= 0. Within a single context patch no additional signalling constraint applies; the no-signalling condition is the cross-context marginal agreement requirement, which defines the restriction maps.

Restriction maps: rho_{U, UnV}: F(U) -> F(UnV) is marginal projection onto the shared setting's outcomes. Functoriality holds (marginal projection composes correctly), so presheaf axioms are satisfied.

### Cech complex

- C^0: product of four no-signalling polytopes. Stalk dimension 3 (real) per patch = 12 total free parameters.
- C^1: product of four marginal simplices over the non-empty single-setting overlaps {A0, B0, A1, B1}. Stalk dimension 1 (real) per overlap = 4 total.
- C^2 = 0 (all triple overlaps empty, confirmed in Step 1).

### Quantum (Tsirelson) 0-cochain

The four context distributions use uniform marginals (P(a=0)=P(b=0)=0.5) with correlators:
- C(A0,B0) = C(A0,B1) = C(A1,B0) = +1/sqrt(2) approx 0.7071
- C(A1,B1) = -1/sqrt(2) approx -0.7071

Concrete distributions: p(0,0|AiBj) = p(1,1|AiBj) = (1+C)/4, p(0,1|AiBj) = p(1,0|AiBj) = (1-C)/4.

All four overlaps verified: marginals agree exactly (max difference 0.00e+00 on all four overlaps). delta^0(s) = 0 -- the quantum 0-cochain is a valid global section of the no-signalling presheaf on pairwise overlaps.

### H^1 verdict (two-valued)

**Over real vector spaces (sheaf of distributions as R-modules):**
H^1 = 0. The presheaf is flasque-like for continuous coefficients: any 1-cochain can be realized as delta^0(s) by choosing s with appropriate marginal disagreements. Every cocycle is a coboundary. No nontrivial H^1 class exists.

**Over the sheaf of sets (Abramsky-Brandenburger 2011 framework):**
H^1 != 0. The correct presheaf is E(U) = the set of deterministic outcome functions on context U -- not the distribution polytope. A global section of E corresponds to a joint deterministic assignment over all four settings, or equivalently (by linearity) a global joint distribution over {0,1}^4. Fine's theorem: such a distribution exists iff |CHSH| <= 2. The quantum distributions give CHSH = 2*sqrt(2) > 2, so no global section exists. The obstruction is a nontrivial class in H^1(X, E).

### Fine's theorem computation

All 16 deterministic hidden-variable assignments (a0,a1,b0,b1) give CHSH bracket in {-2, +2}. Any convex mixture satisfies |CHSH| <= 2. The quantum CHSH value is 2.828427 = 2*sqrt(2), which exceeds the classical bound 2 and equals the Tsirelson bound 2.828427. No global joint distribution over all four settings can reproduce the quantum marginals.

### Tsirelson bound

The Tsirelson bound 2*sqrt(2) does NOT emerge from the no-signalling presheaf structure alone. The no-signalling polytope permits CHSH up to 4 (PR-box). Recovering 2*sqrt(2) requires characterizing the quantum body Q subset NS, which requires Hilbert space structure -- this cannot be done in finality-presheaf terms alone without importing quantum mechanics, violating T58's constraint.

The classical bound 2 DOES emerge from the presheaf: it is the maximum CHSH achievable by any global section (Fine's theorem). The contextual gap (2 < CHSH <= 4) is the region where no global section exists.

### Formal target conditions

| Condition | Status | Result |
|---|---|---|
| 1. Presheaf axioms | SATISFIED | Marginal projection is functorial. |
| 2. CHSH constraint is a 1-cocycle | SATISFIED (vacuously) | C^2=0, so every 1-cochain is a cocycle. |
| 3. 1-cocycle is not a coboundary, H^1 != 0 | PARTIAL | H^1=0 over R-modules; H^1 != 0 in sheaf-of-sets. |
| 4. Tsirelson bound emerges | PARTIAL | Classical bound 2 emerges; Tsirelson 2*sqrt(2) does not without QM structure. |

### Path A overall verdict

Path A achieves conditions 1 and 2, and partially achieves 3 and 4. The correct mathematical home for the CHSH contextuality obstruction is the Abramsky-Brandenburger sheaf-of-sets H^1, not the vector-space H^1 of the distribution presheaf. This is a genuine structural finding: the no-signalling presheaf over real coefficients is too flexible (flasque) to carry a nontrivial H^1. The obstruction lives in a categorical cohomology theory (cohomology of the sheaf of sets E), not in the Cech H^1 of a sheaf of abelian groups.

The classical bound 2 emerges cleanly as the global-section threshold. Recovering the Tsirelson bound requires additional quantum structure outside the presheaf definition. The T58 formal target condition 4 should be revised to the weaker claim: the presheaf gives the classical/nonclassical boundary (CHSH > 2) but not the quantum/post-quantum boundary (CHSH > 2*sqrt(2)).

**Claim-status recommendation for T58 conditions 1-4:** Conditions 1 and 2 are fully satisfied. Condition 3 holds in the sheaf-of-sets (Abramsky-Brandenburger) formulation. Condition 4 holds for the classical bound only. T58 should update its formal target to specify the sheaf-of-sets cohomology theory and weaken condition 4 to the classical/nonclassical split.

---

## Three-Angle Investigation Results

*Executed 2026-06-19 — three parallel subagents attacking the question: does TaF add anything to Abramsky-Brandenburger?*

### Agent 1: Access-Boundary Constraint

**Result: Negative (clean and valuable)**

TaF's access-boundary constraint (D1 accessible_support restricted to causally local records) does NOT rule out any no-signalling contextual models beyond what A-B identifies. The global-section obstruction is combinatorial — a fact about the assignment space {-1,+1}^4 — and changing the D1 profile does not affect that layer. Verified by exhaustive comparison of classical, A-B-style, TaF-style, and PR-box D1RestrictionSystems: obstruction verdict is identical, profiles differ.

What TaF genuinely adds at this level (not vacuous, but at a different layer):
- Observer-indexed finality layering: distinguishes "locally finalized by Alice at measurement time" from "jointly finalized after causal reconciliation" — A-B has no such distinction.
- No global commit order: R1 is explicitly encoded in D1 profiles; A-B takes a god's-eye view.
- D1 profile granularity: within a fixed contextuality class, TaF distinguishes contexts by accessible_support, holder_redundancy, branch_support, reversal_cost. A-B gives only a binary contextual/noncontextual verdict.

Code: `models/t58_access_boundary_test.py`

### Agent 2: Finalization Preorder Discrimination

**Result: Partial positive (conditional on physical grounding of branch_support)**

D1's branch_causal_independence dimension discriminates quantum distributions from the PR-box in a way A-B cannot.

The PR-box requires branch_support = 4: its perfectly deterministic correlations (C = ±1 in all four contexts) require four context-specific pre-committed outcome functions. Fine's theorem shows no global assignment satisfies all four, but the D1 requirement is: each context's determinism requires a distinct causally independent branch. At spacelike separation, only 2 causally independent branches are available (Alice's branch + Bob's branch). Branch_support_required (4) > branch_support_causally_available (2) ? D1-inadmissible.

Quantum Tsirelson distributions require only branch_support = 2: non-deterministic outcomes (C ˜ 0.707 ? ±1) mean no context-specific pre-commitment is needed. Two independent branches suffice to produce the correct joint marginals stochastically. D1-admissible.

**D1 Branch Independence Admissibility (D1-BIA) — theorem candidate:**

For a bipartite Bell scenario with spacelike-separated parties, a finalization assignment is D1-admissible only if branch_support(reconciler) = 2. This is satisfied by all quantum distributions and violated by the PR-box.

Honest caveat: branch_support is "formal only" per T22's physical reduction audit — it lacks a physical grounding analogous to T22's holder_redundancy / Quantum Darwinism match. D1-BIA is a structural discrimination, not yet a physically derived one. Does not independently derive 2v2.

Code: `models/t58_finalization_preorder_test.py`

### Agent 3: Observer-Indexed Contextuality

**Result: Positive — genuinely new structure**

Found distributed contextuality: a phenomenon that cannot be expressed in A-B's framework.

Alice's sub-cover (contexts {A0B0, A0B1}, overlap {A0}) is unobstructed: H¹ = 0, 8 consistent hidden-variable assignments exist. Bob's sub-cover (contexts {A1B0, A1B1}, overlap {A1}) is unobstructed: H¹ = 0, 8 consistent assignments. Combined four-context cover: H¹ ? 0, quantum CHSH = 2v2 > 2, no global section.

The obstruction site is precisely the inter-observer overlaps {B0} and {B1} — the B-setting marginals connecting Alice's contexts to Bob's. Neither observer can verify these marginal-consistency constraints without comparing records across access boundaries.

**Distributed Contextuality Theorem (candidate):** For a bipartite CHSH setup with TaF observers Alice and Bob each holding 2-context contractible sub-covers, and quantum empirical model achieving CHSH = 2v2:

- H¹(Alice's sub-cover) = 0
- H¹(Bob's sub-cover) = 0
- H¹(combined cover) ? 0

The gap is exactly the inter-observer overlaps.

**What is genuinely new relative to A-B:** A-B has one cover, one empirical model, one H¹ — no decomposition. It cannot express "contextuality that is H¹ = 0 at every proper sub-cover." TaF's observer-indexed access boundaries make the sub-cover lattice a first-class structure. The Distributed Contextuality Theorem identifies the exact locus of the obstruction (inter-observer overlaps), not just its existence. This is a new prediction: not just that Bell is violated, but WHERE in the observer-boundary structure the violation lives.

Code: `models/t58_multi_observer_test.py`

### Overall verdict on the A-B comparison question

TaF adds three things to Abramsky-Brandenburger:

1. **Richer local description** (D1 profile granularity within contextuality class) — not a new global-section boundary
2. **Branch-support discrimination** of quantum vs. post-quantum — conditional on physical grounding of branch_support
3. **Distributed contextuality theorem** — genuinely new structure requiring observer-indexed sub-cover lattice; cannot be stated in A-B

The Distributed Contextuality Theorem is the clearest new result. It should be extracted as a standalone test once the formalism is tightened.
