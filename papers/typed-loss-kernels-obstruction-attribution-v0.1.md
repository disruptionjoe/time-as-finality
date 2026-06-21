# Typed Loss Kernels and Obstruction Attribution
# in Categories of Finite Restriction Systems

**Reviewer calibration notice (2026-06-20):** this draft is review-blocked, not
a submission-ready theorem preprint. External reviews in
[`papers/reviews/external-review-typed-loss-kernels-v0.1.md`](reviews/external-review-typed-loss-kernels-v0.1.md)
and
[`papers/reviews/skeptical-review-typed-forgetting-v0.1.md`](reviews/skeptical-review-typed-forgetting-v0.1.md)
found that several claims below are definitional, misformulated, or false as
stated. The loss-kernel composition law should be read as a monoid-valued arrow
annotation, not as a lax functor to a powerset poset; the path-dependence
biconditional is a consequence of the chosen admissibility predicate; and the
cohomology/failure-type monotonicity claims in Section 7 are not usable without
new hypotheses and counterexample checks.

**Version:** 0.1 (preprint draft)
**Date:** 2026-06-20
**Status:** External review draft — mathematically self-contained; no domain-specific vocabulary required

---

## Abstract

We study **finite restriction systems** — finite sets of sites equipped with local
constraint patches — and **typed lossy morphisms** between them, which carry explicit
declarations of preserved and forgotten structure. While the local-to-global gluing
obstruction in such systems reduces to signed-graph parity constraint satisfiability
(a known mechanism), we show that admissible **attribution** of obstruction under
information-losing projection requires additional typed data not expressible in
standard constraint-satisfaction frameworks.

The current calibrated results and blockers are:

1. **(Category bookkeeping.)** Typed restriction morphisms form a category **Res** under composition
   by site-map composition, set-intersection of preserved structure, and set-union
   of forgotten structure. This is a closure check for the chosen formalism, not
   a standalone categorical novelty claim.

2. **(CSP Correspondence.)** The local-to-global gluing obstruction is equivalent
   to the unsatisfiability of a binary signed parity CSP. This reduction is not new;
   we state it precisely to isolate the attribution layer that follows.

3. **(Non-Functor Theorem.)** Obstruction admissibility — the predicate that a
   morphism explains why its target system lacks a global section — is *not* a Boolean
   functor on **Res**. Endpoint admissibility is a property of composed paths, not a
   functorial invariant of individual morphisms.

4. **(Loss-kernel annotation.)** The loss kernel $LK(f) = \text{forgotten\_structure}(f)$
   is an arrow annotation valued in the commutative idempotent monoid
   $(2^S, \cup, \emptyset)$:
   $LK(g \circ f) = LK(f) \cup LK(g)$. For paths with fixed endpoints and fixed
   endpoint admissibility conditions, the current predicate varies exactly with
   the empty/non-empty loss annotation. This is evidence for bookkeeping
   discipline, not by itself evidence that `LossKernel` is a new mathematical
   invariant.

5. **(Review-blocked cohomology claims.)** The draft's failure-type monotonicity
   and cover-topology claims are not established. External review gives direct
   objections to Theorems 7.7, 7.9, and 7.12. Section 7 now records these as
   failed draft claims and minimum repair obligations, not results.

We state the **Typed Forgetting Attribution Conjecture** as the central open problem:
that non-empty loss kernel naming attribution-relevant structure is necessary for
admissible obstruction attribution.

Executable models verify finite witness families, but they do not rescue the
review-blocked general cohomology claims. Algebraic proofs are given only for the
bookkeeping structure that remains after this calibration.

---

## 1. Introduction

### 1.1 The Problem

Given two finite systems $A$ and $B$ connected by an information-losing morphism $f:
A \to B$, when is the obstruction in $B$ — the failure of $B$ to admit a globally
consistent solution — *attributable* to $f$?

The obstruction itself (that $B$ has no global section) is well-studied. It reduces
to a known combinatorial mechanism: signed-graph parity conflict, equivalent to binary
CSP unsatisfiability. This paper does not claim to study this obstruction. It studies
the **attribution question**: given that $A$ is satisfiable, $B$ is not, and $f$ is
an information-losing map between them, what additional structure on $f$ makes the
attribution valid?

The answer is not "nothing additional." The non-functor observation (Section 5) shows
that obstruction admissibility is not determined by the endpoints alone and not
preserved under composition. A morphism $f: A \to B$ may be individually inadmissible
while the composed morphism $g \circ f: A \to C$ is admissible. External review
weakens the older wording here: this is a structural property of the paper's
chosen attribution predicate, but not yet theorem-level evidence for a new
obstruction theory.

### 1.2 What Is New

The objects and machinery in this paper draw from established mathematics:

- Finite constraint satisfaction problems (CSP) [Feder-Vardi 1998; Bulatov 2017]
- Signed graphs and signed parity [Zaslavsky 1982]
- Sheaf-theoretic obstruction (Čech cohomology) [Bott-Tu 1982; Abramsky-Brandenburger 2011]
- Category theory [MacLane 1971]

What we study on top of this machinery:

1. **Typed annotation of morphisms** with preserved and forgotten structure declarations
2. **Loss kernels** as a composable monoid-valued annotation whose promotion beyond
   metadata remains open
3. **Path-dependent admissibility** as a consequence of the chosen annotation
   predicate, not yet as a quotient-surviving theorem
4. **Failure-type tracking** as a failed draft theorem family requiring narrower
   hypotheses before any monotonicity claim can be restored

We believe the contribution is the **typed attribution layer**, not the obstruction
mechanism beneath it. Section 9 (Related Work) expands on this.

### 1.3 Scope and Notation

Throughout this paper:

- All sets are finite unless stated otherwise.
- $S$ denotes a fixed finite universe of **structure names** (string labels for the
  types of information a morphism may preserve or forget).
- $2^S$ denotes the power set of $S$, ordered by inclusion.
- We write $\subseteq$, $\cup$, $\cap$, $\emptyset$ for the standard set operations.
- All morphism composition is written in diagrammatic order: $f;g$ or $g \circ f$
  for "first $f$, then $g$."

---

## 2. Finite Restriction Systems

### 2.1 Core Definitions

**Definition 2.1 (Finite restriction system).** A *finite restriction system* is a
tuple $\mathcal{A} = (V, \Sigma, \mathcal{P})$ where:

- $V$ is a finite set of *sites*;
- $\Sigma$ is a finite *value domain* (we use $\{+1, -1\}$ throughout for concreteness,
  but the theory applies to any finite $\Sigma$);
- $\mathcal{P} = \{P_1, \ldots, P_k\}$ is a finite collection of *patches*, where
  each patch $P_i = (U_i, C_i)$ consists of:
  - a subset $U_i \subseteq V$ (the *support* of the patch),
  - a constraint $C_i \subseteq \Sigma^{U_i}$ (the admissible joint assignments
    on those sites).

**Definition 2.2 (Section and global section).** A *local section* over a subset
$U \subseteq V$ is an assignment $\sigma_U: U \to \Sigma$. A local section $\sigma_{U_i}$
*satisfies patch* $P_i = (U_i, C_i)$ if $\sigma_{U_i} \in C_i$. A *global section*
of $\mathcal{A}$ is an assignment $\sigma: V \to \Sigma$ such that for every patch $P_i$,
the restriction $\sigma|_{U_i}$ satisfies $P_i$. The system $\mathcal{A}$ is *satisfiable*
if it has a global section, and *obstructed* otherwise.

