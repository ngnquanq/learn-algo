import pytest
from .solution import solution


class TestSearchInRotatedSortedArray:
    # -------------------------------------------------------
    # Basic / Example cases
    # -------------------------------------------------------
    def test_example_1(self):
        assert solution([4, 5, 6, 7, 0, 1, 2], 0) == 4

    def test_example_2(self):
        assert solution([4, 5, 6, 7, 0, 1, 2], 3) == -1

    # -------------------------------------------------------
    # Edge cases
    # -------------------------------------------------------
    def test_single_found(self):
        assert solution([1], 1) == 0

    def test_single_not_found(self):
        assert solution([1], 0) == -1

    def test_not_rotated(self):
        assert solution([1, 2, 3, 4, 5], 3) == 2

    def test_two_elements(self):
        assert solution([2, 1], 1) == 1

    def test_target_at_pivot(self):
        assert solution([4, 5, 6, 7, 0, 1, 2], 7) == 3

    def test_target_at_start(self):
        assert solution([4, 5, 6, 7, 0, 1, 2], 4) == 0

    # -------------------------------------------------------
    # Performance cases (large inputs should finish in time)
    # -------------------------------------------------------
    def test_large_input(self):
        n = 5000
        nums = list(range(1000, n)) + list(range(0, 1000))
        assert solution(nums, 0) == n - 1000
