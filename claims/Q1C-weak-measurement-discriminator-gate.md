# Q1C: Weak-Measurement Discriminator Gate

## Claim

A weak-measurement experiment could test Time as Finality only if it supplies a
pre-registered branch, provenance, or undo-cost observable that is independent
of the standard monitored record and changes the TaF verdict while standard
statistics are fixed.

## Class

Subclaim of Q1.

## Status

Dormant.

## Current Strongest Form

Weak measurement is not an active discriminator for the project. The named
superconducting homodyne, uncollapse, and quantum-jump-reversal routes do not
clear the independent-axis gate.

## Earned Content

- T90 defines the reparameterization obstruction: standard-only axes are null,
  and post hoc branch labels are rejected.
- T91 shows that currently named superconducting weak-measurement platform
  families reconstruct their candidate TaF axis from the ordinary monitored
  record or from success-conditioned postselection.
- T93 rejects control-pulse energy, schedule bookkeeping, and
  success-conditioned reversal as non-null undo-cost evidence.
- T94 demotes weak measurement below detector provenance until a real platform
  supplies the missing independent axis.
- T130 screens the most plausible hardware rescue, calorimetric or thermal
  second-meter readout, and finds that the screened literature still supplies
  alternate readout chains rather than a simultaneous dual-meter witness with
  fixed standard monitored statistics.
- T135 sharpens the same loophole against the most relevant screened
  2020-2025 second-meter literature: recent thermal-detector qubit readout,
  nanocalorimetric trajectories, and calorimeter-assisted homodyne still do
  not produce a monitored-qubit simultaneous dual-meter witness with fixed
  standard statistics.
- T137 adds a sharper null class: even a simultaneous second meter is null if
  its event-level statistics are only a downstream transform of the ordinary
  monitored record. Physical distinctness alone does not reopen Q1C.
- T139 closes the coarse-summary loophole: "ordinary monitored statistics held
  fixed" must mean the full pre-registered event-level ordinary record, not a
  dashboard or thresholded export that an auxiliary meter merely refines.
- T143 adds the architecture-level obstruction: once that full event-level
  standard record is treated as the ordinary instrument's conditional log, a
  same-instrument second meter is null by default unless it either captures
  extra environment structure not screened off by the log or explicitly
  enlarges the monitored instrument and states an honest fixed-standard
  comparison.
- T146 turns that obstruction into an executable architecture gate: after
  full-record and postselection screens, only two live proposal classes remain
  for Q1C, an auxiliary channel tied to extra environment structure not
  screened off by the full ordinary log, or an openly enlarged instrument with
  a pre-declared preserved comparison target.
- T149 makes "not screened off by the full ordinary log" operational: at fixed
  full event-level record, the auxiliary channel must give positive
  predeclared decision-risk lift for the Q1C verdict, and the source of that
  lift must be typed as extra environment structure or an explicit instrument
  enlargement with a preserved comparison target.
- T150 closes the verdict-gerrymandering loophole left by T149: positive lift
  counts only when the Q1C verdict is a predeclared map from an independently
  typed TaF axis with nontrivial class support, not when the verdict is merely
  an auxiliary-defined label, a rare-event partition, or a post hoc target.
- T155 adds the absorber under T149/T150: once the full ordinary transcript
  screens off the auxiliary channel, that channel is null across the tested
  finite decision family, not just for one chosen verdict map or loss rule.
- N9 turns the remaining "maybe a real platform already exists" hope into a
  source-backed census: current named homodyne-trajectory, jump-reversal,
  microwave-photon-counter, thermal-detector, nanocalorimetric, and
  calorimeter-assisted quadrature families still supply ordinary records,
  replacement readout, or task changes rather than a live T146/T149/T150 Q1C
  platform.

## Not Earned

- No current weak-measurement platform gives a TaF discriminator.
- No independent branch-support observable is named.
- No independent undo-cost meter is named.
- No postselected reversal result counts as a TaF verdict change.
- No named monitored-qubit platform in the repo supplies a T149-cleared
  auxiliary architecture plus an independently typed TaF verdict target with
  non-gerrymandered support.
