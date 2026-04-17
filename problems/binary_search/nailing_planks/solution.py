"""
Problem: Nailing Planks
Difficulty: Hard
Source: Codility Lesson 14
Tags: binary-search, prefix-sums

Problem Statement:
    You have N planks, where plank i spans positions A[i] to B[i].
    You have M nails at positions C[0], C[1], ..., C[M-1].
    A plank is nailed if at least one nail falls within its range [A[i], B[i]].

    Using the first j nails (C[0..j-1]), find the minimum j such that all
    planks are nailed. Return -1 if it's impossible even with all nails.

Examples:
    Example 1:
        Input:  A = [1,4,5,8], B = [4,5,9,10], C = [4,6,7,10,2]
        Output: 4

Constraints:
    - 1 <= N, M <= 30,000
    - 1 <= A[i] <= B[i] <= 2*M

Hint (read only if stuck):
    Binary search on j (number of nails used). For each candidate j,
    build a prefix sum of nail positions (from C[0..j-1]) and check
    if every plank [A[i], B[i]] has at least one nail in its range.
"""


def solution(A: list[int], B: list[int], C: list[int]) -> int:
    # TODO: implement your solution here
    pass
