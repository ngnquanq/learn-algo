"""
Problem: Koko Eating Bananas
Difficulty: Medium
Source: LeetCode #875
Tags: binary-search

Problem Statement:
    Koko has N piles of bananas. Pile i has piles[i] bananas.
    She eats at speed K bananas per hour. Each hour she picks one pile
    and eats K bananas from it (or finishes the pile if < K remain).

    Find the minimum integer K such that she can finish all bananas
    within h hours.

Examples:
    Example 1:
        Input:  piles = [3,6,7,11], h = 8
        Output: 4

    Example 2:
        Input:  piles = [30,11,23,4,20], h = 5
        Output: 30

Constraints:
    - 1 <= N <= 10,000
    - 1 <= piles[i] <= 10^9
    - N <= h <= 10^9

Hint (read only if stuck):
    Binary search on K from 1 to max(piles).
    For each K, compute total hours = sum(ceil(pile / K) for each pile).
    If total hours <= h, K is feasible — try smaller. Otherwise try larger.
"""


def solution(piles: list[int], h: int) -> int:
    # TODO: implement your solution here
    pass
