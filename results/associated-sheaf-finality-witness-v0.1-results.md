# Associated-Sheaf Finality Witness Results

Result: focused tests pass `6/6`.

Machine-readable output:

- [associated-sheaf-finality-witness-v0.1.json](associated-sheaf-finality-witness-v0.1.json)

## Model

This is the first finite S6 run. It is a deterministic toy model, not a quantum
dynamics simulation.

The fixed finite site is:

```text
(C, J) = six environment fragments E0..E5 with all pairwise overlaps
F      = local pointer / phase / provenance records on each fragment
aF     = approximate effective-descent record object
eta_F  = local sections projected to the stable pointer/provenance record
Cap    = read_pointer, phase_sensitive_branch, reconstruct_provenance_order
Loss_K = capabilities present in F but absent from aF
PO_rec = prep -> measure -> record
```

The declared effective-descent threshold is four matching pointer fragments out
of six, with at least three fragments supporting each retained provenance edge.

## Goal Outcomes

| goal | result | witness |
| --- | --- | --- |
| G1 typed finite site specification | pass | fixed site, cover, overlaps, target category, capabilities |
| G2 minimal gluing / sheafification computation | pass | stable global section first appears at monitoring strength `3` |
| G3 Darwinian-style redundancy cover fixture | pass | redundancy rises while gluing error falls |
| G4 capability non-factorization across `eta_F` | pass | `phase_sensitive_branch` is present in `F` and lost in `aF` |
| G5 temporal provenance reconstruction test | pass | sheaf temporal score improves from `0.666667` to `1.0` at threshold |

## Sweep

| monitoring | true / false / unknown | redundancy | gluing error | stable global section | temporal gain | loss kernel |
| ---: | --- | ---: | ---: | --- | ---: | --- |
| 0 | 1 / 3 / 2 | `0.166667` | `0.833333` | no | `0.0` | phase, pointer |
| 1 | 2 / 2 / 2 | `0.333333` | `0.666667` | no | `-0.166667` | phase, pointer, provenance |
| 2 | 3 / 2 / 1 | `0.5` | `0.5` | no | `-0.25` | phase, pointer, provenance |
| 3 | 4 / 1 / 1 | `0.666667` | `0.333333` | yes | `0.333333` | phase |
| 4 | 5 / 1 / 0 | `0.833333` | `0.166667` | yes | `0.166667` | phase |
| 5 | 6 / 0 / 0 | `1.0` | `0.0` | yes | `0.0` | phase |

## Strongest Result

In this fixed finite cover, effective descent appears first at monitoring
strength `3`:

```text
redundancy      = 4/6
gluing error    = 2/6
observer agree  = 0.8 among known fragments
reversal proxy  = 16
```

At that threshold:

- the pointer record stabilizes;
- both provenance edges `prep -> measure` and `measure -> record` survive into
  the effective global record;
- phase tags are projected out;
- `Cap(F)` does not factor through `Cap(aF)` for the phase-sensitive task;
- the cross-repo effect verdict is `Project[O] + Finalize[R] + Lose[K]`, not
  `Issue[S]`.

## Interpretation

This is a bounded positive for the S6 fixture shape:

```text
presheaf-like local records
  -> effective descent
  -> stable final record
  -> capability loss
  -> improved provenance reconstruction
```

It does not prove the physical bridge. It only shows that the five-goal S6 lane
is executable on a finite typed model and that the measurements named by the
re-vote can be computed together.

## Guardrails

The result is fixture-local.

It does not prove:

- a general sheafification theorem;
- a quantum dynamics result;
- a Quantum Darwinism / SBS threshold in a physical system;
- Born weights;
- source-side issuance.

The next object should replace the deterministic fragment profile with an
open-system or SBS-style fixture while keeping the same outputs:

```text
redundancy
gluing error
eta_F loss profile
capability factorization
provenance reconstruction
```

## Reproduction

```bash
python -m unittest tests.test_associated_sheaf_finality_witness -v
python -m models.run_associated_sheaf_finality --output results/associated-sheaf-finality-witness-v0.1.json
```
