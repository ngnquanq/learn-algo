import pytest
from .solution import solution


class TestCountNonDivisible:
    # -------------------------------------------------------
    # Basic / Example cases
    # -------------------------------------------------------
    def test_example_1(self):
        assert solution([3, 1, 2, 3, 6]) == [2, 4, 3, 2, 0]

    # -------------------------------------------------------
    # Edge cases
    # -------------------------------------------------------
    def test_single(self):
        assert solution([1]) == [0]

    def test_all_ones(self):
        assert solution([1, 1, 1]) == [0, 0, 0]

    def test_all_same(self):
        assert solution([2, 2, 2]) == [0, 0, 0]

    def test_ascending(self):
        assert solution([1, 2, 3, 4, 5, 6]) == [5, 4, 4, 3, 4, 2]

    # -------------------------------------------------------
    # Performance cases (large inputs should finish in time)
    # -------------------------------------------------------
    def test_large_input(self):
        n = 50_000
        A = list(range(1, n + 1))
        result = solution(A)
        assert len(result) == n
        assert result[-1] <= n - 1  # n has at least itself as divisor
