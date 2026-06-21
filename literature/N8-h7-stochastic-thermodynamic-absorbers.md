# N8: H7 Stochastic-Thermodynamic Absorber Map

Status: primary sources checked 2026-06-21.

## Current Repo Verdict

H7 is not currently a thermodynamic-arrow derivation. After T116, T122,
T142, T145, T148, and T152, its defensible content is:

```text
a conditional constructor/resource-accounting theorem:
strict finality direction follows only after the admissible transformations,
resources, reverse channels, and accounting boundary have already been fixed.
```

This note records the closest stochastic-thermodynamic absorbers so future H7
work cannot promote record stability, hard deletion, or open-system
irreversibility without first granting standard nonequilibrium physics its
native variables.

## Primary Sources

- Rolf Landauer, "Irreversibility and Heat Generation in the Computing
  Process," *IBM Journal of Research and Development* 5(3), 183-191 (1961).
  [DOI](https://doi.org/10.1147/rd.53.0183).
- Charles H. Bennett, "Logical Reversibility of Computation,"
  *IBM Journal of Research and Development* 17(6), 525-532 (1973).
  [DOI](https://doi.org/10.1147/rd.176.0525).
- Charles H. Bennett, "Notes on Landauer's Principle, Reversible Computation,
  and Maxwell's Demon," *Studies in History and Philosophy of Modern Physics*
  34, 501-510 (2003). [arXiv](https://arxiv.org/abs/physics/0210005) and
  [DOI](https://doi.org/10.1016/S1355-2198(03)00039-X).
- Christopher Jarzynski, "Nonequilibrium Equality for Free Energy
  Differences," *Physical Review Letters* 78, 2690 (1997).
  [DOI](https://doi.org/10.1103/PhysRevLett.78.2690).
- Gavin E. Crooks, "Entropy Production Fluctuation Theorem and the
  Nonequilibrium Work Relation for Free Energy Differences," *Physical Review
  E* 60, 2721-2726 (1999).
  [DOI](https://doi.org/10.1103/PhysRevE.60.2721).
- Udo Seifert, "Stochastic thermodynamics, fluctuation theorems and molecular
  machines," *Reports on Progress in Physics* 75, 126001 (2012).
  [arXiv](https://arxiv.org/abs/1205.4176) and
  [DOI](https://doi.org/10.1088/0034-4885/75/12/126001).
- Takahiro Sagawa and Masahito Ueda, "Generalized Jarzynski Equality under
  Nonequilibrium Feedback Control," *Physical Review Letters* 104, 090602
  (2010). [DOI](https://doi.org/10.1103/PhysRevLett.104.090602).
- Juan M. R. Parrondo, Jordan M. Horowitz, and Takahiro Sagawa,
  "Thermodynamics of information," *Nature Physics* 11, 131-139 (2015).
  [DOI](https://doi.org/10.1038/nphys3230).
- Massimiliano Esposito and Christian Van den Broeck, "Three faces of the
  second law. I. Master equation formulation," *Physical Review E* 82,
  011143 (2010). [arXiv](https://arxiv.org/abs/1005.1683) and
  [DOI](https://doi.org/10.1103/PhysRevE.82.011143).
- Riccardo Rao and Massimiliano Esposito, "Nonequilibrium Thermodynamics of
  Chemical Reaction Networks: Wisdom from Stochastic Thermodynamics,"
  *Physical Review X* 6, 041064 (2016).
  [arXiv](https://arxiv.org/abs/1602.07257) and
  [DOI](https://doi.org/10.1103/PhysRevX.6.041064).

## Absorber Table

| H7-looking move | Standard absorber | What must be granted before residue |
| --- | --- | --- |
| "The record was deleted, so time has a direction." | Landauer/Bennett information thermodynamics. Logical irreversibility and physical erasure depend on the memory model, heat bath, reset protocol, and whether reversible uncopy handles remain. | Memory states, erased bits, bath temperature, protocol, correlation/source-copy access, reversible-control class, and blank-capacity/sink state. |
| "The record is hard to erase." | Metastability and kinetics. A finite barrier gives a nonzero escape or deletion rate; long lifetime is not constructor impossibility. | Barrier height, attempt rate, reservoir state, horizon, available controls, and whether the claimed impossibility is finite or ideal. |
| "The open process has a preferred direction." | Stochastic thermodynamics and fluctuation theorems. Directional path asymmetry is measured by forward/reverse trajectory probabilities, entropy production, work, heat, and free-energy changes. | Forward and reverse dynamics, bath temperatures, driving protocol, path probabilities, entropy production, work and heat ledgers, and free-energy boundary conditions. |
| "Feedback or observation creates finality." | Thermodynamics of information. Measurement and feedback can trade information for work only after mutual information, measurement error, memory update, and feedback efficacy are included. | Measurement channel, controller memory, feedback protocol, mutual information, efficacy, memory erasure cost, and demon/accounting boundary. |
| "A nonequilibrium steady current is the finality arrow." | Nonequilibrium steady-state thermodynamics. Broken detailed balance can generate entropy-producing currents without producing a scalar finality monotone. | Stationary distribution, currents, affinities, housekeeping/excess or adiabatic/nonadiabatic entropy production, and the scalar score being tested. |
| "Biochemical maintenance stores record finality." | Chemical-reaction-network stochastic thermodynamics. Maintained order is normally paid for by chemostats, fuel, reservoirs, or driven boundary conditions. | Chemostats, chemical potentials, conservation laws, free-energy supply, network topology, and whether the record variable is a thermodynamic state variable or only an observer label. |

## Consequence For H7

The absorber stack does not kill the conditional T18 theorem. It kills the
unqualified physical-arrow reading:

```text
finality increases -> physical time arrow
```

is not licensed unless the model first states which reverse transformations
are physically impossible after standard stochastic-thermodynamic variables
are included.

The current H7 survivor is weaker:

```text
D1/finality topology can define useful observer- and task-indexed capability
objects, but thermodynamic direction belongs to the resource, boundary,
trajectory, and information-accounting structure unless a future substrate
survives this absorber map.
```

## Promotion Gate

A future H7 physical-arrow witness must provide all of the following before it
can be promoted:

1. A named physical record substrate and state space.
2. A declared write, delete, and reverse task.
3. A reverse-edge class of `physical_record_deletion`, not access revocation,
   support-copy removal, provenance loss, or observer-control denial.
4. Forward and reverse dynamics or an explicit proof that the reverse is not
   in the physically allowed transformation class.
5. Thermodynamic ledgers for work, heat, entropy production, free-energy
   drawdown, blank capacity, sink/export history, and reservoir state.
6. Information ledgers for source-copy correlations, controller memory,
   measurement, feedback, and erasure.
7. A task-natural future-operation split that persists after the above fields
   are matched.
8. A reason the reverse is constructor-impossible, not merely high-cost,
   exponentially unlikely, outside one observer's control, or excluded by an
   idealized infinite barrier.

## Demotion Rule

Demote any proposed H7 physical-arrow witness to absorber-owned territory if:

- the apparent arrow is finite-barrier lifetime or kinetic suppression;
- the arrow is standard entropy production, path irreversibility, or free
  energy drawdown;
- monotonicity consumes fresh blank memory, exported history, fuel, chemostat
  resources, or a hidden sink;
- deletion is blocked only because the observer lacks a control window;
- a reversible uncopy exists when source-copy correlations and controls are
  restored;
- the candidate depends on an infinite barrier, perfect code, exact
  superselection, or other ideal limit;
- the D1 topology split remains real but only changes task capability at fixed
  thermodynamic accounting.

The last case is not worthless. It is capability/topology residue. It is just
not thermodynamic-arrow evidence.

## Reinstatement Condition

H7 becomes a live physical-arrow route only if a finite, physically typed
substrate exhibits:

```text
matched stochastic-thermodynamic and information-accounting variables
+ a task-natural D1/future-operation split
+ physical_record_deletion reverse
+ constructor_impossible_after_full_accounting
```

Anything weaker should be recorded as resource-accounting,
stochastic-thermodynamic, or capability-topology result.

## Repo Impact

- Supports the current `weakened_conditional` status of
  [H7](../claims/H7-finality-induced-direction.md).
- Supports the negative reading of
  [T152](../tests/T152-metastable-record-deletion-screen.md): metastability is
  not enough.
- Strengthens the handoff in
  [H7 Physical-Deletion Substrate Handoff](../open-problems/h7-physical-deletion-substrate-handoff.md)
  by naming the external absorber variables a future substrate must freeze.
- Makes the next useful H7 move explicit: either bring a named substrate that
  clears this map, or stop treating H7 as a thermodynamic-arrow route.

## Claim Ledger Update

H7 remains `weakened_conditional`. Add N8 as a literature absorber map:
standard stochastic thermodynamics, Landauer/Bennett information
thermodynamics, fluctuation theorems, feedback thermodynamics, and
nonequilibrium steady-state accounting absorb the current physical-arrow
routes unless a finite record substrate has matched thermodynamic and
information ledgers plus a constructor-impossible physical-deletion reverse.
