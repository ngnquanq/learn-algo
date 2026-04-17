import pytest
from .solution import solution


class TestDistinct:
    # -------------------------------------------------------
    # Basic / Example cases
    # -------------------------------------------------------
    def test_example_1(self):
        assert solution([2, 1, 1, 2, 3, 1]) == 3

    def test_all_distinct(self):
        assert solution([1, 2, 3, 4, 5]) == 5

    # -------------------------------------------------------
    # Edge cases
    # -------------------------------------------------------
    def test_empty(self):
        assert solution([]) == 0

    def test_single_element(self):
        assert solution([42]) == 1

    def test_all_same(self):
        assert solution([7, 7, 7, 7]) == 1

    def test_negatives(self):
        assert solution([-1, -2, -1]) == 2

    def test_mixed_sign(self):
        assert solution([-1, 0, 1]) == 3

    # -------------------------------------------------------
    # Performance cases (large inputs should finish in time)
    # -------------------------------------------------------
    def test_large_input(self):
        A = list(range(-50_000, 50_000))
        assert solution(A) == 100_000
