import pytest
from .solution import solution


class TestHouseRobber:
    # -------------------------------------------------------
    # Basic / Example cases
    # -------------------------------------------------------
    def test_example_1(self):
        assert solution([1, 2, 3, 1]) == 4

    def test_example_2(self):
        assert solution([2, 7, 9, 3, 1]) == 12

    # -------------------------------------------------------
    # Edge cases
    # -------------------------------------------------------
    def test_single_house(self):
        assert solution([5]) == 5

    def test_two_houses(self):
        assert solution([1, 2]) == 2

    def test_all_zeros(self):
        assert solution([0, 0, 0]) == 0

    def test_alternating(self):
        assert solution([100, 1, 1, 100]) == 200

    def test_equal_values(self):
        assert solution([2, 1, 1, 2]) == 4

    # -------------------------------------------------------
    # Performance cases (large inputs should finish in time)
    # -------------------------------------------------------
    def test_max_size(self):
        nums = [400] * 100
        assert solution(nums) == 400 * 50
