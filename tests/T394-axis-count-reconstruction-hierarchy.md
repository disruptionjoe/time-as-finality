# T394: Axis-Count Reconstruction Hierarchy

## Route

Finite order theory / event-finality reconstruction (Direction A, rung 1).

## Claim

Reconstruction of a record-dependency partial order by componentwise
comparison of d monotone finality-axis magnitudes is exactly the classical
notion of order dimension at most d. This makes T49/T50 the d = 1 and d = 2
entry points of a hierarchy: T49's Anti-Scalar Theorem is the d = 1 rung
(dim >= 2 for any structure with an incomparable pair); for every d there
are finite record structures requiring more than d axes (the standard
examples S_d); D1's four named axes reconstruct exactly the event structures
of order dimension <= 4, and S_5 (10 events) is a concrete finite structure
escaping 4-axis reconstruction; and every finite poset is realizable as the
record-dependency order of a FinaliEvent structure via principal-downset
record bases under T48's own containment rule.

Stated in both vocabularies:

- **House:** a FinaliEvent structure (E, <=_rec) admits axis profiles on d
  axes satisfying T50's AM condition iff <=_rec is the intersection of d
  linear extensions. The minimal axis count is an isomorphism invariant of
  the record-dependency order.
- **Neutral:** a finite poset P embeds order-exactly into (R^d, <=
  componentwise) iff dim(P) <= d in the sense of realizers by linear
  extensions (candidate prior art, from memory, unverified: Dushnik-Miller
  1941; see Prior-Art Register below).

## Class

Subclaim of [C1: Experienced Time as Record Finality](../claims/C1-experienced-time-as-record-finality.md)
via the H1 (Record Reconstruction) lineage — the T48/T49/T50/T54/T55 finite
event-finality spine. Refines the first rung of Direction A in
[audits/2026-07-01-high-gravity-research-directions.md](../audits/2026-07-01-high-gravity-research-directions.md)
and supersedes-by-extension the scalarization boundary in
[TECHNICAL-REPORT-direction-a-finite-anti-scalar-generalization-v0.1.md](../technical-reports/TECHNICAL-REPORT-direction-a-finite-anti-scalar-generalization-v0.1.md)
(that report's Theorem 1 is the d = 1 exact-scalar boundary here; its
Theorem 2 tie-collapse classifier is subsumed by this artifact's exhaustive
tie-collapse legs). No claim status changes.

## Status

All four theorems hold in the verified finite ranges. C1 remains
**weakened**; H1 remains **partially supported**; this artifact promotes
nothing. It is finite mathematics about the reconstruction formalism —
paper-facing raw material for Direction A, not a physics claim.

## Target Claims

- [C1: Experienced Time as Record Finality](../claims/C1-experienced-time-as-record-finality.md)
- H1: Record Reconstruction ([HYPOTHESES.md](../HYPOTHESES.md))
- [T48: FinaliEvent Structure](T48-finali-event-structure.md)
- [T49: Reconstruction Without Background Time](T49-reconstruction-without-background-time.md)
- [T50: Axis Monotonicity Theorem](T50-axis-monotonicity-theorem.md)

## Definitions

**Finite event structure (here):** a finite poset P = (E, <=). Events are
labeled 0..n-1; enumeration uses natural labelings (i <_P j implies i < j);
ordered pairs (i, j) mean i <_P j; pair lists are printed index-sorted
(lexicographically) — house convention post-T392 review.

**d-axis reconstruction (house: AM with d axes):** a map m: E -> R^d such
that for all distinct e, f: e <=_P f iff m_k(e) <= m_k(f) for every axis k.
This is T50's AM condition read as a definition of exact reconstructibility,
with the axis count left free.

**Realizer:** d linear extensions L_1..L_d of P with intersection exactly P.
**Minimal axis count / order dimension dim(P):** the least such d.

**Total preorder axis (tie-collapse reading):** a real axis may assign equal
magnitudes to distinct events; each axis is then a total preorder (weak
order), not a linear order. The tie-collapse question is whether preorder
axes can reconstruct more than linear-extension axes. (This is the loophole
the prior Direction A technical report isolated.)

**Standard example S_d:** 2d events, a_1..a_d (labels 0..d-1) and b_1..b_d
(labels d..2d-1), with a_i < b_j iff i != j. The diagonal pairs (a_i, b_i)
are incomparable.

