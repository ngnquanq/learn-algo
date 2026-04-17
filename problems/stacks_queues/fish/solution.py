"""
Problem: Fish
Difficulty: Medium
Source: Codility Lesson 7
Tags: stacks, simulation

Problem Statement:
    You are given two non-empty arrays A and B consisting of N integers.
    Arrays A and B represent N voracious fish in a river, ordered along it.

    The fish are numbered from 0 to N-1. A[i] represents the size of fish i,
    and B[i] represents its direction: 0 = upstream, 1 = downstream.

    If two fish are moving in opposite directions and there are no living fish
    between them, they will meet. When they meet, the larger fish eats the
    smaller one. More precisely, fish P eats fish Q when P < Q, B[P] = 1,
    B[Q] = 0, and A[P] > A[Q]. After fish Q is eaten, fish P continues
    downstream.

    Given the size and direction of each fish, calculate the number of fish
    that will stay alive.

Examples:
    Example 1:
        Input:  A = [4, 3, 2, 1, 5], B = [0, 1, 0, 0, 0]
        Output: 2

Constraints:
    - 1 <= N <= 100,000
    - each element of array A is an integer within the range [0 .. 1,000,000,000]
    - all elements of A are distinct
    - each element of array B is either 0 or 1

Hint (read only if stuck):
    Use a stack to hold downstream-going fish. When an upstream fish appears,
    it fights the fish on top of the stack until it either dies or wins
    against all downstream fish.
"""


def solution(A: list[int], B: list[int]) -> int:
    # TODO: implement your solution here
    pass
