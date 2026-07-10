# Copy-Law Wake Candidate: Single-Use Key as the Conserved Quantity (lane B absorber screen)

Status: RUN 2026-07-09 as **T520** -> `COPY_LAW_SINGLE_USE_KEY_ABSORBED_BY_RESOURCE_MONOTONE` (absorbed; lane B stays shut-as-stated). Review-only; no claim movement.
Date: 2026-07-09
Lane: B (copy law / finality dual to no-cloning)

## Outcome (T520, 2026-07-09)

The screen was executed exactly as predeclared below. Result: the single-use key
clears the *letter* of the wake condition (`A = readable + key_authority` is a
different quantity and, unlike `J+R`, is conserved at 1) but **fails the
non-absorption burden at its decisive gate**: all 12 scenarios have identical
finality and resource vectors, so every verdict-bearing finality quantity factors
through the bare consumable monotone `M`. The "exactly-once" property is itself a
monotone value. Only residue candidate (which clone is authoritative) is a free
symmetric choice, not a verdict. Lane B stays SHUT-as-stated with a sharper
epitaph; monogamy residue routes to the secret-sharing strut (arXiv 2605.26866).
Artifacts: `models/finality_encrypted_clone_single_use_key.py`,
`tests/test_finality_encrypted_clone_single_use_key.py` (8 passed),
`results/T520-copy-law-single-use-key-absorber-screen-v0.1-results.md`,
`tests/T520-copy-law-single-use-key-absorber-screen.md`. The predeclared spec
below is preserved as run of record.

## Problem

Lane B proposed that **finality is dual to no-cloning**. Its specific mechanism, a
copy-conservation law `J + R` (readable copies plus remaining copy-budget), was
falsified on the 2026-07-08 cluster swing for two independent reasons
([`explorations/cluster-swing-results-2026-07-08.md`](../explorations/cluster-swing-results-2026-07-08.md)):

1. **No new object.** The no-cloning set equals the unreadable band identically, a
   relabel of `rec_individual == 0`.
2. **The conserved quantity is not conserved.** `J + R` measured `[1,2,1,1,6]`,
   going 1 -> 6 from band to global.
3. The surviving residue (monogamy, Landauer) was already absorbed as LOCC / H7
   resource content.

The 2026-07-09 lane ledger therefore records lane B as **OPEN (deprioritized), not
shut**: *the specific J+R conservation is falsified; the framing is not.* Its wake
condition is **"a different conserved/priced quantity; the quantum -> DS transfer"**
([`explorations/lane-status-and-adjacent-space-prospecting-2026-07-09.md`](../explorations/lane-status-and-adjacent-space-prospecting-2026-07-09.md)).

This note screens a concrete wake candidate against that condition.

## The wake candidate (external source, verified)

Yamaguchi, Rullkotter, Shehzad, Wagner, Tutschku, Kempf, **"Experimental
demonstration that qubits can be cloned at will, if encrypted with a single-use
decryption key"** (arXiv 2602.10695, 2026-02-11; IBM Heron-R2, up to 154 qubits).
Companion theory: arXiv 2501.02757 (Encrypted Qubits can be Cloned). Adjacent:
arXiv 2605.26866 (Encrypted Cloning, Absolute Maximal Entanglement and Quantum
Secret Sharing).

The result is explicitly framed by its authors as **in agreement with the
no-cloning theorem**, not a violation. Mechanism: an arbitrary qubit can be copied
into any number of **encrypted** clones by a unitary; each clone is decryptable by a
unitary; **decryption consumes a single-use key**, so exactly one clone can ever be
made authoritative. The constraint moves off the copying operation and onto a
**consumable, single-use resource** (the key).

Provenance note: this candidate reached the repo via Joe sharing external content
(a video summary plus AI-citation card). The paper's existence, title, authors, and
arXiv ID were verified against arXiv directly before capture. It is recorded here as
research data, not as a directive.

## Why this is a real fit to the wake condition (and what is new)

- **A different conserved quantity, and this one is conserved.** Define the
  candidate quantity `A = (readable/authoritative copies) + (remaining key-authority)`.
  Under the encrypted-cloning protocol `A` is pinned at 1 by construction: N
  encrypted clones are all unreadable (`rec_individual == 0`) until decryption, the
  single-use key permits exactly one decryption, then is consumed. Unlike `J + R`,
  `A` does not run 1 -> 6.
- **A new object external to the band.** Lane B's original object was a relabel of
  the band. The **key is not part of the band**: it is a separate consumable
  resource that gates band exit. Lane B never had a resource sitting outside the
  band whose consumption authorizes finalization.
