"""
Problem: Partition Equal Subset Sum
Difficulty: Medium-Hard
Source: LeetCode #416
Tags: dynamic-programming, knapsack

Problem Statement:
    Given an integer array nums, return True if you can partition the
    array into two subsets such that the sum of elements in both subsets
    is equal. Otherwise return False.

Examples:
    Example 1:
        Input:  nums = [1, 5, 11, 5]
        Output: True
        Explanation: [1, 5, 5] and [11].

    Example 2:
        Input:  nums = [1, 2, 3, 5]
        Output: False

Constraints:
    - 1 <= N <= 200
    - 1 <= nums[i] <= 100

Hint (read only if stuck):
    If total sum is odd, return False immediately.
    Otherwise, this is a 0/1 knapsack problem: can you pick a subset
    that sums to total // 2? Use a boolean DP array.
"""


def solution(nums: list[int]) -> bool:
    # TODO: implement your solution here
    pass
