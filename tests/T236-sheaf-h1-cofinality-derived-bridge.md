# T236: Full-Poset Cofinality + Multi-Cycle Stability + the Cech->Derived Step

**Verdict (top): conditional (finite_witness + poly_decider).**

**Builds on:** [T231](T231-sheaf-h1-refinement-stability.md) (uniform-bisection /
single-cycle refinement-stability half, `models/sheaf_h1_refinement.py`),
[T226](T226-coefficient-aware-sheaf-h1-continuum.md) (the finite coefficient-aware
Z2 Cech-H1, `models/coefficient_sheaf_h1.py`). **Code:**
`models/sheaf_h1_cofinality.py` · `tests/test_sheaf_h1_cofinality.py` (17 new;
54 passed with the T231+T226 suites) ·
`results/sheaf-h1-cofinality/T236-results.json`. **Imports T231/T226 BY IMPORT
ONLY; modifies neither.**

**Tag:** `finite_witness` + `poly_decider`. The general Z2 cycle-space decider is
a poly_decider (spanning-forest + fundamental-cycle parities, linear algebra over
Z2, NOT a hidden search), cross-validated against T226's exhaustive `2^n`
coboundary search on every small witness. This is the **continuum coefficient-sheaf
bridge** and is **EXPLICITLY DISTINCT from and does NOT touch** the
D1FilteredMorphism category-colimit lane (T232/T237): different object, different
indexing system.

---

## Verdict

**conditional.** T231 discharged the continuum row's **uniform-bisection /
single-cycle** half. T236 closes two of T231's three named residual gaps on finite
witnesses and exhibits the honest third step:

1. **Cofinality over the FULL (wider) poset — DISCHARGED (finite).** Non-uniform
   *staggered* refinements (split an arbitrary SUBSET `S` of the `n` patches,
   leave the rest coarse) generate a directed poset strictly wider than T231's
   bisection chain. The Z2 class (`[g]`-verdict + loop sign) is stable along
   **every** refinement edge in that poset, and the uniform-bisection system is
   provably **cofinal** in it: every staggered cover is dominated by the uniform
   bisection, so the colimit value is chain-independent. Enumerated **exhaustively
   over all `2^n` subsets** and cross-validated against the loop-sign and T231
   wrap-parity deciders.
2. **Multi-cycle / non-annular (H1 rank ≥ 2) — DISCHARGED (finite).** The
   one-cycle structure T231 flagged as load-bearing is removed: a **theta-graph
   witness with H1 rank 2** exhibits all **four** independent classes
   (`(0,0),(1,0),(0,1),(1,1)`) via the **full** Z2 cycle-space cohomology, and the
   class is refinement-stable per cycle. T231's wrap-parity is recovered as the
   rank-1 specialization.
3. **Cech→derived comparison — the honest finite step, NOT the continuum
   theorem.** The finite identity (colimit class == cycle-space H1, stable along
   the cofinal system) is executable; the continuum identification stays **OPEN**
   with the obstruction **named** (a `lim^1` / Mittag-Leffler vanishing over the
   full directed tower, not certifiable from any finite stage). The
   `derived_comparison_is_iso` flag is honestly left **`None`** — never `True`.

The verdict is **conditional**, not **closed**, because (3) is exactly the binding
gap a finite witness may not cross. A general continuum sheaf-cohomology theorem is
**FORBIDDEN** from this finite witness (binding honesty guard).

## What was derived from the sources

- **From T231 (First exact obstruction / Constructive next object, verbatim):** the
  named gap — "a cofinality + colimit-stability theorem over the full directed
  poset of covers (not just the bisection chain), plus the Cech→derived comparison
  identifying the stable finite class with continuum H1," together with T231's
  explicit flag that "the poly_decider is the one-cycle specialization, and the
  cylinder/Mobius classes live in a 1-dimensional H1." T236 attacks both the
  full-poset-cofinality half and the multi-cycle half.
- **From T231 (reused by import):** `subdivide_annular` (uniform bisection),
  `annular_class_obstructed` (wrap-parity decider, used only as a cross-check).
