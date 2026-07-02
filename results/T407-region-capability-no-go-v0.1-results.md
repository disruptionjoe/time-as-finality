# T407 Region-Indexed Capability No-Go — Results v0.1

- **Artifact:** `T407-region-capability-no-go-v0.1`
- **Spec:** [tests/T407-region-capability-no-go.md](../tests/T407-region-capability-no-go.md)
- **Model:** [models/region_capability_no_go.py](../models/region_capability_no_go.py)
- **Test:** [tests/test_region_capability_no_go.py](../tests/test_region_capability_no_go.py)
- **Numbers:** [T407-region-capability-no-go-v0.1.json](T407-region-capability-no-go-v0.1.json)
- **Tags:** direction_a, capability_object, region_indexed_no_go,
  first_c_of_r_instance, anti_scalar_capability, statistics_underdetermination,
  exhaustive_finite_family, no_claim_promotion, prior_art_flagged_from_memory

**Numbering collision — resolved 2026-07-01, authorized by Joe:** a
second, distinct quartet also numbered T397
(`multipath-class-marker-absorber`, another lane) landed mid-session before
this spec registered. Distinct slugs, both intact; the multipath quartet
registered first and keeps T397; this artifact is renumbered T397 → T407
(see the spec's Status section — the two artifacts compose rather than
compete).

## Verdict (house vocabulary; all three legs passed as stated)

**Leg 1 — C(R) realized.** At one fixed region R = {control, record
register, target} (escape registers outside), one fixed 16-protocol +
4-measurement menu, and one declared four-task set (undo_within, undo_cross,
order_postdiction, class_readout; thresholds `v* = 0.9` imported unchanged
from T392/T393, `p* = c* = 0.9`), all 24 configurations of the exhaustively
declared write family have exactly computed capability profiles. Menu values
equal closed-form optima (max residual `8.9e-16`); all 18 zero-valued undo
legs are certified impossible for **every** CPTP map supported on R
(phi-independence `4.2e-17`; channel-independent trace-norm bound
`3.8e-16` — both T393-pattern certificates); 12 distinct profiles realized.

**Leg 2 — anti-scalar at the capability level.** The realized capability
poset is the **exact product of an undo chain (3 levels) and a readout chain
(4 levels)** — a 3 x 4 grid with 18 incomparable pairs and **order dimension
exactly 2** (T394's imported exhaustive checker; realizer reconstruction
verified on all pairs). By T394 Theorem 2 (T49's Anti-Scalar rung,
tie-collapse closed), no scalar capability monotone reproduces the
enactability order. Witnessed concretely: **0 of all 4,683 weak orders** on
the 6-profile spotlight subfamily reproduce the order
(restriction-complete), and per-pair trichotomy witnesses name the defeating
tasks.

**Leg 3 — statistics underdetermine capability.** The declared
non-capability probes (joint computational-basis readout over R, all
marginals, 13 phase/placement combinations) are **exactly equal — max diff
0.0** — across a 16-configuration class that **realizes all 12 capability
profiles**. No functional of the declared R-statistics decides any
capability-typed test that varies on the class (`undo_cross >= v*` splits it
8/8). Featured pair (pristine vs publisher): statistics identical,
profiles (1, 1, 1/3, 2/3) vs (0, 0, 1, 1) — incomparable, gaps 1.0 and 2/3
in the two directions (floor 0.5). Screening-off failure certified with
T392's imported machinery: declared readout gives zero lift on all three
losses and `I(V; S) = 1.3e-15` bits; one menu probe gives lift `1/3` on all
three losses and CMI `2/3` bits. Conversely the pair
(class_keeper, z_keeper) has identical profiles (diff `4.4e-16`) and
distinct statistics (0.083): **neither typing refines the other.**

No claim promotion. No CLAIM-LEDGER entry. Q1D asserted numerically; R1
untouched. The predeclared failure branch for Leg 3 ("capability-statistics
rigidity at k = 3", to be reported as the headline if exact equality with
differing capability proved impossible) was NOT taken — the equality is
realized exactly.

## Predeclarations (fixed before inspecting numbers)

- Thresholds: `v* = 0.9` (V_STAR imported from T392/T393, unchanged),
  `p* = c* = 0.9`; Leg-3 gap floor `CAP_GAP_MIN = 0.5`.
- Phase grids imported from T393 unchanged: uniform 8-point locking grid;
  6-phase certificate sweep including incommensurate values (1, sqrt(2),
  pi/7).
- Configuration family: the FULL write-product (3 r1-writes x 2 r2-writes x
  4 e-writes = 24) — exhaustive, no post-hoc selection.
