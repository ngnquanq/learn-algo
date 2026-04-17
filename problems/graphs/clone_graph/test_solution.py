import pytest
from .solution import solution, Node


def build_graph(adj_list):
    """Build graph from adjacency list (1-indexed)."""
    if not adj_list:
        return None
    nodes = {i + 1: Node(i + 1) for i in range(len(adj_list))}
    for i, neighbors in enumerate(adj_list):
        nodes[i + 1].neighbors = [nodes[n] for n in neighbors]
    return nodes[1]


def graph_to_adj(node):
    """Convert graph back to adjacency list for comparison."""
    if not node:
        return []
    visited = {}
    queue = [node]
    visited[node.val] = node
    while queue:
        curr = queue.pop(0)
        for n in curr.neighbors:
            if n.val not in visited:
                visited[n.val] = n
                queue.append(n)
    result = []
    for i in range(1, len(visited) + 1):
        result.append(sorted([n.val for n in visited[i].neighbors]))
    return result


class TestCloneGraph:
    # -------------------------------------------------------
    # Basic / Example cases
    # -------------------------------------------------------
    def test_example_1(self):
        original = build_graph([[2, 4], [1, 3], [2, 4], [1, 3]])
        cloned = solution(original)
        assert cloned is not original
        assert graph_to_adj(cloned) == [[2, 4], [1, 3], [2, 4], [1, 3]]

    def test_single_node(self):
        original = Node(1)
        cloned = solution(original)
        assert cloned is not original
        assert cloned.val == 1
        assert cloned.neighbors == []

    # -------------------------------------------------------
    # Edge cases
    # -------------------------------------------------------
    def test_none(self):
        assert solution(None) is None

    def test_two_nodes(self):
        original = build_graph([[2], [1]])
        cloned = solution(original)
        assert cloned is not original
        assert cloned.val == 1
        assert len(cloned.neighbors) == 1
        assert cloned.neighbors[0].val == 2
        assert cloned.neighbors[0] is not original.neighbors[0]
