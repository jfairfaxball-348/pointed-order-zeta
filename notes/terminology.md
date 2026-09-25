# Terminology

## Standard mathematical terms confirmed by Session 3

**multiplicative order** — \(\operatorname{ord}_p(a)\), the order of \(a\bmod p\) in \(\mathbf F_p^\times\).

**residual index** — \(I_a(p)=(p-1)/\operatorname{ord}_p(a)\), equivalently the index of \(\langle a\bmod p\rangle\) in \(\mathbf F_p^\times\). This terminology is standard in the Artin/near-primitive-root literature; common notation includes \(i_a(p)\) and \(r_g(p)\).

**near-primitive root of index \(t\)** — standard terminology for the condition that a fixed \(g\) has order \((p-1)/t\) modulo \(p\), equivalently residual index \(t\). Use this when discussing the exact-index layer \(I_a(p)=t\).

**generalized Artin problem** — terminology used for weighted/generalized questions involving sums such as
\[
\sum_{p\le x}f(i_a(p))
\]
and the associated Kummer-degree constants.

**Kummer field / radical-cyclotomic field** — in this project,
\[
K_n(a)=\mathbf Q(\zeta_n,a^{1/n}).
\]
The fixed-\(n\) splitting criterion for residual-index divisibility is standard generalized-Artin machinery.

**entanglement** — dependencies among local radical/cyclotomic splitting fields or the associated profinite Galois image that obstruct naive independence and produce correction factors. Do not use “entanglement” for an exception to the individual fixed-\(n\) splitting criterion.

**Frobenian function** — use carefully in the standard finite-Galois sense: a function on primes determined by Frobenius conjugacy classes in a fixed finite Galois extension. The weight \(p\mapsto I_a(p)^{-z}\) is not established to be Frobenian in this finite-extension sense because it uses the full Kummer tower.

## Project terms after the Session-3 audit

**Pointed Order Zeta** — project name, not a novelty claim.

**two-variable weighted Euler product** — safe descriptive term for
\[
Z_a(s,z)
=
\prod_{p\nmid a}
(1-I_a(p)^{-z}p^{-s})^{-1}.
\]
No direct source for this exact product was located in Session 3, but nonappearance is not evidence of novelty.

**normalized Euler product** — provisional notation
\[
H_a(s,z)
=
Z_a(s,z)\zeta(s)^{-\Delta_a(z)}
\]
for the reframed analytic question. This is a research target, not an established standard object.

## Terms to retire or demote

**Artin--Kummer order spectrum / order spectrum** — do not use as established terminology for \(\Delta_a(z)\). Session 3 found that the mean is an immediate specialization of a general \(f(i_a(p))\) theorem and is more naturally described as a transform of the residual-index distribution.

**spectrum** — retain only, if at all, as informal project shorthand. There is no operator-theoretic, scheme-theoretic, or otherwise standard spectral structure established here.

Preferred descriptions of
\[
\Delta_a(z)
\]
are:

- **Dirichlet transform of the residual-index distribution**;
- **Mellin transform of the discrete residual-index distribution**;
- equivalently, **Laplace transform of \(\log I_a(p)\)**.

## Terms to use cautiously

**zeta function** — acceptable as project packaging because of the Euler product, but it does not imply analytic continuation, functional equation, or standard zeta-function status.

**fractional pole** — avoid unless a precise local analytic model is proved. A leading real logarithmic exponent from a mean value is not by itself a meromorphic pole theorem.

**branch-type singularity** — possible analytic behavior, not established.

**novel Euler product** / **novel spectrum** / **new Artin constant** — forbidden by the Session-3 audit.

**motivic** / **Hodge-theoretic** — do not use as significance language until a genuine realization-theoretic construction requires it.
