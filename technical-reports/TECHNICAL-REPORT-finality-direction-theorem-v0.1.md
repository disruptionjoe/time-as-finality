# Finality Direction Theorem

## Abstract

T18 derives a narrow finality arrow from impossible transformations. In a
finite constructor-style model where admissible transformations are monotone
in D1 finality, strict finalization induces an acyclic partial order. The
reverse of every strict finalization edge is impossible under the same rule.

This is not a derivation of the thermodynamic arrow, coordinate time, proper
time, or phenomenal flow. It is a conditional theorem check: if finality is
cashed out as D1-monotone admissibility, then temporal direction is a theorem
of the admissible-transformation structure.

## Model

Each state carries a D1 vector:

```text
(accessible support, holder redundancy, branch support, reversal cost)
```

A transformation is admissible when:

```text
after >= before componentwise
```

Strict finalization is admissible and has at least one strict D1 increase.
Strict definalization is not admissible because it decreases finalized record
structure.

The model also tracks a thermodynamic-cost proxy, but that proxy is not used
to classify transformations.

## Theorem Statement

In a finite constructor model where admissible transformations are
D1-monotone, strict finalization induces an acyclic partial order; the reverse
of every strict finalization is impossible.

## Exhaustive Verification

T18 checks:

```text
states = 402
transformations = 161202
strict finalization edges = 38205
impossible transformations = 122193
```

All theorem checks pass:

| Check | Result |
| --- | --- |
| strict finalization graph is acyclic | pass |
| every strict finalization has impossible reverse | pass |
| impossible transformations are not closed under reversal | pass |
| finality arrow is partial, not total | pass |

## Witnesses

Impossible reversal witness:

```text
s1-h0-b0-r1-k0 -> s0-h0-b0-r0-k0
```

This decreases finalized record structure and is therefore impossible.

Thermodynamic-divergence witness:

```text
s1-h0-b0-r1-k0 -> s1-h0-b0-r2-k0
```

D1 reversal cost increases, but the thermodynamic-cost proxy remains `0`.
This does not prove thermodynamics is irrelevant in physical systems. It
shows that this formal finality direction is not defined by the thermal proxy.

Incomparable-pair witness:

```text
s1-h0-b0-r2-k0
s1-h0-b1-r1-k0
```

Each gives up a different D1 dimension, so the finality arrow is a partial
order rather than a hidden universal total order.

## Interpretation

The theorem gives TaF a precise but narrow arrow:

```text
less finalized record state -> more finalized record state
```

The arrow is not assumed as primitive time. It follows from the asymmetry
between finalization and definalization under the constructor rule.

The most important guardrail is that this result is conditional. The next
scientific question is whether a physically grounded model justifies
D1-monotone admissibility, and when that condition agrees with or diverges
from ordinary thermodynamic irreversibility.

## Claim Impact

T18 upgrades [H7](claims/H7-finality-induced-direction.md) from an open formal
target to partial support in a finite constructor-style model.

It also gives
[Arrow of Time as Constructor Theorem](open-problems/arrow-of-time-as-constructor-theorem.md)
its first executable theorem check.

## Reproduction

```bash
python -m unittest tests.test_finality_direction_theorem -v
python -m unittest discover -s tests -p "test_*.py" -v
python -m models.run_t18
```

Machine-readable output:

- [results/finality-direction-theorem-v0.1.json](results/finality-direction-theorem-v0.1.json)

Human-readable result note:

- [results/finality-direction-theorem-v0.1-results.md](results/finality-direction-theorem-v0.1-results.md)
