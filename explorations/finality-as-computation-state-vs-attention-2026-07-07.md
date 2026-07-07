# Finality as Computation: the state/attention split as the classical/quantum split

Exploration-grade intake + hypothesis, 2026-07-07 (Joe, chat). Speculative / analogy grade. No claim
movement. Manufactured-convergence risk is high (physics and ML architecture both freshly in view);
the guards and the one falsifiable prediction are load-bearing, the picture is not.

## Stimulus

arXiv:2406.07887 (Waleffe et al., NVIDIA), *An Empirical Study of Mamba-based Language Models* — an
EMPIRICAL comparison of state-space models (Mamba/Mamba-2) vs transformers at 8B scale. Its load-bearing
fact for us: pure state-space models match or beat transformers on most tasks but FAIL on copying /
in-context retrieval / long-range lookup, and the winning architecture is a HYBRID that keeps state and
attention as SEPARATE, interleaved layer types (~43% state, ~7% attention, ~50% MLP), not blended into
one primitive. Two computational modes, irreducible to one, kept separate.

## The mapping (shape-level, not mechanism)

| computational mode | physics mode | GU locus | TaF reading |
|---|---|---|---|
| attention (all-to-all, weighted sum over all positions; no privileged running state) | quantum / path integral (sum over all histories; superposition) | Y14 = "where quantum work happens" (Weinstein, transcript [00:04:08]) | the un-finalized process; all branches live |
| state-space (one running state, sequentially committed, carried forward) | classical (single stationary-phase trajectory; committed history) | X4 = "where classical work happens" | finality — a record become hard to undo |
| state<-attention handoff (commit the summary, drop the all-to-all) | decoherence / measurement / stationary phase | the X4/Y14 projection (pullback) | THE finality event: superposed all-paths collapses to one carried-forward record |

The path integral literally IS attention: a weighted sum over all paths (amplitudes) = a weighted sum
over all positions (attention scores). A classical trajectory IS the state-space recurrence: one
committed path carried forward. The quantum->classical transition IS the attention->state handoff.

## Why this bears on "why QM and the SM are separate"

