# T585: Landauer Physical Capability Gate

## Target Claims

- CapabilityContract v1 can be instantiated in a genuine physical system with
  source-derived states, operations, resources, costs, records, access, and a
  physical quotient.
- The T584 surviving representation/gauge/coarse-graining quotient remains
  nontrivial in that system.

## Setup

Use a one-bit memory cell coupled to a thermal bath and work store. The source
law is a Landauer-style reset cost: minimum reset work is represented in
normalized `kBT ln 2` units as the binary entropy of the memory state.

The fixed context declares:

- source theory: one-bit memory erasure;
- region: one memory cell;
- observer/access: local record distribution, readout, thermal bath
  temperature, and work store;
- tasks: erase to a standard record and certify record stability;
- operations: Landauer reset and stability readout;
- budget: fixed work, time, communication, memory, and error bounds;
- quotient: unit representation and bit-label gauge equivalence.

## Success Criteria

- Known, biased, and max-entropy bit states receive law-derived reset costs.
- The fixed work budget yields a nontrivial physical capability relation.
- Unit representation, bit-label gauge, and irrelevant metadata
  coarse-graining preserve the native capability envelope.
- Access, resource/budget, and hidden-state overreads are classified as
  completions rather than capability or temporal claims.

## Failure Criteria

- Equivalent unit or bit-label representations change the capability envelope.
- The result depends on display labels or sensor metadata declared irrelevant.
- A changed access profile, changed work budget, or hidden entropy difference
  is counted as an intrinsic capability result.
- The fixture is used to claim time, temporal order, issuance, a new source
  law, or a claim-ledger movement.

## Known Physics Constraints

The model uses only a bounded Landauer-style erasure cost as source input. It
does not derive thermodynamics, physical time, or irreversible temporal order.

## Contribution Needed

Run `python -m models.t585_landauer_physical_capability_gate --write-results`
and the focused unit test before using the result as a source-owned input to
the record-capability-order burden.
