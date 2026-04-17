"""
Problem: Three Sum
Difficulty: Medium
Source: LeetCode #15
Tags: two-pointers, sorting

Problem Statement:
    Given an integer array nums, return all unique triplets
    [nums[i], nums[j], nums[k]] such that i != j != k and
    nums[i] + nums[j] + nums[k] == 0.

    The solution must not contain duplicate triplets.
    Return triplets in sorted order.

Examples:
    Example 1:
        Input:  nums = [-1, 0, 1, 2, -1, -4]
        Output: [[-1, -1, 2], [-1, 0, 1]]

    Example 2:
        Input:  nums = [0, 1, 1]
        Output: []

Constraints:
    - 3 <= N <= 3,000
    - O(n^2) expected

Hint (read only if stuck):
    Sort the array. For each element, use two pointers on the
    remaining portion to find pairs that sum to its negation.
    Skip duplicates to avoid duplicate triplets.
"""


def solution(nums: list[int]) -> list[list[int]]:
    # TODO: implement your solution here
    pass
