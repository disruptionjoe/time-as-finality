# T239: Rank-k NON-CYCLE-SHAPED genre -- CAP/consensus quorum-intersection (fourth absorber)

## Verdict: conditional (PASS_NONCYCLE_GENRE at the gate; whether this makes the cross-domain RANK classification GENRE-AGNOSTIC is the integrator's call)

The non-cycle-shaped genre experiment **fired and cleared** the residual edge that
T234 left open by name. A single domain-neutral invariant kappa, **imported verbatim**
from T224 (the same `compute_kappa`, object-identity-confirmed, not re-tuned), was
computed on a domain-A T39 instance for kappa in {0, 1, 2, 3}, transported by an
explicit structure-preserving map to a **FOURTH a-priori-unrelated absorber B'''**
whose native obstruction is computed by a **structurally different, NON-cycle-shaped
mechanism**: a **quorum-intersection failure** (two quorums with empty intersection --
a Helly/set-cover obstruction over node SETS) in a **fresh CAP/consensus quorum system
built from scratch**. The transported kappa predicted the exact integer native rank
**before** B''' was measured natively, and the prediction held on all four rungs:

| domain-A instance (T39) | kappa_A | predicted kappa_B''' | native B''' rank (disjoint split-brain blocks) | nu-side kappa_B''' | match |
|---|---|---|---|---|---|
| three_cell_transitive (three disjoint odd 3-cycles) | 3 | 3 | 3 (three vertex-disjoint pairs of non-intersecting quorums) | 3 | yes |
| two_cell_transitive (two disjoint odd 3-cycles) | 2 | 2 | 2 (two vertex-disjoint split-brain blocks) | 2 | yes |
| one_cell_transitive (one odd 3-cycle) | 1 | 1 | 1 (one split-brain block, two disjoint quorums) | 1 | yes |
| satisfiable_all_same | 0 | 0 | 0 (global intersection property holds, no split brain) | 0 | yes |

The off-by-one guard held (kappa_A = 1 -> native **1, not 2**; kappa_A = 0 -> the
global intersection property, native **0**), and the **rank ceiling is pushed past
T234's k = 2 to k = 3**: ranks {0, 1, 2, 3} land distinctly on the native witness, so
the integer rank, not its sign, is load-bearing across a **fourth domain in a third
native genre that is not cycle-shaped at all**.

This is the first cycle in which the cross-domain rank law is witnessed against a
native obstruction that is **not any kind of cycle**:

- **T234's residual "cycle-shaped only" edge is retired.** T21/T229 (parity cycle)
  and T234 (directed tournament cycle) are both *cycle-shaped* native witnesses.
  B'''s native witness is a **Helly / set-cover** obstruction: two quorums with
  **empty intersection**. The genre-distinctness certificate (`_native_witness_is_helly_not_cyclic`)
  proves three structural facts a cycle witness fails:
  1. **Helly-monotone:** adding ONE shared node to both quorums of a failing block
     **destroys** the obstruction (rank 1 -> 0). A frustrated parity cycle or a
     directed tournament cycle is *not* destroyed by adding a vertex to two of its
     sets, because it is carried by a cycle, not a set intersection. This is the
     decisive separator.
  2. **Acyclic witness:** the within-quorum agreement graph of a failing block is a
     forest (no cycle), so there is **no cycle present to carry a parity or
     orientation**, yet the obstruction fires. A parity-cycle and a tournament-cycle
     witness both *require* a cycle in the witness; this one provably has none.
  3. **Set-structure invariant:** the native rank is unchanged under within-side
     relabeling and the native function calls **none** of the cycle/parity helpers
     (`compute_kappa`, `majority_tournament`, `_beats`, `parity_product`,
     `analyze_chsh_finality`, `native_condorcet_obstruction`) -- checked on
     `co_names` (what the code calls), immune to comment wording.

- **Rank, not just presence, separated in the new genre.** The decisive (1, 2, 3)
  separation -- one vs. two vs. three vertex-disjoint split-brain blocks -- is a
  distinction a present/absent classifier provably cannot make, and the transported
  kappa predicts which. An adversarial test (one block carrying THREE mutually
  disjoint quorums, i.e. three disjoint quorum *pairs*) confirms the witness reports
  independent **rank 1**, not an inflated pair multiplicity.

