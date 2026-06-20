# Technical Report: Dashboard Summary Nonidentifiability v0.1

## Claim Under Test

T78 requires event-level raw logs before a detector deployment can upgrade Q1.
T79 asks whether that requirement is substantive: can a coarse lab dashboard
ever identify the T76/T77 provenance verdict?

## Artifact

T79 constructs a witness pair with the same dashboard-visible summary:

- local and archive timing estimates;
- batching window;
- tag retention;
- signature-verification pass rate;
- threshold-coverage count.

The first completion is the T76 signed detector fixture. The second completion
keeps the same dashboard values but degrades the omitted provenance fields:
forgery acceptance, spoofed-independence leakage, archive/transport trust,
perturbation back-action, ancestry DAG observability, signed-edge coverage,
and DAG truncation/false-sharing rates.

## Current Strongest Claim

Coarse deployment dashboards are non-identifying for the detector branch. The
same summary can be completed into one deployment that robustly supports the
signed provenance route and another that leaks false independence.

## What This Improved

T79 turns the T78 raw-log gate into an executable obstruction rather than a
procedural preference. It identifies exactly why dashboard-level evidence is
not enough: the omitted provenance variables are not recoverable from timing,
retention, and signature-pass rates.

## What This Weakened

T79 weakens any attempt to treat operational dashboards as evidence for Q1.
Even an apparently strong detector dashboard cannot support the detector branch
without raw ancestry, replay, spoof, perturbation, and trust-boundary logs.

## Falsification Condition

T79 fails if one can define a coarse dashboard, omitting raw provenance
channels, that still uniquely fixes the T76/T77 detector verdict for every
compatible completion.

## Claim Ledger Update

Q1 should remain `partially_supported`, but with a sharper detector boundary:

```text
Detector-level support requires event-level raw-log provenance. Coarse timing
and signature dashboards are non-identifying and cannot upgrade Q1.
```

## Next Work

Obtain one real deployment log satisfying T78 and run the locked T76/T77/T79
audit. If only dashboard summaries are available, the detector branch should be
withheld rather than interpreted optimistically.

## Reproduction

```bash
python -m unittest tests.test_dashboard_summary_nonidentifiability -v
python -m models.run_t79
```
