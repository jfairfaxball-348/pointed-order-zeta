# Session Log

## Session 1 — Scaffold

Date: 2026-09-25

Scope honored: scaffold only.

Created the project charter and repository structure. Frozen the initial \(\mathbf G_m\) residual-index statistic, the two-variable Euler product, the provisional prime-average transform, initial analytic domain, and the Kummer-field derivation target.

No comprehensive literature review, theorem claim, novelty claim, analytic continuation, generalisation, Lean work, or paper drafting was performed.

Exit state: **SCAFFOLD_COMPLETE**.

## Session 2 — Foundational derivation

Date: 2026-09-25

Scope honored: foundational derivation only. No comprehensive prior-art audit, novelty claim, full analysis near \(s=1\), elliptic/abelian generalisation, 1-motive/Hodge/motivic work, Lean work, or paper drafting was started.

Established from cyclic-group calculations that for \(p\nmid a\),
\[
n\mid I_a(p)
\iff
n\mid p-1\text{ and }a\bmod p\in(\mathbf F_p^\times)^n.
\]
The separate condition \(n\mid p-1\) is essential.

For fixed \(n\), proved that for \(p\nmid an\) this is equivalent to complete splitting in
\[
K_n(a)=\mathbf Q(\zeta_n,a^{1/n}).
\]
The non-perfect-power hypothesis and positivity of \(a\) are not needed for this individual criterion. Perfect-power effects and entanglement remain relevant to degree/tower formulas.

Invoked fixed-extension Chebotarev to obtain density \(1/[K_n(a):\mathbf Q]\) for each fixed \(n\), while explicitly separating this from the unresolved infinite-sum interchange.

Derived
\[
f(I_a(p))=\sum_{n\mid I_a(p)}(\mu*f)(n),
\]
and for \(f_z(n)=n^{-z}\),
\[
g_z(q^k)=q^{-kz}-q^{-(k-1)z}.
\]
Verified \(g_0=\varepsilon\) and \(g_z(n)\to\mu(n)\) pointwise for fixed \(n\) as \(z\to+\infty\).

Established elementary absolute convergence of the Euler product and logarithmic double series for \(z\ge0,\Re(s)>1\).

Added dependency-free exact computation for factorisation of \(p-1\), multiplicative order, residual index, and an independent modular \(n\)-th-power check. The test suite passes small prime/base checks and an exhaustive cyclic-group check through orders and exponents \(40\).

Most important unresolved issue:
\[
\operatorname{average}_p f(I_a(p))
\stackrel?=
\sum_{n\ge1}\frac{(\mu*f)(n)}{[K_n(a):\mathbf Q]}
\]
requires degree growth and a uniform tail/interchange theorem; fixed-\(n\) Chebotarev is insufficient.

Exit state: **FOUNDATIONS_PASS**.

Next session: source-level prior-art audit against the precise fixed-\(n\), Möbius, and Kummer-degree formulation established here.


## Session 3 — Prior-art / novelty audit

Date: 2026-09-25

Scope honored: source-level prior-art audit. No large computational experiment, full singularity proof, elliptic/abelian generalization, 1-motive/Hodge/motivic development, Lean work, or paper drafting was begun.

The audit found a major collision with established generalized-Artin theory.

Standard terminology was confirmed: \(I_a(p)\) is the **residual index**, and the condition \(I_a(p)=t\) is the **near-primitive-root problem of index \(t\)**.

Felix--Murty (2012), Lemma 2.1, states the fixed-\(n\) criterion
\[
n\mid i_a(p)
\iff
p\text{ splits completely in }\mathbf Q(\zeta_n,a^{1/n})
\]
as a classical result. Pappalardi (1995) gives the same base-\(2\) mechanism and attributes the splitting criterion to Dedekind.

Exact residual-index densities are established generalized-Artin objects. Wagstaff's result, as reproduced in Moree's *Near-Primitive Roots*, gives under GRH
\[
\delta(a,t)
=
\sum_{n\ge1}
\frac{\mu(n)}
{[\mathbf Q(\zeta_{nt},a^{1/(nt)}):\mathbf Q]}.
\]

