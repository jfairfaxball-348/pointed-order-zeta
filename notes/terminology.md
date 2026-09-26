# Terminology

## Standard mathematical terms

**multiplicative order** — \(\operatorname{ord}_p(a)\), the order of \(a\bmod p\) in \(\mathbf F_p^\times\).

**residual index** — \(I_a(p)=(p-1)/\operatorname{ord}_p(a)\), equivalently the index of \(\langle a\bmod p\rangle\) in \(\mathbf F_p^\times\). Common notation in the literature includes \(i_a(p)\) and \(r_g(p)\).

**near-primitive root of index \(t\)** — standard terminology for \(I_a(p)=t\).

**generalized Artin problem** — weighted/generalized questions involving sums such as \(\sum_{p\le x}f(i_a(p))\) and their Kummer-degree constants.

**Kummer field / radical-cyclotomic field** — in this project,
\[
K_n(a)=\mathbf Q(\zeta_n,a^{1/n}).
\]

**entanglement** — dependencies among local radical/cyclotomic splitting fields or the associated profinite Galois image that obstruct naive independence and produce correction factors.

**prime zeta function** —
\[
P(s)=\sum_p p^{-s},\qquad \Re(s)>1.
\]
Do not treat it as entire or analytically harmless outside its initial domain.

**Frobenian function** — use in the standard fixed finite-Galois sense. The full weight \(p\mapsto I_a(p)^{-z}\) is not established to factor through one fixed finite Galois extension.

## Project analytic terminology after Session 4

**weighted prime Dirichlet series** —
\[
P_a(s,z)=\sum_{p\nmid a}I_a(p)^{-z}p^{-s}.
\]
Session 4 identifies this as carrying the difficult \(k=1\) analytic information.

**centered weighted prime Dirichlet series** — preferred name for the surviving analytic object
\[
\boxed{Q_a(s,z)=P_a(s,z)-\Delta_a(z)P(s).}
\]
This is now preferred over the bare Euler product for continuation questions.

**two-variable weighted Euler product** — safe descriptive term for
\[
Z_a(s,z)=\prod_{p\nmid a}(1-I_a(p)^{-z}p^{-s})^{-1}.
\]
It remains useful packaging, not a novelty claim.

**normalized Euler product** —
\[
H_a(s,z)=Z_a(s,z)\zeta(s)^{-\Delta_a(z)}.
\]
Session 4 shows that, in \(\Re(s)>1\), \(\log H_a\) differs from \(Q_a\) by a term holomorphic for \(\Re(s)>1/2\). Thus \(H_a\) is useful but not the most fundamental surviving object.

**matched-cutoff normalization** — numerical procedure in which the truncated \(Z_{a,X}\) is normalized by the zeta Euler product truncated at the same prime cutoff. This avoids an artificial omitted-prime-tail bias. It is a computational convention, not a new analytic object.

**Level 1 — real boundary asymptotic** — a one-sided statement such as
\[
Z_a(s,z)\sim C_a(z)(s-1)^{-\Delta_a(z)},\qquad s\to1^+.
\]
For the source-matched positive-base case, Session 4 obtains this conditionally from Felix--Murty plus partial summation.

**Level 2 — local complex factorization** — holomorphic/nonvanishing factorization in a punctured complex neighborhood crossing \(s=1\). Not established.

**Level 3 — half-plane/global continuation** — continuation to \(\Re(s)>\theta\) with \(\theta<1\). Not established.

## Terms to retire or demote

**Artin--Kummer order spectrum / order spectrum** — do not use as established terminology for \(\Delta_a(z)\). Preferred descriptions are:

- **Dirichlet transform of the residual-index distribution**;
- **Mellin transform of the discrete residual-index distribution**;
- equivalently, **Laplace transform of \(\log I_a(p)\)**.

**spectrum** — retain only as informal project shorthand.

## Terms to use cautiously

**zeta function** — acceptable as project packaging because of the Euler product, but it does not imply analytic continuation, functional equation, or standard zeta-function status.

**fractional pole** — avoid unless a genuine local complex factorization is proved. The Level-1 real exponent is not a meromorphic pole theorem.

**branch-type singularity** / **natural boundary** — possible future analytic behavior, not established.

**novel Euler product** / **novel spectrum** / **new Artin constant** — forbidden by the prior-art audit.

**motivic** / **Hodge-theoretic** — deferred until a genuine realization-theoretic construction requires them.
