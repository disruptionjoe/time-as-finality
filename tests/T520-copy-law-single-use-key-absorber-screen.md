# T520: Copy-Law Single-Use-Key Absorber Screen

## Target Claims

No claim-ledger target. Screens lane B ("finality dual to no-cloning") against its
2026-07-09 wake condition ("a different conserved / priced quantity"), using the
single-use decryption key of arXiv 2602.10695 (Yamaguchi-Kempf et al., encrypted
cloning) as the candidate quantity. Predeclared spec:
`open-problems/copy-law-single-use-key-absorber-screen-2026-07-09.md`.

## Setup

Two independent code paths over the same finite encrypted-clone fixture:

- **Finality reading.** An unknown qubit is copied into `N` quantum-one-time-pad
  encrypted clones; each clone's marginal (uniform Pauli key) is `I/2` -- the
  unreadable band, `rec_individual = 1/2`. A single-use key permits one
  decryption. Candidate conserved quantity `A = readable_copies +
  remaining_key_authority`.
- **Resource ledger.** The key as a bare consumable monotone `M` with no finality
  semantics: clone-encrypt is a free operation, decrypt consumes one unit of `M`.

Controls: single-use (`M=1`), double-use (`M=2`), absent (`M=0`) keys, over
`N in {1,2,3,6}`. Decisive test: does the finality verdict vector
`(can_finalize_now, max_authoritative_copies_ever, cost)` equal the resource
vector `(recoverable_now, total_recoveries, cost)` in every scenario?

## Success Criteria

- Lane B reopens only if a predeclared verdict-bearing finality quantity survives
  the resource reduction (a residue the monotone `M` cannot compute), with the
  full non-absorption burden met.
- The screen must confirm both lane-B death facts hold under the strengthened
  candidate: the encrypted clones reproduce the unreadable band (failure mode 1's
  object was real), and `A` is genuinely conserved (clearing failure mode 2, where
  `J+R` ran `1 -> 6`).

## Verdict

`COPY_LAW_SINGLE_USE_KEY_ABSORBED_BY_RESOURCE_MONOTONE`. The candidate clears the
*letter* of the wake condition -- `A` is a different quantity and, unlike `J+R`,
it is conserved (`A=1` band -> global). But every verdict-bearing finality quantity
factors through the bare consumable monotone `M`: all 12 scenarios have identical
finality and resource vectors, and the "exactly-once" distinction is itself a
monotone value (single- / double- / absent-key are split by `M`, not only by
finality). The only candidate residue -- which clone becomes authoritative -- is a
free symmetric choice, not a verdict. Non-absorption burden not met; the key IS
one-time-pad key-consumption. Lane B stays dead with a sharper epitaph; any
monogamy residue routes to the monogamy <-> quantum-secret-sharing strut (arXiv
2605.26866), not to lane B. Model:
`models/finality_encrypted_clone_single_use_key.py`; tests:
`tests/test_finality_encrypted_clone_single_use_key.py`; results:
`results/T520-copy-law-single-use-key-absorber-screen-v0.1-results.md`.
