# Sixth 15 research orchestration - 2026-06-27

## Scope

Continue the claim-ledger run with fifteen additional bounded synthesis tasks. This round stays additive: no production code, test, or ledger files are edited here. Each task produces a preflight note under `workflows/logs/synthesis/` that identifies the live blocker, the smallest next task, and a plain-English finding.

## Work packets

### Packet A - Q1 and detector infrastructure

1. `T177` Q1 absorber-owned field intake preflight.
2. `T171` detector row-review substitution preflight.
3. `T173/T175/T176/T178` detector authority and freeze-policy consolidation preflight.
4. `T123` same-payload FOA to `T97` integration preflight.
5. `N9/T182` Q1C named platform-family census preflight.

### Packet B - H7, S1, and sheaf bridges

6. `T168/N14` H7 sector/gauge absorber preflight.
7. `N11` H7 protected-memory absorber preflight.
8. `N12` H7 driven-dissipative absorber preflight.
9. `T151/T153` S1 Lorentzian causal-diamond witness preflight.
10. `T231/T236/T241` sheaf-H1 derived cofinality bridge preflight.

### Packet C - record finality, D1 boundary, and finite-to-smooth work

11. `T215` fixed native-network record-finality split preflight.
12. D1Cat cocomplete-boundary preflight.
13. Accessible-witness finite-to-smooth instantiation preflight.
14. `T223` S1 nonuniform-measure candidate intake preflight.
15. `T170` Q1D mature quantum-record framework bridge preflight.

## Plain-English reporting rule

For this round, the final report should say what these tasks found in ordinary language: which items are ready for bounded implementation, which are still evidence-gated, and which need a named external substrate or framework before the repo can claim progress.

## Verification plan

- Confirm that exactly the new synthesis files and this orchestration log are added.
- Run a focused markdown hygiene check over the new files.
- Run `git diff --check` after integration.

