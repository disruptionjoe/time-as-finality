---
title: "PO1 Admissibility Conditions"
version: "0.1"
updated_at: "2026-06-18"
status: technical-report
---

# Technical Report: PO1 Admissibility Conditions v0.1

## Purpose

T31 asks: what is the weakest version of PO1 that survives T27, T29, and T30?

The answer is a seven-condition admissibility schema. Cases satisfying all
seven count as positive PO1 evidence. Cases failing any condition are
classified into four failure types. PO1 is retained at `partially_supported`
and formally narrowed.

---

## Background

T27 identified the Projection-Obstruction Pattern across Witten 1981 and
Nielsen-Ninomiya. T29 turned it into a named schema with five explicit
classifications: faithful_projection_obstruction, lossy_projection_no_new_
obstruction, shared_obstruction, non_definable_projection, and the gap between
richer unobstructed and restricted obstructed. T28 added CAP as a
distributed-systems stress test. T30 hostile-tested PO1 with four
non-physics domains.

T30 found one positive non-physics case (git semantic merge), two negative
controls (database migration, access-control inheritance), and one boundary
(type-system macro expansion). It recommended formalizing admissibility
constraints before counting future cases as PO1 evidence.

T31 executes that recommendation.

---

## The seven admissibility conditions

### AC1: Richer system valid

The richer D1RestrictionSystem must satisfy all T26 axioms: finite unique
sites, one local D1 profile per site, valid edge endpoints, valid patch site
references, non-negative profile dimensions, and closed constraint variables.

**Why necessary:** An invalid system makes no mathematical claims. AC1 is
not a substantive constraint on real cases (all tested richer systems are
valid), but it makes the schema self-contained.

### AC2: Restricted system valid

Same as AC1 for the restricted system.

**Why necessary:** Same as AC1.

### AC3: Projection definable

The site map must be total: every source site has a target in the restricted
system (site_map_total=True).

**Why necessary:** Without a definable projection, we cannot speak of
projection-created obstruction. A category change (Distler-Garibaldi,
type-system macro) means the richer and restricted objects are not related
by restriction at all.

**Failure verdict:** `boundary_non_definable`. These cases are informative
failures, not null results: they identify the boundary of the T26 morphism
class.

### AC4: Local compatibility preserved

All patches of the restricted system must be locally satisfiable
(local_witness_count == patch_count).

**Why necessary:** If the restricted system has a patch that is locally
unsatisfiable, the obstruction is trivial (the system is broken even
locally, before any global-section computation). The interesting case is
where each patch can be locally satisfied but the global section does not
exist. A trivially broken restricted system is too easy to manufacture.

**Current evidence:** No tested case fails on AC4 alone. All 10 cases
have locally satisfiable restricted patches. AC4 is a guard for future
applications.

### AC5: Structure forgotten

The projection must forget named and measurable structure:
- `forgotten_structure` is non-empty (explicit structure is identified as lost)
- `local_profiles_preserved=False` (the morphism loses measurable profile data)

Both conditions must hold.

**Why necessary:** Without forgotten structure, the projection is identity-like
or the loss is not identified. In either case, there is no mechanism to explain
why the restricted obstruction exists but the richer system is unobstructed.

**Current evidence:** No tested case fails on AC5 alone. The synthetic shared
obstruction case fails both AC5 and AC7; the synthetic lossy case fails both
AC5 and AC6. AC5 is a guard for future applications.

### AC6: Restricted system obstructed

The restricted system must have a finite gluing obstruction:
`obstruction_detected=True` (equivalently: global_witness_count=0 and
local_witness_count == patch_count, given AC4).

**Why necessary:** Without obstruction in the restricted system, there is no
no-go to explain. A lossy projection between two unobstructed systems is
not PO1 evidence (database migration case).

**Failure verdict:** `non_admissible_no_new_obstruction`.

### AC7: Richer system unobstructed

The richer system must not have a gluing obstruction:
`obstruction_detected=False` (global_witness_count > 0).

**Why necessary:** Without a global section in the richer system, the
obstruction is not projection-created — it is inherited. Both richer and
restricted systems already suffer the same obstruction; projection does not
explain it. This is the shared-obstruction failure mode (access-control
policy case, synthetic shared-obstruction case).

**Failure verdict:** `non_admissible_shared_obstruction`.

---

## Case reclassification

All 10 cases from T27, T28, T29, and T30 are reclassified.

### Positive instances (all 7 conditions satisfied)

| Case | Source | Notes |
| --- | --- | --- |
| witten_1981 | T27 | Anomaly-inflow patch resolves chirality obstruction in richer system |
| nielsen_ninomiya | T27 | Bulk SPT data resolves three-patch chaining obstruction |
| cap_theorem | T28 | Eventual-consistency richer system resolves CAP impossibility |
| git_semantic_merge | T30 | Rename metadata resolves path-level merge conflict |

All four independently motivated projections. All four have richer systems
with global sections and restricted systems with non-trivial gluing
obstructions.

### Boundary cases (AC3 fails)

