# Roadmap

This repository is gate-driven. Attractive numerical patterns or familiar-looking formulas do not authorize skipping phases.

## 0. SCAFFOLD — complete

Create the research charter, frozen starting definitions, state machine, plans, question log, terminology log, and empty implementation/data/literature/experiment areas.

Exit state: **SCAFFOLD_COMPLETE**.

## 1. FOUNDATIONAL DERIVATION

Verify all elementary identities independently. Derive the relation between residual-index divisibility and splitting in
\[
K_n(a)=\mathbf Q(\zeta_n,a^{1/n})
\]
with every needed restriction stated explicitly. Derive the Möbius-inversion formula rather than importing it as folklore. Add exact small-case executable checks.

Required output: `notes/foundational-derivation.md`.

Allowed exits: `FOUNDATIONS_PASS`, `FOUNDATIONS_NEED_REPAIR`, `OBJECT_COLLAPSES`.

## 2. PRIOR-ART / NOVELTY AUDIT

Only after foundations pass. Search generalized Artin, residual-index distributions, near-primitive roots, Chebotarev/Kummer machinery, weighted Frobenian Euler products, prime-set zeta functions, general functions of residual index, and algebraic-group analogues.

Maintain source-level theorem matching, not abstract-level similarity.

Required outputs: `notes/prior-art-matrix.md`, `notes/literature.md`, `literature/bibliography.bib`.

## 3. COMPUTATIONAL PILOT

Implement exact multiplicative orders via factorization of \(p-1\); compute residual indices, empirical spectra, Kummer-sum comparisons when justified, and finite-prime approximations to \(\log Z_a(s,z)\).

Computation is diagnostic evidence, never proof.

## 4. STRUCTURAL CONJECTURE DISCOVERY

Only after foundations, prior art, and computation. Formulate surviving conjectures precisely, record counterexamples, and actively test alternative transforms of the residual index.

## 5. MATHEMATICAL PROOF

Attempt proofs only for claims that survive the previous gates. Separate unconditional statements from statements depending on GRH, Chebotarev error terms, or other hypotheses.

## 6. GENERALISATION TO ALGEBRAIC GROUPS

Only after the \(\mathbf G_m\) case is understood. Investigate \((E,P)\), \((A,P)\), and pointed semiabelian varieties, including whether subgroup index is actually the correct invariant.

## 7. LEAN / FORMALISATION — only where suitable

Formalize stable, well-scoped results only. Do not use formalization to manufacture confidence in unsettled definitions or novelty.

## 8. ADVERSARIAL NOVELTY AUDIT

Attack every remaining novelty claim with broader terminology, adjacent literatures, equivalent formulations, and expert-level source comparison.

## 9. PAPER

No paper work begins merely because a pilot looks positive. Writing follows stable mathematics and a defensible novelty audit.

## Pilot outcomes

At the end of the pilot, use exactly one of:

- `PILOT_COLLAPSED`
- `PILOT_REFRAMED`
- `PILOT_POSITIVE`
- `PILOT_INCONCLUSIVE`
