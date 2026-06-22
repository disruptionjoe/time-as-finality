# T179: Fixed-Accounting Capability Topology

## Route

Thermodynamic arrow of time, with mathematical-machinery pressure.

## Target Claims

- [H7: Finality-Induced Direction](../claims/H7-finality-induced-direction.md)
- [T145: Physical Record Deletion Fixed-Accounting Screen](T145-physical-record-deletion-fixed-accounting.md)
- [T129: Future Capability Preservation Audit](T129-future-capability-preservation-audit.md)

## Question

Can the one T145 survivor be preserved as a useful formal object without
letting it reopen H7 as physical-arrow evidence?

## Motivation

T145 found a real but demoted split:

```text
same blind-reset accounting + different branch topology
  -> different future branch-failure capability
```

That should not be lost. It says record topology can be part of a capability
kernel even when thermodynamic deletion accounting is fixed. But it should not
be promoted into a thermodynamic-arrow claim, because the deletion reverse is
still ordinary erasure accounting.

T179 turns the split into a theorem target:

```text
fixed absorber vector + topology profile -> future capability
```

and keeps a separate, stricter H7 reinstatement gate:

```text
physical_record_deletion
+ constructor_impossible_after_full_accounting
```

## Setup

Audit five finite cases:

1. `same_accounting_branch_survival_split`
2. `same_accounting_same_topology_control`
3. `changed_erasure_floor_absorber_control`
4. `provenance_loss_non_deletion_control`
5. `constructor_impossible_positive_control`

Track:

- absorber-vector equality;
- topology-profile equality;
- future-task availability;
- reverse-edge class; and
- reverse status.

## Success Criteria

- The T145 branch-topology survivor is classified as capability/topology
  residue.
- Holding topology fixed removes the future-capability split.
- Changing erased bits or free-energy floor is absorbed, not counted as fixed
  accounting.
- Provenance or authority loss is separated from physical record deletion.
- A synthetic constructor-impossible case is admitted only as an H7
  reinstatement positive control, not as a current result.

## Failure Criteria

- Fixed-accounting topology residue is promoted as a thermodynamic arrow.
- Thermodynamic, boundary, provenance, or control changes are counted as
  topology residue.
- The H7 reinstatement gate lacks a positive control.

## Claim Impact

H7 remains `weakened_conditional`. T179 preserves a positive formal target:
minimal topology data for future-operation capability at fixed absorber
accounting.

The next useful theorem is not:

```text
branch topology implies time's arrow
```

but:

```text
for branch-failure tasks, branch_support is the minimal record-topology
coordinate that restores capability sufficiency once thermodynamic and control
accounting are fixed.
```

## Reproduction

```bash
python -m unittest tests.test_fixed_accounting_capability_topology -v
python -m models.run_t179
```
