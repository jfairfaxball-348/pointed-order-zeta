import unittest
from math import gcd

from src.residual_index import (
    factorint,
    is_nth_power_mod_prime,
    multiplicative_order_mod_prime,
    residual_divisibility_criterion,
    residual_index,
)


class ResidualIndexTests(unittest.TestCase):
    def test_factorint(self):
        self.assertEqual(factorint(1), {})
        self.assertEqual(factorint(360), {2: 3, 3: 2, 5: 1})

    def test_exact_orders_and_indices(self):
        cases = [
            (2, 7, 3, 2),
            (3, 13, 3, 4),
            (5, 31, 3, 10),
            (6, 7, 2, 3),
            (10, 11, 2, 5),
        ]
        for a, p, order, index in cases:
            with self.subTest(a=a, p=p):
                self.assertEqual(multiplicative_order_mod_prime(a, p), order)
                self.assertEqual(residual_index(a, p), index)

    def test_criterion_for_small_examples(self):
        primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
        for a in [2, 3, 5, 6, 10]:
            for p in primes:
                if a % p == 0:
                    continue
                for n in range(1, 13):
                    lhs, rhs = residual_divisibility_criterion(a, n, p)
                    with self.subTest(a=a, p=p, n=n):
                        self.assertEqual(lhs, rhs)

    def test_cyclic_group_identity_exhaustively(self):
        # In C_N=<g>, x=g^k has index gcd(N,k), while x is an n-th
        # power iff gcd(n,N) divides k. Exhaust small groups.
        for N in range(1, 41):
            for k in range(N):
                index = gcd(N, k)
                for n in range(1, 41):
                    lhs = index % n == 0
                    rhs = N % n == 0 and k % gcd(n, N) == 0
                    with self.subTest(N=N, k=k, n=n):
                        self.assertEqual(lhs, rhs)

    def test_composite_n(self):
        self.assertEqual(residual_index(3, 13), 4)
        self.assertTrue(is_nth_power_mod_prime(3, 4, 13))
        self.assertEqual(
            residual_divisibility_criterion(3, 4, 13),
            (True, True),
        )

    def test_n_not_dividing_p_minus_one(self):
        # 2 is a fourth power mod 7, but 4 does not divide p-1=6
        # and 4 does not divide I_2(7)=2.
        self.assertTrue(is_nth_power_mod_prime(2, 4, 7))
        self.assertEqual(residual_index(2, 7), 2)
        self.assertEqual(
            residual_divisibility_criterion(2, 4, 7),
            (False, False),
        )

    def test_negative_and_perfect_power_bases(self):
        for a in [-2, 4, 8]:
            for p in [3, 5, 7, 11, 13, 17, 19]:
                if a % p == 0:
                    continue
                for n in range(1, 9):
                    lhs, rhs = residual_divisibility_criterion(a, n, p)
                    self.assertEqual(lhs, rhs)

    def test_prime_dividing_a_is_rejected(self):
        with self.assertRaises(ValueError):
            multiplicative_order_mod_prime(6, 3)


if __name__ == "__main__":
    unittest.main()
