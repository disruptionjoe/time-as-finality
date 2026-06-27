---
document_type: synthesis_preflight
batch_item: sixth_15_task_2
status: complete
authority: non_authoritative
write_scope: workflows/logs/synthesis
claim_effect: none
---

# T171 Detector Row-Review Substitution Preflight

## Status

Preflight only. This note sharpens Q1B admissibility language but supplies no
detector evidence and makes no claim-status change.

## Sources read

- `tests/T171-detector-row-review-substitution-screen.md`
- `workflows/logs/synthesis/2026-06-27-q1b-federated-detector-manifest-preflight.md`

## Plain-English finding

For Q1B claim review, summaries and certificates are not enough. The reviewer
needs the actual bound event-level rows during the challenge window.

## Technical conclusion

Inside the surviving T169-style deployment class, the only row-release shape
that preserves all claim-review operations is:

```text
reviewable_full_rows_with_independent_escrow
```

The following substitutes remain scaffold-only:

- aggregate summaries;
- signed proof certificates without rows;
- private escrow with only an auditor statement;
- sampled public rows;
- delayed full rows after the challenge window closes.

The reason is operational, not rhetorical: those substitutes lose some
combination of lineage verification, event reconstruction, packet challenge,
certification, authority audit, or detector claim review.

## Minimum next task

Fold this into the Q1B packet template by making "full bound event-level rows
reviewable during the challenge window with independent escrow" a mandatory
field, not optional prose.

## Stop condition

Reject any detector deployment packet that offers proof-only, summary-only,
sampled-row, private-escrow-only, or late-release access as equivalent to full
challenge-window row review.

