---
document_type: synthesis_audit_checklist
created: 2026-06-27
status: complete
authority: guidance_only
write_scope: workflows/logs/synthesis
claim_updates: none
---

# LossKernel Normal-Form Integration Checklist

## Status

This is a non-authoritative synthesis artifact for queue item 1 in
`workflows/logs/best-next-move/2026-06-27-next-10-research-orchestration.md`.
It does not update `CLAIM-LEDGER.md`, `ROADMAP.md`, tests, results, code, or
open-problem text.

Working verdict: LossKernel/WO survives as a neighbor-reconstructible audit
normal form. It does not survive here as a prior-art-separated target, a TF1
promotion path, or a new-object claim.

## Read Surfaces Used

- `ROADMAP.md` Mathematical Spine, especially the post-T127/T220 LossKernel
  narrowing.
- `CLAIM-LEDGER.md` Canon Index, TF1 row, CSP-PO1 row, and 2026-06-24 /
  2026-06-26 change-log entries.
- `open-problems/loss-kernel-formalization.md`.
- `open-problems/loss-kernel-witness-obligation-normal-form.md`.
- `tests/T220-losskernel-obligation-factorization-certificate.md`.
- `results/losskernel-obligation-factorization-v0.1-results.md`.

## Baseline To Preserve

The baseline is fixed by T220 and the 2026-06-26 ledger pass:

```text
obligation = psi . nu
```

Here `nu` is the neighbor-visible data map and `obligation` is the canonical
witness-obligation normal form. Because the obligation factors through `nu`, it
is constant on each `nu` fiber. Same-neighbor-data cases therefore collapse to
the same obligation and the same attribution verdict in the canonical regime.

The hidden-source escape remains only a non-factoring escape: it reads source
data outside the current neighbor-visible package. The current repo posture is
that once such a field is named as legitimate audit data, mature neighbor
machinery can absorb it by enlarging the neighbor package.

## Checklist

| Field | Required content | Neighbor absorber mapping | Fail if |
| --- | --- | --- | --- |
| `target_judgment` | Names the exact verdict or settlement question under audit. | CSP verdict, PO1 admissibility, provenance verdict, effect judgment, lens reconstruction target. | The judgment is implicit or changes during the audit. |
| `nu_signature` | Freezes the neighbor-visible data available to mature frameworks. | CSP explanation, why-not provenance, abstract interpretation state, lens view, effect annotations, path/category data. | Any claimed separation hides a difference already present in `nu`. |
| `source_fiber_class` | Names the source lifts over the same `nu` value. | Provenance and audit machinery treat these as same-neighbor-data cases. | The pair differs in endpoint behavior, composite map, target satisfiability, or admitted neighbor data. |
| `obligation_generators` | Lists the smallest source-derived witnesses needed to settle the target judgment. | Why-not provenance, abstract interpretation explanations, effect rows, lens complements, CSP certificates. | Generators are author labels rather than derived obligations. |
| `realization_map` | Shows how `obligation` is reconstructed from `nu`, i.e. `psi(nu)`. | Mature absorber owns the same data after the package is granted. | Reconstruction needs hidden source data while still being described as same-neighbor-data. |
| `fiber_constancy_probe` | Checks whether every case in a `nu` fiber receives the same obligation and verdict. | Same-neighbor-data collapse gate. | A separation is reported without first proving the `nu` signatures identical. |
| `hidden_source_probe` | Records any non-factoring field and whether adding it to `nu'` absorbs the split. | Audit/provenance/effect/lens packages with the named source field admitted. | A hidden-source split is called prior-art-separated before the `nu'` absorption attempt. |
| `absorbed_vs_live` | Classifies the obligation as absorbed, audit-useful, or live only under a named missing absorber. | CSP/provenance/effect/lens/abstract-interpretation/audit comparison. | The note moves directly from "useful checklist" to claim promotion. |

## Safe Language

- "certified canonical normal form"
- "neighbor-reconstructible audit vocabulary"
- "collapse into neighbor-visible data in the canonical regime"
- "same-neighbor-data route retired as a live TF1 novelty path"
- "finite witness with explicit scope guards"
- "useful for admissibility review, comparison, and hostile audit"
- "non-factoring hidden-source escape, not currently live as prior-art
  separation"

## Blocked Language

- "TF1 is promoted"
- "LossKernel is a new mathematical object"
- "LossKernel is prior-art separated"
- "same-neighbor-data separation remains the default rescue path"
- "T220 proves impossibility outside the canonical construction"
- "hidden source data gives novelty before a `nu'` absorption attempt"
- "closed in all future formulations"
- any public-facing claim that drops the finite, constructed, and
  absorber-admissibility scope guards

## Future Non-Factoring Route Admission Gate

A future non-factoring source-field route is admissible for testing only if all
of the following are true before any upgrade language is used:

1. The source field is defined before looking at the target verdict split.
2. The source field is not reconstructible from the frozen `nu` signature.
3. The candidate pair shares the full frozen `nu` signature, endpoint behavior,
   composite map, and target-side satisfiability profile.
4. The obligation is derived by a repeatable rule, not attached as prose
   metadata.
5. The audit explicitly grants the named source field to provenance, effect,
   lens, abstract-interpretation, CSP explanation, and audit machinery as `nu'`.
6. The split still survives that `nu'` absorption attempt.
7. A negative control shows the harness can report collapse when the source
   field is absorbed.

Current status against that gate: not satisfied. T108, T127, T220, and the
2026-06-26 ledger pass all point the other way for the present canonical
construction.

## Acceptance Criteria Satisfaction

| Criterion from queue item 1 | Satisfied here |
| --- | --- |
| States `obligation = psi . nu` and same-neighbor-data collapse as baseline. | Yes: see Baseline To Preserve. |
| Lists safe language, blocked language, and future non-factoring admissibility conditions. | Yes: see Safe Language, Blocked Language, and Future Non-Factoring Route Admission Gate. |
| Maps checklist fields to mature absorbers: CSP/provenance/effect/lens/abstract-interpretation/audit machinery. | Yes: see Checklist table. |
| Contains no TF1 promotion, no new-object claim, and no promoted general-result language. | Yes: all status language is narrowed, finite, and audit-facing. |

## No-Claim-Promotion Guardrail

This checklist may be used to make future LossKernel work cleaner and harder to
overclaim. It does not authorize any ledger edit, roadmap edit, claim upgrade,
new public-facing claim, or reopening of the same-neighbor-data route.
