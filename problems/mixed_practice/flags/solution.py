"""
Problem: Flags
Difficulty: Hard
Source: Codility Lesson 10
Tags: binary-search, greedy

Problem Statement:
    A non-empty array A of N integers is given. A peak is an element
    that is greater than its neighbors: A[i] > A[i-1] and A[i] > A[i+1].

    You want to set K flags on K different peaks. The distance between
    any two flags must be >= K. Find the maximum number of flags that
    can be set.

Examples:
    Example 1:
        Input:  A = [1, 5, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]
        Output: 3

Constraints:
    - 1 <= N <= 400,000

Hint (read only if stuck):
    First find all peaks. Then iterate (or binary search) on K
    from 1 to sqrt(N). For each K, greedily place flags from left
    to right ensuring distance >= K between consecutive flags.
    The maximum K that allows placing >= K flags is the answer.
"""


def solution(A: list[int]) -> int:
    # TODO: implement your solution here
    pass
