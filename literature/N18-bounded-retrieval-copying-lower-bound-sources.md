# N18: Bounded Retrieval / Copying Lower-Bound Sources

Status: primary-source checked for bounded computation-lane calibration on
2026-07-07. No claim movement.

## Scope

This note supports only the narrow T495/T497 question:

```text
Can source-backed machine-learning literature justify treating bounded-record
retrieval as a computation-side capability bottleneck review target?
```

Answer: yes, narrowly. The sources support a computation-side distinction
between full context/copying/retrieval access and fixed-size or compressed
state summaries. They do not support physics mechanism, quantum copyability,
decoherence, Standard Model, public-posture, or cross-repo claims.

## Primary Sources Checked

- Samy Jelassi, David Brandfonbrener, Sham M. Kakade, and Eran Malach,
  "Repeat After Me: Transformers are Better than State Space Models at
  Copying," Proceedings of the 41st International Conference on Machine
  Learning, PMLR 235:21502-21521, 2024.
  URL: https://proceedings.mlr.press/v235/jelassi24a.html
- Albert Gu and Tri Dao, "Mamba: Linear-Time Sequence Modeling with Selective
  State Spaces," arXiv:2312.00752, 2023/2024.
  DOI: https://doi.org/10.48550/arXiv.2312.00752
- Imanol Schlag, Kazuki Irie, and Jurgen Schmidhuber, "Linear Transformers Are
  Secretly Fast Weight Programmers," Proceedings of the 38th International
  Conference on Machine Learning, PMLR 139:9355-9366, 2021.
  URL: https://proceedings.mlr.press/v139/schlag21a.html

## Source-Backed Reading

The Jelassi et al. ICML paper is the direct support for this bounded scope. It
studies copying and retrieval from context and distinguishes Transformers from
generalized state-space models whose latent state does not grow with sequence
length. It supports T497's computation-side use of copying/retrieval as a
capability workload.

The Mamba paper is a caveat source. It says selective SSMs were introduced
partly to address content-based reasoning weaknesses in earlier SSM-like
families and reports strong practical performance. This blocks any simplistic
"SSMs are bad" reading. T497 may use it only to keep the absorber stack honest:
selective state, input-dependent propagation, and architecture details matter.

The Schlag/Irie/Schmidhuber paper supports a second caveat: attention variants
and fast-weight style memory systems are themselves memory-programming systems
with capacity limits and retrieval tasks. This blocks a naive "attention equals
unbounded full history" reading.

## Allowed Use

- Treat bounded-record retrieval as a source-backed computation-side review
  target.
- Use copying/retrieval workload language for T495/T497.
- Require architecture caveats: fixed latent state, selective state, fast
  weights, and retrieval task definitions must be declared.
- Keep T495's distinction between arbitrary retrieval and native retained-task
  controls.

## Disallowed Use

- No physics mechanism import.
- No quantum copyability import.
- No decoherence or Standard Model claim.
- No claim-ledger movement.
- No public-posture movement.
- No cross-repo truth movement.
- No theorem claim beyond the checked source scopes.

## Current Verdict

N18 makes the T495 successor source-backed for a narrow computation-side
composite absorber explanation:

```text
bounded state + task workload + full-history completion
  -> explains why arbitrary retrieval fails while native retained tasks pass
```

It does not create a TaF novelty claim.
