# Pointed Order Zeta: Artin–Kummer Spectra of Reduction Orders

**Status: PILOT_KILL**

The mathematical pilot is closed after Session 6. The project produced useful standalone mathematics and a reproducible residual-index engine, but it did **not** earn another research session under the adversarial go/no-go standard.

## Frozen starting object

Let (ainmathbf Zsetminus{0,pm1}), initially not a perfect power. For (p
mid a),
[
I_a(p)=rac{p-1}{operatorname{ord}_p(a)}
=[mathbf F_p^	imes:langle amod pangle].
]
The frozen Euler product is
[
Z_a(s,z)=prod_{p
mid a}(1-I_a(p)^{-z}p^{-s})^{-1},
qquad zge0,quad Re(s)>1.
]
The prime-average transform is
[
Delta_a(z)=lim_{x	oinfty}rac1{pi(x)}
sum_{substack{ple x\p
mid a}}I_a(p)^{-z},
]
when it exists.

These definitions were never altered.

## What collapsed into prior art

Sessions 2–3 established internally, then source-matched, that:

- (I_a(p)) is the standard residual index;
- for fixed (n) and (p
mid an),
  [
  nmid I_a(p)iff p	ext{ splits completely in }K_n(a)=mathbf Q(zeta_n,a^{1/n});
  ]
- exact residual-index densities and general weighted sums (f(I_a(p))) are generalized-Artin / near-primitive-root territory;
- for fixed real (z>0), the mean (Delta_a(z)) is an immediate specialization of the Felix--Murty weighted theorem in its source-matched positive-base GRH setting;
- Wagstaff's degree formula and Akbary--Fakhari/Lenstra--Moree--Stevenhagen entanglement machinery already control the associated Kummer-degree constants.

The word “spectrum” is therefore only informal historical project shorthand.

## What the analytic pilot proved

Session 4 reduced the Euler-product continuation question to
[
Q_a(s,z)=
sum_{p
mid a}I_a(p)^{-z}p^{-s}
-Delta_a(z)sum_p p^{-s}.
]
The (kge2) logarithmic Euler-product part is holomorphic for (Re(s)>1/2). Felix--Murty's logarithmic prime-counting error gives only Level 1:
[
Z_a(s,z)sim C_a(z)(s-1)^{-Delta_a(z)}
qquad(s	o1^+)
]
under the relevant GRH hypotheses. It does not give complex continuation through (s=1).

Session 5 proved the exact centered finite-level formula
[
C_K(s)
=
rac1{[K:mathbf Q]}
log!left(rac{zeta_K(s)}{zeta(s)}ight)-B_K(s),
]
with (B_K) holomorphic for (Re(s)>1/2), and isolated the infinite-tower obstruction. Under Dedekind GRH,
[
pi_n(x)
=
rac{operatorname{li}(x)}{[K_n(a):mathbf Q]}
+
O_a(sqrt{x}log(nx)),
]
but summing continued levels loses the original divisor-support convergence. Existing large-index control recovers only logarithmic saving, not a power saving.

## Session 6 go / no-go result

Session 6 attacked the signed discrepancy, smoothing, exact-index reorganisation, special (z), large sieve for Frobenius, zero-density methods, and the full nested tower.

The strongest positive result is an exact profinite (L^2) structure. For
[
L_a=igcup_nK_n(a),qquad U_n=operatorname{Gal}(L_a/K_n(a)),
]
one has
[
K_m(a)K_n(a)=K_{operatorname{lcm}(m,n)}(a)
]
and therefore
[
leftlangle
mathbf1_{U_m}-rac1{d_m},
mathbf1_{U_n}-rac1{d_n}
ightangle
=
rac1{d_{operatorname{lcm}(m,n)}}-rac1{d_md_n}.
]
Consequently
[
sum_n g_z(n)left(mathbf1_{U_n}-rac1{d_n}ight)
]
converges in Haar (L^2), with tail
[
O_{a,arepsilon}(N^{-1/2+arepsilon}).
]

This is genuine nested-tower cancellation. It does **not** transfer, with known theorems, to prime Frobenius elements at a power-sized growing level. The signed divisor tail also has an exact obstruction: if (q>N) is prime,
[
sum_{substack{nmid q\n>N}}g_z(n)=q^{-z}-1,
]
whose magnitude tends to (1).

The large-sieve and zero-density results audited in Session 6 do not match the deterministic nested unbounded-degree family in the form needed. Exact-index and large-(z) reorganisations retain the primitive-root (I_a(p)=1) component, so they do not make the core problem easier than classical generalized-Artin/Hooley theory.

Full details: notes/session6-go-no-go.md.

## Why the pilot is killed

The remaining theorem would be a power-saving effective equidistribution theorem for a growing nested Kummer tower. Proving such a theorem would be a recognizable contribution, but the project found no credible reason that the Pointed Order Zeta construction makes it easier than the classical generalized-Artin problem. The best new mechanism—the (L^2) lcm covariance—already persists at the primitive-root endpoint.

Under the Session-6 standard, that is not enough to justify another project session.

No Level-2 continuation was proved. No Level-3 continuation was proved. No natural boundary was proved.

## Standalone outputs worth retaining

- notes/foundational-derivation.md — first-principles residual-index/Kummer derivation.
- notes/prior-art-matrix.md, notes/literature.md — source-level collision map.
- notes/analytic-pilot.md — reduction to the centered prime series.
- notes/continuation-proof.md — finite-level centered (L)-function identity, discriminant bounds, and tower obstruction.
- notes/session6-go-no-go.md — exact discrepancy decomposition, profinite (L^2) theorem, theorem matching, and final decision.
- src/, scripts/, tests/ — exact residual-index and analytic-pilot code.

## Research gates

0. SCAFFOLD — **SCAFFOLD_COMPLETE**  
1. FOUNDATIONAL DERIVATION — **FOUNDATIONS_PASS**  
2. PRIOR-ART / NOVELTY AUDIT — **PRIOR_ART_REFRAME**  
3. REFRAMED COMPUTATIONAL / ANALYTIC PILOT — **ANALYTIC_PILOT_REFRAME**  
4. REFRAMED MATHEMATICAL PROOF — **CONTINUATION_PROOF_OBSTRUCTED**  
5. ADVERSARIAL GO / NO-GO — **PILOT_KILL**

Generalisation, Lean/formalisation, and paper work were not begun.

## Final exit state

**PILOT_KILL**

No Session 7 should occur under this project.
