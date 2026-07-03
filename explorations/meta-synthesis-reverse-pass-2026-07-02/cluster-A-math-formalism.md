---
document_type: persona_meta_synthesis_cluster
cluster: A-math-formalism
primary_reader: agents
read_pattern: current_state
authority: exploratory
pass: reverse-meta-synthesis
created: 2026-07-02
status: exploratory
personas: [2, 5, 6, 10, 11, 14, 15, 23, 24, 26, 37, 47, 52]
note: >
  Persona output is METHOD, not evidence. Reverse order per brief:
  meta-synthesis FIRST, then Hegelian test, then steelman. Rigorous-heterodox.
---

# Cluster A — Math / Formalism (Reverse Meta-Synthesis Pass)

Load-bearing for the ASSEMBLY question. Recurring cross-cluster finding stated up
front so each voice can be read against it: **under every geometric lens in this
cluster the trichotomy refuses to close into one object, and the mode that breaks
it is not fixed — it is whichever mode is orthogonal to that lens's invariant.**
Watch which mode each persona ejects.

---

## 2. Category Theorist

**Meta-synthesis.** There is one functor `F: Models → Boundaries` sending a closed
model to its capability boundary, and the whole taxonomy is a classification of
*which (co)limit F fails to preserve*. E0-declared = F preserves the limit (the
separating datum is literally in the limit cone, hence in the model — that is the
Declarability Lemma restated: finite closed models are limits, and a section of a
limit is co-present). Forcing = F stops preserving a universal construction: E1 =
filtered-colimit non-preservation (the datum only appears "at ∞"); E3 =
non-preservation of a coequalizer/quotient by a symmetry (the datum lives only in
the equivariant/orbit category). The thing we are MISSING: nobody has written F
down as an actual functor, so "physical vs declared" is being argued pointwise
instead of as a natural-transformation failure — the residue should be a *cokernel
of a natural comparison map*, computed once, not three narratives.

**Hegelian.** Antithesis: E2 (computational hardness) has no universal-property
description. Preservation/non-preservation of a limit is a yes/no structural fact;
"hard to compute" is a *metric on the arrows*, invisible to any functor, invariant
under equivalence of categories. Renaming E2 as "a colimit reached slowly" is
pattern-matching, not structure — it dies exactly on item-12's negative (E2 came
back REDESIGN/pre-empted). Synthesis: F is a genuine object for E0/E1/E3; E2 is
not in its image. The categorical content is a *span*, not a tower.

**Steelman.** Concrete claim: define `F: Ind(C_fin) → Set` on a finitely-presented
model category; the boundary residue is `coker(colim F → F(colim))`. E1 = this
cokernel is nonzero only after passing to Ind-completion; E3 = it is nonzero only
in `C^G` (equivariant). The one move that makes it real: exhibit E2 as *not*
expressible this way — prove no functor invariant under categorical equivalence
separates the E2 boundary. That non-representability is the deliverable.

---

## 5. Algebraic Topologist

**Meta-synthesis.** The pieces assemble into one exact sequence with an obstruction
class. The global-correlation separator (item 10) is an `H^1` gluing obstruction: a
1-cocycle that is a coboundary on every proper subset (locally trivial) but not
globally — legitimacy/finality as a section with no local witness. The bold move:
E1/E2/E3 is a *filtration by the page on which the class dies*. A datum that is
already a coboundary at the first page = E0 declared. A class that survives to
E_∞ = a genuine forced boundary. The trichotomy = **three pages at which a local
class either becomes or ceases to be a global obstruction.** What we are missing:
a spectral sequence whose input is the model's cover and whose `E_∞` is the
boundary residue — then E0/E1/E3 are literally differentials `d_r`.

**Hegelian.** Antithesis: the E1/E2/E3 labels reading like spectral-sequence pages
is the single most seductive *rhyme* in the whole program — coincidental notation,
not mathematics. And a spectral sequence needs a filtered complex with a fixed
base ring; the T421 disanalogy (indefinite metric survives) means the coefficients
are not a field of definite signature, so "the class dies at page r" is not
well-posed. Synthesis: keep `H^1` (that is real — it is the only relabel-proof
residue and it survives the negatives). Drop the page-numbering unless a filtered
complex is actually produced.

**Steelman.** Real claim, minus the rhyme: the separator is `Ȟ^1(cover; 𝒜)` of the
observable-algebra sheaf `𝒜`; it is nonzero iff the datum is global-only. E1 = the
class is nonzero only in the direct-limit sheaf (`lim^1` term); E3 = nonzero only
in equivariant cohomology `H^1_G`. The one move: compute `Ȟ^1` for one honest TaF
cover and show it is nonzero — a single worked obstruction beats the analogy.

