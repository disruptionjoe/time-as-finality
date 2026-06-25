# T246: Good-Cover Acyclicity Certificate for the Annular-Tower Witness

**Verdict (top): conditional (finite_witness + poly_decider).**

**Builds on:** [T241](T241-lim1-mittag-leffler-cech-derived.md) (lim^1 / Mittag-Leffler
vanishing certificate + genuine-triple triangulated-annulus witness,
`models/sheaf_h1_lim1_certificate.py`), [T236](T236-sheaf-h1-cofinality-derived-bridge.md)
(full-poset cofinality + general Z2 cycle-space (co)homology,
`models/sheaf_h1_cofinality.py`), [T231](T231-sheaf-h1-refinement-stability.md)
(refinement, `models/sheaf_h1_refinement.py`), [T226](T226-coefficient-aware-sheaf-h1-continuum.md)
(finite coefficient-aware Z2 Cech-H1, `models/coefficient_sheaf_h1.py`). **Code:**
`models/sheaf_h1_good_cover_cofinality.py` ·
`tests/test_sheaf_h1_good_cover_cofinality.py` (28 new; **101 passed** with the
T226+T231+T236+T241 suites) · `results/sheaf-h1-good-cover/T246-results.json`.
**Imports T241/T236/T231/T226 BY IMPORT ONLY; modifies none.**

**Tag:** `finite_witness` + `poly_decider`. The acyclicity decider is the finite
Z2 (co)homology rank of each intersection piece: `b0 = num_components` (union-find,
linear) and `b1 = general_h1_rank` = #E - #V + #components (Euler count) — both
imported **by object identity** from T236, so the SAME homology machinery scores
the intersection pieces and the global cover (no per-piece re-tuned decider). NOT a
hidden search, NOT a hardness/scale claim. This is the **coefficient-sheaf continuum
lane** and is **EXPLICITLY DISTINCT from and does NOT touch** the D1FilteredMorphism
category-colimit lane (T237/T242): different object, different indexing system.

---

## Verdict

**conditional.** T241 cleared the lim^1 / Mittag-Leffler correction at the tower
level (`tower_cech_iso = True`) and named ONE strictly-larger object keeping the
CSP-PO1 continuum row's `continuum_derived_iso` at `None`: the **good-cover /
hypercover cofinality** — every cover refined by an annular cover all of whose finite
intersections are contractible/acyclic. T246 **BUILDS the acyclicity ingredient** on
a finite witness; it does **not** build the all-open-covers cofinality theorem:

1. **The good-cover acyclicity certificate is BUILT (a real positive result).**
   The triangulated-annulus cover (T241, with GENUINE triple overlaps) has **every
   nonempty finite intersection contractible/acyclic** — single patches (arcs),
   pairwise overlaps (arc-overlaps), and the n genuine triples (the
   bridge-meets-two-spine-arcs cell) — read as finite Z2 (co)homology `b0 = 1 &
   b1 = 0`. This is refinement-stable across n = 4, 6, 8 with genuine, growing triple
   counts. Good-cover (Leray) + the already-certified lim^1 = 0 (T241) is **exactly
   the pair** that makes Cech compute the derived functor, so
   **`continuum_derived_iso` is now set `True` FOR THE COUNTABLE ANNULAR-TOWER
   SUBSYSTEM** (good-cover acyclicity established there; all-open-covers cofinality
   not established) — the flag T241 left `None` moves off `None` for that declared
   subsystem, WITH the Leray pair as its license.

2. **The acyclicity check is REAL, not asserted.** A NON-good honesty injector — a
   triple "intersection" realized as a 3-cycle (an annulus, `b1 = 1`, a hole;
   non-contractible) and a disconnected piece (`b0 = 2`) — is correctly **reported
   non-acyclic**, so `is_good_cover` is gated on a genuine acyclicity computation,
   not a hard-coded constant.

