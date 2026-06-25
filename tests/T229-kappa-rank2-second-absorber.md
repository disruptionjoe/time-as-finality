# T229: Rank-2 second unrelated absorber -- the breakout's actual promotion gate

## Verdict: conditional (PASS_RANK2 at the gate; T224 conditional -> closed is the integrator's call)

The rank-2 transport experiment **fired and cleared both** of the two structural
conditions that held T224 at `conditional`. A single domain-neutral invariant
kappa, **unchanged** from T224 (the same `compute_kappa`, not re-tuned), was
computed on a domain-A T39 instance with **kappa_A = 2** (two disjoint frustrated
odd cycles), transported by an explicit structure-preserving map to a **second,
a-priori-unrelated absorber B'** (two independent CHSH boxes, 8 settings, a
parity-product witness per box), and **predicted kappa_B' = 2 and both native
independent obstructions before B' was measured**. Measured natively -- via T21's
own per-box parity-product witness, with **no** appeal to the kappa machinery --
B' carried **exactly two** independent obstructions, matching the prediction. The
off-by-one guard held (kappa_A = 1 transported to native rank **1, not 2**), so the
integer rank, not merely its sign, is load-bearing across domains.

This is the first cycle in which **both** of T224's stated conditions are met at
once:

- **C1 (>= 2 unrelated absorbers).** B' = two-box CHSH is a SECOND absorber with no
  shared derivation (verified in code: neither T21 nor this module imports the T39
  `d1_restriction_system` engine; T28/CAP would and is correctly disqualified,
  exactly as T224 audited). Together with T21 in T224, the >= 2 bar is reached.
- **C2 (rank, not just presence).** The cross-domain step exercised kappa = 2 and
  **separated** native rank 1 from native rank 2 -- a distinction a binary
  present/absent classifier provably cannot make. This upgrades the earned claim
  from obstruction-PRESENCE transport (T224) to obstruction-RANK transport.

The verdict is reported as **conditional** (not unconditionally `closed`) because
this lane is one worker; whether T224 itself moves `conditional -> closed` and the
cross-domain RANK classification theorem is admitted is the **integrator's**
ratification, not this lane's to assert. What is unconditional here: the experiment
ran, the kappa = 2 prediction was made before measurement, and it held with no
shared derivation and no re-tuning. The kill-switch did **not** kill the breakout;
it cleared its promotion gate.

**Failure conditions (explicit, none triggered):** the verdict would have been
`KILLED` if (a) the kappa = 2 prediction mispredicted (B' carrying only one native
obstruction, or the off-by-one guard collapsing rank 1 onto rank 2), or (b)
`compute_kappa` had to be re-tuned for the two-box domain, or (c) B' secretly shared
T39's derivation. All three are checked in code and all three are clean.

## What was derived from the sources

- **tests/T224-typed-loss-transport-test.md** named the exact missing object in its
  "Constructive next object" and "Next proof/computation step" sections: a rank >= 2
  unrelated absorber B' (candidate: two independent CHSH boxes / a two-cell
  contextuality scenario) so that kappa = 2 transported from a two-odd-cycle
  A-instance predicts both native obstructions; passing clears the two-absorber bar
  AND upgrades presence -> rank. This lane builds exactly that object.
- **open-problems/typed-loss-transport-test.md** supplied the protocol (compute
  kappa_A, build a structure-preserving A->B map with no shared derivation, predict
  B before measuring, measure natively, compare) and the PASS bar (prediction holds
  across **>= 2** unrelated absorbers) and the FAIL conditions (per-domain re-tuning;
  trivial shared derivation).
- **models/typed_loss_transport.py** supplied the SINGLE domain-neutral
  `compute_kappa` (union-find spanning forest + BFS Z/2 potential), `nu_from_chsh`,
  and the `shared_derivation_audit` pattern -- all reused unchanged. Its existing
  test `test_two_independent_odd_cycles_has_kappa_2` already confirmed the formula
  reports kappa = 2 for two disjoint frustrated triangles; this lane puts that rung
  to work across domains.

## Strongest positive result

kappa transported A -> B' and predicted B' **exactly at the integer level**, across
three rungs, with the prediction made before B' was measured natively, and the
native witness measured by T21's own per-box parity product (independent of the
kappa machinery):

| domain-A instance (T39) | kappa_A | predicted kappa_B' | native B' rank (T21 per-box parity) | nu-side kappa_B' | match |
|---|---|---|---|---|---|
| two_cell_transitive (two disjoint odd 3-cycles) | 2 | 2 | 2 (both boxes parity_product = -1) | 2 | yes |
| one_cell_transitive (one odd 3-cycle) | 1 | 1 | 1 (one box frustrated) | 1 | yes |
| satisfiable_all_same | 0 | 0 | 0 (no box frustrated) | 0 | yes |

The decisive distinction a presence classifier cannot make is the **(1, 2)
separation**: one-box-frustrated and two-box-frustrated are both "obstructed", but
native rank 1 != 2, and the transported kappa predicts which. This is the rank
information that T224 found was never load-bearing; here it is.

**Honesty guards that make this non-vacuous (load-bearing, all executed in code):**

- **Two genuinely independent native obstructions.** The two CHSH boxes use
  **disjoint settings** (8 settings, 2x4), so the two frustrated 4-cycles are
  vertex-disjoint -- two independent cells, not one relabeled 4-cycle. T21's
  full-scenario global-assignment search confirms no global section exists when the
  boxes are frustrated.
