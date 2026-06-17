# Heliosphere As A Finality Domain

## Status

Exploration. This note treats the heliosphere as a concrete, observation-adjacent instantiation of a [D1](../claims/D1-physical-finality-definition.md) finality domain, and the heliopause as a soft boundary on the permeability spectrum introduced for [B1](../claims/B1-black-holes-finality-boundaries.md). Two claims here are repo-ready as formalization targets (H-Domain, H-Soft-Boundary). One is held pending citation verification (H-Hierarchy). One is filed as an open problem (finality under non-static boundaries).

## Seed Idea

The heliosphere is the region of space where the Sun's solar wind, magnetic field, and energetic-particle environment dominate the local physics. Its outer edge, the heliopause, is where that solar-driven medium gives way to the interstellar medium. The seed idea is that this is not only a navigational region but a finality domain in the D1 sense: a region within which the record-forming substrate has a particular character, bounded by a place where that substrate changes identity.

Where black-hole horizons (B1) are the hard, one-way extreme of a causal-access boundary, the heliopause is a soft, two-way case. Records cross it in both directions and change character as they cross. Holding both in one frame suggests boundary permeability is a continuous parameter, not a binary soft-or-hard label.

## Layer 1: The Heliosphere Record Substrate (physics-facing)

### Working Claim (H-Domain)

Inside the heliopause, the dominant record-forming substrate is solar-wind plasma, the Parker-spiral magnetic field, and solar-energetic-particle populations. These constrain which microphysical events leave durable, redundantly encoded traces, and therefore which events count as more final under D1's four dimensions (redundancy, causal accessibility, robustness, reversal cost). The heliosphere qualifies as a D1 finality domain because the record-bearing media change character at the heliopause, not because of any metaphysical boundary.

### Why It Is Repo-Worthy

D1 currently has no worked physical example of substrate-constrained finality at astrophysical scale. The heliosphere supplies one, with a real boundary (the heliopause) that observation has already characterized in broad strokes.

### Failure Condition

The claim survives only if, for one fixed event class (for example, a charged-particle scattering), at least one D1 dimension shows a substrate-attributable difference inside versus outside the heliopause, where substrate-attributable means the difference persists after normalizing for particle density. A difference that vanishes under density normalization is mere density change, not a finality-substrate boundary, and the heliosphere reduces to a navigation convenience.

### Guardrail

This is a physics-facing claim about record formation in plasma. It does not depend on any observer's beliefs ([G1](../guardrails/G1-human-belief-does-not-create-matter.md)) and makes no claim about replacing established solar or plasma physics ([G2](../guardrails/G2-not-a-replacement-theory.md)).

## Layer 2: The Heliopause As A Substrate-Exchange Boundary (physics-facing)

### Working Claims

- **Two distinct thresholds.** The termination shock and the heliopause are separate finality thresholds, not one. The termination shock is a deceleration boundary (supersonic to subsonic solar wind); the heliopause is a substrate-exchange boundary (solar plasma to interstellar plasma). D1 should assign them distinct signatures without using time-ordering as the discriminator, since the framework derives time from finality. Operational form: characterize the termination shock by a change in reversal-cost or stability (kinetic deceleration) and the heliopause by a change in redundancy-carrier identity (substrate exchange). If both collapse to the same D1 signature, the two-threshold claim fails.
- **Scale-relative sharpness.** For a record class with characteristic stabilization time tau, the heliopause is a sharp domain boundary when tau is much smaller than the crossing time, and a blurred or averaged boundary when tau is much larger. This restates an earlier observer-framed intuition entirely in terms of record-class physics: tau is a property of the record class, not of any observer.

### Repo Connection

These claims extend [T7](../tests/T7-overlapping-causal-domains.md), which asks for a worked example with received signals, direct participation, and a causally distinct region. The Voyager heliopause crossings are exactly that worked example (see Layer 4 and the held citation note).

## Layer 3: Cross-Boundary Observer Experience (cognitive-social)

> Editorial rule for this layer: in every sentence, the grammatical subject is the accessible record set, not the observer's experience. The boundary changes which traces are available to a record-bearing system. It does not change the system's consciousness.

### Working Claims

- **Accessible-record subset, not the renderer.** For an embedded observer ([D2](../claims/D2-observer-as-record-bearing-system.md)) crossing the heliopause, what changes is the set of accessible records that feeds the renderer, not the internal time-rendering machinery. The local stabilization profile, meaning which traces are redundantly encoded around the observer, shifts. The renderer adapts to a changed input set.
- **Reconstructed order, not proper time.** Reconstructed temporal ordering is built from accessible records. If the accessible record set changes at the boundary, reconstructed order may change without proper time changing. This is a cognitive-social illustration of [C1](../claims/C1-experienced-time-as-record-finality.md) and [R1](../claims/R1-relativity-no-global-commit-order.md), not a replacement for special-relativistic proper time.

### Guardrail

This layer is held strictly to [G2](../guardrails/G2-not-a-replacement-theory.md) and [G3](../guardrails/G3-observer-rendering-not-mind-created-matter.md). The phrase "without proper time changing" must appear in any prose that uses the second claim. Any sentence that makes "the observer's experience" the thing the boundary changes is a G3 violation and must be rewritten with accessible records as the subject.

