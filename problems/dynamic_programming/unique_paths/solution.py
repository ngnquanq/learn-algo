"""
Problem: Unique Paths
Difficulty: Medium
Source: LeetCode #62
Tags: dynamic-programming, grid

Problem Statement:
    A robot is located at the top-left corner of an m x n grid.
    It can only move right or down at any point. How many unique
    paths are there to reach the bottom-right corner?

Examples:
    Example 1:
        Input:  m = 3, n = 7
        Output: 28

    Example 2:
        Input:  m = 3, n = 2
        Output: 3

Constraints:
    - 1 <= m, n <= 100

Hint (read only if stuck):
    dp[i][j] = dp[i-1][j] + dp[i][j-1].
    The first row and first column are all 1s (only one way to reach them).
"""


def solution(m: int, n: int) -> int:
    # TODO: implement your solution here
    pass
