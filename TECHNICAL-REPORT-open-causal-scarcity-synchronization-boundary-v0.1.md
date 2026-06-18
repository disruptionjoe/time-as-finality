# Technical Report: Open Causal Scarcity And Closed Synchronization Boundary (T46)

**Version:** v0.1
**Date:** 2026-06-18
**Status:** Implemented

---

## Summary

T46 asks whether the repo can formally distinguish two scarcity regimes for
observer-accessible records:

1. **Open causal scarcity:** a generated record propagates through finite paths,
   so first access is determined by causal proximity to the source.
2. **Closed synchronization scarcity:** a membership-bounded system imposes an
   internal commit order using synchronization rules, so authoritative access is
   determined by participation in the closed substrate.

Result: the distinction is executable in a finite `RecordAccessSystem`.

Best-supported hypothesis: **H3**. Open causal scarcity and closed
synchronization scarcity are both instances of a common finite record-access
frontier structure, but they use different scarcity axes.

The candidate named claim **CS1** should not be promoted to a new claim file
yet. T46 supports it as a finite principle, but more hostile cases are needed.

---

## External Anchors

T46 uses real systems only as anchors for finite abstraction.

- Google describes Spanner as a globally distributed database supporting
  externally consistent distributed transactions with TrueTime, a time API that
  exposes bounded clock uncertainty:
  <https://research.google.com/archive/spanner.html>
- Google Cloud describes external consistency in Spanner through commit
  timestamps and TrueTime uncertainty:
  <https://cloud.google.com/blog/products/databases/strict-serializability-and-external-consistency-in-spanner>
- NYSE/ICE colocation documents describe low-latency local and wide-area
  connectivity around the Mahwah liquidity center:
  <https://www.nyse.com/publicdocs/IGN_Colocation_Mahwah_Technical_Specs.pdf>

The executable model does not implement any of these systems.

---

## New Finite Object

T46 introduces:

```text
RecordAccessSystem
```

with:

- `RecordNode`;
- `PropagationEdge`;
- `RecordEvent`;
- optional `SynchronizationBoundary`;
- observer-specific access observations;
- open finality gradients;
- closed commit observations.

This object is a sidecar. It does not replace `D1RestrictionSystem`.

---

## Open Causal Scarcity Witness

The NYSE-style witness has one source and three observers:

```text
exchange_engine
  -> colocated_rack
  -> metro_pop
  -> remote_region
```

Finite delays:

| Observer | Arrival time |
| --- | ---: |
| colocated_rack | 1 |
| metro_pop | 75 |
| remote_region | 750 |

First-access order:

```text
colocated_rack, metro_pop, remote_region
```

Finding: first access follows finite path delay from the generating node. The
scarcity axis is causal proximity.

This is the T42 reconciliation/access-lag idea applied to actionable record
access.

---

## Closed Synchronization Boundary Witness

The Spanner-style witness has three members and one outside observer:

```text
west_replica
east_replica
central_replica
outside_client
```

The boundary has:

- member IDs;
- quorum requirement;
- bounded uncertainty;
- commit timestamp rule;
- commit wait.

Two transactions are configured so that the internal commit order is:

```text
tx_west, tx_east
```

but the outside raw arrival order is:

```text
tx_east, tx_west
```

The outside observer cannot reconstruct the internal commit order until commit
records have propagated outward. In the executable witness:

| Quantity | Value |
| --- | ---: |
| outside reconstruction time | 60 |
| latest internal visibility time | 25 |
| outside observer lag | 35 |
| synchronization cost total | 16 |

Finding: closed synchronization does not abolish propagation delay. It relocates
finality scarcity from proximity to membership plus synchronization rule.

---

## Boundary Comparison

| Regime | Scarcity axis | What determines first/authoritative access? |
| --- | --- | --- |
| Open causal system | causal proximity | path delay from generating node |
| Closed synchronized system | membership plus rule | boundary membership, quorum, timestamp, uncertainty |

The core distinction is:

```text
open system:
  proximity to source determines first access

closed system:
  membership in synchronized substrate determines authoritative order
```

