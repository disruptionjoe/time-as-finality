# Technical Report: Dolev Redundancy Feasibility Gate v0.1

## Status

Recorded-tier finite admission gate. No claim promotion, public-posture change,
H7 movement, or thermodynamic claim.

## Purpose

T442 tried to place topology inside a definalization heat-cost floor. The hostile
review refuted that placement: a spanning-tree reversible protocol avoids the
claimed `lambda(G)` surcharge. T443 keeps the useful remainder by moving topology
to the place where it is already native: fault-tolerant consensus feasibility.

## Gate

For the classical synchronous point-to-point Byzantine setting, the gate used by
this audit is:

```text
n >= 3f + 1
kappa(G) >= 2f + 1
```

where `n` is the number of holders, `f` is the tolerated number of Byzantine
holder faults, and `kappa(G)` is vertex connectivity.

Reference checked: Danny Dolev, "The Byzantine Generals Strike Again" (1982),
https://www.cs.huji.ac.il/~dolev/pubs/byz-strike-again.pdf. The report uses this
as known distributed-systems context, not as a new TaF theorem.

## Finite Findings

- `line`, `star`, and `cycle` k=5 fixtures fail the `f=1` admission gate because
  their vertex connectivity is below 3.
- `complete` k=5 admits `f=1` because `n=5` and `kappa(K5)=4`.
- `K4` is the minimal complete `f=1` pass.
- `K6` fails `f=2` by node count even though `kappa(K6)=5`.
- `K7` is the minimal complete `f=2` pass.
- `K3,3` passes `f=1`, showing that completeness is not required; enough vertex
  connectivity is.

## Interpretation

The result is a guardrail for D1 holder redundancy:

```text
topology -> robust-finality feasibility
not
topology -> thermodynamic surcharge
```

This is exactly the demotion discipline needed after T442. Topology can still
matter, but only as a known consensus-theory feasibility constraint unless a
future artifact supplies independent substrate evidence.

## What This Does Not Earn

- No heat-cost lower bound.
- No H7 physical-arrow support.
- No proof of Dolev's theorem.
- No claim-ledger movement.
- No public posture change.
- No cross-repo truth movement.

## Next Use

Before future D1 holder-redundancy artifacts use topology as evidence, require
them to declare:

1. the fault model;
2. the communication model;
3. the holder graph;
4. the tolerated `f`;
5. the native feasibility theorem or absorber;
6. whether the claim is feasibility-only or has a separately earned cost
   substrate.
