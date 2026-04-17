"""
Problem: Minimum Window Substring
Difficulty: Hard
Source: LeetCode #76
Tags: sliding-window, hash-map

Problem Statement:
    Given two strings s and t, return the minimum window substring of s
    such that every character in t (including duplicates) is included
    in the window. Return "" if no such window exists.

Examples:
    Example 1:
        Input:  s = "ADOBECODEBANC", t = "ABC"
        Output: "BANC"

    Example 2:
        Input:  s = "a", t = "a"
        Output: "a"

    Example 3:
        Input:  s = "a", t = "aa"
        Output: ""

Constraints:
    - 1 <= |s|, |t| <= 100,000
    - s and t consist of uppercase and lowercase English letters

Hint (read only if stuck):
    Expand the right pointer to include all required characters.
    Once all are included, shrink from the left to find the minimum window.
    Use character frequency counters and a "formed" count.
"""


def solution(s: str, t: str) -> str:
    # TODO: implement your solution here
    pass
