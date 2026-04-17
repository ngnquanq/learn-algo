"""
Problem: Network Delay Time
Difficulty: Medium
Source: LeetCode #743
Tags: graphs, dijkstra, shortest-path

Problem Statement:
    You are given a network of n nodes labeled 1 to n. You are given
    times, a list of travel times as directed edges times[i] = (u, v, w)
    where u is source, v is target, and w is the time.

    Send a signal from node k. Return the minimum time for all nodes
    to receive the signal, or -1 if not all nodes can be reached.

Examples:
    Example 1:
        Input:  times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
        Output: 2

    Example 2:
        Input:  times = [[1,2,1]], n = 2, k = 2
        Output: -1

Constraints:
    - 1 <= n <= 100
    - 1 <= |times| <= 6,000
    - 1 <= u, v <= n
    - 0 <= w <= 100

Hint (read only if stuck):
    Use Dijkstra's algorithm with a min-heap.
    Return the maximum shortest distance to any node, or -1 if any
    node is unreachable.
"""


def solution(times: list[list[int]], n: int, k: int) -> int:
    # TODO: implement your solution here
    pass
