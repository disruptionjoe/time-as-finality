# T89: Accessible Witness Gap Lemma

## Route

Quantum measurement / classical records.

## Target Line

T60 + T19 + T58

## Question

Can the T19 first-person / third-person separation be represented as an H0 gap
instance with explicit ambient object `A`, local object `F`, and gap object
`G = A - F`, without overclaiming that it is literally the same presheaf as the
T58 phantom-order program?

## Motivation

T60 supplies self-closure. T19 supplies non-self-verifiability. T58 supplies a
working degree-0 gap formalism for "globally present, locally missing" content.

The open issue is precision. T58 uses ordered event pairs. T19 uses unary
finality propositions such as `R_self_finality`. A useful unification must keep
the common H0 structure while not pretending the section objects are identical.

## Construction

Use the T19 witness graph with:

- internal patch `U_int`: observer `R` at `e_R_final` with accessible holders
  `A*(R)`;
- external patch `U_ext`: third-person verifier at `e_meta` with full holder
  access.

Define a finite proposition domain over R's state:

```text
P_R = { R_obs, R_self_finality }
```

Define:

1. `A(U)` = ambiently true propositions in `P_R` whose truth is fixed by the
   full graph and restricted to patch `U` as propositions about `R`;
2. `F(U)` = propositions in `P_R` that are internally auditable at `U` by the
   observer anchored at `U` using only its accessible holders and causal past;
3. `G(U) = A(U) - F(U)`.

For the T19 witness:

- `A(U_int) = {R_obs, R_self_finality}`;
- `F(U_int) = {R_obs}`;
- `G(U_int) = {R_self_finality}`;
- `A(U_ext) = F(U_ext) = {R_obs, R_self_finality}`;
- `G(U_ext) = empty`.

## Lemma Target

```text
Accessible Witness Gap Lemma (finite witness form).

If proposition p about observer O is ambiently true in the full graph, but all
decisive witness records for p lie outside O's accessible causal region at patch
U, then p belongs to the degree-0 gap object G(U) = A(U) - F(U).
No computation internal to O at U can remove p from G(U) without changing
accessibility or importing new witness records.
```

## Success Criteria

- T19 is translated into explicit `A`, `F`, and `G` objects.
- `F(U) subset A(U)` holds in the witness family.
- `R_self_finality` appears in `G(U_int)` and not in `G(U_ext)`.
- The statement is explicitly narrower than "T19 is the same presheaf as T58."
- The artifact states what is shared with T58 and what is not.

## Failure Criteria

- `A(U_int)` cannot be defined without sneaking in the desired answer.
- `F(U)` is not a subobject of `A(U)` in the witness family.
- The gap depends on post hoc semantic relabeling rather than witness
  accessibility.
- The artifact claims a full theorem-level equivalence with T58's order-pair
  gap program.

## Expected Result

T19 should fit the T58 branch only at the level of H0 failure shape:

- global content exists;
- local auditable content is a subobject;
- the missing part is represented by a degree-0 gap object.

But T19 should remain a distinct unary witness-gap instance, not a literal
phantom incomparability theorem.
