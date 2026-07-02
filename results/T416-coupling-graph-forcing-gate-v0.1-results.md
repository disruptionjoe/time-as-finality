# T416 - Coupling-Graph Forcing Gate - Results v0.1

- **Artifact:** `T416-coupling-graph-forcing-gate-v0.1`
- **Spec:** [tests/T416-coupling-graph-forcing-gate.md](../tests/T416-coupling-graph-forcing-gate.md)
- **Model:** [models/coupling_graph_forcing_gate.py](../models/coupling_graph_forcing_gate.py)
- **Test:** [tests/test_coupling_graph_forcing_gate.py](../tests/test_coupling_graph_forcing_gate.py)
- **Tags:** R2, coupling_graph, factorization_guardrail, operational_automorphism,
  separator_refactorization, no_claim_promotion

## Verdict

T416 does not discharge R2. It narrows the burden.

The parity separator itself does **not** force the operational automorphism
group. Separator-only evidence admits the full T415 equality-preserving class:
24 reversible linear refactorizations, including 18 entangling
equality-preservers. That is too broad to count as a product/coupling
admissibility rule.

Independent operational evidence can force the admissible class locally:

| Evidence packet | Linear admissible count | With local bit flips | Entangling equality-preservers admitted | Standing |
| --- | ---: | ---: | ---: | --- |
| Separator only | 24 | 192 | 18 | insufficient for R2 |
| Singleton operation support | 6 | 48 | 0 | product atoms forced up to permutation, if independent |
| Path coupling graph `0-1-2` | 2 | 16 | 0 | path graph forced up to reversal, if independent |

The named T415 entangling equality-preserver
`y0=x0^x2, y1=x1^x2, y2=x2` preserves the separator equality and global parity,
but fails singleton-operation support: source factor `x2` spreads over all three
output factors. The fan-in localizer also fails singleton support.

## What This Earns

T416 converts T415's R2 remainder into a concrete gate:

```text
separator-preserving relabels are not enough;
the run must supply independent operation or coupling evidence
```

If that evidence is present, the admissible automorphism group is not a free
declaration in the local fixture. If it is absent, the separator remains
factorization-relative.

## What This Does Not Earn

- No physics claim.
- No claim-ledger movement.
- No proof that any real coupling graph is physically forced.
- No discharge of the broader "why are agents bounded" / R2 problem.

## Reproduction

```bash
python -m pytest tests/test_coupling_graph_forcing_gate.py -q
python -m models.coupling_graph_forcing_gate
```

Focused verification during this run: `7 passed`.
