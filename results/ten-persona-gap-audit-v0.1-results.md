# T387 Results: Ten-Persona Gap Audit

## Verdict

The ladder is not obviously broken, but it is still conditional.

The ten-persona pass found no justification for a claim upgrade. It did find a
clear next target:

```text
derive or falsify why compatibility should mean mutual local attestability
```

## Ten Lenses

| persona | main concern |
|---|---|
| mathematical formalist | Compatibility needs a theorem-ready semantics, not only a useful reading. |
| relativity physicist | Two protocol legs are not automatically null directions with a bilinear interval. |
| distributed systems engineer | Acknowledgment semantics are not the same thing as compatibility semantics. |
| category/sheaf theorist | Pairwise attestations may not glue across overlaps. |
| information theorist | The invariant signal unit and capacity bound are still granted. |
| gauge/coordinate auditor | Hidden foliations and relabel equivalences need explicit controls. |
| adversarial/security reviewer | Receipts can be spoofed, replayed, or forged. |
| minimality/model-selection auditor | Minimality is doing real work and needs its own origin. |
| experimental/falsification designer | The next screen needs sharper positive controls for mutuality. |
| paper reviewer | The claim ledger needs derived, motivated, imported, and open objects separated. |

## Top Missing Objects

| priority | gap | plain-English issue |
|---|---|---|
| 1 | `mutual_attestability_semantics_origin` | T386 depends on compatibility meaning mutual local attestability. That is now the main open object. |
| 2 | `nullness_bilinearity_origin` | A two-leg protocol does not by itself derive nullness or bilinear interval structure. |
| 3 | `two_leg_to_null_signal_bridge` | The bridge from protocol legs to null signal directions is still fragile. |
| 4 | `minimality_principle_origin` | Minimality selects the clean result, but minimality itself is not derived. |
| 5 | `local_to_global_attestation_descent` | Pairwise attestations may not glue into a consistent multi-observer structure. |

## Other Important Gaps

- `higher_dimensional_extension`: the current ladder is mostly 1+1.
- `failure_mode_semantics`: timeout, retry, duplication, and dropped-return controls are missing.
- `gauge_relabel_equivalence_proof`: relabel-only structure needs a quotient/invariance proof.
- `hidden_foliation_and_coordinate_import`: implicit counters or queues may smuggle in global order.
- `signal_unit_capacity_origin`: the shared signal unit remains granted.
- `attestation_authenticity`: spoofed or replayed receipts can fake mutuality.
- `catalog_completeness_boundary`: the screens are targeted catalogs, not exhaustive classifications.

## Recommended Next Goal

```text
T388 mutual-attestability semantics origin screen: test whether record-finality
compatibility requires mutual local attestability, with controls for scalar
tokens, symmetric labels, one-sided readout, global reconciliation, spoofed
receipts, and asymmetric persistence.
```

## Claim Ledger Update

Register T387 as:

```text
ten_persona_audit_finds_no_claim_upgrade_but_prioritizes_mutual_attestability_semantics
```
