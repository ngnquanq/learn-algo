"""
Problem: Count Distinct Slices
Difficulty: Hard
Source: Codility Lesson 15
Tags: two-pointers, caterpillar

Problem Statement:
    An integer M and a non-empty array A of N integers are given.
    A pair (P, Q) where 0 <= P <= Q < N is called a "distinct slice"
    if all elements A[P], A[P+1], ..., A[Q] are distinct.

    Count the number of distinct slices. If the count exceeds
    1,000,000,000, return 1,000,000,000.

Examples:
    Example 1:
        Input:  M = 6, A = [3, 4, 5, 5, 2]
        Output: 9

Constraints:
    - 0 <= N <= 100,000
    - 0 <= A[i] <= M

Hint (read only if stuck):
    Use two pointers (caterpillar method). For each right boundary,
    the number of new slices ending there is (right - left + 1).
    When a duplicate is found, advance the left pointer past the
    previous occurrence.
"""


def solution(M: int, A: list[int]) -> int:
    # TODO: implement your solution here
    pass
