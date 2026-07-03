# T425 - M2 Size-Sweep Absorption Gate - v0.1 results

> Recorded-tier exploratory stress test. `TESTS.md` and `CLAIM-LEDGER.md` are
> UNTOUCHED; the T-number lives only in this header / the spec header. NO claim
> promotion; ledger actions pause for Joe. Cross-domain index language is the
> OBJECT OF STUDY, never evidence for physics or a sibling repo. The only code
> imports are TaF-native T413/T423 machinery plus standard library modules.

- Spec (frozen first): `tests/T425-m2-size-sweep-absorption-gate.md`
- Model: `models/m2_size_sweep_absorption_gate.py`
- Tests: `tests/test_m2_size_sweep_absorption_gate.py` (8 passed)
- Artifact JSON: `results/T425-m2-size-sweep-absorption-gate-v0.1.json`
- Run: `python -m pytest tests/test_m2_size_sweep_absorption_gate.py -q`

## Overall verdict: REDESIGN - the direct larger-index rescue is blocked before index agreement

T424 left one honest escape hatch: n=3 might be too small for a real Route-A
index/cohomology channel. T425 tests the prior gate by sweeping the inherited
T423/T424 AND-doctrine, strict-majority / tie-reject setup across n=3, n=4, and
n=5.

The result is sharper than an index-channel failure:

```text
The inherited SURVIVES-R1 finality datum exists at n=3, but disappears at n=4
and n=5. Every larger-n nonzero gap is absorbed by a 3-judge proper subset.
```

So a larger complex may contain index-looking cycle structure, but under the
same separator it has no global-no-local finality datum to compute.

| size | profiles | v_gap fibers | SURVIVES-R1 | ABSORBED | no separation | min absorbed size |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| n=3 | 64 | 2 | 6 | 0 | 58 | n/a |
| n=4 | 256 | 17 | 0 | 60 | 196 | 3 |
| n=5 | 1024 | 136 | 0 | 390 | 634 | 3 |

## What this says about T424

T424 genuinely improved on T423 Route B: `I_chi` and `I_fr` escaped the v_gap
relabel bar at n=3, even though neither equaled the separator. T424's honest
ceiling said a larger complex might be needed because the triangle capped the
Euler/spectral-flow channels.

T425 closes the direct version of that rescue:

- n=4 and n=5 do contain compatibility-graph cycle structure;
- all 244 n=4 positive-cycle profiles and all 1024 n=5 positive-cycle profiles
  have no SURVIVES-R1 separator;
- every nonzero larger-n gap is visible in a 3-judge proper subset and is
  therefore `ABSORBED`.

That means the issue is not merely "find a better index." The inherited finality
target is atomic to the n=3 doctrinal-paradox fixture.

## Fiber and absorption controls

The full v_gap vector remains a sufficient bookkeeping object for separator
status in this sweep:

- n=3: 0 mixed separator fibers; the single separator fiber has size 6.
- n=4: 0 mixed separator fibers; no separator fibers.
- n=5: 0 mixed separator fibers; no separator fibers.

For n=4 and n=5, all nonzero gaps have `min_sep_size = 3`. The larger whole never
carries a new global-no-local datum under the inherited rule; a 3-person proper
coalition already witnesses the difference.

## Cycle diagnostic

The compatibility-graph cycle-rank diagnostic confirms that the negative is not
just absence of larger graph structure:

| size | cycle-rank-positive profiles | separator profiles among them |
| --- | ---: | ---: |
| n=3 | 28 | 0 |
| n=4 | 244 | 0 |
| n=5 | 1024 | 0 |

This diagnostic is not promoted as a cohomology theorem. It only verifies that
larger profiles have index-looking cycle structure while still lacking the
inherited finality separator.

## Next gate

Any future M2 rescue must predeclare a different aggregation family, threshold
rule, or separator object. That would be a new object, not a direct continuation
of T424's Route-A index search.

## What this earns / does not earn

Earns: a bounded finite negative for the direct n>3 Route-A continuation of the
T423/T424 AND/strict-majority fixture.

Does not earn: a universal theorem about judgment aggregation, social choice,
index theory, physics, or finality; any claim-ledger movement; any cross-repo
evidential use.
