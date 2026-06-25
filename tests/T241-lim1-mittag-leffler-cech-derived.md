# T241: lim^1 / Mittag-Leffler Vanishing Certificate + Retirement of the Thin-Cover (d1=0) Restriction

**Verdict (top): conditional (finite_witness + poly_decider).**

**Builds on:** [T236](T236-sheaf-h1-cofinality-derived-bridge.md) (full-poset
cofinality + multi-cycle + the honest Cech->derived step, `models/sheaf_h1_cofinality.py`),
[T231](T231-sheaf-h1-refinement-stability.md) (uniform-bisection refinement,
`models/sheaf_h1_refinement.py`), [T226](T226-coefficient-aware-sheaf-h1-continuum.md)
(finite coefficient-aware Z2 Cech-H1, `models/coefficient_sheaf_h1.py`). **Code:**
`models/sheaf_h1_lim1_certificate.py` · `tests/test_sheaf_h1_lim1_certificate.py`
(19 new; **73 passed** with the T236+T231+T226 suites) ·
`results/sheaf-h1-lim1/T241-results.json`. **Imports T236/T231/T226 BY IMPORT ONLY;
modifies none.**

**Tag:** `finite_witness` + `poly_decider`. The H^0 dimension / connectivity decider
is a `poly_decider` (union-find component count, linear). The triple-overlap class
is read by T226's exhaustive `transition_is_coboundary` (the FULL coboundary
computation, a `finite_witness` cross-check on small covers). This is the
**coefficient-sheaf continuum lane** and is **EXPLICITLY DISTINCT from and does NOT
touch** the D1FilteredMorphism category-colimit lane (T237/T242): different object,
different indexing system.

---

## Verdict

**conditional.** T236 pinned the CSP-PO1 continuum row to a SINGLE residual gap (the
Cech->derived comparison is an iso only after a `lim^1` / Mittag-Leffler vanishing
over the directed tower) and honestly left `derived_comparison_is_iso = None`. T241
does two things:

1. **The `lim^1` / Mittag-Leffler gap is CLEARED at the tower level (a real positive
   result).** The orientation-sheaf H^0 inverse system over the cofinal
   uniform-bisection chain has H^0 = Z2 (connected) at every stage and every
   restriction connecting map equal to the identity iso, so the system is
   **constant**, Mittag-Leffler holds with stable images, and **`lim^1` vanishes**.
   Cofinality (imported from T236, already discharged) reduces the full-poset
   `lim^1` to this chain's `lim^1`. This is an **exact finite-input ML theorem**
   ("all connecting maps iso => constant system => stable images => ML => `lim^1`=0"),
   NOT a continuum inference. It **licenses the tower-level Cech iso** — the flag
   T236 left `None` is now set **`True`** WITH the ML certificate as its license.

2. **The thin-cover (d1=0) restriction is RETIRED.** A triangulated-annulus cover
   with **genuine triple overlaps** carries the orientation reversal as a valid
   **non-coboundary 1-cocycle**; the **full** coboundary computation reports the
   correct Z2 class refinement-stably on a cover where the triple-overlap cocycle
   condition is **load-bearing**, not vacuous.

The verdict is **conditional**, not **closed**, because a strictly-LARGER claim is
NOT licensed and is now precisely named: identifying the cover-colimit with the
**derived sheaf cohomology of a continuum band** needs, BEYOND `lim^1`=0, a
**good-cover / hypercover cofinality** (the annular tower cofinal in ALL open covers)
that a countable tower does not establish. That is the one newly-named binding
hypothesis; `continuum_derived_iso` stays `None`. A general continuum
sheaf-cohomology theorem is **FORBIDDEN** from this finite witness (binding honesty
guard).

## What was derived from the sources (IMPORT ONLY)

- **From T236 (the named residual gap, verbatim):** "the Cech->derived comparison
  map ... is an iso only after a `lim^1` / Mittag-Leffler vanishing over the directed
  system of covers ... a property of the full infinite tower, not certifiable from
  any finite stage," and the secondary note that all witnesses are **thin covers (no
  triple overlaps), so the cocycle condition is vacuous**. T241 attacks both.
- **Imported by name (no modification):** `cofinality_certificate`,
  `general_class_obstructed`, `general_class_vector`, `general_h1_rank`,
  `num_components` (T236, `sheaf_h1_cofinality.py`); `subdivide_annular`,
  `annular_class_obstructed` (T231, `sheaf_h1_refinement.py`); `CoverNerve`,
  `annular_cover`, `is_cocycle`, `monodromy_sign`, `transition_is_coboundary`,
  `z2_add` (T226, `coefficient_sheaf_h1.py`). Cofinality is **reused** as the bridge
  that reduces the full-poset `lim^1` to the cofinal chain's `lim^1`; the FULL
  coboundary search `transition_is_coboundary` is **reused** as the triple-overlap
  class decider (not the cycle-space shortcut).

## The objects