---

## 6. Representation Theorist

**Meta-synthesis.** E3 is not "one mode among three" — it is the *grading* the other
two live inside. Symmetry/superselection decomposes the global algebra into
isotypic sectors; the separating datum is a coset/character that is invisible
inside any single irreducible block but visible in the whole decomposition. That
is exactly "present in the whole, in no proper subset." So the assembly: the
observable algebra carries a `G`-action; E0 = datum in the trivial isotype
(co-present, invariant); forcing = datum in a nontrivial isotype that the
admissible menu cannot query. The admissibility hinge (item 7) = *choice of which
representations count as physical* — a restriction of the representation ring. The
missing piece: the whole "physical vs declared" line is a **branching rule** —
which characters survive restriction to the admissible subgroup.

**Hegelian.** Antithesis: this swallows E1 and E2 into E3 by fiat. A thermodynamic
limit (E1) and a hardness assumption (E2) are not group-theoretic; forcing them
into isotypic language is the "everything is symmetry" overreach the panel exists
to catch. And T421 says GU's E3 (indefinite metric grading) and TaF's E3
(operational no-recovery) are *different objects* — so even E3 is not one
representation-theoretic thing. Synthesis: E3 genuinely is a branching/grading
story, but it is *two* gradings (Krein/ghost-parity vs recovery-orbit), and neither
subsumes E1/E2.

**Steelman.** Claim: the admissible menu is a subgroup `H ≤ G`; the boundary datum
is a `G`-character `χ` with `χ|_H` trivial but `χ` nontrivial. Declared vs forced =
`χ ∈ ker(res: R(G)→R(H))`. The one move: identify `G` and `H` concretely for one
repo, and show the two E3 gradings are *non-isomorphic* `ℤ/2`-actions — which would
turn T421 from a wound into a representation-theoretic classification.

---

## 10. Formal Methods Researcher

**Meta-synthesis.** The taxonomy is a single typing judgment with one reduction
relation, and it has never been written as executable semantics. "Physical vs
declared" = "well-typed under a context that does / does not export the separating
datum." E0 = the datum is in the context but the interface projection drops it
(a subtyping/coercion, decidable). E1/E2/E3 = three reasons the judgment
`Γ ⊢ query : datum` has *no derivation*: E1 = derivation exists only for the
infinite unfolding (non-terminating, needs a coinductive rule); E2 = a derivation
exists but no *short* one (proof-length lower bound); E3 = no derivation in any
model of the theory (a soundness/no-go). Missing: one operational semantics whose
stuck states ARE the four modes — then the whole map is machine-checkable and the
pre-emption record becomes a proof-search fact, not a literature claim.

**Hegelian.** Antithesis: unifying E1 (needs coinduction), E2 (needs a proof-length
metric), and E3 (needs model-theoretic non-derivability) into "one judgment" hides
that these live at three different logical strengths — you cannot decide all three
in one system (E2's length bound is not even a logical property of the judgment).
The negatives bite: the "universal scope theorem" was withdrawn precisely because a
single system claiming all modes over-reached. Synthesis: build the *checker*, but
expect it to have three separate oracles, not one decision procedure.

**Steelman.** Claim: give a small-step semantics where `query ⇓ v` iff declared;
stuck-∞ = E1, stuck-long = E2 (parameterized by a step budget), stuck-⊥ = E3. The
one move: implement it and re-derive one pre-emption as "the checker reaches E2
stuck." Executable disagreement beats prose.

---

## 11. Programming Languages Theorist

**Meta-synthesis.** The whole program is *parametricity*. A capability boundary is
an abstraction boundary; the separating datum is exactly what a parametrically
polymorphic observer *cannot* see by Reynolds' free theorem. "Physical vs declared"
= "genuinely parametric vs merely abstract (hidden but observable via a side
channel)." The tri-repo residue = one free theorem instantiated in three
signatures. The assembly we're missing: state the boundary as a *relational
parametricity theorem* — the datum is invariant under the logical relation induced
by the admissible-menu type, and E1/E2/E3 = three sources of that invariance
(limit, cost, symmetry).

