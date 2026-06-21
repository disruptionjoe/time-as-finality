# Technical Report: GU Class-Relative No-Go Bridge Audit v0.1

## Summary

T27 asks whether selected GU no-go analyses can be represented as finite
D1RestrictionSystems whose projections preserve the original theorem while
identifying the additional structure carried by the richer model.

Top-level verdict:

```text
H2: only some cases admit faithful finite restriction-system abstractions.
    The bridge identifies exactly which structural assumptions matter.
```

The Projection-Obstruction Pattern — a candidate finite theorem about
class-relative abstraction — is detected across the two faithful cases.

Stretch goal: **REACHED**.

---

## Non-Goals

This report does not claim:

- that Time as Finality proves Geometric Unity;
- that Geometric Unity proves Time as Finality;
- that any physical no-go theorem has been overturned;
- that finite executable models replace the original mathematical proofs.

The goal is to determine whether the same local-to-global restriction
structure appears in the finite abstraction after the physics is stripped away.

---

## Definition

T27 reuses the T26 `D1RestrictionSystem` object unchanged.  The D1Profile
dimensions are reinterpreted for the bridge domain:

| Dimension | Bridge interpretation |
| --- | --- |
| `accessible_support` | count of accessible chiral data at the site |
| `holder_redundancy` | number of independent chirality-carrying mechanisms |
| `branch_support` | degree of chiral branching (left/right separation) |
| `reversal_cost` | cost to suppress or reverse chirality (higher = harder) |

For each case, two systems and one morphism are constructed:

```
Richer D1RestrictionSystem      (fuller substrate)
  ↓
D1RestrictionMorphism           (forgetful functor)
  ↓
Restricted D1RestrictionSystem  (projected class — no-go theorem applies here)
```

---

## Case 1: Witten 1981

### Theorem

In smooth compact Kaluza-Klein compactifications with no background gauge data,
the 4d fermion spectrum is non-chiral.  The Dirac index vanishes inside the
smooth class.

### Richer System: `witten_stratified_richer`

The substrate is a stratified geometric object `(X_tilde, S, B)` where `X_tilde`
is a singular variety, `S` is the singular/defect stratum, and `B` is brane/flux
data at `S`.

| Site | Profile `(as,hr,bs,rc)` | Meaning |
| --- | --- | --- |
| `smooth_bulk` | (0, 1, 0, 3) | smooth bulk: no accessible chirality |
| `defect_stratum` | (1, 2, 1, 1) | singular stratum: accessible chiral data |

Patches:

| Patch | Variables | Constraint | Local satisfiable |
| --- | --- | --- | --- |
| `bulk_local` | `{chiral_bulk}` | none | yes |
| `defect_local` | `{chiral_defect}` | none | yes |
| `anomaly_inflow` | `{chiral_bulk, chiral_defect}` | `chiral_bulk != chiral_defect` | yes |

Global section: **EXISTS** (global_witness_count = 2; assignments `{+1, -1}` and
`{-1, +1}` satisfy the constraint).  The defect carries the anomaly-inflow
chirality independently from the bulk.

### Restricted System: `witten_smooth_restricted`

The class is fixed to smooth, compact, trivial background.  Two smooth patches
share a `smooth_field` variable — the smooth structure forces them to track the
same chirality.  The chirality requirement demands they differ.

| Site | Profile `(as,hr,bs,rc)` | Meaning |
| --- | --- | --- |
| `smooth_site_A` | (0, 1, 0, 3) | smooth patch A |
| `smooth_site_B` | (0, 1, 0, 3) | smooth patch B |

Patches:

| Patch | Variables | Constraint | Local satisfiable |
| --- | --- | --- | --- |
| `patch_A_smooth` | `{chiral_A, smooth_field}` | `chiral_A same smooth_field` | yes |
| `patch_B_smooth` | `{chiral_B, smooth_field}` | `chiral_B same smooth_field` | yes |
| `chirality_requirement` | `{chiral_A, chiral_B}` | `chiral_A != chiral_B` | yes |

