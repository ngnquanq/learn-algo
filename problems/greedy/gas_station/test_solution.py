import pytest
from .solution import solution


class TestGasStation:
    # -------------------------------------------------------
    # Basic / Example cases
    # -------------------------------------------------------
    def test_example_1(self):
        assert solution([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]) == 3

    def test_example_2(self):
        assert solution([2, 3, 4], [3, 4, 3]) == -1

    # -------------------------------------------------------
    # Edge cases
    # -------------------------------------------------------
    def test_single_station_possible(self):
        assert solution([5], [3]) == 0

    def test_single_station_impossible(self):
        assert solution([1], [5]) == -1

    def test_all_equal(self):
        assert solution([3, 3, 3], [3, 3, 3]) == 0

    def test_start_at_zero(self):
        assert solution([5, 1, 1], [1, 1, 1]) == 0

    # -------------------------------------------------------
    # Performance cases (large inputs should finish in time)
    # -------------------------------------------------------
    def test_large_input(self):
        n = 100_000
        gas = [1] * n
        cost = [1] * n
        assert solution(gas, cost) == 0
