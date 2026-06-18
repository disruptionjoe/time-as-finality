---
title: "Impossibility Results as Finite Gluing Obstructions"
status: technical-note
version: "0.1"
updated_at: "2026-06-17"
---

# Impossibility Results as Finite Gluing Obstructions

**Scope.** This note records a pattern identified across T27 and T28: several
canonical impossibility results from different domains share a common finite
structure that the T26 D1RestrictionSystem can express directly.

**Non-goal.** This is not a proof that physics no-go theorems have been
overturned, nor that CAP is solvable.  The pattern is about the mathematics
of class-relative abstraction.

---

## The pattern

A multi-assumption impossibility result often has this structure:

1. **Assumption set A** is individually consistent (each assumption is locally
   satisfiable -- there exists an assignment satisfying it in isolation).
2. **Assumption set A taken together** is inconsistent (no assignment satisfies
   all assumptions simultaneously).
3. **A richer substrate** exists in which some assumption is relaxed or
   generalized, restoring consistency.
4. **A forgetful map** from the richer substrate to the restricted class loses
   exactly the relaxed assumption.

In D1RestrictionSystem terms:

```
Richer system: global section EXISTS (all patches globally satisfiable)
    |
    |  D1RestrictionMorphism (forgetful functor)
    |  - site_map_total = True
    |  - local_profiles_preserved = False (extra structure is lost)
    |  - obstruction_status_preserved = False (obstruction is introduced)
    v
Restricted system: global section OBSTRUCTED (locally satisfiable, globally not)
```

The forgetful morphism is site-map-complete but loses the patch data that
allowed the richer global section.  The no-go theorem, in this encoding, is
the statement that the restricted system is obstructed.  The evasion is the
statement that the richer system is not.

---

## Instances

### Nielsen-Ninomiya (T27)

Domain: quantum field theory / lattice fermions.

Restricted system (three patches):
- `locality_hermitian`: chiral_A same chiral_B
- `translation_invariance`: chiral_B same chiral_C
- `exact_onsit_ua`: chiral_A different chiral_C

Chaining: A=B=C but A!=C.  global_witness_count=0.

Richer system: bulk SPT + boundary + modified Ginsparg-Wilson algebra.
Global section exists via anomaly inflow.  Forgotten: bulk SPT data and
modified algebra structure.

### CAP Theorem (T28)

Domain: distributed systems.

Restricted system (three patches):
- `consistency`: state_A same state_B
- `availability`: state_B same state_C
- `partition_tolerance`: state_A different state_C

Chaining: A=B=C but A!=C.  global_witness_count=0.

Structural identity with NN: same patch_count=3, local_witness_count=3,
global_witness_count=0.  The chaining pattern is identical.

Richer system: eventual-consistency substrate.  Global section exists via
partition divergence and sync reconciliation.  Forgotten: branch_support
(the ability to serve divergent state) and the partition_diverge patch.

### Witten 1981 (T27)

Domain: physics / Kaluza-Klein chirality.

Restricted system (three patches, different structure): two smooth-field
patches force chiral_A = chiral_B = smooth_field, while a chirality
requirement forces chiral_A != chiral_B.  global_witness_count=0.

Richer system: stratified geometry with defect stratum.  Global section
exists via anomaly inflow at the defect.  Forgotten: defect stratum profile
and the anomaly_inflow patch.

*Note:* the Witten obstruction has a slightly different structure (shared
variable forcing rather than pure chaining), but the same Projection-
Obstruction Pattern holds: richer unobstructed, restricted obstructed,
morphism site-map-complete but blocked.

### Distler-Garibaldi (T27) -- excluded from the pattern

Domain: physics / representation theory.

The DG bridge fails with `site_map_total=False`: the richer E8xE8 + bundle
system has a site (sm_chirality) with no counterpart in the single-E8
restricted class.  This is a category change, not an enrichment.  The
Projection-Obstruction Pattern requires site_map_total=True.

DG's exclusion from the pattern is itself informative: it identifies the
boundary between impossibility results that are enrichments (richer structure
relaxes an assumption within the same class) and results that require
genuinely different mathematical objects.

### Arrow's impossibility (sketch -- richer variables needed)

Domain: social choice theory.

