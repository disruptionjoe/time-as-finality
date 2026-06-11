# N6: Compositional Finality Known Neighbors

Status: primary sources checked 2026-06-11.

## CRDT Join-Semilattices

State-based conflict-free replicated data types use a join-semilattice state
space, inflationary updates, and least-upper-bound merge to obtain convergence
despite duplicated and reordered delivery.

- Marc Shapiro, Nuno Preguica, Carlos Baquero, and Marek Zawirski,
  "A Comprehensive Study of Convergent and Commutative Replicated Data Types,"
  INRIA Research Report 7506 (2011).
  [HAL](https://inria.hal.science/inria-00555588).

**Relation to T11:** compatible evidence-token states use this algebraic
shape. The experiment's main negative result is that the D1 profile is a
summary of that state, not the join-semilattice itself.

## Coarse-Graining And Renormalization

Kadanoff's block-spin construction and Wilson's renormalization group formalize
the passage from microscopic variables to effective larger-scale
descriptions. Israeli and Goldenfeld construct coarse-grained cellular
automata whose large-scale dynamics can be simpler than the microscopic rule.

- Leo P. Kadanoff, "Scaling Laws for Ising Models Near Tc," *Physics* 2,
  263-272 (1966). [DOI](https://doi.org/10.1103/PhysicsPhysiqueFizika.2.263).
- Kenneth G. Wilson, "Renormalization Group and Critical Phenomena. II,"
  *Physical Review B* 4, 3184-3205 (1971).
  [DOI](https://doi.org/10.1103/PhysRevB.4.3184).
- Navot Israeli and Nigel Goldenfeld, "Coarse-Graining of Cellular Automata,
  Emergence, and the Predictability of Complex Systems," *Physical Review E*
  73, 026203 (2006). [arXiv](https://arxiv.org/abs/nlin/0508033).

**Constraint on T11:** its checkpoints are explicit information maps, not
renormalization-group flows. No fixed point or universality class is derived.

## Local-To-Global Consistency

Abramsky and Brandenburger use sheaf-theoretic global sections to characterize
whether compatible local measurement data admit one global assignment.

- Samson Abramsky and Adam Brandenburger, "The Sheaf-Theoretic Structure of
  Non-Locality and Contextuality," *New Journal of Physics* 13, 113036
  (2011). [arXiv](https://arxiv.org/abs/1102.0264).

**Relation to T11:** the assignment witness is only the smallest gluing
obstruction. It motivates restriction-map work but does not import quantum
contextuality or claim a cohomological result.

## Epigenetic Inheritance And Context

Experiments show that inherited chromatin states can maintain expression
states, that propagation depends on genomic context, and that the
transcriptional effect of programmed chromatin modifications is
context-dependent.

- Robert T. Coleman and Gary Struhl, "Causal Role for Inheritance of H3K27me3
  in Maintaining the OFF State of a Drosophila HOX Gene," *Science* 356,
  eaai8236 (2017). [DOI](https://doi.org/10.1126/science.aai8236).
- Xiaoyi Wang and Danesh Moazed, "DNA Sequence-Dependent Epigenetic
  Inheritance of Gene Silencing and Histone H3K9 Methylation," *Science* 356,
  88-91 (2017). [DOI](https://doi.org/10.1126/science.aaj2114).
- Cristina Policarpi et al., "Systematic Epigenome Editing Captures the
  Context-Dependent Instructive Function of Chromatin Modifications,"
  *Nature Genetics* 56, 1168-1180 (2024).
  [DOI](https://doi.org/10.1038/s41588-024-01706-w).

Kauffman's random genetic-network work supplies a distinct attractor-based
formalization of epigenesis and differentiated stable modes:

- Stuart A. Kauffman, "Metabolic Stability and Epigenesis in Randomly
  Constructed Genetic Nets," *Journal of Theoretical Biology* 22, 437-467
  (1969). [DOI](https://doi.org/10.1016/0022-5193(69)90015-0).

**Constraint on T11:** inherited expression marks share a formal pattern with
epigenetic regulation. They are not a biological model and do not establish
transgenerational inheritance in any physical or social system.

## Positioning Verdict

The individual mathematical ingredients are established. T11's contribution
is the controlled separation:

> evidence-state join, inherited expression, observer access, finality
> profile, and decision are different compositional stages, and algebraic
> structure at one stage need not survive the next.
