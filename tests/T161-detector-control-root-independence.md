# T161: Detector Control-Root Independence

## Route

Quantum measurement / classical records, with experimental-discriminator
pressure on detector evidence infrastructure.

## Question

Is a nominal T100/T138 authority split enough for Q1B, or can shared critical
control roots collapse apparently separate authorities back into
self-certification?

## Motivation

T100 and T138 made detector admissibility depend on nominal authority domains
and a pre-data manifest. That still leaves one realistic loophole: a workflow
can name separate archive, audit, governance, and control roles while sharing
the same signing HSM, manifest-registration service, publication gate, or
revocation root.

If those shared roots give one hidden control surface authority over multiple
packet functions, the apparent federation is weaker than the role labels make
it look.

## Setup

- Reuse the T100 authority-partition audit as the nominal screen.
- Add critical control-root assignments for:
  - manifest registration;
  - archive write;
  - audit attestation;
  - publication release;
  - revocation registry.
- Quotient nominal authority domains by shared critical roots to form an
  effective authority partition.
- Re-run the T100 audit on that effective partition.
- Include a noncritical shared dashboard control to show that ordinary shared
  observability does not count as a hidden merge by itself.

## Success Criteria

- A nominally admissible four-domain profile with distinct critical roots
  remains admissible.
- A nominal five-domain profile with shared archive/audit HSM collapses.
- A nominal five-domain profile with shared governance/archive release control
  collapses.
- A shared noncritical dashboard does not collapse an otherwise admissible
  partition.
- The result is stated as detector evidence infrastructure, not as detector
  physics or Q1 support.

## Failure Criteria

- Role labels alone are treated as enough for operational independence.
- Shared critical roots do not affect admissibility.
- Shared noncritical services are treated as equivalent to shared packet
  mutation or certification roots.

## Claim Impact

No Q1B promotion. T161 is another narrowing gate: detector admissibility now
depends on the effective authority partition after quotienting by shared
critical packet-control roots.

## Reproduction

```bash
python -m unittest tests.test_detector_control_root_independence -v
python -m models.run_t161
```
