# Consensus-Record Theorem Transfer Results

Result: T20 focused tests pass `6/6`.

## Dictionary

T20 defines a typed dictionary:

| Distributed term | Physical-record term | Preserved structure |
| --- | --- | --- |
| process local state | observer-local finality domain | bounded local view |
| message or commit certificate | record fragment or environmental witness | portable evidence |
| quorum intersection | redundant-holder overlap | shared support blocks contradiction |
| fork or conflicting commit | incompatible finality sections | local commitments may fail to globalize |
| safety | no contradictory stabilized records | exclusion of incompatible final facts |
| liveness | record-amplification progress | eventual availability under bounded conditions |
| adversarial delay | bounded causal access or decoherence lag | reconciliation limits |

## Theorem Transfer

Source theorem:

```text
In a quorum system with 2q > n and locally consistent processes,
two conflicting commit certificates cannot both be valid.
```

Transferred theorem:

```text
In a physical record system with redundant-holder threshold 2q > n
and locally consistent record fragments, two incompatible classical
records cannot both be finalized.
```

The proof structure is preserved:

1. Every final certificate contains at least `q` holders.
2. If `2q > n`, any two final certificates intersect.
3. A shared locally consistent holder cannot certify incompatible values.
4. Therefore incompatible certificates cannot both be final.

## Positive Cases

Consensus case:

```text
n = 5
q = 3
commit_A holders = {n1, n2, n3}
commit_B holders = {n3, n4, n5}
intersection = {n3}
```

Physical-record case:

```text
n = 5
q = 3
spin_up holders = {e1, e2, e3}
spin_down holders = {e3, e4, e5}
intersection = {e3}
D1 profile for each certificate = (3, 3, 1, 3)
```

The same proof blocks contradictory finalization in both cases.

## Boundary Cases

Weak quorum:

```text
n = 4
q = 2
spin_up holders = {e1, e2}
spin_down holders = {e3, e4}
intersection = {}
```

The theorem does not apply because `2q > n` fails.

Contextual/global-section boundary:

```text
A = B
B = C
A != C
```

Each local relation has a quorum certificate, but no global assignment exists.
This is the T13-style warning: quorum safety can block two contradictory
certificates, but it does not prove that all locally certified records glue
into a global finality section.

## Verdict

T20 supports the narrow claim:

```text
some distributed-systems theorems transfer into physical-record finality
when their assumptions are restated as holder, certificate, and consistency
conditions.
```

It rejects the broad claim:

```text
all consensus results automatically become physics theorems.
```

## Reproduction

```bash
python -m unittest tests.test_consensus_record_theorem_transfer -v
python -m models.run_t20
```

Machine-readable output:

- [consensus-record-theorem-transfer-v0.1.json](consensus-record-theorem-transfer-v0.1.json)
