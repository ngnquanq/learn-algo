"""
Problem: Min Abs Sum
Difficulty: Hard
Source: Codility Lesson 17
Tags: dynamic-programming, knapsack

Problem Statement:
    Given array A of N integers, you can multiply each element by
    +1 or -1. Find the minimum absolute value of the resulting sum.

    Formally: minimize |sum(A[i] * d[i])| where each d[i] is +1 or -1.

Examples:
    Example 1:
        Input:  A = [1, 5, 2, -2]
        Output: 0
        Explanation: |+1 -5 +2 -(-2)| = |1-5+2+2| = 0

Constraints:
    - 0 <= N <= 20,000
    - |A[i]| <= 100

Hint (read only if stuck):
    Take absolute values. Let S = sum of |A[i]|. We need to find a subset
    with sum closest to S/2 (then min abs sum = S - 2 * subset_sum).
    Since values are 0..100, count occurrences of each value and use DP
    on value counts rather than on individual elements.
"""


def solution(A: list[int]) -> int:
    # TODO: implement your solution here
    pass
