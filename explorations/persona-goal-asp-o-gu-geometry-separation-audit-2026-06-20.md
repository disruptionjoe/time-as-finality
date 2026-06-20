# Persona Goal: ASP_O(U) GU Geometry Separation Audit

Status: exploratory persona-goal run, non-canonical  
Date: 2026-06-20  
Goal: test whether `ASP_O(U)` is a useful mathematical object or elegant notation for existing machinery.

This artifact does not promote ASP, GU, or any related physics claim. It records a hostile separation/absorption audit and routes consequences only as recommendations.

## Goal Prompt

`ASP_O(U)` means the accessible structured possibility set available to observer `O` over domain `U`.

It should include only futures, reconstructions, interventions, sections, transports, and operation rights that remain:

- causally accessible;
- structurally maintainable;
- admissible;
- usable for downstream operations;
- observer-indexed.

The live question:

```text
Does observer-indexed structured possibility explain future operation availability
in cases where existing measures fail to distinguish?
```

Guardrails used:

- Do not claim ASP replaces entropy.
- Do not claim ASP replaces information.
- Do not claim ASP replaces finality.
- Do not claim ASP proves GU.
- Do not claim ASP explains consciousness.
- Do not claim observers create time.

## Persona Run

Three independent subagent rooms were used.

| Room | Persona posture | Focus |
| --- | --- | --- |
| A | Mathematical physicist, differential geometer, sheaf theorist, fiber bundle specialist, gauge theorist, GU specialist | GU/sheaf typing and whether geometry helps |
| B | Information theory, resource theory, constructor theory, philosophy of science, RL/control, skeptic, minimalist, experimentalist | prior-art absorption and residue |
| C | Formal methods, RL/control, access-control, experimentalist, provenance | finite matched examples |

All rooms were read-only. No canonical files, claims, tests, registries, or roadmap entries were updated.

## Repository Context Used

This run leaned on existing nearby artifacts:

- `explorations/accessible-structured-possibility-gu-persona-review-note-v0.1.md`
- `explorations/research-constellation-orchestrator-2026-06-20-180249-asp-gu-note.md`
- `TECHNICAL-REPORT-accessible-state-space-separation-v0.1.md`
- `TECHNICAL-REPORT-accessible-witness-gap-restriction-v0.1.md`
- `TECHNICAL-REPORT-viability-filter-v0.1.md`
- `TECHNICAL-REPORT-maintenance-viability-split-v0.1.md`
- `TECHNICAL-REPORT-provenance-aware-reconstruction-separation-v0.1.md`
- `tests/T117-accessible-state-space-separation.md`
- `models/accessible_state_space_separation.py`
- `results/accessible-state-space-separation-v0.1-results.md`

The most relevant prior result is T117: ASP separates from coarse entropy, information, finality, viability, persistence, and coarse reachability, but is mostly absorbed by enriched reachable-state, opportunity-set, provenance, commons, mechanism-design, and reconstruction-debt formalisms.

## 1. Strongest Version Of ASP_O(U)

The strongest disciplined object is not raw possibility, not a scalar, not a dynamics, and not a goal.

Best geometric form:

```text
pi : Y -> X
C_O = site of observer-accessible patches U subset X
S(U) = Gamma(U, Y|_U)

ASP_O^T(U,h) =
  { s in S(U) |
    s satisfies declared task family T at horizon h
    under causal access, support, recordability,
    distinguishability, maintainability, viability,
    witness/admissibility/reconstruction conditions }
```

Best finite form:

```text
ASP_O^T(U,h) = admissible future task set
```

A task is in `ASP_O^T(U,h)` only if the observer has:

- required witnesses;
- operation rights;
- admissibility or certification tokens;
- sufficient maintenance budget;
- reconstruction paths;
- causal access over the horizon;
- viability-preserving execution conditions.

Dynamics, viability regions, measures, and goals are separate structures:

```text
Phi = transition / forward transport rule
V   = viability region
mu  = invariant or covariant measure on ASP
G   = optional control or goal functional over ASP
```

Short name recommended by the rooms:

```text
AdmissibleFuture_O,h
```

or:

```text
AccessibleTaskSet_O,h
```

These names avoid implying that ASP is a new physical primitive.

## 2. Weakest Point

The weakest point is type mixing.

The current GU note mixes at least four different objects:

1. contravariant sheaf restriction;
2. covariant forward unfolding;
3. viability/control dynamics;
4. scalar rate or measure language.

Sheaf restriction has the form:

```text
rho_{V,U} : ASP_O(V) -> ASP_O(U)
```

for `U subset V`. Forward unfolding needs a separate flow, transition relation, or connection. It is not supplied by restriction maps.

The expression:

```text
sigma_O^*Y
```

is also suspicious if `sigma_O : U -> Y` is already a section of `pi : Y -> X`. The safe expression is:

```text
Y|_U
```

or a pullback of a separately specified bundle over `Y`.

This matters because rate claims such as:

```text
d mu(ASP_O) / d tau
```

