# T221: Coherent Section Functoriality Verdict (FUNCTOR-OBL-TaF-001)

## Target Claims

- `FUNCTOR-OBL-TaF-001` (`open-problems/functor-obl-taf-001-coherent-section-functor.md`)
- `PO1-NCK-001` (`tests/T188-po1-nck-formal-claim-and-cap-ti-step4.md`,
  `explorations/explorer-nck-formal-definitions-2026-06-22.md`)
- MTI (`claims/MTI-metabolic-temporal-irreducibility.md`)
- T41 (Typed Transport Category — PO1 non-functor result)
- T190 / T191 / T192 (coherent-section base cases, restricted functoriality,
  lambda* derivation)

## Origin

`FUNCTOR-OBL-TaF-001` is the named blocking obligation for BOTH the PO1-NCK
formal connection and the MTI claim. The obligation asks whether

```text
F : States(Ext_S) -> FinSets
F(S) = set of globally coherent sections at state S
F(e) : F(S) -> F(S')   for an admissible extension e : S -> S'
```

is a genuine functor:

```text
F(id_S) = id_{F(S)}            (identity preservation)
F(e2 o e1) = F(e2) o F(e1)     (composition preservation)
```

T190 found the covariant statement "narrowed, not verified": extensions can
delete coherent sections, so `F(e)` need not be a total function. T191 found
that the only clean covariant `FinSets` repair (the section-preserving
subcategory `SectPres(Ext_S)`) is functorial but dynamically sterile
(`N = K = 0`). T192 narrowed PO1-NCK-001 to `PO1 => K`, not `PO1 => lambda*(S)`.

What T190-T192 did NOT do is render a closed verdict on functoriality itself:
T190 *proposed* the contravariant reading `F_op : States(Ext_S)^op -> FinSets`
as the canonical surviving object but never proved it is a functor, and never
recorded what a proven contravariant functor does to the two downstream claims
that asked for a *covariant* one. T221 closes the obligation by (a) giving an
explicit counterexample to the covariant functor in the locus where it fails,
and (b) proving the contravariant functor, then (c) propagating both results to
PO1-NCK-001 and MTI.

This is a pure categorical structure theorem in the style of T41 and T190. The
witnesses are finite restriction-system fixtures stated inline; no executable
model is required and none is claimed (`finite_witness`, per COMPLEXITY-LEDGER).

## Setup

Work in the finite binary same/different restriction systems of T28/T39. A
state `S = (T_S, A_S)` is a finite constraint set over signed variables in
`{-1, +1}`. A globally coherent section `sigma in F(S)` is a total assignment
satisfying every constraint in `T_S` with `A_S(sigma) = 1` and no PO1 gluing
obstruction. An admissible extension `e : S -> S'` adds one or more new
constraints, so the constraint set grows monotonically:
`T_S subseteq T_{S'}`.

The decisive structural fact, already implicit in the definition of `F` and in
T34's endpoint determination, is monotone constraint accumulation:

```text
(MA)  e : S -> S' admissible  =>  T_S subseteq T_{S'}
      and therefore F(S') subseteq F(S)  (more constraints can only remove
      sections, never add them).
```

(MA) is the hinge for the entire verdict. It is the reason the covariant
`FinSets` functor fails and the contravariant one succeeds.

### Fixture set (reused from T190, restated for self-containment)

```text
S0 : no constraints
     F(S0) = { (+1,+1), (+1,-1), (-1,+1), (-1,-1) }          |F(S0)| = 4
e1 : add x_A = x_B
     F(S1) = { (+1,+1), (-1,-1) }                            |F(S1)| = 2
e2 : add x_A = +1
     F(S2) = { (+1,+1) }                                     |F(S2)| = 1
e_bad : add x_A = -x_B  to S2-with-predicates P_A={+1}, P_B={+1}
     F(S_bad) = {}                                           |F(S_bad)| = 0
```

## Part I — Covariant Functor: REFUTED (explicit counterexample)

**Claim under test (covariant):** `F : States(Ext_S) -> FinSets` with
`F(e) : F(S) -> F(S')` sending each section to its forward extension.

**Counterexample object/morphism (failing morphism named):**

