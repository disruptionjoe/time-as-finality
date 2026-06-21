# T152: Metastable-Record Deletion Screen

## Route

Thermodynamic arrow of time.

## Target Claims

- [H7: Finality-Induced Direction](../claims/H7-finality-induced-direction.md)
- [Arrow of Time as Constructor Theorem](../open-problems/arrow-of-time-as-constructor-theorem.md)

## Question

Can the remaining H7 physical-deletion gate be cleared by treating stable
records as finite metastable substrates rather than abstract record tokens?

## Motivation

T145 and T148 leave H7 with a narrow reinstatement condition: find a physically
typed `physical_record_deletion` substrate whose reverse remains
constructor-impossible after free-energy, capacity, sink, observer-boundary,
provenance, source-copy, and reversible-control data are matched.

The most natural physical candidate is metastability. A record may persist
because a finite barrier makes deletion or spontaneous flipping unlikely. T152
asks whether that supplies impossible deletion, or only ordinary
lifetime/barrier/resource accounting.

## Setup

Audit five finite fixtures:

1. `finite_barrier_lifetime_split`
   High and low finite barriers give different retention capability over the
   same horizon.
2. `same_barrier_branch_topology_split`
   The T145 same-accounting topology residue is instantiated with the same
   finite metastable barrier on both sides.
3. `infinite_barrier_constructor_lock`
   An ideal infinite barrier makes deletion impossible by stipulation.
4. `control_window_denial`
   The substrate is finite, but deletion control is unavailable to the
   observer.
5. `hidden_cold_reservoir_or_engineered_barrier`
   Apparent retention improvement comes from changed reservoir or barrier
   engineering data.

The upgrade gate is intentionally narrow:

```text
reverse_edge_class = physical_record_deletion
absorber vector matched
finite barriers
task-natural future-operation split
reverse_status = constructor_impossible_after_full_accounting
```

## Success Criteria

- Finite barrier lifetime splits are absorbed by kinetic barrier accounting.
- Same-barrier topology splits are preserved as future-operation residue but
  not as H7 arrow evidence.
- Infinite barriers classify as constructor idealizations, not finite physical
  substrates.
- Control-denial cases classify as boundary/control accounting.
- Reservoir or engineered-barrier cases classify as changed absorber data.
- No current finite metastable fixture clears the H7 physical-arrow gate.

## Failure Criteria

- A finite nonzero-rate barrier is treated as constructor impossibility.
- Infinite-barrier idealization is promoted as a physical substrate result.
- Observer-inaccessible deletion is confused with substrate-native
  impossibility.
- Barrier, reservoir, or lifetime parameters are hidden from the absorber
  vector.

## Claim Impact

H7 remains `weakened_conditional`.

Add this sharpening:

```text
Metastable records can be long-lived without making deletion impossible.
Finite barriers are kinetic/resource data; infinite barriers and denied
controls are constructor or boundary stipulations. A matched finite-barrier D1
topology split remains future-operation residue, not thermodynamic-arrow
evidence.
```

## Reproduction

```bash
python -m unittest tests.test_metastable_record_deletion_screen -v
python -m models.run_t152
```
