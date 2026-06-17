# Dark-Matter-Adjacent Accessibility Models: Math Verdict

## Status

Exploration, resolved 2026-06-10. The assignment (from the [BACKLOG](BACKLOG.md) dark-matter entry) was not to prove physics but to determine whether any version of "hidden stabilized structure ≈ dark matter, ratio ≈ 5:1" can be made precise enough to test or falsify. Answer: **yes, it can be made precise — and once precise, it fails fast on two independent grounds.** Per the assignment's own success criteria, that is a successful outcome. One safe mathematical residue survives (see Salvage).

## Target

Cosmological dark-to-baryonic ratio ≈ 5.4:1 (Ω_c/Ω_b ≈ 0.265/0.049). Note before any modeling: this is a cosmic *average*; the per-system ratio varies enormously (dwarf spheroidals are far more dark-matter-dominated; some ultra-diffuse galaxies show almost none). A model that "naturally produces 5:1" universally is *already wrong* — the right target is the mean plus its observed variance structure, which raises the bar further.

## Result 1: Hitting 5:1 is trivially easy, therefore evidentially empty

**Option 1 (visibility threshold), computed.** Let finality x be lognormal(σ); stabilized if x ≥ t_f (set at the 20th percentile), rendered if x ≥ t_r. For every σ tested (0.5, 1.0, 2.0) a t_r exists giving exactly 5:1 — and it always lands at the same quantile, 0.8667. That exposes the structure of the problem: the ratio (q − 0.2)/(1 − q) = 5 is a statement about *two quantiles only*. It carries zero information about the finality distribution, the physics, or anything else. One equation, arbitrarily many free parameters: a solution set, not a prediction.

**Option 4 (percolation), computed analytically (Erdős–Rényi, mean degree c).** Visible = giant component (observer inside); hidden = stabilized finite clusters (size ≥ 2). The ratio is a smooth monotone function of c: it equals 5:1 only at c* = 1.0587 — about 6% above the percolation threshold — and collapses to 1.2 at c = 1.2 and 0.33 at c = 1.5. So percolation is the one option where the ratio is governed by real mathematical structure (criticality and universality) rather than a bare threshold, but 5:1 requires *fine-tuning connectivity to sit just above criticality*. Without an independent self-organized-criticality mechanism pinning c there, the ratio is again an input. This was the strongest option and it still needs the one thing it doesn't have.

**Options 2 and 3 inherit the same defect analytically.** Graph-of-graphs accessibility (Option 2) adds nesting but the hidden fraction is still set by community-size and fidelity-decay parameters chosen by the modeler. Bayesian reconstruction (Option 3) is Option 1 with measure-theoretic vocabulary: "elsewhere-finalized but locally non-invariant" structure is a tunable mass under a chosen prior. Both can hit 5:1; neither is constrained to.

**General principle this establishes:** matching a single number with a model containing free parameters has zero evidential value. The model class earns interest only if (a) the ratio emerges from independently fixed parameters, or (b) the model makes a second, independent prediction. Test (b) is Result 2 — and it kills the class.

## Result 2: The gradient test — the generic second prediction, and it falsifies

Every observer-centered accessibility model — Options 1, 2, and 4 alike — shares one structural consequence: renderability decays with causal/graph distance from the observer, so the predicted hidden-to-visible ratio is a **monotonically increasing function of distance from us**. Computed with exponential access decay (length L): at L = 2 the predicted ratio runs from 0.57 (near) to 53 (far); at L = 5, from 0.20 to 3.9. The shape is forced; only the steepness is tunable.

Observation says the opposite. The dark-to-baryonic ratio shows **no Earth-centered gradient**: weak-lensing maps, cluster mass profiles, and the CMB-inferred global ratio are consistent across distance and direction (cosmological isotropy), and the local variance that does exist tracks structure type (dwarfs vs ellipticals vs clusters), not distance from any observer. The Bullet Cluster localizes the hidden mass by its *collisionless dynamics*, spatially separated from the baryonic gas — a configuration that correlates with the system's internal physics and not with any observer's causal-access structure.

So the model class makes exactly one forced falsifiable prediction, and it is already falsified. Option 3 escapes only by going non-spatial, at which point it loses contact with dark matter entirely, since dark matter is *spatially mapped* via lensing.

This compounds the physics objections recorded in [BACKLOG](BACKLOG.md) conjecture 14 (CMB-era timing; dark matter as the least record-forming substance under D2/D1 yet the most gravitating).

