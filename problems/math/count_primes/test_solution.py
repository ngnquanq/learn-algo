import pytest
from .solution import solution


class TestCountPrimes:
    # -------------------------------------------------------
    # Basic / Example cases
    # -------------------------------------------------------
    def test_example_1(self):
        assert solution(10) == 4

    def test_example_2(self):
        assert solution(0) == 0

    def test_example_3(self):
        assert solution(1) == 0

    # -------------------------------------------------------
    # Edge cases
    # -------------------------------------------------------
    def test_two(self):
        assert solution(2) == 0

    def test_three(self):
        assert solution(3) == 1

    def test_hundred(self):
        assert solution(100) == 25

    def test_thousand(self):
        assert solution(1000) == 168

    # -------------------------------------------------------
    # Performance cases (large inputs should finish in time)
    # -------------------------------------------------------
    def test_large_input(self):
        assert solution(5_000_000) == 348513
