import pytest
from .solution import solution


class TestCyclicRotation:
    # -------------------------------------------------------
    # Basic / Example cases
    # -------------------------------------------------------
    def test_example_from_codility(self):
        assert solution([3, 8, 9, 7, 6], 3) == [9, 7, 6, 3, 8]

    def test_single_rotation(self):
        assert solution([1, 2, 3, 4], 1) == [4, 1, 2, 3]

    # -------------------------------------------------------
    # Edge cases
    # -------------------------------------------------------
    def test_empty_array(self):
        assert solution([], 5) == []

    def test_zero_rotations(self):
        assert solution([1, 2, 3], 0) == [1, 2, 3]

    def test_k_equals_length(self):
        """Full rotation should return original array."""
        assert solution([1, 2, 3], 3) == [1, 2, 3]

    def test_k_greater_than_length(self):
        assert solution([1, 2, 3], 7) == solution([1, 2, 3], 1)

    def test_single_element(self):
        assert solution([42], 100) == [42]

    # -------------------------------------------------------
    # Performance case
    # -------------------------------------------------------
    def test_large_input(self):
        n = 100
        A = list(range(n))
        result = solution(A, 1)
        assert result[0] == n - 1
