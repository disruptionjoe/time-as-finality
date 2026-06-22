---
report: five-workflow-governance-review
run_at: 2026-06-21T19:08:11-05:00
status: complete
scope: five inert research-machine workflow definitions
automation_trigger_changes: none
---

# Five Workflow Governance Review

## Review Question

Review the five inert, protocol-level workflow definitions against five quality
checks:

1. explicit stopping condition;
2. bounded artifact;
3. success versus noise distinction;
4. overclaim protection;
5. ability to weaken claims, not just generate more work.

This review did not inspect or edit automation trigger/spec files.

## Findings

| Workflow | Initial assessment | Edit made |
|---|---|---|
| `exploit/contradiction-hunter` | Strong on bounded claim cluster, critic independence, routing, and claim weakening. Stopping condition was present but implicit. | Added explicit governance review gate with stop condition, bounded report, success/noise split, overclaim guard, and claim weakening rule. |
| `explore/motif-census-emergence-detector` | Strong on motif-role classification and demotion, but the success/noise boundary needed to be more visible. | Added review gate distinguishing role-stable recurrence from term-frequency noise and requiring `could_be_definition_if` / `demote_if`. |
| `govern/theory-compression-engine` | Strong on decompression testing and non-canonical compression posture. Needed explicit stop and failed-compression handling. | Added review gate requiring one theory slice, one compression report, lost-structure review, and failed/overcompressed labels. |
| `explore/cross-repo-bridge-builder` | Strong on operation comparison and false analogy. Needed a harder boundedness rule for bridge sprawl. | Added review gate requiring one bridge question, exactly one proposed bridge test, and explicit metaphor-collapse path. |
| `govern/theory-tournament` | Strong on lead-as-routing-proposal and minority preservation. Needed the five checklist items stated directly. | Added review gate requiring one corpus/interpretation set, a bounded report, loss conditions, and challenge routing. |

## Result

All five workflows now expose the five governance checks directly in the spec
body. The review did not convert them into automation targets, schedules, or
trigger mappings.

The most important preservation is unchanged:

> These remain inert, protocol-level workflow definitions.

## Remaining Considerations

Future manual runs should verify whether the gates are actually followed. If a
workflow repeatedly produces useful artifacts and passes the review gate across
several runs, automation can be considered later as a separate governance
decision. Until then, keeping the definitions inert is the safer posture.
