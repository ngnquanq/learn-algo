import pytest
from .solution import solution


class TestThreeSum:
    # -------------------------------------------------------
    # Basic / Example cases
    # -------------------------------------------------------
    def test_example_1(self):
        result = solution([-1, 0, 1, 2, -1, -4])
        expected = [[-1, -1, 2], [-1, 0, 1]]
        assert sorted([sorted(t) for t in result]) == sorted([sorted(t) for t in expected])

    def test_example_2(self):
        assert solution([0, 1, 1]) == []

    # -------------------------------------------------------
    # Edge cases
    # -------------------------------------------------------
    def test_all_zeros(self):
        result = solution([0, 0, 0])
        assert sorted([sorted(t) for t in result]) == [[0, 0, 0]]

    def test_four_zeros(self):
        result = solution([0, 0, 0, 0])
        assert sorted([sorted(t) for t in result]) == [[0, 0, 0]]

    def test_no_triplet(self):
        assert solution([1, 2, 3]) == []

    def test_simple_triplet(self):
        result = solution([-1, 0, 1])
        assert sorted([sorted(t) for t in result]) == [[-1, 0, 1]]

    # -------------------------------------------------------
    # Performance cases (large inputs should finish in time)
    # -------------------------------------------------------
    def test_large_input(self):
        nums = list(range(-1500, 1501))
        result = solution(nums)
        assert isinstance(result, list)
        assert len(result) > 0