**Definition 2.3 (Parity constraint system).** A *parity restriction system* is a
finite restriction system in which $\Sigma = \{+1, -1\}$ and every patch has support
of size 2, with constraint $C_i \in \{\{(+1,+1), (-1,-1)\}, \{(+1,-1), (-1,+1)\}\}$.
We call these *same* (agreeing) and *different* (disagreeing) patches respectively.

**Remark 2.4.** The parity restriction systems are the primary setting for our results.
The constraint language is restrictive enough to admit a clean combinatorial
characterization (Theorem 3.1) while being expressive enough to model the witnesses
of Sections 6 and 7.

**Example 2.5 (Triangle system).** Let $V = \{a, b, c\}$ with patches:
- $(a,b)$: same, $(b,c)$: same, $(a,c)$: different.

The constraints force $\sigma(a) = \sigma(b)$, $\sigma(b) = \sigma(c)$, $\sigma(a) \neq
\sigma(c)$. These are mutually contradictory; no global section exists.

**Example 2.6 (Four-site satisfiable system).** Let $V = \{a, b, c, d\}$ with
patches: $(a,b)$: same, $(b,c)$: same, $(c,d)$: same, $(a,d)$: same. Set $\sigma \equiv +1$.
This is a global section.

### 2.2 The Signed Constraint Graph

For a parity restriction system $\mathcal{A} = (V, \{+1,-1\}, \mathcal{P})$, the
*signed constraint graph* is the graph $G = (V, E, s)$ where:
- $E$ contains an edge $\{u,v\}$ for each patch with support $\{u,v\}$;
- $s: E \to \{+1, -1\}$ assigns $+1$ to same-patches and $-1$ to different-patches.

A *frustrated cycle* in $G$ is a cycle whose signed product $\prod_{e \in \text{cycle}} s(e)$
equals $-1$. A signed graph is *balanced* if it has no frustrated cycles.

---

## 3. Obstruction and Satisfiability

**Theorem 3.1 (CSP Correspondence).** A parity restriction system $\mathcal{A}$ is
satisfiable if and only if its signed constraint graph $G$ is balanced (has no
frustrated cycle). Equivalently, $\mathcal{A}$ is obstructed if and only if $G$
contains at least one frustrated cycle.

*Proof.* ($\Rightarrow$) Suppose $\sigma: V \to \{+1,-1\}$ is a global section. For
any cycle $(v_0, v_1, \ldots, v_k = v_0)$ in $G$, the signed product around the cycle
is $\prod_i s(v_i, v_{i+1})$. Each same-edge contributes $\frac{\sigma(v_{i+1})}{\sigma(v_i)}$
and each different-edge contributes $\frac{-\sigma(v_{i+1})}{\sigma(v_i)}$. The total
product is $\frac{\sigma(v_k)}{\sigma(v_0)} \cdot (\text{signs}) = 1 \cdot (\text{signs})$
since $v_k = v_0$. Under the encoding $s(e) = +1$ for same and $s(e) = -1$ for
different, the product for any closed walk in an assignment-consistent system is $+1$.
So $G$ is balanced.

($\Leftarrow$) If $G$ is balanced, by the theory of signed graphs [Zaslavsky 1982],
$G$ is bipartite under its signing: there exists a two-coloring $\sigma: V \to \{+1,-1\}$
consistent with all edge signs. This $\sigma$ is a global section. $\square$

**Remark 3.2 (Prior art).** Theorem 3.1 is not new. The equivalence between
local-to-global consistency of binary constraints and 2-colorability of signed graphs
is a standard CSP result. Signed-graph balance is classical [Harary 1953]. The CHSH
inequality (Section 6.2) and more general contextuality results (Abramsky-Brandenburger
2011) establish H¹ obstruction in the sheaf-theoretic generalization of this framework.
We state Theorem 3.1 to fix notation and to emphasize that *what follows* concerns the
attribution layer built above this known mechanism, not the obstruction itself.

**Remark 3.3 (Arc consistency adds nothing).** Arc consistency — the property that
every value in the domain of each variable is supported by some assignment to its
neighbors — is trivially satisfied for parity systems: both $+1$ and $-1$ are always
locally consistent. Arc consistency propagation adds no information for this constraint
language. The obstruction is a global, not local, phenomenon.

---

## 4. Typed Lossy Morphisms

### 4.1 Definitions

**Definition 4.1 (Typed lossy morphism).** Given restriction systems $\mathcal{A} =
(V_A, \Sigma, \mathcal{P}_A)$ and $\mathcal{B} = (V_B, \Sigma, \mathcal{P}_B)$, a
*typed lossy morphism* $f: \mathcal{A} \to \mathcal{B}$ consists of:

- a *site map* $\varphi_f: V_A \to V_B$;
- a *preserved structure* $\text{pres}(f) \subseteq S$;
- a *forgotten structure* $\text{forg}(f) \subseteq S$;

such that every patch of $\mathcal{B}$ is expressible as the image of a patch of
$\mathcal{A}$ under $\varphi_f$ (the morphism is *patch-compatible*).

**Definition 4.2 (Loss kernel).** The *loss kernel* of $f$ is:

$$LK(f) = \text{forg}(f) \in 2^S$$

regarded as a subset of the structure-name universe $S$.

**Definition 4.3 (Composition of typed lossy morphisms).** For $f: \mathcal{A} \to
\mathcal{B}$ and $g: \mathcal{B} \to \mathcal{C}$, the *composite* $g \circ f:
\mathcal{A} \to \mathcal{C}$ is defined by:

$$\varphi_{g \circ f} = \varphi_g \circ \varphi_f$$

$$\text{pres}(g \circ f) = \text{pres}(f) \cap \text{pres}(g)$$

$$\text{forg}(g \circ f) = \text{forg}(f) \cup \text{forg}(g)$$

Equivalently: $LK(g \circ f) = LK(f) \cup LK(g)$.

**Definition 4.4 (Identity morphism).** For each $\mathcal{A}$, the *identity
morphism* $\text{id}_{\mathcal{A}}: \mathcal{A} \to \mathcal{A}$ has site map $\text{id}_{V_A}$,
$\text{pres}(\text{id}_\mathcal{A}) = S$, $\text{forg}(\text{id}_\mathcal{A}) = \emptyset$,
and therefore $LK(\text{id}_\mathcal{A}) = \emptyset$.

### 4.2 The Category Res

**Theorem 4.5 (Category).** Finite restriction systems and typed lossy morphisms form
a category **Res** under the composition of Definition 4.3.

*Proof.* We verify associativity and the unit laws.

*Associativity.* Let $f: \mathcal{A} \to \mathcal{B}$, $g: \mathcal{B} \to \mathcal{C}$,
$h: \mathcal{C} \to \mathcal{D}$. Then:

- Site maps: $\varphi_{h \circ (g \circ f)} = \varphi_h \circ (\varphi_g \circ \varphi_f)
  = (\varphi_h \circ \varphi_g) \circ \varphi_f = \varphi_{(h \circ g) \circ f}$,
  since function composition is associative.
- Preserved structure: $\text{pres}(h \circ (g \circ f)) = \text{pres}(g \circ f) \cap
  \text{pres}(h) = (\text{pres}(f) \cap \text{pres}(g)) \cap \text{pres}(h)
  = \text{pres}(f) \cap (\text{pres}(g) \cap \text{pres}(h)) = \text{pres}((h \circ g)
  \circ f)$, since set intersection is associative.