are undefined until `mu`, the allowed transformations, and the observer-relative domain changes are all specified. A local-rate split can be meaningful in finite systems, but it should be described first as different changes in admissible task sets under different observer access profiles, not as physics.

## 3. Closest Prior Art

| Comparator | Audit verdict |
| --- | --- |
| Reachability analysis | Coarse reachability misses ASP. Enriched reachable-state analysis absorbs it when witnesses, rights, provenance tokens, certifications, and reconstruction paths are state variables. |
| Viability kernels | Absorbs ASP if the viability set is defined over future task availability rather than mere survival. |
| Active inference policy spaces | Absorbs ASP if policies range over witness-bearing, authority-valid futures. Residue exists only when the generative model omits rights/certification/provenance. |
| Reinforcement-learning action/state spaces | Absorbs ASP as augmented MDP/POMDP state plus action masks/options. ASP's useful pressure is forcing admissibility predicates to be predeclared rather than hidden in reward shaping. |
| Affordance landscapes | Largely absorbs actionable possibility. Weaker on record witnesses, certification, and repair/reconstruction debt unless enriched. |
| Opportunity sets | Strongest absorption target. ASP is very close to a feasible opportunity/task set under constraints and rights. |
| Information-theoretic distinguishability | Does not absorb ASP alone. Equal bits/distinguishability can still split on future usable operations. Enriched side information and provenance channels can partly absorb it. |
| Finality/reconstruction debt | The strongest TaF residue. Same finalized endpoint can differ in future merge/revert/bisect/repair because missing witnesses create reconstruction debt. Still mostly provenance plus task-enriched control. |
| Sheaf/section compatibility | Useful for typing: `ASP_O : C_O^op -> Set` as a typed subpresheaf, if predicates restrict monotonically. |
| GU source-shadow projection | Useful scaffolding for "rich source -> observer shadow." The residue is a nonfaithful shadow kernel: forgotten source structure determines future admissible operations. No GU validation follows. |

## 4. Minimum Finite Test Cases

All cases use a fixed observer `O`, horizon `h`, and task universe unless stated otherwise. The point is to expose where ASP adds nothing, where it separates, and where raw possibility language misleads.

| Case | Matched toy pair | What splits | Verdict |
| --- | --- | --- | --- |
| 1. Entropy wins | `A`: 4 equally reachable viable states. `B`: 8 equally reachable viable states. Same witness/rights profile; every state supports the same task type. | Raw state volume only. | Entropy explains the distinction. ASP adds no residue because admissibility structure is uniform. |
| 2. Information wins | `A`: 8 states but observer can distinguish only 2 classes. `B`: 8 states with 8 distinguishable labels. Same viability, rights, witnesses, task count. | Distinguishability. | Information explains the distinction. ASP follows only if tasks require those labels. |
| 3. Finality wins | `A`: 8 possible continuations, no stable record of which branch occurred. `B`: 8 continuations, one irreversible checkpoint record fixes branch order. Same task access and viability. | Record-stable restriction/order. | Finality explains the distinction even if opportunity count is unchanged. |
| 4. Viability wins | `A`: 8 accessible tasks, but 5 leave the system outside the survival set after one step. `B`: 8 accessible tasks, all remain inside the viability boundary. Same entropy, information, and finality. | Viability kernel. | Viability explains the distinction. ASP must be filtered by maintainability; raw task access is misleading. |
| 5. ASP wins | `A`: same endpoint repo snapshot, entropy `8`, information `8`, finality `4`, viability `4`, coarse reachable count `4`; has tree, merge base, branch history, signed history, and merge/revert/bisect rights. `B`: same endpoint snapshot and same coarse metrics; has tree only, no merge-base/history certification. | Admissible task set. | ASP separates: `A = {build, merge, revert, bisect}`, `B = {build}`. Coarse entropy/information/finality/viability miss witness/right structure. |
| 6. Expansion false positive | `A -> A'`: raw future states expand from 4 to 12 by adding uncertified branches, duplicate records, and inaccessible garbage. Witnesses and reconstruction paths fall from 2 to 0. | Raw expansion positive, ASP negative. | Possibility expansion is not automatically useful. `|S|` rises while `|ASP|` falls. |
| 7. Contraction positive | `B -> B'`: raw states contract from 12 noisy branches to 5 certified branches; schema, checksum, and audit log are restored. | Raw contraction negative, ASP positive. | Contraction can improve structured possibility. Fewer states support more admissible reconstruction/certification/repair tasks. |
| 8. Local-rate split | Same ambient finite source over two observer patches. `O1` gains a challenge window plus validator signatures: `ASP` grows `1 -> 4`. `O2` sees the same committed state after the challenge window expires: `ASP` stays `1` or falls. | Section-relative change in admissible futures. | Local rates split without invoking physics: different observer sections expose different access, witness, and rights predicates. |

## 5. Matched-Case Table