The strongest collision is Felix--Murty (2012), Theorem 1.7. Under GRH and broad growth conditions on \(g\), for
\[
f(n)=\sum_{d\mid n}g(d)
\]
they prove an asymptotic for
\[
\sum_{p\le x}f(i_a(p))
\]
whose constant is
\[
c_{a,f}
=
\sum_{d\ge1}
\frac{g(d)}
{[\mathbf Q(\zeta_d,a^{1/d}):\mathbf Q]}.
\]
For the project weight \(f_z(n)=n^{-z}\), Session 2 proved \(|g_z(n)|\le1\) for every real \(z>0\). Therefore the proposed \(\Delta_a(z)\) is an immediate specialization of this theorem, under the same GRH hypothesis.

The degree issue from Session 2 is also standard. Felix--Murty Proposition 3.3 reproduces Wagstaff's exact formula
\[
[\mathbf Q(\zeta_n,a^{1/n}):\mathbf Q]
=
\frac{n\varphi(n)}
{\varepsilon(n)(n,h)}
\]
with explicit perfect-power, sign, discriminant, and \(2\)-adic corrections, and Corollary 3.4 gives
\[
[\mathbf Q(\zeta_n,a^{1/n}):\mathbf Q]
\asymp_a n\varphi(n).
\]
Hence the project's \(g_z\)-degree series converges absolutely for fixed real \(z>0\).

Akbary--Fakhari (2024) explicitly formulates the same generalized-Artin constant and develops product/character-sum expressions for multiplicative \(g\). Lenstra--Moree--Stevenhagen (2014) provides the controlling interpretation of entanglement as a correction for dependencies among local splitting fields/Galois images.

No direct primary source was located for the exact two-variable product
\[
Z_a(s,z)
=
\prod_{p\nmid a}(1-I_a(p)^{-z}p^{-s})^{-1}.
\]
However, its definition for \(\Re(s)>1\) is routine packaging, and the leading real \(s\to1^+\) logarithmic coefficient is strongly constrained by Felix--Murty's weighted prime asymptotic plus standard partial summation. Finite-Galois Frobenian/Chebotarev Euler-product theory exhibits the same mean-to-exponent mechanism, although the project weight depends on the full Kummer tower and is not shown to factor through a fixed finite Galois extension.

The project is therefore reframed around a stronger analytic question: whether
\[
H_a(s,z)
=
Z_a(s,z)\zeta(s)^{-\Delta_a(z)}
\]
has genuinely nontrivial holomorphic/nonvanishing continuation, complex-\(z\) structure, or a convergent Artin/Dedekind-\(L\) factorization from the infinite Kummer tower.

The word “spectrum” is demoted. At the \(\mathbf G_m\) mean-value level, \(\Delta_a(z)\) is more naturally a Dirichlet/Mellin transform of the residual-index distribution, equivalently a Laplace transform of \(\log I_a(p)\).

Required outputs created:

- `notes/prior-art-matrix.md`
- `notes/literature.md`
- `literature/bibliography.bib`

Exit state: **PRIOR_ART_REFRAME**.

Next session: proceed only in reframed form. Treat Felix--Murty Theorem 1.7 as controlling input and investigate the analytic infinite-Kummer Euler-product layer rather than rediscovering \(\Delta_a(z)\).


## Session 4 — Reframed computational / analytic pilot

Date: 2026-09-26

Scope honored: analytic reduction and reproducible computation only. The Session-3 generalized-Artin collision was treated as controlling input. No elliptic/abelian generalisation, Lean work, paper drafting, or deep continuation theorem was started.

The logarithm was decomposed as
\[
\log Z_a(s,z)=P_a(s,z)+R_a(s,z),
\]
with
\[
P_a(s,z)=\sum_{p\nmid a}I_a(p)^{-z}p^{-s}.
\]
For real \(z\ge0\), locally uniform absolute convergence proves that \(R_a(s,z)\) is holomorphic on \(\Re(s)>1/2\).

