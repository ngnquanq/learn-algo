"""
Problem: Longest Common Subsequence
Difficulty: Medium
Source: LeetCode #1143
Tags: dynamic-programming, string

Problem Statement:
    Given two strings text1 and text2, return the length of their
    longest common subsequence. A subsequence is a sequence that can
    be derived from the string by deleting characters without changing
    the order. Return 0 if there is no common subsequence.

Examples:
    Example 1:
        Input:  text1 = "abcde", text2 = "ace"
        Output: 3
        Explanation: LCS is "ace".

    Example 2:
        Input:  text1 = "abc", text2 = "abc"
        Output: 3

    Example 3:
        Input:  text1 = "abc", text2 = "def"
        Output: 0

Constraints:
    - 1 <= |text1|, |text2| <= 1,000

Hint (read only if stuck):
    2D DP: if text1[i-1] == text2[j-1], dp[i][j] = dp[i-1][j-1] + 1.
    Otherwise dp[i][j] = max(dp[i-1][j], dp[i][j-1]).
"""


def solution(text1: str, text2: str) -> int:
    # TODO: implement your solution here
    pass
