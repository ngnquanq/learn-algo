import pytest
from .solution import solution


class TestGcdAndLcm:
    # -------------------------------------------------------
    # Basic / Example cases
    # -------------------------------------------------------
    def test_example_1(self):
        assert solution(10, 4) == 5

    def test_example_2(self):
        assert solution(12, 8) == 3

    # -------------------------------------------------------
    # Edge cases
    # -------------------------------------------------------
    def test_one_one(self):
        assert solution(1, 1) == 1

    def test_m_equals_one(self):
        assert solution(1000000000, 1) == 1000000000

    def test_n_equals_m(self):
        assert solution(100, 100) == 1

    def test_coprime(self):
        assert solution(7, 3) == 7

    def test_one_large(self):
        assert solution(1, 1000000000) == 1

    # -------------------------------------------------------
    # Performance cases (large inputs should finish in time)
    # -------------------------------------------------------
    def test_large_input(self):
        assert solution(1000000000, 999999999) == 1000000000
