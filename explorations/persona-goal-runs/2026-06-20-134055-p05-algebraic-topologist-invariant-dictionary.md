# P05 Run - Algebraic Topologist

- timestamp: 2026-06-20T13:40:55-05:00
- goal_id: P05
- selected_persona: Algebraic Topologist
- selected_goal: Create an invariant dictionary separating gap objects, obstruction classes, global-section failures, and auditability failures across T56-T58-T89.
- bounded_question: What is the smallest invariant dictionary that stops `T56/T58/T89` from using one word, `obstruction`, for non-equivalent failure phenomena?

## Repo Context Read

- [`/C:/Users/joe/JB/Github Repos/time-as-finality/tests/T56-sheaf-cohomology-apparent-finality.md`](/C:/Users/joe/JB/Github%20Repos/time-as-finality/tests/T56-sheaf-cohomology-apparent-finality.md)
- [`/C:/Users/joe/JB/Github Repos/time-as-finality/tests/T57-finality-reflection-property.md`](/C:/Users/joe/JB/Github%20Repos/time-as-finality/tests/T57-finality-reflection-property.md)
- [`/C:/Users/joe/JB/Github Repos/time-as-finality/tests/T58-gap-phantom-equivalence.md`](/C:/Users/joe/JB/Github%20Repos/time-as-finality/tests/T58-gap-phantom-equivalence.md)
- [`/C:/Users/joe/JB/Github Repos/time-as-finality/tests/T89-accessible-witness-gap-lemma.md`](/C:/Users/joe/JB/Github%20Repos/time-as-finality/tests/T89-accessible-witness-gap-lemma.md)
- [`/C:/Users/joe/JB/Github Repos/time-as-finality/tests/T92-accessible-witness-gap-restriction.md`](/C:/Users/joe/JB/Github%20Repos/time-as-finality/tests/T92-accessible-witness-gap-restriction.md)
- [`/C:/Users/joe/JB/Github Repos/time-as-finality/TECHNICAL-REPORT-finality-reflection-property-v0.1.md`](/C:/Users/joe/JB/Github%20Repos/time-as-finality/TECHNICAL-REPORT-finality-reflection-property-v0.1.md)
- [`/C:/Users/joe/JB/Github Repos/time-as-finality/TECHNICAL-REPORT-accessible-witness-gap-lemma-v0.1.md`](/C:/Users/joe/JB/Github%20Repos/time-as-finality/TECHNICAL-REPORT-accessible-witness-gap-lemma-v0.1.md)
- [`/C:/Users/joe/JB/Github Repos/time-as-finality/results/gap-phantom-equivalence-v0.1-results.md`](/C:/Users/joe/JB/Github%20Repos/time-as-finality/results/gap-phantom-equivalence-v0.1-results.md)
- [`/C:/Users/joe/JB/Github Repos/time-as-finality/explorations/reconstruction-failure-taxonomy.md`](/C:/Users/joe/JB/Github%20Repos/time-as-finality/explorations/reconstruction-failure-taxonomy.md)
- [`/C:/Users/joe/JB/Github Repos/time-as-finality/explorations/reconstruction-failure-h0-h1-cover-structure.md`](/C:/Users/joe/JB/Github%20Repos/time-as-finality/explorations/reconstruction-failure-h0-h1-cover-structure.md)

## Work Performed

1. Re-read the `T56 -> T57 -> T58` branch to isolate what is actually invariant and what is only supporting language.
2. Re-read `T89` and `T92` to compare the unary proposition-domain gap lane against the order-pair phantom-gap lane.
3. Cross-checked both lanes against the existing reconstruction-failure taxonomy so the dictionary would separate `H0` gaps from genuine no-global-section `H1` failures.

## Result

### 1. Minimal invariant dictionary

