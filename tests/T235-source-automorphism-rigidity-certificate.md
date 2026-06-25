# T235: Source-automorphism rigidity certificate

## Verdict: no-go (route (b) NOT cleared; route (a) bounded subsumption STRENGTHENED to the structure-keyed stratum)

The one untested crack T230 named in the absorption-escape trichotomy -- the
source-automorphism rigidity certificate, keyed to a source-side **symmetry
class** rather than to the **value** of any source field -- is now built and
tested, and it is **closed at gate 2**. The certificate genuinely separates a
same-`nu` pair (gate 1 passes: rigid vs symmetric source gluing give different
automorphism iso-class while `nu` is identical), is local and relabeling-stable
(gates 3a/3b pass by construction, exactly as T230 predicted), and is NOT
absorbed by admitting the source **field value** (`nu'`). But the source-side
**gluing** that the automorphism group is computed from is itself admissible
audit data (T108/T127: mature neighbors absorb any declared source structure once
named), and admitting it as audit data (`nu_struct`) reproduces the separation.
The automorphism iso-class is a **derived function of an admissible source
relation**, so it is absorbed one level up -- the same fate as T230's
`source_reading`, now keyed to a structure rather than a scalar.

The structural bet that "a symmetry class has no single field to admit" is
therefore **false on this construction**: the gluing IS the admissible carrier.
This does NOT flip independent-motivation to EARNED; it STRENGTHENS the T230
route-(a) bounded negative by extending the trichotomy's gate-2 closure from
field-valued source separators to structure-valued ones.

`finite_witness`. No physics / geometry / curvature / connection / new-object
language. "automorphism" = a finite permutation of source endpoints fixing the
lift table and the source gluing; "rigidity certificate" = the (order,
orbit-size-multiset) iso-class fingerprint of that finite permutation group.
Within-domain separation question only; touches nothing in the
kappa/sheaf-H1/D1Cat/MTI lanes.

## What was derived from sources

- From **tests/T230-attribution-invariant-separation.md** (the constructive next
  object, verbatim): "a source-automorphism rigidity certificate ... keyed to a
  source-side *symmetry class* ... rather than to the *value* of any source
  field. The structural bet: if such an automorphism-class invariant separates a
  same-`nu` pair, gate 2 cannot absorb it (there is no single source FIELD to
  admit ...), and gates 3a/3b pass by construction. ... Build the
  source-automorphism groupoid ... and test whether its isomorphism class is
  `nu`-measurable on a same-`nu` fiber." T235 is exactly this test.