The verdict is reported as **conditional** (not unconditionally `closed`) because this
lane is one worker: whether the cross-domain RANK classification is admitted as
**genre-agnostic** across the now-FOUR absorbers / THREE genres is the **integrator's**
ratification, not this lane's to assert. What is unconditional here: the experiment
ran, the kappa predictions were made before measurement, and they held across all four
rungs with no shared derivation, no re-tuning, and against a native witness of a
structurally different, non-cycle-shaped genre.

**Failure conditions (explicit, none triggered).** The verdict would have been
`KILLED` if (a) the kappa prediction mispredicted on any rung, (b) `compute_kappa` had
to be re-tuned for the consensus domain, or (c) the transport path secretly shared
T39's or CAP's derivation. It would have been `CYCLE_SHAPED_ONLY` if the native witness
had turned out to be (secretly) a cycle/parity witness. All are checked in code and all
are clean (`verdict == "PASS_NONCYCLE_GENRE"`, `gate_cleared == True`).

## What was derived from the sources

- **tests/T234-kappa-genre-crossing-third-absorber.md** named the exact missing object
  in its "Constructive next object" section, verbatim: a **non-cycle-shaped native
  genre** -- the T28 CAP/consensus absorber measured by its **own quorum-intersection
  witness** (a failure of two quorums to intersect, a set-cover/Helly-type obstruction,
  not a cycle), with kappa transported in, AST-proving the transport path imports no
  `d1_restriction_system`. This lane builds exactly that object.
- **open-problems/typed-loss-transport-test.md** supplied the protocol (compute
  kappa_A; build a structure-preserving A->B map with no shared derivation; predict B
  before measuring; measure natively; compare), the PASS bar (prediction holds across
  >= 2 unrelated absorbers, rank load-bearing), and the disqualifiers (per-domain
  re-tuning; trivial shared derivation; transport path must not import the d1 engine,
  and `cap_theorem_bridge` is disqualified because it imports that engine).
- **models/typed_loss_transport.py** supplied the SINGLE domain-neutral `compute_kappa`
  and `nu_from_binary_csp`, both reused **unchanged** (object identity with
  `compute_kappa` asserted in the AST audit and tested) and the rung/honesty-guard
  pattern (native witness independent of `compute_kappa`; AST shared-derivation audit;
  per-cell nu cover analogous to the per-box / per-triple cover). The native witness
  mechanism is **replaced** by a quorum set-intersection failure -- the genre cross --
  and the A-side builders are reused (generalized to arbitrary k).

## Strongest positive result

