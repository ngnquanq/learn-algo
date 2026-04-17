import pytest
from .solution import solution


class TestCommonPrimeDivisors:
    # -------------------------------------------------------
    # Basic / Example cases
    # -------------------------------------------------------
    def test_example_1(self):
        assert solution([15, 10, 3], [75, 30, 5]) == 1

    # -------------------------------------------------------
    # Edge cases
    # -------------------------------------------------------
    def test_same_values(self):
        assert solution([6, 6], [6, 6]) == 2

    def test_one_and_one(self):
        assert solution([1], [1]) == 1

    def test_one_and_two(self):
        assert solution([1], [2]) == 0

    def test_prime_and_power(self):
        assert solution([2], [4]) == 1

    def test_different_primes(self):
        assert solution([2], [3]) == 0

    # -------------------------------------------------------
    # Performance cases (large inputs should finish in time)
    # -------------------------------------------------------
    def test_large_input(self):
        Z = 6000
        A = [2 ** 15] * Z
        B = [2 ** 20] * Z
        assert solution(A, B) == Z
