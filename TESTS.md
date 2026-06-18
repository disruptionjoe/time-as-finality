# Tests

The project is useful only if claims can be formalized, stressed, or broken.

## Test Index

| ID | Test | Target claims | Status |
| --- | --- | --- | --- |
| [T1](tests/T1-record-graph-temporal-reconstruction.md) | Record graph temporal reconstruction | C1, D1, D2 | implemented: partial success |
| [T2](tests/T2-quantum-measurement-record-finality.md) | Quantum measurement record finality | Q1, D1, G2 | implemented: dynamical measurement finality lab |
| [T3](tests/T3-spacelike-events-no-global-commit-order.md) | Spacelike events and no global commit order | R1, G2 | open |
| [T4](tests/T4-black-hole-causal-access-boundary.md) | Black-hole causal access boundary | B1, G2 | open |
| [T5](tests/T5-thermodynamic-record-support.md) | Thermodynamic record support | D1, C1 | structural benchmark implemented |
| [T6](tests/T6-snowball-record-finality.md) | Snowball record finality | A1, D1, Q1 | open |
| [T7](tests/T7-overlapping-causal-domains.md) | Overlapping causal domains | R1, B1, S1 | open |
| [T8](tests/T8-observer-renderer-toy-model.md) | Observer renderer toy model | D2, G3 | open |
| [T9](tests/T9-emergence-laboratory.md) | Emergent records across reversible and irreversible local dynamics | D1, C1, T5 | implemented: comparative success |
| [T16](tests/T16-spacetime-aggregation.md) | Spacetime aggregation toy model | S1, H5, R1 | implemented: finite gluing and obstruction witnesses |
| [T17](tests/T17-consensus-finality-crosswalk.md) | Consensus finality crosswalk | A1, D1 | implemented: collapse maps and bounded theorem check |
| [T18](tests/T18-finality-direction-theorem.md) | Finality direction theorem | H7, D1 | implemented: constructor-style finite theorem check |
| [T20](tests/T20-consensus-record-theorem-transfer.md) | Consensus-record theorem transfer | A1, D1, T13, T17 | implemented: theorem-transfer and boundary cases |
| [T21](tests/T21-bell-contextuality-finality.md) | Bell contextuality finality | Q1, D1, T13, T20 | implemented: CHSH contextuality and score comparison |
| [T22](tests/T22-d1-physical-reduction-map.md) | D1 physical reduction map | D1, Q1, T2, T21 | implemented: observable audit and holder-redundancy reduction |
| [T23](tests/T23-invariant-preserving-transformations.md) | Invariant-preserving transformations | IPT, D1, Q1, A1, T2, T20, T22 | implemented: typed IPT kernel, composition check, and obstruction witness |
| [T24](tests/T24-d1-multiscale-observer-field.md) | D1 multiscale observer field | D1, D1-Field, IPT, T13, T21, T23 | implemented: scalar/vector/field audit with transport and gluing counterexamples |
| [T25](tests/T25-minimal-d1-generalization.md) | Minimal D1 generalization | D1, D1-Field, IPT, T13, T21, T23, T24 | implemented: H0-H4 audit and theorem ladder |
| [T26](tests/T26-d1-restriction-system.md) | D1 restriction system | D1, D1-Field, IPT, T25 | implemented: finite graph-indexed D1 restriction object and morphism checks |
| [T27](tests/T27-class-relative-bridge-audit.md) | Class-relative bridge audit | D1RestrictionSystem, PO1 | implemented: GU bridge audit with faithful and non-definable cases |
| [T28](tests/T28-cap-theorem-bridge.md) | CAP theorem bridge | D1RestrictionSystem, PO1, T27 | implemented: CAP as finite gluing obstruction with NN structural comparison |
| [T29](tests/T29-projection-obstruction-schema.md) | Projection-Obstruction Schema | PO1, T26, T27 | implemented: finite schema with positive and boundary cases |
| [T30](tests/T30-cross-domain-projection-obstruction-validation.md) | Cross-domain projection-obstruction validation | PO1, T29 | implemented: hostile non-physics validation with Git and financial risk positives plus translator/poet boundary |
| [T31](tests/T31-po1-admissibility-conditions.md) | PO1 admissibility conditions | PO1, T29, T30 | implemented: seven-condition admissibility checklist and case reclassification |
| [T32](tests/T32-admissibility-derivation.md) | PO1 admissibility derivation | PO1, T31 | implemented: AC dependency graph, minimal basis, and generated subset counterexamples |
| [T33](tests/T33-po1-foundational-derivation.md) | PO1 foundational derivation | PO1, T32 | implemented: IPT/RMT hypothesis matrix (H0-H5); H3 best supported; AC5-naming recommended as Principle P5 |
| [T34](tests/T34-po1-chained-projection.md) | Chained projection analysis | PO1, T29, T31, T32, T33 | implemented: emergent, stepwise, and absorbed obstruction confirmed across three chain shapes |
| [T35](tests/T35-projection-obstruction-discovery-engine.md) | Projection-obstruction discovery engine | PO1, T31, T33, T34 | implemented: bounded finite exploration engine with generated positives, boundaries, and counterexamples |
| [T36](tests/T36-compression-finality-crosswalk.md) | Compression-finality crosswalk | D1, C1, T9 | implemented: finality≠compressibility confirmed; Rule 30 and Rule 0 counterexamples; correlations partial (−0.745, +0.631) |
| [T37](tests/T37-typed-transport-network.md) | Typed transport network | PO1, T26, T31, T34 | implemented: path-dependent admissibility witnessed; diamond network shows same (source, target) with different paths giving different PO1 verdicts (AC5 varies by path) |
| [T38](tests/T38-minimal-multiscale-transport.md) | Minimal multiscale transport | H1+, T26, T31, T37 | implemented: H0 covers 3/10 questions; H1 covers 8/10; H1+ (TypedTransportNetwork + CompressionRecord + EmergenceRecord) covers all 10; H2 and H3 not required |
| [T39](tests/T39-csp-satisfiability-reframing.md) | CSP / satisfiability reframing | PO1, T26, T31, T38 | implemented: PO1 gluing obstruction = binary {-1,1} parity-conflict CSP; arc consistency trivially true; typed projection (AC5, AC7) and admissibility classification are new structure not expressible in standard CSP; H_B best supported |
| [T40](tests/T40-holarchy-lab.md) | Holarchy lab — emergent holonic finality | D1, PO1, TTN, T38, T39 | implemented: holonic emergence confirmed (3-node triangle obstruction from micro-compatible nodes); cross-level AC5 necessary for holonic PO1; H_B best supported |
| [T41](tests/T41-typed-transport-category.md) | Typed transport category prototype | D1, PO1, T26, T31, T34, T37 | implemented: D1RestrictionMorphisms form a proper category (associativity 4/4, left unit 5/5, right unit 5/5); PO1 is not a Boolean functor on D1Cat (T34 restated in categorical language); H_A best supported |
| [T42](tests/T42-local-persistence-reconciliation-split.md) | Local persistence and reconciliation split audit | R1, G2, D1, T3 | implemented: LocalPersistenceReconciliationSystem separates local accumulation from reconciliation lag; four witnesses pass (delay-only, accumulation-only, both, null); H2 best supported |
| [T43](tests/T43-local-persistence-mechanisms.md) | Local persistence accumulation mechanism audit | R1, G2, D1, T42 | implemented: intrinsic rate, resource budget, and interaction density produce local differences with propagation fixed; propagation-shadow rejected; H4 best supported |
| [T44](tests/T44-local-mechanism-identifiability.md) | Local mechanism identifiability audit | R1, G2, T42, T43 | implemented: baseline traces remain ambiguous, but demand-drop plus coupling-rewire separates intrinsic rate, resource budget, and interaction density; H4 best supported |

