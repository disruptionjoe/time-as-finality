# P96 Run - Reconstruction Debt Spine Formalist

- timestamp: 2026-06-20T14:39:30-05:00
- goal_id: P96
- selected_persona: Reconstruction Debt Spine Formalist
- selected_goal: Test whether "reconstruction debt under admissibility constraints" is a deeper organizing object than D1, LossKernel, provenance, access boundaries, or finality separately.
- bounded_question: Can the constellation convergence be stated as a small formal object with inputs, outputs, failure modes, negative controls, and immediate next tests?

## Repo Context Read

- [`/Github Repos/time-as-finality/explorations/research-constellation-orchestrator-2026-06-20.md`](</Github Repos/time-as-finality/explorations/research-constellation-orchestrator-2026-06-20.md>)
- [`/Github Repos/time-as-finality/workflows/explore/research-constellation-orchestrator.md`](</Github Repos/time-as-finality/workflows/explore/research-constellation-orchestrator.md>)
- [`/Github Repos/time-as-finality/open-problems/loss-kernel-formalization.md`](</Github Repos/time-as-finality/open-problems/loss-kernel-formalization.md>)
- [`/Github Repos/time-as-finality/open-problems/obstruction-relocation-reconstruction-debt.md`](</Github Repos/time-as-finality/open-problems/obstruction-relocation-reconstruction-debt.md>)
- [`/Github Repos/time-as-finality/tests/T99-losskernel-quotient-separation.md`](</Github Repos/time-as-finality/tests/T99-losskernel-quotient-separation.md>)
- [`/Github Repos/time-as-finality/models/losskernel_quotient_separation.py`](</Github Repos/time-as-finality/models/losskernel_quotient_separation.py>)
- [`/Github Repos/time-as-finality/explorations/recurring-structure-map-v0.1.md`](</Github Repos/time-as-finality/explorations/recurring-structure-map-v0.1.md>)
- [`/Github Repos/time-as-finality/explorations/persona-future-run-goals-2026-06-20.md`](</Github Repos/time-as-finality/explorations/persona-future-run-goals-2026-06-20.md>)

## Drafted Goal

### P96 - Reconstruction Debt Spine Formalist

- status: done
- last_run: 2026-06-20T14:39:30-05:00
- artifact: explorations/persona-goal-runs/2026-06-20-143930-p96-reconstruction-debt-spine-formalist.md
- goal: Formalize the constellation signal "witnesses -> obligations -> admissibility -> reconstruction debt" as a candidate spine object, then test whether it explains LossKernel, detector provenance, aggregation, access boundaries, and finality without collapsing into commentary.
- ambition: Decide whether reconstruction debt under admissibility constraints is a deeper organizing object worth promoting to the next executable audit, or only a useful synthesis phrase.

## Work Performed

1. Read the constellation output and confirmed that the repeated cross-room pattern was:

   ```text
   information-losing transformation
     -> admissibility boundary
     -> witness obligation
     -> reconstruction debt
     -> observer- or scale-indexed finality verdict
   ```

2. Read T99 and its model to see what already exists executably. T99 shows label-only LossKernel fails the quotient gate and that source-anchored witness obligations conditionally rescue separation.
3. Read the obstruction-relocation open problem to locate the current status of reconstruction debt: open formal target, not conservation law.
4. Compared the proposed spine against P79, P81, P89, P91, P93, P94, and P95. Those are useful subgoals, but none states the candidate object that unifies them.

## Candidate Object

### Reconstruction Debt Under Admissibility Constraints

For a task, observer, or scale `O`; an information-losing map or restriction `f: S -> T`; and a target reconstruction problem `R`, define:

```text
Debt_O,R(f) =
  unmet admissible witness obligations needed to reconstruct, attribute,
  certify, or safely use target structure after f
```

A minimal data shape:

```text
ReconstructionDebtCase =
  source_structure
  target_structure
  transformation_or_access_boundary
  target_task
  admissibility_policy
  required_witness_obligations
  available_witnesses
  discharged_obligations
  unmet_obligations
  debt_measure
  finality_or_attribution_verdict
```

The object is not just "lost information." It is task-indexed and policy-indexed:

```text
loss only matters when it creates an unmet obligation
for a target reconstruction or use task
under an admissibility rule.
```

## Mapping Existing Branches Into The Object

| Branch | Current object | Reconstruction-debt reading |
| --- | --- | --- |
| LossKernel / T99 | source-anchored typed loss witness | Lost witness creates debt only if it resolves a target obstruction and is admissible for the target task. |
| Detector provenance / T87 | event-level raw-log contract | Missing raw log, challenge, authority, or ancestry evidence creates debt before detector records can be admitted. |
| Access boundaries / T19-T89-T92 | inaccessible witness gap | Witness may exist globally but remain unavailable to the bounded observer, leaving observer-indexed debt. |
| Aggregation / P91-P92 | macro-record from subgraph | Compression creates debt when micro-witnesses needed for later attribution are discarded. |
| Typed access / P94 | physical, causal, cryptographic, institutional, cognitive boundaries | Each access type changes which witnesses are admissible, not merely which records are visible. |
| Finality / D1 | observer-indexed finality profile | A finality verdict can be read as "debt acceptable enough for this observer/task/scale," not as truth or complete reconstruction. |

