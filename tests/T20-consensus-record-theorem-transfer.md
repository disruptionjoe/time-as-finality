# T20: Consensus-Record Theorem Transfer

## Target Claims

- [A1: Distributed Systems Finality Analogy](../claims/A1-distributed-systems-finality-analogy.md)
- [D1: Physical Finality Definition](../claims/D1-physical-finality-definition.md)
- [T13: Finality Sheaf Cohomology](T13-finality-sheaf-cohomology.md)
- [T17: Consensus Finality Crosswalk](T17-consensus-finality-crosswalk.md)

## Origin

The v2 persona sprint found that distributed computing and physical record
formation are the strongest cross-persona convergence cluster: many lenses
arrived at the same structural question in different notation.

T20 tests the stronger version of the analogy:

```text
Do theorem structures transfer, or only vocabulary?
```

## Setup

Build a typed dictionary from distributed consensus into physical record
finality:

- process local state -> observer-local finality domain;
- message/certificate -> record fragment or environmental witness;
- quorum intersection -> redundant-holder overlap;
- fork/conflicting commit -> incompatible finality sections;
- safety -> no contradictory stabilized records;
- liveness -> record-amplification progress;
- adversarial delay -> bounded causal access or decoherence lag.

Then attempt one theorem transfer: quorum-intersection safety.

Source theorem:

```text
In a quorum system with 2q > n and locally consistent processes,
two conflicting commit certificates cannot both be valid.
```

Target theorem:

```text
In a physical record system with redundant-holder threshold 2q > n
and locally consistent record fragments, two incompatible classical
records cannot both be finalized.
```

## Success Criteria

- The dictionary is typed and includes caveats.
- The source and target theorem use the same proof steps.
- The record-side certificates produce D1 profiles.
- A weak-quorum boundary case is detected.
- A sheaf-style contextual boundary case is detected, showing that quorum
  safety does not prove global-section existence.
- The result preserves the guardrail that physics is not literally a
  distributed protocol.

## Failure Criteria

- The mapping is only metaphorical and does not preserve proof steps.
- The theorem transfer depends on engineered protocol concepts that have no
  physical-record analogue.
- The boundary cases are not detected.
- The result claims global objectivity from quorum safety alone.

## Status

Implemented as T20 v0.1.

## Reproduction

```bash
python -m unittest tests.test_consensus_record_theorem_transfer -v
python -m models.run_t20
```

## T21 Follow-On

[T21](T21-bell-contextuality-finality.md) implements the contextual boundary
identified by T20. Quorum safety can transfer from distributed systems into
physical-record finality, but Bell/CHSH-style contextuality shows that local
finality sections may still fail to glue into a global section.

## T23 Follow-On

[T23](T23-invariant-preserving-transformations.md) reuses the T20 theorem
transfer as a homology case in the IPT kernel. It preserves holder count,
quorum threshold, quorum-intersection safety, and conflict exclusion across
the consensus-record map.

T23 also reuses T20's weak-quorum boundary as an obstruction witness. When
`n = 4` and `q = 2`, `2q > n` is false, so quorum-intersection safety is not
transported.
