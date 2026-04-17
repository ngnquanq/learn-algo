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



class TestBinaryTreeLevelOrderTraversal:
    # -------------------------------------------------------
    # Basic / Example cases
    # -------------------------------------------------------
    def test_example_1(self):
        root = build_tree([3, 9, 20, None, None, 15, 7])
        assert solution(root) == [[3], [9, 20], [15, 7]]

    def test_example_2(self):
        root = build_tree([1])
        assert solution(root) == [[1]]

    # -------------------------------------------------------
    # Edge cases
    # -------------------------------------------------------
    def test_empty(self):
        assert solution(None) == []

    def test_left_skewed(self):
        root = build_tree([1, 2, None, 3])
        assert solution(root) == [[1], [2], [3]]

    def test_right_skewed(self):
        root = build_tree([1, None, 2, None, 3])
        assert solution(root) == [[1], [2], [3]]

    # -------------------------------------------------------
    # Performance cases (large inputs should finish in time)
    # -------------------------------------------------------
    def test_large_tree(self):
        values = list(range(1, 2001))
        root = build_tree(values)
        result = solution(root)
        assert result[0] == [1]
        assert len(result) >= 10
