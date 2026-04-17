"""
Problem: Jump Game
Difficulty: Medium
Source: LeetCode #55
Tags: greedy, arrays

Problem Statement:
    Given an array of non-negative integers nums, you are initially
    positioned at the first index. Each element represents your maximum
    jump length from that position.

    Determine if you can reach the last index.

Examples:
    Example 1:
        Input:  nums = [2, 3, 1, 1, 4]
        Output: True

    Example 2:
        Input:  nums = [3, 2, 1, 0, 4]
        Output: False

Constraints:
    - 1 <= N <= 100,000
    - 0 <= nums[i] <= 100,000

Hint (read only if stuck):
    Track the farthest reachable index. Iterate through the array:
    if the current index exceeds the farthest reachable, return False.
    Otherwise update farthest = max(farthest, i + nums[i]).
"""


def solution(nums: list[int]) -> bool:
    # TODO: implement your solution here
    pass
