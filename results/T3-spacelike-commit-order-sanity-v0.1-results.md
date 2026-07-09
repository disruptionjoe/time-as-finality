# T3 Spacelike Commit-Order Sanity Results v0.1

Verdict: `T3_SPACELIKE_SANITY_CHECK_BUILT_REVIEW_ONLY`

## Fixture

Events A and B are spacelike-separated in 1+1 Minkowski space. Event C lies in the common causal future of both.

## Frame Orders

- `lab` (`v=0.0`): `simultaneous_in_frame`
- `observer_plus_half_c` (`v=0.5`): `B_before_A`
- `observer_minus_half_c` (`v=-0.5`): `A_before_B`

## Invariant Checks

- Interval A-B: `-4.0` (spacelike)
- Interval A-C: `8.0` (causal future)
- Interval B-C: `8.0` (causal future)
- Proper-time difference across frames: `4.440892098500626e-16`

## Safe Reading

Finality language may track when records from A and B can be compared at C, but it must not add an invariant global commit order between spacelike-separated A and B.

## Not Earned

- R1 claim promotion
- replacement spacetime geometry
- hidden universal present
- global commit order for spacelike events
- proper-time replacement