**Record-basis realization (T48's rule, verbatim):** e_j directly precedes
e_i iff the record basis of e_j's post-finality (target) system is a
NON-EMPTY subset of the record basis of e_i's pre-finality (source) system;
the record-dependency order is the reflexive-transitive closure. The
principal-downset assignment gives event e the target basis
{r_x_locked : x <= e} and the source basis {r_x_locked : x < e} plus its own
raw record — exactly the shape of T48's own witness (U3 =
{r_A_locked, r_B_locked, r_composite_raw}; O3 =
{r_A_locked, r_B_locked, r_composite_locked}).

## Theorem 1 (Reconstruction)

A finite poset P is exactly reconstructible by d monotone axis magnitudes
under componentwise order iff dim(P) <= d.

Proof structure, with the earned/proof-backed split stated explicitly:

1. (<=) Given a realizer L_1..L_d, the rank magnitudes m_k(e) = position of
   e in L_k reconstruct P. **Machine-verified on all n^2 ordered pairs for
   every poset up to n = 6 up to isomorphism (405 classes), at the minimal
   d found by exhaustive search.**
2. (=>, linear-order axes) If d rank-injective axes reconstruct P, their
   induced total orders are linear extensions intersecting to P.
   Definitional.
3. (=>, tie-collapse) If d total-preorder axes W_1..W_d reconstruct P, then
   each W_k contains P, and refining each W_k lexicographically by one fixed
   linear extension L_0 of P yields linear extensions whose intersection is
   P. Short proof: the refinement L_k is a total order; if e <_P f then
   e <=_{W_k} f, and on ties L_0 breaks toward P, so L_k extends P; if
   (e, f) is in every L_k with e != f then e <=_{W_k} f for every k (either
   strictly or via a tie), so (e, f) is in the intersection of the W_k,
   which is P. **Machine-verified constructively on every first-found
   preorder witness (4,473 witnesses across n <= 5), and exhaustively:
   at n <= 5, d <= 2, the posets achievable as intersections of d weak
   orders are exactly those with dim <= d (all pairs of all weak orders
   scanned); at n = 6, d = 2, every dimension-3 class is exhaustively
   refuted over all pairs of extending weak orders.** Beyond these caps the
   lemma is proof-backed, not enumeration-backed — stated honestly.

Minimality is by exhaustive scan: for each poset the search at every
d' < dim(P) exhausts all d'-tuples of linear extensions (completeness of the
scan is argued in the model docstring: any realizer's last extension must
reverse all extra pairs of the first d'-1, which the acyclicity test
detects).

## Theorem 2 (Anti-Scalar as d = 1)

dim(P) = 1 iff P is a chain; equivalently, any incomparable pair forces
dim(P) >= 2. T49's Anti-Scalar Theorem — no total preorder replicates a
partial order with an incomparable pair — is exactly this d = 1 rung.
**Machine-verified over all 405 classes, plus regression: T49's 3-event
witness (e1, e2 < e3; e1 || e2) has dim exactly 2, both as an abstract shape
and as recomputed from the actual T49 model's record order (whose 2-axis
exact match is re-asserted). T49's 2-axis success is thereby explained: it
is the dim(P) = 2 case of Theorem 1, not an accident of the witness.**

## Theorem 3 (Axis-Count Obstruction)

For every d >= 2, dim(S_d) = d, so no fixed axis count suffices for all
finite record structures. Verified:

- **S_3 (6 events):** minimal axis count 3 by brute-force exhaustive search
  (48 linear extensions; every single extension and every extension pair
  refuted; realizer found and verified at d = 3). S_3 is one of exactly 3
  dimension-3 classes among the 318 posets on 6 events.
- **S_4 (8 events):** d = 2 refuted by full scan over all 720 extensions;
  d = 3 refuted exhaustively with automorphism-orbit pruning (|Aut| = 24,
  30 orbit representatives for the first extension, 21,600 scanned pairs;
  coverage: automorphisms map realizers to realizers, so restricting the
  first coordinate to orbit representatives is complete — soundness of the
  orbit action is asserted in code). Explicit verified 4-realizer.
