# T528: S1 Finality-Native Generator Preflight

## Target Claims

- [S1: Spacetime As Consensus Envelope](../claims/S1-spacetime-consensus-envelope.md)
- [T525: Repaired S1 Manifoldlikeness Suite](T525-repaired-s1-manifoldlikeness-suite.md)
- [T526: S1 Reference-Law Gap Audit](T526-s1-reference-law-gap-audit.md)

## Central Question

Can the first post-T526 generator packet produce finite causets from
finality-native record data, without importing Lorentzian `u/v` coordinates,
and survive the repaired S1 diagnostic suite strongly enough to be admitted as
an S1 review target?

## Setup

T528 predeclares a two-receipt local record generator:

```text
events = finite finalized records
left_receipt_order, right_receipt_order = two local receipt streams
x < y iff both local receipt streams place x before y
```

The packet is audited against the T525 repaired suite over 32 deterministic
samples: event counts 8, 12, 16, and 20, with seeds 0 through 7. It also blocks
two shortcuts:

- screen-conditioned survivor laws that choose the generator after seeing the
  diagnostic;
- imported Lorentzian reference laws used as S1 promotion shortcuts.

Hostile controls include a one-channel chain and a hub broadcast order.

## Success Criteria

- The generator uses local receipt comparability rather than imported target
  spacetime coordinates.
- All multi-size samples pass the repaired T525 suite before the packet can be
  admitted as an executed review target.
- Hostile controls are rejected.
- Screen-conditioned and Lorentzian-import shortcuts are rejected or blocked.
- The result counts as no S1 evidence and changes no claim/canon posture.

## Failure Criteria

T528 fails if:

- an incomplete repaired-suite pass is counted as S1 evidence;
- a screen-conditioned generator is admitted;
- imported Lorentzian coordinates are treated as finality-native descent;
- the preflight changes S1 status, reverses T223, or claims spacetime
  derivation.

## Implementation Result

Status: implemented.

The two-receipt generator executes and avoids explicit `u/v` coordinate import,
but it passes only 25 of 32 repaired-suite samples: 7/8 at n=8, 5/8 at n=12,
8/8 at n=16, and 5/8 at n=20. It is therefore rejected as an incomplete
first packet. Hostile controls reject, and shortcut packets are blocked.

## Run Command

```bash
python -m unittest tests.test_t528_s1_finality_native_generator_preflight -v
python -m models.run_t528
```

## Boundary

T528 is a finite generator-preflight result only. It does not derive
spacetime, prove manifoldlikeness, establish a TaF-native sprinkling law,
reconstruct a Lorentzian metric, prove an embedding or continuum theorem,
reverse T223, promote S1, change claim status, change canon, or change public
posture.
