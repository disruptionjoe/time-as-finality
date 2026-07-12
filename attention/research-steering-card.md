# Time-as-Finality Research Steering Card

## Card Contract

Primary function: Joe does not read this card. When Joe says "I have attention
for this," the agent reads this card, runs `python attention/taf_priority_condorcet.py`,
and returns the top few ranked items in order, each with a one-line why, and
nothing else.

Seed assessment: `attention/initial-council-assessment-2026-07-12.md`.

## attention_priority

Generated ranking from `attention/taf_priority_condorcet.py` after Wave 1
T532/T533 on 2026-07-12:

1. TAF9 - New finality-domain law with independent comparability density.
   Why: T532 found no cleared law candidate; the next S1 swing must bring a new
   source law or stop the finite-generator route.
2. TAF10 - Real C(R) surplus packet replacing the T533 synthetic target.
   Why: T533 admits only a synthetic future shape; the next C(R) swing must
   supply a real full-stack-matched noncompletion witness.
3. TAF3 - Law-derived C(R) menus and physical noncompletion witness.
   Why: the C(R) line keeps losing to declared-boundary and completion
   absorbers; derive the operation menu from dynamics.
4. TAF8 - Cross-domain shadow-protection theorem target.
   Why: the kappa and typed-gap catalogues suggest reusable structure, but
   identity and independent-motivation burdens are still open.
5. TAF4 - Finite-to-continuum finality colimit bridge.
   Why: if a native finite law survives, test whether its objects descend toward
   causal-set or Lorentzian structure without coordinate import.
6. TAF6 - Quantum access-structure and monogamy finality theorem.
   Why: T514-T520 leave a cleaner secret-sharing/access-structure strut than the
   falsified BFT threshold analogy.
7. TAF5 - Adapter de-correlation for GU/TI/TAF boundary functors.
   Why: the current two-adapter signal remains review-only until source
   categories and encodings are de-correlated.
8. TAF7 - Detector provenance raw-log independent-axis packet.
   Why: the manifest is ready, but the lane needs a predeclared independent axis
   and data-bearing packet before it can move Q1.

## council

Standing rule: the council proposes RESEARCH ADVANCEMENT of this repo only. It
does NOT propose external review, submission prep, methodology papers, or
"shipping" items. Joe is aware of those; they are not the advancement of the
research.

Personas are always run inline in a single worker, never one-agent-per-persona,
at any count.

Standing roster:

- Orthodox professor: asks whether the result reduces to known resource,
  causal, quantum, computational, or provenance machinery.
- Heterodox-rigorous professor: identifies the unforced choices the structure
  secretly rests on.
- Commercial scientist: prioritizes cheap decisive tests over more narrowing.
- Philosopher of science: names what can kill the line and where the repo is
  protecting instead of exposing.
- Wild mathematically-serious frontier scientist: searches for the highest-upside
  untouched object that could unify the live fragments.
- Causal-set and Lorentzian geometry lens: pressures S1, manifoldlikeness,
  causal order, covariance, and finite-to-continuum descent.
- Quantum information and decoherence lens: keeps records, access structures,
  shareability, entanglement, and measurement guardrails typed.
- Distributed systems and consensus lens: treats finality, settlement,
  authority, and consistency analogies as absorbers unless an invariant survives.
- Resource theory and thermodynamics lens: asks whether C(R) is more than a
  resource preorder, monotone vector, or task-success profile.
- Category, sheaf, and obstruction lens: checks object identity, functoriality,
  cohomology, typed gaps, and bridge discipline.
- Complexity and cryptography lens: separates static hardness boundaries from
  temporal arrows and blocks public-cycle relabels.
- Detector metrology and provenance lens: demands predeclared raw-log fields,
  independent axes, controls, and source provenance before Q1-style movement.

## ranking_engine

Script: `attention/taf_priority_condorcet.py`.

Contract:

- `ITEMS` is the live hypothesis or next-move dictionary.
- `BALLOTS` is the persona dictionary of strict preference orders, best first.
- Item X outranks item Y if a majority of personas prefer X to Y.
- On a Condorcet cycle, the script falls back to Copeland score, pairwise wins
  minus pairwise losses.