- **S_5 (10 events):** dim(S_5) = 5 — hence S_5 **escapes 4-axis
  reconstruction**. The d = 4 brute force is computationally infeasible
  (~4e10 orbit-pruned pair scans) and is **not claimed**; instead the lower
  bound dim(S_5) >= 5 is carried by a fully machine-checked finite
  certificate plus a two-line arithmetic pigeonhole:
  - machine-checked: every cross pair a_i < b_j (i != j) is in the order;
    every diagonal pair (a_i, b_i) is incomparable; for every i < j,
    S_5 + {(b_i, a_i), (b_j, a_j)} contains a cycle (all C(5,2) = 10
    certificates); independently, ALL 17,280 linear extensions are
    enumerated and each reverses at most one diagonal pair; the extension
    count matches the derived closed form (d!)^2 + d((d-1)!)^2 (verified
    for d = 2..5: 6, 48, 720, 17280).
  - two-line pigeonhole (spec-level proof; ingredients above): if
    m: E -> R^4 reconstructs S_5 exactly, each diagonal pair must be
    strictly reversed on some axis (else a_i <= b_i componentwise, but
    a_i || b_i); one axis cannot strictly reverse two diagonal pairs, since
    m_k(b_i) < m_k(a_i) <= m_k(b_j) < m_k(a_j) <= m_k(b_i) is a numeric
    cycle (the middle inequalities are forced by the cross pairs). Five
    diagonal pairs, four axes — impossible. This argument needs no
    tie-collapse lemma: it works directly on real-valued axes.
  - upper bound: explicit 5-realizer (L_k reverses exactly diagonal pair k)
    verified by direct intersection and by rank-magnitude reconstruction.
  - the certificate machinery is cross-validated on S_3 and S_4, where
    brute-force search independently returns the same minimal counts.

**Consequence (stated carefully):** D1's four named finality axes
(causal = reversal_cost, info = holder_redundancy, obs_access =
accessible_support, branch = branch_support) can exactly reconstruct
precisely the event structures of order dimension <= 4. S_5 is a concrete
10-event structure that no assignment of four axis magnitudes reconstructs
exactly. This four-axis consequence treats the four D1Profile fields as
independent, freely-assignable integer magnitudes — formally true of the
v0.1 profile, while D1 itself marks branch_support and reversal_cost
formal-only and T9 shows the axes collapsing to a single count in simple
substrates. Whether physically realized causal orders exceed order dimension
4 is an OPEN question, not addressed here (see Physics-Facing Consequence).

## Theorem 4 (Realizability)

Every finite poset arises as the record-dependency order of a FinaliEvent
structure: assign event e the target record basis = locked records of its
principal downset and the source record basis = locked records of its strict
downset plus its own raw record; then T48's non-empty-subset containment
rule recovers exactly <=_P after reflexive-transitive closure.
**Machine-verified for all 405 classes in both the faithful two-basis
variant and the simplified single-basis (principal downset) variant.**

Honest edge case (the non-empty clause): with STRICT downsets instead of
principal downsets, minimal events get empty target bases, and the non-empty
clause deletes every dependency out of them (2-chain witness: closure is
empty, 0 < 1 is lost); strict downsets also create spurious containments
between incomparable events sharing predecessors. The strict variant
reconstructs exactly the antichains (6 of 405 classes). **The principal
(inclusive) downset is the exact fix, no change to T48's rule is needed, and
T48's own witness already uses inclusive bases (O3 carries its
predecessors' locked records), so the faithful reading of T48 is the working
one.** The clause itself is vacuous for principal downsets (every target
basis contains the event's own locked record) — verified.

House-object spotlight: S_3 is additionally built as six actual
PO1-admissible FinaliEvents over D1RestrictionSystems (unobstructed
same-same-same sources, obstructed parity-conflict targets, T48's builder
pattern), its record-dependency order is computed with T48's own
`_compute_order` and equals S_3, and T50's AM condition (checked with T49's
own `_compare_orders`) holds with the three axes (causal, info, obs_access)
assigned from the verified 3-realizer ranks and **fails for every proper
subset of those axes** — the executable house instantiation of
dim(S_3) = 3.

## Verification Plan

Exhaustive finite verification, deterministic, no sampling anywhere:

1. Enumerate all posets up to isomorphism for n <= 6 via natural labelings
   + canonicalization; self-consistency: natural-labeled count equals
   sum over classes of e(P)/|Aut(P)|, labeled count equals sum of
   n!/|Aut(P)| — three independent computations agreeing; labeled counts at
   n = 3, 4 (19, 219) must match the prior Direction A technical report's
   independently computed values.
2. Theorem 1: minimal axis count for every class by exhaustive
   linear-extension search; rank-magnitude reconstruction re-verified
   pairwise; tie-collapse legs as specified above.
3. Theorem 2: dim = 1 iff chain over all classes; T49 witness regression
   (abstract shape + actual T49 model import).
4. Theorem 3: S_3/S_4 brute force (orbit-pruned where stated), S_5
   certificate + explicit realizer; closed-form extension counts.
5. Theorem 4: all classes, three basis variants (faithful / single /
   strict), plus the 2-chain micro-witness.
