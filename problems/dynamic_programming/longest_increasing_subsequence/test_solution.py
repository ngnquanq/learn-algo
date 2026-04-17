import pytest
from .solution import solution


class TestLongestIncreasingSubsequence:
    # -------------------------------------------------------
    # Basic / Example cases
    # -------------------------------------------------------
    def test_example_1(self):
        assert solution([10, 9, 2, 5, 3, 7, 101, 18]) == 4

    def test_example_2(self):
        assert solution([0, 1, 0, 3, 2, 3]) == 4

    # -------------------------------------------------------
    # Edge cases
    # -------------------------------------------------------
    def test_single(self):
        assert solution([1]) == 1

    def test_all_same(self):
        assert solution([7, 7, 7, 7]) == 1

    def test_increasing(self):
        assert solution([1, 2, 3, 4, 5]) == 5

    def test_decreasing(self):
        assert solution([5, 4, 3, 2, 1]) == 1

    def test_two_elements(self):
        assert solution([1, 2]) == 2

    # -------------------------------------------------------
    # Performance cases (large inputs should finish in time)
    # -------------------------------------------------------
    def test_large_input(self):
        n = 2500
        nums = list(range(n, 0, -1))  # decreasing
        assert solution(nums) == 1

    def test_large_increasing(self):
        n = 2500
        nums = list(range(n))
        assert solution(nums) == n
