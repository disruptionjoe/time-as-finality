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

## T507 refinement (done 2026-07-08)

Model: `models/finality_band_recovery_edges.py` (exit 0). Replaces the ad-hoc fragment count with the
repo's own recovery-by-admissible-op statistic (imports `recovery`, `individual_operation`,
`collective_boost` from the T507 double gate). "Locally readable" = the value difference is recoverable by
the ADMISSIBLE (individual / positivity-preserving, block-diagonal) algebra; "hidden" = recoverable only by
the non-standard full-Krein collective algebra.

Result table:

| scenario | CHSH | rec_individual | rec_collective | readable | redundant | unreadable-band |
|---|---|---|---|---|---|---|
| LOCAL (definite value) | 0.00 | 0.50 | 1.08 | True | False | False |
| CLASSICAL (shared randomness) | 2.00 | 0.50 | 1.08 | True | False | False |
| **BAND (entangled)** | **2.83** | **0.00** | 0.76 | False | False | **True** |
| **ENCRYPTED (classical, scrambled)** | **2.00** | **0.00** | 0.76 | False | False | **True** |
| GLOBAL (redundant broadcast) | 2.00 | 0.50 | 1.08 | True | True | False |

Two things this buys:

1. **Both edges now use ONE repo-native algebra.** The lower edge (readable -> unreadable) and the upper
   edge (unreadable -> readable) are both just admissible recovery (rec_individual) crossing zero. No ad-hoc
   fragment threshold in the edge definition; redundancy only labels *why* recovery returns at the top.

2. **NEW structure -- the entangled band is nested inside a broader unreadability band.** The
   admissible-unreadability wall (rec_individual = 0) catches BOTH the entangled pair AND a
   classically-correlated-but-scrambled value (ENCRYPTED, CHSH <= 2). So:
   - **outer band** = not recoverable by admissible local ops (the readability wall, both edges, one algebra);
   - **inner band** = additionally CHSH > 2 (genuine entanglement).

   The value in the band is a genuine HIDDEN record, not absence: the collective algebra recovers it
   (rec_collective ~ 0.76 > 0). Entangling vs encrypting are two different ways to enter the outer wall from
   below; redundant broadcast is what reopens it from above. No-signaling remains irrelevant.

This means "the entanglement between-band" is a *labelled sub-region* of a more fundamental object: the
band of facts that are jointly present but not recoverable by an observer's admissible local operations.
That is the TaF-native object; entanglement is one way to realise it.

## Next

- **P1 on the bounded band:** state the constructor axiom (reverse-the-correlation) restricted to the
  reversible+deterministic+state-preserving task, graded by QRT, and check its possible->impossible flip
  tracks the outer wall (rec_individual crossing zero), with CHSH>2 as the entanglement label.
- Optional: pin the redundancy threshold to a recovery-count over disjoint fragments (all one algebra)
  rather than an integer, closing the last ad-hoc constant.