- Forgotten structure: $LK(h \circ (g \circ f)) = LK(f) \cup LK(g) \cup LK(h) =
  LK((h \circ g) \circ f)$, since set union is associative.

*Left unit.* $\text{id}_\mathcal{B} \circ f$ has site map $\text{id}_{V_B} \circ \varphi_f
= \varphi_f$; preserved structure $\text{pres}(f) \cap S = \text{pres}(f)$; forgotten
structure $\text{forg}(f) \cup \emptyset = \text{forg}(f)$. So $\text{id}_\mathcal{B}
\circ f = f$.

*Right unit.* $f \circ \text{id}_\mathcal{A}$ has site map $\varphi_f \circ \text{id}_{V_A}
= \varphi_f$; preserved structure $S \cap \text{pres}(f) = \text{pres}(f)$; forgotten
structure $\emptyset \cup \text{forg}(f) = \text{forg}(f)$. So $f \circ
\text{id}_\mathcal{A} = f$. $\square$

*Computational verification:* Associativity verified on four triple-composition witness
families; left and right unit laws verified on five morphism witnesses each.

---

## 5. Obstruction Attribution

### 5.1 Admissibility Conditions

**Definition 5.1 (Admissible obstruction attribution).** A typed lossy morphism $f:
\mathcal{A} \to \mathcal{B}$ is an *admissible obstruction attribution* (we write
$f \in \text{Obstr}$) if all of the following conditions hold:

- **(AC1)** $\mathcal{A}$ is a valid finite restriction system.
- **(AC2)** $\mathcal{B}$ is a valid finite restriction system.
- **(AC3)** $f$ is patch-compatible (definable).
- **(AC5)** $LK(f) \neq \emptyset$ (f forgets at least one named structure element).
- **(AC6)** $\mathcal{B}$ is obstructed (has no global section).
- **(AC7)** $\mathcal{A}$ is satisfiable (has a global section).

**Remark 5.2 (On AC4).** A fourth condition (AC4: local compatibility of the site map)
derives from AC6 in the parity-system semantics. We omit it to avoid redundancy.

**Remark 5.3 (Interpretation).** The predicate Obstr captures "the obstruction in $\mathcal{B}$
is attributable to $f$." It requires: (a) $\mathcal{A}$ had a solution (AC7); (b) the
solution was lost — $\mathcal{B}$ has none (AC6); (c) the morphism $f$ is the definable
transition (AC3); and (d) $f$ carries explicitly named forgotten structure (AC5). The
content of the paper is largely about what happens when we study this predicate as a
function on **Res**.

### 5.2 The Non-Functor Theorem

**Theorem 5.4 (Non-Functor).** The predicate $\text{Obstr}: \text{Mor}(\textbf{Res})
\to \{0,1\}$ is not a Boolean functor from **Res** to the category $(\{0,1\}, \wedge)$.

*Proof.* A Boolean functor $F: \textbf{Res} \to (\{0,1\}, \wedge)$ must satisfy:

$$F(g \circ f) = F(f) \wedge F(g) \quad \text{for all composable } f, g$$

We exhibit a witness in which $\text{Obstr}(g \circ f) = 1$ but $\text{Obstr}(f) = 0$.

*Construction (Emergent Obstruction Witness).* Let:

- $\mathcal{A}$ = source system with sites $\{a_1, a_2, a_3\}$ and a global section.
- $\mathcal{M}$ = intermediate system with sites $\{m_1, m_2, m_3\}$ and a global
  section (intermediate is satisfiable).
- $\mathcal{B}$ = target system with sites $\{b_1, b_2, b_3\}$ with patches forming
  a frustrated triangle: $(b_1,b_2)$:same, $(b_2,b_3)$:same, $(b_1,b_3)$:different.
  By Theorem 3.1, $\mathcal{B}$ is obstructed.
- $f: \mathcal{A} \to \mathcal{M}$: $LK(f) \neq \emptyset$ (forgets some structure). But
  $\mathcal{M}$ is satisfiable, so AC6 fails for $f$. Therefore $f \notin \text{Obstr}$.
- $g: \mathcal{M} \to \mathcal{B}$: $LK(g) \neq \emptyset$ (forgets additional structure).
  $\mathcal{M}$ has a global section (AC7 for $g$); $\mathcal{B}$ is obstructed (AC6
  for $g$). So $g \in \text{Obstr}$.
- $g \circ f: \mathcal{A} \to \mathcal{B}$: $LK(g \circ f) = LK(f) \cup LK(g) \neq
  \emptyset$. $\mathcal{A}$ has a global section (AC7). $\mathcal{B}$ is obstructed
  (AC6). So $g \circ f \in \text{Obstr}$.

In this witness: $\text{Obstr}(f) = 0$, $\text{Obstr}(g) = 1$, $\text{Obstr}(g \circ f) = 1$.
A Boolean functor would require $\text{Obstr}(g \circ f) = \text{Obstr}(f) \wedge
\text{Obstr}(g) = 0 \wedge 1 = 0$. This contradicts $\text{Obstr}(g \circ f) = 1$. $\square$

*Second witness (Emergent-only).* There exist chains $f_1, \ldots, f_n$ where
$\text{Obstr}(f_k) = 0$ for all $k$ (because each intermediate target is satisfiable)
but $\text{Obstr}(f_n \circ \cdots \circ f_1) = 1$ (because the final target is
obstructed). This shows: even $\text{Obstr}(f) \wedge \text{Obstr}(g) = 0 \wedge 0 = 0$
cannot account for $\text{Obstr}(g \circ f) = 1$.

**Corollary 5.5 (Endpoint property).** Obstruction admissibility is an *endpoint
property* of composed morphisms, not a functorial invariant of individual morphisms.
Whether $f \in \text{Obstr}$ depends on the global-section status of $\text{dom}(f)$
and $\text{cod}(f)$, which is not determined locally at the components of a chain.

**Remark 5.6 (Three chain shapes).** The non-functor theorem admits three canonical
chain shapes, verified computationally:

- *Emergent obstruction:* $f \notin \text{Obstr}$ for all proper prefixes; full chain
  $\in \text{Obstr}$. (Obstruction invisible at intermediate levels.)
- *Stepwise propagation:* each step $f_k \in \text{Obstr}$ (each intermediate target
  is obstructed); full chain $\in \text{Obstr}$.
- *Absorbed obstruction:* obstruction appears at an intermediate level (some $f_k
  \in \text{Obstr}$) but disappears by the endpoint (full chain $\notin \text{Obstr}$,
  because the final target is not obstructed).

The absorbed case is crucial for the conjecture in Section 8: it shows that non-empty
$LK(f)$ is necessary but not sufficient for $f \in \text{Obstr}$. AC6 (target
obstruction) is co-required.

---

## 6. Loss Kernels and Path-Dependent Attribution

### 6.1 Loss Kernels as Monoid-Valued Annotations

**Proposition 6.1 (Loss Kernel Monoid-Valued Annotation).** The loss kernel assignment $LK:
\text{Mor}(\textbf{Res}) \to 2^S$ satisfies:

1. $LK(\text{id}_\mathcal{A}) = \emptyset$ for all objects $\mathcal{A} \in \textbf{Res}$.
2. $LK(g \circ f) = LK(f) \cup LK(g)$ for all composable $f: \mathcal{A} \to \mathcal{B}$
   and $g: \mathcal{B} \to \mathcal{C}$.

*Proof.*

