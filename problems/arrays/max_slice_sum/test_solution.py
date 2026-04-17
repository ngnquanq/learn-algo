import pytest
from .solution import solution


class TestMaxSliceSum:
    # -------------------------------------------------------
    # Basic / Example cases
    # -------------------------------------------------------
    def test_example_1(self):
        assert solution([3, 2, -6, 4, 0]) == 5

    def test_example_2(self):
        assert solution([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

    # -------------------------------------------------------
    # Edge cases
    # -------------------------------------------------------
    def test_single_positive(self):
        assert solution([5]) == 5

    def test_single_negative(self):
        assert solution([-3]) == -3

    def test_all_negatives(self):
        assert solution([-1, -2, -3]) == -1

    def test_all_positives(self):
        assert solution([1, 2, 3, 4, 5]) == 15

    def test_negative_in_middle(self):
        assert solution([5, -1, 5]) == 9

    # -------------------------------------------------------
    # Performance cases (large inputs should finish in time)
    # -------------------------------------------------------
    def test_large_input(self):
        n = 1_000_000
        A = [1] * n
        assert solution(A) == n
