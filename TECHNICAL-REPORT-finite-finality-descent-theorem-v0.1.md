# Technical Report: Finite Finality Descent Theorem v0.1

## Summary

T54 turns the T53 observer-colimit boundary into a finite theorem schema.

T53 showed:

```text
valid colimit consistency != canonical reconstruction
```

T54 adds a canonical quotient-union construction and a finite condition basis
for when observer-local FinaliEvent structures determine a unique, AM-valid
global event-finality structure.

Best-supported verdict:

```text
H2 and H3 supported.
H0, H4, and H5 refuted.
H1 partially supported.
```

Full sheaf or categorical descent machinery is not required for the finite
witness family tested here.

## Core Result

Finite Finality Descent Theorem v0.1:

```text
Given finite observer-local FinaliEvent data with total single-valued event
identity maps, overlap witnesses for cross-observer identifications,
compatible source and target records, and agreeing finality-axis profiles, the
canonical quotient-union construction produces a unique global FinaliEvent
structure.

If its dependency relation is a partial order and AM holds, the global
temporal partial order is reconstructible from finality-axis magnitudes.

If any descent condition fails, the failure is classified as nondefinable,
underdetermined, conflicting, or AM-invalid.
```

## Finite Descent Conditions

| ID | Condition |
| --- | --- |
| C1 | Event identity maps are total and single-valued. |
| C2 | Cross-observer identified events have overlap witnesses. |
| C3 | Source records merge without explicit contradiction. |
| C4 | Target records merge without explicit contradiction. |
| C5 | Identified events agree on finality-axis profiles. |
| C6 | The quotient-union dependency order is a valid partial order. |
| C7 | Axis Monotonicity holds on the reconstructed global structure. |

## Algorithm

The executable completion algorithm:

1. Collects observer-local events.
2. Checks that every local event has exactly one identity map.
3. Rejects missing identities as underdetermined.
4. Groups local events into global event classes by identity map.
5. Requires overlap witnesses for cross-observer identifications.
6. Merges source and target records by union.
7. Rejects explicit record contradictions such as `r_x` and `not:r_x`.
8. Rejects finality-axis profile disagreement.
9. Computes the record-dependency partial order.
10. Tests Axis Monotonicity on the reconstructed global structure.
11. Classifies the result.

## Reclassification of Prior Tests

| Prior case | T54 classification | Reason |
| --- | --- | --- |
| T51 phantom incomparability repair | `canonical` | Identity maps, overlap, records, profiles, partial order, and AM all hold. |
| T52 symmetric reconstruction | `canonical` | Complementary observer records quotient-union into the full AM-valid reference order. |
| T53 ambiguous identity | `underdetermined` | Local event identities are not fixed, so the quotient is not canonical. |

## Counterexamples

| Counterexample | Classification | Failed condition |
| --- | --- | --- |
| `CE_missing_event_identity` | `underdetermined` | C1 |
| `CE_insufficient_overlap` | `underdetermined` | C2 |
| `CE_source_record_conflict` | `conflicting` | C3 |
| `CE_target_record_conflict` | `conflicting` | C4 |
| `CE_axis_profile_conflict` | `conflicting` | C5 |
| `CE_hidden_record_ambiguity` | `underdetermined` | hidden repair authority is extra data |
| `CE_nondefinable_map` | `nondefinable` | C1 / definability |
| `CE_am_violation` | `am_invalid` | C7 |

## Hypothesis Evaluation

### H0

T53 boundary cases cannot be compressed into a finite theorem basis.

Status: refuted.

Evidence: all T51, T52, T53, and counterexample classifications match the
finite condition basis.

### H1

Event identity plus record compatibility is sufficient for unique completion.

Status: partially supported.

Evidence: identity plus record compatibility is enough for a unique
quotient-union partial order when maps and records agree. It is not enough for
AM-valid temporal reconstruction, which requires C7.

### H2

AM-compatible axis profiles are additionally required for temporal
reconstruction.

Status: supported.

Evidence: `CE_am_violation` has a unique valid partial-order completion but
fails AM.

### H3

A finite descent theorem classifies the T51-T53 cases.

Status: supported.

Evidence:

```text
T51 = canonical
T52 = canonical
T53 = underdetermined
```

### H4

Uniqueness is decidable only by brute-force completion enumeration.

Status: refuted.

Evidence: the quotient-union algorithm classifies all witnesses without
enumerating completions.

### H5

Full sheaf/categorical descent machinery is required now.

Status: refuted.

Evidence: finite identity, overlap, record, profile, partial-order, and AM
checks suffice for the tested witness family.

## What T54 Adds

T54 makes the next structural boundary precise:

```text
colimit consistency
  is weaker than
canonical completion
  is weaker than
AM-valid temporal reconstruction
```

It also gives the repo a reusable classification layer:

```text
canonical
underdetermined
conflicting
nondefinable
AM-invalid
```

## Repository Recommendation

The repo should treat canonical observer-relative temporal reconstruction as:

```text
finite descent conditions + Axis Monotonicity
```

For now, this should remain a finite theorem. Full sheaf/descent language can
be postponed until a future test produces a finite case that cannot be
classified by quotient-union descent data.

## Next Theorem Target

The next substantial target is not another colimit test. It is a conflict
extension:

```text
FinaliEvent structures with mutually exclusive event alternatives.
```

T48 noted that the current NPW event-structure compatibility uses an empty
conflict relation. After T54, the natural next boundary is to add conflict and
ask whether descent still yields canonical histories when some events are
incompatible rather than merely incomparable.