(1) By Definition 4.4, $\text{forg}(\text{id}_\mathcal{A}) = \emptyset$, so
$LK(\text{id}_\mathcal{A}) = \emptyset$.

(2) By Definition 4.3, $\text{forg}(g \circ f) = \text{forg}(f) \cup \text{forg}(g)$.
Therefore $LK(g \circ f) = \text{forg}(g \circ f) = \text{forg}(f) \cup \text{forg}(g)
= LK(f) \cup LK(g)$. $\square$

**Remark 6.2 (Not a lax-functor claim).** External review correctly flags the
older lax-functor wording as misformulated. What is established here is weaker
and cleaner: $LK$ is an arrow annotation valued in the one-object category
associated to the commutative idempotent monoid $(2^S, \cup, \emptyset)$. Loss
accumulates independently at each step because composition is defined by union.
This is useful bookkeeping, but it does not by itself promote `LossKernel` beyond
standard effect/provenance-style annotation machinery.

**Corollary 6.3 (Monotonicity).** For any composable chain $f_1, \ldots, f_n$ and
any prefix $1 \leq k < n$:

$$LK(f_1) \cup \cdots \cup LK(f_k) \subseteq LK(f_1) \cup \cdots \cup LK(f_n)$$

Loss accumulated along a path can only grow, never shrink.

### 6.2 Typed Transport Graphs

**Definition 6.4 (Typed transport graph).** A *typed transport graph* $\mathcal{G}
= (\mathcal{L}, \mathcal{T})$ is a finite directed graph where:

- $\mathcal{L}$ is a finite set of *layers* (restriction systems $\mathcal{L}_i$);
- $\mathcal{T}$ is a finite set of *typed lossy morphisms* $t_{ij}: \mathcal{L}_i \to
  \mathcal{L}_j$ (one per directed edge).

A *path* from layer $A$ to layer $B$ is a sequence of morphisms $P = (t_1, t_2,
\ldots, t_n)$ with $\text{dom}(t_1) = A$, $\text{cod}(t_n) = B$, and $\text{cod}(t_k)
= \text{dom}(t_{k+1})$ for all $k$. The *composed loss kernel* of $P$ is:

$$LK(P) = \bigcup_{k=1}^n LK(t_k)$$

**Definition 6.5 (Endpoint conditions).** For a fixed pair $(A, B)$ of layers in a
typed transport graph, the *endpoint admissibility conditions* are:
- AC1: $A$ is a valid restriction system.
- AC2: $B$ is a valid restriction system.
- AC6: $B$ is obstructed.
- AC7: $A$ is satisfiable.

These conditions depend only on the systems $A$ and $B$, not on the path between them.

**Definition 6.6 (Path admissibility).** A path $P$ from $A$ to $B$ is *admissible*
($P \in \text{Obstr}$) if conditions AC1, AC2, AC3, AC5, AC6, AC7 all hold for the
composed morphism $P = t_n \circ \cdots \circ t_1$.

### 6.3 Path-Dependence Biconditional

**Proposition 6.7 (Path-Dependence Predicate Unfolding).** Let $(A, B)$ be a fixed pair of
layers in a typed transport graph satisfying the endpoint conditions AC1, AC2, AC6, AC7.
Let $P_1$ and $P_2$ be two paths from $A$ to $B$. Then:

$$P_1 \in \text{Obstr} \;\text{ and }\; P_2 \notin \text{Obstr}
\quad \iff \quad
LK(P_1) \neq \emptyset \;\text{ and }\; LK(P_2) = \emptyset$$

*Proof.* Since AC1, AC2, AC6, AC7 are endpoint conditions, they hold or fail the same
way for all paths from $A$ to $B$. The only path-varying admissibility condition is
AC5: $LK(P) \neq \emptyset$. Therefore:

- If $LK(P_1) \neq \emptyset$ and $LK(P_2) \neq \emptyset$: both satisfy AC5 $\Rightarrow$
  both admit $P_1, P_2 \in \text{Obstr}$ (or both fail some endpoint condition — but
  endpoint conditions are equal). No asymmetry.
- If $LK(P_1) = \emptyset$ and $LK(P_2) = \emptyset$: both fail AC5 $\Rightarrow$ both
  $P_1, P_2 \notin \text{Obstr}$.
- If $LK(P_1) \neq \emptyset$ and $LK(P_2) = \emptyset$: $P_1$ satisfies AC5 $\Rightarrow
  P_1 \in \text{Obstr}$; $P_2$ fails AC5 $\Rightarrow P_2 \notin \text{Obstr}$.
  The biconditional holds in the $(\Rightarrow)$ direction.
- The $(\Leftarrow)$ direction: if $P_1 \in \text{Obstr}$ and $P_2 \notin \text{Obstr}$,
  then since all endpoint conditions hold for both, the only difference must be AC5:
  $LK(P_1) \neq \emptyset$ and $LK(P_2) = \emptyset$. $\square$

**Corollary 6.8.** For a fixed $(A, B)$ pair satisfying the endpoint conditions,
*path-dependent obstruction admissibility is exactly the empty/non-empty distinction
in composed loss kernels for this predicate and fixture family.* This is a
definition-driven diagnostic. It is not yet a quotient-surviving separation from
ordinary provenance, effect systems, abstract interpretation, lenses, or CSP
explanation.

**Witness 6.9 (Diamond Network).** We exhibit a typed transport graph with four layers
$\{A, L_1, L_2, B\}$ and two paths:

- Path $P_1$: $A \to L_1 \to B$, where the morphism $A \to L_1$ has $LK = \{\text{type\_guarantee}\}$.
  Composed: $LK(P_1) = \{\text{type\_guarantee}\} \neq \emptyset$.
  $A$ is satisfiable; $B$ is obstructed. $\therefore P_1 \in \text{Obstr}$.

- Path $P_2$: $A \to L_2 \to B$, where neither morphism forgets any named structure.
  Composed: $LK(P_2) = \emptyset$.
  $\therefore P_2 \notin \text{Obstr}$.

The two paths share source $A$ and target $B$. Their admissibility differs exactly at
AC5, confirmed by the empty/non-empty distinction in composed loss kernels. (Verified
computationally in the diamond network witness family.)

---

## 7. Failure Types and Cover Topology

**Review-blocked section.** External review found the general cohomology claims
in this section false or under-specified as stated. The retained material below
is therefore a record of failed draft claims and finite witnesses, not a set of
usable theorems. The minimum repair is to state exact coefficient systems,
support presheaves, cover hypotheses, and allowed loss morphisms, then add
explicit counterexample checks before any monotonicity claim is restored.

### 7.1 Covers, Presheaves, and Čech Cohomology

We now place the obstruction in a sheaf-theoretic setting. This allows us to distinguish
two qualitatively different failure modes.

**Definition 7.1 (Cover).** Let $X$ be a finite set. A *cover* of $X$ is a finite
collection $\mathcal{U} = \{U_1, \ldots, U_n\}$ of subsets of $X$ with $X = \bigcup_i U_i$.
The *nerve* $N(\mathcal{U})$ of the cover is the simplicial complex whose vertices are
the cover elements and whose $k$-simplices are $(k+1)$-element subsets of $\mathcal{U}$
with non-empty intersection. We say $N(\mathcal{U})$ has a *1-cycle* if there exist
distinct patches $U_{i_1}, \ldots, U_{i_k}$ with $U_{i_j} \cap U_{i_{j+1}} \neq \emptyset$
for all $j$ (indices mod $k$) forming a cycle of length $k \geq 3$ in the nerve.