- **From T226 (reused by import):** `CoverNerve`, `annular_cover`, `is_cocycle`,
  `monodromy_sign`, `transition_is_coboundary` (the exhaustive `2^n` cross-check),
  `z2_add`. `coefficient_sheaf_h1.py` and `sheaf_h1_refinement.py` are **not
  modified**.

## The objects

- **General Z2 cycle-space cohomology** (`general_h1_rank`,
  `general_class_vector`, `general_class_obstructed`). For an arbitrary thin nerve
  graph the coefficient-aware H1 over Z2 is the cycle-space cohomology:
  `dim H1 = b1 = #E − #V + #components` (first Betti number); `[g]` is the **vector
  of fundamental-cycle parities** over a spanning-forest cycle basis (union-find
  spanning forest; each cotree edge closes one fundamental cycle; parity computed
  by tree-potential accumulation). `[g] = 0` iff every fundamental-cycle parity is
  0 iff `g` is a coboundary iff a global section exists. **poly_decider**
  (linear), cross-validated against T226's exhaustive `2^n` `transition_is_coboundary`.
- **Multi-cycle witness** (`theta_two_cycle`). A theta graph: two hub vertices
  joined by three internally-disjoint arcs A, B, C, with two independent
  fundamental cycles `A+B`, `B+C`. A reversal on arc A twists the left cycle only;
  on arc C the right cycle only; the shared arc B is untwisted, so the two cycles
  are independent in the cotree basis. `b1 = 2`; the four twist configs give four
  distinct class vectors.
- **Wider (staggered) refinement poset** (`staggered_subdivide`,
  `cofinality_certificate`). `staggered_subdivide(n, rev, S)` refines an
  `annular_n` by splitting only the patches in `S`, yielding an `n+|S|`-patch
  single-cycle cover with the wrap reversal carried faithfully. For every subset
  `S`: `coarse ≤ staggered(S) ≤ uniform-bisection` in the refinement order. The
  certificate enumerates all `2^n` subsets, checks class stability on each
  refinement edge, and certifies the uniform bisection dominates every staggered
  cover (cofinality).
- **Cech→derived comparison** (`cech_derived_comparison`). Returns the executable
  finite identity, the cofinal-stability flag, `derived_comparison_is_iso = None`
  (undecided from finite data), and the **named** residual obstruction.

## Strongest positive result

`results/sheaf-h1-cofinality/T236-results.json` (verbatim):

| Object | Result |
|---|---|
| theta H1 rank | **2** |
| theta class vectors | `00→(0,0)`, `10→(1,1)`, `01→(0,1)`, `11→(1,0)` — **4 distinct** |
| theta decider cross-validated vs exhaustive `2^n` | **True** |
| multi-cycle class refinement-stable (all 4 configs) | **True** |
| cofinality: staggered covers enumerated | **`2^4 = 16`** |
| cofinality: every staggered edge stable | **True** |
| cofinality: uniform dominates every staggered | **True** |
| cofinality: chain value == poset value | **True** |
| cofinality cross-validated vs loop-sign + wrap-parity | **True** |
| Cech→derived: finite colimit == cycle-space H1 | **True** |
| Cech→derived: `is_iso` flag | **`None` (honestly open)** |

So: (1) the colimit value of the Z2 class is **independent of the refinement
route** through the wider poset, with the bisection chain provably cofinal; (2) the
obstruction survives into a **genuine rank-2 H1** and each cycle's class is
independently refinement-stable; (3) the finite-side identity holds while the
continuum identification is honestly deferred.

## First exact obstruction / missing object (a real finding)

The **single residual gap** keeping the verdict at `conditional`: the Cech→derived
comparison map `H^1_Cech(colim covers) → H^1_derived(orientation sheaf on the
continuum band)` is an iso **only after a `lim^1` / Mittag-Leffler vanishing over
the directed system of covers**. That vanishing is a property of the **full
infinite tower**, not certifiable from any finite stage — so `is_iso` is left
`None`, not `True`. Cofinality (over the wider poset) and the multi-cycle case are
discharged as finite certificates; the derived comparison is **not**.

A secondary honesty note recorded in the finding: the staggered poset and theta
witness are still **thin covers (no triple overlaps)**, so the cocycle condition
is vacuous; a cover with genuine triple intersections (`d1 ≠ 0`) is a further,
separate stress not exercised here.

