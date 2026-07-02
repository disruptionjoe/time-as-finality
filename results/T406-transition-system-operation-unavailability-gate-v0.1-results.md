# T406 Transition-System Operation-Unavailability Gate v0.1 Results

## Verdict

Finite transition-system operation-unavailability gate built.

Under matched T405/T403 payload, operation menu, fixed accounting, and
non-dynamic substrate support, a revision capability split appears only when
the declared transition relation differs. Admitting that relation as native
operation-availability data restores factorization, and matched transition
systems do not split revision capability.

No claim-ledger movement is earned.

## Main Pair

| Check | Result |
| --- | --- |
| Fixed-accounting projection equal | `True` |
| Transition-system completion equal | `False` |
| Operation menu equal | `True` |
| Revision budget equal | `True` |
| Non-dynamic substrate support equal | `True` |
| Absorber-vector mismatches | `[]` |
| Capability split | `can_revise_final_verdict` only |
| Residue label | `absorbed_by_transition_system_completion` |

## Factorization Check

Every finite pair with the same transition-system completion has the same
capability object in this fixture.

## Controls

- Operation-menu variation is absorbed as menu/fixed-accounting completion.
- Resource variation is absorbed by resource accounting.
- Provenance variation is absorbed by provenance completion.
- Control-handle variation is absorbed by control completion.
- Boundary variation is absorbed by boundary completion.
- Hidden source labels are blocked.
- Latch-topology markers are blocked as shortcuts in this gate.

## Interpretation

T406 narrows the post-T405 search. The next positive route cannot merely say
that an operation is unavailable. It needs a domain-native law or measured
substrate dynamics that forces the transition relation without using the
transition relation itself as the separating state.

This remains an absorber/precheck, not a physical-arrow theorem.
