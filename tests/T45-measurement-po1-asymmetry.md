# T45: Measurement PO1 Asymmetry

## Target Claims

- [H2: Quantum Under-Finalization](../HYPOTHESES.md)
- [PO1: Projection-Obstruction Schema](../claims/PO1-projection-obstruction-schema.md)
- [Measurement as PO1 Morphism exploration](../explorations/measurement-as-po1-morphism-v0.1.md)

## Central Question

Is quantum-to-classical measurement a fully PO1-admissible morphism, and is
that morphism structurally asymmetric -- meaning no PO1-admissible morphism
can run in the reverse direction?

## Setup

Two finite D1RestrictionSystems are constructed:

**Quantum layer Y** (richer, pre-finality):
- Three observer sites with high D1 profiles.
- Patches use consistent equality constraints: locally satisfiable AND globally
  satisfiable (global section exists).
- Y is unobstructed.

**Classical layer X** (restricted, post-measurement):
- Three observer sites with lower D1 profiles.
- Patches use parity-conflict constraints (same-same-different over a triangle):
  locally satisfiable per patch but globally obstructed (no global section).
- X is obstructed.

**Forward morphism f: Y -> X** (measurement):
- Total site map: every quantum site maps to a classical site.
- Declared forgotten structure: quantum coherence, superposition, phase
  information, entanglement.
- Projection loses local profile data (preserved dimensions differ between
  source and target).

**Inverse morphism g: X -> Y** (attempted unmeasurement):
- Same sites mapped in reverse.
- Declared forgotten structure: classical record state.

**General asymmetry tests**:
- Try g: X -> Z for additional targets Z (unobstructed, obstructed, trivial).
- Check AC7 for each: does X (as richer system) satisfy the unobstructedness
  requirement?

## Asymmetry Theorem (Candidate)

For any D1RestrictionSystem S with obstruction_detected = True, there is no
PO1-admissible morphism g: S -> Z for any D1RestrictionSystem Z.

Proof sketch: AC7 requires the richer system (source) to be unobstructed.
If S is obstructed, AC7 fails for any target Z. The proof is structural --
it depends only on the obstruction status of S, not on the choice of Z.

## Success Criteria

1. Forward morphism f: Y -> X is fully PO1-admissible (all AC1-AC7 pass).
2. Inverse morphism g: X -> Y fails PO1 admissibility (AC6 and AC7 both fail).
3. For all tested targets Z, any morphism g: X -> Z fails AC7.
4. Asymmetry theorem is verified finite-witness: the theorem holds for the
   tested cases, and the proof sketch is confirmed by the AC7 failure pattern.
5. State which hypotheses the result supports.

## Failure Criteria

1. Forward morphism f: Y -> X fails any of AC1-AC7. (Would indicate the
   quantum/classical construction is not a valid PO1 case.)
2. Inverse morphism g: X -> Y is fully PO1-admissible. (Would refute the
   measurement irreversibility claim.)
3. Some target Z exists such that g: X -> Z is PO1-admissible. (Would show
   the asymmetry does not hold in general.)
4. The asymmetry result is trivial: it holds because X and Y are specifically
   chosen to fail, not because of a structural property. (To avoid this, the
   theorem must be stated as a general result about any obstructed source, not
   about these specific systems.)

## Known Constraints

- This does not claim to model actual quantum mechanics.
- This does not claim that the gluing obstruction in X is the measurement
  problem; it claims PO1 obstruction is a structural analog.
- This does not derive the dimensionality of Y or X.
- This does not claim that unmeasurement is physically impossible beyond
  what the PO1 structural result implies.
- The test is finite and executable; it does not prove the theorem for infinite
  or continuous systems.

## Contribution Needed

- If the asymmetry theorem holds for these cases, state it precisely and add
  it to the theorem ladder.
- If a counterexample is found (g admissible), document which admissibility
  condition passed unexpectedly and revise the construction.
- If the forward morphism fails, diagnose which condition fails and revise
  the quantum system construction.
