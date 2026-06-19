# Persona Clusters

The scoring-time view of the persona system: every persona is assigned a
**primary discipline cluster** so that cross-cluster normalization (operating
model §7–§8) weighs *breadth across distant clusters* rather than raw headcount.

This registry **references**, and does not replace, the canonical persona
sources:

- `personas/EXPERT-PANEL.md` — **canonical** numbered expert personas (1–62)
  that actually score.
- `personas/INDEX.md` — the lens registry (review postures).

> **Canonicalization done (Session 5, H1).** The numbered personas are now
> canonical under `personas/EXPERT-PANEL.md` (was inside the panel skill). The
> skill's `references/personas.md` is a mirror pointer and
> `scripts/build_panel_prompt.py` reads the canonical file. The six new
> Simulation/MMO/Game-Mechanism personas exist as 57–62.

## The seven clusters

1. **math/formalism**
2. **physics/decoherence**
3. **distributed-systems/consensus**
4. **information/networking**
5. **sheaf/category/geometry**
6. **simulation/MMO/game-mechanism**
7. **philosophy/testability/skepticism**

## Numbered-persona → primary cluster (seed)

| cluster | personas (by #) |
|---|---|
| math/formalism | 2 Category Theorist, 5 Algebraic Topologist, 6 Representation Theorist, 10 Formal Methods, 11 PL Theorist, 14 Complexity Theorist, 15 Infinite Models, 23 Resource Theory, 24 Constructor Theory, 26 Phil. of Mathematics, 37 Type-System Designer, 47 Index Theory, 52 Mathematical Minimalist |
| physics/decoherence | 1 Mathematical Physicist, 7 Quantum Foundations, 8 Quantum Information, 25 Philosopher of Physics, 54 Experimentalist |
| distributed-systems/consensus | 9 Distributed Systems, 34 Git Version Control, 35 Database Systems Architect, 36 Access-Control, 55 Hashgraph/Gossip, 56 Avalanche-class Consensus |
| information/networking | 12 Network Propagation, 13 ZK/Cryptography, 22 Information Theorist, 31 AI Learning Theory, 32 Reinforcement Learning, 38 Financial Risk Modeler |
| sheaf/category/geometry | 3 Differential Geometer, 4 Topologist/Sheaf Theorist, 45 Fiber Bundle, 46 Spin Geometry, 48 Gauge Theory, 49 Geometric Unity |
| simulation/MMO/game-mechanism | 16 Dynamical Systems, 17 Symbolic Dynamics, 18 Multiscale Statistics, 21 Complex Systems, **57 Game-Mechanism Designer, 58 MMO Network Architect, 59 Distributed-Simulation Engineer, 60 Virtual-Economy Designer, 61 Interest-Management Specialist, 62 Bandwidth-Bounded-World Architect** |
| philosophy/testability/skepticism | 27 Phil. of Science, 40 Legal Scholar, 41 Linguist, 42 Poet/Literary, 43 Music Theorist, 50 Scientific Skeptic, 51 Research Program Architect, 53 North Star Visionary |

Personas **57–62** are new coverage areas, defined as numbered personas in
`personas/EXPERT-PANEL.md` and mirrored as a lens family in `personas/INDEX.md`.

## Unmapped / cross-cutting (governance decision needed)

The seven clusters do **not** cleanly cover every existing persona. Pending a
governance decision (add a cluster vs accept best-fit):

- 19 Causal Inference, 20 Physics-Informed ML — plausibly information/networking
  or simulation; currently unassigned.
- 28 Evolutionary Biologist, 29 Systems Biologist, 30 Neuroscientist,
  33 Cognitive Scientist, 44 Ecologist — an observer/selection/biology grouping
  the current seven clusters omit.

This gap is recorded as an open question for `govern/persona-governance` and in
`PROJECT-LOG.md`.

## Cross-cluster rules (from the operating model)

- Breadth across *distant* clusters outweighs depth within one.
- A single homogeneous cluster must not dominate by headcount.
- Informed minorities are protected via survival arguments (operating model §5).
