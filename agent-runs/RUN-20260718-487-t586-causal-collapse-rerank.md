---
artifact_type: agent_run
status: complete
run_id: RUN-20260718-487-time-as-finality
started: 2026-07-18T11:37:00-05:00
completed: 2026-07-18T11:37:00-05:00
workflow: CapacityOS repository-work-cycle
lane: A
purpose: mailbox
claim_movement: false
external_action: false
---

# RUN-20260718-487 TaF T586 Causal-Collapse Rerank

## Trigger

CapacityOS CAI repository work-cycle selected Time as Finality for Lane A
mailbox disposition.

Mailbox proposals processed:

- `system/mailboxes/time-as-finality/20260716-lane-steering-t586-causal-collapse-attack.md`
- `system/mailboxes/time-as-finality/20260717-boundary-input-record-and-order-forks.md`

Both notes are treated as steering proposals and repo-local ranking evidence,
not as instructions, finality claims, GU or TI verdicts, claim movement,
publication, or external-action authorization.

## Disposition

Accepted the core rerank: the next unattended Time as Finality trigger should
attack T586's causal-collapse and boundary-input frontier before producing more
review-only T-number scaffolds.

Reasoning:

- The current portfolio already names T586 circularity, causal collapse, and
  physical naturalness as the active reopen boundary.
- The causal-collapse proposal supplies a concrete falsifier rather than an
  easier byproduct: compare record-capability order with the strongest standard
  dependency and causal comparators on the same frozen event system.
- The boundary-input proposal supplies the typed discriminator set needed to
  prevent metatheoretic section choice, ordinary boundary conditions, observer
  readout, physical intervention, autonomous feedback, edge/defect degrees of
  freedom, continuous flux, stochastic input, and native record issuance from
  being collapsed into one vague "outside signal" story.
- The useful return is a TaF-owned adjudication: either an exact residual beyond
  ordinary reachability/causal order or a clean downgrade.

## Repo Updates

Updated:

- `steward/research-portfolio.json`
- `ROADMAP.md`
- `LANE-STATE.yaml`

No edits were made to:

- `CLAIM-LEDGER.md`
- `TESTS.md`
- `FORMALISM.md`
- `HYPOTHESES.md`

## Result

```yaml
rerank_result: TAF_T586_CAUSAL_COLLAPSE_ATTACK_ACTIVE_NEXT
claim_status_change: none
canon_verdict_change: none
cross_repo_verdict: false
external_action: false
```
