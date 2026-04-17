"""
Problem: Tie Ropes
Difficulty: Medium
Source: Codility (common assessment)
Tags: greedy

Problem Statement:
    There are N ropes with lengths given in array A.
    You can tie two adjacent ropes together (their lengths are summed).
    Find the maximum number of ropes with length >= K that can be
    created by tying adjacent ropes.

Examples:
    Example 1:
        Input:  K = 4, A = [1, 2, 3, 4, 1, 1, 3]
        Output: 3

Constraints:
    - 1 <= N <= 100,000
    - 1 <= A[i], K <= 1,000,000,000

Hint (read only if stuck):
    Greedy: scan left to right, accumulating rope lengths.
    When the accumulated length >= K, count one rope and reset
    the accumulator to 0.
"""


def solution(K: int, A: list[int]) -> int:
    # TODO: implement your solution here
    pass
