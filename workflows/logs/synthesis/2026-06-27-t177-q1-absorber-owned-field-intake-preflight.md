---
document_type: synthesis_preflight
batch_item: sixth_15_task_1
status: complete
authority: non_authoritative
write_scope: workflows/logs/synthesis
claim_effect: none
---

# T177 Q1 Absorber-Owned Field Intake Preflight

## Status

Preflight only. This note does not change Q1, its child claims, tests, models,
results, or ledger rows.

## Sources read

- `tests/T177-q1-absorber-owned-field-intake.md`
- Existing Q1 synthesis notes for Q1A, Q1B, Q1C, and Q1D under
  `workflows/logs/synthesis/`

## Plain-English finding

Most false Q1 reopenings can be blocked before branch-specific work starts:
they are not new quantum-finality evidence if they win only by changing the
owned absorber fields.

## Technical conclusion

T177 should be treated as the pre-branch intake screen. It rejects:

- Q1A proposals that change SBS, strong-QD, or provenance closure fields instead
  of splitting D1 at the same closure key.
- Q1B proposals without the current deployment, reviewable-row, five-domain,
  mandatory-quorum, freeze, and successor-policy burdens.
- Q1C proposals without a T166-style packet, typed positive verdict-risk lift,
  and a fixed ordinary event-level record.
- Q1D proposals that use signalling, hidden-variable retrofits, or premature
  joint-correlation language.

The screen is not a no-go theorem for quantum measurement. Its value is intake
discipline: it prevents absorber-owned changes from being counted as TaF
residue.

## Minimum next task

Run or rerun the T177 executable pair:

```text
python -m unittest tests.test_q1_absorber_owned_field_intake -v
python -m models.run_t177
```

Then add only a status note if the current branch-specific gates are unchanged.

## Stop condition

Stop any Q1 branch reopening if the proposal changes its closure key, detector
governance, ordinary record, comparison target, or correlation-record stage
instead of holding the owned fields fixed.

