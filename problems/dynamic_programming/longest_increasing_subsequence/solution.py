"""
Problem: Longest Increasing Subsequence
Difficulty: Medium-Hard
Source: LeetCode #300
Tags: dynamic-programming, binary-search

Problem Statement:
    Given an integer array nums, return the length of the longest
    strictly increasing subsequence.

Examples:
    Example 1:
        Input:  nums = [10, 9, 2, 5, 3, 7, 101, 18]
        Output: 4
        Explanation: [2, 3, 7, 101] or [2, 5, 7, 101].

    Example 2:
        Input:  nums = [0, 1, 0, 3, 2, 3]
        Output: 4

Constraints:
    - 1 <= N <= 2,500
    - -10,000 <= nums[i] <= 10,000

Hint (read only if stuck):
    O(n^2): dp[i] = length of LIS ending at index i.
    dp[i] = max(dp[j] + 1) for all j < i where nums[j] < nums[i].

    O(n log n): Maintain a "tails" array. For each element, binary
    search for where it fits. This gives the optimal answer.
"""


def solution(nums: list[int]) -> int:
    # TODO: implement your solution here
    pass
