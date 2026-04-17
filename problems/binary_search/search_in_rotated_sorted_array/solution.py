"""
Problem: Search in Rotated Sorted Array
Difficulty: Medium
Source: LeetCode #33
Tags: binary-search, arrays

Problem Statement:
    An integer array nums sorted in ascending order was rotated at some
    pivot. Given the rotated array and a target value, return the index
    of target, or -1 if not found.

    You must write an algorithm with O(log n) runtime complexity.
    All values are unique.

Examples:
    Example 1:
        Input:  nums = [4,5,6,7,0,1,2], target = 0
        Output: 4

    Example 2:
        Input:  nums = [4,5,6,7,0,1,2], target = 3
        Output: -1

Constraints:
    - 1 <= N <= 5,000
    - All values are unique
    - Must be O(log n)

Hint (read only if stuck):
    At each step of binary search, one half is always sorted.
    Determine which half is sorted, then check if the target
    falls within that sorted half.
"""


def solution(nums: list[int], target: int) -> int:
    # TODO: implement your solution here
    pass
