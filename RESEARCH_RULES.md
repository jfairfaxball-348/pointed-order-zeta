# Research Rules

## Epistemic discipline

This is an object-discovery project, not a theorem-completion project.

Every substantive statement should be tagged mentally—and in notes where ambiguity matters—as one of:

- **definition**: stipulated object or notation;
- **elementary identity**: still requires a written derivation before being treated as established in-project;
- **literature fact**: requires a precise source and theorem/proposition when material;
- **computation**: finite evidence only;
- **conjecture / target**: unproved;
- **theorem**: permitted only after a complete proof and hypothesis audit;
- **novelty claim**: forbidden until the relevant prior-art gate has been completed.

## Frozen versus provisional

Frozen for the opening investigation:

- \(I_a(p)=(p-1)/\operatorname{ord}_p(a)\);
- \(Z_a(s,z)=\prod_{p\nmid a}(1-I_a(p)^{-z}p^{-s})^{-1}\);
- initial rigorous range real \(z\ge0\), \(\Re(s)>1\);
- provisional mean \(\Delta_a(z)\), when it exists;
- Kummer-tower target \(K_n(a)=\mathbf Q(\zeta_n,a^{1/n})\).

Not frozen:

- “Artin–Kummer order spectrum” as a name;
- the claim that \(I_a(p)^{-z}\) is canonical;
- any singularity theorem;
- any L-function factorization;
- any novelty or priority statement;
- any elliptic, abelian, Hodge, motivic, or 1-motivic interpretation.

## Gate rules

1. Do not perform a comprehensive novelty audit before foundations are internally sound.
2. Do not promote numerical convergence to existence of a density.
3. Do not interchange limits, prime sums, logarithms, or infinite products without proving the relevant convergence.
4. Do not hide exceptional primes, perfect-power effects, or entanglement in notation.
5. Do not call a repackaging new merely because the Euler product or parameterization looks different.
6. Do not force the original weight to survive; replacement by a more canonical transform is a successful reframing.
7. Do not generalize to elliptic curves or abelian varieties until the \(\mathbf G_m\) prototype is understood.
8. Do not begin Lean before the mathematical objects and statements are stable.
9. Do not begin paper drafting or public priority claims during the pilot.

## Novelty test

The strongest question is not “has this exact Euler product been printed?” but whether existing generalized-Artin, Chebotarev, Frobenian, or residual-index machinery already contains it essentially for free.

Later work must distinguish:

A. residual-index distribution;  
B. averages of general \(f(I_a(p))\);  
C. the continuous family \(f_z(n)=n^{-z}\);  
D. the two-variable Euler-product packaging;  
E. a continuously varying singularity exponent / spectrum;  
F. Kummer-tower or L-function factorization;  
G. pointed algebraic-group / 1-motive generalization.

Equivalent mathematics under different notation counts as prior art.
