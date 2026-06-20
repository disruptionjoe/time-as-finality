# T76: Measured Detector Provenance Posterior

## Question

Can the detector-provenance branch be turned from plausible posterior ranges
into a pre-registered measured-posterior audit?

## Motivation

T75 mapped a realistic photon time-tagging stack into the T74 engineered
recovery region, but several ranges were still plausible engineering
posteriors. T76 converts that limitation into a stricter test interface:

```text
deployment evidence -> posterior ranges -> T74 Monte Carlo audit -> Q1 verdict
```

## Evidence Fields

The measured record must include:

- local and archive timing uncertainty;
- event-batch latency;
- tag retention and signature verification;
- accepted forged-tag and spoofed-independent-tag trials;
- independent unique-tag rate;
- detector, archive, and transport trust-boundary checks;
- dependent-copy and independent-channel perturbation responses;
- perturbation back-action events;
- DAG observability, signed-edge verification, DAG truncation, and false
  shared-edge counts;
- pre-registered threshold coverage.

## Success Criteria

- A measured signed fixture lands in `robust_measured_recovery`.
- A timing-only unsigned control keeps the same timing evidence but withholds
  D1 because provenance evidence is insufficient.
- A strong signed deployment with incomplete pre-registration is classified as
  threshold-dependent rather than upgraded.
- No result depends on D1 outcomes when choosing the posterior ranges.

## Failure Criteria

- Timing-only evidence recovers D1 provenance.
- Incomplete pre-registration still upgrades the detector branch.
- The adapter silently treats plausible narrative ranges as measurements.
- Real deployment measurements fall into withhold, false-independence, or
  false-dependence regions.

## Claim Impact

If T76 passes, Q1 remains only `partially_supported` as a measured,
pre-registered detector-provenance protocol. It is not evidence that quantum
measurement, decoherence, or high-resolution detector timing alone produces D1
finality.

## Reproduction

```bash
python -m unittest tests.test_measured_detector_provenance_posterior -v
python -m models.run_t76
```
