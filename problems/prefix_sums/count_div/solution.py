"""
Problem: Count Div
Difficulty: Medium
Source: Codility Lesson 5
Tags: prefix-sums, math

Problem Statement:
    Given three integers A, B and K, return the number of integers within
    the range [A..B] that are divisible by K.

Examples:
    Example 1:
        Input:  A = 6, B = 11, K = 2
        Output: 3
        Explanation: 6, 8, 10 are divisible by 2

Constraints:
    - 0 <= A <= B <= 2,000,000,000
    - 1 <= K <= 2,000,000,000

Hint (read only if stuck):
    Formula: B // K - (A - 1) // K. Handle A = 0 case carefully, or use the
    equivalent: B // K - A // K + (1 if A % K == 0 else 0).
"""


def solution(A: int, B: int, K: int) -> int:
    # TODO: implement your solution here
    pass
