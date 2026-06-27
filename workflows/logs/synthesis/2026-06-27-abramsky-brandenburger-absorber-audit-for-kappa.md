---
document_type: synthesis_absorber_audit
created: 2026-06-27
status: complete
authority: guidance_only
write_scope: workflows/logs/synthesis
claim_updates: none
---

# Abramsky-Brandenburger Absorber Audit For Kappa

## Status

This is a non-authoritative synthesis artifact for queue item 2 in
`workflows/logs/best-next-move/2026-06-27-next-10-research-orchestration.md`.
It does not update `CLAIM-LEDGER.md`, `ROADMAP.md`, tests, results, code, or
open-problem text.

Synthesis verdict: still conditional with named residue. The residue is the
missing Abramsky-Brandenburger-native absorber run: a target empirical model and
native contextuality rank must be frozen independently of source `kappa_A`, and
the harness must include a branch where kappa can miss. No "closed" upgrade is
licensed.

## Read Surfaces Used

- `CLAIM-LEDGER.md` Canon Index, CSP-PO1/kappa row, H1-Sheaf row, Q1D row, and
  2026-06-26 kappa correction.
- `open-problems/typed-loss-transport-test.md`.
- `tests/T224-typed-loss-transport-test.md` and
  `results/typed-loss-transport/T224-results.json`.
- `tests/T229-kappa-rank2-second-absorber.md` and
  `results/kappa-rank2/T229-results.json`.
- `tests/T234-kappa-genre-crossing-third-absorber.md` and
  `results/kappa-genre-crossing/T234-results.json`.
- `tests/T239-kappa-noncycle-genre-quorum-intersection.md` and
  `results/kappa-quorum-intersection/T239-results.json`.
- `tests/T244-kappa-value-gap-noncombinatorial-genre.md` and
  `results/kappa-value-gap/T244-results.json`.
- `tests/T13-finality-sheaf-cohomology.md`.
- `tests/T21-bell-contextuality-finality.md`,
  `results/bell-contextuality-finality-v0.1-results.md`,
  `results/bell-contextuality-finality-v0.1.json`, and
  `technical-reports/TECHNICAL-REPORT-bell-contextuality-finality-v0.1.md`.
- `results/coefficient-sheaf-h1/T226-coefficient-sheaf-h1-v0.1.json`.
- `literature/N6-signed-readout-anchors.md` and
  `literature/N7-q1a-measurement-neighbors.md` as available neighbor notes.

## AB-Native Obstruction First

The AB-native object must be defined before any kappa comparison.

Use the sheaf-contextuality shape, in repo-compatible terms:

```text
measurement scenario = (measurements X, contexts M, outcomes O)
event presheaf E(U) = assignments U -> O
empirical model e = compatible local data on each context C in M
AB obstruction = no global section/global distribution on E(X)
                 restricts to the declared local context data
```

For the finite, possibilistic fragment used by T13/T21, this is the repo's
local-section/no-global-section pattern:

```text
all local context sections exist
named overlaps are compatible
no global assignment exists
```

T21's CHSH case is the existing finite referent: four compatible local contexts
exist, but the parity product is `-1` while any global assignment would force
`+1`. T226 shows the adjacent coefficient-aware finite H1 lesson: carrying the
transition/coefficient data matters, and coefficient-blind encoding can report a
false section.

The AB absorber audit therefore measures target contextuality natively from the
empirical model or support presheaf first. It must not start by emitting one
frustrated signed cycle per desired rank.

## Current Kappa State To Audit Against

The existing kappa suite is positive as a finite re-encoding catalogue, but the
2026-06-26 ledger correction blocks the stronger reading:

- T224: T39 signed-cover `kappa` maps to T21 CHSH presence, rank fragment
  `{0,1}`.
- T229: two-box CHSH reaches rank 2.
- T234: Arrow/Condorcet reaches a second native genre.
- T239: CAP/Helly quorum-intersection reaches a non-cycle finite set genre and
  rank 3.
- T244: value-gap reaches a finite real-threshold absorber and rank 3.

The correction: paired fixtures write the same integer into source cover,
target native rank, and synthetic `nu` cover. The earned statement is one
untuned `compute_kappa` re-expressing five structurally distinct finite native
obstruction notions. Not earned: prediction, genre-agnostic status, or closure.