- Undo scored by phase-locked normalized visibility (T392 gameability
  lemma); manufactured-coherence cheat implemented as a null control.
- Region, menu, tasks declared once, uniformly for every configuration.
- Verdict strings predeclared as module constants, asserted verbatim.
- Exactness tolerance `1e-12` for every relation claimed exact.

## Exact computed values

### 1. Named-configuration capability profiles

| config (r1-write \| r2-write \| e-write) | undo_within | undo_cross | order_post | class | best undo protocols |
| --- | --- | --- | --- | --- | --- |
| pristine (none\|none\|none) | 1.0 | 1.0 | 1/3 | 2/3 | unswitch / unswitch |
| full_keeper (class_ph\|fine_ph\|none) | 1.0 | 1.0 | 1.0 | 1.0 | unwrite_r2+unswitch / unwrite_r1+unswitch |
| class_keeper (class_ph\|none\|none) | 1.0 | 1.0 | 2/3 | 1.0 | unswitch / unwrite_r1+unswitch |
| z_keeper (class_z\|none\|none) | 1.0 | 1.0 | 2/3 | 1.0 | unswitch / unwrite_r1_zbasis+unswitch |
| burn_emitter (none\|none\|burn) | 1.0 | 1.0 | 1/3 | 2/3 | unswitch / unswitch |
| class_keeper_class_emitter (class_ph\|none\|class) | 1.0 | **0.0** | 2/3 | 1.0 | unswitch / — |
| amnesic_emitter (none\|none\|full) | **0.0** | **0.0** | 1/3 | 2/3 | — |
| fine_keeper_full_emitter (none\|fine_ph\|full) | **0.0** | **0.0** | 2/3 | 2/3 | — |
| publisher (class_ph\|fine_ph\|full) | **0.0** | **0.0** | 1.0 | 1.0 | — |

