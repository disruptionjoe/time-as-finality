# T46: Open Causal Scarcity And Closed Synchronization Boundary

## Target Claims

- [R1: Relativity And No Global Commit Order](../claims/R1-relativity-no-global-commit-order.md)
- [A1: Distributed-Systems Finality Analogy](../claims/A1-distributed-systems-finality-analogy.md)
- [PO1: Projection-Obstruction Schema](../claims/PO1-projection-obstruction-schema.md)
- [T42: Local Persistence And Reconciliation Split Audit](T42-local-persistence-reconciliation-split.md)
- [T44: Local Mechanism Identifiability Audit](T44-local-mechanism-identifiability.md)

## Setup

T46 introduces a finite `RecordAccessSystem` sidecar. It compares two ways
record access can become scarce:

1. Open causal scarcity:
   - a record is generated at a source;
   - observers receive it through finite propagation paths;
   - first access is determined by path delay.

2. Closed synchronization scarcity:
   - participants are inside a synchronized membership boundary;
   - commit order is assigned by timestamp, quorum, and uncertainty rules;
   - outside observers must wait for commit records to propagate outward.

The real-world anchors are NYSE-style market-data propagation and
Spanner/TrueTime-style commit ordering. The executable model is only a finite
abstraction of propagation, membership, uncertainty, and commit order.

## Witnesses

### Open causal witness

The NYSE-style witness has one generating node and three observers:

```text
exchange_engine -> colocated_rack
exchange_engine -> metro_pop
exchange_engine -> remote_region
```

Expected result:

```text
colocated_rack before metro_pop before remote_region
```

The scarcity axis is causal proximity.

### Closed synchronization witness

The Spanner-style witness has three member replicas and one outside observer:

```text
west_replica
east_replica
central_replica
outside_client
```

Two transactions are configured so the internal commit order is:

```text
tx_west before tx_east
```

but the outside raw arrival order is:

```text
tx_east before tx_west
```

The outside observer cannot reconstruct the internal commit order until commit
records propagate outward. The scarcity axis is membership plus synchronization
rule.

### Measurement boundary table

T46 also records a conservative measurement-projection boundary:

```text
richer pre-record structure -> observer-accessible record layer
```

This table names preserved and forgotten structure, but it does not claim a
full PO1 theorem, a 14-dimensional quantum layer, or a physical measurement
solution.

## Success Criteria

1. Implement a finite `RecordAccessSystem`.
2. Demonstrate open causal first-access advantage.
3. Demonstrate a closed synchronized commit boundary.
4. Show a case where outside raw arrival order differs from internal commit
   order without violating propagation constraints.
5. State H0-H5 verdicts.
6. Decide whether CS1 should become a named claim.
7. Avoid claims that TaF derives relativity, the speed of light, Spanner, or
   quantum measurement.

## Failure Criteria

1. Open and closed cases collapse into the same observable.
2. The closed case imposes order without an explicit membership boundary.
3. The model treats synchronization as escaping propagation constraints.
4. The measurement table is promoted to a physics claim.
5. The result modifies `D1RestrictionSystem` without need.

## Known Constraints

- This is not a market microstructure model.
- This is not a Spanner implementation.
- This does not derive `c`.
- This does not explain time dilation.
- This does not prove a measurement morphism theorem.
- This does not assume that the richer pre-record layer is 14-dimensional.

## Contribution Needed

Future work should test more hostile domains where the boundary is ambiguous:
cross-exchange arbitrage, dark-pool reporting, public ledger mempools, sensor
fusion networks, and read-replica databases with stale external observers.
