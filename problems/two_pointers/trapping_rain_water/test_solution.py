import pytest
from .solution import solution


class TestTrappingRainWater:
    # -------------------------------------------------------
    # Basic / Example cases
    # -------------------------------------------------------
    def test_example_1(self):
        assert solution([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6

    def test_example_2(self):
        assert solution([4, 2, 0, 3, 2, 5]) == 9

    # -------------------------------------------------------
    # Edge cases
    # -------------------------------------------------------
    def test_empty(self):
        assert solution([]) == 0

    def test_single(self):
        assert solution([3]) == 0

    def test_flat(self):
        assert solution([3, 3, 3]) == 0

    def test_v_shape(self):
        assert solution([5, 0, 5]) == 5

    def test_increasing(self):
        assert solution([1, 2, 3]) == 0

    def test_decreasing(self):
        assert solution([3, 2, 1]) == 0

    def test_two_bars(self):
        assert solution([3, 1]) == 0

    # -------------------------------------------------------
    # Performance cases (large inputs should finish in time)
    # -------------------------------------------------------
    def test_large_input(self):
        n = 100_000
        height = [n] + [0] * (n - 2) + [n]
        assert solution(height) == n * (n - 2)
