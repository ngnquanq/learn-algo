"""
Problem: Gas Station
Difficulty: Medium
Source: LeetCode #134
Tags: greedy, arrays

Problem Statement:
    There are N gas stations along a circular route. Station i has
    gas[i] units of fuel. The cost to travel from station i to
    station i+1 is cost[i].

    Starting with an empty tank at some station, determine if you
    can travel around the circuit once. Return the starting station
    index, or -1 if impossible.

    If a solution exists, it is guaranteed to be unique.

Examples:
    Example 1:
        Input:  gas = [1,2,3,4,5], cost = [3,4,5,1,2]
        Output: 3

    Example 2:
        Input:  gas = [2,3,4], cost = [3,4,3]
        Output: -1

Constraints:
    - 1 <= N <= 100,000
    - 0 <= gas[i], cost[i] <= 10,000

Hint (read only if stuck):
    If total gas >= total cost, a solution exists.
    Track current tank: when it goes negative, reset the start
    to the next station and reset the tank.
"""


def solution(gas: list[int], cost: list[int]) -> int:
    # TODO: implement your solution here
    pass
