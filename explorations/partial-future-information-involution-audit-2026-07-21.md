# Partial-future-information involution audit

Date: 2026-07-21 22:39 CDT  
Run: `RUN-20260721-223532-repository-work-cycle-cai-hourly`  
Lane: 1 — Formalization and truth testing  
Status: exploration-tier scope correction; no claim, canon, or public-posture movement

## Question

The frozen T19 fixture makes `A*(R)` forget the entire future-configuration
space `X`. Its computable functions are therefore constant on the one-block
partition `{X}`. The involution audit correctly proves that no fixpoint-free
involution on `|X| > 2` has that orbit partition.

The same audit then said that allowing `A*(R)` to retain partial coarse future
information could only make coincidence harder. Is that extension valid?

## Exact reduction

Let `q:X -> Q` be the information retained by the lifted `A*(R)`, and let
`P_q` be its fiber partition. A function is computable from `q` exactly when
it is constant on every block of `P_q`. For an involution `alpha`, a function
is `alpha`-even exactly when it is constant on every orbit of `alpha`.

For a codomain with at least two distinguishable values, the two function
classes are equal if and only if

```text
P_q = Orbit(alpha).
```

Different partitions are separated by the indicator of a block belonging to
one partition but not the other. The criterion is exact, not merely necessary.

## Controls

The updated `tests/involution_typing_probe.py` checks both sides.

- Positive, `k=2`: for global complement, the retained parity bit has fibers
  `{00,11}` and `{01,10}`, exactly the two involution orbits. Coincidence is
  restored.
- Negative, `k=2`: retaining the first witness bit has equally many fibers but
  the wrong partition. Coincidence is not restored.
- Positive, `k=3`: retaining the complement-pair identity gives four fibers,
  each exactly one global-complement orbit. Coincidence is restored.

The amount of retained information is not decisive. Orbit alignment is.

## Verdict

The original T-REFUTE remains valid for the frozen full-forget T19 fixture:
its one-block partition cannot equal a multi-orbit fixpoint-free involution
partition. The claimed stability under every partial-information lift does
not survive. An operator-grade lift can make the exclusion mechanisms
coincide if—and only if—its retained-information fibers are the involution
orbits.

This narrows the next legitimate reopener. It must specify the operator-grade
retained-information map independently of the desired involution verdict, then
compare its fiber partition with the candidate involution orbits. Choosing the
coarse-graining after seeing the desired match would be circular.

## Boundary

This is a formal partition result and scope correction. It does not supply a
physical source packet, establish the operator-grade `A*(R)`, reopen T19 by
itself, or move C1, T19, T92, the Complexity Ledger, the Canon Index, or public
posture. The main Lane 1 source gate remains in force.