**Hegelian.** Antithesis: parametricity is a property of *pure, total* languages;
E2 (hardness) is quintessentially about effectful cost and E1 about non-termination
— both break the totality parametricity assumes. So "it's all free theorems" is
true only for E3-flavored boundaries. And the honest negative: single-mode novelty
(the free-theorem-for-E3) is exactly the kind of result the literature already has
(information hiding, noninterference). Synthesis: parametricity cleanly captures
E0-vs-E3 (declared-but-observable vs relationally-invariant); E1/E2 need a
*graded/cost-indexed* logical relation, which is a different, less settled tool.

**Steelman.** Claim: the boundary datum `d` satisfies `d(x) = d(R(x))` for the
logical relation `R` induced by the admissible interface type; declared = `R` is
the identity so parametricity is vacuous; forced = `R` is nontrivial. The one move:
pick the interface type whose free theorem *is* the separator, and show E2 requires
moving to a resource-graded relation — locating exactly where purity fails.

---

## 14. Complexity Theorist

**Meta-synthesis.** The forcing trichotomy is a **resource hierarchy with a hard
seam.** E1 (energy) and E2 (computation) are both *quantitative* — real-valued
costs with monotones and conversion rates; you can ask "how much." E3 (symmetry) is
*qualitative* — a 0/1 superselection, no dial. The bold assembly: energy and
computation are one convertible currency (Landauer already bridges them —
erasure costs `kT ln 2`), so E1↔E2 is a genuine resource-theoretic exchange, and
E3 is the *conserved quantity that no amount of currency buys*. That is the
missing story: **two of the three modes are the same resource at different
exchange rates; the third is a selection rule orthogonal to cost.**

**Hegelian.** Antithesis: Landauer bridges E1/E2 only at the reversibility floor;
generic hardness (E2) is not thermodynamic and a hardness *assumption* is not a
physical cost at all — conflating them re-imports the exact error that sent the
computational-arrow work back as REDESIGN/pre-empted. And calling E3 "the
conserved quantity" is just restating symmetry. Synthesis: survives as a
*two-tier* claim — cost-modes (E1,E2) vs selection-modes (E3) — not a single
linear hierarchy. The tiering is the content.

**Steelman.** Claim: define a partial order by free-operation inclusion; E1 and E2
are comparable (there is a conversion monotone, degrading at the Landauer bound),
E3 is incomparable to both (no monotone maps across a superselection sector). The
one move: exhibit *one* boundary convertible E2→E1 and *one* provably
non-convertible E3→(E1,E2) — proving the seam is real, not rhetorical.

---

## 15. Infinite Models Theorist

**Meta-synthesis.** The Declarability Lemma is a *finiteness/compactness* theorem in
disguise: in a finite closed model every separating datum is definable, hence
co-present — declaration is the finite case. Every forcing mode is a distinct way a
property *fails to survive the passage to the infinite*. E1 = not preserved under
direct limits (the boundary is a `lim`/`lim^1` artifact — true at ∞, false at
every finite stage). E3 = not preserved under quotient by an automorphism group
(the datum is not invariant, so it vanishes in the definable-closure of the
symmetric model). The classifying structure the brief asks for (single home for
E1/E2/E3): **the ways a formula fails to be preserved by a class of
model-morphisms** — direct limits, ultraproducts, automorphism quotients.

**Hegelian.** Antithesis: E2 again has no model-theoretic home. Preservation
theorems are about *definability*, not *tractability*; a datum can be first-order
definable and NP-hard to evaluate. So "three ways to fail preservation" is really
two (limit, symmetry) plus an intruder. This matches item-12 precisely: the
cross-repo unification does not type-check because you are trying to type a
complexity fact in a definability language. Synthesis: E1/E3 share a preservation-
theoretic classifier; E2 is a *finite-model-theory / descriptive-complexity* fact
(where complexity does live) — a **different logic**, and that boundary between the
two logics is the real structural discovery.

**Steelman.** Claim: E1 = `φ` not preserved under `lim→`; E3 = `φ` not
`Aut`-invariant; E2 = `φ` definable but its evaluation is not in the low
descriptive-complexity class the admissible menu affords. The one move: name the
two logics (preservation logic vs descriptive complexity) and show no
interpretation embeds one in the other for these boundaries — turning "doesn't
type-check" into a theorem about *which logic each mode inhabits*.

---

## 23. Resource Theory Researcher

