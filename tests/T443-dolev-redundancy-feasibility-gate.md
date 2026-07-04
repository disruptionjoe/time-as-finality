# T443: Dolev Redundancy Feasibility Gate

## Target Claims

- A1, as a distributed-systems finality analogy under explicit absorber
  discipline.
- D1 holder-redundancy axis, narrowly reframed after T442 hostile review.

## Setup

T442's hostile review refuted the topological thermodynamic surcharge. The
surviving lead is weaker and cleaner: topology belongs to robust-consensus
feasibility, not heat cost.

T443 encodes a finite audit gate for the classical synchronous point-to-point
Byzantine setting:

```text
n >= 3f + 1
vertex_connectivity(G) >= 2f + 1
```

Reference checked: Danny Dolev, "The Byzantine Generals Strike Again" (1982),
which states the `3t + 1` and `2t + 1` network-connectivity condition for the
classical setting. This repo artifact does not re-prove that theorem; it uses
the known condition as an absorber-owned admission gate for TaF holder
redundancy.

## Success Criteria

- Compute exact finite vertex connectivity for small undirected graphs.
- Admit `f=1` fixtures only when `n >= 4` and `kappa(G) >= 3`.
- Admit `f=2` fixtures only when `n >= 7` and `kappa(G) >= 5`.
- Reframe the T442 line/star/cycle/complete family as feasibility: only the
  complete k=5 graph admits one Byzantine holder fault under this gate.
- Make no thermodynamic-cost claim.

## Failure Criteria

- If the gate reintroduces `lambda(G)` or any other graph term as a heat cost,
  the run fails.
- If line/star/cycle fixtures are admitted for `f=1`, the vertex-connectivity
  condition is under-enforced.
- If complete `K6` is admitted for `f=2`, the `3f + 1` node-count condition is
  under-enforced.
- If complete `K7` is blocked for `f=2`, the admission gate is too strict.

## Known Physics Constraints

This is not a physics result. It is a distributed-systems feasibility screen
used to keep the D1 holder-redundancy analogy honest after the T442 heat-cost
demotion.

## Contribution Needed

- Decide whether this feasibility gate should become the required admission
  screen before future D1 holder-redundancy artifacts.
- Any later thermodynamic reading must pass T439/T441-style substrate gates and
  cannot inherit support from this topology feasibility result alone.

## Reproduction

```bash
python -m unittest tests.test_dolev_redundancy_feasibility_gate -v
python -m models.dolev_redundancy_feasibility_gate --write-results
python -m json.tool results/T443-dolev-redundancy-feasibility-gate-v0.1.json
```
