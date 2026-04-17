"""
Problem: Chocolates by Numbers (GCD/LCM)
Difficulty: Medium
Source: Codility Lesson 12 - Euclidean Algorithm
Tags: math, gcd, euclidean-algorithm

Problem Statement:
    There are N chocolates arranged in a circle, numbered 0 to N-1.
    You start at chocolate 0 and eat it. Then you always move M
    positions clockwise and eat the chocolate there (wrapping around).
    You stop when you return to position 0.

    How many chocolates do you eat?

    The answer is N // gcd(N, M).

Examples:
    Example 1:
        Input:  N = 10, M = 4
        Output: 5

    Example 2:
        Input:  N = 12, M = 8
        Output: 3

Constraints:
    - 1 <= N, M <= 1,000,000,000

Hint (read only if stuck):
    The answer is N / gcd(N, M). Implement GCD using the Euclidean
    algorithm: gcd(a, b) = gcd(b, a % b), base case gcd(a, 0) = a.
"""


def solution(N: int, M: int) -> int:
    # TODO: implement your solution here
    pass
