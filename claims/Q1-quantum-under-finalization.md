# Q1: Quantum Under-Finalization

## Claim

Quantum states can be real but not yet finalized as classical records in a particular observer-environment context.

## Class

Conjecture.

## Status

Partially supported.

## What This Does Not Claim

- It does not say quantum states are unreal.
- It does not say human consciousness collapses the wavefunction.
- It does not say decoherence alone solves the measurement problem.
- It does not restore naive local hidden variables.
- It does not allow faster-than-light signalling.

## Why It Might Be True

The quantum/classical transition is deeply tied to record formation, decoherence, pointer bases, environmental redundancy, and observer access. "Under-finalized" may help distinguish real quantum constraint from settled classical fact.

For entanglement, the safe finality chain is:

```text
entangled joint state
  -> local measurement interaction
  -> local record formation
  -> decoherence / environmental redundancy
  -> observer-relative finality
  -> later causal comparison
  -> globally reconciled correlation record
```

The key distinction is that an entangled joint constraint can be real before separated local observers share a classical finalized record. Shared classical finality requires causal reconciliation. The correlation is not a controllable faster-than-light message.

Proof-carrying language may help here: later comparison can certify a nonclassical joint constraint without implying that either local observer had full access to the global state or a hidden local answer in advance.

## How It Could Fail

- It adds no clarity beyond decoherence or quantum Darwinism.
- It smuggles in collapse without saying so.
- It cannot handle basis-dependence.
- It violates Bell/no-signalling constraints.
- It treats a later correlation record as if it were an earlier local hidden variable.
- It turns proof or verification language into an encrypted-message metaphor for entanglement.

## Tests

- [T2: Quantum Measurement Record Finality](../tests/T2-quantum-measurement-record-finality.md)
- [T6: Snowball Record Finality](../tests/T6-snowball-record-finality.md)
- [T21: Bell Contextuality Finality](../tests/T21-bell-contextuality-finality.md)
- [T22: D1 Physical Reduction Map](../tests/T22-d1-physical-reduction-map.md)
- [T23: Invariant-Preserving Transformations](../tests/T23-invariant-preserving-transformations.md)
- [T62: Noisy Measurement Access-Boundary Discriminator](../tests/T62-noisy-measurement-access-boundary.md)
- [T64: Stern-Gerlach Detector Access-Window Discriminator](../tests/T64-stern-gerlach-access-window.md)
- [T66: POVM Detector Calibration Obstruction](../tests/T66-povm-detector-calibration-obstruction.md)
- [T67: POVM Correlation Provenance Obstruction](../tests/T67-povm-correlation-provenance-obstruction.md)
- [T68: Intervention-Sensitive Detector Provenance](../tests/T68-intervention-sensitive-detector-provenance.md)
- [T70: Detector Provenance Robustness](../tests/T70-detector-provenance-robustness.md)
- [T72: Physical Provenance Protocol](../tests/T72-physical-provenance-protocol.md)
- [T74: Provenance Protocol Monte Carlo](../tests/T74-provenance-protocol-monte-carlo.md)
- [T75: Real Detector Stack Provenance Mapping](../tests/T75-real-detector-stack-provenance.md)
- [T76: Measured Detector Provenance Posterior](../tests/T76-measured-detector-provenance-posterior.md)
- [T77: Measured Detector Policy Sensitivity](../tests/T77-measured-detector-policy-sensitivity.md)
- [T78: Pre-registered Detector Deployment Protocol](../tests/T78-preregistered-detector-deployment-protocol.md)
- [T79: Dashboard Summary Nonidentifiability](../tests/T79-dashboard-summary-nonidentifiability.md)
- [T81: Measured Schema Ablation](../tests/T81-measured-schema-ablation.md)
- [T83: Q1 Detector Null Criterion](../tests/T83-q1-detector-null-criterion.md)
- [T85: Measured Detector Channel Dominance](../tests/T85-measured-detector-channel-dominance.md)
- [T86: Ambiguous-Tag Channel Independence](../tests/T86-ambiguous-tag-channel-independence.md)
- [T90: Weak-Measurement Reparameterization Obstruction](../tests/T90-weak-measurement-reparameterization-obstruction.md)
- [T91: Weak-Measurement Platform Audit](../tests/T91-weak-measurement-platform-audit.md)
- [T93: Weak-Measurement Undo-Cost Independence](../tests/T93-weak-measurement-undo-cost-independence.md)
- [T94: Weak-Measurement Priority Demotion](../tests/T94-weak-measurement-priority-demotion.md)

## T21 Result

[T21](../tests/T21-bell-contextuality-finality.md) gives Q1 a finite
contextuality model. Four CHSH-style local measurement contexts each have
valid local finality sections, but no global assignment satisfies all
contexts.

