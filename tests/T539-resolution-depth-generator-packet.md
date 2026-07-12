# T539: Resolution-Depth Generator Packet

## Target Claims

- TAF11: North Star source-law reassessment beyond the finite-generator route.
- [S1: Spacetime As Consensus Envelope](../claims/S1-spacetime-consensus-envelope.md)
- [T538: Descent-Obstruction Resolution Source-Law Packet](T538-descent-obstruction-resolution-source-law-packet.md)

## Central Question

Can the T538-selected descent-obstruction family generate ordered resolution
depths from local record-cover, restriction-map, and compatible-section data
without accepting a free pairwise depth table?

T539 tests the strongest cheap generator: compute cover ranks from restriction
maps, assign each record its first compatible local-section rank, generate
`d(x, y)` from the source record rank, and declare `x < y` when
`d(x, y) < d(y, x)`.

## Success Criteria

- The computation is deterministic and exits 0.
- T538 is consumed as requiring a resolution-depth generator.
- No pairwise ordered-depth table is supplied as input.
- The generated relation is invariant under record and cover relabeling.
- The packet reports whether generated depths are source-law evidence or a
  programmable scalar-rank channel.
- Total-chain, antichain, diamond, and fork controls do not get promoted into
  source-law evidence.
- No S1, claim-ledger, Canon Index, canon-verdict, public-posture,
  external-publication, or cross-repo truth movement occurs.

## Failure Criteria

T539 fails if:

- it imports Lorentzian coordinates or target ordering statistics;
- it accepts pairwise resolution depths as input;
- it treats relabeling invariance alone as source-law success;
- it promotes rank-programmed controls into S1 evidence;
- it moves S1, claim status, Canon Index tiers, canon verdicts, public posture,
  external-publication state, or cross-repo truth.

## Run Command

```bash
python -m models.t539_resolution_depth_generator_packet --write-results
python -m unittest tests.test_t539_resolution_depth_generator_packet -v
```

## Boundary

T539 is a Track-1 source-law generator stress test. It does not establish a
source law, prove S1, derive spacetime, or update any governance or public
posture surface.