| Term | Meaning | Current slot |
| --- | --- | --- |
| `ambient object A(U)` | The globally fixed content restricted to patch `U`. | Shared by `T56/T58/T89`. |
| `local object F(U)` | What patch `U` can locally compute or audit. | Shared by `T56/T58/T89`. |
| `gap object G(U)=A(U)-F(U)` | Ambiently present but locally missing content at `U`. | The core `H0` object. |
| `order-gap witness` | A non-reflexive order pair in `G(U)`. | `T56/T58` lane. |
| `auditability-gap witness` | A proposition in `G(U)` whose decisive witnesses are inaccessible from `U`. | `T89` lane. |
| `global-section failure` | No compatible global section exists at all. | Not instantiated by `T56/T58/T89`. |
| `obstruction class` | A tagged failure family such as `H0_order_gap`, `H0_auditability_gap`, or `H1_no_global_section`. | The slot that prevents vocabulary collapse. |
| `restriction license` | The condition showing the chosen `G` behaves contravariantly enough to deserve gap-presheaf language. | `T57` for order pairs; `T92` for proposition gaps. |

The practical rule is:

```text
"gap object" names missing local access to ambient content.
"global-section failure" names non-existence of any compatible global assignment.
"auditability failure" names a gap caused by inaccessible decisive witnesses.
"obstruction class" is the tagged bucket, not a synonym for any one of the above.
```

### 2. Classification across `T56/T58/T89`

| Surface | Gap object | Obstruction class | Global-section failure? | Auditability failure? |
| --- | --- | --- | --- | --- |
| `T56` | Order-pair gap candidate `G(U)=A(U)-F(U)` in the sparse hidden-intermediary cover. | `H0_order_gap` after the audit; not `H1`. | No. The ambient order exists. | No in the proposition sense; the issue is missing intermediary structure, not a unary truth claim. |
| `T57` | Not a new gap family; it proves restriction closure for the `T56` gap assignment under FRP. | Guardrail / license only. | No. | No. |
| `T58` | Exact phantom-pair gap witness in the tested `T51/T52` class. | `H0_order_gap`. | No. The ambient colimit order exists. | No. |
| `T89` | Unary proposition gap with `G(U_int)={R_self_finality}`. | `H0_auditability_gap`. | No. External/global truth exists. | Yes. This is the canonical bounded-auditability failure. |

The key separation is that `T56/T58/T89` all live in the same degree-0 family, but they are
not the same object:

- `T56/T58` are order-gap instances.
- `T89` is an auditability-gap instance.
- none of them is yet a no-global-section theorem.

### 3. What should count as a genuine obstruction class here

Within this bounded slice, the only honest obstruction tags are:

```text
H0_order_gap
H0_auditability_gap
```

The tag

```text
H1_no_global_section
```

should be reserved for the explicit cyclic-cover / holonomy / contextuality lane outside this
artifact's scope. Using the bare word `obstruction` inside `T56/T58/T89` without one of these
tags invites a false upgrade from "locally missing ambient content" to "no global object exists."

### 4. Why this matters for future wording

The overloaded word `obstruction` currently hides three different questions:

1. Is some ambiently fixed content missing from a bounded local patch?
2. Is that missing content specifically missing because decisive witnesses are inaccessible?
3. Does no compatible global section exist anywhere?

`T56/T58/T89` answer only the first two. They do not answer the third.

So the strongest wording earned today is:

```text
TaF currently has a typed H0 gap dictionary with two witness families:
order gaps and auditability gaps.
```

That is narrower and cleaner than saying the branch has a single "obstruction" story.

## Blocker

There is still no single glossary or guardrail file near the gap branch itself. The
classification exists implicitly across `T57`, `T89`, `T92`, and the exploratory taxonomy
notes, which means later summaries can still blur:

- gap witness,
- auditability failure,
- and genuine no-global-section obstruction.

## Proposed Next Action

1. If a documentation pass is later authorized, add a short glossary near the `T56/T58/T89/T92`
   lane with the three tags `H0_order_gap`, `H0_auditability_gap`, and `H1_no_global_section`.
2. Use this tagging discipline in later LossKernel / reconstruction-debt work so "obstruction"
   does not silently move between missing witness access and genuine global inconsistency.

## Claim-Status Posture

- No claim-status changes recommended.
- Positive narrowing: `T56/T58/T89` support a typed `H0` gap dictionary, not a single undifferentiated obstruction theorem.
- Negative guardrail: none of the bounded `T56/T58/T89` witnesses should be summarized as a no-global-section `H1` failure.