**Missing object:** a `lim^1`-vanishing certificate for the orientation-sheaf
inverse system over the band's cover poset (or a Mittag-Leffler argument for it),
which is the one ingredient that would license the Cech→derived iso — and which a
finite witness structurally cannot supply.

## Constructive next object

The **`lim^1` / Mittag-Leffler vanishing certificate** for the orientation-sheaf
`H^0` inverse system over the full cover poset of the band: prove the connecting
inverse system satisfies Mittag-Leffler (eventually-stable images), which kills the
`lim^1` correction and turns the finite cofinal identity into the Cech→derived iso.
Named, not built. (Distinct object from the D1FilteredMorphism category-colimit
lane.) A bounded interim step: extend the cycle-space stability check to covers
**with triple overlaps** (`d1 ≠ 0`) to retire the thin-cover restriction before
the continuum step.

## Meaning for the relevant claim (CSP-PO1, T222/T231 continuum row)

T231 narrowed the CSP-PO1 continuum row's conditionality to one named gap
(cofinality + Cech→derived over the full poset), with uniform-bisection stability
discharged. T236 narrows it **further**: cofinality over the wider staggered poset
**and** the multi-cycle (rank ≥ 2) case are now discharged as finite certificates,
so the residual is the **single** Cech→derived `lim^1` obstruction. The CSP-PO1
continuum row **remains `conditional`** — **no continuum theorem is claimed**, no
promotion to a continuum `proto_independent` is warranted from this finite witness.
The conditionality is now pinned to one precisely-named missing object.

## Known Physics Constraints

None. Pure finite Z2 linear algebra: union-find spanning forest, fundamental-cycle
parities, Betti-number count. No hardness/scale claim (the decider is a
`poly_decider`, explicitly NOT a hidden search per COMPLEXITY-LEDGER discipline;
the exhaustive `2^n` route is retained only as a small-cover cross-check). No
physics / geometry / curvature / connection / holonomy / new-object language is
promoted. "monodromy" = loop sign-product only; "H1" = finite Z2 cycle-space rank
of a specific finite cover.

## Success / failure criteria

**Success (all met):** (1) the general cycle-space decider agrees with the
exhaustive `2^n` coboundary search on every small witness (annular + theta) and
recovers T231's wrap-parity + the loop sign on single-cycle covers; (2) the theta
witness has H1 rank exactly 2 with four distinct, independently-twistable classes,
refinement-stable per cycle; (3) the staggered poset has the Z2 class stable on
every one of the `2^n` refinement edges, with the uniform bisection cofinal and the
chain value equal to the poset value; (4) the Cech→derived `is_iso` flag is `None`
and the residual `lim^1` obstruction is named.

**Failure (none triggered; guards binding):** stating a general continuum
Cech/sheaf-cohomology theorem from this finite witness → **forbidden**; asserting
the Cech→derived comparison is an iso → **forbidden** (the `lim^1` term is not
certifiable from finite data); any physics/geometry promotion → **forbidden**;
conflation with the D1FilteredMorphism category-colimit lane → **explicitly
disclaimed**; a `closed` verdict → **guarded against** (`test_t236_not_closed_guard`).

## Next proof / computation step

Build the `lim^1` / Mittag-Leffler vanishing certificate for the orientation-sheaf
`H^0` inverse system over the band's full cover poset — the one ingredient that
licenses the Cech→derived iso — after first extending the cycle-space stability
check to covers with genuine triple overlaps (`d1 ≠ 0`). This is the single
remaining step to move CSP-PO1's continuum row from `conditional` toward a stated
continuum certificate, still short of, and not to be confused with, a general
continuum cohomology theorem.

## Reproduction

```
cd "<repo root: .../time-as-finality>"
python -m pytest tests/test_sheaf_h1_cofinality.py -q                                   # 17 passed
python -m pytest tests/test_sheaf_h1_cofinality.py tests/test_sheaf_h1_refinement.py tests/test_coefficient_sheaf_h1.py -q   # 54 passed
python -c "from models.sheaf_h1_cofinality import run_t236_analysis, t236_result_to_dict; import json; print(json.dumps(t236_result_to_dict(run_t236_analysis()), indent=2))"
```

Results snapshot: `results/sheaf-h1-cofinality/T236-results.json`.
