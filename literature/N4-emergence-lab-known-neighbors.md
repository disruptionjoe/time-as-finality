# N4: Emergence Laboratory Known Neighbors

Status: primary sources checked 2026-06-11.

## Elementary Cellular Automata

Wolfram's statistical-mechanics study established elementary cellular
automata as deterministic local-update systems with irreversible,
self-organizing, and dynamically varied behavior.

- Stephen Wolfram, "Statistical Mechanics of Cellular Automata," *Reviews of
  Modern Physics* 55, 601-644 (1983).
  [Author PDF](https://content.wolfram.com/sw-publications/2020/08/statistical-mechanics-cellular-automata.pdf)
  and [DOI](https://doi.org/10.1103/RevModPhys.55.601).

Matthew Cook proved that Rule 110 on an appropriate infinite background is
computationally universal.

- Matthew Cook, "Universality in Elementary Cellular Automata," *Complex
  Systems* 15, 1-40 (2004).
  [Publisher PDF](https://wpmedia.wolfram.com/sites/13/2018/02/15-1-1.pdf)
  and [DOI](https://doi.org/10.25088/ComplexSystems.15.1.1).

**Constraint on this lab:** universality of infinite Rule 110 does not imply
that a width-five periodic instance is computationally irreducible. The lab
does not make that inference.

## Reversible Computation And Cellular Automata

Bennett showed that general computation can be embedded in logically
reversible computation. Toffoli and Fredkin developed reversible and
conservative computational structures, including cellular-automaton
constructions.

- Charles H. Bennett, "Logical Reversibility of Computation," *IBM Journal of
  Research and Development* 17, 525-532 (1973).
  [PDF](https://mathweb.ucsd.edu/~sbuss/CourseWeb/Math268_2013W/Bennett_Reversibiity.pdf)
  and [DOI](https://doi.org/10.1147/rd.176.0525).
- Tommaso Toffoli, "Computation and Construction Universality of Reversible
  Cellular Automata," *Journal of Computer and System Sciences* 15, 213-231
  (1977). [DOI](https://doi.org/10.1016/S0022-0000(77)80007-X).
- Edward Fredkin and Tommaso Toffoli, "Conservative Logic,"
  *International Journal of Theoretical Physics* 21, 219-253 (1982).
  [MIT report](https://publications.csail.mit.edu/lcs/pubs/pdf/MIT-LCS-TM-197.pdf)
  and [DOI](https://doi.org/10.1007/BF01857727).

**Relation to the implementation:** the second-order update used here is a
standard reversible-lift idea. Its value is comparative, not novel.

## Thermodynamics Of Information

Landauer connected logical irreversibility with a minimum heat cost for
erasure. Bennett clarified that computation need not dissipate that cost at
every logical step when it is implemented reversibly.

- Rolf Landauer, "Irreversibility and Heat Generation in the Computing
  Process," *IBM Journal of Research and Development* 5, 183-191 (1961).
  [DOI](https://doi.org/10.1147/rd.53.0183).
- Charles H. Bennett, "Notes on Landauer's Principle, Reversible Computation,
  and Maxwell's Demon," *Studies in History and Philosophy of Modern Physics*
  34, 501-510 (2003).
  [PDF](https://www.cs.princeton.edu/courses/archive/fall06/cos576/papers/bennett03.pdf).

**Constraint on this lab:** `k_B T ln(2) H(X|Y)` is a lower bound under the
stated memory and input model. It is not measured device dissipation.

## Computational Irreducibility And Coarse-Graining

Wolfram argues that some computations cannot be shortcut. Israeli and
Goldenfeld provide an essential counterweight: computationally irreducible
microscopic systems can have predictable, computationally reducible
coarse-grained descriptions.

- Stephen Wolfram, *A New Kind of Science*, "Computational Irreducibility"
  (2002). [Author text](https://www.wolframscience.com/nks/p740--computational-irreducibility/).
- Navot Israeli and Nigel Goldenfeld, "Computational Irreducibility and the
  Predictability of Complex Physical Systems," *Physical Review Letters* 92,
  074105 (2004). [arXiv](https://arxiv.org/abs/nlin/0309047) and
  [DOI](https://doi.org/10.1103/PhysRevLett.92.074105).
- Navot Israeli and Nigel Goldenfeld, "Coarse-Graining of Cellular Automata,
  Emergence, and the Predictability of Complex Systems," *Physical Review E*
  73, 026203 (2006). [arXiv](https://arxiv.org/abs/nlin/0508033).

**Constraint on this lab:** exhaustive preimage search on a finite state space
is a computational benchmark, not proof of computational irreducibility.

## Actual Sensitivity And Causal Structure

Boolean derivatives provide a formal way to ask whether changing one input
bit changes an output bit. The laboratory uses this local counterfactual
sensitivity to build trajectory-specific causal edges.

- O. Martin, A. M. Odlyzko, and S. Wolfram, "Algebraic Properties of Cellular
  Automata," *Communications in Mathematical Physics* 93, 219-258 (1984).
  [DOI](https://doi.org/10.1007/BF01223745).
- Franco Bagnoli, "Boolean Derivatives and Computation of Cellular Automata,"
  *International Journal of Modern Physics C* 3, 307-320 (1992).
  [arXiv version](https://arxiv.org/abs/cond-mat/9912353) and
  [DOI](https://doi.org/10.1142/S0129183192000257).

The resulting edge relation is a causal model of the computation. It should
not be confused with derivation of relativistic spacetime causal structure.

## Positioning Verdict

The laboratory's contribution is not a new CA rule, reversible construction,
or thermodynamic principle. It is a controlled comparison using one intrinsic
record definition across reversible and irreversible local dynamics.

The strongest defensible result is:

> Counterfactual record traces and observer-relative access are independent of
> logical irreversibility, while thermodynamic information loss, inversion
> structure, and trace persistence are substrate-dependent.
