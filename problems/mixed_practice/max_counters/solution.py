"""
Problem: Max Counters
Difficulty: Hard
Source: Codility Lesson 4
Tags: arrays, counting, lazy-propagation

Problem Statement:
    You are given N counters, all initially set to 0, and M operations:
    - increase(X): counter X is increased by 1 (1 <= X <= N)
    - max counter: all counters are set to the maximum counter value

    Operations are given as array A where:
    - A[K] in 1..N means increase(A[K])
    - A[K] == N+1 means max counter

    Return the final values of all counters.

Examples:
    Example 1:
        Input:  N = 5, A = [3, 4, 4, 6, 1, 4, 4]
        Output: [3, 2, 2, 4, 2]

Constraints:
    - 1 <= N, M <= 100,000
    - 1 <= A[i] <= N + 1

Hint (read only if stuck):
    Naive approach (reset all on max counter) is O(N*M).
    Use lazy propagation: track a "floor" value (last max counter value).
    On increment, first ensure counter >= floor, then increment.
    At the end, apply the floor to all counters.
"""


def solution(N: int, A: list[int]) -> list[int]:
    # TODO: implement your solution here
    pass