Global section: **OBSTRUCTED** (global_witness_count = 0).

The shared `smooth_field` forces `chiral_A = smooth_field = chiral_B`, but
`chirality_requirement` demands `chiral_A != chiral_B`.  Contradiction.

This is the finite abstraction of the Witten theorem.

### Morphism: `witten_smoothing_functor`

The smoothing functor `phi_smooth` maps the stratified substrate to the smooth
shadow.

| Source site | Target site |
| --- | --- |
| `smooth_bulk` | `smooth_site_A` |
| `defect_stratum` | `smooth_site_B` |

Declared preserved dimensions: `reversal_cost`.

Morphism analysis:

| Check | Result |
| --- | --- |
| site_map_total | True |
| local_profiles_preserved | **False** — defect profile (1,2,1,1) vs smooth_site_B (0,1,0,3) |
| trust_path_preserved | True |
| obstruction_status_preserved | **False** — richer=False, restricted=True |
| reached | False |
| failure kind | `local_profile_mismatch` |

### What is forgotten

- The defect stratum profile: `accessible_support`, `holder_redundancy`, `branch_support`
  are all non-zero at the defect but zero at the smooth shadow.
- The `anomaly_inflow` patch: the `chiral_defect != chiral_bulk` constraint is
  lost.  This is exactly the mechanism that allowed the global section to exist.
- All brane, flux, and singular-geometry data `B` at `S`.

### What is preserved

- `reversal_cost` at the smooth bulk site.
- The trust transport path.
- The smooth-shadow proposition value (`non_chiral`).

### Bridge verdict

**FAITHFUL (H1).**  The finite D1RestrictionSystem captures the Witten
class-relative structure.  The restricted system encodes the no-go theorem as a
gluing obstruction.  The morphism analysis identifies the defect profile and the
anomaly-inflow patch as the forgotten structure.

---

## Case 2: Nielsen-Ninomiya

### Theorem

A free bilinear lattice fermion action that is local, Hermitian,
translation-invariant, and carries exact on-site U(1)_V and U(1)_A has an equal
number of left- and right-handed species.  The net chiral spectrum is zero.

### Richer System: `nn_bulk_boundary_richer`

The substrate is a (d+1)-dimensional SPT bulk together with a d-dimensional
boundary and a modified Ginsparg-Wilson algebra.

| Site | Profile `(as,hr,bs,rc)` | Meaning |
| --- | --- | --- |
| `bulk_spt` | (1, 2, 1, 1) | SPT bulk: accessible via anomaly inflow |
| `boundary_site` | (1, 1, 1, 2) | boundary: accessible chiral modes |
| `modified_algebra` | (1, 1, 0, 1) | Ginsparg-Wilson algebra structure |

Patches:

| Patch | Variables | Constraint | Local satisfiable |
| --- | --- | --- | --- |
| `anomaly_inflow_local` | `{anomaly_in}` | none | yes |
| `boundary_chiral` | `{chiral_left, chiral_right}` | `chiral_left != chiral_right` | yes |
| `algebra_consistency` | `{anomaly_in, chiral_left}` | `anomaly_in same chiral_left` | yes |

Global section: **EXISTS** (global_witness_count = 2; e.g., `{anomaly_in=+1, chiral_left=+1, chiral_right=-1}`).

### Restricted System: `nn_onsit_lattice_restricted`

Three lattice sites encode the three groups of Nielsen-Ninomiya assumptions:
locality+hermiticity, translation invariance, and on-site exact U(1)_A.

| Site | Profile `(as,hr,bs,rc)` | Meaning |
| --- | --- | --- |
| `lattice_A` | (0, 1, 0, 2) | on-site site A |
| `lattice_B` | (0, 1, 0, 2) | on-site site B |
| `lattice_C` | (0, 1, 0, 2) | on-site site C |

Patches:

