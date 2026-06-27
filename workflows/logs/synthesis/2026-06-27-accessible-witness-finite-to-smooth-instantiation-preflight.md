---
document_type: synthesis_preflight
batch_item: sixth_15_task_13
status: complete
authority: non_authoritative
write_scope: workflows/logs/synthesis
claim_effect: none
---

# Accessible-Witness Finite-To-Smooth Instantiation Preflight

## Status

Preflight only. This note identifies a first bounded finite-to-smooth bridge
candidate. It does not create a smooth physics claim.

## Sources read

- `open-problems/finite-to-smooth-shadow-bridge.md`
- `open-problems/accessible-witness-gap-restriction-theorem.md`
- `tests/T92-accessible-witness-gap-restriction.md`
- `results/accessible-witness-gap-restriction-v0.1-results.md`
- `workflows/logs/synthesis/2026-06-27-accessible-witness-gap-restriction-preflight.md`

## Plain-English finding

The best first finite-to-smooth bridge is not a grand geometry claim. It is a
small comparison: take the finite accessible-witness gap and ask whether its
gap verdict survives when represented as a presheaf or sheaf over access
patches.

## Technical conclusion

T92 already supports a finite conditional statement:

```text
G(U) = A(U) - F(U)
```

restricts contravariantly for finite typed proposition-domain systems when
ambient restriction, audit monotonicity, and stable proposition typing hold.
That makes it a suitable source object for the finite-to-smooth bridge's first
bounded run:

```text
finite access patches -> presheaf/sheaf over an access-indexed base
```

The preserved capability object should be the accessible-witness gap verdict,
not a vague phenomenal label.

## Minimum next task

Build one bridge card that freezes source patches, target access base,
restriction maps, sheafification step, preserved gap object, and controls for
semantic relabeling and audit-monotonicity failure.

## Stop condition

Stop the bridge if it only translates finite labels into smooth vocabulary, if
the target sheaf adds the gap by hand, or if the gap verdict disappears under
restriction/refinement without an accounted residue.

