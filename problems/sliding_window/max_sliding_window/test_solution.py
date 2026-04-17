import pytest
from .solution import solution


class TestMaxSlidingWindow:
    # -------------------------------------------------------
    # Basic / Example cases
    # -------------------------------------------------------
    def test_example_1(self):
        assert solution([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]

    def test_example_2(self):
        assert solution([1], 1) == [1]

    # -------------------------------------------------------
    # Edge cases
    # -------------------------------------------------------
    def test_k_equals_1(self):
        assert solution([5, 3, 4], 1) == [5, 3, 4]

    def test_k_equals_n(self):
        assert solution([1, 3, -1, -3, 5], 5) == [5]

    def test_all_same(self):
        assert solution([5, 5, 5, 5], 2) == [5, 5, 5]

    def test_decreasing(self):
        assert solution([5, 4, 3, 2, 1], 3) == [5, 4, 3]

    def test_increasing(self):
        assert solution([1, 2, 3, 4, 5], 3) == [3, 4, 5]

    # -------------------------------------------------------
    # Performance cases (large inputs should finish in time)
    # -------------------------------------------------------
    def test_large_input(self):
        n = 100_000
        nums = list(range(n))
        k = 50_000
        result = solution(nums, k)
        assert len(result) == n - k + 1
        assert result[-1] == n - 1