```text
Object:   S2 with F(S2) = { (+1,+1) }            (a one-element set, the FinSets object 1)
Morphism: e_bad : S2 -> S_bad,  add x_A = -x_B
Image:    F(S_bad) = {}                          (the FinSets object 0)
```

`F(e_bad)` would have to be a function `F(S2) -> F(S_bad)`, i.e. a function
`1 -> 0` in `FinSets`. **No such function exists** (`Hom_FinSets(1, 0) = empty`).

**Where functoriality fails — precise locus.** The failure is NOT in identity
preservation and NOT in composition preservation. It is upstream of both: `F`
is not a well-defined object map into the *morphisms* of `FinSets`. The proposed
arrow `F(e_bad)` has no value at all. Concretely:

- Fixture B (selective survival) shows `F(e1)` is non-total: the source sections
  `(+1,-1)` and `(-1,+1)` of `F(S0)` have no image in `F(S1)` (they are deleted
  by the new constraint, not mapped anywhere). A non-total assignment is not a
  `FinSets` morphism.
- Fixture C / `e_bad` shows the strictly stronger typing failure: even when the
  source is the terminal-looking singleton, the codomain is empty, so the
  hom-set that `F(e_bad)` must inhabit is itself empty.

This is the standard reason feasible-solution-set assignments are not covariant
under constraint addition. It is the same shape as T41's result that PO1 is not
a Boolean functor on the D1 morphism category: the morphism-level action of a
solution-set-valued construction does not respect the forward arrow.

**Verdict I:** `F : States(Ext_S) -> FinSets` (covariant) is **not a functor**.
The failing object is `S_bad` (empty section set) reached by the failing
morphism `e_bad : S2 -> S_bad`; the failing functor law is *being a morphism map
at all* (totality / codomain typing), which logically precedes both identity and
composition preservation. This refutes the covariant reading on which the NCK
definitions and PO1-NCK-001 were stated.

## Part II — Contravariant Functor: PROVEN

**Theorem (T221).** Define `F_op : States(Ext_S)^op -> FinSets` by:

```text
on objects:    F_op(S) = F(S)  (the finite set of globally coherent sections)
on morphisms:  for e : S -> S' in States(Ext_S), the opposite arrow
               e^op : S' -> S in States(Ext_S)^op is sent to the inclusion
               iota_e : F(S') ->  F(S),  iota_e(sigma) = sigma.
```

`F_op` is a genuine functor `States(Ext_S)^op -> FinSets`.

**Proof.**

*(0) Well-typed on objects.* `F(S)` is a finite set for every finite state `S`
(finitely many assignments over finitely many signed variables). So `F_op(S)`
is an object of `FinSets`.

*(1) Well-typed on morphisms (totality, the exact thing Part I lacked).* For any
admissible `e : S -> S'`, (MA) gives `F(S') subseteq F(S)`. The set-theoretic
inclusion `iota_e : F(S') -> F(S)`, `sigma |-> sigma`, is therefore a total,
well-defined function. The covariant failure (`1 -> 0` impossible) does not
arise here: in the contravariant direction the empty set sits in the *domain*,
and `iota : {} -> F(S)` is the unique (vacuous) empty function, which always
exists in `FinSets`. The typing failure of Part I is exactly cured by reversing
the arrow.

*(2) Identity preservation.* `id_S : S -> S` adds no constraints, so
`F(S) subseteq F(S)` with the inclusion equal to `id_{F(S)}`. Hence
`F_op(id_S^op) = iota_{id_S} = id_{F(S)} = id_{F_op(S)}`.

*(3) Composition preservation.* Let `e1 : S -> S'` and `e2 : S' -> S''`. In
`States(Ext_S)^op` the composite of `e2^op : S'' -> S'` then `e1^op : S' -> S`
is `(e2 o e1)^op : S'' -> S`. By (MA),
`F(S'') subseteq F(S') subseteq F(S)`, and the three inclusions are ordinary
subset inclusions. Set inclusions compose strictly:

```text
iota_{e1} o iota_{e2} : F(S'') -> F(S'') ->[id] ... = the inclusion F(S'') -> F(S)
                      = iota_{e2 o e1}.
```

