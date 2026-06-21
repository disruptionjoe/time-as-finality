# N11: H7 Protected-Memory Absorber

Status: primary sources checked 2026-06-21.

## Current Repo Verdict

Protected-memory proposals do not currently reopen H7's physical-arrow route.
After T145, T148, T152, T160, and N8, their defensible role is narrower:

```text
protected or self-correcting memory can be a serious stress test for H7's
physical_record_deletion gate, but it is not H7 evidence by default
```

The present literature supports four absorber readings before any H7 residue
is entertained:

1. active recovery or syndrome-processing support rather than passive deletion
   impossibility;
2. long lifetime or growing energy barrier rather than impossible deletion;
3. higher-dimensional or idealized symmetry protection rather than a finite
   ordinary substrate reading; or
4. engineered bath/control structure that belongs to the driven-dissipative
   absorber class, not to a substrate-native reverse impossibility.

## Primary Sources

- Eric Dennis, Alexei Kitaev, Andrew Landahl, and John Preskill,
  "Topological quantum memory," *Journal of Mathematical Physics* 43, 4452
  (2002). [arXiv](https://arxiv.org/abs/quant-ph/0110143) and
  [DOI](https://doi.org/10.1063/1.1499754).
- Sergey Bravyi and Barbara Terhal, "A no-go theorem for a two-dimensional
  self-correcting quantum memory based on stabilizer codes,"
  *New Journal of Physics* 11, 043029 (2009).
  [arXiv](https://arxiv.org/abs/0810.1983) and
  [DOI](https://doi.org/10.1088/1367-2630/11/4/043029).
- R. Alicki, M. Horodecki, P. Horodecki, and R. Horodecki,
  "On thermal stability of topological qubit in Kitaev's 4D model,"
  *Open Systems & Information Dynamics* 17, 1-20 (2010).
  [arXiv](https://arxiv.org/abs/0811.0033).
- Benjamin J. Brown, Daniel Loss, Jiannis K. Pachos, Chris N. Self, and
  James R. Wootton, "Quantum memories at finite temperature,"
  *Reviews of Modern Physics* 88, 045005 (2016).
  [arXiv](https://arxiv.org/abs/1411.6643) and
  [DOI](https://doi.org/10.1103/RevModPhys.88.045005).
- Fernando Pastawski, Lucas Clemente, and Juan Ignacio Cirac,
  "Quantum memories based on engineered dissipation,"
  *Physical Review A* 83, 012304 (2011).
  [arXiv](https://arxiv.org/abs/1010.2901) and
  [DOI](https://doi.org/10.1103/PhysRevA.83.012304).
- Sam Roberts and Stephen D. Bartlett,
  "Symmetry-Protected Self-Correcting Quantum Memories,"
  *Physical Review X* 10, 031041 (2020).
  [arXiv](https://arxiv.org/abs/1805.01474) and
  [DOI](https://doi.org/10.1103/PhysRevX.10.031041).

## Absorber Shape

Protected-memory papers ask whether encoded information survives thermal noise
for a memory time that grows strongly with system size, often without frequent
active correction. H7 asks a different question:

```text
does a physical_record_deletion reverse remain constructor-impossible after
thermodynamic, information, boundary, and control data are matched?
```

That mismatch matters. A protected memory can be impressive and still fail H7
because "stored for a very long time" is weaker than "deletion reverse is not
physically available under the matched control class."

## Comparison Table

| Protected-memory move | Source-backed fact | H7 absorber reading |
| --- | --- | --- |
| 2D surface / toric-code memory | Dennis et al. treat protection through error recovery thresholds, with fast measurements and classical processing in the standard architecture. Bravyi-Terhal then show that 2D local stabilizer-code memories have only a constant energy barrier, ruling out self-correction in that class. | Active-recovery support or finite-barrier lifetime, not deletion impossibility. |
| 4D toric-code memory | Alicki et al. show exponentially long relaxation below a critical temperature for certain observables, but the construction uses measurements on all individual spins plus a polynomial-time algorithm. | Strong thermal stability candidate, but still a protected-memory lifetime result with explicit recovery structure, not a frozen H7 deletion-reverse witness. |
| Finite-temperature self-correction program in general | Brown et al. review the field as an open search shaped by no-go theorems and loopholes across 2D, 3D, and higher-dimensional models. | Confirms that protected memory is a live neighboring research area, but not a current H7 bridge. |
| Engineered-dissipation memories | Pastawski-Clemente-Cirac explicitly protect encoded information by engineering the bath coupling. | This changes the allowed drive and environment class, so it belongs to the driven-dissipative absorber, not to substrate-native deletion impossibility. |
| Symmetry-protected self-correction | Roberts-Bartlett obtain self-correction by imposing a strong 1-form symmetry structure. | This is an exact symmetry/control restriction unless given a finite operational enforcement story that survives T160's superselection/control screen. |

## What This Improves

T160 already said "protected memories are null by default." This note makes
that sentence evidence-backed rather than merely procedural.

The key improvement is a sharper distinction:

```text
protected storage time != constructor-impossible physical deletion
```

That prevents H7 from quietly borrowing credibility from the quantum-memory
literature when the actual protected-memory success metric is different from
the repo's deletion-reverse gate.

## What This Weakens

This weakens the strongest remaining intuitive H7 reopening story:

```text
maybe topological or error-correcting memories already realize the kind of
irreversible record finality H7 wants
```

The current literature does not support that upgrade. The cleanest known cases
either:

- rely on active decoding or measurement infrastructure;
- provide long but finite or asymptotic lifetime claims;
- move to higher-dimensional constructions or strong symmetry restrictions; or
- change the environment/control model directly.

All four are real scientific achievements. None is yet the H7 object.

## Protected-Memory Reinstatement Gate

A future H7 proposal drawing on protected-memory physics must freeze all of the
following before it counts as more than a neighbor citation:

1. The encoded record token and the exact delete / reverse task.
2. The reverse-edge class:
   `physical_record_deletion`, not logical corruption, access loss, failed
   decoding, or unavailable syndrome information.
3. The allowed control class, including whether syndrome extraction,
   decoder computation, bath engineering, or symmetry enforcement are granted.
4. The fixed absorber vector:
   - work / heat / free-energy drawdown;
   - blank capacity, sink, or exported history;
   - source-copy correlations and reversible handles;
   - observer/control boundary;
   - bath/reset channels.
5. The protected-memory-specific absorber data:
   - code distance or lattice size;
   - syndrome access and decoder assumptions;
   - barrier height or excitation geometry;
   - symmetry or sector enforcement mechanism;
   - dimensionality and boundary conditions.
6. A task-natural future-operation split that survives after those fields are
   matched.
7. A reason the reverse is impossible, not merely exponentially suppressed,
   decoder-dependent, bath-dependent, or idealization-dependent.

No current protected-memory source in this note clears that burden for H7.

## Demotion Rule

Demote a protected-memory proposal to absorber-owned territory if:

- the headline result is coherence time or logical lifetime scaling;
- the proposal needs active syndrome measurement, classical decoding, or
  engineered dissipation not counted in the comparison;
- the barrier is finite and the argument is kinetic rather than impossible;
- the stability depends on higher-dimensional geometry with no finite ordinary
  substrate interpretation for the H7 task;
- the protection depends on externally enforced symmetry or exact sector
  restrictions with no finite operational enforcement audit; or
- the supposed residue disappears once the delete/reverse task is restated as
  ordinary error correction, lifetime, or control-boundary accounting.

## Claim Ledger Update

H7 remains `weakened_conditional`.

Add N11 as a protected-memory absorber:

```text
topological, self-correcting, symmetry-protected, and engineered-dissipation
quantum memories are neighboring stress tests, not current H7 evidence.
Their standard success metrics are active recovery, lifetime scaling, energy
barrier growth, symmetry restriction, or bath engineering rather than a
matched-accounting constructor-impossible physical_record_deletion reverse.
```

## Recommended Next Move

Do not reopen H7 with generic references to surface codes, toric codes,
protected memories, or self-correction.

The next non-null H7 move from this family would need one named finite
protected-memory substrate, one deletion task rather than a storage task, and
an audit showing that the reverse fails after decoder, bath, symmetry, and
thermodynamic variables are all made explicit.
