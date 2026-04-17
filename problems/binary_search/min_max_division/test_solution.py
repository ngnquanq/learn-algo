import pytest
from .solution import solution


class TestMinMaxDivision:
    # -------------------------------------------------------
    # Basic / Example cases
    # -------------------------------------------------------
    def test_example_1(self):
        assert solution(3, 5, [2, 1, 5, 1, 2, 2, 2]) == 6

    # -------------------------------------------------------
    # Edge cases
    # -------------------------------------------------------
    def test_single_block(self):
        assert solution(1, 10, [2, 1, 5, 1, 2, 2, 2]) == 15

    def test_k_equals_n(self):
        assert solution(5, 10, [2, 1, 5, 1, 2]) == 5

    def test_single_element(self):
        assert solution(1, 10, [7]) == 7

    def test_all_zeros(self):
        assert solution(3, 0, [0, 0, 0, 0, 0]) == 0

    def test_all_same(self):
        assert solution(2, 5, [5, 5, 5]) == 10

    # -------------------------------------------------------
    # Performance cases (large inputs should finish in time)
    # -------------------------------------------------------
    def test_large_input(self):
        n = 100_000
        A = [1] * n
        assert solution(1, 1, A) == n
