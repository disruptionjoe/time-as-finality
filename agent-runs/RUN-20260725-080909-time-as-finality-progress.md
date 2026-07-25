---
artifact_type: run_plan_and_receipt
status: complete
run_id: RUN-20260725-080909-time-as-finality-progress
parent_run_id: RUN-20260725-080909-repository-work-cycle-nbl-hourly
owner_id: time-as-finality
workflow: repo-progress-run
mode: execute
lane_id: "1"
starting_revision: 317e7b991c3c
---

# T225 Predictive-Absorption Computational Status

## Plan

Classify the exact status of T225's learned one-condition host predictor
without extending its binary corpus, evidence, or claim.

## Collision and Lane selection

The preceding T224 receipt is complete and pushed; no active run or writer
claim existed. Lane 1 is the only active numbered Lane. T225 is the explicit
next handoff and its finite corpus can be reconciled without touching the
higher-value but presently ineligible TaF-2/F4 paths.

## Execution and result

T225's `learn_rule` searches six declared Boolean conditions and checks seven
training plus two in-class holdout records. This is a polynomial-time
classifier in the size of its already encoded finite corpus, so the executable
classifier earns `poly_decider`. The empirical host prediction remains a
`finite_witness`: two hosts, one learned splitter, and holdouts sharing existing
signature classes cannot establish a scalable absorber theorem.

## Validation

- `python3 -m unittest tests.test_predictive_absorption_functor -v`: pass.
- Result JSON reproduced by the fixture and JSON parsed: pass.
- `LANES.yaml` and `LANE-STATE.yaml` parse: pass.
- `git diff --check`: pass.

## Receipt

Phase result: `progressed`. The ledger and Lane state now separate T225's
polynomial fixed-corpus classifier from its finite predictive evidence. No
claim, Canon Index, canon, North Star, Lane control, public posture,
publication, external action, Runtime, or cross-repository truth changed.

Next handoff: use the next bounded computational-status frontier only if it
preserves the fixed-corpus/no-scalability guard; TaF-2 and F4 remain higher
value but gated.
