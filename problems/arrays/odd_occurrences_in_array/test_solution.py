import pytest
from .solution import solution


class TestOddOccurrencesInArray:
    # -------------------------------------------------------
    # Basic / Example cases
    # -------------------------------------------------------
    def test_example_1(self):
        assert solution([9, 3, 9, 3, 9, 7, 9]) == 7

    def test_example_2(self):
        assert solution([1, 1, 2]) == 2

    # -------------------------------------------------------
    # Edge cases
    # -------------------------------------------------------
    def test_single_element(self):
        assert solution([42]) == 42

    def test_large_values(self):
        assert solution([1000000000, 1000000000, 999999999]) == 999999999

    def test_three_same(self):
        assert solution([5, 5, 5]) == 5

    def test_multiple_pairs(self):
        assert solution([1, 2, 3, 1, 2, 3, 4]) == 4

    # -------------------------------------------------------
    # Performance cases (large inputs should finish in time)
    # -------------------------------------------------------
    def test_large_input(self):
        n = 999_999
        A = list(range(1, n)) + list(range(1, n)) + [777]
        assert solution(A) == 777
