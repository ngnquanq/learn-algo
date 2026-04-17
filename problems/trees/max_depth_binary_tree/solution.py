class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
Problem: Maximum Depth of Binary Tree
Difficulty: Medium
Source: LeetCode #104
Tags: trees, dfs, recursion

Problem Statement:
    Given the root of a binary tree, return its maximum depth.
    The maximum depth is the number of nodes along the longest path
    from the root node down to the farthest leaf node.

Examples:
    Example 1:
        Input:  root = [3, 9, 20, None, None, 15, 7]
        Output: 3

    Example 2:
        Input:  root = [1, None, 2]
        Output: 2

Constraints:
    - 0 <= number of nodes <= 10,000
    - -100 <= Node.val <= 100

Hint (read only if stuck):
    Recursive: return 1 + max(depth(left), depth(right)).
    Base case: None -> 0.
"""


def solution(root: TreeNode | None) -> int:
    # TODO: implement your solution here
    pass
