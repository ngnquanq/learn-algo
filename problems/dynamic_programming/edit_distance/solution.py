"""
Problem: Edit Distance
Difficulty: Hard
Source: LeetCode #72
Tags: dynamic-programming, string

Problem Statement:
    Given two strings word1 and word2, return the minimum number of
    operations required to convert word1 to word2.

    You have three operations:
    - Insert a character
    - Delete a character
    - Replace a character

Examples:
    Example 1:
        Input:  word1 = "horse", word2 = "ros"
        Output: 3
        Explanation: horse -> rorse (replace h with r) -> rose (remove r)
                     -> ros (remove e)

    Example 2:
        Input:  word1 = "intention", word2 = "execution"
        Output: 5

Constraints:
    - 0 <= |word1|, |word2| <= 500

Hint (read only if stuck):
    2D DP where dp[i][j] = min edits to convert word1[0..i-1] to word2[0..j-1].
    If characters match: dp[i][j] = dp[i-1][j-1].
    Otherwise: dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]).
"""


def solution(word1: str, word2: str) -> int:
    # TODO: implement your solution here
    pass
