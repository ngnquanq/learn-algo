import pytest
from .solution import solution


class TestNumberOfDiscIntersections:
    # -------------------------------------------------------
    # Basic / Example cases
    # -------------------------------------------------------
    def test_example_1(self):
        assert solution([1, 5, 2, 1, 4, 0]) == 11

    def test_three_discs(self):
        assert solution([1, 1, 1]) == 3

    # -------------------------------------------------------
    # Edge cases
    # -------------------------------------------------------
    def test_empty(self):
        assert solution([]) == 0

    def test_single(self):
        assert solution([0]) == 0

    def test_no_overlap(self):
        assert solution([0, 0, 0, 0]) == 0

    def test_large_radius(self):
        assert solution([1000000000, 1000000000]) == 1

    def test_exceeds_limit(self):
        n = 100_000
        A = [n] * n
        assert solution(A) == -1

    # -------------------------------------------------------
    # Performance cases (large inputs should finish in time)
    # -------------------------------------------------------
    def test_large_input(self):
        n = 100_000
        A = [0] * n
        assert solution(A) == 0
