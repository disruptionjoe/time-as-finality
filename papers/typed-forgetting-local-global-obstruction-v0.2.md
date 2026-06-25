# A Finite Typed Calculus for Local-to-Global Obstruction Under Information-Losing Morphisms

**Version:** 0.2 (neutral synthesis draft)
**Date:** 2026-06-24
**Status:** Internal synthesis draft. Mathematically self-contained. No domain-specific vocabulary required.

---

## Reader orientation

This is a synthesis pass over a finite typed calculus. It is written so that a
mathematician with no knowledge of the originating research program can read it
as ordinary finite combinatorics and category theory. Nothing in the abstract or
body depends on any application domain.

The draft is deliberately conservative about novelty. Where a result is standard,
it is labeled standard. Where a result is bookkeeping forced by a definition, it
is labeled bookkeeping. The honest scope statement in Section 1.3 and the
new-versus-known table in Section 10 are the load-bearing parts of the
calibration. Two prior external reviews of earlier drafts (recorded in
`papers/reviews/`) found that earlier versions mislabeled definitional
consequences and false cohomology claims as theorems. This version removes those
claims and keeps only what survives.

---

## Abstract

We study finite restriction systems: finite sets of sites carrying local
constraint patches, together with a predicate for whether the local constraints
admit a consistent global assignment. We study typed morphisms between such
systems, which carry explicit declarations of which named structure each morphism
preserves and which it forgets. The local-to-global obstruction itself (a system
of locally satisfiable patches with no global assignment) reduces exactly to
signed-graph 2-colorability, which is classical. Our object of study is the
typed layer built on top of this known obstruction: a calculus for tracking when
projection, restriction, or morphism composition creates, hides, displaces, or
reveals the obstruction.

We assemble five components and grade each one honestly. (i) The signed-graph
parity characterization of the obstruction is restated as background. (ii) Typed
morphisms form a category; the obstruction-attribution predicate on that category
is not a Boolean functor. (iii) The natural functorial object in this setting is
the contravariant restriction-of-solutions functor; the covariant
forward-solution-set assignment is provably not a functor. (iv) The finite
results have a sharp finite-to-infinite boundary: the category laws, the
non-functor result, and the cross-level obstruction survive to countable and
infinite analogues by compactness, while the parity characterization is
conditional at the continuum, where a coefficient-blind encoding produces a false
global section. (v) The candidate "typed loss" annotation does not separate from
its neighbor data: the canonical witness obligation factors through the
neighbor-visible realization map, so the loss annotation collapses to a canonical
normal form rather than a prior-art-separated invariant.

The honest summary is that the obstruction mechanism, the parity
characterization, and the categoryhood are known or routine; the contravariant
functor verdict and the finite-to-infinite boundary verdict are clean small
results; and the typed-loss attribution layer is, on current evidence, a
canonical bookkeeping normal form rather than a new invariant. We state the one
genuinely open separation question precisely and record why the most natural
route to it is now structurally closed.

---

## 1. Introduction

### 1.1 The setting

A *finite restriction system* is a finite set of sites, a finite value domain, a
finite collection of local patches (each a constraint on a subset of sites), and
the induced predicate "does a global assignment satisfying all patches exist."
When every patch is individually satisfiable but no global assignment exists, the
system is *obstructed*. This is the finite local-to-global obstruction. It is
old and well understood.

We add one piece of data to the morphisms between such systems. A *typed lossy
morphism* is a site map together with two declarations: the named structure it
*preserves* and the named structure it *forgets*. The motivating question is not
whether an obstruction exists (that is decided by the patches) but whether the
appearance of an obstruction in a target system can be *attributed* to a
particular information-losing morphism into that target.

### 1.2 What we are and are not claiming

We are not claiming to have discovered the local-to-global obstruction, nor a new
obstruction theorem. We are studying a typed accounting layer above a known
obstruction. The contribution, if any, is a calculus for attribution and
displacement of obstruction under typed forgetting, plus two clean structural
verdicts (the functor direction and the finite-to-infinite boundary).

### 1.3 Honest scope statement (new versus known)

This is the most important paragraph in the paper. We separate the components by
their actual standing.

**Known mathematics, restated as background.**

- The obstruction itself is signed-graph imbalance, equivalently unsatisfiability
  of a binary same/different constraint system. This is classical (Harary 1953,
  Zaslavsky 1982), and is a standard special case of the sheaf-theoretic
  global-section obstruction (Abramsky and Brandenburger 2011). We claim nothing
  here.

