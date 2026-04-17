"""
Problem: Number of Disc Intersections
Difficulty: Hard
Source: Codility Lesson 6
Tags: sorting, sweep-line

Problem Statement:
    We draw N discs on a plane. Disc i is centered at (i, 0) with
    radius A[i]. Two discs intersect if they share at least one common
    point (including tangent).

    Count the number of pairs of intersecting discs.
    Return -1 if the number exceeds 10,000,000.

Examples:
    Example 1:
        Input:  A = [1, 5, 2, 1, 4, 0]
        Output: 11

Constraints:
    - 0 <= N <= 100,000
    - 0 <= A[i] <= 2,147,483,647

Hint (read only if stuck):
    For each disc i, compute start = i - A[i] and end = i + A[i].
    Sort the start points. For each disc, use binary search or sweep
    line to count how many other discs have already started.
"""


def solution(A: list[int]) -> int:
    # TODO: implement your solution here
    pass
