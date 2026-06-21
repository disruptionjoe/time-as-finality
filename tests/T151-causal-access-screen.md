# T151: Causal-Access Screen

## Route

Spacetime reconstruction / black holes / causal access.

## Target Claims

- [B1: Black Holes As Finality-Domain Boundaries](../claims/B1-black-holes-finality-boundaries.md)
- [S1: Spacetime As Consensus Envelope](../claims/S1-spacetime-consensus-envelope.md)
- [R1: Relativity And No Global Commit Order](../claims/R1-relativity-no-global-commit-order.md)

## Question

Does finality-boundary language add anything beyond ordinary causal record
reachability once the observer, source event, channel type, and boundary
permeability are declared?

## Motivation

B1 and S1 are underdeveloped compared with the Q1 and H7 branches. Their main
risk is rhetorical inflation: treating a horizon or boundary as if it were a
new finality mechanism when the safe content is only causal accessibility.

T151 installs a finite absorber before future horizon or spacetime language can
be promoted.

## Setup

Represent a causal record system with:

```text
RecordEvent
RecordChannel
ObserverProfile
CausalRecordSystem
```

The access capability is:

```text
Can record tokens from source event e reach observer O through declared
classical channels?
```

The screen separately tracks:

- direct local participation;
- received remote signal records;
- local interior access;
- exterior direct classical access;
- encoded or indirect nonclassical channels;
- boundary direction and transformed record character.

## Controls

1. `remote_signal_control`
   A remote source sends a classical signal record to an observer. This is
   causal record access without direct participation.
2. `horizon_classical_export_cap`
   An interior event is locally accessible to an infalling observer but lacks an
   outward classical path to the exterior observer.
3. `encoded_indirect_horizon_channel`
   The direct classical record is inaccessible, but an encoded/indirect channel
   is declared. This blocks all-information overclaims.
4. `soft_boundary_permeability`
   A heliopause-like boundary admits bidirectional classical exchange with
   transformed record character. This is a permeability parameter, not a
   horizon-like cap.

## Success Criteria

- Remote observation is accepted as received causal record access.
- Horizon language is classified as causal-reachability bookkeeping for direct
  classical records.
- All-information black-hole claims are rejected unless the native physics is
  typed.
- Soft boundaries are parameterized instead of collapsed into horizon language.

## Failure Criteria

- The screen denies ordinary astronomical observation.
- A direct classical horizon boundary is treated as new TaF evidence after the
  causal graph is fixed.
- Encoded, holographic, or quantum information claims are judged by the
  classical screen alone.
- Boundary permeability is reduced to a binary accessible/inaccessible label.

## Claim Impact

B1 should be weakened:

```text
For direct classical records, a horizon is a causal-access boundary: exterior
observers can use only records connected to them by declared classical channels.
This is translation residue under ordinary causal reachability, not a new
black-hole or spacetime mechanism.
```

S1 must carry causal-access maps in addition to local-order compatibility. R1
must keep remote record access distinct from direct participation.

## Reproduction

```bash
python -m unittest tests.test_causal_access_screen -v
python -m models.run_t151
```
