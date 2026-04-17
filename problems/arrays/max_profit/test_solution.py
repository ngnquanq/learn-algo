import pytest
from .solution import solution


class TestMaxProfit:
    # -------------------------------------------------------
    # Basic / Example cases
    # -------------------------------------------------------
    def test_example_1(self):
        assert solution([23171, 21011, 21123, 21366, 21013, 21367]) == 356

    def test_example_2(self):
        assert solution([7, 1, 5, 3, 6, 4]) == 5

    # -------------------------------------------------------
    # Edge cases
    # -------------------------------------------------------
    def test_empty(self):
        assert solution([]) == 0

    def test_single(self):
        assert solution([5]) == 0

    def test_decreasing(self):
        assert solution([5, 4, 3, 2, 1]) == 0

    def test_all_same(self):
        assert solution([3, 3, 3, 3]) == 0

    def test_two_elements_profit(self):
        assert solution([1, 2]) == 1

    def test_two_elements_no_profit(self):
        assert solution([2, 1]) == 0

    # -------------------------------------------------------
    # Performance cases (large inputs should finish in time)
    # -------------------------------------------------------
    def test_large_input(self):
        n = 400_000
        A = list(range(n, 0, -1))  # decreasing
        A[-1] = n + 1  # spike at end
        assert solution(A) == n + 1 - A[-2]
