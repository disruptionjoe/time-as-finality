# T394 Axis-Count Reconstruction Hierarchy — Results v0.1

- **Artifact:** `T394-axis-count-reconstruction-hierarchy-v0.1`
- **Spec:** [tests/T394-axis-count-reconstruction-hierarchy.md](../tests/T394-axis-count-reconstruction-hierarchy.md)
- **Model:** [models/axis_count_reconstruction_hierarchy.py](../models/axis_count_reconstruction_hierarchy.py)
- **Test:** [tests/test_axis_count_reconstruction_hierarchy.py](../tests/test_axis_count_reconstruction_hierarchy.py)
- **Numbers:** [T394-axis-count-reconstruction-hierarchy-v0.1.json](T394-axis-count-reconstruction-hierarchy-v0.1.json)
- **Tags:** direction_a_rung1, order_dimension, exhaustive_finite,
  deterministic, no_claim_promotion, candidate_prior_art_flagged

## Verdict (house vocabulary)

**All four theorems hold in the verified finite ranges.** d-axis finality
reconstruction (T50's AM with d axes) is exactly order dimension <= d:
verified for every poset up to n = 6 up to isomorphism, with the
tie-collapse loophole closed exhaustively where feasible and constructively
everywhere found. T49's Anti-Scalar Theorem is the d = 1 rung and its
3-event witness falls out as dim = 2. The standard examples give a strict
axis-count hierarchy — dim(S_3) = 3 and dim(S_4) = 4 by exhaustive search,
dim(S_5) = 5 by machine-checked certificate — so **D1's four named axes
reconstruct exactly the event structures of order dimension <= 4, and S_5
(10 events) escapes 4-axis reconstruction**. Every finite poset is realized
as a record-dependency order by T48's own containment rule with
principal-downset record bases, and the non-empty clause is shown to be
exactly why principal (not strict) downsets are the faithful choice.

No claim promotion: C1 stays weakened, H1 stays partially supported. The
correspondence with classical order-dimension theory (Dushnik-Miller) is
flagged as candidate prior art from memory, unverified — Theorems 1-3 are
presumed re-derivations with exhaustive finite verification and a
house-vocabulary bridge until the literature is checked.

## Predeclarations (fixed before verdicts were read)

- Caps: full iso sweep at n <= 6; tie-collapse preorder sweep at n <= 5,
  d <= 2, plus targeted n = 6, d = 2 refutation of every dimension-3 class;
  S_5 lower bound by certificate (d = 4 brute force declared infeasible in
  advance, ~4e10 pruned scans). Caps chosen for the < 60 s runtime budget.
- Labeling convention (post-T392 house rule): events 0..n-1; pairs (i, j)
  mean i <_P j; pair lists index-sorted; S_d labeled a_i = i-1, b_j = d+j-1.
- Determinism: no sampling anywhere; all scan orders fixed by construction.
- Honesty rule: fix the constructions, never the assertions; any failed leg
  is reported as a refutation of the corresponding theorem.

## Exact computed values

### Enumeration (self-consistency triple-checked)

| n | iso classes | natural-labeled | labeled |
| --- | --- | --- | --- |
| 1 | 1 | 1 | 1 |
| 2 | 2 | 2 | 3 |
| 3 | 5 | 7 | 19 |
| 4 | 16 | 40 | 219 |
| 5 | 63 | 357 | 4,231 |
| 6 | 318 | 4,824 | 130,023 |

- Identity `natural = sum e(P)/|Aut(P)|` and `labeled = sum n!/|Aut(P)|`:
  **hold** (enumeration, extension counting, and automorphism counting
  agree).
- Labeled counts at n = 3, 4 (**19, 219**) match the prior Direction A
  technical report's independently computed values. The full sequences
  match the remembered OEIS A000112 / A001035 values (candidate prior art,
  from memory, unverified).

### Theorem 1 — Reconstruction iff dim <= d

- 405 classes checked; minimal axis count by exhaustive linear-extension
  search; realizer rank magnitudes reproduce the order on **all n^2 ordered
  pairs in all 405 cases**.
- **Dimension census** (classes per minimal axis count):

| n | dim 1 | dim 2 | dim 3 |
| --- | --- | --- | --- |
| 1 | 1 | — | — |
| 2 | 1 | 1 | — |
| 3 | 1 | 4 | — |
| 4 | 1 | 15 | — |
| 5 | 1 | 62 | — |
| 6 | 1 | 314 | **3** |

- Tie-collapse (total-preorder axes add nothing):
  - n <= 5, d <= 2 exhaustive: achieved posets == dim <= 2 posets at every
    n (weak-order counts 1, 3, 13, 75, 541; achieved labeled posets at
    d = 2: 1, 3, 19, 219, 4,231 — independently reproducing the labeled
    counts, since every poset with n <= 5 has dim <= 2).
  - d = 1 exhaustive: single-preorder-representable == chains at every n.
  - n = 6, d = 2 targeted: all three dimension-3 classes refuted over all
    pairs of extending weak orders (446^2 = 198,916 and 256^2 = 65,536
    twice; zero representations found).
  - Constructive lexicographic linearization verified on **4,473**
    first-found preorder witnesses: all pass.

### Theorem 2 — Anti-Scalar as d = 1

- dim(P) = 1 iff P is a chain: holds for all 405 classes; every
  incomparable pair forces dim >= 2.
- **T49 witness regression:** the 3-event shape {(0, 2), (1, 2)} has
  dim = 2, incomparable pair list [(0, 1)] (index-sorted; 0 = e1_A_locking,
  1 = e2_B_locking, 2 = e3_composite_locking, sorted by name). The actual
  T49 model's record order re-imports as the same shape, its dim recomputes
  as 2, and its own `comparison_2axis.is_exact_match` re-asserts True.
  T49's 2-axis success is the dim = 2 case of Theorem 1.

### Theorem 3 — Axis-count obstruction (standard examples)

| example | events | linear extensions | closed form (d!)^2 + d((d-1)!)^2 | max diagonal reversals per extension | minimal axis count | method |
| --- | --- | --- | --- | --- | --- | --- |
| S_2 | 4 | 6 | 6 | 1 | 2 | census (n = 4 sweep) |
| S_3 | 6 | 48 | 48 | 1 | **3** | brute force (all extensions / pairs) |
| S_4 | 8 | 720 | 720 | 1 | **4** | brute force, orbit-pruned |
| S_5 | 10 | 17,280 | 17,280 | 1 | **5** | certificate + explicit realizer |

- S_4 refutations: d = 2 full scan over 720 extensions; d = 3 exhaustive
  with automorphism-orbit pruning — |Aut(S_4)| = 24, 30 orbit
  representatives for the first extension, **21,600 pairs scanned, no
  realizer** (coverage argument in spec; orbit-action soundness asserted in
  code).
- S_5 certificate (all machine-checked): cross pairs present; all 5
  diagonal pairs incomparable; all C(5,2) = 10 two-reversal cycle
  certificates; every one of the 17,280 extensions reverses at most one
  diagonal pair. Two-line pigeonhole in the spec closes dim >= 5 directly
  at the real-magnitude level. Explicit 5-realizer (index-sorted, L_k
  reverses exactly diagonal pair k):

```text
L_1 = (1, 2, 3, 4, 5, 0, 6, 7, 8, 9)
L_2 = (0, 2, 3, 4, 6, 1, 5, 7, 8, 9)
L_3 = (0, 1, 3, 4, 7, 2, 5, 6, 8, 9)
L_4 = (0, 1, 2, 4, 8, 3, 5, 6, 7, 9)
L_5 = (0, 1, 2, 3, 9, 4, 5, 6, 7, 8)
```

  intersection exactly S_5; rank magnitudes reconstruct on all 100 pairs.
- The d = 4 brute force for S_5 was **not attempted** (infeasible); the
  certificate machinery is cross-validated on S_3 and S_4 where brute force
  independently agrees.
- **Consequence:** 4-axis reconstruction covers exactly order dimension
  <= 4; S_5 escapes. Whether physical causal orders exceed dimension 4:
  open, flagged as candidate prior-art territory (Minkowski causal-order
  dimension literature, from memory, unverified).

### Theorem 4 — Realizability via T48's containment rule

| variant | exact on | note |
| --- | --- | --- |
| faithful (locked strict-downset + own raw as source; locked principal downset as target) | **405 / 405** | mirrors T48's own witness bases |
| single basis (locked principal downset both roles) | **405 / 405** | simplified statement |
| strict downsets | 6 / 405 | succeeds **only on antichains** |

- Non-empty clause: vacuous for principal downsets (every target basis
  contains the event's own locked record) — verified on all classes. For
  strict downsets it deletes every dependency out of minimal events:
  2-chain witness — poset [(0, 1)], strict-variant closure **[]** (fails);
  faithful variant recovers [(0, 1)] exactly. No fix to T48's rule is
  needed; the principal downset is the faithful reading.

### House-object spotlight — S_3 as FinaliEvents

- Six events `s3_a1, s3_a2, s3_a3, s3_b1, s3_b2, s3_b3` (index-sorted) over
  D1RestrictionSystems (unobstructed sources, obstructed parity-conflict
  targets, T48 builder pattern): **all six `fully_admissible`** (PO1).
- Record-dependency order computed with T48's own `_compute_order` from the
  Theorem 4 bases: is a partial order and **equals S_3 exactly** (12 pairs
  including reflexive).
- AM (T49's own `_compare_orders`): with axes
  (causal = reversal_cost, info = holder_redundancy,
  obs_access = accessible_support) set to the 3-realizer ranks and
  branch = 0, the 3-axis componentwise order matches the record order
  **36/36 ordered pairs**; every proper subset of the three axes fails
  (all six subsets checked: causal / info / obs_access alone and all three
  2-axis combinations, each inexact). Executable house instantiation of
  dim(S_3) = 3.

### Runtimes (informational)

```text
enumeration                 2.4 s
theorem1 dimension sweep    0.1 s
theorem1 tie-collapse      11.0 s
theorem2                    0.2 s
theorem3                    0.4 s
theorem4                    0.03 s
house spotlight             0.002 s
total                      ~14.1 s
```

## Honest weaknesses (reviewer-facing)

- **Novelty:** if the from-memory Dushnik-Miller attribution is correct,
  Theorems 1-3 are re-derivations; the earned content is the exhaustive
  finite verification, the tie-collapse closure, Theorem 4's realizability
  under T48's specific containment rule, and the executable D1/PO1 bridge.
  Stated in the spec before a reviewer has to say it.
- The tie-collapse lemma is enumeration-backed only at (n <= 5, d <= 2) and
  (n = 6, d = 2, dim-3 classes); beyond that it is proof-backed (short
  lexicographic-refinement proof in the spec, constructively verified on
  4,473 witnesses).
- dim(S_5) >= 5 is certificate-backed, not brute-force-backed; the
  certificate is cross-validated at S_3/S_4. The two-line pigeonhole is
  spec-level logic whose finite ingredients are machine-checked.
- The spotlight's axis magnitudes are abstract realizer ranks carried in
  D1Profile fields; no physical magnitude semantics is claimed.
- n = 7+ census not attempted (runtime cap), so "exactly 3 dimension-3
  classes" is an n = 6 statement only.

## pytest output

```text
platform linux -- Python 3.10.12, pytest-9.1.1, pluggy-1.6.0
collected 29 items

tests/test_axis_count_reconstruction_hierarchy.py::test_enumeration_iso_class_counts PASSED
tests/test_axis_count_reconstruction_hierarchy.py::test_enumeration_internal_identities_hold PASSED
tests/test_axis_count_reconstruction_hierarchy.py::test_labeled_counts_match_prior_direction_a_report PASSED
tests/test_axis_count_reconstruction_hierarchy.py::test_theorem1_realizer_magnitudes_reconstruct_for_all_classes PASSED
tests/test_axis_count_reconstruction_hierarchy.py::test_theorem1_dimension_census PASSED
tests/test_axis_count_reconstruction_hierarchy.py::test_theorem1_tie_collapse_preorders_add_nothing PASSED
tests/test_axis_count_reconstruction_hierarchy.py::test_theorem1_dim3_classes_have_no_two_preorder_representation PASSED
tests/test_axis_count_reconstruction_hierarchy.py::test_theorem1_lexicographic_linearization_verified_on_all_witnesses PASSED
tests/test_axis_count_reconstruction_hierarchy.py::test_theorem1_holds PASSED
tests/test_axis_count_reconstruction_hierarchy.py::test_theorem2_dim1_iff_chain_up_to_n6 PASSED
tests/test_axis_count_reconstruction_hierarchy.py::test_theorem2_t49_witness_regression PASSED
tests/test_axis_count_reconstruction_hierarchy.py::test_theorem2_any_incomparable_pair_blocks_single_axis PASSED
tests/test_axis_count_reconstruction_hierarchy.py::test_theorem2_holds PASSED
tests/test_axis_count_reconstruction_hierarchy.py::test_theorem3_s3_needs_exactly_three_axes PASSED
tests/test_axis_count_reconstruction_hierarchy.py::test_theorem3_s3_appears_in_n6_census_as_dim3 PASSED
tests/test_axis_count_reconstruction_hierarchy.py::test_theorem3_s4_needs_exactly_four_axes PASSED
tests/test_axis_count_reconstruction_hierarchy.py::test_theorem3_s5_escapes_four_axes PASSED
tests/test_axis_count_reconstruction_hierarchy.py::test_theorem3_certificate_cross_validated_against_brute_force PASSED
tests/test_axis_count_reconstruction_hierarchy.py::test_theorem3_explicit_realizer_reverses_exactly_one_diagonal_each PASSED
tests/test_axis_count_reconstruction_hierarchy.py::test_theorem3_holds PASSED
tests/test_axis_count_reconstruction_hierarchy.py::test_theorem4_principal_downset_bases_realize_every_poset PASSED
tests/test_axis_count_reconstruction_hierarchy.py::test_theorem4_strict_downset_variant_fails_outside_antichains PASSED
tests/test_axis_count_reconstruction_hierarchy.py::test_theorem4_two_chain_micro_witness PASSED
tests/test_axis_count_reconstruction_hierarchy.py::test_theorem4_holds PASSED
tests/test_axis_count_reconstruction_hierarchy.py::test_house_spotlight_events_are_po1_admissible PASSED
tests/test_axis_count_reconstruction_hierarchy.py::test_house_spotlight_record_order_is_s3 PASSED
tests/test_axis_count_reconstruction_hierarchy.py::test_house_spotlight_am_holds_on_three_axes_and_fails_on_subsets PASSED
tests/test_axis_count_reconstruction_hierarchy.py::test_primitives_sanity_on_small_cases PASSED
tests/test_axis_count_reconstruction_hierarchy.py::test_all_theorems_hold_and_verdict_language_is_restrained PASSED

29 passed in 13.29s
```

The T48/T49/T50 runners (`python -m models.run_t48` / `run_t49` / `run_t50`)
were re-run alongside and rewrote no tracked result content (empty diff).

## Recommended next (no promotion)

- Prior-art verification pass (Dushnik-Miller, Trotter, Minkowski
  causal-order dimension) before any of this enters `literature/` or
  paper-facing text.
- Direction A rung 2: the process-matrix translation — the audit's single
  creative hinge. The dimension census and the S_d escape witnesses are the
  raw material this artifact hands to that attempt.
