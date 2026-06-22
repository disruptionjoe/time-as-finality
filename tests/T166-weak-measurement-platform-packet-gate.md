# T166: Weak-Measurement Platform-Packet Gate

## Route

Quantum measurement / classical records.

## Target Claims

- [Q1C: Weak-Measurement Discriminator Gate](../claims/Q1C-weak-measurement-discriminator-gate.md)
- [Q1: Quantum Under-Finalization](../claims/Q1-quantum-under-finalization.md)

## Question

Once Q1C is externally bottlenecked, what minimum pre-analysis packet must a
named platform supply before the repo should spend any more effort on it?

## Motivation

T146, T149, T150, T158, and N9 have already stripped away the internal weak-
measurement loopholes. The remaining failure mode is softer: a future platform
proposal can still look like progress while never freezing the ordinary
record, verdict rule, audit data burden, or enlarged-instrument back-
projection needed to test it honestly.

T166 turns the current Q1C handoff into an executable intake gate.

## Setup

Audit five packet classes:

1. `admissible_extra_environment_packet`
   Freezes the full ordinary event-level record, auxiliary channel, live
   architecture class, independently typed TaF axis, verdict map, support
   floor, loss rule, null controls, and event-level audit burden.
2. `enlarged_instrument_missing_back_projection`
   Declares an enlarged instrument but omits the eventwise back-projection to
   the full ordinary standard record.
3. `same_instrument_packet`
   Tries to reopen Q1C without naming either live architecture class.
4. `coarse_record_packet`
   Freezes only a coarse ordinary record rather than the full event-level log.
5. `scaffold_only_packet`
   Freezes the prose fields but refuses the event-level audit packet needed to
   run the downstream screens.

## Success Criteria

- Q1C proposals remain dormant by default unless they first clear a complete
  packet-intake contract.
- Enlarged-instrument packets must declare both the preserved full-record
  target and its eventwise back-projection.
- Event-level audit data is required at intake, not treated as an optional
  later detail.
- The current frontier remains inadmissible.

## Failure Criteria

- A platform sketch counts without freezing the full ordinary record.
- Same-instrument proposals count without naming extra-environment structure
  or explicit instrument enlargement.
- Enlarged-instrument packets count without a back-projection to the full
  standard record.
- A scaffold-only packet with no event-level audit burden is treated as live.

## Claim Impact

Q1C remains dormant.

Add this sharpening:

```text
Q1C reinstatement now has two stages. A platform must first clear the T166
packet gate, then clear the T149/T150/T158 event-level screens.
```

## Reproduction

```bash
python -m unittest tests.test_weak_measurement_platform_packet_gate -v
python -m models.run_t166
```
