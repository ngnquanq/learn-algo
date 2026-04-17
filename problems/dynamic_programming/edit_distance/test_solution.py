import pytest
from .solution import solution


class TestEditDistance:
    # -------------------------------------------------------
    # Basic / Example cases
    # -------------------------------------------------------
    def test_example_1(self):
        assert solution("horse", "ros") == 3

    def test_example_2(self):
        assert solution("intention", "execution") == 5

    # -------------------------------------------------------
    # Edge cases
    # -------------------------------------------------------
    def test_both_empty(self):
        assert solution("", "") == 0

    def test_one_empty(self):
        assert solution("abc", "") == 3

    def test_other_empty(self):
        assert solution("", "abc") == 3

    def test_same_string(self):
        assert solution("abc", "abc") == 0

    def test_single_chars(self):
        assert solution("a", "b") == 1

    def test_swap(self):
        assert solution("ab", "ba") == 2

    # -------------------------------------------------------
    # Performance cases (large inputs should finish in time)
    # -------------------------------------------------------
    def test_large_input(self):
        word1 = "a" * 500
        word2 = "b" * 500
        assert solution(word1, word2) == 500