- **H^0 inverse system + ML certificate** (`h0_dimension`, `_restriction_is_iso`,
  `mittag_leffler_certificate`). H^0 of the constant Z2 orientation sheaf on a cover
  nerve = locally-constant Z2 functions = `Z2^(#components)`. The refinement tower's
  connecting maps are restriction-along-refinement. For the connected band every
  stage is connected (H^0 = Z2) and every restriction is the identity iso, computed
  from component counts (a **real check**: a disconnected fine cover would NOT be an
  iso — verified in `test_ml_certificate_is_a_real_iso_check_not_an_assertion`). All
  maps iso => constant system => images stable => Mittag-Leffler => `lim^1`=0.
- **Triple-overlap witness** (`triangulated_annulus`, `triple_overlap_verdict`,
  `triple_overlap_refinement_stable`). A cyclic spine of `n` patches plus a bridge
  patch over each spine edge gives `n` **genuine** triples `(i, i+1, b_i)` (d1 != 0
  exercised). The Mobius reversal is placed on the spine wrap edge AND one bridge
  edge of the wrap triple, so **every triple's cocycle sum is 0** (valid cocycle —
  the d1=0 condition is non-vacuously satisfied) while the global wrap parity is odd
  (`[g]`!=0). Read by the **full** `transition_is_coboundary`.
- **Upgraded comparison** (`lim1_comparison`). Splits T236's single `None` flag into
  `tower_cech_iso` (now `True`, licensed by ML) and `continuum_derived_iso` (still
  `None`, missing object = good-cover cofinality).

## Strongest positive result

`results/sheaf-h1-lim1/T241-results.json` (verbatim):

| Object | Result |
|---|---|
| H^0 dim at every chain stage (annular_4..64) | **1 (connected, = Z2)** |
| every connecting (restriction) map iso | **True** |
| H^0 inverse system constant | **True** |
| images eventually stable (Mittag-Leffler) | **True** |
| `lim^1` vanishes | **True** |
| cofinal chain controls full tower (T236) | **True** |
| triple-overlap cover genuine triples | **4 / 6 / 8 (d1 non-vacuous)** |
| triple-overlap valid cocycle (every triple sums 0) | **True** |
| triple-overlap cylinder full-coboundary section | **True (`[g]`=0)** |
| triple-overlap Mobius full-coboundary section | **False (`[g]`!=0)** |
| triple-overlap class refinement-stable (n=4,6,8) | **True** |
| **tower-level Cech iso (was `None` in T236)** | **True (licensed by ML)** |
| **continuum derived-sheaf iso** | **`None` (honestly open, missing object named)** |

A **stronger honesty point** recorded in the witness: on the triple-overlap Mobius
the naive multiplicative loop-sign shortcut is **fooled** (the twist is split over
two edges, so `monodromy_sign = +1`), yet the **full coboundary cohomology** still
detects the nontrivial class (`transition_is_coboundary = False`). The class is read
by genuine cohomology, not the loop-sign heuristic — asserted in
`test_triple_overlap_loop_sign_shortcut_is_fooled_full_cohomology_is_not`.

## Honesty guards (what would FALSIFY; none triggered)

- **Object-identity / no re-tuning:** the triple-overlap class is decided by T226's
  `transition_is_coboundary` (the FULL exhaustive d0-image search) imported
  unmodified, NOT a per-cover-retuned decider. The H^0 iso is computed from
  union-find component counts, not asserted; a disconnected fine cover returns
  `is_iso=False` (`test_ml_certificate_is_a_real_iso_check_not_an_assertion`).
- **`is_iso` not set True from finite data illegitimately:** the binding T236 guard.
  `tower_cech_iso=True` is licensed **only** by the exact finite-input ML theorem
  (all verified-iso connecting maps => `lim^1`=0) reduced to the full poset by
  T236-discharged cofinality — NOT by extrapolating a continuum fact. The
  strictly-larger `continuum_derived_iso` stays `None`
  (`test_continuum_derived_iso_stays_none_with_named_missing_object`), and the True
  is gated on the ML cert, not hard-coded
  (`test_ml_failure_would_leave_tower_iso_none`).
- **Cocycle condition non-vacuous:** an UN-balanced single spine reversal **fails**
  `is_cocycle` (`test_triple_overlap_cocycle_condition_is_nonvacuous_and_valid`), so
  d1=0 is a genuine load-bearing constraint, not a vacuous pass.
- **Sibling suites green:** the 54-test T226+T231+T236 suite is untouched and passes
  alongside the 19 new tests (**73 passed**;
  `test_imports_leave_sibling_suites_untouched`).
- **No continuum theorem / no `closed`:** `test_verdict_is_conditional_not_closed`,
  `test_no_continuum_theorem_asserted`. No physics / curvature / connection /
  holonomy / new-object language: "monodromy" = loop sign-product only; "H^1"/"H^0" =
  finite Z2 cochain-complex (co)homology of a SPECIFIC finite cover.

## First exact obstruction / missing object

