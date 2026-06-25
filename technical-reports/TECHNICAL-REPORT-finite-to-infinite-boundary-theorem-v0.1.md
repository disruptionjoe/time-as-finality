# Technical Report: Finite-to-Infinite Boundary Theorem v0.1

## Question

T59 opened the finite-to-infinite boundary audit and resolved one edge — the
Mobius continuum probe for the T39 signed-graph parity criterion — but left the
remaining load-bearing `proto_independent` results at a Step-1 classification
table. T222 asks the closing question for each of the four:

```text
Does the result survive to an infinite / continuous analogue, or is it strictly
finite? Exhibit a witness on each side of the line.
```

The four results are CSP-PO1 (signed-graph 2-colorability gluing obstruction),
D1Cat (typed transport category laws), the PO1 Non-Functor theorem, and HEF
(holonic emergence).

## Method

The discipline mirrors T59. Every verdict carries two executable witnesses: a
*surviving generalization* (proof restated without finiteness and checked on a
finitely-represented infinite instance) and, on the other side, either a
continuum / colimit obstruction or a scope guard. The same signed-graph parity
engine that backs T39/T40/T59 backs the three obstruction-flavored results, so
the boundary is read off one shared mechanism, not four ad hoc ones.

The load-bearing honesty guard is inherited verbatim from T59: a coefficient-blind
scalar encoding can report a false global section. No result is permitted to
"survive to the continuum" by forgetting transition/coefficient data.

## Result

```text
CSP-PO1          conditional   survives countable scale (compactness);
                               strictly finite at the continuum unless
                               coefficient/transition data are carried.
D1Cat laws       survives      category axioms are algebraic, site-cardinality
                               independent; colimit closure is a separate open
                               obstruction.
PO1 Non-Functor  survives      existential refutation is monotone under
                               category extension; embeds into any ambient.
HEF              survives      finite negative cycle, compactness-stable under
                               unbounded acyclic depth.
```

Three survive, one is conditional, none is strictly finite. The single boundary
line is the **continuum coefficient layer of the parity engine; countability is
never the obstruction**.

## Witnesses

### CSP-PO1 — conditional

Survival (countable): growing prefixes of an all-same infinite signed path stay
satisfiable (windows n = 3, 5, 8, 20 all satisfiable); a planted finite negative
triangle on `{x_0, x_1, x_2}` is detected in every prefix that contains it.
de Bruijn–Erdős / propositional compactness lifts the finite verdict to the
countable limit: an infinite signed CSP is unsatisfiable iff some finite
sub-CSP is.

Continuum obstruction (inherited from T59):

| Encoding | Mobius overlaps | Parity verdict | Truth |
| --- | --- | --- | --- |
| transition-aware Z2 | same, different | obstructed (direct conflict) | obstructed |
| coefficient-blind scalar | same, same | **satisfiable** | obstructed |

The coefficient-blind encoding reports a false global section despite monodromy
−1. Parity is licensed at the continuum only after the coefficient object and
transition signs are reduced to a signed finite (transition-aware Z2) problem;
the replacement target is coefficient-aware sheaf H1, not blind same/different
CSP.

### D1Cat — survives

Survival: the category axioms are checked on a countably-infinite (index-shift)
site map on N. Associativity `(f;g);h = f;(g;h)` and the left/right unit laws
hold at every one of 1000 sampled coordinates; `preserved_dims` intersection is
exhaustively associative and unital over all 16 subsets of the fixed four-element
universe `D1_DIMENSIONS`. Site cardinality never enters either proof — site_map
composition is function composition; `preserved_dims` lives in a fixed universe.

Other side — the genuinely fragile structure-level edge: the colimit of a
transfinite strictly-descending chain. The accumulated `forgotten_structure`
colimit is a countable set union (well-defined as a set), but the
`preserved_dims` intersection along the descending chain reaches the empty set.
The limit object preserves no dimension, which lies outside the profile axioms
every finite D1 object satisfies. No D1Cat colimit construction exists yet, so
the category-completeness question is open — distinct from, and weaker than, the
category-laws result.

### PO1 Non-Functor — survives