**Meta-synthesis.** One frame swallows the trichotomy: **a boundary is physical iff
the separating datum is not a free resource.** Every resource theory = (free
states, free operations, monotones). Pick the free set and the whole taxonomy
falls out: E0-declared = the datum is free (reachable by free operations, just not
requested). E1 = free operations reach it only asymptotically (thermo resource
theory, `nonequilibrium free energy` monotone). E2 = reaching it costs a
computational resource (a complexity monotone). E3 = the resource theory of
asymmetry (WAY theorem; the datum is charged under a conserved quantity, forbidden
by covariance). The assembly we're missing: **the trichotomy is a choice of
free-operation class, and the three classes form a *lattice*, not a chain.**

**Hegelian.** Antithesis: "pick the free set and everything follows" is unfalsifiable
elasticity — any impossibility can be dressed as non-freeness after the fact. The
program already learned this: dressing E3 cross-repo as a resource adapter came
back ABANDON-to-disanalogy (T421). And the three free-operation classes may not
share a partial order at all (14 says E3 is incomparable to E1/E2). Synthesis:
resource theory is the right *language* but its content is only earned by naming
the free set BEFORE seeing the boundary and showing the monotone is non-trivial
and sublinear (else it is absorbed by counting/entropy — the standard failure).

**Steelman.** Claim: three free-operation classes `𝒪_thermo, 𝒪_comp, 𝒪_asym`; a
boundary's mode = the minimal class whose monotone is nonzero on the datum. The one
move: prove the classes are pairwise incomparable (a datum free under one, costly
under another) — establishing a genuine *lattice of forcings*, which is a stronger
and more honest object than "a hierarchy."

---

## 24. Constructor Theory Researcher

**Meta-synthesis.** Constructor theory gives the single predicate the whole program
has been circling: **possible / impossible.** The bold assembly is a *resourced*
constructor theory. Deutsch-Marletto say a task is possible or not; the four-mode
taxonomy is the missing refinement — the **reason-type of an impossibility.** E0 =
task possible (datum co-present, a constructor exists), simply not performed.
E1/E2/E3 = impossible, tagged by the *counterfactual that would restore
possibility*: add unbounded energy/steps (E1), add computational power (E2), break
a symmetry (E3). "Physical vs declared" becomes one crisp statement across all
three forcings: *declared = possible task not done; forced = impossible task,
reason-typed.* That single sentence is what the pieces add up to.

**Hegelian.** Antithesis: constructor theory is deliberately *modal and
resource-free* — its whole selling point is possible/impossible without cost
accounting. Bolting a reason-type/resource onto it is either (a) a genuine
enrichment nobody has done, or (b) smuggling standard resource theory back in and
calling it constructor theory. The honest negative: the "why impossible" classifier
is exactly the universal scope theorem that was *withdrawn as pre-empted*. So the
reason-type may already exist under other names. Synthesis: the *unifying sentence*
survives (one possible/impossible statement across all forcings is real and clean);
the *novelty* survives only if the reason-type is not already a known
impossibility-classification.

**Steelman.** Claim: enrich constructor theory with a labeled impossibility monad —
`Impossible⟨r⟩` for `r ∈ {limit, cost, symmetry}` — where `r` names the free
resource whose addition makes the task possible. This is one predicate over all
three repos. The one move: show that at least the *tagging functor* (impossibility
→ reason-type) is not present in existing constructor-theoretic or resource-
theoretic literature — locate the actual gap.

---

## 26. Philosophy Of Mathematics Researcher

**Meta-synthesis.** "One object, three shadows" is a *structuralist identity claim*
that has never been tested against the structuralist identity criterion. Structural
realism says an object just is its position in a pattern; two descriptions name the
same object iff their positions are isomorphic. The program has three *analogies*
(TaF boundedness, GU generation count, TI crossing) and is treating them as one
object on the strength of resemblance. The missing move is not more analogy — it is
the **isomorphism of roles**: a structure-preserving bijection between the three
role-networks. Assembled correctly, the profound story is that "physical vs
declared" is a claim about *which facts are structural (relabel-invariant) vs which
are merely presentational* — the separator (item 10) is precisely the structural
residue, the part no relabeling can move.

**Hegelian.** Antithesis: T421 is the disproof of the isomorphism — GU's E3 and
TaF's E3 pull opposite ways, so the role-networks are *not* isomorphic; the "one
object" is three objects that rhyme. Item-12 confirms: the identity is untested and
where tested (E3 adapter) it failed. Synthesis: the honest structural claim is
weaker but real — the three share a *sub*structure (the H^1 relabel-invariant
residue) without being isomorphic wholes. "One shadow, three objects," not "one
object, three shadows."

**Steelman.** Claim: define the role-network of each repo as a labeled category;
test for a full faithful functor between them. The one move: don't assert identity —
compute the *maximal common substructure* (the pullback of the three role-networks)
and show it is exactly the global-correlation separator. That pullback, if
non-trivial, is the earned "one object."

