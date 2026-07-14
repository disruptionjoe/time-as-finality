# T558: Sheaf Obstruction Transport Source-Law Packet

## Target Claims

S1, TAF11, TAF4, TAF8, T557, T556, T548, T541.

## Setup

Consume T557 as the frozen source-family contract:

- selected family: `sheaf_obstruction_transport_family`;
- source variables: finite event covers, local finality sections, restriction
  morphisms, settlement obstruction witnesses, transport consistency squares,
  and allowed refinement steps;
- mature absorbers: ordinary sheaf gluing completion, resource transport
  monotone, consensus state-machine, and record-provenance completion;
- falsifiers: all obstructions glue under declared restrictions, transport
  square commutes after mature absorbers, same variables realize the target by
  relabeling, and hidden target/cross-repo rule required.

Test the selected family without target labels, cross-repo truth, Observerse
replay, APRD replay, TAF4 movement, TAF8 execution, or claim/canon/public
posture movement.

## Success Criteria

- T557 is consumed as source authority.
- The source variables, mature absorbers, and falsifiers remain unchanged.
- Each mature absorber receives a control case.
- Each declared falsifier is triggered by at least one control case.
- Observerse replay, APRD replay, target import, and relabel-only target
  realization reject.
- A formal noncommuting transport fixture may remain only as formal residue.
- No source law, TAF4, TAF8, claim-ledger, Canon Index, canon-verdict,
  public-posture, North Star, external-publication, or cross-repo movement is
  made.

## Failure Criteria

T558 fails if:

- the T557 contract changes;
- any mature absorber is skipped;
- any T557 falsifier is untested;
- a spent route or target/cross-repo import is admitted;
- a formal residue is treated as source-law evidence;
- TAF4, TAF8, external publication, or cross-repo truth is moved.

## Known Physics Constraints

No physics, geometry, causal-set, Lorentzian, quantum, source-law, or
shadow-protection claim is earned by this packet.

## Implementation Result

Status: implemented.

T558 consumes T557 as preflight authority, exercises all four mature absorbers,
triggers all four declared falsifiers, rejects Observerse replay, APRD replay,
hidden target/cross-repo import, and relabel-only target realization, and leaves
exactly one formal noncommuting transport fixture as residue. Because that
residue has no domain-native payload, it is not source-law evidence.

The next burden is `t559_domain_native_sheaf_transport_packet_burden_gate`: a
future packet must supply a domain-native sheaf obstruction transport payload
with the same frozen variables and a noncommuting transport square that survives
the four mature absorbers.

## Run Command

```bash
python -m models.t558_sheaf_obstruction_transport_source_law_packet --write-results
python -m unittest tests.test_t558_sheaf_obstruction_transport_source_law_packet -v
```

## Boundary

T558 is an absorber/falsifier packet. It does not establish a source law, move
TAF4, execute TAF8, or change claim/canon/public posture.
