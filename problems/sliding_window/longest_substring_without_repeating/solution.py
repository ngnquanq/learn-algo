"""
Problem: Longest Substring Without Repeating Characters
Difficulty: Medium
Source: LeetCode #3
Tags: sliding-window, hash-map

Problem Statement:
    Given a string s, find the length of the longest substring
    without repeating characters.

Examples:
    Example 1:
        Input:  s = "abcabcbb"
        Output: 3
        Explanation: "abc"

    Example 2:
        Input:  s = "bbbbb"
        Output: 1

    Example 3:
        Input:  s = "pwwkew"
        Output: 3
        Explanation: "wke"

Constraints:
    - 0 <= |s| <= 50,000
    - s consists of English letters, digits, symbols, and spaces

Hint (read only if stuck):
    Sliding window with a set or dictionary tracking characters
    in the current window. When a duplicate is found, shrink the
    window from the left until the duplicate is removed.
"""


def solution(s: str) -> int:
    # TODO: implement your solution here
    pass
