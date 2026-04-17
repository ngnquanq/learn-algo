import pytest
from .solution import solution


class TestEquiLeader:
    # -------------------------------------------------------
    # Basic / Example cases
    # -------------------------------------------------------
    def test_example_1(self):
        assert solution([4, 3, 4, 4, 4, 2]) == 2

    def test_example_2(self):
        assert solution([1, 2, 3, 4, 5]) == 0

    # -------------------------------------------------------
    # Edge cases
    # -------------------------------------------------------
    def test_all_same(self):
        assert solution([4, 4, 4, 4]) == 3

    def test_two_same(self):
        assert solution([1, 1]) == 1

    def test_two_different(self):
        assert solution([1, 2]) == 0

    def test_no_leader(self):
        assert solution([1, 2, 1, 2]) == 0

    # -------------------------------------------------------
    # Performance cases (large inputs should finish in time)
    # -------------------------------------------------------
    def test_large_input(self):
        n = 100_000
        A = [1] * n
        assert solution(A) == n - 1