6. House spotlight via T48/T49's own imported machinery.

Caps (documented in the model): N_MAX_ISO_SWEEP = 6 (n = 7 has 2045 classes,
not attempted), N_MAX_PREORDER_SWEEP = 5 with D_MAX_PREORDER_SWEEP = 2 (the
full n = 6 weak-order pair sweep over 4683^2 pairs is replaced by the
targeted dimension-3 refutation), S_5 certificate-only at d = 4. Runtime
~14 s total.

## Success Criteria

1. Minimal axis count equals exhaustive-search order dimension for every
   poset up to n = 6, with realizer magnitudes re-verified on all pairs.
2. Tie-collapse legs all negative (preorder axes add nothing) in the stated
   ranges; constructive linearization verified on every witness.
3. dim = 1 iff chain on all classes; T49 witness dim = 2 with the T49
   model's 2-axis match re-asserted.
4. dim(S_3) = 3 and dim(S_4) = 4 by exhaustive search; S_5 certificate
   ingredients all machine-checked and the explicit 5-realizer exact.
5. Theorem 4 faithful and single variants exact on all 405 classes; strict
   variant fails outside antichains with the 2-chain witness.
6. S_3 spotlight: all six events fully_admissible; record order equals S_3;
   AM holds on 3 axes and fails on every proper subset.
7. Enumeration self-consistency identities hold and match the prior report.

## Failure Conditions

1. Any poset up to n = 6 where the componentwise reconstruction at the
   found minimal d disagrees with the record order on any pair. (Would
   break the Dushnik-Miller correspondence claim at finite scale.)
2. Any poset where preorder (tied) axes reconstruct with fewer axes than
   linear extensions in the exhaustively swept ranges. (Would revive the
   tie-collapse loophole and demote Theorem 1 to the linear-order reading.)
3. dim(S_3) != 3 or dim(S_4) != 4 under brute force, or any S_5 certificate
   ingredient failing. (Would break Theorem 3 and the four-axis
   consequence.)
4. The faithful record-basis construction failing on any poset. (Would mean
   T48's containment rule does not realize all finite posets and the
   realizability claim must be weakened to a poset subclass.)
5. The S_3 FinaliEvent spotlight failing PO1 admissibility or AM. (Would
   mean the abstract theorem does not survive contact with the house
   objects.)
6. Tuning any cap, tolerance, or construction to force a verdict. Caps were
   fixed for runtime before verdicts were read; every verdict is a computed
   boolean, and a negative on any leg would be reported as-is.

## Neighbors / Prior Art

In-repo:

- **T48 (FinaliEvent Structure)** — supplies the record-dependency
  definition (containment rule used verbatim here, including the non-empty
  clause) and the house objects the spotlight instantiates.
- **T49 (Reconstruction Without Background Time)** — the d = 2 finite
  witness this artifact generalizes; its Anti-Scalar Theorem is Theorem 2's
  d = 1 rung; its 3-event witness is a pinned regression here.
- **T50 (Axis Monotonicity Theorem)** — AM is the reconstruction condition
  whose axis count this artifact makes into the hierarchy parameter;
  Theorem 1 characterizes exactly when AM-satisfying profiles exist for a
  given axis count.
- **T54 (Finite Finality Descent Theorem)** and the T51-T55 spine — the
  observer-colimit side of the same finite program; not touched here.
