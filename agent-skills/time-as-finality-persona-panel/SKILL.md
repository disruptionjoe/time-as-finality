---
name: time-as-finality-persona-panel
description: Run the Time as Finality persona panel for repo research questions, goal drafting, hostile audits, theorem critique, synthesis, or cross-domain evaluation. Use when Joe asks to use the TaF persona panel, ask the panel, run personas, steelman through personas, get independent mathematical/scientific lenses, or evaluate a Time as Finality idea through diverse expert perspectives.
---

# Time as Finality Persona Panel

Use this skill to run independent persona critique and synthesis for the Time
as Finality repo.

## Core Rule

Personas must think independently before synthesis. Do not let one persona see
another persona's response until the synthesis phase.

## Workflow

1. Read `references/personas.md`.
2. Select either:
   - the full panel;
   - a focused subset by persona number or domain;
   - a hostile subset for overclaim checks.
3. Give each selected persona the same task prompt and repo context.
4. Require the standard response structure:
   - summary of understanding;
   - strongest insight;
   - strongest criticism;
   - hidden assumptions;
   - rose;
   - bud;
   - thorn;
   - confidence 1-10;
   - suggested experiment;
   - suggested theorem or mathematical direction;
   - suggested falsification test.
5. Only after independent responses, synthesize:
   - convergences;
   - disagreements;
   - strongest warning;
   - strongest next executable goal;
   - claim-status recommendation.
6. If voting is requested, use quadratic voting:
   - each persona gets 100 vote points;
   - vote cost is `intensity^2`;
   - intensity is 1-10;
   - a persona may spend on multiple options until its budget is exhausted.

## Useful Invocation Patterns

Chat call:

```text
Use the repo skill at agent-skills/time-as-finality-persona-panel to evaluate:
<question or draft goal>
```

Focused panel:

```text
Use the TaF persona panel with personas 1, 4, 7, 9, 25, 50, 52, and 54 on:
<question>
```

Hostile audit:

```text
Use the TaF persona panel hostile subset to find overclaims and falsification tests for:
<claim>
```

Prompt-builder command:

```bash
python agent-skills/time-as-finality-persona-panel/scripts/build_panel_prompt.py --focus "T46 CS1 boundary" --personas 1,4,9,50,52,54
```

Write prompt to a file:

```bash
python agent-skills/time-as-finality-persona-panel/scripts/build_panel_prompt.py --focus "next theorem goal" --all --output tmp-persona-panel-prompt.md
```

## Default Subsets

Use the full panel for major forks, claim promotion, and theory architecture.

Use a focused subset for goal drafting or quick critique:

```text
1, 2, 4, 7, 9, 10, 22, 23, 25, 50, 51, 52, 54
```

Use the hostile subset for overclaim checks:

```text
25, 27, 42, 50, 52, 54
```

Use the GU/geometry subset for Observerse, Y -> X, bundle, or index questions:

```text
1, 3, 4, 5, 6, 45, 46, 47, 48, 49, 50, 52
```

Use the distributed/record-access subset for R1, A1, T42-T46, consensus, and
propagation questions:

```text
9, 10, 12, 13, 22, 23, 24, 34, 35, 38, 39, 50, 54
```

## Output Discipline

Keep claims conservative. Distinguish:

- analogy;
- homology;
- reduction;
- equivalence.

Do not promote a claim unless multiple independent personas support it and the
repo has executable or formal evidence.

Route likely outputs as:

- technical report for a completed audit;
- test track for executable follow-up;
- open problem for a theorem not yet earned;
- claim-ledger update only when evidence warrants it.