Because every map involved is "send sigma to sigma," composing them is the
identity-on-elements map from the smallest set to the largest, which is exactly
the inclusion assigned to the composite. Hence
`F_op((e2 o e1)^op) = F_op(e1^op) o F_op(e2^op)`, the contravariant
composition law. (Equivalently: `F_op` is the restriction-of-solutions
construction, which is the canonical contravariant powerset-monotone functor for
any monotonically growing constraint set.)

*(4) Witness check on the fixtures.* With
`F(S2) = {(+1,+1)} subseteq F(S1) = {(+1,+1),(-1,-1)} subseteq F(S0) (all four)`:

```text
iota_{e2} : F(S2) -> F(S1)          (+1,+1) |-> (+1,+1)
iota_{e1} : F(S1) -> F(S0)          each section |-> itself
iota_{e1} o iota_{e2} : F(S2) -> F(S0)   (+1,+1) |-> (+1,+1)
iota_{e2 o e1} : F(S2) -> F(S0)          (+1,+1) |-> (+1,+1)   EQUAL.
```

And through the obstruction, `F(S_bad) = {}`:
`iota : {} -> F(S2)` is the empty function and composes correctly with any
further inclusion, since the empty function is initial. No typing failure
appears. QED.

**Verdict II:** `F_op : States(Ext_S)^op -> FinSets` **is a functor**
(identity and composition preserved; morphism action total because
restriction-of-solutions is canonically contravariant).

## Part III — Resolution of FUNCTOR-OBL-TaF-001

FUNCTOR-OBL-TaF-001 is hereby **resolved by a directional split**:

```text
F  : States(Ext_S)    -> FinSets   is NOT a functor   (Part I, counterexample e_bad)
F_op : States(Ext_S)^op -> FinSets is     a functor   (Part II, proof)
```

The obligation is discharged in the sense of being *settled*: there is now a
proven functor (the contravariant one) and an explicit counterexample ruling out
the covariant one. But the direction that is functorial is the *opposite* of the
direction the PO1-NCK and MTI program required. This is the load-bearing finding
and the reason the cascade below is a re-scope, not a green light.

**Why the direction matters.** The NCK dynamics are forward-in-issuance:
`N = d|F(S)|/dt` (sections appearing as the state evolves under issuance) and
`K = lambda * |F(S)| * p_obs` (sections being destroyed by obstruction as the
state advances). Both are statements about how `|F(S)|` changes as `S` moves
*forward* along admissible extensions — the covariant direction. The proven
functor `F_op` runs the other way (stricter -> looser), so it transports
sections backward and cannot, on its own, type a forward growth/destruction
rate. The section-preserving covariant repair `SectPres` that *is* covariant is
the one T191 already showed is sterile (`N = K = 0`).

So the honest categorical posture after T221 is:

```text
- The coherent-section construction is a well-defined contravariant FinSets
  functor (Part II).
- It is NOT a covariant FinSets functor (Part I).
- Neither functorial form supplies a covariant, dynamically non-trivial
  FinSets functor. The forward issuance dynamics (N, K) are therefore NOT
  carried by a FinSets functor at all; at best they live in a partial-map /
  relation-valued covariant assignment F_partial : States(Ext_S) -> ParSets,
  which is not the object PO1-NCK-001 was stated over.
```

## Success Criteria

1. Covariant `F` refuted by an explicit failing object/morphism in `FinSets`
   (`S_bad`, `e_bad`, hom-set `Hom(1,0) = empty`). MET (Part I).
2. Contravariant `F_op` proven a functor: object map well-typed, morphism map
   total via (MA), identity preserved, composition preserved. MET (Part II).
3. The failing functor law for the covariant case is named precisely (morphism
   totality / codomain typing, prior to identity and composition). MET.
4. Cascade to PO1-NCK-001 and MTI recorded with direction (Part IV). MET.

## Failure Criteria

- If (MA) fails — i.e. some admissible extension *adds* a coherent section that
  was not present before — then `F(S') subseteq F(S)` is false, `F_op`'s
  inclusion is not well-defined, and Part II collapses. (MA) holds because
  admissible extensions only add constraints; an extension that could create new
  sections would have to *remove* a constraint, which is not an `Ext_S` morphism.
  This is the single load-bearing assumption and is recorded as the falsifier.
