# Information Portfolio

The information-gain ledger. Value in this program is measured by **change in
understanding over time**, not by the win/loss record of hypotheses. A line that
failed can still have produced large information gain (operating model §3). This
registry is maintained by `govern/information-portfolio`.

> **Seed note (Phase 2, Session 4).** Seeded with a few illustrative entries; the
> first `information-portfolio` run will normalize and extend it.

## Entries

| line | status | information gain (what understanding changed) | gain type |
|---|---|---|---|
| RL-006 Compression-finality crosswalk | archived | Established that compressibility is a *downstream observable* of stable records, not a D1 finality dimension; Rule 30 (high finality, low compressibility) and Rule 0 counterexamples across all 256 ECA rules. A "wrong" line that sharpened a definition. | definition sharpened; counterexample produced |
| RL-001 FinaliEvent → finite descent | active (primary) | Showed canonical observer-relative temporal reconstruction requires finite descent conditions plus Axis Monotonicity; separated partial-order consistency, descent uniqueness, and axis reconstructability (T53→T54). | theorem inspired; better test produced |
| RL-002 PO1 schema | active (secondary) | PO1 compresses to a four-principle basis; AC4 follows from AC6; measurement asymmetry and DAG theorems established. | formalism strengthened; cross-domain validation |
| RL-005 Local persistence | active (explored) | Finite probes separate the T43 mechanism families (demand-drop + coupling-rewire); baseline traces remain ambiguous. | identifiability boundary clarified |

## Gain-type vocabulary (from operating model §3)

A line raises information gain when it: reveals a missing definition, exposes a
flaw in a stronger line, inspires a new theorem, improves persona clustering,
produces a better test, or seeds a stronger exploit candidate.

## How this registry is maintained

`govern/information-portfolio` appends an entry whenever a workflow run changes
the program's understanding — including, especially, when a line is archived. It
also reports the portfolio balance across explore/exploit/govern so the program
can see whether it is over- or under-investing in any posture.