| Patch | Variables | Constraint | Local satisfiable | NN assumption group |
| --- | --- | --- | --- | --- |
| `locality_hermitian` | `{chiral_A, chiral_B}` | `chiral_A same chiral_B` | yes | locality + hermiticity |
| `translation_invariance` | `{chiral_B, chiral_C}` | `chiral_B same chiral_C` | yes | translation invariance |
| `exact_onsit_ua` | `{chiral_A, chiral_C}` | `chiral_A != chiral_C` | yes | on-site exact U(1)_A |

Global section: **OBSTRUCTED** (global_witness_count = 0).

The chain `chiral_A = chiral_B = chiral_C` (from the first two patches) forces
`chiral_A = chiral_C`, but `exact_onsit_ua` demands `chiral_A != chiral_C`.
Contradiction.  This is the finite abstraction of the doubling theorem.

### Morphism: `nn_onsit_locality_functor`

The on-site locality functor `phi_local` maps the bulk+boundary+algebra to the
d-dimensional on-site lattice.

| Source site | Target site |
| --- | --- |
| `bulk_spt` | `lattice_A` |
| `boundary_site` | `lattice_B` |
| `modified_algebra` | `lattice_C` |

Morphism analysis:

| Check | Result |
| --- | --- |
| site_map_total | True |
| local_profiles_preserved | **False** — bulk profile (1,2,1,1) vs lattice_A (0,1,0,2) |
| trust_path_preserved | True |
| obstruction_status_preserved | **False** — richer=False, restricted=True |
| reached | False |
| failure kind | `local_profile_mismatch` |

### What is forgotten

- The bulk SPT data: `accessible_support`, `holder_redundancy`, `branch_support`.
- The `anomaly_inflow_local` and `algebra_consistency` patches — the mechanism
  that allows the bulk to supply chiral content to the boundary.
- The modified Ginsparg-Wilson algebra structure.

### Bridge verdict

**FAITHFUL (H1).**  The on-site-locality morphism correctly identifies the bulk
SPT data and the modified algebra as the forgotten structure.  The three-patch
obstruction in the restricted system models the doubling theorem as a
local-to-global contradiction between the three assumption groups.

---

## Case 3: Distler-Garibaldi

### Theorem

There is no real form of E8 containing subgroups SL(2,C) and G satisfying all
three ToE conditions: (ToE1) G connected compact centralizing SL(2,C); (ToE2)
V_{m,n}=0 for m+n>4; (ToE3) V_{2,1} complex as a G-representation.

### Richer System: `dg_e8xe8_bundle_richer`

The richer object is E8 x E8 with a Calabi-Yau bundle and flux (candidate a
from the GU no-go map).  This has four sites.

| Site | Profile `(as,hr,bs,rc)` | Meaning |
| --- | --- | --- |
| `e8_factor_1` | (1, 1, 1, 2) | first E8 factor |
| `e8_factor_2` | (1, 1, 1, 2) | second E8 factor |
| `cy_bundle` | (1, 2, 1, 1) | Calabi-Yau bundle with flux |
| `sm_chirality` | (1, 1, 1, 1) | SM chiral generation content |

Global section: **EXISTS** (global_witness_count = 4).  The two E8 factors are
compatible (`v_e81 same v_e82`) and the bundle encodes the SM chirality
(`v_bundle same v_sm`).

### Restricted System: `dg_single_e8_restricted`

Three sites represent the SL(2,C) x G decomposition of a single E8 adjoint.
Six patches encode the individual ToE conditions, the E8 structure constraint,
the SM physics demand, and the Distler-Garibaldi theorem.

| Site | Profile `(as,hr,bs,rc)` | Meaning |
| --- | --- | --- |
| `sl2c_sector` | (0, 1, 0, 3) | SL(2,C) Lorentz sector |
| `g_centralizer` | (0, 1, 0, 3) | G centralizer sector |
| `matter_spectrum` | (0, 0, 0, 3) | matter V_{m,n} content |

