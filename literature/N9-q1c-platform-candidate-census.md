# N9: Q1C Platform Candidate Census

Status: primary sources checked 2026-06-21.

This note asks a narrow question:

```text
Do named superconducting weak-measurement and second-meter platform families
actually instantiate one of the two live Q1C escape classes left by T146,
T149, and T150?
```

Those two classes are:

1. an auxiliary channel tied to extra environment or detector structure that is
   not screened off by the full ordinary event-level record; or
2. an explicit instrument enlargement with a predeclared preserved comparison
   target.

The purpose of this note is not to defend Q1C. It is to decide whether the
current literature supplies a real platform candidate or whether the route
should remain dormant.

## Primary Sources

- K. W. Murch, S. J. Weber, C. Macklin, and I. Siddiqi, "Observing single
  quantum trajectories of a superconducting qubit" (arXiv:1305.7270, submitted
  May 30, 2013).
  [arXiv](https://arxiv.org/abs/1305.7270)
- Z. K. Minev et al., "To catch and reverse a quantum jump mid-flight"
  (arXiv:1803.00545, submitted March 1, 2018; Nature 570, 200-204, 2019).
  [arXiv](https://arxiv.org/abs/1803.00545)
  [DOI](https://doi.org/10.1038/s41586-019-1287-z)
- A. Opremcak et al., "Measurement of a Superconducting Qubit with a Microwave
  Photon Counter" (arXiv:1803.01014, submitted March 2, 2018; Science 361,
  1239-1242, 2018).
  [arXiv](https://arxiv.org/abs/1803.01014)
  [DOI](https://doi.org/10.1126/science.aat4625)
- Bayan Karimi and Jukka P. Pekola, "Quantum trajectory analysis of single
  microwave photon detection by nanocalorimetry" (arXiv:2001.01943, submitted
  January 7, 2020; Phys. Rev. Lett. 124, 170601, 2020).
  [arXiv](https://arxiv.org/abs/2001.01943)
  [DOI](https://doi.org/10.1103/PhysRevLett.124.170601)
- G. Koolstra et al., "Monitoring fast superconducting qubit dynamics using a
  neural network" (arXiv:2108.12023, submitted August 26, 2021; Phys. Rev. X
  12, 031017, 2022).
  [arXiv](https://arxiv.org/abs/2108.12023)
  [DOI](https://doi.org/10.1103/PhysRevX.12.031017)
- Andras M. Gunyho et al., "Single-Shot Readout of a Superconducting Qubit
  Using a Thermal Detector" (arXiv:2303.03668, submitted March 7, 2023;
  Nature Electronics 7, 210-215, 2024).
  [arXiv](https://arxiv.org/abs/2303.03668)
  [DOI](https://doi.org/10.1038/s41928-024-01147-7)
- Ezad Shojaee et al., "Broadband pulsed quadrature measurements with
  calorimeters" (arXiv:2503.00188, published December 8, 2025 in Phys. Rev. A
  112).
  [NIST entry](https://www.nist.gov/publications/broadband-pulsed-quadrature-measurements-calorimeters)
  [DOI](https://doi.org/10.1103/wmz2-5ft7)

## Platform Census

| Platform family | What the source actually measures | Q1C class | Verdict |
| --- | --- | --- | --- |
| Murch 2013, Koolstra 2021 homodyne trajectory platforms | A continuous noisy voltage record from the ordinary weak monitored chain, used to reconstruct the conditional qubit trajectory. | ordinary instrument baseline | Not a Q1C auxiliary-channel candidate. The monitored voltage trace is the ordinary record `R`, not a second axis `A`. |
| Minev 2018/2019 jump-reversal platform | Continuous monitoring of an auxiliary level to predict and reverse a jump mid-flight, plus feedback conditioned on that same monitoring stream. | same-instrument / postselected-control family | Does not clear Q1C. In repo terms this is ordinary monitored-trajectory content or success-conditioned control, not an independently typed TaF axis at fixed ordinary statistics. |
| Opremcak 2018 microwave photon counter | Millikelvin-stage photon-counter readout replacing the usual linear-amplifier voltage chain. | explicit readout replacement | Important hardware, but not a fixed-standard auxiliary meter. It changes the ordinary readout chain itself. |
| Gunyho 2023 / 2024 thermal-detector qubit readout | Single-shot superconducting-qubit readout using a thermal detector instead of a parametric-amplifier chain. | explicit readout replacement | Same verdict as Opremcak. This is an honest alternate instrument, not a simultaneous second meter over fixed ordinary weak-measurement statistics. |
| Karimi and Pekola 2020 nanocalorimetric trajectories | A calorimetric click or heat-sensitive record that defines the photon-detection trajectory. | alternate ordinary record | Too close to the target to ignore, but still not Q1C. The calorimetric stream is itself the trajectory record rather than an auxiliary verdict-changing channel on top of a fixed standard record. |
| Shojaee et al. 2025 broadband pulsed quadrature with calorimeters | A generalized quadrature-measurement formalism for broadband optical modes using calorimeters and a local oscillator. | formalism change / enlarged task | Not a monitored-qubit platform and not a same-statistics dual-meter witness. It changes the measurement object and task. |

## What The Census Shows

Three patterns dominate.

### 1. Standard superconducting weak-measurement platforms treat the monitored trace as the ordinary record

The homodyne-trajectory sources make the basic architecture explicit: the noisy
voltage trace is the measurement record from which the conditional trajectory is
reconstructed. That is exactly why T143/T149 bite so hard. Once the full
event-level monitored trace is declared as `R`, there is no extra Q1C channel
yet.

### 2. The best "second-meter" hardware papers mostly change the ordinary instrument

The microwave-photon-counter and thermal-detector papers matter because they
show that non-amplifier readout chains are real. But they do not give a
simultaneous auxiliary meter whose decision value survives conditioning on a
fixed ordinary weak-measurement transcript. They replace the readout chain.

This keeps them outside the first live T146 class and moves them into the
second class only in a weak sense: they are honest enlarged or alternate
instruments, but they do not yet declare a preserved comparison target that
would let Q1C ask its fixed-standard question cleanly.

### 3. Calorimetric and quadrature hybrids still change the record or the task

Nanocalorimetry is the closest physical family to the hoped-for route because
it couples trajectory language to an energy-sensitive record. But the
calorimetric clicks are still the trajectory-defining record, not a verdict
channel added on top of a fixed ordinary one.

The 2025 broadband pulsed quadrature paper pushes farther toward mixed
measurement architectures, but for a different task: broadband mode quadrature
measurement. That is useful evidence that calorimeters can participate in
quadrature constructions. It is not evidence that a monitored superconducting
qubit already has a Q1C-valid auxiliary meter.

## Net Verdict

The current primary-source census does not reveal a concrete monitored-qubit
platform in the live extra-environment class.

It also does not reveal an already named platform that cleanly satisfies the
live enlarged-instrument class with:

1. a predeclared preserved comparison target;
2. a frozen full ordinary record `R`;
3. a distinct auxiliary channel `A`;
4. an independently typed TaF axis `H`; and
5. a fixed verdict map `V = g(H)`.

So the honest outcome is:

```text
Q1C has real neighboring hardware families, but no current named platform in
the screened literature clears the repo's live admissibility burden.
```

## What This Weakens

This weakens the hope that one more generic scan of superconducting
weak-measurement papers will uncover a hidden Q1C platform.

More sharply:

```text
the missing Q1C object is not "any second detector";
it is a very specific auxiliary-channel architecture that current named
platform families do not yet instantiate.
```

## What Would Reopen Q1C

Only two source-backed discoveries would change the current verdict.

1. A monitored-qubit experiment that keeps the ordinary event-level record
   fixed while an auxiliary channel tied to extra environment structure gives
   non-gerrymandered decision lift.
2. An explicit enlarged-instrument proposal that states, in advance, the
   preserved comparison target and exposes event-level data sufficient for the
   T149/T150 screens.

Until then, Q1C should remain dormant.

## Repo Impact

- Supports the current `dormant` status of
  [Q1C](../claims/Q1C-weak-measurement-discriminator-gate.md).
- Strengthens the external-platform posture of
  [Q1C auxiliary-channel handoff](../open-problems/q1c-auxiliary-channel-platform-handoff.md).
- Narrows future Q1C work away from generic literature scans and toward either
  explicit extra-environment channels or honest enlarged-instrument protocols.
