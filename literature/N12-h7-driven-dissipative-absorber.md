# N12: H7 Driven-Dissipative Absorber

Status: primary sources checked 2026-06-21.

## Current Repo Verdict

Driven-dissipative and chemostat-maintained record proposals do not currently
reopen H7's physical-arrow route. After T145, T148, T152, T160, N8, and N11,
their defensible role is narrower:

```text
driven dissipation is a serious neighboring stability program, but it is not
H7 evidence by default because the maintained record typically depends on
explicit pumping, reset, bath engineering, or chemostat work
```

The present literature supports four absorber readings before any H7 residue
is entertained:

1. engineered dissipation implements an always-on decoder, reset channel, or
   target-state preparation mechanism rather than a substrate-native deletion
   impossibility;
2. nonequilibrium steady states are maintained by drive, bath, chemical
   potentials, or chemostats whose work and entropy budgets belong in the
   comparison object;
3. driven-dissipative phase transitions and bistability can create sharp
   memory-like structure or long switching times without making deletion
   constructor-impossible; or
4. a maintained attractor, current, or logical subspace is a stability or
   preparation result, not yet a matched-accounting `physical_record_deletion`
   obstruction.

## Primary Sources

- Frank Verstraete, Michael M. Wolf, and J. Ignacio Cirac, "Quantum
  computation and quantum-state engineering driven by dissipation," *Nature
  Physics* 5, 633-636 (2009). [arXiv](https://arxiv.org/abs/0803.1447) and
  [DOI](https://doi.org/10.1038/nphys1342).
- Massimiliano Esposito and Christian Van den Broeck, "The Three Faces of the
  Second Law: I. Master Equation Formulation," *Physical Review E* 82, 011143
  (2010). [arXiv](https://arxiv.org/abs/1005.1683) and
  [DOI](https://doi.org/10.1103/PhysRevE.82.011143).
- Fernando Pastawski, Lucas Clemente, and Juan Ignacio Cirac, "Quantum
  memories based on engineered dissipation," *Physical Review A* 83, 012304
  (2011). [arXiv](https://arxiv.org/abs/1010.2901) and
  [DOI](https://doi.org/10.1103/PhysRevA.83.012304).
- Hao Ge and Hong Qian, "Thermodynamic Limit of a Nonequilibrium Steady-State:
  Maxwell-Type Construction for a Bistable Biochemical System," *Physical
  Review Letters* 103, 148103 (2009). [arXiv](https://arxiv.org/abs/0904.2056)
  and [DOI](https://doi.org/10.1103/PhysRevLett.103.148103).
- Riccardo Rao and Massimiliano Esposito, "Nonequilibrium Thermodynamics of
  Chemical Reaction Networks: Wisdom from Stochastic Thermodynamics,"
  *Physical Review X* 6, 041064 (2016). [arXiv](https://arxiv.org/abs/1602.07257)
  and [DOI](https://doi.org/10.1103/PhysRevX.6.041064).
- Julia Hannukainen and Jonas Larson, "Dissipation driven quantum phase
  transitions and symmetry breaking," *Physical Review A* 98, 042113 (2018).
  [arXiv](https://arxiv.org/abs/1703.10238) and
  [DOI](https://doi.org/10.1103/PhysRevA.98.042113).
- Alice Grimm, Nicolas Eickbusch, Stijian Krastanov, Simone Perriello, Suhas
  Mundhada, Bryan M. Terhal, and Zlatko K. Minev, "Stabilization and
  operation of a Kerr-cat qubit," *Nature* 584, 205-209 (2020).
  [arXiv](https://arxiv.org/abs/1907.12131) and
  [DOI](https://doi.org/10.1038/s41586-020-2587-z).
- Zaki Leghtas et al., "Protecting a bosonic qubit with autonomous quantum
  error correction," *Nature* 585, 368-372 (2020).
  [arXiv](https://arxiv.org/abs/2004.09322) and
  [DOI](https://doi.org/10.1038/s41586-020-2603-3).
- Dany Lachance-Quirion et al., "Autonomous quantum error correction of
  Gottesman-Kitaev-Preskill states," *Nature* 631, 336-341 (2024).
  [arXiv](https://arxiv.org/abs/2310.11400) and
  [DOI](https://doi.org/10.1038/s41586-024-07507-8).

## Absorber Shape

Driven-dissipative work studies how a target state, code space, or stable
nonequilibrium sector can be maintained by balancing drive and loss or by
engineering the system-bath coupling.

H7 asks a different question:

```text
does a physical_record_deletion reverse remain constructor-impossible after
work, bath, sink/export, source-copy, boundary, and control data are matched?
```

That mismatch matters. A maintained nonequilibrium record can be scientifically
important and still fail H7 because:

- the record is preserved by ongoing free-energy throughput;
- reset, bath, or decoder structure is part of the mechanism;
- deletion remains possible once the pump/control class is admitted; or
- the claimed asymmetry is ordinary steady-state or phase-selection
  thermodynamics rather than a deletion obstruction.

## Comparison Table

| Driven-dissipative move | Source-backed fact | H7 absorber reading |
| --- | --- | --- |
| Dissipative state engineering or computation | Verstraete-Wolf-Cirac show that local Markovian dissipation can be designed so the steady state encodes a target computation or prepared state. | Environment engineering can create the record attractor; that is preparation/stabilization power, not deletion impossibility. |
| Engineered-dissipation quantum memories and AQEC | Pastawski-Clemente-Cirac, Leghtas et al., and Lachance-Quirion et al. protect logical information by engineered baths, autonomous reset, or reservoir engineering. | The memory depends on an always-on correction/reset structure. Count that pump/reset/decoder resource and the result moves into control-and-bath accounting, not H7 residue. |
| Nonequilibrium steady states or chemostatted biochemical memories | Esposito-Van den Broeck and Rao-Esposito formulate entropy production, work splitting, and chemostat-maintained nonequilibrium structure explicitly. | A sustained record or switch is paid for by drive, affinities, chemostats, or housekeeping dissipation. Those are absorber variables, not evidence of impossible deletion. |
| Bistable or phase-transition-like maintained records | Ge-Qian and Hannukainen-Larson show that driven or open systems can exhibit bistability, phase selection, or nonanalytic steady-state structure. | Sharp switching and long residence times can exist without making the reverse impossible. This is steady-state selection or kinetic structure, not a matched-accounting deletion obstruction. |
| Cat-qubit or stabilized manifold storage | Grimm et al. stabilize a Kerr-cat manifold through driven dissipation and use that structure for protected logical operation. | The logical manifold is maintained by explicit drive-loss balance. If that balance is allowed, the phenomenon is an engineered attractor, not substrate-native irreversibility. |

## What This Improves

T160 already said "driven dissipation is null by default." This note turns that
sentence into a literature-backed absorber rather than a procedural guess.

The key improvement is a sharper distinction:

```text
maintained nonequilibrium memory != constructor-impossible physical deletion
```

That matters because driven-dissipative platforms are among the most plausible
future candidates an external physicist might suggest for H7.

## What This Weakens

This weakens the intuitive reopening story:

```text
maybe a pumped, autonomous, or dissipatively stabilized memory already
realizes the kind of irreversible record finality H7 wants
```

The current literature does not support that upgrade. The standard success
metrics are steady-state preparation, logical lifetime extension, autonomous
error correction, switching robustness, or dissipative phase structure. Those
are real achievements, but they are not yet the H7 object unless the delete /
reverse task survives after the pump, bath, and control resources are frozen.

## Driven-Dissipative Reinstatement Gate

A future H7 proposal drawing on driven-dissipative physics must freeze all of
the following before it counts as more than a neighbor citation:

1. The encoded record token and the exact delete / reverse task.
2. The reverse-edge class:
   `physical_record_deletion`, not leaving an attractor, losing access,
   turning off a pump, or exiting one control regime for another.
3. The allowed control class, including whether continuous pumping, bath
   engineering, autonomous reset, decoder action, or feedback-free reservoir
   engineering are granted.
4. The fixed absorber vector:
   - work or free-energy throughput;
   - bath temperatures, chemical potentials, or chemostats;
   - housekeeping dissipation, currents, or entropy production;
   - sink or exported-history state;
   - source-copy correlations and reversible handles;
   - observer/control boundary.
5. The driven-dissipative-specific absorber data:
   - drive amplitudes, detunings, loss channels, and reset rates;
   - steady-state manifold or attractor structure;
   - lifetime or switching-time scaling;
   - symmetry or code-space assumptions if used.
6. A task-natural future-operation split that survives after those fields are
   matched.
7. A reason the reverse is impossible, not merely costly, pump-dependent,
   decoder-dependent, phase-selected, or kinetically suppressed.

No current driven-dissipative source in this note clears that burden for H7.

## Demotion Rule

Demote a driven-dissipative proposal to absorber-owned territory if:

- the result is target-state preparation or stabilization of a steady state;
- the record persists only while a drive, pump, chemostat, or reset channel is
  maintained;
- the proposal needs autonomous decoder or reservoir-engineering structure not
  counted in the comparison;
- the effect is a nonequilibrium current, phase selection, or bistable
  residence-time result rather than a deletion obstruction;
- the lifetime gain disappears when the bath, work, or control resources are
  matched; or
- the supposed residue vanishes once the delete/reverse task is restated as
  ordinary open-system thermodynamic maintenance.

## Claim Ledger Update

H7 remains `weakened_conditional`.

Add N12 as a driven-dissipative absorber:

```text
driven-dissipative, chemostatted, and autonomously corrected memories are
neighboring stability programs, not current H7 evidence. Their standard success
metrics are steady-state preparation, maintained nonequilibrium order, lifetime
extension, or autonomous correction under explicit pump, bath, reset, or drive
resources rather than a matched-accounting constructor-impossible
physical_record_deletion reverse.
```

## Recommended Next Move

Do not reopen H7 with generic references to autonomous stabilization,
nonequilibrium steady states, dissipative phase transitions, cat qubits,
engineered baths, or self-maintaining biochemical switches.

The next non-null H7 move from this family would need one named finite
driven-dissipative substrate, one deletion task rather than a storage or
preparation task, and an audit showing that the reverse fails after pump,
bath, chemostat, decoder, work, and control variables are all made explicit.
