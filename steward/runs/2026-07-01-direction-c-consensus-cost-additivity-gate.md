# Time As Finality Progress Run

Status: completed.

Run family: Repo Progress Run.

Target repo: Time As Finality.

Automation: Hourly Nobel Prize Winner.

Started: 2026-07-01T20:05:34-05:00 local.

## Required Reads

- `AGENTS.md`
- `steward/README.md`
- `Vision - North Star.md`
- `Method - Research Program Guidelines.md`
- `Lead Research Line - Time as Finality.md`
- `CONTRIBUTING.md`
- `ROADMAP.md`
- `HYPOTHESES.md`
- `CLAIM-LEDGER.md`
- `COMPLEXITY-LEDGER.md`
- `TESTS.md`
- `audits/2026-07-01-high-gravity-research-directions.md`
- T110/T142/T145 thermodynamic-arrow neighborhood

## Worktree Boundary

The worktree already contains active or pre-existing T392/T393/T394/T395
material and a dirty `TESTS.md`. This run did not edit, stage, or commit
those files.

`TESTS.md` will not be edited in this run. T396 will be treated as an
unregistered executable gate until the active lane is settled and the registry
can be updated coherently.

## Selected Objective

Advance Direction C from `audits/2026-07-01-high-gravity-research-directions.md`
with a finite additivity gate:

```text
Does a record-consensus cost bound contain anything beyond ordinary entropy
reduction / erasure bookkeeping once the input distribution, consensus rule,
and exported transcript are declared?
```

This is the biggest safe non-overlapping one-session move because Direction A
has already advanced through T394 and active T395, Direction B is tied to the
T392/T393 lane, and Direction C is explicitly always-on.

## Plan

1. Implement `models/consensus_cost_additivity_gate.py`.
2. Add focused unit tests in `tests/test_consensus_cost_additivity_gate.py`.
3. Generate `results/T396-consensus-cost-additivity-gate-v0.1.json`.
4. Write `results/T396-consensus-cost-additivity-gate-v0.1-results.md`.
5. Append this run receipt and steward memory.

## Governance Boundary

No North Star changes.

No claim-status, public-posture, roadmap, or cross-repo truth changes.

No claim-ledger edit unless a future integrator chooses to register the result.

## Execution

Created:

- `models/consensus_cost_additivity_gate.py`
- `tests/test_consensus_cost_additivity_gate.py`
- `results/T396-consensus-cost-additivity-gate-v0.1.json`
- `results/T396-consensus-cost-additivity-gate-v0.1-results.md`

Main result:

- root-copy independent inputs give the expected `k - 1` bit erasure floor;
- already-consensus inputs cost zero despite five holders, refuting
  holder-count-only lower bounds;
- majority, parity, and single-error fixtures are explained by
  `H(X|Y)` plus ordinary conditional-correlation bookkeeping;
- exporting the full transcript makes the closed reversible control cost zero;
- no standalone consensus-structure thermodynamic term is earned in the
  declared finite map.

## Verification

Ran:

```text
python -m unittest tests.test_consensus_cost_additivity_gate -v
python -m models.consensus_cost_additivity_gate
python -m json.tool results\T396-consensus-cost-additivity-gate-v0.1.json
```

Result:

```text
9 tests passed.
JSON validated.
```

## Governance Result

No North Star changes.

No canon, claim status, public posture, roadmap, or cross-repo truth changes.

No `TESTS.md` edit because it is part of the active dirty lane.

## Receipt

Direction C now has a finite additivity gate. The current weak form of the
record-consensus thermodynamic bound collapses to entropy bookkeeping:
`H(X)-H(Y)` under coarse graining, and zero cost under full transcript export.
The next worthy Direction C artifact must add substrate-native finite-time,
reliability, communication-geometry, metastability, or reset-dynamics
constraints before claiming any consensus-specific thermodynamic residue.

Completed: 2026-07-01T20:09:23-05:00 local.
