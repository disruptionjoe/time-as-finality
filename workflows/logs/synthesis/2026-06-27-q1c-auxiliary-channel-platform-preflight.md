---
document_type: synthesis_preflight
batch_item: third_batch_task_3
status: complete
authority: non_authoritative
write_scope: workflows/logs/synthesis
claim_effect: none
---

# Q1C Auxiliary-Channel Platform Preflight

## Scope

This note completes third-batch task 3 from
`workflows/logs/best-next-move/2026-06-27-third-10-research-orchestration.md`.
It is a synthesis/preflight artifact only. It does not update
`CLAIM-LEDGER.md`, `ROADMAP.md`, tests, results, models, README, or
open-problem files.

This preflight does not supply weak-measurement evidence. It freezes the
platform packet burden that a future named monitored platform must satisfy
before Q1C can be treated as live again.

## Grounding Readout

Read surfaces used:

- `open-problems/q1c-auxiliary-channel-platform-handoff.md`.
- `CLAIM-LEDGER.md` Q1 and Q1C rows.
- Q1C platform context from T146, T149, T150, T158, T166, T182, and T183, as
  named by the orchestration file and handoff.

Current baseline:

- Q1 remains `demoted` as a roadmap umbrella.
- Q1C remains `dormant`.
- Weak measurement is reinstatement-only.
- A second meter or auxiliary readout is not enough. A platform must freeze the
  full ordinary event-level record, the auxiliary channel, an independently
  typed TaF axis, a fixed verdict map, a support floor, a loss rule, and a live
  architecture class before analysis.

## Frozen Packet Burden

A Q1C platform packet is admissible only if it freezes the following tuple:

```text
R, A, H, V = g(H), L
```

where:

- `R` is the full ordinary event-level monitored record, not a dashboard,
  thresholded export, or coarse summary.
- `A` is the auxiliary channel schema, including calibration and event
  alignment.
- `H` is an independently typed TaF axis, not a label defined by the auxiliary
  meter.
- `V = g(H)` is a fixed verdict map declared before results are inspected.
- `L` is the declared loss rule for predicting `V` from `R` alone and from
  `(R, A)`.

The packet must also freeze:

1. The class-support floor for every verdict class.
2. The architecture class:
   - extra environment or detector structure not screened off by `R`; or
   - explicit instrument enlargement with a preserved comparison target.
3. Null controls for coarse-record refinement, postselection,
   auxiliary-defined labels, rare-target partitions, screened-off auxiliaries,
   and same-instrument underdeclaration.
4. If the instrument is enlarged, an eventwise back-projection from the enlarged
   data to the full ordinary standard record.

Packets that do not freeze these fields are scaffold-only or null for Q1C.

## Platform Audit Checklist

| Field | Required content | Reject if |
| --- | --- | --- |
| `platform_id` | Named monitored quantum platform and responsible group. | The packet is an abstract meter family only. |
| `R_schema` | Full ordinary event-level monitored transcript. | `R` is a dashboard, thresholded export, or coarse summary. |
| `A_schema` | Auxiliary channel with calibration and event alignment. | `A` is a downstream transform of `R`. |
| `architecture_class` | Extra environment/detector structure or enlarged instrument with preserved target. | The same instrument is relabeled without extra structure. |
| `H_axis` | Independently typed TaF axis. | The axis is defined by the auxiliary meter or post hoc target. |
| `V_map` | Fixed `V = g(H)` verdict map. | Verdict labels are chosen after analysis. |
| `support_floor` | Nontrivial support requirement for every verdict class. | Lift exists only on a vanishingly rare class. |
| `loss_rule` | Predeclared rule comparing predictions from `R` and `(R, A)`. | The scoring rule is selected after seeing lift. |
| `back_projection` | For enlarged instruments, eventwise projection to full ordinary `R`. | The preserved target is coarse or drifts by event. |
| `event_level_audit` | Rows sufficient to test conditional sufficiency and target honesty. | Only aggregate summaries are exposed. |

