import pytest
from .solution import solution


class TestStoneWall:
    # -------------------------------------------------------
    # Basic / Example cases
    # -------------------------------------------------------
    def test_example_1(self):
        assert solution([8, 8, 5, 7, 9, 8, 7, 4, 8]) == 7

    # -------------------------------------------------------
    # Edge cases
    # -------------------------------------------------------
    def test_single(self):
        assert solution([5]) == 1

    def test_all_same(self):
        assert solution([5, 5, 5]) == 1

    def test_increasing(self):
        assert solution([1, 2, 3, 4, 5]) == 5

    def test_decreasing(self):
        assert solution([5, 4, 3, 2, 1]) == 5

    def test_valley(self):
        assert solution([3, 1, 3]) == 3

    def test_reuse_block(self):
        assert solution([1, 2, 1]) == 2

    # -------------------------------------------------------
    # Performance cases (large inputs should finish in time)
    # -------------------------------------------------------
    def test_large_input(self):
        n = 100_000
        H = [1] * n
        assert solution(H) == 1
