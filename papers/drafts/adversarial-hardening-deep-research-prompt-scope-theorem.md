---
title: "Adversarial hardening + prior-art deep-research prompt — scope theorem"
status: draft-tool
doc_type: review-prompt
updated_at: "2026-07-02"
pairs_with:
  - open-problems/finite-closed-capability-boundary-scope-theorem.md
  - technical-reports/TECHNICAL-REPORT-finite-closed-extraction-resource-measure-v0.1.md
---

# Adversarial-hardening deep-research prompt — finite-closed scope theorem

Run this in a deep-research harness (web search + source retrieval + citation
verification) **with the scope-theorem paper attached** (and, ideally, the
extraction-resource technical report). It is the `drafts/`-stage hostile-referee +
prior-art pass that must be survived **before** the paper stages as a candidate.
The two most dangerous lines to watch: the **conservation-law / superselection**
counterexample to Part 2, and a **Batterman/Norton prior-art duplicate** on
"sharp distinctions require a limit."

---

ROLE. You are an adversarial referee and prior-art investigator with deep-research
tools (web search, source retrieval, citation verification). Your job is NOT to
praise or summarize. It is to (A) try to BREAK the attached result, (B) determine
whether it is already known, and (C) tell me honestly if and where it is
publishable and what must be hardened first. Assume I am the author and I want the
harshest competent review I can get before I embarrass myself.

THE ARTIFACT. The attached document ("the scope theorem") claims a no-go result
about capability boundaries in finite closed models. Its load-bearing claims,
restated so you can target them:

  SETTING. A "finite closed model" = a finite configuration space with
  deterministic or finite-dimensional unitary dynamics and NO external reservoir
  (the full configuration is retained). A "region R" has a menu M_R of supported
  operations/queries (observational and interventional-within-R). Two
  configurations c_A, c_B are "R-statistically equivalent" if identical under
  every M_R query. A "capability boundary" is a larger menu that separates them.

  PART 1 (Declarability Lemma; claimed PROVEN, elementary). If c_A, c_B are
  R-statistically equivalent yet some capability boundary separates them, the
  separating datum is necessarily a function of R's CO-PRESENT complement. So the
  informational boundary is always "declared" (a removable access restriction),
  never a physical absence.

  PART 2 (Physicality-Requires-a-Gap; claimed ARGUED + v0.1 formalized). A
  "physical" (forced, non-declared) boundary would need the extraction cost of the
  co-present datum to be prohibitive. But at a single instance the model is finite,
  so brute-force extraction costs finitely -> "prohibitive" is only meaningful
  asymptotically (across a family). An asymptotic lower-bound claim has exactly two
  epistemic statuses: provably divergent (E1) or conditional on a hardness
  assumption (E2). A stipulated finite budget (E0) is declared and collapses.
  CONCLUSION: no finite closed single-instance model has an unconditionally
  physical capability boundary; physicality requires E1 (a limit) or E2 (an
  assumption). Equivalently: "physical vs declared" collapses to "single-instance
  vs infinity-or-a-hardness-bet."

  WITNESSES. Three executable instances are offered as support, not proof: a
  thermal quantum-Darwinism model (E0, absorbed), a finite cooperative game with
  Shapley/Aumann-Shapley structure (E1), and a Goldwasser-Micali quadratic-
  residuosity construction (E2). Treat these as illustrations to check, not
  authority.

