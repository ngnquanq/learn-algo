class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
Problem: Lowest Common Ancestor of a Binary Tree
Difficulty: Medium
Source: LeetCode #236
Tags: trees, dfs, recursion

Problem Statement:
    Given a binary tree, find the lowest common ancestor (LCA) of two
    given nodes p and q. The LCA is the lowest node that has both p
    and q as descendants (a node can be a descendant of itself).

    All node values are unique. Both p and q exist in the tree.

Examples:
    Example 1:
        Input:  root = [3,5,1,6,2,0,8,None,None,7,4], p = 5, q = 1
        Output: 3

    Example 2:
        Input:  root = [3,5,1,6,2,0,8,None,None,7,4], p = 5, q = 4
        Output: 5

Constraints:
    - 2 <= number of nodes <= 10,000
    - All values are unique
    - p != q, both exist in the tree

Hint (read only if stuck):
    Recursively search left and right subtrees. If both return non-None,
    the current node is the LCA. If only one returns non-None, that
    result is the LCA.
"""


def solution(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    # TODO: implement your solution here
    pass