- **Native rank measured WITHOUT compute_kappa.** `native_two_box_obstruction` runs
  T21's own `analyze_chsh_finality` per box and counts frustrated boxes; the test
  `test_native_witness_does_not_call_compute_kappa` inspects the function's compiled
  `co_names` to prove it never calls the kappa machinery. The nu-side kappa and the
  native rank are therefore independent corroboration, both landing at 2.
- **No shared derivation (AST-checked).** `shared_derivation_audit_rank2` and the
  test parse the module AST: B' (the bell module) and this harness contain **no
  import** of `d1_restriction_system`; T28/CAP **does** import it and is disqualified
  -- the same boundary T224 crossed, re-confirmed for the rank-2 object.
- **kappa NOT re-tuned.** `compute_kappa` is imported from T224 and used verbatim;
  re-specifying it per domain would be a FAIL, and the single-formula flag is asserted.

## First exact obstruction / missing object

With both T224 conditions cleared at the gate, the first remaining obstruction to an
unconditional `closed` is **not** internal to this experiment -- it is the **scope of
the rank ladder demonstrated**. The cross-domain rank classification is now witnessed
at ranks {0, 1, 2}. It is **not** yet witnessed that the transport law holds for
**arbitrary** k (a kappa = 3 A-instance predicting a three-box B', etc.), nor that B'
must be CHSH-shaped: both absorbers cleared so far are signed-graph / parity covers,
so the "second absorber" is unrelated-by-derivation but **same-genre-by-structure**
(both are frustrated-cycle covers). The honest open edge is a third absorber whose
neighbor-visible cover is a parity cover but whose **native** obstruction is **not** a
signed-graph frustration computation (e.g. an Arrow/SMD aggregation or a CAP/commit
obstruction read natively, with kappa transported in), to show the rank law is not
confined to the CHSH structural genre.

## Constructive next object (named, not built here)

A **rank-k, genre-crossing third absorber**: take an absorber from the T224 hole bank
whose native obstruction is computed by a NON-signed-graph mechanism (Arrow/SMD
aggregation impossibility, or T28 CAP read through its OWN commit-obstruction witness
rather than the shared engine), present its neighbor-visible same/different cover,
transport kappa = k from a k-cell A-instance, and predict the integer number of its
native independent obstructions before measuring. Passing at k >= 2 across a
structurally different native witness would close the residual "same-genre" edge and
make the cross-domain rank-classification statement maximally hostile-domain hardened.

## Meaning for the relevant claim

- The **breakout bet** (heterodox/orthodox 62-persona pass) is **not killed and is
  now past its promotion gate at the entry level**: the cross-domain recurrence is
  not a projected template at rank 2, because a structure-preserving map across
  genuinely independent code predicted the **exact integer** count of independent
  obstructions, separating rank 1 from rank 2.
- It **upgrades T224's earned claim** from "cross-domain obstruction-presence
  classifier" to "cross-domain obstruction-**rank** classifier" and supplies the
  SECOND unrelated absorber T224 explicitly lacked. The honest claim now available
  (pending integrator ratification) is the cross-domain **rank**-classification
  statement *kappa transported from A predicts the exact integer number of
  independent native obstructions in an unrelated absorber* -- a statement living in
  **no single absorber**, which is exactly the **independent motivation** the
  2026-06-24 MATHEMATICAL-INDEPENDENCE-AUDIT found NOT EARNED (criterion 6).
- It **promotes no physics/geometry/curvature/new-object language.** kappa is a Z/2
  graph-homology rank over a finite cover; "two boxes" is two disjoint odd cycles in
  a finite signed graph; CHSH is used as a structural contextuality cover (parity
  equations), as in T21, not a quantum amplitude simulation. The only claim is a
  finite cross-domain rank-classification statement, tagged finite_witness.

## Next proof / computation step

Build the genre-crossing rank-k third absorber named above (Arrow/SMD or
native-witness CAP), transport kappa = k before measuring, and verify the integer
rank prediction against a native witness that is NOT a signed-graph frustration
computation. If it holds, the "same-genre" residual edge closes and the cross-domain
rank-classification theorem is hostile-domain complete. If it misses, the transport
law is bounded to the frustrated-cycle genre -- still a real, citable cross-domain
result, with its exact boundary named.

## Complexity / language tags

- `finite_witness`: all instances are finite executable fixtures (T39 two-cell cover;
  two-box CHSH, 8 settings / 8 contexts); no scalable/continuum theorem is asserted
  from them. The rank ladder demonstrated is {0, 1, 2}, stated as such.
- `poly_decider`: kappa is union-find spanning forest + BFS Z/2 potential; the native
  rank is a per-box parity product. Both are finite classifiers, not hidden searches
  and not NP-hardness claims.
- No general Cech/sheaf-cohomology theorem is promoted; "dim H^1" is the finite Z/2
  cycle-space rank of a specific finite cover, named as such.

## Known Physics Constraints

None. T229 is a finite typed-machinery audit. The Bell/CHSH side is used only as a
structural contextuality cover (parity equations per box), as in T21 -- not a quantum
amplitude simulation, not a Bell-probability derivation. No time, observer-metaphysics,
curvature, holonomy, or new-object language is used; "two boxes" and "independent
cells" are graph-theoretic (vertex-disjoint odd cycles).

## Reproduction

```bash
python -m pytest tests/test_kappa_rank2_transport.py -v
python -m models.kappa_rank2_transport          # prints the full protocol JSON
# raw output: results/kappa-rank2/T229-results.json
# regression (T224 untouched): python -m pytest tests/test_typed_loss_transport.py tests/test_kappa_rank2_transport.py -q
```
