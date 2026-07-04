# T443 Dolev Redundancy Feasibility Gate v0.1 Results

## Overall Verdict

`DOLEV_REDUNDANCY_FEASIBILITY_GATE_BUILT_NO_COST_CLAIM`

T443 keeps the surviving topology lead after T442, but moves it out of
thermodynamics and into robust-consensus feasibility. The finite gate encodes
the known synchronous point-to-point Byzantine threshold:

```text
n >= 3f + 1
vertex_connectivity(G) >= 2f + 1
```

## Key Fixture Results

| fixture | n | f | kappa(G) | required | admitted | reading |
|---|---:|---:|---:|---:|---|---|
| line k=5 | 5 | 1 | 1 | n>=4, kappa>=3 | no | not enough holder connectivity |
| star k=5 | 5 | 1 | 1 | n>=4, kappa>=3 | no | hub is a single cut point |
| cycle k=5 | 5 | 1 | 2 | n>=4, kappa>=3 | no | two-connected is still too weak |
| complete k=5 | 5 | 1 | 4 | n>=4, kappa>=3 | yes | robust-finality feasibility admitted |
| complete K4 | 4 | 1 | 3 | n>=4, kappa>=3 | yes | minimal complete f=1 pass |
| K3,3 | 6 | 1 | 3 | n>=4, kappa>=3 | yes | completeness not required |
| complete K6 | 6 | 2 | 5 | n>=7, kappa>=5 | no | node count blocks |
| cycle k=7 | 7 | 2 | 2 | n>=7, kappa>=5 | no | connectivity blocks |
| complete K7 | 7 | 2 | 6 | n>=7, kappa>=5 | yes | minimal complete f=2 pass |

## What This Earns

- A finite, executable admission gate for using topology in D1 holder-redundancy
  arguments.
- A clean post-T442 demotion: topology remains relevant only as feasibility
  unless a separate substrate earns a cost reading.
- A guardrail against reviving the refuted `lambda(G)` heat surcharge.

## What This Does Not Earn

- No thermodynamic cost floor.
- No H7 physical arrow.
- No new distributed-systems theorem.
- No claim-ledger, roadmap, North Star, canon, or public-posture movement.

## Verification

Passed:

```bash
python -m unittest tests.test_dolev_redundancy_feasibility_gate -v
python -m models.dolev_redundancy_feasibility_gate --write-results
python -m json.tool results/T443-dolev-redundancy-feasibility-gate-v0.1.json
```

The focused suite ran 7 tests. The model emitted
`results/T443-dolev-redundancy-feasibility-gate-v0.1.json`, and the JSON parsed.
