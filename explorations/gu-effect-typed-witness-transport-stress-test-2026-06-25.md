---
title: "GU Effect-Typed Witness Transport Stress Test"
status: exploration
doc_type: cross_repo_stress_test
updated_at: "2026-06-25"
source_repos:
  - "../../gu-formalization"
  - "../../temporal-issuance"
verdict: "USE_GU_AS_HOSTILE_TESTBED_NOT_TAF_CLAIM_PROMOTION"
---

# GU Effect-Typed Witness Transport Stress Test

## Purpose

Preserve the Time as Finality side of the GU / Temporal Issuance bridge.

GU should not import Time as Finality as a physics proof. Time as Finality
should not import GU as evidence that finality generates source dynamics. The
useful connection is narrower: GU is a hard stress test for TaF transport,
projection, finality, and loss machinery.

## Transfer From Time as Finality To GU

Time as Finality gives GU reusable formal discipline:

- `InvariantPreservingTransformation`: named invariants must be declared and
  checked across maps.
- `TypedTransportNetwork`: paths can accumulate different forgotten structure.
- `RecordFinality`: finality is a record/certificate state, not full truth.
- `Projection/obstruction discipline`: visible readout can lose capability.
- Fault/finality ledgers: claim status should not outrun its dependencies.

This helps GU by forcing each blocker to say whether it is about source
construction, projection/readout, finality/certification, or quotient loss.

## Transfer From GU Back To Time as Finality

GU provides a hostile geometry-facing test for TaF abstractions:

| TaF object | GU stressor | why it matters |
|---|---|---|
| `InvariantPreservingTransformation` | VZ actual operator certificate, RS quotient, QFT Gram positivity | Tests whether declared invariants survive real analytic and algebraic maps. |
| `TypedTransportNetwork` | multiple proof paths through selector, quotient, operator, projection, and loop states | Tests path-dependent forgotten-structure outside toy graph cases. |
| `RecordFinality` | actual operator certificates and claim-DAG finality | Tests proof-carrying finality without confusing certificate status with theorem status. |
| `LossKernel` | H-linear quotienting, finite-mode truncation, gauge/ghost loss | Tests whether forgotten structure has downstream mathematical force. |
| observer-finality layer | CHSH/readout gates from GU-derived states and admissible observables | Tests whether observer-finality can remain local and domain-relative under real physics-facing constraints. |

## The Shared Candidate Object

```text
EffectTypedWitnessTransport =
(
  GU_stage,
  source_or_domain_object,
  effect_tags,
  preserved_invariants,
  lost_structure,
  projection_or_readout_map,
  record_or_certificate_state,
  absorber_or_fault_model,
  closure_gate
)
```

The effect tags are:

```text
Issue[S]
Project[O]
Finalize[R]
Lose[K]
```

TaF should treat this as a stress fixture for its own machinery, not as a new
TaF claim.

## No-Claim-Movement Rule

This note does not move C1, D1, H7, or any GU claim.

The only admissible next result is one of:

- TaF machinery classifies a GU blocker more clearly.
- GU exposes a missing TaF transport/finality/loss obligation.
- The bridge is absorbed as translation residue.
- A finite fixture is proposed with explicit failure conditions.

## Links To Preserve

- GU crosswalk note:
  `../../gu-formalization/explorations/time-as-finality-crosswalk/effect-typed-witness-transport-bidirectional-crosswalk-2026-06-25.md`
- GU five-goal synthesis:
  `../../gu-formalization/explorations/hourly-cycle1-effect-typed-witness-transport-five-goal-synthesis-2026-06-25.md`
- Temporal Issuance note:
  `../../temporal-issuance/explorations/E075-gu-effect-typed-witness-transport-2026-06-25.md`
- TaF temporal issuance bridge:
  `temporal-issuance-bridge-v0.1.md`
- TaF proof-carrying finality open problem:
  `../open-problems/proof-carrying-record-finality.md`
