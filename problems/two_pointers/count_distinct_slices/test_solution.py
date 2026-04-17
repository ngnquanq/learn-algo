import pytest
from .solution import solution


class TestCountDistinctSlices:
    # -------------------------------------------------------
    # Basic / Example cases
    # -------------------------------------------------------
    def test_example_1(self):
        assert solution(6, [3, 4, 5, 5, 2]) == 9

    # -------------------------------------------------------
    # Edge cases
    # -------------------------------------------------------
    def test_empty(self):
        assert solution(0, []) == 0

    def test_single(self):
        assert solution(5, [5]) == 1

    def test_all_same(self):
        assert solution(1, [0, 0, 0]) == 3

    def test_all_distinct(self):
        assert solution(4, [0, 1, 2, 3, 4]) == 15

    def test_cap_at_billion(self):
        n = 100_000
        A = list(range(n))
        result = solution(n - 1, A)
        assert result == 1_000_000_000

    # -------------------------------------------------------
    # Performance cases (large inputs should finish in time)
    # -------------------------------------------------------
    def test_large_input(self):
        n = 100_000
        A = [0] * n
        assert solution(0, A) == n
