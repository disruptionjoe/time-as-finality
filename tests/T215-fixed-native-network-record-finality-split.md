# T215: Fixed Native Network Record-Finality Split

## Target Claims

- T206 request for fixed-native-state finality witnesses
- Capability Projection
- Time as Finality record capability

## Origin

T206 absorbed timing summaries into native network theory. The live route is no
longer another transport metric; it is a different capability at fixed native
transport state.

## Formal Target

Hold the native network fixed:

```text
same incidence
same capacities
same demand
same delay law
same C_flow
```

and vary only the record policy:

```text
append-only history with challenge window
overwrite/no-history policy
```

## Setup / Fixtures

Use the executable disjoint network. Define capability:

```text
Cap(Y) = (C_flow(Y), record_reconstructable(policy))
```

## Positive Control

The two policies have the same `C_flow` but different record reconstructability:

```text
(8/3, True)
(8/3, False)
```

## Negative Control

If the capability under test is only `C_flow`, the pair is null.

## Absorber Pass

Network-flow theory owns the first coordinate. Record/provenance/ledger theory
owns the second coordinate. The split is not WBE residue; it is a typed
record-finality capability layered on top of the same transport state.

## Results

The executable fixture finds a fixed-network-state split for record
reconstructability.

## Verdict: promoted

Promoted as a better next research route: fixed native transport state plus a
declared record/finality capability.

## Falsification Conditions

Demote if record policy is declared outside the admissible source state, or if
the task family does not require reconstruction/audit capability.

## Next Step

T216 grants provenance and ledger theory their native absorbers.
