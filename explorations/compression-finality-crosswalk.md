# Compression as an Observable of Finality

## Status

Exploration only. No claim updates. T36 delivers the promised experiment;
findings are recorded below.

## Core Distinction

Compression should not be treated as identical to finality or automatically
added as a D1 dimension. The stronger hypothesis is that compressibility is an
observer-relative observable downstream of stable record formation:

```text
finality → stable records → predictability → compression
```

Not:

```text
compression = finality
```

High-finality records (high redundancy, high reversal cost, strong branch
support) are records for which an embedded observer can construct short
descriptions. Low-finality branches look like incompressible noise from within
the observer's access boundary. Compressibility is therefore a consequence of
finality structure, not a component of it.

## Open Questions

1. Why is the world compressible at all? Can the repo's record-stabilization
   model constrain which physical substrates produce compressible causal graphs
   rather than asserting compressibility as a background fact?

2. Does high-finality record structure correlate with lower description length?
   This is the testable direction: run prefix-coding experiments on
   finality-weighted causal DAGs and measure whether finality thresholds
   correspond to compressibility phase transitions.

3. Can projection/gluing obstruction be detected as failure of global
   compression? A restriction projection that introduces a gluing obstruction
   (AC6=True) may correspond to a context where no globally efficient code
   exists — analogous to contextuality in Bell tests preventing a global
   probability assignment.

4. Can observer-relative entropy be defined over accessible finality support?
   Shannon entropy assumes a global probability distribution and ideal decoder.
   The repo's observer has only bounded causal access. Conditional entropy
   relative to the observer's restriction system and projection obstructions
   may explain why different observers at different scales experience different
   compressibility — and different temporal densities.

5. Should algorithmic information theory become a future mathematical lens? The
   Kolmogorov complexity of accessible record subgraphs is a natural candidate
   for a compressibility observable. It is not decidable in general but is
   estimable in finite models, which is the current regime.

## What This Is Not

- Not an argument that compression is the right D1 dimension to add.
- Not a claim that prediction errors cause gluing obstructions (causation runs
  the other way: structural obstructions constrain what can be predicted).
- Not a claim that intelligence or cognition is the right lens for physical
  record formation.

## Relation to Existing Claims

| Existing claim | Potential connection | Status |
| --- | --- | --- |
| D1 reversal cost | High reversal cost ≈ low conditional entropy for observer | formal only |
| D1 holder redundancy | Redundancy enables compression by reducing surprise | formal only |
| T18 finality direction | Arrow could be reframed as increasing accessible compressibility | speculative |
| T5 thermodynamic support | Landauer cost and entropy share the same substrate | known neighbor |
| T9 emergence lab | Compressibility phase transitions across 256 rules | candidate test |

## T36 Findings (v0.1)

T36 ran the promised experiment across all 256 elementary CA rules. Key results:

**The identity hypothesis is falsified.**

Two counterexamples mark the boundary:

- **Rule 30**: survival=1.000, compressibility=0.065. Every intervention leaves
  a durable trace, but the trace patterns are nearly maximally diverse (30 of 32
  possible patterns observed). Durable records do not imply compressibility.

- **Rule 0**: survival=0.000, compressibility=1.000. No intervention leaves any
  trace (the all-zeros attractor erases everything). The trivially degenerate
  trace distribution is perfectly compressible. Compressibility does not imply
  durable records.

**Correlations are substantial but not identities:**

| Relationship | Pearson r |
| --- | --- |
| Compressibility vs. trace_survival | −0.745 |
| Compressibility vs. lost_bits | +0.631 |

Both quantities co-vary with the underlying structure of the restriction system
but are not synonyms for either each other or for D1 finality.

**Divergence witnesses:**
- Rules 15 & 166: same survival ≈ 1.000, compressibility gap 0.496
- Rules 2 & 8: same lost_bits ≈ 2.594, compressibility gap 0.597

**Corrected relationship:**

```text
restriction system
    → projection
    → stable records
    → predictive structure
    → compression opportunities
```

Compressibility is a diagnostic observable of record architecture, not a
measure of record stability. The open questions below remain open; the strongest
form of the hypothesis has been narrowed.

**What this does not support:**
- Adding compressibility as a D1 dimension.
- Treating compressibility as a proxy for information loss (lost_bits).
- The monotone reading: high finality → high compressibility. Rule 30 refutes this.

See [T36](../tests/T36-compression-finality-crosswalk.md) and
[TECHNICAL-REPORT-compression-finality-crosswalk-v0.1.md](../TECHNICAL-REPORT-compression-finality-crosswalk-v0.1.md)
for full results.