| Case | Entropy matched? | Information matched? | Finality matched? | Viability matched? | Reachable-state count matched? | ASP different? | Winner |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Entropy wins | No | Yes | Yes | Yes | No | Usually yes, but only by state volume | Entropy |
| Information wins | Yes | No | Yes | Yes | Yes | Only if tasks require distinguishability | Information |
| Finality wins | Yes | Yes | No | Yes | Yes | Not necessarily | Finality |
| Viability wins | Yes | Yes | Yes | No | Yes | Yes after maintainability filter | Viability |
| ASP wins | Yes | Yes | Yes | Yes | Yes, coarse | Yes | ASP against coarse baselines |
| Expansion false positive | No, raw count rises | Often no | Often no | Often no | No | Yes, ASP falls | ASP as guardrail |
| Contraction positive | No, raw count falls | Often no | Often improves | Often improves | No | Yes, ASP rises | ASP as guardrail |
| Local-rate split | Globally yes | Globally yes | Globally yes | Globally yes | Globally yes | Yes by observer profile | ASP as observer-indexed audit |

The `ASP wins` row is narrow. It wins only against coarse baselines. Once reachability, opportunity sets, viability, control, active inference, or RL are enriched with witnesses, rights, provenance, certifications, and reconstruction paths, the split is mostly absorbed.

## 6. Separation Or Absorption Verdict

ASP separates from:

- raw entropy/state count;
- coarse information bits;
- coarse finality score;
- coarse viability labels;
- coarse reachable-state count;
- endpoint-only source-shadow descriptions.

ASP is absorbed by:

- enriched reachable-state analysis;
- task-enriched viability kernels;
- augmented MDP/POMDP action-state spaces;
- active inference policy spaces with witness-bearing future states;
- opportunity-set economics;
- provenance-aware reconstruction systems;
- mechanism design and access-control models;
- finality/reconstruction-debt accounting when the operation family is explicit.

The strongest finite separation is the version-control/provenance pattern:

```text
same endpoint
same coarse metrics
different retained witnesses / rights / certifications
therefore different future admissible operations
```

The strongest absorption is the same pattern:

```text
if merge bases, signed history, branch history, operation rights,
and reconstruction paths are state variables, enriched reachability
already computes the ASP split.
```

So ASP survives as a disciplined audit object, not as an independent primitive.

## 7. Recommendation

Recommendation: promote to active exploration only as a narrow formalization target. Do not promote ASP as a core claim or GU primitive.

Use this status:

```text
preserve and formalize as vocabulary/test object
```

not:

```text
abandon
```

and not:

```text
promote to canon
```

The reason is precise: the finite matched examples show useful separation from coarse baselines, but the separation is not independent of enriched prior art.

Best next formalization:

```text
ASP Typed Subpresheaf And Absorption Audit v0.2
```

with four required checks:

1. Restriction closure:

```text
if s in ASP_O(V) and U subset V, then s|_U in ASP_O(U)
```

2. Relabeling invariance:

```text
pure observer/record/task relabeling preserves ASP structure
```

3. Boundary covariance:

```text
access refinement/coarsening changes ASP only by declared boundary maps
```

4. Absorption rerun:

```text
compare ASP first against coarse baselines,
then against enriched reachability/opportunity/provenance/viability models
```

## Claim-Status Impact

No core claim should be updated.

Possible future non-canonical wording:

```text
ASP_O(U) is an observer/task-indexed admissible-future set. It is useful
for auditing future operation availability when coarse state volume,
distinguishability, finality, viability, and reachability are matched.
It is mostly absorbed by enriched reachability, opportunity-set,
provenance, and task-enriched viability formalisms.
```

Forbidden wording:

```text
ASP replaces entropy.
ASP replaces information.
ASP replaces finality.
ASP proves GU.
ASP explains consciousness.
Observers create time.
Possibility expansion is intrinsically good.
```

## Bottom Line

GU-style geometry helps define ASP more cleanly by forcing a typed section/subpresheaf discipline and by separating ambient source structure from observer-facing shadows.

It does not make ASP independent.

The live residue is operational:

```text
Which future operations are admissible for this observer, over this horizon,
given these witnesses, rights, records, reconstruction paths, and viability
constraints?
```

That is useful enough to preserve and formalize as an active exploration object. It is not strong enough to promote.

## Candidate Best Next Move

Candidate best next move: Draft `ASP Typed Subpresheaf And Absorption Audit v0.2` as an open-problem/test-spec artifact.

Reason: The goal run found a real finite separation against coarse baselines, but also found strong absorption by enriched prior art. The next useful move is to make the restriction, invariance, boundary-covariance, and absorption checks explicit.

Evidence: All three rooms converged on `ASP_O : C_O^op -> Set` or finite admissible task sets; T117 already executes matched separations; the hostile room identified opportunity sets and enriched reachability as the strongest absorbers.

Risks: The v0.2 audit may fully collapse ASP into enriched opportunity/reachability/provenance language, leaving only terminology.

What would change this recommendation: A finite or executable case where ASP predicts future operation availability while enriched reachability, enriched viability, opportunity sets, provenance, information with side channels, and finality/reconstruction-debt accounting all remain matched or less precise.
