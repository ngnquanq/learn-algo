import pytest
from .solution import solution


class TestMinimumPathSum:
    # -------------------------------------------------------
    # Basic / Example cases
    # -------------------------------------------------------
    def test_example_1(self):
        assert solution([[1, 3, 1], [1, 5, 1], [4, 2, 1]]) == 7

    def test_example_2(self):
        assert solution([[1, 2, 3], [4, 5, 6]]) == 12

    # -------------------------------------------------------
    # Edge cases
    # -------------------------------------------------------
    def test_single_cell(self):
        assert solution([[5]]) == 5

    def test_single_row(self):
        assert solution([[1, 2, 3]]) == 6

    def test_single_column(self):
        assert solution([[1], [2], [3]]) == 6

    def test_all_zeros(self):
        assert solution([[0, 0], [0, 0]]) == 0

    # -------------------------------------------------------
    # Performance cases (large inputs should finish in time)
    # -------------------------------------------------------
    def test_large_grid(self):
        n = 200
        grid = [[1] * n for _ in range(n)]
        assert solution(grid) == 2 * n - 1