**Definition 7.2 (Presheaf over a cover).** A *presheaf* $F$ on $(X, \mathcal{U})$
assigns to each $U_i \in \mathcal{U}$ a set $F(U_i)$ of local sections, and to each
non-empty intersection $U_i \cap U_j$ restriction maps $\rho_{ij}: F(U_i) \to
F(U_i \cap U_j)$ satisfying $\rho_{ii} = \text{id}$ and the compatibility condition
$\rho_{ij} \circ \rho_{jk} = \rho_{ik}$ on triple intersections.

A *global section* of $F$ is a tuple $(s_i)_{i} \in \prod_i F(U_i)$ such that
$\rho_{ij}(s_i) = \rho_{ji}(s_j)$ for all $i, j$ with $U_i \cap U_j \neq \emptyset$.

**Definition 7.3 (Čech cohomology).** For a presheaf $F$ on $(X, \mathcal{U})$,
the Čech cohomology groups $\check{H}^n(\mathcal{U}, F)$ are defined via the standard
Čech complex. For our purposes, we use:

- $\check{H}^0(\mathcal{U}, F)$: sections that are locally defined everywhere; in the
  finite case, this tracks whether global sections exist.
- $\check{H}^1(\mathcal{U}, F)$: obstructions to patching locally consistent sections
  into global ones; non-trivial $H^1$ means such patching fails despite local compatibility.

### 7.2 Two Failure Types

**Definition 7.4 (Ambient and observer presheaves).** We consider pairs $(A, F)$ where:

- $A$ is the *ambient presheaf*: $A(U_i) = $ all admissible local sections at $U_i$;
- $F \subseteq A$ is the *observer sub-presheaf*: $F(U_i) \subseteq A(U_i)$ captures
  the locally accessible sections.

The *gap presheaf* $G = A/F$ records which ambient sections are inaccessible to $F$
at each patch: $G(U_i) = A(U_i) \setminus F(U_i)$.

**Definition 7.5 (H⁰ and H¹ failure).** A pair $(A, F)$ exhibits:

- **H⁰ failure** if $A$ has a global section but $F$ does not. Equivalently,
  $\check{H}^0(G) \neq 0$: there are gap sections that cannot be reached by the
  observer. *The answer exists; the observer cannot reach it.*
  
- **H¹ failure** if $A$ itself has no global section: $\check{H}^1(\mathcal{U}, A) \neq 0$.
  Local sections exist and are pairwise compatible on overlaps, but cannot be globally
  patched. *No consistent global answer exists at all.*

We order the failure types: $H^1 > H^0 > \text{none}$.

**Remark 7.6 (Examples).**

- *H⁰ failure (temporal access).* A nested cover $\{U_0 \subseteq U_1\}$ has an acyclic
  nerve (a single edge). No $H^1$ is possible. Observer $F$ sees only $v_0 = 0$ at $U_0$
  while the ambient $A$ also allows $v_0 = 1$. The answer $v_0 = 1$ exists (in $A$) but
  is inaccessible (not in $F$). H⁰ failure.

- *H¹ failure (contextual obstruction).* The CHSH 4-cycle cover $\{A_0B_0, A_0B_1,
  A_1B_1, A_1B_0\}$ has a 4-cycle in its nerve. Quantum (non-local) sections assign
  outcomes with holonomy $-1$. The signed product around the 4-cycle is $-1 \neq +1$,
  so by Theorem 3.1, no global section exists. By Theorem 3.1 in the Čech formulation:
  $\check{H}^1(\mathcal{U}, A) \cong \mathbb{Z}/2\mathbb{Z}$, non-trivial. H¹ failure.

### 7.3 Review-Blocked Cover Topology Claims

**Invalid draft claim 7.7 (Acyclic Cover Theorem).** If the nerve $N(\mathcal{U})$ has no 1-cycle
(is a forest), then $\check{H}^n(\mathcal{U}, F) = 0$ for all $n \geq 1$ and all
presheaves $F$. In particular, no H¹ failure can occur on a cover with acyclic nerve.

*Proof sketch.* The Čech complex $C^*(\mathcal{U}, F)$ over a cover with acyclic nerve
is exact. The exactness follows from the standard nerve theorem: acyclicity of $N(\mathcal{U})$
implies the Čech complex computes trivial higher cohomology. For the finite binary parity
setting, this can be verified directly: a frustration-free cycle requires a 1-cycle in
the nerve; without one, all cycles have even sign product $+1$ and the system is
satisfiable whenever local sections are globally compatible. $\square$

**Correction status.** Do not use this as a theorem. External review gives a
two-set acyclic-cover counterexample with $F(U_1)=0$, $F(U_2)=0$,
$F(U_1 \cap U_2)=\mathbb{Z}$ and zero restriction maps, yielding
$C^0=0$ and $C^1=\mathbb{Z}$. Any restored statement must restrict the
coefficient system or the class of sheaves/presheaves.

**Corollary 7.8.** The following cover structures force $H^1 = 0$:

1. *Nested covers*: $\{U_0 \subseteq U_1\}$ — acyclic (single edge), $H^1 = 0$.
2. *Two-element covers*: Mayer-Vietoris gives $H^1 = 0$.
3. *Sparse pairwise overlaps (no shared variable in cycles)*: vacuous $H^1$.

**Invalid draft claim 7.9 (Holonomy and H1).** For a 4-cycle cover $\mathcal{U} = \{U_1, U_2,
U_3, U_4\}$ with $\mathbb{Z}/2\mathbb{Z}$ coefficients, a presheaf $F$ has non-trivial
$\check{H}^1(\mathcal{U}, F) \cong \mathbb{Z}/2\mathbb{Z}$ if and only if the signed
product around the 4-cycle (the *holonomy*) is $-1$.

*Proof.* The Čech 1-cocycles on a 4-cycle with $\mathbb{Z}/2\mathbb{Z}$ coefficients
are elements of $(\mathbb{Z}/2\mathbb{Z})^4$ satisfying the cocycle condition. A section
$f$ is a coboundary iff the holonomy $\prod_i s_i = +1$ (product of boundary values).
Non-trivial $H^1$ elements correspond to holonomy $-1$. The CHSH quantum sections
achieve holonomy $-1$ (the CHSH inequality is saturated). $\square$

**Correction status.** Do not use this as an iff theorem about $H^1$ itself.
For constant $\mathbb{Z}/2\mathbb{Z}$ coefficients on a 4-cycle, the group
$H^1$ is already nontrivial independently of a sign labeling. A repair must
instead define a specific support-presheaf or twisted-coefficient obstruction
class and prove nonvanishing of that class under stated hypotheses.

**Invalid draft corollary 7.10 (Spatial vs. Temporal Failure Types).** Temporal access restrictions
(nested covers, observer sub-presheaves on acyclic covers) produce H⁰ failures.
Spacelike causal separation requiring a cyclic 4-context cover produces H¹ failures.
Cover topology is the primary determinant of failure type.

**Correction status.** This is too strong. External review blocks the claim that
cover topology alone determines failure type; the support presheaf, coefficient
system, and allowed local sections are load-bearing.

### 7.4 Failure-Type Monotonicity

**Definition 7.11 (Typed loss morphism types).** We distinguish:

- *Topology-preserving* loss morphism: same cover $\mathcal{U}$, reduced or relabeled
  section-space at patches. The nerve $N(\mathcal{U})$ is unchanged.
