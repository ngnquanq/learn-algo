import pytest
from .solution import solution


class TestJumpGame:
    # -------------------------------------------------------
    # Basic / Example cases
    # -------------------------------------------------------
    def test_example_1(self):
        assert solution([2, 3, 1, 1, 4]) is True

    def test_example_2(self):
        assert solution([3, 2, 1, 0, 4]) is False

    # -------------------------------------------------------
    # Edge cases
    # -------------------------------------------------------
    def test_single_element(self):
        assert solution([0]) is True

    def test_cannot_move(self):
        assert solution([0, 1]) is False

    def test_just_reaches(self):
        assert solution([1, 0]) is True

    def test_all_ones(self):
        assert solution([1, 1, 1, 1]) is True

    def test_all_zeros(self):
        assert solution([0, 0, 0]) is False

    def test_large_first_jump(self):
        assert solution([100, 0, 0, 0, 0]) is True

    # -------------------------------------------------------
    # Performance cases (large inputs should finish in time)
    # -------------------------------------------------------
    def test_large_input(self):
        n = 100_000
        nums = [1] * n
        assert solution(nums) is True