| Case | Source | Failure | Notes |
| --- | --- | --- | --- |
| distler_garibaldi | T27 | site_map_total=False | sm_chirality has no single-E8 counterpart |
| type_system_macro_expansion | T30 | site_map_total=False | macro_expansion_phase has no target in no-macro restricted system |

Both are category changes. The richer object introduces a site (or category of
sites) with no counterpart in the restricted class. This is not a failure of
PO1 — it is a correct identification of where T26 morphism machinery ends.

### Non-admissible cases

| Case | Source | Failure | Notes |
| --- | --- | --- | --- |
| synthetic_lossy_no_obstruction | T29 | AC6=False | Both systems have global sections; loss alone is insufficient |
| synthetic_shared_obstruction | T29 | AC7=False | Richer already obstructed; obstruction is inherited |
| database_expand_contract | T30 | AC6=False | Expand-contract migration loses rollout detail without creating impossibility |
| access_control_inheritance | T30 | AC7=False | Policy conflict exists in both systems; richer adds metadata, not resolution |

---

## The weakest PO1

The minimum conditions that correctly classify all 10 tested cases:

**AC1 + AC2 + AC3 + AC6 + AC7**

These five conditions produce the correct verdict for every case in the test
set. No case fails on AC4 or AC5 alone.

The weakest PO1 schema:

> A projection from a richer D1RestrictionSystem (with no gluing obstruction)
> to a restricted D1RestrictionSystem (with a gluing obstruction), where the
> projection is definable (site map total) and both systems are valid, is a
> finite Projection-Obstruction instance.

---

## The recommended PO1

**AC1 + AC2 + AC3 + AC4 + AC5 + AC6 + AC7**

The two additional conditions guard against:

- **Without AC4:** A restricted system where some patches are locally
  unsatisfiable would count as PO1 evidence. The obstruction is trivial
  (the system is broken before any global-section check). Easy to manufacture.

- **Without AC5:** A lossless projection (or one where no structure is named
  as forgotten) would count as PO1 evidence. The mechanism explaining why
  the richer system is unobstructed and the restricted system is obstructed
  would be unnamed.

Both guards are precautionary. They do not change any verdict in the current
test set. They are included because:

1. AC4 is cheap to check (one count comparison).
2. AC5 connects the schema to a domain understanding (what was forgotten and
   why it mattered).
3. Without both, the schema can be satisfied by manufactured three-patch
   contradictions that have no independent motivation.

---

## Does PO1 split?

No. T31 finds one positive schema that survives all hostile tests. The schema
does not decompose into incompatible subclaims.

The failure cases are correctly classified as four distinct non-positive types:
boundary (non-definable projection), shared obstruction, no new obstruction,
and trivial obstruction. These are exclusions from the positive schema, not
evidence for a different schema.

---

## PO1 status recommendation

**`partially_supported_narrowed`**

PO1 is retained at `partially_supported`. T31 formally narrows it by adding
explicit admissibility conditions.

The narrowed claim:

> A definable projection from a globally satisfiable richer D1RestrictionSystem
> to a non-trivially obstructed restricted D1RestrictionSystem, where the
> projection forgets named and measurable structure, is a faithful finite
> Projection-Obstruction instance.

**What this claim does:**

- Identifies a class of impossibility results that share a finite abstraction
- Allows the abstraction to be checked computationally
- Distinguishes four failure types (non-definable, shared obstruction,
  no new obstruction, trivial obstruction)
- Provides a reusable admissibility check for future cases

**What this claim does not do:**

- Prove any original no-go theorem
- Show that the pattern holds in all domains
- Remove the need for independently motivated projections
- Apply to category-change cases (DG, type-system macro)
- Generalize beyond finite binary-variable patch systems

---

## Open questions

1. **AC5 precision.** The current definition of AC5 uses `local_profiles_preserved`
   as a proxy for "measurable loss." A stronger definition would require that
   removing the forgotten structure from the richer system creates an
   obstruction in the richer system. This would directly test the causal claim
   (forgotten structure is what resolves the richer global section) rather than
   a proxy.

2. **AC4 and non-binary variables.** AC4 requires local satisfiability over
   binary variables. For Arrow's impossibility (which requires ranked variables),
   local satisfiability has a different meaning. T26 cannot currently check AC4
   for Arrow. This is noted as a future extension.

3. **Composition.** T31 does not test whether two PO1 instances can be composed
   (stacked forgetful functors). Composition would require the T26 morphism
   composition laws, which are not yet proved.

---

## Artifacts

- `models/po1_admissibility_conditions.py` — conditions, checker, audit runner
- `models/run_t31.py` — JSON runner
- `tests/test_po1_admissibility_conditions.py` — 27 tests, all passing
- `tests/T31-po1-admissibility-conditions.md` — test specification
- `results/po1-admissibility-conditions-v0.1.json` — machine-readable results
- `results/po1-admissibility-conditions-v0.1-results.md` — results summary
- `claims/PO1-projection-obstruction-schema.md` — updated claim
