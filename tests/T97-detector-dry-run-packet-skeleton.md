# T97: Detector Dry-Run Packet Skeleton

## Route

Quantum measurement / classical records, with experimental-discriminator
pressure on the detector-provenance path.

## Question

After T87 fixed the raw-log contract, T95 mapped the detector stack, and T96
split the burden into native timing, middleware, custom controls, and
governance, can the surviving detector route be reduced to one locked dry-run
packet skeleton that a lab can freeze before collecting events?

## Motivation

The detector branch is now weak unless it can leave constructed fixtures. The
highest-value next step is not another synthetic detector result. It is a
pre-data packet that a skeptical reviewer can inspect before a run: exact
schemas, filenames, join keys, hashes, immutable exports, hostile controls, and
demotion rules.

## Success Criteria

- Every T87 table has exact required columns and no unregistered columns.
- Every table has a file name, join key, schema hash, export checksum, and
  immutable pre-data export point.
- The packet declares all T86 hostile control roles and channel-isolation
  tests.
- The locked packet is admitted only as a pre-data scaffold, not as evidence.
- T87 rejects the scaffold if scored immediately, with the live reason being
  absence of real raw deployment rows.

## Failure Criteria

- Template rows are allowed to populate T76/T86 evidence counts.
- Schema drift is allowed before or after data collection.
- Post hoc packet assembly is treated as equivalent to pre-registration.
- Missing ambiguous-tag or DAG contamination controls are ignored.
- The packet is described as empirical support.

## Claim Impact

If T97 passes, Q1 remains `partially_supported` but narrows again: the detector
branch has a concrete dry-run packet skeleton, not evidence. The next blocker
is operational execution: freeze the packet before the first event and populate
it with real rows without changing schema, policy, controls, or demotion rules.

If a realistic lab workflow cannot freeze and fill the packet pre-data, the
detector branch should be demoted below the active Q1 frontier.

## Reproduction

```bash
python -m unittest tests.test_detector_dry_run_packet_skeleton -v
python -m models.run_t97
```
