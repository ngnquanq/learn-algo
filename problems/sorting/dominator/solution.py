"""
Problem: Dominator
Difficulty: Medium
Source: Codility Lesson 8
Tags: arrays, leader, boyer-moore

Problem Statement:
    An element of array A is a dominator if it occurs in more than half
    of the elements of A. Return the index of any dominator element.
    Return -1 if no dominator exists.

Examples:
    Example 1:
        Input:  A = [3, 4, 3, 2, 3, -1, 3, 3]
        Output: 0 (or any index where A[i] == 3)

    Example 2:
        Input:  A = [1, 2, 3]
        Output: -1

Constraints:
    - 0 <= N <= 100,000
    - Values can be any integer

Hint (read only if stuck):
    Use Boyer-Moore majority vote algorithm to find a candidate,
    then verify it actually occurs more than N/2 times.
"""


def solution(A: list[int]) -> int:
    # TODO: implement your solution here
    pass
