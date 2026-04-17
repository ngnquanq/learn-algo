"""
Problem: Min Max Division
Difficulty: Hard
Source: Codility Lesson 14
Tags: binary-search, greedy

Problem Statement:
    Divide array A of N integers into K blocks (contiguous segments)
    to minimize the maximum sum among blocks.

    Each block must contain at least one element. Return the minimized
    maximum block sum.

Examples:
    Example 1:
        Input:  K = 3, M = 5, A = [2, 1, 5, 1, 2, 2, 2]
        Output: 6
        Explanation: [2,1], [5,1], [2,2,2] — max sum is 6.

Constraints:
    - 1 <= K, N <= 100,000
    - 0 <= A[i] <= M <= 10,000

Hint (read only if stuck):
    Binary search on the answer. The answer is between max(A) and sum(A).
    For a candidate max sum, greedily check if you can split into <= K blocks.
"""


def solution(K: int, M: int, A: list[int]) -> int:
    # TODO: implement your solution here
    pass
