# Open Questions

This is a live question bank, not a conjecture list.

## Foundational — resolved in Session 2

- For \(p\nmid a\),
  \[
  n\mid I_a(p)\iff n\mid p-1\text{ and }a\bmod p\in(\mathbf F_p^\times)^n.
  \]
- For fixed \(n\) and \(p\nmid an\),
  \[
  n\mid I_a(p)\iff p\text{ splits completely in }K_n(a)=\mathbf Q(\zeta_n,a^{1/n}).
  \]
- The non-perfect-power hypothesis is not needed for the individual splitting equivalence; it affects degree formulas and later constants.
- Entanglement is not an exception to the fixed-\(n\) criterion.

## Prior art — resolved or substantially resolved in Session 3

- Residual index and exact residual-index densities are standard generalized-Artin / near-primitive-root objects.
- General \(f(I_a(p))\) averages and the Möbius/Kummer degree constant are controlled by the weighted-Hooley/generalized-Artin literature.
- For fixed real \(z>0\), \(\Delta_a(z)\) is an immediate specialization of Felix--Murty Theorem 1.7 under their GRH hypotheses in the source-matched positive-base setup.
- Wagstaff's degree formula gives \([K_n(a):\mathbf Q]\asymp_a n\varphi(n)\) and hence absolute convergence of the real-\(z\) degree series.
- The word “spectrum” remains informal project shorthand rather than established terminology.

## Analytic pilot — resolved in Session 4

- **Does the Felix--Murty error already prove a finite real normalization?** Yes. For any fixed \(1<\beta<2\), their source-matched weighted theorem gives a discrepancy \(D_z(x)=O(x/(\log x)^\beta)\). Partial summation gives a finite continuous boundary value for
  \[
  Q_a(s,z)=P_a(s,z)-\Delta_a(z)P(s)
  \]
  on \(\Re(s)=1\). Consequently, under the same GRH hypotheses,
  \[
  H_a(s,z)=Z_a(s,z)\zeta(s)^{-\Delta_a(z)}
  \]
  has a finite positive real limit as \(s\to1^+\).
- **Does that error give differentiability at \(s=1\)?** Not by this argument. One derivative would require an integrable extra \(\log x\), hence an error stronger than \(x/(\log x)^{2+\eta}\); Felix--Murty supplies exponents strictly below \(2\) in this specialization.
- **Does it give complex continuation across \(\Re(s)=1\)?** No. A fixed logarithmic saving gives a boundary statement, not a half-plane crossing. A power-saving discrepancy \(O(x^\theta)\), \(\theta<1\), would be of the right form for Mellin continuation to \(\Re(s)>\theta\).
- **Is the \(k\ge2\) remainder hard?** No. For real \(z\ge0\), it is holomorphic for \(\Re(s)>1/2\).
- **Is prime-zeta normalization cleaner?** Yes. In \(\Re(s)>1\),
  \[
  \log H_a(s,z)=Q_a(s,z)+R_a(s,z)-\Delta_a(z)R_\zeta(s),
  \]
  and the second bracket is holomorphic for \(\Re(s)>1/2\).
- **Can the Kummer indicator expansion be interchanged with the prime sum?** Yes for real \(z>0\), \(\Re(s)>1\), by absolute convergence using
  \[
  \sum_{n\mid I}|g_z(n)|\le \tau(I).
  \]
- **Can a fixed Kummer level be expressed using \(L\)-functions?** Yes. Regular-character orthogonality expresses the completely-split indicator, hence the prime series, through finite sums of \(\log L(s,\chi)\), equivalently \([K:\mathbf Q]^{-1}\log\zeta_K(s)\), plus ramified/prime-power corrections.
- **Does degree growth alone justify summing those separated \(L\)-expressions over the tower?** No. The reorganization loses the divisor-support convergence mechanism; a new uniform estimate or cancellation mechanism is required.
- **What does complex \(z\) add at the degree-series level?** For positive non-perfect-power \(a\), the Kummer degree series converges absolutely and locally uniformly for \(\Re(z)>-1\). This does not establish a complex-\(z\) prime-average theorem.

## Highest-priority surviving question

The Euler product is no longer the preferred primitive object. Define
\[
P_a(s,z)=\sum_{p\nmid a}I_a(p)^{-z}p^{-s},
\qquad
P(s)=\sum_p p^{-s},
\]
and
\[
\boxed{Q_a(s,z)=P_a(s,z)-\Delta_a(z)P(s).}
\]

The theorem-sized question for the next session is:

> For fixed positive non-perfect-power \(a\) and fixed real \(z>0\), under a precisely stated GRH package, does \(Q_a(s,z)\) admit holomorphic continuation to any half-plane \(\Re(s)>1-\delta\) with \(\delta>0\)? If so, can this be obtained from a uniformly convergent Kummer-tower Artin/Dedekind-\(L\) expansion or from a logarithmic-derivative variant?

Subquestions:

- What conductor/discriminant bounds for \(K_n(a)\) are strong enough to control the \(n\)-sum after finite-level character decomposition?
- Is the logarithmic derivative more natural because it removes branch choices for \(\log L(s,\chi)\)?
- Can tower-level cancellation preserve the original divisor-support convergence after reorganization?
- Does any valid continuation reveal secondary singularities or a natural boundary?
- Is there a useful complex-\(z\) weighted prime theorem, rather than merely a holomorphic parameter in the degree series?
- Does Felix--Murty Theorem 1.7, or a later theorem of equal generality, explicitly cover negative integer bases for general \(f(i_a(p))\)?

## Deferred generalisation

Elliptic curves, abelian varieties, 1-motives, Hodge theory, Lean, and paper work remain outside the current gate.

## Session-4 gate

Exit state: **ANALYTIC_PILOT_REFRAME**.

Session 5 should proceed only in reframed mathematical-proof form around \(Q_a(s,z)\) and the tower continuation problem. The Level-1 real boundary asymptotic is no longer a research target.
