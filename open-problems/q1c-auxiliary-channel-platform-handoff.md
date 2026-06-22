# Q1C Auxiliary-Channel Platform Handoff

## Status

External platform-admissibility issue draft. This is not weak-measurement
evidence, not a prediction, and not a Q1C upgrade.

## Route

Quantum measurement / classical records.

## Why This Exists

T140 says the Q1 branch has no active internal upgrade route. T146, T149, and
T150 then narrowed Q1C further: a weak-measurement proposal is null unless it
names

- the full ordinary event-level record `R`;
- an auxiliary channel `A`;
- an independently typed TaF axis `H`;
- a fixed verdict map `V = g(H)`;
- a declared loss rule;
- and either extra-environment structure or an explicit instrument
  enlargement with a preserved comparison target.

This file converts that blocker into a concrete handoff. Its purpose is to
make Q1C externally testable or operationally dormant rather than an excuse
for more internal toy models.

## Current Strongest Claim

Q1C survives only as a reinstatement gate:

```text
No weak-measurement platform counts for Q1C unless an auxiliary channel gives
positive predeclared verdict-risk lift over the full ordinary monitored
transcript, and that lift targets a predeclared TaF verdict map from an
independently typed axis rather than an auxiliary-defined or rare-event label.
```

The live question is not whether an experiment has a second meter. The live
question is whether the platform yields a non-gerrymandered TaF decision
problem that standard monitored statistics cannot already settle.

## Issue Draft

### Title

Pre-registered auxiliary-channel platform for Q1C admissibility

### Objective

Find one monitored quantum platform whose experimenters are willing to freeze a
Q1C-valid auxiliary-channel specification before analysis and accept the null
verdicts below.

### Background To Send

The project is not asking a lab to endorse Time as Finality. It is asking
whether a monitored quantum platform can name an auxiliary channel whose
decision value survives the current null screens.

The nearest repo artifacts are:

- [T140 Q1 Frontier Escape Matrix](../tests/T140-q1-frontier-escape-matrix.md)
- [T146 Weak-Measurement Escape Architecture Gate](../tests/T146-weak-measurement-escape-architecture-gate.md)
- [T149 Weak-Measurement Conditional-Sufficiency Gate](../tests/T149-weak-measurement-conditional-sufficiency-gate.md)
- [T150 Weak-Measurement Verdict-Admissibility Gate](../tests/T150-weak-measurement-verdict-admissibility-gate.md)
- [T158 Weak-Measurement Preserved-Target Gate](../tests/T158-weak-measurement-preserved-target-gate.md)
- [T166 Weak-Measurement Platform-Packet Gate](../tests/T166-weak-measurement-platform-packet-gate.md)

### Stage 1: Minimum Pre-analysis Commitment

Before any platform packet is treated as admissible for Q1C, it should clear
the T166 intake gate. That means freezing:

1. The full ordinary event-level monitored record schema `R`, not a dashboard
   or thresholded summary.
2. The auxiliary channel schema `A`, including calibration and event alignment.
3. The architectural class:
   - extra environment or detector structure not screened off by `R`; or
   - explicit instrument enlargement with a preserved comparison target.
4. An independently typed TaF axis `H`.
5. A fixed verdict map `V = g(H)` declared before looking at results.
6. A class-support floor for every verdict class.
7. A declared loss rule for predicting `V` from `R` alone and from `(R, A)`.
8. A null-control plan covering coarse-record refinement, postselection,
   auxiliary-defined labels, rare-target partitions, and same-instrument
   underdeclaration.
9. If the proposal enlarges the monitored instrument, an eventwise
   back-projection from enlarged data to the full ordinary standard record.

Packets that do not freeze those fields should be treated as null or scaffold-
only, not as live Q1C progress.

### Stage 2: Required Data And Architecture Burden

The platform must later supply enough event-level detail to audit:

1. Whether `A` is conditionally determined by `R`.
2. Whether any apparent lift survives when `R` is treated as the full ordinary
   transcript rather than a coarsened export.
3. Whether `H` is typed independently of the auxiliary meter.
4. Whether the verdict support floor is satisfied without post hoc partition
   surgery.
5. Whether an enlarged-instrument proposal preserved the comparison target it
   promised to preserve.
6. Whether that preserved target is the full ordinary event-level standard
   record rather than a coarse summary.
7. Whether the enlarged instrument's declared back-projection lets the
   standard target drift on any admissible events.

If the platform cannot expose those checks at event level, Q1C remains null
for that platform.

## Non-null Outcomes

The only positive near-term outcome is narrow:

```text
A named monitored platform freezes R, A, H, V = g(H), the loss rule, and the
architecture class before analysis, then shows positive verdict-risk lift from
(R, A) over R alone without verdict gerrymandering or screened-off auxiliary
content.
```

That would not validate Time as Finality. It would only reopen Q1C as a
reviewable platform-specific discriminator candidate.

## Null Outcomes

Treat the route as null for Q1C if any of these occur:

- The "ordinary monitored record" is only a coarse summary.
- The auxiliary meter is a downstream transform of the ordinary transcript.
- The verdict is defined directly from the auxiliary meter.
- The verdict target is chosen after analysis.
- The lift exists only on a vanishingly rare verdict class.
- The proposal stays inside the same instrument but never names extra
  environment structure or explicit instrument enlargement.
- Instrument enlargement is claimed without a preserved comparison target.
- Instrument enlargement is claimed without an eventwise back-projection to the
  full ordinary standard record.
- The claimed preserved target is only a coarse summary or drifts under the
  proposed back-projection.
- The platform reports only aggregate summaries rather than event-level data
  needed for the screens above.

## Decision Rule

If no named platform can clear the T166 packet gate by freezing the full
`R, A, H, V, L` tuple plus support floor, null controls, and event-level audit
burden, Q1C should remain dormant and should not receive additional internal
toy-model effort.

If a platform can freeze the tuple but refuses the event-level screens, Q1C
remains a scaffold-only admissibility protocol and gains no experimental
standing.

## What This Would Improve

- Converts the Q1C blocker into a yes/no external ask.
- Prevents "has a second meter" from being confused with a live TaF route.
- Gives future runs a concrete reason to leave Q1C dormant until a platform
  clears the burden.

## What This Weakens

This weakens Q1C as an autonomous internal research route. The branch now
depends on a concrete platform specification, not another abstract meter
family. If no platform can satisfy the handoff, Q1C should stay below active
quantum-measurement work.

## Claim Ledger Update

Q1C remains `dormant`. The next non-null artifact is not another internal weak
measurement model; it is a named platform that first clears the T166 packet
gate by predeclaring `R`, `A`, `H`, `V = g(H)`, a support floor, a loss rule,
a live T146 architecture class, null controls, and event-level audit data, and
for any enlarged-instrument route an eventwise back-projection to the full
ordinary standard record, then survives the T149/T150/T158 event-level
screens.