The `sm_physics_demand` patch forces `v21_complex same g_connected`, while the
`dg_theorem` patch forces `v21_complex different g_connected` (given that
`g_connected same v_high_spin` holds in single-E8).  These two patches are each
locally satisfiable but globally contradictory.

Global section: **OBSTRUCTED** (global_witness_count = 0; all 6 patches locally
satisfiable, local_witness_count = 6).

### Morphism: `dg_single_e8_adjoint_functor`

The attempted forgetful map `phi_singleE8` maps three of four richer sites to
restricted sites.  The fourth site (`sm_chirality`) has **no counterpart** in
single-E8 representation theory.

Site map (incomplete):

| Source site | Target site |
| --- | --- |
| `e8_factor_1` | `sl2c_sector` |
| `e8_factor_2` | `g_centralizer` |
| `cy_bundle` | `matter_spectrum` |
| `sm_chirality` | **(no target)** |

Morphism analysis:

| Check | Result |
| --- | --- |
| site_map_total | **False** — `sm_chirality` has no target |
| local_profiles_preserved | False |
| trust_path_preserved | True |
| obstruction_status_preserved | False |
| reached | False |
| failure kind | **`site_map_incomplete`** |

### What is forgotten

- The `sm_chirality` site itself: it has no image in single-E8.
- The second E8 factor and the product-group structure.
- The Calabi-Yau bundle data and flux.

### Bridge verdict

**BRIDGE FAILS — CATEGORY CHANGE (H3).**

This failure is categorically different from Cases 1 and 2:

| Aspect | Witten / NN | Distler-Garibaldi |
| --- | --- | --- |
| site_map_total | True | **False** |
| Morphism defined | Yes | **No** |
| Failure kind | `local_profile_mismatch` | **`site_map_incomplete`** |
| Nature of richer object | enrichment (+ defect / + bulk) | **category change** (product group, K-M) |

The richer DG objects (E8 x E8, K(E10), SO(3,11)) are not enrichments of
single-E8.  They are structurally different mathematical objects.  The
forgetful functor `phi_singleE8` cannot be represented as a D1RestrictionSystem
morphism because there is no site in the restricted system that can receive the
`sm_chirality` content.

This matches the GU no-go map's diagnosis: "Every successful evasion leaves the
class entirely...the forgetful operation is more like 'collapse a category' than
'compute a shadow'."

---

## Cross-Case Analysis

### Comparison Table

| Criterion | Witten | Nielsen-Ninomiya | Distler-Garibaldi |
| --- | --- | --- | --- |
| Richer system valid | Yes | Yes | Yes |
| Restricted system valid | Yes | Yes | Yes |
| Richer: global section exists | Yes (2 witnesses) | Yes (2 witnesses) | Yes (4 witnesses) |
| Restricted: obstructed | Yes (0 witnesses) | Yes (0 witnesses) | Yes (0 witnesses) |
| All restricted patches locally satisfiable | Yes (3/3) | Yes (3/3) | Yes (6/6) |
| Morphism site_map_total | Yes | Yes | **No** |
| local_profiles_preserved | No | No | No |
| trust_path_preserved | Yes | Yes | Yes |
| obstruction_status_preserved | No | No | No |
| Morphism failure kind | profile_mismatch | profile_mismatch | **site_map_incomplete** |
| Hypothesis | H1 | H1 | **H3** |

### Projection-Obstruction Pattern

The two H1 cases share a common finite structure:

```
Richer system: global section EXISTS
    ↓  forgetful morphism (site_map_total=True)
Restricted system: global section OBSTRUCTED
```

The morphism is defined but blocked by two simultaneous failures:
1. `local_profiles_preserved = False` — profile data is lost at the site level
2. `obstruction_status_preserved = False` — the morphism introduces an obstruction
   that did not exist in the richer system

The forgotten structure in both cases is the patch data that allowed the richer
system's global section to exist:

| Case | Forgotten patch data |
| --- | --- |
| Witten | `anomaly_inflow`: `chiral_defect != chiral_bulk` |
| Nielsen-Ninomiya | `boundary_chiral`: `chiral_left != chiral_right` + `algebra_consistency` |

