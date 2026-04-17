"""
Problem: Clone Graph
Difficulty: Medium
Source: LeetCode #133
Tags: graphs, bfs, dfs, hash-map

Problem Statement:
    Given a reference of a node in a connected undirected graph, return
    a deep copy (clone) of the graph. Each node has a value and a list
    of its neighbors.

Examples:
    Example 1:
        Input:  adjList = [[2,4],[1,3],[2,4],[1,3]]
        Output: deep copy of the graph

Constraints:
    - 0 <= number of nodes <= 100
    - 1 <= Node.val <= number of nodes
    - No self-loops, no repeated edges
    - The graph is connected

Hint (read only if stuck):
    BFS or DFS with a hash map {original_node -> cloned_node}.
    Clone each node, then wire up the neighbors using the map.
"""


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def solution(node: Node | None) -> Node | None:
    # TODO: implement your solution here
    pass
