export const meta = {
  name: 'persona-idea-sprint',
  description: 'Run 43 TaF persona lenses against current repo state, vote cross-disciplinarily, produce convergence map',
  phases: [
    { title: 'Generate', detail: '5 parallel disciplinary groups × ~8 personas each × 3 idea tiers' },
    { title: 'Synthesize', detail: 'Cross-disciplinary voting: novelty / profundity / publishability / intrigue + convergence map' },
    { title: 'Save', detail: 'Write full sprint doc to explorations/ and route top ideas to tests/ and open-problems/' },
  ],
}

// Args: { date: string (YYYY-MM-DD), focus?: string }
const DATE = (args && args.date) ? args.date : 'unknown-date'
const FOCUS = (args && args.focus) ? args.focus : null

const REPO = String.raw`C:\Users\joe\JB\Github Repos\time-as-finality`

// Current repo context prompt — each group agent reads these files itself
const REPO_CONTEXT_PROMPT = `
The Time as Finality repo is at: ${REPO}

Read these files to understand the current state of the theory before generating ideas:
1. ESSAY.md — core thesis
2. HYPOTHESES.md — formal hypotheses H1-H7+
3. ROADMAP.md — what has been done and what is planned
4. CLAIM-LEDGER.md — all claims and their status
5. TESTS.md — which tests have been built
6. personas/INDEX.md — the full persona lens registry (you will filter to your assigned group)
7. models/spacetime_aggregation.py — T16/T13 Cech cohomology implementation (skim top 100 lines for context)

The core thesis: time for embedded observers is the order of record-finalization. The past is
what has become hard to undo. D1 is a componentwise preorder across four dimensions:
(1) number of accessible records, (2) distinct-holder redundancy, (3) causal branch support,
(4) graph reversal count. The theory is NOT a physics derivation — it is an observer-protocol
framework that may constrain or be constrained by physics.
`

const IDEA_FORMAT = `
For each persona, output exactly this format:

[PERSONA NAME] | USEFUL
Title: <5-10 word name>
Claim: <one sentence>
Why not wrong: <one sentence — why this lens doesn't reject it>
Deliverable: <most concrete next step>

[PERSONA NAME] | BIG
Title: ...
Claim: ...
Why not wrong: ...
Deliverable: ...

[PERSONA NAME] | WILD SWING
Title: ...
Claim: ...
Why not wrong: ...
Deliverable: ...

Keep each idea self-contained. Do not hedge beyond "Why not wrong." Be specific.
`