## Verdict

| Option | Can it be made precise? | Can it hit 5:1? | Is 5:1 a prediction? | Gradient test |
|---|---|---|---|---|
| 1 Threshold | Yes | Always (pure quantile choice) | No — input | Fails |
| 2 Graph-of-graphs | Yes | Yes (parameter choice) | No — input | Fails |
| 3 Bayesian | Yes | Yes (prior/measure choice) | No — input | Evades only by going non-spatial → loses the target |
| 4 Percolation | Yes | Only at c ≈ 1.06, just above criticality | Only with an unsupplied SOC mechanism | Fails |

**Close the dark-matter interpretation.** All four options, made precise, either hit 5:1 vacuously or require fine-tuning, and the entire spatial class is falsified by the absence of an observer-centered gradient. This is the assignment's "clearly fails" outcome, achieved cheaply — the idea did its job by dying informatively.

## Salvage: what survives, decoupled from cosmology

1. **The accessibility gap A_i as a repo quantity (WC-20).** "What fraction of stabilized structure is accessible to observer i" is well-posed on the T1 record graph, connects to the Holevo accessible-information gap, and needs no cosmological referent. The dark-matter intuition's only safe descendant.
2. **Records-percolation as pure math.** "Under what conditions does record propagation sit near criticality, and what does the cluster-size distribution of *record redundancy* look like?" is a legitimate T6-adjacent question. If an SOC argument for record networks ever materializes, revisit — as mathematics, not as dark matter.
3. **The gradient test itself as a guardrail tool.** "Does this observer-indexed proposal predict an observer-centered gradient that observation excludes?" is a reusable one-line falsifier for any future accessibility-based physics analogy in this repo. Worth remembering; it closed this one in an afternoon.

## Revival Attempt Log (closure-robustness procedure)

**2026-06-10, revival attempt 1 (Joe):** observers are everywhere and non-human; hidden structure may be local, part of a higher-dimensional manifold we are a projection of, or rendered in the local time-series graph but not yet stable enough for our rendering threshold. **Outcome: the accessibility closure stands; the revival produced a genuinely different claim (uniform rendering-threshold, not distance-decaying accessibility) which escapes the gradient and locality kills but fails on the opposite fact — dark matter is *high*-finality, not under-finalized.** Its gravitational records score high on all four D1 dimensions (redundant across independent probes, accessible, robust over ~90 years, costly to reverse); halos are among the most stable classical structures known. "Dark" = missing one record channel (EM coupling), not missing stabilization. Retreating to "we only render part of it" is true of all objects (the distant-star point) and has no discriminating content.

**Occupied neighboring lanes for the surviving intuitions (verify before citing):** higher-manifold shadow → braneworld / Kaluza-Klein dark matter; real-but-not-classically-stabilized → fuzzy / ultralight wave dark matter (galaxy-scale coherent field, Lyman-alpha constrained). If pursued, the move is a literature note against these, not a finality reframe.

**2026-06-10, revival attempt 2 (Joe):** gravitational signatures are *leading indicators* of matter, not matter — dark matter as structure below the rendering threshold, everywhere including locally. **Outcome: full every-lens review + 10 Hegelian dialectics in [dm-leading-indicator-lens-review.md](dm-leading-indicator-lens-review.md). Temporal component ("not yet") closed by ~12 independent lens directions; categorical component promoted and transformed into channel-indexed finality (WC-29), plus two keepers: zero-knowledge gravity (lensing as ZK proof of stress-energy — verified theorem, undisclosed witness) and the substrate selection effect (observers built from the EM sector define "matter" by their own channels).** This attempt partially succeeded — the process extracted a real D1 upgrade, demonstrating the typed battery is not a rubber-stamp kill machine.

**Net salvage upgraded:** dark matter is the universe's worked example that stabilization and accessibility are independent dimensions (WC-20) — maximal finality, narrow record channel. Keep as supporting evidence for separating D1's dimensions; do not keep as something finality explains.

## Relation To Repo

- [BACKLOG entry and conjecture 14 annotation](BACKLOG.md)
- [D1: Physical Finality Definition](../claims/D1-physical-finality-definition.md) — accessibility vs stabilization separation (WC-20)
- [G1](../guardrails/G1-human-belief-does-not-create-matter.md), ESSAY §9 — the fenced parent claim ("mass is finality density")
- [T6: Snowball Record Finality](../tests/T6-snowball-record-finality.md) — percolation residue
- Audit 2026-06-10, Track B method