The non-functor theorem is existential: there exist composable `f, g` with
`PO1(f) = PO1(g) = False` but `PO1(f;g) = True`, so PO1 is not the Boolean-and
functor. An existential refutation, once witnessed by a finite instance, is
monotone under category extension: it embeds unchanged into any infinite-site
ambient because PO1 is an endpoint-pair-local predicate, and the ambient site
count does not enter the verdict. Embeddings into ambients of 10, 100, and
10 000 sites all preserve the `(False, False, True)` triple.

Scope guard (load-bearing): only the **negative** result persists. T222 does not
certify a positive (lax / indexed) functor at infinity; if obstruction detection
is later redefined via sheaf H1 for infinite systems, the positive functor
question resets. Survival means "the obstruction persists", not "the functor
exists".

### HEF — survives

Survival: a holonic obstruction is a negative cycle in the combined
(micro + cross-level) signed graph, and negative cycles are finite. A planted
cross-level parity triangle on the bottom three levels stays obstructed at depths
0, 1, 5, 50, 500; the same holarchy without the planted −1 stays satisfiable at
every depth. König's lemma / compactness: an infinite-depth holarchy is
obstructed iff some finite sub-holarchy is.

False-dissolution guard (T59 discipline applied to depth): the intuition that an
infinite-path limit "satisfies all cross-level parity conditions" and dissolves
the obstruction is exactly the coefficient-blind move — it forgets the planted
−1 transition. Replacing the planted `L0 ≠ L2` (−1) with a same (+1) edge is the
only thing that restores satisfiability at depth 500. Dissolution is an artifact
of dropping coefficient data, not a real limit effect.

## Hypothesis Evaluation

### H0

All four proto_independent results are strictly finite artifacts.

Status: refuted. Three carry without finiteness; the fourth carries to countable
scale and is conditional only at the continuum.

### H1

The boundary is at countability (countably infinite already breaks the results).

Status: refuted. Every result survives countable scale. The CSP-PO1 break is at
the continuum coefficient layer, not at cardinality.

### H2

The boundary is at the continuum coefficient layer of the shared signed-graph
parity engine; carrying coefficient/transition data is necessary and sufficient
for continuum survival of the obstruction-flavored results.

Status: best_supported. The Mobius witness localizes the only false-section
failure to the coefficient-blind continuum encoding; HEF inherits exactly the
same condition; D1Cat and PO1 non-functor are off this axis (algebraic /
existential) and survive independently.

## Claim Impact

This sharpens, not weakens, the proto_independent rows:

```text
CSP-PO1   add: survives countable (compactness); continuum-conditional on
          coefficient/transition data (T59 false-section boundary, now a verdict).
D1Cat     add: category laws boundary-free for infinite site sets; colimit
          closure is a separate open obstruction.
PO1-NF    add: non-functor result survives to infinity (monotone); positive
          functor at infinity open.
HEF       add: survives infinite nesting depth (compactness); inherits the
          CSP-PO1 continuum condition for genuinely continuous holarchies.
```

The most load-bearing finite restriction for any external paper is **CSP-PO1 at
the continuum**, because the parity engine is shared under HEF and the holonic
results, and the continuum is the one place a coefficient-blind reuse silently
produces a false global section. The D1Cat colimit gap is a secondary, contained,
structure-level open item.

## What T222 Does Not Decide

- It does not build the coefficient-aware sheaf-H1 replacement for continuous
  orientation data; it states it as the required next object.
- It does not construct a D1Cat colimit or prove none exists.
- It does not decide whether a repaired lax / indexed functor exists for
  infinite-system morphisms.
- It does not promote S1, Q1, H7, or HEF to physics claims.
- It claims no general Čech / sheaf-cohomology theorem from any finite witness
  (explicit ROADMAP language guardrail).

## Recommended Next Goal

Build the coefficient-aware H1 obstruction object for continuous orientation /
transition data and compare its verdict against PO1 admissibility metadata, then
attempt the D1Cat transfinite colimit construction. These two moves convert the
two remaining `conditional` edges (CSP-PO1 continuum, D1Cat colimit) into
verdicts and clear the last honest blocker on continuum-domain publication
language.