This supports the narrow under-finalization claim: local classical records can
be finalized in their own measurement contexts while a single global
noncontextual record assignment remains unavailable. The result is structural,
not a detector-level simulation.

The probability-bearing extension compares three CHSH regimes: classical
noncontextual score `2`, quantum Tsirelson score `2*sqrt(2)`, and PR-box
no-signalling score `4`. This sharpens Q1's claim: quantum contextuality sits
between global classical finality and post-quantum no-signalling consistency.
- [Proof-Carrying Record Finality](../open-problems/proof-carrying-record-finality.md)

## T22 Result

[T22](../tests/T22-d1-physical-reduction-map.md) gives Q1 the first executable
comparison requested by the quantum-Darwinism neighbor. In a binary
system-environment toy model, each informative environment fragment has
`I(S;E_i) = 1.0` bit and the noise fragment has `I(S;N1) = 0.0`.

With delta `0.1`, the information threshold is `0.9` bits. Raw accessible
environmental redundancy counts `E1`, `E2`, and `E3`, for a value of `3`.
After quotienting the correlated duplicate `E3` with `E1`, the
independence-corrected accessible redundancy is `2`, matching D1 holder
redundancy.

This partially supports Q1 only as a record-finality vocabulary for
environmental redundancy. It does not simulate quantum amplitudes,
decoherence dynamics, detector noise, or collapse.

## T2 v0.1 Result

[T2](../tests/T2-quantum-measurement-record-finality.md) extends T22 into a
small dynamical measurement model:

```text
S -> A -> E1, E2, E3
```

using reversible CNOT interactions in the `computational_z` pointer basis.
The model computes reduced pointer coherence, fragment mutual information,
environmental `R_delta`, and observer-relative D1 profiles.

The main positive result is a decohered-but-inaccessible case. After the first
environment copy, pointer coherence is `0.0`; after all copies,
environmental `R_delta` is `3`. But an outside observer with no access has:

```text
D1 = (0, 0, 0, 0)
```

This supports Q1's narrow claim that "decohered in the pointer basis" and
"final as a classical record for this observer" are distinct predicates in
the toy substrate. It also preserves the guardrail: T2 uses unitary dynamics
only and never selects a collapse outcome.

## T23 Result

[T23](../tests/T23-invariant-preserving-transformations.md) turns the T2 to
T22 quantum bridge into a typed invariant-preserving reduction:

```text
T2 global measurement state
  -> T2 local observer D1 view
  -> T22 reduction schema
```

The composition preserves:

```text
pointer_basis = computational_z
```

and the second reduction preserves holder redundancy, accessible support, and
observer-access indexing. This supports Q1 as part of a broader invariant
transport program, while keeping the same limits: no collapse, no Born-rule
derivation, no detector-level model, and no claim that quantum measurement is
equivalent to the other T23 domains.

## T62 Result

[T62](../tests/T62-noisy-measurement-access-boundary.md) weakens Q1 away from
new noisy measurement dynamics. It separates pointer decoherence,
Quantum-Darwinism-style environmental redundancy, and observer-relative D1
finality in a finite noisy-channel matrix.

The strongest positive result is the `redundant_but_inaccessible` witness:
environmental records can be redundant while an observer with no access window
has D1 profile `(0, 0, 0, 0)`. The main boundary is that
`decohered_not_darwinist` is already standard decoherence-versus-redundancy
territory. TaF adds only access-boundary and independence bookkeeping.

## T64 Result

[T64](../tests/T64-stern-gerlach-access-window.md) moves the T62 audit into a
Stern-Gerlach detector proxy with screen, electronics, log, archive, and weak
bath fragments. It preserves the access-boundary distinction but weakens Q1:
detector finality flips under plausible information-threshold choices.

T64 also adds a no-signalling guardrail. In the entangled-pair variant, remote
setting changes alter correlations but not the local noisy detector marginal.
The earned claim is therefore narrow: TaF can express an access-window and
independence-filter predicate over already formed detector records, but it has
no calibration-free Stern-Gerlach prediction yet.

## T66-T81 Detector Provenance Result

[T66](../tests/T66-povm-detector-calibration-obstruction.md) replaces declared
channel reliabilities with calibrated POVM response matrices and shows that
threshold/provenance underdetermination remains. [T67](../tests/T67-povm-correlation-provenance-obstruction.md)
then refutes the passive-correlation repair: copied archives and independent
readout chains can have identical pairwise agreement and phi correlation while
requiring opposite D1 independence partitions.

[T68](../tests/T68-intervention-sensitive-detector-provenance.md) gives a
conditional positive result. Intervention-sensitive provenance metadata can
fix the partition before D1 scoring through origin tags, perturbation response,
delayed-copy ancestry, and signed provenance DAG data.

