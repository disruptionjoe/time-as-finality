# T12 v0.1 Results: Coupling-Profile Reconstruction

Date: 2026-06-16

## Reproduction

```bash
python -m unittest tests.test_t12_coupling -v
python -m models.run_t12
```

Result: 7 tests pass. Full machine-readable output:
[t12-coupling-v0.1.json](t12-coupling-v0.1.json).

## Scenario

One causal record graph contains four propositions on three channels. Four
observers share the same observation event and identical holder access. Only
coupling profile and one conditional-acceptance flag vary. Threshold is 2.

## Findings

Same graph, same algorithm, different profiles produce different reconstructed
relations:

```text
all channels:       A<C  B<C  D<C
O1 {grav, em}:      A<C  B<C
O2 {grav, social}:  A<C  D<C
O3 {grav}:          A<C
```

No observer relation inverts the all-channel relation. Observer pairs agree
on shared reconstructible content.

Hardness and reach separate three grades:

| Proposition | Channel | Binding | Reach | Hardness | Grade |
| --- | --- | --- | ---: | ---: | --- |
| A, C | grav | unconditional | 1.00 | 1.00 | matter-grade |
| B | em | unconditional | 0.25 | 1.00 | narrow unconditional |
| D | social | conditional | 0.50 | 0.50 | idea-grade |

`O4` reconstructs `D` but is not constrained by it because
`accepts_conditional = false`.

## Limits

- Channels and binding flags are hand-authored.
- One channel per proposition is assumed.
- The conditional-acceptance flag is a placeholder, not a cognitive model.
- This supports M1 only as a toy coupling-profile result.

## Verdict

T12 supports the narrower M1 claim: coupling profile can change which
observer-relative temporal relation is reconstructed without creating causal
contradiction.