- That the typed morphisms form a category is routine once composition is
  defined. Any class of objects with associative composition and identities is a
  category. We claim nothing structural from categoryhood alone.

- That the forgotten-structure annotation accumulates by set union along
  composition is true by the definition of composition. It is a commutative
  idempotent monoid annotation, of the same shape as graded or indexed effect
  annotations and provenance accumulation. We claim nothing new here either.

**Clean small results that we do claim, with bounded scope.**

- The obstruction-attribution predicate is not a Boolean functor on the category
  of typed morphisms (Section 5). This is a genuine, if modest, structural
  observation: attribution is an endpoint property of a composed path, not a
  functorial invariant of individual arrows.

- The natural functorial object is the *contravariant* restriction-of-solutions
  functor, and the *covariant* forward-solution-set assignment is provably not a
  functor (Section 6). The reason is monotone constraint accumulation: adding
  constraints can only delete solutions, so a forward map into the solution set
  would have to send a nonempty set to an empty one with no available function.
  The contravariant inclusion of solution sets is total and functorial.

- The finite results have a sharp boundary at infinity (Section 7). The category
  laws, the non-functor result, and the cross-level obstruction survive to
  countable and infinite analogues. The parity characterization survives
  countable scale by compactness but is conditional at the continuum: a
  coefficient-blind scalar encoding reports a false global section despite
  nontrivial monodromy. Countability is never the obstruction; the continuum
  coefficient layer is the only boundary.

**A candidate that does not (yet) separate.**

- The "typed loss" annotation was proposed as a new attribution invariant. On the
  canonical derivation, it does not separate from neighbor-visible data: the
  canonical witness obligation factors through the realization map that records
  exactly what mature provenance, abstract interpretation, lens, effect, and
  categorical neighbors are allowed to read (Section 8). It therefore collapses
  to a canonical normal form, not a prior-art-separated invariant. The honest
  statement is a collapse result, not a separation theorem.

### 1.4 Relation to prior work, in one paragraph

The obstruction sits inside sheaf-theoretic contextuality and CSP/homomorphism
theory. The attribution ambition sits next to database provenance, why-not
provenance, lenses and bidirectional transformations, abstract interpretation,
and graded/indexed effect systems. None of these are claimed as ours, and the
collapse result of Section 8 says explicitly that the canonical loss annotation
is recoverable from the data those neighbors already carry. Section 9 expands
this.

---

## 2. Finite restriction systems

**Definition 2.1 (Finite restriction system).** A finite restriction system is a
tuple `A = (V, Sigma, P)` where `V` is a finite set of sites, `Sigma` is a finite
value domain, and `P = {P_1, ..., P_k}` is a finite set of patches. Each patch
`P_i = (U_i, C_i)` has a support `U_i` (a subset of `V`) and a constraint `C_i`
(a set of admissible joint assignments on `U_i`).

**Definition 2.2 (Global section).** A global section is an assignment
`sigma: V -> Sigma` whose restriction to each `U_i` lies in `C_i`. The system is
*satisfiable* if it has a global section, and *obstructed* otherwise.

**Definition 2.3 (Parity restriction system).** A parity restriction system has
`Sigma = {+1, -1}` and every patch of support 2, with constraint either *same*
(the two sites agree) or *different* (they disagree).

**Example 2.4 (Triangle).** Sites `{a, b, c}` with patches `(a,b)` same, `(b,c)`
same, `(a,c)` different. Each patch is individually satisfiable, but the three
together force `sigma(a) = sigma(b) = sigma(c)` and `sigma(a) != sigma(c)`. No
global section exists. This is the minimal obstruction.

**Definition 2.5 (Signed constraint graph).** For a parity restriction system,
the signed constraint graph `G = (V, E, s)` has an edge for each support pair,
signed `+1` for same and `-1` for different. A cycle is *frustrated* if its signed
edge product is `-1`. `G` is *balanced* if it has no frustrated cycle.

---

## 3. The obstruction is signed-graph imbalance (background)

**Theorem 3.1 (Parity characterization, classical).** A parity restriction
system is satisfiable if and only if its signed constraint graph is balanced.

*Proof.* If a global section exists, the signed product around any cycle telescopes
to `+1`, so no cycle is frustrated. Conversely a balanced signed graph admits a
consistent two-coloring by switching (Zaslavsky 1982), which is a global section.
QED.

