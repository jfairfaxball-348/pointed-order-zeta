# Open Questions

This is a live question bank, not a conjecture list.

## Foundational — resolved in Session 2

- For \(p\nmid a\),
  \[
  n\mid I_a(p)
  \iff
  n\mid p-1\text{ and }a\bmod p\in(\mathbf F_p^\times)^n.
  \]
- For fixed \(n\) and \(p\nmid an\),
  \[
  n\mid I_a(p)
  \iff
  p\text{ splits completely in }K_n(a)=\mathbf Q(\zeta_n,a^{1/n}).
  \]
- The non-perfect-power hypothesis is not needed for the individual splitting equivalence; it affects degree formulas and later constants.
- Negative bases require no correction in the individual criterion.
- Entanglement is not an exception to the fixed-\(n\) criterion.
- The shorthand “\(a\) is an \(n\)-th power mod \(p\)” without \(n\mid p-1\) is false as an equivalent formulation.

## Prior art — resolved or substantially resolved in Session 3

- **Is residual index standard?** Yes. The literature uses residual index \(i_a(p)\) or \(r_g(p)\).
- **Is \(I_a(p)=t\) known?** Yes. This is the fixed residual-index / near-primitive-root problem. Wagstaff and Moree give GRH-conditional densities in Kummer-degree form, with explicit correction factors.
- **Is \(n\mid I_a(p)\) standard?** Yes. Felix--Murty Lemma 2.1 records the exact complete-splitting criterion in \(\mathbf Q(\zeta_n,a^{1/n})\) as classical.
- **Are general \(f(I_a(p))\) averages known?** Yes. Pappalardi gives an earlier weighted-Hooley framework; Felix--Murty Theorem 1.7 treats fixed \(a\) and a broad class of \(f\).
- **Is the Möbius/Kummer series known?** Yes:
  \[
  c_{a,f}
  =
  \sum_{n\ge1}
  \frac{(\mu*f)(n)}
  {[\mathbf Q(\zeta_n,a^{1/n}):\mathbf Q]}.
  \]
  Felix--Murty derives this constant; Akbary--Fakhari develops product/entanglement expressions for such constants.
- **Does known theory imply \(\Delta_a(z)\)?** Yes, under the GRH hypotheses of Felix--Murty Theorem 1.7, for every fixed real \(z>0\), because Session 2 proved \(|g_z(n)|\le1\). At \(z=0\), \(\Delta_a(0)=1\) is elementary.
- **Does the degree series converge?** Yes for fixed real \(z>0\). Wagstaff's exact degree formula gives
  \[
  [K_n(a):\mathbf Q]\asymp_a n\varphi(n),
  \]
  so
  \[
  \sum_n\frac{|g_z(n)|}{[K_n(a):\mathbf Q]}
  \ll_a
  \sum_n\frac1{n\varphi(n)}<\infty.
  \]
- **What does entanglement do?** It corrects naive independence/local products and degree factorization. It does not alter the individual fixed-\(n\) splitting equivalence.
- **Is “spectrum” standard?** No supporting usage was found. The natural description is a Dirichlet/Mellin transform of the residual-index distribution, equivalently a Laplace transform of \(\log I_a(p)\).

## Reframed Euler-product questions — highest priority

The project now takes \(\Delta_a(z)\) and its generalized-Artin Kummer-degree formula as known input under the relevant hypotheses.

- For fixed real \(z>0\), define
  \[
  H_a(s,z)
  =
  Z_a(s,z)\zeta(s)^{-\Delta_a(z)}
  \]
  with omitted-prime normalization treated consistently. Does \(H_a(s,z)\) extend holomorphically and nonvanishingly across \(\Re(s)=1\)?
- What is the largest half-plane in which such a normalized factor can be continued, conditionally on GRH or unconditionally?
- Is there a useful convergent factorization of \(Z_a(s,z)\), \(H_a(s,z)\), or a logarithmic derivative in terms of Dedekind or Artin \(L\)-functions from the Kummer tower?
- Does an infinite product of \(L\)-functions converge in a useful region, and what degree/conductor estimates are required?
- Does the infinite Kummer tower create a natural boundary or secondary singularities?
- Can one obtain uniform estimates in \(z\), or holomorphic dependence for complex \(z\)?
- Is the frozen local factor
  \[
  (1-I_a(p)^{-z}p^{-s})^{-1}
  \]
  analytically useful, or is another Euler-factor design more canonical once the generalized-Artin mean is regarded as old?

## Leading singular coefficient — mostly reframed, not a novelty target

Felix--Murty gives an asymptotic for
\[
\sum_{p\le x}I_a(p)^{-z}
\]
under GRH. Standard partial summation therefore strongly suggests that the \(k=1\) term in \(\log Z_a(s,z)\) has leading coefficient \(\Delta_a(z)\) as \(s\to1^+\), while the \(k\ge2\) terms are absolutely regular there.

Session 4 should not spend its main effort rediscovering this leading coefficient. The worthwhile question is whether a **stronger analytic normalization/continuation theorem** survives.

## Transform/object selection

- Should \(\Delta_a(z)\) be treated simply as the Dirichlet/Mellin transform
  \[
  \sum_{t\ge1}\delta_a(t)t^{-z}
  \]
  of the known residual-index distribution?
- Is the full discrete distribution \(\delta_a(t)\) the more fundamental arithmetic object?
- If the Euler-product layer survives, is \(I^{-z}\) the best weight for exposing its analytic structure?
- Would a probability-generating transform, logarithmic derivative, or another normalization be more natural?

## Generalisation — still deferred

- What is the right analogue of residual index when the reduced finite group is noncyclic?
- Should one use subgroup index, saturation index, cokernel structure, or elementary divisors?
- Is the 1-motive \([\mathbf Z\to G]\) the natural home for pointed reduction data?
- Does any Hodge/motivic structure add information not already encoded by the adelic representation?
- These questions received only nearby-prior-art checking in Session 3 and must not be treated as surviving novelty claims.

## Session-3 gate

Exit state: **PRIOR_ART_REFRAME**.

Session 4 should proceed only with the analytic infinite-Kummer Euler-product question reframed around known generalized-Artin input.
