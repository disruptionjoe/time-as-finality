# T398 Results: Resource-Profile Absorber for C(R)

- **Artifact:** `T398-resource-profile-absorber-v0.1`
- **Spec:** [tests/T398-resource-profile-absorber.md](../tests/T398-resource-profile-absorber.md)
- **Model:** [models/resource_profile_absorber.py](../models/resource_profile_absorber.py)
- **Test:** [tests/test_resource_profile_absorber.py](../tests/test_resource_profile_absorber.py)
- **Numbers:** [T398-resource-profile-absorber-v0.1.json](T398-resource-profile-absorber-v0.1.json)
- **Tags:** direction_a, capability_object, resource_preorder_absorber,
  c_of_r, no_claim_promotion

## Verdict

The T397 `C(R)` profile object is absorbed at the finite
resource-preorder level.

Once `C(R)` profiles are admitted as resource states under the declared
region/menu/task context, the anti-scalar and incomparability content is
exactly the product of two resource coordinates:

- undo capability: 3 levels;
- readout capability: 4 levels.

The quotient has 12 resource objects, relation size 48 under T397's strict
comparability convention, preorder size 60 including reflexives, and 18
incomparable pairs. Two axes jointly classify every object.

So Leg 2 of T397 remains a valid finite audit result, but not a
resource-theory novelty route. It is ordinary non-total resource
convertibility once the resource profile is granted.

## Absorber Findings

| Challenge | T398 result |
| --- | --- |
| Anti-scalar theorem shape | Absorbed. Product resource preorders naturally have incomparable elements and no faithful scalar total preorder. |
| Statistics-flat class | Absorbed as incomplete observer shadow. Declared Z-readout statistics omit the admitted resource profile. |
| Region indexing | Absorbed as context parameter in this finite run. The declared region, menu, and task family are the resource-theory context. |
| Physical realization | Translation residue. T397 remains useful as a region-indexed statistics/capability audit example. |

## Exact Checks

- Resource quotient: 12 objects from all 24 T397 configurations.
- Preorder: 48 strict comparable pairs, 18 incomparable pairs.
- Axes: 3 undo levels x 4 readout levels, jointly complete.
- Scalar gate: T397's 4,683 weak-order scan still has 0 reproducing scalars,
  but T398 classifies that as absorbed resource-preorder behavior.
- Factorization: no same-resource-profile configurations split on any T397
  capability verdict.
- Statistics-flat class: size 16, statistics constant, all 12 resource
  objects realized.
- Featured pair: same declared statistics, different resource objects.

## What Survives

T397 survives as a disciplined translation artifact:

```text
declared statistics can be an incomplete observer shadow of admitted
capability/resource profile state
```

That is useful for review and for designing the stronger region-indexed
discriminator, but it does not promote `C(R)` as a new resource-theory object.

## What Does Not Survive

- No new resource-theory theorem.
- No scalar-monotone novelty claim.
- No claim-ledger movement.
- No physics, hardware, platform, or spacetime claim.
- No verified external LOCC/coherence/majorization prior-art note; that
  remains separate work before external-facing language.

## Falsification Condition

This absorber would fail if two configurations in the same admitted resource
profile and same declared context split on a capability verdict, or if the
region index induced a conversion obstruction not captured by the admitted
profile preorder plus declared region/menu/task context.

## Recommended Next

Move to the stronger discriminator from
[open-problems/region-indexed-capability-discriminator.md](../open-problems/region-indexed-capability-discriminator.md):
equality under all `R`-supported intervention statistics, with separation only
by a boundary-crossing menu.

## Verification

```text
python -m pytest tests/test_resource_profile_absorber.py -q
10 passed in 5.14s

python -m json.tool results\T398-resource-profile-absorber-v0.1.json
json-ok
```
