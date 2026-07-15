# T582: W192 Record-Conditioned Capability Discriminator Gate

## Target Claims

TAF3, TAF5, TAF8, T541, T580, T581, and the region-indexed capability
discriminator.

## Setup

Consume the frozen written-spinor W192 packet as external stress-test input.
Keep the before and after cases identical except for explicit access to the
frozen K-positive `psi`. Use the corrected proxy task menu and keep the absent
native `ad(P)` current, quotient, holdout, and retarded response distinct from
the written proxy.

## Success Criteria

- T581 has parked TAF11 and routes W192 separately.
- Exactly the record-conditioned vertex-lift task changes.
- The change is classified as explicit state/resource completion.
- Structural equality is separated from failed access-complete and
  intervention equality.
- Fixed-source, completed-shadow, changed-menu, Action-2-only, and
  Action-3-only controls pass.
- Native evidence is staged in order through `TYPE_ADMISSIBLE`,
  `QUOTIENT_RESPONSE_READY`, and `RETARDED_PHYSICS_READY`.
- Missing Action 2 or Action 3 evidence fails closed.

## Failure Criteria

- The arbitrary-`v` lift or operator-only shell is made state dependent.
- The proxy central no-go is transferred to the absent native `ad(P)` map.
- An embedded-subalgebra packet is labeled full native.
- Quotient readiness or a written shell is treated as retarded physics.
- A positive capability verdict is issued while a completion absorber fires or
  Action 2 or Action 3 evidence is absent.

## Run Command

```bash
python -m models.t582_w192_record_conditioned_capability_discriminator_gate --write-results
python -m unittest tests.test_t582_w192_record_conditioned_capability_discriminator_gate -v
```

## Boundary

T582 is a deterministic cross-domain stress-test gate. It does not verify GU
physics, establish a TaF capability theorem, move TAF8, import TI source truth,
or move claims, Canon status, public posture, publication, S1, or cross-repo
truth.