---

## 37. Type-System Designer

**Meta-synthesis.** The relabel-proof residue is a **type-preservation invariant**:
the datum that survives every well-typed renaming is what type preservation
protects across compilation/α-renaming. "Physical vs declared" = "invariant under
all admissible relabelings vs an artifact of one labeling." The admissible-menu
class (item 7) is literally the *typing context* that fixes which renamings are
well-typed — change the context (the observable algebra) and the physical/unphysical
line moves, exactly as pseudo-Hermitian QM says. The assembly we're missing: a
subject-reduction theorem where the preserved type IS the boundary, and the three
forcings are three ways preservation can be *witnessed* (limit-indexed types,
cost-indexed/graded types, symmetry-indexed/refinement types).

**Hegelian.** Antithesis: type preservation is a theorem about *one* language's
reduction; a cross-repo invariant would need a shared type system the three repos
demonstrably do not share (that is the "does not type-check" negative, taken
literally). And graded types for E2 are an active research frontier, not a settled
tool — claiming it unifies is premature. Synthesis: within a single repo the
boundary-as-preserved-type is solid and executable; *across* repos it is a
conjecture that the type-check failure has already falsified once.

**Steelman.** Claim: the separator is the unique type invariant under the groupoid
of admissible relabelings; E0 = the invariant is trivial (any labeling works),
forced = nontrivial. The one move: define the relabeling groupoid for one repo and
prove subject reduction — a real theorem — then show the cross-repo functor fails,
making the negative a *typed* statement.

---

## 47. Index Theory Expert

**Meta-synthesis.** This is the crown assembly for 2/5/47. The tri-repo residue, the
H^1 separator, and the admissibility hinge are *one object*: **the index of a
boundary Dirac-type operator.** Atiyah-Singer says analytic index = topological
index — *one integer, computed three ways*; that is precisely "one object, three
shadows" made rigorous. The generation count in GU is famously index-theoretic; TaF
boundedness = dimension of the kernel of an accessibility operator; TI crossing =
spectral flow across the boundary. The admissibility hinge (item 7) = the **choice
of self-adjoint extension / physical metric** that makes the operator elliptic and
the index well-defined — different admissible menus = different boundary conditions
= different index. E1 = index nonzero via an analytic (heat-kernel, `lim`) route;
E3 = index protected by an equivariant/symmetry (`ℤ/2`, spectral-flow) route.

**Hegelian.** Antithesis — two wounds. (1) **E2 has no index-theoretic home.** The
index is a homotopy invariant; computational hardness is not homotopy-invariant, it
is presentation-dependent — there is provably no elliptic operator whose index *is*
a complexity class. So the "one object" excludes E2 by construction. (2) T421: an
indefinite metric means the boundary operator is *not* essentially self-adjoint /
not elliptic in the definite sense — Atiyah-Singer's `ℤ`-valued index degenerates
to a **Krein-space / `ℤ/2` (mod-2) index or a spectral flow**, and that is a
genuinely different invariant. So GU's E3 (indefinite grading) and TaF's E3
(operational, definite) give *different index theories* — the disanalogy is exact,
not incidental. Synthesis: the index object is real and unifies separator + residue
+ hinge for **E1/E3 under a definite admissible metric**; it does *not* reach E2,
and it *bifurcates* at T421 into Z-index vs Z/2-index.

**Steelman.** Claim: the boundary residue is `ind(D_∂)` of a Dirac-type operator
`D_∂` whose boundary condition is fixed by the admissible observable algebra; E1 =
analytic-index route, E3 = equivariant route; the physical/declared line = whether
`ind ≠ 0`. The one move that makes it real AND names the wound: prove `ind(D_∂)`
represents E1/E3 but that **no index represents E2** (complexity is not a homotopy
invariant), and that the indefinite-metric admissible class yields a `ℤ/2` index
distinct from the definite one. That single theorem would convert three "honest
negatives" (E2 pre-empted, E3 disanalogy, unification doesn't type-check) into
*predictions of the index framework* — the strongest available assembly.

---

## 52. Mathematical Minimalist

