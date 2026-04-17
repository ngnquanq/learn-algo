import pytest
from .solution import solution


class TestNetworkDelayTime:
    # -------------------------------------------------------
    # Basic / Example cases
    # -------------------------------------------------------
    def test_example_1(self):
        assert solution([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2) == 2

    def test_example_2(self):
        assert solution([[1, 2, 1]], 2, 2) == -1

    def test_example_3(self):
        assert solution([[1, 2, 1]], 2, 1) == 1

    # -------------------------------------------------------
    # Edge cases
    # -------------------------------------------------------
    def test_single_node(self):
        assert solution([], 1, 1) == 0

    def test_unreachable(self):
        assert solution([[1, 2, 1]], 3, 1) == -1

    def test_multiple_paths(self):
        assert solution([[1, 2, 10], [1, 3, 1], [3, 2, 1]], 3, 1) == 2

    # -------------------------------------------------------
    # Performance cases (large inputs should finish in time)
    # -------------------------------------------------------
    def test_large_input(self):
        n = 100
        times = []
        for i in range(1, n):
            times.append([i, i + 1, 1])
        assert solution(times, n, 1) == n - 1
