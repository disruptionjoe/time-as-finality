# Technical Report: Accessible Witness Gap Lemma v0.1

## Claim Under Test

The active T60 + T19 + T58 line aims to determine whether the phenomenal-bridge
thread can be turned into a publishable formal result. The concrete question is
whether T19 is genuinely an H0 gap-instance in the same sense that T58 captures
phantom incomparability by a gap object `G = A - F`.

The risk is overreach. T58 works with ordered event pairs. T19 works with unary
finality propositions about one observer. This report tests the strongest
honest unification.

## Result

T19 does fit the T58 program at the level of H0 failure shape, but not as the
same section object.

The right statement is:

```text
T19 is a unary accessible-witness gap instance.
T58 is an order-pair phantom-gap instance.
They share the same degree-0 local-to-global failure pattern:
ambiently true content exists, locally auditable content is a proper subobject,
and the missing part is represented by G = A - F.
```

What is shared is the H0 structure. What differs is the kind of section:

- T58 sections are non-reflexive order pairs;
- T19 sections are truth-valued self-finality propositions.

## Explicit A / F / G Translation For T19

Fix the T19 witness graph and proposition domain

```text
P_R = { R_obs, R_self_finality }.
```

Let:

- `U_int` be the bounded observer patch for `R` at `e_R_final` with accessible
  holders `A*(R)`;
- `U_ext` be the external patch at `e_meta` with full holder access.

Define:

```text
A(U) = propositions in P_R whose truth about R is fixed by the full graph
       when restricted to patch U as a proposition-domain question.

F(U) = propositions in P_R that are auditable at U using only witnesses in the
       observer's accessible holders and causal past.

G(U) = A(U) - F(U).
```

For the finite T19 witness:

```text
A(U_int) = {R_obs, R_self_finality}
F(U_int) = {R_obs}
G(U_int) = {R_self_finality}

A(U_ext) = {R_obs, R_self_finality}
F(U_ext) = {R_obs, R_self_finality}
G(U_ext) = empty
```

This gives the exact T19 separation:

```text
global / external verdict = YES
local / internal verdict  = NO
```

without claiming that the internal patch lacks self-related structure entirely.
T60 already showed the opposite: closure exists.

## Why This Is An H0 Gap

The T19 witness is not an H1 contextuality obstruction.

- The relevant cover is nested: `U_int subset U_ext`.
- The global truth exists.
- The failure is that one locally bounded patch cannot access the decisive
  witnesses for a true proposition.

So the missing content is degree-0:

```text
there exists a section in the ambient object
that is absent from the local auditable object.
```

That is exactly the H0 pattern already isolated by T56-T58, even though the
section language here is unary rather than order-theoretic.

## Accessible Witness Gap Lemma

The strongest lemma currently earned is:

```text
Accessible Witness Gap Lemma (finite witness form).

Let O be a bounded observer at patch U, and let p be a proposition about O.
Suppose:
1. p is ambiently true in the full graph;
2. every witness decisive for p lies outside O's accessible causal region at U;
3. F(U) contains exactly those propositions auditable from O's accessible
   holders and causal past.

Then p belongs to the degree-0 gap object G(U) = A(U) - F(U).
Moreover, no computation internal to O at U can move p from G(U) into F(U)
without a change in accessible witness structure.
```

For T19, `p = R_self_finality`.

## What This Strengthens

This gives the T60 + T19 + T58 line a cleaner mathematical target:

1. T60 is the positive existence side: self-related closure can exist.
2. T19 is the bounded-auditability failure side: a true proposition about that
   closure can remain locally unauditable.
3. T58 provides the right language for the missing content: a degree-0 gap
   object, not necessarily an H1 obstruction.

That is publishable in principle because it is precise, falsifiable, and does
not depend on solving consciousness.

## What This Does Not Yet Prove

This report does not prove:

- that T19 and T58 instantiate one identical presheaf;
- that every phenomenal-bridge gap can be encoded as `G = A - F`;
- that the T19 gap object already has a full restriction theory matching T57;
- that the result is a general theorem beyond the finite witness family.

Those are still open.

## Main Boundary

The T58 suborder condition has no literal copy in T19 because T19 sections are
not ordered pairs. The closest analogue is only:

```text
F(U) subset A(U)
```

for the proposition-domain witness family.

So the current result is a narrower theorem candidate than full T19/T58
identity:

```text
same H0 failure form,
different section objects.
```

## Best Next Move

The next serious theorem step is to define restriction maps for the T19
proposition-domain gap object and test whether a T57-style closure statement is
true:

```text
if V subset U, does G(U) restrict into G(V)?
```

If yes, the T19 branch joins the T56-T58 gap program more tightly.
If no, the correct final result is narrower: an Accessible Witness Gap Lemma
without a full gap-presheaf theorem.
