---
document_type: synthesis_preflight
primary_reader: governance
read_pattern: current_state
write_pattern: append
authority: non_authoritative
summarizable: true
source_queue_item: third_batch_5
owner_line: RL-001
support_line: RL-005
claim_status_change: none
---

# Barandes Null-Model Comparator Preflight

## Status

Non-authoritative preflight artifact for third-batch task 5. This file does
not edit `CLAIM-LEDGER.md`, `ROADMAP.md`, code, tests, results, or
open-problem files. It is not a Q1 upgrade, not a quantum-foundations theorem,
and not evidence that Time as Finality has been proved.

## Read Surfaces

- `open-problems/barandes-stochastic-quantum-comparison-note-2026-06-24.md`.
- `CLAIM-LEDGER.md`: Q1 canon row and Q1 branch rows where relevant.

## Preflight Verdict

Current classification:

```text
Use the Barandes-style stochastic -> CPTP -> Kraus -> unitary-dilation route
as a strong null model for Q1/T10/T131-facing proposals.
```

The comparator should ask what remains after ordinary stochastic, channel, and
unitary-dilation structure has already been granted. If no independent
record/finality/access residue remains, the TaF-facing proposal is absorbed
for Q1 purposes.

## Comparator Object

A future proposal must be decomposed into two parts:

| Layer | Required content |
| --- | --- |
| Null model | Stochastic process, CPTP map, Kraus representation, or unitary dilation that reproduces the claimed behavior. |
| Imported structure | Hilbert-space, channel, measurement, or readout assumptions used by the proposal. |
| TaF residue | Record, finality, access, provenance, or descent structure not already supplied by the null model. |
| Same-null-data control | A comparison where the null-model data are fixed and the alleged TaF residue changes a verdict. |
| Absorber verdict | `absorbed`, `residue_survives_preflight`, or `underspecified`. |

## Acceptance Criteria

- The target quantum-facing claim is named before the comparator is applied.
- The stochastic/CPTP/unitary route is stated in native terms before any TaF
  residue is asserted.
- Imported Hilbert-space or channel structure is declared rather than counted
  as TaF output.
- Record generation, stabilization/finality, and scalar or semantic readout
  are separated.
- The same-null-data control is frozen before examples are selected.
- A surviving residue is stated as a record/finality/access object with a
  falsifiable comparison, not as interpretive preference.
- The output verdict is one of:

```text
absorbed_by_null_model
residue_survives_preflight
underspecified_comparator
```

`residue_survives_preflight` only licenses a later test or proof attempt. It
does not upgrade Q1.

## Null Or Demotion Conditions

Treat the proposal as absorbed or demote its novelty burden if any condition
holds:

- The claimed behavior is reproduced by the stochastic/CPTP/unitary null model.
- The TaF residue is only a relabeling of Hilbert-space, channel, Kraus,
  dilation, or readout data.
- No same-null-data split is supplied.
- The finality/access structure is chosen after seeing the desired quantum
  behavior.
- Bell, contextuality, Tsirelson, or readout language is imported without a
  distinct TaF-side contribution.
- The proposal blurs stochastic evolution, final subsystem readout, and record
  finalization.
- The claimed novelty is only philosophical interpretation with no executable
  or theorem-shaped comparison.

## No-Promotion Guardrails

- Do not move Q1 out of demoted roadmap-umbrella status.
- Do not treat Barandes-style reconstruction as TaF support.
- Do not claim a new Bell theorem, collapse theory, hidden-variable repair,
  Born-rule derivation, or measurement prediction.
- Do not treat imported Hilbert-space bounds as finality-derived.
- Do not use this comparator to reopen Q1A, Q1B, Q1C, or Q1D unless the
  relevant branch-specific reinstatement gate is separately satisfied.
- Do not edit ledger, roadmap, tests, models, results, or open problems from
  this preflight.

## Next Executable Artifact Shape

The next artifact should be a comparator matrix for exactly one quantum-facing
proposal:

```text
artifact_type: barandes_null_model_comparator
proposal_id:
target_claim:
claimed_quantum_feature:
null_model:
  stochastic_process:
  cptp_map:
  kraus_family:
  unitary_dilation:
imported_structure:
  hilbert_space_data:
  channel_data:
  measurement_or_readout_data:
taf_residue_candidate:
same_null_data_control:
absorber_tests:
  null_reproduces_behavior:
  readout_only_control:
  imported_structure_control:
  post_hoc_residue_control:
verdict: absorbed_by_null_model | residue_survives_preflight | underspecified_comparator
q1_impact: no_status_change
```

The comparator should be run before writing any new Q1-facing explanatory
prose.