## Audit Protocol

1. Freeze the source panel:
   - choose source instances with `kappa_A` in `{0,1,2,3}` before target
     construction;
   - store only variables, signed edges, `nu_A`, and computed `kappa_A`;
   - do not let source rank determine target context count or target native
     rank.
2. Freeze the AB target panel:
   - define measurement set `X`, context cover `M`, outcome set `O`, and local
     support/probability data for each target model;
   - compute AB-native status from the target only: global section exists,
     strong/possibilistic contextuality status, and an explicit native rank or
     residue measure if one is justified;
   - record noncontextual controls with global sections.
3. Only after both panels are frozen, define the candidate transport map:
   - map source `nu_A` to the AB measurement-cover data without adding cells
     just to match `kappa_A`;
   - state exactly what structure is preserved;
   - reject any map that merely copies the integer rank into target layout.
4. Compare:
   - predicted kappa value from the source;
   - AB-native value from target empirical model/support;
   - kappa computed on any derived target `nu_B`;
   - mismatch must be reported as a miss, not repaired by changing the target.
5. Include falsifying branches:
   - at least one target whose AB-native rank is lower than source `kappa_A`;
   - at least one target whose AB-native obstruction exists but the proposed
     binary `nu_B` encoding fails to recover it;
   - at least one noncontextual target where a count-all or raw-cell classifier
     would over-report.

## Required Branches

| Branch | Purpose | Pass/fail value |
| --- | --- | --- |
| AB positive control | T21-style CHSH support with local sections and no global section. | Confirms the AB-native solver detects contextuality without kappa. |
| AB null control | Classical/noncontextual support with a global section. | Confirms native rank can be zero. |
| Rank-decoupled source control | Source `kappa_A = 2` or `3`, target AB model frozen with native rank `1`. | Must report a kappa miss if prediction says `2` or `3`. |
| Encoding-loss control | AB-native obstruction present, proposed binary `nu_B` rank zero or undefined because coefficient/context data were lost. | Distinguishes AB contextuality from coefficient-blind signed-cover reuse. |
| Count-all adversary | Raw context/cell count predicts obstruction where AB global section exists. | Confirms the harness can reject pass-by-design counting. |

The rank-decoupled and encoding-loss controls are the key missing pieces in the
current kappa suite. Without them, the audit repeats the construction flaw the
2026-06-26 ledger identified.

## Verdict Options

- `absorbed`: AB-native contextuality fully reconstructs the kappa catalogue, and
  kappa adds no residue beyond AB empirical-model contextuality.
- `still conditional with named residue`: AB explains the current finite
  catalogue, but a named residue remains, such as a transport map that predicts a
  target-native value after both source and target are frozen independently.
- `inconclusive for precise missing object`: the AB-native rank, target panel, or
  falsifying branch is not yet built.

Current synthesis verdict: `still conditional with named residue`. The named
residue is the absent independent AB target panel plus falsifying branch. Until
that exists, the safer claim is that kappa is a finite multi-absorber
re-encoding catalogue awaiting the decisive AB absorber.

## Acceptance Criteria Satisfaction

| Criterion from queue item 2 | Satisfied here |
| --- | --- |
| Defines the AB native obstruction independently before any kappa comparison. | Yes: see AB-Native Obstruction First. |
| Freezes source instances without writing the target native rank by construction. | Yes: see Audit Protocol steps 1-3. |
| Includes a falsifying branch where kappa can miss, not only a pass-by-design fixture. | Yes: see Required Branches, especially rank-decoupled and encoding-loss controls. |
| Verdict is absorbed, still conditional with named residue, or inconclusive for precise missing object; no "closed" upgrade. | Yes: current verdict is `still conditional with named residue`; no closure is licensed. |

## No-Claim-Promotion Guardrail

This note authorizes no implementation and no status edit. It should be used as
the acceptance envelope for a later test/results turn. Until that turn builds
the AB-native target panel and reports at least one possible miss branch, do not
describe kappa as closed, predictive, genre-agnostic, or prior-art-separated from
AB sheaf contextuality.
