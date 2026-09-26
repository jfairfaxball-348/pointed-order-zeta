# Pointed Order Zeta: Artin–Kummer Spectra of Reduction Orders

**Status: ANALYTIC_PILOT_REFRAME**

This is a high-risk object-discovery project. Novelty is not assumed, and the Session-3 prior-art conclusions remain controlling.

## Frozen starting object

Let \(a\in\mathbf Z\setminus\{0,\pm1\}\), initially not a perfect power. For \(p\nmid a\),
\[
I_a(p)=\frac{p-1}{\operatorname{ord}_p(a)}
=[\mathbf F_p^\times:\langle a\bmod p\rangle].
\]
The frozen Euler product is
\[
Z_a(s,z)=\prod_{p\nmid a}(1-I_a(p)^{-z}p^{-s})^{-1},
\qquad z\ge0,\quad \Re(s)>1.
\]
The prime-average transform is
\[
\Delta_a(z)=\lim_{x\to\infty}\frac1{\pi(x)}
\sum_{\substack{p\le x\\p\nmid a}}I_a(p)^{-z},
\]
whenever the limit exists.

These definitions are unchanged by Session 4.

## What Sessions 2–3 established

For fixed \(n\) and \(p\nmid an\),
\[
n\mid I_a(p)
\iff
p\text{ splits completely in }K_n(a)=\mathbf Q(\zeta_n,a^{1/n}).
\]
The residual index, fixed residual-index densities, general weighted averages \(f(I_a(p))\), the Möbius/Kummer degree constant, and \(\Delta_a(z)\) for fixed real \(z>0\) under the relevant GRH hypotheses are established generalized-Artin territory. Felix--Murty is the controlling weighted source; Wagstaff controls the degree formula; Akbary--Fakhari controls product/entanglement structure of the constants.

The word “spectrum” is therefore only informal project shorthand.

## Session-4 analytic reduction

Write
\[
P_a(s,z)=\sum_{p\nmid a}I_a(p)^{-z}p^{-s}
\]
and
\[
R_a(s,z)=\sum_{p\nmid a}\sum_{k\ge2}
\frac{I_a(p)^{-zk}}{k p^{ks}}.
\]
For real \(z\ge0\), \(R_a\) is holomorphic for \(\Re(s)>1/2\).

Let \(P(s)=\sum_p p^{-s}\) be the prime zeta function and define
\[
\boxed{Q_a(s,z)=P_a(s,z)-\Delta_a(z)P(s).}
\]
Then, in \(\Re(s)>1\),
\[
\log\bigl(Z_a(s,z)\zeta(s)^{-\Delta_a(z)}\bigr)
=
Q_a(s,z)
+
\text{a function holomorphic for }\Re(s)>1/2.
\]
Thus \(Q_a\), rather than the bare Euler-product packaging, is the preferred surviving analytic object.

In the source-matched positive-base setting, Felix--Murty's GRH-conditional weighted error has exponent \(\beta>1\). Partial summation therefore proves that
\[
H_a(s,z)=Z_a(s,z)\zeta(s)^{-\Delta_a(z)}
\]
has a finite positive real limit as \(s\to1^+\). Equivalently,
\[
Z_a(s,z)\sim C_a(z)(s-1)^{-\Delta_a(z)}.
\]
This is only a Level-1 real boundary asymptotic. It does not prove holomorphic continuation through \(s=1\).

## Session-4 computational pilot

The exact Session-2 arithmetic code has been extended with sieve-backed prime/factor data, exact residual indices, prime Dirichlet sums, logarithmic Euler products, the source-matched positive non-perfect-power Kummer degree formula, complex-z diagnostics, and matched-cutoff normalization.

Default reproducible pilot parameters are \(X=10^6\) and \(N=5\times10^5\), with bases \(2,3,5,6,10\). The full unit-test suite has 13 passing tests. Results and reproducibility details are in notes/computational-pilot.md.

## What survives

At fixed Kummer level, the completely-split prime series has the standard finite-Galois character decomposition into Artin/Dedekind \(L\)-functions. For real \(z>0\), the Kummer-indicator expansion can also be interchanged absolutely with the prime sum in \(\Re(s)>1\).

The unresolved difficulty is tower-level: after separating the finite-level \(L\)-function expressions, the original divisor-support convergence is lost, and degree growth alone does not justify an infinite \(L\)-product.

The theorem-sized next question is whether, under a precise hypothesis package,
\[
Q_a(s,z)
\]
admits holomorphic continuation to any half-plane \(\Re(s)>1-\delta\) with \(\delta>0\), perhaps through a uniformly controlled Kummer-tower \(L\)-function or logarithmic-derivative expansion.

## Research gates

0. SCAFFOLD — complete: SCAFFOLD_COMPLETE  
1. FOUNDATIONAL DERIVATION — complete: FOUNDATIONS_PASS  
2. PRIOR-ART / NOVELTY AUDIT — complete: PRIOR_ART_REFRAME  
3. REFRAMED COMPUTATIONAL / ANALYTIC PILOT — complete: ANALYTIC_PILOT_REFRAME  
4. NEXT PROOF / STRUCTURAL SESSION — only in reframed form around \(Q_a(s,z)\)  
5. GENERALISATION — deferred  
6. LEAN / FORMALISATION — deferred  
7. ADVERSARIAL NOVELTY AUDIT — later  
8. PAPER — later

## Current exit state

**ANALYTIC_PILOT_REFRAME**

The frozen Euler product remains useful notation, but Session 4 found that its Level-1 boundary behavior collapses to a standard consequence of the known weighted prime asymptotic. The centered weighted prime Dirichlet series \(Q_a(s,z)\) is now the preferred analytic target. No novelty claim is made for that target.
