"""Print a small exact table checking n | I_a(p) against the power criterion."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.residual_index import (
    multiplicative_order_mod_prime,
    residual_divisibility_criterion,
    residual_index,
)


def main() -> None:
    bases = [2, 3, 5, 6, 10]
    primes = [5, 7, 11, 13, 17, 19]
    ns = [2, 3, 4, 6]

    for a in bases:
        print(f"a={a}")
        for p in primes:
            if a % p == 0:
                continue
            order = multiplicative_order_mod_prime(a, p)
            index = residual_index(a, p)
            checks = []
            for n in ns:
                lhs, rhs = residual_divisibility_criterion(a, n, p)
                assert lhs == rhs
                if lhs:
                    checks.append(str(n))
            print(
                f"  p={p:2d} ord={order:2d} I={index:2d} "
                f"divisors-in-{ns}={','.join(checks) or '-'}"
            )


if __name__ == "__main__":
    main()
