import pytest
from .solution import solution


class TestCountSemiprimes:
    # -------------------------------------------------------
    # Basic / Example cases
    # -------------------------------------------------------
    def test_example_1(self):
        assert solution(26, [1, 4, 16], [26, 10, 20]) == [10, 4, 0]

    # -------------------------------------------------------
    # Edge cases
    # -------------------------------------------------------
    def test_n_equals_1(self):
        assert solution(1, [1], [1]) == [0]

    def test_smallest_semiprime(self):
        assert solution(4, [1], [4]) == [1]

    def test_single_point_semiprime(self):
        assert solution(10, [4], [4]) == [1]

    def test_single_point_not_semiprime(self):
        assert solution(10, [5], [5]) == [0]

    # -------------------------------------------------------
    # Performance cases (large inputs should finish in time)
    # -------------------------------------------------------
    def test_large_input(self):
        N = 50_000
        P = [1] * 30_000
        Q = [N] * 30_000
        result = solution(N, P, Q)
        assert len(result) == 30_000
        assert all(r == result[0] for r in result)
