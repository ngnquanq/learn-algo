"""
Problem: Course Schedule
Difficulty: Medium
Source: LeetCode #207
Tags: graphs, topological-sort, dfs

Problem Statement:
    There are numCourses courses labeled 0 to numCourses-1.
    prerequisites[i] = [a, b] means you must take course b before a.
    Return True if you can finish all courses (no cycle), False otherwise.

Examples:
    Example 1:
        Input:  numCourses = 2, prerequisites = [[1, 0]]
        Output: True

    Example 2:
        Input:  numCourses = 2, prerequisites = [[1, 0], [0, 1]]
        Output: False

Constraints:
    - 1 <= numCourses <= 2,000
    - 0 <= |prerequisites| <= 5,000
    - prerequisites[i].length == 2

Hint (read only if stuck):
    This is cycle detection in a directed graph.
    Use Kahn's algorithm (BFS with in-degree counting) or
    DFS with three states (unvisited, in-progress, visited).
"""


def solution(numCourses: int, prerequisites: list[list[int]]) -> bool:
    # TODO: implement your solution here
    pass
