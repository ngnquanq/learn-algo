import pytest
from .solution import solution


class TestGenomicRangeQuery:
    # -------------------------------------------------------
    # Basic / Example cases
    # -------------------------------------------------------
    def test_example_1(self):
        assert solution("CAGCCTA", [2, 5, 0], [4, 5, 6]) == [2, 4, 1]

    def test_single_char_a(self):
        assert solution("A", [0], [0]) == [1]

    # -------------------------------------------------------
    # Edge cases
    # -------------------------------------------------------
    def test_all_same_a(self):
        assert solution("AAAA", [0, 1], [3, 2]) == [1, 1]

    def test_single_char_t(self):
        assert solution("T", [0], [0]) == [4]

    def test_single_position_query(self):
        """P[i] == Q[i] for each nucleotide type."""
        assert solution("ACGT", [0], [0]) == [1]
        assert solution("ACGT", [1], [1]) == [2]
        assert solution("ACGT", [2], [2]) == [3]
        assert solution("ACGT", [3], [3]) == [4]

    def test_all_same_g(self):
        assert solution("GGG", [0, 1], [2, 2]) == [3, 3]

    # -------------------------------------------------------
    # Performance cases (large inputs should finish in time)
    # -------------------------------------------------------
    def test_large_input(self):
        S = "ACGT" * 25_000  # length 100,000
        P = list(range(0, 50_000))
        Q = list(range(50_000, 100_000))
        result = solution(S, P, Q)
        assert len(result) == 50_000
        # Every range spanning at least 4 chars will contain an A
        assert all(r == 1 for r in result)