**Meta-synthesis.** Strip the decoration. You do not need spectral sequences, index
theory, or constructor theory to state the assembly — you need **one map and its
cokernel, plus a grading.** The map: `α: (local sections) → (global section)`
(assemble-the-parts). The residue is `coker(α)` — that single object is the
separator, the tri-repo residue, and the "global property with no local
representative," all at once. The grading (by the free-resource / admissible-menu)
records *where* the cokernel class sits: trivial = E0, and E1/E2/E3 = three
gradings of the same cokernel. The smallest object that unifies the pieces is a
**single non-split short exact sequence** `0 → local → global → coker → 0`;
everything else in this cluster is a different *presentation* of that one
non-splitting.

**Hegelian.** Antithesis: minimality can under-fit. If `coker(α)` is graded by an
*indefinite* form (T421), then "dimension of the cokernel" is not well-defined —
the minimal object lives in a category *without a dimension function*, so the single
number the program wants (is the boundary physical? one bit) may not exist. And a
cokernel does not distinguish E2 from E1/E3 (14, 15, 47 all eject E2) — so the
"one grading" is really two-plus-an-intruder. Synthesis: the minimal object is real
and clarifying — one non-split extension — but its grading is not a chain and its
dimension is not always defined; minimality reveals the *obstruction to a single
number*, which is itself the finding.

**Steelman.** Claim: the entire program reduces to one non-split extension
`0→L→G→C→0` in a graded category; "physical vs declared" = "the extension does not
split." The one move: write that sequence for ONE repo explicitly and check whether
`C` admits a well-defined dimension under the admissible grading — if it does not,
you have *proved* why a single scalar physicality verdict cannot exist (the deepest
possible deliverable from the smallest possible object).

---

## Cluster Meta-Synthesis

Three nominations, ordered by how much they are *structure* vs *rhyme*.

**N1 — The trichotomy is a SPAN, not a hierarchy; E2 is the obstruction to
unification, and that obstruction is the theorem. (STRONGEST — real structure.)**
Backers: 47, 14, 15, 52, 2 (with 6, 23 corroborating from the resource side).
Every geometric/logical lens in this cluster independently *ejects the same mode*:
under index theory, cohomology, model-theoretic preservation, and functorial
(co)limit-preservation, **E1 and E3 share a home (a local-to-global obstruction
computed geometrically) and E2 (computational hardness) has no representative**,
because complexity is presentation-dependent / not homotopy-invariant / not a
definability property. This is not a failure to unify — it is a *falsifiable
prediction*: **no functorial, homotopy-invariant, or preservation-theoretic
invariant will ever represent the E2 boundary**, which exactly explains item-12's
scars (the computational arrow returning pre-empted; the cross-repo unification not
type-checking). Real structure because it makes a concrete, refutable claim and it
*derives* the honest negatives rather than ignoring them. The convergence of five
independent lenses on the same ejected mode is the single most non-obvious finding
in the cluster.

**N2 — Separator + residue + admissibility hinge = ONE index of a boundary
Dirac-type operator; the admissible metric is the self-adjoint extension; T421 is
the Z-index → Z/2-index bifurcation. (STRONG — real structure, but scoped to
E1/E3.)** Backers: 47 lead, 5 (H^1), 2 (cokernel), 6 (equivariant route). This is
the bold "one object, three shadows made rigorous" via Atiyah-Singer (one integer,
three computations). It genuinely fuses item 6 (residue), item 10 (H^1 separator),
and item 7 (which metric is physical = choice of boundary condition), and it turns
the T421 disanalogy into a *precise* statement (definite metric → ℤ index;
indefinite → ℤ/2 / spectral-flow index — different invariants, so GU-E3 ≠ TaF-E3
by theorem, not by vibe). Docked below N1 only because it inherits N1's wound: it
cannot reach E2. Real, but a partial object.

**N3 — Resourced constructor theory: one possible/impossible predicate across all
three forcings, tagged by reason-type. (COHERENT — but closest to rhyme /
re-encoding.)** Backers: 24 lead, 23, 14. The cleanest single *sentence* the pieces
produce ("declared = possible-but-not-done; forced = impossible, reason-typed"),
and it is genuinely unifying at the language level. It is nominated but flagged: it
risks being a re-encoding of standard resource theory in constructor-theoretic
dress, and its novelty is exactly the withdrawn universal-scope classifier — so it
is real *framing* but its *content* is unproven until the impossibility-tagging
functor is shown absent from existing literature.

**One-line honest read.** N1 is real structure and the genuine breakthrough of the
cluster (five lenses, one ejected mode, a falsifiable claim that *predicts* the
program's own negatives). N2 is real structure but scoped — a beautiful partial
object that cannot hold E2. N3 is a real reframe but the thinnest — likely rhyme
until the specific novelty gap is exhibited.