- Remaining ties break by average ballot position, then item id.
- Re-ranking means editing `ITEMS` and `BALLOTS`, then running the script.
- The script is deterministic and exits 0 when ballots are well formed.

## execution_strategy

Wave method:

- A wave is a dependency-bounded batch of hypotheses attacked together.
- Stop a wave and start a new one exactly when the next batch depends on the
  current wave's result.
- Independent probes fan out in parallel. Only genuinely dependent probes
  serialize.
- Each swing produces one durable artifact: a deterministic test or computation
  that exits 0 plus a short writeup.
- Every writeup labels every claim COMPUTED or ARGUED with a confidence level.
- Commit and push the artifact.

Generative re-ranking loop:

1. After each wave or parallel batch, the inline council reflects on what the
   wave taught: what is missing, what became more important, and what was
   narrowed or falsified.
2. The council drafts new hypotheses before voting. Do not merely nudge the old
   list.
3. The council votes strict ballots over the refreshed candidate set.
4. Run `python attention/taf_priority_condorcet.py`.
5. Update this card's `attention_priority`, `open_threads / swing_status`, and
   `next_action`.

Discipline:

- Honesty above all. NARROWED and FALSIFIED are SUCCESSES, not failures - the
  whole value is that the loop catches its own wrong guesses. Never manufacture
  a result; never p-hack a computation toward a wanted answer; if you are
  choosing a value because it matches a target, stop and say so.
- Research advancement of THIS repo only (no shipping/external/methodology-paper
  items as council picks).
- One durable, reproducible artifact per swing, committed and pushed.
- Personas always inline, never per-agent.
- No em-dashes in prose.

## open_threads / swing_status

| id | status | live question | current state |
| --- | --- | --- | --- |
| TAF9 | open, top priority | Can a new finality-domain law supply independent comparability density after T532 found no cleared candidate? | T532 completed. Two-channel receipt-product stays independently natural but negative; three-channel receipt-product has expected density 1/4; target import, screen conditioning, and band fitting reject. |
| TAF10 | open | Can a real C(R) packet replace T533's synthetic future target with exact full-stack profile matches plus an independent non-task-success noncompletion witness? | T533 completed. Only the synthetic future target admits as review-only; no current C(R) success. |
| TAF3 | open, blocked on TAF9 or TAF10 | Can C(R) menus and noncompletion be derived from a domain-native law rather than declared boundaries? | Started as a dependency lane in Wave 1; no law-derived menu claim is allowed yet. |
| TAF4 | open, depends on TAF9 survivor | Can native finite finality objects descend toward causal-set or Lorentzian structure? | T526 calibrates target, T528 native preflight incomplete, T532 found no cleared law. |
| TAF5 | open, lower immediate rank | Can GU/TI/TAF adapters de-correlate enough to carry source-category truth? | T504-T506 gates built, real source categories not supplied. |
| TAF6 | open, secondary lane | Can quantum access-structure and monogamy results yield a clean finality theorem? | T514-T520 narrowed away false BFT/copy-law analogies. |
| TAF7 | open, execution-ready only with data | Can detector provenance supply a predeclared independent finality axis? | T521 manifest template built, no data-bearing packet. |
| TAF8 | open, theorem target | Can shadow protection transfer across domains without identity-by-construction? | T492/T499/T501 show schema value but object identity remains blocked. |

## next_action

When Joe opens the lane, route the next swing to TAF9:

Predeclare a new finality-domain law with an independent reason for its
comparability density. It must not be the already-negative two-channel receipt
product, the density-mismatched three-channel product, a Lorentzian u/v import,
T528/T530 screen conditioning, or a post-hoc repaired-band fit. The swing should
produce one deterministic test plus one writeup labeling COMPUTED vs ARGUED
claims with confidence.

If no credible new law can be predeclared, the correct move is a demotion or
pause packet for the S1 finite-generator route, not another gate. TAF10 can run
in parallel if a real domain packet exists, but TAF3 remains blocked until TAF9
or TAF10 supplies a law or noncompletion target.