All values exact rationals (asserted at 1e-9); menu vs closed-form max
residual `8.9e-16` over all 24 configurations; branch-sum vs gate-built
construction max diff `3.9e-17`; local order unitary vs T395's `u_of_order`
diff `0.0`. Family-wide: `undo_within >= undo_cross` everywhere (escaped
class copies kill cross-class undo while within-class coherence survives —
T395's structure, now at the capability level).

### 2. Impossibility certificates (all 18 zero undo legs)

| certificate | worst case over 18 legs |
| --- | --- |
| phi-independence of rho_R (6 phases incl. incommensurate) | **4.2e-17** (< 1e-12) |
| channel-independent bound `3(||Re X||_1 + ||Im X||_1)` | **3.8e-16** (< v* = 0.9; covers ALL CPTP maps on R) |
| menu maximum on the same legs | 0.0 |
| pass-leg phi-dependence floor (teeth) | **0.102** (> 0.1) |
| sanity: pristine bound vs achieved | 2.83 >= 1.0 |
| Haar spot check (20 seeded unitaries on R, illustrative) | 3.3e-17 (< 0.05) |
| manufactured-coherence cheat: raw / locked | 1.5 / **3.9e-17** |

### 3. The realized capability poset (Leg 2)

12 distinct profiles; 48 comparable + 18 incomparable pairs = C(12,2) = 66;
not a chain; **order dimension exactly 2** (T394 `minimal_axis_count`);
2-realizer rank magnitudes verified to reconstruct the order on all pairs.
The poset is the exact product order of:

- undo axis (3-chain): (0,0) < (1,0) < (1,1)
- readout axis (4-chain): (1/3, 2/3) < (2/3, 2/3) < (2/3, 1) < (1, 1)

Hasse sketch (rows = undo level, columns = readout level; every edge one
step right or up; 17 edges = 3(4-1) + 4(3-1)):

```
undo (1,1):  pristine/burn -- fine_keeper -- class_keeper/z_keeper -- full_keeper
                 |                |                  |                    |
undo (1,0):  class_emitter -- +fine_kept -- class_keeper_class_em. -- full_kept+class_em.
                 |                |                  |                    |
undo (0,0):  amnesic_em.  -- fine_keeper_full_em. -- class+full_em. -- publisher
```

Anti-scalar witnesses:

- Exhaustive: **0 / 4,683** weak orders (all total preorders on the
  6-profile spotlight subfamily {pristine, full_keeper, amnesic_emitter,
  publisher, class_keeper_class_emitter, fine_keeper_full_emitter})
  reproduce the enactability order. Restriction-complete for the full
  family.
- Trichotomy (pristine vs publisher): pristine strictly better at
  {undo_within, undo_cross} (gaps 1.0); publisher strictly better at
  {order_postdiction, class_readout} (gaps 2/3, 1/3); any real-valued f
  must order them and thereby deny one strict advantage.

### 4. Statistics classes and the featured pair (Leg 3)

- Statistics partition of the 24 configurations: **2 classes, sizes 16 and
  8** (the z-basis-write configurations form the second class). Max
  intra-class diff **0.0** (exact float equality); min inter-class diff
  0.083 (teeth).
- The 16-member flat class **realizes all 12 capability profiles**; the
  capability test `undo_cross >= v*` splits it 8 pass / 8 fail while every
  declared statistic is constant on it.
- Featured pair (pristine, publisher): stats max diff **0.0** over 13
  phase/placement combinations; capability gaps: max 1.0 in pristine's
  favor, 2/3 in publisher's favor — both above the 0.5 floor; incomparable.

### 5. Screening-off certificate (T392 machinery, imported)

Equal-prior mixture {pristine, publisher}; verdict = fixed map from the
certified undo_cross axis (`cross-undo-capable-at-R` vs
`cross-undo-incapable-at-R`); three-loss family (T155 discipline).

| quantity | zero_one | false_capable_costly | false_incapable_costly |
| --- | --- | --- | --- |
| prior-only risk | 0.5 | 0.5 | 0.5 |
| full declared-readout risk | 0.5 | 0.5 | 0.5 |
| statistics lift | **0.0** | **0.0** | **0.0** |
| probe risk (record X x X + (c,t) Z) | 1/6 | 1/6 | 1/6 |
| probe lift | **1/3** | **1/3** | **1/3** |
| T137 downstream-null lift | 0.0 | 0.0 | 0.0 |

`I(V; declared readout) = 1.3e-15` bits;
`I(V; probe | probe's statistics part) = 2/3` bits exactly;
T137 null CMI `0.0`.

### 6. Null controls

- **Vacuity control** (pristine vs z_keeper): the same statistics-typed
  functional family DOES distinguish this pair — stats diff 0.083, 0-1
  Bayes lift **0.25**. The Leg-3 equality certificates are not vacuous.
- **Converse pair** (class_keeper vs z_keeper): capability profiles
  identical (max diff `4.4e-16`), statistics distinct (0.083). Capability
  functionals cannot decide the statistics class either — the
  underdetermination is two-directional.
- **Burn null** (T393 B'-analog): order-uncorrelated emission with
  excitation probability 1.0 (vs 0.0 pristine) moves neither the profile
  (diff 0.0) nor the statistics (diff 0.0). Emission per se does no work.

### 7. Q1D no-signalling certificate

- Declared R readout vs preparation phase: max diff **2.8e-17**.
- Declared R readout vs escape-register writes: max diff **0.0** (outside-
  region couplings cannot steer the declared readout).
- (c, r1, r2) marginal vs target-operation settings (predeclared Ry
  perturbations, angles 0.9 / 0.7): max diff **4.2e-17**; teeth: the same
  settings move the target marginal by **0.130**.
- Disclosed: a single target traverses all operations; the asserted surface
  is non-steerability of the declared readout (same disclosure as T395).

## Honest weaknesses (reviewer-facing)

- **The resource-theory absorber is unrun and presumed hungry.** Capability
  profiles are monotone vectors; incomparability under a restricted
  operation class is standard resource theory (LOCC/majorization,
  coherence — from memory, unverified). Leg 2's theorem-shape is presumed
  absorbed; the claimed residue is only the region-indexing, the
  record-access physicality, and the exact statistics-flat family. The
  absorber run gates any promotion.
- **The profile values are identities of the branch form.** As in T395's
  re-scope: undo values are 0/1 because copies are perfect and the escape
  overlap is exactly 0 or 1; readout optima are group-counting identities.
  The 24-configuration sweep re-verifies these identities across the
  family rather than probing 24 contingencies. The earned content is the
  assembled three-leg object with its certificates, not any single number.
- **Knife-edge couplings.** Perfect CNOT-grade writes; the graded
  (partial-amplitude) family is the named v0.2 card, with T393's
  thresholded-forcing machinery the intended tool.
- **The statistics/capability boundary is convention-relative.** Everything
  is stated relative to the house's declared Z-readout convention and the
  declared menu; a different declared readout would move the boundary. The
  converse pair shows the two typings are mutually non-reducing under THIS
  convention, which is the honest scope of the no-go.
- **Menu-relativity of C(R).** Task values are menu optima; in this family
  they happen to be menu-robust (readout optima are global; undo
  impossibility is all-channel), which is a family feature, not a general
  property of the construction.
- **Dimension 2 is family-realized, not a law.** The grid structure (two
  clean axes) is a finding about THIS write family; nothing excludes
  capability posets of higher dimension elsewhere (T394's S_d ladder names
  the escalation).

## pytest output

```
platform linux -- Python 3.10.12, pytest-9.1.1, pluggy-1.6.0
collected 34 items

tests/test_region_capability_no_go.py::test_predeclared_constants PASSED
tests/test_region_capability_no_go.py::test_region_declared_once_and_partitioned PASSED
tests/test_region_capability_no_go.py::test_menu_is_finite_and_config_independent PASSED
tests/test_region_capability_no_go.py::test_construction_cross_checks PASSED
tests/test_region_capability_no_go.py::test_named_profiles_exact PASSED
tests/test_region_capability_no_go.py::test_menu_achieves_closed_form_optima PASSED
tests/test_region_capability_no_go.py::test_twelve_distinct_profiles PASSED
tests/test_region_capability_no_go.py::test_undo_hierarchy_within_ge_cross PASSED
tests/test_region_capability_no_go.py::test_pass_fail_pattern_typed PASSED
tests/test_region_capability_no_go.py::test_zero_legs_all_certified_against_all_channels PASSED
tests/test_region_capability_no_go.py::test_pass_legs_have_phi_dependence_teeth PASSED
tests/test_region_capability_no_go.py::test_channel_bound_respects_achievability PASSED
tests/test_region_capability_no_go.py::test_haar_spot_check_illustrative PASSED
tests/test_region_capability_no_go.py::test_manufactured_coherence_null PASSED
tests/test_region_capability_no_go.py::test_poset_shape PASSED
tests/test_region_capability_no_go.py::test_featured_pairs_are_incomparable PASSED
tests/test_region_capability_no_go.py::test_order_dimension_exactly_two_via_t394 PASSED
tests/test_region_capability_no_go.py::test_grid_product_structure PASSED
tests/test_region_capability_no_go.py::test_exhaustive_scalar_refutation PASSED
tests/test_region_capability_no_go.py::test_trichotomy_witnesses_concrete PASSED
tests/test_region_capability_no_go.py::test_statistics_partition_two_classes PASSED
tests/test_region_capability_no_go.py::test_flat_class_realizes_all_profiles PASSED
tests/test_region_capability_no_go.py::test_featured_pair_stats_equal_capability_incomparable PASSED
tests/test_region_capability_no_go.py::test_capability_test_undecidable_by_statistics PASSED
tests/test_region_capability_no_go.py::test_screening_statistics_carry_zero PASSED
tests/test_region_capability_no_go.py::test_screening_probe_positive_across_loss_family PASSED
tests/test_region_capability_no_go.py::test_t137_downstream_null PASSED
tests/test_region_capability_no_go.py::test_vacuity_control_statistics_do_distinguish_another_pair PASSED
tests/test_region_capability_no_go.py::test_converse_pair_capability_identical_statistics_distinct PASSED
tests/test_region_capability_no_go.py::test_burn_null_emission_alone_is_innocuous PASSED
tests/test_region_capability_no_go.py::test_q1d_no_signalling PASSED
tests/test_region_capability_no_go.py::test_verdict_strings_predeclared_and_restrained PASSED
tests/test_region_capability_no_go.py::test_t395_order_machinery_provenance PASSED
tests/test_region_capability_no_go.py::test_result_dict_is_json_serializable PASSED

34 passed in 3.03s
```

The T392 (18), T393 (29), T394 (29), and T395 (35) suites were re-run
alongside and remain green (111 passed in 15.2 s). T407 imports from all
four by name.

## Recommended next (no promotion)

- **Run the resource-theory absorber** before any investment in C(R) as a
  named object: map the profile poset onto verified resource-theoretic
  monotone structure and test whether the region-indexed residue survives —
  the T395 kill-test pattern, one level up. Gates everything.
- Partial-amplitude deformation of the family (graded undo via
  controlled-Ry escape, T393's alpha machinery): does incomparability
  survive off the knife edge at the declared thresholds?
- Capability posets of dimension 3 (engineer escape structures realizing
  T394's S_3 at the capability level).
- The TI-side twin of survivor (a): the Ext_S burden re-typed against this
  artifact's capability-typed readout. TI-owned; pauses for Joe.
- Verify flagged prior art before anything external-facing; pauses for Joe
  per AGENTS.md.