The verdict is **conditional**, not **closed**, because a strictly-LARGER claim is
NOT licensed and is now precisely named: identifying the cover-colimit Cech-H^1 with
the derived-functor sheaf cohomology of the **full continuum band over ALL open
covers** needs the annular tower to be **cofinal in ALL open covers** (every open
cover refined by an annular/good one) — which a **countable** annular tower does NOT
establish (an arbitrary, e.g. genuinely 2-dimensional or irregular, open cover need
not be refined by an annular one). So `continuum_derived_iso_all_open_covers` stays
`None` with that residual NAMED. A general continuum sheaf-cohomology theorem is
**FORBIDDEN** from this finite witness (binding honesty guard).

## What was derived from the sources (IMPORT ONLY)

- **From T241 (the named residual gap, verbatim):** "the GOOD-COVER / hypercover
  cofinality — the annular refinement tower being cofinal in ALL open covers of the
  band ... every cover is refined by an annular cover all of whose finite
  intersections are contractible / acyclic." T246 builds the acyclicity ingredient on
  the witness and pins the residual to the all-open-covers cofinality.
- **Imported by name (no modification):** `mittag_leffler_certificate`,
  `triangulated_annulus` (T241, `sheaf_h1_lim1_certificate.py`); `num_components`,
  `general_h1_rank` (T236, `sheaf_h1_cofinality.py`); `CoverNerve`, `annular_cover`,
  `is_cocycle` (T226, `coefficient_sheaf_h1.py`). The lim^1 = 0 leg of the Leray pair
  is the T241 ML certificate **by object identity** (asserted in
  `test_lim1_leg_is_imported_t241_ml_certificate_not_reasserted`); the triangulated
  cover whose intersections are scored is T241's `triangulated_annulus` **by object
  identity** (`test_triangulated_annulus_is_imported_t241_object`); the homology
  scorer is the T236 functions **by object identity**
  (`test_homology_decider_is_imported_t236_object_not_retuned`).

## The objects

- **Acyclicity atom** (`acyclicity_verdict`, `_piece_homology`). A nonempty finite
  intersection piece is acyclic (contractible, as the finite witness sees it) iff its
  finite Z2 (co)homology is point-like: `b0 = 1` (connected) AND `b1 = 0` (no cycle).
  Both read off the imported T236 ranks.
- **Good-cover certificate** (`good_cover_certificate`). Reads the intersection
  structure off T241's `triangulated_annulus(n, wrap_twist=False)` (the twist lives
  in H^1 and does not change WHICH intersections are nonempty), realizes each
  nonempty single/pairwise/triple piece combinatorially (arc / arc-overlap / triple =
  a contractible TREE cell), and certifies all acyclic. n genuine triples for n spine
  patches.
- **Non-good injector** (`non_good_injector`, `_triple_piece_bad_annular`,
  `_disconnected_piece_bad`). The annular (3-cycle, `b1 = 1`) and disconnected
  (`b0 = 2`) bad pieces; the certificate must report both non-acyclic.
- **Leray pair** (`leray_pair_verdict`). good-cover (this module) + lim^1 = 0 (T241)
  => `continuum_derived_iso_annular_tower = True`, gated on BOTH legs; the
  all-open-covers iso stays `None` with the residual named.

## Strongest positive result

`results/sheaf-h1-good-cover/T246-results.json` (verbatim):

| Object | Result |
|---|---|
| triangulated_annulus_4 is a good cover | **True** |
| every nonempty single intersection acyclic (b0=1, b1=0) | **True** |
| every nonempty pairwise intersection acyclic | **True** |
| every genuine triple intersection acyclic (tree cell) | **True (4 triples)** |
| good cover refinement-stable (n = 4, 6, 8) | **True (triples 4/6/8, growing)** |
| NON-good annular triple piece reported acyclic | **False (b1 = 1, correctly rejected)** |
| NON-good disconnected piece reported acyclic | **False (b0 = 2, correctly rejected)** |
| injector correctly rejects both bad pieces | **True** |
| lim^1 = 0 certified (imported T241 ML certificate) | **True** |
| Leray pair complete on annular tower (good-cover + lim^1=0) | **True** |
| **continuum_derived_iso (annular-tower subsystem)** | **True (licensed by the Leray pair)** |
| **continuum_derived_iso (all open covers)** | **`None` (honestly open, residual named)** |