- From **models/attribution_invariant_separation.py** (re-used BY IMPORT ONLY,
  unmodified): the realization map `nu` (csp + provenance + category), the
  admissible enlargement `nu_prime` (the formal content of "absorption returns
  one level up": a source field, once admitted, is itself a neighbor field), the
  `relabel` action and `is_relabel_stable` gate, `_separating_same_nu_pair`, and
  the `_freeze` canonicalizer. The T230 test suite remains green (14/14) after my
  work, certifying the import is unmodified.
- From **open-problems/loss-kernel-witness-obligation-normal-form.md** ("What
  Would Kill This Recast" item 2; "Recommended Next Move" item 4): "Every tested
  `WO(f,J)` is definitionally identical to a standard neighbor object once the
  same data are granted" and "T108 and T127 already show mature
  provenance/effect/abstraction systems absorb any declared source field once it
  is named." T235 makes "any declared source field" precise enough to include a
  source **relation** (the gluing) and shows the symmetry-class invariant built
  on top of it inherits the absorption.

## Strongest positive result

The **source-automorphism groupoid** of a typed-lossy morphism is built
explicitly and computed by exhaustive finite permutation-group enumeration. For a
4-endpoint source `{p,q,r,s}` with a lift table symmetric under the swap
`(p q)(r s)` (the shared `nu`-visible data), the rigidity certificate -- the
`(group order, orbit-size multiset)` iso-class -- is a **genuine off-`nu`
separator** on a same-`nu` fiber:

| member | source gluing | Aut order | rigid | certificate | `nu` |
|---|---|---|---|---|---|
| `aut_rigid` | `{p},{q,r},{s}` (breaks swap) | 1 | yes | `(1,(1,1,1,1))` | shared |
| `aut_symmetric` | `{p,q},{r,s}` (respects swap) | 2 | no | `(2,(2,2))` | shared |
| `aut_symmetric2` | `{p,q},{r,s}`, different field value | 2 | no | `(2,(2,2))` | shared |

Decisive booleans (executed, `results/source-automorphism/T235-results.json`):

- `certificate_nu_measurable = False` -- Q1 answered: the automorphism iso-class
  is **not** determined by `nu`. This is the genuinely new fact vs the
  `source_fiber_cardinality` trap (which slides back inside `nu`). The certificate
  passes **gate 1**.
- `separation_absorbed_by_nu_prime = False` -- admitting the source FIELD value
  alone does NOT reproduce the separation. This is what distinguishes it from
  T230's `source_reading`, which dies immediately to `nu'`.
- `separation_absorbed_by_nu_struct = True` -- **the decisive obstruction.**
  Admitting the source GLUING as audit data DOES reproduce the separation. **Gate
  2 fires.**
- `relabel_stable = True`, `local = True` -- gates 3a/3b pass, exactly as the bet
  promised.
- `clears_route_b = False`, `failure_gate = gate2_absorbed_by_admitted_source_structure`.
- `nonvacuity_injected_pair_clears = True` -- the non-vacuity injector (re-using
  T230's discipline) exhibits a synthetic same-`nu` pair that separates, is
  relabel-stable, and has identical `nu'` AND identical `nu_struct`, so it CLEARS
  all gates. This proves the harness CAN report a clear, so the no-go is a real
  negative, not a constant-no harness.

Also confirmed (`test_certificate_keyed_to_symmetry_class_not_field_value`):
`aut_symmetric` and `aut_symmetric2` carry **different** hidden field values but
the **same** gluing, and get the **same** certificate -- so the certificate is
genuinely keyed to the symmetry CLASS, not to a field value. This is the part of
the bet that holds. It is exactly why `nu'` (field admission) cannot absorb it.
The bet fails only because the symmetry class is computed from a relation that is
**also** admissible.

## First exact obstruction / missing object

Gate 2 absorbs the automorphism class because the source-side **gluing** the
group is computed from is admissible audit data, and the iso-class is a derived
function of it: once the gluing is admitted (`nu_struct`), a mature neighbor
reproduces every distinction the certificate makes. The bet treated "symmetry
class" as if it had no admissible carrier; it has one -- the relation it acts on.

The **missing object** route (b) still needs is a source-side symmetry datum that
is simultaneously: (i) not `nu`-visible, (ii) not a free decoration, (iii) not
external / non-local, AND (iv) **not reconstructible from any admissible source
field OR source relation** -- a symmetry class with genuinely no admissible
carrier. The plain automorphism-group construction does not supply one: its
carrier (the gluing) is admissible, so the iso-class is absorbed with it. No such
non-reconstructible symmetry datum is exhibited on this finite family.

## Constructive next object

A **globalization-obstruction certificate**: instead of the automorphism group of
a single admissible gluing, take **locally-defined** `nu`-fixing source
automorphisms over a cover of the source and ask whether they **patch to a global
one**. The obstruction to globalization (a finite Z/2 or torsor obstruction
class) is the candidate symmetry datum whose value might be stable under admitting
the local automorphism data -- i.e. admitting each local piece as audit data
would NOT, by itself, reconstruct the global patching obstruction, leaving gate 2
nothing single to admit. Build that obstruction invariant and test whether it is
`nu_struct`-measurable on a same-`nu` fiber. That is the residual crack; the
value-keyed (T230) and structure-keyed (T235) cracks are now both closed.

## Meaning for the relevant claim

- **Independent-motivation criterion: NOT flipped to EARNED.** The single
  untested crack T230 named is tested and closed at gate 2.
- **Route (a) bounded subsumption is STRENGTHENED.** T230 closed the trichotomy
  over field-valued source separators (`source_reading` dies to `nu'`). T235
  extends gate-2 closure to **structure-valued** source separators: the
  automorphism iso-class, though `nu'`-non-absorbable and not `nu`-measurable, is
  `nu_struct`-absorbed. The citable bounded negative now reads: *every local,
  relabeling-stable separator on the family -- whether keyed to a source field
  value or to a source symmetry class -- is reproduced by some admissible
  enlargement (`nu'` or `nu_struct`) and hence factors through admissible neighbor
  data.* The LossKernel line is cleanly closeable for the symmetry-class route.
- The result is reported at the **test level**: `verdict = no-go`,
  `route_a_strengthened = True`. Whether this ratifies any LossKernel-line claim
  movement (e.g. demoting TF1's same-neighbor-data novelty route to closed) is the
  **integrator's** call, not this lane's.

## Known Physics Constraints

None. T235 is a finite typed-machinery audit over hand-built typed-lossy cases.
No time, finality, observer, consciousness, quantum-interpretation, curvature,
gravity, connection, or new-object language. "Automorphism" is a finite
permutation of source endpoints; "rigidity certificate" is a finite
permutation-group iso-class fingerprint; the groupoid is enumerated exhaustively
over a 4-element set. Tagged `finite_witness` (COMPLEXITY-LEDGER): a finite
executable fixture over a single `nu`-fiber, NOT a scalable/continuum theorem, NOT
a hardness claim, NOT a `poly_decider` search. The gates are decidable finite
checks (fiber-constancy, finite permutation orbit, registry-insensitivity).

## Falsification condition

This no-go is overturned in route (b)'s favor by exhibiting ONE same-`nu` pair
`(a,b)` and a symmetry-class invariant `I` with `I(a) != I(b)`, relabel-stable
AND local, where the separation is **NOT** reproduced by `nu_struct` for ANY
admissible enlargement -- i.e. admitting every source field AND the source gluing
still leaves the pair indistinguishable to a mature neighbor while `I` separates
them. The harness then reports `clears_route_b = True` and the verdict flips to
`EARNED-candidate`. The non-vacuity injector proves the harness CAN report this;
the actual source-automorphism construction does not, because its carrier (the
gluing) is admissible. The designated candidate to try is the
globalization-obstruction certificate (next object).

## Next proof / computation step

Build the globalization-obstruction invariant: locally-defined `nu`-fixing source
automorphisms over a cover of the source, with the obstruction to patching them to
a global automorphism as a finite obstruction class. Test whether that obstruction
is `nu_struct`-measurable on a same-`nu` fiber. If `nu_struct`-measurable, the
LossKernel line closes fully (no-go final, route (a) complete over all three
crack types); if NOT `nu_struct`-measurable and it separates a same-`nu` pair with
no admissible carrier, route (b) is alive and independent-motivation trends
EARNED -- record with maximum care, this is the program's crux.

## Reproduction

```bash
python -m unittest tests.test_source_automorphism_rigidity -v   # 15 checks
python -m pytest tests/test_source_automorphism_rigidity.py -q  # 15 passed
python -m models.source_automorphism_rigidity                   # prints structured report
```

- Model: `models/source_automorphism_rigidity.py` (imports
  `models/attribution_invariant_separation.py` by import only; T230 suite stays
  green: 14/14).
- Test: `tests/test_source_automorphism_rigidity.py` (15 checks, green under both
  unittest and pytest).
- Results: `results/source-automorphism/T235-results.json`.