[T70](../tests/T70-detector-provenance-robustness.md) stress-tests that repair.
The rule survives moderate single-channel degradation when redundant
authenticated provenance channels remain. It fails cleanly when trusted
channels are absent or contaminated: D1 is withheld rather than inferred from
passive similarity, partial-DAG thresholds, or semantic labels.

[T72](../tests/T72-physical-provenance-protocol.md) replaces Boolean
degradation flags with interval/probability protocol parameters: clock error,
signature failure, archive batching, trust boundaries, perturbation back-action,
and partial provenance-DAG observability. It shows robust recovery under
declared physical reliability bounds, an ambiguous withhold region, an ad hoc
threshold failure, and unsafe false-independence/false-dependence regimes.

[T74](../tests/T74-provenance-protocol-monte-carlo.md) converts that regime
table into a deterministic stress-prior audit. In `400` samples per family,
robust recovery survives in the `engineered_lab` family at rate `0.905`, while
it disappears entirely in the broader `mixed_lab` and `field_degraded`
families. Outside the engineered corner, the protocol mostly withholds D1
rather than fixing a provenance partition.

[T75](../tests/T75-real-detector-stack-provenance.md) maps a source-anchored,
posterior-modeled photon time-tagging stack into the T72/T74 protocol
coordinates: PicoQuant HydraHarp 500-class time tagging, White Rabbit
synchronization, and a hash-chained RFC-3161-style signed archive. Under the
mapped plausible posteriors, the signed stack lands in robust recovery in
`400/400` samples. The unsigned-control variant keeps the timing hardware but
loses robust recovery (`0.005` robust rate), mostly withholding D1.

[T76](../tests/T76-measured-detector-provenance-posterior.md) converts that
stack-level story into a measured evidence schema. Timing resolution alone no
longer counts; authentication, trust-boundary, perturbation, and DAG evidence
must all be present in the deployment record before the signed route remains
positive.

[T77](../tests/T77-measured-detector-policy-sensitivity.md) then shows that the
signed fixture is not the fragile part. The fragile part is control separation:
under a permissive policy corridor, the timing-only unsigned control already
leaks false positives.

[T78](../tests/T78-preregistered-detector-deployment-protocol.md) moves the
boundary before data collection. A detector run can only test Q1 if it fixes
the T76 evidence schema, T77-safe policy corridor, negative controls, raw-log
sources, and demotion rule before the first event.

[T79](../tests/T79-dashboard-summary-nonidentifiability.md) makes the raw-log
requirement load-bearing. It constructs two deployments with the same coarse
dashboard summary for timing, tag retention, signature verification, and
threshold coverage, but opposite provenance verdicts: one robustly supports
the signed route and the other leaks false independence because spoof, trust,
perturbation, and DAG failures are hidden from the dashboard view.

[T81](../tests/T81-measured-schema-ablation.md) then turns the scrutiny back
onto the audit itself. Under single-category ablation of the signed T76
fixture, only trust-boundary evidence fully removes robust recovery and only
incomplete pre-registration demotes the verdict to a threshold-dependent one.
Timing, retention/signature pass rates, spoof-resistance counts, perturbation
counts, and DAG-summary counts are not yet independently decisive in the
current witness family.

The detector branch of Q1 should therefore be stated as an
intervention-sensitive provenance/accounting framework over already formed
detector records under explicit physical protocol assumptions. It does not
recover detector finality from calibrated outcome statistics or passive
correlations alone. T75 gives a source-anchored, posterior-modeled candidate
route into the engineered region, but T76-T81 show that the route remains
valid only for measured, pre-registered, event-level raw-log provenance
protocols, and that the present executable route currently earns less than its
full schema claims. Dashboard summaries, fixture counts, and post hoc policy
selection cannot upgrade Q1. Nor can the current model claim that every
measured provenance channel is already independently load-bearing.

## T83 Result

[T83](../tests/T83-q1-detector-null-criterion.md) compresses the detector
sequence into a single failure rule. The detector branch is null whenever its
verdict reduces to passive outcome statistics, coarse deployment dashboards,
post hoc provenance declarations, or a broad measured schema whose decisive
content is actually a narrower hidden subset.

Under T66-T81, the current detector branch does not beat that null criterion.
Its strongest supported content is therefore narrower than a detector theory:
it is a conservative admissibility filter for when detector records may count
as evidence for observer-relative finality. The branch becomes non-null only
if a pre-registered raw-log protocol yields a verdict that survives those null
reductions.

## T85 Result

[T85](../tests/T85-measured-detector-channel-dominance.md) sharpens the
post-T81 blocker. Holding trust boundaries and pre-registration fixed at the
signed T76 values, a hostile spoof/unique-tag family independently demotes the
signed fixture from robust recovery to conservative withhold. But even hostile
single-category perturbation and DAG families do not demote the fixture while
authenticated tags remain strong.

