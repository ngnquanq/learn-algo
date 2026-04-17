import pytest
from .solution import solution


class TestNailingPlanks:
    # -------------------------------------------------------
    # Basic / Example cases
    # -------------------------------------------------------
    def test_example_1(self):
        assert solution([1, 4, 5, 8], [4, 5, 9, 10], [4, 6, 7, 10, 2]) == 4

    # -------------------------------------------------------
    # Edge cases
    # -------------------------------------------------------
    def test_single_plank_single_nail(self):
        assert solution([1], [5], [3]) == 1

    def test_impossible(self):
        assert solution([1], [2], [5]) == -1

    def test_all_nails_same_position(self):
        assert solution([1, 5], [3, 7], [2, 2, 2]) == -1

    def test_first_nail_works(self):
        assert solution([1], [10], [5]) == 1

    # -------------------------------------------------------
    # Performance cases (large inputs should finish in time)
    # -------------------------------------------------------
    def test_large_input(self):
        n = 30_000
        A = list(range(1, n + 1))
        B = list(range(1, n + 1))
        C = list(range(1, n + 1))
        assert solution(A, B, C) == n
