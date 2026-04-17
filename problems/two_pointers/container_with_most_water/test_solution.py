import pytest
from .solution import solution


class TestContainerWithMostWater:
    # -------------------------------------------------------
    # Basic / Example cases
    # -------------------------------------------------------
    def test_example_1(self):
        assert solution([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49

    def test_example_2(self):
        assert solution([1, 1]) == 1

    # -------------------------------------------------------
    # Edge cases
    # -------------------------------------------------------
    def test_two_elements(self):
        assert solution([1, 2]) == 1

    def test_all_same(self):
        assert solution([5, 5, 5, 5]) == 15

    def test_increasing(self):
        assert solution([1, 2, 3, 4, 5]) == 6

    def test_decreasing(self):
        assert solution([5, 4, 3, 2, 1]) == 6

    def test_zeros(self):
        assert solution([0, 0]) == 0

    # -------------------------------------------------------
    # Performance cases (large inputs should finish in time)
    # -------------------------------------------------------
    def test_large_input(self):
        n = 100_000
        height = [10_000] * n
        assert solution(height) == 10_000 * (n - 1)
