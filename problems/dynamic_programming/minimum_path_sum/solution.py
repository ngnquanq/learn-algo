"""
Problem: Minimum Path Sum
Difficulty: Medium
Source: LeetCode #64
Tags: dynamic-programming, grid

Problem Statement:
    Given an m x n grid filled with non-negative numbers, find a path
    from the top-left to the bottom-right which minimizes the sum of
    all numbers along its path.

    You can only move right or down at any step.

Examples:
    Example 1:
        Input:  grid = [[1,3,1],[1,5,1],[4,2,1]]
        Output: 7
        Explanation: Path 1->3->1->1->1 = 7.

    Example 2:
        Input:  grid = [[1,2,3],[4,5,6]]
        Output: 12

Constraints:
    - 1 <= m, n <= 200
    - 0 <= grid[i][j] <= 200

Hint (read only if stuck):
    dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1]).
    Handle first row and column specially (can only come from one direction).
"""


def solution(grid: list[list[int]]) -> int:
    # TODO: implement your solution here
    pass
