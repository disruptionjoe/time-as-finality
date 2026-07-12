# T533: C(R) Surplus Starter Packet Classifier

## Target Claims

- `C(R)` capability object.
- T500 competency/resource/permission/provenance stack gate.
- T529 competency-surplus admission gate.
- `open-problems/region-indexed-capability-discriminator.md`.

## Setup

T529 admits only future review targets that match the full competency profile
and supply an independent noncompletion witness for a non-task-success
capability. T500 adds the fuller stack:

```text
full competency profile
+ resource preorder/profile
+ permission profile
+ provenance profile
```

T533 starts the TAF2 lane by making that post-T529 burden into a deterministic
packet classifier. It does not instantiate a successful `C(R)` witness.

## Success Criteria

- The classifier consumes the T500 and T529 floors.
- A packet is review-admitted only if it has reproducible exact-match
  certificates for competency, resource, permission, and provenance profiles.
- The review-admitted packet must also supply a predeclared, domain-native,
  independent noncompletion witness for a non-task-success capability.
- Negative cases reject simple-statistic, full-profile-equivalent,
  declared-only, and resource-only packets.
- At most one synthetic future-target positive control is admitted, and only as
  review-only.
- The writeup labels claims as COMPUTED or ARGUED with confidence.

## Failure Criteria

- The classifier treats flat simple statistics as `C(R)` surplus over the full
  stack.
- The classifier treats a full-profile-equivalent task-success coordinate as
  surplus.
- The classifier accepts declared profile matching without reproducible match
  certificates.
- The classifier accepts resource completion without competency, permission,
  and provenance completion.
- The classifier claims a current `C(R)` success, moves claims/canon/public
  posture, authorizes external publication, or updates cross-repo truth.

## Known Physics Constraints

No physics claim is made. T533 is a finite packet-screening artifact over
internal TaF admission gates.

## Reproduction

```bash
python -m models.t533_cr_surplus_starter_packet_classifier --write-results
python -m unittest tests.test_t533_cr_surplus_starter_packet_classifier -v
```
