import pytest
from .solution import solution


class TestCountDiv:
    # -------------------------------------------------------
    # Basic / Example cases
    # -------------------------------------------------------
    def test_example_1(self):
        assert solution(6, 11, 2) == 3

    def test_zero_to_zero_k_one(self):
        assert solution(0, 0, 1) == 1

    # -------------------------------------------------------
    # Edge cases
    # -------------------------------------------------------
    def test_a_equals_b_divisible(self):
        assert solution(10, 10, 5) == 1

    def test_a_equals_b_not_divisible(self):
        assert solution(10, 10, 3) == 0

    def test_a_zero_b_zero_k_large(self):
        assert solution(0, 0, 11) == 1

    def test_k_greater_than_b(self):
        assert solution(5, 7, 20) == 0

    def test_k_greater_than_b_but_a_zero(self):
        assert solution(0, 7, 20) == 1

    def test_full_range(self):
        assert solution(0, 2_000_000_000, 1) == 2_000_000_001

    def test_a_equals_zero(self):
        # 0, 3, 6, 9 -> 4 values
        assert solution(0, 10, 3) == 4

    # -------------------------------------------------------
    # Performance cases (large inputs should finish in time)
    # -------------------------------------------------------
    def test_large_values(self):
        # Must be O(1), not iterative
        result = solution(0, 2_000_000_000, 2)
        assert result == 1_000_000_001
