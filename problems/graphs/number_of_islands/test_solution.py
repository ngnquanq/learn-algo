import pytest
from .solution import solution


class TestNumberOfIslands:
    # -------------------------------------------------------
    # Basic / Example cases
    # -------------------------------------------------------
    def test_one_large_island(self):
        grid = [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ]
        assert solution(grid) == 1

    def test_three_islands(self):
        grid = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ]
        assert solution(grid) == 3

    # -------------------------------------------------------
    # Edge cases
    # -------------------------------------------------------
    def test_all_water(self):
        grid = [
            ["0", "0", "0"],
            ["0", "0", "0"],
        ]
        assert solution(grid) == 0

    def test_all_land(self):
        # Entire grid is one connected island
        grid = [
            ["1", "1", "1"],
            ["1", "1", "1"],
        ]
        assert solution(grid) == 1

    def test_single_cell_land(self):
        assert solution([["1"]]) == 1

    def test_single_cell_water(self):
        assert solution([["0"]]) == 0

    def test_diagonal_not_connected(self):
        # Diagonal cells are NOT connected — 4 islands, not 1
        grid = [
            ["1", "0", "1"],
            ["0", "1", "0"],
            ["1", "0", "1"],
        ]
        assert solution(grid) == 5

    def test_thin_horizontal_island(self):
        grid = [["1", "1", "1", "1", "1"]]
        assert solution(grid) == 1

    def test_thin_vertical_island(self):
        grid = [["1"], ["1"], ["1"], ["1"]]
        assert solution(grid) == 1

    def test_checkerboard(self):
        # Every '1' is isolated — each is its own island
        grid = [
            ["1", "0", "1", "0"],
            ["0", "1", "0", "1"],
            ["1", "0", "1", "0"],
        ]
        assert solution(grid) == 6

    # -------------------------------------------------------
    # Performance case
    # -------------------------------------------------------
    def test_large_all_land(self):
        # 300×300 solid land = 1 island, must finish within timeout
        grid = [["1"] * 300 for _ in range(300)]
        assert solution(grid) == 1

    def test_large_checkerboard(self):
        # 100×100 checkerboard — many isolated islands
        grid = [
            ["1" if (r + c) % 2 == 0 else "0" for c in range(100)]
            for r in range(100)
        ]
        result = solution(grid)
        assert result == 5000  # half the cells, each isolated
