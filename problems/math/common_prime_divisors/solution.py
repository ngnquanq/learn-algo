"""
Problem: Common Prime Divisors
Difficulty: Hard
Source: Codility Lesson 12
Tags: math, gcd

Problem Statement:
    Given arrays A and B of Z integers, count pairs (A[i], B[i]) that
    have exactly the same set of prime divisors.

    For example, 15 and 75 have the same prime divisors {3, 5}.

Examples:
    Example 1:
        Input:  A = [15, 10, 3], B = [75, 30, 5]
        Output: 1
        Explanation: Only (15, 75) share primes {3, 5}.

Constraints:
    - 1 <= Z <= 6,000
    - 1 <= A[i], B[i] <= 2^30

Hint (read only if stuck):
    Two numbers have the same prime divisors iff:
    Let g = gcd(a, b). Then repeatedly divide a by gcd(a, g) until
    gcd is 1 or a is 1. Do the same for b. Both must reduce to 1.
"""


def solution(A: list[int], B: list[int]) -> int:
    # TODO: implement your solution here
    pass