## Minimum Compatibility Constraints

Any formalization must:

- preserve no-signalling;
- preserve proper time and invariant interval structure;
- distinguish physical record-stability from human belief;
- distinguish local access loss from physical reversal;
- not treat decoherence as a complete measurement-problem solution;
- not derive the thermodynamic arrow by assertion;
- not require a hidden universal present;
- not treat probabilistic consensus finality as absolute truth.
- not deny remote observation as causal record access.
- not treat observer rendering as mind-created matter.

## Executable Suite

```bash
python -m unittest discover -s tests -p "test_*.py" -v
python -m models.run_t1
python -m models.run_t2
python -m models.run_emergence_lab
python -m models.run_t16
python -m models.run_t17
python -m models.run_t18
python -m models.run_t20
python -m models.run_t21
python -m models.run_t22
python -m models.run_t23
python -m models.run_t24
python -m models.run_t25
python -m models.run_t26
python -m models.run_t27
python -m models.run_t28
python -m models.run_t29
python -m models.run_t30
python -m models.run_t31
python -m models.run_t32
python -m models.run_t33
python -m models.run_t34
python -m models.run_t35
python -m models.run_t36
python -m models.run_t37
python -m models.run_t38
python -m models.run_t39
python -m models.run_t40
python -m models.run_t41
python -m models.run_t42
python -m models.run_t43
python -m models.run_t44
```

