# T383: Relativity Pattern Falsification Suite

## Target Claims

R1, S1, D1, PO1, and the T382 clean-adapter result:

```text
How fragile is the two-null-channel adapter under targeted perturbations?
```

## Setup

Start with the baseline reciprocal two-null-channel adapter. Perturb it with:

- anisotropic signal calibration,
- nonreciprocal scaling,
- per-step channel delay,
- deterministic record noise,
- missing signal channel,
- extra primitive channel,
- coarse-grained access.

Check:

- interval preservation,
- invariant signal calibration,
- two-channel completeness,
- minimal basis,
- exact record access.

## Success Criteria

- Baseline two-null-channel adapter survives.
- Anisotropic and nonreciprocal scaling fail.
- Delayed channel fails invariant signal calibration.
- Deterministic noise is demoted under exact access.
- Missing channel fails completeness.
- Extra primitive channel fails minimality.
- Coarse-graining is partial, not exact success.

## Failure Criteria

- A perturbed adapter is promoted despite breaking one of the declared
  requirements.
- Coarse-grained or noisy access is treated as exact record-level invariance.
- The finite perturbation catalog is treated as exhaustive.

## Known Constraints

This is a declared perturbation suite, not a universal stability theorem. It
does not test every deformation of the adapter.

## Contribution Needed

Use T377-T383 to write the synthesis packet: what is now forced, what is merely
clean, what remains imported, and what the next open object is.
