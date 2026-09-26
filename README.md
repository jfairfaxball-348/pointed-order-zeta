# Pointed Order Zeta: Artin–Kummer Spectra of Reduction Orders

**Status: CONTINUATION_PROOF_OBSTRUCTED**

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

These definitions are unchanged by Sessions 4–5.

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
P_a(s,z)=\sum_{p\nmid a}I_a(p)^{-z}p^{-s},
\]
and let
\[
P(s)=\sum_p p^{-s}.
\]
Session 4 isolated
\[
\boxed{Q_a(s,z)=P_a(s,z)-\Delta_a(z)P(s)}
\]
as the difficult prime-supported analytic object. The \(k\ge2\) part of \(\log Z_a\) is holomorphic for \(\Re(s)>1/2\).

In the source-matched positive-base setting, Felix--Murty's GRH-conditional weighted error gives a finite right boundary value of \(Q_a\) at \(s=1\), hence
\[
Z_a(s,z)\sim C_a(z)(s-1)^{-\Delta_a(z)}
\qquad(s\to1^+).
\]
This is Level 1 only. It does not imply differentiability or complex continuation through \(s=1\).

## Session-5 proof analysis

For proofs, it is cleaner to use the omitted-prime equivalent
\[
Q_a^\circ(s,z)
=
\sum_{p\nmid a}
\bigl(I_a(p)^{-z}-\Delta_a(z)\bigr)p^{-s},
\]
since
\[
Q_a(s,z)
=
Q_a^\circ(s,z)
-
\Delta_a(z)\sum_{p\mid a}p^{-s}.
\]

In \(\Re(s)>1\), Session 5 proved the exact absolutely convergent centered Kummer expansion
\[
Q_a^\circ(s,z)
=
\sum_{n\ge1}g_z(n)
\left(
S_{a,n}(s)-\frac1{[K_n(a):\mathbf Q]}P_a^\circ(s,0)
\right).
\]

For a finite Galois extension \(K/\mathbf Q\), define
\[
C_K(s)
=
P_{\rm split}(s;K)-\frac1{[K:\mathbf Q]}P(s).
\]
Regular-character orthogonality cancels the trivial character exactly, and
\[
\boxed{
C_K(s)
=
\frac1{[K:\mathbf Q]}
\log\!\left(\frac{\zeta_K(s)}{\zeta(s)}\right)
-
B_K(s),
}
\]
where \(B_K\) is holomorphic for \(\Re(s)>1/2\). By Aramata--Brauer, every fixed centered level continues through a neighborhood of \(s=1\) unconditionally; under Dedekind GRH it is holomorphic for \(\Re(s)>1/2\).

For positive non-perfect-power \(a\),
\[
\log|\operatorname{Disc}(K_n(a))|
\le
[K_n(a):\mathbf Q](3\log n+\log a),
\]
and the source-matched GRH Chebotarev estimate is
\[
\pi_n(x)
=
\frac{\operatorname{li}(x)}{[K_n(a):\mathbf Q]}
+
O_a(\sqrt{x}\log(nx)).
\]
Consequently, on compact subsets of \(\Re(s)>1/2\),
\[
C_{K_n(a)}(s)=O_{a,\Omega}(\log(2n)).
\]

This is the decisive obstruction: on prime levels \(q\),
\[
|g_z(q)|=1-q^{-z}\to1,
\]
so the available continued finite-level bound is not summable over the tower. A moving truncation also stops at the known logarithmic error because the prime-supported large-divisor tail has no available power-saving estimate at a power-sized cutoff.

The logarithmic derivative removes branch choices but does not improve tower convergence. No Level-2 or Level-3 continuation of the full \(Q_a\) is proved, and no natural-boundary claim is made.

Detailed proof analysis is in notes/continuation-proof.md.

## Session-4 computational pilot

The exact arithmetic engine contains sieve-backed prime/factor data, exact residual indices, prime Dirichlet sums, logarithmic Euler products, the source-matched positive non-perfect-power Kummer degree formula, complex-\(z\) diagnostics, and matched-cutoff normalization.

Default reproducible pilot parameters are \(X=10^6\) and \(N=5\times10^5\), with bases \(2,3,5,6,10\). The full unit-test suite has 13 passing tests. Results and reproducibility details are in notes/computational-pilot.md.

Session 5 made no code changes because the decisive obstruction is analytic rather than numerical.

## What survives

The primary analytic object remains \(Q_a(s,z)\), with \(Q_a^\circ(s,z)\) preferred for proof bookkeeping.

The theorem-sized surviving problem is now narrower:

> Can one prove a power-saving **tower-averaged centered Kummer discrepancy**, preserving the original divisor-support structure, rather than summing termwise continued finite-level \(L\)-function bounds?

A successful result would need cancellation across \(n\), a power-saving estimate for the large-divisor prime tail, or a different argument that avoids tower separation.

## Research gates

0. SCAFFOLD — complete: SCAFFOLD_COMPLETE  
1. FOUNDATIONAL DERIVATION — complete: FOUNDATIONS_PASS  
2. PRIOR-ART / NOVELTY AUDIT — complete: PRIOR_ART_REFRAME  
3. REFRAMED COMPUTATIONAL / ANALYTIC PILOT — complete: ANALYTIC_PILOT_REFRAME  
4. REFRAMED MATHEMATICAL PROOF — complete: CONTINUATION_PROOF_OBSTRUCTED  
5. NEXT PROOF SESSION — only in reframed form around tower-averaged power-saving discrepancy  
6. GENERALISATION — deferred  
7. LEAN / FORMALISATION — deferred  
8. ADVERSARIAL NOVELTY AUDIT — later  
9. PAPER — later

## Current exit state

**CONTINUATION_PROOF_OBSTRUCTED**

The continuation target remains substantive, but the natural Kummer/Chebotarev/\(L\)-function route is rigorously blocked at the tower-summation step by nonsummable finite-level bounds and only logarithmic control of the divisor-supported tail. This is a method obstruction, not a theorem of non-continuation.
