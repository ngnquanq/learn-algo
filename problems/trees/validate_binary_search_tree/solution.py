class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
Problem: Validate Binary Search Tree
Difficulty: Medium
Source: LeetCode #98
Tags: trees, dfs, bst

Problem Statement:
    Given the root of a binary tree, determine if it is a valid
    binary search tree (BST).

    A valid BST is defined as:
    - The left subtree of a node contains only nodes with keys
      strictly less than the node's key.
    - The right subtree contains only nodes with keys strictly
      greater than the node's key.
    - Both subtrees must also be valid BSTs.

Examples:
    Example 1:
        Input:  root = [2, 1, 3]
        Output: True

    Example 2:
        Input:  root = [5, 1, 4, None, None, 3, 6]
        Output: False
        Explanation: Root is 5 but right child 4 is less than 5.

Constraints:
    - 1 <= number of nodes <= 10,000
    - -2^31 <= Node.val <= 2^31 - 1

Hint (read only if stuck):
    Recursively validate with min/max bounds. Left child must be
    in range (min_val, node.val) and right child in (node.val, max_val).
    Or: do an in-order traversal and check it's strictly increasing.
"""


def solution(root: TreeNode | None) -> bool:
    # TODO: implement your solution here
    pass
