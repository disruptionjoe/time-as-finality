# T145: Physical Record Deletion Fixed-Accounting Screen

## Route

Thermodynamic arrow of time.

## Question

After T142 and T144 isolate `physical_record_deletion` as the only plausible
H7 arrow-bearing reverse class, does any current fixture still support a
physical-arrow reading when the absorber data are fixed?

The fixed data are:

- free-energy / erased-bit floor;
- blank-capacity change;
- sink or exported-history state;
- observer boundary;
- provenance / authority state;
- source-copy status; and
- reversible-control access.

## Motivation

T142 left one non-arrow residue: same one-bit blind-reset cost can coexist
with different D1 topology. T144 then warned that "definalization" must name
its reverse-edge class. T145 asks whether the fixed-erasure-floor residue is
actually H7 evidence or only future-operation/topology residue.

## Setup

Audit six finite fixtures:

1. same-chain copy deletion versus branch-spread copy deletion at the same
   one-bit blind-reset floor;
2. correlated uncopy versus blind reset;
3. one-bit versus two-bit blind reset;
4. hidden sink/exported-history control;
5. observer access revocation; and
6. authority/provenance revocation.

The H7 upgrade gate is intentionally narrow. A fixture can upgrade H7 only if:

```text
reverse_edge_class = physical_record_deletion
absorber vector matched
task-natural future-operation split present
reverse_status = constructor_impossible_after_full_accounting
```

## Success Criteria

- The same-floor branch-topology fixture is preserved as a capability split
  but not as arrow evidence.
- Correlated uncopy versus blind reset fails fixed accounting because
  reversible-control and erasure-work data differ.
- Sink/export, access-boundary, and provenance/governance variants are
  rejected by their proper absorber class.
- No current fixture clears the H7 physical-arrow upgrade gate.

## Failure Criteria

- A D1 topology split at fixed erasure floor is silently promoted to a
  thermodynamic arrow.
- Access or provenance loss is treated as physical record deletion.
- A fixture with changed reversible-control, sink, or free-energy data is
  treated as fixed-accounting evidence.

## Claim Impact

H7 is narrowed again. Fixed-accounting D1 topology can matter for future
operation availability, but that supports a capability/topology audit, not a
thermodynamic-arrow derivation. The missing object is still a substrate-native
physical deletion reverse that remains impossible after full absorber
accounting.

## Reproduction

```bash
python -m unittest tests.test_physical_record_deletion_fixed_accounting -v
python -m models.run_t145
```
