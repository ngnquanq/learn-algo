"""
Problem: House Robber
Difficulty: Medium
Source: LeetCode #198
Tags: dynamic-programming

Problem Statement:
    You are a robber planning to rob houses along a street.
    Each house has a certain amount of money. Adjacent houses have
    security systems connected — if two adjacent houses are broken
    into on the same night, the police will be alerted.

    Maximize the amount of money you can rob without alerting the police.

Examples:
    Example 1:
        Input:  nums = [1, 2, 3, 1]
        Output: 4
        Explanation: Rob house 0 (1) and house 2 (3) = 4.

    Example 2:
        Input:  nums = [2, 7, 9, 3, 1]
        Output: 12
        Explanation: Rob house 0 (2), house 2 (9), house 4 (1) = 12.

Constraints:
    - 1 <= N <= 100
    - 0 <= nums[i] <= 400

Hint (read only if stuck):
    dp[i] = max(dp[i-1], dp[i-2] + nums[i]).
    You either skip house i (take dp[i-1]) or rob it (dp[i-2] + nums[i]).
"""


def solution(nums: list[int]) -> int:
    # TODO: implement your solution here
    pass
