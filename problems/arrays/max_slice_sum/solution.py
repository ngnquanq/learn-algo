"""
Problem: Max Slice Sum
Difficulty: Medium
Source: Codility Lesson 9 / LeetCode #53
Tags: arrays, dynamic-programming, kadane

Problem Statement:
    Find the maximum sum of a contiguous subarray of a given array A.
    The subarray must contain at least one element.

Examples:
    Example 1:
        Input:  A = [3, 2, -6, 4, 0]
        Output: 5
        Explanation: Subarray [3, 2] has sum 5.

    Example 2:
        Input:  A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        Output: 6
        Explanation: Subarray [4, -1, 2, 1] has sum 6.

Constraints:
    - 1 <= N <= 1,000,000
    - -1,000,000 <= A[i] <= 1,000,000

Hint (read only if stuck):
    Kadane's algorithm: max_ending_here = max(A[i], max_ending_here + A[i]).
    Track the global maximum across all positions.
"""


def solution(A: list[int]) -> int:
    # TODO: implement your solution here
    pass
