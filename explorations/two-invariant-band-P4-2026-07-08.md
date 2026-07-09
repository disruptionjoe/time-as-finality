# Two-invariant band: P4 run to completion (2026-07-08)

Executes starter-swing P4 from
`explorations/entanglement-between-local-and-global-finality-2026-07-08.md`.
Model: `models/finality_two_invariant_band_separation.py` (runs, exit 0, all checks pass).

## Question

The note proposed "correlation without control" (no-signaling) as the *defining* invariant of the
between-band. P4 predicted that fails, and that a two-invariant band is needed. This run settles it on a
4-scenario separation table (plus a band-exit control).

## Result table

| scenario | CHSH | no-signaling | local-readable | redundant | in-band |
|---|---|---|---|---|---|
| LOCAL (product / definite value) | 0.00 | True | n/a | False | False |
| CLASSICAL (shared randomness) | 2.00 | True | 1.00 | False | False |
| **BAND (entangled pair)** | **2.83** | **True** | **0.50** | **False** | **True** |
| GLOBAL (redundant broadcast record) | 2.00 | True | 1.00 | True | False |
| BAND_EXIT (band after measure+broadcast) | 2.00 | True | 1.00 | True | False |

## Findings

1. **No-signaling is flat.** It holds in every scenario -- product, classical, band, global. It separates
   nothing and therefore cannot define or bound the band. Face (c) "correlation without control" is
   **demoted from definer to background property.** (Confirms the P4 killshot.)

2. **Local readability is non-monotone along the finality gradient.** Readable (classical, acc 1.0) ->
   **unreadable at the band (acc 0.5, chance)** -> readable again (global, acc 1.0). The band *is* the
   readability dip. A single monotone order parameter cannot capture a dip, which is the structural reason
   one invariant is not enough. This also kills, in passing, any hope of local-readability as the "smallest
   irreversible quorum" style scalar (P5, already dead): it is not monotone.

3. **The band is uniquely selected** by "a genuine correlation not reproducible by a locally pre-readable
   value" (correlation present AND CHSH > 2). Exactly one scenario satisfies it: the entangled pair.

4. **The two edges are crossed by two different physical events** -- this is the reshaped two-invariant
   band:
   - **LOWER edge (local/classical -> band): entanglement onset.** CHSH crosses 2; a local hidden
     (pre-readable) value ceases to exist. Readability drops 1.0 -> 0.5.
   - **UPPER edge (band -> global): redundancy / broadcast.** The BAND_EXIT control measures and
     broadcasts the band; local readability is restored (0.5 -> 1.0) and fragment count rises (0 -> 6,
     crossing the redundancy threshold). Readability rises 0.5 -> 1.0.

## Verdict

The note's "two-invariant band" is **confirmed but reshaped.** The band's boundary invariants are
**entanglement-onset (lower)** and **redundancy-onset (upper)** -- crossed by two distinct events. What
drops out:

- **no-signaling / correlation-without-control** is *not* a band invariant (flat everywhere). The note's
  earlier promotion of it to "necessary defining face" (from the pullback pass) is **overturned by
  measurement.**
- **local readability** is not an order parameter (non-monotone); it is a *diagnostic* whose dip marks the
  band.

## Honest limits

- The scenarios are minimal correlation-table / marginal models, not a full open-system simulation. CHSH
  and marginals are the real physics; redundancy is modelled as an integer fragment count, not a decohered
  environment. The qualitative separation is robust; a quantitative redundancy threshold (how many
  fragments = "global") is not pinned here and is the natural next refinement (ties to
  `models/finality_records_vs_redundancy_discriminator.py` and T507).
- "Local readability" is operationalised as MAP-estimate accuracy of the shared value from A's marginal
  alone, and tied to the CHSH<=2 local-hidden-value account. That is faithful to the repo discriminator's
  "recoverable by an admissible op" but is a *specific* admissible-op choice (local classical readout),
  not the full positivity-preserving algebra.

## Next

- Replace the integer fragment count with the records-vs-redundancy recovery statistic (T507) so the upper
  edge is defined by the same admissible-op algebra as the rest of the repo, not an ad-hoc threshold.
- Then P1 (constructor axiom, restricted to the reversible+deterministic+state-preserving task, graded by
  QRT) can sit on top of this cleanly bounded band.
