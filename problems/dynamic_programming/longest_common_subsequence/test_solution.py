import pytest
from .solution import solution


class TestLongestCommonSubsequence:
    # -------------------------------------------------------
    # Basic / Example cases
    # -------------------------------------------------------
    def test_example_1(self):
        assert solution("abcde", "ace") == 3

    def test_example_2(self):
        assert solution("abc", "abc") == 3

    def test_example_3(self):
        assert solution("abc", "def") == 0

    # -------------------------------------------------------
    # Edge cases
    # -------------------------------------------------------
    def test_single_match(self):
        assert solution("a", "a") == 1

    def test_single_no_match(self):
        assert solution("a", "b") == 0

    def test_palindromic(self):
        assert solution("abcba", "abcbcba") == 5

    # -------------------------------------------------------
    # Performance cases (large inputs should finish in time)
    # -------------------------------------------------------
    def test_large_input(self):
        text1 = "a" * 1000
        text2 = "a" * 1000
        assert solution(text1, text2) == 1000
