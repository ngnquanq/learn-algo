"""
Problem: Max Profit
Difficulty: Medium
Source: Codility Lesson 9 / LeetCode #121
Tags: arrays, greedy

Problem Statement:
    Given an array A of N integers representing daily stock prices,
    find the maximum profit from a single buy-sell transaction.
    You must buy before you sell.

    Return 0 if no profit is possible.

Examples:
    Example 1:
        Input:  A = [23171, 21011, 21123, 21366, 21013, 21367]
        Output: 356
        Explanation: Buy at 21011, sell at 21367.

    Example 2:
        Input:  A = [7, 1, 5, 3, 6, 4]
        Output: 5
        Explanation: Buy at 1, sell at 6.

Constraints:
    - 0 <= N <= 400,000
    - 0 <= A[i] <= 200,000

Hint (read only if stuck):
    Track the minimum price seen so far as you scan left to right.
    At each position, the best profit is current price minus that minimum.
"""


def solution(A: list[int]) -> int:
    # Initiate the values
    lowest_price = float('inf')
    max_profit = 0

    # Check if the array is empty
    if not A:
        return 0
    
    # Check if the array has only one element
    if len(A) == 1:
        return 0

    # Iterate through the array 
    for price in A:
        current_price = price 
        if lowest_price >= current_price:
            lowest_price = current_price
        else:
            max_profit = max(max_profit, current_price - lowest_price)
    
    return max_profit