**Remark 3.2 (Standing).** Theorem 3.1 is not ours. It is signed-graph balance
(Harary 1953; Zaslavsky 1982), and the equivalence between binary same/different
satisfiability and signed 2-colorability is standard in the CSP and contextuality
literature. We state it only to fix the object that the typed layer sits above.
Arc consistency adds nothing here: both values are always locally supported, so
the obstruction is global, not local.

**Remark 3.3 (Status discipline).** On the declared binary same/different
fragment, satisfiability is decided by the signed-graph parity classifier. This
is a polynomial-style decider over that fragment only. We make no hardness,
NP-hardness, or general-CSP-completeness claim anywhere in this paper.

---

## 4. Typed lossy morphisms and the category Res

**Definition 4.1 (Typed lossy morphism).** Given restriction systems `A` and `B`
over a common value domain, a typed lossy morphism `f: A -> B` is a site map
`phi_f: V_A -> V_B`, a preserved set `pres(f)` (a subset of a fixed finite
universe `S` of structure names), and a forgotten set `forg(f)` (a subset of
`S`), such that every patch of `B` is the image of a patch of `A` under `phi_f`
(patch-compatibility).

**Definition 4.2 (Composition and identity).** For `f: A -> B` and `g: B -> C`,
the composite has site map `phi_g . phi_f`, preserved set
`pres(f) intersect pres(g)`, and forgotten set `forg(f) union forg(g)`. The
identity on `A` has the identity site map, `pres = S`, and `forg = empty`.

**Theorem 4.3 (Category, routine).** Finite restriction systems and typed lossy
morphisms form a category Res.

*Proof.* Site maps compose associatively (function composition); preserved sets
compose associatively (intersection); forgotten sets compose associatively
(union). The identity laws hold because `S` is the unit of intersection and the
empty set is the unit of union, and the identity site map is the unit of function
composition. Patch-compatibility is preserved by composition because the image of
an image is an image. QED.

**Remark 4.4 (Standing).** This is a definition chase, presented as a proposition
rather than a discovery. Categories of structured objects with decorated
morphisms are ubiquitous (restriction categories, decorated cospans, graded and
indexed monads). The point of Res is only that the chosen syntax is closed under
composition, so that the predicate of Section 5 has a category to fail to be a
functor on.

---

## 5. Obstruction attribution is not a Boolean functor

**Definition 5.1 (Attribution predicate).** A typed lossy morphism `f: A -> B` is
an *admissible obstruction attribution*, written `f in Obstr`, if: `A` and `B`
are valid finite restriction systems; `f` is patch-compatible; `forg(f)` is
nonempty; `B` is obstructed; and `A` is satisfiable.

**Theorem 5.2 (Non-functor).** `Obstr: Mor(Res) -> {0, 1}` is not a Boolean
functor from Res to the one-object monoid `({0,1}, and)`.

*Proof.* A Boolean functor must send identities to `1` and satisfy
`F(g . f) = F(f) and F(g)`. Two independent failures occur.

First, the identity law already fails: `forg(id_A) = empty`, so `id_A` is not in
`Obstr`, hence `Obstr(id_A) = 0 != 1`. A solution-set-valued admissibility
predicate that requires nonempty forgetting can never be functorial, because
identities forget nothing.

Second, composition fails even ignoring identities. Take `A` satisfiable with a
global section, an intermediate `M` satisfiable, and a target `B` an obstructed
triangle (Example 2.4). Let `f: A -> M` and `g: M -> B` each forget some named
structure. Then `f` is not in `Obstr` because `M` is not obstructed (the
target-obstruction condition fails), while `g . f: A -> B` is in `Obstr` because
`A` is satisfiable, `B` is obstructed, and the accumulated forgotten set is
nonempty. So `Obstr(g . f) = 1` while `Obstr(f) and Obstr(g) = 0 and 1 = 0`. QED.

**Corollary 5.3 (Endpoint property).** Whether `f in Obstr` depends on the
global-section status of the domain and codomain of `f`, which is not determined
locally at the components of a chain. Attribution is an endpoint property of the
composed path, not a functorial invariant of individual morphisms.

