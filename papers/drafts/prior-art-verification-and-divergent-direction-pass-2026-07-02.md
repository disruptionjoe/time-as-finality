---
title: "Scope theorem — prior-art verification + divergent persona direction pass"
status: draft-review
doc_type: prior-art-and-direction
updated_at: "2026-07-02"
pairs_with:
  - open-problems/finite-closed-capability-boundary-scope-theorem.md
  - literature/Adversarial Referee Report on the Finite-Closed Capability-Boundary Scope Theorem deep-research-report.md
---

# Prior-art verification + divergent direction pass — scope theorem

Method, not evidence. Web citations verified by direct arXiv fetch (2026-07-02).
Persona pass is one process wearing ten masks — it generates targets and a vote,
never evidence. No claim movement.

## Part 1 — Prior-art verification (all sources fetched and confirmed)

| Component | Source (verified) | Confirmed statement | Verdict |
| --- | --- | --- | --- |
| **E1** sharpness needs a limit | Kadanoff 2010, arXiv:1002.2985 | "a sharp phase transition **only occurs in the presence of some sort of infinity**"; finite bodies show rounded transitions. | **KNOWN — named "extended singularity theorem."** Top novelty threat, confirmed. |
| **E1** finite-N has a weaker real version | Butterfield 2011, arXiv:1106.0702 | novel behavior deduced at N→∞, but "a weaker, yet still vivid ... behaviour ... occurs before ... the limit ... And it is this weaker behaviour which is physically real." | **KNOWN.** |
| **E1/E3** finite systems only approximate SSB | Landsman 2013, arXiv:1305.4473 | "no finite system should display" SSB; large finite systems break via exponential sensitivity. | **KNOWN.** |
| **E3** symmetry/conservation no-go | Kuramochi–Tajima 2023, arXiv:2208.13494 | additive conservation ⇒ exactly implementable projective measurements commute with the conserved observable; exact position measurement under momentum conservation impossible. | **KNOWN & current.** Confirms E3 is real. |
| **E3** formal home | Marvian–Spekkens; Ahmadi–Jennings–Rudolph 2012, arXiv:1212.3378 | WAY formulated as the **resource theory of asymmetry** (symmetric ops; asymmetric resource needed for exact asymmetric measurement). | **KNOWN — E3 is an existing resource theory.** |
| **Part 1** access decomposition | Koashi–Imoto 2001, quant-ph/0101144 | dof split into classical (read-only), nonclassical (inaccessible), and none. | **KNOWN.** |
| **Part 1** no-hiding vs masking | Braunstein–Pati 2006, gr-qc/0603046; Zhu 2020, arXiv:2010.07843 | no-hiding (info not fully in correlations) as special case; but **real quantum states CAN be masked in correlations**. | **KNOWN** (and the counterexample that broke the naive lemma). |
| **framing** capabilities = possible/impossible tasks | Deutsch–Marletto **constructor theory** (2012–) | physics stated "**exclusively in terms of which transformations/tasks are possible vs impossible, and why**"; derives locally-inaccessible entangled information. | **KNOWN — the entire capability-boundary framing is constructor theory.** |
| **E2** hardness is family-indexed | Goldwasser–Micali 1984; Yao 1982 | computational indistinguishability is inherently ensemble/parameter-indexed. | **KNOWN.** |

**Novelty verdict (evidence-based): LOW.** Every mode (E1 Kadanoff; E2 crypto; E3
resource theory of asymmetry) **and** the overall framing (constructor theory) has
an established home; Part 1 is Koashi–Imoto/no-hiding/masking. The only thing not
found verbatim is the specific **assembly** — a four-mode declared-vs-physical
taxonomy *for capability/finality boundaries*, with the crypto crosswalk and the
tri-repo (E3=GU) alignment. That is a synthesis/perspective, not a research result.
**As a novel-theorem paper the scope theorem is dead; the value is (a) internal
(an organizing map) and (b) possibly one narrow under-covered angle.**

## Part 2 — Ten divergent personas: what are we missing + vote

Each: the miss they see, then a vote (option + intensity 1–5) on next direction.

