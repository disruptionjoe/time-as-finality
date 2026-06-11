# Proof-Carrying Metastable Finality Laboratory

## Research Question

Does combining coarse-graining, bounded proof verification, and Snowball-style
repeated sampling produce a richer finality structure than static trace
persistence, ordinary redundancy, Bayesian evidence aggregation, or local
majority metastability?

T9 is the baseline. It studies whether local dynamics produce persistent
counterfactual traces. T10 studies what a population of bounded reconcilers can
do with hidden, coarse-grained records.

## Hidden State And Coarse-Graining

The hidden state is a nine-bit vector divided into three blocks of three bits.
Each block is mapped to its majority bit, and the public binary claim is the
majority of those three block values:

```text
nine-bit microstate
  -> three block-majority bits
  -> one binary macro claim
```

The complete state space contains 512 microstates. Exactly 256 map to each
claim, so revealing only the claim hides eight bits under the uniform model.

This is an explicit coarse-graining, not a claim that this particular map is
physically privileged.

## Proof Functionality

The implementation uses an ideal proof functionality. It issues a certificate
only when a hidden microstate satisfies the coarse-graining relation. A public
certificate exposes:

- epoch;
- binary claim;
- independent support count;
- opaque commitment and proof identifiers.

It does not expose the microstate. Certificates can be recursively merged
while counting unique sources, so duplicate evidence cannot increase support.

This models completeness, sound verification, bounded disclosure, and
proof-carrying aggregation. It is not a secure ZK construction and makes no
cryptographic performance claim.

## Record Population

Honest agents receive noisy local copies of one global microstate. Their
certificates prove that the reported macro claim matches their own hidden
record, not that their record perfectly matches the global state.

Two adversary classes are compared:

1. **forged opposition:** false claims carry invalid certificates;
2. **valid dissent:** false claims carry valid certificates for genuinely
   conflicting hidden records.

The second class is essential. Proof validity is not truth.

## Snowball Process

Each non-Byzantine agent repeatedly samples seven peers. A poll succeeds when
five responses support one candidate. Agents accumulate candidate confidence
and decide after four consecutive successful polls for the same candidate.

In proof mode:

- invalid responses are rejected;
- adopted preferences carry recursively merged evidence;
- public support counts unique hidden sources.

The protocol uses rounds as algorithmic steps. T10 does not derive physical
time from them.

## Baselines

The same generated records are evaluated with:

1. **static trace persistence:** records remain present but do not reconcile;
2. **ordinary redundancy:** one-shot majority of valid leaf claims;
3. **Bayesian MAP:** independent equal-reliability reports under a stated
   sensor model;
4. **proofless local-majority dynamics:** repeated sampling without proof
   verification or confidence memory;
5. **raw Snowball:** confidence accumulation without certificate checking.

## Falsification Criteria

The stronger proposal fails if:

- proof verification cannot outperform raw sampling against forged evidence;
- proofs incorrectly filter valid but conflicting records;
- Snowball confidence is treated as evidence of truth;
- the combination never separates support, verification, confidence, and
  coarse-grained reversal structure;
- its epistemic performance is no better than an ordinary Bayesian baseline;
- protocol metastability is presented as a physical law.

## Reproduction

```bash
python -m unittest discover -s tests -p "test_*.py" -v
python -m models.run_proof_carrying_finality
```
