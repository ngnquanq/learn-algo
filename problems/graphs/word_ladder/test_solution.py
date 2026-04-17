import pytest
from .solution import solution


class TestWordLadder:
    # -------------------------------------------------------
    # Basic / Example cases
    # -------------------------------------------------------
    def test_example_1(self):
        assert solution("hit", "cog",
                         ["hot", "dot", "dog", "lot", "log", "cog"]) == 5

    def test_example_2(self):
        assert solution("hit", "cog",
                         ["hot", "dot", "dog", "lot", "log"]) == 0

    # -------------------------------------------------------
    # Edge cases
    # -------------------------------------------------------
    def test_end_not_in_list(self):
        assert solution("a", "c", ["b"]) == 0

    def test_one_step(self):
        assert solution("a", "b", ["b"]) == 2

    def test_no_path(self):
        assert solution("abc", "xyz", ["abd", "xyd"]) == 0

    def test_single_char_words(self):
        assert solution("a", "c", ["a", "b", "c"]) == 2

    # -------------------------------------------------------
    # Performance cases (large inputs should finish in time)
    # -------------------------------------------------------
    def test_large_input(self):
        # Build a chain: aaa -> baa -> bba -> bbb -> ...
        word_list = []
        base = "a" * 5
        for i in range(5):
            for c in "bcdefghij":
                w = list(base)
                for j in range(i):
                    w[j] = chr(ord("a") + j + 1)
                w[i] = c
                word_list.append("".join(w))
        result = solution("aaaaa", "aaaaa", word_list)
        assert isinstance(result, int)
