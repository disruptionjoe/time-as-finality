# Steward Memory Log — Time as Finality

Chronological run/learning log for this repo's steward (per the CapacityOS Steward
Protocol, step 7). Append newest entries at the bottom of each section. Durable,
recurring, high-value lessons get promoted into the steward summary (`AGENTS.md`).
Routine detail stays here; it is not loaded by default.

## Runs

| date | run | mode | outcome | note |
|---|---|---|---|---|
| 2026-06-30 | RUN-20260630-031 | steward rollout | completed | Replaced AGENTS.md with the tailored steward contract (folded in prior North Star orientation); added `_local/` to .gitignore. |
| 2026-06-30 | RUN-20260630-032 | progress | completed | Extracted CONTRIBUTING claim/test file shapes into copy-ready `templates/` + index. |
| 2026-06-30 | RUN-20260630-033 | stewardship | completed | Stood up this log; consistency sweep clean. |

## Learnings

- **2026-06-30 — folding an existing AGENTS.md preserves repo orientation.** The
  old AGENTS.md here was a "Read First" North Star map, not a steward contract.
  Folding its orientation links into the new contract's "Read first" section (rather
  than discarding them) kept the only allowed overwrite lossless. *Generalizable
  method learning — flag for upward emit to CapacityOS System (Learning Intake):
  when a repo's pre-existing AGENTS.md carries repo-specific orientation/North-Star
  facts, the rollout must transcribe those into the new contract before replacing,
  not just append the standard contract.*
- **2026-06-30 — consistency sweep.** `.gitignore` ignores `_local/`; AGENTS.md
  artifact zones (public library `JB/library/repos/public/time-as-finality/`, vault,
  `_local/` scratch) match the locked Information Classification; the new `templates/`
  shapes are byte-faithful to the shapes in `CONTRIBUTING.md` and assert no claims;
  `templates/README.md` points back at CONTRIBUTING and restates (not overrides) the
  promotion gates. No transcribe-then-retire obligation outstanding.
## 2026-07-01

- Stewardship fleet pass preserved the high-gravity audit and T392 finite-witness artifacts while leaving claim ledger and roadmap unchanged. See `steward/runs/2026-07-01-stewardship-fleet-pass.md`.
- Discovery fleet pass found attention-weighting is the main need: review pending high-gravity audit material and keep complexity/theorem language disciplined. See `steward/runs/2026-07-01-discovery-fleet-pass.md`.
- Progress run advanced Direction A without touching the active T392/T393 lane. It created `technical-reports/TECHNICAL-REPORT-direction-a-finite-anti-scalar-generalization-v0.1.md` and `steward/runs/2026-07-01-direction-a-progress-run.md`, sharpening the anti-scalar gate: exact scalar failure is easy, but scalar tie-collapse resistance is the real next executable target.
- Progress run advanced Direction C without touching the active T392/T393/T395 lane. It created T396 consensus-cost additivity artifacts and `steward/runs/2026-07-01-direction-c-consensus-cost-additivity-gate.md`; finite bit-consensus cost collapses to ordinary `H(X)-H(Y)` entropy bookkeeping unless a future substrate-native protocol adds reliability, finite-time, communication-geometry, metastability, or reset-dynamics constraints.
- Progress run blocked on collision with recent active local work. The worktree already had dirty `TESTS.md` plus T392-T395 model/test/result/audit surfaces, so the run recorded `steward/runs/2026-07-01-progress-run-collision-receipt.md` and did not select a new research artifact.
- Progress run closed and versioned the active T397 batch rather than starting a competing lane. The batch includes the multipath class-marker absorber and the region-indexed capability no-go; both keep the T397 number collision explicit and pause renumbering for Joe. Verification: 11 multipath tests, 34 region-capability tests, 111 imported T392-T395 tests, and both T397 JSON files parsed. No claim-ledger movement; next gate is the resource-theory absorber for the C(R) profile object. See `steward/runs/2026-07-01-close-t397-capability-batch.md`.
## 2026-07-02

- Progress run created T398, the resource-profile absorber for T397's `C(R)` object. Verdict: once C(R) profiles are admitted as resource states under the declared region/menu/task context, the T397 profile quotient is exactly a 3 x 4 product resource preorder; anti-scalar shape and statistics-flat class are absorbed as resource-preorder behavior / incomplete observer shadow. No claim-ledger movement. See `steward/runs/2026-07-02-resource-profile-absorber.md`.
- Progress run created T399, the boundary-crossing intervention statistics screen. Verdict: the strengthened formal shape exists in a Bell-pair fixture (all R-supported statistics/interventions equal, joint boundary menu separates), but it is absorbed by ordinary enlarged-state access and boundary relocation. No claim-ledger movement. See `steward/runs/2026-07-02-boundary-crossing-intervention-screen.md`.
- Progress run created T400, the boundary-forced task gate. Verdict: T399-style optional enlarged-state access fails the new gate; hidden-datum, closure-key, and class-marker shortcuts are blocked; a synthetic R:B parity task passes only as a formal positive control. No domain-native physical/finality task or claim-ledger movement is earned. See `steward/runs/2026-07-02-boundary-forced-task-gate.md`.
- Progress run created T401, the finality-boundary reconciliation screen. Verdict: aligned and anti-aligned two-holder record distributions have identical region and boundary-local statistics, including the declared finite R intervention menu, while the predeclared merged/final record task forces the R:B same/different relation and separates. This clears the finite finality-task shape but is absorbed by ordinary joint-record completion; no claim-ledger movement. See `steward/runs/2026-07-02-finality-boundary-reconciliation-screen.md`.
- Progress run created T402, the causal-domain boundary forcing screen. Verdict: a finite 1+1 common-future verdict event clears the physical-substrate forced-task shape, with R-only and B-only domains unable to determine the separator while the joint R:B domain can; the result is absorbed by ordinary causal-domain completion plus joint input access. No claim-ledger movement. See `steward/runs/2026-07-02-causal-domain-boundary-forcing-screen.md`.
- Progress run created T403, the same-domain finality-lock screen. Verdict: with T402 causal-domain data, joint payload, verdict payload, revision budget, and operation menu all matched, provisional vs sealed record state splits only `can_revise_final_verdict`; explicit finality-state completion absorbs the split. No claim-ledger movement. See `steward/runs/2026-07-02-same-domain-finality-lock-screen.md`.
- Progress run created T405, the physical-latch finality-lock screen, while leaving an unrelated untracked T404 resource-theory absorber draft untouched. Verdict: replacing T403's stipulated flag with rewritable-vs-fused latch topology gives a `can_revise_final_verdict` split under matched causal, joint-payload, resource, provenance, control, and boundary accounting, but explicit latch-substrate completion absorbs it. No claim-ledger movement. See `steward/runs/2026-07-02-physical-latch-finality-lock-screen.md`.
