"""
Problem: Container With Most Water
Difficulty: Medium
Source: LeetCode #11
Tags: two-pointers, greedy

Problem Statement:
    Given n non-negative integers height[0], height[1], ..., height[n-1]
    representing vertical lines, find two lines that together with the
    x-axis form a container that holds the most water.

    Return the maximum amount of water a container can store.

Examples:
    Example 1:
        Input:  height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        Output: 49

    Example 2:
        Input:  height = [1, 1]
        Output: 1

Constraints:
    - 2 <= N <= 100,000
    - 0 <= height[i] <= 10,000

Hint (read only if stuck):
    Use two pointers starting from both ends.
    The water is limited by the shorter line.
    Move the pointer pointing to the shorter line inward.
"""


def solution(height: list[int]) -> int:
    # TODO: implement your solution here
    pass
