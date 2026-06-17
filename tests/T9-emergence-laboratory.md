# T9: Emergence Laboratory

## Target Claims

- [D1: Physical Finality Definition](../claims/D1-physical-finality-definition.md)
- [C1: Experienced Time As Record Finality](../claims/C1-experienced-time-as-record-finality.md)
- [T5: Thermodynamic Record Support](T5-thermodynamic-record-support.md)

## Setup

Compare all 256 elementary binary radius-one cellular-automaton rules on a
finite periodic lattice with reversible second-order lifts of the same rules.

Generate records from counterfactual seed influence rather than hand-authored
record tokens. Derive actual-sensitivity causal edges from Boolean
derivatives. Restrict terminal traces to bounded observer windows.

## Success Criteria

- The same record definition runs on reversible and irreversible substrates.
- Reversibility and information loss are exhaustively checked.
- Observer-relative access differences arise without changing the dynamics.
- Graph, computational, and thermodynamic reversal quantities are reported
  separately.
- Minimal counterexamples and failed universality claims are preserved.

## Failure Criteria

- Records require external pattern labels.
- Reversible and irreversible substrates require unrelated definitions.
- Landauer cost is inferred from Hamming distance without an information-loss
  calculation.
- Finite brute-force search is called computational irreducibility.
- Update steps are falsely described as a derivation of time itself.

## Result

Status: **implemented; comparative success with major narrowing**.

Run:

```bash
python -m unittest discover -s tests -p "test_*.py" -v
python -m models.run_emergence_lab
```

Evidence:

- [Emergence Lab results](../results/emergence-lab-v0.1-results.md)
- [Comparative technical report](../TECHNICAL-REPORT-emergence-lab-v0.1.md)
- [Machine-readable output](../results/emergence-lab-v0.1.json)

## Contribution Needed

Replace the chosen terminal observer windows with observers that are
themselves persistent dynamical subsystems, then test whether access and
record interpretation can be generated rather than stipulated.
