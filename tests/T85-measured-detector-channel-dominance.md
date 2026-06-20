# T85: Measured Detector Channel Dominance

## Route

Quantum measurement / classical records.

## Question

After T81, which of the remaining measured detector evidence categories can
still independently change the verdict under a hostile single-category stress
family, and which ones remain non-decisive because other accepted channels
already settle provenance?

## Motivation

T81 showed that trust boundaries and pre-registration are load-bearing in the
current executable audit. That still left an important ambiguity: perhaps
spoof resistance, perturbation response, or DAG observability would become
independently decisive once tested against a better hostile family. If they do
not, the detector schema should be compressed again.

## Construction

- Hold the signed T76 fixture's trust and pre-registration values fixed.
- Build one hostile single-category family for each remaining category:
  spoof/unique-tag evidence, perturbation response, and DAG observability.
- Re-run the T74 Monte Carlo audit on each family without changing any other
  measured category.

## Success Criteria

- At least one remaining category is shown to be independently decisive or
  explicitly shown not to be under hostile single-category stress.
- The result narrows the detector branch rather than broadening it rhetorically.
- The artifact states what witness family would be needed for perturbation or
  DAG channels to become independently decisive.

## Failure Criteria

- Every hostile single-category family leaves the verdict unchanged without any
  explanatory narrowing.
- The artifact treats a broad schema as justified when only one subchannel is
  actually decisive.
- The result relies on changing trust boundaries or pre-registration again
  rather than the targeted category.

## Known Physics Constraints

- This is still a protocol audit over already formed detector records.
- No new detector dynamics, collapse rule, or signalling claim is added.
- A positive result here would still be about admissibility of evidence, not a
  new quantum law.

## Contribution Needed

If perturbation or DAG observability are meant to stay in the core detector
schema, the next witness family must make authenticated tags ambiguous while
leaving one of those channels uniquely able to separate copied from
independent records.
