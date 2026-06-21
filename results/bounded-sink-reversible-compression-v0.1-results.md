# T106 Results: Bounded-Sink Reversible Compression

## Strongest claim

For the T80/T84 witness, reversible compression with a bounded sink does not rescue H7. Orderless compression is non-injective; ordered lossless export is reversible only while consuming blank sink capacity; and when the bounded sink is included and the cycle is closed, the apparent monotone decreases on the reversible return path.

## T80/T84 sequence

- Observed masks: `[[1, 0], [1, 1], [1, 0], [0, 0], [1, 0], [1, 1]]`
- Exported overwritten slots: `[[0, 0], [0, 0], [0, 0], [1, 0], [1, 1], [1, 0]]`
- Local ring support: `[1, 3, 4, 3, 2, 3]`
- Exported support: `[0, 0, 0, 1, 3, 4]`
- Accounted support: `[1, 3, 4, 4, 5, 7]`

## Compression and sink audits

| Audit | Verdict | Key data |
| --- | --- | --- |
| Undersized RLE sink | The RLE sink exhausts before the finite export history is fully encoded; compression does not supply an autonomous arrow. | capacity `3`, required `4`, exhausted index `5` |
| Exact RLE sink | The RLE sink can encode this finite export history, but only as a bounded finite resource sized for the sequence. | capacity `4`, block counts `[1, 1, 1, 2, 3, 4]` |
| Ordered stack export | reversible only with blank sink slots | injective `True`, lost bits `0.0` |
| Orderless counter compression | merges histories | injective `False`, max preimages `4`, lost bits `1.3499821432005525` |

## Closed bounded cycle

- Forward accounted support: `[0, 1, 3, 4, 4, 5, 7]`
- Full-cycle accounted support: `[0, 1, 3, 4, 4, 5, 7, 5, 4, 4, 3, 1, 0]`
- Forward accounted monotone: `True`
- Full-cycle accounted monotone: `False`
- Strict cycle monotone possible: `False`

The forward branch has monotone accounting, but the closed bounded reversible cycle does not. On a finite cycle, any scalar that is nondecreasing on every reversible edge must be constant around the cycle, so a strict finality arrow cannot live in the closed bounded state space.

## What this improved

T106 converts the T84 next-step loophole into a finite obstruction: the relevant distinction is not raw versus compressed storage, but whether the overwritten records remain reconstructable in the state space, are erased, or are hidden in an excluded environment.

## What this weakened

This further weakens H7 as a physical-arrow claim. The tested bounded reversible sink supplies at most a forward-branch resource accounting curve, not an autonomous finality direction after all degrees of freedom are included.

## Falsification condition

T106 fails if a finite bounded reversible compressor over the same T80 exported-slot family gives a strict D1-relevant monotone on the closed full state space without erasure, excluded history, fresh blank capacity, or a hidden side channel.

## H7 update

H7 should remain only a conditional constructor theorem. T106 adds that bounded reversible compression/export does not separate the finality direction from resource accounting: a strict monotone appears only on an open forward branch or after excluding the sink return path from the state.

## Claim ledger update

Add T106 to H7: bounded reversible compression does not rescue the physical-arrow reading. Orderless compression is non-injective, ordered export consumes sink capacity, and the closed bounded cycle has no nontrivial strict monotone once the sink is included.

## Open blocker

No finite closed reversible observer model has produced a strict D1-relevant monotone after including the memory, compression sink, and return/unwind degrees of freedom.

## Recommended next

Either formalize this as a general finite-permutation obstruction for H7, or look for an open-system thermodynamic model where H7's remaining content is explicitly the observer-indexed coarse graining rather than a new arrow of time.
