# T221 Results: Coherent Section Functoriality Verdict (FUNCTOR-OBL-TaF-001)

## Outcome

`FUNCTOR-OBL-TaF-001` is **resolved by a directional split**, not discharged in
the program's favor.

```text
F  : States(Ext_S)    -> FinSets   is NOT a functor   (counterexample)
F_op : States(Ext_S)^op -> FinSets is     a functor   (proof)
```

The direction that is functorial (contravariant) is the opposite of the
direction PO1-NCK-001 and the NCK dynamics required (covariant). The obligation
is therefore *settled*, and the settlement removes a support leg rather than
supplying one.

## Verdict Table

| Question | Verdict | Where it fails / holds |
| --- | --- | --- |
| Covariant `F : States(Ext_S) -> FinSets` a functor? | **NO** | Morphism map not total: `F(e_bad)` would be `1 -> 0` in FinSets, hom-set empty. Failure precedes identity/composition laws. |
| Identity preservation (covariant) | n/a | `F(id_S) = id` holds in isolation but is moot once the morphism map fails to exist. |
| Composition preservation (covariant) | n/a | Never reached; `F(e)` is not a morphism for obstruction-creating `e`. |
| Contravariant `F_op : States(Ext_S)^op -> FinSets` a functor? | **YES** | Inclusion `F(S') subseteq F(S)` total by monotone constraint accumulation (MA); identity and composition preserved. |
| A covariant, dynamically non-trivial FinSets functor exists? | **NO** | Covariant fails (this test); section-preserving covariant repair is sterile, `N=K=0` (T191). |

## Failing Object / Morphism (named, per governance)

```text
Failing object:   S_bad  with  F(S_bad) = {}        (FinSets object 0)
Failing morphism: e_bad : S2 -> S_bad,  adds x_A = -x_B
Source:           F(S2) = {(+1,+1)}                 (FinSets object 1)
Obstruction:      Hom_FinSets(1, 0) = empty  =>  F(e_bad) has no value.
Failing law:      morphism-map totality / codomain typing
                  (logically prior to identity and composition preservation).
```

## Proof Summary (contravariant)

Monotone constraint accumulation (MA): an admissible extension `e : S -> S'`
only adds constraints, so `F(S') subseteq F(S)`. Sending `e^op : S' -> S` to the
set inclusion `iota_e : F(S') -> F(S)` gives:

- well-typed objects (finite section sets);
- total morphism maps (inclusions, including the always-existing empty function
  `{} -> F(S)` — the codomain-typing failure of the covariant case is cured by
  reversing the arrow);
- identity preserved (`iota_{id_S} = id_{F(S)}`);
- composition preserved (set inclusions compose to the inclusion of the
  composite: `iota_{e1} o iota_{e2} = iota_{e2 o e1}`).

This is the canonical contravariant restriction-of-solutions functor. Verified
on the T190 fixtures: `F(S2) subseteq F(S1) subseteq F(S0)` with element-wise
identity inclusions composing correctly, and `F(S_bad) = {}` composing as the
initial empty function.

## Cascade

| Claim | Status change | Reason |
| --- | --- | --- |
| **PO1-NCK-001** | `candidate` -> `candidate (re-scoped, FUNCTOR-OBL resolved-by-refutation)` | Covariant functor it assumed does not exist. With T192 (`PO1 => K` only), surviving statement is "K is a PO1-native obstruction term read off the contravariant section count; lambda*(S) is a mixed object PO1 does not derive." Blocker resolved, not satisfied. |
| **MTI** | `partially_supported` (UNCHANGED) | T184-T188 metric-vs-causal evidence never depended on covariant functoriality. Both FUNCTOR-OBL-TaF-001 and PO1-NCK-001 blockers are now *settled*; only the exact WBE continuum derivation remains open. No new metric evidence, so no promotion. |
| **FUNCTOR-OBL-TaF-001** | open -> **resolved (directional split)** | Counterexample (covariant) + proof (contravariant). |

## Repo-Safe Reading

```text
The coherent-section construction is a contravariant FinSets functor and not a
covariant one. The forward issuance dynamics (N, K growing with the state) are
not carried by any FinSets functor; if anywhere, they live in a covariant
partial-map object F_partial : States(Ext_S) -> ParSets, which is not the
object PO1-NCK-001 was stated over. PO1 still natively types K; it does not
type lambda*(S). MTI stands on its independent T184-T188 evidence.
```

## What This Changes

- Stop citing FUNCTOR-OBL-TaF-001 as an *open* blocker; cite it as *resolved by
  directional split* (covariant refuted, contravariant proven).
- Stop stating PO1-NCK-001 as "lambda*(S) is a consequence of PO1"; the warranted
  form is "K is a PO1-native obstruction term; lambda*(S) is mixed dynamics."
- The only live promotion path for lambda*(S) is now `F_partial` over `ParSets`
  with `N`/`C` typed there (T192's open question); `FinSets` is closed for the
  forward dynamics.
- MTI's blocker list reduces to a single open item: exact WBE continuum
  derivation.

## Falsification Conditions

- T221 Part II (the contravariant functor) fails if any admissible `Ext_S`
  morphism is shown to *add* a coherent section (violating MA). No current
  morphism class does so, because `Ext_S` morphisms only add constraints.
- The cascade re-scoping of PO1-NCK-001 is reversed only if `F_partial` over
  `ParSets` is given full partial-functor semantics that carry non-trivial,
  PO1-derived `N` and `C` — at which point PO1-NCK-001 may be re-promotable over
  `ParSets` (never over covariant `FinSets`).

## Method / Status

Pure finite categorical structure theorem in the style of T41 and T190; finite
inline witness fixtures; no executable model. Computational status:
`finite_witness`. No scale, hardness, or geometry language introduced.
