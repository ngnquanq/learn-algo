import pytest
from .solution import solution


class TestFish:
    # -------------------------------------------------------
    # Basic / Example cases
    # -------------------------------------------------------
    def test_example_1(self):
        assert solution([4, 3, 2, 1, 5], [0, 1, 0, 0, 0]) == 2

    def test_all_downstream(self):
        assert solution([4, 3, 2, 1, 5], [1, 1, 1, 1, 1]) == 5

    # -------------------------------------------------------
    # Edge cases
    # -------------------------------------------------------
    def test_all_upstream(self):
        assert solution([1, 2, 3], [0, 0, 0]) == 3

    def test_single_fish(self):
        assert solution([10], [0]) == 1
        assert solution([10], [1]) == 1

    def test_alternating_downstream_eats(self):
        """Downstream fish are larger, eat all upstream."""
        assert solution([10, 1, 10, 1], [1, 0, 1, 0]) == 2

    def test_largest_downstream_first(self):
        assert solution([5, 4, 3, 2, 1], [1, 0, 0, 0, 0]) == 1

    def test_upstream_wins_all(self):
        assert solution([1, 2, 3, 4, 100], [1, 1, 1, 1, 0]) == 1

    # -------------------------------------------------------
    # Performance cases (large inputs should finish in time)
    # -------------------------------------------------------
    def test_large_input(self):
        n = 100_000
        A = list(range(1, n + 1))
        B = [1] * (n // 2) + [0] * (n // 2)
        result = solution(A, B)
        # The largest fish (in the upstream group) eats all downstream
        assert result == n // 2
