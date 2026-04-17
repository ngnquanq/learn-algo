import pytest
from .solution import solution


class TestFlags:
    # -------------------------------------------------------
    # Basic / Example cases
    # -------------------------------------------------------
    def test_example_1(self):
        assert solution([1, 5, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]) == 3

    # -------------------------------------------------------
    # Edge cases
    # -------------------------------------------------------
    def test_no_peaks(self):
        assert solution([1, 2, 3]) == 0

    def test_single_peak(self):
        assert solution([1, 2, 1]) == 1

    def test_monotonic(self):
        assert solution([1, 2, 3, 4, 5]) == 0

    def test_plateau(self):
        assert solution([1, 2, 2, 1]) == 0

    def test_two_adjacent_peaks(self):
        assert solution([1, 3, 1, 3, 1]) == 2

    # -------------------------------------------------------
    # Performance cases (large inputs should finish in time)
    # -------------------------------------------------------
    def test_large_input(self):
        n = 400_000
        A = [1, 3] * (n // 2)
        A.append(1)
        result = solution(A)
        assert result >= 1
