import pytest
from .solution import solution


class TestMaxDoubleSliceSum:
    # -------------------------------------------------------
    # Basic / Example cases
    # -------------------------------------------------------
    def test_example_1(self):
        assert solution([3, 2, 6, -1, 4, 5, -1, 2]) == 17

    # -------------------------------------------------------
    # Edge cases
    # -------------------------------------------------------
    def test_minimum_length(self):
        assert solution([0, 0, 0]) == 0

    def test_all_negatives(self):
        assert solution([-1, -1, -1]) == 0

    def test_large_negative_middle(self):
        assert solution([5, -100, 5]) == 0

    def test_all_ones(self):
        assert solution([1, 1, 1, 1, 1]) == 2

    def test_spike_at_middle(self):
        assert solution([0, 10, -5, 10, 0]) == 10

    def test_four_elements(self):
        assert solution([1, 2, 3, 4]) == 2

    # -------------------------------------------------------
    # Performance cases (large inputs should finish in time)
    # -------------------------------------------------------
    def test_large_input(self):
        n = 100_000
        A = [1] * n
        result = solution(A)
        assert result == n - 3  # skip first, last, and one middle element
