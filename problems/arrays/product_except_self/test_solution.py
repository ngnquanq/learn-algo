import pytest
from .solution import solution


class TestProductExceptSelf:
    # -------------------------------------------------------
    # Basic / Example cases
    # -------------------------------------------------------
    def test_example_1(self):
        assert solution([1, 2, 3, 4]) == [24, 12, 8, 6]

    def test_example_2(self):
        assert solution([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]

    # -------------------------------------------------------
    # Edge cases
    # -------------------------------------------------------
    def test_two_elements(self):
        assert solution([3, 7]) == [7, 3]

    def test_single_zero(self):
        """Only one zero: one position gets the product of the rest."""
        assert solution([1, 0, 3, 4]) == [0, 12, 0, 0]

    def test_two_zeros(self):
        """Two or more zeros: every output must be 0."""
        assert solution([0, 0, 3, 4]) == [0, 0, 0, 0]

    def test_all_ones(self):
        assert solution([1, 1, 1, 1]) == [1, 1, 1, 1]

    def test_negative_numbers(self):
        assert solution([-1, -2, -3, -4]) == [-24, -12, -8, -6]

    def test_mixed_sign(self):
        assert solution([-1, 1, -1, 1]) == [-1, 1, -1, 1]

    # -------------------------------------------------------
    # Performance case — must finish well within the 10s timeout
    # -------------------------------------------------------
    def test_large_input(self):
        n = 10 ** 5
        nums = [1] * n          # all ones → every answer is 1
        result = solution(nums)
        assert len(result) == n
        assert all(v == 1 for v in result)
