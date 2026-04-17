import pytest
from .solution import solution


class TestDominator:
    # -------------------------------------------------------
    # Basic / Example cases
    # -------------------------------------------------------
    def test_example_1(self):
        A = [3, 4, 3, 2, 3, -1, 3, 3]
        result = solution(A)
        assert result != -1
        assert A[result] == 3

    def test_no_dominator(self):
        assert solution([1, 2, 3]) == -1

    # -------------------------------------------------------
    # Edge cases
    # -------------------------------------------------------
    def test_empty(self):
        assert solution([]) == -1

    def test_single(self):
        assert solution([5]) == 0

    def test_exactly_half(self):
        assert solution([1, 1, 2, 2]) == -1

    def test_two_same(self):
        A = [7, 7]
        result = solution(A)
        assert result in [0, 1]

    def test_dominator_at_end(self):
        A = [1, 2, 3, 3, 3]
        result = solution(A)
        assert result != -1
        assert A[result] == 3

    # -------------------------------------------------------
    # Performance cases (large inputs should finish in time)
    # -------------------------------------------------------
    def test_large_input(self):
        n = 100_000
        A = [42] * (n // 2 + 1) + list(range(n // 2 + 1, n))
        result = solution(A)
        assert result != -1
        assert A[result] == 42
