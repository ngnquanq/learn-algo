"""
Problem: Passing Cars
Difficulty: Medium
Source: Codility Lesson 5
Tags: prefix-sums, counting

Problem Statement:
    A non-empty array A consisting of N integers is given. The consecutive
    elements of array A represent consecutive cars on a road. Each element is
    either 0 (car traveling east) or 1 (car traveling west).

    We say that a pair of cars (P, Q), where 0 <= P < Q < N, is passing when
    P is traveling east and Q is traveling west (A[P] = 0, A[Q] = 1).

    Return the number of pairs of passing cars. Return -1 if the number
    exceeds 1,000,000,000.

Examples:
    Example 1:
        Input:  A = [0, 1, 0, 1, 1]
        Output: 5

Constraints:
    - 1 <= N <= 100,000
    - each element of array A is either 0 or 1
    - return -1 if the count exceeds 1,000,000,000

Hint (read only if stuck):
    Count the suffix sum of 1s (westbound cars). For each 0 (eastbound car),
    add the number of remaining 1s to the total.
"""


def solution(A: list[int]) -> int:
    # Init backward array
    backward_arr = [0] * len(A)
    for i in range(len(A) - 2, -1, -1):
        backward_arr[i] = backward_arr[i + 1] + A[i + 1]
    
    # Calculate results
    result = sum([backward_arr[i] if A[i]==0 else 0 for i in range(0,len(A))])

    if result > 1000000000:
        return -1
    else:
        return result