## Immediate Test Against T99

T99 already supplies the core positive and negative shape.

Positive fixture:

```text
same source
same target
same ordinary composite map
same endpoint behavior
same naive lost-label set
different source-anchored witness obligation
=> different attribution verdict
```

Debt reading:

```text
required obligation = source witness that resolves target_branch_ambiguity
available witness in relevant path = signed_preimage_selector
available witness in decorative path = display_color_tag
debt differs even though naive loss labels match
```

This supports the candidate object better than label-only LossKernel because the decisive quantity is not the lost label. It is whether an admissible witness obligation remains unmet.

Negative control shape:

```text
lost source structure irrelevant to target task
or non-admissible for target reconstruction
=> no meaningful reconstruction debt
```

This is the critical guardrail. Without this negative control, "reconstruction debt" would become a name for any loss and would fail as mathematics.

## What This Explains Better Than Current Objects

### Better than D1 alone

D1 describes finality coordinates, but it does not by itself say what missing witness makes a verdict unsafe. Reconstruction debt gives a reason a D1-like verdict is withheld, demoted, or task-relative.

### Better than label-only LossKernel

T99 shows label-only LossKernel fails the quotient gate. Reconstruction debt requires a witness obligation and an admissibility policy, which prevents decorative labels from counting.

### Better than provenance alone

Provenance records ancestry. Reconstruction debt asks whether that ancestry discharges the witness obligation for the target task. A complete-looking ancestry record can still fail if it lacks the right challenge, authority, or admissibility property.

### Better than access alone

Access says what can be reached. Reconstruction debt asks what remains unresolved because the needed witness is outside the access boundary or fails the access type.

### Better than finality alone

Finality can become a verdict over tolerated debt:

```text
final_for(O, R) iff Debt_O,R(f) is empty or admissibly bounded
```

That is safer than treating finality as truth, stability, or record count.

## Failure Modes

This candidate object should be rejected or demoted if:

1. Debt cannot be measured without simply reading LossKernel labels back into the answer.
2. Every loss automatically becomes debt.
3. Admissibility policies are unconstrained and chosen post hoc.
4. Standard provenance, effects, view-update, abstract interpretation, or information theory fully captures the object with no residual.
5. The object cannot produce negative controls where loss occurs but no debt remains.
6. Debt cannot change any attribution, reconstruction, or finality verdict in a finite witness family.

## Candidate Measures

Start finite and non-grandiose:

```text
debt_count = number of unmet admissible witness obligations
debt_types = typed set of unmet obligations
ambiguity_count = number of compatible reconstructions remaining
non_uniqueness = ambiguity_count > 1
debt_severity = lexicographic class:
  none < decorative < task_relevant < obstruction_resolving < safety_critical
```

Only after these work should entropy, coding cost, or rate-distortion language be used.

## Recommended Next Executable Audit

Build a bounded test tentatively named with the next free test id:

```text
Reconstruction Debt Spine Audit
```

Minimum cases:

1. **T99 LossKernel quotient case:** label-only loss equal, witness debt different.
2. **Detector raw-log case:** dashboard summary present, challenge/authority witness missing.
3. **Access-boundary case:** witness exists globally, inaccessible to observer.
4. **Aggregation case:** macro-record preserves constraint but discards later-needed micro-witness.
5. **Negative control:** loss occurs, but lost structure is irrelevant or non-admissible for target task, so no debt remains.

Acceptance criteria:

- Each case has explicit `required_witness_obligations`.
- Each case has explicit `available_witnesses`.
- Debt is computed before the verdict.
- At least one positive case changes verdict because debt differs.
- At least one negative control has non-empty loss but zero meaningful debt.

## Result

Bounded-run verdict: promote this as the next candidate spine to test, but only as an executable audit target.

The constellation signal should not be canonized yet. It is strong enough to shape the next test because it compresses several branches:

```text
LossKernel = loss-side witness accounting
provenance = evidence graph for discharging obligations
access boundary = observer-relative witness availability
aggregation = scale-relative witness preservation or deletion
finality = verdict over acceptable unresolved debt
```

The key research move is to try to break this compression with negative controls and prior-art comparison.

## Claim-Status Posture

- No claim status changes.
- TF1 remains an `open_formal_target`.
- Reconstruction debt remains an open formal target, not a theorem.
- D1, Q1, and LossKernel should not be rewritten yet.
- The next legitimate promotion is a finite executable audit, not roadmap or claim-language expansion.