The load-bearing honesty point: the good (tree) realization of a genuine triple is
acyclic (`b1 = 0`) while the cyclic (3-cycle) realization is NOT (`b1 = 1`) — the
certificate distinguishes a contractible common-region triple from an annular
around-a-hole triple by a genuine `b1` computation
(`test_good_cover_certificate_would_fail_on_a_cyclic_triple`).

## Honesty guards (what would FALSIFY; none triggered)

- **The good-cover check is REAL, not asserted:** a 3-cycle (annulus, `b1 = 1`) and a
  disconnected piece (`b0 = 2`) are correctly reported NON-acyclic
  (`test_non_good_annular_triple_is_rejected`,
  `test_non_good_disconnected_piece_is_rejected`,
  `test_injector_correctly_rejects_both_bad_pieces`).
- **Object-identity / no re-tuning:** the homology scorer IS the imported T236
  `num_components` / `general_h1_rank` (`test_homology_decider_is_imported_t236_object_not_retuned`,
  `test_piece_homology_matches_imported_t236_ranks`); the scored cover IS T241's
  `triangulated_annulus` (`test_triangulated_annulus_is_imported_t241_object`); the
  lim^1 leg IS T241's `mittag_leffler_certificate`
  (`test_lim1_leg_is_imported_t241_ml_certificate_not_reasserted`).
- **`continuum_derived_iso` not set True illegitimately:** the annular-tower iso is
  `True` ONLY when BOTH legs of the Leray pair are genuinely certified. Forcing the
  good-cover leg to fail drops it to `None`
  (`test_continuum_iso_would_be_none_if_good_cover_failed`); forcing the lim^1 leg to
  fail drops it to `None` (`test_continuum_iso_would_be_none_if_lim1_failed`). The
  strictly-larger all-open-covers iso stays `None`
  (`test_continuum_derived_iso_set_true_only_for_annular_tower`).
- **No continuum theorem / no `closed`:** `test_verdict_is_conditional_not_closed`,
  `test_no_continuum_theorem_asserted`. No physics / curvature / connection /
  holonomy / new-object language (`test_no_physics_or_new_object_language_in_summary`):
  "contractible/acyclic" = `b0 = 1 & b1 = 0` of a SPECIFIC finite combinatorial
  piece; "H^1"/"H^0" = finite Z2 cochain-complex (co)homology of a SPECIFIC finite
  cover.
- **Sibling suites green:** the 73-test T226+T231+T236+T241 suite is untouched and
  passes alongside the 28 new tests (**101 passed**;
  `test_imports_leave_sibling_suites_untouched`).

## First exact obstruction / missing object

T241's good-cover acyclicity object is **BUILT** on the witness; the good-cover +
lim^1 = 0 Leray pair licenses `continuum_derived_iso` **for the countable
annular-tower subsystem**. The **single remaining object** keeping the verdict at
`conditional`: the **all-open-covers cofinality** — that the annular refinement tower
is cofinal in ALL open covers of the band (every open cover refined by an annular/good
one). A countable annular tower does NOT establish this (an arbitrary, e.g. genuinely
2-dimensional or irregular, open cover need not be refined by any annular cover); a
finite witness structurally cannot supply it. The good-cover acyclicity ingredient
itself is now certified; what remains is the all-open-covers cofinality of the tower.

## Constructive next object

An **all-open-covers cofinality** argument (or citation) for the annular good-cover
tower of the band: show every open cover of the band is refined by some annular (good)
cover in the tower — e.g. a Lebesgue-number / paracompactness argument that an
arbitrary open cover of the (1-dimensional, contractible-arc-coverable) band admits a
common annular refinement. This is the one ingredient that, on top of the now-built
good-cover acyclicity and the certified lim^1 = 0, would move
`continuum_derived_iso_all_open_covers` off `None`. Named, not built (a finite witness
cannot supply an all-open-covers statement). Distinct object from the
D1FilteredMorphism category-colimit lane.

## Meaning for the relevant claim (CSP-PO1, T222/T231/T236/T241 continuum row)

