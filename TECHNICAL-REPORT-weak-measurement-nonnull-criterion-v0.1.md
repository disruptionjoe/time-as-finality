# Technical Report: Weak-Measurement Non-Null Criterion v0.1

## Claim Under Test

T12 is currently the highest-upside open route inside Q1. If Time as Finality
can produce a continuous-monitoring or weak-measurement protocol with a
record-finalization time distinct from standard decoherence or
Quantum-Darwinism-style redundancy, the project gains a plausible experimental
discriminator.

The risk is equally clear: with the current D1 proxies, that proposed
discriminator may collapse into ordinary decoherence plus access-window and
threshold choices. This report states the collapse condition explicitly.

## Result

The weak-measurement route is not yet an earned discriminating prediction.
With the current repo-level measurement machinery, it becomes non-null only if
at least one D1 coordinate is operationalized by a measured or intervention-set
observable that is not reducible to:

- pointer-coherence decay;
- fragment mutual information / redundancy;
- a declared observer access window; or
- a post hoc threshold or provenance partition.

Without that extra observable, `t_finality` is only a renamed threshold time on
standard monitored-record statistics.

## Formal Non-Null Criterion

Let

```text
t_decohere(epsilon) = inf { t : C(t) <= epsilon }
```

for a chosen coherence witness `C(t)`, and let

```text
t_finality = inf { t :
  A(t) >= k_A,
  H(t) >= k_H,
  B(t) >= k_B,
  R(t) >= k_R
}
```

where:

- `A(t)` = accessible support;
- `H(t)` = independent holder redundancy;
- `B(t)` = branch support;
- `R(t)` = reversal-cost surrogate.

Then the TaF weak-measurement route is non-null only if at least one of
`H(t)`, `B(t)`, or `R(t)` is fixed by a pre-registered measured/intervention
observable not determined by the same sufficient statistics that already fix
`C(t)` and ordinary redundancy counts.

If all four coordinates are functions only of coherence decay, fragment
information, access windows, and analyst-chosen thresholds, then `t_finality`
is not a new prediction. It is a re-parameterization of existing monitored
record formation.

## Why The Current Repo Fails This Criterion

T2, T62, T64, and T66 establish useful boundaries, but they do not yet provide
the extra operational content T12 needs.

- T2 gives a dynamical decohered-but-inaccessible witness, but branch support is
  fixed at `1` and reversal cost is a counting proxy.
- T62 and T64 show that observer access and duplicate filtering matter, but the
  verdict remains threshold-sensitive.
- T66 shows POVM calibration does not choose thresholds or provenance
  partitions.
- T83-T87 show the detector branch surviving only as a pre-registered raw-log
  admissibility protocol over already formed records.

The current measurement stack therefore earns this narrower statement:

```text
TaF can currently audit when monitored detector records may count as
observer-relative evidence. It does not yet supply an independent
weak-measurement finalization observable.
```

## What A Real Escape Route Would Look Like

A serious T12 implementation now needs one of the following:

1. an intervention-defined holder-redundancy observable:
   copied-versus-independent monitored records separated by raw provenance or
   isolated perturbation controls during the trajectory;
2. a branch-support observable:
   a pre-registered witness that multiple candidate record branches remain live
   for the same observer even after coherence suppression;
3. a reversal-cost observable:
   an experimentally grounded undo/erasure cost or pulse-budget measure that is
   not a trivial monotone transform of support count.

If none of those can be stated concretely before modeling, T12 should be
demoted from "prediction route" to "blocked operationalization problem."

## What This Improved

This report converts T12 from an aspirational placeholder into a falsifiable
intake gate. It tells a serious reader exactly what must be supplied before a
continuous-monitoring model would count as new physics rather than vocabulary.

It also protects the repo from a common failure mode: presenting a different
threshold on coherence loss or fragment redundancy as if it were an independent
quantum prediction.

## What This Weakened Or Falsified

This weakens the current strongest experimental-sounding path inside Q1.
Nothing in the repo yet justifies calling T12 a discriminating prediction.

It also weakens any attempt to operationalize branch support or reversal cost by
simple monotone proxies of record count. That move would make the route null by
construction.

## Falsification Condition

This report fails if either of the following occurs:

1. a pre-registered continuous-monitoring protocol using only standard
   decoherence/redundancy statistics yields a TaF verdict that cannot be
   re-expressed as thresholded standard record formation; or
2. a concrete monitored platform supplies an independently measured branch,
   provenance, or reversal-cost observable that changes `t_finality` while
   leaving the standard decoherence verdict unchanged.

Either outcome would show the present non-null criterion is too pessimistic.

## Claim Ledger Update

Q1 should remain `partially_supported`, but the weak-measurement branch should
now be stated more narrowly:

```text
T12 is not yet an earned discriminator. It becomes a valid prediction route
only when at least one D1 coordinate beyond accessible support is tied to a
pre-registered measured/intervention observable that is not reducible to
decoherence, redundancy, access windows, or post hoc threshold choice.
```

## Open Blocker

The repo lacks an operational definition of branch support or reversal cost for
continuous monitoring that is both measurable and non-circular. Until that
exists, the highest-upside open measurement route is conceptually blocked.

## Next Work

Choose one concrete monitoring platform and force the issue:

- superconducting qubit homodyne trajectory with a pre-registered branch-live
  witness; or
- trapped-ion/cavity-QED reversal protocol with a nontrivial undo-cost
  observable.

If neither can be specified cleanly, demote T12 in the roadmap and stop
describing it as the project's main experimental discriminator.