**Remark 5.4 (Three chain shapes).** The non-functoriality has three canonical
shapes. *Emergent*: no proper prefix is in `Obstr` but the full chain is (the
obstruction is invisible at every intermediate level). *Stepwise*: each step is
in `Obstr` and so is the chain. *Absorbed*: an intermediate step is in `Obstr`
but the chain is not, because the final codomain is satisfiable. The absorbed
case is the structural reason nonempty forgetting is necessary but not sufficient
for attribution.

**Remark 5.5 (Honest standing).** This is a small, true observation, not a deep
theorem. The first failure (identities) is immediate from the predicate. The
value of the result is the precise statement that attribution is an
endpoint-of-path property, together with the three-shape taxonomy, which is the
useful part for displacement accounting.

---

## 6. The functorial object is contravariant restriction of solutions

Section 5 says the attribution predicate is not a functor. A natural follow-up is
to ask what *is* functorial in this setting. The answer is clean and is the
contravariant restriction-of-solutions functor.

**Setup 6.1.** Let `States` be the category whose objects are states `S`,
each a finite constraint set over signed variables in `{+1, -1}`, and whose
morphisms `e: S -> S'` are *extensions*, which add one or more new constraints.
Extensions accumulate constraints monotonically: `e: S -> S'` implies the
constraint set of `S` is contained in that of `S'`. Let `F(S)` be the finite set
of global sections of `S`.

**Lemma 6.2 (Monotone accumulation).** If `e: S -> S'` is an extension then
`F(S')` is a subset of `F(S)`. Adding constraints can only delete solutions, never
create them.

**Theorem 6.3 (Covariant assignment is not a functor).** The covariant
assignment `S |-> F(S)` with a forward action on solutions is not a functor
`States -> FinSets`.

*Proof.* Take a one-element solution set `F(S) = {sigma}` and an extension
`e: S -> S'` adding a constraint that `sigma` violates, so `F(S') = empty`. A
covariant action `F(e): F(S) -> F(S')` would be a function from a one-element set
to the empty set, and no such function exists. The failure is upstream of the
identity and composition laws: the proposed arrow has no value at all, because
its required codomain hom-set is empty. (Even before this extreme case, a forward
action is non-total: extensions delete some solutions, which then have no forward
image.) QED.

**Theorem 6.4 (Contravariant restriction of solutions is a functor).** Define
`F_op: States^op -> FinSets` by `F_op(S) = F(S)` on objects and, for the opposite
arrow `e^op: S' -> S` of an extension `e: S -> S'`, the inclusion
`iota_e: F(S') -> F(S)`, `sigma |-> sigma`. Then `F_op` is a functor.

*Proof.* By Lemma 6.2, `F(S')` is a subset of `F(S)`, so the inclusion is a total
well-defined function (when `F(S')` is empty, this is the unique empty function,
which always exists; the typing failure of Theorem 6.3 is exactly cured by
reversing the arrow). The identity extension gives the identity inclusion.
Composition: for `e1: S -> S'` and `e2: S' -> S''` we have
`F(S'') subset F(S') subset F(S)`, and the composite of the two element-fixing
inclusions is the element-fixing inclusion `F(S'') -> F(S)`, which is the
inclusion assigned to the composite extension. So composition is preserved
contravariantly. QED.

**Remark 6.5 (What this earns and what it does not).** Theorem 6.4 identifies the
canonical functorial object: restriction of solutions is the standard
contravariant powerset-monotone functor for any monotonically growing constraint
set. This is the honest categorical posture. It does *not* supply a covariant
functor. Any forward rate of solution creation or destruction lives, at best, in a
partial-map-valued covariant assignment into the category of sets and partial
functions, which is not the object `FinSets` and is left open. The reader should
read Theorem 6.4 as "the right functor here is the obvious contravariant one,"
not as a novel categorical structure. Its value is that it resolves which
direction is functorial, which earlier drafts left ambiguous.

---

## 7. The finite-to-infinite boundary

The results above are finite. We record exactly which survive to countable and
continuous analogues, with a witness on each side of the line. A single
signed-graph parity engine backs the obstruction-flavored results, so the boundary
is shared.

**Theorem 7.1 (Per-result boundary verdicts).** Using a finitely-represented
infinite instance on the surviving side and an explicit obstruction on the other:

- *Category laws (Res):* **survive**. Associativity and the unit laws hold on a
  countably-infinite index-shift site map at every coordinate; the preserved-set
  intersection is associative and unital in the fixed finite name universe. The
  separate question of transfinite colimit closure is an explicit open
  obstruction: the preserved-set intersection of a strictly descending chain can
  empty, so the colimit morphism preserves no name. Boundary-free at the category
  level; colimit closure is open.

- *Non-functor result:* **survives**. The finite functor-failure triple embeds
  unchanged into any infinite-site ambient because the predicate is
  endpoint-pair-local. Only the negative result persists; whether a repaired lax
  or indexed functor exists at infinity is a separate open question.

- *Cross-level obstruction (Section 8.4 below):* **survives**. A planted
  cross-level frustrated triangle stays obstructed at unbounded nesting depth by a
  compactness (Konig) argument. The only way depth appears to dissolve the
  obstruction is by dropping the `-1` cross-level sign, which is the
  coefficient-blind move below, not a real limit effect.

- *Parity characterization (Theorem 3.1):* **conditional**. It survives countable
  scale unconditionally: growing prefixes of an all-same infinite path stay
  satisfiable, a planted finite frustrated triangle is detected in every prefix,
  and the de Bruijn-Erdos / compactness lift carries the finite verdict to the
  countable graph. At the continuum it is conditional: a coefficient-blind scalar
  encoding (same plus same) reports a *false global section* despite monodromy
  `-1`. Carrying the transition/coefficient data is required for any continuum
  statement.

**Theorem 7.2 (The single boundary line).** The only boundary is the continuum
coefficient layer of the shared signed-graph parity engine. Countability is never
the obstruction.

**Remark 7.3 (Honesty guard).** No result is allowed to "survive to the
continuum" by forgetting transition or coefficient data. The continuum failure
mode is exactly a coefficient-blind encoding reporting a global section that does
not exist. This guards against the most natural overclaim, that the finite parity
result lifts verbatim to continuous orientation data. It does not. A
coefficient-aware obstruction object for continuous transition data is the
explicit next construction and is not built here.

---

## 8. The typed-loss annotation collapses to a canonical normal form

This section records the most consequential calibration. The originating program
proposed a "typed loss" object as a new attribution invariant. The honest finding
is a *collapse*, not a separation.

### 8.1 The annotation and its composition law

**Definition 8.1 (Loss annotation).** The loss annotation of `f` is
`LK(f) = forg(f)`, valued in the commutative idempotent monoid
`(2^S, union, empty)`, with `LK(g . f) = LK(f) union LK(g)` and
`LK(id) = empty`.

**Remark 8.2 (Standing).** This composition law is true by the definition of
composition (Definition 4.2). It is a monoid-valued arrow annotation of the same
shape as graded/indexed effect annotations and provenance accumulation. It is
*not* a lax functor to a powerset poset, and it is *not* by itself evidence of a
new invariant. This corrects an earlier draft that overstated it.

### 8.2 The separation question

The only way the loss annotation could be a new invariant is if it separated two
morphisms that are indistinguishable to all mature neighbor frameworks. Make this
precise. Let

```text
nu : Case -> neighbor-visible signature
```

be the realization map recording exactly the data every mature neighbor is
allowed to read: the CSP explanation, the why-not provenance, the abstract
interpretation, the lens, the effect annotation, and the categorical bookkeeping.
The lift table, the ordinary composite map, and the endpoint behavior are all
inside `nu`. Let

```text
obligation : Case -> witness-obligation normal form
```

be the canonical witness obligation derived from the source-lift judgment table.
A separation in the strong sense would be two cases sharing `nu` but receiving
different obligations.

### 8.3 The factorization certificate

**Theorem 8.3 (Obligation factorization, collapse).** The canonical obligation
factors through the neighbor-visible realization map:

```text
obligation = psi . nu
```

Equivalently, `obligation` is constant on every fiber of `nu`. A neighbor handed
only `nu(case)` recomputes the obligation exactly.

*Proof sketch (finite, exhaustive).* The obligation is a deterministic function of
the source-lift judgment table, and the judgment table is contained in the
neighbor signature `nu`. An exhaustive finite check over the canonical case family
confirms that every fiber of `nu` carries a constant obligation and a constant
verdict, and that the obligation is reconstructible from `nu` alone. A positive
control (two cases differing only in a free label and a path tag) receives the
same obligation; free decorations do not move it. QED (as a certified finite
check).