T241 cleared the lim^1 gap and named good-cover cofinality as the single residual.
T246 **builds the good-cover acyclicity ingredient** on the triangulated-annulus
tower (refinement-stably, with a real acyclicity check proven by the non-good
injector) and, paired with the certified lim^1 = 0, licenses `continuum_derived_iso`
**for the countable annular-tower subsystem**. The residual is now a **single,
strictly-larger, sharply-pinned** binding hypothesis: all-open-covers cofinality of
the tower. The CSP-PO1 continuum row **remains `conditional`** — **no general
continuum sheaf-cohomology theorem is claimed**, no promotion to a continuum
`proto_independent` is warranted from this finite witness — but its conditionality is
now pinned to that one all-open-covers cofinality object, with the good-cover
acyclicity ingredient discharged on the annular tower. **Report at test level;
promotion deferred to the integrator.**

## Known Physics Constraints

None. Pure finite Z2 linear algebra: union-find component counts (`b0` / H^0),
Euler-characteristic cycle-rank counts (`b1` / H^1) of intersection pieces, and the
exact finite-input Leray + ML pairing. No hardness/scale claim (the acyclicity
decider is a `poly_decider`, explicitly NOT a hidden search per COMPLEXITY-LEDGER
discipline). No physics / geometry / curvature / connection / holonomy / new-object
language is promoted; "contractible/acyclic" is a finite combinatorial (co)homology
statement only.

## Success / failure criteria

**Success (all met):** (1) the triangulated-annulus cover is a good cover — every
nonempty single/pairwise/triple intersection acyclic (`b0 = 1, b1 = 0`), with genuine
non-vacuous triples, refinement-stably across n = 4, 6, 8 with growing triple counts;
(2) the non-good injector (annular `b1 = 1` triple, disconnected `b0 = 2` piece) is
correctly reported non-acyclic, so the check is real; (3) good-cover + lim^1 = 0
licenses `continuum_derived_iso` for the annular-tower subsystem (gated on BOTH legs)
while the all-open-covers iso stays `None` with its residual named; (4) the sibling
73-test suite stays green (101 passed total).

**Failure (none triggered; guards binding):** stating a general continuum Cech/sheaf
theorem from this finite witness -> **forbidden**; asserting
`continuum_derived_iso_all_open_covers` True -> **forbidden** (all-open-covers
cofinality not certifiable from finite data); setting the annular-tower iso True
WITHOUT both Leray legs -> **gated against**
(`test_continuum_iso_would_be_none_if_good_cover_failed`,
`test_continuum_iso_would_be_none_if_lim1_failed`); a rubber-stamp acyclicity check
-> **guarded** (the annular/disconnected injector must be rejected); conflation with
the D1FilteredMorphism lane -> **explicitly disclaimed**; a `closed` verdict ->
**guarded** (`test_verdict_is_conditional_not_closed`).

## Next proof / computation step

Build (or cite) the **all-open-covers cofinality** of the annular good-cover tower —
the one remaining ingredient that, on top of the now-built good-cover acyclicity and
the certified lim^1 = 0, would move the continuum derived-sheaf identification off
`None` over ALL open covers. This is the single remaining tower-level step for
CSP-PO1's continuum row, still short of, and not to be confused with, a general
continuum cohomology theorem.

## Reproduction

```
cd "<repo root: .../time-as-finality>"
python -m pytest tests/test_sheaf_h1_good_cover_cofinality.py -q                              # 28 passed
python -m pytest tests/test_sheaf_h1_good_cover_cofinality.py tests/test_sheaf_h1_lim1_certificate.py tests/test_sheaf_h1_cofinality.py tests/test_sheaf_h1_refinement.py tests/test_coefficient_sheaf_h1.py -q   # 101 passed
python -c "from models.sheaf_h1_good_cover_cofinality import run_t246_analysis, t246_result_to_dict; import json; print(json.dumps(t246_result_to_dict(run_t246_analysis()), indent=2))"
```

Results snapshot: `results/sheaf-h1-good-cover/T246-results.json`.
