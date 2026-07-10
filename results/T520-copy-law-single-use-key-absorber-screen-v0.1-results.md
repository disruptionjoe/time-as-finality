# T520 Results: Copy-Law Single-Use-Key Absorber Screen

Verdict: **`COPY_LAW_SINGLE_USE_KEY_ABSORBED_BY_RESOURCE_MONOTONE`**
Date: 2026-07-09. Model: `models/finality_encrypted_clone_single_use_key.py`
(exit 0, 8/8 checks). Tests: `tests/test_finality_encrypted_clone_single_use_key.py`
(8 passed). Data: `results/T520-copy-law-single-use-key-absorber-screen-v0.1.json`.

## What was tested

Lane B's 2026-07-09 wake condition -- "a different conserved / priced quantity" --
against the single-use decryption key of arXiv 2602.10695 (encrypted cloning,
Yamaguchi-Kempf et al.), which lets a qubit be copied into any number of encrypted
clones while decryption consumes a single-use key so exactly one clone is ever
authoritative ("in agreement with no-cloning").

## Findings

1. **The unreadable-band object is real (lane-B failure mode 1 confirmed).** Each
   encrypted clone's marginal is `I/2` to machine precision (`||marg - I/2|| =
   2.4e-18`); two different sources have identical encrypted marginals
   (trace distance `0.0`), so the band is unreadable and `rec_individual = 1/2`.
   The encrypted clones ARE the unreadable band -- a relabel, as the cluster swing
   found.

2. **The candidate quantity clears lane-B failure mode 2.** `A = readable_copies +
   remaining_key_authority` is conserved: `A_band = A_global = 1` for the single-use
   key, versus the falsified `J+R` which ran `1 -> 6`. Controls conserve `A` at
   their own value (double-use `A=2`, absent `A=0`). So the letter of the wake
   condition is met: a different quantity, and this one is actually conserved.

3. **But it is absorbed by the bare resource monotone (decisive).** Across all
   `3 keys x 4 clone-counts = 12` scenarios, the finality verdict vector
   `(can_finalize_now, max_authoritative_copies_ever, cost)` equals the resource
   vector `(recoverable_now, total_recoveries, cost)` -- 12/12. The "exactly-once"
   property is not a finality-only quantity: it is the value `total_recoveries = M`
   the resource ledger already reports (single- / double- / absent-key are
   distinguished by the monotone, not only by the finality reading).

4. **No residue.** The one candidate residue -- which clone becomes authoritative
   -- is a free symmetric choice under clone relabeling, i.e. observer-made, not a
   forced verdict. The predeclared non-absorption burden fails at its decisive
   gate (`verdict_quantity_not_computed_by_ledger = False`): the key's role reduces
   to one-time-pad key-consumption.

## Interpretation

The single-use key is a genuinely better candidate than `J+R` -- it is a real
consumable resource external to the band and it is actually conserved -- but it
walks straight into the resource-theory absorber that already ate lane B's
monogamy / Landauer residue (and that owns the Q1A / RSPS / H7 lineage). "Exactly
one authoritative commit" is one-time-pad key-exhaustion under a finality relabel.

Lane B ("finality dual to no-cloning") **stays SHUT-as-stated** with a sharper
epitaph: even the strengthened, actually-conserved copy quantity is resource
bookkeeping. Any surviving monogamy content routes to the monogamy <-> quantum
secret sharing strut (arXiv 2605.26866), which is a known, real bridge -- not to a
lane-B reopening.

## No-movement boundary

No claim-ledger, COMPLEXITY-LEDGER, ROADMAP, README, North Star, public-posture,
hard-policy, external-publication, or cross-repo truth movement. A negative screen,
recorded as progress.
