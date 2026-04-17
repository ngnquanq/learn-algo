import pytest
from .solution import solution


class TestClimbingStairs:
    # -------------------------------------------------------
    # Basic / Example cases
    # -------------------------------------------------------
    def test_example_1(self):
        assert solution(2) == 2

    def test_example_2(self):
        assert solution(3) == 3

    # -------------------------------------------------------
    # Edge cases
    # -------------------------------------------------------
    def test_one_step(self):
        assert solution(1) == 1

    def test_four_steps(self):
        assert solution(4) == 5

    def test_five_steps(self):
        assert solution(5) == 8

    def test_ten_steps(self):
        assert solution(10) == 89

    def test_max(self):
        assert solution(45) == 1836311903
