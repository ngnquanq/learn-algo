import pytest
from .solution import solution


class TestSolution:
    # -------------------------------------------------------
    # Basic / Example cases
    # -------------------------------------------------------
    def test_example_1(self):
        assert solution(...) == ...

    def test_example_2(self):
        assert solution(...) == ...

    # -------------------------------------------------------
    # Edge cases
    # -------------------------------------------------------
    def test_empty_input(self):
        assert solution([]) == ...

    def test_single_element(self):
        assert solution([1]) == ...

    # -------------------------------------------------------
    # Performance cases (large inputs should finish in time)
    # -------------------------------------------------------
    def test_large_input(self):
        n = 10 ** 6
        result = solution(list(range(n)))
        assert result == ...
