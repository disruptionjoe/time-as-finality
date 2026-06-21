---
document_type: correction_note
status: non_canonical_exploration
authority: terminology_and_prior_art_guidance
created: 2026-06-20
---

# ASP Naming And Prior-Art Correction Note v0.1

## Purpose

This note corrects the naming and novelty posture around the recent
"accessible possibility / accessible state space" thread.

It does not update claims, roadmap state, test status, North Star language, or
workflow state. It is a guardrail for future artifacts.

## Correction Summary

Three points should be separated.

1. **Acronym hygiene:** `ASP` is a bad final abbreviation. In technical
   computing contexts, `ASP` strongly collides with Answer Set Programming.
2. **Novelty posture:** "Accessible State Space" should not be presented as a
   recognized scientific term, a new primitive, or a discovered law.
3. **Actual candidate object:** the useful object is a compound intersection:

```text
reachable
  cap maintainable
  cap admissible
  cap reconstructable
  cap actionable
```

That object is closer to an operational future set than to plain reachability
or a raw state space.

## Why `ASP` Should Be Rejected As Final Terminology

`ASP` is already established in computer science as Answer Set Programming.
That collision is not cosmetic. Answer Set Programming is a mature logic and
knowledge-representation paradigm with solvers, textbooks, and ACM-indexed
usage.

Using `ASP` for this repo's object would create avoidable ambiguity in exactly
the neighboring technical territory where the repo already talks about
logic, admissibility, search spaces, witnesses, and constraints.

Acceptable posture:

```text
ASP may appear in scratch notes only as temporary shorthand.
Do not use ASP in paper-facing, test-facing, or open-problem titles.
```

## Novelty Correction

Do not write:

```text
Accessible State Space is a recognized scientific primitive.
Accessible State Space is more fundamental than entropy, information, or
finality.
ASP is a new mathematical object.
```

Safer wording:

```text
The repo is testing a compound, observer/task-indexed audit object assembled
from existing notions: reachability, viability, admissibility, reconstruction,
and feasible action/operation sets.
```

The only possible value is not novelty by naming. The possible value is a
cross-framework audit:

```text
When do the existing frameworks disagree about what futures remain usable for
an observer/task?
```

If no such disagreement survives enriched prior-art models, the object should
be treated as integration vocabulary only.

## Preferred Naming Options

| Candidate name | Use when | Strength | Risk |
| --- | --- | --- | --- |
| **Admissible Future Set** | Provenance, authority, legal/institutional, detector-log, or witness-obligation cases are central. | Best technical fit for TaF's admissibility discipline. | May sound too legal or policy-heavy for physics/cognition. |
| **Operational Future Space** | The emphasis is future usable operations, tasks, interventions, or operation rights. | Broad, concrete, and less overloaded than "state space." | "Space" can still invite vague geometry. |
| **Future Opportunity Structure** | The goal is broader and less technical, especially for emergence, goals, or platform capacity. | Good exploratory language; signals structure rather than primitive. | "Opportunity" collides with economics and can sound informal. |
| **Accessible Task Set** | The model is explicitly finite and task-indexed. | Cleanest executable term. | Too narrow for broad conceptual notes. |
| **Admissible Operation Set** | Rights, permissions, and executable operations are primary. | Good for T117-style finite audits. | Less natural for biological or cognitive examples. |

Recommendation:

```text
Use "Admissible Future Set" for formal/provenance-heavy artifacts.
Use "Operational Future Space" for broad exploratory synthesis.
Use "Accessible Task Set" inside executable finite models.
Avoid "ASP" outside scratch text.
```

## Prior-Art Frame

The compound object is assembled from existing literatures. It should be
described as an audit intersection, not a replacement primitive.

