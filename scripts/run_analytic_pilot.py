"""Reproduce the compact Session-4 computational pilot tables.

Default settings are deliberately moderate: X=1e6 and N=5e5. Calculations use
Python binary64 complex arithmetic for transformed weights and logarithms; all
prime generation, factorization, multiplicative orders, residual indices, and
Kummer degrees are exact integers.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.analytic_pilot import (  # noqa: E402
    compute_prime_residual_data,
    log_z,
    kummer_delta_partials,
    mobius_convolution_weights_up_to,
    matched_log_h,
    spectrum_prime_average,
    smallest_prime_factor_sieve,
    totients_up_to,
)


def encode_complex(z: complex) -> dict[str, float]:
    return {"real": float(z.real), "imag": float(z.imag)}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime-cutoff", type=int, default=1_000_000)
    parser.add_argument("--kummer-cutoff", type=int, default=500_000)
    parser.add_argument("--output-dir", type=Path, default=ROOT / "data")
    args = parser.parse_args()

    bases = [2, 3, 5, 6, 10]
    z_values = [0.0, 0.5, 1.0, 2.0, 4.0, 8.0]
    empirical_cutoffs = [10_000, 100_000, args.prime_cutoff]
    kummer_cutoffs = [1_000, 10_000, 100_000, args.kummer_cutoff]
    epsilons = [0.1, 0.05, 0.02, 0.01]
    normalization_bases = [2, 5, 10]
    normalization_z = [0.5, 1.0, 2.0]
    normalization_cutoffs = [10_000, 100_000, args.prime_cutoff]

    limit = max(args.prime_cutoff, args.kummer_cutoff)
    primes, spf = smallest_prime_factor_sieve(limit)
    phi = totients_up_to(args.kummer_cutoff, primes)
    data = {
        a: compute_prime_residual_data(a, args.prime_cutoff, primes, spf)
        for a in bases
    }

    args.output_dir.mkdir(parents=True, exist_ok=True)
    delta_rows: list[dict[str, object]] = []
    delta_estimates: dict[tuple[int, float], complex] = {}
    g_cache = {
        z: mobius_convolution_weights_up_to(args.kummer_cutoff, z, spf)
        for z in z_values
    }
    for a in bases:
        for z in z_values:
            for x in empirical_cutoffs:
                value = spectrum_prime_average(data[a], primes, z, x)
                delta_rows.append({
                    "route": "prime",
                    "base": a,
                    "z": z,
                    "cutoff": x,
                    "real": value.real,
                    "imag": value.imag,
                })
            partials = kummer_delta_partials(a, z, kummer_cutoffs, spf, phi, g_cache[z])
            for n in kummer_cutoffs:
                value = partials[n]
                delta_rows.append({
                    "route": "kummer",
                    "base": a,
                    "z": z,
                    "cutoff": n,
                    "real": value.real,
                    "imag": value.imag,
                })
                if n == args.kummer_cutoff:
                    delta_estimates[(a, z)] = value

    with (args.output_dir / "session4_delta.csv").open("w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=["route", "base", "z", "cutoff", "real", "imag"])
        writer.writeheader()
        writer.writerows(delta_rows)

    norm_rows: list[dict[str, object]] = []
    for a in normalization_bases:
        for z in normalization_z:
            delta = delta_estimates[(a, z)]
            for eps in epsilons:
                s = 1.0 + eps
                for x in normalization_cutoffs:
                    value = matched_log_h(data[a], primes, s, z, delta, x)
                    norm_rows.append({
                        "base": a,
                        "z": z,
                        "epsilon": eps,
                        "s_real": s,
                        "prime_cutoff": x,
                        "delta_real": delta.real,
                        "logH_real": value.real,
                        "logH_imag": value.imag,
                    })

    with (args.output_dir / "session4_normalization.csv").open("w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(norm_rows[0]))
        writer.writeheader()
        writer.writerows(norm_rows)

    complex_z = [0.25 + 2j, 0.05 + 5j, 3j]
    complex_rows = []
    for z in complex_z:
        gz = mobius_convolution_weights_up_to(args.kummer_cutoff, z, spf)
        partials = kummer_delta_partials(2, z, kummer_cutoffs, spf, phi, gz)
        kvals = {str(n): encode_complex(partials[n]) for n in kummer_cutoffs}
        pval = spectrum_prime_average(data[2], primes, z, args.prime_cutoff)
        complex_rows.append({
            "z": encode_complex(z),
            "kummer": kvals,
            "prime_average": encode_complex(pval),
        })

    primitive_s = 1.1
    primitive_x = args.prime_cutoff
    base2 = data[2]
    primitive_log = 0j
    for p, index in zip(base2.primes, base2.indices):
        if p > primitive_x:
            break
        if index == 1:
            import cmath, math
            primitive_log -= cmath.log(1 - cmath.exp(-primitive_s * math.log(p)))
    primitive_comparison = {
        "base": 2,
        "s": primitive_s,
        "prime_cutoff": primitive_x,
        "primitive_root_log_product": encode_complex(primitive_log),
        "z4_log_product": encode_complex(log_z(base2, primitive_s, 4.0, primitive_x)),
        "z8_log_product": encode_complex(log_z(base2, primitive_s, 8.0, primitive_x)),
    }

    summary = {
        "session": 4,
        "prime_cutoff": args.prime_cutoff,
        "kummer_cutoff": args.kummer_cutoff,
        "arithmetic": "exact integer prime/factor/order/index/degree; binary64 transformed weights/logs",
        "degree_formula": "positive non-perfect-power Wagstaff/Felix-Murty specialization: n*phi(n)/epsilon, epsilon=2 iff n even and d(a)|n",
        "bases": bases,
        "z_values": z_values,
        "complex_z_diagnostics": complex_rows,
        "large_z_primitive_product": primitive_comparison,
        "notes": [
            "Prime and Kummer routes are validation routes, not a new theorem.",
            "Normalization tables use the same prime cutoff in Z and the zeta Euler product.",
            "Full-zeta normalization of a finite Z truncation has a large omitted-prime bias near s=1.",
        ],
    }
    (args.output_dir / "session4_summary.json").write_text(json.dumps(summary, indent=2) + "\n")


if __name__ == "__main__":
    main()