- **TECHNICAL-REPORT-direction-a-finite-anti-scalar-generalization-v0.1**
  — the prior Direction A progress artifact. Aligned with and extended:
  its exact-scalar boundary (Theorem 1 there) is the d = 1 rung here; its
  tie-collapse classifier (Theorem 2 there) is subsumed by this artifact's
  exhaustive tie-collapse legs; its labeled counts (19, 219) are re-derived
  and asserted; its recommended next artifact ("Finite Temporal-Order
  Scalarization Taxonomy") is delivered by the dimension census plus the
  preorder sweeps, under the sharper dimension framing.
- **T126/T154/T156-T167/T223 (causal-set embeddability family)** — poset
  combinatorics for the S1 spacetime lane; different target (embeddability
  filters, ordering fractions), no order-dimension content; the T223
  decisive verdict killed the finite-colimit spacetime route, which this
  artifact does not reopen.

Candidate prior art (FROM MEMORY, UNVERIFIED — the repo's no-fake-citations
rule applies: none of these may enter `literature/` or external-facing text
without verification against the actual papers):

- Dushnik & Miller, "Partially ordered sets" (Amer. J. Math., 1941) —
  order dimension; the standard examples S_d with dim(S_d) = d.
- Szpilrajn (1930) — every partial order extends to a total order.
- Hiraguchi (1951) — dim(P) <= n/2 for n >= 4 (consistent with the census:
  max dim 2 at n = 4, 5 and max dim 3 at n = 6; not load-bearing here).
- Ore; Trotter, "Combinatorics and Partially Ordered Sets: Dimension
  Theory" (1992) — dimension = embedding into R^d with componentwise order;
  the standard reference frame for Theorem 1's equivalence.
- OEIS A000112 (unlabeled posets: 1, 2, 5, 16, 63, 318) and A001035
  (labeled posets: 1, 3, 19, 219, 4231, 130023) — this run's enumeration
  reproduces both sequences independently.
- Nielsen-Plotkin-Winskel (1981) event structures — already the T48 frame.

If the Dushnik-Miller correspondence is confirmed against the literature,
Theorems 1-3 are a re-derivation with exhaustive finite verification and a
house-vocabulary translation, not new mathematics; the new content is the
identification of the finality-axis count with dimension, the tie-collapse
closure, Theorem 4's realizability via T48's containment rule, and the
executable bridge to the D1/PO1 house objects. This is stated so a hostile
reviewer does not have to say it first.

## Physics-Facing Consequence (restrained)

A d-axis finality reconstruction imposes a structural constraint: event
structures of order dimension > d cannot be exactly reconstructed by d
monotone finality axes, no matter how the magnitudes are chosen. D1's four
named axes therefore cover exactly the dimension <= 4 event structures, and
S_5 is a concrete finite escape witness. Whether physically realized causal
orders (e.g., finite event sets in Minkowski causality) exceed order
dimension 4 is an OPEN question and candidate prior-art territory
(from-memory candidates only, unverified: literature on the order dimension
of Minkowski causal orders / causal-set posets; 1+1 Minkowski causality is
the componentwise order on R^2 in lightcone coordinates, which is why
dimension-2 structures feel "spacelike-planar"). No claim about spacetime is
made; T223's demotion of the finite-colimit spacetime route stands
untouched.

## Known Constraints

- All results are finite-range: n <= 6 for the full sweeps, S_5 at n = 10
  via certificate. No general-n theorem is claimed beyond the proof-backed
  steps explicitly marked as such (tie-collapse lemma, S_d pigeonhole).
- The d = 4 brute-force refutation for S_5 is not performed (infeasible);
  the lower bound rests on the certificate, cross-validated at S_3/S_4.
- Axis magnitudes here are abstract integers (realizer ranks). The spotlight
  shows the D1Profile fields can carry them for S_3; nothing is claimed
  about physically meaningful magnitude assignments.
- Theorem 4 realizes posets as record-basis structures; it does not claim
  the resulting FinaliEvent structures are physically realizable systems,
  only that T48's formal rule imposes no order-theoretic restriction.

## What This Does Not Earn

- No claim promotion: C1 stays weakened, H1 stays partially supported.
- No inequality for temporal order (Direction A rung 2): this artifact
  supplies the finite mathematical floor, not the process-matrix
  translation, which remains the single creative hinge and is untouched.
- No statement that physical causal orders have dimension > 4 or <= 4 —
  that is flagged open.
- No spacetime claim, no continuum claim, no reopening of the T223-killed
  finite-colimit route.
- No novelty claim over the classical dimension-theory literature; the
  candidate prior art above is presumed to contain Theorems 1-3 in some
  form until verified otherwise.

## Reproduction

```bash
python -m pytest tests/test_axis_count_reconstruction_hierarchy.py -v
python -m models.axis_count_reconstruction_hierarchy
```

Deterministic; ~14 s each. The T48/T49/T50 runners were re-run alongside and
rewrote no tracked result content.

## Contribution Needed

- Verify the candidate prior art (Dushnik-Miller, Trotter, Minkowski
  causal-order dimension) against the actual papers before any of it enters
  `literature/` or paper-facing text; then state precisely which parts of
  Theorems 1-3 are re-derivations.
- Direction A rung 2: translate the axis-count obstruction into
  process-matrix / causal-order vocabulary and look for a quantitative
  bound (the audit's CHSH move). The dimension census (1 / 314 / 3 at
  n = 6) and S_d witnesses are the raw material.
- Extend the census to n = 7 (2045 classes) if a rung-2 candidate needs it;
  requires a faster canonicalizer, not new mathematics.
- A physically motivated axis-magnitude semantics for dimension-3-or-higher
  structures (the spotlight assigns realizer ranks, which are abstract).
