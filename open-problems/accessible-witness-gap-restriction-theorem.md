# Accessible Witness Gap Restriction Theorem

## Status

Open theorem target. This file turns the T19/T58 item from the 2026-06-20
all-persona review into an explicit ambitious goal.

## Why This Is The Neglected One

The active queue has five items:

1. LossKernel separation/collapse test.
2. T90 weak-measurement platform instantiation.
3. T87 real-run detector feasibility audit.
4. H7 entropy-accounting hard case.
5. T19/T58 gap restriction maps.

The first four sit in obvious research lanes: formal math paper, Q1
measurement, detector protocol, and thermodynamic arrow. The fifth is easiest
to neglect because it touches the phenomenal-bridge vocabulary. The goal here
is to keep it theorem-shaped and prevent it from becoming philosophy prose.

## Ambitious Goal

Prove or refute a restriction theorem for the T19 proposition-domain gap object.

Target statement:

```text
Accessible Witness Gap Restriction Theorem.

Let U be an observer patch and V subset U a smaller accessible patch. Let P_O
be a finite proposition domain about observer O. Define:

A(U) = propositions in P_O whose truth is fixed by the full record graph when
       restricted to U as a proposition-domain question.

F(U) = propositions in P_O auditable at U using only accessible holders and
       causal-past witnesses.

G(U) = A(U) - F(U).

Under explicit witness-monotonicity and proposition-restriction conditions,
restriction sends G(U) into G(V).
```

If true, T19 becomes more than an isolated finite witness: it joins the T56-T58
gap program as a unary accessible-witness gap object with restriction closure.

If false, the result is still valuable: T19 remains a finite Accessible Witness
Gap Lemma, but not a gap-presheaf theorem. That would prevent overclaim and
keep the phenomenal bridge narrow.

## Definitions To Build

### Patch

A patch is a bounded observer-access region:

```text
U = (events_U, holders_U, causal_past_U)
```

with restriction `rho_{U->V}` when `V subset U`.

### Proposition Domain

For T19, the minimal proposition domain is:

```text
P_R = {R_obs, R_self_finality}
```

The general target allows finite `P_O`, but the first theorem should not exceed
the two-proposition T19 domain unless the proof needs it.

### Ambient Proposition Object

`A(U)` contains propositions whose truth about `O` is fixed by the full graph,
restricted to the question expressible at `U`.

This must not smuggle in first-person access. `A(U)` is ambient/third-person.

### Auditable Proposition Object

`F(U)` contains propositions whose witnesses lie inside `U`'s accessible
holders and causal past.

This is the local/first-person audit object.

### Gap Object

```text
G(U) = A(U) - F(U)
```

For the T19 witness:

```text
G(U_int) = {R_self_finality}
G(U_ext) = empty
```

## Needed Conditions

The theorem should make every condition explicit. Candidate conditions:

1. **Ambient restriction:** if a proposition is ambiently true at `U`, its
   restriction is ambiently true at `V` when the proposition remains expressible
   at `V`.
2. **Audit monotonicity:** if `V subset U`, every witness auditable at `V` is
   also auditable at `U`.
3. **No semantic relabeling:** restriction cannot identify
   `R_self_finality` with `R_obs` unless that identification is declared as a
   collapse condition.
4. **Witness locality:** `F(U)` is determined only by witnesses in `U`, not by
   external knowledge of the full graph.
5. **Stable proposition typing:** propositions have typed witness conditions;
   they are not free-text semantic labels.

## Expected Theorem Shape

The theorem is likely not:

```text
G is always a presheaf for arbitrary proposition assignments.
```

The safer expected result is:

```text
For finite T19-style accessible-witness systems satisfying audit monotonicity
and stable proposition typing, the gap assignment restricts contravariantly:
rho_{U->V}(G(U)) subset G(V).
```

The theorem should also include a counterexample showing why the conditions
are necessary.

## Failure Modes

The ambitious goal fails, usefully, if any of these occur:

- `G(U)` restricts to a proposition that becomes auditable in `V`.
- proposition restriction is not well-defined without extra semantic choices;
- `A(U)` changes with patch in a way that is not functorial;
- `F(V) subset rho(F(U))` fails for a legitimate nested witness system;
- the only way to make closure true is to define `F` or `G` circularly.

Any failure should produce a named obstruction, not a vague "phenomenal gap."

## First Executable Target

Add a test track, tentatively:

```text
T92: Accessible Witness Gap Restriction
```

Minimum model:

1. Reuse the T19 seven-node witness.
2. Define nested patches `U_int subset U_mid subset U_ext`.
3. Define typed propositions and their witness requirements.
4. Compute `A(U)`, `F(U)`, and `G(U)` for each patch.
5. Check `rho_{U->V}(G(U)) subset G(V)` for all nested pairs.
6. Include at least one hostile semantic-relabeling control and one
   witness-monotonicity violation control.

## Success Criteria

- The T19 witness satisfies the restriction theorem.
- At least one non-chain witness satisfies it, so the result is not just the
  original graph restated.
- At least one control fails, proving the theorem uses real hypotheses.
- The result explicitly says whether T19 joins the T56-T58 gap-presheaf
  program or remains a narrower finite lemma.

## Claim Impact If Successful

C1 may be sharpened, not upgraded:

```text
The first-person/third-person finality gap has a finite degree-0
accessible-witness form with restriction closure for typed proposition-domain
witness systems.
```

Do not claim:

- a solution to consciousness;
- a complexity-class separation;
- a general H1/cohomology theorem;
- identity between T19 proposition gaps and T58 order-pair gaps.

## Claim Impact If Refuted

If restriction closure fails, weaken the branch:

```text
T19 is an isolated Accessible Witness Gap Lemma. It shares H0 failure shape
with T58 but does not define a gap-presheaf object under the tested
restriction maps.
```

That would still be progress because it prevents the phenomenal/gap bridge
from overreaching.

## Suggested Next Run

Implement T92 as the minimal executable theorem/refutation target. The run
should produce:

- `models/accessible_witness_gap_restriction.py`;
- `tests/test_accessible_witness_gap_restriction.py`;
- `tests/T92-accessible-witness-gap-restriction.md`;
- `TECHNICAL-REPORT-accessible-witness-gap-restriction-v0.1.md`;
- JSON/Markdown results.

The key acceptance question:

```text
Does the T19 proposition-domain gap object actually restrict like the T57
gap object, or was the all-persona review right to keep it as a neglected
but risky bridge?
```

## Status Addendum (2026-07-07): typed-gap bridge outcome

T92 implemented the minimal restriction theorem target. T492 then tested the
remaining bridge question against T113:
`results/T492-typed-gap-category-bridge-v0.1-results.md`.

Verdict:
`COMMON_TYPED_GAP_SCHEMA_SUPPORTED_OBJECT_IDENTITY_BLOCKED`. The T19/T92
proposition-domain gap and the T58/T113 order-pair phantom gap share a common
finite typed-gap schema, but not object identity. The schema is:

```text
patches + A(U) + F(U) + G(U)=A(U)-F(U) + typed predicate tau + restriction
```

The T19 branch therefore joins the T56-T58 gap program only as a typed-gap
schema instance. It remains distinct from T58 order-pair phantom gaps and still
does not prove a consciousness, cohomology, or complexity-class theorem. Future
work would need actual morphisms between typed gap systems, not just another
same-shape finite witness.