## Required Event-Level Screens

After the packet is frozen and data are available, the platform must expose
enough event-level detail to audit:

1. Whether `A` is conditionally determined by `R`.
2. Whether apparent lift survives when `R` is the full ordinary event-level
   transcript.
3. Whether `H` was typed independently of `A`.
4. Whether `V = g(H)` was fixed before results.
5. Whether every verdict class meets the support floor without post hoc
   partition surgery.
6. Whether any positive lift targets verdict risk rather than auxiliary echo.
7. Whether an enlarged-instrument proposal preserved the comparison target.
8. Whether the preserved target is the full ordinary standard record.
9. Whether the back-projection lets the standard target drift on admissible
   events.

If these checks cannot be run at event level, the platform does not reopen Q1C.

## Null And Demotion Conditions

Treat the route as null for Q1C, or demote it to scaffold-only, if any of the
following occur:

- No named monitored platform packet exists.
- `R` is only a dashboard, coarse summary, thresholded transcript, or incomplete
  ordinary record.
- `A` is conditionally determined by `R` or is a downstream transform of the
  ordinary transcript.
- `H` is typed from the auxiliary channel instead of independently.
- `V` is defined directly from the auxiliary meter.
- The verdict target or loss rule is chosen after analysis.
- The reported lift exists only on a vanishingly rare verdict class.
- The route relies on postselection or post hoc class partitioning.
- The same instrument is relabeled without naming extra environment structure
  or explicit instrument enlargement.
- Instrument enlargement lacks a preserved comparison target.
- Instrument enlargement lacks eventwise back-projection to the full ordinary
  standard record.
- The claimed preserved target is only a coarse summary or drifts under the
  back-projection.
- Event-level rows are withheld and replaced by aggregate summaries.
- The positive lift disappears when standard monitored statistics are treated as
  the full event-level transcript.

Without a named packet satisfying the full stack, Q1C remains `dormant`.

## Acceptance Criteria

This preflight satisfies the third-batch task by:

- Freezing the `R, A, H, V, L` packet burden.
- Requiring the full ordinary event-level record rather than dashboards or
  summaries.
- Blocking auxiliary-defined verdicts, rare-target partitions, postselected
  lifts, screened-off auxiliary channels, same-instrument relabeling, and
  enlarged instruments without preserved full-record targets.
- Keeping Q1C dormant unless a named platform packet clears the T166-style
  intake and later survives the T149/T150/T158/T183 event-level screens.

## Next Executable Artifact Shape

The next non-null artifact should be a named platform packet with enough
event-level commitments to run the screens. Its minimum shape is:

```text
q1c_auxiliary_platform_packet:
  platform_id:
  responsible_group:
  R_schema:
  A_schema:
  A_calibration_and_alignment:
  architecture_class:
  H_axis:
  verdict_map_V_equals_g_H:
  support_floor:
  loss_rule_L:
  null_control_plan:
  event_level_release_plan:
  conditional_sufficiency_test:
  typed_verdict_lift_test:
  preserved_target_test:
  back_projection:
  demotion_rule:
```

The executable follow-on should first validate the frozen packet. Only after
that should it score whether `(R, A)` gives positive predeclared verdict-risk
lift over full `R` alone without verdict gerrymandering or screened-off
auxiliary content.

## No-Promotion Guardrails

- Do not cite this preflight as weak-measurement evidence, Q1C support, or a
  platform result.
- Do not promote Q1C above `dormant` without a named platform packet and
  event-level positive verdict-risk lift over full `R`.
- Do not treat a second meter, alternate readout chain, or auxiliary dashboard
  as a Q1C route by itself.
- Do not accept auxiliary-defined, rare-target, postselected, screened-off, or
  coarse-record lifts as branch progress.
- Do not edit `CLAIM-LEDGER.md`, `ROADMAP.md`, tests, results, models, README,
  or open-problem files from this synthesis note.
