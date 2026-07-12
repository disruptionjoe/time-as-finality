# T538: Descent-Obstruction Resolution Source-Law Packet

## Target Claims

- TAF11: North Star source-law reassessment beyond the finite-generator route.
- [S1: Spacetime As Consensus Envelope](../claims/S1-spacetime-consensus-envelope.md)
- [T537: Source-Law Family And Falsifier Packet](T537-source-law-family-and-falsifier-packet.md)

## Central Question

Does the T537-selected `descent_obstruction_resolution_family` already define a
source-law packet, or do its declared variables still allow arbitrary relation
programming through free resolution-depth choices?

T538 computes the candidate relation before reading any target ordering
statistic or Lorentzian reference. It then tests whether the packet survives
hostile controls and whether the source variables determine the relation rather
than merely storing it.

## Source-Law Recipe Tested

Given ordered records `x, y`, compute their obstruction-resolution depths
`d(x, y)` and `d(y, x)` from the declared finite record-cover packet. The
candidate relation declares `x < y` when `d(x, y) < d(y, x)`.

## Success Criteria

- The computation is deterministic and exits 0.
- T537 is consumed as selecting `descent_obstruction_resolution_family`.
- The relation is computed without target ordering statistics or Lorentzian
  coordinates.
- Cover relabeling and restriction-map isomorphism controls preserve the
  computed relation.
- Total-chain and antichain controls do not get promoted into source-law
  evidence.
- The packet reports whether the declared variables determine a law or remain
  underconstrained.
- No S1, claim-ledger, Canon Index, canon-verdict, public-posture,
  external-publication, or cross-repo truth movement occurs.

## Failure Criteria

T538 fails if:

- it imports Lorentzian coordinates or target ordering statistics;
- it promotes a total-chain or antichain control into S1 evidence;
- it treats relabeling invariance alone as source-law success;
- it hides arbitrary relation programming by preloaded resolution depths;
- it moves S1, claim status, Canon Index tiers, canon verdicts, public posture,
  external-publication state, or cross-repo truth.

## Run Command

```bash
python -m models.t538_descent_obstruction_resolution_source_law_packet --write-results
python -m unittest tests.test_t538_descent_obstruction_resolution_source_law_packet -v
```

## Boundary

T538 is a Track-1 source-law stress test. It does not establish a source law,
prove S1, derive spacetime, or update any governance or public posture surface.
