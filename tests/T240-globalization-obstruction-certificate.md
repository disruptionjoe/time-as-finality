# T240: Globalization-obstruction certificate (LossKernel route (b), criterion-6 crux)

## Verdict: no-go (route (b) NOT cleared; route (a) bounded subsumption COMPLETED over all three crack types — value, structure, globalization)

The LAST untested route-(b) crack named in T235's `Constructive next object` /
`Next proof / computation step` — a **globalization-obstruction certificate**
(locally-defined `nu`-fixing source automorphisms over a cover, with the finite
`Z/2` Cech-H1 obstruction to patching them into a global automorphism) — is now
built, run through the full T230/T235 gate harness, and **closed at gate 2**. But
it closes in the *sharpest possible* way, and the manner of closure is itself the
load-bearing finding: the obstruction **separates** a same-`nu` pair, is **local**
and **relabel-stable**, and **SURVIVES both prior absorbers** (T235's `nu_struct`
= source field + gluing, AND the per-piece `nu_piece` = the cover plus every
per-vertex local-group iso-class). It is absorbed ONLY by `nu_cocycle`: admitting
the per-overlap **transition cocycle** — the cross-frame gluing *relation* — as
audit data reconstructs the obstruction. By the T108/T127/T235 discipline (a
mature neighbor absorbs any declared source *relation* once named, and the gluing
is exactly such a relation), the transition cocycle is admissible source
structure, so gate 2 fires and `clears_route_b = False`.

This is the first route-(b) crack that survived **two** successive absorbers and
fell only to a **third**, strictly more permissive one. The whole question
collapses to one crisp claim — *is the transition cocycle admissible source
structure?* — and under the program's own absorber discipline the answer is yes.

`finite_witness` + `poly_decider` (COMPLEXITY-LEDGER): a finite executable
fixture over hand-built typed-lossy cases; local automorphism groups by exhaustive
finite permutation enumeration; the obstruction by exhaustive finite GF(2)
Gaussian elimination (an explicit linear decider, NOT a search, NOT a hardness
claim). No physics / geometry / curvature / connection / holonomy / gravity /
spacetime / new-object language. "`Z/2` H1 / obstruction rank" = the finite `Z/2`
cycle-space rank (`dim Z^1 − dim B^1`) of a SPECIFIC finite cover's transition
system, named as such — NOT a continuum or general sheaf-cohomology theorem.
Within-domain separation question only; touches nothing in the
kappa / sheaf-H1 / D1Cat / MTI lanes.

## What was derived from sources (IMPORT ONLY)

- From **models/attribution_invariant_separation.py** (T230, re-used by import,
  unmodified): the realization map `nu`, the admissible enlargement `nu_prime`,
  the `relabel` action and `is_relabel_stable` gate, the `_separating_same_nu_pair`
  finder, and the `_freeze` canonicalizer. The T230 suite stays green (14/14).
- From **models/source_automorphism_rigidity.py** (T235, re-used by import,
  unmodified): `_source_endpoints`, the source-gluing registry (`gluing_of`,
  `set_gluing`, `clear_gluings`), and the `nu_struct` enlargement (admit every
  source field AND the source gluing). The T235 suite stays green (15/15).
- From **tests/T235-source-automorphism-rigidity-certificate.md** (the
  constructive next object, verbatim): "take **locally-defined** `nu`-fixing
  source automorphisms over a cover of the source and ask whether they **patch to
  a global one**. The obstruction to globalization (a finite `Z/2` or torsor
  obstruction class) is the candidate symmetry datum ... Build that obstruction
  invariant and test whether it is `nu_struct`-measurable on a same-`nu` fiber."
  T240 is exactly this, with the gate-2 test sharpened to also admit the
  transition cocycle (`nu_cocycle`), the relational carrier T235 anticipated.
- **NO import of `models/d1_restriction_system`** and **no use of
  `cap_theorem_bridge.py`** (the disqualified shared-derivation transport path).
  Enforced by an AST audit in the test suite (`test_shared_derivation_audit_no_d1_engine_import`,
  `test_imports_only_named_siblings`).

## Strongest positive result

The globalization obstruction is the finite `Z/2` Cech-H1 rank of the transition
system over a 3-piece cyclic cover. Carrier `{a,b,c,d,e,f}`, full-symmetric
all-True lift table (the shared `nu`-visible data, closed under every permutation
so local symmetry is governed by the gluing), source gluing into three swappable
pairs `{a,b},{c,d},{e,f}`, cover `U0={a,b,c,d}`, `U1={c,d,e,f}`, `U2={e,f,a,b}`
with overlaps `{c,d},{a,b},{e,f}` (each a glued, swap-admitting pair) and **no
triple overlap** — so every 1-cochain is a cocycle and the nerve's H1 has `Z/2`
rank 1 (`dim Z^1 = 3`, `dim B^1 = 2`).

