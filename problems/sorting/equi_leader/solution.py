"""
Problem: Equi Leader
Difficulty: Medium
Source: Codility Lesson 8
Tags: arrays, leader, prefix

Problem Statement:
    An equi leader is an index S such that the leader of A[0..S] equals
    the leader of A[S+1..N-1]. A leader is an element that occurs in more
    than half the elements of a sequence.

    Count the number of equi leaders.

Examples:
    Example 1:
        Input:  A = [4, 3, 4, 4, 4, 2]
        Output: 2

    Example 2:
        Input:  A = [1, 2, 3, 4, 5]
        Output: 0

Constraints:
    - 1 <= N <= 100,000

Hint (read only if stuck):
    First find the leader of the whole array using Boyer-Moore voting.
    Then scan left to right, maintaining prefix count of the leader.
    At each split point, check if the leader dominates both halves.
"""


def solution(A: list[int]) -> int:
    # TODO: implement your solution here
    pass
