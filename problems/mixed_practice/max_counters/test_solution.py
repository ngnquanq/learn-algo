import pytest
from .solution import solution


class TestMaxCounters:
    # -------------------------------------------------------
    # Basic / Example cases
    # -------------------------------------------------------
    def test_example_1(self):
        assert solution(5, [3, 4, 4, 6, 1, 4, 4]) == [3, 2, 2, 4, 2]

    # -------------------------------------------------------
    # Edge cases
    # -------------------------------------------------------
    def test_single_counter(self):
        assert solution(1, [1, 1, 1]) == [3]

    def test_all_max_counter(self):
        assert solution(3, [4, 4, 4]) == [0, 0, 0]

    def test_no_operations(self):
        assert solution(3, []) == [0, 0, 0]

    def test_increment_then_max(self):
        assert solution(2, [1, 2, 3, 1]) == [2, 1]

    # -------------------------------------------------------
    # Performance cases (large inputs should finish in time)
    # -------------------------------------------------------
    def test_large_input(self):
        n = 100_000
        # Alternate increment and max counter
        A = []
        for i in range(n):
            A.append(1)
            A.append(n + 1)
        result = solution(n, A)
        assert len(result) == n
