# Time-as-Finality Research Steering Card

## Card Contract

Primary function: Joe does not read this card. When Joe says "I have attention
for this," the agent reads this card, runs `python attention/taf_priority_condorcet.py`,
and returns the top few ranked items in order, each with a one-line why, and
nothing else.

Seed assessment: `attention/initial-council-assessment-2026-07-12.md`.
Branch map: `attention/branch-map-council-2026-07-12.md`.

## attention_priority

Steering note (2026-07-22): the Wave-1 triple-diamond prep steering has landed
(`explorations/2026-07-22-wave1-triple-diamond-prep-steering.md`). It re-frames
the next Track-1 wave toward the TaF-1 finality-native source-law swing
(de-pause TAF9/TAF11; run the reversal-self-dual reflector enumeration, F4
first), armed with TaF-2's anomaly-matching as family F6. The subordinate
Track-2 TaF-3 paper-routing gate is now RESOLVED: the Kuratowski
interior-operator check PASSED, licensing an S4-interior title for the
first-person-finality paper at fixture grade (broad "certify your own present"
headline stays embargoed). Track-2 paper work reports up and is not a council
pick; the Condorcet ranking below is over Track-1 research-advancement items
only and is unchanged by this run (re-run 2026-07-22, deterministic, exit 0:
TAF8 > TAF3 > TAF12 > TAF4 > TAF6 > TAF5 > TAF7).

Generated ranking from `attention/taf_priority_condorcet.py` after T582 on
2026-07-14 (unchanged on the 2026-07-22 re-run):

1. TAF8 - Cross-domain shadow-protection theorem target.
   Why: T582 absorbed W192 as explicit state/resource completion, so TAF8 still
   waits for a real domain-native cross-domain packet.
2. TAF3 - Law-derived C(R) menus and physical noncompletion witness.
   Why: The current C(R) line keeps losing to declared-boundary and completion
   absorbers; derive the operation menu from dynamics.
3. TAF12 - Data-bearing C(R) packet acquisition for TAF10.
   Why: T535 found no real packet in hand; the branch waits for exact
   full-stack profiles plus an independent noncompletion witness.
4. TAF4 - Finite-to-continuum finality colimit bridge.
   Why: Still blocked after T579; the causal-set measure-law probe supplied no
   finality-native continuum bridge.
5. TAF6 - Quantum access-structure and monogamy finality theorem.
   Why: T514-T520 leave a cleaner secret-sharing/access-structure strut than the
   falsified BFT threshold analogy.
6. TAF5 - Adapter de-correlation for GU/TI/TAF boundary functors.
   Why: The current two-adapter signal remains review-only until source
   categories and encodings are de-correlated.
7. TAF7 - Detector provenance raw-log independent-axis packet.
   Why: The manifest is ready, but the lane needs a predeclared independent axis
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
| TAF11 | closed and parked as limited review material | Does the firewalled T559-T581 package survive without promotion by momentum? | T581 closed and parked the review package, named evidence-only reopen conditions, blocked source-law and protected-truth movement, and left no unattended successor on the old TAF11 route. |
| TAF12 | paused branch | Can a real data-bearing packet replace T533/T535 synthetic or absent C(R) targets? | T535 completed. Five existing-source candidates checked; none has exact full-stack profiles plus independent non-task-success noncompletion witness. |
| TAF3 | blocked | Can C(R) menus and noncompletion be derived from a domain-native law rather than declared boundaries? | Still blocked. T534 supplied no source law and T535 supplied no real noncompletion target. |
| TAF4 | blocked on source-law survivor | Can native finite finality objects descend toward causal-set or Lorentzian structure? | T526 calibrates target, T528 native preflight incomplete, T532/T534 found no cleared law, T548 narrowed APRD, and T579's causal-set measure-law probe supplied no continuum or Lorentzian bridge. TAF4 movement still waits for a real bridge, not a target import. |
| TAF5 | open, lower immediate rank | Can GU/TI/TAF adapters de-correlate enough to carry source-category truth? | T504-T506 gates built, real source categories not supplied. |
| TAF6 | open, secondary lane | Can quantum access-structure and monogamy results yield a clean finality theorem? | T514-T520 narrowed away false BFT/copy-law analogies. |
| TAF7 | open, execution-ready only with data | Can detector provenance supply a predeclared independent finality axis? | T521 manifest template built, no data-bearing packet. |
| TAF8 | open, waiting for cross-domain packet | Can shadow protection transfer across domains without identity-by-construction? | T541 completed the review-only nonidentity witness-packet gate. T582 tested frozen W192 separately and absorbed it as explicit state/resource completion, so TAF8 still waits for a real domain-native cross-domain packet under the same spine. |

## next_action

Wave-1 prep landed (2026-07-22). Next Track-1 wave: the TaF-1 finality-native
source-law swing - de-pause TAF9/TAF11 and run the reversal-self-dual reflector
enumeration (F4 first, the knob-free anchor; F2/F3 as funded challengers),
committing the frozen spec before results; arm with TaF-2's anomaly-matching as
family F6. TaF-2 is spec-prep only (no compute yet). The Track-2 TaF-3 paper gate
is resolved (Kuratowski PASS, S4-interior title licensed at fixture grade); hold
the broad-headline embargo. Paper-lane work reports up and is not a council pick.

Do not rerun T580, T581, or T582. TAF11 is parked unless one named T581 reopen
condition arrives with concrete evidence.

Use the T541 TAF8 gate only when a real domain-native cross-domain packet is
available under the same predeclared spine. W192 does not qualify in its current
frozen proxy form because T582 absorbed it as explicit state/resource
completion.

If no TAF8 packet exists, select the highest-ranked executable branch that has
its required input packet. TAF12 may run only if a real data-bearing packet
exists. TAF3 may resume only through a law-derived C(R) menu or physical
noncompletion witness, not by reusing the parked TAF11 package.
