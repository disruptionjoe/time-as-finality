# T234: Rank-k GENRE-CROSSING third absorber -- hostile-domain completion

## Verdict: conditional (PASS_GENRE_CROSS at the gate; whether this moves T224 conditional -> closed is the integrator's call)

The genre-crossing rank-k experiment **fired and cleared** the residual edge that
T229 left open by name. A single domain-neutral invariant kappa, **imported
verbatim** from T224 (the same `compute_kappa`, AST-confirmed identical object, not
re-tuned), was computed on a domain-A T39 instance with **kappa_A = 2** (two disjoint
frustrated odd cycles), transported by an explicit structure-preserving map to a
**THIRD a-priori-unrelated absorber B''** whose native obstruction is computed by a
**structurally different, NON-signed-graph mechanism** -- a directed-3-cycle
(Condorcet) count over an **oriented majority tournament** (the Arrow/SMD social-
choice genre) -- and **predicted kappa_B'' = 2 and both native independent
obstructions before B'' was measured natively**. Measured natively, via T234's own
tournament cycle witness with **no** appeal to the kappa machinery (AST-proven, see
below), B'' carried **exactly two** vertex-disjoint Condorcet cycles, matching the
prediction. The off-by-one guard held (kappa_A = 1 -> native rank **1, not 2**;
kappa_A = 0 -> a transitive profile with a Condorcet winner, native rank **0**), so
the integer rank, not its sign, is load-bearing across a third domain in a **second
native genre**.

This is the first cycle in which the cross-domain rank law is witnessed across a
native obstruction witness that is **not** a Z/2 signed-graph parity product:

