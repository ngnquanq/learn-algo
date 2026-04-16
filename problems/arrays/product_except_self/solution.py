"""
Problem: Product of Array Except Self
Difficulty: Medium
Source: LeetCode #238
Tags: arrays, prefix-sum, prefix-product

Problem Statement:
    Given an integer array `nums`, return an array `answer` such that
    `answer[i]` is equal to the product of all elements of `nums` EXCEPT
    `nums[i]`.

    The product of any prefix or suffix of `nums` is guaranteed to fit in a
    32-bit integer.

    ⚠️  You must write an algorithm that runs in O(n) time complexity.
    ⚠️  You must NOT use division.

Examples:
    Example 1:
        Input:  nums = [1, 2, 3, 4]
        Output: [24, 12, 8, 6]

        Explanation:
            answer[0] = 2 * 3 * 4 = 24
            answer[1] = 1 * 3 * 4 = 12
            answer[2] = 1 * 2 * 4 = 8
            answer[3] = 1 * 2 * 3 = 6

    Example 2:
        Input:  nums = [-1, 1, 0, -3, 3]
        Output: [0, 0, 9, 0, 0]

Constraints:
    - 2 <= len(nums) <= 10^5
    - -30 <= nums[i] <= 30
    - The product of any prefix or suffix fits in a 32-bit integer
    - You may not use the division operator (/)
    - Must solve in O(n) time

Hint (read only if stuck):
    Think about two separate passes over the array:
    one going LEFT → RIGHT, one going RIGHT → LEFT.
    What useful value can you accumulate in each pass?
"""


def solution(nums: list[int]) -> list[int]:
    # TODO: implement your solution here

    # Prefix product from left to right
    prefix_product = [1] * len(nums)
    for i in range(1, len(nums)):
        prefix_product[i] = prefix_product[i - 1] * nums[i - 1]

    # Suffix product from right to left
    suffix_product = [1] * len(nums)
    for i in range(len(nums) - 2, -1, -1):
        suffix_product[i] = suffix_product[i + 1] * nums[i + 1]

    results = [prefix_product[i] * suffix_product[i] for i in range(len(nums))]

    return results