| member | gluing | cover | transition signs | cocycle | coboundary | obstruction rank |
|---|---|---|---|---|---|---|
| `glob_patch` | `{a,b},{c,d},{e,f}` | shared | `(0,0,0)` | yes | yes | **0** (patches) |
| `glob_obstructed` | `{a,b},{c,d},{e,f}` | shared | `(1,0,0)` | yes | **no** | **1** (no global) |

Both share **identical `nu`, gluing, AND cover**; they differ ONLY in the
transition cocycle. Decisive booleans (executed,
`results/globalization-obstruction/T240-results.json`):

- `separates_same_nu_pair = True` — the obstruction rank (0 vs 1) separates the
  pair. **Gate 1 passes.** `obstruction_nu_measurable = False`.
- `separation_absorbed_by_nu_struct = False` — T235's absorber (field + gluing) is
  identical on the pair and **cannot** reproduce the separation. This is the
  genuinely new fact vs T235: the structure-keyed absorber that closed the prior
  crack does not reach this one.
- `separation_absorbed_by_nu_piece = False` — admitting the cover plus every
  per-vertex local-group iso-class (the bet's favorable per-PIECE reading) also
  does NOT reproduce it. The per-piece local symmetry types are identical; only
  the cross-overlap gluing differs. **The route-(b) bet holds at the per-piece
  level.**
- `separation_absorbed_by_nu_cocycle = True` — **the decisive obstruction.**
  Admitting the per-overlap transition cocycle (every transition sign, keyed to
  its overlap carrier) as audit data reconstructs the H1 rank, which is a
  deterministic finite GF(2) function of the cocycle. **Gate 2 fires.**
- `relabel_stable = True`, `local = True` — gates 3a/3b pass.
- `clears_route_b = False`,
  `failure_gate = gate2_absorbed_by_admitted_transition_cocycle`.
- `route_b_alive_under_piece_reading_only = True` — the honest middle finding:
  route (b) WOULD be alive if the transition cocycle were inadmissible; it is
  admissible, so it dies.
- `nonvacuity_injected_pair_clears = True` — the injector exhibits a same-`nu`
  pair with IDENTICAL `nu_struct`, `nu_piece` AND `nu_cocycle` that a synthetic
  invariant separates, clearing every gate. The harness CAN report a clear, so the
  no-go is a real negative, not a constant-no harness.

Math correctness is independently checked: triangle-nerve H1 rank = 1; untwisted
cocycle is a coboundary (rank 0); a single loop sign is a non-coboundary (rank 1);
a genuine coboundary twist (two edges at one vertex) gives rank 0 — proving the
obstruction quotients by coboundaries and is not merely "any nonzero sign."

## Honesty guards (all checked; none triggered)

- **AST shared-derivation audit** (`test_shared_derivation_audit_no_d1_engine_import`,
  `test_imports_only_named_siblings`): the model imports ONLY
  `models.attribution_invariant_separation` and `models.source_automorphism_rigidity`
  (plus stdlib). NO `d1_restriction_system`, NO `cap_theorem_bridge`. The
  transport/derivation path does not touch the d1 engine.
- **Object-identity assertion** (`test_object_identity_compute_not_retuned_per_case`):
  `globalization_obstruction` is a single uniform function with no per-case-name
  branch; re-running it on a renamed clone of each member (same source data)
  yields the same rank. `compute`-style logic is not re-tuned per case.
- **No `is_iso`-from-finite-data / no continuum claim**
  (`test_no_continuum_or_general_sheaf_assertion`): the rank is a finite `Z/2`
  cycle-space rank of a specific finite cover; the result object carries no
  `criterion_6_earned` / `independence_earned` field and never self-promotes.
  Verdict stays a test-level no-go.
- **Non-vacuity** (`NonVacuityTests`): the injector clears all gates, certifying
  the no-go is a real negative.
- **Import siblings green**: T230 14/14, T235 15/15 after the import; their own
  `analyze()` still returns `no-go` (`ImportSiblingGreenTests`).
- **Tag discipline**: `finite_witness` + `poly_decider` (the GF(2) decider is an
  explicit finite enumeration, not a search/hardness claim).

## First exact obstruction / missing object

The transition cocycle is **admissible source structure**. It is a source-side
gluing-between-frames *relation* — the same KIND of object as T235's source
gluing, which T235 already proved admissible (T108/T127). The H1 obstruction rank
is a deterministic finite GF(2) function of the cocycle and the nerve, so
admitting the cocycle (`nu_cocycle`) reconstructs every distinction the
certificate makes — absorbed one level up, exactly like T230's field value and
T235's gluing, now keyed to a relational cocycle. The bet "admitting each local
piece does not reconstruct the global obstruction" is **true for per-PIECE
admission** (`nu_piece`) but the absorber discipline does not stop at per-piece:
the cross-overlap *relation* is itself admissible, and it is the minimal datum
carrying H1. The missing object route (b) still needs is a globalization
obstruction whose carrier is provably **NOT** any admissible source relation; the
transition-cocycle construction does not supply one (its carrier is admissible).

## Constructive next object

The value-keyed (T230 field), structure-keyed (T235 gluing), and globalization
(T240 transition cocycle) cracks are now **all** closed at gate 2 by absorption of
a source field/relation. Within the per-domain absorber discipline, **every**
source-side separator on this family has an admissible carrier; LossKernel route
(b) is exhausted on the finite witness. The constructive next object is therefore
NOT another LossKernel sub-object (the OBJECT is always absorbed): it is the
**map-between-absorbers** frontier the 62-persona breakout named — transport a
neighbor-visible obstruction (kappa = `Z/2` H1 rank of a signed cover) BETWEEN two
a-priori-unrelated absorbers via a structure-preserving map with no shared
derivation, where the unit of analysis is the MAP, not the object the absorber
discipline keeps swallowing. The fact that the absorber had to reach for the
cross-frame relation to swallow this crack — after two weaker absorbers failed —
is precisely the structural signal that read.

## Meaning for the relevant claim

- **Independent-motivation (criterion 6): NOT flipped to EARNED via the LossKernel
  route.** T240 closes the last untested route-(b) crack.
- **Route (a) bounded subsumption is now COMPLETE over all three crack types.**
  The citable bounded negative reads: *every local, relabel-stable source-side
  separator on the family — whether keyed to a source field value (T230), a source
  symmetry class / gluing (T235), or a globalization obstruction over a cover
  (T240) — is reproduced by SOME admissible enlargement (`nu'`, `nu_struct`, or
  `nu_cocycle`) and hence factors through admissible neighbor data.* The
  LossKernel / TF1 same-neighbor-data novelty route is cleanly closeable.
- **Reported at the test level only.** `verdict = no-go`,
  `route_a_strengthened = True`, `losskernel_line_closes_fully = True`. Whether
  this ratifies a LossKernel-line / TF1 ledger movement (e.g. demoting the
  same-neighbor-data novelty route to `closed`) is the **integrator's** call.
  Record with maximum care: this is criterion-6's crux, and the honest nuance is
  that the crack survived two absorbers before the third caught it.

## Known Physics Constraints

None. T240 is a finite typed-machinery audit over hand-built typed-lossy cases. No
time, finality, observer, consciousness, quantum-interpretation, curvature,
gravity, connection, holonomy, or new-object language. "Local automorphism" = a
finite permutation of a sub-carrier fixing the restricted lift table and gluing;
"transition cocycle" = a finite `Z/2` 1-cochain on the nerve edges;
"obstruction rank" = the finite `Z/2` cycle-space rank `dim Z^1 − dim B^1` of a
specific finite cover. All groups enumerated exhaustively over finite sets; the
obstruction by finite GF(2) Gaussian elimination. Tagged `finite_witness` +
`poly_decider`: a finite executable fixture + an explicit finite linear decider,
NOT a scalable/continuum theorem, NOT a hardness/NP claim, NOT a hidden search.

## Falsification condition

This no-go is overturned in route (b)'s favor by exhibiting ONE same-`nu` pair
`(a,b)` and the globalization obstruction with `rank(a) != rank(b)`,
relabel-stable AND local, where the separation is reproduced by **NONE** of
`nu_struct`, `nu_piece`, OR `nu_cocycle` — i.e. admitting every source field, the
gluing, the cover, every per-vertex local-group iso-class, AND the full transition
cocycle still leaves the pair indistinguishable to a mature neighbor while the
obstruction separates them. The harness then reports `clears_route_b = True` and
the verdict flips to `EARNED-candidate`. The non-vacuity injector proves the
harness CAN report this; the actual transition-cocycle construction does not,
because its carrier (the cocycle) is admissible.

## Next proof / computation step

Read `clears_route_b`, `separation_absorbed_by_nu_cocycle`, and
`route_b_alive_under_piece_reading_only` in
`results/globalization-obstruction/T240-results.json`. `clears_route_b = False`
via `gate2_absorbed_by_admitted_transition_cocycle`: the LossKernel line closes
fully and criterion-6 work moves OFF the LossKernel object to the
map-between-absorbers (kappa) frontier (open-problems/typed-loss-transport-test.md).
A genuine route-(b) revival would require a globalization obstruction whose carrier
is provably NOT an admissible source relation — not supplied by the
transition-cocycle construction.

## Reproduction

```bash
python -m unittest tests.test_globalization_obstruction_certificate -v   # 30 checks
python -m pytest tests/test_globalization_obstruction_certificate.py -q  # 30 passed
python -m models.globalization_obstruction_certificate                   # prints structured report
```

- Model: `models/globalization_obstruction_certificate.py` (imports
  `models/attribution_invariant_separation.py` and
  `models/source_automorphism_rigidity.py` by import only; both sibling suites
  stay green: 14/14 and 15/15).
- Test: `tests/test_globalization_obstruction_certificate.py` (30 checks, green
  under both unittest and pytest).
- Results: `results/globalization-obstruction/T240-results.json`.
