class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
Problem: Binary Tree Level Order Traversal
Difficulty: Medium
Source: LeetCode #102
Tags: trees, bfs

Problem Statement:
    Given the root of a binary tree, return the level order traversal
    of its nodes' values (i.e., from left to right, level by level).

Examples:
    Example 1:
        Input:  root = [3, 9, 20, None, None, 15, 7]
        Output: [[3], [9, 20], [15, 7]]

    Example 2:
        Input:  root = [1]
        Output: [[1]]

    Example 3:
        Input:  root = []
        Output: []

Constraints:
    - 0 <= number of nodes <= 2,000
    - -1,000 <= Node.val <= 1,000

Hint (read only if stuck):
    Use BFS with a queue. Process all nodes at the current level
    before moving to the next level by tracking the queue size.
"""


def solution(root: TreeNode | None) -> list[list[int]]:
    # TODO: implement your solution here
    pass
