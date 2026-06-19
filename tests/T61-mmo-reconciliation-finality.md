# T61: MMO Reconciliation Finality

## Target Claims

- [A1: Distributed-Systems Finality Analogy](../claims/A1-distributed-systems-finality-analogy.md)
- [T37: Typed Transport Network](T37-typed-transport-network.md)
- [T42: Local Persistence And Reconciliation Split Audit](T42-local-persistence-reconciliation-split.md)
- [T46: Open Causal Scarcity And Closed Synchronization Boundary](T46-open-causal-scarcity-synchronization-boundary.md)
- [T55: Conflict-Enriched FinaliEvent Descent](T55-conflict-finalievent-descent.md)

## Purpose

T61 uses a finite MMO-style distributed simulation as a hostile engineered
domain for observer-relative finality. The goal is not metaphor. The goal is to
test whether TaF can distinguish:

- apparent local finality;
- authoritative event finality;
- predicted state;
- delayed reconciliation;
- rollback or correction;
- explicit conflict repair.

## Required Entities

The finite system contains:

- two clients;
- one edge replica / local cache;
- one authoritative simulation region;
- observer-specific local state views;
- propagation delays;
- predicted client actions;
- authoritative commits;
- rollback or correction;
- at least one incompatible event pair.

## Model Reuse

T61 must reuse existing machinery where possible:

- T46 `RecordAccessSystem` for propagation delays and authority membership;
- T37 `TypedTransportNetwork` and D1 morphisms for state movement;
- T55 conflict-enriched FinaliEvents for incompatible predictions;
- D1 profiles for observer-access support, holder redundancy, branch support,
  and reversal cost.

## Positive Witness

One client predicts an action locally. The authority later commits the same
action. The client has apparent local finality before authoritative event
finality, but reconciliation upgrades the local view without rollback.

Expected result:

```text
client apparent finality != authority event finality
authority commit matches prediction
no conflict
no rollback
```

## Failure Witness

Two clients predict incompatible claims over the same resource from stale local
views. The authority commits one branch and rejects the other. The losing local
prediction cannot be silently merged; it requires rollback, compensation, or
explicit conflict handling.

Expected result:

```text
client_a apparent finality conflicts with client_b apparent finality
only one branch becomes authoritative
losing branch rolls back
conflict is represented by T55-style conflict data
```

## Success Criteria

1. The model is finite and minimal.
2. The model does not invent a parallel formalism.
3. The model includes executable tests.
4. The positive witness separates apparent and authoritative finality without
   contradiction.
5. The failure witness requires rollback, compensation, or explicit conflict
   handling.
6. The report answers:
   - what is final locally;
   - what is final authoritatively;
   - what is only predicted;
   - what gets rolled back;
   - what records propagate;
   - which observer sees which event when;
   - how reversal cost changes before and after authoritative commit;
   - whether the result strengthens A1, motivates a new claim, or exposes a gap.

## Failure Criteria

1. Apparent local finality and authoritative event finality collapse into one
   label.
2. Rollback is treated as erasure instead of an explicit propagated record.
3. Conflict is silently repaired without T55-style conflict data.
4. The result claims that physical reality is like an MMO.
5. The result promotes a new named claim without further hostile cases.

## Reproduction

```bash
python -m pytest tests/test_mmo_reconciliation_finality.py -q
python -m models.run_t61
```

