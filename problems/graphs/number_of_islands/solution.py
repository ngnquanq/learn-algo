"""
Problem: Number of Islands
Difficulty: Medium
Source: LeetCode #200
Tags: graphs, BFS, DFS, matrix traversal, flood fill

Real-World Context:
    You are working on a GIS (Geographic Information System) feature for
    a mapping service (think Google Maps). You have a satellite image
    represented as a 2D grid where '1' = land and '0' = water.

    Your task: count how many distinct islands appear in the image.
    Two land cells are part of the same island if they are adjacent
    horizontally or vertically.

    This pattern also appears in: object detection, network cluster
    analysis, connected-component labelling in computer vision, and
    flood-fill tools in image editors.

Problem Statement:
    Given an m×n grid of characters '1' (land) and '0' (water),
    return the number of islands.

    An island is surrounded by water and is formed by connecting
    adjacent land cells horizontally or vertically.

Examples:
    Example 1:
        Input:
            grid = [
                ["1","1","1","1","0"],
                ["1","1","0","1","0"],
                ["1","1","0","0","0"],
                ["0","0","0","0","0"]
            ]
        Output: 1

    Example 2:
        Input:
            grid = [
                ["1","1","0","0","0"],
                ["1","1","0","0","0"],
                ["0","0","1","0","0"],
                ["0","0","0","1","1"]
            ]
        Output: 3

Constraints:
    - m == len(grid)
    - n == len(grid[0])
    - 1 <= m, n <= 300
    - grid[i][j] is '0' or '1'

Hint (read only if stuck):
    Iterate every cell. When you find a '1' (unvisited land):
    - Increment your island counter.
    - "Sink" the entire island using BFS or DFS — mark every connected
      land cell as visited (e.g. replace '1' with '0') so you don't
      count it again.
    A queue-based BFS with 4-directional neighbours works cleanly.
"""


from collections import deque


def solution(grid: list[list[str]]) -> int:
    """Calculates the number of islands in a 2D grid using BFS.
    
    Time Complexity: O(M * N) where M is rows and N is columns.
    Space Complexity: O(min(M, N)) for the BFS queue in worst case.
    """
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    island_count = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                # Found a new island
                island_count += 1
                # Start sinking the island using BFS
                queue = deque([(r, c)])
                grid[r][c] = "0"  # Mark as visited (sink)

                while queue:
                    curr_r, curr_c = queue.popleft()
                    
                    # Check 4-directional neighbors
                    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        nr, nc = curr_r + dr, curr_c + dc
                        
                        if (0 <= nr < rows and 0 <= nc < cols and 
                                grid[nr][nc] == "1"):
                            grid[nr][nc] = "0"  # Sink it
                            queue.append((nr, nc))

    return island_count