Arrow's theorem states that no rank-order voting system satisfies
unanimity, independence of irrelevant alternatives (IIA), and non-dictatorship
simultaneously.  The three-patch chaining structure is present: the conditions
interact globally in a way that produces contradiction even though each is
individually satisfiable.

A full T26 encoding is not constructed here because the variables need to
range over preference orderings rather than binary values.  The current T26
constraint system uses binary (same/different) variables.  A richer variable
type (e.g., ranked choice over finite alternatives) would be required to
encode Arrow faithfully.  This is noted as a future extension, not a gap
in the current results.

---

## T26 as minimal executable sheaf cohomology

The T26 D1RestrictionSystem is the smallest object that can express the
local-to-global obstruction without requiring topology, continuous geometry,
or the full apparatus of sheaf cohomology.

The analogy is precise but finite:

| Sheaf cohomology concept | T26 analog |
| --- | --- |
| Open cover of a topological space | Sites in the D1RestrictionSystem |
| Local sections on each open set | LocalD1Value + proposition_value per site |
| Gluing condition on overlaps | RestrictionPatch with PatchConstraint |
| Global section | Assignment satisfying all patch constraints simultaneously |
| H^1 obstruction (Cech 1-cocycle) | Gluing obstruction: local_witness_count = n but global_witness_count = 0 |
| Restriction map | D1RestrictionMorphism |
| Forgetful functor | Morphism with local_profiles_preserved=False |

The T26 system does not use topology.  It replaces open sets with finite
sites, continuous overlap conditions with discrete patch constraints, and
Cech cohomology with explicit enumeration over binary variable assignments.
The obstruction is detected computationally, not derived cohomologically.

This makes T26 accessible to engineers, computer scientists, and
anyone studying impossibility results without a background in differential
geometry.

---

## Evasion = patch relaxation

In every H1 case, the evasion of an impossibility result corresponds to
relaxing exactly one patch in the restricted system:

| Impossibility result | Restricted patch dropped | Evasion |
| --- | --- | --- |
| Nielsen-Ninomiya | `exact_onsit_ua` (on-site U(1)_A) | Ginsparg-Wilson / overlap fermions |
| CAP | `partition_tolerance` (or: `consistency`) | Eventual consistency (AP systems); strong consistency (CP systems) |
| Witten 1981 | `chirality_requirement` (in the smooth class) | Exit to geometric class (defect stratum) |

The richer system is not a counterexample to the impossibility theorem.  It
is an object outside the theorem's domain.  The T26 encoding makes this
explicit: the forgetful morphism maps the richer object into the restricted
class, and the morphism's failure (local_profile_mismatch,
obstruction_status_preserved=False) records what was left behind.

---

## Enrichment vs. category change

The T27 Distler-Garibaldi finding establishes a qualitative distinction:

**Enrichment** (H1 cases): the richer object supplies extra patch data within
the same site-map topology.  The forgetful morphism is site-map-total.  The
morphism is blocked by profile mismatch and obstruction change, not by an
incomplete site map.

**Category change** (H3 case, DG): the richer object requires additional sites
with no counterpart in the restricted class.  The site map is incomplete.  The
forgetful map cannot even be stated as a restriction-system morphism.

This distinction is measurable at the T26 level:
- Enrichment: `site_map_total=True`, `morphism_failure_kind="local_profile_mismatch"`
- Category change: `site_map_total=False`, `morphism_failure_kind="site_map_incomplete"`

---

## Open extensions

1. **Binary-variable limitation.** Arrow's impossibility and similar results
   require richer variable types.  A T26 extension with ordered or ranked
   variables would enable faithful encoding.

2. **Morphism composition.** The T26 morphism is defined but composition
   laws are not proved.  A composition theorem would allow chaining forgetful
   functors (e.g., from the richer E8xE8 system through an intermediate
   class to the single-E8 restricted class).

3. **Non-geometric Witten evasions.** T27 used the geometric exit
   (defect stratum).  Whether observer-indexed or causal-set-indexed
   chirality also produces a faithful bridge is not tested.

---

## Artifacts

- T27 bridge audit: `models/gu_class_relative_bridge.py`
- T28 CAP bridge: `models/cap_theorem_bridge.py`
- T27 results: `results/gu-class-relative-bridge-v0.1.json`
- T28 results: `results/cap-theorem-bridge-v0.1.json`
- T26 core: `models/d1_restriction_system.py`
