# N5: Proof-Carrying Metastable Finality Known Neighbors

Status: primary sources checked 2026-06-11.

## Snow Consensus

The Snow family introduces leaderless probabilistic consensus through repeated
random subsampling and a deliberately metastable preference process.

- Team Rocket, Maofan Yin, Kevin Sekniqi, Robbert van Renesse, and Emin Gun
  Sirer, "Scalable and Probabilistic Leaderless BFT Consensus through
  Metastability," 2020. [arXiv](https://arxiv.org/abs/1906.08936).
- Ignacio Amores-Sesar, Christian Cachin, and Enrico Tedeschi, "When Is Spring
  Coming? A Security Analysis of Avalanche Consensus," OPODIS 2022.
  [arXiv](https://arxiv.org/abs/2210.03423).

**Constraint on T10:** Snow protocols are engineered agreement mechanisms
with explicit sampling, timing, fault, and quorum assumptions. Their
metastability is not automatically a model of physical record formation.

## Zero Knowledge

Goldwasser, Micali, and Rackoff introduced proof systems in which a verifier
can become convinced of a statement without gaining additional witness
knowledge beyond what the statement implies.

- Shafi Goldwasser, Silvio Micali, and Charles Rackoff, "The Knowledge
  Complexity of Interactive Proof Systems," *SIAM Journal on Computing*
  18(1), 1989. [DOI](https://doi.org/10.1137/0218012).

**Constraint on T10:** the implemented verifier is an ideal functionality. It
does not establish simulation-based zero knowledge, computational soundness,
or any concrete security level.

## Proof-Carrying Data

Proof-carrying data composes proofs across distributed computations so later
messages can attest to the validity of their histories.

- Alessandro Chiesa and Eran Tromer, "Proof-Carrying Data and Hearsay
  Arguments from Signature Cards," 2010.
  [Author PDF](https://ic-people.epfl.ch/~achiesa/docs/CT10.pdf).
- Nir Bitansky, Ran Canetti, Alessandro Chiesa, and Eran Tromer, "Recursive
  Composition and Bootstrapping for SNARKs and Proof-Carrying Data," 2012.
  [IACR ePrint](https://eprint.iacr.org/2012/095).

**Relation to T10:** recursively merged certificates and unique-source support
are abstract PCD-like behavior. The implementation demonstrates the needed
relation structure, not a novel PCD construction.

## Coarse-Graining

Israeli and Goldenfeld show that cellular automata with complicated
microscopic behavior can admit simpler, predictive coarse descriptions.

- Navot Israeli and Nigel Goldenfeld, "Coarse-Graining of Cellular Automata,
  Emergence, and the Predictability of Complex Systems," *Physical Review E*
  73, 026203 (2006). [arXiv](https://arxiv.org/abs/nlin/0508033).

**Constraint on T10:** its two-level majority map is selected by the modeler.
The experiment measures its compression and perturbation robustness but does
not derive an optimal or physically natural macrovariable.

## Physical Metastability

Metastability in stochastic physical systems concerns long-lived regions and
rare transitions in state-space dynamics.

- Claudio Landim, "Metastable Markov Chains," *Probability Surveys* 16,
  143-227 (2019). [arXiv](https://arxiv.org/abs/1807.04144).

**Constraint on T10:** protocol confidence counters are not free-energy
barriers, transition rates, or thermodynamic metastability. The comparison is
structural and must remain labeled.

## Positioning Verdict

No individual mechanism is novel. T10's contribution is the controlled
composition and the negative separation result:

> proof verification filters inadmissible claims, coarse-graining hides
> irrelevant distinctions, and metastable sampling produces agreement, but
> none of those operations guarantees that accepted agreement tracks the
> global hidden state.