GU's own framing (transcript we read): the GR-vs-SM divide is "an unacknowledged battle between Ehresmann
and Riemann" [00:14:43] — metric geometry (Riemannian, classical, state) vs gauge/bundle geometry
(Ehresmannian, quantum, attention) — two irreducibly different geometries where the unifying move
(Einstein's contraction) is DISALLOWED in the gauge world. That is the geometric version of the Mamba
result: you cannot collapse state and attention into one primitive; the best architecture interleaves
them. So GU's insistence that these are two separate geometries is, on this reading, the same structural
fact as "state and attention are irreducibly separate computational modes."

On the precise phrasing "QM vs SM separate," the clean version is **mechanism vs finalized content**:
attention/quantum is the mechanism (all paths, the process); the SM's specific gauge content is what gets
FINALIZED — the structure stable under collapse of the process. This ties to GU's `located, not forced`:
the SM content is *located* as what survives finalization, not *forced* by the mechanism. The separateness
is then a prediction (two irreducible modes + a selection), not an embarrassment.

## Differential test (Joe's challenge, 2026-07-07): does it beat metaphor?

Pushed to check whether this lines up with MEASURABLE quantum-vs-classical differences in ways other
explanations do not, the honest result is a downgrade AND a sharpening:

- **The naive mapping FAILS a polarity test.** "Attention = quantum superposition" implies quantum =
  good-at-copying, because Transformers are good at copying/retrieval and SSMs are bad at it. But the
  copyable states in physics are the CLASSICAL (measured/decohered) ones; unknown quantum states cannot be
  cloned. The mapping points the wrong way — because "attention" conflates two properties: an all-paths
  PROCESS (superposition-like) and RETRIEVAL of stored items (memory-like). Only the second is load-bearing.
- **The surviving mapping is the information-RETENTION axis, and it is measurable.** Transformer = retain
  the full history explicitly (KV cache O(n)), reversible-in-principle, information-conserving. SSM =
  compress the past irreversibly into a bounded O(1) state, provably losing arbitrary-retrieval. That axis
  lines up with a real measurable distinction: unitary evolution conserves information (interference
  visibility, coherence times, the black-hole information paradox) vs decoherence/thermodynamic evolution
  that loses it (entropy production, Landauer kT ln2 erasure). Same quantitative tradeoff: the cost of the
  full reversible description grows with system size on both sides (KV cache with sequence length <-> quantum
  coherence with system size). The SSM<-Transformer compression IS structurally decoherence = finality.
- **But as an EXPLANATION it is not novel — it is isomorphic to one physics already has.** Zurek
  decoherence/einselection + quantum Darwinism (classicality = information loss to environment + redundancy)
  and Landauer (irreversibility = thermodynamic cost) already give this. The SSM/Transformer framing
  restates it in architecture vocabulary; it does not out-explain the decoherence account. Claiming
  otherwise would be overselling. (from memory: Zurek; Landauer.)
- **Where it could be MORE than metaphor — the real payload.** The SSM-vs-Transformer literature has
  something the physics side states only loosely: HARD, PROVABLE complexity-separation theorems about
  exactly what a bounded-state model CANNOT compute that full-attention can (copying / state-tracking lower
  bounds; Merrill et al., from memory). Physics says "classical coarse-graining loses information" vaguely;
  the SSM lower bounds name PRECISELY which class of retrievals a bounded memory provably cannot perform —
  which is exactly the shape of the C(R) open problem (what a bounded classical record can/cannot
  re-collect). The non-trivial move is therefore NOT "physics is a Transformer" but **importing the SSM
  lower-bound theorems as candidate sharp statements of the finality/capability boundary.**

## The one falsifiable prediction (the cure for manufactured convergence)

The composite must predict something neither half does. Candidate: **the classical<-quantum transition
carries the computational signature of an attention->state handoff — an information/retrieval bottleneck
at finalization.** State-space models provably lose exactly the copying/retrieval capability that
attention supplies; if decoherence is that same handoff, the "records" that survive finalization should
be subject to an analogous retrieval bound (what a bounded classical record can and cannot re-collect
from the pre-collapse process). That is a capability statement (C(R)-typed), not a picture, and it is
where T392/T395 machinery could bite.

## Executable check: T495

T495 converts the surviving part of the analogy into a finite C(R)-style
capability screen: full-history visibility factors arbitrary indexed retrieval
over a five-bit stream, while last-2 and parity committed states have
non-singleton arbitrary-retrieval spreads. The same bounded states pass their
native retained-suffix or parity positive controls.

Verdict: `BOUNDED_RETRIEVAL_BOTTLENECK_BUILT_RETENTION_AXIS_ONLY`. This supports
only the retention-axis review target. It does not revive the naive
attention/quantum copyability mapping, does not prove a physics mechanism, and
does not import SSM/Transformer lower-bound theorem language without a separate
source-checked packet.

## Honest grades and guards

- **Analogy grade**, shape-level. Coupling-flow is not record-flow; projection is not finality; TaF has
  no action. Borrow the *shape* (two irreducible modes + a finalization transition), never the mechanism.
- **The stimulus paper is EMPIRICAL** — it shows the hybrid wins, it does NOT prove the modes are
  irreducibly separate. For a rigorous "why separate," the load-bearing literature is the expressivity
  results, cited from memory (verify before any use): Merrill, Petty & Sabharwal, *The Illusion of State
  in State-Space Models* (arXiv:2404.08819) — diagonal SSMs sit in TC0-ish and cannot do inherent state
  tracking (S5); Merrill & Sabharwal on transformers as (log-uniform) TC0; Deletang et al., *Neural
  Networks and the Chomsky Hierarchy*. These characterize what each mode can/cannot compute — the actual
  content a physics claim would need.
- **Manufactured convergence**: physics and ML architecture are both freshly in view this session;
  resemblance is a warning, not evidence. The falsifiable prediction above is the only thing that would
  make this more than a vivid picture.
- No claim movement in any repo. Cross-links: GU X4/Y14 + Ehresmann/Riemann (the geometry that would
  realize the split) and `located, not forced` (content located, not forced); TI issuance (the process
  side); ai-epistemology E036 (state/attention rhymes with the convergent/divergent automation split —
  a minor, separate hook, not this note's claim).