**Corollary 8.4 (No same-neighbor-data separation).** No pair of cases both shares
the neighbor signature and separates while factoring through `nu`. The
search-negative of the earlier finite audit is therefore *forced*, not
accidental: same-neighbor-data separation is impossible in the canonical regime.

**Proposition 8.5 (The only escape is not a separation).** The unique way to break
the factorization is an obligation that reads a source datum exposed by no
neighbor package. Such an obligation does separate, but it is not a prior-art
separation: admitting that datum as legitimate audit data enlarges the neighbor
package from `nu` to `nu'`, and the collapse returns one level up. A would-be
falsifier must argue that some source field used by the obligation is legitimately
outside every mature neighbor package, which prior audits show mature
provenance/effect/abstraction systems absorb once the field is named.

**Remark 8.6 (Honest standing).** Theorem 8.3 is a collapse certificate, not a
promotion. The strongest surviving value of the loss annotation is a canonical,
neighbor-reconstructible normal form for source-derived witness obligations: an
audit and integration vocabulary, not a separation theorem. The loss annotation
is not claimed to be a new mathematical object.

### 8.4 Cross-level attribution

The attribution predicate extends to cross-level morphisms, where patches connect
sites across nesting levels. A planted cross-level frustrated triangle produces a
cross-level obstruction even when each within-level system is satisfiable, and the
attribution requires a nonempty cross-level forgotten set exactly as in the
single-level case. This is the within-level minimal obstruction (Example 2.4)
relocated to the cross-level layer; it survives unbounded nesting depth by the
compactness argument of Theorem 7.1.

---

## 9. Related work

We locate the components precisely, since the calibration depends on it.

- *Sheaf-theoretic contextuality* (Abramsky and Brandenburger 2011; Abramsky,
  Mansfield, Barbosa on the cohomological obstruction). This covers the
  obstruction itself and is the home of the global-section formulation. The
  cohomological obstruction is sufficient but not necessary for contextuality;
  earlier drafts of this material made false general cohomology claims, which are
  removed in this version.

- *Signed graphs and parity CSP* (Harary 1953; Zaslavsky 1982). This is Theorem
  3.1 exactly. We add nothing to it.

- *CSP and homomorphism theory* (Feder and Vardi 1998; Bulatov 2017). The
  obstruction is a binary satisfiability question. The mature language for
  structure-altering maps is homomorphisms, polymorphisms, and reductions, not
  typed forgetting. Our annotation sits next to that theory, not inside it.

- *Provenance and why-not provenance.* The attribution ambition is conceptually
  closest here. The collapse certificate (Theorem 8.3) makes the relationship
  explicit and in the wrong direction for novelty: the canonical obligation is
  recoverable from neighbor-visible (including provenance) data.

- *Lenses, abstract interpretation, graded and indexed effects.* These already
  formalize structured forgetting, precision loss, and monoidal annotation
  accumulation. The loss annotation is a particularly simple instance (a set under
  union); it carries less than provenance semirings.

- *Restriction categories* (Cockett and Lack 2002). A terminology caution: our
  "restriction system" is not the categorical "restriction category" of partial
  maps. Our morphisms are total and carry forgetting declarations.

---

## 10. New versus known, in one table

| Component | Standing | One-line justification |
|---|---|---|
| Local-to-global obstruction = signed-graph imbalance (Thm 3.1) | Known | Harary 1953, Zaslavsky 1982; standard CSP/contextuality special case. |
| Typed morphisms form a category Res (Thm 4.3) | Routine | Definition chase; closure under composition only. |
| Loss annotation composes by union (Def 8.1) | Bookkeeping | True by definition of composition; a monoid annotation. |
| Attribution predicate is not a Boolean functor (Thm 5.2) | Small new result | Identity already breaks it; precise endpoint-of-path statement plus three-shape taxonomy. |
| Covariant solution-set assignment is not a functor (Thm 6.3) | Small new result | Forward map into solutions has empty-codomain typing failure under constraint addition. |
| Contravariant restriction of solutions is the functor (Thm 6.4) | Clean, canonical | Standard contravariant powerset-monotone functor; resolves the direction question. |
| Finite-to-infinite boundary verdicts (Thm 7.1, 7.2) | Clean small result | Category laws / non-functor / cross-level survive; parity is continuum-conditional. |
| Typed-loss annotation is a new invariant | Not earned | Collapse certificate (Thm 8.3): obligation factors through neighbor data. |

---