**Candidate finite theorem (Projection-Obstruction Schema):**

> A theorem proved within a projected class corresponds to a gluing obstruction
> in the restricted D1RestrictionSystem, while the richer object resolves that
> obstruction via extra patch data invisible to the restricted class.  The
> forgetful morphism is site-map-complete but loses exactly that patch data,
> detected as local_profile_mismatch and obstruction_status_preserved=False.

This theorem is about the mathematics of class-relative abstraction, not about
any particular physical theory.

**T29 follow-on:** [T29: Projection-Obstruction Schema](tests/T29-projection-obstruction-schema.md)
formalizes this stretch result as the named finite schema `PO1`. T27 found
the pattern in Witten and Nielsen-Ninomiya and found a non-definable boundary
in Distler-Garibaldi. T29 adds synthetic boundary cases showing that projection
can exist without producing an obstruction, and that obstruction can exist in
both rich and restricted systems without being projection-created.

---

## Hypothesis Evaluations

| Hypothesis | Status | Evidence |
| --- | --- | --- |
| H0: no useful bridge exists | **Rejected** for Witten and NN | both admit faithful finite bridge models |
| H1: faithful finite abstraction | **Supported** for Witten and NN | all tests pass; pattern detected |
| H2: only some cases; bridge identifies structure | **Best overall verdict** | two H1 + one H3 |
| H3: richer mathematics required | **Supported for DG** | site_map_incomplete; category change confirmed |

---

## Informative Failures

| Attempted claim | What failed | Boundary |
| --- | --- | --- |
| All three cases admit H1 bridges | DG bridge is site_map_incomplete | DG richer objects are category changes, not enrichments |
| The morphism fully characterizes the forgotten structure | morphism reports only the first failure (profile_mismatch); obstruction non-preservation is secondary | the BridgeCase explicitly records both failures |
| The restricted DG system encodes the DG theorem as a standard gluing obstruction | it does, but the richer-to-restricted morphism can't be defined | two separate failures: (1) restricted has an obstruction; (2) the morphism is incomplete |
| T26 supports presheaf or category-level bridges | T26 morphisms require site-map-total; functors between different categories are not representable | DG calls for presheaf-level or functor-category-level machinery |

---

## Recommendation

Adopt H2 as the top-level verdict.

For Witten 1981 and Nielsen-Ninomiya:

- The finite bridge is **structurally faithful**.
- The Projection-Obstruction Pattern is a candidate finite schema, later
  formalized as [PO1](claims/PO1-projection-obstruction-schema.md) in T29.
- The morphism analysis correctly identifies the forgotten structure.
- The no-go theorem maps to a gluing obstruction in the restricted class.

For Distler-Garibaldi:

- The bridge fails with `site_map_incomplete`.
- This is an **informative negative**, not a failure of the framework.
- It identifies the exact boundary of T26: restriction-system morphisms require
  site-map completeness, which requires the richer and restricted systems to
  share the same site vocabulary.
- DG calls for richer morphism machinery: presheaf functors or category-level
  forgetful maps that can represent product-group or Kac-Moody structure.

Do not claim that any physical no-go theorem has been overturned.  The abstract
local-to-global structure survives in the finite abstraction.  The physics is
unchanged.

---

## Artifacts

| Artifact | Path |
| --- | --- |
| Bridge models | `models/gu_class_relative_bridge.py` |
| Runner | `models/run_t27.py` |
| Test suite | `tests/test_gu_class_relative_bridge.py` |
| Test specification | `tests/T27-class-relative-bridge-audit.md` |
| JSON results | `results/gu-class-relative-bridge-v0.1.json` |
| Results summary | `results/gu-class-relative-bridge-v0.1-results.md` |
| This report | `TECHNICAL-REPORT-class-relative-bridge-audit-v0.1.md` |
| GU crosswalk | `gu-formalization/explorations/time-as-finality-crosswalk/bridge-audit-crosswalk.md` |