This narrows the detector branch again. The current executable route behaves
mainly like:

```text
pre-registration gate
  + trust-boundary gate
  + authenticated-tag sufficiency
```

with perturbation and DAG evidence still motivated, but not yet independently
decisive, in the present witness family.

## T86 Result

[T86](../tests/T86-ambiguous-tag-channel-independence.md) tests the hostile
family requested by T85. Timing and authenticated tags are deliberately made
ambiguous while trust and pre-registration remain fixed.

The all-ambiguous control withholds D1 completely. Clean perturbation-only and
clean signed-DAG-only fixtures each recover robust measured provenance in
`400/400` samples. Back-action-contaminated perturbation and truncated/false
shared-edge DAG controls withhold completely.

This partially rescues perturbation response and signed ancestry from deletion
as schema channels, but only as isolated, pre-registered raw-log tests. It does
not upgrade Q1 into detector dynamics or empirical support without a real T78
deployment.

## T91 Result

[T91](../tests/T91-weak-measurement-platform-audit.md) instantiates T90 on
three named superconducting weak-measurement families: homodyne trajectories,
partial-measurement uncollapse, and mid-flight quantum-jump reversal.

All three fail the independent-axis gate. The homodyne and quantum-jump routes
derive their candidate TaF branch/reversal witnesses from the same monitored
record already used by standard quantum trajectory theory. The uncollapse route
fails differently: its apparent reversal witness is conditioned on
success/null-outcome selection, so it is not yet a pre-registered independent
reversal-cost observable.

This narrows T12 again. The currently named superconducting weak-measurement
platforms validate trajectory control and feedback, but they do not yet supply
an independent D1 branch-support or reversal-cost axis. T12 should therefore be
treated as a blocked operationalization problem until a platform names an axis
that is distinct from the monitored record itself and does not rely on
postselection.

## T93 Result

[T93](../tests/T93-weak-measurement-undo-cost-independence.md) isolates the
physically metered undo-cost escape hatch left by T91.

The audit rejects three common false positives. Control-pulse energy or
schedule bookkeeping is a `null_proxy_cost`; success-conditioned reversal is a
`null_postselected_cost`; and an independent meter that varies without changing
the verdict is `independent_but_not_decisive`.

The only admitted shape is stricter: a calibrated, pre-registered meter must
change the TaF verdict while coherence, redundancy, access, and reversal-success
statistics are fixed. No real platform in the repo currently supplies that
meter, so T12 remains blocked rather than upgraded.

## T94 Result

[T94](../tests/T94-weak-measurement-priority-demotion.md) turns the accumulated
weak-measurement obstruction chain into a route-selection rule.

Detector provenance remains blocked but still executable on a named
instrumentation path: source-anchored stack, pre-registered raw-log protocol,
and isolated rescue witnesses under hostile ambiguity. Weak measurement is in a
worse state. After T91 and T93, it has no real platform with a pre-registered
independent branch, provenance, or undo-cost axis.

The roadmap consequence is now explicit rather than conditional:

```text
detector provenance stays ahead;
weak measurement is reinstated only after a real platform clears the
independent-axis gate.
```

## T100 Result

[T100](../tests/T100-detector-authority-domain-bound.md) upgrades the recent
detector-governance narrowing from staffing examples to a complete finite
enumeration over the five T97 authority domains.

The result is exact rather than suggestive:

```text
minimum admissible authority domains = 4
```

No partition with three or fewer authority domains survives once trust-auditor
independence and governance/control/archive separation are enforced. There are
exactly three minimal four-domain merge classes, each merging instrument
operation with exactly one of governance, control design, or archive custody,
while trust auditing remains separate.

This narrows detector provenance again. Under the current T97/T98 packet, a
small-lab future deployment is not merely difficult; it is structurally
inadmissible unless the packet itself changes.

## Contribution Needed

Two concrete needs remain, and the detector-side one is now stronger than the
weak-measurement one.

For detector provenance, obtain one concrete deployment that satisfies T78 and
publish its raw event-level logs: event loss, signature verification failures,
replay/spoof tests, perturbation trials, trust-boundary audits, and DAG
truncation exports. If only dashboard summaries are available, withhold the
detector branch rather than treating it as empirical support.

For weak measurement, stop treating standard homodyne, uncollapse, or
quantum-jump-reversal platforms as near-ready T12 tests. T94 makes the
priority consequence explicit: T12 is now demoted below the detector-
provenance route in the active roadmap. Reinstate it only if a monitored
platform can name either a duplicated-record provenance channel during
monitoring or a calibrated undo-cost meter satisfying T93: fixed before
analysis, independent of the monitored record and control schedule, and not
conditioned on reversal success.
