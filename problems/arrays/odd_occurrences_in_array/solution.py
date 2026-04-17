"""
Problem: Odd Occurrences in Array
Difficulty: Medium
Source: Codility Lesson 2 / LeetCode #136
Tags: arrays, bit-manipulation, xor

Problem Statement:
    A non-empty array A consisting of N integers is given. The array contains
    an odd number of elements, and each element of the array can be paired with
    another element that has the same value, except for one element that is left
    unpaired.

    Find the value of the unpaired element.

Examples:
    Example 1:
        Input:  A = [9, 3, 9, 3, 9, 7, 9]
        Output: 7

    Example 2:
        Input:  A = [1, 1, 2]
        Output: 2

Constraints:
    - N is an odd integer within the range [1 .. 1,000,000]
    - each element of array A is an integer within the range [1 .. 1,000,000,000]
    - all but one of the values in A occur an even number of times

Hint (read only if stuck):
    XOR of a number with itself is 0. XOR all elements together; pairs cancel
    out and the unpaired element remains.
"""


def solution(A: list[int]) -> int:
    # TODO: implement your solution here
    pass
