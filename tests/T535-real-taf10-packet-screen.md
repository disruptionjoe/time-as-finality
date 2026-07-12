# T535: Real TAF10 Packet Screen

## Target Claims

- TAF10: real C(R) surplus packet replacing the T533 synthetic target.
- T533 C(R) surplus starter packet classifier.
- T500/T529 competency, resource, permission, provenance stack burden.
- Region-indexed capability discriminator open problem.

## Setup

T533 admitted only a synthetic future target. T535 checks whether existing repo
material already contains a real packet shape that can replace that synthetic
target without relaxing the T533 burden.

The screen evaluates existing-source candidates from:

1. current T407/T398/T493/T494 C(R) and competency absorber family;
2. T411/T412 physical-boundary lineage;
3. T514-T520 quantum access, monogamy, and copy-law lane;
4. T521 detector provenance manifest lane.

## Success Criteria

- The computation exits 0 and writes deterministic JSON and Markdown results.
- The screen consumes T533 classifier logic for exact full-stack matching and
  independent witness admissibility.
- At least two concrete existing-source packet candidates are evaluated.
- Each candidate is checked for exact full-stack profile matching across
  competency, resource, permission, and provenance profiles.
- Each candidate is checked for an independent non-task-success noncompletion
  witness.
- Outcomes are one of `CLEARED`, `NARROWED`, `FALSIFIED`, `PAUSE`, or
  `REVIEW_ONLY`.
- If no candidate clears, the writeup names the exact missing field blocking a
  real TAF10 packet.
- Claims are labeled `COMPUTED` or `ARGUED` with confidence.

## Failure Criteria

- The screen treats T407/T398 simple-statistics spread as C(R) success over a
  full competency/resource/permission/provenance stack.
- The screen treats a resource, permission, provenance, joint-record, or
  completion field as an independent noncompletion witness.
- The screen treats the T521 manifest template as data-bearing detector
  evidence.
- The screen moves claims, canon, registry, roadmap, attention cards, public
  posture, external publication, or cross-repo truth.
- The screen lets the Track-2 C(R) byproduct replace the Track-1 source-law
  question.

## Known Physics Constraints

No physics claim is made. T535 is a finite packet-screening artifact over
existing repo results and admission criteria.

## Reproduction

```bash
python -m models.t535_real_taf10_packet_screen --write-results
python -m unittest tests.test_t535_real_taf10_packet_screen -v
```
