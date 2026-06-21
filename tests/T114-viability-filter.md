# T114: Viability Filter

## Route

Mathematical machinery / North-Star formalization.

## Question

Can the synthesis

```text
geometry supplies possible structures;
maintenance, finality, and emergence select viable experienced structures
```

be stated as a finite, falsifiable filter rather than as metaphor?

## Setup

Define a finite set of candidate structures. Each candidate is evaluated
through gates:

1. geometry: finite constraints are mutually satisfiable;
2. dynamics: the candidate is reachable under a declared transition rule;
3. maintenance: repair, entropy export, and stability-window constraints pass;
4. finality: accessible records and reconstruction-debt budget pass;
5. emergence-platform: the finalized structure supports enough downstream
   operation rights to generate further structure.

## Success Criteria

- Geometry-admissible candidates can still fail viability.
- Maintained candidates can still fail observer-experienced status if record
  finality fails.
- Finalized structures need not be emergence platforms.
- A matched standard-state pair can differ only by record access and split the
  observer-experienced verdict.
- Negative controls prevent every possible or disappearing structure from
  being counted as meaningful.

## Failure Criteria

- The filter upgrades a core physics claim.
- Geometry language appears without a finite object.
- Every positive verdict is determined by standard maintenance variables alone.
- Emergence-platform status is assigned after seeing the desired conclusion.
- The model lacks negative controls.

## Claim Impact

T114 is a North-Star artifact only. It does not upgrade D1, H7, S1, or Q1. It
creates a testable interface for deciding whether the viability-filter
intuition has independent content or collapses to standard stability,
thermodynamics, information theory, or coarse-graining.

## Reproduction

```bash
python -m unittest tests.test_viability_filter -v
python -m models.run_t114
```
