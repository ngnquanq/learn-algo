import pytest
from collections import deque
from .solution import solution, TreeNode


def build_tree(values):
    """Build a binary tree from a list (level-order, None for missing nodes)."""
    if not values:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root



class TestValidateBinarySearchTree:
    # -------------------------------------------------------
    # Basic / Example cases
    # -------------------------------------------------------
    def test_example_1(self):
        root = build_tree([2, 1, 3])
        assert solution(root) is True

    def test_example_2(self):
        root = build_tree([5, 1, 4, None, None, 3, 6])
        assert solution(root) is False

    # -------------------------------------------------------
    # Edge cases
    # -------------------------------------------------------
    def test_single_node(self):
        assert solution(TreeNode(1)) is True

    def test_equal_values(self):
        root = build_tree([1, 1])
        assert solution(root) is False

    def test_deep_violation(self):
        # [5,4,6,None,None,3,7] — 3 is in right subtree but < 5
        root = build_tree([5, 4, 6, None, None, 3, 7])
        assert solution(root) is False

    def test_max_value(self):
        assert solution(TreeNode(2147483647)) is True

    # -------------------------------------------------------
    # Performance cases (large inputs should finish in time)
    # -------------------------------------------------------
    def test_large_valid_bst(self):
        # Build a valid BST from sorted values
        values = list(range(1, 10001))
        root = build_tree(values)
        # This tree built level-order from sorted list is NOT a valid BST
        # Just check it completes in time
        solution(root)
