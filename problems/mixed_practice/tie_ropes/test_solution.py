import pytest
from .solution import solution


class TestTieRopes:
    # -------------------------------------------------------
    # Basic / Example cases
    # -------------------------------------------------------
    def test_example_1(self):
        assert solution(4, [1, 2, 3, 4, 1, 1, 3]) == 3

    # -------------------------------------------------------
    # Edge cases
    # -------------------------------------------------------
    def test_single_rope_enough(self):
        assert solution(4, [4]) == 1

    def test_single_rope_not_enough(self):
        assert solution(4, [3]) == 0

    def test_all_enough(self):
        assert solution(1, [1, 1, 1]) == 3

    def test_none_enough(self):
        assert solution(100, [1, 1, 1]) == 0

    def test_all_large(self):
        assert solution(4, [4, 4, 4]) == 3

    # -------------------------------------------------------
    # Performance cases (large inputs should finish in time)
    # -------------------------------------------------------
    def test_large_input(self):
        n = 100_000
        A = [1] * n
        assert solution(1, A) == n