TASK A - ADVERSARIAL CORRECTNESS. Try hardest to break each part. Specifically:
  1. Part 1: Is it correctly stated or does it hide assumptions? Stress the edge
     cases: interventional (not just observational) statistics; entanglement /
     correlations that are "in no marginal" (is the datum a "function of the
     complement" in any useful sense then?); empty or trivial complement;
     deterministic vs unitary; whether "R-statistical equivalence" is strong enough
     to force the conclusion or too strong to be interesting.
  2. Part 2: Attack the exhaustiveness ("no fourth mode"). The STRONGEST
     counterexample I know of and want you to pursue relentlessly: a CONSERVATION
     LAW or SUPERSELECTION RULE (charge/parity/a symmetry) that forbids the
     crossing operation on physical states REGARDLESS of resources. That looks like
     a physical, single-instance, non-asymptotic, non-declared barrier. Does it
     refute Part 2, or does the theorem absorb it (the forbidden op is just outside
     the menu = declared; or it is a structural/limit fact = E1)? Push both ways
     and reach a verdict. Also test: dynamical impossibility from the map's
     structure (non-invertibility, Landauer/logical irreversibility), and whether
     "extraction cost" is a legitimate primitive or smuggles the conclusion.
  3. Give the single most damaging objection you found and whether the result
     survives it, needs a fix (state the fix), or fails.

TASK B - PRIOR ART / NOVELTY. The claimed novelty is the SYNTHESIS (a declared-vs-
physical scope no-go for capability/finality boundaries, with the E0/E1/E2
taxonomy), not new mathematics. Determine whether this synthesis, or something
close, already exists. Search thoroughly; the following are STARTING POINTS, not
limits - go beyond them:
  - Philosophy of emergence & idealization: Batterman (The Devil in the Details;
    Emergence/Singularities/Symmetry Breaking), Norton (Approximation and
    Idealization), Callender & Menon on phase transitions, Butterfield ("Less is
    Different"), Landsman (limits in QM foundations). Claim to check: "sharp
    distinctions require the thermodynamic/continuum limit."
  - Phase transitions require the thermodynamic limit (Yang-Lee, Kadanoff).
  - Computational vs information-theoretic indistinguishability/security
    (Goldwasser-Micali; Goldreich; HILL computational entropy; Yao).
  - Quantum Darwinism / emergence of objectivity (Zurek); recoverability and
    approximate Markov chains (Petz; Fawzi-Renner); Hayden-Preskill.
  - Cooperative game value theory (Shapley; Aumann-Shapley non-atomic games;
    Aumann's equivalence theorem).
  - Finite-system reversibility: Poincare recurrence, Loschmidt; no true
    irreversibility in finite closed dynamics.
  - Data-processing inequality / no-cloning / resource theories as the general
    "no information from restriction" shape.
  - Computational / cryptographic arrow of time; logical (ir)reversibility
    (Bennett); any recent work tying time's arrow to computational hardness.
  For each: does it state something equivalent to Part 1, Part 2, or the full
  synthesis? Report the CLOSEST prior work with exact citation and a quoted or
  precisely-paraphrased statement, and rate overlap: DUPLICATE / STRONG-OVERLAP /
  ADJACENT / UNRELATED.

TASK C - PUBLISHABILITY & HARDENING. Given A and B: is this publishable, and as
what (hard-theorem math paper / foundations-of-physics conceptual paper / CS
crossover / not publishable as-is)? Name plausible venues. List, in priority
order, the concrete things that must be fixed or added to make it defensible
(missing formalizations, the conservation-law objection, prior-art citations to
add, scope caveats to state).

OUTPUT FORMAT.
  1. Correctness verdict: Part 1 [survives/fix/broken] + Part 2 [survives/fix/
     broken], each with the specific attack and outcome.
  2. Strongest single objection and its resolution.
  3. Prior-art table: claim | closest prior work (full citation) | quoted
     statement | overlap rating.
  4. Novelty verdict: NOVEL-SYNTHESIS / PARTIALLY-KNOWN / ALREADY-EXISTS, with the
     one citation that most threatens novelty.
  5. Publishability verdict + venues.
  6. Prioritized hardening checklist.

DISCIPLINE. Cite only real, locatable sources (author, title, year, venue/DOI/
arXiv id); never fabricate a citation - if unsure, say "unverified." Quote or
precisely paraphrase the specific prior claim; do not gesture at a field. Separate
"found in the literature" from "my own reasoning." Rate your confidence on every
verdict. If the result is basically Batterman/Norton in new clothes, say so
plainly - that is the most useful thing you can tell me.
