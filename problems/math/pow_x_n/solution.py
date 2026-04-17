"""
Problem: Pow(x, n)
Difficulty: Medium
Source: LeetCode #50
Tags: math, binary-exponentiation, recursion

Problem Statement:
    Implement pow(x, n), which calculates x raised to the power n.

Examples:
    Example 1:
        Input:  x = 2.0, n = 10
        Output: 1024.0

    Example 2:
        Input:  x = 2.1, n = 3
        Output: 9.261

    Example 3:
        Input:  x = 2.0, n = -2
        Output: 0.25

Constraints:
    - -100.0 < x < 100.0
    - -2^31 <= n <= 2^31 - 1
    - n is an integer
    - x is not zero when n is negative

Hint (read only if stuck):
    Binary exponentiation: if n is even, pow(x, n) = pow(x*x, n//2).
    If n is odd, pow(x, n) = x * pow(x, n-1).
    Handle negative n by computing pow(1/x, -n).
"""


def solution(x: float, n: int) -> float:
    # TODO: implement your solution here
    pass