- **The residual "same-genre" edge (T229's first exact obstruction) is retired.**
  T21 single-box CHSH (T224) and the T229 two-box CHSH are both frustrated-cycle /
  parity covers whose native witness is a sign-symmetric parity product. B'''s native
  witness is a **directed** cycle in an **oriented** tournament: orientation is
  load-bearing (reversing every majority edge gives the opposite tournament, not a
  symmetry), which a parity product structurally cannot represent. The genre cross is
  certified in code (`_native_witness_is_orientation_sensitive`): under ballot
  reversal the obstruction still fires while at least one majority edge flips sign --
  impossible for a sign-flip-invariant Z/2 witness.

- **Rank, not just presence, separated in the new genre.** The decisive (1, 2)
  separation -- one Condorcet triple vs. two vertex-disjoint Condorcet triples -- is a
  distinction a present/absent classifier provably cannot make, and the transported
  kappa predicts which. An adversarial 4-candidate test (several overlapping
  3-cycles) confirms the witness reports independent **rank 1**, not an inflated raw
  triple multiplicity.

The verdict is reported as **conditional** (not unconditionally `closed`) because
this lane is one worker: whether T224 itself moves `conditional -> closed` and the
cross-domain RANK classification theorem is admitted across the now-THREE absorbers /
TWO genres is the **integrator's** ratification, not this lane's to assert. What is
unconditional here: the experiment ran, the kappa = 2 prediction was made before
measurement, and it held with no shared derivation, no re-tuning, and against a
native witness of a structurally different genre.

**Failure conditions (explicit, none triggered).** The verdict would have been
`KILLED` if (a) the kappa prediction mispredicted on any rung, (b) `compute_kappa` had
to be re-tuned for the social-choice domain, or (c) the transport path secretly shared
T39's or CAP's derivation. It would have been `SAME_GENRE` if the native witness had
turned out not to be orientation-sensitive (i.e. secretly a parity cover). All four
are checked in code and all four are clean (`verdict == "PASS_GENRE_CROSS"`,
`gate_cleared == True`).

## What was derived from the sources

- **tests/T229-kappa-rank2-second-absorber.md** named the exact missing object in its
  "First exact obstruction" and "Constructive next object" sections, verbatim: a
  rank-k third absorber whose neighbor-visible cover is a parity cover but whose
  **native** obstruction is **not** a signed-graph frustration computation
  (candidates: Arrow/SMD aggregation, or CAP read through its own commit witness),
  with kappa transported in. This lane builds exactly that object, choosing Arrow/SMD.
- **open-problems/typed-loss-transport-test.md** supplied the protocol (compute
  kappa_A; build a structure-preserving A->B map with no shared derivation; predict B
  before measuring; measure natively; compare) and the PASS bar (prediction holds
  across **>= 2** unrelated absorbers, rank load-bearing) and the disqualifiers
  (per-domain re-tuning; trivial shared derivation).
- **models/kappa_rank2_transport.py** supplied the rung structure (kappa in {0,1,2}
  with off-by-one guards) and the honesty-guard pattern (native witness independent
  of `compute_kappa`; AST shared-derivation audit; per-cell nu cover analogous to the
  per-box cover). The native witness mechanism is **replaced** by a tournament
  directed-cycle count -- the genre cross -- and the A-side builders are reused.
- **models/typed_loss_transport.py** supplied the SINGLE domain-neutral
  `compute_kappa` and `nu_from_binary_csp`, both reused **unchanged** (object identity
  with `compute_kappa` asserted in the AST audit and tested).

## Strongest positive result

kappa transported A -> B'' and predicted B'' **exactly at the integer level** across
three rungs, with the prediction made before B'' was measured natively, and the native
witness measured by a tournament directed-cycle count **independent of the kappa
machinery**:

| domain-A instance (T39) | kappa_A | predicted kappa_B'' | native B'' rank (Condorcet tournament cycles) | nu-side kappa_B'' | match |
|---|---|---|---|---|---|
| two_cell_transitive (two disjoint odd 3-cycles) | 2 | 2 | 2 (two vertex-disjoint Condorcet triples {a,b,c}, {d,e,f}) | 2 | yes |
| one_cell_transitive (one odd 3-cycle) | 1 | 1 | 1 (one Condorcet paradox, no winner) | 1 | yes |
| satisfiable_all_same | 0 | 0 | 0 (transitive profile, Condorcet winner = a) | 0 | yes |

The decisive distinction a presence classifier cannot make is the **(1, 2)
separation**, here landing in a native genre that is not a parity cover at all.

**Honesty guards that make this non-vacuous (all executed in code, all clean):**

- **Genre is genuinely different (orientation-sensitive native witness).**
  `native_condorcet_obstruction` reads a strict majority **tournament** (an oriented
  complete digraph) and counts vertex-disjoint **directed** 3-cycles. The certificate
  `_native_witness_is_orientation_sensitive` shows that under global ballot reversal
  the obstruction still fires while a majority edge flips sign -- a sign-symmetric
  parity product is invariant under exactly that operation, so the witness is provably
  not a Z/2 parity computation. (`test_native_witness_is_orientation_sensitive`,
  `test_reversed_profile_flips_a_majority_edge`.)
- **Native rank measured WITHOUT compute_kappa (AST + co_names proven).** The native
  witness's compiled `co_names` contain no `compute_kappa`; the AST audit confirms it.
  (`test_native_witness_does_not_call_compute_kappa`.)
- **nu-cover and native witness are INDEPENDENT code paths.** `nu_from_condorcet` does
  not call the native packing and the native witness does not call `nu_from_condorcet`
  or `compute_kappa`; their agreement on the same integer is corroboration through
  independent code, not one calling the other.
  (`test_nu_cover_does_not_call_native_packing_and_vice_versa`.) The per-cell nu cover
  (one signed 3-cycle per independent Condorcet triple, referenced against a single
  domain-neutral Copeland-descending order) is the direct analogue of T229's
  per-**box** cover, so kappa = independent native rank by construction, not by tuning.
- **No shared derivation (AST-checked, precisely scoped).** A dedicated AST scan of
  the genuine transport-path functions (module top-level imports + the transport
  functions' own imports, **excluding** the inspection-only audit helper) proves the
  transport path imports **neither** `models.d1_restriction_system` **nor**
  `models.cap_theorem_bridge`. T28/CAP is re-confirmed disqualified: its source DOES
  import the T39 engine (inspected, not routed through). This satisfies the brief's
  CAP-eligibility rule (no `d1_restriction_system` in the transport path) by choosing
  the Arrow/SMD route, which avoids the engine entirely.
  (`test_transport_path_imports_neither_d1_nor_cap`, `test_ast_audit_clean_and_cap_disqualified`.)
- **kappa NOT re-tuned (object identity).** `compute_kappa is typed_loss_transport.compute_kappa`
  is asserted and tested. (`test_compute_kappa_is_the_verbatim_T224_object`.)

## First exact obstruction / missing object

With the same-genre edge retired, the cross-domain rank law is now witnessed across
**three** absorbers spanning **two** native genres (signed-graph parity product;
oriented-tournament directed cycle), at ranks {0, 1, 2}. The first remaining
obstruction to an unconditional `closed` is no longer "same genre"; it is **genre
breadth and rank ceiling**:

1. **Two genres, not yet an arbitrary genre.** Both genres cleared are still
   *cycle-shaped* native witnesses (a frustrated parity cycle; a directed tournament
   cycle). A native obstruction that is **not cycle-shaped at all** -- e.g. a
   CAP/commit obstruction read through its own commit witness (a quorum-intersection
   failure, not a cycle), or a rate-distortion / value-gap obstruction -- remains
   untested. (CAP is eligible per the brief only if its native witness is measured by
   its OWN commit witness and the transport path avoids `d1_restriction_system`;
   building that without routing through the shared engine is the next genre.)
2. **Rank ceiling at k = 2.** The ladder is witnessed at {0, 1, 2}. Arbitrary k (a
   kappa = 3 A-instance predicting three disjoint Condorcet triples in a 9-candidate
   tournament, etc.) is not yet witnessed; the construction extends mechanically but
   the executed fixture stops at 2.

## Constructive next object (named, not built here)

A **non-cycle-shaped native genre**: take the T28 CAP/consensus absorber and measure
its native obstruction by its **own commit/quorum-intersection witness** (a failure of
two quorums to intersect -- a set-cover/Helly-type obstruction, not a cycle), present
its neighbor-visible same/different cover, transport kappa = k, and predict the integer
number of independent native commit obstructions before measuring -- AST-proving the
transport path still imports no `d1_restriction_system`. Passing at k >= 2 against a
native witness that is not cycle-shaped would push the rank law past the second genre
boundary named above and make the cross-domain rank classification genre-agnostic.

## Meaning for the relevant claim

- The **breakout bet** (heterodox/orthodox 62-persona pass) is **not killed and its
  promotion gate is now hostile-domain hardened across genres**: a structure-
  preserving map across genuinely independent code predicted the **exact integer**
  count of independent obstructions in a third absorber whose native witness lives in
  a different structural genre, separating rank 1 from rank 2.
- It **completes the residual edge T229 left open**: the cross-domain RANK
  classification (`kappa transported from A predicts the exact integer number of
  independent native obstructions in an unrelated absorber`) is now witnessed across
  THREE unrelated absorbers and TWO native genres, so it is **not confined to the
  frustrated-cycle / CHSH structural genre**. This statement lives in **no single
  absorber**, which is exactly the **independent motivation** the 2026-06-24
  MATHEMATICAL-INDEPENDENCE-AUDIT found NOT EARNED (criterion 6). Whether this moves
  T224 `conditional -> closed` and whether the claim promotes PRESENCE/RANK ->
  genre-complete is the **integrator's** ratification.
- It **promotes no physics/geometry/curvature/new-object language.** kappa is a Z/2
  graph-homology rank over a finite cover; "Condorcet cycle" is a directed 3-cycle in
  a finite majority tournament; "majority tournament" is a finite oriented graph over
  a fixed candidate set. No social-welfare-as-physical-law, no Arrow's-theorem-as-
  metaphysics: the only claim is a finite cross-domain rank-classification statement,
  tagged finite_witness + poly_decider.

## Next proof / computation step

Build the non-cycle-shaped native genre named above (CAP commit/quorum-intersection
witness, transport path AST-clean of `d1_restriction_system`), transport kappa = k
before measuring, and verify the integer rank prediction against a native witness that
is not cycle-shaped. If it holds, the genre boundary is pushed past cycle-shaped
witnesses and the rank classification becomes genre-agnostic. If it misses, the
transport law's exact boundary is named (cycle-shaped native obstructions only) --
still a real, citable two-genre cross-domain result.

## Complexity / language tags

- `finite_witness`: all instances are finite executable fixtures (T39 two-cell cover;
  Condorcet profiles of 3 and 6 candidates with 3 ballots each); no scalable /
  continuum theorem is asserted. The rank ladder demonstrated is {0, 1, 2}, stated as
  such; genres demonstrated are two (parity product; tournament directed cycle).
- `poly_decider`: kappa is union-find spanning forest + BFS Z/2 potential; the native
  rank is majority-tournament construction (O(candidates^2 * ballots)) + directed
  3-cycle enumeration + greedy vertex-disjoint packing (O(candidates^3)). Both are
  finite classifiers over declared inputs, NOT hidden searches and NOT NP-hardness
  claims. No CSP-completeness or hardness language is used (open_hardness only, if any).
- No general Cech/sheaf-cohomology theorem is promoted; "dim H^1" is the finite Z/2
  cycle-space rank of a specific finite cover, named as such.

## Known Physics Constraints

None. T234 is a finite typed-machinery audit. The social-choice side is used only as
a structural aggregation cover (majority tournament + same/different parity), not as a
welfare-economics or Arrow's-impossibility-as-law derivation. No time, observer-
metaphysics, curvature, holonomy, or new-object language is used; "Condorcet cycle"
and "independent obstruction" are graph-theoretic (vertex-disjoint directed 3-cycles
in a finite tournament).

## Reproduction

```bash
python -m pytest tests/test_kappa_genre_crossing_transport.py -v
python -m models.kappa_genre_crossing_transport          # prints the full protocol JSON
# raw output: results/kappa-genre-crossing/T234-results.json
# regression (T224 + T229 untouched): \
#   python -m pytest tests/test_typed_loss_transport.py tests/test_kappa_rank2_transport.py tests/test_kappa_genre_crossing_transport.py -q
```
