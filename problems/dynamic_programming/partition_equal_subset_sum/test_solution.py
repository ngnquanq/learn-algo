import pytest
from .solution import solution


class TestPartitionEqualSubsetSum:
    # -------------------------------------------------------
    # Basic / Example cases
    # -------------------------------------------------------
    def test_example_1(self):
        assert solution([1, 5, 11, 5]) is True

    def test_example_2(self):
        assert solution([1, 2, 3, 5]) is False

    # -------------------------------------------------------
    # Edge cases
    # -------------------------------------------------------
    def test_single_element(self):
        assert solution([1]) is False

    def test_two_equal(self):
        assert solution([1, 1]) is True

    def test_odd_total(self):
        assert solution([1, 2, 4]) is False

    def test_all_same_even_count(self):
        assert solution([2, 2, 2, 2]) is True

    def test_large_single(self):
        assert solution([100]) is False

    def test_many_ones(self):
        assert solution([1] * 200) is True

    # -------------------------------------------------------
    # Performance cases (large inputs should finish in time)
    # -------------------------------------------------------
    def test_large_input(self):
        nums = list(range(1, 101))  # sum = 5050, odd -> False
        assert solution(nums) is False

    def test_large_input_true(self):
        nums = [1] * 200
        assert solution(nums) is True
