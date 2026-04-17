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



def find_node(root, val):
    """Find a node with given value in the tree."""
    if root is None:
        return None
    if root.val == val:
        return root
    return find_node(root.left, val) or find_node(root.right, val)


class TestLowestCommonAncestor:
    # -------------------------------------------------------
    # Basic / Example cases
    # -------------------------------------------------------
    def test_example_1(self):
        root = build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
        p = find_node(root, 5)
        q = find_node(root, 1)
        assert solution(root, p, q).val == 3

    def test_example_2(self):
        root = build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
        p = find_node(root, 5)
        q = find_node(root, 4)
        assert solution(root, p, q).val == 5

    # -------------------------------------------------------
    # Edge cases
    # -------------------------------------------------------
    def test_root_is_lca(self):
        root = build_tree([1, 2, 3])
        p = find_node(root, 2)
        q = find_node(root, 3)
        assert solution(root, p, q).val == 1

    def test_parent_child(self):
        root = build_tree([1, 2])
        p = find_node(root, 1)
        q = find_node(root, 2)
        assert solution(root, p, q).val == 1

    # -------------------------------------------------------
    # Performance cases (large inputs should finish in time)
    # -------------------------------------------------------
    def test_large_tree(self):
        values = list(range(1, 10001))
        root = build_tree(values)
        p = find_node(root, 9999)
        q = find_node(root, 10000)
        result = solution(root, p, q)
        assert result is not None