| Component | Existing homes |
| --- | --- |
| Reachable | Reachable-set analysis, control theory, transition systems, causal access. |
| Maintainable | Viability theory, resilience, active inference/free energy, homeostasis, maintenance/resource accounting. |
| Admissible | Formal methods, proof obligations, legal/provenance authority, TaF PO1/T87-style admissibility gates. |
| Reconstructable | Information theory, coding, provenance, reconstruction debt, database lineage, observer access. |
| Actionable | Opportunity sets, mechanism design, control actions, operation rights, affordance theory, constructor-theoretic tasks. |

The object is most useful when these components disagree.

Example:

```text
A future task may be reachable but not admissible.
A record may be stored but not reconstructable.
A system may be maintainable but not actionable.
A state may be viable but lack authority or witness rights for future use.
```

That disagreement is the research target.

## Relation To T117

`T117-accessible-state-space-separation` already has the right conservative
shape in substance:

```text
ASP(observer, horizon) = admissible future task set
```

and it correctly states:

```text
No core claim is upgraded.
The object is mostly absorbed by enriched reachable-state, opportunity-set,
provenance, commons, and mechanism-design formalisms.
```

But the terminology should be revised before any serious promotion:

```text
old: Accessible State Space Separation Audit
better: Admissible Future Set Separation Audit
or: Operational Future Set Separation Audit
```

The test's strongest concept is not "state space." It is:

```text
same coarse future reachability
different admissible future task set
because witnesses, rights, maintenance budget, reconstruction paths, or
certification tokens differ.
```

## Naming Decision Table

| Goal | Recommended name |
| --- | --- |
| Paper-facing formal object | Admissible Future Set |
| Finite executable test variable | Accessible Task Set or Admissible Operation Set |
| Broad exploration / North-Star-adjacent prose | Operational Future Space |
| Emergence/platform discussion | Future Opportunity Structure |
| Scratch shorthand only | ASP |

## Failure Conditions

Abandon this naming branch if:

1. The intersection is assigned after the conclusion rather than computed from
   predeclared witness/right/maintenance/reconstruction/action requirements.
2. Reachability plus enriched state variables fully predicts every case.
3. Opportunity-set economics, mechanism design, viability theory, or
   provenance already captures the target with no useful residue.
4. The term encourages claims that entropy, information, or finality have been
   replaced.
5. The object cannot produce negative controls where a future is reachable but
   not admissible, maintainable, reconstructable, or actionable.

## Recommended Next Artifact

Do not try to prove "ASP exists."

Build a correction and comparison artifact:

```text
Admissible Future Set Prior-Art Audit
```

Minimum required outputs:

- Define the intersection:

  ```text
  reachable cap maintainable cap admissible cap reconstructable cap actionable
  ```

- For each prior-art neighbor, state which component it already covers.
- Preserve at least one negative control:

  ```text
  reachable but not admissible
  maintainable but not actionable
  stored but not reconstructable
  actionable locally but not authority-valid
  ```

- Report whether any gap remains between the literatures.

## Sources For Acronym Hygiene

- Lifschitz, "What Is Answer Set Programming?" states that Answer Set
  Programming (`ASP`) is a declarative programming approach for difficult
  search problems: https://www.cs.utexas.edu/~vl/papers/wiasp.pdf
- Communications of the ACM, "Answer Set Programming at a Glance": https://cacm.acm.org/research/answer-set-programming-at-a-glance/
- ACM Computing Classification System includes "Logic programming and answer
  set programming" under knowledge representation and reasoning:
  https://cran.r-project.org/web/classifications/ACM-2012.html

## Final Correction

Recommended repo posture:

```text
Reject ASP as final terminology.
Preserve the concept only as a cross-framework audit object.
Prefer Admissible Future Set when admissibility/witness/authority matters.
Prefer Operational Future Space when the broader future-operation framing
matters.
Prefer Future Opportunity Structure for broad exploratory prose.
```

The strongest current concept is:

```text
Admissible Future Set_O,h =
  reachable futures
  cap maintainable futures
  cap admissible futures
  cap reconstructable futures
  cap actionable futures
```

It is not a new primitive. It is a candidate diagnostic intersection for
finding gaps between existing theories.
