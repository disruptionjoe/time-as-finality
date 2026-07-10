# Open Problem: Jevons Rebound Capability Gate

## Status

Open gate / absorber candidate. No claim promotion.

Seeded by CapacityOS mailbox processing in
`RUN-20260710-303-mailbox-processing-fanout-hourly`.

## Question

When a record, finalization, reversal, search, or transport operation becomes
cheaper, total use of that operation may increase. A lower unit cost can
therefore increase aggregate burden, record count, reversal debt, or future
operation load.

The gate asks:

```text
Is an apparent capability/finality improvement still an improvement after
demand response is modeled, or is it ordinary resource-demand accounting?
```

## Minimal Gate

Declare:

```text
R      bounded region or access profile
M      operation menu
op     operation whose unit cost changes
c      unit cost of op
D(c)   demanded operation count
B(c)   aggregate burden, record count, reversal debt, or future-operation load
C(R,M) capability object before and after demand response
```

The rebound concern fires when:

```text
c decreases
D(c) increases
B(c) increases or changes the capability comparison
```

The result is useful only if `B(c)` is domain-native and predeclared. A
post-hoc burden variable is just another hidden descriptor.

## Admission Requirements

A future packet should include:

- a named operation and unit-cost measure;
- a predeclared demand-response rule or measured demand packet;
- the aggregate burden or reversal-debt quantity before pair selection;
- fixed observer/access profile and operation menu;
- positive controls where lower unit cost remains a net improvement;
- negative controls where demand response erases or reverses the apparent
  improvement;
- an absorber check against ordinary resource theory, maintenance load,
  queueing/congestion, and viability/control accounting.

## Success Criteria

The gate succeeds if it distinguishes:

```text
unit efficiency improvement
```

from:

```text
net finality/capability improvement after aggregate demand response
```

without moving claim status or importing source-side Temporal Issuance
language.

## Failure / Demotion Criteria

Demote this route if:

- the split factors through ordinary resource accounting once total operation
  count is included;
- the burden variable is chosen after seeing the pair;
- demand is imported as an unexplained hidden label;
- the result is only queueing, congestion, maintenance, or viability accounting
  with no TaF-specific residue;
- the proposed split requires source-side possibility-growth language, which
  belongs in Temporal Issuance instead.

## Cross-Repo Boundary

TaF owns only the capability/finality accounting side: `C(R,M)`, declared
operation menus, aggregate burden, and future-operation availability. If a
future packet needs a source-side possibility-growth interpretation, route it
to the Temporal Issuance mailbox rather than importing TI truth here.
