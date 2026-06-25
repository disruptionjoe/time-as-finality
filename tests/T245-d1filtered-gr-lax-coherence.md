# T245: D1Filtered Associated-Graded Lax-Coherence Battery

**Verdict (top): conditional (finite_witness + poly_decider).**

**Builds on:** [T242](T242-compose-meet-total-functor.md),
[T237](T237-d1filtered-graded-functor.md),
[T232](T232-d1filtered-morphism-graded-colimit.md), and
[T228](T228-d1cat-transfinite-colimit-decision.md). **Code:**
`models/d1filtered_gr_lax_coherence.py`;
`tests/test_d1filtered_gr_lax_coherence.py`;
`results/d1filtered-gr-lax-coherence/T245-results.json`.

## Verdict

T245 upgrades T242's pairwise `gr_semilattice` comparison into a finite triple
coherence battery. On the selected full-top-anchored generator triples, the
schedule pentagon commutes:

```text
gr_semilattice((f;g);h) -> mu(mu(gr f, gr g), gr h)
```

The target `mu` fold associates on the nose across the tested battery, and the
comparison cells exist. Some tested cells are directed/non-strict, so the battery
supports a genuinely lax reading for those witnesses rather than a strict one.

## Negative Boundary

The full-category upgrade is blocked off-anchor. With a non-full-top leg
interleaved with a non-nested drop, the genuine meet-closure composite records a
dropped support dimension that T237's `mu` fold does not see. The comparison cell
then fails to exist. The named repair is a top-aware fold `mu_top`.

## Scope

This is **not** a subcategory-wide lax-functor theorem and not a complete
pseudofunctor refutation. The earned statement is:

```text
selected full-top-anchored generator pentagons commute, and a concrete off-anchor
mu-under-count obstruction blocks the current full-category upgrade.
```

General cocompleteness at infinity remains open, and this lane is distinct from
the sheaf/Cech continuum lane.
