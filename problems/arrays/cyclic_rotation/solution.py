"""
Problem: Cyclic Rotation
Difficulty: Easy
Source: Codility - Arrays

Problem Statement:
    An array A consisting of N integers is given. Rotation of the array means
    that each element is shifted right by one index, and the last element of
    the array is moved to the first place.

    Goal: Rotate array A K times, return the resulting array.

Examples:
    Input:  A = [3, 8, 9, 7, 6], K = 3
    Output: [9, 7, 6, 3, 8]

Constraints:
    - 0 <= N <= 100
    - 0 <= K <= 100
    - each element of A is an integer in range [-1000, 1000]
"""


def solution(A: list[int], K: int) -> list[int]:
    if not A:
        return A
    K = K % len(A)
    return A[-K:] + A[:-K] if K else A[:]
