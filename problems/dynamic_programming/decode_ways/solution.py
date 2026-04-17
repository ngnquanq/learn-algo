"""
Problem: Decode Ways
Difficulty: Medium
Source: LeetCode #91
Tags: dynamic-programming, string

Problem Statement:
    A message containing letters A-Z can be encoded as numbers:
    'A' -> "1", 'B' -> "2", ..., 'Z' -> "26".

    Given a string s containing only digits, return the number of
    ways to decode it. Leading zeros are invalid (e.g., "06" cannot
    be decoded).

Examples:
    Example 1:
        Input:  s = "12"
        Output: 2
        Explanation: "AB" (1,2) or "L" (12).

    Example 2:
        Input:  s = "226"
        Output: 3
        Explanation: "BZ" (2,26), "VF" (22,6), or "BBF" (2,2,6).

    Example 3:
        Input:  s = "06"
        Output: 0
        Explanation: "06" has a leading zero, invalid.

Constraints:
    - 1 <= |s| <= 100
    - s contains only digits

Hint (read only if stuck):
    dp[i] counts decodings of s[0..i-1].
    If s[i-1] != '0', dp[i] += dp[i-1] (single digit decode).
    If 10 <= int(s[i-2:i]) <= 26, dp[i] += dp[i-2] (two digit decode).
"""


def solution(s: str) -> int:
    # TODO: implement your solution here
    pass