## Layer 4: Permeability Spectrum, Hierarchy, And Moving Boundaries

### H-Soft-Boundary (physics-facing, repo-ready)

Finality-domain boundaries fall on a continuous permeability spectrum. The heliopause is a soft point (bidirectional record exchange with character change: interstellar cosmic rays in, solar particles out). The event horizon (B1) is the hard extreme (one-way classical export, capped). The contribution to B1 is a continuous boundary-permeability parameter, with the heliopause and the horizon as two points on it rather than two categories.

Failure condition: the difference must be stateable as a measurable export asymmetry across the boundary, not a metaphor. If every boundary turns out bidirectional at some scale with no privileged threshold, that is itself the finding: permeability is genuinely continuous and belongs in B1 as a parameter, not a binary soft-or-hard distinction.

### H-Hierarchy (physics-facing, held pending citation verification)

Nested astrophysical structures (planetary magnetospheres, the heliosphere, the Local Bubble, the galactic disk) may form a finality-domain hierarchy, with measurable substrate-driven record-stabilization differences at each boundary. A candidate observational test is cosmic-ray-induced isotope production rates, which change across the heliopause and would change again at the Local Bubble boundary if the substrate model holds.

`[citations verified]` Primary sources for the Voyager heliopause crossings, confirmed against journal records:

**Voyager 1 crossing (25 August 2012, ~121.7 AU):**

- Stone, E.C., Cummings, A.C., McDonald, F.B., Heikkila, B.C., Lal, N., and Webber, W.R. (2013). "Voyager 1 Observes Low-Energy Galactic Cosmic Rays in a Region Depleted of Heliospheric Ions." *Science* 341, 150–153. DOI: 10.1126/science.1236408. Measured a step increase in galactic cosmic ray flux (>50% increase in ~1 GV nuclei) and simultaneous drop in anomalous cosmic ray intensities at the crossing.
- Burlaga, L.F., Ness, N.F., and Stone, E.C. (2013). "Magnetic Field Observations as Voyager 1 Entered the Heliosheath Depletion Region." *Science* 341, 147–150. DOI: 10.1126/science.1235451. Measured magnetic field strength increase from ~0.2 to ~0.4 nT at the boundary; notably, field direction did not rotate substantially at the crossing.
- Gurnett, D.A., Kurth, W.S., Burlaga, L.F., and Ness, N.F. (2013). "In Situ Observations of Interstellar Plasma with Voyager 1." *Science* 341, 1489–1492. DOI: 10.1126/science.1241681. Detected electron plasma oscillations at ~2.6 kHz on 9 April 2013, corresponding to an electron density of ~0.08 cm⁻³, close to the expected interstellar medium value (compared to ~0.002 cm⁻³ in the outer heliosphere).

**Voyager 2 crossing (5 November 2018, ~119 AU):**

- Stone, E.C., Cummings, A.C., Heikkila, B.C., and Lal, N. (2019). "Cosmic Ray Measurements from Voyager 2 as it Crossed into Interstellar Space." *Nature Astronomy* 3, 1013–1018. DOI: 10.1038/s41550-019-0928-3. Observed sharp decrease in low-energy heliospheric ions and increase in galactic cosmic rays at the heliopause; cosmic ray intensities just beyond the heliopause were ~90% of values further out.
- Burlaga, L.F., Ness, N.F., Berdichevsky, D.B., et al. (2019). "Magnetic Field and Particle Measurements Made by Voyager 2 at and near the Heliopause." *Nature Astronomy* 3, 1007–1012. DOI: 10.1038/s41550-019-0920-y. Found a thinner and simpler heliopause than Voyager 1 crossed, stronger interstellar magnetic fields, and a magnetic barrier in the heliosheath adjacent to the heliopause.
- Richardson, J.D., et al. (2019). "Voyager 2 Plasma Observations of the Heliopause and Interstellar Medium." *Nature Astronomy* 3, 1019–1023. DOI: 10.1038/s41550-019-0929-2. First direct plasma measurements at and beyond the heliopause; observed a 1.5 AU wide boundary layer with plasma twice as dense as typical heliosheath plasma; the HP transition itself occurred in less than one day.

No primary-source isotope-rate measurements at the heliopause boundary were located in this verification pass. The isotope-rate test (H4.2) remains a theoretical prediction drawn from the Voyager crossing data and terrestrial/meteoritics literature; it is not yet an independently verified measurement and should be marked as a candidate observational test rather than a confirmed result.

### Open Problem: Finality Under Non-Static Boundaries

The heliosphere expands and contracts with the roughly 11-year solar cycle, making the heliopause a moving finality boundary. D1 does not currently say how records formed near a periodically moving boundary should be characterized. This is filed as [Finality Under Non-Static Boundaries](../open-problems/finality-under-non-static-boundaries.md).

## Next Useful Test

Extend [T7](../tests/T7-overlapping-causal-domains.md) with the Voyager heliopause crossings as a worked example: a record-graph diagram showing solar-domain-only records, interstellar-domain-only records, and the overlap region around the heliopause where both substrates contribute. Once primary-source citations are verified, promote H-Hierarchy to a claim and add the isotope-rate test as its success criterion.