## 11. The one open separation question, stated precisely

The single genuinely open question is whether *any* attribution invariant
separates from the neighbor-visible data in this setting.

**Open Problem 11.1 (Separation or collapse).** Does there exist an attribution
map on typed lossy morphisms that (a) separates two cases sharing the full
neighbor-visible signature `nu`, and (b) is itself a function of `nu`? Theorem 8.3
shows these two requirements are contradictory for the canonical witness-obligation
construction. A positive answer must therefore come from *outside* that canonical
construction, and must avoid the escape of Proposition 8.5 (reading a source field
that any mature neighbor would absorb once named).

This is the honest frontier. The natural route to separation (same-neighbor-data
quotient on the canonical derivation) is structurally closed. Either a genuinely
external construction separates, in which case there is a new invariant, or every
natural construction collapses, in which case the calculus is a canonical
bookkeeping normal form over known obstruction theory. Both outcomes are
informative.

---

## 12. Conclusion

We have assembled a finite typed calculus for tracking when projection,
restriction, or composition creates, hides, displaces, or reveals a finite
local-to-global obstruction, and we have graded each component honestly. The
obstruction mechanism and its parity characterization are known. Categoryhood and
the loss annotation are routine. The two clean small results are the
non-functoriality of attribution and the verdict that the functorial direction is
contravariant restriction of solutions. The finite-to-infinite boundary is sharp
and sits at the continuum coefficient layer. The proposed typed-loss invariant
collapses to a canonical normal form: the canonical witness obligation factors
through the neighbor-visible data map, so no same-neighbor-data separation exists
in the canonical regime.

The program's defensible thesis is narrow and clear: an obstruction is not
informative without an attribution account, the canonical attribution account is a
neighbor-reconstructible normal form, and the open question is whether any
attribution invariant escapes that normal form. We do not overstate it. The
obstruction is old; the bookkeeping is canonical; the separation is open.

---

## References

Abramsky, S. and Brandenburger, A. (2011). The sheaf-theoretic structure of
non-locality and contextuality. New Journal of Physics, 13, 113036.

Bulatov, A. (2017). A dichotomy theorem for nonuniform CSPs. Proceedings of FOCS
2017, 319-330.

Cockett, J.R.B. and Lack, S. (2002). Restriction categories I: categories of
partial maps. Theoretical Computer Science, 270(1-2), 223-259.

Feder, T. and Vardi, M.Y. (1998). The computational structure of monotone monadic
SNP and constraint satisfaction. SIAM Journal on Computing, 28(1), 57-104.

Harary, F. (1953). On the notion of balance of a signed graph. Michigan
Mathematical Journal, 2(2), 143-146.

MacLane, S. (1971). Categories for the Working Mathematician. Springer-Verlag.

Zaslavsky, T. (1982). Signed graphs. Discrete Applied Mathematics, 4(1), 47-74.

---

## Appendix A: Provenance of the components

For internal traceability only. The neutral statements above are drawn from the
following finite executable checks, none of which require any application-domain
vocabulary to state.

| Section | Component | Source check |
|---|---|---|
| 3 | Parity characterization | T39 (signed-graph parity, poly-decider on the binary fragment) |
| 4 | Category Res | T41 (associativity and unit laws verified on finite witnesses) |
| 5 | Non-functor | T41 (Boolean-and functor law violated on the emergent witness) |
| 6 | Contravariant functor verdict | T221 (covariant refuted by empty-codomain counterexample; contravariant proven) |
| 7 | Finite-to-infinite boundary | T222 (per-result two-sided witnesses; continuum coefficient layer is the line) |
| 8 | Loss-annotation collapse | T220 (obligation factorization certificate); T127 (search-negative it upgrades) |
| 8.4 | Cross-level obstruction | T40 (holonic emergence; cross-level forgotten set necessary) |

A note on an adjacent line not used in this paper. A separate finite enumeration
of a uniform ordinal ensemble (used elsewhere in the originating program for a
geometric question outside this paper's scope) returned a finite no-go: through an
exact eight-element enumeration the band-and-deletion-stable survivor fraction is
monotone decreasing (about 0.036, then 0.034, then 0.009) with every survivor a
thin height-bounded poset. That result is not part of this typed-calculus paper.
It is mentioned only to record that the originating program does not lean on it
for any claim made here, and that this paper makes no geometric, dimensional, or
continuum-construction claim of any kind.
