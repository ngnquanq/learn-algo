"""
Problem: Sliding Window Maximum
Difficulty: Hard
Source: LeetCode #239
Tags: sliding-window, monotonic-deque

Problem Statement:
    Given an array of integers nums and a sliding window of size k,
    return the max value in each window as the window moves from
    left to right.

Examples:
    Example 1:
        Input:  nums = [1,3,-1,-3,5,3,6,7], k = 3
        Output: [3,3,5,5,6,7]

    Example 2:
        Input:  nums = [1], k = 1
        Output: [1]

Constraints:
    - 1 <= N <= 100,000
    - 1 <= k <= N
    - -10,000 <= nums[i] <= 10,000

Hint (read only if stuck):
    Use a monotonic decreasing deque that stores indices.
    For each new element: remove indices out of window from front,
    remove smaller elements from back, then add current index.
    The front of the deque is always the max of the current window.
"""


def solution(nums: list[int], k: int) -> list[int]:
    # TODO: implement your solution here
    pass