Writing \(P(s)=\sum_p p^{-s}\) and
\[
Q_a(s,z)=P_a(s,z)-\Delta_a(z)P(s),
\]
Session 4 obtained the exact identity
\[
\log H_a(s,z)
=
Q_a(s,z)+R_a(s,z)-\Delta_a(z)R_\zeta(s)
\]
in \(\Re(s)>1\), where \(R_\zeta=\log\zeta-P\) is also holomorphic for \(\Re(s)>1/2\). Thus the difficult analytic information is concentrated in the centered prime series \(Q_a\).

In the source-matched positive-base setup, Felix--Murty Theorem 1.7 supplies under GRH an error \(O(x/(\log x)^\beta)\) for every fixed \(\beta<2\). Choosing \(\beta>1\), partial summation shows that \(Q_a(s,z)\) has a finite continuous boundary value on \(\Re(s)=1\). Hence
\[
H_a(s,z)=Z_a(s,z)\zeta(s)^{-\Delta_a(z)}
\]
has a finite positive real limit as \(s\to1^+\), and therefore
\[
Z_a(s,z)\sim C_a(z)(s-1)^{-\Delta_a(z)}.
\]
This is a Level-1 real boundary statement only. The known logarithmic error does not supply differentiability at \(s=1\) or continuation into any open half-plane \(\Re(s)<1\).

For real \(z>0\), \(\Re(s)>1\), the Kummer-indicator expansion was shown to interchange absolutely with the prime sum using the divisor-support bound \(\sum_{n\mid I}|g_z(n)|\le\tau(I)\). At each fixed Kummer level, regular-character orthogonality gives an exact finite-Galois decomposition of the completely-split prime series into logarithms of Artin \(L\)-functions, equivalently a normalized \(\log\zeta_{K_n}\), plus ramified and higher-prime-power corrections. However, naively separating these expressions over the infinite tower loses the original divisor-support convergence mechanism; degree growth alone does not justify the resulting infinite \(L\)-product.

The exact computational engine was extended and validated by 13 passing unit tests. With default cutoffs \(X=10^6\) and \(N=5\times10^5\), empirical prime means for \(a=2,3,5,6,10\) and \(z=0,1/2,1,2,4,8\) track the Kummer-degree predictions at roughly \(10^{-4}\) to \(10^{-3}\), with \(a=10\) showing slower convergence near \(2\times10^{-3}\). Matched-cutoff normalized logarithms are stable to about \(10^{-3}\) across the tested cutoffs. No stable secondary term or Level-2/Level-3 continuation signal was found.

Complex-z diagnostics were also implemented. Independently of the prime-mean problem, the positive non-perfect-power Kummer degree series was proved absolutely and locally uniformly convergent for \(\Re(z)>-1\). No complex-z weighted-prime theorem was claimed.

Strongest collapse: the Level-1 normalization of the frozen Euler product is routine once the Felix--Murty weighted prime asymptotic is accepted, and the \(k\ge2\) Euler-product layer is analytically harmless for \(\Re(s)>1/2\).

Replacement analytic object:
\[
\boxed{Q_a(s,z)=P_a(s,z)-\Delta_a(z)P(s).}
\]

Required outputs created:

- notes/analytic-pilot.md
- notes/computational-pilot.md
- src/analytic_pilot.py
- scripts/run_analytic_pilot.py

Exit state: **ANALYTIC_PILOT_REFRAME**.

Next session: proceed only in reframed mathematical-proof form. The theorem-sized target is whether \(Q_a(s,z)\) admits holomorphic continuation to any half-plane crossing \(\Re(s)=1\), and whether the finite-level Artin/Dedekind-\(L\) identities can be reorganized uniformly over the Kummer tower. Do not re-open the Level-1 boundary asymptotic as a novelty target.
