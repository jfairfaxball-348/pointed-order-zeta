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

## Continuation proof — resolved or obstructed in Session 5

- The clean proof object is
  \[
  Q_a^\circ(s,z)
  =
  \sum_{p\nmid a}
  \bigl(I_a(p)^{-z}-\Delta_a(z)\bigr)p^{-s},
  \]
  which differs from the frozen \(Q_a(s,z)\) by the finite entire term
  \[
  -\Delta_a(z)\sum_{p\mid a}p^{-s}.
  \]
- In \(\Re(s)>1\), the centered Kummer expansion is exact and absolutely convergent:
  \[
  Q_a^\circ(s,z)
  =
  \sum_{n\ge1}g_z(n)
  \left(
  S_{a,n}(s)-\frac{1}{[K_n(a):\mathbf Q]}P_a^\circ(s,0)
  \right).
  \]
- At each fixed finite Galois level,
  \[
  C_K(s)
  =
  P_{\rm split}(s;K)-\frac1{[K:\mathbf Q]}P(s)
  \]
  has the exact representation
  \[
  C_K(s)
  =
  \frac1{[K:\mathbf Q]}
  \log\!\left(\frac{\zeta_K(s)}{\zeta(s)}\right)
  -
  B_K(s),
  \]
  where \(B_K\) is holomorphic for \(\Re(s)>1/2\). The trivial character and the \(s=1\) pole cancel exactly.
- Aramata--Brauer gives local continuation of every fixed \(C_K\) through \(s=1\) unconditionally. Under Dedekind GRH, each fixed level is holomorphic on \(\Re(s)>1/2\).
- For positive non-perfect-power \(a\),
  \[
  \log|\operatorname{Disc}(K_n(a))|
  \le
  [K_n(a):\mathbf Q](3\log n+\log a).
  \]
- Under GRH,
  \[
  \pi_n(x)
  =
  \frac{\operatorname{li}(x)}{[K_n(a):\mathbf Q]}
  +
  O_a(\sqrt{x}\log(nx)),
  \]
  and hence on compact subsets of \(\Re(s)>1/2\),
  \[
  C_{K_n(a)}(s)=O_{a,\Omega}(\log(2n)).
  \]
- This finite-level bound is not summable over the tower against \(g_z\), since for prime \(q\),
  \[
  |g_z(q)|=1-q^{-z}\to1.
  \]
  This proves failure of the standard locally-uniform absolute-convergence argument; it does not prove divergence of the actual tower.
- The logarithmic derivative removes branch choices but does not improve tower convergence.
- A moving truncation reproduces the Felix--Murty logarithmic discrepancy. The finite Chebotarev part and Kummer-degree mean tail could formally balance at \(N=x^{1/4}\), but the prime-supported large-divisor tail has no available power-saving bound there.
- No Level-2 or Level-3 continuation of the full \(Q_a\) was proved.

## Highest-priority surviving question after Session 5

For fixed positive non-perfect-power \(a\) and real \(z>0\), can one obtain a genuine power saving by preserving cancellation across the Kummer tower rather than summing finite-level absolute bounds?

A concrete target is to prove, for some \(\alpha,\delta>0\), a centered estimate of the form
\[
\sum_{n\le x^\alpha}
g_z(n)
\left(
\pi_n(x)-\frac{\operatorname{li}(x)}{[K_n(a):\mathbf Q]}
\right)
+
\mathcal T_z(x;x^\alpha)
-
\operatorname{li}(x)
\sum_{n>x^\alpha}
\frac{g_z(n)}{[K_n(a):\mathbf Q]}
=
O(x^{1-\delta}),
\]
where
\[
\mathcal T_z(x;N)
=
\sum_{\substack{p\le x\\p\nmid a}}
\sum_{\substack{n\mid I_a(p)\\n>N}}g_z(n).
\]

Subquestions:

- Can a large sieve for Frobenius, a zero-density theorem, or an explicit-formula argument give cancellation in the finite-level \(n\)-sum beyond
  \[
  O_a(\sqrt{x}N\log(Nx))?
  \]
- Can the divisor-supported tail \(\mathcal T_z(x;N)\) be centered with a power saving for any power-sized \(N=x^\alpha\)?
- Is smoothing in \(x\) enough to expose such cancellation, and can smoothing then be removed or converted to continuation of \(Q_a\)?
- Can the scalar cancellation encoded by
  \[
  \sum_{n\ge1}\frac{g_z(n)}{n^w}
  =
  \frac{\zeta(w+z)}{\zeta(w)}
  \]
  be transferred to the nonmultiplicative family \(C_{K_n}(s)\)?
- Could \(Q_a(s,z)\) continue across \(\Re(s)=1\) by a mechanism not visible from Kummer-level separation?
- Does Felix--Murty Theorem 1.7, or a later theorem of equal generality, explicitly cover negative integer bases for general \(f(i_a(p))\)?

## Deferred generalisation

Elliptic curves, abelian varieties, 1-motives, Hodge theory, Lean, and paper work remain outside the current gate.

## Session-5 gate

Exit state: **CONTINUATION_PROOF_OBSTRUCTED**.

Session 6 may proceed only in reframed proof form around tower-averaged cancellation / power-saving divisor-support estimates. Do not repeat the naively separated infinite \(L\)-function expansion, and do not infer a natural boundary from its failure.
