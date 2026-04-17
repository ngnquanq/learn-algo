import pytest
from .solution import solution


class TestKokoEatingBananas:
    # -------------------------------------------------------
    # Basic / Example cases
    # -------------------------------------------------------
    def test_example_1(self):
        assert solution([3, 6, 7, 11], 8) == 4

    def test_example_2(self):
        assert solution([30, 11, 23, 4, 20], 5) == 30

    def test_example_3(self):
        assert solution([30, 11, 23, 4, 20], 6) == 23

    # -------------------------------------------------------
    # Edge cases
    # -------------------------------------------------------
    def test_single_pile(self):
        assert solution([100], 100) == 1

    def test_h_equals_n(self):
        assert solution([3, 6, 7, 11], 4) == 11

    def test_all_ones(self):
        assert solution([1, 1, 1], 3) == 1

    def test_large_pile_lots_of_time(self):
        assert solution([1000000000], 1000000000) == 1

    # -------------------------------------------------------
    # Performance cases (large inputs should finish in time)
    # -------------------------------------------------------
    def test_large_input(self):
        n = 10_000
        piles = [1_000_000_000] * n
        h = n
        assert solution(piles, h) == 1_000_000_000
