# 2026-07-02 Resource-Profile Absorber Progress Run

## Governance Loaded

- `AGENTS.md`
- `steward/README.md`
- `Vision - North Star.md`
- `Method - Research Program Guidelines.md`
- `Lead Research Line - Time as Finality.md`
- `CONTRIBUTING.md`
- `ROADMAP.md`
- `TESTS.md`
- T397 region-capability artifacts and the region-indexed capability
  discriminator card

## Worktree State

Before edits, the only visible untracked file was `results/_rmtest.json`,
treated as scratch / non-artifact material and left untouched.

## Objective

Run the named next gate from T397: a resource-theory absorber for the bounded
region capability profile object `C(R)`.

Scope is intentionally narrow:

1. Reuse the existing T397 `C(R)` profile family.
2. Map the realized profiles to a finite resource preorder.
3. Test whether the anti-scalar and statistics-flat findings survive as
   formal residue once resource profile state and context are admitted.
4. Preserve any surviving content as translation / physical-realization
   residue only; do not move the claim ledger.

## Planned Verification

- `python -m pytest tests/test_resource_profile_absorber.py -q`
- `python -m models.resource_profile_absorber`
- JSON parse of generated results
- focused T397 regression
- `git diff --check`

## Receipt

Completed.

## Artifacts Created

- `tests/T398-resource-profile-absorber.md`
- `models/resource_profile_absorber.py`
- `tests/test_resource_profile_absorber.py`
- `results/T398-resource-profile-absorber-v0.1.json`
- `results/T398-resource-profile-absorber-v0.1-results.md`

## Surfaces Updated

- `TESTS.md`
- `ROADMAP.md`
- `open-problems/region-indexed-capability-discriminator.md`
- `steward/memory-log.md`

## Result

T398 grants the finite resource-profile absorber:

- T397's `C(R)` profiles quotient to 12 resource objects.
- The quotient is exactly a 3 undo-level x 4 readout-level product resource
  preorder.
- T397 relation accounting is preserved: 48 strict comparable pairs, 60
  preorder pairs including reflexives, 18 incomparable pairs.
- Two monotone axes jointly classify every object.
- No same-resource-profile configurations split on any T397 capability
  verdict.
- T397's 16-member statistics-flat class realizes all 12 resource objects.

Interpretation: the anti-scalar shape and statistics-flat class are absorbed
as finite resource-preorder behavior / incomplete observer shadow once the
resource profile and declared region/menu/task context are admitted. T397
remains translation residue and a useful region-indexed audit example, but not
a promoted resource-theory novelty claim.

No claim-ledger movement. No North Star/canon/public-posture change. No
external prior-art verification was claimed.

## Verification

Passed:

```text
python -m pytest tests/test_resource_profile_absorber.py tests/test_region_capability_no_go.py -q
44 passed in 12.68s

python -m models.resource_profile_absorber
model-ok

python -m json.tool results\T398-resource-profile-absorber-v0.1.json
json-ok

git diff --check
clean
```

## Next Safe Lane

The stronger Direction-A discriminator now has to require equality under all
`R`-supported intervention statistics and separation only by a boundary-
crossing menu. A separate verified literature note is still needed before any
external-facing resource-theory phrasing.
