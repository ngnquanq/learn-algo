import pytest
from .solution import solution


class TestRedundantConnection:
    # -------------------------------------------------------
    # Basic / Example cases
    # -------------------------------------------------------
    def test_example_1(self):
        assert solution([[1, 2], [1, 3], [2, 3]]) == [2, 3]

    def test_example_2(self):
        assert solution([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]) == [1, 4]

    # -------------------------------------------------------
    # Edge cases
    # -------------------------------------------------------
    def test_minimum_graph(self):
        assert solution([[1, 2], [2, 3], [1, 3]]) == [1, 3]

    def test_last_edge_redundant(self):
        assert solution([[1, 2], [2, 3], [3, 1]]) == [3, 1]

    # -------------------------------------------------------
    # Performance cases (large inputs should finish in time)
    # -------------------------------------------------------
    def test_large_input(self):
        n = 1000
        edges = [[i, i + 1] for i in range(1, n)]
        edges.append([1, n - 1])  # redundant edge
        assert solution(edges) == [1, n - 1]
