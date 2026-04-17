"""
Problem: Redundant Connection
Difficulty: Medium
Source: LeetCode #684
Tags: graphs, union-find

Problem Statement:
    A tree is a connected graph with no cycles. Given a graph that
    started as a tree with N nodes and had one additional edge added,
    find that redundant edge. Return the last such edge in the input.

Examples:
    Example 1:
        Input:  edges = [[1,2],[1,3],[2,3]]
        Output: [2,3]

    Example 2:
        Input:  edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
        Output: [1,4]

Constraints:
    - 3 <= N <= 1,000
    - edges[i] = [u, v], 1-indexed

Hint (read only if stuck):
    Use Union-Find (Disjoint Set Union). Process edges in order.
    The first edge where both endpoints are already in the same set
    is the redundant edge (the last one if processed in order).
"""


def solution(edges: list[list[int]]) -> list[int]:
    # TODO: implement your solution here
    pass
