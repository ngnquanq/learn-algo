"""
Problem: Count Semiprimes
Difficulty: Hard
Source: Codility Lesson 11
Tags: math, sieve, prefix-sums

Problem Statement:
    A semiprime is a natural number that is the product of exactly
    two (not necessarily distinct) prime numbers: 4, 6, 9, 10, 14, 15...

    Given N and arrays P, Q of M queries, for each query return the
    count of semiprimes in the range [P[i], Q[i]].

Examples:
    Example 1:
        Input:  N = 26, P = [1, 4, 16], Q = [26, 10, 20]
        Output: [10, 4, 0]

Constraints:
    - 1 <= N <= 50,000
    - 1 <= M <= 30,000
    - 1 <= P[i] <= Q[i] <= N

Hint (read only if stuck):
    1. Use a sieve to find the smallest prime factor of each number.
    2. A number x is a semiprime if x / smallest_prime_factor(x) is prime.
    3. Build a prefix sum array of semiprimes.
    4. Answer each query in O(1) using prefix sums.
"""


def solution(N: int, P: list[int], Q: list[int]) -> list[int]:
    # TODO: implement your solution here
    pass
