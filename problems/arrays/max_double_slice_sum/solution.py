"""
Problem: Max Double Slice Sum
Difficulty: Hard
Source: Codility Lesson 9
Tags: arrays, dynamic-programming, kadane

Problem Statement:
    A triplet (X, Y, Z) where 0 <= X < Y < Z <= N-1 defines a "double slice"
    consisting of elements A[X+1..Y-1] and A[Y+1..Z-1].

    The sum of a double slice is:
        sum(A[X+1..Y-1]) + sum(A[Y+1..Z-1])

    Find the maximum sum of any double slice.

    Note: both slices can be empty (e.g., if Y = X+1 or Z = Y+1), contributing 0.

Examples:
    Example 1:
        Input:  A = [3, 2, 6, -1, 4, 5, -1, 2]
        Output: 17
        Explanation: (0, 3, 6) gives sum = (2+6) + (4+5) = 17.

Constraints:
    - 3 <= N <= 100,000
    - -10,000 <= A[i] <= 10,000

Hint (read only if stuck):
    Compute two arrays:
    - max_left[i]: max sum of subarray ending at i, starting from the left (floor at 0)
    - max_right[i]: max sum of subarray starting at i, going right (floor at 0)
    Answer = max(max_left[i-1] + max_right[i+1]) for i in 1..N-2.
    Floor at 0 because the slices can be empty.
"""


def solution(A: list[int]) -> int:
    # TODO: implement your solution here
    pass
