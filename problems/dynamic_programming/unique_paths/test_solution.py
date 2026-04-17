import pytest
from .solution import solution


class TestUniquePaths:
    # -------------------------------------------------------
    # Basic / Example cases
    # -------------------------------------------------------
    def test_example_1(self):
        assert solution(3, 7) == 28

    def test_example_2(self):
        assert solution(3, 2) == 3

    # -------------------------------------------------------
    # Edge cases
    # -------------------------------------------------------
    def test_1x1(self):
        assert solution(1, 1) == 1

    def test_1xn(self):
        assert solution(1, 5) == 1

    def test_nx1(self):
        assert solution(5, 1) == 1

    def test_2x2(self):
        assert solution(2, 2) == 2

    def test_10x10(self):
        assert solution(10, 10) == 48620

    # -------------------------------------------------------
    # Performance cases (large inputs should finish in time)
    # -------------------------------------------------------
    def test_large_grid(self):
        result = solution(100, 100)
        assert result > 0