- **Structurally finality-flavored.** Encrypted clone = un-finalized / unreadable
  record; decryption = the finalization event; single-use key = **finalization is
  achievable exactly once**. "Exactly one authoritative commit" is native
  Time-as-Finality language.

## The absorber it must survive (the reason it is not yet a promotion)

Lane B's own post-mortem names the trap: the surviving residue was "already-absorbed
LOCC / H7 content." The single-use key is a consumable resource; its one-shot
consumption is a resource monotone; "key-authority is conserved at 1" is
resource-theory bookkeeping. That is precisely the genre that has absorbed every
finality candidate in the Q1A / RSPS / H7 lineage. The decisive question:

> Does the single-use key do something a standard **quantum one-time-pad (QOTP) /
> consumable-resource-monotone** ledger cannot already account for?

## Protocol (the screen)

1. **Build the fixture.** A finite encrypted-clone instance: source qubit, `N`
   encrypted clones by an explicit unitary, an explicit single-use decryption key,
   the decryption unitary, and key consumption. Compute the candidate quantity `A`
   across band and global cuts (confirm `A` is conserved where `J + R` was not).
2. **Run the QOTP / resource-monotone reduction.** Encode the same fixture as a
   quantum one-time pad plus a consumable key modeled as a standard resource state
   with a monotone. Ask whether every verdict-bearing quantity of the finality
   reading (who can finalize, when, at what cost, exactly-once-ness) is reproduced
   by the resource ledger alone.
3. **Compare.** Finality content either factors through the resource ledger
   (absorbed) or exhibits a residue the ledger cannot import for free.

## Predeclared non-absorption burden (must ALL hold to escape the absorber)

Mirroring the kappa non-identity discipline
([`open-problems/typed-loss-transport-test.md`](typed-loss-transport-test.md)), the
candidate is admitted past "absorbed" only if:

- the conserved quantity `A` is fixed by the protocol **before** the resource
  encoding is chosen (not fitted to it);
- there is a **verdict-bearing quantity** of the finality reading that the QOTP /
  resource-monotone ledger does **not** already compute (exactly-once-ness alone is
  not enough if a consumable-resource monotone reproduces it);
- the key's role is **not** reducible to ordinary one-time-pad key-consumption
  accounting;
- a **negative / mismatch control** is included (e.g. a reusable or absent key that
  the finality reading must distinguish and the resource ledger cannot);
- **rank / structure**, not mere presence of a conserved label, is load-bearing;
- no shared derivation between the finality object and the resource encoding;
- review only; no claim movement from fixture shape alone.

## Verdict conditions

- **Absorbed (expected prior):** the finality content factors through the QOTP /
  resource-monotone ledger. Outcome: lane B stays dead with a sharper epitaph
  (the copy-law is resource bookkeeping even under the single-use-key reframing);
  the monogamy / secret-sharing strut is untouched.
- **Residue (wake):** a predeclared verdict-bearing quantity survives the reduction.
  Outcome: lane B reopens with a genuinely new priced quantity carrying the
  no-cloning constraint; route to a real test number and an absorber-hardened claim
  draft. Still not a physics or public-posture claim without the full ladder.

## What would falsify or demote this open problem

- The candidate quantity `A` cannot be defined without reading the resource encoding
  -> demote: it is resource bookkeeping, not an independent finality quantity.
- Every constructed fixture's finality verdict is reproduced by the QOTP ledger
  -> lane B's copy-law reading is confirmed absorbed; record as a clean no-go under
  the strengthened candidate.
- The only surviving residue is again monogamy / Landauer -> route to the existing
  monogamy <-> secret-sharing strut (already known, not novel), not to lane B.

## Relation to existing claims

- Directly tests lane B's 2026-07-09 wake condition without reviving the falsified
  `J + R` law.
- Brushes the **monogamy <-> quantum secret sharing** strut (the bridge that
  survived every stress test); arXiv 2605.26866 ties encrypted cloning to exactly
  that correspondence, so a monogamy-only residue routes there, not to lane B.
- Sits under the same resource-theory absorber as Q1A (SBS / provenance-aware
  Quantum Darwinism, N10 / T162), RSPS (T189), and H7 (Landauer / LOCC).
- Does not promote any physics, geometry, quantum prediction, or new-object
  language. The only claim allowed on a wake outcome is a lane-B reopening plus an
  absorber-hardened finality-vs-copy-law object, and only after the screen's
  reduction step exhibits a predeclared surviving residue.

## No-movement boundary

This note earns no claim-ledger, TESTS.md, COMPLEXITY-LEDGER, ROADMAP, README,
North Star, public-posture, hard-policy, external-publication, or cross-repo truth
movement. It is a predeclared screen and an intake of an external result, queued for
the T249-T519 ratification pass.