- If a future `Ext_S` morphism class is defined that both deletes constraints
  and preserves admissibility, both verdicts must be re-derived.
- If `F_partial : States(Ext_S) -> ParSets` is given full partial-functor
  semantics and shown to carry non-trivial `N`/`K`, then PO1-NCK-001 may be
  re-promotable over `ParSets` (not over `FinSets`); T221 does not close that
  door, it only closes the `FinSets`-covariant door.

## Part IV — Cascade to PO1-NCK-001 and MTI

**PO1-NCK-001: DEMOTED / RE-SCOPED.** PO1-NCK-001 was stated over the covariant
`F : States(Ext_S) -> FinSets` and carried an implicit covariant functoriality
assumption. Part I shows that assumption is false: there is no covariant
`FinSets` functor. Combined with T192 (`PO1 => K`, not `PO1 => lambda*(S)`), the
maximal honest surviving statement is:

```text
PO1 natively types the obstruction term K(lambda,S) = lambda * |F(S)| * p_obs(S),
where |F(S)| is read off the (contravariant-functorial, T221 Part II) coherent
section set. PO1 does NOT, via any FinSets functor, derive the interior optimum
lambda*(S): the gain term N and the cost term C require the covariant forward
direction, which is not FinSets-functorial.
```

PO1-NCK-001 stays `candidate` but is re-scoped from "lambda*(S) is a consequence
of PO1" down to "K is a PO1-native obstruction term; lambda*(S) is a mixed
dynamics object not derivable from PO1 alone." The FUNCTOR-OBL-TaF-001 blocker is
removed by *resolution-as-refutation*: it is no longer "pending verification," it
is settled, and the settlement removes (does not supply) the support leg
PO1-NCK-001 needed.

**MTI: UNCHANGED (stays PARTIALLY_SUPPORTED).** MTI's positive evidence
(T184 mu_M superadditivity vs entropy subadditivity; T185 three TaF-specific
MSY residues; T186/T187 beta(Beta) > beta(Alpha) for identical causal order;
T188 G encodes topology but not timing) **never depended on covariant
functoriality of F.** Those results are about whether the branching exponent
beta carries metric-temporal information not in causal order — a question
settled by the delivery-time fixtures, independent of how `F` behaves on
morphisms. Therefore the FUNCTOR-OBL-TaF-001 blocker on MTI is **discharged**
(resolved, no longer open) without changing MTI's status: it neither promotes nor
demotes MTI. The two MTI blockers FUNCTOR-OBL-TaF-001 and PO1-NCK-001 are now
*settled*, leaving MTI's only remaining open blocker the exact WBE continuum
derivation. MTI does not promote past PARTIALLY_SUPPORTED on T221 because T221
adds no new metric-vs-causal evidence; it only clears two formal blockers by
resolving them rather than by satisfying them.

## Known Physics Constraints

None directly. T221 is a finite categorical structure theorem about the
coherent-section construction over `States(Ext_S)`. No curvature, gravity,
torsion, connection, or geometry language is introduced. No scale or hardness
claim is made; the witnesses are finite fixtures (`finite_witness`). The result
honors the absorber posture: the canonical absorber for "feasible-solution sets
under added constraints are contravariant, not covariant" is ordinary category
theory (as flagged in T190's absorber pass), and T221 explicitly does NOT claim
a novel categorical obstruction — it claims a clean directional verdict that
closes a named obligation.

## Contribution Needed

- Decide whether `F_partial : States(Ext_S) -> ParSets` (covariant partial-map)
  is worth formalizing as the carrier of forward `N`/`K` dynamics, or whether
  the PO1-NCK line should be retired to "K-only" status permanently.
- If `F_partial` is pursued: state its identity and composition laws under
  partial-function composition and check whether `N` and `C` become typable
  there (T192's open question, now the only live promotion path for lambda*(S)).
- Confirm (MA) is preserved by every existing and future `Ext_S` morphism class;
  flag any constraint-removing morphism as a falsifier of T221 Part II.