- No named platform in the repo has frozen the full `R, A, H, V = g(H), L`
  tuple needed to reopen Q1C under T149 and T150.

## Falsification Or Demotion Condition

If a proposed weak-measurement route derives its TaF variable from the same
monitoring stream used by standard quantum trajectory theory, or conditions it
on reversal success, it is null for Q1C. The same holds for any simultaneous
second meter whose statistics are conditionally determined by the ordinary
monitored record, or whose apparent witness survives only because the ordinary
record was fixed at a coarsened summary rather than at the full event-level
trajectory. It also holds for same-instrument auxiliary channels whose verdict
content is screened off once that full event-level trajectory is treated as the
ordinary instrument log, or which never name extra environment structure or an
explicit instrument enlargement in the first place. It also holds when a
proposal's apparent positive lift depends on defining the verdict directly from
the auxiliary meter, choosing the verdict target after analysis, or isolating a
vanishingly rare verdict class. It also holds when the auxiliary channel is
screened off by the full ordinary transcript, in which case no tested
predeclared finite decision problem gains by adding that channel at all.

## Reinstatement Condition

Reopen Q1C only after a concrete platform names a calibrated, pre-registered
axis that is not reconstructed from the monitored record, not a control-schedule
proxy, not postselected, not screened off by the ordinary monitored record, and
verdict-changing under fixed coherence, redundancy, access, reversal-success
statistics, and the full pre-registered event-level standard monitored record.
Operationally, the platform must declare the full ordinary record `R`,
auxiliary channel `A`, independently typed TaF axis `H`, verdict map `V=g(H)`,
and loss rule, then show positive decision-risk lift from `(R,A)` over `R`
alone. Each verdict class must have nontrivial predeclared support. If the
proposal enlarges the monitored instrument, that enlargement and the preserved
comparison target must be declared explicitly in advance. If it does not
enlarge the instrument, it must instead identify extra environment or detector
structure whose verdict content survives conditioning on the full ordinary
event log.

The current repo handoff for that burden is:

- [Q1C Auxiliary-Channel Platform Handoff](../open-problems/q1c-auxiliary-channel-platform-handoff.md)

## Primary Evidence

- [T90: Weak-Measurement Reparameterization Obstruction](../tests/T90-weak-measurement-reparameterization-obstruction.md)
- [T91: Weak-Measurement Platform Audit](../tests/T91-weak-measurement-platform-audit.md)
- [T93: Weak-Measurement Undo-Cost Independence](../tests/T93-weak-measurement-undo-cost-independence.md)
- [T94: Weak-Measurement Priority Demotion](../tests/T94-weak-measurement-priority-demotion.md)
- [T130: Weak-Measurement Dual-Meter Screen](../tests/T130-weak-measurement-dual-meter-screen.md)
- [T135: Weak-Measurement Second-Meter Checkpoint](../tests/T135-weak-measurement-second-meter-checkpoint.md)
- [T137: Weak-Measurement Postprocessed Second-Meter Obstruction](../tests/T137-weak-measurement-postprocessed-second-meter-obstruction.md)
- [T139: Weak-Measurement Full-Record Sufficiency Boundary](../tests/T139-weak-measurement-full-record-sufficiency-boundary.md)
- [T143: Weak-Measurement Instrument Sufficiency Obstruction](../tests/T143-weak-measurement-instrument-sufficiency-obstruction.md)
- [T146: Weak-Measurement Escape Architecture Gate](../tests/T146-weak-measurement-escape-architecture-gate.md)
- [T149: Weak-Measurement Conditional-Sufficiency Gate](../tests/T149-weak-measurement-conditional-sufficiency-gate.md)
- [T150: Weak-Measurement Verdict-Admissibility Gate](../tests/T150-weak-measurement-verdict-admissibility-gate.md)
- [T155: Weak-Measurement Blackwell Boundary](../tests/T155-weak-measurement-blackwell-boundary.md)
- [N9: Q1C Platform Candidate Census](../literature/N9-q1c-platform-candidate-census.md)
- [Q1C Auxiliary-Channel Platform Handoff](../open-problems/q1c-auxiliary-channel-platform-handoff.md)