- *Sub-cover restriction*: new cover $\mathcal{U}' \subseteq \mathcal{U}$ (some patches
  are dropped). The nerve $N(\mathcal{U}')$ is a subgraph of $N(\mathcal{U})$.

**Invalid draft claim 7.12 (Failure-Type Monotonicity).** Let $f: (A, \mathcal{U}) \to (B, \mathcal{V})$
be a typed loss morphism of either topology-preserving or sub-cover restriction type.
Then:

$$\text{failure\_type}(B) \leq \text{failure\_type}(A)$$

in the ordering $H^1 > H^0 > \text{none}$. In particular, the transition $H^0 \to H^1$
is impossible under these morphism types.

*Proof.*

*Case 1 (Topology-preserving).* The cover $\mathcal{U}$ is unchanged, so the nerve
$N(\mathcal{U}) = N(\mathcal{V})$ is unchanged. If $N(\mathcal{U})$ is acyclic, then
by Theorem 7.7, $\check{H}^1(\mathcal{V}, B) = 0$: no $H^1$ failure is possible in
the target. If $N(\mathcal{U})$ contains cycles, the section-space reduction may shrink
$\check{H}^1$ (if the reduced sections no longer witness the holonomy) but cannot
create new $H^1$ classes from a $H^0$-only source, since the cycle structure that
supports $H^1$ must be inherited from the source.

*Case 2 (Sub-cover restriction).* $\mathcal{V} \subseteq \mathcal{U}$, so $N(\mathcal{V})$
is a subgraph of $N(\mathcal{U})$. A subgraph of a forest is a forest (removing vertices
or edges from an acyclic graph preserves acyclicity). Therefore if $N(\mathcal{U})$ is
acyclic (source had only $H^0$ failures), then $N(\mathcal{V})$ is acyclic, and by
Theorem 7.7, $\check{H}^1(\mathcal{V}, B) = 0$. The transition $H^0 \to H^1$ cannot
occur.

If $N(\mathcal{U})$ had cycles, dropping patches from $\mathcal{U}$ can only remove
cycles from the nerve, potentially reducing $H^1$ to $H^0$ or to no failure — but
never increasing the failure type. $\square$

**Correction status.** Do not use this as a theorem. The source/target
diagnostic mixes custom "H0 failure" language with standard cohomology, and
fixed-cover section-space reductions can create or destroy global-section
obstructions. A repair must define a narrow loss-morphism class and prove
preservation for that class only, with counterexamples outside the class.

**Remark 7.13 (Excluded class).** The only operation that could create $H^1$ from $H^0$
is *patch identification*: merging two non-adjacent patches into one, which can introduce
cycles in an acyclic nerve. This operation is NOT a typed loss morphism: identifying two
distinct contexts (patches) changes the cover structure in a way that reidentifies
previously distinct measurement contexts. This is not information-forgetting but
context-reidentification, and is excluded from the class of typed loss morphisms
studied here.

**Witnesses (T69, verified computationally):**

- *W1 (H⁰ preserved)*: Topology-preserving loss on nested 2-element cover. Source:
  $H^0$ gap (observer cannot reach $v_0 = 1$), $H^1 = 0$. Target after projecting away
  $v_1$: same nesting topology, $H^0$ gap preserved, $H^1 = 0$. No failure-type increase.

- *W2 (H¹ destroyed)*: CHSH 4-cycle cover restricted to Alice's 2-context sub-cover
  $\{A_0B_0, A_0B_1\}$. Source: $\check{H}^1 \cong \mathbb{Z}/2\mathbb{Z}$ (holonomy $-1$).
  Target: 2-element acyclic cover, $H^1 = 0$, 8 global sections. $H^1 \to H^0$ achieved.

- *W3 (H⁰ → H¹ impossible)*: Exhaustive search over 4 acyclic source covers and all
  sub-cover restrictions. Zero counterexamples found. Algebraic argument: acyclic source
  nerve $+$ sub-cover $\Rightarrow$ acyclic target nerve $\Rightarrow H^1 = 0$.

**Remark 7.14 (Second mechanism for H¹ destruction).** Section-space projection
that eliminates the sole shared variable between two patches can disconnect the nerve
without dropping any patch. (Example: projecting Alice's outcome away from each
CHSH context leaves Bob-only contexts that share no overlap variable, disconnecting
the 4-cycle into two disjoint edges.) This is a second mechanism by which
topology-preserving loss can in fact destroy H¹, and it is distinct from sub-cover
restriction. The LossKernel flag `cycle_destroying = True` marks morphisms of either
type.

---

## 8. The Typed Forgetting Attribution Conjecture

**Conjecture 8.1 (Typed Forgetting Attribution — TF1).** Let $f: \mathcal{A} \to
\mathcal{B}$ be a typed lossy morphism with $\mathcal{A}$ satisfiable (AC7) and
$\mathcal{B}$ obstructed (AC6). Then $f \in \text{Obstr}$ (admissible attribution)
only if $LK(f) \neq \emptyset$ and there exists a sub-system $\mathcal{A}' \subseteq
\mathcal{A}$ obtained by removing the structure named in $LK(f)$ such that
$\mathcal{A}'$ has no global section.

In words: the attribution is admissible only when the loss kernel names structure whose
presence in $\mathcal{A}$ was necessary for satisfiability.

### 8.1 Evidence

**(a) Predicate unfolding (Proposition 6.7).** For paths in typed transport graphs with fixed
satisfying endpoints, $P \in \text{Obstr} \iff LK(P) \neq \emptyset$. The biconditional
holds exactly: all PO1-admissible paths have non-empty LK; all non-admissible paths
have empty LK (verified on diamond network witness, T73).

**(b) Non-empty LK is necessary.** If $LK(f) = \emptyset$, then $f$ forgets nothing:
$\mathcal{A}$ and $\mathcal{B}$ contain the same named structure. Since $\mathcal{A}$
is satisfiable with this structure present, the obstruction in $\mathcal{B}$ cannot
be attributed to information loss through $f$. Condition AC5 ($LK(f) \neq \emptyset$)
is required for admissibility.

**(c) Non-empty LK is not sufficient.** The absorbed obstruction case (Remark 5.6)
shows $LK(f) \neq \emptyset$ without $f \in \text{Obstr}$: when the target $\mathcal{B}$
is satisfiable (AC6 fails), there is no obstruction to attribute. The conjecture's
content is not that $LK(f) \neq \emptyset$ suffices, but that it must hold and must
name structure relevant to satisfiability.

**(d) Cross-level attribution also requires non-empty LK (Holonic case).** In typed
transport graphs with cross-level morphisms (where patches span multiple abstraction
levels), holonic obstruction attribution still requires non-empty LK at the cross-level
morphism. Source-satisfiable + target-obstructed is insufficient without named forgotten
cross-level structure. (Verified computationally on holonic witness family, T40.)

### 8.2 Known Boundary

The conjecture as stated in 8.1 has two components:
1. $LK(f) \neq \emptyset$ (necessary, proven by AC5 analysis).
2. $LK(f)$ names attribution-relevant structure (the structure whose removal in $\mathcal{A}$
   would destroy $\mathcal{A}$'s satisfiability).

Component (1) is established. Component (2) is the open direction: we do not yet have
a proof that $LK(f)$ names *causally responsible* structure (in the sense that removing
it from $\mathcal{A}$ would cause the global section to disappear). The difficulty is
that many different structures may be necessary for satisfiability; $LK(f)$ names *one*
of them, but we have not proved it names a *witnessing* one.

### 8.3 Why It Might Fail

- The formal content of "attribution-relevant" may collapse to AC6 + non-empty LK, with
  no additional condition.
- A non-empty loss kernel may name structure that was present in $\mathcal{A}$ but
  irrelevant to satisfiability (the kernel names a red herring).
- Absorbed obstruction cases may require a recovery morphism not captured in the current
  framework.

---

## 9. Related Work

We locate this paper's contributions relative to the closest prior work.

### 9.1 Sheaf-Theoretic Contextuality

Abramsky and Brandenburger [AB11] established the sheaf-theoretic framework for
non-locality and contextuality: empirical models are presheaves on measurement context
covers, and contextuality is the non-existence of a global section. The Čech cohomology
obstructions we study (Definition 7.5) are instances of their framework.

*Our contribution relative to [AB11]:* We add the typed loss morphism layer and
record a failed attempt at failure-type monotonicity for this class of morphisms
(invalid draft claim 7.12). The sheaf framework identifies when an obstruction
exists; our attribution framework asks when a specific morphism is responsible.
The non-functor observation (Theorem 5.4) and loss-kernel monoid annotation
(Proposition 6.1) are not present in [AB11].

### 9.2 Signed Graphs and Parity CSP

The balance condition for signed graphs (Harary 1953; Zaslavsky 1982) is the standard
characterization of 2-colorability of signed graphs. Our Theorem 3.1 is a direct
instance of this. The equivalence between binary same/different constraints and signed
graph 2-colorability is well known in the CSP literature.

*Our contribution relative to signed-graph theory:* Signed-graph theory characterizes
the obstruction but says nothing about morphisms between signed-graph systems, about
which morphisms are responsible for creating the obstruction, or about how loss of
named structure changes the satisfiability. The typed loss morphism and attribution
predicate are our additions.

### 9.3 Category Theory and Monoidal Categories

Our category **Res** (Theorem 4.5) fits naturally in the tradition of categories of
relational structures with structure-preserving maps. The loss kernel is currently
only a monoid-valued annotation on arrows (Proposition 6.1), close to standard
effect/provenance-style accumulation.

Restriction categories [Cockett-Lack 2002] formalize categories of partial maps where
not all morphisms are defined everywhere. Our morphisms are total but carry forgetting
declarations; the relationship to restriction categories is structural rather than direct.

*Our contribution:* The specific typed annotation structure (preserved/forgotten
declaration), the monoid-valued composition of loss kernels, and the non-functor
observation are the local additions. External review blocks treating these as a
new categorical structure without a stronger separation or universal property.

### 9.4 Categorical Quantum Mechanics

Coecke, Abramsky, and collaborators developed categorical quantum mechanics using
compact closed categories and string diagrams [AC04]. The CHSH holonomy fixture
discussed in invalid draft claim 7.9 is related to their treatment of
non-locality, but the iff cohomology statement is not established here.

*Our contribution:* We work in a finite combinatorial (non-quantum) setting. The parity
system obstruction is not quantum; it is a finite signed-graph phenomenon. The quantum
case is a physical realization of a more general combinatorial structure.

### 9.5 Information-Theoretic Loss

Shannon's entropy characterizes information loss as a scalar quantity. Our loss kernel
$LK(f)$ is a *typed set-valued* annotation: it names what was lost, not merely how
much. The distinction matters for attribution: knowing the amount of information lost
does not tell you whether the lost structure was the specific structure that resolved
the target obstruction.

*Our contribution:* A set-valued, composable, typed annotation for information-losing
morphisms, with a proven composition law (Proposition 6.1) and candidate
attribution implications (Proposition 6.7, Conjecture 8.1).

### 9.6 Summary of Novelty Claims

The following items are local formalism components or open candidates, not
publication-grade novelty claims:

| Result | Statement |
|--------|-----------|
| Theorem 4.5 | Typed restriction morphisms form a category **Res** |
| Theorem 5.4 | Obstruction admissibility is not a Boolean functor on **Res** |
| Proposition 6.1 | Loss kernel is monoid-valued: $LK(g \circ f) = LK(f) \cup LK(g)$ |
| Proposition 6.7 | Path-dependence predicate unfolding for fixed-endpoint paths |
| Invalid draft claim 7.12 | Failure-type monotonicity is review-blocked and must be rebuilt before use |
| Conjecture 8.1 | Typed Forgetting Attribution: $LK(f) \neq \emptyset$ and attribution-relevant is necessary for admissibility |

The following results are not new and are stated here for context:

| Result | Attribution |
|--------|-------------|
| Theorem 3.1 | Signed-graph 2-colorability characterization [Harary 1953; Zaslavsky 1982] |
| Invalid draft claim 7.7 | Acyclic nerve does not imply vanishing for all presheaves without extra hypotheses |
| Invalid draft claim 7.9 | Holonomy does not characterize $H^1$ itself without a specified obstruction class |

---

## 10. Domains and Witnesses

To establish that the framework is not domain-specific, we list the six witness families
on which the core results have been verified.

| Domain | Witness | Result type |
|--------|---------|-------------|
| Parity constraint triangle | Example 2.5 | Obstructed; Theorem 3.1 instantiated |
| Compiler pipeline (source → machine code) | Emergent obstruction chain | Non-functor (Theorem 5.4), three chain shapes (Remark 5.6) |
| Typed transport diamond | Diamond network (Witness 6.9) | Path-dependence predicate unfolding (Proposition 6.7) |
| Distributed consensus (CAP) | Network partition forcing tradeoff | PO1 instance; obstruction attribution verified |
| Version control (merge conflict) | Three-way merge with incompatible histories | PO1 instance |
| CHSH contextuality | Alice-Bob 4-context cover | parity obstruction fixture; older H1 iff reading is review-blocked (invalid draft claim 7.9) |

The compiler, consensus, and version-control witnesses establish that the framework
is not tied to the physical or quantum setting.

---

## 11. Open Problems

**Problem 11.1 (Typed Forgetting Attribution Conjecture — TF1).** Prove or disprove
Conjecture 8.1. The key difficulty is formalizing "attribution-relevant" in a way that
is both weaker than "necessary for satisfiability" (which would require searching over
all possible sub-systems) and stronger than "non-empty" (which the absorbed case shows
is insufficient).

A promising approach: define attribution-relevance via the *minimal frustrated cycle*
— the LK must name structure whose removal would prevent the formation of a frustrated
cycle in $\mathcal{B}$ given the structure of $\mathcal{A}$.

**Problem 11.2 (Minimal loss kernel).** For a fixed $(A, B)$ pair satisfying AC6 and
AC7, does there exist a minimal loss kernel $LK^* \subseteq S$ such that $f \in
\text{Obstr} \Leftrightarrow LK(f) \supseteq LK^*$? This would give a canonical
"minimum forgetting" for attribution at fixed endpoints.

**Problem 11.3 (Functorial restriction of Obstr).** Is there a non-trivial full
subcategory $\textbf{Res}' \subseteq \textbf{Res}$ on which $\text{Obstr}$ restricts
to a functor? The non-functor theorem (Theorem 5.4) shows $\text{Obstr}$ fails globally.
A characterization of the subcategory where functoriality holds would clarify the
structural boundary.

**Problem 11.4 (Higher failure types).** Do $H^n$ failures for $n \geq 2$ occur in
finite restriction systems? The current framework produces $H^0$ and $H^1$ failures.
Higher cohomological obstructions would require covers with more complex topologies
(e.g., triangulated 2-complexes in the nerve) and may not arise from binary parity
systems alone.

**Problem 11.5 (Neutral statement of TF1 in terms of signed graphs).** The conjecture
(8.1) has a combinatorial restatement: $LK(f)$ must name structure such that removing
it from the signed constraint graph of $\mathcal{A}$ produces an unbalanced graph.
Can this be made precise and proved for the parity-system case?

**Problem 11.6 (Causal structure and failure type).** In physical applications, the
cover topology (acyclic vs. cyclic) correlates with whether measurement contexts are
timelike-separated (acyclic, H⁰) or spacelike-separated (potentially cyclic, H¹). Is
there a formal theorem connecting causal graph topology to cover nerve topology, making
the failure-type distinction a consequence of causal structure?

---

## 12. Conclusion

We have studied finite restriction systems and typed lossy morphisms between them,
with the goal of understanding when and why a morphism is responsible for a loss of
global satisfiability. The main findings are:

**Conclusion calibration.** The next two original conclusion paragraphs are
superseded by the reviewer calibration above. They should not be cited as final
results: the attribution layer currently gives monoid-valued bookkeeping, and
failure-type monotonicity is review-blocked rather than established.

**The attribution layer is non-trivial.** Despite the obstruction mechanism being
known (signed-graph parity), the attribution predicate (Obstr) has non-trivial algebraic
structure:
- It is not a functor on the morphism category (Theorem 5.4).
- It depends on the accumulated typed loss over a path, not on individual morphisms
  (Proposition 6.7, Corollary 6.8).
- The loss kernel governing it composes as a monoid annotation (Proposition 6.1), making the
  empty/non-empty distinction in composed kernels the precise discriminator.

**Superseded claim: failure types are topologically determined.** The cover nerve topology is the
primary determinant of failure type: acyclic covers can only produce H⁰ failures;
cyclic covers (with appropriate sections) can produce H¹ failures. Typed loss morphisms
cannot increase failure type (invalid draft claim 7.12), meaning information loss can degrade
obstruction degree but cannot create higher-degree obstruction.

**One central conjecture remains open.** The Typed Forgetting Attribution Conjecture
(Conjecture 8.1) — that admissible attribution requires the loss kernel to name
attribution-relevant structure — is supported by all evidence but unproved. It is the
natural generalization of the monoid-annotation law and the path-dependence predicate
into a full attribution theorem.

The program's thesis is that *obstruction is not meaningful without an attribution
account*. Seeing that $\mathcal{B}$ is obstructed is not enough. One must also name
the structure that was present in $\mathcal{A}$ and removed by $f$, and show that
removal was relevant. The typed loss kernel is the current bookkeeping object
for that account; whether it is more than integration vocabulary remains open.

---

## References

[AB11] Abramsky, S. and Brandenburger, A. (2011). "The sheaf-theoretic structure of
non-locality and contextuality." *New Journal of Physics*, 13, 113036.

[AC04] Abramsky, S. and Coecke, B. (2004). "A categorical semantics of quantum
protocols." *Proceedings of the 19th Annual IEEE Symposium on Logic in Computer
Science*, 415–425.

[BT82] Bott, R. and Tu, L.W. (1982). *Differential Forms in Algebraic Topology*.
Springer-Verlag.

[Bul17] Bulatov, A. (2017). "A dichotomy theorem for nonuniform CSPs." *Proceedings
of FOCS 2017*, 319–330.

[CL02] Cockett, J.R.B. and Lack, S. (2002). "Restriction categories I: categories of
partial maps." *Theoretical Computer Science*, 270(1–2), 223–259.

[FV98] Feder, T. and Vardi, M.Y. (1998). "The computational structure of monotone
monadic SNP and constraint satisfaction." *SIAM Journal on Computing*, 28(1), 57–104.

[Har53] Harary, F. (1953). "On the notion of balance of a signed graph." *Michigan
Mathematical Journal*, 2(2), 143–146.

[Lei04] Leinster, T. (2004). *Higher Operads, Higher Categories*. Cambridge University
Press. arXiv:math/0305049.

[Mac71] MacLane, S. (1971). *Categories for the Working Mathematician*. Springer-Verlag.

[Zas82] Zaslavsky, T. (1982). "Signed graphs." *Discrete Applied Mathematics*, 4(1),
47–74.

---

## Appendix A: Executable Model Reference

All results in this paper have been verified on finite witness families via executable
Python models. The models are available in the companion repository.

| Section | Theorem | Model file | Tests |
|---------|---------|-----------|-------|
| §4 | Category (Theorem 4.5) | `models/po1_admissibility_conditions.py` | T41: 14/14 pass |
| §3 | CSP Correspondence (Theorem 3.1) | `models/po1_chained_projection.py` | T39: verified |
| §5 | Non-Functor (Theorem 5.4) | `models/po1_chained_projection.py` | T34: 3 chain shapes |
| §6 | Loss Kernel monoid annotation (Proposition 6.1) | `models/losskernel_composition.py` | T73: 17/17 pass |
| §6 | Path-Dependence Biconditional (Theorem 6.7) | `models/transport_network.py` + `models/losskernel_composition.py` | T37, T73: pass |
| §7 | Failure-type monotonicity failed theorem family (invalid draft claim 7.12) | `models/losskernel_failure_type.py` | T69 finite fixtures pass; general theorem review-blocked |

**Appendix correction.** The row labeled "Path-Dependence Biconditional
(Theorem 6.7)" should be read as "Path-dependence predicate unfolding
(Proposition 6.7)."

*Note on proof status:* Theorem 4.5 and Proposition 6.1 have algebraic proofs as
given in the text. Theorem 5.4 and Proposition 6.7 have proof sketches verified
by construction on witness families. Invalid draft claim 7.12 is review-blocked
despite finite T69 fixtures passing. Conjecture 8.1 has no proof; Section 8 gives
evidence and boundary.

---

## Appendix B: Glossary of Terms

| Term | Definition | Section |
|------|-----------|---------|
| Finite restriction system | $(V, \Sigma, \mathcal{P})$: sites, values, patches | §2.1 |
| Global section | Total assignment satisfying all patches | §2.1 |
| Obstructed | No global section | §2.1 |
| Parity restriction system | $\Sigma = \{+1,-1\}$, binary same/different patches | §2.3 |
| Signed constraint graph | Graph with $\pm 1$ edge signs encoding same/different | §2.2 |
| Balanced (signed graph) | No frustrated cycle | §2.2 |
| Typed lossy morphism | Site map with preserved/forgotten structure declarations | §4.1 |
| Loss kernel $LK(f)$ | Forgotten structure of $f$ | §4.2 |
| **Res** | Category of finite restriction systems + typed lossy morphisms | §4.2 |
| Admissible obstruction attribution (Obstr) | AC1+AC2+AC3+AC5+AC6+AC7 | §5.1 |
| Cover | Finite collection $\mathcal{U}$ of subsets covering $X$ | §7.1 |
| Nerve $N(\mathcal{U})$ | Simplicial complex of overlapping patches | §7.1 |
| H⁰ failure | Global section exists in $A$; observer sub-presheaf $F$ cannot reach it | §7.2 |
| H¹ failure | No global section exists at all; local-to-global patching fails | §7.2 |
| Topology-preserving loss morphism | Same cover, reduced section-space | §7.4 |
| Sub-cover restriction | Patch-dropping loss morphism | §7.4 |