// Five parallel groups — persona families per group
const GROUP_PROMPTS = [
  {
    label: 'Group A — Quantum & Measurement',
    prompt: `You are voicing 8 persona lenses from the Time as Finality repo for a cross-disciplinary idea sprint.

${REPO_CONTEXT_PROMPT}

Your assigned personas (from personas/INDEX.md — read the file to get each lens's definition):
1. Quantum measurement / decoherence (Local TaF Lenses section)
2. Quantum foundations / decoherence expert (TaF Crosswalk Lenses section)
3. Lattice QFT / anomaly theorist (TaF Crosswalk Lenses section)
4. QFT theorist (Foundational Math Lenses section)
5. Quantum measurement theorist (Substrate-Loophole Lenses section)
6. Quantum circuits / tensor networks (Computation-Substrate Lenses section)
7. Quantum measurement problem-shape (Heterodox Problem-Shape Math Lenses section)
8. ZK cryptography (Local TaF Lenses section)

For each persona: read its description in the index, then voice it against the CURRENT repo state.
Generate three ideas at increasing ambition: Useful / Big / Wild Swing.
A Wild Swing is something ambitious that the persona genuinely does not see a fatal objection to.
Do NOT sandbag. If a lens can see a real path, name it.

${IDEA_FORMAT}

${FOCUS ? `Sprint focus area: ${FOCUS}` : 'No focus area — full repo state, any direction.'}

After all 8 × 3 = 24 ideas, write a one-paragraph GROUP SUMMARY naming the single strongest
signal your group found — the idea or cluster most worth the synthesis agent's attention.`
  },
  {
    label: 'Group B — Relativity & Geometry',
    prompt: `You are voicing 8 persona lenses from the Time as Finality repo for a cross-disciplinary idea sprint.

${REPO_CONTEXT_PROMPT}

Your assigned personas (from personas/INDEX.md — read the file to get each lens's definition):
1. Relativity / causal-structure (Local TaF Lenses section)
2. Relativity / causal structure expert (TaF Crosswalk Lenses section)
3. General relativist (Foundational Math Lenses section)
4. Differential geometer (Foundational Math Lenses section)
5. Cartan / twistor theorist (Substrate-Loophole Lenses section)
6. Higher / derived geometer (Substrate-Loophole Lenses section)
7. Cartan-twistor problem-shape (Heterodox Problem-Shape Math Lenses section)
8. Higher-derived problem-shape (Heterodox Problem-Shape Math Lenses section)

For each persona: read its description in the index, then voice it against the CURRENT repo state.
Generate three ideas at increasing ambition: Useful / Big / Wild Swing.
A Wild Swing is something ambitious that the persona genuinely does not see a fatal objection to.

${IDEA_FORMAT}

${FOCUS ? `Sprint focus area: ${FOCUS}` : 'No focus area — full repo state, any direction.'}

After all 8 × 3 = 24 ideas, write a one-paragraph GROUP SUMMARY naming the single strongest
signal your group found.`
  },
  {
    label: 'Group C — Math & Formal',
    prompt: `You are voicing 8 persona lenses from the Time as Finality repo for a cross-disciplinary idea sprint.

${REPO_CONTEXT_PROMPT}

Your assigned personas (from personas/INDEX.md — read the file to get each lens's definition):
1. Godel (Local TaF Lenses section)
2. Algebraic topologist (Foundational Math Lenses section)
3. Gauge theorist (Foundational Math Lenses section)
4. Representation theorist (Foundational Math Lenses section)
5. Mathematical physicist (Foundational Math Lenses section)
6. Heterodox critical theorist (Foundational Math Lenses section)
7. Spinor / Clifford theorist (Foundational Math Lenses section)
8. Higher-dimensional / Kaluza-Klein theorist (Foundational Math Lenses section)

For each persona: read its description in the index, then voice it against the CURRENT repo state.
Generate three ideas at increasing ambition: Useful / Big / Wild Swing.

${IDEA_FORMAT}

${FOCUS ? `Sprint focus area: ${FOCUS}` : 'No focus area — full repo state, any direction.'}

After all 8 × 3 = 24 ideas, write a one-paragraph GROUP SUMMARY naming the single strongest
signal your group found.`
  },
  {
    label: 'Group D — Computation & Distributed Systems',
    prompt: `You are voicing 10 persona lenses from the Time as Finality repo for a cross-disciplinary idea sprint.

${REPO_CONTEXT_PROMPT}

Your assigned personas (from personas/INDEX.md — read the file to get each lens's definition):
1. BFT / CAP impossibility (Local TaF Lenses section)
2. DAG / partial-order causality (Local TaF Lenses section)
3. Wolfram physics (Computation-Substrate Lenses section)
4. Cellular automata (Computation-Substrate Lenses section)
5. Complexity / decidability (Computation-Substrate Lenses section)
6. Constructor theory (Computation-Substrate Lenses section)
7. BFT / CAP / FLP consensus impossibility (Distributed-Systems Lenses section)
8. Avalanche / Snowball metastable consensus (Distributed-Systems Lenses section)
9. Hashgraph / gossip-about-gossip provenance (Distributed-Systems Lenses section)
10. Stigmergy / swarm coordination (Distributed-Systems Lenses section)

For each persona: read its description in the index, then voice it against the CURRENT repo state.
Generate three ideas at increasing ambition: Useful / Big / Wild Swing.

${IDEA_FORMAT}

${FOCUS ? `Sprint focus area: ${FOCUS}` : 'No focus area — full repo state, any direction.'}

After all 10 × 3 = 30 ideas, write a one-paragraph GROUP SUMMARY naming the single strongest
signal your group found.`
  },
  {
    label: 'Group E — Conceptual, Critical & Analogy',
    prompt: `You are voicing 9 persona lenses from the Time as Finality repo for a cross-disciplinary idea sprint.

${REPO_CONTEXT_PROMPT}

Your assigned personas (from personas/INDEX.md — read the file to get each lens's definition):
1. Hostile rigor gatekeeper (Local TaF Lenses section)
2. Escher (Local TaF Lenses section)
3. Bach (Local TaF Lenses section)
4. Fractal and evolutionary models (Local TaF Lenses section)
5. Avalanche / Snowball consensus (Local TaF Lenses section)
6. GU formalist / no-go discipline (TaF Crosswalk Lenses section)
7. Black-hole / holography expert (TaF Crosswalk Lenses section)
8. Philosopher of science / hostile skeptic (TaF Crosswalk Lenses section)
9. Publication / contributor strategist (TaF Crosswalk Lenses section)

For each persona: read its description in the index, then voice it against the CURRENT repo state.
Generate three ideas at increasing ambition: Useful / Big / Wild Swing.
The Hostile Rigor Gatekeeper and Hostile Skeptic should still produce actionable ideas, not
just criticism — their Wild Swings are ideas they think could survive their own scrutiny.

${IDEA_FORMAT}

${FOCUS ? `Sprint focus area: ${FOCUS}` : 'No focus area — full repo state, any direction.'}

After all 9 × 3 = 27 ideas, write a one-paragraph GROUP SUMMARY naming the single strongest
signal your group found.`
  },
]