kappa transported A -> B''' and predicted B''' **exactly at the integer level** across
four rungs {0, 1, 2, 3}, with the prediction made before B''' was measured natively,
and the native witness measured by a **set-intersection (Helly) failure independent of
the kappa machinery** (see the table above).

The decisive distinction a presence classifier cannot make is the **(1, 2, 3)
separation**, here landing in a native genre that is **not a cycle at all**.

**Honesty guards that make this non-vacuous (all executed in code, all clean):**

- **Genre is genuinely non-cycle (Helly/set-cover witness).** `native_quorum_obstruction`
  reads node SETS and counts vertex-disjoint pairs of **non-intersecting quorums**. The
  certificate `_native_witness_is_helly_not_cyclic` proves it is Helly-monotone
  (a shared node kills the obstruction), carried by an acyclic agreement forest, and
  set-structure invariant -- none of which a cycle witness is.
  (`test_native_witness_is_helly_not_cycle_shaped`,
  `test_helly_monotonicity_shared_node_kills_obstruction`,
  `test_native_witness_carries_no_cycle`,
  `test_native_witness_calls_no_cycle_or_parity_helpers`.)
- **Native rank measured WITHOUT compute_kappa (co_names proven).** The native
  witness's compiled `co_names` contain no `compute_kappa` and no cycle/parity helper.
  (`test_native_witness_does_not_call_compute_kappa`,
  `test_native_witness_calls_no_cycle_or_parity_helpers`.)
- **nu-cover and native witness are INDEPENDENT code paths.** `nu_from_quorum_system`
  does not call `native_quorum_obstruction` and the native witness does not call
  `nu_from_quorum_system` or `compute_kappa`; their agreement on the same integer is
  corroboration through independent code, not one calling the other.
  (`test_nu_cover_does_not_call_native_witness_and_vice_versa`.) The per-block nu cover
  (one signed odd 3-cycle per independent failing block) is the direct analogue of
  T229's per-box / T234's per-triple cover, so kappa = independent native rank by
  construction, not by tuning.
- **No shared derivation (AST-checked, precisely scoped).** A dedicated AST scan of the
  genuine transport-path functions (module top-level imports + the transport functions'
  own imports, **excluding** the inspection-only audit helper) proves the transport
  path imports **neither** `models.d1_restriction_system` **nor**
  `models.cap_theorem_bridge`. The native quorum witness is built **fresh from
  scratch** precisely to avoid `cap_theorem_bridge` (which imports the d1 engine).
  T28/CAP is re-confirmed disqualified: its source DOES import the d1 engine
  (inspected, not routed through).
  (`test_transport_path_imports_neither_d1_nor_cap`,
  `test_ast_audit_clean_and_cap_disqualified`,
  `test_fresh_native_witness_does_not_import_cap_theorem_bridge_at_top_level`.)
- **kappa NOT re-tuned (object identity).** `compute_kappa is typed_loss_transport.compute_kappa`
  is asserted and tested. (`test_compute_kappa_is_the_verbatim_T224_object`.)
- **Rank is independent, not inflated.** A block with three disjoint quorums (three
  disjoint quorum *pairs*) is counted as independent **rank 1**, not 3.
  (`test_adversarial_many_disjoint_quorum_pairs_in_one_block_count_as_rank_1`.) The
  construction scales mechanically: native rank == k for k = 0..5
  (`test_k_split_brain_system_scales_to_arbitrary_k`).

## First exact obstruction / missing object

With the cycle-shaped-only edge retired, the cross-domain rank law is now witnessed
across **four** absorbers spanning **three** native genres (signed-graph parity cycle;
oriented-tournament directed cycle; Helly/set-cover quorum-intersection failure), at
ranks {0, 1, 2, 3}. The first remaining obstruction to an unconditional `closed` is no
longer "cycle-shaped only"; it is **whether genre-agnosticism is now established or
merely strongly indicated**:

1. **Three genres, strong but not a proof of arbitrariness.** Three structurally
   distinct native witnesses now agree with the transported integer, including one that
   is provably non-cycle. Whether this licenses the *general* claim "the rank law holds
   in any absorber that presents a binary same/different cover" -- as opposed to "holds
   across these three demonstrated genres" -- is a generalization the finite witnesses
   do not by themselves prove. It is the integrator's call whether four absorbers /
   three genres / rank ceiling 3 suffices to ratify genre-agnosticism.
2. **All witnesses share the per-cell nu encoding.** Every domain's nu cover is, by the
   transport-test's design, the universal binary same/different cover (one signed odd
   3-cycle per independent cell). The genre cross lives entirely in the **native**
   witnesses, which differ structurally. A residual skeptic could ask for a native
   witness whose *independent-cell notion* is itself non-combinatorial (e.g. a
   continuous value-gap rank); that is the next genre frontier, and it is untested.

## Constructive next object (named, not built here)

A **non-combinatorial native genre**: an absorber whose native obstruction rank is a
**value-gap / rate-distortion floor** (a POMDP value gap or a rate-distortion rank,
named in `open-problems/typed-loss-transport-test.md`) -- a native witness that is
neither a cycle nor a finite set-intersection failure but a real-valued separation
whose **integer rank** (number of independent above-floor gaps) is transported-kappa-
predicted. Passing at k >= 2 against such a witness would push the rank law past the
finite-combinatorial boundary entirely and make the strongest case for genre-
agnosticism. If it misses, the transport law's exact boundary is named (finite-
combinatorial native obstructions only) -- still a real, citable three-genre result.

## Meaning for the relevant claim

- The **breakout bet** (heterodox/orthodox 62-persona pass) is **not killed and its
  promotion gate is now hardened past the cycle-shaped boundary**: a structure-
  preserving map across genuinely independent code predicted the **exact integer** count
  of independent obstructions in a fourth absorber whose native witness is a Helly/
  set-cover obstruction -- not any kind of cycle -- separating ranks 1, 2, and 3.
- It **completes the residual edge T234 left open**: the cross-domain RANK
  classification (`kappa transported from A predicts the exact integer number of
  independent native obstructions in an unrelated absorber`) is now witnessed across
  FOUR unrelated absorbers and THREE native genres, so it is **not confined to
  cycle-shaped native obstructions**. This statement lives in **no single absorber**,
  which is exactly the **independent motivation** the 2026-06-24
  MATHEMATICAL-INDEPENDENCE-AUDIT found NOT EARNED (criterion 6). Whether this moves the
  cross-domain rank classification to **genre-agnostic** (and whether T224 / the claim
  promotes) is the **integrator's** ratification.
- It **promotes no physics / geometry / curvature / new-object / CAP-theorem-as-law
  language.** kappa is a Z/2 graph-homology rank over a finite cover; "quorum" is a
  finite node subset; "split brain" is a pair of node subsets with empty intersection;
  "quorum-intersection failure" is the emptiness of a finite set intersection. No
  consensus-as-physical-law, no CAP-theorem-as-metaphysics: the only claim is a finite
  cross-domain rank-classification statement, tagged finite_witness + poly_decider.

## Recommendation to the integrator

- Treat T239 as the FOURTH absorber and the THIRD native genre (first non-cycle-shaped)
  for the cross-domain RANK classification. The rank ceiling is now witnessed to k = 3.
- The honest available move is to upgrade the cross-domain rank classification from
  "witnessed across three cycle-shaped-and-tournament genres" to "witnessed across
  three genres, one of which is provably non-cycle (Helly/set-cover)", i.e. the rank
  law is **genre-AGNOSTIC across the demonstrated genres**, NOT confined to cycle-shaped
  native obstructions. Whether to phrase the promotion as fully "genre-agnostic" vs.
  "non-cycle genre demonstrated" is the integrator's call (see First-obstruction item 1).
- Do NOT promote any new-object/physics/consensus-as-law language; the result is a
  finite cross-domain rank-classification statement only.

## Next proof / computation step

Build the non-combinatorial native genre named above (a value-gap / rate-distortion
rank witness, transport path AST-clean of `d1_restriction_system` and
`cap_theorem_bridge`), transport kappa = k before measuring, and verify the integer
rank prediction against a native witness that is neither a cycle nor a finite
set-intersection failure. If it holds, the genre boundary is pushed past finite
combinatorics and the rank classification's genre-agnosticism is maximally supported.
If it misses, the transport law's exact boundary is named -- still a real, citable
three-genre cross-domain result.

## Complexity / language tags

- `finite_witness`: all instances are finite executable fixtures (T39 k-cell covers for
  k in {0,1,2,3}; quorum systems of 5--12 nodes with 2--6 quorums); no scalable /
  continuum theorem is asserted. The rank ladder demonstrated is {0, 1, 2, 3}, stated
  as such; genres demonstrated are three (parity cycle; tournament directed cycle;
  Helly set-cover).
- `poly_decider`: kappa is union-find spanning forest + BFS Z/2 potential; the native
  rank is quorum-pair enumeration + set-intersection emptiness test + greedy
  vertex-disjoint block packing (O(|quorums|^2 * |nodes| + |nodes|)). Both are finite
  classifiers over declared inputs, NOT hidden searches and NOT NP-hardness claims. No
  CSP-completeness or hardness language is used.
- No general Cech/sheaf-cohomology theorem is promoted; "dim H^1" is the finite Z/2
  cycle-space rank of a specific finite cover, named as such.

## Known Physics Constraints

None. T239 is a finite typed-machinery audit. The consensus side is used only as a
structural set-system cover (quorum family + same/different parity), not as a
distributed-systems CAP-theorem-as-physical-law derivation. No time, observer-
metaphysics, curvature, holonomy, gravity, or new-object language is used; "quorum" and
"quorum-intersection failure" are set-theoretic (a finite node subset; the emptiness of
a finite set intersection).

## Reproduction

```bash
python -m pytest tests/test_kappa_quorum_intersection_transport.py -v
python -m models.kappa_quorum_intersection_transport          # prints the full protocol JSON
# raw output: results/kappa-quorum-intersection/T239-results.json
# regression (T224 + T229 + T234 untouched):
#   python -m pytest tests/test_typed_loss_transport.py tests/test_kappa_rank2_transport.py \
#     tests/test_kappa_genre_crossing_transport.py tests/test_kappa_quorum_intersection_transport.py -q
```
