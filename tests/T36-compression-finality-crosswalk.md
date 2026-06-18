# T36: Compression-Finality Crosswalk

## Target Claims

D1, C1, T9 (emergence laboratory substrate)

## Setup

The experiment runs all 256 elementary CA rules on the same substrate as the
T9 emergence laboratory (width=5, layers=3, 32 initial states × 5 seed indices
= 160 traces per rule). For each rule and each seed-intervention trace, two
independent columns of metrics are computed:

**D1 finality column**
- `trace_survival_fraction`: fraction of the 160 traces producing a nonzero
  trace_mask (record of the intervention survives to the terminal layer).
- `mean_accessible_support`: mean Hamming weight of surviving trace_masks.

**Compression column**
- `trace_shannon_entropy`: H(trace distribution) in bits, where the distribution
  is over the 2^5 = 32 possible trace_mask patterns.
- `trace_compressibility`: 1 − entropy/log₂(2^5); 0 = uniform/incompressible,
  1 = deterministic/perfectly compressible.
- `zlib_ratio`: zlib-compressed length / raw length for all traces concatenated.

The core question: do compressibility and finality diverge on at least one rule
family? If yes, compressibility is empirically distinct from D1 finality in this
model and cannot be added as a D1 dimension without justification.

## Success Criteria

- `divergence_exists = True`.
- At least one witness with same trace_survival but different compressibility
  (gap > 0.2).
- At least one witness with same lost_bits but different compressibility
  (gap > 0.2).
- compression-survival Pearson correlation is neither +1 nor −1 (compressibility
  is not identical to finality).
- Rule 0 (all-zeros attractor): survival=0, compressibility=1.
- Rule 30 (chaotic): survival≈1, compressibility<0.15.
- Rule 150 (reversible, XOR-based): injective, survival=1, 0.1<comp<0.9.

## Failure Criteria

- `divergence_exists = False`: compressibility collapses to a linear function of
  trace_survival or lost_bits — no independent information.
- All witnesses have gap < 0.05: compressibility is experimentally
  indistinguishable from existing metrics at this resolution.
- compression-survival correlation = ±1.0: compressibility is a reparametrization
  of D1 trace_survival, not a new observable.

## Known Physics Constraints

This is a finite cellular automaton experiment, not a physics derivation. The
results constrain what can be claimed about the relationship between
compressibility and finality within the toy model. Extension to continuous
physical substrates, quantum decoherence, or relativistic causal graphs is open.

## Contribution Needed

- Repeat with larger width (width=7 or width=9) to verify divergence persists
  beyond finite-size effects.
- Test whether compressibility predicts T9's existing counterexamples
  (same_loss_different_survival / same_survival_different_loss) more cleanly
  than either metric alone.
- Define a compressibility preorder over trace distributions and check whether
  it partially orders the 256 rules consistently with D1 finality.
- Connect to Shannon's noiseless coding theorem: do high-compressibility rules
  admit shorter record descriptions per intervention, and does that bound the
  observer's reconstruction threshold?
