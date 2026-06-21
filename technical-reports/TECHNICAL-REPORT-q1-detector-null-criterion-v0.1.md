# Technical Report: Q1 Detector Null Criterion v0.1

## Claim Under Test

The detector branch of Q1 has accumulated many boundary results. The missing
artifact is a compact criterion stating when that branch adds independent
measurement content and when it collapses into provenance bookkeeping over
already formed records.

## Result

The current executable detector branch does not support a new detector-dynamics
claim. It supports a stricter admissibility filter on when detector records may
count as evidence for observer-relative finality.

The sharp criterion is:

```text
Q1 detector branch has independent content only if a pre-registered,
event-level, raw-log protocol yields a D1/provenance verdict that cannot be
reduced to passive outcome statistics, coarse deployment summaries, or an
externally declared provenance partition.
```

The current repo does not yet satisfy that stronger condition. T66-T81 instead
support the narrower statement:

```text
Detector-side Q1 is presently an intervention-sensitive provenance-admissibility
criterion over already formed detector records.
```

## Null Criterion

Treat the detector branch as null whenever any of the following holds:

1. the D1 verdict is fixed entirely by passive detector statistics or calibrated
   POVM summaries;
2. the D1 verdict is fixed entirely by a coarse deployment dashboard rather than
   event-level raw logs;
3. the D1 verdict is fixed by a provenance partition that is declared after the
   fact or justified only by semantic labels;
4. the executable audit uses a broad measured schema in prose, but only a
   smaller hidden subset is actually load-bearing in the witness family.

If any null condition holds, TaF is not yet adding detector-level measurement
physics. It is imposing an evidence discipline on classical records.

## Support Chain

- T66: calibrated POVM response matrices do not determine the provenance
  partition.
- T67: passive agreement and phi correlation cannot distinguish copied from
  independent records.
- T68: the partition can be fixed only with intervention-sensitive provenance
  metadata.
- T70: that repair survives only while trusted authenticated channels remain.
- T72 and T74: robust recovery occupies a narrow engineered region under
  explicit protocol assumptions.
- T76 through T79: admissibility requires measured, pre-registered, event-level
  raw logs; dashboard summaries are non-identifying.
- T81: in the current witness family, trust-boundary evidence and
  pre-registration are load-bearing while the rest of the declared schema is
  not yet independently decisive.

## Current Strongest Claim

The most defensible detector-side claim is now:

```text
Q1 does not presently provide an independent detector-dynamics law or a
calibration-free discriminator. It provides a conservative rule for withholding
or permitting D1-style detector claims, conditional on pre-registered
provenance instrumentation over raw logs.
```

This is weaker than a measurement theory and stronger than unconstrained
post hoc bookkeeping.

## What This Improved

This report compresses eight detector artifacts into one falsifiable rule. A
serious reader can now tell immediately what would count as progress and what
would merely restate the existing branch with more examples.

It also clarifies the comparison with decoherence and Quantum Darwinism. Unless
the null criterion is beaten, TaF is not competing with those frameworks on
measurement dynamics. It is only proposing a stricter record-admissibility
discipline.

## What This Weakened

This weakens any claim that the current detector branch is already an
experimental discriminator for new quantum physics.

It also weakens the broad T76 evidence-schema packaging. The present executable
route behaves primarily as:

```text
trusted boundary gate + pre-registration gate + raw-log gate
```

with additional measured channels not yet independently earned.

## Falsification Criterion

This report is falsified if either of the following occurs:

1. a pre-registered rule using only passive outcome statistics or coarse
   summaries correctly classifies hostile copied-versus-independent witness
   families;
2. a raw-log detector deployment shows that spoof resistance, perturbation
   response, or DAG observability alone can force the verdict in a way not
   reducible to trust-boundary and pre-registration gates.

The first outcome would collapse the provenance burden. The second would show
the current null criterion is too pessimistic and the measured schema has
earned more of its breadth.

## Claim Ledger Update

Q1 should remain `partially_supported`, but its detector branch should now be
stated as:

```text
an admissibility filter on detector-side evidence, not an independent detector
theory. The branch becomes non-null only when a pre-registered raw-log protocol
beats passive-statistics, dashboard-summary, and post hoc provenance
alternatives.
```

## Open Blocker

The repo still lacks a witness family or real deployment in which a measured
channel other than trust-boundary evidence or pre-registration is independently
decisive.

## Next Work

Build one hostile raw-log family where exactly one currently non-decisive
channel changes the verdict on its own:

- spoof resistance alone;
- perturbation response alone; or
- DAG observability alone.

If none can be made independently decisive, compress the detector schema and
state openly that the executable branch is a narrow admissibility gate rather
than a broad provenance theory.
