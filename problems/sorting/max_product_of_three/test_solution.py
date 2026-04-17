import pytest
from .solution import solution


class TestMaxProductOfThree:
    # -------------------------------------------------------
    # Basic / Example cases
    # -------------------------------------------------------
    def test_example_1(self):
        assert solution([-3, 1, 2, -2, 5, 6]) == 60

    def test_simple_positive(self):
        assert solution([1, 2, 3]) == 6

    # -------------------------------------------------------
    # Edge cases
    # -------------------------------------------------------
    def test_all_negatives(self):
        assert solution([-5, -4, -3, -2, -1]) == -6

    def test_two_large_negatives(self):
        assert solution([-1000, -999, 1, 2, 3]) == 999_000

    def test_all_same(self):
        assert solution([5, 5, 5]) == 125

    def test_exactly_three_elements(self):
        assert solution([10, 20, 30]) == 6000

    def test_mixed_with_zero(self):
        assert solution([-5, -4, 0, 1, 2]) == 40

    # -------------------------------------------------------
    # Performance cases (large inputs should finish in time)
    # -------------------------------------------------------
    def test_large_input(self):
        A = list(range(-500, 500)) + [1000]
        result = solution(A)
        assert result > 0
