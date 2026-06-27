---
document_type: synthesis_status
batch_item: seventh_20_task_1
status: complete
authority: non_authoritative
write_scope: workflows/logs/synthesis
claim_effect: none
---

# T183 Q1C Reinstatement Stack Intake

## Status

This is a status/intake note only. It does not reopen Q1C.

## Sources read

- `tests/T183-weak-measurement-reinstatement-stack.md`
- `results/weak-measurement-reinstatement-stack-v0.1-results.md`
- `workflows/logs/synthesis/2026-06-27-n9-t182-q1c-named-platform-family-census-preflight.md`

## Plain-English finding

Q1C is not "almost reopened" when one local gate passes. A future platform must
clear the whole stack at once.

## Technical conclusion

T183 composes the live Q1C obligations into one proposal-level screen:

- T166 packet intake.
- Architecture consistency.
- T149/T150 typed verdict lift.
- T158 preserved-target honesty for enlarged instruments.

Packet-only promises, zero-lift packets, auxiliary-defined verdicts,
target-drift enlarged instruments, coarse-record packets, and the current
frontier remain blocked. Q1C stays `dormant`.

## Minimum next task

Use the T183 stack as the first-page checklist for any named Q1C platform. Do
not score a local positive control until the full stack is filled.

## Stop condition

Stop Q1C work if the candidate lacks event-level verdict data, changes the
ordinary record, defines the verdict through the auxiliary channel itself, or
cannot preserve the comparison target under enlargement.

