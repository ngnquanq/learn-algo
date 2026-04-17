"""
Problem: Max Product of Three
Difficulty: Medium
Source: Codility Lesson 6
Tags: sorting, arrays

Problem Statement:
    A non-empty array A of N integers is given. The product of triplet
    (P, Q, R) is A[P] * A[Q] * A[R] where 0 <= P < Q < R < N.

    Find the maximal product of any triplet.

Examples:
    Example 1:
        Input:  A = [-3, 1, 2, -2, 5, 6]
        Output: 60

Constraints:
    - 3 <= N <= 100,000
    - each element of array A is an integer within the range [-1000 .. 1000]

Hint (read only if stuck):
    Sort the array. The answer is the maximum of (product of last 3 elements)
    vs (product of first 2 elements * last element). Two large negatives can
    produce a large positive product.
"""


def solution(A: list[int]) -> int:
    # TODO: implement your solution here
    pass