// ─── Phase 1: Generate ────────────────────────────────────────────────────────

phase('Generate')
log('Dispatching 5 parallel disciplinary groups...')

const GROUP_RESULTS = await parallel(
  GROUP_PROMPTS.map(g => () =>
    agent(g.prompt, { label: g.label, phase: 'Generate' })
  )
)

const validResults = GROUP_RESULTS.filter(Boolean)
log(`${validResults.length}/5 groups completed`)

// ─── Phase 2: Synthesize ──────────────────────────────────────────────────────

phase('Synthesize')

const allIdeas = validResults.join('\n\n---GROUP BOUNDARY---\n\n')

const synthesisPrompt = `You are the synthesis agent for a Time as Finality persona idea sprint.

Below are idea outputs from 5 independent disciplinary groups (43 persona lenses total,
129+ ideas). Each group worked in isolation — they did not see each other's outputs.

YOUR TASK: Cross-disciplinary voting and convergence mapping.

${REPO_CONTEXT_PROMPT}

─── ALL GROUP OUTPUTS ───
${allIdeas}
─── END OF GROUP OUTPUTS ───

VOTING CATEGORIES — pick top entries for each:

**Most Novel** (top 3)
Ideas that do NOT appear in any form in the existing ROADMAP.md, TESTS.md, or HYPOTHESES.md.
Genuinely new directions for the theory.

**Most Profound** (top 3)
Ideas whose success would most reshape the theory's claims or scope.
If this works, what does TaF become?

**Highest Publishable Potential** (top 3)
Ideas closest to a bounded, verifiable result suitable for a CS or physics venue.
Name the venue type.

**Most Intriguing / Worth a Bet** (top 5)
Ideas you would personally investigate if you had 2 weeks. Explain each in one sentence.

─── CROSS-PERSONA CONVERGENCE MAP ───

A convergence is when 2+ groups, using DIFFERENT vocabulary and formalisms, arrive at
structurally the same claim. These are the primary output signal.

List each convergence cluster:
- Cluster name
- Which groups / which personas contributed
- The shared structural claim in neutral language (not one group's vocabulary)
- Why this convergence is meaningful (what it suggests about the theory's attractors)
- Recommended next step

─── SPRINT SUMMARY ───

Write a 3-paragraph summary:
1. What the sprint found overall
2. What surprised you (ideas that appeared in multiple groups without coordination)
3. What the theory should do next — top 1-2 actionable recommendations

Format your full output as a well-organized markdown document with clear section headers.
This will be saved verbatim to explorations/all-persona-idea-sprint-${DATE}.md`

log('Running synthesis and voting...')
const synthesisResult = await agent(synthesisPrompt, {
  label: 'Synthesis & Voting',
  phase: 'Synthesize',
})

// ─── Phase 3: Save ────────────────────────────────────────────────────────────

phase('Save')

const HEADER = `# All-Persona Idea Sprint — ${DATE}

**Method:** 43 persona lenses × 3 idea tiers (Useful / Big / Wild Swing) + cross-disciplinary voting
**Repo state:** Post T10-T18, Cech cohomology (T13), finality direction theorem (T18), 6 new open problems
**Groups:** 5 parallel disciplinary groups ran independently; no group saw another's output during generation
${FOCUS ? `**Focus:** ${FOCUS}` : ''}

---

## Raw Group Outputs

`

const savePrompt = `Save the following content as a new file in the Time as Finality repo.

File path: ${REPO}\\explorations\\all-persona-idea-sprint-${DATE}.md

Content to write (write it EXACTLY, do not modify or summarize):

${HEADER}
${validResults.map((r, i) => `### ${GROUP_PROMPTS[i].label}\n\n${r}`).join('\n\n---\n\n')}

---

## Synthesis, Voting & Convergence Map

${synthesisResult}

---

*Generated by persona-idea-sprint workflow from agent-skills/persona-idea-sprint.js*
*All 43 persona lenses from personas/INDEX.md. Groups ran in parallel without seeing each other's output.*

After writing the file, also check ROADMAP.md and HYPOTHESES.md to see if the top-voted ideas
introduce anything that should be added (new phases, new hypotheses). If so, make minimal,
targeted additions — do not rewrite existing content.

Finally, check if any top-voted ideas warrant a new test spec file in tests/ or a new open problem
in open-problems/. If so, create one file per idea using the existing format as a template
(read tests/T13-finality-sheaf-cohomology.md as a style reference). Do not create more than
3 new files — choose only the most ready ideas.

Report back: what files you created or modified, and the top 3 convergence findings.`

log('Writing sprint document and routing top ideas...')
const saveResult = await agent(savePrompt, { label: 'Write outputs', phase: 'Save' })

return {
  groupsCompleted: validResults.length,
  date: DATE,
  saveResult,
  synthesisPreview: synthesisResult ? synthesisResult.slice(0, 500) : null,
}
