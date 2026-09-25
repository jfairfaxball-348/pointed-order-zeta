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
