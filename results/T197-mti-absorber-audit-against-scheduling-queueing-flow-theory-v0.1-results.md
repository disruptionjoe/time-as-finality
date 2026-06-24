# T197 Results: MTI Absorber Audit Against Scheduling / Queueing / Flow Theory

## Correction Notice

Updated after the T187 review/T200-T209 follow-up. The absorption result should
be read as applying to a conditional harmonic/equal-load timing summary, not an
exact constrained Moses optimization. T206 extends this absorption to the
capacity-aware network proxy.

## Outcome

`absorbed`

In the current harmonic-proxy regime, Cap_TI Candidate C does not
survive as an independent capability theorem. Its predictive content collapses
to the harmonic-mean delivery-time summary `T*`, and that summary is already
owned by standard scheduling, queueing, flow, and performance-style readings.

## Absorber Table

| Neighbor | Standard object granted | Relation to current Candidate C | Result |
| --- | --- | --- | --- |
| Scheduling / operations | effective service-time / completion-time summary | `R` behaves like a pre-run completion proxy derived from aggregate delay | absorbed |
| Queueing theory | service-rate and congestion summary | T185 already grounded `C(lambda)` as queue congestion; current `R` uses no extra TaF structure beyond effective timing | absorbed |
| Network flow / transport | inverse-time allocation and effective delivery time | T187 computes `T*` from the same inverse-time weighting law | absorbed |
| Control / performance engineering | before-the-fact convergence / response-time estimate | predicting fewer rounds from lower effective delay is ordinary performance modeling | absorbed |

## Why The Verdict Tightened

Three earlier tests made the absorber pass much stronger:

- T193: the capability compresses to `(n, T*)`, and effectively to `T*` in the exact family.
- T194: no stricter hostile survivor remains once `(n, T*)` is matched.
- T198: the control rule is explicit: move `T*` to get a split; preserve `T*` to get a null.

Once those are true, the remaining burden is no longer "is there a split?" but:

```text
does the split depend on anything beyond a standard effective-delay summary?
```

For the current exact family, the answer is no.

## Control Readout

| Control class | Expected behavior | Readout |
| --- | --- | --- |
| P1 Alpha/Beta positive split | different `T*` should split | yes, but the split is already absorber-owned |
| N1 branch relabeling | same `T*` should be null | null |
| N2 compensated same-`T*` tradeoff | same `T*` should be null | null |
| N3 topology variation with same `T*` | same `T*` should be null | null |

The important point is that the positive split survives only when the standard
performance summary changes, and every matched-summary hostile control collapses.

## Repo-Safe Reading

The current exact-family result is:

```text
Candidate C is translation residue, not independent capability residue.
```

What the repo still has is a useful dictionary:

```text
reconciliation-bound language <-> harmonic-mean delivery-time summary
```

What the repo does not currently have is a same-neighbor-data capability theorem
that mature scheduling / queueing / flow theories fail to explain.

## What Remains Open

This absorption result does not close the entire MTI line. It narrows the live
burden sharply:

1. T195 should test whether broader non-tree graph families introduce predictive
   structure beyond `T*`.
2. A future reconciliation protocol could still reopen the claim if it depends
   on PO1 / gluing structure at fixed standard timing summaries.
3. T196 may still matter if a continuum bridge creates a nontrivial quantity not
   already absorbed by operations-style neighbors.

Until one of those happens, the current exact-family Candidate C is best treated
as absorbed.