The closed system still pays real finite costs:

- commit wait;
- bounded uncertainty;
- quorum delay;
- external propagation delay;
- membership boundary.

---

## Measurement Projection Boundary

T46 also records a conservative boundary table:

```text
richer pre-record structure Y_candidate
  -> measurement_or_finalization_projection
observer-accessible record layer X
```

Preserved structure:

- classical outcome label;
- stable pointer record;
- accessible correlation statistics;
- conservation-compatible coarse quantities;
- record-holder accessibility relation.

Forgotten structure:

- relative phase information;
- unmeasured counterfactual contexts;
- coherence not preserved in accessible records;
- environment entanglement not available to the observer.

Verdict: this is a candidate projection boundary only. It names AC5-like
forgotten structure, but T46 does not claim AC1-AC7 or a full measurement PO1
theorem.

This table does not derive a 14-dimensional layer, does not demote the Standard
Model to classical residue, and does not claim superluminal usable information.

---

## Hypothesis Verdicts

| Hypothesis | Verdict |
| --- | --- |
| H0 | rejected_for_finite_abstraction |
| H1 | supported |
| H2 | supported |
| H3 | best_supported |
| H4 | partially_supported |
| H5 | rejected_for_finite_access_distinction |

H0 is rejected at the finite-abstraction level because the executable model
separates open causal arrival from closed commit order.

H1 is supported: open causal scarcity is T42-style propagation/access lag.

H2 is supported: closed synchronization needs membership, quorum, timestamp,
and uncertainty data beyond raw propagation edges.

H3 is best supported: both regimes instantiate a common record-access frontier.

H4 is partially supported only as boundary language. Full PO1 status would need
a separate D1RestrictionSystem admissibility proof.

H5 is rejected for the finite distinction, but remains a guardrail against
physical overinterpretation.

---

## Theorem Earned

**Finite Record-Access Scarcity Theorem**

In the T46 `RecordAccessSystem` witnesses, open systems expose finality scarcity
as causal-proximity advantage, while closed synchronized systems relocate
scarcity to membership plus bounded commit rules. The closed system does not
abolish propagation delay; outside observers can reconstruct internal order
only after commit records propagate outward.

---

## Candidate Claim

Candidate **CS1: Causal Scarcity Boundary Principle**

Possible wording:

> Open record systems expose finality gradients through causal proximity to
> record-generating nodes. Closed synchronized systems can impose internal
> commit order across distributed nodes, but only by creating a membership
> boundary and paying synchronization costs. Such systems relocate finality
> scarcity from proximity to participation; they do not abolish causal
> propagation constraints.

Recommendation: keep CS1 as a candidate claim for now. Do not create a claim
file until hostile cases test whether the principle survives beyond the two
motivating witnesses.

---

## What T46 Does Not Claim

- It does not model actual NYSE market microstructure.
- It does not implement Google Spanner.
- It does not derive the speed of light.
- It does not explain relativity or time dilation.
- It does not prove a quantum measurement theorem.
- It does not assume `Y` is 14-dimensional.
- It does not claim that Standard Model physics is merely classical residue.
- It does not claim that closed systems escape causal propagation constraints.

---

## Recommendation

Add `RecordAccessSystem` as a sidecar formal object for R1/A1-facing work.

Use it whenever the repo needs to distinguish:

```text
record generation
record propagation
observer access
internal commit order
external reconstruction
measurement-like projection into records
```

The next useful hostile tests are:

- cross-exchange latency arbitrage;
- dark-pool reporting delays;
- public ledger mempools;
- read-replica databases with stale external observers;
- sensor fusion with trusted internal clocks and delayed public readout.

---

## Evidence

Executable files:

- `models/record_access_systems.py`
- `models/run_t46.py`
- `tests/test_record_access_systems.py`

Result artifacts:

- `results/open-causal-scarcity-synchronization-boundary-v0.1.json`
- `results/open-causal-scarcity-synchronization-boundary-v0.1-results.md`

Run:

```bash
python -m pytest tests/test_record_access_systems.py -q
python -m models.run_t46
```
