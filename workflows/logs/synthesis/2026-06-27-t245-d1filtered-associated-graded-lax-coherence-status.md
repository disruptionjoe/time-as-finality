---
document_type: synthesis_status
batch_item: seventh_20_task_20
status: complete
authority: non_authoritative
write_scope: workflows/logs/synthesis
claim_effect: none
---

# T245 D1Filtered Associated-Graded Lax-Coherence Status

## Status

This note summarizes T245's finite coherence battery. It does not claim a full
lax-functor theorem or cocompleteness.

## Sources read

- `tests/T245-d1filtered-gr-lax-coherence.md`
- `results/d1filtered-gr-lax-coherence/T245-results.json`
- `workflows/logs/synthesis/2026-06-27-d1filtered-lax-functor-coherence-gate.md`
- `workflows/logs/synthesis/2026-06-27-d1cat-cocomplete-boundary-preflight.md`

## Plain-English finding

The associated-graded schedule behaves coherently on the tested anchored
triples, but the current fold misses data off-anchor. The next repair is
top-aware, not a broad category-completeness claim.

## Technical conclusion

T245 upgrades the pairwise T242 comparison to a finite triple battery:

- selected full-top-anchored generator pentagons commute;
- comparison cells exist and are genuinely lax/non-strict in several cases;
- the full-category upgrade is blocked by off-anchor `mu` under-counting.

The named repair is:

```text
mu_top
```

General cocompleteness at infinity remains open, and this discrete D1Filtered
lane stays separate from the sheaf/Cech continuum lane.

## Minimum next task

Build the top-aware fold and rerun the obstruction battery. Only then ask
whether the comparison cells satisfy a broader lax-functor coherence law.

## Stop condition

Stop if anchored finite coherence is reported as a subcategory-wide lax-functor
theorem, a pseudofunctor theorem, or D1Filtered cocompleteness.

