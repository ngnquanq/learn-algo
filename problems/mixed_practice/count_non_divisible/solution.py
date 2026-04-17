"""
Problem: Count Non-Divisible
Difficulty: Hard
Source: Codility Lesson 11
Tags: sieve, counting

Problem Statement:
    For each element A[i], count the number of elements in A that
    are NOT divisors of A[i].

Examples:
    Example 1:
        Input:  A = [3, 1, 2, 3, 6]
        Output: [2, 4, 3, 2, 0]

Constraints:
    - 1 <= N <= 50,000
    - 1 <= A[i] <= 2 * N

Hint (read only if stuck):
    Count occurrences of each value. For each unique value v, enumerate
    its divisors up to sqrt(v) and sum their occurrence counts.
    Non-divisors = N - divisor_count.
"""


def solution(A: list[int]) -> list[int]:
    # TODO: implement your solution here
    pass
