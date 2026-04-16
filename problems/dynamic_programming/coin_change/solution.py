"""
Problem: Coin Change
Difficulty: Medium
Source: LeetCode #322
Tags: dynamic programming, bottom-up DP, BFS

Real-World Context:
    You are building the change-dispensing logic for an ATM or a
    self-checkout machine. Given the denominations available in the
    machine and a target amount a customer needs as change, compute
    the FEWEST number of coins/bills needed to make up that amount.
    If it's impossible (e.g. no coin fits), return -1.

Problem Statement:
    You are given an integer array `coins` representing coin denominations
    and an integer `amount` representing a total amount of money.

    Return the fewest number of coins needed to make up `amount`.
    If that amount cannot be made up by any combination of the coins,
    return -1.

    You may assume you have an infinite supply of each denomination.

Examples:
    Example 1:
        Input:  coins = [1, 5, 10, 25], amount = 36
        Output: 3
        Explanation: 25 + 10 + 1 = 36 → 3 coins

    Example 2:
        Input:  coins = [2], amount = 3
        Output: -1
        Explanation: cannot make 3 with only 2s

    Example 3:
        Input:  coins = [1, 2, 5], amount = 11
        Output: 3
        Explanation: 5 + 5 + 1 = 11 → 3 coins

    Example 4:
        Input:  coins = [1, 2, 5], amount = 0
        Output: 0
        Explanation: 0 coins needed for amount 0

Constraints:
    - 1 <= len(coins) <= 12
    - 1 <= coins[i] <= 2^31 - 1
    - 0 <= amount <= 10^4
    - All coin values are distinct

Hint (read only if stuck):
    Define dp[i] = minimum coins to make amount i.
    Base case: dp[0] = 0.
    Transition: for each amount i, try every coin c.
        If i >= c, then dp[i] = min(dp[i], dp[i - c] + 1)
    Build the table bottom-up from 0 → amount.
"""


def solution(coins: list[int], amount: int) -> int:
    # TODO: implement your solution here
    pass
