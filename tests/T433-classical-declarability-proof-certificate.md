# T433 - Classical Declarability Proof Certificate - spec (frozen)

> Recorded-tier exploratory artifact. `TESTS.md`, `ROADMAP.md`, and
> `CLAIM-LEDGER.md` are UNTOUCHED; the T-number lives only in this header / the
> results header. No claim promotion. This is a classical finite-product proof
> certificate only; it does not touch the quantum E3 route.

- Model: `models/classical_declarability_proof_certificate.py`
- Tests: `tests/test_classical_declarability_proof_certificate.py`
- Results: `results/T433-classical-declarability-proof-certificate-v0.1-results.md`
- Run: `python -m pytest tests/test_classical_declarability_proof_certificate.py -q`

## The question this test settles

T432 made the classical finite-boundary declarability gate executable by sweep.
T433 asks for the next internal obligation named by the capability-boundary
taxonomy:

```text
Can the classical single-instance C-fragment be stated as a constructive proof
certificate, not only an exhaustive small Boolean sweep?
```

## Certificate inputs

- `Omega`: a finite classical product code.
- `A0`: observables factoring through the declared region projection `pi_R`.
- `A1`: the full co-present finite classical code / identity readout.
- `d`: a total datum `Omega -> V`.

## Success / Kill Criteria

### Success

The certificate must show:

- `d` is A0-measurable exactly when it is constant on `pi_R` fibers;
- if `d` is not A0-measurable, same-A0 boundary pairs exist;
- every total `d` is A1-measurable because `d = d o id_Omega`;
- a single-instance physical candidate relative to A1 would require an A0
  boundary that fails A1 measurability;
- no valid finite classical product case satisfies that candidate condition.

### Guard cases

The named cases must include:

- an A0-visible null control;
- a complement-bit boundary;
- a full-support relation boundary;
- a non-binary finite product case.

### REDESIGN

If a finite classical product-code case has a total datum that fails A1
measurability, stop: either A1 was misdefined or the datum is not a valid total
classical datum.

## Honest Ceiling

Finite classical product-code proof certificate only. T433 is not a universal
no-go theorem, not a quantum theorem, not a WAY/E3 result, not claim-ledger
movement, not physics evidence, and not cross-repo support.