Direction options:
- **D1** — write the honest synthesis/perspective paper (foundations venue).
- **D2** — isolate + test the one under-covered angle: **computational finality / a
  computational arrow of time** (E2 applied to time's arrow), as a candidate novel
  result.
- **D3** — pivot to the **GU adapter theorem** (E3 = Krein/ghost grading ↔
  operational admissibility) — a concrete cross-repo result.
- **D4** — keep the taxonomy as an **internal map only**; no paper; redirect effort
  to the North Star question the map opened.
- **D5** — **formalize** the taxonomy categorically / resource-theoretically.

| # | Persona | The miss it sees | Vote |
| --- | --- | --- | --- |
| 50 | Scientific Skeptic | Nothing novel survives; four known programs in a trench coat. Stop polishing a non-result. | **D4** (5) |
| 25 | Philosopher of Physics | This *is* the Batterman/Butterfield "is the infinite limit physically real" debate; "declared vs physical" = "idealization vs real." | D1 (3), leans D4 |
| 51 | Research Program Architect | Opportunity cost: a synthesis paper is low ROI; only a cross-repo adapter is a real new result. | **D3** (4) |
| 24 | Constructor Theorist | The framing is *ours* (Deutsch–Marletto). But a **constructor-theoretic taxonomy of WHY tasks are impossible** (E1/E2/E3 as impossibility-modes) is an open question in CT and could be genuinely new. | **D2/D5** (4) |
| 8 | Quantum Information | E3 = resource theory of asymmetry (no novelty). The **E2 computational angle is under-explored in QI** — recovery hardness as a boundary. | **D2** (3) |
| 2 | Category Theorist | The map isn't a structure. But resource theories already supply structure; a genuine classifying object is risky-but-possibly-novel. | D5 (2), leans D4 |
| 23 | Resource Theorist | E1/E2/E3 are *three different* resource theories (RG, computational, asymmetry). Unifying them as one "capability-boundary-crossing" resource theory could contribute — high absorption risk. | D5 (3) |
| 49 | Geometric Unity Specialist | The real prize is the **E3 = GU adapter**; the taxonomy is a sideshow. | **D3** (5) |
| 14 | Complexity Theorist | The **least-covered, most-plausibly-novel** angle is a **computational arrow of time** (crypto → finality). Isolate it. | **D2** (4) |
| 53 | North Star Visionary | The taxonomy is a detour. The payoff is the *question* it opened: **is the arrow of time E1 (thermodynamic), E2 (computational), or E3 (symmetry)?** Chase that. | **D4** (5) |

### Tally (sum of intensities)

- **D2 (computational finality / arrow of time): ~11** (24, 8, 14) — strongest single result-directed vote.
- **D4 (internal map + North Star question): ~12** (50, 53, +2/25 leans) — strongest overall.
- **D3 (GU adapter): 9** (51, 49).
- **D5 (formalize): ~7** (24 shared, 23, 2).
- **D1 (write the synthesis paper as-is): 3** (25) — **lowest**, matching the LOW novelty verdict.

### Synthesis

Two things the panel agrees on: **(i)** writing the broad taxonomy as a novel
paper (D1) is not worth it — the verification confirms it is Kadanoff + constructor
theory + resource-theory-of-asymmetry + crypto, repackaged; and **(ii)** the
taxonomy's real value is the **internal organizing map** (D4), which stands
regardless of external novelty. Where external novelty might still exist, the panel
points at two narrow, concrete targets, not the broad paper: the **computational
arrow of time** (D2 — crypto applied to finality/time, genuinely under-trodden) and
the **GU adapter** (D3 — a specific cross-repo theorem). D1 is effectively rejected.

## Recommended next direction

1. **Adopt D4 as the baseline:** keep the four-mode taxonomy as the program's
   internal map (it already earns its keep — it explains the kill history and aligns
   the tri-repo). Do **not** invest in the broad synthesis paper as a novelty claim.
2. **Take D2 as the next swing:** isolate whether "**computational finality / a
   computational arrow of time**" (records that are one-way-hard to recover, so the
   arrow is computational not thermodynamic) is a genuine, checkable, novel result —
   the one angle the prior-art sweep did **not** find a home for. It is cheap,
   self-contained (builds on T417), and the most likely to be actually new.
3. **Hold D3 (GU adapter) as the cross-repo prize** for after D2, or in parallel:
   attempt the Krein-grading ↔ operational-admissibility adapter translation the GU
   note already scoped.

Path A/B (classical theorem / taxonomy paper) is downgraded: at most a short,
honestly-positioned *perspective* note that cites Kadanoff, constructor theory, and
the resource theory of asymmetry up front — only if Joe wants a public artifact.
The research energy goes to D2, then D3.