The suites use only Python's standard library. Evidence records:

- [T1 v0.1 Results](results/T1-v0.1-results.md)
- [Quantum Measurement Finality v0.1 Results](results/quantum-measurement-finality-v0.1-results.md)
- [Emergence Laboratory v0.1 Results](results/emergence-lab-v0.1-results.md)
- [Spacetime Aggregation v0.1 Results](results/spacetime-aggregation-v0.1-results.md)
- [Consensus Finality Crosswalk v0.1 Results](results/consensus-finality-crosswalk-v0.1-results.md)
- [Finality Direction Theorem v0.1 Results](results/finality-direction-theorem-v0.1-results.md)
- [Consensus-Record Theorem Transfer v0.1 Results](results/consensus-record-theorem-transfer-v0.1-results.md)
- [Bell Contextuality Finality v0.1 Results](results/bell-contextuality-finality-v0.1-results.md)
- [D1 Physical Reduction Map v0.1 Results](results/d1-physical-reduction-map-v0.1-results.md)
- [Invariant-Preserving Transformations v0.1 Results](results/invariant-preserving-transformations-v0.1-results.md)
- [D1 Multiscale Observer Field v0.1 Results](results/d1-multiscale-observer-field-v0.1-results.md)
- [Minimal D1 Generalization v0.1 Results](results/minimal-d1-generalization-v0.1-results.md)
- [D1 Restriction System v0.1 Results](results/d1-restriction-system-v0.1-results.md)
- [GU Class-Relative Bridge v0.1 Results](results/gu-class-relative-bridge-v0.1-results.md)
- [CAP Theorem Bridge v0.1 Results](results/cap-theorem-bridge-v0.1-results.md)
- [Projection-Obstruction Schema v0.1 Results](results/projection-obstruction-schema-v0.1-results.md)
- [Cross-Domain Projection-Obstruction Validation v0.1 Results](results/cross-domain-projection-obstruction-validation-v0.1-results.md)
- [PO1 Admissibility Conditions v0.1 Results](results/po1-admissibility-conditions-v0.1-results.md)
- [PO1 Admissibility Derivation v0.1 Results](results/po1-admissibility-derivation-v0.1-results.md)
- [PO1 Chained Projection v0.1 Results](results/po1-chained-projection-v0.1-results.md)
- [Compression-Finality Crosswalk v0.1 Results](results/compression-finality-crosswalk-v0.1-results.md)
- [Projection-Obstruction Discovery Engine v0.1 Results](results/projection-obstruction-discovery-engine-v0.1-results.md)
- [Typed Transport Network v0.1 Results](results/transport-network-v0.1-results.md)
- [CSP Satisfiability Reframing v0.1 Results](results/csp-satisfiability-reframing-v0.1-results.md)
- [Holarchy Lab v0.1 Results](results/holarchy-lab-v0.1-results.md)
- [Typed Transport Category v0.1 Results](results/typed-transport-category-v0.1-results.md)
- [Local Persistence and Reconciliation Split v0.1 Results](results/local-persistence-reconciliation-split-v0.1-results.md)
- [Local Persistence Mechanisms v0.1 Results](results/local-persistence-mechanisms-v0.1-results.md)
- [Local Mechanism Identifiability v0.1 Results](results/local-mechanism-identifiability-v0.1-results.md)

## How To Add A Test

Create a file under `tests/` with:

```md
# T#: Test Name

## Target Claims

## Setup

## Success Criteria

## Failure Criteria

## Known Physics Constraints

## Contribution Needed
```
