# T168: H7 Sector-Restriction Screen

## Route

Thermodynamic arrow of time, with a mathematical-machinery guardrail for exact
sector and gauge language.

## Target Claims

- [H7: Finality-Induced Direction](../claims/H7-finality-induced-direction.md)
- [T160: H7 Substrate-Family Screen](T160-h7-substrate-family-screen.md)
- [H7 Physical-Deletion Substrate Handoff](../open-problems/h7-physical-deletion-substrate-handoff.md)

## Question

Can the remaining H7 physical-deletion gate be cleared by claiming that exact
sector, superselection, symmetry, or gauge restrictions make record deletion
impossible?

## Motivation

T160 treats exact sector and gauge restrictions as null by default unless they
admit a finite operational substrate where physical deletion remains
constructor-impossible after matched accounting. Without an executable screen,
future work can still smuggle in the same failure under different names:
charge conservation, gauge redundancy, exact superselection, or finite
symmetry protection.

T168 tests the finite proof-obligation shape. It is not a theorem of gauge
theory.

## Setup

Audit six fixtures:

1. `local_sector_delete_forbidden_without_reservoir`
   Deletion is forbidden only because the local operation class excludes a
   compensating conserved quantity.
2. `compensating_reservoir_restores_deletion`
   A reservoir or sink carries the conserved quantity, turning the obstruction
   into ordinary accounting.
3. `gauge_relabeling_record_loss`
   The apparent record change is pure representative relabeling with no
   gauge-invariant physical deletion.
4. `exact_superselection_constructor_lock`
   An exact sector ban forbids deletion by ideal stipulation rather than a
   finite substrate-native obstruction.
5. `finite_symmetry_breaking_control`
   A finite enforcement mechanism blocks deletion only until the finite
   symmetry-breaking control or leakage path is admitted.
6. `matched_sector_branch_topology_residue`
   A T145-style branch topology split survives matched sector accounting but
   deletion remains finite-control possible.

The upgrade gate is narrow:

```text
reverse_edge_class = physical_record_deletion
absorber vector matched
finite operational substrate
gauge-invariant difference
task-natural future-operation split
reverse_status = constructor_impossible_after_full_accounting
```

## Success Criteria

- Local sector-only deletion bans classify as operation-class stipulations.
- Compensating reservoirs absorb apparent sector obstruction.
- Gauge relabelings classify as non-deletion.
- Exact sector bans classify as ideal restrictions, not finite substrate
  results.
- Finite symmetry enforcement classifies as control/resource accounting.
- Matched branch topology remains capability residue, not arrow evidence.
- No current sector/gauge fixture clears the H7 physical-arrow gate.

## Failure Criteria

- A pure gauge representative change is treated as physical record deletion.
- Charge or sector conservation is promoted without reservoir/accounting data.
- Exact superselection is promoted without a finite operational substrate.
- Finite symmetry protection is treated as constructor impossibility after
  allowing the relevant finite control class.
- A matched future-operation split is promoted as thermodynamic-arrow evidence
  while the deletion reverse remains finite-control possible.

## Claim Impact

H7 remains `weakened_conditional`.

Add this sharpening:

```text
Exact sector and gauge restriction proposals are null by default. They reopen
H7 only with a finite operational substrate, a gauge-invariant deletion
distinction, matched conserved-quantity/reservoir/control data, and a physical
deletion reverse that remains constructor-impossible after that accounting.
```

## Reproduction

```bash
python -m unittest tests.test_h7_sector_restriction_screen -v
python -m models.run_t168
```
