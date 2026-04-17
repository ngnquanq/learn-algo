import pytest
from .solution import solution


class TestMinAbsSum:
    # -------------------------------------------------------
    # Basic / Example cases
    # -------------------------------------------------------
    def test_example_1(self):
        assert solution([1, 5, 2, -2]) == 0

    def test_example_2(self):
        assert solution([3, 3, 3, 4, 5]) == 0

    # -------------------------------------------------------
    # Edge cases
    # -------------------------------------------------------
    def test_empty(self):
        assert solution([]) == 0

    def test_single(self):
        assert solution([1]) == 1

    def test_all_zeros(self):
        assert solution([0, 0, 0]) == 0

    def test_single_large(self):
        assert solution([100]) == 100

    def test_two_equal(self):
        assert solution([1, 1]) == 0

    def test_three_same(self):
        assert solution([7, 7, 7]) == 7

    # -------------------------------------------------------
    # Performance cases (large inputs should finish in time)
    # -------------------------------------------------------
    def test_large_input(self):
        A = [100] * 20_000
        assert solution(A) == 0

    def test_large_odd(self):
        A = [1] * 19_999
        assert solution(A) == 1
