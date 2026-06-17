# Time as Finality

**The past is what has become hard to undo.**

Time as Finality is an open research project testing whether observer-relative
temporal order and classical objectivity can be modeled through the
stabilization of physical records across causally bounded systems.

This is not a completed theory of physics. It is a claim-led formalization project: every major claim is labeled, linked, challenged, and paired with tests or failure conditions.

## Project Definition

Time as Finality asks whether:

> For an embedded record-processing system, a temporal partial order can be
> reconstructed from the causal partial order and stabilization frontiers of
> accessible records.

The project sits between foundations of time, quantum measurement, decoherence, classical objectivity, relativity, black-hole causal access, thermodynamics, and distributed-systems finality.

## What This Is

- An open formalization project.
- A conjecture suite with explicit failure conditions.
- A claim-by-claim research repository.
- A place to connect public essay claims to specific tests.
- A bridge language between record formation, temporal experience, and classical objectivity.
- An executable finite-graph model with documented positive and negative
  results.

## What This Is Not

- Not a finished physical theory.
- Not a replacement for quantum mechanics, special relativity, general relativity, or thermodynamics.
- Not a claim that human belief creates matter.
- Not a claim that decoherence alone solves the measurement problem.
- Not a claim that black-hole interiors are unreal.

## Start Here

- [TECHNICAL-NOTE-v0.1.md](TECHNICAL-NOTE-v0.1.md) - first formal result and
  evidence verdict.
- [TECHNICAL-REPORT-emergence-lab-v0.1.md](TECHNICAL-REPORT-emergence-lab-v0.1.md)
  - comparative result across reversible and irreversible local dynamics.
- [TECHNICAL-REPORT-proof-carrying-metastable-finality-v0.1.md](TECHNICAL-REPORT-proof-carrying-metastable-finality-v0.1.md)
  - coarse-graining, bounded proof verification, and Snowball-style consensus.
- [TECHNICAL-REPORT-compositional-finality-v0.1.md](TECHNICAL-REPORT-compositional-finality-v0.1.md)
  - evidence joins, inherited expression, recursive composition, and the
    failure of a universal finality semilattice.
- [TECHNICAL-REPORT-signed-readout-v0.1.md](TECHNICAL-REPORT-signed-readout-v0.1.md)
  - signed and interfering readout, with finite witnesses separating finality
    profiles from Born-style readout.
- [TECHNICAL-REPORT-integrated-finality-v0.1.md](TECHNICAL-REPORT-integrated-finality-v0.1.md)
  - integrated observer-context stress test across coupling, inherited
    expression, proof validation, consensus confidence, and signed readout.
- [TECHNICAL-REPORT-generated-integrated-finality-v0.1.md](TECHNICAL-REPORT-generated-integrated-finality-v0.1.md)
  - generated 448-case stress lab for integrated finality successes and
    breakpoints.
- [TECHNICAL-REPORT-dynamical-phase-records-v0.1.md](TECHNICAL-REPORT-dynamical-phase-records-v0.1.md)
  - local-dynamics derivation of signed record traces and cancellation.
- [COMPOSITIONAL-FINALITY-LAB.md](COMPOSITIONAL-FINALITY-LAB.md)
  - T11 mechanisms, checkpoint policies, epigenetic lens, and counterexamples.
- [PROOF-CARRYING-METASTABLE-LAB.md](PROOF-CARRYING-METASTABLE-LAB.md)
  - T10 mechanisms, baselines, and falsification criteria.
- [EMERGENCE-LAB.md](EMERGENCE-LAB.md) - laboratory definitions, physical
  assumptions, and required counterexamples.
- [FORMALISM.md](FORMALISM.md) - primitives, observer taxonomy, preorder, and
  reconstruction rule.
- [results/T1-v0.1-results.md](results/T1-v0.1-results.md) - reproducible test
  results and counterexample.
- [ESSAY.md](ESSAY.md) - public essay, linked claim by claim.
- [CLAIM-LEDGER.md](CLAIM-LEDGER.md) - status of every major claim.
- [HYPOTHESES.md](HYPOTHESES.md) - central hypothesis and failure conditions.
- [TESTS.md](TESTS.md) - formalization and falsification paths.
- [ROADMAP.md](ROADMAP.md) - best next contributions.
- [GLOSSARY.md](GLOSSARY.md) - working definitions.

## How To Contribute

Pick a claim. Strengthen it, formalize it, connect it to existing literature, or break it.

Good contributions include:

- a sharper definition of physical finality;
- a toy model that reconstructs observer-relative temporal order;
- a counterexample showing the framework smuggles primitive time back in;
- a literature note connecting a claim to prior work;
- a test case from quantum measurement, relativity, thermodynamics, or black-hole physics;
- a revision that makes the public essay harder to misunderstand.

See [CONTRIBUTING.md](CONTRIBUTING.md).

## Repository Map

```text
claims/         Claim-by-claim research notes.
tests/          Test proposals and toy formalization paths.
models/         Executable formal models.
results/        Reproducible model outputs and evidence verdicts.
literature/     Prior-art and known-neighbor notes.
open-problems/  Unresolved technical questions.
guardrails/     Explicit non-claims and misuse boundaries.
```

## Run The Formal Model

```bash
python -m unittest discover -s tests -p "test_*.py" -v
python -m models.run_t1
python -m models.run_emergence_lab
python -m models.run_proof_carrying_finality
python -m models.run_compositional_finality
python -m models.run_t12
python -m models.run_t13
python -m models.run_t14
python -m models.run_t15
python -m models.run_t16
```

## Citation / Reuse

This is early-stage open research. If you use the framing, please attribute the project and link back to the repository.