T236's `lim^1` obstruction is **cleared** at the tower level. The **single remaining
tower-level object** keeping the verdict at `conditional`: the **good-cover /
hypercover cofinality** — the annular refinement tower being cofinal in ALL open
covers of the band, which is what additionally licenses identifying the cover-colimit
Cech-H^1 with the **derived functor** sheaf cohomology of a continuum band. The
`lim^1` term is now certified zero; the good-cover cofinality is a strictly separate,
strictly-larger condition that a countable annular tower does not establish, and a
finite witness structurally cannot supply.

## Constructive next object

A **good-cover / hypercover cofinality certificate** for the band: exhibit (or cite)
that the annular refinement tower is cofinal in the open covers of the band in the
sense that makes Cech compute the derived functor (e.g. every cover is refined by an
annular cover all of whose finite intersections are contractible / acyclic). Named,
not built. This is the one ingredient that, on top of the now-certified `lim^1`=0,
would move `continuum_derived_iso` off `None`. (Distinct object from the
D1FilteredMorphism category-colimit lane.)

## Meaning for the relevant claim (CSP-PO1, T222/T231/T236 continuum row)

T236 narrowed the CSP-PO1 continuum row's conditionality to ONE named gap (the
`lim^1` / Mittag-Leffler vanishing) and ONE secondary honesty note (thin covers,
vacuous cocycle). T241 **clears the `lim^1` gap at the tower level** and **retires
the thin-cover restriction** with a genuine-triple witness. The residual is now a
**single, strictly-larger, newly-named** binding hypothesis: good-cover cofinality
for the continuum derived identification. The CSP-PO1 continuum row **remains
`conditional`** — **no continuum theorem is claimed**, no promotion to a continuum
`proto_independent` is warranted from this finite witness — but its conditionality is
now pinned to that one good-cover cofinality object, with both prior gaps discharged.
**Report at test level; promotion deferred to the integrator.**

## Known Physics Constraints

None. Pure finite Z2 linear algebra: union-find component counts (H^0 dim), exhaustive
`2^n` d0-image coboundary search (the triple-overlap class), and an exact
finite-input Mittag-Leffler argument (all connecting maps iso => `lim^1`=0). No
hardness/scale claim (the H^0 decider is a `poly_decider`, explicitly NOT a hidden
search per COMPLEXITY-LEDGER discipline; the exhaustive `2^n` route is retained only
as the small-cover class decider). No physics / geometry / curvature / connection /
holonomy / new-object language is promoted.

## Success / failure criteria

**Success (all met):** (1) every stage of the cofinal chain is connected (H^0 = Z2)
and every restriction connecting map is the identity iso, so the H^0 inverse system
is constant, Mittag-Leffler holds, `lim^1` vanishes, and cofinality reduces the
full-poset `lim^1` to the chain's; (2) the triangulated-annulus cover has genuine
triples (d1 non-vacuous), passes the cocycle check non-vacuously (an un-balanced
twist fails it), and the full coboundary computation reports cylinder=section /
Mobius=obstructed refinement-stably across n=4,6,8; (3) the tower-level Cech iso is
licensed `True` by the ML certificate while the continuum derived iso stays `None`
with its missing object named; (4) the sibling 54-test suite stays green.

**Failure (none triggered; guards binding):** stating a general continuum Cech/sheaf
theorem from this finite witness -> **forbidden**; asserting `continuum_derived_iso`
True -> **forbidden** (good-cover cofinality not certifiable from finite data);
setting `tower_cech_iso` True WITHOUT the ML certificate -> **gated against**
(`test_ml_failure_would_leave_tower_iso_none`); a vacuous cocycle pass ->
**guarded** (un-balanced twist fails `is_cocycle`); conflation with the
D1FilteredMorphism lane -> **explicitly disclaimed**; a `closed` verdict ->
**guarded** (`test_verdict_is_conditional_not_closed`).

## Next proof / computation step

Build (or cite) the **good-cover / hypercover cofinality certificate** for the band
— the one remaining ingredient that, on top of the now-certified `lim^1`=0, would
license the continuum derived-sheaf identification. This is the single remaining
tower-level step to move CSP-PO1's continuum row from `conditional` toward a stated
continuum certificate, still short of, and not to be confused with, a general
continuum cohomology theorem.

## Reproduction

```
cd "<repo root: .../time-as-finality>"
python -m pytest tests/test_sheaf_h1_lim1_certificate.py -q                                   # 19 passed
python -m pytest tests/test_sheaf_h1_lim1_certificate.py tests/test_sheaf_h1_cofinality.py tests/test_sheaf_h1_refinement.py tests/test_coefficient_sheaf_h1.py -q   # 73 passed
python -c "from models.sheaf_h1_lim1_certificate import run_t241_analysis, t241_result_to_dict; import json; print(json.dumps(t241_result_to_dict(run_t241_analysis()), indent=2))"
```

Results snapshot: `results/sheaf-h1-lim1/T241-results.json`.
