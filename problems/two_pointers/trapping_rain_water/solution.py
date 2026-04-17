"""
Problem: Trapping Rain Water
Difficulty: Hard
Source: LeetCode #42
Tags: two-pointers, dynamic-programming

Problem Statement:
    Given n non-negative integers representing an elevation map where
    the width of each bar is 1, compute how much water it can trap
    after raining.

Examples:
    Example 1:
        Input:  height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        Output: 6

    Example 2:
        Input:  height = [4, 2, 0, 3, 2, 5]
        Output: 9

Constraints:
    - 0 <= N <= 100,000
    - 0 <= height[i] <= 100,000

Hint (read only if stuck):
    Two-pointer approach: maintain left_max and right_max.
    Water at each position = min(left_max, right_max) - height[i].
    Process from the side with the smaller max.
"""


def solution(height: list[int]) -> int:
    # TODO: implement your solution here
    pass
